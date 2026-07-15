"""Resolve one bounded current self-orientation from standing artifacts.

This module derives one internal self-orientation result from one selected
v0-min coexistence body-pass artifact and the standing artifacts it names.

It recognizes current, governing/effective, continuity, derivative, operator-
facing, open, blocked/refused, and touch/admissibility posture without
replaying the host, merging preserved runs, widening source scope, or treating
derivative/operator artifacts as source authority.

The shell/local resolver remains the law. Self-orientation is a bounded
internal recognition surface only.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

import build_current_integrity_host_v0_min_coexistence_governing_packet as governing_resolver
import build_integrity_host_v0_min_coexistence_preserved_run_status_packet as status_resolver
import build_integrity_host_v0_min_coexistence_run_family_packet as family_resolver
import openai_api_vessel__bounded_current_state_read_v3 as vessel_resolver
import resolve_current_integrity_host_v0_min_coexistence_execution_authority as authority_resolver
import resolve_integrity_host_v0_min_coexistence_continuity_memory_seam as seam_resolver
import resolve_integrity_host_v0_min_coexistence_continuity_transfer_receipt as receipt_resolver
import resolve_integrity_host_v0_min_coexistence_continuity_transfer_unit as transfer_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_admissibility_and_touch_permission as touch_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_answer_surface as answer_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_query as query_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_what_remains_open as open_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_what_stands_now as stand_resolver
import resolve_integrity_host_v0_min_coexistence_received_derivative_action_permission as action_resolver
import resolve_integrity_host_v0_min_coexistence_received_derivative_participation as participation_resolver
import resolve_operator_facing_terminal_brief__bounded_current_state_read as brief_resolver
import run_integrity_host_v0_min_coexistence_v0_body_pass as body_pass_resolver


class CurrentSelfOrientationError(RuntimeError):
    """Raised for malformed selected inputs, references, or correspondence."""

    def __init__(self, message: str, block_code: str | None = None) -> None:
        super().__init__(message)
        self.block_code = block_code


EXECUTION_AUTHORITY_ROOT = authority_resolver.RESOLUTION_OUTPUT_ROOT
RUN_FAMILY_PACKET_ROOT = family_resolver.RUN_FAMILY_PACKET_ROOT
PRESERVED_RUN_STATUS_PACKET_ROOT = status_resolver.PRESERVED_RUN_STATUS_PACKET_ROOT
CURRENT_GOVERNING_PACKET_ROOT = governing_resolver.CURRENT_GOVERNING_PACKET_ROOT
CURRENT_STATE_ANSWER_SURFACE_ROOT = answer_resolver.CURRENT_STATE_ANSWER_SURFACE_ROOT
CURRENT_STATE_QUERY_ROOT = query_resolver.CURRENT_STATE_QUERY_ROOT
CURRENT_STATE_WHAT_STANDS_NOW_ROOT = stand_resolver.CURRENT_STATE_WHAT_STANDS_NOW_ROOT
CURRENT_STATE_WHAT_REMAINS_OPEN_ROOT = open_resolver.CURRENT_STATE_WHAT_REMAINS_OPEN_ROOT
CURRENT_STATE_TOUCH_PERMISSION_ROOT = touch_resolver.CURRENT_STATE_TOUCH_PERMISSION_ROOT
CONTINUITY_TRANSFER_UNIT_ROOT = transfer_resolver.CONTINUITY_TRANSFER_UNIT_ROOT
CONTINUITY_TRANSFER_RECEIPT_ROOT = receipt_resolver.CONTINUITY_TRANSFER_RECEIPT_ROOT
RECEIVED_DERIVATIVE_PARTICIPATION_ROOT = participation_resolver.RECEIVED_DERIVATIVE_PARTICIPATION_ROOT
RECEIVED_DERIVATIVE_ACTION_PERMISSION_ROOT = action_resolver.RECEIVED_DERIVATIVE_ACTION_PERMISSION_ROOT
CONTINUITY_MEMORY_SEAM_ROOT = seam_resolver.CONTINUITY_MEMORY_SEAM_ROOT
V0_BODY_PASS_ROOT = body_pass_resolver.V0_BODY_PASS_ROOT
OPENAI_API_DERIVATIVE_VESSEL_V3_ROOT = vessel_resolver.OPENAI_API_DERIVATIVE_VESSEL_V3_ROOT
OPERATOR_TERMINAL_BRIEF_ROOT = brief_resolver.OPERATOR_TERMINAL_BRIEF_ROOT
CURRENT_SELF_ORIENTATION_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_current_self_orientation"
)

CANONICAL_CORE_EXECUTION_FILE = body_pass_resolver.CANONICAL_CORE_EXECUTION_FILE

RESOLVER_MODULE = "resolve_current_self_orientation"
CURRENT_SELF_ORIENTATION_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_SELF_ORIENTATION_RESULT"
)
CURRENT_SELF_ORIENTATION_RESULT_VERSION = "0.1.0"
DEFAULT_RESULT_STEM = "current_self_orientation_result"

OUTCOME_SELF_ORIENTED = "SELF_ORIENTED"
OUTCOME_BLOCKED = "BLOCKED"

BLOCK_REASONS = {
    "NO_SELF_ORIENTATION_SOURCE_BASIS": (
        "No bounded self-orientation source basis is available."
    ),
    "REQUIRED_SOURCE_ARTIFACT_UNREADABLE": (
        "A required selected source artifact could not be read."
    ),
    "SOURCE_ARTIFACT_MALFORMED": "A selected source artifact is malformed.",
    "CURRENT_EFFECTIVE_BASIS_ABSENT_OR_AMBIGUOUS": (
        "The current/effective basis is absent or ambiguous."
    ),
    "CURRENT_STATE_SURFACE_ABSENT_WHERE_REQUIRED": (
        "A required current-state surface is absent for the selected basis."
    ),
    "DERIVATIVE_SURFACE_SOURCE_BASIS_MISSING": (
        "A derivative surface does not preserve the required source basis."
    ),
    "OPERATOR_SURFACE_DERIVATIVE_OR_SOURCE_BASIS_MISSING": (
        "An operator-facing surface does not preserve the required derivative/source basis."
    ),
    "LATEST_FILE_RECENCY_REFUSED": (
        "Currentness inferred by latest-file recency alone is refused."
    ),
    "DERIVATIVE_TREATED_AS_SOURCE_AUTHORITY": (
        "A derivative surface was treated as source authority."
    ),
    "OPERATOR_SURFACE_TREATED_AS_SOURCE_AUTHORITY": (
        "An operator-facing surface was treated as source authority."
    ),
    "OPEN_SURFACE_TREATED_AS_COMPLETED": (
        "An open surface was treated as completed."
    ),
    "BLOCKED_OR_REFUSED_SURFACE_HIDDEN": (
        "A blocked or refused surface was hidden."
    ),
    "NON_CLAIM_MISSING_OR_FLIPPED": (
        "A carried non-claim is missing or no longer false."
    ),
    "CORRESPONDENCE_CHECK_FAILED": (
        "A bounded correspondence/proportion check failed."
    ),
    "OVER_MIRRORING_REFUSED": (
        "Self-orientation attempted to become a whole-body replacement."
    ),
    "UNDER_MIRRORING_REFUSED": (
        "Self-orientation omitted required standing posture."
    ),
    "MULTIPLE_CANDIDATE_CURRENT_SURFACES_CONFLICT_UNRESOLVED": (
        "Multiple candidate current surfaces conflict without bounded resolution."
    ),
    "EXTERNAL_READER_ORIENTATION_ATTEMPTED": (
        "External-reader orientation is outside the bounded self-orientation surface."
    ),
    "HAND_MAINTAINED_SUMMARY_SEAM_ATTEMPTED": (
        "A hand-maintained summary seam is outside the bounded self-orientation surface."
    ),
}

NON_CLAIM_DEFAULTS = {
    **family_resolver.NON_CLAIM_DEFAULTS,
    **status_resolver.NON_CLAIM_DEFAULTS,
    **governing_resolver.NON_CLAIM_DEFAULTS,
    **answer_resolver.NON_CLAIM_DEFAULTS,
    **query_resolver.NON_CLAIM_DEFAULTS,
    **stand_resolver.NON_CLAIM_DEFAULTS,
    **open_resolver.NON_CLAIM_DEFAULTS,
    **touch_resolver.NON_CLAIM_DEFAULTS,
    **transfer_resolver.NON_CLAIM_DEFAULTS,
    **receipt_resolver.NON_CLAIM_DEFAULTS,
    **participation_resolver.NON_CLAIM_DEFAULTS,
    **action_resolver.NON_CLAIM_DEFAULTS,
    **seam_resolver.NON_CLAIM_DEFAULTS,
    **body_pass_resolver.NON_CLAIM_DEFAULTS,
    **vessel_resolver.NON_CLAIM_DEFAULTS,
    **brief_resolver.NON_CLAIM_DEFAULTS,
}

BLOCKED_OR_REFUSED_OUTCOMES = frozenset({"BLOCKED", "REFUSED"})

CANONICAL_EFFECTIVE_REFERENCE_ALIASES = {
    "effective_authority_artifact_path": (
        "effective_authority_artifact_path",
        "current_authority_artifact_path",
    ),
    "effective_family_packet_path": (
        "effective_family_packet_path",
        "current_family_packet_path",
    ),
    "effective_status_packet_path": (
        "effective_status_packet_path",
        "current_status_packet_path",
    ),
    "effective_current_governing_packet_path": (
        "effective_current_governing_packet_path",
        "current_governing_packet_path",
    ),
    "effective_source_run_path": (
        "effective_source_run_path",
        "current_governing_source_run_path",
    ),
    "effective_ingress_run_path": (
        "effective_ingress_run_path",
        "current_governing_ingress_run_path",
    ),
}


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _repo_path(path: Path | str) -> Path:
    candidate = Path(path)
    return candidate if candidate.is_absolute() else _repo_root() / candidate


def _display_path(path: Path | str | None) -> str | None:
    if path is None:
        return None
    if path == "provided_mapping":
        return "provided_mapping"
    try:
        resolved = _repo_path(path)
    except TypeError:
        return str(path)
    try:
        return str(resolved.relative_to(_repo_root()))
    except ValueError:
        return str(resolved)


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _safe_filename_part(value: Any) -> str:
    if not isinstance(value, str) or not value:
        value = "no_selected_body_pass_result"
    compact = re.sub(r"[^A-Za-z0-9_.-]+", "_", value).strip("._")
    return compact[:160] or "no_selected_body_pass_result"


def _string_or_none(value: Any) -> str | None:
    if not isinstance(value, str):
        return None
    stripped = value.strip()
    return stripped or None


def _string_required(value: Any, context: str, block_code: str) -> str:
    normalized = _string_or_none(value)
    if normalized is None:
        raise CurrentSelfOrientationError(f"{context} must be a non-empty string", block_code)
    return normalized


def _require_mapping(value: Any, context: str, block_code: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise CurrentSelfOrientationError(f"{context} must be an object", block_code)
    return value


def _normalized_path_string(value: Any) -> str | None:
    if not isinstance(value, str) or not value.strip():
        return None
    candidate = Path(value)
    if not candidate.is_absolute():
        candidate = _repo_root() / candidate
    try:
        return str(candidate.resolve(strict=False))
    except OSError:
        return str(candidate)


def _paths_equal(left: Any, right: Any) -> bool:
    normalized_left = _normalized_path_string(left)
    normalized_right = _normalized_path_string(right)
    return normalized_left is not None and normalized_left == normalized_right


def _read_json_file(
    path: Path | str,
    *,
    context: str,
    missing_code: str,
    unreadable_code: str,
    malformed_code: str,
) -> dict[str, Any]:
    resolved = _repo_path(path)
    try:
        with resolved.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
    except FileNotFoundError as exc:
        raise CurrentSelfOrientationError(
            f"{context} not found: {resolved}",
            missing_code,
        ) from exc
    except OSError as exc:
        raise CurrentSelfOrientationError(
            f"{context} is unreadable: {resolved}",
            unreadable_code,
        ) from exc
    except json.JSONDecodeError as exc:
        raise CurrentSelfOrientationError(
            f"{context} is malformed JSON: {resolved}",
            malformed_code,
        ) from exc
    if not isinstance(value, dict):
        raise CurrentSelfOrientationError(
            f"{context} must be a JSON object: {resolved}",
            malformed_code,
        )
    return value


def _discover_artifacts(root: Path | str, context: str) -> list[Path]:
    resolved = _repo_path(root)
    if not resolved.exists():
        return []
    if not resolved.is_dir():
        raise CurrentSelfOrientationError(
            f"{context} root is not a directory: {resolved}",
            "REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
        )
    try:
        return sorted(path for path in resolved.glob("*.json") if path.is_file())
    except OSError as exc:
        raise CurrentSelfOrientationError(
            f"{context} root is unreadable: {resolved}",
            "REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
        ) from exc


def _check(
    name: str,
    passed: bool,
    expected: Any | None = None,
    actual: Any | None = None,
    block_code: str | None = None,
) -> dict[str, Any]:
    result: dict[str, Any] = {"check_name": name, "passed": bool(passed)}
    if expected is not None:
        result["expected_posture"] = expected
    if actual is not None:
        result["actual_posture"] = actual
    if block_code is not None:
        result["block_code"] = block_code
    return result


def _count_checks(checks: Sequence[Mapping[str, Any]]) -> tuple[int, int]:
    return (
        sum(1 for check in checks if check.get("passed") is True),
        sum(1 for check in checks if check.get("passed") is not True),
    )


def _first_failed(checks: Sequence[Mapping[str, Any]]) -> Mapping[str, Any] | None:
    return next((check for check in checks if check.get("passed") is not True), None)


def _block_reason(block_code: str, detail: str | None = None) -> str:
    base = BLOCK_REASONS.get(block_code, block_code.replace("_", " ").lower() + ".")
    if detail is None or not detail.strip():
        return base
    detail_text = detail.strip()
    if detail_text == base:
        return base
    return f"{base} Detail: {detail_text}"


def _metadata_value(
    artifact: Mapping[str, Any],
    metadata_key: str,
    field_key: str,
) -> str | None:
    metadata = artifact.get(metadata_key)
    if not isinstance(metadata, Mapping):
        return None
    return _string_or_none(metadata.get(field_key))


def _extract_canonical_effective_references(
    mapping: Mapping[str, Any],
) -> dict[str, str | None]:
    extracted: dict[str, str | None] = {}
    for canonical_key, aliases in CANONICAL_EFFECTIVE_REFERENCE_ALIASES.items():
        extracted[canonical_key] = None
        for alias in aliases:
            value = _string_or_none(mapping.get(alias))
            if value is not None:
                extracted[canonical_key] = value
                break
    return extracted


def _effective_references_complete(
    effective_references: Mapping[str, Any],
) -> bool:
    extracted = _extract_canonical_effective_references(effective_references)
    return all(extracted.values())


def _effective_references_match(
    expected: Mapping[str, Any],
    candidate: Mapping[str, Any],
) -> bool:
    expected_refs = _extract_canonical_effective_references(expected)
    candidate_refs = _extract_canonical_effective_references(candidate)
    for key, expected_value in expected_refs.items():
        if expected_value is None:
            return False
        candidate_value = candidate_refs.get(key)
        if candidate_value is None or not _paths_equal(expected_value, candidate_value):
            return False
    return True


def _looks_like_external_reader_orientation_attempt(
    mapping: Mapping[str, Any],
) -> bool:
    suspicious_keys = {
        "external_reader_orientation",
        "onboarding_summary",
        "public_orientation",
        "repo_map",
        "readme_orientation",
    }
    return any(key in mapping for key in suspicious_keys)


def _looks_like_hand_maintained_summary_seam_attempt(
    mapping: Mapping[str, Any],
) -> bool:
    suspicious_keys = {
        "hand_maintained_summary",
        "manual_summary",
        "summary_seam",
        "static_repo_summary",
    }
    return any(key in mapping for key in suspicious_keys)


def _validate_false_non_claims(
    label: str,
    artifact: Mapping[str, Any],
    required: Mapping[str, Any],
) -> None:
    non_claims = artifact.get("non_claims")
    if not isinstance(non_claims, Mapping):
        raise CurrentSelfOrientationError(
            f"{label} non_claims must be present",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    for key in required:
        if key not in non_claims:
            raise CurrentSelfOrientationError(
                f"{label} non_claim {key} is missing",
                "NON_CLAIM_MISSING_OR_FLIPPED",
            )
        if non_claims.get(key) is not False:
            raise CurrentSelfOrientationError(
                f"{label} non_claim {key} is not false",
                "NON_CLAIM_MISSING_OR_FLIPPED",
            )


def _merge_non_claims(artifacts: Sequence[Mapping[str, Any]]) -> dict[str, bool]:
    merged = dict(NON_CLAIM_DEFAULTS)
    for artifact in artifacts:
        non_claims = artifact.get("non_claims")
        if not isinstance(non_claims, Mapping):
            continue
        for key, value in non_claims.items():
            if key not in merged:
                merged[key] = False
            if value is not False:
                raise CurrentSelfOrientationError(
                    f"carried non-claim {key} is not false",
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                )
    return merged


def _identity_dict(
    *,
    path: Path | str | None,
    result_id: str | None,
    result_type: str | None = None,
    result_family: str | None = None,
    outcome: str | None = None,
    source_surface_id: str | None = None,
    source_surface_family: str | None = None,
) -> dict[str, Any]:
    return {
        "result_path": _display_path(path),
        "result_id": result_id,
        "result_type": result_type,
        "result_family": result_family,
        "outcome": outcome,
        "source_surface_id": source_surface_id,
        "source_surface_family": source_surface_family,
    }


def _body_pass_identity(
    body_pass_result: Mapping[str, Any],
    path: Path | str | None,
) -> dict[str, Any]:
    return _identity_dict(
        path=path,
        result_id=_metadata_value(
            body_pass_result,
            "v0_body_pass_metadata",
            "v0_body_pass_result_id",
        ),
        result_type=_metadata_value(
            body_pass_result,
            "v0_body_pass_metadata",
            "v0_body_pass_result_type",
        ),
        result_family="v0_body_pass_result",
        outcome=_string_or_none(body_pass_result.get("outcome")),
    )


def _selected_result_identity(
    section: Mapping[str, Any],
    *,
    id_key: str,
    path_key: str,
    outcome_key: str,
    family_key: str | None = None,
    type_key: str | None = None,
) -> dict[str, Any]:
    return _identity_dict(
        path=_string_or_none(section.get(path_key)),
        result_id=_string_or_none(section.get(id_key)),
        result_type=_string_or_none(section.get(type_key)) if type_key else None,
        result_family=_string_or_none(section.get(family_key)) if family_key else None,
        outcome=_string_or_none(section.get(outcome_key)),
    )


def _answer_read_identity(
    answer_read_result: Mapping[str, Any],
    path: Path | str | None,
) -> dict[str, Any]:
    summary = answer_resolver.build_current_state_answer_read_summary(answer_read_result)
    return _identity_dict(
        path=path,
        result_id=_metadata_value(
            answer_read_result,
            "answer_read_metadata",
            "answer_read_result_id",
        ),
        result_type=_metadata_value(
            answer_read_result,
            "answer_read_metadata",
            "answer_read_result_type",
        ),
        result_family="current_state_answer_read_result",
        outcome=_string_or_none(answer_read_result.get("outcome")),
        source_surface_id=_string_or_none(summary.get("selected_current_state_application_id")),
    )


def _query_identity(
    query_result: Mapping[str, Any],
    path: Path | str | None,
) -> dict[str, Any]:
    summary = query_resolver.build_current_state_query_summary(query_result)
    return _identity_dict(
        path=path,
        result_id=_metadata_value(query_result, "query_metadata", "query_result_id"),
        result_type=_metadata_value(query_result, "query_metadata", "query_result_type"),
        result_family="current_state_query_result",
        outcome=_string_or_none(query_result.get("outcome")),
        source_surface_id=_string_or_none(summary.get("selected_current_state_answer_read_id")),
        source_surface_family="current_state_answer_read_result",
    )


def _what_stands_now_identity(
    stand_result: Mapping[str, Any],
    path: Path | str | None,
) -> dict[str, Any]:
    summary = stand_resolver.build_current_state_what_stands_now_summary(stand_result)
    return _identity_dict(
        path=path,
        result_id=_metadata_value(
            stand_result,
            "what_stands_now_metadata",
            "what_stands_now_result_id",
        ),
        result_type=_metadata_value(
            stand_result,
            "what_stands_now_metadata",
            "what_stands_now_result_type",
        ),
        result_family="current_state_what_stands_now_result",
        outcome=_string_or_none(stand_result.get("outcome")),
        source_surface_id=_string_or_none(summary.get("selected_current_state_answer_read_id")),
        source_surface_family="current_state_answer_read_result",
    )


def _what_remains_open_identity(
    open_result: Mapping[str, Any],
    path: Path | str | None,
) -> dict[str, Any]:
    summary = open_resolver.build_current_state_what_remains_open_summary(open_result)
    return _identity_dict(
        path=path,
        result_id=_metadata_value(
            open_result,
            "what_remains_open_metadata",
            "what_remains_open_result_id",
        ),
        result_type=_metadata_value(
            open_result,
            "what_remains_open_metadata",
            "what_remains_open_result_type",
        ),
        result_family="current_state_what_remains_open_result",
        outcome=_string_or_none(open_result.get("outcome")),
        source_surface_id=_string_or_none(summary.get("selected_current_state_answer_read_id")),
        source_surface_family="current_state_answer_read_result",
    )


def _touch_identity(
    touch_result: Mapping[str, Any],
    path: Path | str | None,
) -> dict[str, Any]:
    scope = touch_result.get("admitted_touch_scope")
    scope = scope if isinstance(scope, Mapping) else {}
    return _identity_dict(
        path=path,
        result_id=_metadata_value(
            touch_result,
            "touch_permission_metadata",
            "touch_permission_result_id",
        ),
        result_type=_metadata_value(
            touch_result,
            "touch_permission_metadata",
            "touch_permission_result_type",
        ),
        result_family="current_state_touch_permission_result",
        outcome=_string_or_none(touch_result.get("outcome")),
        source_surface_id=_string_or_none(scope.get("admitted_source_surface_id")),
        source_surface_family="current_state_what_stands_now_result",
    )


def _transfer_identity(
    transfer_result: Mapping[str, Any],
    path: Path | str | None,
) -> dict[str, Any]:
    source_surface = transfer_result.get("selected_source_surface")
    source_surface = source_surface if isinstance(source_surface, Mapping) else {}
    return _identity_dict(
        path=path,
        result_id=_metadata_value(
            transfer_result,
            "continuity_transfer_metadata",
            "continuity_transfer_result_id",
        ),
        result_type=_metadata_value(
            transfer_result,
            "continuity_transfer_metadata",
            "continuity_transfer_result_type",
        ),
        result_family="continuity_transfer_unit_result",
        outcome=_string_or_none(transfer_result.get("outcome")),
        source_surface_id=_string_or_none(source_surface.get("selected_source_surface_id")),
        source_surface_family="current_state_what_stands_now_result",
    )


def _receipt_identity(
    receipt_result: Mapping[str, Any],
    path: Path | str | None,
) -> dict[str, Any]:
    source_surface = receipt_result.get("selected_source_surface")
    source_surface = source_surface if isinstance(source_surface, Mapping) else {}
    return _identity_dict(
        path=path,
        result_id=_metadata_value(
            receipt_result,
            "continuity_transfer_receipt_metadata",
            "continuity_transfer_receipt_result_id",
        ),
        result_type=_metadata_value(
            receipt_result,
            "continuity_transfer_receipt_metadata",
            "continuity_transfer_receipt_result_type",
        ),
        result_family="continuity_transfer_receipt_result",
        outcome=_string_or_none(receipt_result.get("outcome")),
        source_surface_id=_string_or_none(source_surface.get("selected_source_surface_id")),
        source_surface_family="current_state_what_stands_now_result",
    )


def _participation_identity(
    participation_result: Mapping[str, Any],
    path: Path | str | None,
) -> dict[str, Any]:
    source_surface = participation_result.get("selected_source_surface")
    source_surface = source_surface if isinstance(source_surface, Mapping) else {}
    return _identity_dict(
        path=path,
        result_id=_metadata_value(
            participation_result,
            "received_derivative_participation_metadata",
            "received_derivative_participation_result_id",
        ),
        result_type=_metadata_value(
            participation_result,
            "received_derivative_participation_metadata",
            "received_derivative_participation_result_type",
        ),
        result_family="received_derivative_participation_result",
        outcome=_string_or_none(participation_result.get("outcome")),
        source_surface_id=_string_or_none(source_surface.get("selected_source_surface_id")),
        source_surface_family="current_state_what_stands_now_result",
    )


def _action_identity(
    action_result: Mapping[str, Any],
    path: Path | str | None,
) -> dict[str, Any]:
    source_surface = action_result.get("selected_source_surface")
    source_surface = source_surface if isinstance(source_surface, Mapping) else {}
    return _identity_dict(
        path=path,
        result_id=_metadata_value(
            action_result,
            "received_derivative_action_permission_metadata",
            "received_derivative_action_permission_result_id",
        ),
        result_type=_metadata_value(
            action_result,
            "received_derivative_action_permission_metadata",
            "received_derivative_action_permission_result_type",
        ),
        result_family="received_derivative_action_permission_result",
        outcome=_string_or_none(action_result.get("outcome")),
        source_surface_id=_string_or_none(source_surface.get("selected_source_surface_id")),
        source_surface_family="current_state_what_stands_now_result",
    )


def _seam_identity(
    seam_result: Mapping[str, Any],
    path: Path | str | None,
) -> dict[str, Any]:
    source_surface = seam_result.get("selected_source_surface")
    source_surface = source_surface if isinstance(source_surface, Mapping) else {}
    return _identity_dict(
        path=path,
        result_id=_metadata_value(
            seam_result,
            "continuity_memory_seam_metadata",
            "continuity_memory_seam_result_id",
        ),
        result_type=_metadata_value(
            seam_result,
            "continuity_memory_seam_metadata",
            "continuity_memory_seam_result_type",
        ),
        result_family="continuity_memory_seam_result",
        outcome=_string_or_none(seam_result.get("outcome")),
        source_surface_id=_string_or_none(source_surface.get("selected_source_surface_id")),
        source_surface_family="current_state_what_stands_now_result",
    )


def _vessel_identity(
    vessel_result: Mapping[str, Any],
    path: Path | str | None,
) -> dict[str, Any]:
    selected_source = vessel_result.get("selected_source_surface")
    selected_source = selected_source if isinstance(selected_source, Mapping) else {}
    return _identity_dict(
        path=path,
        result_id=_metadata_value(
            vessel_result,
            "openai_api_derivative_vessel_v3_metadata",
            "vessel_result_id",
        ),
        result_type=_metadata_value(
            vessel_result,
            "openai_api_derivative_vessel_v3_metadata",
            "vessel_result_type",
        ),
        result_family=brief_resolver.ALLOWED_SOURCE_RESULT_FAMILY,
        outcome=_string_or_none(vessel_result.get("outcome")),
        source_surface_id=_string_or_none(selected_source.get("selected_source_surface_id")),
        source_surface_family=_string_or_none(
            selected_source.get("selected_source_surface_family")
        ),
    )


def _brief_identity(
    brief_result: Mapping[str, Any],
    path: Path | str | None,
) -> dict[str, Any]:
    selected_vessel = brief_result.get("selected_vessel_result")
    selected_vessel = selected_vessel if isinstance(selected_vessel, Mapping) else {}
    return _identity_dict(
        path=path,
        result_id=_metadata_value(
            brief_result,
            "operator_terminal_brief_metadata",
            "brief_result_id",
        ),
        result_type=_metadata_value(
            brief_result,
            "operator_terminal_brief_metadata",
            "brief_result_type",
        ),
        result_family="operator_terminal_brief_result",
        outcome=_string_or_none(brief_result.get("outcome")),
        source_surface_id=_string_or_none(selected_vessel.get("selected_source_surface_id")),
        source_surface_family=_string_or_none(
            selected_vessel.get("selected_source_surface_family")
        ),
    )


def _artifact_blocked_identity(
    identity: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "surface_path": identity.get("result_path"),
        "surface_id": identity.get("result_id"),
        "surface_family": identity.get("result_family"),
        "surface_outcome": identity.get("outcome"),
    }


def _empty_selected_orientation_inputs(
    body_pass_path: Path | str | None = None,
) -> dict[str, Any]:
    return {
        "selected_body_pass_result": _identity_dict(
            path=body_pass_path,
            result_id=None,
            result_family="v0_body_pass_result",
        ),
        "selected_seam_result": _identity_dict(path=None, result_id=None),
        "selected_action_permission_result": _identity_dict(path=None, result_id=None),
        "selected_participation_result": _identity_dict(path=None, result_id=None),
        "selected_receipt_result": _identity_dict(path=None, result_id=None),
        "selected_transfer_result": _identity_dict(path=None, result_id=None),
        "selected_touch_permission_result": _identity_dict(path=None, result_id=None),
        "selected_source_surface": _identity_dict(path=None, result_id=None),
        "selected_current_state_answer_read_result": _identity_dict(path=None, result_id=None),
        "selected_current_state_query_results": [],
        "selected_current_state_what_stands_now_result": _identity_dict(path=None, result_id=None),
        "selected_current_state_what_remains_open_results": [],
        "selected_vessel_results": [],
        "selected_operator_terminal_brief_results": [],
        "selected_effective_references": {
            "effective_authority_artifact_path": None,
            "effective_family_packet_path": None,
            "effective_status_packet_path": None,
            "effective_current_governing_packet_path": None,
            "effective_source_run_path": None,
            "effective_ingress_run_path": None,
        },
    }


def _body_pass_result_id_for_filename(result: Mapping[str, Any]) -> str | None:
    selected = result.get("selected_orientation_inputs")
    selected = selected if isinstance(selected, Mapping) else {}
    body_pass = selected.get("selected_body_pass_result")
    body_pass = body_pass if isinstance(body_pass, Mapping) else {}
    return _string_or_none(body_pass.get("result_id"))


def _validate_body_pass_result(artifact: Mapping[str, Any]) -> None:
    if _looks_like_external_reader_orientation_attempt(artifact):
        raise CurrentSelfOrientationError(
            "external-reader orientation input is out of scope",
            "EXTERNAL_READER_ORIENTATION_ATTEMPTED",
        )
    if _looks_like_hand_maintained_summary_seam_attempt(artifact):
        raise CurrentSelfOrientationError(
            "hand-maintained summary seam input is out of scope",
            "HAND_MAINTAINED_SUMMARY_SEAM_ATTEMPTED",
        )

    metadata = _require_mapping(
        artifact.get("v0_body_pass_metadata"),
        "v0 body pass metadata",
        "SOURCE_ARTIFACT_MALFORMED",
    )
    for key in (
        "v0_body_pass_result_id",
        "v0_body_pass_result_type",
        "v0_body_pass_result_version",
    ):
        _string_required(metadata.get(key), f"v0 body pass metadata {key}", "SOURCE_ARTIFACT_MALFORMED")

    if _string_or_none(artifact.get("outcome")) != body_pass_resolver.OUTCOME_V0_BODY_PASS_CONFIRMED:
        raise CurrentSelfOrientationError(
            "body pass result is not confirmed",
            "NO_SELF_ORIENTATION_SOURCE_BASIS",
        )

    posture = _require_mapping(
        artifact.get("body_pass_posture"),
        "v0 body pass posture",
        "SOURCE_ARTIFACT_MALFORMED",
    )
    for key in (
        "closure_seam_stands",
        "currentness_without_recency_fraud",
        "derivative_carry_without_source_collapse",
        "lineage_preserved",
        "organs_present_and_successful",
        "v0_body_reads_as_one_bounded_body",
    ):
        if posture.get(key) is not True:
            raise CurrentSelfOrientationError(
                f"v0 body pass posture {key} must be true",
                "CORRESPONDENCE_CHECK_FAILED",
            )

    for key in (
        "selected_seam_result",
        "selected_action_permission_result",
        "selected_participation_result",
        "selected_receipt_result",
        "selected_transfer_result",
        "selected_touch_permission_result",
        "selected_source_surface",
        "block",
        "non_claims",
        "checks",
    ):
        if key == "checks":
            if not isinstance(artifact.get(key), list):
                raise CurrentSelfOrientationError(
                    "v0 body pass checks must be a list",
                    "SOURCE_ARTIFACT_MALFORMED",
                )
        else:
            _require_mapping(artifact.get(key), key, "SOURCE_ARTIFACT_MALFORMED")

    _validate_false_non_claims(
        "v0 body pass",
        artifact,
        body_pass_resolver.NON_CLAIM_DEFAULTS,
    )


def _read_selected_artifact(
    selected_identity: Mapping[str, Any],
    *,
    context: str,
    metadata_key: str,
    metadata_id_key: str,
    expected_outcome: str,
) -> tuple[Path, dict[str, Any]]:
    selected_path = _string_required(
        selected_identity.get("result_path"),
        f"{context} path",
        "SOURCE_ARTIFACT_MALFORMED",
    )
    selected_id = _string_required(
        selected_identity.get("result_id"),
        f"{context} id",
        "SOURCE_ARTIFACT_MALFORMED",
    )
    selected_outcome = _string_required(
        selected_identity.get("outcome"),
        f"{context} outcome",
        "SOURCE_ARTIFACT_MALFORMED",
    )
    if selected_outcome != expected_outcome:
        raise CurrentSelfOrientationError(
            f"{context} selected outcome is not {expected_outcome}",
            "CORRESPONDENCE_CHECK_FAILED",
        )

    artifact = _read_json_file(
        selected_path,
        context=context,
        missing_code="REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
        unreadable_code="REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
        malformed_code="SOURCE_ARTIFACT_MALFORMED",
    )
    artifact_id = _metadata_value(artifact, metadata_key, metadata_id_key)
    if artifact_id != selected_id:
        raise CurrentSelfOrientationError(
            f"{context} id does not match the selected lineage reference",
            "CORRESPONDENCE_CHECK_FAILED",
        )
    if _string_or_none(artifact.get("outcome")) != expected_outcome:
        raise CurrentSelfOrientationError(
            f"{context} outcome does not match the selected lineage reference",
            "CORRESPONDENCE_CHECK_FAILED",
        )
    return _repo_path(selected_path), artifact


def _body_pass_selected_inputs(
    body_pass_result: Mapping[str, Any],
    body_pass_path: Path | str | None,
) -> dict[str, Any]:
    selected_inputs = _empty_selected_orientation_inputs(body_pass_path)
    selected_inputs["selected_body_pass_result"] = _body_pass_identity(
        body_pass_result,
        body_pass_path,
    )
    selected_inputs["selected_seam_result"] = _selected_result_identity(
        _require_mapping(
            body_pass_result.get("selected_seam_result"),
            "selected_seam_result",
            "SOURCE_ARTIFACT_MALFORMED",
        ),
        id_key="selected_seam_result_id",
        path_key="selected_seam_result_path",
        outcome_key="selected_seam_result_outcome",
    )
    selected_inputs["selected_action_permission_result"] = _selected_result_identity(
        _require_mapping(
            body_pass_result.get("selected_action_permission_result"),
            "selected_action_permission_result",
            "SOURCE_ARTIFACT_MALFORMED",
        ),
        id_key="selected_action_permission_result_id",
        path_key="selected_action_permission_result_path",
        outcome_key="selected_action_permission_result_outcome",
    )
    selected_inputs["selected_participation_result"] = _selected_result_identity(
        _require_mapping(
            body_pass_result.get("selected_participation_result"),
            "selected_participation_result",
            "SOURCE_ARTIFACT_MALFORMED",
        ),
        id_key="selected_participation_result_id",
        path_key="selected_participation_result_path",
        outcome_key="selected_participation_result_outcome",
    )
    selected_inputs["selected_receipt_result"] = _selected_result_identity(
        _require_mapping(
            body_pass_result.get("selected_receipt_result"),
            "selected_receipt_result",
            "SOURCE_ARTIFACT_MALFORMED",
        ),
        id_key="selected_receipt_result_id",
        path_key="selected_receipt_result_path",
        outcome_key="selected_receipt_result_outcome",
    )
    selected_inputs["selected_transfer_result"] = _selected_result_identity(
        _require_mapping(
            body_pass_result.get("selected_transfer_result"),
            "selected_transfer_result",
            "SOURCE_ARTIFACT_MALFORMED",
        ),
        id_key="selected_transfer_result_id",
        path_key="selected_transfer_result_path",
        outcome_key="selected_transfer_result_outcome",
    )
    selected_inputs["selected_touch_permission_result"] = _selected_result_identity(
        _require_mapping(
            body_pass_result.get("selected_touch_permission_result"),
            "selected_touch_permission_result",
            "SOURCE_ARTIFACT_MALFORMED",
        ),
        id_key="selected_touch_permission_result_id",
        path_key="selected_touch_permission_result_path",
        outcome_key="selected_touch_permission_result_outcome",
    )
    selected_source_surface = _require_mapping(
        body_pass_result.get("selected_source_surface"),
        "selected_source_surface",
        "SOURCE_ARTIFACT_MALFORMED",
    )
    selected_inputs["selected_source_surface"] = _selected_result_identity(
        selected_source_surface,
        id_key="selected_source_surface_id",
        path_key="selected_source_surface_path",
        outcome_key="selected_source_surface_outcome",
        family_key="selected_source_surface_family",
    )
    selected_inputs["selected_effective_references"] = dict(
        _extract_canonical_effective_references(
            _require_mapping(
                selected_source_surface.get("selected_source_surface_effective_references"),
                "selected_source_surface_effective_references",
                "CURRENT_EFFECTIVE_BASIS_ABSENT_OR_AMBIGUOUS",
            )
        )
    )
    return selected_inputs


def _discover_latest_successful_body_pass_result() -> tuple[Path, dict[str, Any]]:
    candidates = _discover_artifacts(V0_BODY_PASS_ROOT, "v0 body pass")
    for path in reversed(candidates):
        try:
            artifact = _read_json_file(
                path,
                context="v0 body pass result",
                missing_code="NO_SELF_ORIENTATION_SOURCE_BASIS",
                unreadable_code="REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
                malformed_code="SOURCE_ARTIFACT_MALFORMED",
            )
            _validate_body_pass_result(artifact)
        except CurrentSelfOrientationError:
            continue
        return path, artifact
    raise CurrentSelfOrientationError(
        "no confirmed body pass result is available",
        "NO_SELF_ORIENTATION_SOURCE_BASIS",
    )


def _selected_body_pass_artifact(
    body_pass_result: Mapping[str, Any] | None = None,
    body_pass_result_path: Path | str | None = None,
) -> tuple[Path | str, dict[str, Any], str]:
    if body_pass_result is not None:
        if not isinstance(body_pass_result, Mapping):
            raise CurrentSelfOrientationError(
                "body_pass_result must be a mapping",
                "SOURCE_ARTIFACT_MALFORMED",
            )
        artifact = dict(body_pass_result)
        _validate_body_pass_result(artifact)
        return "provided_mapping", artifact, "provided_body_pass_mapping"
    if body_pass_result_path is not None:
        artifact = _read_json_file(
            body_pass_result_path,
            context="selected v0 body pass result",
            missing_code="REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
            unreadable_code="REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
            malformed_code="SOURCE_ARTIFACT_MALFORMED",
        )
        _validate_body_pass_result(artifact)
        return _repo_path(body_pass_result_path), artifact, "explicit_body_pass_result_path"
    discovered_path, artifact = _discover_latest_successful_body_pass_result()
    return discovered_path, artifact, "successful_body_pass_discovery"


def _read_effective_artifact_bundle(
    effective_references: Mapping[str, Any],
) -> dict[str, Any]:
    if not _effective_references_complete(effective_references):
        raise CurrentSelfOrientationError(
            "selected effective references are incomplete",
            "CURRENT_EFFECTIVE_BASIS_ABSENT_OR_AMBIGUOUS",
        )

    authority_path = _string_required(
        effective_references.get("effective_authority_artifact_path"),
        "effective_authority_artifact_path",
        "CURRENT_EFFECTIVE_BASIS_ABSENT_OR_AMBIGUOUS",
    )
    family_path = _string_required(
        effective_references.get("effective_family_packet_path"),
        "effective_family_packet_path",
        "CURRENT_EFFECTIVE_BASIS_ABSENT_OR_AMBIGUOUS",
    )
    status_path = _string_required(
        effective_references.get("effective_status_packet_path"),
        "effective_status_packet_path",
        "CURRENT_EFFECTIVE_BASIS_ABSENT_OR_AMBIGUOUS",
    )
    governing_path = _string_required(
        effective_references.get("effective_current_governing_packet_path"),
        "effective_current_governing_packet_path",
        "CURRENT_EFFECTIVE_BASIS_ABSENT_OR_AMBIGUOUS",
    )

    authority = _read_json_file(
        authority_path,
        context="effective execution authority artifact",
        missing_code="REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
        unreadable_code="REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
        malformed_code="SOURCE_ARTIFACT_MALFORMED",
    )
    family = _read_json_file(
        family_path,
        context="effective run family packet",
        missing_code="REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
        unreadable_code="REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
        malformed_code="SOURCE_ARTIFACT_MALFORMED",
    )
    status = _read_json_file(
        status_path,
        context="effective preserved run status packet",
        missing_code="REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
        unreadable_code="REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
        malformed_code="SOURCE_ARTIFACT_MALFORMED",
    )
    governing = _read_json_file(
        governing_path,
        context="effective current governing packet",
        missing_code="REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
        unreadable_code="REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
        malformed_code="SOURCE_ARTIFACT_MALFORMED",
    )
    return {
        "authority_path": _repo_path(authority_path),
        "authority": authority,
        "family_path": _repo_path(family_path),
        "family": family,
        "status_path": _repo_path(status_path),
        "status": status,
        "governing_path": _repo_path(governing_path),
        "governing": governing,
    }


def _selected_answer_read_path_and_id(
    stand_result: Mapping[str, Any],
) -> tuple[str, str]:
    selected_answer = _require_mapping(
        stand_result.get("selected_current_state_answer_read"),
        "selected_current_state_answer_read",
        "SOURCE_ARTIFACT_MALFORMED",
    )
    return (
        _string_required(
            selected_answer.get("current_state_answer_read_result_path"),
            "selected current-state answer/read path",
            "SOURCE_ARTIFACT_MALFORMED",
        ),
        _string_required(
            selected_answer.get("current_state_answer_read_result_id"),
            "selected current-state answer/read id",
            "SOURCE_ARTIFACT_MALFORMED",
        ),
    )


def _read_answer_read_result(
    stand_result: Mapping[str, Any],
    effective_references: Mapping[str, Any],
) -> tuple[Path, dict[str, Any], dict[str, Any]]:
    answer_read_path, expected_answer_read_id = _selected_answer_read_path_and_id(stand_result)
    answer_read_result = _read_json_file(
        answer_read_path,
        context="selected current-state answer/read result",
        missing_code="CURRENT_STATE_SURFACE_ABSENT_WHERE_REQUIRED",
        unreadable_code="REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
        malformed_code="SOURCE_ARTIFACT_MALFORMED",
    )
    if _metadata_value(
        answer_read_result,
        "answer_read_metadata",
        "answer_read_result_id",
    ) != expected_answer_read_id:
        raise CurrentSelfOrientationError(
            "selected current-state answer/read id does not match the what-stands-now lineage",
            "CORRESPONDENCE_CHECK_FAILED",
        )
    if _string_or_none(answer_read_result.get("outcome")) != answer_resolver.OUTCOME_ANSWERED:
        raise CurrentSelfOrientationError(
            "selected current-state answer/read result is not answered",
            "CURRENT_STATE_SURFACE_ABSENT_WHERE_REQUIRED",
        )

    output = _require_mapping(
        answer_read_result.get("answer_read_output"),
        "answer_read_output",
        "SOURCE_ARTIFACT_MALFORMED",
    )
    if not _effective_references_match(effective_references, output):
        raise CurrentSelfOrientationError(
            "current-state answer/read result does not correspond to the selected effective basis",
            "CORRESPONDENCE_CHECK_FAILED",
        )
    _validate_false_non_claims(
        "current-state answer/read result",
        answer_read_result,
        answer_resolver.NON_CLAIM_DEFAULTS,
    )
    return _repo_path(answer_read_path), answer_read_result, answer_resolver.build_current_state_answer_read_summary(answer_read_result)


def _discover_matching_query_results(
    expected_answer_read_id: str,
    effective_references: Mapping[str, Any],
) -> list[tuple[Path, dict[str, Any], dict[str, Any]]]:
    matches: list[tuple[Path, dict[str, Any], dict[str, Any]]] = []
    for path in _discover_artifacts(CURRENT_STATE_QUERY_ROOT, "current-state query"):
        try:
            artifact = _read_json_file(
                path,
                context="current-state query result",
                missing_code="CURRENT_STATE_SURFACE_ABSENT_WHERE_REQUIRED",
                unreadable_code="REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
                malformed_code="SOURCE_ARTIFACT_MALFORMED",
            )
        except CurrentSelfOrientationError:
            continue
        summary = query_resolver.build_current_state_query_summary(artifact)
        selected_answer_id = _string_or_none(summary.get("selected_current_state_answer_read_id"))
        if selected_answer_id != expected_answer_read_id:
            continue
        effective_inputs = _require_mapping(
            artifact.get("effective_query_inputs"),
            "effective_query_inputs",
            "SOURCE_ARTIFACT_MALFORMED",
        )
        if not _effective_references_match(effective_references, effective_inputs):
            raise CurrentSelfOrientationError(
                "current-state query result shares the selected answer/read basis but not the effective basis",
                "CORRESPONDENCE_CHECK_FAILED",
            )
        matches.append((path, artifact, summary))
    if not matches:
        raise CurrentSelfOrientationError(
            "no current-state query result matches the selected answer/read and effective basis",
            "CURRENT_STATE_SURFACE_ABSENT_WHERE_REQUIRED",
        )
    return matches


def _discover_matching_what_remains_open_results(
    expected_answer_read_id: str,
    effective_references: Mapping[str, Any],
) -> list[tuple[Path, dict[str, Any], dict[str, Any]]]:
    matches: list[tuple[Path, dict[str, Any], dict[str, Any]]] = []
    for path in _discover_artifacts(CURRENT_STATE_WHAT_REMAINS_OPEN_ROOT, "what-remains-open"):
        try:
            artifact = _read_json_file(
                path,
                context="what-remains-open result",
                missing_code="CURRENT_STATE_SURFACE_ABSENT_WHERE_REQUIRED",
                unreadable_code="REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
                malformed_code="SOURCE_ARTIFACT_MALFORMED",
            )
        except CurrentSelfOrientationError:
            continue
        summary = open_resolver.build_current_state_what_remains_open_summary(artifact)
        selected_answer_id = _string_or_none(summary.get("selected_current_state_answer_read_id"))
        if selected_answer_id != expected_answer_read_id:
            continue
        effective_inputs = _require_mapping(
            artifact.get("effective_open_inputs"),
            "effective_open_inputs",
            "SOURCE_ARTIFACT_MALFORMED",
        )
        if not _effective_references_match(effective_references, effective_inputs):
            raise CurrentSelfOrientationError(
                "what-remains-open result shares the selected answer/read basis but not the effective basis",
                "CORRESPONDENCE_CHECK_FAILED",
            )
        matches.append((path, artifact, summary))
    if not matches:
        raise CurrentSelfOrientationError(
            "no what-remains-open result matches the selected answer/read and effective basis",
            "CURRENT_STATE_SURFACE_ABSENT_WHERE_REQUIRED",
        )
    return matches


def _discover_matching_vessel_results(
    selected_source_surface_id: str,
    effective_references: Mapping[str, Any],
) -> list[tuple[Path, dict[str, Any], dict[str, Any]]]:
    matches: list[tuple[Path, dict[str, Any], dict[str, Any]]] = []
    for path in _discover_artifacts(OPENAI_API_DERIVATIVE_VESSEL_V3_ROOT, "vessel v3"):
        try:
            artifact = _read_json_file(
                path,
                context="vessel v3 result",
                missing_code="DERIVATIVE_SURFACE_SOURCE_BASIS_MISSING",
                unreadable_code="REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
                malformed_code="SOURCE_ARTIFACT_MALFORMED",
            )
        except CurrentSelfOrientationError:
            continue
        selected_source = artifact.get("selected_source_surface")
        if not isinstance(selected_source, Mapping):
            continue
        if _string_or_none(selected_source.get("selected_source_surface_id")) != selected_source_surface_id:
            continue
        if _string_or_none(selected_source.get("selected_source_surface_family")) != vessel_resolver.ALLOWED_SOURCE_FAMILY:
            raise CurrentSelfOrientationError(
                "a matched vessel result does not preserve the allowed upstream source family",
                "DERIVATIVE_SURFACE_SOURCE_BASIS_MISSING",
            )
        request = _require_mapping(
            artifact.get("vessel_request"),
            "vessel_request",
            "SOURCE_ARTIFACT_MALFORMED",
        )
        if _string_or_none(request.get("allowed_source_family")) != vessel_resolver.ALLOWED_SOURCE_FAMILY:
            raise CurrentSelfOrientationError(
                "a matched vessel result widened its source family",
                "DERIVATIVE_SURFACE_SOURCE_BASIS_MISSING",
            )
        payload = _require_mapping(
            request.get("bounded_source_payload"),
            "bounded_source_payload",
            "SOURCE_ARTIFACT_MALFORMED",
        )
        payload_effective_refs = _extract_canonical_effective_references(payload)
        for key in (
            "effective_authority_artifact_path",
            "effective_source_run_path",
            "effective_ingress_run_path",
        ):
            expected = _string_or_none(effective_references.get(key))
            actual = _string_or_none(payload_effective_refs.get(key))
            if expected is None or actual is None or not _paths_equal(expected, actual):
                raise CurrentSelfOrientationError(
                    "a matched vessel result does not correspond to the selected effective basis",
                    "CORRESPONDENCE_CHECK_FAILED",
                )
        matches.append((path, artifact, vessel_resolver.build_bounded_current_state_vessel_summary(artifact)))
    if not matches:
        raise CurrentSelfOrientationError(
            "no bounded vessel v3 result matches the selected source surface",
            "DERIVATIVE_SURFACE_SOURCE_BASIS_MISSING",
        )
    return matches


def _discover_matching_operator_brief_results(
    selected_source_surface_id: str,
    matching_vessel_ids: set[str],
) -> list[tuple[Path, dict[str, Any], dict[str, Any]]]:
    matches: list[tuple[Path, dict[str, Any], dict[str, Any]]] = []
    for path in _discover_artifacts(OPERATOR_TERMINAL_BRIEF_ROOT, "operator terminal brief"):
        try:
            artifact = _read_json_file(
                path,
                context="operator terminal brief result",
                missing_code="OPERATOR_SURFACE_DERIVATIVE_OR_SOURCE_BASIS_MISSING",
                unreadable_code="REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
                malformed_code="SOURCE_ARTIFACT_MALFORMED",
            )
        except CurrentSelfOrientationError:
            continue
        selected_vessel = artifact.get("selected_vessel_result")
        if not isinstance(selected_vessel, Mapping):
            continue
        if _string_or_none(selected_vessel.get("selected_source_surface_id")) != selected_source_surface_id:
            continue
        if _string_or_none(selected_vessel.get("selected_source_surface_family")) != brief_resolver.UPSTREAM_ALLOWED_SOURCE_FAMILY:
            raise CurrentSelfOrientationError(
                "a matched operator brief does not preserve the required upstream source family",
                "OPERATOR_SURFACE_DERIVATIVE_OR_SOURCE_BASIS_MISSING",
            )
        vessel_id = _string_or_none(selected_vessel.get("selected_vessel_result_id"))
        if vessel_id is None or vessel_id not in matching_vessel_ids:
            raise CurrentSelfOrientationError(
                "a matched operator brief does not preserve a matched vessel basis",
                "OPERATOR_SURFACE_DERIVATIVE_OR_SOURCE_BASIS_MISSING",
            )
        matches.append((path, artifact, brief_resolver.build_operator_terminal_brief_summary(artifact)))
    if not matches:
        raise CurrentSelfOrientationError(
            "no operator terminal brief matches the selected vessel/source basis",
            "OPERATOR_SURFACE_DERIVATIVE_OR_SOURCE_BASIS_MISSING",
        )
    return matches


def _validate_derivative_posture(
    transfer_result: Mapping[str, Any],
    receipt_result: Mapping[str, Any],
    participation_result: Mapping[str, Any],
    action_result: Mapping[str, Any],
    vessel_results: Sequence[Mapping[str, Any]],
    operator_results: Sequence[Mapping[str, Any]],
) -> None:
    transfer_payload = _require_mapping(
        transfer_result.get("transfer_payload"),
        "transfer_payload",
        "SOURCE_ARTIFACT_MALFORMED",
    )
    if transfer_payload.get("source_remains_source") is not True:
        raise CurrentSelfOrientationError(
            "continuity transfer collapsed derivative/source posture",
            "DERIVATIVE_TREATED_AS_SOURCE_AUTHORITY",
        )

    receipt_payload = _require_mapping(
        receipt_result.get("receipt_payload"),
        "receipt_payload",
        "SOURCE_ARTIFACT_MALFORMED",
    )
    if receipt_payload.get("source_remains_source") is not True:
        raise CurrentSelfOrientationError(
            "continuity receipt collapsed derivative/source posture",
            "DERIVATIVE_TREATED_AS_SOURCE_AUTHORITY",
        )
    if receipt_payload.get("carried_derivative_remains_derivative") is not True:
        raise CurrentSelfOrientationError(
            "continuity receipt lost derivative posture",
            "DERIVATIVE_TREATED_AS_SOURCE_AUTHORITY",
        )

    participation_payload = _require_mapping(
        participation_result.get("participation_payload"),
        "participation_payload",
        "SOURCE_ARTIFACT_MALFORMED",
    )
    if participation_payload.get("source_remains_source") is not True:
        raise CurrentSelfOrientationError(
            "received derivative participation collapsed source posture",
            "DERIVATIVE_TREATED_AS_SOURCE_AUTHORITY",
        )
    if participation_payload.get("participation_payload_remains_derivative") is not True:
        raise CurrentSelfOrientationError(
            "received derivative participation lost derivative posture",
            "DERIVATIVE_TREATED_AS_SOURCE_AUTHORITY",
        )

    action_payload = _require_mapping(
        action_result.get("action_permission_payload"),
        "action_permission_payload",
        "SOURCE_ARTIFACT_MALFORMED",
    )
    if action_payload.get("source_remains_source") is not True:
        raise CurrentSelfOrientationError(
            "received derivative action permission collapsed source posture",
            "DERIVATIVE_TREATED_AS_SOURCE_AUTHORITY",
        )
    if action_payload.get("action_permission_payload_remains_derivative") is not True:
        raise CurrentSelfOrientationError(
            "received derivative action permission lost derivative posture",
            "DERIVATIVE_TREATED_AS_SOURCE_AUTHORITY",
        )

    for artifact in vessel_results:
        derivative_answer = _require_mapping(
            artifact.get("derivative_answer"),
            "derivative_answer",
            "SOURCE_ARTIFACT_MALFORMED",
        )
        if derivative_answer.get("source_remains_source") is not True:
            raise CurrentSelfOrientationError(
                "vessel derivative answer collapsed source posture",
                "DERIVATIVE_TREATED_AS_SOURCE_AUTHORITY",
            )
        if derivative_answer.get("model_output_remains_derivative") is not True:
            raise CurrentSelfOrientationError(
                "vessel derivative answer lost derivative posture",
                "DERIVATIVE_TREATED_AS_SOURCE_AUTHORITY",
            )

    for artifact in operator_results:
        brief_output = _require_mapping(
            artifact.get("brief_output"),
            "brief_output",
            "SOURCE_ARTIFACT_MALFORMED",
        )
        if brief_output.get("source_remains_source") is not True:
            raise CurrentSelfOrientationError(
                "operator brief collapsed source posture",
                "OPERATOR_SURFACE_TREATED_AS_SOURCE_AUTHORITY",
            )
        if brief_output.get("vessel_output_remains_derivative") is not True:
            raise CurrentSelfOrientationError(
                "operator brief lost vessel derivative posture",
                "OPERATOR_SURFACE_TREATED_AS_SOURCE_AUTHORITY",
            )
        if brief_output.get("brief_remains_derivative") is not True:
            raise CurrentSelfOrientationError(
                "operator brief lost derivative posture",
                "OPERATOR_SURFACE_TREATED_AS_SOURCE_AUTHORITY",
            )


def _check_open_posture(
    what_remains_open_results: Sequence[Mapping[str, Any]],
) -> None:
    for open_result in what_remains_open_results:
        outcome = _string_or_none(open_result.get("outcome"))
        if outcome not in {
            open_resolver.OUTCOME_ANSWERED_WHAT_REMAINS_OPEN,
            open_resolver.OUTCOME_BLOCKED,
        }:
            raise CurrentSelfOrientationError(
                "what-remains-open outcome is outside the bounded open posture",
                "OPEN_SURFACE_TREATED_AS_COMPLETED",
            )


def _recognized_current_executable_core_line(
    body_pass_identity: Mapping[str, Any],
    seam_identity: Mapping[str, Any],
    source_identity: Mapping[str, Any],
    effective_references: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "canonical_core_execution_file": CANONICAL_CORE_EXECUTION_FILE,
        "recognized_from_standing_body_pass": True,
        "selected_body_pass_result_id": body_pass_identity.get("result_id"),
        "selected_seam_result_id": seam_identity.get("result_id"),
        "selected_source_surface_id": source_identity.get("result_id"),
        "effective_current_governing_source_run_path": effective_references.get(
            "effective_source_run_path"
        ),
        "effective_current_governing_ingress_run_path": effective_references.get(
            "effective_ingress_run_path"
        ),
    }


def _recognized_governing_effective_basis(
    effective_references: Mapping[str, Any],
    effective_bundle: Mapping[str, Any],
) -> dict[str, Any]:
    authority = effective_bundle["authority"]
    family = effective_bundle["family"]
    status = effective_bundle["status"]
    governing = effective_bundle["governing"]
    return {
        "recognized_from_explicit_effective_references": True,
        "effective_references": dict(effective_references),
        "current_execution_authority_artifact_path": _display_path(
            effective_bundle["authority_path"]
        ),
        "run_family_packet_path": _display_path(effective_bundle["family_path"]),
        "preserved_run_status_packet_path": _display_path(effective_bundle["status_path"]),
        "current_governing_packet_path": _display_path(effective_bundle["governing_path"]),
        "execution_authority_summary": authority_resolver.build_execution_authority_summary(
            authority
        ),
        "run_family_summary": family_resolver.build_run_family_summary(family),
        "preserved_run_status_summary": status_resolver.build_preserved_run_status_summary(
            status
        ),
        "current_governing_summary": governing_resolver.build_current_governing_summary(
            governing
        ),
    }


def _recognized_current_state_surfaces(
    answer_identity: Mapping[str, Any],
    answer_summary: Mapping[str, Any],
    query_results: Sequence[tuple[Path, Mapping[str, Any], Mapping[str, Any]]],
    stand_identity: Mapping[str, Any],
    stand_summary: Mapping[str, Any],
    open_results: Sequence[tuple[Path, Mapping[str, Any], Mapping[str, Any]]],
) -> dict[str, Any]:
    return {
        "current_state_answer_read_result": {
            **dict(answer_identity),
            "summary": dict(answer_summary),
        },
        "current_state_query_results": [
            {
                **_query_identity(artifact, path),
                "summary": dict(summary),
            }
            for path, artifact, summary in query_results
        ],
        "current_state_what_stands_now_result": {
            **dict(stand_identity),
            "summary": dict(stand_summary),
        },
        "current_state_what_remains_open_results": [
            {
                **_what_remains_open_identity(artifact, path),
                "summary": dict(summary),
            }
            for path, artifact, summary in open_results
        ],
    }


def _recognized_continuity_surfaces(
    transfer_result: Mapping[str, Any],
    transfer_path: Path | str,
    receipt_result: Mapping[str, Any],
    receipt_path: Path | str,
    seam_result: Mapping[str, Any],
    seam_path: Path | str,
    body_pass_result: Mapping[str, Any],
    body_pass_path: Path | str,
) -> dict[str, Any]:
    return {
        "continuity_transfer_unit_result": {
            **_transfer_identity(transfer_result, transfer_path),
            "summary": transfer_resolver.build_continuity_transfer_unit_summary(
                transfer_result
            ),
        },
        "continuity_transfer_receipt_result": {
            **_receipt_identity(receipt_result, receipt_path),
            "summary": receipt_resolver.build_continuity_transfer_receipt_summary(
                receipt_result
            ),
        },
        "continuity_memory_seam_result": {
            **_seam_identity(seam_result, seam_path),
            "summary": seam_resolver.build_continuity_memory_seam_summary(seam_result),
        },
        "v0_body_pass_result": {
            **_body_pass_identity(body_pass_result, body_pass_path),
            "summary": body_pass_resolver.build_v0_body_pass_summary(body_pass_result),
        },
    }


def _recognized_derivative_surfaces(
    participation_result: Mapping[str, Any],
    participation_path: Path | str,
    action_result: Mapping[str, Any],
    action_path: Path | str,
    vessel_results: Sequence[tuple[Path, Mapping[str, Any], Mapping[str, Any]]],
) -> dict[str, Any]:
    return {
        "received_derivative_participation_result": {
            **_participation_identity(participation_result, participation_path),
            "summary": participation_resolver.build_received_derivative_participation_summary(
                participation_result
            ),
        },
        "received_derivative_action_permission_result": {
            **_action_identity(action_result, action_path),
            "summary": action_resolver.build_received_derivative_action_permission_summary(
                action_result
            ),
        },
        "openai_api_derivative_vessel_v3_results": [
            {
                **_vessel_identity(artifact, path),
                "summary": dict(summary),
            }
            for path, artifact, summary in vessel_results
        ],
    }


def _recognized_operator_facing_surfaces(
    operator_results: Sequence[tuple[Path, Mapping[str, Any], Mapping[str, Any]]],
) -> dict[str, Any]:
    return {
        "operator_terminal_brief_results": [
            {
                **_brief_identity(artifact, path),
                "summary": dict(summary),
            }
            for path, artifact, summary in operator_results
        ]
    }


def _recognized_open_surfaces(
    open_results: Sequence[tuple[Path, Mapping[str, Any], Mapping[str, Any]]],
    non_claims: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "what_remains_open_results": [
            {
                **_what_remains_open_identity(artifact, path),
                "summary": dict(summary),
            }
            for path, artifact, summary in open_results
        ],
        "carried_non_claims": dict(non_claims),
    }


def _recognized_touch_admissibility_surfaces(
    touch_result: Mapping[str, Any],
    touch_path: Path | str,
) -> dict[str, Any]:
    return {
        "current_state_touch_permission_result": {
            **_touch_identity(touch_result, touch_path),
            "summary": touch_resolver.build_current_state_touch_permission_summary(
                touch_result
            ),
            "admitted_touch_scope": dict(
                _require_mapping(
                    touch_result.get("admitted_touch_scope"),
                    "admitted_touch_scope",
                    "SOURCE_ARTIFACT_MALFORMED",
                )
            ),
        }
    }


def _recognized_blocked_or_refused_surfaces(
    query_results: Sequence[tuple[Path, Mapping[str, Any], Mapping[str, Any]]],
    open_results: Sequence[tuple[Path, Mapping[str, Any], Mapping[str, Any]]],
    vessel_results: Sequence[tuple[Path, Mapping[str, Any], Mapping[str, Any]]],
    operator_results: Sequence[tuple[Path, Mapping[str, Any], Mapping[str, Any]]],
) -> list[dict[str, Any]]:
    blocked: list[dict[str, Any]] = []
    for path, artifact, _summary in query_results:
        identity = _query_identity(artifact, path)
        if identity.get("outcome") in BLOCKED_OR_REFUSED_OUTCOMES:
            blocked.append(_artifact_blocked_identity(identity))
    for path, artifact, _summary in open_results:
        identity = _what_remains_open_identity(artifact, path)
        if identity.get("outcome") in BLOCKED_OR_REFUSED_OUTCOMES:
            blocked.append(_artifact_blocked_identity(identity))
    for path, artifact, _summary in vessel_results:
        identity = _vessel_identity(artifact, path)
        if identity.get("outcome") in BLOCKED_OR_REFUSED_OUTCOMES:
            blocked.append(_artifact_blocked_identity(identity))
    for path, artifact, _summary in operator_results:
        identity = _brief_identity(artifact, path)
        if identity.get("outcome") in BLOCKED_OR_REFUSED_OUTCOMES:
            blocked.append(_artifact_blocked_identity(identity))
    return blocked


def _build_correspondence_checks(
    *,
    discovery_mode: str,
    body_pass_result: Mapping[str, Any],
    answer_read_result: Mapping[str, Any],
    query_results: Sequence[tuple[Path, Mapping[str, Any], Mapping[str, Any]]],
    stand_result: Mapping[str, Any],
    open_results: Sequence[tuple[Path, Mapping[str, Any], Mapping[str, Any]]],
    touch_result: Mapping[str, Any],
    transfer_result: Mapping[str, Any],
    receipt_result: Mapping[str, Any],
    participation_result: Mapping[str, Any],
    action_result: Mapping[str, Any],
    seam_result: Mapping[str, Any],
    vessel_results: Sequence[tuple[Path, Mapping[str, Any], Mapping[str, Any]]],
    operator_results: Sequence[tuple[Path, Mapping[str, Any], Mapping[str, Any]]],
    non_claims: Mapping[str, Any],
    blocked_or_refused_surfaces: Sequence[Mapping[str, Any]],
    effective_references: Mapping[str, Any],
    recognized_sections: Mapping[str, Any],
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    successful_vessel_count = sum(
        1
        for _path, artifact, _summary in vessel_results
        if artifact.get("outcome") == vessel_resolver.OUTCOME_ANSWERED_DERIVATIVE_READ
    )
    successful_operator_count = sum(
        1
        for _path, artifact, _summary in operator_results
        if artifact.get("outcome") == brief_resolver.OUTCOME_BRIEF_RENDERED
    )

    checks.append(
        _check(
            "current_self_orientation_uses_explicit_anchor_or_successful_filtered_discovery",
            discovery_mode
            in {
                "provided_body_pass_mapping",
                "explicit_body_pass_result_path",
                "successful_body_pass_discovery",
            },
            expected="explicit body-pass basis or filtered successful discovery",
            actual=discovery_mode,
            block_code="LATEST_FILE_RECENCY_REFUSED",
        )
    )
    checks.append(
        _check(
            "current_body_pass_posture_booleans_are_true",
            all(
                _require_mapping(
                    body_pass_result.get("body_pass_posture"),
                    "body_pass_posture",
                    "SOURCE_ARTIFACT_MALFORMED",
                ).get(key)
                is True
                for key in (
                    "closure_seam_stands",
                    "currentness_without_recency_fraud",
                    "derivative_carry_without_source_collapse",
                    "lineage_preserved",
                    "organs_present_and_successful",
                    "v0_body_reads_as_one_bounded_body",
                )
            ),
            expected="all body-pass posture booleans true",
            actual=_require_mapping(
                body_pass_result.get("body_pass_posture"),
                "body_pass_posture",
                "SOURCE_ARTIFACT_MALFORMED",
            ),
            block_code="CORRESPONDENCE_CHECK_FAILED",
        )
    )
    checks.append(
        _check(
            "every_named_source_surface_is_readable",
            True,
            expected="all named source surfaces readable",
            actual="all selected artifacts loaded",
            block_code="REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
        )
    )
    checks.append(
        _check(
            "governing_effective_basis_is_explicit_not_latest_file_guessing",
            _effective_references_complete(effective_references),
            expected="complete explicit effective references",
            actual=dict(effective_references),
            block_code="CURRENT_EFFECTIVE_BASIS_ABSENT_OR_AMBIGUOUS",
        )
    )
    checks.append(
        _check(
            "current_state_answer_read_is_answered_and_corresponds",
            answer_read_result.get("outcome") == answer_resolver.OUTCOME_ANSWERED,
            expected=answer_resolver.OUTCOME_ANSWERED,
            actual=answer_read_result.get("outcome"),
            block_code="CURRENT_STATE_SURFACE_ABSENT_WHERE_REQUIRED",
        )
    )
    checks.append(
        _check(
            "current_state_query_results_are_visible_and_coherent",
            bool(query_results),
            expected="at least one matching current-state query result",
            actual=len(query_results),
            block_code="CURRENT_STATE_SURFACE_ABSENT_WHERE_REQUIRED",
        )
    )
    checks.append(
        _check(
            "what_stands_now_result_is_answered_and_current",
            stand_result.get("outcome") == stand_resolver.OUTCOME_ANSWERED_WHAT_STANDS_NOW,
            expected=stand_resolver.OUTCOME_ANSWERED_WHAT_STANDS_NOW,
            actual=stand_result.get("outcome"),
            block_code="CURRENT_STATE_SURFACE_ABSENT_WHERE_REQUIRED",
        )
    )
    checks.append(
        _check(
            "what_remains_open_results_are_visible_and_open",
            bool(open_results),
            expected="at least one matching what-remains-open result",
            actual=len(open_results),
            block_code="CURRENT_STATE_SURFACE_ABSENT_WHERE_REQUIRED",
        )
    )
    checks.append(
        _check(
            "touch_permission_is_admissibility_not_general_authority",
            touch_result.get("outcome") == touch_resolver.OUTCOME_ADMITTED_FOR_TOUCH,
            expected=touch_resolver.OUTCOME_ADMITTED_FOR_TOUCH,
            actual=touch_result.get("outcome"),
            block_code="CURRENT_STATE_SURFACE_ABSENT_WHERE_REQUIRED",
        )
    )
    checks.append(
        _check(
            "continuity_transfer_and_receipt_remain_transfer_and_receipt",
            transfer_result.get("outcome") == transfer_resolver.OUTCOME_TRANSFERRED
            and receipt_result.get("outcome") == receipt_resolver.OUTCOME_RECEIVED,
            expected={
                "transfer": transfer_resolver.OUTCOME_TRANSFERRED,
                "receipt": receipt_resolver.OUTCOME_RECEIVED,
            },
            actual={
                "transfer": transfer_result.get("outcome"),
                "receipt": receipt_result.get("outcome"),
            },
            block_code="CORRESPONDENCE_CHECK_FAILED",
        )
    )
    checks.append(
        _check(
            "received_derivative_participation_and_action_permission_remain_derivative",
            participation_result.get("outcome") == participation_resolver.OUTCOME_PARTICIPATED
            and action_result.get("outcome") == action_resolver.OUTCOME_ACTION_PERMITTED,
            expected={
                "participation": participation_resolver.OUTCOME_PARTICIPATED,
                "action_permission": action_resolver.OUTCOME_ACTION_PERMITTED,
            },
            actual={
                "participation": participation_result.get("outcome"),
                "action_permission": action_result.get("outcome"),
            },
            block_code="DERIVATIVE_TREATED_AS_SOURCE_AUTHORITY",
        )
    )
    checks.append(
        _check(
            "continuity_memory_seam_and_v0_body_pass_remain_non_final",
            seam_result.get("outcome") == seam_resolver.OUTCOME_SEAM_CLOSED
            and body_pass_result.get("outcome") == body_pass_resolver.OUTCOME_V0_BODY_PASS_CONFIRMED,
            expected={
                "seam": seam_resolver.OUTCOME_SEAM_CLOSED,
                "body_pass": body_pass_resolver.OUTCOME_V0_BODY_PASS_CONFIRMED,
            },
            actual={
                "seam": seam_result.get("outcome"),
                "body_pass": body_pass_result.get("outcome"),
            },
            block_code="CORRESPONDENCE_CHECK_FAILED",
        )
    )
    checks.append(
        _check(
            "bounded_vessel_results_are_present_and_derivative",
            successful_vessel_count > 0,
            expected="at least one matching answered bounded vessel result",
            actual={
                "matched_result_count": len(vessel_results),
                "successful_result_count": successful_vessel_count,
            },
            block_code="DERIVATIVE_SURFACE_SOURCE_BASIS_MISSING",
        )
    )
    checks.append(
        _check(
            "operator_terminal_brief_results_are_present_and_operator_facing_derivative",
            successful_operator_count > 0,
            expected="at least one matching rendered operator terminal brief",
            actual={
                "matched_result_count": len(operator_results),
                "successful_result_count": successful_operator_count,
            },
            block_code="OPERATOR_SURFACE_DERIVATIVE_OR_SOURCE_BASIS_MISSING",
        )
    )
    checks.append(
        _check(
            "open_surfaces_are_not_converted_to_completed",
            all(
                artifact.get("outcome")
                in {
                    open_resolver.OUTCOME_ANSWERED_WHAT_REMAINS_OPEN,
                    open_resolver.OUTCOME_BLOCKED,
                }
                for _path, artifact, _summary in open_results
            ),
            expected="what-remains-open outcomes stay open or blocked",
            actual=[artifact.get("outcome") for _path, artifact, _summary in open_results],
            block_code="OPEN_SURFACE_TREATED_AS_COMPLETED",
        )
    )
    checks.append(
        _check(
            "blocked_or_refused_surfaces_remain_visible_when_present",
            True,
            expected="explicit blocked/refused posture remains visible",
            actual=blocked_or_refused_surfaces if blocked_or_refused_surfaces else "none explicitly selected",
            block_code="BLOCKED_OR_REFUSED_SURFACE_HIDDEN",
        )
    )
    checks.append(
        _check(
            "non_claims_remain_false_and_carried_forward",
            all(value is False for value in non_claims.values()),
            expected=False,
            actual=dict(non_claims),
            block_code="NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    checks.append(
        _check(
            "self_orientation_distinguishes_current_governing_derivative_open_blocked_touch_categories",
            all(
                key in recognized_sections
                for key in (
                    "recognized_current_executable_core_line",
                    "recognized_governing_effective_basis",
                    "recognized_current_state_surfaces",
                    "recognized_continuity_surfaces",
                    "recognized_derivative_surfaces",
                    "recognized_operator_facing_surfaces",
                    "recognized_open_surfaces",
                    "recognized_blocked_or_refused_surfaces",
                    "recognized_touch_admissibility_surfaces",
                )
            ),
            expected="distinct recognition categories",
            actual=sorted(recognized_sections),
            block_code="UNDER_MIRRORING_REFUSED",
        )
    )
    checks.append(
        _check(
            "self_orientation_does_not_over_mirror_into_whole_body_replacement",
            True,
            expected="bounded recognition sections and summaries only",
            actual="bounded recognition sections",
            block_code="OVER_MIRRORING_REFUSED",
        )
    )
    checks.append(
        _check(
            "self_orientation_does_not_under_mirror_required_standing_posture",
            bool(query_results)
            and bool(open_results)
            and successful_vessel_count > 0
            and successful_operator_count > 0,
            expected="required current, open, derivative, and operator-facing posture present",
            actual={
                "query_result_count": len(query_results),
                "open_result_count": len(open_results),
                "vessel_result_count": len(vessel_results),
                "successful_vessel_result_count": successful_vessel_count,
                "operator_result_count": len(operator_results),
                "successful_operator_result_count": successful_operator_count,
            },
            block_code="UNDER_MIRRORING_REFUSED",
        )
    )
    return checks


def _result_id(body_pass_result_id: str | None, outcome: str) -> str:
    base = body_pass_result_id or "no_selected_body_pass_result"
    suffix = (
        "current_self_oriented" if outcome == OUTCOME_SELF_ORIENTED else "current_self_orientation_blocked"
    )
    return f"{base}__{suffix}"


def _metadata(body_pass_result_id: str | None, outcome: str) -> dict[str, Any]:
    return {
        "self_orientation_result_id": _result_id(body_pass_result_id, outcome),
        "self_orientation_result_type": CURRENT_SELF_ORIENTATION_RESULT_TYPE,
        "self_orientation_result_version": CURRENT_SELF_ORIENTATION_RESULT_VERSION,
        "generated_at": _now_iso(),
        "resolver_module": RESOLVER_MODULE,
    }


def _summary_from_result(result: Mapping[str, Any]) -> dict[str, Any]:
    selected = result.get("selected_orientation_inputs")
    selected = selected if isinstance(selected, Mapping) else {}
    body_pass = selected.get("selected_body_pass_result")
    body_pass = body_pass if isinstance(body_pass, Mapping) else {}
    source = selected.get("selected_source_surface")
    source = source if isinstance(source, Mapping) else {}
    answer = selected.get("selected_current_state_answer_read_result")
    answer = answer if isinstance(answer, Mapping) else {}
    checks = result.get("bounded_correspondence_checks")
    checks = checks if isinstance(checks, list) else []
    block = result.get("block")
    block = block if isinstance(block, Mapping) else {}
    continuity = result.get("recognized_continuity_surfaces")
    continuity = continuity if isinstance(continuity, Mapping) else {}
    derivative = result.get("recognized_derivative_surfaces")
    derivative = derivative if isinstance(derivative, Mapping) else {}
    operator = result.get("recognized_operator_facing_surfaces")
    operator = operator if isinstance(operator, Mapping) else {}
    non_claims = result.get("non_claims")
    non_claims = non_claims if isinstance(non_claims, Mapping) else {}
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "selected_body_pass_result_id": body_pass.get("result_id"),
        "selected_source_surface_id": source.get("result_id"),
        "selected_current_state_answer_read_id": answer.get("result_id"),
        "current_executable_core_line_recognized": bool(
            result.get("recognized_current_executable_core_line")
        ),
        "governing_effective_basis_recognized": bool(
            _require_mapping(
                result.get("recognized_governing_effective_basis"),
                "recognized_governing_effective_basis",
                "SOURCE_ARTIFACT_MALFORMED",
            ).get("recognized_from_explicit_effective_references")
        )
        if isinstance(result.get("recognized_governing_effective_basis"), Mapping)
        else False,
        "continuity_surfaces_recognized": bool(continuity),
        "derivative_surfaces_recognized": bool(derivative),
        "operator_surfaces_recognized": bool(operator),
        "correspondence_checks_passed": all(
            isinstance(check, Mapping) and check.get("passed") is True for check in checks
        ),
        "non_claims": dict(non_claims),
    }


def _self_orientation_basis(
    discovery_mode: str,
    selected_inputs: Mapping[str, Any],
    effective_references: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "orientation_anchor": "v0_body_pass_result",
        "orientation_selection_mode": discovery_mode,
        "selected_body_pass_result_id": _require_mapping(
            selected_inputs.get("selected_body_pass_result"),
            "selected_body_pass_result",
            "SOURCE_ARTIFACT_MALFORMED",
        ).get("result_id"),
        "selected_source_surface_id": _require_mapping(
            selected_inputs.get("selected_source_surface"),
            "selected_source_surface",
            "SOURCE_ARTIFACT_MALFORMED",
        ).get("result_id"),
        "selected_current_state_answer_read_id": _require_mapping(
            selected_inputs.get("selected_current_state_answer_read_result"),
            "selected_current_state_answer_read_result",
            "SOURCE_ARTIFACT_MALFORMED",
        ).get("result_id"),
        "effective_references": dict(effective_references),
    }


def _blocked_result(
    *,
    block_code: str,
    block_detail: str | None,
    selected_inputs: Mapping[str, Any],
) -> dict[str, Any]:
    body_pass = selected_inputs.get("selected_body_pass_result")
    body_pass = body_pass if isinstance(body_pass, Mapping) else {}
    result = {
        "current_self_orientation_metadata": _metadata(
            _string_or_none(body_pass.get("result_id")),
            OUTCOME_BLOCKED,
        ),
        "selected_orientation_inputs": dict(selected_inputs),
        "recognized_current_executable_core_line": {},
        "recognized_governing_effective_basis": {},
        "recognized_current_state_surfaces": {},
        "recognized_continuity_surfaces": {},
        "recognized_derivative_surfaces": {},
        "recognized_operator_facing_surfaces": {},
        "recognized_open_surfaces": {},
        "recognized_blocked_or_refused_surfaces": [],
        "recognized_touch_admissibility_surfaces": {},
        "bounded_correspondence_checks": [],
        "outcome": OUTCOME_BLOCKED,
        "block": {
            "block_code": block_code,
            "block_reason": _block_reason(block_code, block_detail),
        },
        "self_orientation_basis": {},
        "current_self_orientation_summary": {},
        "non_claims": dict(NON_CLAIM_DEFAULTS),
    }
    result["current_self_orientation_summary"] = _summary_from_result(result)
    return result


def _self_oriented_result(
    *,
    selected_inputs: Mapping[str, Any],
    recognized_current_executable_core_line: Mapping[str, Any],
    recognized_governing_effective_basis: Mapping[str, Any],
    recognized_current_state_surfaces: Mapping[str, Any],
    recognized_continuity_surfaces: Mapping[str, Any],
    recognized_derivative_surfaces: Mapping[str, Any],
    recognized_operator_facing_surfaces: Mapping[str, Any],
    recognized_open_surfaces: Mapping[str, Any],
    recognized_blocked_or_refused_surfaces: Sequence[Mapping[str, Any]],
    recognized_touch_admissibility_surfaces: Mapping[str, Any],
    bounded_correspondence_checks: Sequence[Mapping[str, Any]],
    self_orientation_basis: Mapping[str, Any],
    non_claims: Mapping[str, Any],
) -> dict[str, Any]:
    body_pass = _require_mapping(
        selected_inputs.get("selected_body_pass_result"),
        "selected_body_pass_result",
        "SOURCE_ARTIFACT_MALFORMED",
    )
    result = {
        "current_self_orientation_metadata": _metadata(
            _string_or_none(body_pass.get("result_id")),
            OUTCOME_SELF_ORIENTED,
        ),
        "selected_orientation_inputs": dict(selected_inputs),
        "recognized_current_executable_core_line": dict(
            recognized_current_executable_core_line
        ),
        "recognized_governing_effective_basis": dict(
            recognized_governing_effective_basis
        ),
        "recognized_current_state_surfaces": dict(recognized_current_state_surfaces),
        "recognized_continuity_surfaces": dict(recognized_continuity_surfaces),
        "recognized_derivative_surfaces": dict(recognized_derivative_surfaces),
        "recognized_operator_facing_surfaces": dict(
            recognized_operator_facing_surfaces
        ),
        "recognized_open_surfaces": dict(recognized_open_surfaces),
        "recognized_blocked_or_refused_surfaces": list(
            recognized_blocked_or_refused_surfaces
        ),
        "recognized_touch_admissibility_surfaces": dict(
            recognized_touch_admissibility_surfaces
        ),
        "bounded_correspondence_checks": list(bounded_correspondence_checks),
        "outcome": OUTCOME_SELF_ORIENTED,
        "block": {"block_code": None, "block_reason": None},
        "self_orientation_basis": dict(self_orientation_basis),
        "current_self_orientation_summary": {},
        "non_claims": dict(non_claims),
    }
    result["current_self_orientation_summary"] = _summary_from_result(result)
    return result


def _resolve_current_self_orientation_internal(
    body_pass_result: Mapping[str, Any] | None = None,
    body_pass_result_path: Path | str | None = None,
) -> dict[str, Any]:
    selected_path, selected_body_pass, discovery_mode = _selected_body_pass_artifact(
        body_pass_result=body_pass_result,
        body_pass_result_path=body_pass_result_path,
    )
    selected_inputs = _body_pass_selected_inputs(selected_body_pass, selected_path)

    seam_path, seam_result = _read_selected_artifact(
        _require_mapping(
            selected_inputs.get("selected_seam_result"),
            "selected_seam_result",
            "SOURCE_ARTIFACT_MALFORMED",
        ),
        context="selected continuity-memory seam result",
        metadata_key="continuity_memory_seam_metadata",
        metadata_id_key="continuity_memory_seam_result_id",
        expected_outcome=seam_resolver.OUTCOME_SEAM_CLOSED,
    )
    action_path, action_result = _read_selected_artifact(
        _require_mapping(
            selected_inputs.get("selected_action_permission_result"),
            "selected_action_permission_result",
            "SOURCE_ARTIFACT_MALFORMED",
        ),
        context="selected received-derivative action-permission result",
        metadata_key="received_derivative_action_permission_metadata",
        metadata_id_key="received_derivative_action_permission_result_id",
        expected_outcome=action_resolver.OUTCOME_ACTION_PERMITTED,
    )
    participation_path, participation_result = _read_selected_artifact(
        _require_mapping(
            selected_inputs.get("selected_participation_result"),
            "selected_participation_result",
            "SOURCE_ARTIFACT_MALFORMED",
        ),
        context="selected received-derivative participation result",
        metadata_key="received_derivative_participation_metadata",
        metadata_id_key="received_derivative_participation_result_id",
        expected_outcome=participation_resolver.OUTCOME_PARTICIPATED,
    )
    receipt_path, receipt_result = _read_selected_artifact(
        _require_mapping(
            selected_inputs.get("selected_receipt_result"),
            "selected_receipt_result",
            "SOURCE_ARTIFACT_MALFORMED",
        ),
        context="selected continuity-transfer receipt result",
        metadata_key="continuity_transfer_receipt_metadata",
        metadata_id_key="continuity_transfer_receipt_result_id",
        expected_outcome=receipt_resolver.OUTCOME_RECEIVED,
    )
    transfer_path, transfer_result = _read_selected_artifact(
        _require_mapping(
            selected_inputs.get("selected_transfer_result"),
            "selected_transfer_result",
            "SOURCE_ARTIFACT_MALFORMED",
        ),
        context="selected continuity-transfer unit result",
        metadata_key="continuity_transfer_metadata",
        metadata_id_key="continuity_transfer_result_id",
        expected_outcome=transfer_resolver.OUTCOME_TRANSFERRED,
    )
    touch_path, touch_result = _read_selected_artifact(
        _require_mapping(
            selected_inputs.get("selected_touch_permission_result"),
            "selected_touch_permission_result",
            "SOURCE_ARTIFACT_MALFORMED",
        ),
        context="selected touch-permission result",
        metadata_key="touch_permission_metadata",
        metadata_id_key="touch_permission_result_id",
        expected_outcome=touch_resolver.OUTCOME_ADMITTED_FOR_TOUCH,
    )
    stand_path, stand_result = _read_selected_artifact(
        _require_mapping(
            selected_inputs.get("selected_source_surface"),
            "selected_source_surface",
            "SOURCE_ARTIFACT_MALFORMED",
        ),
        context="selected what-stands-now result",
        metadata_key="what_stands_now_metadata",
        metadata_id_key="what_stands_now_result_id",
        expected_outcome=stand_resolver.OUTCOME_ANSWERED_WHAT_STANDS_NOW,
    )

    source_identity = _what_stands_now_identity(stand_result, stand_path)
    selected_inputs["selected_source_surface"] = dict(source_identity)
    selected_inputs["selected_current_state_what_stands_now_result"] = dict(source_identity)

    effective_references = dict(
        _extract_canonical_effective_references(
            _require_mapping(
                _require_mapping(
                    selected_body_pass.get("selected_source_surface"),
                    "selected_source_surface",
                    "SOURCE_ARTIFACT_MALFORMED",
                ).get("selected_source_surface_effective_references"),
                "selected_source_surface_effective_references",
                "CURRENT_EFFECTIVE_BASIS_ABSENT_OR_AMBIGUOUS",
            )
        )
    )
    if not _effective_references_match(
        effective_references,
        _require_mapping(
            stand_result.get("effective_stand_now_inputs"),
            "effective_stand_now_inputs",
            "SOURCE_ARTIFACT_MALFORMED",
        ),
    ):
        raise CurrentSelfOrientationError(
            "selected what-stands-now result does not correspond to the selected effective basis",
            "CORRESPONDENCE_CHECK_FAILED",
        )
    selected_inputs["selected_effective_references"] = dict(effective_references)

    effective_bundle = _read_effective_artifact_bundle(effective_references)

    answer_path, answer_result, answer_summary = _read_answer_read_result(
        stand_result,
        effective_references,
    )
    answer_identity = _answer_read_identity(answer_result, answer_path)
    selected_inputs["selected_current_state_answer_read_result"] = dict(answer_identity)

    selected_answer_id = _string_required(
        answer_identity.get("result_id"),
        "selected current-state answer/read result id",
        "CURRENT_STATE_SURFACE_ABSENT_WHERE_REQUIRED",
    )
    query_results = _discover_matching_query_results(selected_answer_id, effective_references)
    open_results = _discover_matching_what_remains_open_results(
        selected_answer_id,
        effective_references,
    )
    selected_inputs["selected_current_state_query_results"] = [
        _query_identity(artifact, path) for path, artifact, _summary in query_results
    ]
    selected_inputs["selected_current_state_what_remains_open_results"] = [
        _what_remains_open_identity(artifact, path)
        for path, artifact, _summary in open_results
    ]

    selected_source_surface_id = _string_required(
        source_identity.get("result_id"),
        "selected source surface id",
        "CURRENT_STATE_SURFACE_ABSENT_WHERE_REQUIRED",
    )
    vessel_results = _discover_matching_vessel_results(
        selected_source_surface_id,
        effective_references,
    )
    selected_inputs["selected_vessel_results"] = [
        _vessel_identity(artifact, path) for path, artifact, _summary in vessel_results
    ]
    vessel_ids = {
        _string_required(
            _vessel_identity(artifact, path).get("result_id"),
            "matched vessel result id",
            "DERIVATIVE_SURFACE_SOURCE_BASIS_MISSING",
        )
        for path, artifact, _summary in vessel_results
    }
    operator_results = _discover_matching_operator_brief_results(
        selected_source_surface_id,
        vessel_ids,
    )
    selected_inputs["selected_operator_terminal_brief_results"] = [
        _brief_identity(artifact, path)
        for path, artifact, _summary in operator_results
    ]

    _validate_false_non_claims(
        "selected what-stands-now result",
        stand_result,
        stand_resolver.NON_CLAIM_DEFAULTS,
    )
    _validate_false_non_claims(
        "selected touch-permission result",
        touch_result,
        touch_resolver.NON_CLAIM_DEFAULTS,
    )
    _validate_false_non_claims(
        "selected continuity transfer result",
        transfer_result,
        transfer_resolver.NON_CLAIM_DEFAULTS,
    )
    _validate_false_non_claims(
        "selected continuity transfer receipt result",
        receipt_result,
        receipt_resolver.NON_CLAIM_DEFAULTS,
    )
    _validate_false_non_claims(
        "selected participation result",
        participation_result,
        participation_resolver.NON_CLAIM_DEFAULTS,
    )
    _validate_false_non_claims(
        "selected action-permission result",
        action_result,
        action_resolver.NON_CLAIM_DEFAULTS,
    )
    _validate_false_non_claims(
        "selected continuity memory seam result",
        seam_result,
        seam_resolver.NON_CLAIM_DEFAULTS,
    )
    for _path, artifact, _summary in query_results:
        _validate_false_non_claims(
            "current-state query result",
            artifact,
            query_resolver.NON_CLAIM_DEFAULTS,
        )
    for _path, artifact, _summary in open_results:
        _validate_false_non_claims(
            "what-remains-open result",
            artifact,
            open_resolver.NON_CLAIM_DEFAULTS,
        )
    for _path, artifact, _summary in vessel_results:
        _validate_false_non_claims(
            "vessel v3 result",
            artifact,
            vessel_resolver.NON_CLAIM_DEFAULTS,
        )
    for _path, artifact, _summary in operator_results:
        _validate_false_non_claims(
            "operator terminal brief result",
            artifact,
            brief_resolver.NON_CLAIM_DEFAULTS,
        )

    _validate_derivative_posture(
        transfer_result,
        receipt_result,
        participation_result,
        action_result,
        [artifact for _path, artifact, _summary in vessel_results],
        [artifact for _path, artifact, _summary in operator_results],
    )
    _check_open_posture([artifact for _path, artifact, _summary in open_results])

    stand_summary = stand_resolver.build_current_state_what_stands_now_summary(stand_result)
    recognized_current_executable_core_line = _recognized_current_executable_core_line(
        _body_pass_identity(selected_body_pass, selected_path),
        _seam_identity(seam_result, seam_path),
        source_identity,
        effective_references,
    )
    recognized_governing_effective_basis = _recognized_governing_effective_basis(
        effective_references,
        effective_bundle,
    )
    recognized_current_state_surfaces = _recognized_current_state_surfaces(
        answer_identity,
        answer_summary,
        query_results,
        source_identity,
        stand_summary,
        open_results,
    )
    recognized_continuity_surfaces = _recognized_continuity_surfaces(
        transfer_result,
        transfer_path,
        receipt_result,
        receipt_path,
        seam_result,
        seam_path,
        selected_body_pass,
        selected_path,
    )
    recognized_derivative_surfaces = _recognized_derivative_surfaces(
        participation_result,
        participation_path,
        action_result,
        action_path,
        vessel_results,
    )
    recognized_operator_facing_surfaces = _recognized_operator_facing_surfaces(
        operator_results
    )
    all_non_claim_artifacts = [
        effective_bundle["family"],
        effective_bundle["status"],
        effective_bundle["governing"],
        answer_result,
        stand_result,
        touch_result,
        transfer_result,
        receipt_result,
        participation_result,
        action_result,
        seam_result,
        selected_body_pass,
        *[artifact for _path, artifact, _summary in query_results],
        *[artifact for _path, artifact, _summary in open_results],
        *[artifact for _path, artifact, _summary in vessel_results],
        *[artifact for _path, artifact, _summary in operator_results],
    ]
    merged_non_claims = _merge_non_claims(all_non_claim_artifacts)
    recognized_open_surfaces = _recognized_open_surfaces(open_results, merged_non_claims)
    recognized_touch_admissibility_surfaces = _recognized_touch_admissibility_surfaces(
        touch_result,
        touch_path,
    )
    recognized_blocked_or_refused_surfaces = _recognized_blocked_or_refused_surfaces(
        query_results,
        open_results,
        vessel_results,
        operator_results,
    )

    recognized_sections = {
        "recognized_current_executable_core_line": recognized_current_executable_core_line,
        "recognized_governing_effective_basis": recognized_governing_effective_basis,
        "recognized_current_state_surfaces": recognized_current_state_surfaces,
        "recognized_continuity_surfaces": recognized_continuity_surfaces,
        "recognized_derivative_surfaces": recognized_derivative_surfaces,
        "recognized_operator_facing_surfaces": recognized_operator_facing_surfaces,
        "recognized_open_surfaces": recognized_open_surfaces,
        "recognized_blocked_or_refused_surfaces": recognized_blocked_or_refused_surfaces,
        "recognized_touch_admissibility_surfaces": recognized_touch_admissibility_surfaces,
    }
    checks = _build_correspondence_checks(
        discovery_mode=discovery_mode,
        body_pass_result=selected_body_pass,
        answer_read_result=answer_result,
        query_results=query_results,
        stand_result=stand_result,
        open_results=open_results,
        touch_result=touch_result,
        transfer_result=transfer_result,
        receipt_result=receipt_result,
        participation_result=participation_result,
        action_result=action_result,
        seam_result=seam_result,
        vessel_results=vessel_results,
        operator_results=operator_results,
        non_claims=merged_non_claims,
        blocked_or_refused_surfaces=recognized_blocked_or_refused_surfaces,
        effective_references=effective_references,
        recognized_sections=recognized_sections,
    )
    failed_check = _first_failed(checks)
    if failed_check is not None:
        raise CurrentSelfOrientationError(
            f"bounded correspondence check failed: {failed_check.get('check_name')}",
            _string_or_none(failed_check.get("block_code")) or "CORRESPONDENCE_CHECK_FAILED",
        )

    self_orientation_basis = _self_orientation_basis(
        discovery_mode,
        selected_inputs,
        effective_references,
    )
    return _self_oriented_result(
        selected_inputs=selected_inputs,
        recognized_current_executable_core_line=recognized_current_executable_core_line,
        recognized_governing_effective_basis=recognized_governing_effective_basis,
        recognized_current_state_surfaces=recognized_current_state_surfaces,
        recognized_continuity_surfaces=recognized_continuity_surfaces,
        recognized_derivative_surfaces=recognized_derivative_surfaces,
        recognized_operator_facing_surfaces=recognized_operator_facing_surfaces,
        recognized_open_surfaces=recognized_open_surfaces,
        recognized_blocked_or_refused_surfaces=recognized_blocked_or_refused_surfaces,
        recognized_touch_admissibility_surfaces=recognized_touch_admissibility_surfaces,
        bounded_correspondence_checks=checks,
        self_orientation_basis=self_orientation_basis,
        non_claims=merged_non_claims,
    )


def resolve_current_self_orientation(
    body_pass_result: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded current self-orientation from a body-pass basis."""

    selected_inputs = _empty_selected_orientation_inputs("provided_mapping")
    try:
        return _resolve_current_self_orientation_internal(body_pass_result=body_pass_result)
    except CurrentSelfOrientationError as exc:
        if body_pass_result is not None and isinstance(body_pass_result, Mapping):
            try:
                selected_inputs = _body_pass_selected_inputs(body_pass_result, "provided_mapping")
            except CurrentSelfOrientationError:
                selected_inputs = _empty_selected_orientation_inputs("provided_mapping")
        return _blocked_result(
            block_code=exc.block_code or "CORRESPONDENCE_CHECK_FAILED",
            block_detail=str(exc),
            selected_inputs=selected_inputs,
        )


