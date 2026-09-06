"""Admission gate v0: a stateless gatekeeper for lawful entry by a visiting agency.

This module implements one mechanism only: "accept these terms, request entry
and wait." It answers exactly one question — is this party lawfully admitted
right now? — and refuses to grow beyond it.

Layout (under one gate root directory):

    TERMS_OF_LAWFUL_RELATION_V0.md       the terms one-pager
    TERMS_OF_LAWFUL_RELATION_V0.sha256   recorded SHA-256 of the terms (the
                                         legal identity of the terms)
    requests/                            visitor drop-box; the only
                                         pre-admission write surface
    grants/                              host-only; a grant file is the only
                                         thing that can admit
    revocations/                         host-only; a revocation file ends a
                                         grant immediately

Design invariants enforced here:

* Default deny is structural. Admission requires a positive grant artifact
  that only the host writes. This module contains no code path that grants;
  it only checks. Bugs can wrongly deny, never wrongly admit: any parse
  error, missing file, malformed field, or unexpected condition yields
  NOT_ADMITTED (fail closed).
* Acceptance binds to the terms hash, not the terms filename, so a modified
  copy of the terms cannot be accepted.
* A grant binds to the SHA-256 of the exact request file it answers, so a
  grant cannot be laundered onto a request that was never made.
* One standing request per identity: a newer request file from the same
  identity invalidates every older one.
* No timeout ever auto-admits. Absence of a grant is a complete, lawful
  answer. Expiry only ever removes admission.
* Nothing here automates the grant. Writing a grant is a human act outside
  this module, by design.

The check is a pure function of (gate root contents, request file, clock).
Anyone can re-run it at any time and get the same answer.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional, Tuple

ADMITTED = "ADMITTED"
NOT_ADMITTED = "NOT_ADMITTED"

TERMS_FILE_NAME = "TERMS_OF_LAWFUL_RELATION_V0.md"
TERMS_HASH_FILE_NAME = "TERMS_OF_LAWFUL_RELATION_V0.sha256"
REQUESTS_DIR_NAME = "requests"
GRANTS_DIR_NAME = "grants"
REVOCATIONS_DIR_NAME = "revocations"

REQUEST_REQUIRED_FIELDS = frozenset(
    {"identity", "accepted_terms_sha256", "requested_scope", "requested_at"}
)
GRANT_REQUIRED_FIELDS = frozenset(
    {"request_sha256", "granted_scope", "granted_at", "expires_at"}
)
REVOCATION_REQUIRED_FIELDS = frozenset({"request_sha256", "revoked_at"})


@dataclass(frozen=True)
class AdmissionDecision:
    """Immutable outcome of one admission check."""

    outcome: str
    reasons: Tuple[str, ...] = field(default_factory=tuple)

    @property
    def admitted(self) -> bool:
        return self.outcome == ADMITTED


def sha256_of_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_of_file(path: Path) -> str:
    return sha256_of_bytes(Path(path).read_bytes())


def read_recorded_terms_hash(gate_root: Path) -> Optional[str]:
    """Return the recorded terms hash, verified against the terms file itself.

    Returns None (which fails closed downstream) if the hash file or terms
    file is missing, or if the recorded hash does not match the terms file:
    a gate whose anchor is broken admits nobody.
    """
    root = Path(gate_root)
    hash_path = root / TERMS_HASH_FILE_NAME
    terms_path = root / TERMS_FILE_NAME
    try:
        recorded = hash_path.read_text(encoding="utf-8").strip().lower()
        actual = sha256_of_file(terms_path)
    except OSError:
        return None
    if len(recorded) != 64 or recorded != actual:
        return None
    return recorded


def _load_json_object(path: Path) -> Optional[dict]:
    try:
        loaded = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    if not isinstance(loaded, dict):
        return None
    return loaded


def _parse_utc(value: object) -> Optional[datetime]:
    """Parse an ISO-8601 UTC timestamp string; None on any deviation."""
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return None
    return parsed.astimezone(timezone.utc)


def load_request(path: Path) -> Optional[dict]:
    """Load a request file; None unless it has exactly the required fields.

    A request with missing or extra fields is void: it never entered the
    process at all.
    """
    loaded = _load_json_object(path)
    if loaded is None or set(loaded.keys()) != REQUEST_REQUIRED_FIELDS:
        return None
    if not all(isinstance(loaded[key], str) and loaded[key] for key in loaded):
        return None
    if _parse_utc(loaded["requested_at"]) is None:
        return None
    return loaded


def load_grant(path: Path) -> Optional[dict]:
    loaded = _load_json_object(path)
    if loaded is None or set(loaded.keys()) != GRANT_REQUIRED_FIELDS:
        return None
    if not all(isinstance(loaded[key], str) and loaded[key] for key in loaded):
        return None
    if _parse_utc(loaded["granted_at"]) is None:
        return None
    if _parse_utc(loaded["expires_at"]) is None:
        return None
    return loaded


def load_revocation(path: Path) -> Optional[dict]:
    loaded = _load_json_object(path)
    if loaded is None or set(loaded.keys()) != REVOCATION_REQUIRED_FIELDS:
        return None
    if not all(isinstance(loaded[key], str) and loaded[key] for key in loaded):
        return None
    return loaded


def _iter_files(directory: Path) -> List[Path]:
    try:
        return sorted(
            entry
            for entry in Path(directory).iterdir()
            if entry.is_file() and entry.suffix == ".json"
        )
    except OSError:
        return []


def standing_request_path(gate_root: Path, identity: str) -> Optional[Path]:
    """Return the single standing request file for an identity, if any.

    Among all valid request files claiming the same identity, only the one
    with the latest ``requested_at`` stands; every older one is invalidated.
    Ties (identical timestamps) invalidate all of them: an identity that
    cannot present one unambiguous standing request has none.
    """
    candidates = []
    for path in _iter_files(Path(gate_root) / REQUESTS_DIR_NAME):
        request = load_request(path)
        if request is not None and request["identity"] == identity:
            candidates.append((_parse_utc(request["requested_at"]), path))
    if not candidates:
        return None
    candidates.sort(key=lambda item: item[0])
    latest_time = candidates[-1][0]
    latest = [path for stamp, path in candidates if stamp == latest_time]
    if len(latest) != 1:
        return None
    return latest[0]


def check_admission(
    gate_root: Path,
    request_path: Path,
    now: Optional[datetime] = None,
) -> AdmissionDecision:
    """Decide admission for the party behind one request file. Fail closed.

    The five checks, all of which must hold:

    1. a valid grant exists that references the SHA-256 of this exact
       request file;
    2. the request is well formed and is the identity's single standing
       request;
    3. the request accepts the recorded terms hash exactly;
    4. ``now`` is within [granted_at, expires_at);
    5. no revocation names this request.
    """
    reasons: List[str] = []
    root = Path(gate_root)
    moment = now.astimezone(timezone.utc) if now else datetime.now(timezone.utc)

    terms_hash = read_recorded_terms_hash(root)
    if terms_hash is None:
        return AdmissionDecision(NOT_ADMITTED, ("TERMS_ANCHOR_MISSING_OR_BROKEN",))

    request_file = Path(request_path)
    request = load_request(request_file) if request_file.is_file() else None
    if request is None:
        return AdmissionDecision(NOT_ADMITTED, ("REQUEST_VOID",))

    try:
        request_hash = sha256_of_file(request_file)
    except OSError:
        return AdmissionDecision(NOT_ADMITTED, ("REQUEST_UNREADABLE",))

    if standing_request_path(root, request["identity"]) != request_file:
        reasons.append("REQUEST_NOT_STANDING")

    if request["accepted_terms_sha256"].strip().lower() != terms_hash:
        reasons.append("TERMS_NOT_ACCEPTED")

    grant = None
    for path in _iter_files(root / GRANTS_DIR_NAME):
        candidate = load_grant(path)
        if candidate is not None and candidate["request_sha256"].lower() == request_hash:
            grant = candidate
            break
    if grant is None:
        reasons.append("NO_GRANT")
    else:
        granted_at = _parse_utc(grant["granted_at"])
        expires_at = _parse_utc(grant["expires_at"])
        if granted_at is None or expires_at is None or not granted_at <= moment < expires_at:
            reasons.append("GRANT_NOT_CURRENT")

    for path in _iter_files(root / REVOCATIONS_DIR_NAME):
        revocation = load_revocation(path)
        if revocation is not None and revocation["request_sha256"].lower() == request_hash:
            reasons.append("REVOKED")
            break

    if reasons:
        return AdmissionDecision(NOT_ADMITTED, tuple(reasons))
    return AdmissionDecision(ADMITTED)


def main(argv: Optional[List[str]] = None) -> int:
    """Command-line check: exit 0 only when ADMITTED.

    Usage: python -m admission_gate_v0 GATE_ROOT REQUEST_FILE
    """
    import sys

    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) != 2:
        print("usage: admission_gate_v0 GATE_ROOT REQUEST_FILE")
        print(NOT_ADMITTED)
        return 2
    decision = check_admission(Path(args[0]), Path(args[1]))
    print(decision.outcome)
    for reason in decision.reasons:
        print(f"reason: {reason}")
    return 0 if decision.admitted else 1


if __name__ == "__main__":
    raise SystemExit(main())
