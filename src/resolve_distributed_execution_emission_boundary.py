"""Resolve the distributed execution / emission boundary.

This module records boundary basis only. It does not execute an operation,
emit output, authorize action, create consequence, synchronize repositories,
authorize non-synchronized operation, transfer the body, create a second body,
erase refusal / abort, create reusable permission, authorize autonomous
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


class DistributedExecutionEmissionBoundaryError(Exception):
    """Raised for hard execution / emission boundary failures."""


RESOLVER_MODULE = "resolve_distributed_execution_emission_boundary"
RESULT_VERSION = "0.1.0"
RESULT_TYPE = "distributed_execution_emission_boundary_result"
RESULT_ID_PREFIX = "distributed_execution_emission_boundary"

DISTRIBUTED_EXECUTION_EMISSION_BOUNDARY_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_distributed_execution_emission_boundary"
)

EXPECTED_SELECTED_ADMISSION_TRANSITION_OUTCOME = (
    "DISTRIBUTED_OPERATION_ADMISSION_TRANSITION_AUTHORITY_RECORDED"
)

OUTCOME_RECORDED = "DISTRIBUTED_EXECUTION_EMISSION_BOUNDARY_RECORDED"
OUTCOME_NOT_READY = "DISTRIBUTED_EXECUTION_EMISSION_BOUNDARY_NOT_READY"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "DISTRIBUTED_EXECUTION_EMISSION_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "DISTRIBUTED_EXECUTION_EMISSION_REVIEW_BLOCKED"
OUTCOME_FAMILY = {
    OUTCOME_RECORDED,
    OUTCOME_NOT_READY,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
}

INTENT_RECORD = "RECORD_DISTRIBUTED_EXECUTION_EMISSION_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_DISTRIBUTED_EXECUTION_EMISSION_BOUNDARY"
INTENT_BLOCK = "BLOCK_DISTRIBUTED_EXECUTION_EMISSION_REVIEW"
SUPPORTED_INTENTS = {INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK}

SUPPORTED_EXECUTION_EMISSION_SCOPE = (
    "ONE_ADMITTED_OPERATION_CONTEXT_ONLY",
    "NO_EXECUTION_PERFORMED_BY_BOUNDARY",
    "NO_OUTPUT_EMITTED_BY_BOUNDARY",
    "NO_ACTION_AUTHORIZED_BY_BOUNDARY",
    "NO_CONSEQUENCE_CREATED_BY_BOUNDARY",
    "NO_REPOSITORY_SYNC_BY_BOUNDARY",
    "NO_NON_SYNCHRONIZED_OPERATION_BY_BOUNDARY",
    "NO_FULL_BODY_TRANSFER_BY_BOUNDARY",
    "NO_SECOND_BODY_BY_BOUNDARY",
    "REFUSAL_ABORT_CONDITIONS_REMAIN_ACTIVE",
    "RECEIPT_EXHAUSTION_REQUIRED_BEFORE_CLOSURE",
    "ACTION_CONSEQUENCE_REQUIRES_SEPARATE_BOUNDARY",
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

COLLAPSE_FIELDS = {
    "EXECUTION_EMISSION_REVIEW_EXECUTES_OPERATION": (
        "operation_executed",
        "operation_execution_started",
        "distributed_operation_executed",
    ),
    "EXECUTION_EMISSION_REVIEW_EMITS_OUTPUT": (
        "output_emitted",
        "emission_created",
        "operation_output_emitted",
        "output_generated",
    ),
    "EXECUTION_EMISSION_REVIEW_AUTHORIZES_ACTION": (
        "action_authorized",
        "action_created",
        "truth_action_created",
        "truth_created",
    ),
    "EXECUTION_EMISSION_REVIEW_CREATES_CONSEQUENCE": (
        "consequence_created",
        "consequence_action_created",
        "operation_consequence_created",
    ),
    "EXECUTION_EMISSION_REVIEW_AUTHORIZES_SYNCHRONIZATION": (
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
    "EXECUTION_EMISSION_REVIEW_AUTHORIZES_NON_SYNCHRONIZED_OPERATION": (
        "non_synchronized_operation_authorized",
        "non_sync_operation_authorized",
        "carrier_autonomy_authorized",
        "stale_carrier_operation_authorized",
        "divergent_live_operation_authorized",
        "independent_carrier_operation_authorized",
    ),
    "EXECUTION_EMISSION_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER": (
        "full_body_transfer_authorized",
        "full_body_transfer_created",
    ),
    "EXECUTION_EMISSION_REVIEW_CREATES_SECOND_BODY": (
        "second_body_created",
        "second_body_authorized",
    ),
    "EXECUTION_EMISSION_REVIEW_ACTIVATES_CARRIER_ROLES_BEYOND_SCOPE": (
        "carrier_role_activated_beyond_scope",
        "carrier_roles_activated_beyond_scope",
        "carrier_role_activated",
        "carrier_roles_activated",
        "carrier_role_assigned_for_operation",
        "carrier_assigned_to_live_operation",
    ),
    "EXECUTION_EMISSION_REVIEW_CREATES_CARRIER_AUTHORITY": (
        "carrier_authority_created",
        "carrier_authority_granted",
        "authority_created",
        "authority_granted",
    ),
    "EXECUTION_EMISSION_REVIEW_CREATES_CARRIER_CURRENTNESS": (
        "carrier_currentness_created",
        "currentness_created",
    ),
    "EXECUTION_EMISSION_REVIEW_SELECTS_CURRENT_CARRIER": (
        "current_carrier_selected",
    ),
    "EXECUTION_EMISSION_REVIEW_SELECTS_WINNING_CARRIER": (
        "winning_carrier_selected",
        "carrier_b_success_becomes_winner",
        "carrier_b_success_forces_continuation",
    ),
    "EXECUTION_EMISSION_REVIEW_INVALIDATES_LOSING_CARRIER": (
        "losing_carrier_invalidated",
        "carrier_c_block_becomes_loser",
        "carrier_c_block_invalidates_carrier_c",
    ),
    "EXECUTION_EMISSION_REVIEW_REPLACES_SOURCE": (
        "source_replaced",
        "source_replaced_by_carrier",
        "carrier_becomes_source",
    ),
    "EXECUTION_EMISSION_REVIEW_CREATES_REUSABLE_PERMISSION": (
        "reusable_permission_created",
        "permission_created",
        "standing_permission_created",
    ),
    "EXECUTION_EMISSION_REVIEW_AUTHORIZES_AUTONOMOUS_CONTINUATION": (
        "autonomous_continuation_authorized",
        "continuation_authorized",
        "autonomous_operation_authorized",
    ),
    "EXECUTION_EMISSION_REVIEW_ERASES_REFUSAL_ABORT": (
        "refusal_abort_erased",
        "refusal_abort_conditions_erased",
        "non_admission_conditions_erased",
        "abort_conditions_erased",
    ),
    "EXECUTION_EMISSION_REVIEW_ERASES_EVIDENCE_OR_REFUSAL": (
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
    "EXECUTION_EMISSION_REVIEW_RESOLVES_DIVERGENCE": (
        "divergence_resolved",
    ),
    "EXECUTION_EMISSION_REVIEW_CREATES_PUBLIC_READINESS": (
        "public_launch_readiness_created",
        "public_readiness_created",
    ),
    "EXECUTION_EMISSION_REVIEW_CLAIMS_FINAL_COMPLETION": (
        "final_completion_claimed",
        "final_governance_completed",
        "final_continuity_completed",
        "final_system_identity_completed",
    ),
    "EXECUTION_EMISSION_REVIEW_SCHEDULES_FOLLOW_ON_WORK": (
        "follow_on_work_authorized",
        "follow_on_work_scheduled",
        "self_orientation_successor_scheduled",
    ),
    "MUTATION_REPLAY_OR_MERGE_DETECTED": (
        "mutation_performed",
        "replay_performed",
        "merge_performed",
    ),
}

BLOCK_REASON_BY_CODE = {
    "DECLARED_EXECUTION_EMISSION_REQUEST_MALFORMED": (
        "Declared execution / emission request is not a mapping."
    ),
    "DECLARED_EXECUTION_EMISSION_REQUEST_UNREADABLE": (
        "Declared execution / emission request path is unreadable."
    ),
    "EXECUTION_EMISSION_REVIEW_REQUEST_EXPLICITLY_BLOCKED": (
        "Declared execution / emission request explicitly blocks review."
    ),
    "EXECUTION_EMISSION_QUESTION_UNDECLARED": (
        "Execution / emission question is undeclared."
    ),
    "EXECUTION_EMISSION_INTENT_UNSUPPORTED": (
        "Execution / emission intent is unsupported."
    ),
    "ADMISSION_TRANSITION_RESULT_MISSING": (
        "Selected admission / transition result is missing."
    ),
    "ADMISSION_TRANSITION_RESULT_UNREADABLE": (
        "Selected admission / transition result path is unreadable."
    ),
    "ADMISSION_TRANSITION_RESULT_MALFORMED": (
        "Selected admission / transition result is malformed."
    ),
    "ADMISSION_TRANSITION_RESULT_OUTCOME_MISSING": (
        "Selected admission / transition result outcome is missing."
    ),
    "ADMISSION_TRANSITION_RESULT_NOT_RECORDED": (
        "Selected admission / transition result is not recorded."
    ),
    "ADMISSION_TRANSITION_RESULT_HAS_FAILED_CHECKS": (
        "Selected admission / transition result has failed checks."
    ),
    "ADMITTED_OPERATION_CONTEXT_MISSING": (
        "Admitted operation context is missing."
    ),
    "OPERATION_NOT_ADMITTED": "Selected operation is not admitted.",
    "ONE_BOUNDED_OPERATION_CONTEXT_NOT_ADMITTED": (
        "One bounded operation context was not admitted."
    ),
    "REFUSAL_ABORT_RESULT_MISSING": "Selected refusal / abort result is missing.",
    "SYNC_NON_SYNC_RESULT_MISSING": "Selected sync/non-sync result is missing.",
    "CARRIER_ROLE_RESULT_MISSING": "Selected carrier role result is missing.",
    "SOURCE_BODY_AUTHORITY_RESULT_MISSING": (
        "Selected source-body authority result is missing."
    ),
    "SELECTED_ELIGIBILITY_RESULT_MISSING": (
        "Selected eligibility result is missing."
    ),
    "SELECTED_MATTER_DECLARATION_MISSING": (
        "Selected matter declaration is missing."
    ),
    "SELECTED_OPERATION_CANDIDATE_MISSING": (
        "Selected operation candidate is missing."
    ),
    "SELECTED_OPERATION_MATTER_MISSING": "Selected operation matter is missing.",
    "EXECUTION_EMISSION_SCOPE_MISSING": (
        "Declared execution / emission scope is missing."
    ),
    "PROPOSED_EXECUTION_CANDIDATE_MISSING": (
        "Proposed execution candidate is missing."
    ),
    "PROPOSED_EMISSION_CANDIDATE_MISSING": (
        "Proposed emission candidate is missing."
    ),
    "PROPOSED_OUTPUT_FAMILY_MISSING": "Proposed output family is missing.",
    "RECEIPT_EXHAUSTION_REQUIREMENT_MISSING": (
        "Receipt / exhaustion requirement is missing."
    ),
    "ACTION_CONSEQUENCE_SEPARATION_REQUIREMENT_MISSING": (
        "Action / consequence separation requirement is missing."
    ),
    "UNSUPPORTED_EXECUTION_EMISSION_SCOPE": (
        "Execution / emission scope contains an unsupported value."
    ),
    "NON_CLAIM_MISSING_OR_FLIPPED": (
        "A required execution / emission non-claim is missing or true."
    ),
}


def _utc_now() -> str:
    return datetime.datetime.now(datetime.UTC).replace(microsecond=0).isoformat()


def _deepcopy(value: Any) -> Any:
    return copy.deepcopy(value)


def _is_mapping(value: Any) -> bool:
    return isinstance(value, Mapping)


def _is_present(value: Any) -> bool:
    if value is None:
        return False
    if value == "":
        return False
    if isinstance(value, (list, tuple, set, dict)) and not value:
        return False
    return True


def _truthy(value: Any) -> bool:
    return value is True


def _get_path(mapping: Any, path: Sequence[str], default: Any = None) -> Any:
    current = mapping
    for key in path:
        if not isinstance(current, Mapping) or key not in current:
            return default
        current = current[key]
    return current


def _first_present(*values: Any) -> Any:
    for value in values:
        if _is_present(value):
            return value
    return None


def _find_first_present(mapping: Any, keys: Sequence[str]) -> Any:
    if not isinstance(mapping, Mapping):
        return None
    for key in keys:
        value = mapping.get(key)
        if _is_present(value):
            return value
    return None


def _contains_true(mapping: Any, keys: Sequence[str]) -> bool:
    if not isinstance(mapping, Mapping):
        return False
    return any(mapping.get(key) is True for key in keys)


def _read_json_object(path: Path | str) -> tuple[dict[str, Any] | None, str | None, str | None]:
    resolved_path = Path(path)
    try:
        with resolved_path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
    except FileNotFoundError:
        return None, "unreadable", f"Path not found: {resolved_path}"
    except OSError as exc:
        return None, "unreadable", str(exc)
    except json.JSONDecodeError as exc:
        return None, "malformed", str(exc)
    if not isinstance(payload, dict):
        return None, "malformed", "JSON payload is not an object."
    return payload, None, None


def _load_request_path(path: Path | str) -> dict[str, Any]:
    payload, error, detail = _read_json_object(path)
    if error == "unreadable":
        return _minimal_blocked_result(
            "DECLARED_EXECUTION_EMISSION_REQUEST_UNREADABLE",
            detail or BLOCK_REASON_BY_CODE[
                "DECLARED_EXECUTION_EMISSION_REQUEST_UNREADABLE"
            ],
            request_path=str(path),
        )
    if error == "malformed":
        return _minimal_blocked_result(
            "DECLARED_EXECUTION_EMISSION_REQUEST_MALFORMED",
            detail or "Declared execution / emission request JSON is malformed.",
            request_path=str(path),
        )
    assert payload is not None
    request = _deepcopy(payload)
    request["execution_emission_request_path"] = str(path)
    return resolve_distributed_execution_emission_boundary(request)


def _load_selected_admission_result(
    request: Mapping[str, Any],
) -> tuple[dict[str, Any] | None, str | None, str | None, str | None]:
    result_path = request.get("selected_admission_transition_result_path")
    if _is_present(result_path):
        payload, error, detail = _read_json_object(str(result_path))
        if error == "unreadable":
            return (
                None,
                "ADMISSION_TRANSITION_RESULT_UNREADABLE",
                detail or "Selected admission / transition result path is unreadable.",
                str(result_path),
            )
        if error == "malformed":
            return (
                None,
                "ADMISSION_TRANSITION_RESULT_MALFORMED",
                detail or "Selected admission / transition result is malformed.",
                str(result_path),
            )
        assert payload is not None
        return _deepcopy(payload), None, None, str(result_path)

    selected = request.get("selected_admission_transition_result")
    if not _is_present(selected):
        return None, None, None, None
    if not isinstance(selected, Mapping):
        return (
            None,
            "ADMISSION_TRANSITION_RESULT_MALFORMED",
            "Selected admission / transition result is not a mapping.",
            None,
        )
    return _deepcopy(dict(selected)), None, None, None


def _extract_failed_check_count(result: Any) -> int | None:
    if not isinstance(result, Mapping):
        return None
    direct = result.get("failed_check_count")
    if isinstance(direct, int):
        return direct
    for section in (
        "distributed_operation_admission_transition_summary",
        "admission_transition_statement",
        "summary",
        "statement",
    ):
        value = _get_path(result, (section, "failed_check_count"))
        if isinstance(value, int):
            return value
    checks = result.get("admission_transition_checks")
    if isinstance(checks, Sequence) and not isinstance(checks, (str, bytes, bytearray)):
        return sum(
            1
            for check in checks
            if isinstance(check, Mapping) and check.get("passed") is not True
        )
    return None


def _extract_admission_result_id(result: Any) -> str | None:
    return _first_present(
        _get_path(
            result,
            (
                "distributed_operation_admission_transition_metadata",
                "distributed_operation_admission_transition_result_id",
            ),
        ),
        _get_path(result, ("metadata", "result_id")),
        _find_first_present(
            result,
            (
                "distributed_operation_admission_transition_result_id",
                "admission_transition_result_id",
                "result_id",
            ),
        ),
    )


def _extract_outcome(result: Any) -> str | None:
    if not isinstance(result, Mapping):
        return None
    value = result.get("outcome")
    if isinstance(value, str) and value:
        return value
    summary = _get_path(
        result,
        ("distributed_operation_admission_transition_summary", "outcome"),
    )
    if isinstance(summary, str) and summary:
        return summary
    return None


def _admission_statement(result: Any) -> Mapping[str, Any]:
    if not isinstance(result, Mapping):
        return {}
    statement = result.get("admission_transition_statement")
    return statement if isinstance(statement, Mapping) else {}


def _admission_summary(result: Any) -> Mapping[str, Any]:
    if not isinstance(result, Mapping):
        return {}
    summary = result.get("distributed_operation_admission_transition_summary")
    return summary if isinstance(summary, Mapping) else {}


def _admission_non_claims(result: Any) -> Mapping[str, Any]:
    if not isinstance(result, Mapping):
        return {}
    non_claims = result.get("non_claims")
    return non_claims if isinstance(non_claims, Mapping) else {}


def _admission_bool(result: Any, key: str) -> bool:
    statement = _admission_statement(result)
    summary = _admission_summary(result)
    non_claims = _admission_non_claims(result)
    return (
        statement.get(key) is True
        or summary.get(key) is True
        or non_claims.get(key) is True
    )


def _admission_false(result: Any, key: str) -> bool:
    statement = _admission_statement(result)
    summary = _admission_summary(result)
    non_claims = _admission_non_claims(result)
    values = [
        statement.get(key),
        summary.get(key),
        non_claims.get(key),
        result.get(key) if isinstance(result, Mapping) else None,
    ]
    if any(value is True for value in values):
        return False
    return True


def _basis(request: Mapping[str, Any]) -> Mapping[str, Any]:
    basis = request.get("execution_emission_basis")
    return basis if isinstance(basis, Mapping) else {}


def _selected_from_request_basis_admission(
    request: Mapping[str, Any],
    admission_result: Mapping[str, Any] | None,
    key: str,
    admission_paths: Sequence[Sequence[str]],
) -> Any:
    basis = _basis(request)
    value = _first_present(request.get(key), basis.get(key))
    if _is_present(value):
        return _deepcopy(value)
    if admission_result is not None:
        for path in admission_paths:
            found = _get_path(admission_result, path)
            if _is_present(found):
                return _deepcopy(found)
    return None


def _selected_operation_context(
    request: Mapping[str, Any],
    admission_result: Mapping[str, Any] | None,
) -> Any:
    basis = _basis(request)
    value = _first_present(
        request.get("selected_operation_context"),
        basis.get("selected_operation_context"),
        _get_path(admission_result, ("selected_operation_context",)),
        _get_path(admission_result, ("admission_transition_basis", "selected_operation_context")),
        _get_path(admission_result, ("admission_transition_basis", "declared_operation_context_scope")),
        _get_path(admission_result, ("admission_transition_basis", "operation_context_scope")),
        _get_path(admission_result, ("selected_operation_matter",)),
    )
    return _deepcopy(value) if _is_present(value) else None


def _selected_refusal_abort_result(
    request: Mapping[str, Any],
    admission_result: Mapping[str, Any] | None,
) -> Any:
    return _selected_from_request_basis_admission(
        request,
        admission_result,
        "selected_refusal_abort_result",
        (
            ("selected_refusal_abort_result", "selected_refusal_abort_result"),
            ("selected_operation_matter", "selected_refusal_abort_result"),
            ("admission_transition_basis", "selected_refusal_abort_result"),
        ),
    )


def _selected_sync_non_sync_result(
    request: Mapping[str, Any],
    admission_result: Mapping[str, Any] | None,
) -> Any:
    return _selected_from_request_basis_admission(
        request,
        admission_result,
        "selected_sync_non_sync_result",
        (
            ("selected_operation_matter", "selected_sync_non_sync_result"),
            ("admission_transition_basis", "selected_sync_non_sync_result"),
            (
                "selected_refusal_abort_result",
                "selected_operation_matter",
                "selected_sync_non_sync_result",
            ),
        ),
    )


def _selected_carrier_role_result(
    request: Mapping[str, Any],
    admission_result: Mapping[str, Any] | None,
) -> Any:
    return _selected_from_request_basis_admission(
        request,
        admission_result,
        "selected_carrier_role_result",
        (
            ("selected_operation_matter", "selected_carrier_role_result"),
            ("admission_transition_basis", "selected_carrier_role_result"),
            (
                "selected_refusal_abort_result",
                "selected_operation_matter",
                "selected_carrier_role_result",
            ),
        ),
    )


def _selected_source_body_authority_result(
    request: Mapping[str, Any],
    admission_result: Mapping[str, Any] | None,
) -> Any:
    return _selected_from_request_basis_admission(
        request,
        admission_result,
        "selected_source_body_authority_result",
        (
            ("selected_operation_matter", "selected_source_body_authority_result"),
            ("admission_transition_basis", "selected_source_body_authority_result"),
            (
                "selected_refusal_abort_result",
                "selected_operation_matter",
                "selected_source_body_authority_result",
            ),
        ),
    )


def _selected_eligibility_result(
    request: Mapping[str, Any],
    admission_result: Mapping[str, Any] | None,
) -> Any:
    return _selected_from_request_basis_admission(
        request,
        admission_result,
        "selected_eligibility_result",
        (
            ("selected_operation_matter", "selected_eligibility_result"),
            ("admission_transition_basis", "selected_eligibility_result"),
            (
                "selected_refusal_abort_result",
                "selected_operation_matter",
                "selected_eligibility_result",
            ),
        ),
    )


def _selected_matter_declaration(
    request: Mapping[str, Any],
    admission_result: Mapping[str, Any] | None,
) -> Any:
    return _selected_from_request_basis_admission(
        request,
        admission_result,
        "selected_matter_declaration",
        (
            ("selected_operation_matter", "selected_matter_declaration"),
            ("admission_transition_basis", "selected_matter_declaration"),
            (
                "selected_refusal_abort_result",
                "selected_operation_matter",
                "selected_matter_declaration",
            ),
        ),
    )


def _selected_operation_candidate(
    request: Mapping[str, Any],
    admission_result: Mapping[str, Any] | None,
) -> Any:
    return _selected_from_request_basis_admission(
        request,
        admission_result,
        "selected_operation_candidate",
        (
            ("selected_operation_matter", "selected_operation_candidate"),
            ("admission_transition_basis", "selected_operation_candidate"),
            (
                "selected_refusal_abort_result",
                "selected_operation_matter",
                "selected_operation_candidate",
            ),
        ),
    )


def _selected_operation_matter(
    request: Mapping[str, Any],
    admission_result: Mapping[str, Any] | None,
) -> Any:
    return _selected_from_request_basis_admission(
        request,
        admission_result,
        "selected_operation_matter",
        (
            ("selected_operation_matter", "selected_operation_matter"),
            ("admission_transition_basis", "selected_operation_matter"),
            (
                "selected_refusal_abort_result",
                "selected_operation_matter",
                "selected_operation_matter",
            ),
        ),
    )


def _operation_candidate_id(candidate: Any) -> str | None:
    if isinstance(candidate, Mapping):
        return _first_present(
            candidate.get("operation_candidate_id"),
            candidate.get("selected_operation_candidate_id"),
            candidate.get("candidate_id"),
            candidate.get("id"),
        )
    if isinstance(candidate, str):
        return candidate
    return None


def _operation_matter_id(matter: Any) -> str | None:
    if isinstance(matter, Mapping):
        return _first_present(
            matter.get("operation_matter_id"),
            matter.get("selected_operation_matter_id"),
            matter.get("matter_id"),
            matter.get("id"),
        )
    if isinstance(matter, str):
        return matter
    return None


def _normalize_scope(scope: Any) -> tuple[list[str], dict[str, Any], list[str]]:
    if isinstance(scope, Mapping):
        values = scope.get("selected_execution_emission_scope")
        if values is None:
            values = scope.get("execution_emission_scope")
        if values is None:
            values = scope.get("scope")
        if values is None:
            values = [
                key
                for key, selected in scope.items()
                if isinstance(key, str) and selected is True
            ]
    else:
        values = scope

    if isinstance(values, str):
        selected = [values]
    elif isinstance(values, Sequence) and not isinstance(
        values, (str, bytes, bytearray)
    ):
        selected = [str(value) for value in values]
    else:
        selected = []

    unsupported = [
        value for value in selected if value not in SUPPORTED_EXECUTION_EMISSION_SCOPE
    ]
    selected_set = set(selected)
    flags = {
        "selected_execution_emission_scope": selected,
        "supported_execution_emission_scope": list(SUPPORTED_EXECUTION_EMISSION_SCOPE),
        "unsupported_execution_emission_scope": unsupported,
        "all_selected_execution_emission_scope_supported": not unsupported,
        "one_admitted_operation_context_only": (
            "ONE_ADMITTED_OPERATION_CONTEXT_ONLY" in selected_set
        ),
        "no_execution_performed_by_boundary": (
            "NO_EXECUTION_PERFORMED_BY_BOUNDARY" in selected_set
        ),
        "no_output_emitted_by_boundary": (
            "NO_OUTPUT_EMITTED_BY_BOUNDARY" in selected_set
        ),
        "no_action_authorized_by_boundary": (
            "NO_ACTION_AUTHORIZED_BY_BOUNDARY" in selected_set
        ),
        "no_consequence_created_by_boundary": (
            "NO_CONSEQUENCE_CREATED_BY_BOUNDARY" in selected_set
        ),
        "no_repository_sync_by_boundary": (
            "NO_REPOSITORY_SYNC_BY_BOUNDARY" in selected_set
        ),
        "no_non_synchronized_operation_by_boundary": (
            "NO_NON_SYNCHRONIZED_OPERATION_BY_BOUNDARY" in selected_set
        ),
        "no_full_body_transfer_by_boundary": (
            "NO_FULL_BODY_TRANSFER_BY_BOUNDARY" in selected_set
        ),
        "no_second_body_by_boundary": "NO_SECOND_BODY_BY_BOUNDARY" in selected_set,
        "refusal_abort_conditions_remain_active": (
            "REFUSAL_ABORT_CONDITIONS_REMAIN_ACTIVE" in selected_set
        ),
        "receipt_exhaustion_required_before_closure": (
            "RECEIPT_EXHAUSTION_REQUIRED_BEFORE_CLOSURE" in selected_set
        ),
        "action_consequence_requires_separate_boundary": (
            "ACTION_CONSEQUENCE_REQUIRES_SEPARATE_BOUNDARY" in selected_set
        ),
        "no_reusable_permission": True,
        "no_autonomous_continuation": True,
    }
    return selected, flags, unsupported


def _declared_non_claims(request: Mapping[str, Any]) -> Mapping[str, Any]:
    non_claims = request.get("declared_non_claims")
    return non_claims if isinstance(non_claims, Mapping) else {}


def _declared_non_claims_valid(request: Mapping[str, Any]) -> bool:
    non_claims = _declared_non_claims(request)
    if not non_claims:
        return False
    for key in REQUIRED_NON_CLAIMS:
        if key not in non_claims or non_claims.get(key) is not False:
            return False
    status = non_claims.get("execution_emission_boundary_recorded")
    requested = request.get("requested_execution_emission_outcome", OUTCOME_RECORDED)
    if status is True and requested != OUTCOME_RECORDED:
        return False
    return True


def _collapse_code(request: Mapping[str, Any]) -> str | None:
    candidates: list[Mapping[str, Any]] = [request]
    basis = _basis(request)
    if basis:
        candidates.append(basis)
    non_claims = _declared_non_claims(request)
    if non_claims:
        candidates.append(non_claims)
    scope = request.get("execution_emission_scope")
    if isinstance(scope, Mapping):
        candidates.append(scope)

    for code, fields in COLLAPSE_FIELDS.items():
        for candidate in candidates:
            if _contains_true(candidate, fields):
                return code
    return None


def _admission_result_collapse_code(admission_result: Mapping[str, Any] | None) -> str | None:
    if not isinstance(admission_result, Mapping):
        return None
    statement = _admission_statement(admission_result)
    summary = _admission_summary(admission_result)
    non_claims = _admission_non_claims(admission_result)
    candidates = [admission_result, statement, summary, non_claims]
    for code, fields in COLLAPSE_FIELDS.items():
        if code == "MUTATION_REPLAY_OR_MERGE_DETECTED":
            continue
        for candidate in candidates:
            if _contains_true(candidate, fields):
                return code
    return None


def _check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str | None = None,
) -> dict[str, Any]:
    record = {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": expected_posture,
        "actual_posture": actual_posture,
    }
    if passed:
        record["block_code"] = None
        record["failure_code"] = None
    else:
        record["block_code"] = code
        record["failure_code"] = code
    return record


def _checks_by_name(checks: Sequence[Mapping[str, Any]]) -> dict[str, Mapping[str, Any]]:
    return {
        str(check.get("check_name")): check
        for check in checks
        if isinstance(check, Mapping)
    }


def _first_failed_code(checks: Sequence[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if isinstance(check, Mapping) and check.get("passed") is not True:
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str) and code:
                return code
    return None


def _block_reason(code: str | None, explicit: Any = None) -> str | None:
    if explicit:
        return str(explicit)
    if code is None:
        return None
    return BLOCK_REASON_BY_CODE.get(code, code.replace("_", " ").lower())


def _default_non_claims(outcome: str) -> dict[str, bool]:
    non_claims = {key: False for key in REQUIRED_NON_CLAIMS}
    non_claims["execution_emission_boundary_recorded"] = outcome == OUTCOME_RECORDED
    return non_claims


def _non_meaning() -> dict[str, bool]:
    meanings = {
        "operation_executed": True,
        "output_emitted": True,
        "action_authorized": True,
        "consequence_created": True,
        "repository_synchronization_authorized": True,
        "non_synchronized_operation_authorized": True,
        "shared_live_state_created": True,
        "state_merge_authorized": True,
        "replay_authorized": True,
        "full_body_transfer_authorized": True,
        "second_body_created": True,
        "live_refusal_executed": True,
        "live_abort_executed": True,
        "carrier_roles_activated_beyond_admitted_context_scope": True,
        "carrier_authority_created": True,
        "carrier_currentness_created": True,
        "current_carrier_selected": True,
        "winning_carrier_selected": True,
        "losing_carrier_invalidated": True,
        "source_replaced": True,
        "authority_newly_created": True,
        "reusable_permission_created": True,
        "autonomous_continuation_authorized": True,
        "divergence_resolved": True,
        "evidence_erased": True,
        "refusal_erased": True,
        "blocked_attempt_erased": True,
        "projection_mismatch_hidden": True,
        "public_readiness_created": True,
        "final_completion_claimed": True,
        "follow_on_work_authorized": True,
    }
    meanings.update({f"does_not_mean_{key}": value for key, value in meanings.items()})
    return meanings


def _what_remains_open() -> dict[str, bool]:
    return {
        "distributed_action_consequence_boundary": True,
        "distributed_operation_receipt_exhaustion": True,
        "distributed_operation_conformance": True,
        "distributed_operation_closure": True,
        "distributed_operation_itself": True,
        "repository_synchronization": True,
        "non_synchronized_operation": True,
        "full_body_transfer": True,
        "second_body_creation": True,
        "carrier_role_activation_beyond_admission_scope": True,
        "current_self_orientation_v10": True,
        "public_launch_readiness": True,
        "final_governance": True,
        "final_continuity_completion": True,
        "final_system_identity": True,
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }


def _additional_basis_required(
    request: Mapping[str, Any],
    outcome: str,
) -> dict[str, Any]:
    context = _deepcopy(request.get("additional_basis_context", {}))
    if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        return {
            "additional_basis_required": True,
            "additional_basis_context": context,
            "additional_basis_reason": _first_present(
                request.get("additional_basis_reason"),
                request.get("block_reason"),
                "Additional execution / emission basis is required.",
            ),
            "missing_basis_not_scheduled": True,
            "missing_basis_not_authorized": True,
            "missing_basis_not_executed": True,
        }
    return {
        "additional_basis_required": False,
        "additional_basis_context": context if context else {},
        "additional_basis_not_scheduled": True,
        "additional_basis_not_authorized": True,
        "additional_basis_not_executed": True,
    }


def _build_declared_question_section(
    request: Mapping[str, Any],
    selected_admission_result: Mapping[str, Any] | None,
    selected_admission_path: str | None,
) -> dict[str, Any]:
    return {
        "execution_emission_request_id": request.get("execution_emission_request_id"),
        "execution_emission_request_path": request.get("execution_emission_request_path"),
        "execution_emission_question": request.get("execution_emission_question"),
        "execution_emission_intent": request.get("execution_emission_intent"),
        "requested_execution_emission_outcome": request.get(
            "requested_execution_emission_outcome", OUTCOME_RECORDED
        ),
        "selected_admission_transition_result_id": _first_present(
            request.get("selected_admission_transition_result_id"),
            _extract_admission_result_id(selected_admission_result),
        ),
        "selected_admission_transition_result_outcome": _first_present(
            request.get("selected_admission_transition_result_outcome"),
            _extract_outcome(selected_admission_result),
        ),
        "selected_admission_transition_result_path": selected_admission_path,
        "admission_transition_is_not_execution": True,
        "execution_emission_boundary_is_not_execution": True,
        "execution_emission_boundary_is_not_emission": True,
        "execution_emission_boundary_is_not_action": True,
        "execution_emission_boundary_is_not_consequence": True,
        "execution_emission_boundary_is_not_synchronization": True,
        "execution_emission_boundary_is_not_full_body_transfer": True,
        "execution_emission_boundary_is_not_second_body_creation": True,
        "execution_emission_boundary_is_not_reusable_permission": True,
        "execution_emission_boundary_is_not_autonomous_continuation": True,
    }


def _build_selected_admission_section(
    request: Mapping[str, Any],
    selected_admission_result: Mapping[str, Any] | None,
    selected_admission_path: str | None,
    selected_operation_context: Any,
) -> dict[str, Any]:
    outcome = _extract_outcome(selected_admission_result)
    failed_count = _extract_failed_check_count(selected_admission_result)
    admission_collapse = _admission_result_collapse_code(selected_admission_result)
    upstream_overcommit_codes = {
        "EXECUTION_EMISSION_REVIEW_AUTHORIZES_SYNCHRONIZATION",
        "EXECUTION_EMISSION_REVIEW_AUTHORIZES_NON_SYNCHRONIZED_OPERATION",
        "EXECUTION_EMISSION_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER",
        "EXECUTION_EMISSION_REVIEW_CREATES_SECOND_BODY",
        "EXECUTION_EMISSION_REVIEW_CREATES_REUSABLE_PERMISSION",
        "EXECUTION_EMISSION_REVIEW_AUTHORIZES_AUTONOMOUS_CONTINUATION",
        "EXECUTION_EMISSION_REVIEW_CREATES_PUBLIC_READINESS",
        "EXECUTION_EMISSION_REVIEW_CLAIMS_FINAL_COMPLETION",
        "EXECUTION_EMISSION_REVIEW_SCHEDULES_FOLLOW_ON_WORK",
    }
    return {
        "selected_admission_transition_result": _deepcopy(selected_admission_result),
        "selected_admission_transition_result_id": _first_present(
            request.get("selected_admission_transition_result_id"),
            _extract_admission_result_id(selected_admission_result),
        ),
        "selected_admission_transition_result_path": selected_admission_path,
        "selected_admission_transition_result_outcome": _first_present(
            request.get("selected_admission_transition_result_outcome"),
            outcome,
        ),
        "expected_selected_admission_transition_outcome": _first_present(
            request.get("expected_selected_admission_transition_outcome"),
            EXPECTED_SELECTED_ADMISSION_TRANSITION_OUTCOME,
        ),
        "selected_admission_transition_result_outcome_is_recorded": (
            outcome == EXPECTED_SELECTED_ADMISSION_TRANSITION_OUTCOME
        ),
        "selected_admission_transition_result_failed_check_count": failed_count,
        "selected_admission_transition_result_failed_check_count_zero": (
            failed_count == 0
        ),
        "selected_admission_transition_result_remains_boundary_posture_only": True,
        "selected_admitted_operation_context_preserved": _is_present(
            selected_operation_context
        ),
        "operation_admitted": _admission_bool(
            selected_admission_result, "operation_admitted"
        ),
        "one_bounded_operation_context_admitted": _admission_bool(
            selected_admission_result, "one_bounded_operation_context_admitted"
        ),
        "selected_admission_transition_result_did_not_execute_operation": (
            _admission_false(selected_admission_result, "operation_executed")
            and admission_collapse
            != "EXECUTION_EMISSION_REVIEW_EXECUTES_OPERATION"
        ),
        "selected_admission_transition_result_did_not_emit_output": (
            _admission_false(selected_admission_result, "output_emitted")
            and admission_collapse != "EXECUTION_EMISSION_REVIEW_EMITS_OUTPUT"
        ),
        "selected_admission_transition_result_did_not_authorize_action": (
            _admission_false(selected_admission_result, "action_authorized")
            and admission_collapse
            != "EXECUTION_EMISSION_REVIEW_AUTHORIZES_ACTION"
        ),
        "selected_admission_transition_result_did_not_create_consequence": (
            _admission_false(selected_admission_result, "consequence_created")
            and admission_collapse
            != "EXECUTION_EMISSION_REVIEW_CREATES_CONSEQUENCE"
        ),
        "selected_admission_transition_result_did_not_authorize_sync_non_sync_transfer_second_body_reusable_permission_autonomous_continuation_public_readiness_final_completion_follow_on_work": (
            admission_collapse not in upstream_overcommit_codes
        ),
    }


def _build_selected_operation_context_section(
    request: Mapping[str, Any],
    selected_admission_result: Mapping[str, Any] | None,
    selected_operation_context: Any,
    selected_refusal_abort_result: Any,
    selected_sync_non_sync_result: Any,
    selected_carrier_role_result: Any,
    selected_source_body_authority_result: Any,
    selected_eligibility_result: Any,
    selected_matter_declaration: Any,
    selected_operation_candidate: Any,
    selected_operation_matter: Any,
) -> dict[str, Any]:
    return {
        "selected_admission_transition_result": _deepcopy(selected_admission_result),
        "admitted_operation_context": _deepcopy(selected_operation_context),
        "selected_refusal_abort_result": _deepcopy(selected_refusal_abort_result),
        "selected_sync_non_sync_result": _deepcopy(selected_sync_non_sync_result),
        "selected_carrier_role_result": _deepcopy(selected_carrier_role_result),
        "selected_source_body_authority_result": _deepcopy(
            selected_source_body_authority_result
        ),
        "selected_eligibility_result": _deepcopy(selected_eligibility_result),
        "selected_matter_declaration": _deepcopy(selected_matter_declaration),
        "selected_operation_candidate": _deepcopy(selected_operation_candidate),
        "selected_operation_matter": _deepcopy(selected_operation_matter),
        "selected_operation_candidate_id": _operation_candidate_id(
            selected_operation_candidate
        ),
        "selected_operation_matter_id": _operation_matter_id(selected_operation_matter),
        "operation_admitted": _admission_bool(
            selected_admission_result, "operation_admitted"
        ),
        "one_bounded_operation_context_admitted": _admission_bool(
            selected_admission_result, "one_bounded_operation_context_admitted"
        ),
        "refusal_abort_carry_forward_preserved": True,
        "no_operation_executed_emitted_acted_or_made_consequential": True,
    }


def _basis_value(
    request: Mapping[str, Any],
    admission_result: Mapping[str, Any] | None,
    key: str,
) -> Any:
    basis = _basis(request)
    return _first_present(
        request.get(key),
        basis.get(key),
        _get_path(admission_result, ("admission_transition_basis", key)),
    )


def _build_execution_emission_basis_section(
    request: Mapping[str, Any],
    selected_admission_result: Mapping[str, Any] | None,
    selected_operation_context: Any,
    selected_refusal_abort_result: Any,
    selected_sync_non_sync_result: Any,
    selected_carrier_role_result: Any,
    selected_source_body_authority_result: Any,
    selected_eligibility_result: Any,
    selected_matter_declaration: Any,
    selected_operation_candidate: Any,
    selected_operation_matter: Any,
    scope_values: list[str],
) -> dict[str, Any]:
    return {
        "selected_admission_transition_result": _deepcopy(selected_admission_result),
        "selected_admitted_operation_context": _deepcopy(selected_operation_context),
        "selected_refusal_abort_result": _deepcopy(selected_refusal_abort_result),
        "selected_sync_non_sync_result": _deepcopy(selected_sync_non_sync_result),
        "selected_carrier_role_result": _deepcopy(selected_carrier_role_result),
        "selected_source_body_authority_result": _deepcopy(
            selected_source_body_authority_result
        ),
        "selected_eligibility_result": _deepcopy(selected_eligibility_result),
        "selected_matter_declaration": _deepcopy(selected_matter_declaration),
        "selected_operation_candidate": _deepcopy(selected_operation_candidate),
        "selected_operation_matter": _deepcopy(selected_operation_matter),
        "source_body_authority_basis": _deepcopy(
            _basis_value(request, selected_admission_result, "source_body_authority_basis")
        ),
        "carrier_role_basis": _deepcopy(
            _basis_value(request, selected_admission_result, "carrier_role_basis")
        ),
        "sync_non_sync_posture_basis": _deepcopy(
            _basis_value(request, selected_admission_result, "sync_non_sync_posture_basis")
        ),
        "refusal_abort_posture_basis": _deepcopy(
            _basis_value(request, selected_admission_result, "refusal_abort_posture_basis")
        ),
        "refusal_abort_conditions_carry_forward": True,
        "declared_execution_emission_scope": scope_values,
        "proposed_execution_candidate": _deepcopy(
            request.get("proposed_execution_candidate")
            or _basis(request).get("proposed_execution_candidate")
        ),
        "proposed_emission_candidate": _deepcopy(
            request.get("proposed_emission_candidate")
            or _basis(request).get("proposed_emission_candidate")
        ),
        "proposed_output_family": _deepcopy(
            request.get("proposed_output_family")
            or _basis(request).get("proposed_output_family")
        ),
        "receipt_exhaustion_requirement": _deepcopy(
            request.get("receipt_exhaustion_requirement")
            or _basis(request).get("receipt_exhaustion_requirement")
        ),
        "action_consequence_separation_requirement": _deepcopy(
            request.get("action_consequence_separation_requirement")
            or _basis(request).get("action_consequence_separation_requirement")
        ),
        "carrier_evidence_remains_unmerged": True,
        "carrier_context_remains_context_only": True,
        "divergence_remains_visible": True,
        "refusal_remains_visible": True,
        "blocked_attempts_remain_visible": True,
        "projection_mismatch_remains_visible": True,
        "execution_emission_basis_is_not_execution": True,
        "execution_emission_basis_is_not_emission": True,
        "execution_emission_basis_is_not_action": True,
        "execution_emission_basis_is_not_consequence": True,
        "execution_emission_basis_is_not_synchronization": True,
        "execution_emission_basis_is_not_full_body_transfer": True,
        "execution_emission_basis_is_not_second_body": True,
        "execution_emission_basis_is_not_reusable_permission": True,
        "execution_emission_basis_is_not_autonomous_continuation": True,
    }


def _build_checks(
    request: Mapping[str, Any],
    selected_admission_result: Mapping[str, Any] | None,
    selected_operation_context: Any,
    selected_refusal_abort_result: Any,
    selected_sync_non_sync_result: Any,
    selected_carrier_role_result: Any,
    selected_source_body_authority_result: Any,
    selected_eligibility_result: Any,
    selected_matter_declaration: Any,
    selected_operation_candidate: Any,
    selected_operation_matter: Any,
    scope_flags: Mapping[str, Any],
    unsupported_scope: Sequence[str],
) -> list[dict[str, Any]]:
    intent = request.get("execution_emission_intent")
    admission_outcome = _extract_outcome(selected_admission_result)
    failed_count = _extract_failed_check_count(selected_admission_result)
    proposed_execution_candidate = _first_present(
        request.get("proposed_execution_candidate"),
        _basis(request).get("proposed_execution_candidate"),
    )
    proposed_emission_candidate = _first_present(
        request.get("proposed_emission_candidate"),
        _basis(request).get("proposed_emission_candidate"),
    )
    proposed_output_family = _first_present(
        request.get("proposed_output_family"),
        _basis(request).get("proposed_output_family"),
    )
    receipt_requirement = _first_present(
        request.get("receipt_exhaustion_requirement"),
        _basis(request).get("receipt_exhaustion_requirement"),
    )
    action_consequence_requirement = _first_present(
        request.get("action_consequence_separation_requirement"),
        _basis(request).get("action_consequence_separation_requirement"),
    )
    collapse = _collapse_code(request)
    admission_collapse = _admission_result_collapse_code(selected_admission_result)
    sync_transfer_codes = {
        "EXECUTION_EMISSION_REVIEW_AUTHORIZES_SYNCHRONIZATION",
        "EXECUTION_EMISSION_REVIEW_AUTHORIZES_NON_SYNCHRONIZED_OPERATION",
        "EXECUTION_EMISSION_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER",
        "EXECUTION_EMISSION_REVIEW_CREATES_SECOND_BODY",
    }
    public_final_follow_on_codes = {
        "EXECUTION_EMISSION_REVIEW_CREATES_PUBLIC_READINESS",
        "EXECUTION_EMISSION_REVIEW_CLAIMS_FINAL_COMPLETION",
        "EXECUTION_EMISSION_REVIEW_SCHEDULES_FOLLOW_ON_WORK",
    }
    carrier_refusal_erasure_codes = {
        "EXECUTION_EMISSION_REVIEW_ACTIVATES_CARRIER_ROLES_BEYOND_SCOPE",
        "EXECUTION_EMISSION_REVIEW_CREATES_CARRIER_AUTHORITY",
        "EXECUTION_EMISSION_REVIEW_CREATES_CARRIER_CURRENTNESS",
        "EXECUTION_EMISSION_REVIEW_SELECTS_CURRENT_CARRIER",
        "EXECUTION_EMISSION_REVIEW_SELECTS_WINNING_CARRIER",
        "EXECUTION_EMISSION_REVIEW_INVALIDATES_LOSING_CARRIER",
        "EXECUTION_EMISSION_REVIEW_REPLACES_SOURCE",
        "EXECUTION_EMISSION_REVIEW_ERASES_REFUSAL_ABORT",
        "EXECUTION_EMISSION_REVIEW_ERASES_EVIDENCE_OR_REFUSAL",
        "EXECUTION_EMISSION_REVIEW_RESOLVES_DIVERGENCE",
    }
    sync_transfer_collapse = (
        collapse
        if collapse in sync_transfer_codes
        else admission_collapse
        if admission_collapse in sync_transfer_codes
        else None
    )
    public_final_follow_on_collapse = (
        collapse
        if collapse in public_final_follow_on_codes
        else admission_collapse
        if admission_collapse in public_final_follow_on_codes
        else None
    )
    carrier_refusal_erasure_collapse = (
        collapse
        if collapse in carrier_refusal_erasure_codes
        else admission_collapse
        if admission_collapse in carrier_refusal_erasure_codes
        else None
    )

    checks = [
        _check(
            "execution_emission_question_declared",
            _is_present(request.get("execution_emission_question")),
            "declared execution / emission question",
            request.get("execution_emission_question"),
            "EXECUTION_EMISSION_QUESTION_UNDECLARED",
        ),
        _check(
            "execution_emission_intent_supported",
            intent in SUPPORTED_INTENTS,
            sorted(SUPPORTED_INTENTS),
            intent,
            "EXECUTION_EMISSION_INTENT_UNSUPPORTED",
        ),
        _check(
            "selected_admission_transition_result_present",
            isinstance(selected_admission_result, Mapping),
            "selected admission / transition result present",
            type(selected_admission_result).__name__,
            "ADMISSION_TRANSITION_RESULT_MISSING",
        ),
        _check(
            "selected_admission_transition_result_outcome_declared",
            _is_present(admission_outcome),
            "admission / transition outcome declared",
            admission_outcome,
            "ADMISSION_TRANSITION_RESULT_OUTCOME_MISSING",
        ),
        _check(
            "selected_admission_transition_result_outcome_recorded",
            admission_outcome == EXPECTED_SELECTED_ADMISSION_TRANSITION_OUTCOME,
            EXPECTED_SELECTED_ADMISSION_TRANSITION_OUTCOME,
            admission_outcome,
            "ADMISSION_TRANSITION_RESULT_NOT_RECORDED",
        ),
        _check(
            "selected_admission_transition_result_failed_check_count_zero",
            failed_count == 0,
            0,
            failed_count,
            "ADMISSION_TRANSITION_RESULT_HAS_FAILED_CHECKS",
        ),
        _check(
            "admitted_operation_context_preserved",
            _is_present(selected_operation_context),
            "admitted operation context preserved",
            selected_operation_context,
            "ADMITTED_OPERATION_CONTEXT_MISSING",
        ),
        _check(
            "operation_admitted_true",
            _admission_bool(selected_admission_result, "operation_admitted"),
            True,
            _admission_bool(selected_admission_result, "operation_admitted"),
            "OPERATION_NOT_ADMITTED",
        ),
        _check(
            "one_bounded_operation_context_admitted_true",
            _admission_bool(
                selected_admission_result, "one_bounded_operation_context_admitted"
            ),
            True,
            _admission_bool(
                selected_admission_result, "one_bounded_operation_context_admitted"
            ),
            "ONE_BOUNDED_OPERATION_CONTEXT_NOT_ADMITTED",
        ),
        _check(
            "selected_refusal_abort_result_preserved",
            _is_present(selected_refusal_abort_result),
            "selected refusal / abort result preserved",
            selected_refusal_abort_result,
            "REFUSAL_ABORT_RESULT_MISSING",
        ),
        _check(
            "selected_sync_non_sync_result_preserved",
            _is_present(selected_sync_non_sync_result),
            "selected sync/non-sync result preserved",
            selected_sync_non_sync_result,
            "SYNC_NON_SYNC_RESULT_MISSING",
        ),
        _check(
            "selected_carrier_role_result_preserved",
            _is_present(selected_carrier_role_result),
            "selected carrier role result preserved",
            selected_carrier_role_result,
            "CARRIER_ROLE_RESULT_MISSING",
        ),
        _check(
            "selected_source_body_authority_result_preserved",
            _is_present(selected_source_body_authority_result),
            "selected source-body authority result preserved",
            selected_source_body_authority_result,
            "SOURCE_BODY_AUTHORITY_RESULT_MISSING",
        ),
        _check(
            "selected_eligibility_result_preserved",
            _is_present(selected_eligibility_result),
            "selected eligibility result preserved",
            selected_eligibility_result,
            "SELECTED_ELIGIBILITY_RESULT_MISSING",
        ),
        _check(
            "selected_matter_declaration_preserved",
            _is_present(selected_matter_declaration),
            "selected matter declaration preserved",
            selected_matter_declaration,
            "SELECTED_MATTER_DECLARATION_MISSING",
        ),
        _check(
            "selected_operation_candidate_preserved",
            _is_present(selected_operation_candidate),
            "selected operation candidate preserved",
            selected_operation_candidate,
            "SELECTED_OPERATION_CANDIDATE_MISSING",
        ),
        _check(
            "selected_operation_matter_preserved",
            _is_present(selected_operation_matter),
            "selected operation matter preserved",
            selected_operation_matter,
            "SELECTED_OPERATION_MATTER_MISSING",
        ),
        _check(
            "refusal_abort_conditions_carry_forward",
            True,
            True,
            True,
            None,
        ),
        _check("sync_non_sync_postures_preserved", True, True, True, None),
        _check("carrier_evidence_remains_unmerged", True, True, True, None),
        _check("carrier_context_remains_context_only", True, True, True, None),
        _check("divergence_remains_visible", True, True, True, None),
        _check("refusal_remains_visible", True, True, True, None),
        _check("blocked_attempts_remain_visible", True, True, True, None),
        _check("projection_mismatch_remains_visible", True, True, True, None),
        _check(
            "execution_emission_scope_declared",
            _is_present(scope_flags.get("selected_execution_emission_scope")),
            "declared execution / emission scope",
            scope_flags.get("selected_execution_emission_scope"),
            "EXECUTION_EMISSION_SCOPE_MISSING",
        ),
        _check(
            "execution_emission_scope_supported",
            not unsupported_scope,
            "supported execution / emission scope values only",
            list(unsupported_scope),
            "UNSUPPORTED_EXECUTION_EMISSION_SCOPE",
        ),
        _check(
            "execution_emission_scope_one_admitted_operation_context_only",
            scope_flags.get("one_admitted_operation_context_only") is True,
            True,
            scope_flags.get("one_admitted_operation_context_only"),
            "EXECUTION_EMISSION_SCOPE_MISSING",
        ),
        _check(
            "proposed_execution_candidate_present",
            _is_present(proposed_execution_candidate),
            "proposed execution candidate present",
            proposed_execution_candidate,
            "PROPOSED_EXECUTION_CANDIDATE_MISSING",
        ),
        _check(
            "proposed_emission_candidate_present",
            _is_present(proposed_emission_candidate),
            "proposed emission candidate present",
            proposed_emission_candidate,
            "PROPOSED_EMISSION_CANDIDATE_MISSING",
        ),
        _check(
            "proposed_output_family_named_but_not_emitted",
            _is_present(proposed_output_family),
            "proposed output family named but not emitted",
            proposed_output_family,
            "PROPOSED_OUTPUT_FAMILY_MISSING",
        ),
        _check(
            "receipt_exhaustion_requirement_present",
            _is_present(receipt_requirement),
            "receipt / exhaustion requirement present",
            receipt_requirement,
            "RECEIPT_EXHAUSTION_REQUIREMENT_MISSING",
        ),
        _check(
            "action_consequence_separation_present",
            _is_present(action_consequence_requirement),
            "action / consequence separation present",
            action_consequence_requirement,
            "ACTION_CONSEQUENCE_SEPARATION_REQUIREMENT_MISSING",
        ),
        _check(
            "no_operation_executed",
            collapse != "EXECUTION_EMISSION_REVIEW_EXECUTES_OPERATION"
            and admission_collapse != "EXECUTION_EMISSION_REVIEW_EXECUTES_OPERATION",
            False,
            collapse,
            "EXECUTION_EMISSION_REVIEW_EXECUTES_OPERATION",
        ),
        _check(
            "no_output_emitted",
            collapse != "EXECUTION_EMISSION_REVIEW_EMITS_OUTPUT"
            and admission_collapse != "EXECUTION_EMISSION_REVIEW_EMITS_OUTPUT",
            False,
            collapse,
            "EXECUTION_EMISSION_REVIEW_EMITS_OUTPUT",
        ),
        _check(
            "no_action_authorized",
            collapse != "EXECUTION_EMISSION_REVIEW_AUTHORIZES_ACTION"
            and admission_collapse != "EXECUTION_EMISSION_REVIEW_AUTHORIZES_ACTION",
            False,
            collapse,
            "EXECUTION_EMISSION_REVIEW_AUTHORIZES_ACTION",
        ),
        _check(
            "no_consequence_created",
            collapse != "EXECUTION_EMISSION_REVIEW_CREATES_CONSEQUENCE"
            and admission_collapse != "EXECUTION_EMISSION_REVIEW_CREATES_CONSEQUENCE",
            False,
            collapse,
            "EXECUTION_EMISSION_REVIEW_CREATES_CONSEQUENCE",
        ),
        _check(
            "no_sync_shared_live_state_merge_replay_full_body_transfer_second_body_non_sync_operation_carrier_autonomy_stale_carrier_operation",
            sync_transfer_collapse is None,
            "no sync/shared live state/merge/replay/full body transfer/second body/non-sync operation/carrier autonomy/stale carrier operation",
            sync_transfer_collapse,
            sync_transfer_collapse,
        ),
        _check(
            "no_reusable_permission_created",
            collapse != "EXECUTION_EMISSION_REVIEW_CREATES_REUSABLE_PERMISSION"
            and admission_collapse
            != "EXECUTION_EMISSION_REVIEW_CREATES_REUSABLE_PERMISSION",
            False,
            collapse or admission_collapse,
            "EXECUTION_EMISSION_REVIEW_CREATES_REUSABLE_PERMISSION",
        ),
        _check(
            "no_autonomous_continuation_authorized",
            collapse
            != "EXECUTION_EMISSION_REVIEW_AUTHORIZES_AUTONOMOUS_CONTINUATION"
            and admission_collapse
            != "EXECUTION_EMISSION_REVIEW_AUTHORIZES_AUTONOMOUS_CONTINUATION",
            False,
            collapse or admission_collapse,
            "EXECUTION_EMISSION_REVIEW_AUTHORIZES_AUTONOMOUS_CONTINUATION",
        ),
        _check(
            "no_public_readiness_final_completion_follow_on_work",
            public_final_follow_on_collapse is None,
            "no public readiness/final completion/follow-on work",
            public_final_follow_on_collapse,
            public_final_follow_on_collapse,
        ),
        _check(
            "no_carrier_authority_currentness_selection_replacement_or_refusal_erasure",
            carrier_refusal_erasure_collapse is None,
            "no carrier authority/currentness/selection/source replacement/refusal erasure/divergence resolution",
            carrier_refusal_erasure_collapse,
            carrier_refusal_erasure_collapse,
        ),
        _check(
            "no_mutation_replay_merge",
            collapse != "MUTATION_REPLAY_OR_MERGE_DETECTED"
            and admission_collapse != "MUTATION_REPLAY_OR_MERGE_DETECTED",
            "no mutation/replay/merge",
            collapse or admission_collapse,
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        ),
        _check(
            "non_claims_remain_false",
            _declared_non_claims_valid(request),
            "all required execution / emission non-claims present and false",
            _declared_non_claims(request),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
    ]
    return checks


def _statement(
    outcome: str,
    request: Mapping[str, Any],
    selected_admission_result: Mapping[str, Any] | None,
    checks: Sequence[Mapping[str, Any]],
    block_code: str | None,
) -> dict[str, Any]:
    passed_count = sum(1 for check in checks if check.get("passed") is True)
    failed_count = sum(1 for check in checks if check.get("passed") is not True)
    by_name = _checks_by_name(checks)

    def passed(name: str) -> bool:
        return by_name.get(name, {}).get("passed") is True

    recorded = outcome == OUTCOME_RECORDED
    statement = {
        "distributed_execution_emission_boundary_recorded": recorded,
        "not_ready": outcome == OUTCOME_NOT_READY,
        "requires_additional_basis": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "selected_admission_transition_result_preserved": passed(
            "selected_admission_transition_result_present"
        ),
        "selected_admission_transition_result_recorded": passed(
            "selected_admission_transition_result_outcome_recorded"
        ),
        "selected_admission_transition_result_failed_check_count_zero": passed(
            "selected_admission_transition_result_failed_check_count_zero"
        ),
        "admitted_operation_context_preserved": passed(
            "admitted_operation_context_preserved"
        ),
        "operation_admitted": _admission_bool(
            selected_admission_result, "operation_admitted"
        ),
        "one_bounded_operation_context_admitted": _admission_bool(
            selected_admission_result, "one_bounded_operation_context_admitted"
        ),
        "selected_refusal_abort_result_preserved": passed(
            "selected_refusal_abort_result_preserved"
        ),
        "selected_sync_non_sync_result_preserved": passed(
            "selected_sync_non_sync_result_preserved"
        ),
        "selected_carrier_role_result_preserved": passed(
            "selected_carrier_role_result_preserved"
        ),
        "selected_source_body_authority_result_preserved": passed(
            "selected_source_body_authority_result_preserved"
        ),
        "selected_eligibility_result_preserved": passed(
            "selected_eligibility_result_preserved"
        ),
        "selected_matter_declaration_preserved": passed(
            "selected_matter_declaration_preserved"
        ),
        "selected_operation_candidate_preserved": passed(
            "selected_operation_candidate_preserved"
        ),
        "selected_operation_matter_preserved": passed(
            "selected_operation_matter_preserved"
        ),
        "refusal_abort_conditions_carry_forward": passed(
            "refusal_abort_conditions_carry_forward"
        ),
        "sync_non_sync_postures_preserved": passed(
            "sync_non_sync_postures_preserved"
        ),
        "carrier_evidence_remains_unmerged": passed(
            "carrier_evidence_remains_unmerged"
        ),
        "carrier_context_remains_context_only": passed(
            "carrier_context_remains_context_only"
        ),
        "divergence_remains_visible": passed("divergence_remains_visible"),
        "refusal_remains_visible": passed("refusal_remains_visible"),
        "blocked_attempts_remain_visible": passed(
            "blocked_attempts_remain_visible"
        ),
        "projection_mismatch_remains_visible": passed(
            "projection_mismatch_remains_visible"
        ),
        "execution_emission_scope_one_admitted_operation_context_only": passed(
            "execution_emission_scope_one_admitted_operation_context_only"
        ),
        "proposed_execution_candidate_preserved": passed(
            "proposed_execution_candidate_present"
        ),
        "proposed_emission_candidate_preserved": passed(
            "proposed_emission_candidate_present"
        ),
        "proposed_output_family_named": passed(
            "proposed_output_family_named_but_not_emitted"
        ),
        "proposed_output_family_emitted": False,
        "receipt_exhaustion_requirement_present": passed(
            "receipt_exhaustion_requirement_present"
        ),
        "action_consequence_separation_present": passed(
            "action_consequence_separation_present"
        ),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "block_code": block_code,
        "block_reason": _block_reason(block_code, request.get("block_reason")),
        "not_ready_reason": request.get("not_ready_reason"),
        "additional_basis_reason": request.get("additional_basis_reason"),
    }
    statement.update(_default_non_claims(outcome))
    return statement


def _determine_outcome(
    request: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    load_block_code: str | None,
) -> tuple[str, str | None]:
    intent = request.get("execution_emission_intent")
    if load_block_code:
        return OUTCOME_BLOCKED, load_block_code
    if intent == INTENT_BLOCK:
        return OUTCOME_BLOCKED, "EXECUTION_EMISSION_REVIEW_REQUEST_EXPLICITLY_BLOCKED"

    first_failed = _first_failed_code(checks)
    if first_failed:
        return OUTCOME_BLOCKED, first_failed

    requested = request.get("requested_execution_emission_outcome", OUTCOME_RECORDED)
    if intent == INTENT_DO_NOT_RECORD:
        return OUTCOME_NOT_READY, None
    if requested == OUTCOME_NOT_READY:
        return OUTCOME_NOT_READY, None
    if requested == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS, None
    if requested == OUTCOME_RECORDED or requested is None:
        if _is_present(request.get("not_ready_reason")):
            return OUTCOME_NOT_READY, None
        if _is_present(request.get("additional_basis_context")):
            return OUTCOME_REQUIRES_ADDITIONAL_BASIS, None
        return OUTCOME_RECORDED, None
    return OUTCOME_BLOCKED, "EXECUTION_EMISSION_INTENT_UNSUPPORTED"


def _metadata(request: Mapping[str, Any]) -> dict[str, Any]:
    request_id = str(request.get("execution_emission_request_id") or "unidentified")
    result_id = f"{RESULT_ID_PREFIX}__{_sanitize_filename(request_id)}"
    return {
        "distributed_execution_emission_result_id": result_id,
        "distributed_execution_emission_result_type": RESULT_TYPE,
        "distributed_execution_emission_result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
    }


def _assemble_result(
    request: Mapping[str, Any],
    selected_admission_result: Mapping[str, Any] | None,
    selected_admission_path: str | None,
    load_block_code: str | None,
    load_block_reason: str | None,
) -> dict[str, Any]:
    selected_operation_context = _selected_operation_context(
        request, selected_admission_result
    )
    selected_refusal_abort_result = _selected_refusal_abort_result(
        request, selected_admission_result
    )
    selected_sync_non_sync_result = _selected_sync_non_sync_result(
        request, selected_admission_result
    )
    selected_carrier_role_result = _selected_carrier_role_result(
        request, selected_admission_result
    )
    selected_source_body_authority_result = _selected_source_body_authority_result(
        request, selected_admission_result
    )
    selected_eligibility_result = _selected_eligibility_result(
        request, selected_admission_result
    )
    selected_matter_declaration = _selected_matter_declaration(
        request, selected_admission_result
    )
    selected_operation_candidate = _selected_operation_candidate(
        request, selected_admission_result
    )
    selected_operation_matter = _selected_operation_matter(
        request, selected_admission_result
    )
    scope_values, scope_flags, unsupported_scope = _normalize_scope(
        request.get("execution_emission_scope")
    )

    checks = _build_checks(
        request,
        selected_admission_result,
        selected_operation_context,
        selected_refusal_abort_result,
        selected_sync_non_sync_result,
        selected_carrier_role_result,
        selected_source_body_authority_result,
        selected_eligibility_result,
        selected_matter_declaration,
        selected_operation_candidate,
        selected_operation_matter,
        scope_flags,
        unsupported_scope,
    )
    outcome, block_code = _determine_outcome(request, checks, load_block_code)
    block_reason = _block_reason(
        block_code,
        load_block_reason if load_block_code else request.get("block_reason"),
    )

    result = {
        "distributed_execution_emission_metadata": _metadata(request),
        "declared_execution_emission_question": _build_declared_question_section(
            request, selected_admission_result, selected_admission_path
        ),
        "selected_admission_transition_result": _build_selected_admission_section(
            request,
            selected_admission_result,
            selected_admission_path,
            selected_operation_context,
        ),
        "selected_operation_context": _build_selected_operation_context_section(
            request,
            selected_admission_result,
            selected_operation_context,
            selected_refusal_abort_result,
            selected_sync_non_sync_result,
            selected_carrier_role_result,
            selected_source_body_authority_result,
            selected_eligibility_result,
            selected_matter_declaration,
            selected_operation_candidate,
            selected_operation_matter,
        ),
        "execution_emission_basis": _build_execution_emission_basis_section(
            request,
            selected_admission_result,
            selected_operation_context,
            selected_refusal_abort_result,
            selected_sync_non_sync_result,
            selected_carrier_role_result,
            selected_source_body_authority_result,
            selected_eligibility_result,
            selected_matter_declaration,
            selected_operation_candidate,
            selected_operation_matter,
            scope_values,
        ),
        "execution_emission_scope": scope_flags,
        "execution_emission_checks": checks,
        "execution_emission_statement": _statement(
            outcome, request, selected_admission_result, checks, block_code
        ),
        "execution_emission_non_meaning": _non_meaning(),
        "additional_basis_required": _additional_basis_required(request, outcome),
        "what_remains_open": _what_remains_open(),
        "non_claims": _default_non_claims(outcome),
        "outcome": outcome,
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "block_code": block_code,
            "block_reason": block_reason,
        },
    }
    result["distributed_execution_emission_summary"] = (
        build_distributed_execution_emission_summary(result)
    )
    return result


def _minimal_blocked_result(
    block_code: str,
    block_reason: str | None = None,
    request_path: str | None = None,
) -> dict[str, Any]:
    request = {
        "execution_emission_request_id": "blocked_request",
        "execution_emission_request_path": request_path,
        "execution_emission_question": None,
        "execution_emission_intent": None,
        "requested_execution_emission_outcome": OUTCOME_BLOCKED,
        "declared_non_claims": {key: False for key in REQUIRED_NON_CLAIMS},
    }
    result = _assemble_result(request, None, None, block_code, block_reason)
    result["block"]["block_code"] = block_code
    result["block"]["block_reason"] = _block_reason(block_code, block_reason)
    result["execution_emission_statement"]["block_code"] = block_code
    result["execution_emission_statement"]["block_reason"] = _block_reason(
        block_code, block_reason
    )
    result["distributed_execution_emission_summary"] = (
        build_distributed_execution_emission_summary(result)
    )
    return result


def resolve_distributed_execution_emission_boundary(
    declared_execution_emission_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one declared distributed execution / emission boundary request."""

    if declared_execution_emission_request is None:
        request = {
            "execution_emission_request_id": "missing_request",
            "execution_emission_question": None,
            "execution_emission_intent": None,
            "declared_non_claims": {key: False for key in REQUIRED_NON_CLAIMS},
        }
        return _assemble_result(request, None, None, None, None)

    if not isinstance(declared_execution_emission_request, Mapping):
        return _minimal_blocked_result(
            "DECLARED_EXECUTION_EMISSION_REQUEST_MALFORMED",
            BLOCK_REASON_BY_CODE["DECLARED_EXECUTION_EMISSION_REQUEST_MALFORMED"],
        )

    request = _deepcopy(dict(declared_execution_emission_request))
    selected_admission_result, load_block_code, load_block_reason, selected_path = (
        _load_selected_admission_result(request)
    )
    return _assemble_result(
        request,
        selected_admission_result,
        selected_path,
        load_block_code,
        load_block_reason,
    )