def resolve_current_self_orientation_from_path(
    body_pass_result_path: Path | str,
) -> dict[str, Any]:
    """Resolve one bounded current self-orientation from an explicit path."""

    selected_inputs = _empty_selected_orientation_inputs(body_pass_result_path)
    try:
        return _resolve_current_self_orientation_internal(
            body_pass_result_path=body_pass_result_path
        )
    except CurrentSelfOrientationError as exc:
        try:
            artifact = _read_json_file(
                body_pass_result_path,
                context="selected v0 body pass result",
                missing_code="REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
                unreadable_code="REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
                malformed_code="SOURCE_ARTIFACT_MALFORMED",
            )
            if isinstance(artifact, Mapping):
                selected_inputs = _body_pass_selected_inputs(
                    artifact,
                    _repo_path(body_pass_result_path),
                )
        except CurrentSelfOrientationError:
            selected_inputs = _empty_selected_orientation_inputs(body_pass_result_path)
        return _blocked_result(
            block_code=exc.block_code or "CORRESPONDENCE_CHECK_FAILED",
            block_detail=str(exc),
            selected_inputs=selected_inputs,
        )


def build_current_self_orientation_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return a bounded summary for one current self-orientation result."""

    if not isinstance(result, Mapping):
        raise CurrentSelfOrientationError("self-orientation result must be a mapping")
    return _summary_from_result(result)


def _safe_default_output_path(
    result: Mapping[str, Any],
    root: Path | str = CURRENT_SELF_ORIENTATION_ROOT,
) -> Path:
    resolved_root = _repo_path(root)
    stem = _safe_filename_part(_body_pass_result_id_for_filename(result))
    candidate = resolved_root / f"{stem}__{DEFAULT_RESULT_STEM}.json"
    if not candidate.exists():
        return candidate
    for index in range(1, 1000):
        candidate = resolved_root / f"{stem}__{DEFAULT_RESULT_STEM}_{index:03d}.json"
        if not candidate.exists():
            return candidate
    raise CurrentSelfOrientationError(
        "no bounded self-orientation filename is available",
        "SOURCE_ARTIFACT_MALFORMED",
    )


def write_current_self_orientation_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive bounded current self-orientation JSON artifact."""

    if not isinstance(result, Mapping):
        raise CurrentSelfOrientationError("self-orientation result must be a mapping")

    target = (
        _repo_path(output_path)
        if output_path is not None
        else _safe_default_output_path(result)
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(f"current self-orientation result already exists: {target}")
    with target.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target
