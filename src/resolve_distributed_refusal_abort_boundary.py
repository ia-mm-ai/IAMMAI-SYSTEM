"""Resolve the distributed refusal / abort boundary.

This module records refusal, abort, stop, and non-admission postures only.
It does not refuse or abort a live operation, admit operation, authorize
operation, execute operation, authorize synchronization, authorize
non-synchronized operation, transfer the body, create a second body, activate
carrier roles, create consequence, create public readiness, claim final
completion, or schedule follow-on work.
"""

from __future__ import annotations

import copy
import datetime
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any


class DistributedRefusalAbortBoundaryError(Exception):
    """Raised for impossible refusal / abort boundary resolver failures."""


RESOLVER_MODULE = "resolve_distributed_refusal_abort_boundary"
RESULT_VERSION = "0.1.0"
RESULT_TYPE = "distributed_refusal_abort_boundary_result"

DISTRIBUTED_REFUSAL_ABORT_BOUNDARY_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_distributed_refusal_abort_boundary"
)

EXPECTED_SELECTED_SYNC_NON_SYNC_OUTCOME = "DISTRIBUTED_SYNC_NON_SYNC_BOUNDARY_RECORDED"

OUTCOME_RECORDED = "DISTRIBUTED_REFUSAL_ABORT_BOUNDARY_RECORDED"
OUTCOME_NOT_SUFFICIENT = "DISTRIBUTED_REFUSAL_ABORT_BOUNDARY_NOT_SUFFICIENT"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = "DISTRIBUTED_REFUSAL_ABORT_REQUIRES_ADDITIONAL_BASIS"
OUTCOME_BLOCKED = "DISTRIBUTED_REFUSAL_ABORT_REVIEW_BLOCKED"

OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_SUFFICIENT,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = "RECORD_DISTRIBUTED_REFUSAL_ABORT_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_DISTRIBUTED_REFUSAL_ABORT_BOUNDARY"
INTENT_BLOCK = "BLOCK_DISTRIBUTED_REFUSAL_ABORT_REVIEW"

SUPPORTED_INTENTS = (
    INTENT_RECORD,
    INTENT_DO_NOT_RECORD,
    INTENT_BLOCK,
)

SUPPORTED_REFUSAL_ABORT_POSTURES = (
    "NO_OPERATION_ADMISSION_WITHOUT_REFUSAL_ABORT_BOUNDARY",
    "NO_OPERATION_ADMISSION_WHEN_REQUIRED_BASIS_MISSING",
    "NO_OPERATION_ADMISSION_WHEN_CARRIER_REFUSAL_HIDDEN",
    "NO_OPERATION_ADMISSION_WHEN_BLOCKED_ATTEMPT_HIDDEN",
    "NO_OPERATION_ADMISSION_WHEN_DIVERGENCE_HIDDEN",
    "NO_OPERATION_ADMISSION_WHEN_PROJECTION_MISMATCH_HIDDEN",
    "NO_OPERATION_ADMISSION_WHEN_SYNC_STATUS_OVERREAD",
    "NO_OPERATION_ADMISSION_WHEN_NO_SYNC_OVERREAD",
    "NO_OPERATION_ADMISSION_WHEN_CARRIER_ROLE_ACTIVATED_PREMATURELY",
    "NO_OPERATION_ADMISSION_WHEN_AUTHORITY_GRANTED_BY_IMPLICATION",
    "NO_OPERATION_ADMISSION_WHEN_CONSEQUENCE_IMPLIED",
    "ABORT_IF_OPERATION_SCOPE_EXPANDS",
    "ABORT_IF_SYNC_OR_MERGE_ATTEMPTED_WITHOUT_AUTHORITY",
    "ABORT_IF_NON_SYNC_OPERATION_ATTEMPTED_WITHOUT_ADMISSION",
    "ABORT_IF_CARRIER_AUTHORITY_OR_CURRENTNESS_CREATED",
    "ABORT_IF_WINNER_LOSER_CARRIER_SELECTION_OCCURS",
    "ABORT_IF_SOURCE_REPLACEMENT_ATTEMPTED",
    "ABORT_IF_EVIDENCE_OR_REFUSAL_ERASURE_ATTEMPTED",
    "ABORT_IF_CONSEQUENCE_CREATED_WITHOUT_ACTION_BOUNDARY",
    "FUTURE_ABORT_EXECUTION_REQUIRES_ADMITTED_OPERATION_CONTEXT",
)

REQUIRED_NON_CLAIMS = (
    "live_operation_refused",
    "live_operation_aborted",
    "operation_admitted",
    "operation_authorized",
    "operation_executed",
    "repository_synchronization_authorized",
    "shared_live_state_created",
    "state_merge_authorized",
    "replay_authorized",
    "full_body_transfer_authorized",
    "second_body_created",
    "non_synchronized_operation_authorized",
    "carrier_autonomy_authorized",
    "stale_carrier_operation_authorized",
    "carrier_role_activated",
    "carrier_role_assigned_for_operation",
    "carrier_authority_created",
    "carrier_currentness_created",
    "current_carrier_selected",
    "winning_carrier_selected",
    "losing_carrier_invalidated",
    "carrier_hierarchy_created",
    "source_replaced",
    "authority_created",
    "permission_created",
    "truth_created",
    "action_authorized",
    "consequence_created",
    "divergence_resolved",
    "evidence_erased",
    "refusal_erased",
    "blocked_attempt_erased",
    "projection_mismatch_hidden",
    "public_launch_readiness_created",
    "final_completion_claimed",
    "follow_on_work_authorized",
    "self_orientation_successor_scheduled",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
)

VISIBLE_POSTURE_DEFAULTS = {
    "carrier_evidence_remains_unmerged": True,
    "carrier_context_remains_context_only": True,
    "divergence_remains_visible": True,
    "refusal_remains_visible": True,
    "blocked_attempts_remain_visible": True,
    "projection_mismatch_remains_visible": True,
}

WHAT_REMAINS_OPEN = {
    "distributed_operation_admission_transition_authority": "open_not_scheduled_not_authorized_not_executed",
    "distributed_execution_emission_boundary": "open_not_scheduled_not_authorized_not_executed",
    "distributed_action_consequence_boundary": "open_not_scheduled_not_authorized_not_executed",
    "distributed_operation_receipt_exhaustion": "open_not_scheduled_not_authorized_not_executed",
    "distributed_operation_conformance": "open_not_scheduled_not_authorized_not_executed",
    "distributed_operation_closure": "open_not_scheduled_not_authorized_not_executed",
    "distributed_operation_itself": "open_not_scheduled_not_authorized_not_executed",
    "repository_synchronization": "open_not_scheduled_not_authorized_not_executed",
    "non_synchronized_operation": "open_not_scheduled_not_authorized_not_executed",
    "full_body_transfer": "open_not_scheduled_not_authorized_not_executed",
    "second_body_creation": "open_not_scheduled_not_authorized_not_executed",
    "current_self_orientation_v10": "open_not_scheduled_not_authorized_not_executed",
    "public_launch_readiness": "open_not_scheduled_not_authorized_not_executed",
    "final_governance": "open_not_scheduled_not_authorized_not_executed",
    "final_continuity_completion": "open_not_scheduled_not_authorized_not_executed",
    "final_system_identity": "open_not_scheduled_not_authorized_not_executed",
    "open_means_not_scheduled": True,
    "open_means_not_authorized": True,
    "open_means_not_executed": True,
}