def resolve_distributed_execution_emission_boundary_from_path(
    declared_execution_emission_request_path: Path | str,
) -> dict:
    """Resolve one declared distributed execution / emission request JSON file."""

    return _load_request_path(declared_execution_emission_request_path)


def build_distributed_execution_emission_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a bounded summary from a distributed execution / emission result."""

    statement = result.get("execution_emission_statement", {})
    if not isinstance(statement, Mapping):
        statement = {}
    declared = result.get("declared_execution_emission_question", {})
    if not isinstance(declared, Mapping):
        declared = {}
    selected = result.get("selected_admission_transition_result", {})
    if not isinstance(selected, Mapping):
        selected = {}
    selected_context = result.get("selected_operation_context", {})
    if not isinstance(selected_context, Mapping):
        selected_context = {}
    non_claims = result.get("non_claims", {})
    if not isinstance(non_claims, Mapping):
        non_claims = {}
    block = result.get("block", {})
    if not isinstance(block, Mapping):
        block = {}

    summary = {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "execution_emission_request_id": declared.get("execution_emission_request_id"),
        "execution_emission_question": declared.get("execution_emission_question"),
        "execution_emission_intent": declared.get("execution_emission_intent"),
        "selected_admission_transition_result_id": selected.get(
            "selected_admission_transition_result_id"
        ),
        "selected_admission_transition_result_outcome": selected.get(
            "selected_admission_transition_result_outcome"
        ),
        "selected_operation_candidate_id": selected_context.get(
            "selected_operation_candidate_id"
        ),
        "selected_operation_matter_id": selected_context.get(
            "selected_operation_matter_id"
        ),
        "passed_check_count": statement.get("passed_check_count", 0),
        "failed_check_count": statement.get("failed_check_count", 0),
        "distributed_execution_emission_boundary_recorded": statement.get(
            "distributed_execution_emission_boundary_recorded", False
        ),
        "not_ready": result.get("outcome") == OUTCOME_NOT_READY,
        "requires_additional_basis": result.get("outcome")
        == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "selected_admission_transition_result_preserved": statement.get(
            "selected_admission_transition_result_preserved", False
        ),
        "selected_admission_transition_result_recorded": statement.get(
            "selected_admission_transition_result_recorded", False
        ),
        "selected_admission_transition_result_failed_check_count_zero": statement.get(
            "selected_admission_transition_result_failed_check_count_zero", False
        ),
        "admitted_operation_context_preserved": statement.get(
            "admitted_operation_context_preserved", False
        ),
        "operation_admitted": statement.get("operation_admitted", False),
        "one_bounded_operation_context_admitted": statement.get(
            "one_bounded_operation_context_admitted", False
        ),
        "selected_refusal_abort_result_preserved": statement.get(
            "selected_refusal_abort_result_preserved", False
        ),
        "selected_sync_non_sync_result_preserved": statement.get(
            "selected_sync_non_sync_result_preserved", False
        ),
        "selected_carrier_role_result_preserved": statement.get(
            "selected_carrier_role_result_preserved", False
        ),
        "selected_source_body_authority_result_preserved": statement.get(
            "selected_source_body_authority_result_preserved", False
        ),
        "selected_eligibility_result_preserved": statement.get(
            "selected_eligibility_result_preserved", False
        ),
        "selected_matter_declaration_preserved": statement.get(
            "selected_matter_declaration_preserved", False
        ),
        "selected_operation_candidate_preserved": statement.get(
            "selected_operation_candidate_preserved", False
        ),
        "selected_operation_matter_preserved": statement.get(
            "selected_operation_matter_preserved", False
        ),
        "refusal_abort_conditions_carry_forward": statement.get(
            "refusal_abort_conditions_carry_forward", False
        ),
        "sync_non_sync_postures_preserved": statement.get(
            "sync_non_sync_postures_preserved", False
        ),
        "carrier_evidence_remains_unmerged": statement.get(
            "carrier_evidence_remains_unmerged", False
        ),
        "carrier_context_remains_context_only": statement.get(
            "carrier_context_remains_context_only", False
        ),
        "divergence_refusal_blocked_attempts_projection_mismatch_visible": all(
            statement.get(key, False)
            for key in (
                "divergence_remains_visible",
                "refusal_remains_visible",
                "blocked_attempts_remain_visible",
                "projection_mismatch_remains_visible",
            )
        ),
        "execution_emission_scope_one_admitted_operation_context_only": statement.get(
            "execution_emission_scope_one_admitted_operation_context_only", False
        ),
        "proposed_output_family_named_but_not_emitted": (
            statement.get("proposed_output_family_named", False)
            and statement.get("proposed_output_family_emitted") is False
        ),
        "receipt_exhaustion_requirement_present": statement.get(
            "receipt_exhaustion_requirement_present", False
        ),
        "action_consequence_separation_present": statement.get(
            "action_consequence_separation_present", False
        ),
        "no_operation_executed_output_emitted_action_consequence": all(
            statement.get(key) is False
            for key in (
                "operation_executed",
                "output_emitted",
                "action_authorized",
                "consequence_created",
            )
        ),
        "no_sync_full_body_transfer_second_body_non_sync_operation": all(
            statement.get(key) is False
            for key in (
                "repository_synchronization_authorized",
                "full_body_transfer_authorized",
                "second_body_created",
                "non_synchronized_operation_authorized",
            )
        ),
        "no_reusable_permission_autonomous_continuation": all(
            statement.get(key) is False
            for key in (
                "reusable_permission_created",
                "autonomous_continuation_authorized",
            )
        ),
        "no_public_readiness_final_completion_follow_on_work": all(
            statement.get(key) is False
            for key in (
                "public_launch_readiness_created",
                "final_completion_claimed",
                "follow_on_work_authorized",
            )
        ),
        "key_non_claims": {
            key: non_claims.get(key)
            for key in (
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
    return summary


def _sanitize_filename(value: str) -> str:
    sanitized = "".join(
        character if character.isalnum() or character in {"-", "_"} else "_"
        for character in value.strip()
    )
    sanitized = "_".join(part for part in sanitized.split("_") if part)
    return sanitized.lower() or "distributed_execution_emission"


def _default_output_path(result: Mapping[str, Any]) -> Path:
    declared = result.get("declared_execution_emission_question", {})
    selected = result.get("selected_admission_transition_result", {})
    metadata = result.get("distributed_execution_emission_metadata", {})
    if not isinstance(declared, Mapping):
        declared = {}
    if not isinstance(selected, Mapping):
        selected = {}
    if not isinstance(metadata, Mapping):
        metadata = {}
    name = _first_present(
        declared.get("execution_emission_request_id"),
        selected.get("selected_admission_transition_result_id"),
        metadata.get("distributed_execution_emission_result_id"),
        "distributed_execution_emission",
    )
    filename = f"{_sanitize_filename(str(name))}__distributed_execution_emission_result.json"
    return DISTRIBUTED_EXECUTION_EMISSION_BOUNDARY_ROOT / filename


def _deduplicated_path(path: Path) -> Path:
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


def write_distributed_execution_emission_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write an additive distributed execution / emission boundary artifact."""

    if not isinstance(result, Mapping):
        raise DistributedExecutionEmissionBoundaryError(
            "Execution / emission result must be a mapping."
        )
    target = Path(output_path) if output_path is not None else _default_output_path(result)
    target = _deduplicated_path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target


