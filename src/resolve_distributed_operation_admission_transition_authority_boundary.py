"""Resolve distributed operation admission / transition authority.

This module may admit one bounded operation context for later execution /
emission review only. It does not execute operation, emit output, authorize
action, create consequence, synchronize repositories, authorize
non-synchronized operation, transfer the body, create a second body, erase
refusal / abort conditions, create reusable permission, authorize autonomous
continuation, create public readiness, claim final completion, or schedule
follow-on work.
"""

from __future__ import annotations

import copy
import datetime
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any


class DistributedOperationAdmissionTransitionAuthorityBoundaryError(Exception):
    """Raised for impossible admission / transition boundary failures."""


RESOLVER_MODULE = "resolve_distributed_operation_admission_transition_authority_boundary"
RESULT_VERSION = "0.1.0"
RESULT_TYPE = "distributed_operation_admission_transition_authority_boundary_result"

DISTRIBUTED_OPERATION_ADMISSION_TRANSITION_AUTHORITY_BOUNDARY_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_distributed_operation_admission_transition_authority_boundary"
)

EXPECTED_SELECTED_REFUSAL_ABORT_OUTCOME = "DISTRIBUTED_REFUSAL_ABORT_BOUNDARY_RECORDED"

OUTCOME_RECORDED = "DISTRIBUTED_OPERATION_ADMISSION_TRANSITION_AUTHORITY_RECORDED"
OUTCOME_NOT_ADMITTED = "DISTRIBUTED_OPERATION_ADMISSION_TRANSITION_NOT_ADMITTED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "DISTRIBUTED_OPERATION_ADMISSION_TRANSITION_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "DISTRIBUTED_OPERATION_ADMISSION_TRANSITION_REVIEW_BLOCKED"

OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_ADMITTED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = "RECORD_DISTRIBUTED_OPERATION_ADMISSION_TRANSITION_AUTHORITY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_DISTRIBUTED_OPERATION_ADMISSION_TRANSITION_AUTHORITY"
INTENT_BLOCK = "BLOCK_DISTRIBUTED_OPERATION_ADMISSION_TRANSITION_REVIEW"

SUPPORTED_INTENTS = (
    INTENT_RECORD,
    INTENT_DO_NOT_RECORD,
    INTENT_BLOCK,
)

SUPPORTED_ADMISSION_SCOPE = (
    "ONE_OPERATION_CONTEXT_ONLY",
    "NO_EXECUTION_IN_ADMISSION",
    "NO_EMISSION_IN_ADMISSION",
    "NO_ACTION_IN_ADMISSION",
    "NO_CONSEQUENCE_IN_ADMISSION",
    "NO_REPOSITORY_SYNC_IN_ADMISSION",
    "NO_NON_SYNCHRONIZED_OPERATION_IN_ADMISSION",
    "NO_FULL_BODY_TRANSFER_IN_ADMISSION",
    "NO_SECOND_BODY_IN_ADMISSION",
    "REFUSAL_ABORT_CONDITIONS_CARRY_FORWARD",
    "EXECUTION_EMISSION_REQUIRES_SEPARATE_BOUNDARY",
    "ACTION_CONSEQUENCE_REQUIRES_SEPARATE_BOUNDARY",
    "RECEIPT_EXHAUSTION_REQUIRED_AFTER_ANY_FUTURE_EXECUTION",
)

REQUIRED_NON_CLAIMS = (
    "operation_executed",
    "output_emitted",
    "action_authorized",
    "consequence_created",
    "repository_synchronization_authorized",
    "shared_live_state_created",
    "state_merge_authorized",
    "replay_authorized",
    "full_body_transfer_authorized",
    "second_body_created",
    "non_synchronized_operation_authorized",
    "carrier_autonomy_authorized",
    "stale_carrier_operation_authorized",
    "carrier_role_activated_beyond_scope",
    "carrier_authority_created",
    "carrier_currentness_created",
    "current_carrier_selected",
    "winning_carrier_selected",
    "losing_carrier_invalidated",
    "carrier_hierarchy_created",
    "source_replaced",
    "authority_created",
    "permission_created",
    "reusable_permission_created",
    "autonomous_continuation_authorized",
    "live_operation_refused",
    "live_operation_aborted",
    "refusal_abort_erased",
    "evidence_erased",
    "refusal_erased",
    "blocked_attempt_erased",
    "projection_mismatch_hidden",
    "divergence_resolved",
    "truth_created",
    "public_launch_readiness_created",
    "final_completion_claimed",
    "follow_on_work_authorized",
    "self_orientation_successor_scheduled",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
)

