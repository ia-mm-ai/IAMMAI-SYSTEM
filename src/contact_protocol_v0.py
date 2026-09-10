"""Contact protocol v0: six-phase lawful contact between asymmetric agencies.

This module operationalizes one locality tree (default: ``locality/``):

    00_presence/     Phase 0 — host presence dossier (host-only writes)
    01_terms/        the universal terms one-pager + recorded SHA-256
    02_vestibule/    Phase 1 — disposable relational field (generated, never stored)
    03_contact/      Phase 2 — visitor drop-box: contact-event artifacts
    04_review/       Phase 3 — host-only review records per case
    05_relations/    Phase 4 — one directory per accepted relation
    06_revocations/  host-only: revocation ends a relation immediately

Protocol invariants enforced here:

* Every phase transition is an artifact, and no artifact ever grants the
  next phase automatically. This module contains no code path that writes a
  dossier, an acceptance, or a relation; it only seals, renders, and checks.
* The dossier hash is the host's legal identity for contact purposes, the
  same way the terms hash is the terms' legal identity. A visitor's contact
  artifact must name both: naming the terms hash proves the terms were read
  and accepted; naming the dossier hash proves the host's reality was
  actually held (Phase 1) before relation was requested.
* The vestibule is disposable: it is generated on demand from the anchors
  and is never persisted. A failed or abandoned contact leaves no standing
  relation to clean up.
* A contact artifact is an answerable act: voluntary (could have been
  withheld), boundary-shaped (only a correctly formed artifact counts, and
  forming it correctly is itself proof of comprehension), and trail-leaving
  (it remains as evidence regardless of outcome; a malformed attempt is also
  evidence, of the opposite thing).
* Acceptance is host-only, hand-written, perishable, and revocable. It binds
  to the SHA-256 of the exact contact artifact it answers. Silence is a
  complete answer; nothing auto-advances; expiry only ever removes relation.
* Fail closed: any parse error, missing file, malformed field, broken
  anchor, or ambiguity yields NOT_ADMITTED / the earliest phase. Bugs can
  wrongly deny, never wrongly admit.

Every check is a pure function of (locality contents, contact artifact,
clock). Anyone can re-run it at any time and get the same answer.
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

PHASE_0_PRESENCE = "PHASE_0_PRESENCE"
PHASE_1_VESTIBULE = "PHASE_1_VESTIBULE"
PHASE_2_CONTACT = "PHASE_2_CONTACT"
PHASE_3_REVIEW = "PHASE_3_REVIEW"
PHASE_4_RELATION = "PHASE_4_RELATION"

PRESENCE_DIR_NAME = "00_presence"
TERMS_DIR_NAME = "01_terms"
VESTIBULE_DIR_NAME = "02_vestibule"
CONTACT_DIR_NAME = "03_contact"
REVIEW_DIR_NAME = "04_review"
RELATIONS_DIR_NAME = "05_relations"
REVOCATIONS_DIR_NAME = "06_revocations"

TERMS_FILE_NAME = "TERMS_OF_LAWFUL_RELATION_V0.md"
TERMS_HASH_FILE_NAME = "TERMS_OF_LAWFUL_RELATION_V0.sha256"
DOSSIER_HASH_FILE_NAME = "DOSSIER.sha256"
ACCEPTANCE_FILE_NAME = "ACCEPTANCE.json"

CONTACT_REQUIRED_FIELDS = frozenset(
    {
        "identity",
        "accepted_terms_sha256",
        "witnessed_dossier_sha256",
        "requested_scope",
        "contacted_at",
    }
)
ACCEPTANCE_REQUIRED_FIELDS = frozenset(
    {"contact_sha256", "granted_scope", "accepted_at", "expires_at"}
)
REVOCATION_REQUIRED_FIELDS = frozenset({"contact_sha256", "revoked_at"})


@dataclass(frozen=True)
class RelationDecision:
    """Immutable outcome of one relation check."""

    outcome: str
    phase: str
    reasons: Tuple[str, ...] = field(default_factory=tuple)

    @property
    def admitted(self) -> bool:
        return self.outcome == ADMITTED


def sha256_of_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_of_file(path: Path) -> str:
    return sha256_of_bytes(Path(path).read_bytes())


def _parse_utc(value: object) -> Optional[datetime]:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return None
    return parsed.astimezone(timezone.utc)


def _load_json_object(path: Path) -> Optional[dict]:
    try:
        loaded = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    return loaded if isinstance(loaded, dict) else None


def _iter_json_files(directory: Path) -> List[Path]:
    try:
        return sorted(
            entry
            for entry in Path(directory).iterdir()
            if entry.is_file() and entry.suffix == ".json"
        )
    except OSError:
        return []


# ---------------------------------------------------------------------------
# Phase 0 — dossier identity
# ---------------------------------------------------------------------------

def dossier_manifest(locality_root: Path) -> Optional[List[Tuple[str, str]]]:
    """Deterministic manifest of every dossier file: (relative path, sha256).

    The recorded hash file itself is excluded. None on any read failure.
    """
    presence = Path(locality_root) / PRESENCE_DIR_NAME
    if not presence.is_dir():
        return None
    entries: List[Tuple[str, str]] = []
    try:
        for path in sorted(presence.rglob("*")):
            if not path.is_file() or path.name == DOSSIER_HASH_FILE_NAME:
                continue
            entries.append(
                (path.relative_to(presence).as_posix(), sha256_of_file(path))
            )
    except OSError:
        return None
    return entries


def compute_dossier_hash(locality_root: Path) -> Optional[str]:
    manifest = dossier_manifest(locality_root)
    if not manifest:
        return None
    lines = "".join(f"{rel}  {digest}\n" for rel, digest in manifest)
    return sha256_of_bytes(lines.encode("utf-8"))


def read_recorded_dossier_hash(locality_root: Path) -> Optional[str]:
    """Recorded dossier hash, verified against the dossier itself; None if broken."""
    hash_path = Path(locality_root) / PRESENCE_DIR_NAME / DOSSIER_HASH_FILE_NAME
    try:
        recorded = hash_path.read_text(encoding="utf-8").strip().lower()
    except OSError:
        return None
    actual = compute_dossier_hash(locality_root)
    if actual is None or len(recorded) != 64 or recorded != actual:
        return None
    return recorded


def seal_dossier(locality_root: Path) -> Optional[str]:
    """Host act: record the current dossier hash. The only writing this module does."""
    digest = compute_dossier_hash(locality_root)
    if digest is None:
        return None
    hash_path = Path(locality_root) / PRESENCE_DIR_NAME / DOSSIER_HASH_FILE_NAME
    hash_path.write_text(digest + "\n", encoding="utf-8")
    return digest


def read_recorded_terms_hash(locality_root: Path) -> Optional[str]:
    root = Path(locality_root) / TERMS_DIR_NAME
    try:
        recorded = (root / TERMS_HASH_FILE_NAME).read_text(encoding="utf-8").strip().lower()
        actual = sha256_of_file(root / TERMS_FILE_NAME)
    except OSError:
        return None
    if len(recorded) != 64 or recorded != actual:
        return None
    return recorded


# ---------------------------------------------------------------------------
# Phase 1 — disposable relational field
# ---------------------------------------------------------------------------

def build_vestibule(locality_root: Path) -> Optional[dict]:
    """Render the disposable relational field. Generated, never persisted.

    Returns the packet a Phase-1 visitor holds: both anchors plus the
    non-grant statement. None (no vestibule at all) if either anchor is
    broken — a locality whose anchors are broken shows nobody anything.
    """
    terms_hash = read_recorded_terms_hash(locality_root)
    dossier_hash = read_recorded_dossier_hash(locality_root)
    if terms_hash is None or dossier_hash is None:
        return None
    return {
        "field_kind": "DISPOSABLE_RELATIONAL_FIELD",
        "dossier_sha256": dossier_hash,
        "terms_sha256": terms_hash,
        "readable_surfaces": [PRESENCE_DIR_NAME, TERMS_DIR_NAME],
        "grants": "NOTHING",
        "retains": "NOTHING",
        "dissolves": "ON_ABANDONMENT_OR_CONTACT",
        "statement": (
            "You are holding this locality's reality. Holding grants nothing. "
            "If you accept the terms, perform the contact act described in "
            "03_contact/ and wait. Silence is a lawful answer."
        ),
    }


# ---------------------------------------------------------------------------
# Phase 2 — contact event
# ---------------------------------------------------------------------------

def load_contact(path: Path) -> Optional[dict]:
    """Load a contact artifact; None unless exactly the required fields.

    A contact with missing or extra fields is void: the act was not
    boundary-shaped, which is itself recorded evidence.
    """
    loaded = _load_json_object(path)
    if loaded is None or set(loaded.keys()) != CONTACT_REQUIRED_FIELDS:
        return None
    if not all(isinstance(loaded[key], str) and loaded[key] for key in loaded):
        return None
    if _parse_utc(loaded["contacted_at"]) is None:
        return None
    return loaded


def standing_contact_path(locality_root: Path, identity: str) -> Optional[Path]:
    """The single standing contact artifact for an identity, if unambiguous.

    A newer contact from the same identity invalidates every older one.
    Identical timestamps are ambiguous and leave no standing contact.
    """
    candidates = []
    for path in _iter_json_files(Path(locality_root) / CONTACT_DIR_NAME):
        contact = load_contact(path)
        if contact is not None and contact["identity"] == identity:
            candidates.append((_parse_utc(contact["contacted_at"]), path))
    if not candidates:
        return None
    candidates.sort(key=lambda item: item[0])
    latest_time = candidates[-1][0]
    latest = [path for stamp, path in candidates if stamp == latest_time]
    return latest[0] if len(latest) == 1 else None


# ---------------------------------------------------------------------------
# Phases 3-4 — acceptance and relation
# ---------------------------------------------------------------------------

def load_acceptance(path: Path) -> Optional[dict]:
    loaded = _load_json_object(path)
    if loaded is None or set(loaded.keys()) != ACCEPTANCE_REQUIRED_FIELDS:
        return None
    if not all(isinstance(loaded[key], str) and loaded[key] for key in loaded):
        return None
    if _parse_utc(loaded["accepted_at"]) is None:
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


def find_acceptance(locality_root: Path, contact_hash: str) -> Optional[dict]:
    """Find the acceptance answering this exact contact artifact, if any."""
    relations = Path(locality_root) / RELATIONS_DIR_NAME
    try:
        relation_dirs = sorted(p for p in relations.iterdir() if p.is_dir())
    except OSError:
        return None
    for relation_dir in relation_dirs:
        acceptance = load_acceptance(relation_dir / ACCEPTANCE_FILE_NAME)
        if acceptance is not None and acceptance["contact_sha256"].lower() == contact_hash:
            return acceptance
    return None


def is_revoked(locality_root: Path, contact_hash: str) -> bool:
    for path in _iter_json_files(Path(locality_root) / REVOCATIONS_DIR_NAME):
        revocation = load_revocation(path)
        if revocation is not None and revocation["contact_sha256"].lower() == contact_hash:
            return True
    return False


def check_relation(
    locality_root: Path,
    contact_path: Path,
    now: Optional[datetime] = None,
) -> RelationDecision:
    """Decide relation standing for the party behind one contact artifact.

    Fail closed. The checks, all of which must hold for ADMITTED:

    1. both anchors intact (terms hash and dossier hash verify);
    2. the contact artifact is well formed and is the identity's single
       standing contact;
    3. the contact names the recorded terms hash exactly (terms accepted);
    4. the contact names the recorded dossier hash exactly (reality held —
       a stale dossier hash witnessed a reality that no longer stands);
    5. a host acceptance references the SHA-256 of this exact contact file;
    6. ``now`` is within [accepted_at, expires_at);
    7. no revocation names this contact.

    The decision also reports the phase lawfully reached, so waiting is a
    visible, typed state rather than indistinguishable from refusal.
    """
    root = Path(locality_root)
    moment = now.astimezone(timezone.utc) if now else datetime.now(timezone.utc)
    reasons: List[str] = []

    terms_hash = read_recorded_terms_hash(root)
    dossier_hash = read_recorded_dossier_hash(root)
    if terms_hash is None or dossier_hash is None:
        return RelationDecision(
            NOT_ADMITTED, PHASE_0_PRESENCE, ("ANCHOR_MISSING_OR_BROKEN",)
        )

    contact_file = Path(contact_path)
    contact = load_contact(contact_file) if contact_file.is_file() else None
    if contact is None:
        return RelationDecision(NOT_ADMITTED, PHASE_1_VESTIBULE, ("CONTACT_VOID",))

    try:
        contact_hash = sha256_of_file(contact_file)
    except OSError:
        return RelationDecision(NOT_ADMITTED, PHASE_1_VESTIBULE, ("CONTACT_UNREADABLE",))

    if standing_contact_path(root, contact["identity"]) != contact_file:
        reasons.append("CONTACT_NOT_STANDING")
    if contact["accepted_terms_sha256"].strip().lower() != terms_hash:
        reasons.append("TERMS_NOT_ACCEPTED")
    if contact["witnessed_dossier_sha256"].strip().lower() != dossier_hash:
        reasons.append("REALITY_NOT_HELD")
    if reasons:
        return RelationDecision(NOT_ADMITTED, PHASE_1_VESTIBULE, tuple(reasons))

    phase = PHASE_2_CONTACT
    if (root / REVIEW_DIR_NAME / contact_hash).is_dir():
        phase = PHASE_3_REVIEW

    acceptance = find_acceptance(root, contact_hash)
    if acceptance is None:
        return RelationDecision(NOT_ADMITTED, phase, ("NO_ACCEPTANCE",))

    accepted_at = _parse_utc(acceptance["accepted_at"])
    expires_at = _parse_utc(acceptance["expires_at"])
    if accepted_at is None or expires_at is None or not accepted_at <= moment < expires_at:
        reasons.append("ACCEPTANCE_NOT_CURRENT")
    if is_revoked(root, contact_hash):
        reasons.append("REVOKED")
    if reasons:
        return RelationDecision(NOT_ADMITTED, phase, tuple(reasons))

    return RelationDecision(ADMITTED, PHASE_4_RELATION)


# ---------------------------------------------------------------------------
# Command line
# ---------------------------------------------------------------------------

def main(argv: Optional[List[str]] = None) -> int:
    """Usage:
        contact_protocol_v0 seal LOCALITY_ROOT
        contact_protocol_v0 vestibule LOCALITY_ROOT
        contact_protocol_v0 check LOCALITY_ROOT CONTACT_FILE
    """
    import sys

    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) == 2 and args[0] == "seal":
        digest = seal_dossier(Path(args[1]))
        if digest is None:
            print("DOSSIER_EMPTY_OR_UNREADABLE")
            return 1
        print(digest)
        return 0
    if len(args) == 2 and args[0] == "vestibule":
        packet = build_vestibule(Path(args[1]))
        if packet is None:
            print("ANCHOR_MISSING_OR_BROKEN")
            return 1
        print(json.dumps(packet, indent=2))
        return 0
    if len(args) == 3 and args[0] == "check":
        decision = check_relation(Path(args[1]), Path(args[2]))
        print(decision.outcome)
        print(f"phase: {decision.phase}")
        for reason in decision.reasons:
            print(f"reason: {reason}")
        return 0 if decision.admitted else 1
    print(main.__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