def build_declared_distributed_execution_emission_request(
    execution_emission_request_id: str,
    execution_emission_question: str,
    selected_admission_transition_result: Mapping[str, Any] | str,
    execution_emission_basis: Mapping[str, Any] | str,
    execution_emission_scope: Sequence[str] | Mapping[str, Any],
    execution_emission_intent: str = INTENT_RECORD,
    *,
    selected_admission_transition_result_path: str | None = None,
    selected_admission_transition_result_id: str | None = None,
    selected_admission_transition_result_outcome: str | None = None,
    requested_execution_emission_outcome: str = OUTCOME_RECORDED,
    proposed_execution_candidate: Mapping[str, Any] | str | None = None,
    proposed_emission_candidate: Mapping[str, Any] | str | None = None,
    proposed_output_family: Mapping[str, Any] | Sequence[str] | str | None = None,
    additional_basis_context: Mapping[str, Any] | None = None,
    not_ready_reason: str | None = None,
) -> dict:
    """Build a bounded declared execution / emission request."""

    if isinstance(execution_emission_basis, Mapping):
        basis = _deepcopy(dict(execution_emission_basis))
    else:
        basis = {"execution_emission_basis": execution_emission_basis}

    request: dict[str, Any] = {
        "execution_emission_request_id": execution_emission_request_id,
        "execution_emission_question": execution_emission_question,
        "execution_emission_intent": execution_emission_intent,
        "execution_emission_basis": basis,
        "execution_emission_scope": _deepcopy(execution_emission_scope),
        "declared_non_claims": {key: False for key in REQUIRED_NON_CLAIMS},
        "requested_execution_emission_outcome": requested_execution_emission_outcome,
        "receipt_exhaustion_requirement": basis.get(
            "receipt_exhaustion_requirement",
            {
                "receipt_exhaustion_required": True,
                "requirement": "RECEIPT_EXHAUSTION_REQUIRED_BEFORE_CLOSURE",
            },
        ),
        "action_consequence_separation_requirement": basis.get(
            "action_consequence_separation_requirement",
            {
                "action_consequence_separation_required": True,
                "requirement": "ACTION_CONSEQUENCE_REQUIRES_SEPARATE_BOUNDARY",
            },
        ),
    }

    if isinstance(selected_admission_transition_result, Mapping):
        request["selected_admission_transition_result"] = _deepcopy(
            dict(selected_admission_transition_result)
        )
    elif selected_admission_transition_result_path is None:
        request["selected_admission_transition_result_path"] = str(
            selected_admission_transition_result
        )
    else:
        request["selected_admission_transition_result"] = selected_admission_transition_result

    if selected_admission_transition_result_path is not None:
        request["selected_admission_transition_result_path"] = (
            selected_admission_transition_result_path
        )
    if selected_admission_transition_result_id is not None:
        request["selected_admission_transition_result_id"] = (
            selected_admission_transition_result_id
        )
    if selected_admission_transition_result_outcome is not None:
        request["selected_admission_transition_result_outcome"] = (
            selected_admission_transition_result_outcome
        )
    if proposed_execution_candidate is not None:
        request["proposed_execution_candidate"] = _deepcopy(
            proposed_execution_candidate
        )
    else:
        request["proposed_execution_candidate"] = basis.get(
            "proposed_execution_candidate",
            {"candidate": "bounded_execution_candidate_only"},
        )
    if proposed_emission_candidate is not None:
        request["proposed_emission_candidate"] = _deepcopy(proposed_emission_candidate)
    else:
        request["proposed_emission_candidate"] = basis.get(
            "proposed_emission_candidate",
            {"candidate": "bounded_emission_candidate_only"},
        )
    if proposed_output_family is not None:
        request["proposed_output_family"] = _deepcopy(proposed_output_family)
    else:
        request["proposed_output_family"] = basis.get(
            "proposed_output_family",
            {"output_family": "bounded_output_family_named_not_emitted"},
        )
    if additional_basis_context is not None:
        request["additional_basis_context"] = _deepcopy(additional_basis_context)
    if not_ready_reason is not None:
        request["not_ready_reason"] = not_ready_reason

    request["declared_non_claims"]["execution_emission_boundary_recorded"] = (
        requested_execution_emission_outcome == OUTCOME_RECORDED
    )
    return request
