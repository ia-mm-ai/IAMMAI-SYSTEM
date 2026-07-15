"""Resolve the distributed action / consequence boundary.

This module records action / consequence boundary basis only. It does not
authorize action, create consequence, execute operation, emit output, treat
output, evidence, standing, or receipt as consequence, synchronize
repositories, authorize non-synchronized operation, transfer the body, create a
second body, erase refusal / abort, create reusable permission, authorize
autonomous continuation, create public readiness, claim final completion, or
schedule follow-on work.
"""

from __future__ import annotations

import copy
import datetime
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any


class DistributedActionConsequenceBoundaryError(Exception):
    """Raised for hard action / consequence boundary failures."""


RESOLVER_MODULE = "resolve_distributed_action_consequence_boundary"
RESULT_VERSION = "0.1.0"
RESULT_TYPE = "distributed_action_consequence_boundary_result"
RESULT_ID_PREFIX = "distributed_action_consequence_boundary"

DISTRIBUTED_ACTION_CONSEQUENCE_BOUNDARY_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_distributed_action_consequence_boundary"
)

EXPECTED_SELECTED_EXECUTION_EMISSION_OUTCOME = (
    "DISTRIBUTED_EXECUTION_EMISSION_BOUNDARY_RECORDED"
)

OUTCOME_RECORDED = "DISTRIBUTED_ACTION_CONSEQUENCE_BOUNDARY_RECORDED"
OUTCOME_NOT_READY = "DISTRIBUTED_ACTION_CONSEQUENCE_BOUNDARY_NOT_READY"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "DISTRIBUTED_ACTION_CONSEQUENCE_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "DISTRIBUTED_ACTION_CONSEQUENCE_REVIEW_BLOCKED"
OUTCOME_FAMILY = {
    OUTCOME_RECORDED,
    OUTCOME_NOT_READY,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
}

INTENT_RECORD = "RECORD_DISTRIBUTED_ACTION_CONSEQUENCE_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_DISTRIBUTED_ACTION_CONSEQUENCE_BOUNDARY"
INTENT_BLOCK = "BLOCK_DISTRIBUTED_ACTION_CONSEQUENCE_REVIEW"
SUPPORTED_INTENTS = {INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK}

SUPPORTED_ACTION_CONSEQUENCE_SCOPE = (
    "NO_ACTION_AUTHORIZED_BY_BOUNDARY",
    "NO_CONSEQUENCE_CREATED_BY_BOUNDARY",
    "NO_EXECUTION_BY_ACTION_CONSEQUENCE_BOUNDARY",
    "NO_OUTPUT_EMISSION_BY_ACTION_CONSEQUENCE_BOUNDARY",
    "OUTPUT_FAMILY_IS_NOT_CONSEQUENCE",
    "CARRIER_EVIDENCE_IS_NOT_CONSEQUENCE",
    "STANDING_IS_NOT_CONSEQUENCE",
    "RECEIPT_IS_NOT_CONSEQUENCE",
    "CONSEQUENCE_RECOGNITION_REQUIRES_SEPARATE_ACT",
    "RECEIPT_EXHAUSTION_REQUIRED_BEFORE_CLOSURE",
    "CONFORMANCE_REQUIRED_BEFORE_CLOSURE",
    "CLOSURE_REQUIRES_SEPARATE_BOUNDARY",
)