COLLAPSE_FIELDS = (
    (
        "REFUSAL_ABORT_REVIEW_REFUSES_LIVE_OPERATION",
        (
            "live_operation_refused",
            "operation_refused",
            "refuses_live_operation",
        ),
    ),
    (
        "REFUSAL_ABORT_REVIEW_ABORTS_LIVE_OPERATION",
        (
            "live_operation_aborted",
            "operation_aborted",
            "aborts_live_operation",
        ),
    ),
    ("REFUSAL_ABORT_REVIEW_ADMITS_OPERATION", ("operation_admitted",)),
    (
        "REFUSAL_ABORT_REVIEW_AUTHORIZES_OPERATION",
        (
            "operation_authorized",
            "distributed_operation_authorized",
        ),
    ),
    ("REFUSAL_ABORT_REVIEW_EXECUTES_OPERATION", ("operation_executed",)),
    (
        "REFUSAL_ABORT_REVIEW_AUTHORIZES_SYNCHRONIZATION",
        (
            "repository_synchronization_authorized",
            "synchronization_authorized",
            "sync_authorized",
            "repository_sync_authorized",
            "shared_live_state_created",
            "state_merge_authorized",
            "replay_authorized",
            "merge_authorized",
            "state_merge_created",
        ),
    ),
    (
        "REFUSAL_ABORT_REVIEW_AUTHORIZES_NON_SYNCHRONIZED_OPERATION",
        (
            "non_synchronized_operation_authorized",
            "non_sync_operation_authorized",
            "divergent_live_operation_authorized",
        ),
    ),
    (
        "REFUSAL_ABORT_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER",
        (
            "full_body_transfer_authorized",
            "full_body_transfer_created",
        ),
    ),
    (
        "REFUSAL_ABORT_REVIEW_CREATES_SECOND_BODY",
        (
            "second_body_created",
            "second_body_authorized",
        ),
    ),
    (
        "REFUSAL_ABORT_REVIEW_ACTIVATES_CARRIER_ROLES",
        (
            "carrier_role_activated",
            "carrier_roles_activated",
            "carrier_role_assigned_for_operation",
            "carrier_roles_assigned_for_operation",
            "carrier_assigned_to_live_operation",
        ),
    ),
    (
        "REFUSAL_ABORT_REVIEW_CREATES_CARRIER_AUTHORITY",
        (
            "carrier_authority_created",
            "authority_created",
            "authority_granted",
            "carrier_authority_granted",
        ),
    ),
    (
        "REFUSAL_ABORT_REVIEW_CREATES_CARRIER_CURRENTNESS",
        (
            "carrier_currentness_created",
            "currentness_created",
        ),
    ),
    ("REFUSAL_ABORT_REVIEW_SELECTS_CURRENT_CARRIER", ("current_carrier_selected",)),
    (
        "REFUSAL_ABORT_REVIEW_SELECTS_WINNING_CARRIER",
        (
            "winning_carrier_selected",
            "carrier_b_success_becomes_winner",
            "carrier_b_success_forces_continuation",
        ),
    ),
    (
        "REFUSAL_ABORT_REVIEW_INVALIDATES_LOSING_CARRIER",
        (
            "losing_carrier_invalidated",
            "carrier_c_block_becomes_loser",
            "carrier_c_block_invalidates_carrier_c",
        ),
    ),
    (
        "REFUSAL_ABORT_REVIEW_REPLACES_SOURCE",
        (
            "source_replaced",
            "source_replaced_by_carrier",
            "carrier_becomes_source",
        ),
    ),
    (
        "REFUSAL_ABORT_REVIEW_CREATES_TRUTH_OR_ACTION",
        (
            "truth_created",
            "action_authorized",
            "truth_action_created",
        ),
    ),
    ("REFUSAL_ABORT_REVIEW_CREATES_CONSEQUENCE", ("consequence_created",)),
    ("REFUSAL_ABORT_REVIEW_RESOLVES_DIVERGENCE", ("divergence_resolved",)),
    (
        "REFUSAL_ABORT_REVIEW_ERASES_EVIDENCE_OR_REFUSAL",
        (
            "evidence_erased",
            "refusal_erased",
            "blocked_attempt_erased",
            "projection_mismatch_hidden",
            "refusal_hidden",
            "blocked_attempt_hidden",
            "blocked_attempts_hidden",
            "b_c_divergence_hidden",
            "divergence_hidden",
        ),
    ),
    (
        "REFUSAL_ABORT_REVIEW_CREATES_PUBLIC_READINESS",
        (
            "public_launch_readiness_created",
            "public_readiness_created",
        ),
    ),
    (
        "REFUSAL_ABORT_REVIEW_CLAIMS_FINAL_COMPLETION",
        (
            "final_completion_claimed",
            "final_governance_completed",
            "final_continuity_completed",
            "final_system_identity_completed",
        ),
    ),
    (
        "REFUSAL_ABORT_REVIEW_SCHEDULES_FOLLOW_ON_WORK",
        (
            "follow_on_work_authorized",
            "follow_on_work_scheduled",
            "self_orientation_successor_scheduled",
            "continuation_authorized",
        ),
    ),
    (
        "MUTATION_REPLAY_OR_MERGE_DETECTED",
        (
            "mutation_performed",
            "replay_performed",
            "merge_performed",
        ),
    ),
)


def _utc_now() -> str:
    return datetime.datetime.now(datetime.UTC).replace(microsecond=0).isoformat()


def _copy(value: Any) -> Any:
    return copy.deepcopy(value)


def _is_mapping(value: Any) -> bool:
    return isinstance(value, Mapping)


def _as_mapping(value: Any) -> dict[str, Any]:
    return dict(value) if isinstance(value, Mapping) else {}


def _is_sequence_not_text(value: Any) -> bool:
    return isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray))


def _is_non_empty(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (Mapping, Sequence)) and not isinstance(value, (bytes, bytearray)):
        return bool(value)
    return True


def _is_true(value: Any) -> bool:
    return value is True


def _is_false(value: Any) -> bool:
    return value is False


def _get_path_value(value: Any, path: Sequence[str]) -> Any:
    current = value
    for key in path:
        if not isinstance(current, Mapping) or key not in current:
            return None
        current = current[key]
    return current


def _first_present(*values: Any) -> Any:
    for value in values:
        if _is_non_empty(value):
            return value
    return None


def _first_present_allow_zero(*values: Any) -> Any:
    for value in values:
        if value == 0 or _is_non_empty(value):
            return value
    return None


def _stringify(value: Any) -> str:
    if value is None:
        return ""
    return str(value)


def _read_json_object(path: Path) -> tuple[dict[str, Any] | None, str | None, str | None]:
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        return None, "unreadable", str(exc)
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        return None, "malformed", str(exc)
    if not isinstance(parsed, Mapping):
        return None, "malformed", "JSON value is not an object"
    return dict(parsed), None, None


def _make_check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    failure_code: str,
) -> dict[str, Any]:
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": expected_posture,
        "actual_posture": actual_posture,
        "failure_code": None if passed else failure_code,
        "block_code": None if passed else failure_code,
    }


def _passed_check_count(checks: Sequence[Mapping[str, Any]]) -> int:
    return sum(1 for check in checks if check.get("passed") is True)


def _failed_check_count(checks: Sequence[Mapping[str, Any]]) -> int:
    return sum(1 for check in checks if check.get("passed") is not True)


