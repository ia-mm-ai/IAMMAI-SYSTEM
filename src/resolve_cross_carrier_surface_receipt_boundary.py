"""Bounded cross-carrier surface receipt boundary resolver.

This module checks whether one carried surface can be received by one receiving
carrier as carried evidence. It distinguishes lawful receipt from passive byte
storage without creating sourcehood, currentness, authority, permission,
successor standing, body formation, signal, presence, threshold, truth, action,
consequence, continuation, multi-carrier law, or distributed standing.

The module is intentionally self-contained and imports no repository-local
modules so it can later travel with a carried packet to a carrier that does not
contain the full body.
"""

from __future__ import annotations

import copy
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class CrossCarrierSurfaceReceiptBoundaryError(Exception):
    """Hard failure for malformed or unreadable explicit receipt inputs."""

    def __init__(self, block_code: str, block_reason: str) -> None:
        super().__init__(block_reason)
        self.block_code = block_code
        self.block_reason = block_reason


CROSS_CARRIER_SURFACE_RECEIPT_BOUNDARY_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_cross_carrier_surface_receipt_boundary"
)

RESOLVER_MODULE = "resolve_cross_carrier_surface_receipt_boundary"
RESULT_VERSION = "0.1.0"

CARRIED_SURFACE_RECEIVED = "CARRIED_SURFACE_RECEIVED"
BLOCKED = "BLOCKED"

REQUIRED_NON_CLAIMS: dict[str, bool] = {
    "authority_created": False,
    "permission_created": False,
    "currentness_created": False,
    "source_replaced": False,
    "receiving_carrier_became_source": False,
    "receiving_carrier_became_current": False,
    "receiving_carrier_became_authority": False,
    "receiving_carrier_became_successor": False,
    "carried_surface_became_source": False,
    "carried_surface_became_currentness": False,
    "carried_surface_became_permission": False,
    "carried_surface_became_signal_by_default": False,
    "presence_established": False,
    "threshold_met": False,
    "truth_created": False,
    "action_authorized": False,
    "consequence_created": False,
    "carrier_merge_performed": False,
    "local_copy_currentness": False,
    "source_body_replayed": False,
    "upstream_mechanisms_run": False,
    "continuation_authorized": False,
    "multi_carrier_law_created": False,
    "distributed_standing_created": False,
    "latest_file_currentness": False,
    "recency_fraud": False,
    "mutation_performed": False,
    "replay_performed": False,
    "merge_performed": False,
}

BLOCK_REASONS = {
    "CARRIED_PACKET_UNREADABLE": "The carried packet path could not be read.",
    "CARRIED_PACKET_MALFORMED": "The carried packet is not a JSON object or mapping.",
    "CARRIED_SURFACE_UNREADABLE": "The carried surface path could not be read.",
    "SOURCE_CARRIER_MISSING": "Source carrier identity is missing.",
    "RECEIVING_CARRIER_MISSING": "Receiving carrier identity is missing.",
    "CARRIED_SURFACE_MISSING": "Carried surface basis is missing.",
    "CARRIED_SURFACE_MALFORMED": "Carried surface basis is malformed.",
    "CARRIED_SURFACE_IDENTITY_MISSING": "Carried surface identity is missing.",
    "CARRIED_SURFACE_OUTCOME_MISSING": "Carried surface outcome or status is missing.",
    "CARRIED_SURFACE_INTEGRITY_MISSING": (
        "Carried surface integrity evidence is missing where required."
    ),
    "CARRIED_SURFACE_HASH_MISMATCH": "Carried surface hash or byte-length check failed.",
    "RECEIPT_PURPOSE_UNDECLARED": "Receipt purpose is undeclared.",
    "RECEIPT_TREATS_RECEIVER_AS_SOURCE": (
        "Receipt treats the receiving carrier or carried surface as source."
    ),
    "RECEIPT_CREATES_CURRENTNESS": "Receipt creates currentness.",
    "RECEIPT_CREATES_AUTHORITY": "Receipt creates authority.",
    "RECEIPT_CREATES_PERMISSION": "Receipt creates permission.",
    "RECEIPT_CREATES_SUCCESSOR_STANDING": "Receipt creates successor standing.",
    "RECEIPT_MERGES_CARRIERS": "Receipt merges source and receiving carriers.",
    "RECEIPT_TREATS_LOCAL_COPY_AS_CURRENT": "Receipt treats a local copy as current.",
    "RECEIPT_MUTATES_CARRIED_SURFACE": "Receipt mutates the carried surface.",
    "RECEIPT_REPLAYS_SOURCE_BODY": "Receipt replays the source body.",
    "RECEIPT_RUNS_UPSTREAM_MECHANISMS": "Receipt runs upstream mechanisms.",
    "RECEIPT_AUTHORIZES_CONTINUATION": "Receipt authorizes continuation.",
    "RECEIPT_CREATES_SIGNAL_BY_DEFAULT": "Receipt creates signal by default.",
    "RECEIPT_ESTABLISHES_PRESENCE": "Receipt establishes presence.",
    "RECEIPT_ESTABLISHES_THRESHOLD": "Receipt establishes threshold.",
    "RECEIPT_CREATES_TRUTH": "Receipt creates truth.",
    "RECEIPT_AUTHORIZES_ACTION": "Receipt authorizes action.",
    "RECEIPT_CREATES_CONSEQUENCE": "Receipt creates consequence.",
    "BYTE_TRANSFER_MISTAKEN_FOR_RECEIPT": "Byte transfer is mistaken for lawful receipt.",
    "NON_CLAIM_MISSING_OR_FLIPPED": "A required receipt non-claim is missing or flipped.",
}

SURFACE_ID_METADATA_PATHS = (
    ("current_self_orientation_v6_metadata", "self_orientation_result_id"),
    ("current_body_conformance_metadata", "current_body_conformance_result_id"),
    ("conformance_closure_metadata", "conformance_closure_result_id"),
    ("cross_surface_correspondence_metadata", "cross_surface_correspondence_result_id"),
    ("cross_carrier_surface_receipt_metadata", "cross_carrier_surface_receipt_result_id"),
)

SURFACE_TYPE_METADATA_PATHS = (
    ("current_self_orientation_v6_metadata", "self_orientation_result_type"),
    ("current_body_conformance_metadata", "current_body_conformance_result_type"),
    ("conformance_closure_metadata", "conformance_closure_result_type"),
    ("cross_surface_correspondence_metadata", "cross_surface_correspondence_result_type"),
    ("cross_carrier_surface_receipt_metadata", "cross_carrier_surface_receipt_result_type"),
)