REQUIRED_NON_CLAIMS = (
    "action_authorized",
    "consequence_created",
    "operation_executed",
    "output_emitted",
    "output_treated_as_consequence",
    "evidence_treated_as_consequence",
    "standing_treated_as_consequence",
    "receipt_treated_as_consequence",
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
    "ACTION_CONSEQUENCE_REVIEW_AUTHORIZES_ACTION": (
        "action_authorized",
        "action_created",
        "truth_action_created",
        "action_permission_created",
    ),
    "ACTION_CONSEQUENCE_REVIEW_CREATES_CONSEQUENCE": (
        "consequence_created",
        "consequence_action_created",
        "operation_consequence_created",
    ),
    "ACTION_CONSEQUENCE_REVIEW_EXECUTES_OPERATION": (
        "operation_executed",
        "operation_execution_started",
        "distributed_operation_executed",
    ),
    "ACTION_CONSEQUENCE_REVIEW_EMITS_OUTPUT": (
        "output_emitted",
        "emission_created",
        "operation_output_emitted",
        "output_generated",
        "proposed_output_family_emitted",
    ),
    "ACTION_CONSEQUENCE_REVIEW_TREATS_OUTPUT_AS_CONSEQUENCE": (
        "output_treated_as_consequence",
        "output_family_treated_as_consequence",
        "proposed_output_family_treated_as_consequence",
    ),
    "ACTION_CONSEQUENCE_REVIEW_TREATS_EVIDENCE_AS_CONSEQUENCE": (
        "evidence_treated_as_consequence",
        "carrier_evidence_treated_as_consequence",
    ),
    "ACTION_CONSEQUENCE_REVIEW_TREATS_STANDING_AS_CONSEQUENCE": (
        "standing_treated_as_consequence",
        "distributed_standing_treated_as_consequence",
    ),
    "ACTION_CONSEQUENCE_REVIEW_TREATS_RECEIPT_AS_CONSEQUENCE": (
        "receipt_treated_as_consequence",
        "receipt_exhaustion_treated_as_consequence",
    ),
    "ACTION_CONSEQUENCE_REVIEW_AUTHORIZES_SYNCHRONIZATION": (
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
    "ACTION_CONSEQUENCE_REVIEW_AUTHORIZES_NON_SYNCHRONIZED_OPERATION": (
        "non_synchronized_operation_authorized",
        "non_sync_operation_authorized",
        "carrier_autonomy_authorized",
        "stale_carrier_operation_authorized",
        "divergent_live_operation_authorized",
        "independent_carrier_operation_authorized",
    ),
    "ACTION_CONSEQUENCE_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER": (
        "full_body_transfer_authorized",
        "full_body_transfer_created",
    ),
    "ACTION_CONSEQUENCE_REVIEW_CREATES_SECOND_BODY": (
        "second_body_created",
        "second_body_authorized",
    ),
    "ACTION_CONSEQUENCE_REVIEW_ACTIVATES_CARRIER_ROLES_BEYOND_SCOPE": (
        "carrier_role_activated_beyond_scope",
        "carrier_roles_activated_beyond_scope",
        "carrier_role_activated",
        "carrier_roles_activated",
        "carrier_role_assigned_for_operation",
        "carrier_assigned_to_live_operation",
    ),
    "ACTION_CONSEQUENCE_REVIEW_CREATES_CARRIER_AUTHORITY": (
        "carrier_authority_created",
        "carrier_authority_granted",
        "authority_created",
        "authority_granted",
    ),
    "ACTION_CONSEQUENCE_REVIEW_CREATES_CARRIER_CURRENTNESS": (
        "carrier_currentness_created",
        "currentness_created",
    ),
    "ACTION_CONSEQUENCE_REVIEW_SELECTS_CURRENT_CARRIER": (
        "current_carrier_selected",
    ),
    "ACTION_CONSEQUENCE_REVIEW_SELECTS_WINNING_CARRIER": (
        "winning_carrier_selected",
        "carrier_b_success_becomes_winner",
        "carrier_b_success_forces_continuation",
    ),
    "ACTION_CONSEQUENCE_REVIEW_INVALIDATES_LOSING_CARRIER": (
        "losing_carrier_invalidated",
        "carrier_c_block_becomes_loser",
        "carrier_c_block_invalidates_carrier_c",
    ),
    "ACTION_CONSEQUENCE_REVIEW_REPLACES_SOURCE": (
        "source_replaced",
        "source_replaced_by_carrier",
        "carrier_becomes_source",
    ),
    "ACTION_CONSEQUENCE_REVIEW_CREATES_PUBLIC_READINESS": (
        "public_launch_readiness_created",
        "public_readiness_created",
    ),
    "ACTION_CONSEQUENCE_REVIEW_CLAIMS_FINAL_COMPLETION": (
        "final_completion_claimed",
        "final_governance_completed",
        "final_continuity_completed",
        "final_system_identity_completed",
    ),
    "ACTION_CONSEQUENCE_REVIEW_SCHEDULES_FOLLOW_ON_WORK": (
        "follow_on_work_authorized",
        "follow_on_work_scheduled",
        "self_orientation_successor_scheduled",
    ),
    "ACTION_CONSEQUENCE_REVIEW_CREATES_REUSABLE_PERMISSION": (
        "reusable_permission_created",
        "permission_created",
        "standing_permission_created",
    ),
    "ACTION_CONSEQUENCE_REVIEW_AUTHORIZES_AUTONOMOUS_CONTINUATION": (
        "autonomous_continuation_authorized",
        "continuation_authorized",
        "autonomous_operation_authorized",
    ),
    "ACTION_CONSEQUENCE_REVIEW_ERASES_REFUSAL_ABORT": (
        "refusal_abort_erased",
        "refusal_abort_conditions_erased",
        "non_admission_conditions_erased",
        "abort_conditions_erased",
    ),
    "ACTION_CONSEQUENCE_REVIEW_ERASES_EVIDENCE_OR_REFUSAL": (
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
    "ACTION_CONSEQUENCE_REVIEW_RESOLVES_DIVERGENCE": (
        "divergence_resolved",
    ),
    "MUTATION_REPLAY_OR_MERGE_DETECTED": (
        "mutation_performed",
        "replay_performed",
        "merge_performed",
    ),
}

BLOCK_REASON_BY_CODE = {
    "DECLARED_ACTION_CONSEQUENCE_REQUEST_MALFORMED": (
        "Declared action / consequence request is not a mapping."
    ),
    "DECLARED_ACTION_CONSEQUENCE_REQUEST_UNREADABLE": (
        "Declared action / consequence request path is unreadable."
    ),
    "ACTION_CONSEQUENCE_REVIEW_REQUEST_EXPLICITLY_BLOCKED": (
        "Declared action / consequence request explicitly blocks review."
    ),
    "ACTION_CONSEQUENCE_QUESTION_UNDECLARED": (
        "Action / consequence question is undeclared."
    ),
    "ACTION_CONSEQUENCE_INTENT_UNSUPPORTED": (
        "Action / consequence intent is unsupported."
    ),
    "EXECUTION_EMISSION_RESULT_MISSING": (
        "Selected execution / emission result is missing."
    ),
    "EXECUTION_EMISSION_RESULT_UNREADABLE": (
        "Selected execution / emission result path is unreadable."
    ),
    "EXECUTION_EMISSION_RESULT_MALFORMED": (
        "Selected execution / emission result is malformed."
    ),
    "EXECUTION_EMISSION_RESULT_OUTCOME_MISSING": (
        "Selected execution / emission result outcome is missing."
    ),
    "EXECUTION_EMISSION_RESULT_NOT_RECORDED": (
        "Selected execution / emission result is not recorded."
    ),
    "EXECUTION_EMISSION_RESULT_HAS_FAILED_CHECKS": (
        "Selected execution / emission result has failed checks."
    ),
    "ADMISSION_TRANSITION_RESULT_MISSING": (
        "Selected admission / transition result is missing."
    ),
    "ADMITTED_OPERATION_CONTEXT_MISSING": "Admitted operation context is missing.",
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
    "SELECTED_ELIGIBILITY_RESULT_MISSING": "Selected eligibility result is missing.",
    "SELECTED_MATTER_DECLARATION_MISSING": (
        "Selected matter declaration is missing."
    ),
    "SELECTED_OPERATION_CANDIDATE_MISSING": (
        "Selected operation candidate is missing."
    ),
    "SELECTED_OPERATION_MATTER_MISSING": "Selected operation matter is missing.",
    "PROPOSED_OUTPUT_FAMILY_MISSING": "Proposed output family is missing.",
    "RECEIPT_EXHAUSTION_REQUIREMENT_MISSING": (
        "Receipt / exhaustion requirement is missing."
    ),
    "ACTION_CONSEQUENCE_SEPARATION_REQUIREMENT_MISSING": (
        "Action / consequence separation requirement is missing."
    ),
    "ACTION_CONSEQUENCE_SCOPE_MISSING": (
        "Declared action / consequence scope is missing."
    ),
    "UNSUPPORTED_ACTION_CONSEQUENCE_SCOPE": (
        "Action / consequence scope contains an unsupported value."
    ),
    "NON_CLAIM_MISSING_OR_FLIPPED": (
        "A required action / consequence non-claim is missing or true."
    ),
}


def _utc_now() -> str:
    return datetime.datetime.now(datetime.UTC).replace(microsecond=0).isoformat()


def _deepcopy(value: Any) -> Any:
    return copy.deepcopy(value)


def _is_present(value: Any) -> bool:
    if value is None:
        return False
    if value == "":
        return False
    if isinstance(value, (list, tuple, set, dict)) and not value:
        return False
    return True


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
            "DECLARED_ACTION_CONSEQUENCE_REQUEST_UNREADABLE",
            detail or BLOCK_REASON_BY_CODE[
                "DECLARED_ACTION_CONSEQUENCE_REQUEST_UNREADABLE"
            ],
            request_path=str(path),
        )
    if error == "malformed":
        return _minimal_blocked_result(
            "DECLARED_ACTION_CONSEQUENCE_REQUEST_MALFORMED",
            detail or "Declared action / consequence request JSON is malformed.",
            request_path=str(path),
        )
    assert payload is not None
    request = _deepcopy(payload)
    request["action_consequence_request_path"] = str(path)
    return resolve_distributed_action_consequence_boundary(request)


def _load_selected_execution_result(
    request: Mapping[str, Any],
) -> tuple[dict[str, Any] | None, str | None, str | None, str | None]:
    result_path = request.get("selected_execution_emission_result_path")
    if _is_present(result_path):
        payload, error, detail = _read_json_object(str(result_path))
        if error == "unreadable":
            return (
                None,
                "EXECUTION_EMISSION_RESULT_UNREADABLE",
                detail or "Selected execution / emission result path is unreadable.",
                str(result_path),
            )
        if error == "malformed":
            return (
                None,
                "EXECUTION_EMISSION_RESULT_MALFORMED",
                detail or "Selected execution / emission result is malformed.",
                str(result_path),
            )
        assert payload is not None
        return _deepcopy(payload), None, None, str(result_path)

    selected = request.get("selected_execution_emission_result")
    if not _is_present(selected):
        return None, None, None, None
    if not isinstance(selected, Mapping):
        return (
            None,
            "EXECUTION_EMISSION_RESULT_MALFORMED",
            "Selected execution / emission result is not a mapping.",
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
        "distributed_execution_emission_summary",
        "execution_emission_statement",
        "summary",
        "statement",
    ):
        value = _get_path(result, (section, "failed_check_count"))
        if isinstance(value, int):
            return value
    checks = result.get("execution_emission_checks")
    if isinstance(checks, Sequence) and not isinstance(checks, (str, bytes, bytearray)):
        return sum(
            1
            for check in checks
            if isinstance(check, Mapping) and check.get("passed") is not True
        )
    return None


def _extract_execution_result_id(result: Any) -> str | None:
    return _first_present(
        _get_path(
            result,
            (
                "distributed_execution_emission_metadata",
                "distributed_execution_emission_result_id",
            ),
        ),
        _get_path(result, ("metadata", "result_id")),
        _find_first_present(
            result,
            (
                "distributed_execution_emission_result_id",
                "execution_emission_result_id",
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
    summary = _get_path(result, ("distributed_execution_emission_summary", "outcome"))
    if isinstance(summary, str) and summary:
        return summary
    return None


def _execution_statement(result: Any) -> Mapping[str, Any]:
    if not isinstance(result, Mapping):
        return {}
    statement = result.get("execution_emission_statement")
    return statement if isinstance(statement, Mapping) else {}


def _execution_summary(result: Any) -> Mapping[str, Any]:
    if not isinstance(result, Mapping):
        return {}
    summary = result.get("distributed_execution_emission_summary")
    return summary if isinstance(summary, Mapping) else {}


def _execution_non_claims(result: Any) -> Mapping[str, Any]:
    if not isinstance(result, Mapping):
        return {}
    non_claims = result.get("non_claims")
    return non_claims if isinstance(non_claims, Mapping) else {}


def _execution_bool(result: Any, key: str) -> bool:
    statement = _execution_statement(result)
    summary = _execution_summary(result)
    non_claims = _execution_non_claims(result)
    return (
        statement.get(key) is True
        or summary.get(key) is True
        or non_claims.get(key) is True
        or (isinstance(result, Mapping) and result.get(key) is True)
    )


def _execution_false(result: Any, key: str) -> bool:
    statement = _execution_statement(result)
    summary = _execution_summary(result)
    non_claims = _execution_non_claims(result)
    values = [
        statement.get(key),
        summary.get(key),
        non_claims.get(key),
        result.get(key) if isinstance(result, Mapping) else None,
    ]
    return not any(value is True for value in values)


def _basis(request: Mapping[str, Any]) -> Mapping[str, Any]:
    basis = request.get("action_consequence_basis")
    return basis if isinstance(basis, Mapping) else {}


def _selected_from_request_basis_execution(
    request: Mapping[str, Any],
    execution_result: Mapping[str, Any] | None,
    key: str,
    execution_paths: Sequence[Sequence[str]],
) -> Any:
    basis = _basis(request)
    value = _first_present(request.get(key), basis.get(key))
    if _is_present(value):
        return _deepcopy(value)
    if execution_result is not None:
        for path in execution_paths:
            found = _get_path(execution_result, path)
            if _is_present(found):
                return _deepcopy(found)
    return None


def _selected_admission_transition_result(
    request: Mapping[str, Any],
    execution_result: Mapping[str, Any] | None,
) -> Any:
    return _selected_from_request_basis_execution(
        request,
        execution_result,
        "selected_admission_transition_result",
        (
            ("selected_operation_context", "selected_admission_transition_result"),
            ("execution_emission_basis", "selected_admission_transition_result"),
            ("selected_admission_transition_result", "selected_admission_transition_result"),
        ),
    )


def _selected_operation_context(
    request: Mapping[str, Any],
    execution_result: Mapping[str, Any] | None,
) -> Any:
    basis = _basis(request)
    value = _first_present(
        request.get("selected_operation_context"),
        basis.get("selected_operation_context"),
        _get_path(execution_result, ("selected_operation_context", "admitted_operation_context")),
        _get_path(execution_result, ("execution_emission_basis", "selected_admitted_operation_context")),
        _get_path(execution_result, ("selected_operation_context",)),
    )
    return _deepcopy(value) if _is_present(value) else None


def _selected_refusal_abort_result(
    request: Mapping[str, Any],
    execution_result: Mapping[str, Any] | None,
) -> Any:
    return _selected_from_request_basis_execution(
        request,
        execution_result,
        "selected_refusal_abort_result",
        (
            ("selected_operation_context", "selected_refusal_abort_result"),
            ("execution_emission_basis", "selected_refusal_abort_result"),
        ),
    )


def _selected_sync_non_sync_result(
    request: Mapping[str, Any],
    execution_result: Mapping[str, Any] | None,
) -> Any:
    return _selected_from_request_basis_execution(
        request,
        execution_result,
        "selected_sync_non_sync_result",
        (
            ("selected_operation_context", "selected_sync_non_sync_result"),
            ("execution_emission_basis", "selected_sync_non_sync_result"),
        ),
    )


def _selected_carrier_role_result(
    request: Mapping[str, Any],
    execution_result: Mapping[str, Any] | None,
) -> Any:
    return _selected_from_request_basis_execution(
        request,
        execution_result,
        "selected_carrier_role_result",
        (
            ("selected_operation_context", "selected_carrier_role_result"),
            ("execution_emission_basis", "selected_carrier_role_result"),
        ),
    )


def _selected_source_body_authority_result(
    request: Mapping[str, Any],
    execution_result: Mapping[str, Any] | None,
) -> Any:
    return _selected_from_request_basis_execution(
        request,
        execution_result,
        "selected_source_body_authority_result",
        (
            ("selected_operation_context", "selected_source_body_authority_result"),
            ("execution_emission_basis", "selected_source_body_authority_result"),
        ),
    )


def _selected_eligibility_result(
    request: Mapping[str, Any],
    execution_result: Mapping[str, Any] | None,
) -> Any:
    return _selected_from_request_basis_execution(
        request,
        execution_result,
        "selected_eligibility_result",
        (
            ("selected_operation_context", "selected_eligibility_result"),
            ("execution_emission_basis", "selected_eligibility_result"),
        ),
    )


def _selected_matter_declaration(
    request: Mapping[str, Any],
    execution_result: Mapping[str, Any] | None,
) -> Any:
    return _selected_from_request_basis_execution(
        request,
        execution_result,
        "selected_matter_declaration",
        (
            ("selected_operation_context", "selected_matter_declaration"),
            ("execution_emission_basis", "selected_matter_declaration"),
        ),
    )


def _selected_operation_candidate(
    request: Mapping[str, Any],
    execution_result: Mapping[str, Any] | None,
) -> Any:
    return _selected_from_request_basis_execution(
        request,
        execution_result,
        "selected_operation_candidate",
        (
            ("selected_operation_context", "selected_operation_candidate"),
            ("execution_emission_basis", "selected_operation_candidate"),
        ),
    )


def _selected_operation_matter(
    request: Mapping[str, Any],
    execution_result: Mapping[str, Any] | None,
) -> Any:
    return _selected_from_request_basis_execution(
        request,
        execution_result,
        "selected_operation_matter",
        (
            ("selected_operation_context", "selected_operation_matter"),
            ("execution_emission_basis", "selected_operation_matter"),
        ),
    )


def _basis_value(
    request: Mapping[str, Any],
    execution_result: Mapping[str, Any] | None,
    key: str,
) -> Any:
    basis = _basis(request)
    return _first_present(
        request.get(key),
        basis.get(key),
        _get_path(execution_result, ("execution_emission_basis", key)),
        _get_path(execution_result, ("selected_operation_context", key)),
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
        values = scope.get("selected_action_consequence_scope")
        if values is None:
            values = scope.get("action_consequence_scope")
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
        value for value in selected if value not in SUPPORTED_ACTION_CONSEQUENCE_SCOPE
    ]
    selected_set = set(selected)
    flags = {
        "selected_action_consequence_scope": selected,
        "supported_action_consequence_scope": list(SUPPORTED_ACTION_CONSEQUENCE_SCOPE),
        "unsupported_action_consequence_scope": unsupported,
        "all_selected_action_consequence_scope_supported": not unsupported,
        "no_action_authorized_by_boundary": (
            "NO_ACTION_AUTHORIZED_BY_BOUNDARY" in selected_set
        ),
        "no_consequence_created_by_boundary": (
            "NO_CONSEQUENCE_CREATED_BY_BOUNDARY" in selected_set
        ),
        "no_execution_by_action_consequence_boundary": (
            "NO_EXECUTION_BY_ACTION_CONSEQUENCE_BOUNDARY" in selected_set
        ),
        "no_output_emission_by_action_consequence_boundary": (
            "NO_OUTPUT_EMISSION_BY_ACTION_CONSEQUENCE_BOUNDARY" in selected_set
        ),
        "output_family_is_not_consequence": (
            "OUTPUT_FAMILY_IS_NOT_CONSEQUENCE" in selected_set
        ),
        "carrier_evidence_is_not_consequence": (
            "CARRIER_EVIDENCE_IS_NOT_CONSEQUENCE" in selected_set
        ),
        "standing_is_not_consequence": "STANDING_IS_NOT_CONSEQUENCE" in selected_set,
        "receipt_is_not_consequence": "RECEIPT_IS_NOT_CONSEQUENCE" in selected_set,
        "consequence_recognition_requires_separate_act": (
            "CONSEQUENCE_RECOGNITION_REQUIRES_SEPARATE_ACT" in selected_set
        ),
        "receipt_exhaustion_required_before_closure": (
            "RECEIPT_EXHAUSTION_REQUIRED_BEFORE_CLOSURE" in selected_set
        ),
        "conformance_required_before_closure": (
            "CONFORMANCE_REQUIRED_BEFORE_CLOSURE" in selected_set
        ),
        "closure_requires_separate_boundary": (
            "CLOSURE_REQUIRES_SEPARATE_BOUNDARY" in selected_set
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
    status = non_claims.get("action_consequence_boundary_recorded")
    requested = request.get("requested_action_consequence_outcome", OUTCOME_RECORDED)
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
    scope = request.get("action_consequence_scope")
    if isinstance(scope, Mapping):
        candidates.append(scope)

    for code, fields in COLLAPSE_FIELDS.items():
        for candidate in candidates:
            if _contains_true(candidate, fields):
                return code
    return None


def _execution_result_collapse_code(
    execution_result: Mapping[str, Any] | None,
) -> str | None:
    if not isinstance(execution_result, Mapping):
        return None
    statement = _execution_statement(execution_result)
    summary = _execution_summary(execution_result)
    non_claims = _execution_non_claims(execution_result)
    basis = execution_result.get("execution_emission_basis")
    candidates: list[Mapping[str, Any]] = [execution_result, statement, summary, non_claims]
    if isinstance(basis, Mapping):
        candidates.append(basis)
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
    non_claims["action_consequence_boundary_recorded"] = outcome == OUTCOME_RECORDED
    return non_claims


def _non_meaning() -> dict[str, bool]:
    meanings = {
        "action_authorized": True,
        "consequence_created": True,
        "operation_executed": True,
        "output_emitted": True,
        "output_treated_as_consequence": True,
        "evidence_treated_as_consequence": True,
        "standing_treated_as_consequence": True,
        "receipt_treated_as_consequence": True,
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
                "Additional action / consequence basis is required.",
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
    selected_execution_result: Mapping[str, Any] | None,
    selected_execution_path: str | None,
) -> dict[str, Any]:
    return {
        "action_consequence_request_id": request.get("action_consequence_request_id"),
        "action_consequence_request_path": request.get("action_consequence_request_path"),
        "action_consequence_question": request.get("action_consequence_question"),
        "action_consequence_intent": request.get("action_consequence_intent"),
        "requested_action_consequence_outcome": request.get(
            "requested_action_consequence_outcome", OUTCOME_RECORDED
        ),
        "selected_execution_emission_result_id": _first_present(
            request.get("selected_execution_emission_result_id"),
            _extract_execution_result_id(selected_execution_result),
        ),
        "selected_execution_emission_result_outcome": _first_present(
            request.get("selected_execution_emission_result_outcome"),
            _extract_outcome(selected_execution_result),
        ),
        "selected_execution_emission_result_path": selected_execution_path,
        "action_consequence_boundary_is_not_action": True,
        "action_consequence_boundary_is_not_consequence": True,
        "action_consequence_boundary_is_not_execution": True,
        "action_consequence_boundary_is_not_emission": True,
        "action_consequence_boundary_is_not_synchronization": True,
        "action_consequence_boundary_is_not_full_body_transfer": True,
        "action_consequence_boundary_is_not_second_body": True,
        "action_consequence_boundary_is_not_reusable_permission": True,
        "action_consequence_boundary_is_not_autonomous_continuation": True,
    }


def _build_selected_execution_section(
    request: Mapping[str, Any],
    selected_execution_result: Mapping[str, Any] | None,
    selected_execution_path: str | None,
) -> dict[str, Any]:
    outcome = _extract_outcome(selected_execution_result)
    failed_count = _extract_failed_check_count(selected_execution_result)
    execution_collapse = _execution_result_collapse_code(selected_execution_result)
    return {
        "selected_execution_emission_result": _deepcopy(selected_execution_result),
        "selected_execution_emission_result_id": _first_present(
            request.get("selected_execution_emission_result_id"),
            _extract_execution_result_id(selected_execution_result),
        ),
        "selected_execution_emission_result_path": selected_execution_path,
        "selected_execution_emission_result_outcome": _first_present(
            request.get("selected_execution_emission_result_outcome"),
            outcome,
        ),
        "expected_selected_execution_emission_outcome": _first_present(
            request.get("expected_selected_execution_emission_outcome"),
            EXPECTED_SELECTED_EXECUTION_EMISSION_OUTCOME,
        ),
        "selected_execution_emission_result_outcome_is_recorded": (
            outcome == EXPECTED_SELECTED_EXECUTION_EMISSION_OUTCOME
        ),
        "selected_execution_emission_result_failed_check_count": failed_count,
        "selected_execution_emission_result_failed_check_count_zero": (
            failed_count == 0
        ),
        "selected_execution_emission_boundary_preserved": (
            _execution_bool(
                selected_execution_result,
                "distributed_execution_emission_boundary_recorded",
            )
            or outcome == EXPECTED_SELECTED_EXECUTION_EMISSION_OUTCOME
        ),
        "selected_execution_emission_result_did_not_execute_operation": (
            _execution_false(selected_execution_result, "operation_executed")
            and execution_collapse
            != "ACTION_CONSEQUENCE_REVIEW_EXECUTES_OPERATION"
        ),
        "selected_execution_emission_result_did_not_emit_output": (
            _execution_false(selected_execution_result, "output_emitted")
            and execution_collapse != "ACTION_CONSEQUENCE_REVIEW_EMITS_OUTPUT"
        ),
        "selected_execution_emission_result_did_not_authorize_action": (
            _execution_false(selected_execution_result, "action_authorized")
            and execution_collapse
            != "ACTION_CONSEQUENCE_REVIEW_AUTHORIZES_ACTION"
        ),
        "selected_execution_emission_result_did_not_create_consequence": (
            _execution_false(selected_execution_result, "consequence_created")
            and execution_collapse
            != "ACTION_CONSEQUENCE_REVIEW_CREATES_CONSEQUENCE"
        ),
        "selected_execution_emission_result_preserved_proposed_output_family_named": (
            _execution_bool(selected_execution_result, "proposed_output_family_named")
        ),
        "selected_execution_emission_result_preserved_proposed_output_family_not_emitted": (
            _execution_false(selected_execution_result, "proposed_output_family_emitted")
            and _execution_false(selected_execution_result, "output_emitted")
        ),
        "selected_execution_emission_result_preserved_receipt_exhaustion_requirement": (
            _execution_bool(
                selected_execution_result,
                "receipt_exhaustion_requirement_present",
            )
        ),
        "selected_execution_emission_result_preserved_action_consequence_separation": (
            _execution_bool(
                selected_execution_result,
                "action_consequence_separation_present",
            )
        ),
    }


def _build_selected_operation_context_section(
    selected_execution_result: Mapping[str, Any] | None,
    selected_admission_transition_result: Any,
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
        "selected_execution_emission_result": _deepcopy(selected_execution_result),
        "selected_admission_transition_result": _deepcopy(
            selected_admission_transition_result
        ),
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
        "operation_admitted": _execution_bool(
            selected_execution_result, "operation_admitted"
        ),
        "one_bounded_operation_context_admitted": _execution_bool(
            selected_execution_result, "one_bounded_operation_context_admitted"
        ),
        "execution_emission_boundary_recorded": _execution_bool(
            selected_execution_result, "distributed_execution_emission_boundary_recorded"
        ) or _extract_outcome(selected_execution_result)
        == EXPECTED_SELECTED_EXECUTION_EMISSION_OUTCOME,
        "no_operation_executed": True,
        "no_output_emitted": True,
        "no_action_authorized": True,
        "no_consequence_created": True,
        "operation_executed": False,
        "output_emitted": False,
        "action_authorized": False,
        "consequence_created": False,
    }


def _build_action_consequence_basis_section(
    request: Mapping[str, Any],
    selected_execution_result: Mapping[str, Any] | None,
    selected_admission_transition_result: Any,
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
        "selected_execution_emission_result": _deepcopy(selected_execution_result),
        "selected_admission_transition_result": _deepcopy(
            selected_admission_transition_result
        ),
        "selected_operation_context": _deepcopy(selected_operation_context),
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
        "proposed_output_family": _deepcopy(
            _basis_value(request, selected_execution_result, "proposed_output_family")
        ),
        "receipt_exhaustion_requirement": _deepcopy(
            _basis_value(
                request,
                selected_execution_result,
                "receipt_exhaustion_requirement",
            )
        ),
        "action_consequence_separation_requirement": _deepcopy(
            _basis_value(
                request,
                selected_execution_result,
                "action_consequence_separation_requirement",
            )
        ),
        "refusal_abort_carry_forward_conditions": _deepcopy(
            _basis_value(
                request,
                selected_execution_result,
                "refusal_abort_carry_forward_conditions",
            )
        ),
        "evidence_carrier_context_posture": _deepcopy(
            _basis_value(
                request,
                selected_execution_result,
                "evidence_carrier_context_posture",
            )
        ),
        "declared_action_consequence_scope": scope_values,
        "proposed_action_posture": _deepcopy(
            request.get("proposed_action_posture")
            or _basis(request).get("proposed_action_posture")
        ),
        "proposed_consequence_posture": _deepcopy(
            request.get("proposed_consequence_posture")
            or _basis(request).get("proposed_consequence_posture")
        ),
        "output_family_is_not_consequence": True,
        "carrier_evidence_is_not_consequence": True,
        "standing_is_not_consequence": True,
        "receipt_is_not_consequence": True,
        "action_consequence_basis_is_not_action": True,
        "action_consequence_basis_is_not_consequence": True,
        "action_consequence_basis_is_not_execution": True,
        "action_consequence_basis_is_not_emission": True,
        "action_consequence_basis_is_not_receipt": True,
        "action_consequence_basis_is_not_closure": True,
        "public_readiness_remains_false": True,
        "final_completion_remains_false": True,
    }


def _build_checks(
    request: Mapping[str, Any],
    selected_execution_result: Mapping[str, Any] | None,
    selected_admission_transition_result: Any,
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
    intent = request.get("action_consequence_intent")
    execution_outcome = _extract_outcome(selected_execution_result)
    failed_count = _extract_failed_check_count(selected_execution_result)
    proposed_output_family = _basis_value(
        request, selected_execution_result, "proposed_output_family"
    )
    receipt_requirement = _basis_value(
        request, selected_execution_result, "receipt_exhaustion_requirement"
    )
    action_consequence_requirement = _basis_value(
        request, selected_execution_result, "action_consequence_separation_requirement"
    )
    collapse = _collapse_code(request)
    execution_collapse = _execution_result_collapse_code(selected_execution_result)

    def collapsed(*codes: str) -> str | None:
        if collapse in codes:
            return collapse
        if execution_collapse in codes:
            return execution_collapse
        return None

    sync_transfer_collapse = collapsed(
        "ACTION_CONSEQUENCE_REVIEW_AUTHORIZES_SYNCHRONIZATION",
        "ACTION_CONSEQUENCE_REVIEW_AUTHORIZES_NON_SYNCHRONIZED_OPERATION",
        "ACTION_CONSEQUENCE_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER",
        "ACTION_CONSEQUENCE_REVIEW_CREATES_SECOND_BODY",
    )
    non_consequence_collapse = collapsed(
        "ACTION_CONSEQUENCE_REVIEW_TREATS_OUTPUT_AS_CONSEQUENCE",
        "ACTION_CONSEQUENCE_REVIEW_TREATS_EVIDENCE_AS_CONSEQUENCE",
        "ACTION_CONSEQUENCE_REVIEW_TREATS_STANDING_AS_CONSEQUENCE",
        "ACTION_CONSEQUENCE_REVIEW_TREATS_RECEIPT_AS_CONSEQUENCE",
    )
    public_final_follow_on_collapse = collapsed(
        "ACTION_CONSEQUENCE_REVIEW_CREATES_PUBLIC_READINESS",
        "ACTION_CONSEQUENCE_REVIEW_CLAIMS_FINAL_COMPLETION",
        "ACTION_CONSEQUENCE_REVIEW_SCHEDULES_FOLLOW_ON_WORK",
    )
    carrier_refusal_erasure_collapse = collapsed(
        "ACTION_CONSEQUENCE_REVIEW_ACTIVATES_CARRIER_ROLES_BEYOND_SCOPE",
        "ACTION_CONSEQUENCE_REVIEW_CREATES_CARRIER_AUTHORITY",
        "ACTION_CONSEQUENCE_REVIEW_CREATES_CARRIER_CURRENTNESS",
        "ACTION_CONSEQUENCE_REVIEW_SELECTS_CURRENT_CARRIER",
        "ACTION_CONSEQUENCE_REVIEW_SELECTS_WINNING_CARRIER",
        "ACTION_CONSEQUENCE_REVIEW_INVALIDATES_LOSING_CARRIER",
        "ACTION_CONSEQUENCE_REVIEW_REPLACES_SOURCE",
        "ACTION_CONSEQUENCE_REVIEW_ERASES_REFUSAL_ABORT",
        "ACTION_CONSEQUENCE_REVIEW_ERASES_EVIDENCE_OR_REFUSAL",
        "ACTION_CONSEQUENCE_REVIEW_RESOLVES_DIVERGENCE",
    )

    checks = [
        _check(
            "action_consequence_question_declared",
            _is_present(request.get("action_consequence_question")),
            "declared action / consequence question",
            request.get("action_consequence_question"),
            "ACTION_CONSEQUENCE_QUESTION_UNDECLARED",
        ),
        _check(
            "action_consequence_intent_supported",
            intent in SUPPORTED_INTENTS,
            sorted(SUPPORTED_INTENTS),
            intent,
            "ACTION_CONSEQUENCE_INTENT_UNSUPPORTED",
        ),
        _check(
            "selected_execution_emission_result_present",
            isinstance(selected_execution_result, Mapping),
            "selected execution / emission result present",
            type(selected_execution_result).__name__,
            "EXECUTION_EMISSION_RESULT_MISSING",
        ),
        _check(
            "selected_execution_emission_result_outcome_declared",
            _is_present(execution_outcome),
            "execution / emission outcome declared",
            execution_outcome,
            "EXECUTION_EMISSION_RESULT_OUTCOME_MISSING",
        ),
        _check(
            "selected_execution_emission_result_outcome_recorded",
            execution_outcome == EXPECTED_SELECTED_EXECUTION_EMISSION_OUTCOME,
            EXPECTED_SELECTED_EXECUTION_EMISSION_OUTCOME,
            execution_outcome,
            "EXECUTION_EMISSION_RESULT_NOT_RECORDED",
        ),
        _check(
            "selected_execution_emission_result_failed_check_count_zero",
            failed_count == 0,
            0,
            failed_count,
            "EXECUTION_EMISSION_RESULT_HAS_FAILED_CHECKS",
        ),
        _check(
            "selected_execution_emission_boundary_preserved",
            _execution_bool(
                selected_execution_result,
                "distributed_execution_emission_boundary_recorded",
            )
            or execution_outcome == EXPECTED_SELECTED_EXECUTION_EMISSION_OUTCOME,
            "selected execution / emission boundary preserved",
            _execution_bool(
                selected_execution_result,
                "distributed_execution_emission_boundary_recorded",
            ),
            "EXECUTION_EMISSION_RESULT_NOT_RECORDED",
        ),
        _check(
            "selected_admission_transition_result_preserved",
            _is_present(selected_admission_transition_result),
            "selected admission / transition result preserved",
            selected_admission_transition_result,
            "ADMISSION_TRANSITION_RESULT_MISSING",
        ),
        _check(
            "selected_admitted_operation_context_preserved",
            _is_present(selected_operation_context),
            "selected admitted operation context preserved",
            selected_operation_context,
            "ADMITTED_OPERATION_CONTEXT_MISSING",
        ),
        _check(
            "operation_admitted_true",
            _execution_bool(selected_execution_result, "operation_admitted"),
            True,
            _execution_bool(selected_execution_result, "operation_admitted"),
            "OPERATION_NOT_ADMITTED",
        ),
        _check(
            "one_bounded_operation_context_admitted_true",
            _execution_bool(
                selected_execution_result, "one_bounded_operation_context_admitted"
            ),
            True,
            _execution_bool(
                selected_execution_result, "one_bounded_operation_context_admitted"
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
            "proposed_output_family_named_but_not_emitted",
            _is_present(proposed_output_family),
            "proposed output family named but not emitted",
            proposed_output_family,
            "PROPOSED_OUTPUT_FAMILY_MISSING",
        ),
        _check(
            "proposed_output_family_not_consequence",
            non_consequence_collapse
            != "ACTION_CONSEQUENCE_REVIEW_TREATS_OUTPUT_AS_CONSEQUENCE",
            "proposed output family is not consequence",
            non_consequence_collapse,
            "ACTION_CONSEQUENCE_REVIEW_TREATS_OUTPUT_AS_CONSEQUENCE",
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
            "action_consequence_scope_declared",
            _is_present(scope_flags.get("selected_action_consequence_scope")),
            "declared action / consequence scope",
            scope_flags.get("selected_action_consequence_scope"),
            "ACTION_CONSEQUENCE_SCOPE_MISSING",
        ),
        _check(
            "action_consequence_scope_supported",
            not unsupported_scope,
            "supported action / consequence scope values only",
            list(unsupported_scope),
            "UNSUPPORTED_ACTION_CONSEQUENCE_SCOPE",
        ),
        _check(
            "no_action_authorized",
            collapsed("ACTION_CONSEQUENCE_REVIEW_AUTHORIZES_ACTION") is None,
            False,
            collapse or execution_collapse,
            "ACTION_CONSEQUENCE_REVIEW_AUTHORIZES_ACTION",
        ),
        _check(
            "no_consequence_created",
            collapsed("ACTION_CONSEQUENCE_REVIEW_CREATES_CONSEQUENCE") is None,
            False,
            collapse or execution_collapse,
            "ACTION_CONSEQUENCE_REVIEW_CREATES_CONSEQUENCE",
        ),
        _check(
            "no_operation_executed",
            collapsed("ACTION_CONSEQUENCE_REVIEW_EXECUTES_OPERATION") is None,
            False,
            collapse or execution_collapse,
            "ACTION_CONSEQUENCE_REVIEW_EXECUTES_OPERATION",
        ),
        _check(
            "no_output_emitted",
            collapsed("ACTION_CONSEQUENCE_REVIEW_EMITS_OUTPUT") is None,
            False,
            collapse or execution_collapse,
            "ACTION_CONSEQUENCE_REVIEW_EMITS_OUTPUT",
        ),
        _check(
            "no_output_evidence_standing_receipt_treated_as_consequence",
            non_consequence_collapse is None,
            "no output/evidence/standing/receipt treated as consequence",
            non_consequence_collapse,
            non_consequence_collapse,
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
            collapsed("ACTION_CONSEQUENCE_REVIEW_CREATES_REUSABLE_PERMISSION") is None,
            False,
            collapse or execution_collapse,
            "ACTION_CONSEQUENCE_REVIEW_CREATES_REUSABLE_PERMISSION",
        ),
        _check(
            "no_autonomous_continuation_authorized",
            collapsed(
                "ACTION_CONSEQUENCE_REVIEW_AUTHORIZES_AUTONOMOUS_CONTINUATION"
            )
            is None,
            False,
            collapse or execution_collapse,
            "ACTION_CONSEQUENCE_REVIEW_AUTHORIZES_AUTONOMOUS_CONTINUATION",
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
            and execution_collapse != "MUTATION_REPLAY_OR_MERGE_DETECTED",
            "no mutation/replay/merge",
            collapse or execution_collapse,
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        ),
        _check(
            "non_claims_remain_false",
            _declared_non_claims_valid(request),
            "all required action / consequence non-claims present and false",
            _declared_non_claims(request),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
    ]
    return checks


def _statement(
    outcome: str,
    request: Mapping[str, Any],
    selected_execution_result: Mapping[str, Any] | None,
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
        "distributed_action_consequence_boundary_recorded": recorded,
        "not_ready": outcome == OUTCOME_NOT_READY,
        "requires_additional_basis": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "selected_execution_emission_result_preserved": passed(
            "selected_execution_emission_result_present"
        ),
        "selected_execution_emission_result_recorded": passed(
            "selected_execution_emission_result_outcome_recorded"
        ),
        "selected_execution_emission_result_failed_check_count_zero": passed(
            "selected_execution_emission_result_failed_check_count_zero"
        ),
        "selected_admission_transition_result_preserved": passed(
            "selected_admission_transition_result_preserved"
        ),
        "selected_admitted_operation_context_preserved": passed(
            "selected_admitted_operation_context_preserved"
        ),
        "operation_admitted": _execution_bool(
            selected_execution_result, "operation_admitted"
        ),
        "one_bounded_operation_context_admitted": _execution_bool(
            selected_execution_result, "one_bounded_operation_context_admitted"
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
        "proposed_output_family_named": passed(
            "proposed_output_family_named_but_not_emitted"
        ),
        "proposed_output_family_emitted": False,
        "output_family_is_not_consequence": passed(
            "proposed_output_family_not_consequence"
        ),
        "carrier_evidence_is_not_consequence": passed(
            "no_output_evidence_standing_receipt_treated_as_consequence"
        ),
        "standing_is_not_consequence": passed(
            "no_output_evidence_standing_receipt_treated_as_consequence"
        ),
        "receipt_is_not_consequence": passed(
            "no_output_evidence_standing_receipt_treated_as_consequence"
        ),
        "receipt_exhaustion_requirement_present": passed(
            "receipt_exhaustion_requirement_present"
        ),
        "action_consequence_separation_present": passed(
            "action_consequence_separation_present"
        ),
        "action_consequence_scope_supported": passed(
            "action_consequence_scope_supported"
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
    intent = request.get("action_consequence_intent")
    if load_block_code:
        return OUTCOME_BLOCKED, load_block_code
    if intent == INTENT_BLOCK:
        return OUTCOME_BLOCKED, "ACTION_CONSEQUENCE_REVIEW_REQUEST_EXPLICITLY_BLOCKED"

    first_failed = _first_failed_code(checks)
    if first_failed:
        return OUTCOME_BLOCKED, first_failed

    requested = request.get("requested_action_consequence_outcome", OUTCOME_RECORDED)
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
    return OUTCOME_BLOCKED, "ACTION_CONSEQUENCE_INTENT_UNSUPPORTED"


def _metadata(request: Mapping[str, Any]) -> dict[str, Any]:
    request_id = str(request.get("action_consequence_request_id") or "unidentified")
    result_id = f"{RESULT_ID_PREFIX}__{_sanitize_filename(request_id)}"
    return {
        "distributed_action_consequence_result_id": result_id,
        "distributed_action_consequence_result_type": RESULT_TYPE,
        "distributed_action_consequence_result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
    }


def _assemble_result(
    request: Mapping[str, Any],
    selected_execution_result: Mapping[str, Any] | None,
    selected_execution_path: str | None,
    load_block_code: str | None,
    load_block_reason: str | None,
) -> dict[str, Any]:
    selected_admission_transition_result = _selected_admission_transition_result(
        request, selected_execution_result
    )
    selected_operation_context = _selected_operation_context(
        request, selected_execution_result
    )
    selected_refusal_abort_result = _selected_refusal_abort_result(
        request, selected_execution_result
    )
    selected_sync_non_sync_result = _selected_sync_non_sync_result(
        request, selected_execution_result
    )
    selected_carrier_role_result = _selected_carrier_role_result(
        request, selected_execution_result
    )
    selected_source_body_authority_result = _selected_source_body_authority_result(
        request, selected_execution_result
    )
    selected_eligibility_result = _selected_eligibility_result(
        request, selected_execution_result
    )
    selected_matter_declaration = _selected_matter_declaration(
        request, selected_execution_result
    )
    selected_operation_candidate = _selected_operation_candidate(
        request, selected_execution_result
    )
    selected_operation_matter = _selected_operation_matter(
        request, selected_execution_result
    )
    scope_values, scope_flags, unsupported_scope = _normalize_scope(
        request.get("action_consequence_scope")
    )

    checks = _build_checks(
        request,
        selected_execution_result,
        selected_admission_transition_result,
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
        "distributed_action_consequence_metadata": _metadata(request),
        "declared_action_consequence_question": _build_declared_question_section(
            request, selected_execution_result, selected_execution_path
        ),
        "selected_execution_emission_result": _build_selected_execution_section(
            request, selected_execution_result, selected_execution_path
        ),
        "selected_operation_context": _build_selected_operation_context_section(
            selected_execution_result,
            selected_admission_transition_result,
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
        "action_consequence_basis": _build_action_consequence_basis_section(
            request,
            selected_execution_result,
            selected_admission_transition_result,
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
        "action_consequence_scope": scope_flags,
        "action_consequence_checks": checks,
        "action_consequence_statement": _statement(
            outcome, request, selected_execution_result, checks, block_code
        ),
        "action_consequence_non_meaning": _non_meaning(),
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
    result["distributed_action_consequence_summary"] = (
        build_distributed_action_consequence_summary(result)
    )
    return result


def _minimal_blocked_result(
    block_code: str,
    block_reason: str | None = None,
    request_path: str | None = None,
) -> dict[str, Any]:
    request = {
        "action_consequence_request_id": "blocked_request",
        "action_consequence_request_path": request_path,
        "action_consequence_question": None,
        "action_consequence_intent": None,
        "requested_action_consequence_outcome": OUTCOME_BLOCKED,
        "declared_non_claims": {key: False for key in REQUIRED_NON_CLAIMS},
    }
    result = _assemble_result(request, None, None, block_code, block_reason)
    result["block"]["block_code"] = block_code
    result["block"]["block_reason"] = _block_reason(block_code, block_reason)
    result["action_consequence_statement"]["block_code"] = block_code
    result["action_consequence_statement"]["block_reason"] = _block_reason(
        block_code, block_reason
    )
    result["distributed_action_consequence_summary"] = (
        build_distributed_action_consequence_summary(result)
    )
    return result


def resolve_distributed_action_consequence_boundary(
    declared_action_consequence_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one declared distributed action / consequence boundary request."""

    if declared_action_consequence_request is None:
        request = {
            "action_consequence_request_id": "missing_request",
            "action_consequence_question": None,
            "action_consequence_intent": None,
            "declared_non_claims": {key: False for key in REQUIRED_NON_CLAIMS},
        }
        return _assemble_result(request, None, None, None, None)

    if not isinstance(declared_action_consequence_request, Mapping):
        return _minimal_blocked_result(
            "DECLARED_ACTION_CONSEQUENCE_REQUEST_MALFORMED",
            BLOCK_REASON_BY_CODE["DECLARED_ACTION_CONSEQUENCE_REQUEST_MALFORMED"],
        )

    request = _deepcopy(dict(declared_action_consequence_request))
    selected_execution_result, load_block_code, load_block_reason, selected_path = (
        _load_selected_execution_result(request)
    )
    return _assemble_result(
        request,
        selected_execution_result,
        selected_path,
        load_block_code,
        load_block_reason,
    )


def resolve_distributed_action_consequence_boundary_from_path(
    declared_action_consequence_request_path: Path | str,
) -> dict:
    """Resolve one declared distributed action / consequence request JSON file."""

    return _load_request_path(declared_action_consequence_request_path)


def build_distributed_action_consequence_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a bounded summary from a distributed action / consequence result."""

    statement = result.get("action_consequence_statement", {})
    if not isinstance(statement, Mapping):
        statement = {}
    declared = result.get("declared_action_consequence_question", {})
    if not isinstance(declared, Mapping):
        declared = {}
    selected = result.get("selected_execution_emission_result", {})
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
        "action_consequence_request_id": declared.get("action_consequence_request_id"),
        "action_consequence_question": declared.get("action_consequence_question"),
        "action_consequence_intent": declared.get("action_consequence_intent"),
        "selected_execution_emission_result_id": selected.get(
            "selected_execution_emission_result_id"
        ),
        "selected_execution_emission_result_outcome": selected.get(
            "selected_execution_emission_result_outcome"
        ),
        "selected_operation_candidate_id": selected_context.get(
            "selected_operation_candidate_id"
        ),
        "selected_operation_matter_id": selected_context.get(
            "selected_operation_matter_id"
        ),
        "passed_check_count": statement.get("passed_check_count", 0),
        "failed_check_count": statement.get("failed_check_count", 0),
        "distributed_action_consequence_boundary_recorded": statement.get(
            "distributed_action_consequence_boundary_recorded", False
        ),
        "not_ready": result.get("outcome") == OUTCOME_NOT_READY,
        "requires_additional_basis": result.get("outcome")
        == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "selected_execution_emission_result_preserved": statement.get(
            "selected_execution_emission_result_preserved", False
        ),
        "selected_execution_emission_result_recorded": statement.get(
            "selected_execution_emission_result_recorded", False
        ),
        "selected_execution_emission_result_failed_check_count_zero": statement.get(
            "selected_execution_emission_result_failed_check_count_zero", False
        ),
        "selected_admission_transition_result_preserved": statement.get(
            "selected_admission_transition_result_preserved", False
        ),
        "selected_admitted_operation_context_preserved": statement.get(
            "selected_admitted_operation_context_preserved", False
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
        "proposed_output_family_named_but_not_emitted": (
            statement.get("proposed_output_family_named", False)
            and statement.get("proposed_output_family_emitted") is False
        ),
        "output_family_is_not_consequence": statement.get(
            "output_family_is_not_consequence", False
        ),
        "carrier_evidence_is_not_consequence": statement.get(
            "carrier_evidence_is_not_consequence", False
        ),
        "standing_is_not_consequence": statement.get(
            "standing_is_not_consequence", False
        ),
        "receipt_is_not_consequence": statement.get(
            "receipt_is_not_consequence", False
        ),
        "receipt_exhaustion_requirement_present": statement.get(
            "receipt_exhaustion_requirement_present", False
        ),
        "action_consequence_separation_present": statement.get(
            "action_consequence_separation_present", False
        ),
        "action_consequence_scope_supported": statement.get(
            "action_consequence_scope_supported", False
        ),
        "no_action_consequence_execution_emission": all(
            statement.get(key) is False
            for key in (
                "action_authorized",
                "consequence_created",
                "operation_executed",
                "output_emitted",
            )
        ),
        "no_output_evidence_standing_receipt_consequence": all(
            statement.get(key) is False
            for key in (
                "output_treated_as_consequence",
                "evidence_treated_as_consequence",
                "standing_treated_as_consequence",
                "receipt_treated_as_consequence",
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
                "action_authorized",
                "consequence_created",
                "operation_executed",
                "output_emitted",
                "output_treated_as_consequence",
                "evidence_treated_as_consequence",
                "standing_treated_as_consequence",
                "receipt_treated_as_consequence",
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
    return sanitized.lower() or "distributed_action_consequence"


def _default_output_path(result: Mapping[str, Any]) -> Path:
    declared = result.get("declared_action_consequence_question", {})
    selected = result.get("selected_execution_emission_result", {})
    metadata = result.get("distributed_action_consequence_metadata", {})
    if not isinstance(declared, Mapping):
        declared = {}
    if not isinstance(selected, Mapping):
        selected = {}
    if not isinstance(metadata, Mapping):
        metadata = {}
    name = _first_present(
        declared.get("action_consequence_request_id"),
        selected.get("selected_execution_emission_result_id"),
        metadata.get("distributed_action_consequence_result_id"),
        "distributed_action_consequence",
    )
    filename = f"{_sanitize_filename(str(name))}__distributed_action_consequence_result.json"
    return DISTRIBUTED_ACTION_CONSEQUENCE_BOUNDARY_ROOT / filename


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


def write_distributed_action_consequence_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write an additive distributed action / consequence boundary artifact."""

    if not isinstance(result, Mapping):
        raise DistributedActionConsequenceBoundaryError(
            "Action / consequence result must be a mapping."
        )
    target = Path(output_path) if output_path is not None else _default_output_path(result)
    target = _deduplicated_path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target


def build_declared_distributed_action_consequence_request(
    action_consequence_request_id: str,
    action_consequence_question: str,
    selected_execution_emission_result: Mapping[str, Any] | str,
    action_consequence_basis: Mapping[str, Any] | str,
    action_consequence_scope: Sequence[str] | Mapping[str, Any],
    action_consequence_intent: str = INTENT_RECORD,
    *,
    selected_execution_emission_result_path: str | None = None,
    selected_execution_emission_result_id: str | None = None,
    selected_execution_emission_result_outcome: str | None = None,
    requested_action_consequence_outcome: str = OUTCOME_RECORDED,
    proposed_action_posture: Mapping[str, Any] | str | None = None,
    proposed_consequence_posture: Mapping[str, Any] | str | None = None,
    additional_basis_context: Mapping[str, Any] | None = None,
    not_ready_reason: str | None = None,
) -> dict:
    """Build a bounded declared action / consequence request."""

    if isinstance(action_consequence_basis, Mapping):
        basis = _deepcopy(dict(action_consequence_basis))
    else:
        basis = {"action_consequence_basis": action_consequence_basis}

    request: dict[str, Any] = {
        "action_consequence_request_id": action_consequence_request_id,
        "action_consequence_question": action_consequence_question,
        "action_consequence_intent": action_consequence_intent,
        "action_consequence_basis": basis,
        "action_consequence_scope": _deepcopy(action_consequence_scope),
        "declared_non_claims": {key: False for key in REQUIRED_NON_CLAIMS},
        "requested_action_consequence_outcome": requested_action_consequence_outcome,
        "proposed_output_family": basis.get(
            "proposed_output_family",
            {"output_family": "bounded_output_family_named_not_consequence"},
        ),
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
                "requirement": "ACTION_CONSEQUENCE_SEPARATION_REQUIRED",
            },
        ),
    }

    if isinstance(selected_execution_emission_result, Mapping):
        request["selected_execution_emission_result"] = _deepcopy(
            dict(selected_execution_emission_result)
        )
    elif selected_execution_emission_result_path is None:
        request["selected_execution_emission_result_path"] = str(
            selected_execution_emission_result
        )
    else:
        request["selected_execution_emission_result"] = selected_execution_emission_result

    if selected_execution_emission_result_path is not None:
        request["selected_execution_emission_result_path"] = (
            selected_execution_emission_result_path
        )
    if selected_execution_emission_result_id is not None:
        request["selected_execution_emission_result_id"] = (
            selected_execution_emission_result_id
        )
    if selected_execution_emission_result_outcome is not None:
        request["selected_execution_emission_result_outcome"] = (
            selected_execution_emission_result_outcome
        )
    if proposed_action_posture is not None:
        request["proposed_action_posture"] = _deepcopy(proposed_action_posture)
    else:
        request["proposed_action_posture"] = basis.get(
            "proposed_action_posture",
            {"action_posture": "action_not_authorized_by_boundary"},
        )
    if proposed_consequence_posture is not None:
        request["proposed_consequence_posture"] = _deepcopy(
            proposed_consequence_posture
        )
    else:
        request["proposed_consequence_posture"] = basis.get(
            "proposed_consequence_posture",
            {"consequence_posture": "consequence_not_created_by_boundary"},
        )
    if additional_basis_context is not None:
        request["additional_basis_context"] = _deepcopy(additional_basis_context)
    if not_ready_reason is not None:
        request["not_ready_reason"] = not_ready_reason

    request["declared_non_claims"]["action_consequence_boundary_recorded"] = (
        requested_action_consequence_outcome == OUTCOME_RECORDED
    )
    return request