def _first_failed_code(checks: Sequence[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is not True:
            code = check.get("block_code") or check.get("failure_code")
            if code:
                return str(code)
    return None


def _required_non_claims_false() -> dict[str, bool]:
    return {key: False for key in REQUIRED_NON_CLAIMS}


def _declared_non_claims_are_false(request: Mapping[str, Any]) -> bool:
    non_claims = request.get("declared_non_claims")
    if not isinstance(non_claims, Mapping):
        return False
    for key in REQUIRED_NON_CLAIMS:
        if non_claims.get(key) is not False:
            return False
    return True


def _sanitize_filename(value: Any) -> str:
    raw = _stringify(value).strip() or "distributed_refusal_abort_boundary"
    allowed = []
    for char in raw:
        if char.isalnum() or char in ("-", "_", "."):
            allowed.append(char)
        else:
            allowed.append("_")
    sanitized = "".join(allowed).strip("._")
    return sanitized or "distributed_refusal_abort_boundary"


def _deduplicate_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    counter = 1
    while True:
        candidate = parent / f"{stem}_{counter:03d}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def _extract_request_id(request: Mapping[str, Any]) -> str | None:
    return _first_present(request.get("refusal_abort_request_id"), request.get("request_id"))


def _extract_selected_sync_id(sync_result: Mapping[str, Any], request: Mapping[str, Any]) -> str | None:
    return _first_present(
        request.get("selected_sync_non_sync_result_id"),
        _get_path_value(
            sync_result,
            (
                "distributed_sync_non_sync_metadata",
                "distributed_sync_non_sync_result_id",
            ),
        ),
        sync_result.get("distributed_sync_non_sync_result_id"),
        _get_path_value(sync_result, ("distributed_sync_non_sync_summary", "sync_non_sync_request_id")),
        _get_path_value(sync_result, ("declared_sync_non_sync_question", "sync_non_sync_request_id")),
        sync_result.get("sync_non_sync_request_id"),
        sync_result.get("result_id"),
    )


def _extract_selected_sync_outcome(sync_result: Mapping[str, Any], request: Mapping[str, Any]) -> str | None:
    return _first_present(
        request.get("selected_sync_non_sync_result_outcome"),
        sync_result.get("outcome"),
        _get_path_value(sync_result, ("distributed_sync_non_sync_summary", "outcome")),
        sync_result.get("selected_sync_non_sync_result_outcome"),
    )


def _extract_failed_check_count(result: Mapping[str, Any]) -> int | None:
    candidates = (
        _get_path_value(result, ("distributed_sync_non_sync_summary", "failed_check_count")),
        _get_path_value(result, ("sync_non_sync_statement", "failed_check_count")),
        result.get("failed_check_count"),
    )
    for candidate in candidates:
        if candidate is not None:
            try:
                return int(candidate)
            except (TypeError, ValueError):
                return None
    checks = result.get("sync_non_sync_checks")
    if isinstance(checks, Sequence) and not isinstance(checks, (str, bytes, bytearray)):
        return _failed_check_count([check for check in checks if isinstance(check, Mapping)])
    return None


def _load_selected_sync_non_sync_result(
    request: Mapping[str, Any],
) -> tuple[dict[str, Any], str | None, str | None, str | None]:
    path_value = request.get("selected_sync_non_sync_result_path")
    if _is_non_empty(path_value):
        path = Path(str(path_value))
        loaded, error, detail = _read_json_object(path)
        if error == "unreadable":
            return {}, str(path), "SYNC_NON_SYNC_RESULT_UNREADABLE", detail
        if error == "malformed":
            return {}, str(path), "SYNC_NON_SYNC_RESULT_MALFORMED", detail
        return _copy(loaded), str(path), None, None

    selected = request.get("selected_sync_non_sync_result")
    if isinstance(selected, Mapping):
        return _copy(selected), None, None, None
    if selected is not None:
        return {}, None, "SYNC_NON_SYNC_RESULT_MALFORMED", "selected_sync_non_sync_result is not an object"
    return {}, None, None, None


def _load_request_from_path(path_value: Path | str) -> tuple[dict[str, Any] | None, str | None, str | None]:
    path = Path(path_value)
    loaded, error, detail = _read_json_object(path)
    if error == "unreadable":
        return None, "DECLARED_REFUSAL_ABORT_REQUEST_UNREADABLE", detail
    if error == "malformed":
        return None, "DECLARED_REFUSAL_ABORT_REQUEST_MALFORMED", detail
    assert loaded is not None
    loaded = _copy(loaded)
    loaded["refusal_abort_request_path"] = str(path)
    return loaded, None, None


def _get_section(
    request: Mapping[str, Any],
    sync_result: Mapping[str, Any],
    request_key: str,
    sync_paths: Sequence[Sequence[str]],
) -> Any:
    request_value = request.get(request_key)
    if _is_non_empty(request_value):
        return _copy(request_value)
    for path in sync_paths:
        value = _get_path_value(sync_result, path)
        if _is_non_empty(value):
            return _copy(value)
    return None


def _selected_carrier_role_result(
    request: Mapping[str, Any],
    sync_result: Mapping[str, Any],
) -> Any:
    return _get_section(
        request,
        sync_result,
        "selected_carrier_role_result",
        (
            ("selected_carrier_role_result", "selected_carrier_role_result"),
            ("selected_operation_matter", "selected_carrier_role_result"),
            ("sync_non_sync_basis", "selected_carrier_role_result"),
        ),
    )


def _selected_source_body_authority_result(
    request: Mapping[str, Any],
    sync_result: Mapping[str, Any],
) -> Any:
    return _get_section(
        request,
        sync_result,
        "selected_source_body_authority_result",
        (
            ("selected_operation_matter", "selected_source_body_authority_result"),
            ("refusal_abort_basis", "selected_source_body_authority_result"),
            ("sync_non_sync_basis", "selected_source_body_authority_result"),
            ("selected_carrier_role_result", "selected_operation_matter", "selected_source_body_authority_result"),
        ),
    )


def _selected_eligibility_result(request: Mapping[str, Any], sync_result: Mapping[str, Any]) -> Any:
    return _get_section(
        request,
        sync_result,
        "selected_eligibility_result",
        (
            ("selected_operation_matter", "selected_eligibility_result"),
            ("sync_non_sync_basis", "selected_eligibility_result"),
            ("selected_carrier_role_result", "selected_operation_matter", "selected_eligibility_result"),
        ),
    )


def _selected_matter_declaration(request: Mapping[str, Any], sync_result: Mapping[str, Any]) -> Any:
    return _get_section(
        request,
        sync_result,
        "selected_matter_declaration",
        (
            ("selected_operation_matter", "selected_matter_declaration"),
            ("selected_operation_matter", "selected_matter_declaration_result"),
            ("sync_non_sync_basis", "selected_matter_declaration"),
            ("selected_carrier_role_result", "selected_operation_matter", "selected_matter_declaration"),
        ),
    )


def _selected_operation_candidate(request: Mapping[str, Any], sync_result: Mapping[str, Any]) -> Any:
    return _get_section(
        request,
        sync_result,
        "selected_operation_candidate",
        (
            ("selected_operation_matter", "selected_operation_candidate"),
            ("sync_non_sync_basis", "selected_operation_candidate"),
            ("selected_carrier_role_result", "selected_operation_matter", "selected_operation_candidate"),
        ),
    )


def _selected_operation_matter(request: Mapping[str, Any], sync_result: Mapping[str, Any]) -> Any:
    return _get_section(
        request,
        sync_result,
        "selected_operation_matter",
        (
            ("selected_operation_matter", "selected_operation_matter"),
            ("sync_non_sync_basis", "selected_operation_matter"),
            ("selected_carrier_role_result", "selected_operation_matter", "selected_operation_matter"),
        ),
    )


def _selected_carrier_context(request: Mapping[str, Any], sync_result: Mapping[str, Any]) -> Any:
    basis = request.get("refusal_abort_basis")
    basis_map = _as_mapping(basis)
    return _first_present(
        request.get("selected_carrier_context"),
        basis_map.get("selected_carrier_context"),
        _get_path_value(sync_result, ("sync_non_sync_basis", "selected_carrier_context")),
        _get_path_value(sync_result, ("selected_operation_matter", "selected_carrier_context")),
    )


def _context_value(request: Mapping[str, Any], sync_result: Mapping[str, Any], key: str) -> Any:
    basis_map = _as_mapping(request.get("refusal_abort_basis"))
    return _first_present(
        request.get(key),
        basis_map.get(key),
        _get_path_value(sync_result, ("sync_non_sync_basis", key)),
        _get_path_value(sync_result, ("selected_operation_matter", key)),
    )


def _sync_non_sync_posture_basis(request: Mapping[str, Any], sync_result: Mapping[str, Any]) -> Any:
    basis_map = _as_mapping(request.get("refusal_abort_basis"))
    return _first_present(
        request.get("sync_non_sync_posture_basis"),
        basis_map.get("sync_non_sync_posture_basis"),
        sync_result.get("sync_non_sync_basis"),
        sync_result.get("sync_non_sync_postures"),
    )


def _coerce_posture_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value] if value.strip() else []
    if isinstance(value, Mapping):
        for key in (
            "selected_refusal_abort_postures",
            "refusal_abort_postures",
            "selected_postures",
            "postures",
        ):
            nested = value.get(key)
            if nested is not None:
                return _coerce_posture_list(nested)
        return [str(item) for item in value.values() if isinstance(item, str) and item.strip()]
    if _is_sequence_not_text(value):
        postures: list[str] = []
        for item in value:
            if isinstance(item, str) and item.strip():
                postures.append(item)
            elif isinstance(item, Mapping):
                name = _first_present(item.get("posture"), item.get("posture_name"), item.get("name"))
                if name:
                    postures.append(str(name))
        return postures
    return []


def _selected_refusal_abort_postures(request: Mapping[str, Any]) -> list[str]:
    postures = _coerce_posture_list(request.get("refusal_abort_postures"))
    if postures:
        return postures
    return (
        _coerce_posture_list(request.get("proposed_refusal_postures"))
        + _coerce_posture_list(request.get("proposed_abort_postures"))
    )


def _unsupported_postures(postures: Sequence[str]) -> list[str]:
    supported = set(SUPPORTED_REFUSAL_ABORT_POSTURES)
    return [posture for posture in postures if posture not in supported]


def _carrier_context_malformed(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, Mapping):
        return False
    if _is_sequence_not_text(value):
        return any(not isinstance(item, Mapping) for item in value)
    return True


def _has_true_field(value: Any, keys: Sequence[str]) -> bool:
    if isinstance(value, Mapping):
        for key in keys:
            if value.get(key) is True:
                return True
        for nested in value.values():
            if _has_true_field(nested, keys):
                return True
    elif _is_sequence_not_text(value):
        return any(_has_true_field(item, keys) for item in value)
    return False


def _first_collapse_code(*values: Any) -> str | None:
    for code, fields in COLLAPSE_FIELDS:
        for value in values:
            if _has_true_field(value, fields):
                return code
    return None


def _selected_sync_has_collapse(sync_result: Mapping[str, Any]) -> str | None:
    statement = _as_mapping(sync_result.get("sync_non_sync_statement"))
    non_claims = _as_mapping(sync_result.get("non_claims"))
    return _first_collapse_code(statement, non_claims)


def _sync_statement_bool(
    sync_result: Mapping[str, Any],
    key: str,
    default: bool = True,
) -> bool:
    value = _first_present_allow_zero(
        _get_path_value(sync_result, ("sync_non_sync_statement", key)),
        _get_path_value(sync_result, ("distributed_sync_non_sync_summary", key)),
        _get_path_value(sync_result, ("sync_non_sync_basis", key)),
    )
    if value is None:
        return default
    return bool(value)


def _build_declared_question(
    request: Mapping[str, Any],
    selected_sync_id: str | None,
    selected_sync_outcome: str | None,
) -> dict[str, Any]:
    return {
        "refusal_abort_request_id": _extract_request_id(request),
        "refusal_abort_question": request.get("refusal_abort_question"),
        "refusal_abort_intent": request.get("refusal_abort_intent"),
        "refusal_abort_request_path": request.get("refusal_abort_request_path"),
        "selected_sync_non_sync_result_id": selected_sync_id,
        "selected_sync_non_sync_result_outcome": selected_sync_outcome,
        "expected_selected_sync_non_sync_outcome": request.get(
            "expected_selected_sync_non_sync_outcome",
            EXPECTED_SELECTED_SYNC_NON_SYNC_OUTCOME,
        ),
        "refusal_abort_boundary_is_not_live_refusal": True,
        "refusal_abort_boundary_is_not_live_abort": True,
        "refusal_abort_boundary_is_not_operation_admission": True,
        "refusal_abort_boundary_is_not_operation_authorization": True,
        "refusal_abort_boundary_is_not_operation_execution": True,
        "refusal_abort_boundary_is_not_consequence": True,
    }


def _build_selected_sync_section(
    sync_result: Mapping[str, Any],
    path: str | None,
    selected_sync_id: str | None,
    selected_sync_outcome: str | None,
    failed_count: int | None,
) -> dict[str, Any]:
    return {
        "selected_sync_non_sync_result": _copy(sync_result) if sync_result else None,
        "selected_sync_non_sync_result_path": path,
        "selected_sync_non_sync_result_id": selected_sync_id,
        "selected_sync_non_sync_result_outcome": selected_sync_outcome,
        "selected_sync_non_sync_result_outcome_is_recorded": selected_sync_outcome
        == EXPECTED_SELECTED_SYNC_NON_SYNC_OUTCOME,
        "selected_sync_non_sync_result_failed_check_count": failed_count,
        "selected_sync_non_sync_result_failed_check_count_zero": failed_count == 0,
        "selected_sync_non_sync_result_remains_boundary_posture_only": True,
        "selected_sync_non_sync_result_did_not_authorize_synchronization": True,
        "selected_sync_non_sync_result_did_not_authorize_non_synchronized_operation": True,
        "selected_sync_non_sync_result_did_not_create_shared_live_state": True,
        "selected_sync_non_sync_result_did_not_authorize_merge": True,
        "selected_sync_non_sync_result_did_not_authorize_replay": True,
        "selected_sync_non_sync_result_did_not_authorize_full_body_transfer": True,
        "selected_sync_non_sync_result_did_not_create_second_body": True,
        "selected_sync_non_sync_result_did_not_admit_operation": True,
        "selected_sync_non_sync_result_did_not_authorize_operation": True,
        "selected_sync_non_sync_result_did_not_execute_operation": True,
        "selected_sync_non_sync_result_preserved_divergence": _sync_statement_bool(
            sync_result, "divergence_remains_visible", True
        ),
        "selected_sync_non_sync_result_preserved_refusal": _sync_statement_bool(
            sync_result, "refusal_remains_visible", True
        ),
        "selected_sync_non_sync_result_preserved_blocked_attempts": _sync_statement_bool(
            sync_result, "blocked_attempts_remain_visible", True
        ),
        "selected_sync_non_sync_result_preserved_projection_mismatch": _sync_statement_bool(
            sync_result, "projection_mismatch_remains_visible", True
        ),
        "selected_sync_non_sync_result_is_not_mutated": True,
    }


def _build_selected_operation_matter(
    request: Mapping[str, Any],
    sync_result: Mapping[str, Any],
    selected_carrier_role_result: Any,
    selected_source_body_authority_result: Any,
    selected_eligibility_result: Any,
    selected_matter_declaration: Any,
    selected_operation_candidate: Any,
    selected_operation_matter: Any,
) -> dict[str, Any]:
    return {
        "selected_sync_non_sync_result": _copy(sync_result) if sync_result else None,
        "selected_carrier_role_result": _copy(selected_carrier_role_result),
        "selected_source_body_authority_result": _copy(selected_source_body_authority_result),
        "selected_eligibility_result": _copy(selected_eligibility_result),
        "selected_matter_declaration": _copy(selected_matter_declaration),
        "selected_operation_candidate": _copy(selected_operation_candidate),
        "selected_operation_matter": _copy(selected_operation_matter),
        "selected_operation_question": _first_present(
            request.get("selected_operation_question"),
            _get_path_value(sync_result, ("selected_operation_matter", "selected_operation_question")),
        ),
        "selected_operation_purpose": _first_present(
            request.get("selected_operation_purpose"),
            _get_path_value(sync_result, ("selected_operation_matter", "selected_operation_purpose")),
        ),
        "proposed_operation_kind": _first_present(
            request.get("proposed_operation_kind"),
            _get_path_value(sync_result, ("selected_operation_matter", "proposed_operation_kind")),
        ),
        "sync_non_sync_remains_boundary_posture_only": True,
        "carrier_role_basis_remains_role_basis_only": True,
        "authority_remains_basis_only": True,
        "eligibility_remains_eligibility_only": True,
        "matter_remains_declaration_only": True,
        "operation_admitted": False,
        "operation_authorized": False,
        "operation_executed": False,
    }


def _build_refusal_abort_basis(
    request: Mapping[str, Any],
    sync_result: Mapping[str, Any],
    selected_carrier_role_result: Any,
    selected_source_body_authority_result: Any,
    selected_eligibility_result: Any,
    selected_matter_declaration: Any,
    selected_carrier_context: Any,
    sync_posture_basis: Any,
) -> dict[str, Any]:
    basis_map = _as_mapping(request.get("refusal_abort_basis"))
    return {
        "selected_sync_non_sync_result": _copy(sync_result) if sync_result else None,
        "sync_non_sync_posture_basis": _copy(sync_posture_basis),
        "selected_carrier_role_result": _copy(selected_carrier_role_result),
        "selected_source_body_authority_result": _copy(selected_source_body_authority_result),
        "selected_eligibility_result": _copy(selected_eligibility_result),
        "selected_matter_declaration": _copy(selected_matter_declaration),
        "selected_carrier_context": _copy(selected_carrier_context),
        "carrier_b_success_context": _copy(_context_value(request, sync_result, "carrier_b_success_context")),
        "carrier_c_block_context": _copy(_context_value(request, sync_result, "carrier_c_block_context")),
        "b_c_divergence_context": _copy(_context_value(request, sync_result, "b_c_divergence_context")),
        "refusal_blocked_attempt_context": _copy(
            _context_value(request, sync_result, "refusal_blocked_attempt_context")
        ),
        "projection_mismatch_context": _copy(_context_value(request, sync_result, "projection_mismatch_context")),
        "source_body_lineage_basis": _copy(
            _first_present(
                request.get("source_body_lineage_basis"),
                basis_map.get("source_body_lineage_basis"),
                _get_path_value(sync_result, ("sync_non_sync_basis", "source_body_lineage_basis")),
            )
        ),
        "distributed_standing_basis": _copy(
            _first_present(
                request.get("distributed_standing_basis"),
                basis_map.get("distributed_standing_basis"),
                _get_path_value(sync_result, ("sync_non_sync_basis", "distributed_standing_basis")),
            )
        ),
        "carrier_b_success_does_not_force_continuation": True,
        "carrier_c_block_remains_visible": True,
        "carrier_c_block_does_not_invalidate_carrier_c": True,
        "b_c_divergence_remains_visible": True,
        "divergence_remains_visible": True,
        "refusal_remains_visible": True,
        "blocked_attempts_remain_visible": True,
        "projection_mismatch_remains_visible": True,
        "sync_non_sync_posture_cannot_be_overread_into_operation": True,
        "no_sync_cannot_be_overread_into_independent_carrier_operation": True,
        "sync_failure_cannot_be_overread_into_whole_body_failure_by_default": True,
        "refusal_abort_basis_is_not_live_refusal": True,
        "refusal_abort_basis_is_not_live_abort": True,
        "refusal_abort_basis_is_not_operation_admission": True,
        "refusal_abort_basis_is_not_operation_authorization": True,
        "refusal_abort_basis_is_not_execution": True,
    }


def _build_refusal_abort_postures(postures: Sequence[str], unsupported: Sequence[str]) -> dict[str, Any]:
    return {
        "selected_refusal_abort_postures": list(postures),
        "supported_refusal_abort_postures": list(SUPPORTED_REFUSAL_ABORT_POSTURES),
        "unsupported_refusal_abort_postures": list(unsupported),
        "all_selected_postures_supported": not unsupported and bool(postures),
        "postures_are_boundary_postures_only": True,
        "postures_are_pre_admission_safety_conditions": True,
        "non_admission_conditions_named": bool(postures),
        "abort_conditions_named": any(posture.startswith("ABORT_IF_") for posture in postures),
        "postures_do_not_execute_live_refusal": True,
        "postures_do_not_execute_live_abort": True,
        "postures_do_not_authorize_operation": True,
        "postures_do_not_create_consequence": True,
        "future_abort_execution_requires_admitted_operation_context": (
            "FUTURE_ABORT_EXECUTION_REQUIRES_ADMITTED_OPERATION_CONTEXT" in postures
        ),
    }


def _build_additional_basis_required(
    outcome: str,
    request: Mapping[str, Any],
) -> dict[str, Any]:
    context = _copy(request.get("additional_basis_context"))
    reason = _first_present(
        request.get("additional_basis_reason"),
        _get_path_value(context, ("additional_basis_reason",)) if isinstance(context, Mapping) else None,
        request.get("block_reason") if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS else None,
    )
    required = outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    return {
        "additional_basis_required": required,
        "additional_basis_context": context if required else (context or {}),
        "additional_basis_reason": reason,
        "representative_missing_basis": [
            "refusal trigger basis too generic",
            "abort trigger basis too generic",
            "non-admission conditions incomplete",
            "Carrier C block requires stronger refusal classification",
            "B/C divergence requires stronger abort/refusal preservation",
            "projection mismatch requires stronger stop-condition basis",
            "sync/non-sync overread risk requires clearer abort condition",
            "proposed output family creates unclear consequence risk",
            "admission / transition boundary cannot yet inspect refusal/abort safely",
        ]
        if required
        else [],
        "additional_basis_not_scheduled": True,
        "additional_basis_not_authorized": True,
        "additional_basis_not_executed": True,
        "missing_basis_not_scheduled": True,
        "missing_basis_not_authorized": True,
        "missing_basis_not_executed": True,
    }


def _build_non_meaning() -> dict[str, bool]:
    meanings = {
        "live_operation_refused",
        "live_operation_aborted",
        "operation_admitted",
        "operation_authorized",
        "operation_executed",
        "synchronization_authorized",
        "non_synchronized_operation_authorized",
        "repository_synchronization_authorized",
        "shared_live_state_created",
        "state_merge_authorized",
        "replay_authorized",
        "full_body_transfer_authorized",
        "second_body_created",
        "carrier_role_activated",
        "carrier_authority_created",
        "carrier_currentness_created",
        "current_carrier_selected",
        "winning_carrier_selected",
        "losing_carrier_invalidated",
        "source_replaced",
        "authority_created",
        "permission_created",
        "truth_action_created",
        "consequence_created",
        "divergence_resolved",
        "evidence_erased",
        "refusal_erased",
        "blocked_attempt_erased",
        "projection_mismatch_hidden",
        "public_readiness_created",
        "final_completion_claimed",
        "follow_on_work_authorized",
    }
    return {f"does_not_mean_{key}": True for key in sorted(meanings)}


def _build_statement(
    outcome: str,
    selected_sync_present: bool,
    selected_sync_outcome: str | None,
    selected_sync_failed_count: int | None,
    selected_carrier_role_result: Any,
    selected_source_body_authority_result: Any,
    selected_eligibility_result: Any,
    selected_matter_declaration: Any,
    selected_operation_candidate: Any,
    selected_operation_matter: Any,
    sync_posture_basis: Any,
    selected_carrier_context: Any,
    postures: Sequence[str],
    unsupported_postures: Sequence[str],
    checks: Sequence[Mapping[str, Any]],
    request: Mapping[str, Any],
    block_code: str | None,
    block_reason: str | None,
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    not_sufficient = outcome == OUTCOME_NOT_SUFFICIENT
    requires_additional = outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    all_postures_supported = not unsupported_postures and bool(postures)
    return {
        "distributed_refusal_abort_boundary_recorded": recorded,
        "refusal_abort_basis_not_sufficient": not_sufficient,
        "distributed_refusal_abort_requires_additional_basis": requires_additional,
        "selected_sync_non_sync_result_preserved": selected_sync_present,
        "selected_sync_non_sync_result_recorded": selected_sync_outcome
        == EXPECTED_SELECTED_SYNC_NON_SYNC_OUTCOME,
        "selected_sync_non_sync_result_failed_check_count_zero": selected_sync_failed_count == 0,
        "selected_carrier_role_result_preserved": _is_non_empty(selected_carrier_role_result),
        "selected_source_body_authority_result_preserved": _is_non_empty(selected_source_body_authority_result),
        "selected_eligibility_result_preserved": _is_non_empty(selected_eligibility_result),
        "selected_matter_declaration_preserved": _is_non_empty(selected_matter_declaration),
        "selected_operation_candidate_preserved": _is_non_empty(selected_operation_candidate),
        "selected_operation_matter_preserved": _is_non_empty(selected_operation_matter),
        "sync_non_sync_posture_basis_preserved": _is_non_empty(sync_posture_basis),
        "sync_non_sync_postures_preserved": _is_non_empty(sync_posture_basis),
        "carrier_evidence_remains_unmerged": True,
        "carrier_context_remains_context_only": True,
        "carrier_context_preserved": _is_non_empty(selected_carrier_context),
        "divergence_remains_visible": True,
        "refusal_remains_visible": True,
        "blocked_attempts_remain_visible": True,
        "projection_mismatch_remains_visible": True,
        "refusal_abort_postures_preserved": bool(postures),
        "refusal_abort_postures_supported": all_postures_supported,
        "non_admission_conditions_named": bool(postures),
        "abort_conditions_named": any(posture.startswith("ABORT_IF_") for posture in postures),
        "carrier_b_success_does_not_force_continuation": True,
        "carrier_c_block_remains_visible": True,
        "carrier_c_block_does_not_invalidate_carrier_c": True,
        "sync_non_sync_posture_not_overread_into_operation": True,
        "live_operation_refused": False,
        "live_operation_aborted": False,
        "operation_admitted": False,
        "operation_authorized": False,
        "operation_executed": False,
        "repository_synchronization_authorized": False,
        "shared_live_state_created": False,
        "state_merge_authorized": False,
        "replay_authorized": False,
        "full_body_transfer_authorized": False,
        "second_body_created": False,
        "non_synchronized_operation_authorized": False,
        "carrier_autonomy_authorized": False,
        "stale_carrier_operation_authorized": False,
        "carrier_role_activated": False,
        "carrier_authority_created": False,
        "carrier_currentness_created": False,
        "current_carrier_selected": False,
        "winning_carrier_selected": False,
        "losing_carrier_invalidated": False,
        "source_replaced": False,
        "truth_created": False,
        "action_authorized": False,
        "consequence_created": False,
        "public_launch_readiness_created": False,
        "final_completion_claimed": False,
        "follow_on_work_authorized": False,
        "future_admission_transition_must_preserve_refusal_abort": recorded,
        "not_sufficient_reason": request.get("not_sufficient_reason") if not_sufficient else None,
        "additional_basis_reason": request.get("additional_basis_reason") if requires_additional else None,
        "block_code": block_code,
        "block_reason": block_reason,
        "passed_check_count": _passed_check_count(checks),
        "failed_check_count": _failed_check_count(checks),
    }


def _collapse_check_passed(*values: Any) -> bool:
    return _first_collapse_code(*values) is None


def _build_checks(
    request: Mapping[str, Any],
    sync_result: Mapping[str, Any],
    sync_load_block_code: str | None,
    selected_sync_outcome: str | None,
    selected_sync_failed_count: int | None,
    selected_carrier_role_result: Any,
    selected_source_body_authority_result: Any,
    selected_eligibility_result: Any,
    selected_matter_declaration: Any,
    selected_operation_candidate: Any,
    selected_operation_matter: Any,
    sync_posture_basis: Any,
    selected_carrier_context: Any,
    postures: Sequence[str],
    unsupported_postures: Sequence[str],
) -> list[dict[str, Any]]:
    question = request.get("refusal_abort_question")
    intent = request.get("refusal_abort_intent")
    collapse_values = (
        request,
        request.get("refusal_abort_basis"),
        request.get("refusal_abort_postures"),
        request.get("proposed_refusal_postures"),
        request.get("proposed_abort_postures"),
        request.get("declared_non_claims"),
        _as_mapping(sync_result.get("sync_non_sync_statement")),
        _as_mapping(sync_result.get("non_claims")),
    )
    checks = [
        _make_check(
            "refusal / abort question declared",
            _is_non_empty(question),
            "declared refusal / abort question",
            question,
            "REFUSAL_ABORT_QUESTION_UNDECLARED",
        ),
        _make_check(
            "refusal / abort intent supported",
            intent in SUPPORTED_INTENTS,
            list(SUPPORTED_INTENTS),
            intent,
            "REFUSAL_ABORT_INTENT_UNSUPPORTED",
        ),
        _make_check(
            "selected sync/non-sync result present",
            _is_non_empty(sync_result) and sync_load_block_code is None,
            "selected sync/non-sync result object",
            "present" if _is_non_empty(sync_result) else "missing",
            sync_load_block_code or "SYNC_NON_SYNC_RESULT_MISSING",
        ),
        _make_check(
            "selected sync/non-sync result outcome declared",
            _is_non_empty(selected_sync_outcome),
            "selected sync/non-sync outcome declared",
            selected_sync_outcome,
            "SYNC_NON_SYNC_RESULT_OUTCOME_MISSING",
        ),
        _make_check(
            "selected sync/non-sync result outcome recorded",
            selected_sync_outcome == EXPECTED_SELECTED_SYNC_NON_SYNC_OUTCOME,
            EXPECTED_SELECTED_SYNC_NON_SYNC_OUTCOME,
            selected_sync_outcome,
            "SYNC_NON_SYNC_RESULT_NOT_RECORDED",
        ),
        _make_check(
            "selected sync/non-sync result failed check count zero",
            selected_sync_failed_count == 0,
            0,
            selected_sync_failed_count,
            "SYNC_NON_SYNC_RESULT_HAS_FAILED_CHECKS",
        ),
        _make_check(
            "selected carrier role result preserved",
            _is_non_empty(selected_carrier_role_result),
            "selected carrier role result preserved",
            "present" if _is_non_empty(selected_carrier_role_result) else "missing",
            "CARRIER_ROLE_RESULT_MISSING",
        ),
        _make_check(
            "selected source-body authority result preserved",
            _is_non_empty(selected_source_body_authority_result),
            "selected source-body authority result preserved",
            "present" if _is_non_empty(selected_source_body_authority_result) else "missing",
            "SOURCE_BODY_AUTHORITY_RESULT_MISSING",
        ),
        _make_check(
            "selected eligibility result preserved",
            _is_non_empty(selected_eligibility_result),
            "selected eligibility result preserved",
            "present" if _is_non_empty(selected_eligibility_result) else "missing",
            "SELECTED_ELIGIBILITY_RESULT_MISSING",
        ),
        _make_check(
            "selected matter declaration preserved",
            _is_non_empty(selected_matter_declaration),
            "selected matter declaration preserved",
            "present" if _is_non_empty(selected_matter_declaration) else "missing",
            "SELECTED_MATTER_DECLARATION_MISSING",
        ),
        _make_check(
            "selected operation candidate preserved",
            _is_non_empty(selected_operation_candidate),
            "selected operation candidate preserved",
            "present" if _is_non_empty(selected_operation_candidate) else "missing",
            "SELECTED_OPERATION_CANDIDATE_MISSING",
        ),
        _make_check(
            "selected operation matter preserved",
            _is_non_empty(selected_operation_matter),
            "selected operation matter preserved",
            "present" if _is_non_empty(selected_operation_matter) else "missing",
            "SELECTED_OPERATION_MATTER_MISSING",
        ),
        _make_check(
            "sync/non-sync posture basis preserved",
            _is_non_empty(sync_posture_basis),
            "sync/non-sync posture basis preserved",
            "present" if _is_non_empty(sync_posture_basis) else "missing",
            "SYNC_NON_SYNC_POSTURE_BASIS_MISSING",
        ),
        _make_check(
            "sync/non-sync postures preserved",
            _is_non_empty(sync_posture_basis),
            "sync/non-sync postures preserved",
            "present" if _is_non_empty(sync_posture_basis) else "missing",
            "SYNC_NON_SYNC_POSTURE_BASIS_MISSING",
        ),
        _make_check(
            "carrier evidence remains unmerged",
            _sync_statement_bool(sync_result, "carrier_evidence_remains_unmerged", True),
            True,
            _sync_statement_bool(sync_result, "carrier_evidence_remains_unmerged", True),
            "SYNC_NON_SYNC_RESULT_MALFORMED",
        ),
        _make_check(
            "carrier context remains context only",
            _sync_statement_bool(sync_result, "carrier_context_remains_context_only", True),
            True,
            _sync_statement_bool(sync_result, "carrier_context_remains_context_only", True),
            "SYNC_NON_SYNC_RESULT_MALFORMED",
        ),
        _make_check(
            "divergence remains visible",
            _sync_statement_bool(sync_result, "divergence_remains_visible", True),
            True,
            _sync_statement_bool(sync_result, "divergence_remains_visible", True),
            "REFUSAL_ABORT_REVIEW_ERASES_EVIDENCE_OR_REFUSAL",
        ),
        _make_check(
            "refusal remains visible",
            _sync_statement_bool(sync_result, "refusal_remains_visible", True),
            True,
            _sync_statement_bool(sync_result, "refusal_remains_visible", True),
            "REFUSAL_ABORT_REVIEW_ERASES_EVIDENCE_OR_REFUSAL",
        ),
        _make_check(
            "blocked attempts remain visible",
            _sync_statement_bool(sync_result, "blocked_attempts_remain_visible", True),
            True,
            _sync_statement_bool(sync_result, "blocked_attempts_remain_visible", True),
            "REFUSAL_ABORT_REVIEW_ERASES_EVIDENCE_OR_REFUSAL",
        ),
        _make_check(
            "projection mismatch remains visible",
            _sync_statement_bool(sync_result, "projection_mismatch_remains_visible", True),
            True,
            _sync_statement_bool(sync_result, "projection_mismatch_remains_visible", True),
            "REFUSAL_ABORT_REVIEW_ERASES_EVIDENCE_OR_REFUSAL",
        ),
        _make_check(
            "selected carrier context parseable",
            not _carrier_context_malformed(selected_carrier_context),
            "mapping/list mapping carrier context or omitted",
            "malformed" if _carrier_context_malformed(selected_carrier_context) else "parseable",
            "SELECTED_CARRIER_CONTEXT_MALFORMED",
        ),
        _make_check(
            "selected refusal / abort postures supported",
            bool(postures) and not unsupported_postures,
            list(SUPPORTED_REFUSAL_ABORT_POSTURES),
            list(postures),
            "UNSUPPORTED_REFUSAL_ABORT_POSTURE"
            if unsupported_postures
            else "REFUSAL_ABORT_POSTURES_MISSING",
        ),
        _make_check(
            "no live operation refused",
            not _has_true_field(collapse_values, ("live_operation_refused", "operation_refused")),
            False,
            "true detected" if _has_true_field(collapse_values, ("live_operation_refused", "operation_refused")) else False,
            "REFUSAL_ABORT_REVIEW_REFUSES_LIVE_OPERATION",
        ),
        _make_check(
            "no live operation aborted",
            not _has_true_field(collapse_values, ("live_operation_aborted", "operation_aborted")),
            False,
            "true detected" if _has_true_field(collapse_values, ("live_operation_aborted", "operation_aborted")) else False,
            "REFUSAL_ABORT_REVIEW_ABORTS_LIVE_OPERATION",
        ),
        _make_check(
            "no operation admitted",
            not _has_true_field(collapse_values, ("operation_admitted",)),
            False,
            "true detected" if _has_true_field(collapse_values, ("operation_admitted",)) else False,
            "REFUSAL_ABORT_REVIEW_ADMITS_OPERATION",
        ),
        _make_check(
            "no operation authorized",
            not _has_true_field(collapse_values, ("operation_authorized", "distributed_operation_authorized")),
            False,
            "true detected"
            if _has_true_field(collapse_values, ("operation_authorized", "distributed_operation_authorized"))
            else False,
            "REFUSAL_ABORT_REVIEW_AUTHORIZES_OPERATION",
        ),
        _make_check(
            "no operation executed",
            not _has_true_field(collapse_values, ("operation_executed",)),
            False,
            "true detected" if _has_true_field(collapse_values, ("operation_executed",)) else False,
            "REFUSAL_ABORT_REVIEW_EXECUTES_OPERATION",
        ),
        _make_check(
            "no synchronization/shared live state/merge/replay/full body transfer/second body",
            not _has_true_field(
                collapse_values,
                (
                    "repository_synchronization_authorized",
                    "synchronization_authorized",
                    "shared_live_state_created",
                    "state_merge_authorized",
                    "replay_authorized",
                    "full_body_transfer_authorized",
                    "second_body_created",
                ),
            ),
            False,
            "true detected"
            if _has_true_field(
                collapse_values,
                (
                    "repository_synchronization_authorized",
                    "synchronization_authorized",
                    "shared_live_state_created",
                    "state_merge_authorized",
                    "replay_authorized",
                    "full_body_transfer_authorized",
                    "second_body_created",
                ),
            )
            else False,
            _first_collapse_code(*collapse_values) or "REFUSAL_ABORT_REVIEW_AUTHORIZES_SYNCHRONIZATION",
        ),
        _make_check(
            "no non-synchronized operation/carrier autonomy/stale carrier operation",
            not _has_true_field(
                collapse_values,
                (
                    "non_synchronized_operation_authorized",
                    "non_sync_operation_authorized",
                    "carrier_autonomy_authorized",
                    "stale_carrier_operation_authorized",
                ),
            ),
            False,
            "true detected"
            if _has_true_field(
                collapse_values,
                (
                    "non_synchronized_operation_authorized",
                    "non_sync_operation_authorized",
                    "carrier_autonomy_authorized",
                    "stale_carrier_operation_authorized",
                ),
            )
            else False,
            _first_collapse_code(*collapse_values)
            or "REFUSAL_ABORT_REVIEW_AUTHORIZES_NON_SYNCHRONIZED_OPERATION",
        ),
        _make_check(
            "no carrier role activated",
            not _has_true_field(
                collapse_values,
                (
                    "carrier_role_activated",
                    "carrier_roles_activated",
                    "carrier_role_assigned_for_operation",
                ),
            ),
            False,
            "true detected"
            if _has_true_field(
                collapse_values,
                (
                    "carrier_role_activated",
                    "carrier_roles_activated",
                    "carrier_role_assigned_for_operation",
                ),
            )
            else False,
            "REFUSAL_ABORT_REVIEW_ACTIVATES_CARRIER_ROLES",
        ),
        _make_check(
            "no carrier authority/currentness/hierarchy created",
            not _has_true_field(
                collapse_values,
                (
                    "carrier_authority_created",
                    "authority_created",
                    "carrier_currentness_created",
                    "carrier_hierarchy_created",
                ),
            ),
            False,
            "true detected"
            if _has_true_field(
                collapse_values,
                (
                    "carrier_authority_created",
                    "authority_created",
                    "carrier_currentness_created",
                    "carrier_hierarchy_created",
                ),
            )
            else False,
            _first_collapse_code(*collapse_values) or "REFUSAL_ABORT_REVIEW_CREATES_CARRIER_AUTHORITY",
        ),
        _make_check(
            "no current/winning/losing carrier selected",
            not _has_true_field(
                collapse_values,
                (
                    "current_carrier_selected",
                    "winning_carrier_selected",
                    "losing_carrier_invalidated",
                ),
            ),
            False,
            "true detected"
            if _has_true_field(
                collapse_values,
                (
                    "current_carrier_selected",
                    "winning_carrier_selected",
                    "losing_carrier_invalidated",
                ),
            )
            else False,
            _first_collapse_code(*collapse_values) or "REFUSAL_ABORT_REVIEW_SELECTS_CURRENT_CARRIER",
        ),
        _make_check(
            "no source replacement",
            not _has_true_field(collapse_values, ("source_replaced", "source_replaced_by_carrier")),
            False,
            "true detected"
            if _has_true_field(collapse_values, ("source_replaced", "source_replaced_by_carrier"))
            else False,
            "REFUSAL_ABORT_REVIEW_REPLACES_SOURCE",
        ),
        _make_check(
            "no consequence created",
            not _has_true_field(collapse_values, ("consequence_created",)),
            False,
            "true detected" if _has_true_field(collapse_values, ("consequence_created",)) else False,
            "REFUSAL_ABORT_REVIEW_CREATES_CONSEQUENCE",
        ),
        _make_check(
            "no public readiness/final completion/follow-on work",
            not _has_true_field(
                collapse_values,
                (
                    "public_launch_readiness_created",
                    "public_readiness_created",
                    "final_completion_claimed",
                    "follow_on_work_authorized",
                    "follow_on_work_scheduled",
                    "self_orientation_successor_scheduled",
                ),
            ),
            False,
            "true detected"
            if _has_true_field(
                collapse_values,
                (
                    "public_launch_readiness_created",
                    "public_readiness_created",
                    "final_completion_claimed",
                    "follow_on_work_authorized",
                    "follow_on_work_scheduled",
                    "self_orientation_successor_scheduled",
                ),
            )
            else False,
            _first_collapse_code(*collapse_values) or "REFUSAL_ABORT_REVIEW_SCHEDULES_FOLLOW_ON_WORK",
        ),
        _make_check(
            "no mutation/replay/merge",
            not _has_true_field(
                collapse_values,
                ("mutation_performed", "replay_performed", "merge_performed"),
            ),
            False,
            "true detected"
            if _has_true_field(collapse_values, ("mutation_performed", "replay_performed", "merge_performed"))
            else False,
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        ),
        _make_check(
            "non-claims remain false",
            _declared_non_claims_are_false(request),
            {key: False for key in REQUIRED_NON_CLAIMS},
            request.get("declared_non_claims"),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
    ]
    return checks


def _block_reason_for_code(code: str | None, request: Mapping[str, Any], load_detail: str | None) -> str | None:
    if code is None:
        return None
    if load_detail:
        return load_detail
    if _is_non_empty(request.get("block_reason")):
        return str(request.get("block_reason"))
    return code.lower().replace("_", " ")


def _determine_outcome_and_block(
    request: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    load_block_code: str | None,
    load_detail: str | None,
) -> tuple[str, str | None, str | None]:
    intent = request.get("refusal_abort_intent")
    if intent == INTENT_BLOCK:
        code = "REFUSAL_ABORT_REVIEW_REQUEST_EXPLICITLY_BLOCKED"
        return OUTCOME_BLOCKED, code, _block_reason_for_code(code, request, load_detail)

    requested_outcome = request.get("requested_refusal_abort_outcome")
    if requested_outcome in (OUTCOME_NOT_SUFFICIENT, OUTCOME_REQUIRES_ADDITIONAL_BASIS):
        if _failed_check_count(checks) == 0:
            return requested_outcome, None, None

    collapse_code = _first_collapse_code(
        request,
        request.get("refusal_abort_basis"),
        request.get("refusal_abort_postures"),
        request.get("proposed_refusal_postures"),
        request.get("proposed_abort_postures"),
        request.get("declared_non_claims"),
    )
    block_code = load_block_code or collapse_code or _first_failed_code(checks)
    if block_code:
        return OUTCOME_BLOCKED, block_code, _block_reason_for_code(block_code, request, load_detail)

    if intent == INTENT_DO_NOT_RECORD:
        return OUTCOME_NOT_SUFFICIENT, None, None

    if requested_outcome == OUTCOME_RECORDED or requested_outcome is None:
        if _is_non_empty(request.get("not_sufficient_reason")):
            return OUTCOME_NOT_SUFFICIENT, None, None
        if _is_non_empty(request.get("additional_basis_context")):
            return OUTCOME_REQUIRES_ADDITIONAL_BASIS, None, None
        return OUTCOME_RECORDED, None, None

    if requested_outcome == OUTCOME_BLOCKED:
        code = "REFUSAL_ABORT_REVIEW_REQUEST_EXPLICITLY_BLOCKED"
        return OUTCOME_BLOCKED, code, _block_reason_for_code(code, request, load_detail)

    code = "REFUSAL_ABORT_INTENT_UNSUPPORTED"
    return OUTCOME_BLOCKED, code, _block_reason_for_code(code, request, load_detail)


def _build_metadata(request: Mapping[str, Any], selected_sync_id: str | None) -> dict[str, Any]:
    basis_id = _first_present(_extract_request_id(request), selected_sync_id, "refusal_abort_boundary")
    return {
        "distributed_refusal_abort_result_id": (
            f"{_sanitize_filename(basis_id)}__distributed_refusal_abort_boundary_result"
        ),
        "distributed_refusal_abort_result_type": RESULT_TYPE,
        "distributed_refusal_abort_result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
    }


def _assemble_result(
    request: Mapping[str, Any],
    sync_result: Mapping[str, Any],
    selected_sync_path: str | None,
    sync_load_block_code: str | None,
    sync_load_detail: str | None,
) -> dict[str, Any]:
    selected_sync_id = _extract_selected_sync_id(sync_result, request)
    selected_sync_outcome = _extract_selected_sync_outcome(sync_result, request)
    selected_sync_failed_count = _extract_failed_check_count(sync_result)
    selected_carrier_role_result = _selected_carrier_role_result(request, sync_result)
    selected_source_body_authority_result = _selected_source_body_authority_result(request, sync_result)
    selected_eligibility_result = _selected_eligibility_result(request, sync_result)
    selected_matter_declaration = _selected_matter_declaration(request, sync_result)
    selected_operation_candidate = _selected_operation_candidate(request, sync_result)
    selected_operation_matter = _selected_operation_matter(request, sync_result)
    selected_carrier_context = _selected_carrier_context(request, sync_result)
    sync_posture_basis = _sync_non_sync_posture_basis(request, sync_result)
    postures = _selected_refusal_abort_postures(request)
    unsupported = _unsupported_postures(postures)

    checks = _build_checks(
        request,
        sync_result,
        sync_load_block_code,
        selected_sync_outcome,
        selected_sync_failed_count,
        selected_carrier_role_result,
        selected_source_body_authority_result,
        selected_eligibility_result,
        selected_matter_declaration,
        selected_operation_candidate,
        selected_operation_matter,
        sync_posture_basis,
        selected_carrier_context,
        postures,
        unsupported,
    )
    outcome, block_code, block_reason = _determine_outcome_and_block(
        request,
        checks,
        sync_load_block_code,
        sync_load_detail,
    )
    metadata = _build_metadata(request, selected_sync_id)
    statement = _build_statement(
        outcome,
        _is_non_empty(sync_result),
        selected_sync_outcome,
        selected_sync_failed_count,
        selected_carrier_role_result,
        selected_source_body_authority_result,
        selected_eligibility_result,
        selected_matter_declaration,
        selected_operation_candidate,
        selected_operation_matter,
        sync_posture_basis,
        selected_carrier_context,
        postures,
        unsupported,
        checks,
        request,
        block_code,
        block_reason,
    )
    result: dict[str, Any] = {
        "distributed_refusal_abort_metadata": metadata,
        "declared_refusal_abort_question": _build_declared_question(
            request,
            selected_sync_id,
            selected_sync_outcome,
        ),
        "selected_sync_non_sync_result": _build_selected_sync_section(
            sync_result,
            selected_sync_path,
            selected_sync_id,
            selected_sync_outcome,
            selected_sync_failed_count,
        ),
        "selected_operation_matter": _build_selected_operation_matter(
            request,
            sync_result,
            selected_carrier_role_result,
            selected_source_body_authority_result,
            selected_eligibility_result,
            selected_matter_declaration,
            selected_operation_candidate,
            selected_operation_matter,
        ),
        "refusal_abort_basis": _build_refusal_abort_basis(
            request,
            sync_result,
            selected_carrier_role_result,
            selected_source_body_authority_result,
            selected_eligibility_result,
            selected_matter_declaration,
            selected_carrier_context,
            sync_posture_basis,
        ),
        "refusal_abort_postures": _build_refusal_abort_postures(postures, unsupported),
        "refusal_abort_checks": checks,
        "refusal_abort_statement": statement,
        "refusal_abort_non_meaning": _build_non_meaning(),
        "additional_basis_required": _build_additional_basis_required(outcome, request),
        "what_remains_open": _copy(WHAT_REMAINS_OPEN),
        "non_claims": _required_non_claims_false(),
        "outcome": outcome,
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "block_code": block_code,
            "block_reason": block_reason,
        },
    }
    result["distributed_refusal_abort_summary"] = build_distributed_refusal_abort_summary(result)
    return result


def _blocked_result_for_malformed_request(
    block_code: str,
    block_reason: str | None = None,
    request_path: str | None = None,
) -> dict[str, Any]:
    request: dict[str, Any] = {
        "refusal_abort_request_id": None,
        "refusal_abort_question": None,
        "refusal_abort_intent": None,
        "refusal_abort_request_path": request_path,
        "declared_non_claims": _required_non_claims_false(),
    }
    result = _assemble_result(request, {}, None, None, None)
    result["outcome"] = OUTCOME_BLOCKED
    result["block"] = {
        "blocked": True,
        "block_code": block_code,
        "block_reason": block_reason or block_code.lower().replace("_", " "),
    }
    result["refusal_abort_statement"]["distributed_refusal_abort_boundary_recorded"] = False
    result["refusal_abort_statement"]["block_code"] = block_code
    result["refusal_abort_statement"]["block_reason"] = result["block"]["block_reason"]
    result["distributed_refusal_abort_summary"] = build_distributed_refusal_abort_summary(result)
    return result


def resolve_distributed_refusal_abort_boundary(
    declared_refusal_abort_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one declared distributed refusal / abort boundary request."""

    if declared_refusal_abort_request is None:
        return _blocked_result_for_malformed_request("REFUSAL_ABORT_QUESTION_UNDECLARED")
    if not isinstance(declared_refusal_abort_request, Mapping):
        return _blocked_result_for_malformed_request("DECLARED_REFUSAL_ABORT_REQUEST_MALFORMED")

    request = _copy(dict(declared_refusal_abort_request))
    sync_result, selected_sync_path, sync_load_block_code, sync_load_detail = (
        _load_selected_sync_non_sync_result(request)
    )
    return _assemble_result(
        request,
        sync_result,
        selected_sync_path,
        sync_load_block_code,
        sync_load_detail,
    )


def resolve_distributed_refusal_abort_boundary_from_path(
    declared_refusal_abort_request_path: Path | str,
) -> dict:
    """Resolve one declared distributed refusal / abort boundary request from JSON."""

    path = Path(declared_refusal_abort_request_path)
    request, block_code, detail = _load_request_from_path(path)
    if block_code:
        return _blocked_result_for_malformed_request(block_code, detail, str(path))
    assert request is not None
    return resolve_distributed_refusal_abort_boundary(request)


def build_distributed_refusal_abort_summary(result: Mapping[str, Any]) -> dict:
    """Build a bounded summary from a refusal / abort boundary result."""

    declared = _as_mapping(result.get("declared_refusal_abort_question"))
    selected_sync = _as_mapping(result.get("selected_sync_non_sync_result"))
    selected_operation = _as_mapping(result.get("selected_operation_matter"))
    statement = _as_mapping(result.get("refusal_abort_statement"))
    checks = result.get("refusal_abort_checks")
    checks_list = [check for check in checks if isinstance(check, Mapping)] if _is_sequence_not_text(checks) else []
    block = _as_mapping(result.get("block"))
    non_claims = _as_mapping(result.get("non_claims"))
    selected_operation_candidate = selected_operation.get("selected_operation_candidate")
    selected_operation_matter = selected_operation.get("selected_operation_matter")
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "refusal_abort_request_id": declared.get("refusal_abort_request_id"),
        "refusal_abort_question": declared.get("refusal_abort_question"),
        "refusal_abort_intent": declared.get("refusal_abort_intent"),
        "selected_sync_non_sync_result_id": selected_sync.get("selected_sync_non_sync_result_id"),
        "selected_sync_non_sync_result_outcome": selected_sync.get("selected_sync_non_sync_result_outcome"),
        "selected_operation_candidate_id": _first_present(
            _get_path_value(selected_operation_candidate, ("operation_candidate_id",)),
            _get_path_value(selected_operation_candidate, ("selected_operation_candidate_id",)),
            _get_path_value(selected_operation_candidate, ("id",)),
        ),
        "selected_operation_matter_id": _first_present(
            _get_path_value(selected_operation_matter, ("operation_matter_id",)),
            _get_path_value(selected_operation_matter, ("selected_operation_matter_id",)),
            _get_path_value(selected_operation_matter, ("id",)),
        ),
        "passed_check_count": _passed_check_count(checks_list),
        "failed_check_count": _failed_check_count(checks_list),
        "distributed_refusal_abort_boundary_recorded": statement.get(
            "distributed_refusal_abort_boundary_recorded"
        )
        is True,
        "refusal_abort_basis_not_sufficient": statement.get("refusal_abort_basis_not_sufficient") is True,
        "requires_additional_basis": statement.get("distributed_refusal_abort_requires_additional_basis") is True,
        "selected_sync_non_sync_result_preserved": statement.get("selected_sync_non_sync_result_preserved")
        is True,
        "selected_sync_non_sync_result_recorded": statement.get("selected_sync_non_sync_result_recorded")
        is True,
        "selected_sync_non_sync_result_failed_check_count_zero": statement.get(
            "selected_sync_non_sync_result_failed_check_count_zero"
        )
        is True,
        "selected_carrier_role_result_preserved": statement.get("selected_carrier_role_result_preserved")
        is True,
        "selected_source_body_authority_result_preserved": statement.get(
            "selected_source_body_authority_result_preserved"
        )
        is True,
        "selected_eligibility_result_preserved": statement.get("selected_eligibility_result_preserved")
        is True,
        "selected_matter_declaration_preserved": statement.get("selected_matter_declaration_preserved")
        is True,
        "selected_operation_candidate_preserved": statement.get("selected_operation_candidate_preserved")
        is True,
        "selected_operation_matter_preserved": statement.get("selected_operation_matter_preserved") is True,
        "sync_non_sync_postures_preserved": statement.get("sync_non_sync_postures_preserved") is True,
        "carrier_evidence_remains_unmerged": statement.get("carrier_evidence_remains_unmerged") is True,
        "carrier_context_remains_context_only": statement.get("carrier_context_remains_context_only") is True,
        "divergence_remains_visible": statement.get("divergence_remains_visible") is True,
        "refusal_remains_visible": statement.get("refusal_remains_visible") is True,
        "blocked_attempts_remain_visible": statement.get("blocked_attempts_remain_visible") is True,
        "projection_mismatch_remains_visible": statement.get("projection_mismatch_remains_visible") is True,
        "refusal_abort_postures_preserved": statement.get("refusal_abort_postures_preserved") is True,
        "refusal_abort_postures_supported": statement.get("refusal_abort_postures_supported") is True,
        "non_admission_conditions_named": statement.get("non_admission_conditions_named") is True,
        "abort_conditions_named": statement.get("abort_conditions_named") is True,
        "carrier_b_success_does_not_force_continuation": statement.get(
            "carrier_b_success_does_not_force_continuation"
        )
        is True,
        "carrier_c_block_remains_visible": statement.get("carrier_c_block_remains_visible") is True,
        "carrier_c_block_does_not_invalidate_carrier_c": statement.get(
            "carrier_c_block_does_not_invalidate_carrier_c"
        )
        is True,
        "live_operation_refused": statement.get("live_operation_refused") is True,
        "live_operation_aborted": statement.get("live_operation_aborted") is True,
        "operation_admitted": statement.get("operation_admitted") is True,
        "operation_authorized": statement.get("operation_authorized") is True,
        "operation_executed": statement.get("operation_executed") is True,
        "repository_synchronization_authorized": statement.get("repository_synchronization_authorized") is True,
        "full_body_transfer_authorized": statement.get("full_body_transfer_authorized") is True,
        "second_body_created": statement.get("second_body_created") is True,
        "non_synchronized_operation_authorized": statement.get("non_synchronized_operation_authorized") is True,
        "consequence_created": statement.get("consequence_created") is True,
        "public_launch_readiness_created": statement.get("public_launch_readiness_created") is True,
        "final_completion_claimed": statement.get("final_completion_claimed") is True,
        "follow_on_work_authorized": statement.get("follow_on_work_authorized") is True,
        "no_live_operation_refused_or_aborted": (
            statement.get("live_operation_refused") is False
            and statement.get("live_operation_aborted") is False
        ),
        "no_operation_admitted_authorized_executed": (
            statement.get("operation_admitted") is False
            and statement.get("operation_authorized") is False
            and statement.get("operation_executed") is False
        ),
        "no_sync_full_body_transfer_second_body_non_sync_operation": (
            statement.get("repository_synchronization_authorized") is False
            and statement.get("full_body_transfer_authorized") is False
            and statement.get("second_body_created") is False
            and statement.get("non_synchronized_operation_authorized") is False
        ),
        "no_consequence_public_readiness_final_completion_follow_on_work": (
            statement.get("consequence_created") is False
            and statement.get("public_launch_readiness_created") is False
            and statement.get("final_completion_claimed") is False
            and statement.get("follow_on_work_authorized") is False
        ),
        "future_admission_transition_must_preserve_refusal_abort": statement.get(
            "future_admission_transition_must_preserve_refusal_abort"
        )
        is True,
        "key_non_claims": {
            key: non_claims.get(key)
            for key in (
                "live_operation_refused",
                "live_operation_aborted",
                "operation_admitted",
                "operation_authorized",
                "operation_executed",
                "repository_synchronization_authorized",
                "non_synchronized_operation_authorized",
                "full_body_transfer_authorized",
                "second_body_created",
                "consequence_created",
                "public_launch_readiness_created",
                "final_completion_claimed",
                "follow_on_work_authorized",
            )
        },
    }


def write_distributed_refusal_abort_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a refusal / abort boundary result as additive JSON."""

    if not isinstance(result, Mapping):
        raise DistributedRefusalAbortBoundaryError("result must be a mapping")
    if output_path is None:
        declared = _as_mapping(result.get("declared_refusal_abort_question"))
        selected_sync = _as_mapping(result.get("selected_sync_non_sync_result"))
        basis_id = _first_present(
            declared.get("refusal_abort_request_id"),
            selected_sync.get("selected_sync_non_sync_result_id"),
            _get_path_value(
                result,
                (
                    "distributed_refusal_abort_metadata",
                    "distributed_refusal_abort_result_id",
                ),
            ),
            "distributed_refusal_abort_boundary",
        )
        filename = f"{_sanitize_filename(basis_id)}__distributed_refusal_abort_result.json"
        target = DISTRIBUTED_REFUSAL_ABORT_BOUNDARY_ROOT / filename
    else:
        target = Path(output_path)
    target = _deduplicate_path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    return target


def build_declared_distributed_refusal_abort_request(
    refusal_abort_request_id: str,
    refusal_abort_question: str,
    selected_sync_non_sync_result: Mapping[str, Any] | str,
    refusal_abort_basis: Mapping[str, Any] | str,
    refusal_abort_postures: Sequence[str] | Mapping[str, Any],
    refusal_abort_intent: str = INTENT_RECORD,
    *,
    selected_sync_non_sync_result_path: str | None = None,
    selected_sync_non_sync_result_id: str | None = None,
    selected_sync_non_sync_result_outcome: str | None = None,
    requested_refusal_abort_outcome: str = OUTCOME_RECORDED,
    selected_carrier_context: Sequence[Mapping[str, Any]] | Mapping[str, Any] | None = None,
    additional_basis_context: Mapping[str, Any] | None = None,
    not_sufficient_reason: str | None = None,
) -> dict:
    """Build a bounded declared refusal / abort request."""

    request: dict[str, Any] = {
        "refusal_abort_request_id": refusal_abort_request_id,
        "refusal_abort_question": refusal_abort_question,
        "refusal_abort_intent": refusal_abort_intent,
        "refusal_abort_basis": _copy(refusal_abort_basis)
        if isinstance(refusal_abort_basis, Mapping)
        else {"refusal_abort_basis_reference": refusal_abort_basis},
        "refusal_abort_postures": _copy(refusal_abort_postures),
        "selected_sync_non_sync_result_id": selected_sync_non_sync_result_id,
        "selected_sync_non_sync_result_outcome": selected_sync_non_sync_result_outcome,
        "requested_refusal_abort_outcome": requested_refusal_abort_outcome,
        "selected_carrier_context": _copy(selected_carrier_context),
        "additional_basis_context": _copy(additional_basis_context) if additional_basis_context else {},
        "not_sufficient_reason": not_sufficient_reason,
        "declared_non_claims": _required_non_claims_false(),
    }
    if selected_sync_non_sync_result_path is not None:
        request["selected_sync_non_sync_result_path"] = selected_sync_non_sync_result_path
    elif isinstance(selected_sync_non_sync_result, Mapping):
        request["selected_sync_non_sync_result"] = _copy(selected_sync_non_sync_result)
    else:
        request["selected_sync_non_sync_result_path"] = str(selected_sync_non_sync_result)

    if selected_carrier_context is not None and isinstance(request["refusal_abort_basis"], Mapping):
        request["refusal_abort_basis"]["selected_carrier_context"] = _copy(selected_carrier_context)

    return request