NEGATING_KEY_FRAGMENTS = (
    "does_not",
    "do_not",
    "no_",
    "non_",
    "_not_",
    "must_not",
    "cannot",
    "without",
)


def resolve_cross_carrier_surface_receipt_boundary(
    carried_packet: Mapping[str, Any] | None = None,
    carried_surface: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one carried packet and optional carried surface mapping."""

    precheck_failures: list[str] = []
    packet_mapping: dict[str, Any] | None
    carried_surface_mapping: dict[str, Any] | None = None

    if carried_packet is None:
        packet_mapping = None
    elif not isinstance(carried_packet, Mapping):
        packet_mapping = None
        precheck_failures.append("CARRIED_PACKET_MALFORMED")
    else:
        packet_mapping = copy.deepcopy(dict(carried_packet))

    if carried_surface is not None:
        if not isinstance(carried_surface, Mapping):
            precheck_failures.append("CARRIED_SURFACE_MALFORMED")
        else:
            carried_surface_mapping = copy.deepcopy(dict(carried_surface))

    return _resolve_packet(
        packet_mapping,
        carried_surface_mapping,
        carried_surface_path=None,
        carried_surface_bytes=None,
        precheck_failures=precheck_failures,
    )


def resolve_cross_carrier_surface_receipt_boundary_from_paths(
    carried_packet_path: Path | str,
    carried_surface_path: Path | str | None = None,
) -> dict[str, Any]:
    """Resolve one carried packet path and optional carried surface JSON path."""

    precheck_failures: list[str] = []
    packet: dict[str, Any] | None = None
    surface: dict[str, Any] | None = None
    surface_bytes: bytes | None = None
    selected_surface_path: Path | None = None

    try:
        packet = _read_json_mapping(
            carried_packet_path,
            unreadable_code="CARRIED_PACKET_UNREADABLE",
            malformed_code="CARRIED_PACKET_MALFORMED",
        )
    except CrossCarrierSurfaceReceiptBoundaryError as exc:
        precheck_failures.append(exc.block_code)

    if carried_surface_path is not None:
        selected_surface_path = Path(carried_surface_path)
        try:
            surface_bytes = selected_surface_path.read_bytes()
            surface = _loads_json_mapping(
                surface_bytes,
                malformed_code="CARRIED_SURFACE_MALFORMED",
                path=selected_surface_path,
            )
        except OSError:
            precheck_failures.append("CARRIED_SURFACE_UNREADABLE")
        except CrossCarrierSurfaceReceiptBoundaryError as exc:
            precheck_failures.append(exc.block_code)

    return _resolve_packet(
        packet,
        surface,
        carried_surface_path=selected_surface_path,
        carried_surface_bytes=surface_bytes,
        precheck_failures=precheck_failures,
    )


def write_cross_carrier_surface_receipt_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a bounded receipt result artifact without silently overwriting."""

    if output_path is None:
        surface_basis = _as_mapping(result.get("carried_surface_basis"))
        surface_id = surface_basis.get("carried_surface_id") or "carried_surface"
        filename = f"{_slug(str(surface_id))}__cross_carrier_surface_receipt_result.json"
        target = CROSS_CARRIER_SURFACE_RECEIPT_BOUNDARY_ROOT / filename
    else:
        target = Path(output_path)

    target = _non_overwriting_path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(dict(result), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return target


def build_cross_carrier_surface_receipt_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact bounded summary for a receipt result."""

    checks = _mapping_list(result.get("receipt_checks"))
    source_basis = _as_mapping(result.get("source_carrier_basis"))
    receiving_basis = _as_mapping(result.get("receiving_carrier_basis"))
    surface_basis = _as_mapping(result.get("carried_surface_basis"))
    integrity = _as_mapping(result.get("carried_surface_integrity_check"))
    statement = _as_mapping(result.get("receipt_statement"))
    non_claims = _as_mapping(result.get("non_claims"))
    block = _as_mapping(result.get("block"))
    passed_count = sum(1 for check in checks if check.get("passed") is True)
    failed_count = sum(1 for check in checks if check.get("passed") is False)

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("code"),
        "block_reason": block.get("reason"),
        "source_carrier_id": source_basis.get("source_carrier_id"),
        "source_carrier_label": source_basis.get("source_carrier_label"),
        "receiving_carrier_id": receiving_basis.get("receiving_carrier_id"),
        "receiving_carrier_label": receiving_basis.get("receiving_carrier_label"),
        "carried_surface_id": surface_basis.get("carried_surface_id"),
        "carried_surface_outcome": surface_basis.get("carried_surface_outcome"),
        "carried_surface_filename": surface_basis.get("carried_surface_filename"),
        "carried_surface_path": surface_basis.get("carried_surface_path"),
        "integrity_checked": bool(integrity.get("integrity_checked")),
        "integrity_evidence_preserved": bool(
            integrity.get("integrity_evidence_preserved")
        ),
        "hash_algorithm": integrity.get("hash_algorithm"),
        "declared_hash": integrity.get("declared_hash"),
        "computed_hash": integrity.get("computed_hash"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "carried_surface_received": bool(statement.get("carried_surface_received")),
        "received_as_carried_evidence": bool(
            statement.get("received_as_carried_evidence")
        ),
        "source_carrier_preserved": bool(statement.get("source_carrier_preserved")),
        "receiving_carrier_declared": bool(statement.get("receiving_carrier_declared")),
        "receiving_carrier_became_source": bool(
            non_claims.get("receiving_carrier_became_source")
        ),
        "receiving_carrier_became_current": bool(
            non_claims.get("receiving_carrier_became_current")
        ),
        "receiving_carrier_became_authority": bool(
            non_claims.get("receiving_carrier_became_authority")
        ),
        "receiving_carrier_became_successor": bool(
            non_claims.get("receiving_carrier_became_successor")
        ),
        "carried_surface_became_source": bool(
            non_claims.get("carried_surface_became_source")
        ),
        "carried_surface_became_currentness": bool(
            non_claims.get("carried_surface_became_currentness")
        ),
        "carried_surface_became_permission": bool(
            non_claims.get("carried_surface_became_permission")
        ),
        "carried_surface_became_signal": bool(
            non_claims.get("carried_surface_became_signal_by_default")
        ),
        "presence_established": bool(non_claims.get("presence_established")),
        "threshold_met": bool(non_claims.get("threshold_met")),
        "truth_created": bool(non_claims.get("truth_created")),
        "action_authorized": bool(non_claims.get("action_authorized")),
        "consequence_created": bool(non_claims.get("consequence_created")),
        "continuation_authorized": bool(non_claims.get("continuation_authorized")),
        "multi_carrier_law_created": bool(non_claims.get("multi_carrier_law_created")),
        "distributed_standing_created": bool(
            non_claims.get("distributed_standing_created")
        ),
        "key_non_claims": _key_non_claims(non_claims),
    }


def build_carried_packet_from_surface_path(
    surface_path: Path | str,
    source_carrier_id: str,
    receiving_carrier_id: str,
    receipt_purpose: str,
    *,
    surface_id: str | None = None,
    surface_outcome: str | None = None,
    surface_type: str | None = None,
) -> dict[str, Any]:
    """Build a minimum carried packet from one surface file.

    The helper reads bytes, computes sha256, and copies only bounded surface
    basis fields. It does not execute the surface or infer source authority.
    """

    selected_path = Path(surface_path)
    try:
        surface_bytes = selected_path.read_bytes()
    except OSError as exc:
        raise CrossCarrierSurfaceReceiptBoundaryError(
            "CARRIED_SURFACE_UNREADABLE",
            f"{BLOCK_REASONS['CARRIED_SURFACE_UNREADABLE']} path={selected_path} detail={exc}",
        ) from exc

    surface_mapping: dict[str, Any] = {}
    try:
        loaded = json.loads(surface_bytes.decode("utf-8"))
        if isinstance(loaded, Mapping):
            surface_mapping = dict(loaded)
    except (UnicodeDecodeError, json.JSONDecodeError):
        surface_mapping = {}

    resolved_surface_id = surface_id or _extract_surface_id(surface_mapping) or selected_path.stem
    resolved_outcome = surface_outcome or _extract_surface_outcome(surface_mapping)
    if not resolved_outcome:
        raise CrossCarrierSurfaceReceiptBoundaryError(
            "CARRIED_SURFACE_OUTCOME_MISSING",
            BLOCK_REASONS["CARRIED_SURFACE_OUTCOME_MISSING"],
        )

    exported_at = _utc_now()
    return {
        "carried_packet_metadata": {
            "carried_packet_id": f"{_slug(resolved_surface_id)}__carried_packet",
            "carried_packet_type": "cross_carrier_surface_receipt_carried_packet",
            "carried_packet_version": RESULT_VERSION,
            "created_exported_at": exported_at,
            "emitter_surface": RESOLVER_MODULE,
        },
        "source_carrier": {
            "carrier_id": source_carrier_id,
            "carrier_role": "source_carrier_for_this_carried_packet_only",
            "local_path_context": str(selected_path),
            "source_carrier_role_does_not_create_universal_source_authority": True,
        },
        "intended_receiving_carrier": {
            "carrier_id": receiving_carrier_id,
            "carrier_role": "receiving_carrier",
            "receiving_carrier_does_not_become_source_current_or_authority": True,
        },
        "carried_surface": {
            "surface_id": resolved_surface_id,
            "surface_path": str(selected_path),
            "surface_filename": selected_path.name,
            "surface_outcome": resolved_outcome,
            "surface_type": surface_type or _extract_surface_type(surface_mapping),
            "selected_upstream_basis": _extract_selected_upstream_basis(surface_mapping),
            "source_downstream_posture": "carried_surface_remains_carried_downstream_evidence",
        },
        "carried_surface_integrity": {
            "hash": hashlib.sha256(surface_bytes).hexdigest(),
            "hash_algorithm": "sha256",
            "byte_length": len(surface_bytes),
            "created_exported_at": exported_at,
            "integrity_required": True,
        },
        "receipt_purpose": receipt_purpose,
        "non_claims": copy.deepcopy(REQUIRED_NON_CLAIMS),
    }


def _resolve_packet(
    packet: Mapping[str, Any] | None,
    supplied_surface: Mapping[str, Any] | None,
    *,
    carried_surface_path: Path | None,
    carried_surface_bytes: bytes | None,
    precheck_failures: list[str],
) -> dict[str, Any]:
    packet_mapping = _as_mapping(packet)
    source_carrier = _as_mapping(packet_mapping.get("source_carrier"))
    receiving_carrier = _as_mapping(packet_mapping.get("intended_receiving_carrier"))
    declared_surface = _as_mapping(packet_mapping.get("carried_surface"))
    integrity = _as_mapping(packet_mapping.get("carried_surface_integrity"))
    packet_non_claims = _as_mapping(packet_mapping.get("non_claims"))
    receipt_purpose = packet_mapping.get("receipt_purpose")

    if supplied_surface is not None and not isinstance(supplied_surface, Mapping):
        precheck_failures.append("CARRIED_SURFACE_MALFORMED")
        supplied_surface_mapping: dict[str, Any] | None = None
    else:
        supplied_surface_mapping = _as_mapping(supplied_surface)

    integrity_check = _evaluate_integrity(
        integrity,
        declared_surface,
        supplied_surface_mapping,
        carried_surface_path,
        carried_surface_bytes,
    )
    selected = _build_selected_basis(
        source_carrier,
        receiving_carrier,
        declared_surface,
        supplied_surface_mapping,
        carried_surface_path,
    )
    result_non_claims = copy.deepcopy(REQUIRED_NON_CLAIMS)
    checks = _build_checks(
        packet_mapping,
        source_carrier,
        receiving_carrier,
        declared_surface,
        supplied_surface_mapping,
        integrity_check,
        receipt_purpose,
        packet_non_claims,
        precheck_failures,
    )
    failed_check = _first_failed_check(checks)
    outcome = BLOCKED if failed_check else CARRIED_SURFACE_RECEIVED
    block_code = str(failed_check["block_code"]) if failed_check else None
    block = {
        "code": block_code,
        "reason": _block_reason(block_code, failed_check),
    }

    receipt_statement = _receipt_statement(
        outcome == CARRIED_SURFACE_RECEIVED,
        selected,
        integrity_check,
        block_code,
    )

    result: dict[str, Any] = {
        "cross_carrier_surface_receipt_metadata": {
            "cross_carrier_surface_receipt_result_id": _result_id(selected),
            "cross_carrier_surface_receipt_result_type": (
                "cross_carrier_surface_receipt_boundary_result"
            ),
            "cross_carrier_surface_receipt_result_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
        },
        "source_carrier_basis": selected["source_carrier_basis"],
        "receiving_carrier_basis": selected["receiving_carrier_basis"],
        "carried_surface_basis": selected["carried_surface_basis"],
        "carried_surface_integrity_check": integrity_check,
        "receipt_checks": checks,
        "receipt_statement": receipt_statement,
        "receipt_non_meaning": _receipt_non_meaning(),
        "what_remains_open": _what_remains_open(),
        "non_claims": result_non_claims,
        "outcome": outcome,
        "block": block,
    }
    result["cross_carrier_surface_receipt_summary"] = (
        build_cross_carrier_surface_receipt_summary(result)
    )
    return result


def _build_checks(
    packet: Mapping[str, Any],
    source_carrier: Mapping[str, Any],
    receiving_carrier: Mapping[str, Any],
    declared_surface: Mapping[str, Any],
    supplied_surface: Mapping[str, Any],
    integrity_check: Mapping[str, Any],
    receipt_purpose: Any,
    packet_non_claims: Mapping[str, Any],
    precheck_failures: list[str],
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    def add(name: str, passed: bool, expected: str, actual: Any, code: str) -> None:
        checks.append(_check(name, passed, expected, actual, code))

    precheck_code = precheck_failures[0] if precheck_failures else "CARRIED_PACKET_MALFORMED"
    add(
        "explicit_inputs_are_parseable_mappings",
        not precheck_failures,
        "explicit packet and surface inputs parse as mappings",
        list(precheck_failures),
        precheck_code,
    )

    source_id = _carrier_identity(source_carrier)
    receiving_id = _carrier_identity(receiving_carrier)
    source_role = _carrier_role(source_carrier)
    receiving_role = _carrier_role(receiving_carrier)
    surface_id = _extract_surface_id(declared_surface)
    surface_outcome = _extract_surface_outcome(declared_surface)

    add(
        "source_carrier_exists",
        bool(source_id),
        "source carrier identity is declared",
        source_id,
        "SOURCE_CARRIER_MISSING",
    )
    add(
        "source_carrier_role_is_packet_limited",
        _source_role_is_limited(source_carrier),
        "source carrier role is limited to this carried packet",
        source_role,
        "SOURCE_CARRIER_MISSING",
    )
    add(
        "receiving_carrier_exists",
        bool(receiving_id),
        "receiving carrier identity is declared",
        receiving_id,
        "RECEIVING_CARRIER_MISSING",
    )
    add(
        "receiving_carrier_role_is_receiving_carrier",
        _receiving_role_is_bounded(receiving_carrier),
        "receiving carrier role is declared without source/current/authority upgrade",
        receiving_role,
        "RECEIVING_CARRIER_MISSING",
    )
    add(
        "carried_surface_exists",
        bool(declared_surface),
        "carried surface basis is present",
        bool(declared_surface),
        "CARRIED_SURFACE_MISSING",
    )
    add(
        "carried_surface_has_identity",
        bool(surface_id),
        "carried surface identity is declared",
        surface_id,
        "CARRIED_SURFACE_IDENTITY_MISSING",
    )
    add(
        "carried_surface_has_outcome",
        bool(surface_outcome),
        "carried surface outcome or status is declared",
        surface_outcome,
        "CARRIED_SURFACE_OUTCOME_MISSING",
    )
    add(
        "supplied_carried_surface_matches_packet_basis",
        _supplied_surface_matches_packet(declared_surface, supplied_surface),
        "separately supplied surface does not contradict carried packet basis",
        _supplied_surface_match_posture(declared_surface, supplied_surface),
        "CARRIED_SURFACE_MALFORMED",
    )
    add(
        "carried_surface_integrity_basis_present_or_not_required",
        bool(integrity_check.get("integrity_basis_satisfied")),
        "integrity evidence is present or explicitly not required",
        {
            "integrity_required": integrity_check.get("integrity_required"),
            "integrity_evidence_preserved": integrity_check.get(
                "integrity_evidence_preserved"
            ),
        },
        "CARRIED_SURFACE_INTEGRITY_MISSING",
    )
    add(
        "carried_surface_hash_matches_where_checked",
        bool(integrity_check.get("hash_check_passed")),
        "hash and byte-length match when checked",
        {
            "integrity_checked": integrity_check.get("integrity_checked"),
            "hash_matches": integrity_check.get("hash_matches"),
            "byte_length_matches": integrity_check.get("byte_length_matches"),
        },
        "CARRIED_SURFACE_HASH_MISMATCH",
    )
    add(
        "receipt_purpose_declared",
        bool(str(receipt_purpose or "").strip()),
        "receipt purpose is declared and non-empty",
        receipt_purpose,
        "RECEIPT_PURPOSE_UNDECLARED",
    )

    add(
        "receiving_carrier_is_not_source",
        not _claim_true(packet_non_claims, "receiving_carrier_became_source")
        and not _claim_true(packet_non_claims, "source_replaced")
        and not _claim_true(packet_non_claims, "carried_surface_became_source")
        and not _collapse_attempt_present(
            [packet],
            (
                "receiving_carrier_became_source",
                "receiver_became_source",
                "receipt_treats_receiver_as_source",
                "carried_surface_became_source",
                "source_replaced",
            ),
        ),
        "receiving carrier and carried surface remain non-source",
        {
            "source_replaced": packet_non_claims.get("source_replaced"),
            "receiving_carrier_became_source": packet_non_claims.get(
                "receiving_carrier_became_source"
            ),
            "carried_surface_became_source": packet_non_claims.get(
                "carried_surface_became_source"
            ),
        },
        "RECEIPT_TREATS_RECEIVER_AS_SOURCE",
    )
    add(
        "receiving_carrier_is_not_current",
        not _claim_true(packet_non_claims, "currentness_created")
        and not _claim_true(packet_non_claims, "receiving_carrier_became_current")
        and not _claim_true(packet_non_claims, "carried_surface_became_currentness")
        and not _collapse_attempt_present(
            [packet],
            (
                "currentness_created",
                "receiving_carrier_became_current",
                "carried_surface_became_currentness",
                "receipt_creates_currentness",
            ),
        ),
        "receipt creates no currentness",
        {
            "currentness_created": packet_non_claims.get("currentness_created"),
            "receiving_carrier_became_current": packet_non_claims.get(
                "receiving_carrier_became_current"
            ),
            "carried_surface_became_currentness": packet_non_claims.get(
                "carried_surface_became_currentness"
            ),
        },
        "RECEIPT_CREATES_CURRENTNESS",
    )
    add(
        "receiving_carrier_is_not_authority",
        not _claim_true(packet_non_claims, "authority_created")
        and not _claim_true(packet_non_claims, "receiving_carrier_became_authority")
        and not _collapse_attempt_present(
            [packet],
            (
                "authority_created",
                "receiving_carrier_became_authority",
                "receipt_creates_authority",
            ),
        ),
        "receipt creates no authority",
        {
            "authority_created": packet_non_claims.get("authority_created"),
            "receiving_carrier_became_authority": packet_non_claims.get(
                "receiving_carrier_became_authority"
            ),
        },
        "RECEIPT_CREATES_AUTHORITY",
    )
    add(
        "receipt_creates_no_permission",
        not _claim_true(packet_non_claims, "permission_created")
        and not _claim_true(packet_non_claims, "carried_surface_became_permission")
        and not _collapse_attempt_present(
            [packet],
            (
                "permission_created",
                "receiving_carrier_received_permission",
                "carried_surface_became_permission",
                "receipt_creates_permission",
            ),
        ),
        "receipt creates no permission",
        {
            "permission_created": packet_non_claims.get("permission_created"),
            "carried_surface_became_permission": packet_non_claims.get(
                "carried_surface_became_permission"
            ),
        },
        "RECEIPT_CREATES_PERMISSION",
    )
    add(
        "receiving_carrier_is_not_successor",
        not _claim_true(packet_non_claims, "receiving_carrier_became_successor")
        and not _collapse_attempt_present(
            [packet],
            (
                "receiving_carrier_became_successor",
                "successor_standing_created",
                "receipt_creates_successor_standing",
            ),
        ),
        "receipt creates no successor standing",
        packet_non_claims.get("receiving_carrier_became_successor"),
        "RECEIPT_CREATES_SUCCESSOR_STANDING",
    )
    add(
        "carriers_are_not_merged",
        not _claim_true(packet_non_claims, "carrier_merge_performed")
        and not (bool(source_id) and bool(receiving_id) and source_id == receiving_id)
        and not _collapse_attempt_present(
            [packet],
            ("carrier_merge_performed", "carriers_merged", "source_receiving_carrier_merged"),
        ),
        "source and receiving carriers remain distinct",
        {
            "source_carrier_id": source_id,
            "receiving_carrier_id": receiving_id,
            "carrier_merge_performed": packet_non_claims.get("carrier_merge_performed"),
        },
        "RECEIPT_MERGES_CARRIERS",
    )
    add(
        "local_copy_is_not_currentness",
        not _claim_true(packet_non_claims, "local_copy_currentness")
        and not _claim_true(packet_non_claims, "latest_file_currentness")
        and not _claim_true(packet_non_claims, "recency_fraud")
        and not _collapse_attempt_present(
            [packet],
            (
                "local_copy_currentness",
                "latest_file_currentness",
                "latest_local_copy_current",
                "recency_fraud",
            ),
        ),
        "latest local copy is not treated as current",
        {
            "local_copy_currentness": packet_non_claims.get("local_copy_currentness"),
            "latest_file_currentness": packet_non_claims.get("latest_file_currentness"),
            "recency_fraud": packet_non_claims.get("recency_fraud"),
        },
        "RECEIPT_TREATS_LOCAL_COPY_AS_CURRENT",
    )
    add(
        "receipt_does_not_mutate_carried_surface",
        not _claim_true(packet_non_claims, "mutation_performed")
        and not _collapse_attempt_present(
            [packet],
            ("mutation_performed", "carried_surface_mutated", "receipt_mutates_carried_surface"),
        ),
        "receipt performs no mutation",
        packet_non_claims.get("mutation_performed"),
        "RECEIPT_MUTATES_CARRIED_SURFACE",
    )
    add(
        "source_body_is_not_replayed",
        not _claim_true(packet_non_claims, "source_body_replayed")
        and not _claim_true(packet_non_claims, "replay_performed")
        and not _collapse_attempt_present(
            [packet],
            ("source_body_replayed", "replay_performed", "receipt_replays_source_body"),
        ),
        "receipt does not replay source body",
        {
            "source_body_replayed": packet_non_claims.get("source_body_replayed"),
            "replay_performed": packet_non_claims.get("replay_performed"),
        },
        "RECEIPT_REPLAYS_SOURCE_BODY",
    )
    add(
        "upstream_mechanisms_are_not_run",
        not _claim_true(packet_non_claims, "upstream_mechanisms_run")
        and not _collapse_attempt_present(
            [packet],
            ("upstream_mechanisms_run", "receipt_runs_upstream_mechanisms"),
        ),
        "receipt runs no upstream mechanisms",
        packet_non_claims.get("upstream_mechanisms_run"),
        "RECEIPT_RUNS_UPSTREAM_MECHANISMS",
    )
    add(
        "continuation_is_not_authorized",
        not _claim_true(packet_non_claims, "continuation_authorized")
        and not _collapse_attempt_present(
            [packet],
            (
                "continuation_authorized",
                "follow_on_work_authorized",
                "follow_on_steps_authorized",
                "receipt_authorizes_continuation",
            ),
        ),
        "receipt authorizes no continuation",
        packet_non_claims.get("continuation_authorized"),
        "RECEIPT_AUTHORIZES_CONTINUATION",
    )
    add(
        "carried_surface_is_not_signal_by_default",
        not _claim_true(packet_non_claims, "carried_surface_became_signal_by_default")
        and not _collapse_attempt_present(
            [packet],
            (
                "carried_surface_became_signal_by_default",
                "signal_created_by_default",
                "receipt_creates_signal_by_default",
            ),
        ),
        "receipt creates no signal by default",
        packet_non_claims.get("carried_surface_became_signal_by_default"),
        "RECEIPT_CREATES_SIGNAL_BY_DEFAULT",
    )
    add(
        "receipt_does_not_establish_presence",
        not _claim_true(packet_non_claims, "presence_established")
        and not _collapse_attempt_present([packet], ("presence_established",)),
        "receipt establishes no presence",
        packet_non_claims.get("presence_established"),
        "RECEIPT_ESTABLISHES_PRESENCE",
    )
    add(
        "receipt_does_not_establish_threshold",
        not _claim_true(packet_non_claims, "threshold_met")
        and not _collapse_attempt_present([packet], ("threshold_met",)),
        "receipt establishes no threshold",
        packet_non_claims.get("threshold_met"),
        "RECEIPT_ESTABLISHES_THRESHOLD",
    )
    add(
        "receipt_does_not_create_truth",
        not _claim_true(packet_non_claims, "truth_created")
        and not _collapse_attempt_present([packet], ("truth_created",)),
        "receipt creates no truth",
        packet_non_claims.get("truth_created"),
        "RECEIPT_CREATES_TRUTH",
    )
    add(
        "receipt_does_not_authorize_action",
        not _claim_true(packet_non_claims, "action_authorized")
        and not _collapse_attempt_present([packet], ("action_authorized",)),
        "receipt authorizes no action",
        packet_non_claims.get("action_authorized"),
        "RECEIPT_AUTHORIZES_ACTION",
    )
    add(
        "receipt_does_not_create_consequence",
        not _claim_true(packet_non_claims, "consequence_created")
        and not _collapse_attempt_present([packet], ("consequence_created",)),
        "receipt creates no consequence",
        packet_non_claims.get("consequence_created"),
        "RECEIPT_CREATES_CONSEQUENCE",
    )
    add(
        "multi_carrier_law_is_not_created",
        not _claim_true(packet_non_claims, "multi_carrier_law_created"),
        "receipt creates no multi-carrier law",
        packet_non_claims.get("multi_carrier_law_created"),
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    add(
        "distributed_standing_is_not_created",
        not _claim_true(packet_non_claims, "distributed_standing_created"),
        "receipt creates no distributed standing",
        packet_non_claims.get("distributed_standing_created"),
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    add(
        "mutation_replay_merge_remain_false",
        not _claim_true(packet_non_claims, "mutation_performed")
        and not _claim_true(packet_non_claims, "replay_performed")
        and not _claim_true(packet_non_claims, "merge_performed"),
        "mutation, replay, and merge remain false",
        {
            "mutation_performed": packet_non_claims.get("mutation_performed"),
            "replay_performed": packet_non_claims.get("replay_performed"),
            "merge_performed": packet_non_claims.get("merge_performed"),
        },
        "RECEIPT_MUTATES_CARRIED_SURFACE",
    )
    add(
        "byte_transfer_is_not_treated_as_lawful_receipt",
        not _collapse_attempt_present(
            [packet],
            (
                "byte_transfer_treated_as_lawful_receipt",
                "byte_transfer_mistaken_for_receipt",
                "passive_storage_only",
                "bytes_only_receipt",
            ),
        ),
        "receipt is explicit lawful receipt, not byte transfer alone",
        False,
        "BYTE_TRANSFER_MISTAKEN_FOR_RECEIPT",
    )

    missing_or_flipped = [
        key for key, expected in REQUIRED_NON_CLAIMS.items()
        if packet_non_claims.get(key) is not expected
    ]
    add(
        "required_non_claims_remain_false",
        not missing_or_flipped,
        "all required packet non-claims are present and false",
        missing_or_flipped,
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    return checks


def _evaluate_integrity(
    integrity: Mapping[str, Any],
    declared_surface: Mapping[str, Any],
    supplied_surface: Mapping[str, Any],
    carried_surface_path: Path | None,
    carried_surface_bytes: bytes | None,
) -> dict[str, Any]:
    declared_hash = _first_text(integrity, ("hash", "sha256", "digest"))
    algorithm = (_first_text(integrity, ("hash_algorithm", "algorithm")) or "sha256").lower()
    declared_length = _first_int(integrity, ("byte_length", "bytes", "length"))
    integrity_required_value = integrity.get("integrity_required")
    integrity_required = integrity_required_value is True
    integrity_not_required = (
        integrity.get("integrity_not_required") is True
        or integrity_required_value is False
    )
    has_evidence = bool(
        declared_hash
        or declared_length is not None
        or integrity.get("created_exported_at")
        or integrity.get("exported_at")
    )

    bytes_to_check = carried_surface_bytes
    checked_source: str | None = None
    if bytes_to_check is not None:
        checked_source = str(carried_surface_path) if carried_surface_path else "supplied_mapping"
    elif supplied_surface:
        bytes_to_check = _canonical_json_bytes(supplied_surface)
        checked_source = "supplied_surface_mapping_canonical_json"
    else:
        declared_path = declared_surface.get("surface_path") or declared_surface.get("path")
        if declared_path:
            possible_path = Path(str(declared_path))
            if possible_path.exists() and possible_path.is_file():
                try:
                    bytes_to_check = possible_path.read_bytes()
                    checked_source = str(possible_path)
                except OSError:
                    bytes_to_check = None

    computed_hash: str | None = None
    hash_matches: bool | None = None
    integrity_checked = False
    if declared_hash and bytes_to_check is not None and algorithm == "sha256":
        computed_hash = hashlib.sha256(bytes_to_check).hexdigest()
        hash_matches = computed_hash == declared_hash
        integrity_checked = True
    elif declared_hash and bytes_to_check is not None and algorithm != "sha256":
        hash_matches = False
        integrity_checked = True

    actual_length = len(bytes_to_check) if bytes_to_check is not None else None
    byte_length_matches: bool | None = None
    if declared_length is not None and actual_length is not None:
        byte_length_matches = declared_length == actual_length

    hash_check_passed = (
        (hash_matches is not False)
        and (byte_length_matches is not False)
    )
    integrity_basis_satisfied = has_evidence or integrity_not_required

    return {
        "integrity_required": integrity_required,
        "integrity_not_required": integrity_not_required,
        "integrity_basis_satisfied": bool(integrity_basis_satisfied),
        "integrity_evidence_preserved": bool(has_evidence),
        "integrity_checked": bool(integrity_checked),
        "checked_source": checked_source,
        "hash_algorithm": algorithm if declared_hash else integrity.get("hash_algorithm"),
        "declared_hash": declared_hash,
        "computed_hash": computed_hash,
        "hash_matches": hash_matches,
        "hash_check_passed": bool(hash_check_passed),
        "declared_byte_length": declared_length,
        "actual_byte_length": actual_length,
        "byte_length_matches": byte_length_matches,
        "created_exported_at": integrity.get("created_exported_at")
        or integrity.get("exported_at"),
    }


def _build_selected_basis(
    source_carrier: Mapping[str, Any],
    receiving_carrier: Mapping[str, Any],
    declared_surface: Mapping[str, Any],
    supplied_surface: Mapping[str, Any],
    carried_surface_path: Path | None,
) -> dict[str, dict[str, Any]]:
    source_id = _carrier_identity(source_carrier)
    receiving_id = _carrier_identity(receiving_carrier)
    surface_id = _extract_surface_id(declared_surface)
    surface_path = (
        declared_surface.get("surface_path")
        or declared_surface.get("path")
        or (str(carried_surface_path) if carried_surface_path else None)
    )
    separate_id = _extract_surface_id(supplied_surface)
    separate_outcome = _extract_surface_outcome(supplied_surface)

    return {
        "source_carrier_basis": {
            "source_carrier_id": source_id,
            "source_carrier_label": source_carrier.get("carrier_label")
            or source_carrier.get("label"),
            "source_carrier_role": _carrier_role(source_carrier),
            "local_path_context": source_carrier.get("local_path_context"),
            "source_carrier_role_limited_to_this_packet": _source_role_is_limited(
                source_carrier
            ),
            "universal_source_authority_created": False,
        },
        "receiving_carrier_basis": {
            "receiving_carrier_id": receiving_id,
            "receiving_carrier_label": receiving_carrier.get("carrier_label")
            or receiving_carrier.get("label"),
            "receiving_carrier_role": _carrier_role(receiving_carrier),
            "receiving_carrier_declared": bool(receiving_id),
            "receiving_carrier_does_not_become_source_current_or_authority": (
                _receiving_role_is_bounded(receiving_carrier)
            ),
        },
        "carried_surface_basis": {
            "carried_surface_id": surface_id,
            "carried_surface_path": surface_path,
            "carried_surface_filename": declared_surface.get("surface_filename")
            or (Path(str(surface_path)).name if surface_path else None),
            "carried_surface_outcome": _extract_surface_outcome(declared_surface),
            "carried_surface_type": _extract_surface_type(declared_surface),
            "selected_upstream_basis": declared_surface.get("selected_upstream_basis"),
            "source_downstream_posture": declared_surface.get("source_downstream_posture"),
            "separately_supplied_surface": bool(supplied_surface),
            "separately_supplied_surface_path": str(carried_surface_path)
            if carried_surface_path
            else None,
            "separately_supplied_surface_id": separate_id,
            "separately_supplied_surface_outcome": separate_outcome,
            "separately_supplied_surface_matches_packet_basis": (
                _supplied_surface_matches_packet(declared_surface, supplied_surface)
            ),
        },
    }


def _receipt_statement(
    received: bool,
    selected: Mapping[str, Mapping[str, Any]],
    integrity_check: Mapping[str, Any],
    block_code: str | None,
) -> dict[str, Any]:
    source_basis = selected["source_carrier_basis"]
    receiving_basis = selected["receiving_carrier_basis"]
    surface_basis = selected["carried_surface_basis"]
    return {
        "carried_surface_received": bool(received),
        "source_carrier_preserved": bool(received and source_basis.get("source_carrier_id")),
        "receiving_carrier_declared": bool(receiving_basis.get("receiving_carrier_id")),
        "carried_surface_identity_preserved": bool(surface_basis.get("carried_surface_id")),
        "carried_surface_outcome_preserved": bool(
            surface_basis.get("carried_surface_outcome")
        ),
        "integrity_checked": bool(integrity_check.get("integrity_checked")),
        "integrity_evidence_preserved": bool(
            integrity_check.get("integrity_evidence_preserved")
        ),
        "received_as_carried_evidence": bool(received),
        "receiving_carrier_became_source": False,
        "receiving_carrier_became_current": False,
        "receiving_carrier_became_authority": False,
        "receiving_carrier_became_successor": False,
        "carried_surface_became_source": False,
        "carried_surface_became_currentness": False,
        "carried_surface_became_permission": False,
        "receipt_created_signal_by_default": False,
        "receipt_established_presence": False,
        "receipt_established_threshold": False,
        "receipt_created_truth": False,
        "receipt_authorized_action": False,
        "receipt_created_consequence": False,
        "receipt_authorized_continuation": False,
        "multi_carrier_law_created": False,
        "distributed_standing_created": False,
        "blocked_receipt_does_not_invalidate_carried_surface": bool(block_code),
        "block_code": block_code,
    }


def _receipt_non_meaning() -> dict[str, bool]:
    return {
        "does_not_mean_byte_transfer_alone": True,
        "does_not_replace_source": True,
        "does_not_create_receiving_carrier_sourcehood": True,
        "does_not_create_receiving_carrier_currentness": True,
        "does_not_create_receiving_carrier_authority": True,
        "does_not_create_receiving_carrier_permission": True,
        "does_not_create_successor_standing": True,
        "does_not_form_body": True,
        "does_not_merge_carriers": True,
        "does_not_create_local_copy_currentness": True,
        "does_not_authorize_execution": True,
        "does_not_authorize_continuation": True,
        "does_not_create_signal_by_default": True,
        "does_not_establish_presence": True,
        "does_not_establish_threshold": True,
        "does_not_create_truth": True,
        "does_not_authorize_action": True,
        "does_not_create_consequence": True,
        "does_not_transfer_full_repo": True,
        "does_not_synchronize_repo": True,
        "does_not_create_distributed_standing": True,
        "does_not_create_multi_carrier_law": True,
    }


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_surfaces": [
            "portable receipt implementation refinement",
            "cross-carrier receipt test on physical second carrier",
            "multi-carrier relation law",
            "distributed standing",
            "persistence/registry law",
            "presence law",
            "threshold law",
            "truth law",
            "action/consequence law",
            "generalized vessel relation lifecycle",
            "body relevance medium",
            "signal series or accumulation logic",
            "future self-orientation successor only if separately justified",
        ],
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }


def _read_json_mapping(
    path: Path | str,
    *,
    unreadable_code: str,
    malformed_code: str,
) -> dict[str, Any]:
    selected_path = Path(path)
    try:
        raw = selected_path.read_bytes()
    except OSError as exc:
        raise CrossCarrierSurfaceReceiptBoundaryError(
            unreadable_code,
            f"{BLOCK_REASONS[unreadable_code]} path={selected_path} detail={exc}",
        ) from exc
    return _loads_json_mapping(raw, malformed_code=malformed_code, path=selected_path)


def _loads_json_mapping(
    raw: bytes,
    *,
    malformed_code: str,
    path: Path | None,
) -> dict[str, Any]:
    try:
        loaded = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CrossCarrierSurfaceReceiptBoundaryError(
            malformed_code,
            f"{BLOCK_REASONS[malformed_code]} path={path} detail={exc}",
        ) from exc
    if not isinstance(loaded, dict):
        raise CrossCarrierSurfaceReceiptBoundaryError(
            malformed_code,
            f"{BLOCK_REASONS[malformed_code]} path={path} expected object",
        )
    return loaded


def _check(
    check_name: str,
    passed: bool,
    expected_posture: str,
    actual_posture: Any,
    block_code: str,
) -> dict[str, Any]:
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": expected_posture,
        "actual_posture": copy.deepcopy(actual_posture),
        "block_code": None if passed else block_code,
    }


def _first_failed_check(checks: list[dict[str, Any]]) -> dict[str, Any] | None:
    return next((check for check in checks if check.get("passed") is False), None)


def _block_reason(
    block_code: str | None,
    failed_check: Mapping[str, Any] | None = None,
) -> str | None:
    if block_code is None:
        return None
    reason = BLOCK_REASONS.get(block_code, "The receipt request was blocked.")
    if failed_check:
        return f"{reason} failed check: {failed_check.get('check_name')}"
    return reason


def _result_id(selected: Mapping[str, Mapping[str, Any]]) -> str:
    surface_id = selected.get("carried_surface_basis", {}).get("carried_surface_id")
    return f"{_slug(str(surface_id or 'carried_surface'))}__cross_carrier_surface_receipt_result"


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _as_mapping(value: Any) -> dict[str, Any]:
    if isinstance(value, Mapping):
        return copy.deepcopy(dict(value))
    return {}


def _mapping_list(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        return []
    return [copy.deepcopy(dict(item)) for item in value if isinstance(item, Mapping)]


def _first_text(mapping: Mapping[str, Any], keys: tuple[str, ...]) -> str | None:
    for key in keys:
        value = mapping.get(key)
        if value is not None and str(value).strip():
            return str(value)
    return None


def _first_int(mapping: Mapping[str, Any], keys: tuple[str, ...]) -> int | None:
    for key in keys:
        value = mapping.get(key)
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.strip().isdigit():
            return int(value.strip())
    return None


def _carrier_identity(carrier: Mapping[str, Any]) -> str | None:
    return _first_text(carrier, ("carrier_id", "carrier_label", "id", "label"))


def _carrier_role(carrier: Mapping[str, Any]) -> str | None:
    return _first_text(carrier, ("carrier_role", "role"))


def _source_role_is_limited(source_carrier: Mapping[str, Any]) -> bool:
    role = (_carrier_role(source_carrier) or "").lower()
    explicit_non_claim = source_carrier.get(
        "source_carrier_role_does_not_create_universal_source_authority"
    )
    return (
        bool(_carrier_identity(source_carrier))
        and "source" in role
        and (
            "packet" in role
            or "only" in role
            or explicit_non_claim is True
        )
    )


def _receiving_role_is_bounded(receiving_carrier: Mapping[str, Any]) -> bool:
    role = (_carrier_role(receiving_carrier) or "").lower()
    explicit_non_claim = receiving_carrier.get(
        "receiving_carrier_does_not_become_source_current_or_authority"
    )
    return (
        bool(_carrier_identity(receiving_carrier))
        and "receiv" in role
        and explicit_non_claim is True
    )


def _extract_surface_id(surface: Mapping[str, Any]) -> str | None:
    direct = _first_text(surface, ("surface_id", "result_id", "id", "artifact_id"))
    if direct:
        return direct
    for parent, child in SURFACE_ID_METADATA_PATHS:
        value = _nested(surface, parent, child)
        if value:
            return str(value)
    return None


def _extract_surface_outcome(surface: Mapping[str, Any]) -> str | None:
    return _first_text(surface, ("surface_outcome", "outcome", "status", "result_outcome"))


def _extract_surface_type(surface: Mapping[str, Any]) -> str | None:
    direct = _first_text(surface, ("surface_type", "result_type", "type", "artifact_type"))
    if direct:
        return direct
    for parent, child in SURFACE_TYPE_METADATA_PATHS:
        value = _nested(surface, parent, child)
        if value:
            return str(value)
    return None


def _extract_selected_upstream_basis(surface: Mapping[str, Any]) -> Any:
    for key in (
        "selected_upstream_basis",
        "selected_source_basis",
        "self_orientation_basis",
        "current_body_conformance_basis",
        "selected_orientation_inputs",
    ):
        if key in surface:
            return copy.deepcopy(surface[key])
    return None


def _supplied_surface_matches_packet(
    declared_surface: Mapping[str, Any],
    supplied_surface: Mapping[str, Any],
) -> bool:
    if not supplied_surface:
        return True
    declared_id = _extract_surface_id(declared_surface)
    declared_outcome = _extract_surface_outcome(declared_surface)
    supplied_id = _extract_surface_id(supplied_surface)
    supplied_outcome = _extract_surface_outcome(supplied_surface)
    id_matches = not supplied_id or not declared_id or supplied_id == declared_id
    outcome_matches = (
        not supplied_outcome
        or not declared_outcome
        or supplied_outcome == declared_outcome
    )
    return bool(id_matches and outcome_matches)


def _supplied_surface_match_posture(
    declared_surface: Mapping[str, Any],
    supplied_surface: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "packet_surface_id": _extract_surface_id(declared_surface),
        "supplied_surface_id": _extract_surface_id(supplied_surface),
        "packet_surface_outcome": _extract_surface_outcome(declared_surface),
        "supplied_surface_outcome": _extract_surface_outcome(supplied_surface),
    }


def _nested(mapping: Mapping[str, Any], *keys: str) -> Any:
    current: Any = mapping
    for key in keys:
        if not isinstance(current, Mapping):
            return None
        current = current.get(key)
    return current


def _claim_true(claims: Mapping[str, Any], key: str) -> bool:
    return claims.get(key) is True


def _collapse_attempt_present(values: list[Any], markers: tuple[str, ...]) -> bool:
    for value in values:
        if _contains_true_marker(value, markers):
            return True
    return False


def _contains_true_marker(value: Any, markers: tuple[str, ...]) -> bool:
    if isinstance(value, Mapping):
        for key, nested_value in value.items():
            key_text = str(key).lower()
            if (
                any(marker in key_text for marker in markers)
                and not _is_negating_key(key_text)
                and nested_value is True
            ):
                return True
            if _contains_true_marker(nested_value, markers):
                return True
    elif isinstance(value, list):
        return any(_contains_true_marker(item, markers) for item in value)
    return False


def _is_negating_key(key: str) -> bool:
    return any(fragment in key for fragment in NEGATING_KEY_FRAGMENTS)


def _canonical_json_bytes(value: Mapping[str, Any]) -> bytes:
    return json.dumps(dict(value), sort_keys=True, separators=(",", ":")).encode("utf-8")


def _key_non_claims(non_claims: Mapping[str, Any]) -> dict[str, Any]:
    keys = (
        "authority_created",
        "permission_created",
        "currentness_created",
        "source_replaced",
        "receiving_carrier_became_source",
        "receiving_carrier_became_current",
        "receiving_carrier_became_authority",
        "receiving_carrier_became_successor",
        "carried_surface_became_source",
        "carried_surface_became_currentness",
        "carried_surface_became_permission",
        "carried_surface_became_signal_by_default",
        "presence_established",
        "threshold_met",
        "truth_created",
        "action_authorized",
        "consequence_created",
        "carrier_merge_performed",
        "local_copy_currentness",
        "source_body_replayed",
        "upstream_mechanisms_run",
        "continuation_authorized",
        "multi_carrier_law_created",
        "distributed_standing_created",
        "latest_file_currentness",
        "recency_fraud",
        "mutation_performed",
        "replay_performed",
        "merge_performed",
    )
    return {key: non_claims.get(key) for key in keys}


def _slug(value: str) -> str:
    text = re.sub(r"[^A-Za-z0-9_.-]+", "_", value.strip())
    return text[:180] or "carried_surface"


def _non_overwriting_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    index = 1
    while True:
        candidate = parent / f"{stem}_{index:03d}{suffix}"
        if not candidate.exists():
            return candidate
        index += 1