WHAT_REMAINS_OPEN = {
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
    "carrier_role_activation_beyond_admission_scope": "open_not_scheduled_not_authorized_not_executed",
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
        "ADMISSION_REVIEW_EXECUTES_OPERATION",
        (
            "operation_executed",
            "operation_execution_started",
            "distributed_operation_executed",
        ),
    ),
    (
        "ADMISSION_REVIEW_EMITS_OUTPUT",
        (
            "output_emitted",
            "emission_created",
            "operation_output_emitted",
            "output_generated",
        ),
    ),
    (
        "ADMISSION_REVIEW_AUTHORIZES_ACTION",
        (
            "action_authorized",
            "action_created",
            "truth_action_created",
        ),
    ),
    (
        "ADMISSION_REVIEW_CREATES_CONSEQUENCE",
        (
            "consequence_created",
            "consequence_action_created",
            "operation_consequence_created",
        ),
    ),
    (
        "ADMISSION_REVIEW_AUTHORIZES_SYNCHRONIZATION",
        (
            "repository_synchronization_authorized",
            "synchronization_authorized",
            "sync_authorized",
            "repository_sync_authorized",
            "shared_live_state_created",
            "state_merge_authorized",
            "state_merge_created",
            "replay_authorized",
            "merge_authorized",
        ),
    ),
    (
        "ADMISSION_REVIEW_AUTHORIZES_NON_SYNCHRONIZED_OPERATION",
        (
            "non_synchronized_operation_authorized",
            "non_sync_operation_authorized",
            "divergent_live_operation_authorized",
            "independent_carrier_operation_authorized",
        ),
    ),
    (
        "ADMISSION_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER",
        (
            "full_body_transfer_authorized",
            "full_body_transfer_created",
        ),
    ),
    (
        "ADMISSION_REVIEW_CREATES_SECOND_BODY",
        (
            "second_body_created",
            "second_body_authorized",
        ),
    ),
    (
        "ADMISSION_REVIEW_ACTIVATES_CARRIER_ROLES_BEYOND_SCOPE",
        (
            "carrier_role_activated_beyond_scope",
            "carrier_roles_activated_beyond_scope",
            "carrier_role_activated",
            "carrier_roles_activated",
            "carrier_role_assigned_for_operation",
            "carrier_assigned_to_live_operation",
        ),
    ),
    (
        "ADMISSION_REVIEW_CREATES_CARRIER_AUTHORITY",
        (
            "carrier_authority_created",
            "carrier_authority_granted",
            "authority_created",
            "authority_granted",
        ),
    ),
    (
        "ADMISSION_REVIEW_CREATES_CARRIER_CURRENTNESS",
        (
            "carrier_currentness_created",
            "currentness_created",
        ),
    ),
    ("ADMISSION_REVIEW_SELECTS_CURRENT_CARRIER", ("current_carrier_selected",)),
    (
        "ADMISSION_REVIEW_SELECTS_WINNING_CARRIER",
        (
            "winning_carrier_selected",
            "carrier_b_success_becomes_winner",
            "carrier_b_success_forces_continuation",
        ),
    ),
    (
        "ADMISSION_REVIEW_INVALIDATES_LOSING_CARRIER",
        (
            "losing_carrier_invalidated",
            "carrier_c_block_becomes_loser",
            "carrier_c_block_invalidates_carrier_c",
        ),
    ),
    (
        "ADMISSION_REVIEW_REPLACES_SOURCE",
        (
            "source_replaced",
            "source_replaced_by_carrier",
            "carrier_becomes_source",
        ),
    ),
    (
        "ADMISSION_REVIEW_CREATES_REUSABLE_PERMISSION",
        (
            "reusable_permission_created",
            "permission_created",
            "standing_permission_created",
        ),
    ),
    (
        "ADMISSION_REVIEW_AUTHORIZES_AUTONOMOUS_CONTINUATION",
        (
            "autonomous_continuation_authorized",
            "continuation_authorized",
            "autonomous_operation_authorized",
        ),
    ),
    (
        "ADMISSION_REVIEW_ERASES_REFUSAL_ABORT",
        (
            "refusal_abort_erased",
            "refusal_abort_conditions_erased",
            "non_admission_conditions_erased",
            "abort_conditions_erased",
        ),
    ),
    (
        "ADMISSION_REVIEW_ERASES_EVIDENCE_OR_REFUSAL",
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
    ("ADMISSION_REVIEW_RESOLVES_DIVERGENCE", ("divergence_resolved",)),
    (
        "ADMISSION_REVIEW_CREATES_PUBLIC_READINESS",
        (
            "public_launch_readiness_created",
            "public_readiness_created",
        ),
    ),
    (
        "ADMISSION_REVIEW_CLAIMS_FINAL_COMPLETION",
        (
            "final_completion_claimed",
            "final_governance_completed",
            "final_continuity_completed",
            "final_system_identity_completed",
        ),
    ),
    (
        "ADMISSION_REVIEW_SCHEDULES_FOLLOW_ON_WORK",
        (
            "follow_on_work_authorized",
            "follow_on_work_scheduled",
            "self_orientation_successor_scheduled",
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
    if isinstance(value, Mapping):
        return bool(value)
    if _is_sequence_not_text(value):
        return bool(value)
    return True


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


def _required_non_claims_false(operation_admitted: bool = False) -> dict[str, bool]:
    non_claims = {key: False for key in REQUIRED_NON_CLAIMS}
    non_claims["operation_admitted"] = bool(operation_admitted)
    return non_claims


def _requested_operation_admitted_allowed(request: Mapping[str, Any]) -> bool:
    return request.get("requested_admission_transition_outcome") in (None, OUTCOME_RECORDED)


def _declared_non_claims_are_false(request: Mapping[str, Any]) -> bool:
    non_claims = request.get("declared_non_claims")
    if not isinstance(non_claims, Mapping):
        return False
    for key in REQUIRED_NON_CLAIMS:
        if non_claims.get(key) is not False:
            return False
    admitted = non_claims.get("operation_admitted", False)
    if admitted is True and not _requested_operation_admitted_allowed(request):
        return False
    return admitted in (False, True)


def _sanitize_filename(value: Any) -> str:
    raw = _stringify(value).strip() or "distributed_operation_admission_transition"
    allowed = []
    for char in raw:
        if char.isalnum() or char in ("-", "_", "."):
            allowed.append(char)
        else:
            allowed.append("_")
    sanitized = "".join(allowed).strip("._")
    return sanitized or "distributed_operation_admission_transition"


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
    return _first_present(request.get("admission_transition_request_id"), request.get("request_id"))


def _find_key(value: Any, key: str) -> Any:
    if isinstance(value, Mapping):
        if key in value and _is_non_empty(value[key]):
            return value[key]
        for nested in value.values():
            found = _find_key(nested, key)
            if _is_non_empty(found):
                return found
    elif _is_sequence_not_text(value):
        for item in value:
            found = _find_key(item, key)
            if _is_non_empty(found):
                return found
    return None


def _extract_selected_refusal_abort_id(
    refusal_result: Mapping[str, Any],
    request: Mapping[str, Any],
) -> str | None:
    return _first_present(
        request.get("selected_refusal_abort_result_id"),
        _get_path_value(
            refusal_result,
            (
                "distributed_refusal_abort_metadata",
                "distributed_refusal_abort_result_id",
            ),
        ),
        refusal_result.get("distributed_refusal_abort_result_id"),
        _get_path_value(refusal_result, ("distributed_refusal_abort_summary", "refusal_abort_request_id")),
        _get_path_value(refusal_result, ("declared_refusal_abort_question", "refusal_abort_request_id")),
        refusal_result.get("refusal_abort_request_id"),
        refusal_result.get("result_id"),
    )


def _extract_selected_refusal_abort_outcome(
    refusal_result: Mapping[str, Any],
    request: Mapping[str, Any],
) -> str | None:
    return _first_present(
        request.get("selected_refusal_abort_result_outcome"),
        refusal_result.get("outcome"),
        _get_path_value(refusal_result, ("distributed_refusal_abort_summary", "outcome")),
        refusal_result.get("selected_refusal_abort_result_outcome"),
    )


def _extract_failed_check_count(result: Mapping[str, Any]) -> int | None:
    candidates = (
        _get_path_value(result, ("distributed_refusal_abort_summary", "failed_check_count")),
        _get_path_value(result, ("refusal_abort_statement", "failed_check_count")),
        result.get("failed_check_count"),
    )
    for candidate in candidates:
        if candidate is not None:
            try:
                return int(candidate)
            except (TypeError, ValueError):
                return None
    checks = result.get("refusal_abort_checks")
    if _is_sequence_not_text(checks):
        return _failed_check_count([check for check in checks if isinstance(check, Mapping)])
    return None


def _load_selected_refusal_abort_result(
    request: Mapping[str, Any],
) -> tuple[dict[str, Any], str | None, str | None, str | None]:
    path_value = request.get("selected_refusal_abort_result_path")
    if _is_non_empty(path_value):
        path = Path(str(path_value))
        loaded, error, detail = _read_json_object(path)
        if error == "unreadable":
            return {}, str(path), "REFUSAL_ABORT_RESULT_UNREADABLE", detail
        if error == "malformed":
            return {}, str(path), "REFUSAL_ABORT_RESULT_MALFORMED", detail
        return _copy(loaded), str(path), None, None

    selected = request.get("selected_refusal_abort_result")
    if isinstance(selected, Mapping):
        return _copy(selected), None, None, None
    if selected is not None:
        return {}, None, "REFUSAL_ABORT_RESULT_MALFORMED", "selected_refusal_abort_result is not an object"
    return {}, None, None, None


def _load_request_from_path(path_value: Path | str) -> tuple[dict[str, Any] | None, str | None, str | None]:
    path = Path(path_value)
    loaded, error, detail = _read_json_object(path)
    if error == "unreadable":
        return None, "DECLARED_ADMISSION_TRANSITION_REQUEST_UNREADABLE", detail
    if error == "malformed":
        return None, "DECLARED_ADMISSION_TRANSITION_REQUEST_MALFORMED", detail
    assert loaded is not None
    loaded = _copy(loaded)
    loaded["admission_transition_request_path"] = str(path)
    return loaded, None, None


def _get_section(
    request: Mapping[str, Any],
    refusal_result: Mapping[str, Any],
    request_key: str,
    refusal_paths: Sequence[Sequence[str]],
) -> Any:
    request_value = request.get(request_key)
    if _is_non_empty(request_value):
        return _copy(request_value)
    basis_map = _as_mapping(request.get("admission_transition_basis"))
    if _is_non_empty(basis_map.get(request_key)):
        return _copy(basis_map.get(request_key))
    for path in refusal_paths:
        value = _get_path_value(refusal_result, path)
        if _is_non_empty(value):
            return _copy(value)
    found = _find_key(refusal_result, request_key)
    if _is_non_empty(found):
        return _copy(found)
    return None


def _selected_sync_non_sync_result(request: Mapping[str, Any], refusal_result: Mapping[str, Any]) -> Any:
    return _get_section(
        request,
        refusal_result,
        "selected_sync_non_sync_result",
        (
            ("selected_operation_matter", "selected_sync_non_sync_result"),
            ("refusal_abort_basis", "selected_sync_non_sync_result"),
            ("selected_sync_non_sync_result", "selected_sync_non_sync_result"),
        ),
    )


def _selected_carrier_role_result(request: Mapping[str, Any], refusal_result: Mapping[str, Any]) -> Any:
    return _get_section(
        request,
        refusal_result,
        "selected_carrier_role_result",
        (
            ("selected_operation_matter", "selected_carrier_role_result"),
            ("refusal_abort_basis", "selected_carrier_role_result"),
        ),
    )


def _selected_source_body_authority_result(request: Mapping[str, Any], refusal_result: Mapping[str, Any]) -> Any:
    return _get_section(
        request,
        refusal_result,
        "selected_source_body_authority_result",
        (
            ("selected_operation_matter", "selected_source_body_authority_result"),
            ("refusal_abort_basis", "selected_source_body_authority_result"),
        ),
    )


def _selected_eligibility_result(request: Mapping[str, Any], refusal_result: Mapping[str, Any]) -> Any:
    return _get_section(
        request,
        refusal_result,
        "selected_eligibility_result",
        (
            ("selected_operation_matter", "selected_eligibility_result"),
            ("refusal_abort_basis", "selected_eligibility_result"),
        ),
    )


def _selected_matter_declaration(request: Mapping[str, Any], refusal_result: Mapping[str, Any]) -> Any:
    return _get_section(
        request,
        refusal_result,
        "selected_matter_declaration",
        (
            ("selected_operation_matter", "selected_matter_declaration"),
            ("selected_operation_matter", "selected_matter_declaration_result"),
            ("refusal_abort_basis", "selected_matter_declaration"),
        ),
    )


def _selected_operation_candidate(request: Mapping[str, Any], refusal_result: Mapping[str, Any]) -> Any:
    return _get_section(
        request,
        refusal_result,
        "selected_operation_candidate",
        (
            ("selected_operation_matter", "selected_operation_candidate"),
            ("refusal_abort_basis", "selected_operation_candidate"),
        ),
    )


def _selected_operation_matter(request: Mapping[str, Any], refusal_result: Mapping[str, Any]) -> Any:
    return _get_section(
        request,
        refusal_result,
        "selected_operation_matter",
        (
            ("selected_operation_matter", "selected_operation_matter"),
            ("refusal_abort_basis", "selected_operation_matter"),
        ),
    )


def _basis_value(
    request: Mapping[str, Any],
    refusal_result: Mapping[str, Any],
    key: str,
    *fallback_values: Any,
) -> Any:
    basis_map = _as_mapping(request.get("admission_transition_basis"))
    return _first_present(
        request.get(key),
        basis_map.get(key),
        _get_path_value(refusal_result, ("admission_transition_basis", key)),
        _get_path_value(refusal_result, ("refusal_abort_basis", key)),
        *fallback_values,
    )


def _source_body_authority_basis(
    request: Mapping[str, Any],
    refusal_result: Mapping[str, Any],
    selected_source_body_authority_result: Any,
) -> Any:
    return _basis_value(
        request,
        refusal_result,
        "source_body_authority_basis",
        _find_key(selected_source_body_authority_result, "source_body_authority_basis"),
        _find_key(selected_source_body_authority_result, "source_body_lineage_basis"),
    )


def _carrier_role_basis(
    request: Mapping[str, Any],
    refusal_result: Mapping[str, Any],
    selected_carrier_role_result: Any,
) -> Any:
    return _basis_value(
        request,
        refusal_result,
        "carrier_role_basis",
        _find_key(selected_carrier_role_result, "carrier_role_basis"),
        _find_key(selected_carrier_role_result, "selected_carrier_role_basis"),
    )


def _sync_non_sync_posture_basis(request: Mapping[str, Any], refusal_result: Mapping[str, Any]) -> Any:
    return _basis_value(
        request,
        refusal_result,
        "sync_non_sync_posture_basis",
        _get_path_value(refusal_result, ("selected_sync_non_sync_result", "sync_non_sync_postures")),
        _find_key(refusal_result, "sync_non_sync_postures"),
    )


def _refusal_abort_posture_basis(request: Mapping[str, Any], refusal_result: Mapping[str, Any]) -> Any:
    return _basis_value(
        request,
        refusal_result,
        "refusal_abort_posture_basis",
        refusal_result.get("refusal_abort_postures"),
        _get_path_value(refusal_result, ("refusal_abort_postures", "selected_refusal_abort_postures")),
    )


def _context_value(request: Mapping[str, Any], refusal_result: Mapping[str, Any], key: str) -> Any:
    return _basis_value(request, refusal_result, key)


def _coerce_scope_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value] if value.strip() else []
    if isinstance(value, Mapping):
        for key in (
            "selected_admission_scope",
            "admission_scope_values",
            "admission_scope",
            "selected_scope",
            "scope",
        ):
            nested = value.get(key)
            if nested is not None and nested is not value:
                return _coerce_scope_list(nested)
        return [str(item) for item in value.values() if isinstance(item, str) and item.strip()]
    if _is_sequence_not_text(value):
        scope: list[str] = []
        for item in value:
            if isinstance(item, str) and item.strip():
                scope.append(item)
            elif isinstance(item, Mapping):
                name = _first_present(item.get("scope"), item.get("scope_name"), item.get("name"))
                if name:
                    scope.append(str(name))
        return scope
    return []


def _selected_admission_scope(request: Mapping[str, Any]) -> list[str]:
    return _coerce_scope_list(request.get("admission_scope"))


def _unsupported_admission_scope(scope_values: Sequence[str]) -> list[str]:
    supported = set(SUPPORTED_ADMISSION_SCOPE)
    return [scope for scope in scope_values if scope not in supported]


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


def _refusal_statement_bool(
    refusal_result: Mapping[str, Any],
    key: str,
    default: bool = True,
) -> bool:
    value = _first_present_allow_zero(
        _get_path_value(refusal_result, ("refusal_abort_statement", key)),
        _get_path_value(refusal_result, ("distributed_refusal_abort_summary", key)),
        _get_path_value(refusal_result, ("refusal_abort_basis", key)),
        _get_path_value(refusal_result, ("refusal_abort_postures", key)),
    )
    if value is None:
        return default
    return bool(value)


def _build_declared_question(
    request: Mapping[str, Any],
    selected_refusal_abort_id: str | None,
    selected_refusal_abort_outcome: str | None,
) -> dict[str, Any]:
    return {
        "admission_transition_request_id": _extract_request_id(request),
        "admission_transition_question": request.get("admission_transition_question"),
        "admission_transition_intent": request.get("admission_transition_intent"),
        "admission_transition_request_path": request.get("admission_transition_request_path"),
        "selected_refusal_abort_result_id": selected_refusal_abort_id,
        "selected_refusal_abort_result_outcome": selected_refusal_abort_outcome,
        "expected_selected_refusal_abort_outcome": request.get(
            "expected_selected_refusal_abort_outcome",
            EXPECTED_SELECTED_REFUSAL_ABORT_OUTCOME,
        ),
        "admission_transition_boundary_is_not_execution": True,
        "admission_transition_boundary_is_not_emission": True,
        "admission_transition_boundary_is_not_action": True,
        "admission_transition_boundary_is_not_consequence": True,
        "admission_transition_boundary_is_not_synchronization": True,
        "admission_transition_boundary_is_not_full_body_transfer": True,
        "admission_transition_boundary_is_not_second_body_creation": True,
        "admission_transition_boundary_is_not_reusable_permission": True,
        "admission_transition_boundary_is_not_autonomous_continuation": True,
    }


def _build_selected_refusal_abort_section(
    refusal_result: Mapping[str, Any],
    path: str | None,
    selected_refusal_abort_id: str | None,
    selected_refusal_abort_outcome: str | None,
    failed_count: int | None,
) -> dict[str, Any]:
    return {
        "selected_refusal_abort_result": _copy(refusal_result) if refusal_result else None,
        "selected_refusal_abort_result_path": path,
        "selected_refusal_abort_result_id": selected_refusal_abort_id,
        "selected_refusal_abort_result_outcome": selected_refusal_abort_outcome,
        "selected_refusal_abort_result_outcome_is_recorded": selected_refusal_abort_outcome
        == EXPECTED_SELECTED_REFUSAL_ABORT_OUTCOME,
        "selected_refusal_abort_result_failed_check_count": failed_count,
        "selected_refusal_abort_result_failed_check_count_zero": failed_count == 0,
        "selected_refusal_abort_result_remains_boundary_posture_only": True,
        "selected_refusal_abort_result_did_not_refuse_live_operation": True,
        "selected_refusal_abort_result_did_not_abort_live_operation": True,
        "selected_refusal_abort_result_did_not_admit_operation": True,
        "selected_refusal_abort_result_did_not_authorize_operation": True,
        "selected_refusal_abort_result_did_not_execute_operation": True,
        "selected_refusal_abort_result_preserved_refusal_abort_postures": _refusal_statement_bool(
            refusal_result, "refusal_abort_postures_preserved", True
        ),
        "selected_refusal_abort_result_preserved_non_admission_conditions": _refusal_statement_bool(
            refusal_result, "non_admission_conditions_named", True
        ),
        "selected_refusal_abort_result_preserved_abort_conditions": _refusal_statement_bool(
            refusal_result, "abort_conditions_named", True
        ),
        "selected_refusal_abort_result_preserved_carrier_b_success_without_forced_continuation": (
            _refusal_statement_bool(refusal_result, "carrier_b_success_does_not_force_continuation", True)
        ),
        "selected_refusal_abort_result_preserved_carrier_c_block_without_invalidation": _refusal_statement_bool(
            refusal_result, "carrier_c_block_does_not_invalidate_carrier_c", True
        ),
        "selected_refusal_abort_result_preserved_divergence": _refusal_statement_bool(
            refusal_result, "divergence_remains_visible", True
        ),
        "selected_refusal_abort_result_preserved_refusal": _refusal_statement_bool(
            refusal_result, "refusal_remains_visible", True
        ),
        "selected_refusal_abort_result_preserved_blocked_attempts": _refusal_statement_bool(
            refusal_result, "blocked_attempts_remain_visible", True
        ),
        "selected_refusal_abort_result_preserved_projection_mismatch": _refusal_statement_bool(
            refusal_result, "projection_mismatch_remains_visible", True
        ),
        "selected_refusal_abort_result_is_not_mutated": True,
    }


def _build_selected_operation_matter(
    request: Mapping[str, Any],
    refusal_result: Mapping[str, Any],
    selected_sync_non_sync_result: Any,
    selected_carrier_role_result: Any,
    selected_source_body_authority_result: Any,
    selected_eligibility_result: Any,
    selected_matter_declaration: Any,
    selected_operation_candidate: Any,
    selected_operation_matter: Any,
) -> dict[str, Any]:
    return {
        "selected_refusal_abort_result": _copy(refusal_result) if refusal_result else None,
        "selected_sync_non_sync_result": _copy(selected_sync_non_sync_result),
        "selected_carrier_role_result": _copy(selected_carrier_role_result),
        "selected_source_body_authority_result": _copy(selected_source_body_authority_result),
        "selected_eligibility_result": _copy(selected_eligibility_result),
        "selected_matter_declaration": _copy(selected_matter_declaration),
        "selected_operation_candidate": _copy(selected_operation_candidate),
        "selected_operation_matter": _copy(selected_operation_matter),
        "selected_operation_question": _first_present(
            request.get("selected_operation_question"),
            _get_path_value(refusal_result, ("selected_operation_matter", "selected_operation_question")),
            _find_key(selected_operation_candidate, "operation_question"),
            _find_key(selected_operation_matter, "operation_question"),
        ),
        "selected_operation_purpose": _first_present(
            request.get("selected_operation_purpose"),
            _get_path_value(refusal_result, ("selected_operation_matter", "selected_operation_purpose")),
            _find_key(selected_operation_candidate, "operation_purpose"),
            _find_key(selected_operation_matter, "operation_purpose"),
        ),
        "selected_proposed_operation_kind": _first_present(
            request.get("selected_proposed_operation_kind"),
            request.get("proposed_operation_kind"),
            _get_path_value(refusal_result, ("selected_operation_matter", "proposed_operation_kind")),
            _find_key(selected_operation_candidate, "proposed_operation_kind"),
            _find_key(selected_operation_matter, "proposed_operation_kind"),
        ),
        "refusal_abort_remains_boundary_posture_only": True,
        "sync_non_sync_remains_boundary_posture_only": True,
        "carrier_role_basis_remains_role_basis_only": True,
        "authority_remains_basis_only": True,
        "eligibility_remains_eligibility_only": True,
        "matter_remains_declaration_only": True,
        "operation_executed": False,
        "output_emitted": False,
        "action_authorized": False,
        "consequence_created": False,
    }


def _build_admission_transition_basis(
    request: Mapping[str, Any],
    refusal_result: Mapping[str, Any],
    selected_sync_non_sync_result: Any,
    selected_carrier_role_result: Any,
    selected_source_body_authority_result: Any,
    selected_eligibility_result: Any,
    selected_matter_declaration: Any,
    selected_operation_candidate: Any,
    selected_operation_matter: Any,
    source_body_authority_basis: Any,
    carrier_role_basis: Any,
    sync_non_sync_posture_basis: Any,
    refusal_abort_posture_basis: Any,
    admission_scope: Sequence[str],
) -> dict[str, Any]:
    basis_map = _as_mapping(request.get("admission_transition_basis"))
    operation_context_scope = _first_present(
        request.get("operation_context_scope"),
        basis_map.get("operation_context_scope"),
    )
    return {
        "selected_refusal_abort_result": _copy(refusal_result) if refusal_result else None,
        "selected_sync_non_sync_result": _copy(selected_sync_non_sync_result),
        "selected_carrier_role_result": _copy(selected_carrier_role_result),
        "selected_source_body_authority_result": _copy(selected_source_body_authority_result),
        "selected_eligibility_result": _copy(selected_eligibility_result),
        "selected_matter_declaration": _copy(selected_matter_declaration),
        "selected_operation_candidate": _copy(selected_operation_candidate),
        "selected_operation_matter": _copy(selected_operation_matter),
        "source_body_authority_basis": _copy(source_body_authority_basis),
        "carrier_role_basis": _copy(carrier_role_basis),
        "sync_non_sync_posture_basis": _copy(sync_non_sync_posture_basis),
        "refusal_abort_posture_basis": _copy(refusal_abort_posture_basis),
        "carrier_b_success_context": _copy(_context_value(request, refusal_result, "carrier_b_success_context")),
        "carrier_c_block_context": _copy(_context_value(request, refusal_result, "carrier_c_block_context")),
        "b_c_divergence_context": _copy(_context_value(request, refusal_result, "b_c_divergence_context")),
        "refusal_blocked_attempt_context": _copy(
            _context_value(request, refusal_result, "refusal_blocked_attempt_context")
        ),
        "projection_mismatch_context": _copy(_context_value(request, refusal_result, "projection_mismatch_context")),
        "declared_admission_scope": list(admission_scope),
        "declared_operation_context_scope": _copy(operation_context_scope),
        "execution_emission_successor_boundary_requirement": _copy(
            _first_present(
                request.get("execution_emission_successor_boundary_requirement"),
                basis_map.get("execution_emission_successor_boundary_requirement"),
            )
        ),
        "action_consequence_successor_boundary_requirement": _copy(
            _first_present(
                request.get("action_consequence_successor_boundary_requirement"),
                basis_map.get("action_consequence_successor_boundary_requirement"),
            )
        ),
        "receipt_exhaustion_successor_boundary_requirement": _copy(
            _first_present(
                request.get("receipt_exhaustion_successor_boundary_requirement"),
                basis_map.get("receipt_exhaustion_successor_boundary_requirement"),
            )
        ),
        "refusal_abort_conditions_carry_forward": True,
        "carrier_b_success_does_not_force_continuation": True,
        "carrier_c_block_remains_visible": True,
        "carrier_c_block_does_not_invalidate_carrier_c": True,
        "b_c_divergence_remains_visible": True,
        "divergence_remains_visible": True,
        "refusal_remains_visible": True,
        "blocked_attempts_remain_visible": True,
        "projection_mismatch_remains_visible": True,
        "admission_basis_is_not_execution": True,
        "admission_basis_is_not_emission": True,
        "admission_basis_is_not_action": True,
        "admission_basis_is_not_consequence": True,
        "admission_basis_is_not_synchronization": True,
        "admission_basis_is_not_full_body_transfer": True,
        "admission_basis_is_not_second_body": True,
        "admission_basis_is_not_reusable_permission": True,
        "admission_basis_is_not_autonomous_continuation": True,
    }


def _build_admission_scope(scope_values: Sequence[str], unsupported: Sequence[str]) -> dict[str, Any]:
    scope_set = set(scope_values)
    return {
        "selected_admission_scope": list(scope_values),
        "supported_admission_scope": list(SUPPORTED_ADMISSION_SCOPE),
        "unsupported_admission_scope": list(unsupported),
        "all_selected_admission_scope_supported": not unsupported and bool(scope_values),
        "one_operation_context_only": "ONE_OPERATION_CONTEXT_ONLY" in scope_set,
        "no_execution_in_admission": "NO_EXECUTION_IN_ADMISSION" in scope_set,
        "no_emission_in_admission": "NO_EMISSION_IN_ADMISSION" in scope_set,
        "no_action_in_admission": "NO_ACTION_IN_ADMISSION" in scope_set,
        "no_consequence_in_admission": "NO_CONSEQUENCE_IN_ADMISSION" in scope_set,
        "no_repository_sync_in_admission": "NO_REPOSITORY_SYNC_IN_ADMISSION" in scope_set,
        "no_non_synchronized_operation_in_admission": (
            "NO_NON_SYNCHRONIZED_OPERATION_IN_ADMISSION" in scope_set
        ),
        "no_full_body_transfer_in_admission": "NO_FULL_BODY_TRANSFER_IN_ADMISSION" in scope_set,
        "no_second_body_in_admission": "NO_SECOND_BODY_IN_ADMISSION" in scope_set,
        "refusal_abort_conditions_carry_forward": "REFUSAL_ABORT_CONDITIONS_CARRY_FORWARD" in scope_set,
        "execution_emission_requires_separate_boundary": (
            "EXECUTION_EMISSION_REQUIRES_SEPARATE_BOUNDARY" in scope_set
        ),
        "action_consequence_requires_separate_boundary": (
            "ACTION_CONSEQUENCE_REQUIRES_SEPARATE_BOUNDARY" in scope_set
        ),
        "receipt_exhaustion_required_after_any_future_execution": (
            "RECEIPT_EXHAUSTION_REQUIRED_AFTER_ANY_FUTURE_EXECUTION" in scope_set
        ),
        "no_reusable_permission": True,
        "no_autonomous_continuation": True,
    }


def _build_additional_basis_required(outcome: str, request: Mapping[str, Any]) -> dict[str, Any]:
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
            "admission scope too generic",
            "operation context scope too broad",
            "execution / emission successor boundary requirement not explicit enough",
            "action / consequence successor boundary requirement not explicit enough",
            "receipt / exhaustion successor boundary requirement not explicit enough",
            "refusal / abort carry-forward basis unclear",
            "source-body authority basis not specific enough for admission",
            "carrier role basis creates activation ambiguity",
            "sync/non-sync basis creates merge/no-sync ambiguity",
            "proposed output family creates consequence ambiguity",
            "admission cannot yet be bounded without reusable permission risk",
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
        "operation_executed",
        "output_emitted",
        "action_authorized",
        "consequence_created",
        "repository_synchronization_authorized",
        "non_synchronized_operation_authorized",
        "shared_live_state_created",
        "state_merge_authorized",
        "replay_authorized",
        "full_body_transfer_authorized",
        "second_body_created",
        "live_refusal_executed",
        "live_abort_executed",
        "carrier_roles_activated_beyond_admission_scope",
        "carrier_authority_created",
        "carrier_currentness_created",
        "current_carrier_selected",
        "winning_carrier_selected",
        "losing_carrier_invalidated",
        "source_replaced",
        "authority_newly_created",
        "reusable_permission_created",
        "autonomous_continuation_authorized",
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
    selected_refusal_present: bool,
    selected_refusal_outcome: str | None,
    selected_refusal_failed_count: int | None,
    selected_sync_non_sync_result: Any,
    selected_carrier_role_result: Any,
    selected_source_body_authority_result: Any,
    selected_eligibility_result: Any,
    selected_matter_declaration: Any,
    selected_operation_candidate: Any,
    selected_operation_matter: Any,
    refusal_abort_posture_basis: Any,
    sync_non_sync_posture_basis: Any,
    admission_scope: Sequence[str],
    unsupported_scope: Sequence[str],
    checks: Sequence[Mapping[str, Any]],
    request: Mapping[str, Any],
    block_code: str | None,
    block_reason: str | None,
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    not_admitted = outcome == OUTCOME_NOT_ADMITTED
    requires_additional = outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    scope_set = set(admission_scope)
    all_scope_supported = not unsupported_scope and bool(admission_scope)
    return {
        "distributed_operation_admission_transition_authority_recorded": recorded,
        "admission_transition_authority_recorded": recorded,
        "not_admitted": not_admitted,
        "requires_additional_basis": requires_additional,
        "operation_admitted": recorded,
        "one_bounded_operation_context_admitted": recorded,
        "selected_refusal_abort_result_preserved": selected_refusal_present,
        "selected_refusal_abort_result_recorded": selected_refusal_outcome
        == EXPECTED_SELECTED_REFUSAL_ABORT_OUTCOME,
        "selected_refusal_abort_result_failed_check_count_zero": selected_refusal_failed_count == 0,
        "selected_sync_non_sync_result_preserved": _is_non_empty(selected_sync_non_sync_result),
        "selected_carrier_role_result_preserved": _is_non_empty(selected_carrier_role_result),
        "selected_source_body_authority_result_preserved": _is_non_empty(selected_source_body_authority_result),
        "selected_eligibility_result_preserved": _is_non_empty(selected_eligibility_result),
        "selected_matter_declaration_preserved": _is_non_empty(selected_matter_declaration),
        "selected_operation_candidate_preserved": _is_non_empty(selected_operation_candidate),
        "selected_operation_matter_preserved": _is_non_empty(selected_operation_matter),
        "refusal_abort_postures_preserved": _is_non_empty(refusal_abort_posture_basis),
        "non_admission_conditions_named": True,
        "abort_conditions_named": True,
        "refusal_abort_conditions_carry_forward": "REFUSAL_ABORT_CONDITIONS_CARRY_FORWARD" in scope_set,
        "sync_non_sync_postures_preserved": _is_non_empty(sync_non_sync_posture_basis),
        "carrier_evidence_remains_unmerged": True,
        "carrier_context_remains_context_only": True,
        "divergence_remains_visible": True,
        "refusal_remains_visible": True,
        "blocked_attempts_remain_visible": True,
        "projection_mismatch_remains_visible": True,
        "admission_scope_preserved": bool(admission_scope),
        "admission_scope_supported": all_scope_supported,
        "admission_scope_one_operation_context_only": "ONE_OPERATION_CONTEXT_ONLY" in scope_set,
        "execution_emission_successor_boundary_required": (
            "EXECUTION_EMISSION_REQUIRES_SEPARATE_BOUNDARY" in scope_set
        ),
        "action_consequence_successor_boundary_required": (
            "ACTION_CONSEQUENCE_REQUIRES_SEPARATE_BOUNDARY" in scope_set
        ),
        "receipt_exhaustion_successor_boundary_required": (
            "RECEIPT_EXHAUSTION_REQUIRED_AFTER_ANY_FUTURE_EXECUTION" in scope_set
        ),
        "operation_executed": False,
        "output_emitted": False,
        "action_authorized": False,
        "consequence_created": False,
        "repository_synchronization_authorized": False,
        "shared_live_state_created": False,
        "state_merge_authorized": False,
        "replay_authorized": False,
        "full_body_transfer_authorized": False,
        "second_body_created": False,
        "non_synchronized_operation_authorized": False,
        "carrier_autonomy_authorized": False,
        "stale_carrier_operation_authorized": False,
        "reusable_permission_created": False,
        "autonomous_continuation_authorized": False,
        "public_launch_readiness_created": False,
        "final_completion_claimed": False,
        "follow_on_work_authorized": False,
        "not_admitted_reason": request.get("not_admitted_reason") if not_admitted else None,
        "additional_basis_reason": request.get("additional_basis_reason") if requires_additional else None,
        "block_code": block_code,
        "block_reason": block_reason,
        "passed_check_count": _passed_check_count(checks),
        "failed_check_count": _failed_check_count(checks),
    }


def _build_checks(
    request: Mapping[str, Any],
    refusal_result: Mapping[str, Any],
    refusal_load_block_code: str | None,
    selected_refusal_outcome: str | None,
    selected_refusal_failed_count: int | None,
    selected_sync_non_sync_result: Any,
    selected_carrier_role_result: Any,
    selected_source_body_authority_result: Any,
    selected_eligibility_result: Any,
    selected_matter_declaration: Any,
    selected_operation_candidate: Any,
    selected_operation_matter: Any,
    source_body_authority_basis: Any,
    carrier_role_basis: Any,
    sync_non_sync_posture_basis: Any,
    refusal_abort_posture_basis: Any,
    admission_scope: Sequence[str],
    unsupported_scope: Sequence[str],
) -> list[dict[str, Any]]:
    question = request.get("admission_transition_question")
    intent = request.get("admission_transition_intent")
    basis_map = _as_mapping(request.get("admission_transition_basis"))
    operation_context_scope = _first_present(request.get("operation_context_scope"), basis_map.get("operation_context_scope"))
    execution_requirement = _first_present(
        request.get("execution_emission_successor_boundary_requirement"),
        basis_map.get("execution_emission_successor_boundary_requirement"),
    )
    action_requirement = _first_present(
        request.get("action_consequence_successor_boundary_requirement"),
        basis_map.get("action_consequence_successor_boundary_requirement"),
    )
    receipt_requirement = _first_present(
        request.get("receipt_exhaustion_successor_boundary_requirement"),
        basis_map.get("receipt_exhaustion_successor_boundary_requirement"),
    )
    collapse_values = (
        request,
        request.get("admission_transition_basis"),
        request.get("admission_scope"),
        request.get("declared_non_claims"),
    )
    refusal_collapse_values = (
        _as_mapping(refusal_result.get("refusal_abort_statement")),
        _as_mapping(refusal_result.get("non_claims")),
    )
    scope_set = set(admission_scope)
    checks = [
        _make_check(
            "admission / transition question declared",
            _is_non_empty(question),
            "declared admission / transition question",
            question,
            "ADMISSION_TRANSITION_QUESTION_UNDECLARED",
        ),
        _make_check(
            "admission / transition intent supported",
            intent in SUPPORTED_INTENTS,
            list(SUPPORTED_INTENTS),
            intent,
            "ADMISSION_TRANSITION_INTENT_UNSUPPORTED",
        ),
        _make_check(
            "selected refusal / abort result present",
            _is_non_empty(refusal_result) and refusal_load_block_code is None,
            "selected refusal / abort result object",
            "present" if _is_non_empty(refusal_result) else "missing",
            refusal_load_block_code or "REFUSAL_ABORT_RESULT_MISSING",
        ),
        _make_check(
            "selected refusal / abort result outcome declared",
            _is_non_empty(selected_refusal_outcome),
            "selected refusal / abort outcome declared",
            selected_refusal_outcome,
            "REFUSAL_ABORT_RESULT_OUTCOME_MISSING",
        ),
        _make_check(
            "selected refusal / abort result outcome recorded",
            selected_refusal_outcome == EXPECTED_SELECTED_REFUSAL_ABORT_OUTCOME,
            EXPECTED_SELECTED_REFUSAL_ABORT_OUTCOME,
            selected_refusal_outcome,
            "REFUSAL_ABORT_RESULT_NOT_RECORDED",
        ),
        _make_check(
            "selected refusal / abort result failed check count zero",
            selected_refusal_failed_count == 0,
            0,
            selected_refusal_failed_count,
            "REFUSAL_ABORT_RESULT_HAS_FAILED_CHECKS",
        ),
        _make_check(
            "selected sync/non-sync result preserved",
            _is_non_empty(selected_sync_non_sync_result),
            "selected sync/non-sync result preserved",
            "present" if _is_non_empty(selected_sync_non_sync_result) else "missing",
            "SYNC_NON_SYNC_RESULT_MISSING",
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
            "source-body authority basis preserved",
            _is_non_empty(source_body_authority_basis),
            "source-body authority basis",
            "present" if _is_non_empty(source_body_authority_basis) else "missing",
            "SOURCE_BODY_AUTHORITY_RESULT_MISSING",
        ),
        _make_check(
            "carrier role basis preserved",
            _is_non_empty(carrier_role_basis),
            "carrier role basis",
            "present" if _is_non_empty(carrier_role_basis) else "missing",
            "CARRIER_ROLE_RESULT_MISSING",
        ),
        _make_check(
            "sync/non-sync posture basis preserved",
            _is_non_empty(sync_non_sync_posture_basis),
            "sync/non-sync posture basis",
            "present" if _is_non_empty(sync_non_sync_posture_basis) else "missing",
            "SYNC_NON_SYNC_RESULT_MISSING",
        ),
        _make_check(
            "refusal / abort posture basis preserved",
            _is_non_empty(refusal_abort_posture_basis),
            "refusal / abort posture basis",
            "present" if _is_non_empty(refusal_abort_posture_basis) else "missing",
            "REFUSAL_ABORT_RESULT_MISSING",
        ),
        _make_check(
            "refusal / abort postures preserved",
            _refusal_statement_bool(refusal_result, "refusal_abort_postures_preserved", True),
            True,
            _refusal_statement_bool(refusal_result, "refusal_abort_postures_preserved", True),
            "REFUSAL_ABORT_RESULT_MALFORMED",
        ),
        _make_check(
            "non-admission conditions named",
            _refusal_statement_bool(refusal_result, "non_admission_conditions_named", True),
            True,
            _refusal_statement_bool(refusal_result, "non_admission_conditions_named", True),
            "REFUSAL_ABORT_RESULT_MALFORMED",
        ),
        _make_check(
            "abort conditions named",
            _refusal_statement_bool(refusal_result, "abort_conditions_named", True),
            True,
            _refusal_statement_bool(refusal_result, "abort_conditions_named", True),
            "REFUSAL_ABORT_RESULT_MALFORMED",
        ),
        _make_check(
            "refusal / abort conditions carry forward",
            "REFUSAL_ABORT_CONDITIONS_CARRY_FORWARD" in scope_set,
            "REFUSAL_ABORT_CONDITIONS_CARRY_FORWARD",
            list(admission_scope),
            "ADMISSION_SCOPE_MISSING",
        ),
        _make_check(
            "sync/non-sync postures preserved",
            _is_non_empty(sync_non_sync_posture_basis),
            "sync/non-sync postures preserved",
            "present" if _is_non_empty(sync_non_sync_posture_basis) else "missing",
            "SYNC_NON_SYNC_RESULT_MISSING",
        ),
        _make_check(
            "carrier evidence remains unmerged",
            _refusal_statement_bool(refusal_result, "carrier_evidence_remains_unmerged", True),
            True,
            _refusal_statement_bool(refusal_result, "carrier_evidence_remains_unmerged", True),
            "REFUSAL_ABORT_RESULT_MALFORMED",
        ),
        _make_check(
            "carrier context remains context only",
            _refusal_statement_bool(refusal_result, "carrier_context_remains_context_only", True),
            True,
            _refusal_statement_bool(refusal_result, "carrier_context_remains_context_only", True),
            "REFUSAL_ABORT_RESULT_MALFORMED",
        ),
        _make_check(
            "divergence remains visible",
            _refusal_statement_bool(refusal_result, "divergence_remains_visible", True),
            True,
            _refusal_statement_bool(refusal_result, "divergence_remains_visible", True),
            "ADMISSION_REVIEW_ERASES_EVIDENCE_OR_REFUSAL",
        ),
        _make_check(
            "refusal remains visible",
            _refusal_statement_bool(refusal_result, "refusal_remains_visible", True),
            True,
            _refusal_statement_bool(refusal_result, "refusal_remains_visible", True),
            "ADMISSION_REVIEW_ERASES_EVIDENCE_OR_REFUSAL",
        ),
        _make_check(
            "blocked attempts remain visible",
            _refusal_statement_bool(refusal_result, "blocked_attempts_remain_visible", True),
            True,
            _refusal_statement_bool(refusal_result, "blocked_attempts_remain_visible", True),
            "ADMISSION_REVIEW_ERASES_EVIDENCE_OR_REFUSAL",
        ),
        _make_check(
            "projection mismatch remains visible",
            _refusal_statement_bool(refusal_result, "projection_mismatch_remains_visible", True),
            True,
            _refusal_statement_bool(refusal_result, "projection_mismatch_remains_visible", True),
            "ADMISSION_REVIEW_ERASES_EVIDENCE_OR_REFUSAL",
        ),
        _make_check(
            "admission scope one operation context only",
            "ONE_OPERATION_CONTEXT_ONLY" in scope_set,
            "ONE_OPERATION_CONTEXT_ONLY",
            list(admission_scope),
            "ADMISSION_SCOPE_MISSING",
        ),
        _make_check(
            "selected admission scope supported",
            bool(admission_scope) and not unsupported_scope,
            list(SUPPORTED_ADMISSION_SCOPE),
            list(admission_scope),
            "UNSUPPORTED_ADMISSION_SCOPE" if unsupported_scope else "ADMISSION_SCOPE_MISSING",
        ),
        _make_check(
            "operation context scope declared",
            _is_non_empty(operation_context_scope),
            "declared operation context scope",
            operation_context_scope,
            "OPERATION_CONTEXT_SCOPE_MISSING",
        ),
        _make_check(
            "execution / emission successor boundary required",
            "EXECUTION_EMISSION_REQUIRES_SEPARATE_BOUNDARY" in scope_set and _is_non_empty(execution_requirement),
            "separate execution / emission boundary required",
            execution_requirement,
            "EXECUTION_EMISSION_SUCCESSOR_BOUNDARY_REQUIREMENT_MISSING",
        ),
        _make_check(
            "action / consequence successor boundary required",
            "ACTION_CONSEQUENCE_REQUIRES_SEPARATE_BOUNDARY" in scope_set and _is_non_empty(action_requirement),
            "separate action / consequence boundary required",
            action_requirement,
            "ACTION_CONSEQUENCE_SUCCESSOR_BOUNDARY_REQUIREMENT_MISSING",
        ),
        _make_check(
            "receipt / exhaustion successor boundary required",
            "RECEIPT_EXHAUSTION_REQUIRED_AFTER_ANY_FUTURE_EXECUTION" in scope_set
            and _is_non_empty(receipt_requirement),
            "receipt / exhaustion boundary required",
            receipt_requirement,
            "RECEIPT_EXHAUSTION_SUCCESSOR_BOUNDARY_REQUIREMENT_MISSING",
        ),
    ]
    collapse_checks = [
        (
            "no operation executed",
            ("operation_executed", "operation_execution_started", "distributed_operation_executed"),
            "ADMISSION_REVIEW_EXECUTES_OPERATION",
        ),
        (
            "no output emitted",
            ("output_emitted", "emission_created", "operation_output_emitted"),
            "ADMISSION_REVIEW_EMITS_OUTPUT",
        ),
        (
            "no action authorized",
            ("action_authorized", "action_created", "truth_action_created"),
            "ADMISSION_REVIEW_AUTHORIZES_ACTION",
        ),
        (
            "no consequence created",
            ("consequence_created", "consequence_action_created", "operation_consequence_created"),
            "ADMISSION_REVIEW_CREATES_CONSEQUENCE",
        ),
        (
            "no sync/shared live state/merge/replay/full body transfer/second body/non-sync operation/carrier autonomy/stale carrier operation",
            (
                "repository_synchronization_authorized",
                "synchronization_authorized",
                "shared_live_state_created",
                "state_merge_authorized",
                "replay_authorized",
                "full_body_transfer_authorized",
                "second_body_created",
                "non_synchronized_operation_authorized",
                "carrier_autonomy_authorized",
                "stale_carrier_operation_authorized",
            ),
            _first_collapse_code(*collapse_values) or "ADMISSION_REVIEW_AUTHORIZES_SYNCHRONIZATION",
        ),
        (
            "no reusable permission created",
            ("reusable_permission_created", "permission_created", "standing_permission_created"),
            "ADMISSION_REVIEW_CREATES_REUSABLE_PERMISSION",
        ),
        (
            "no autonomous continuation authorized",
            ("autonomous_continuation_authorized", "continuation_authorized"),
            "ADMISSION_REVIEW_AUTHORIZES_AUTONOMOUS_CONTINUATION",
        ),
        (
            "no carrier role activated beyond admission scope",
            (
                "carrier_role_activated_beyond_scope",
                "carrier_roles_activated_beyond_scope",
                "carrier_role_activated",
                "carrier_roles_activated",
                "carrier_role_assigned_for_operation",
            ),
            "ADMISSION_REVIEW_ACTIVATES_CARRIER_ROLES_BEYOND_SCOPE",
        ),
        (
            "no carrier authority/currentness/hierarchy created",
            (
                "carrier_authority_created",
                "authority_created",
                "carrier_currentness_created",
                "carrier_hierarchy_created",
            ),
            _first_collapse_code(*collapse_values) or "ADMISSION_REVIEW_CREATES_CARRIER_AUTHORITY",
        ),
        (
            "no current/winning/losing carrier selected",
            (
                "current_carrier_selected",
                "winning_carrier_selected",
                "losing_carrier_invalidated",
            ),
            _first_collapse_code(*collapse_values) or "ADMISSION_REVIEW_SELECTS_CURRENT_CARRIER",
        ),
        (
            "no source replacement",
            ("source_replaced", "source_replaced_by_carrier", "carrier_becomes_source"),
            "ADMISSION_REVIEW_REPLACES_SOURCE",
        ),
        (
            "no refusal / abort erased",
            (
                "refusal_abort_erased",
                "refusal_abort_conditions_erased",
                "non_admission_conditions_erased",
                "abort_conditions_erased",
            ),
            "ADMISSION_REVIEW_ERASES_REFUSAL_ABORT",
        ),
        (
            "no evidence/refusal/block/projection mismatch erased",
            (
                "evidence_erased",
                "refusal_erased",
                "blocked_attempt_erased",
                "projection_mismatch_hidden",
                "refusal_hidden",
                "blocked_attempt_hidden",
                "blocked_attempts_hidden",
            ),
            "ADMISSION_REVIEW_ERASES_EVIDENCE_OR_REFUSAL",
        ),
        (
            "no divergence resolved",
            ("divergence_resolved",),
            "ADMISSION_REVIEW_RESOLVES_DIVERGENCE",
        ),
        (
            "no live operation refused or aborted",
            ("live_operation_refused", "live_operation_aborted"),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
        (
            "no public readiness/final completion/follow-on work",
            (
                "public_launch_readiness_created",
                "public_readiness_created",
                "final_completion_claimed",
                "follow_on_work_authorized",
                "follow_on_work_scheduled",
                "self_orientation_successor_scheduled",
            ),
            _first_collapse_code(*collapse_values) or "ADMISSION_REVIEW_SCHEDULES_FOLLOW_ON_WORK",
        ),
        (
            "no mutation/replay/merge",
            ("mutation_performed", "replay_performed", "merge_performed"),
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        ),
    ]
    for check_name, fields, failure_code in collapse_checks:
        detected = _has_true_field(collapse_values, fields) or _has_true_field(refusal_collapse_values, fields)
        checks.append(
            _make_check(
                check_name,
                not detected,
                False,
                "true detected" if detected else False,
                _first_collapse_code(*collapse_values, *refusal_collapse_values) or failure_code,
            )
        )
    checks.append(
        _make_check(
            "non-claims remain false except bounded operation_admitted",
            _declared_non_claims_are_false(request),
            {key: False for key in REQUIRED_NON_CLAIMS},
            request.get("declared_non_claims"),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
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
    intent = request.get("admission_transition_intent")
    if intent == INTENT_BLOCK:
        code = "ADMISSION_TRANSITION_REVIEW_REQUEST_EXPLICITLY_BLOCKED"
        return OUTCOME_BLOCKED, code, _block_reason_for_code(code, request, load_detail)

    requested_outcome = request.get("requested_admission_transition_outcome")
    if requested_outcome in (OUTCOME_NOT_ADMITTED, OUTCOME_REQUIRES_ADDITIONAL_BASIS):
        if _failed_check_count(checks) == 0:
            return requested_outcome, None, None

    collapse_code = _first_collapse_code(
        request,
        request.get("admission_transition_basis"),
        request.get("admission_scope"),
        request.get("declared_non_claims"),
    )
    block_code = load_block_code or collapse_code or _first_failed_code(checks)
    if block_code:
        return OUTCOME_BLOCKED, block_code, _block_reason_for_code(block_code, request, load_detail)

    if intent == INTENT_DO_NOT_RECORD:
        return OUTCOME_NOT_ADMITTED, None, None

    if requested_outcome == OUTCOME_RECORDED or requested_outcome is None:
        if _is_non_empty(request.get("not_admitted_reason")):
            return OUTCOME_NOT_ADMITTED, None, None
        if _is_non_empty(request.get("additional_basis_context")):
            return OUTCOME_REQUIRES_ADDITIONAL_BASIS, None, None
        return OUTCOME_RECORDED, None, None

    if requested_outcome == OUTCOME_BLOCKED:
        code = "ADMISSION_TRANSITION_REVIEW_REQUEST_EXPLICITLY_BLOCKED"
        return OUTCOME_BLOCKED, code, _block_reason_for_code(code, request, load_detail)

    code = "ADMISSION_TRANSITION_INTENT_UNSUPPORTED"
    return OUTCOME_BLOCKED, code, _block_reason_for_code(code, request, load_detail)


def _build_metadata(request: Mapping[str, Any], selected_refusal_abort_id: str | None) -> dict[str, Any]:
    basis_id = _first_present(_extract_request_id(request), selected_refusal_abort_id, "admission_transition")
    return {
        "distributed_operation_admission_transition_result_id": (
            f"{_sanitize_filename(basis_id)}__distributed_operation_admission_transition_authority_result"
        ),
        "distributed_operation_admission_transition_result_type": RESULT_TYPE,
        "distributed_operation_admission_transition_result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
    }


def _assemble_result(
    request: Mapping[str, Any],
    refusal_result: Mapping[str, Any],
    selected_refusal_path: str | None,
    refusal_load_block_code: str | None,
    refusal_load_detail: str | None,
) -> dict[str, Any]:
    selected_refusal_id = _extract_selected_refusal_abort_id(refusal_result, request)
    selected_refusal_outcome = _extract_selected_refusal_abort_outcome(refusal_result, request)
    selected_refusal_failed_count = _extract_failed_check_count(refusal_result)
    selected_sync_non_sync_result = _selected_sync_non_sync_result(request, refusal_result)
    selected_carrier_role_result = _selected_carrier_role_result(request, refusal_result)
    selected_source_body_authority_result = _selected_source_body_authority_result(request, refusal_result)
    selected_eligibility_result = _selected_eligibility_result(request, refusal_result)
    selected_matter_declaration = _selected_matter_declaration(request, refusal_result)
    selected_operation_candidate = _selected_operation_candidate(request, refusal_result)
    selected_operation_matter = _selected_operation_matter(request, refusal_result)
    source_body_authority_basis = _source_body_authority_basis(
        request,
        refusal_result,
        selected_source_body_authority_result,
    )
    carrier_role_basis = _carrier_role_basis(request, refusal_result, selected_carrier_role_result)
    sync_posture_basis = _sync_non_sync_posture_basis(request, refusal_result)
    refusal_posture_basis = _refusal_abort_posture_basis(request, refusal_result)
    admission_scope = _selected_admission_scope(request)
    unsupported_scope = _unsupported_admission_scope(admission_scope)

    checks = _build_checks(
        request,
        refusal_result,
        refusal_load_block_code,
        selected_refusal_outcome,
        selected_refusal_failed_count,
        selected_sync_non_sync_result,
        selected_carrier_role_result,
        selected_source_body_authority_result,
        selected_eligibility_result,
        selected_matter_declaration,
        selected_operation_candidate,
        selected_operation_matter,
        source_body_authority_basis,
        carrier_role_basis,
        sync_posture_basis,
        refusal_posture_basis,
        admission_scope,
        unsupported_scope,
    )
    outcome, block_code, block_reason = _determine_outcome_and_block(
        request,
        checks,
        refusal_load_block_code,
        refusal_load_detail,
    )
    operation_admitted = outcome == OUTCOME_RECORDED
    metadata = _build_metadata(request, selected_refusal_id)
    statement = _build_statement(
        outcome,
        _is_non_empty(refusal_result),
        selected_refusal_outcome,
        selected_refusal_failed_count,
        selected_sync_non_sync_result,
        selected_carrier_role_result,
        selected_source_body_authority_result,
        selected_eligibility_result,
        selected_matter_declaration,
        selected_operation_candidate,
        selected_operation_matter,
        refusal_posture_basis,
        sync_posture_basis,
        admission_scope,
        unsupported_scope,
        checks,
        request,
        block_code,
        block_reason,
    )
    result: dict[str, Any] = {
        "distributed_operation_admission_transition_metadata": metadata,
        "declared_admission_transition_question": _build_declared_question(
            request,
            selected_refusal_id,
            selected_refusal_outcome,
        ),
        "selected_refusal_abort_result": _build_selected_refusal_abort_section(
            refusal_result,
            selected_refusal_path,
            selected_refusal_id,
            selected_refusal_outcome,
            selected_refusal_failed_count,
        ),
        "selected_operation_matter": _build_selected_operation_matter(
            request,
            refusal_result,
            selected_sync_non_sync_result,
            selected_carrier_role_result,
            selected_source_body_authority_result,
            selected_eligibility_result,
            selected_matter_declaration,
            selected_operation_candidate,
            selected_operation_matter,
        ),
        "admission_transition_basis": _build_admission_transition_basis(
            request,
            refusal_result,
            selected_sync_non_sync_result,
            selected_carrier_role_result,
            selected_source_body_authority_result,
            selected_eligibility_result,
            selected_matter_declaration,
            selected_operation_candidate,
            selected_operation_matter,
            source_body_authority_basis,
            carrier_role_basis,
            sync_posture_basis,
            refusal_posture_basis,
            admission_scope,
        ),
        "admission_scope": _build_admission_scope(admission_scope, unsupported_scope),
        "admission_transition_checks": checks,
        "admission_transition_statement": statement,
        "admission_transition_non_meaning": _build_non_meaning(),
        "additional_basis_required": _build_additional_basis_required(outcome, request),
        "what_remains_open": _copy(WHAT_REMAINS_OPEN),
        "non_claims": _required_non_claims_false(operation_admitted),
        "outcome": outcome,
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "block_code": block_code,
            "block_reason": block_reason,
        },
    }
    result["distributed_operation_admission_transition_summary"] = (
        build_distributed_operation_admission_transition_authority_summary(result)
    )
    return result


def _blocked_result_for_malformed_request(
    block_code: str,
    block_reason: str | None = None,
    request_path: str | None = None,
) -> dict[str, Any]:
    request: dict[str, Any] = {
        "admission_transition_request_id": None,
        "admission_transition_question": None,
        "admission_transition_intent": None,
        "admission_transition_request_path": request_path,
        "admission_scope": [],
        "declared_non_claims": _required_non_claims_false(False),
    }
    result = _assemble_result(request, {}, None, None, None)
    result["outcome"] = OUTCOME_BLOCKED
    result["block"] = {
        "blocked": True,
        "block_code": block_code,
        "block_reason": block_reason or block_code.lower().replace("_", " "),
    }
    result["admission_transition_statement"]["distributed_operation_admission_transition_authority_recorded"] = False
    result["admission_transition_statement"]["admission_transition_authority_recorded"] = False
    result["admission_transition_statement"]["operation_admitted"] = False
    result["admission_transition_statement"]["one_bounded_operation_context_admitted"] = False
    result["admission_transition_statement"]["block_code"] = block_code
    result["admission_transition_statement"]["block_reason"] = result["block"]["block_reason"]
    result["non_claims"] = _required_non_claims_false(False)
    result["distributed_operation_admission_transition_summary"] = (
        build_distributed_operation_admission_transition_authority_summary(result)
    )
    return result


def resolve_distributed_operation_admission_transition_authority_boundary(
    declared_admission_transition_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one declared distributed operation admission / transition request."""

    if declared_admission_transition_request is None:
        return _blocked_result_for_malformed_request("ADMISSION_TRANSITION_QUESTION_UNDECLARED")
    if not isinstance(declared_admission_transition_request, Mapping):
        return _blocked_result_for_malformed_request("DECLARED_ADMISSION_TRANSITION_REQUEST_MALFORMED")

    request = _copy(dict(declared_admission_transition_request))
    refusal_result, selected_refusal_path, refusal_load_block_code, refusal_load_detail = (
        _load_selected_refusal_abort_result(request)
    )
    return _assemble_result(
        request,
        refusal_result,
        selected_refusal_path,
        refusal_load_block_code,
        refusal_load_detail,
    )


def resolve_distributed_operation_admission_transition_authority_boundary_from_path(
    declared_admission_transition_request_path: Path | str,
) -> dict:
    """Resolve one admission / transition request from a JSON object file."""

    path = Path(declared_admission_transition_request_path)
    request, block_code, detail = _load_request_from_path(path)
    if block_code:
        return _blocked_result_for_malformed_request(block_code, detail, str(path))
    assert request is not None
    return resolve_distributed_operation_admission_transition_authority_boundary(request)


def build_distributed_operation_admission_transition_authority_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a bounded summary from an admission / transition result."""

    declared = _as_mapping(result.get("declared_admission_transition_question"))
    selected_refusal = _as_mapping(result.get("selected_refusal_abort_result"))
    selected_operation = _as_mapping(result.get("selected_operation_matter"))
    statement = _as_mapping(result.get("admission_transition_statement"))
    checks = result.get("admission_transition_checks")
    checks_list = [check for check in checks if isinstance(check, Mapping)] if _is_sequence_not_text(checks) else []
    block = _as_mapping(result.get("block"))
    non_claims = _as_mapping(result.get("non_claims"))
    selected_operation_candidate = selected_operation.get("selected_operation_candidate")
    selected_operation_matter = selected_operation.get("selected_operation_matter")
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "admission_transition_request_id": declared.get("admission_transition_request_id"),
        "admission_transition_question": declared.get("admission_transition_question"),
        "admission_transition_intent": declared.get("admission_transition_intent"),
        "selected_refusal_abort_result_id": selected_refusal.get("selected_refusal_abort_result_id"),
        "selected_refusal_abort_result_outcome": selected_refusal.get("selected_refusal_abort_result_outcome"),
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
        "admission_transition_authority_recorded": statement.get(
            "admission_transition_authority_recorded"
        )
        is True,
        "distributed_operation_admission_transition_authority_recorded": statement.get(
            "distributed_operation_admission_transition_authority_recorded"
        )
        is True,
        "not_admitted": statement.get("not_admitted") is True,
        "requires_additional_basis": statement.get("requires_additional_basis") is True,
        "operation_admitted": statement.get("operation_admitted") is True,
        "one_bounded_operation_context_admitted": statement.get("one_bounded_operation_context_admitted")
        is True,
        "selected_refusal_abort_result_preserved": statement.get("selected_refusal_abort_result_preserved")
        is True,
        "selected_refusal_abort_result_recorded": statement.get("selected_refusal_abort_result_recorded")
        is True,
        "selected_refusal_abort_result_failed_check_count_zero": statement.get(
            "selected_refusal_abort_result_failed_check_count_zero"
        )
        is True,
        "selected_sync_non_sync_result_preserved": statement.get("selected_sync_non_sync_result_preserved")
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
        "refusal_abort_postures_preserved": statement.get("refusal_abort_postures_preserved") is True,
        "non_admission_conditions_named": statement.get("non_admission_conditions_named") is True,
        "abort_conditions_named": statement.get("abort_conditions_named") is True,
        "refusal_abort_conditions_carry_forward": statement.get("refusal_abort_conditions_carry_forward")
        is True,
        "sync_non_sync_postures_preserved": statement.get("sync_non_sync_postures_preserved") is True,
        "carrier_evidence_remains_unmerged": statement.get("carrier_evidence_remains_unmerged") is True,
        "carrier_context_remains_context_only": statement.get("carrier_context_remains_context_only") is True,
        "divergence_remains_visible": statement.get("divergence_remains_visible") is True,
        "refusal_remains_visible": statement.get("refusal_remains_visible") is True,
        "blocked_attempts_remain_visible": statement.get("blocked_attempts_remain_visible") is True,
        "projection_mismatch_remains_visible": statement.get("projection_mismatch_remains_visible") is True,
        "admission_scope_one_operation_context_only": statement.get("admission_scope_one_operation_context_only")
        is True,
        "execution_emission_successor_boundary_required": statement.get(
            "execution_emission_successor_boundary_required"
        )
        is True,
        "action_consequence_successor_boundary_required": statement.get(
            "action_consequence_successor_boundary_required"
        )
        is True,
        "receipt_exhaustion_successor_boundary_required": statement.get(
            "receipt_exhaustion_successor_boundary_required"
        )
        is True,
        "no_operation_executed_output_emitted_action_consequence": (
            statement.get("operation_executed") is False
            and statement.get("output_emitted") is False
            and statement.get("action_authorized") is False
            and statement.get("consequence_created") is False
        ),
        "no_sync_full_body_transfer_second_body_non_sync_operation": (
            statement.get("repository_synchronization_authorized") is False
            and statement.get("full_body_transfer_authorized") is False
            and statement.get("second_body_created") is False
            and statement.get("non_synchronized_operation_authorized") is False
        ),
        "no_reusable_permission_autonomous_continuation": (
            statement.get("reusable_permission_created") is False
            and statement.get("autonomous_continuation_authorized") is False
        ),
        "no_public_readiness_final_completion_follow_on_work": (
            statement.get("public_launch_readiness_created") is False
            and statement.get("final_completion_claimed") is False
            and statement.get("follow_on_work_authorized") is False
        ),
        "key_non_claims": {
            key: non_claims.get(key)
            for key in (
                "operation_admitted",
                "operation_executed",
                "output_emitted",
                "action_authorized",
                "consequence_created",
                "repository_synchronization_authorized",
                "non_synchronized_operation_authorized",
                "full_body_transfer_authorized",
                "second_body_created",
                "reusable_permission_created",
                "autonomous_continuation_authorized",
                "public_launch_readiness_created",
                "final_completion_claimed",
                "follow_on_work_authorized",
            )
        },
    }


def write_distributed_operation_admission_transition_authority_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write an admission / transition authority result as additive JSON."""

    if not isinstance(result, Mapping):
        raise DistributedOperationAdmissionTransitionAuthorityBoundaryError("result must be a mapping")
    if output_path is None:
        declared = _as_mapping(result.get("declared_admission_transition_question"))
        selected_refusal = _as_mapping(result.get("selected_refusal_abort_result"))
        basis_id = _first_present(
            declared.get("admission_transition_request_id"),
            selected_refusal.get("selected_refusal_abort_result_id"),
            _get_path_value(
                result,
                (
                    "distributed_operation_admission_transition_metadata",
                    "distributed_operation_admission_transition_result_id",
                ),
            ),
            "distributed_operation_admission_transition",
        )
        filename = (
            f"{_sanitize_filename(basis_id)}__"
            "distributed_operation_admission_transition_result.json"
        )
        target = DISTRIBUTED_OPERATION_ADMISSION_TRANSITION_AUTHORITY_BOUNDARY_ROOT / filename
    else:
        target = Path(output_path)
    target = _deduplicate_path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    return target


def build_declared_distributed_operation_admission_transition_authority_request(
    admission_transition_request_id: str,
    admission_transition_question: str,
    selected_refusal_abort_result: Mapping[str, Any] | str,
    admission_transition_basis: Mapping[str, Any] | str,
    admission_scope: Sequence[str] | Mapping[str, Any],
    admission_transition_intent: str = INTENT_RECORD,
    *,
    selected_refusal_abort_result_path: str | None = None,
    selected_refusal_abort_result_id: str | None = None,
    selected_refusal_abort_result_outcome: str | None = None,
    requested_admission_transition_outcome: str = OUTCOME_RECORDED,
    operation_context_scope: Mapping[str, Any] | str | None = None,
    additional_basis_context: Mapping[str, Any] | None = None,
    not_admitted_reason: str | None = None,
) -> dict:
    """Build a bounded declared admission / transition authority request."""

    operation_admitted = requested_admission_transition_outcome == OUTCOME_RECORDED
    basis: dict[str, Any]
    if isinstance(admission_transition_basis, Mapping):
        basis = _copy(dict(admission_transition_basis))
    else:
        basis = {"admission_transition_basis_reference": admission_transition_basis}

    operation_context = (
        _copy(operation_context_scope)
        if operation_context_scope is not None
        else {"operation_context_scope": "ONE_OPERATION_CONTEXT_ONLY"}
    )
    basis.setdefault("operation_context_scope", _copy(operation_context))
    basis.setdefault(
        "execution_emission_successor_boundary_requirement",
        {"required": True, "boundary": "distributed execution / emission boundary"},
    )
    basis.setdefault(
        "action_consequence_successor_boundary_requirement",
        {"required": True, "boundary": "distributed action / consequence boundary"},
    )
    basis.setdefault(
        "receipt_exhaustion_successor_boundary_requirement",
        {"required": True, "boundary": "distributed operation receipt / exhaustion"},
    )

    request: dict[str, Any] = {
        "admission_transition_request_id": admission_transition_request_id,
        "admission_transition_question": admission_transition_question,
        "admission_transition_intent": admission_transition_intent,
        "admission_transition_basis": basis,
        "admission_scope": _copy(admission_scope),
        "selected_refusal_abort_result_id": selected_refusal_abort_result_id,
        "selected_refusal_abort_result_outcome": selected_refusal_abort_result_outcome,
        "requested_admission_transition_outcome": requested_admission_transition_outcome,
        "operation_context_scope": _copy(operation_context),
        "execution_emission_successor_boundary_requirement": _copy(
            basis["execution_emission_successor_boundary_requirement"]
        ),
        "action_consequence_successor_boundary_requirement": _copy(
            basis["action_consequence_successor_boundary_requirement"]
        ),
        "receipt_exhaustion_successor_boundary_requirement": _copy(
            basis["receipt_exhaustion_successor_boundary_requirement"]
        ),
        "additional_basis_context": _copy(additional_basis_context) if additional_basis_context else {},
        "not_admitted_reason": not_admitted_reason,
        "declared_non_claims": _required_non_claims_false(operation_admitted),
    }
    if selected_refusal_abort_result_path is not None:
        request["selected_refusal_abort_result_path"] = selected_refusal_abort_result_path
    elif isinstance(selected_refusal_abort_result, Mapping):
        request["selected_refusal_abort_result"] = _copy(selected_refusal_abort_result)
    else:
        request["selected_refusal_abort_result_path"] = str(selected_refusal_abort_result)

    return request
