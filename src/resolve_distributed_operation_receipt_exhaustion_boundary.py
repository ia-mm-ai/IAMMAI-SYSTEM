"""Resolve the distributed operation receipt / exhaustion boundary.

This module records boundary-chain receipt / exhaustion accounting only. It
does not claim actual operation receipt, execution receipt, output receipt,
action receipt, consequence receipt, conformance, closure, public readiness,
final completion, reusable permission, autonomous continuation, action,
consequence, execution, emission, synchronization, full body transfer, second
body, or follow-on work.
"""

from __future__ import annotations

import copy
import datetime
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any


class DistributedOperationReceiptExhaustionBoundaryError(Exception):
    """Raised for hard receipt / exhaustion boundary failures."""


RESOLVER_MODULE = "resolve_distributed_operation_receipt_exhaustion_boundary"
RESULT_VERSION = "0.1.0"
RESULT_TYPE = "distributed_operation_receipt_exhaustion_boundary_result"
RESULT_ID_PREFIX = "distributed_operation_receipt_exhaustion_boundary"

DISTRIBUTED_OPERATION_RECEIPT_EXHAUSTION_BOUNDARY_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_distributed_operation_receipt_exhaustion_boundary"
)

EXPECTED_SELECTED_ACTION_CONSEQUENCE_OUTCOME = (
    "DISTRIBUTED_ACTION_CONSEQUENCE_BOUNDARY_RECORDED"
)

OUTCOME_RECORDED = "DISTRIBUTED_OPERATION_RECEIPT_EXHAUSTION_BOUNDARY_RECORDED"
OUTCOME_NOT_READY = "DISTRIBUTED_OPERATION_RECEIPT_EXHAUSTION_NOT_READY"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "DISTRIBUTED_OPERATION_RECEIPT_EXHAUSTION_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "DISTRIBUTED_OPERATION_RECEIPT_EXHAUSTION_REVIEW_BLOCKED"
OUTCOME_FAMILY = {
    OUTCOME_RECORDED,
    OUTCOME_NOT_READY,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
}

INTENT_RECORD = "RECORD_DISTRIBUTED_OPERATION_RECEIPT_EXHAUSTION_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_DISTRIBUTED_OPERATION_RECEIPT_EXHAUSTION_BOUNDARY"
INTENT_BLOCK = "BLOCK_DISTRIBUTED_OPERATION_RECEIPT_EXHAUSTION_REVIEW"
SUPPORTED_INTENTS = {INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK}

SUPPORTED_RECEIPT_EXHAUSTION_SCOPE = (
    "BOUNDARY_CHAIN_RECEIPT_ONLY",
    "NO_ACTUAL_OPERATION_RECEIPT",
    "NO_EXECUTION_RECEIPT",
    "NO_OUTPUT_RECEIPT",
    "NO_ACTION_RECEIPT",
    "NO_CONSEQUENCE_RECEIPT",
    "NO_CONFORMANCE_CLAIM",
    "NO_CLOSURE_CLAIM",
    "NO_PUBLIC_READINESS_CLAIM",
    "NO_FINAL_COMPLETION_CLAIM",
    "NO_REUSABLE_PERMISSION_REMAINS",
    "NO_AUTONOMOUS_CONTINUATION_AUTHORIZED",
    "FUTURE_EXECUTION_REQUIRES_FRESH_RECEIPT_EXHAUSTION",
    "CONFORMANCE_REQUIRES_SEPARATE_BOUNDARY",
    "CLOSURE_REQUIRES_SEPARATE_BOUNDARY",
)

REQUIRED_NON_CLAIMS = (
    "actual_operation_receipt_recorded",
    "execution_receipt_recorded",
    "output_receipt_recorded",
    "action_receipt_recorded",
    "consequence_receipt_recorded",
    "operation_executed",
    "output_emitted",
    "action_authorized",
    "consequence_created",
    "receipt_treated_as_consequence",
    "conformance_claimed",
    "closure_claimed",
    "public_launch_readiness_created",
    "final_completion_claimed",
    "follow_on_work_authorized",
    "reusable_permission_created",
    "autonomous_continuation_authorized",
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
    "live_operation_refused",
    "live_operation_aborted",
    "refusal_abort_erased",
    "evidence_erased",
    "refusal_erased",
    "blocked_attempt_erased",
    "projection_mismatch_hidden",
    "divergence_resolved",
    "truth_created",
    "self_orientation_successor_scheduled",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
)

COLLAPSE_FIELDS = {
    "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_ACTUAL_OPERATION_RECEIPT": (
        "actual_operation_receipt_recorded",
        "actual_operation_receipt_claimed",
        "operation_receipt_recorded",
        "operation_receipt_claimed",
    ),
    "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_EXECUTION_RECEIPT": (
        "execution_receipt_recorded",
        "execution_receipt_claimed",
        "actual_execution_receipt_recorded",
    ),
    "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_OUTPUT_RECEIPT": (
        "output_receipt_recorded",
        "output_receipt_claimed",
        "emission_receipt_recorded",
        "emitted_output_receipt_recorded",
    ),
    "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_ACTION_RECEIPT": (
        "action_receipt_recorded",
        "action_receipt_claimed",
    ),
    "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_CONSEQUENCE_RECEIPT": (
        "consequence_receipt_recorded",
        "consequence_receipt_claimed",
    ),
    "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_CONFORMANCE": (
        "conformance_claimed",
        "conformance_achieved",
        "operation_conformance_claimed",
    ),
    "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_CLOSURE": (
        "closure_claimed",
        "closure_achieved",
        "operation_closed",
        "operation_closure_claimed",
    ),
    "RECEIPT_EXHAUSTION_REVIEW_TREATS_RECEIPT_AS_CONSEQUENCE": (
        "receipt_treated_as_consequence",
        "receipt_exhaustion_treated_as_consequence",
        "boundary_chain_receipt_treated_as_consequence",
    ),
    "RECEIPT_EXHAUSTION_REVIEW_AUTHORIZES_ACTION": (
        "action_authorized",
        "action_created",
        "truth_action_created",
        "action_permission_created",
    ),
    "RECEIPT_EXHAUSTION_REVIEW_CREATES_CONSEQUENCE": (
        "consequence_created",
        "consequence_action_created",
        "operation_consequence_created",
    ),
    "RECEIPT_EXHAUSTION_REVIEW_EXECUTES_OPERATION": (
        "operation_executed",
        "operation_execution_started",
        "distributed_operation_executed",
    ),
    "RECEIPT_EXHAUSTION_REVIEW_EMITS_OUTPUT": (
        "output_emitted",
        "emission_created",
        "operation_output_emitted",
        "output_generated",
        "proposed_output_family_emitted",
    ),
    "RECEIPT_EXHAUSTION_REVIEW_AUTHORIZES_SYNCHRONIZATION": (
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
    "RECEIPT_EXHAUSTION_REVIEW_AUTHORIZES_NON_SYNCHRONIZED_OPERATION": (
        "non_synchronized_operation_authorized",
        "non_sync_operation_authorized",
        "carrier_autonomy_authorized",
        "stale_carrier_operation_authorized",
        "divergent_live_operation_authorized",
        "independent_carrier_operation_authorized",
    ),
    "RECEIPT_EXHAUSTION_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER": (
        "full_body_transfer_authorized",
        "full_body_transfer_created",
    ),
    "RECEIPT_EXHAUSTION_REVIEW_CREATES_SECOND_BODY": (
        "second_body_created",
        "second_body_authorized",
    ),
    "RECEIPT_EXHAUSTION_REVIEW_CREATES_PUBLIC_READINESS": (
        "public_launch_readiness_created",
        "public_readiness_created",
    ),
    "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_FINAL_COMPLETION": (
        "final_completion_claimed",
        "final_governance_completed",
        "final_continuity_completed",
        "final_system_identity_completed",
    ),
    "RECEIPT_EXHAUSTION_REVIEW_SCHEDULES_FOLLOW_ON_WORK": (
        "follow_on_work_authorized",
        "follow_on_work_scheduled",
        "self_orientation_successor_scheduled",
    ),
    "RECEIPT_EXHAUSTION_REVIEW_CREATES_REUSABLE_PERMISSION": (
        "reusable_permission_created",
        "permission_created",
        "standing_permission_created",
    ),
    "RECEIPT_EXHAUSTION_REVIEW_AUTHORIZES_AUTONOMOUS_CONTINUATION": (
        "autonomous_continuation_authorized",
        "continuation_authorized",
        "autonomous_operation_authorized",
    ),
    "RECEIPT_EXHAUSTION_REVIEW_ERASES_REFUSAL_ABORT": (
        "refusal_abort_erased",
        "refusal_abort_conditions_erased",
        "non_admission_conditions_erased",
        "abort_conditions_erased",
    ),
    "RECEIPT_EXHAUSTION_REVIEW_ERASES_EVIDENCE_OR_REFUSAL": (
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
    "RECEIPT_EXHAUSTION_REVIEW_RESOLVES_DIVERGENCE": (
        "divergence_resolved",
    ),
    "MUTATION_REPLAY_OR_MERGE_DETECTED": (
        "mutation_performed",
        "replay_performed",
        "merge_performed",
    ),
}

BLOCK_REASON_BY_CODE = {
    "DECLARED_RECEIPT_EXHAUSTION_REQUEST_MALFORMED": (
        "Declared receipt / exhaustion request is not a mapping."
    ),
    "DECLARED_RECEIPT_EXHAUSTION_REQUEST_UNREADABLE": (
        "Declared receipt / exhaustion request path is unreadable."
    ),
    "RECEIPT_EXHAUSTION_REVIEW_REQUEST_EXPLICITLY_BLOCKED": (
        "Declared receipt / exhaustion request explicitly blocks review."
    ),
    "RECEIPT_EXHAUSTION_QUESTION_UNDECLARED": (
        "Receipt / exhaustion question is undeclared."
    ),
    "RECEIPT_EXHAUSTION_INTENT_UNSUPPORTED": (
        "Receipt / exhaustion intent is unsupported."
    ),
    "ACTION_CONSEQUENCE_RESULT_MISSING": (
        "Selected action / consequence result is missing."
    ),
    "ACTION_CONSEQUENCE_RESULT_UNREADABLE": (
        "Selected action / consequence result path is unreadable."
    ),
    "ACTION_CONSEQUENCE_RESULT_MALFORMED": (
        "Selected action / consequence result is malformed."
    ),
    "ACTION_CONSEQUENCE_RESULT_OUTCOME_MISSING": (
        "Selected action / consequence result outcome is missing."
    ),
    "ACTION_CONSEQUENCE_RESULT_NOT_RECORDED": (
        "Selected action / consequence result is not recorded."
    ),
    "ACTION_CONSEQUENCE_RESULT_HAS_FAILED_CHECKS": (
        "Selected action / consequence result has failed checks."
    ),
    "EXECUTION_EMISSION_RESULT_MISSING": (
        "Selected execution / emission result is missing."
    ),
    "ADMISSION_TRANSITION_RESULT_MISSING": (
        "Selected admission / transition result is missing."
    ),
    "ADMITTED_OPERATION_CONTEXT_MISSING": (
        "Selected admitted operation context is missing."
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
    "SELECTED_ELIGIBILITY_RESULT_MISSING": "Selected eligibility result is missing.",
    "SELECTED_MATTER_DECLARATION_MISSING": (
        "Selected matter declaration is missing."
    ),
    "SELECTED_OPERATION_CANDIDATE_MISSING": (
        "Selected operation candidate is missing."
    ),
    "SELECTED_OPERATION_MATTER_MISSING": "Selected operation matter is missing.",
    "RECEIPT_EXHAUSTION_SCOPE_MISSING": (
        "Declared receipt / exhaustion scope is missing."
    ),
    "CONFORMANCE_DEPENDENCY_MISSING": "Conformance dependency is missing.",
    "CLOSURE_DEPENDENCY_MISSING": "Closure dependency is missing.",
    "UNSUPPORTED_RECEIPT_EXHAUSTION_SCOPE": (
        "Receipt / exhaustion scope contains an unsupported value."
    ),
    "NON_CLAIM_MISSING_OR_FLIPPED": (
        "A required receipt / exhaustion non-claim is missing or true."
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
            "DECLARED_RECEIPT_EXHAUSTION_REQUEST_UNREADABLE",
            detail
            or BLOCK_REASON_BY_CODE[
                "DECLARED_RECEIPT_EXHAUSTION_REQUEST_UNREADABLE"
            ],
            request_path=str(path),
        )
    if error == "malformed":
        return _minimal_blocked_result(
            "DECLARED_RECEIPT_EXHAUSTION_REQUEST_MALFORMED",
            detail or "Declared receipt / exhaustion request JSON is malformed.",
            request_path=str(path),
        )
    assert payload is not None
    request = _deepcopy(payload)
    request["receipt_exhaustion_request_path"] = str(path)
    return resolve_distributed_operation_receipt_exhaustion_boundary(request)


def _load_selected_action_result(
    request: Mapping[str, Any],
) -> tuple[dict[str, Any] | None, str | None, str | None, str | None]:
    result_path = request.get("selected_action_consequence_result_path")
    if _is_present(result_path):
        payload, error, detail = _read_json_object(str(result_path))
        if error == "unreadable":
            return (
                None,
                "ACTION_CONSEQUENCE_RESULT_UNREADABLE",
                detail or "Selected action / consequence result path is unreadable.",
                str(result_path),
            )
        if error == "malformed":
            return (
                None,
                "ACTION_CONSEQUENCE_RESULT_MALFORMED",
                detail or "Selected action / consequence result is malformed.",
                str(result_path),
            )
        assert payload is not None
        return _deepcopy(payload), None, None, str(result_path)

    selected = request.get("selected_action_consequence_result")
    if not _is_present(selected):
        return None, None, None, None
    if not isinstance(selected, Mapping):
        return (
            None,
            "ACTION_CONSEQUENCE_RESULT_MALFORMED",
            "Selected action / consequence result is not a mapping.",
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
        "distributed_action_consequence_summary",
        "action_consequence_statement",
        "summary",
        "statement",
    ):
        value = _get_path(result, (section, "failed_check_count"))
        if isinstance(value, int):
            return value
    checks = result.get("action_consequence_checks")
    if isinstance(checks, Sequence) and not isinstance(checks, (str, bytes, bytearray)):
        return sum(
            1
            for check in checks
            if isinstance(check, Mapping) and check.get("passed") is not True
        )
    return None


def _extract_action_result_id(result: Any) -> str | None:
    return _first_present(
        _get_path(
            result,
            (
                "distributed_action_consequence_metadata",
                "distributed_action_consequence_result_id",
            ),
        ),
        _get_path(result, ("metadata", "result_id")),
        _find_first_present(
            result,
            (
                "distributed_action_consequence_result_id",
                "action_consequence_result_id",
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
    summary = _get_path(result, ("distributed_action_consequence_summary", "outcome"))
    if isinstance(summary, str) and summary:
        return summary
    return None


def _action_statement(result: Any) -> Mapping[str, Any]:
    if not isinstance(result, Mapping):
        return {}
    statement = result.get("action_consequence_statement")
    return statement if isinstance(statement, Mapping) else {}


def _action_summary(result: Any) -> Mapping[str, Any]:
    if not isinstance(result, Mapping):
        return {}
    summary = result.get("distributed_action_consequence_summary")
    return summary if isinstance(summary, Mapping) else {}


def _action_non_claims(result: Any) -> Mapping[str, Any]:
    if not isinstance(result, Mapping):
        return {}
    non_claims = result.get("non_claims")
    return non_claims if isinstance(non_claims, Mapping) else {}


def _action_bool(result: Any, key: str) -> bool:
    statement = _action_statement(result)
    summary = _action_summary(result)
    non_claims = _action_non_claims(result)
    return (
        statement.get(key) is True
        or summary.get(key) is True
        or non_claims.get(key) is True
        or (isinstance(result, Mapping) and result.get(key) is True)
    )


def _action_no_true(result: Any, key: str) -> bool:
    return not _action_bool(result, key)


def _basis(request: Mapping[str, Any]) -> Mapping[str, Any]:
    basis = request.get("receipt_exhaustion_basis")
    return basis if isinstance(basis, Mapping) else {}


def _selected_from_request_basis_action(
    request: Mapping[str, Any],
    action_result: Mapping[str, Any] | None,
    key: str,
    action_paths: Sequence[Sequence[str]],
) -> Any:
    basis = _basis(request)
    value = _first_present(request.get(key), basis.get(key))
    if _is_present(value):
        return _deepcopy(value)
    if action_result is not None:
        for path in action_paths:
            found = _get_path(action_result, path)
            if _is_present(found):
                return _deepcopy(found)
    return None


def _selected_execution_emission_result(
    request: Mapping[str, Any],
    action_result: Mapping[str, Any] | None,
) -> Any:
    return _selected_from_request_basis_action(
        request,
        action_result,
        "selected_execution_emission_result",
        (
            ("selected_operation_context", "selected_execution_emission_result"),
            ("action_consequence_basis", "selected_execution_emission_result"),
            ("selected_execution_emission_result", "selected_execution_emission_result"),
            ("selected_execution_emission_result",),
        ),
    )


def _selected_admission_transition_result(
    request: Mapping[str, Any],
    action_result: Mapping[str, Any] | None,
) -> Any:
    return _selected_from_request_basis_action(
        request,
        action_result,
        "selected_admission_transition_result",
        (
            ("selected_operation_context", "selected_admission_transition_result"),
            ("action_consequence_basis", "selected_admission_transition_result"),
        ),
    )


def _selected_operation_context(
    request: Mapping[str, Any],
    action_result: Mapping[str, Any] | None,
) -> Any:
    basis = _basis(request)
    value = _first_present(
        request.get("selected_operation_context"),
        basis.get("selected_operation_context"),
        _get_path(action_result, ("selected_operation_context", "selected_admitted_operation_context")),
        _get_path(action_result, ("selected_operation_context", "admitted_operation_context")),
        _get_path(action_result, ("action_consequence_basis", "selected_operation_context")),
        _get_path(action_result, ("selected_operation_context",)),
    )
    return _deepcopy(value) if _is_present(value) else None


def _selected_refusal_abort_result(
    request: Mapping[str, Any],
    action_result: Mapping[str, Any] | None,
) -> Any:
    return _selected_from_request_basis_action(
        request,
        action_result,
        "selected_refusal_abort_result",
        (
            ("selected_operation_context", "selected_refusal_abort_result"),
            ("action_consequence_basis", "selected_refusal_abort_result"),
        ),
    )


def _selected_sync_non_sync_result(
    request: Mapping[str, Any],
    action_result: Mapping[str, Any] | None,
) -> Any:
    return _selected_from_request_basis_action(
        request,
        action_result,
        "selected_sync_non_sync_result",
        (
            ("selected_operation_context", "selected_sync_non_sync_result"),
            ("action_consequence_basis", "selected_sync_non_sync_result"),
        ),
    )


def _selected_carrier_role_result(
    request: Mapping[str, Any],
    action_result: Mapping[str, Any] | None,
) -> Any:
    return _selected_from_request_basis_action(
        request,
        action_result,
        "selected_carrier_role_result",
        (
            ("selected_operation_context", "selected_carrier_role_result"),
            ("action_consequence_basis", "selected_carrier_role_result"),
        ),
    )


def _selected_source_body_authority_result(
    request: Mapping[str, Any],
    action_result: Mapping[str, Any] | None,
) -> Any:
    return _selected_from_request_basis_action(
        request,
        action_result,
        "selected_source_body_authority_result",
        (
            ("selected_operation_context", "selected_source_body_authority_result"),
            ("action_consequence_basis", "selected_source_body_authority_result"),
        ),
    )


def _selected_eligibility_result(
    request: Mapping[str, Any],
    action_result: Mapping[str, Any] | None,
) -> Any:
    return _selected_from_request_basis_action(
        request,
        action_result,
        "selected_eligibility_result",
        (
            ("selected_operation_context", "selected_eligibility_result"),
            ("action_consequence_basis", "selected_eligibility_result"),
        ),
    )


def _selected_matter_declaration(
    request: Mapping[str, Any],
    action_result: Mapping[str, Any] | None,
) -> Any:
    return _selected_from_request_basis_action(
        request,
        action_result,
        "selected_matter_declaration",
        (
            ("selected_operation_context", "selected_matter_declaration"),
            ("action_consequence_basis", "selected_matter_declaration"),
        ),
    )


def _selected_operation_candidate(
    request: Mapping[str, Any],
    action_result: Mapping[str, Any] | None,
) -> Any:
    return _selected_from_request_basis_action(
        request,
        action_result,
        "selected_operation_candidate",
        (
            ("selected_operation_context", "selected_operation_candidate"),
            ("action_consequence_basis", "selected_operation_candidate"),
        ),
    )


def _selected_operation_matter(
    request: Mapping[str, Any],
    action_result: Mapping[str, Any] | None,
) -> Any:
    return _selected_from_request_basis_action(
        request,
        action_result,
        "selected_operation_matter",
        (
            ("selected_operation_context", "selected_operation_matter"),
            ("action_consequence_basis", "selected_operation_matter"),
        ),
    )


def _basis_value(
    request: Mapping[str, Any],
    action_result: Mapping[str, Any] | None,
    key: str,
) -> Any:
    basis = _basis(request)
    return _first_present(
        request.get(key),
        basis.get(key),
        _get_path(action_result, ("action_consequence_basis", key)),
        _get_path(action_result, ("selected_operation_context", key)),
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
        values = scope.get("selected_receipt_exhaustion_scope")
        if values is None:
            values = scope.get("receipt_exhaustion_scope")
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
        value for value in selected if value not in SUPPORTED_RECEIPT_EXHAUSTION_SCOPE
    ]
    selected_set = set(selected)
    flags = {
        "selected_receipt_exhaustion_scope": selected,
        "supported_receipt_exhaustion_scope": list(SUPPORTED_RECEIPT_EXHAUSTION_SCOPE),
        "unsupported_receipt_exhaustion_scope": unsupported,
        "all_selected_receipt_exhaustion_scope_supported": not unsupported,
        "boundary_chain_receipt_only": "BOUNDARY_CHAIN_RECEIPT_ONLY" in selected_set,
        "no_actual_operation_receipt": "NO_ACTUAL_OPERATION_RECEIPT" in selected_set,
        "no_execution_receipt": "NO_EXECUTION_RECEIPT" in selected_set,
        "no_output_receipt": "NO_OUTPUT_RECEIPT" in selected_set,
        "no_action_receipt": "NO_ACTION_RECEIPT" in selected_set,
        "no_consequence_receipt": "NO_CONSEQUENCE_RECEIPT" in selected_set,
        "no_conformance_claim": "NO_CONFORMANCE_CLAIM" in selected_set,
        "no_closure_claim": "NO_CLOSURE_CLAIM" in selected_set,
        "no_public_readiness_claim": "NO_PUBLIC_READINESS_CLAIM" in selected_set,
        "no_final_completion_claim": "NO_FINAL_COMPLETION_CLAIM" in selected_set,
        "no_reusable_permission_remains": (
            "NO_REUSABLE_PERMISSION_REMAINS" in selected_set
        ),
        "no_autonomous_continuation_authorized": (
            "NO_AUTONOMOUS_CONTINUATION_AUTHORIZED" in selected_set
        ),
        "future_execution_requires_fresh_receipt_exhaustion": (
            "FUTURE_EXECUTION_REQUIRES_FRESH_RECEIPT_EXHAUSTION" in selected_set
        ),
        "conformance_requires_separate_boundary": (
            "CONFORMANCE_REQUIRES_SEPARATE_BOUNDARY" in selected_set
        ),
        "closure_requires_separate_boundary": (
            "CLOSURE_REQUIRES_SEPARATE_BOUNDARY" in selected_set
        ),
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
    status = non_claims.get("receipt_exhaustion_boundary_recorded")
    requested = request.get("requested_receipt_exhaustion_outcome", OUTCOME_RECORDED)
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
    scope = request.get("receipt_exhaustion_scope")
    if isinstance(scope, Mapping):
        candidates.append(scope)

    for code, fields in COLLAPSE_FIELDS.items():
        for candidate in candidates:
            if _contains_true(candidate, fields):
                return code
    return None


def _action_result_collapse_code(
    action_result: Mapping[str, Any] | None,
) -> str | None:
    if not isinstance(action_result, Mapping):
        return None
    statement = _action_statement(action_result)
    summary = _action_summary(action_result)
    non_claims = _action_non_claims(action_result)
    basis = action_result.get("action_consequence_basis")
    candidates: list[Mapping[str, Any]] = [
        action_result,
        statement,
        summary,
        non_claims,
    ]
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
    non_claims["receipt_exhaustion_boundary_recorded"] = outcome == OUTCOME_RECORDED
    return non_claims


def _non_meaning() -> dict[str, bool]:
    meanings = {
        "actual_operation_receipt_recorded": True,
        "operation_executed": True,
        "output_emitted": True,
        "action_authorized": True,
        "consequence_created": True,
        "execution_receipt_recorded": True,
        "output_receipt_recorded": True,
        "action_receipt_recorded": True,
        "consequence_receipt_recorded": True,
        "receipt_treated_as_consequence": True,
        "conformance_achieved": True,
        "closure_achieved": True,
        "public_readiness_created": True,
        "final_completion_claimed": True,
        "follow_on_work_authorized": True,
        "reusable_permission_created": True,
        "autonomous_continuation_authorized": True,
        "repository_synchronization_authorized": True,
        "non_synchronized_operation_authorized": True,
        "full_body_transfer_authorized": True,
        "second_body_created": True,
        "divergence_resolved": True,
        "evidence_erased": True,
        "refusal_erased": True,
        "blocked_attempt_erased": True,
        "projection_mismatch_hidden": True,
    }
    meanings.update({f"does_not_mean_{key}": value for key, value in meanings.items()})
    return meanings


def _what_remains_open() -> dict[str, bool]:
    return {
        "distributed_operation_conformance": True,
        "distributed_operation_closure": True,
        "distributed_operation_itself": True,
        "actual_operation_execution": True,
        "actual_output_emission": True,
        "action_authorization": True,
        "consequence_creation": True,
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


def _context(
    request: Mapping[str, Any],
    action_result: Mapping[str, Any] | None,
    selected_path: str | None,
) -> dict[str, Any]:
    selected_execution = _selected_execution_emission_result(request, action_result)
    selected_admission = _selected_admission_transition_result(request, action_result)
    selected_operation_context = _selected_operation_context(request, action_result)
    selected_refusal_abort = _selected_refusal_abort_result(request, action_result)
    selected_sync_non_sync = _selected_sync_non_sync_result(request, action_result)
    selected_carrier_role = _selected_carrier_role_result(request, action_result)
    selected_authority = _selected_source_body_authority_result(request, action_result)
    selected_eligibility = _selected_eligibility_result(request, action_result)
    selected_matter_declaration = _selected_matter_declaration(request, action_result)
    selected_candidate = _selected_operation_candidate(request, action_result)
    selected_matter = _selected_operation_matter(request, action_result)
    scope_source = _first_present(
        request.get("receipt_exhaustion_scope"),
        _basis(request).get("declared_receipt_exhaustion_scope"),
        _basis(request).get("receipt_exhaustion_scope"),
    )
    selected_scope, scope_flags, unsupported_scope = _normalize_scope(scope_source)
    selected_action_scope = _first_present(
        request.get("selected_action_consequence_scope"),
        _basis(request).get("selected_action_consequence_scope"),
        _get_path(action_result, ("action_consequence_scope", "selected_action_consequence_scope")),
        _get_path(action_result, ("action_consequence_basis", "declared_action_consequence_scope")),
    )

    source_maps: list[Mapping[str, Any]] = [
        request,
        _basis(request),
        _action_statement(action_result),
        _action_summary(action_result),
        _action_non_claims(action_result),
    ]
    if isinstance(selected_operation_context, Mapping):
        source_maps.append(selected_operation_context)

    operation_admitted = any(
        mapping.get("operation_admitted") is True for mapping in source_maps
    )
    one_bounded_operation_context_admitted = any(
        mapping.get("one_bounded_operation_context_admitted") is True
        or mapping.get("one_bounded_operation_context_only") is True
        for mapping in source_maps
    )
    action_consequence_boundary_preserved = any(
        mapping.get("distributed_action_consequence_boundary_recorded") is True
        or mapping.get("action_consequence_boundary_recorded") is True
        or mapping.get("action_consequence_boundary_preserved") is True
        for mapping in source_maps
    )

    return {
        "selected_action_consequence_result_id": _first_present(
            request.get("selected_action_consequence_result_id"),
            _extract_action_result_id(action_result),
        ),
        "selected_action_consequence_result_outcome": _first_present(
            request.get("selected_action_consequence_result_outcome"),
            _extract_outcome(action_result),
        ),
        "selected_action_consequence_result_path": selected_path,
        "selected_action_consequence_failed_check_count": _extract_failed_check_count(
            action_result
        ),
        "selected_execution_emission_result": selected_execution,
        "selected_admission_transition_result": selected_admission,
        "selected_operation_context": selected_operation_context,
        "selected_refusal_abort_result": selected_refusal_abort,
        "selected_sync_non_sync_result": selected_sync_non_sync,
        "selected_carrier_role_result": selected_carrier_role,
        "selected_source_body_authority_result": selected_authority,
        "selected_eligibility_result": selected_eligibility,
        "selected_matter_declaration": selected_matter_declaration,
        "selected_operation_candidate": selected_candidate,
        "selected_operation_matter": selected_matter,
        "selected_operation_candidate_id": _operation_candidate_id(selected_candidate),
        "selected_operation_matter_id": _operation_matter_id(selected_matter),
        "selected_action_consequence_scope": _deepcopy(selected_action_scope),
        "proposed_output_family": _basis_value(
            request, action_result, "proposed_output_family"
        ),
        "receipt_exhaustion_requirement": _basis_value(
            request, action_result, "receipt_exhaustion_requirement"
        ),
        "action_consequence_separation_requirement": _basis_value(
            request, action_result, "action_consequence_separation_requirement"
        ),
        "conformance_dependency": _basis_value(
            request, action_result, "conformance_dependency"
        ),
        "closure_dependency": _basis_value(request, action_result, "closure_dependency"),
        "unperformed_non_consequential_posture": _basis_value(
            request, action_result, "unperformed_non_consequential_posture"
        ),
        "exhaustion_accounting_posture": _basis_value(
            request, action_result, "exhaustion_accounting_posture"
        ),
        "selected_receipt_exhaustion_scope": selected_scope,
        "receipt_exhaustion_scope_flags": scope_flags,
        "unsupported_receipt_exhaustion_scope": unsupported_scope,
        "operation_admitted": operation_admitted,
        "one_bounded_operation_context_admitted": (
            one_bounded_operation_context_admitted
        ),
        "action_consequence_boundary_preserved": action_consequence_boundary_preserved,
        "action_result_action_unauthorized": _action_no_true(
            action_result, "action_authorized"
        ),
        "action_result_consequence_uncreated": _action_no_true(
            action_result, "consequence_created"
        ),
        "action_result_operation_unexecuted": _action_no_true(
            action_result, "operation_executed"
        ),
        "action_result_output_unemitted": _action_no_true(action_result, "output_emitted"),
        "output_evidence_standing_receipt_non_consequence": (
            _action_no_true(action_result, "output_treated_as_consequence")
            and _action_no_true(action_result, "evidence_treated_as_consequence")
            and _action_no_true(action_result, "standing_treated_as_consequence")
            and _action_no_true(action_result, "receipt_treated_as_consequence")
        ),
    }


def _build_checks(
    request: Mapping[str, Any],
    action_result: Mapping[str, Any] | None,
    load_code: str | None,
    context: Mapping[str, Any],
) -> list[dict[str, Any]]:
    question = request.get("receipt_exhaustion_question")
    intent = request.get("receipt_exhaustion_intent")
    selected_outcome = context.get("selected_action_consequence_result_outcome")
    failed_count = context.get("selected_action_consequence_failed_check_count")
    selected_scope = context.get("selected_receipt_exhaustion_scope")
    unsupported_scope = context.get("unsupported_receipt_exhaustion_scope") or []
    request_collapse_code = _collapse_code(request)
    action_collapse_code = _action_result_collapse_code(action_result)
    collapse_code = request_collapse_code or action_collapse_code

    checks = [
        _check(
            "receipt / exhaustion question declared",
            _is_present(question),
            "declared receipt / exhaustion question",
            question,
            "RECEIPT_EXHAUSTION_QUESTION_UNDECLARED",
        ),
        _check(
            "receipt / exhaustion intent supported",
            intent in SUPPORTED_INTENTS,
            sorted(SUPPORTED_INTENTS),
            intent,
            "RECEIPT_EXHAUSTION_INTENT_UNSUPPORTED",
        ),
        _check(
            "receipt / exhaustion review not explicitly blocked",
            intent != INTENT_BLOCK,
            "not BLOCK_DISTRIBUTED_OPERATION_RECEIPT_EXHAUSTION_REVIEW",
            intent,
            "RECEIPT_EXHAUSTION_REVIEW_REQUEST_EXPLICITLY_BLOCKED",
        ),
        _check(
            "selected action / consequence result present",
            action_result is not None and load_code is None,
            "selected action / consequence result mapping",
            "present" if action_result is not None else "missing",
            load_code or "ACTION_CONSEQUENCE_RESULT_MISSING",
        ),
        _check(
            "selected action / consequence result outcome declared",
            _is_present(selected_outcome),
            "selected action / consequence outcome declared",
            selected_outcome,
            "ACTION_CONSEQUENCE_RESULT_OUTCOME_MISSING",
        ),
        _check(
            "selected action / consequence result outcome recorded",
            selected_outcome == EXPECTED_SELECTED_ACTION_CONSEQUENCE_OUTCOME,
            EXPECTED_SELECTED_ACTION_CONSEQUENCE_OUTCOME,
            selected_outcome,
            "ACTION_CONSEQUENCE_RESULT_NOT_RECORDED",
        ),
        _check(
            "selected action / consequence result failed check count zero",
            failed_count == 0,
            0,
            failed_count,
            "ACTION_CONSEQUENCE_RESULT_HAS_FAILED_CHECKS",
        ),
        _check(
            "selected execution / emission result preserved",
            _is_present(context.get("selected_execution_emission_result")),
            "selected execution / emission result",
            context.get("selected_execution_emission_result"),
            "EXECUTION_EMISSION_RESULT_MISSING",
        ),
        _check(
            "selected admission / transition result preserved",
            _is_present(context.get("selected_admission_transition_result")),
            "selected admission / transition result",
            context.get("selected_admission_transition_result"),
            "ADMISSION_TRANSITION_RESULT_MISSING",
        ),
        _check(
            "selected admitted operation context preserved",
            _is_present(context.get("selected_operation_context")),
            "selected admitted operation context",
            context.get("selected_operation_context"),
            "ADMITTED_OPERATION_CONTEXT_MISSING",
        ),
        _check(
            "operation admitted true",
            context.get("operation_admitted") is True,
            True,
            context.get("operation_admitted"),
            "OPERATION_NOT_ADMITTED",
        ),
        _check(
            "one bounded operation context admitted true",
            context.get("one_bounded_operation_context_admitted") is True,
            True,
            context.get("one_bounded_operation_context_admitted"),
            "ONE_BOUNDED_OPERATION_CONTEXT_NOT_ADMITTED",
        ),
        _check(
            "selected refusal / abort result preserved",
            _is_present(context.get("selected_refusal_abort_result")),
            "selected refusal / abort result",
            context.get("selected_refusal_abort_result"),
            "REFUSAL_ABORT_RESULT_MISSING",
        ),
        _check(
            "selected sync/non-sync result preserved",
            _is_present(context.get("selected_sync_non_sync_result")),
            "selected sync/non-sync result",
            context.get("selected_sync_non_sync_result"),
            "SYNC_NON_SYNC_RESULT_MISSING",
        ),
        _check(
            "selected carrier role result preserved",
            _is_present(context.get("selected_carrier_role_result")),
            "selected carrier role result",
            context.get("selected_carrier_role_result"),
            "CARRIER_ROLE_RESULT_MISSING",
        ),
        _check(
            "selected source-body authority result preserved",
            _is_present(context.get("selected_source_body_authority_result")),
            "selected source-body authority result",
            context.get("selected_source_body_authority_result"),
            "SOURCE_BODY_AUTHORITY_RESULT_MISSING",
        ),
        _check(
            "selected eligibility result preserved",
            _is_present(context.get("selected_eligibility_result")),
            "selected eligibility result",
            context.get("selected_eligibility_result"),
            "SELECTED_ELIGIBILITY_RESULT_MISSING",
        ),
        _check(
            "selected matter declaration preserved",
            _is_present(context.get("selected_matter_declaration")),
            "selected matter declaration",
            context.get("selected_matter_declaration"),
            "SELECTED_MATTER_DECLARATION_MISSING",
        ),
        _check(
            "selected operation candidate preserved",
            _is_present(context.get("selected_operation_candidate")),
            "selected operation candidate",
            context.get("selected_operation_candidate"),
            "SELECTED_OPERATION_CANDIDATE_MISSING",
        ),
        _check(
            "selected operation matter preserved",
            _is_present(context.get("selected_operation_matter")),
            "selected operation matter",
            context.get("selected_operation_matter"),
            "SELECTED_OPERATION_MATTER_MISSING",
        ),
        _check(
            "action / consequence boundary preserved",
            context.get("action_consequence_boundary_preserved") is True,
            True,
            context.get("action_consequence_boundary_preserved"),
            "ACTION_CONSEQUENCE_RESULT_NOT_RECORDED",
        ),
        _check(
            "action unauthorized",
            context.get("action_result_action_unauthorized") is True,
            False,
            False if context.get("action_result_action_unauthorized") else True,
            "RECEIPT_EXHAUSTION_REVIEW_AUTHORIZES_ACTION",
        ),
        _check(
            "consequence uncreated",
            context.get("action_result_consequence_uncreated") is True,
            False,
            False if context.get("action_result_consequence_uncreated") else True,
            "RECEIPT_EXHAUSTION_REVIEW_CREATES_CONSEQUENCE",
        ),
        _check(
            "operation unexecuted",
            context.get("action_result_operation_unexecuted") is True,
            False,
            False if context.get("action_result_operation_unexecuted") else True,
            "RECEIPT_EXHAUSTION_REVIEW_EXECUTES_OPERATION",
        ),
        _check(
            "output un-emitted",
            context.get("action_result_output_unemitted") is True,
            False,
            False if context.get("action_result_output_unemitted") else True,
            "RECEIPT_EXHAUSTION_REVIEW_EMITS_OUTPUT",
        ),
        _check(
            "output / evidence / standing / receipt non-consequence",
            context.get("output_evidence_standing_receipt_non_consequence") is True,
            "not treated as consequence",
            context.get("output_evidence_standing_receipt_non_consequence"),
            "RECEIPT_EXHAUSTION_REVIEW_TREATS_RECEIPT_AS_CONSEQUENCE",
        ),
        _check(
            "receipt / exhaustion requirement present",
            _is_present(context.get("receipt_exhaustion_requirement")),
            "receipt / exhaustion requirement",
            context.get("receipt_exhaustion_requirement"),
            "RECEIPT_EXHAUSTION_REQUIREMENT_MISSING",
        ),
        _check(
            "conformance dependency present",
            _is_present(context.get("conformance_dependency")),
            "conformance dependency",
            context.get("conformance_dependency"),
            "CONFORMANCE_DEPENDENCY_MISSING",
        ),
        _check(
            "closure dependency present",
            _is_present(context.get("closure_dependency")),
            "closure dependency",
            context.get("closure_dependency"),
            "CLOSURE_DEPENDENCY_MISSING",
        ),
        _check(
            "receipt / exhaustion scope declared",
            bool(selected_scope),
            "declared receipt / exhaustion scope",
            selected_scope,
            "RECEIPT_EXHAUSTION_SCOPE_MISSING",
        ),
        _check(
            "receipt / exhaustion scope supported",
            bool(selected_scope) and not unsupported_scope,
            "all selected scope values supported",
            unsupported_scope,
            "UNSUPPORTED_RECEIPT_EXHAUSTION_SCOPE",
        ),
        _check(
            "no actual operation receipt claimed",
            collapse_code != "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_ACTUAL_OPERATION_RECEIPT",
            False,
            collapse_code == "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_ACTUAL_OPERATION_RECEIPT",
            "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_ACTUAL_OPERATION_RECEIPT",
        ),
        _check(
            "no execution receipt claimed",
            collapse_code != "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_EXECUTION_RECEIPT",
            False,
            collapse_code == "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_EXECUTION_RECEIPT",
            "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_EXECUTION_RECEIPT",
        ),
        _check(
            "no output receipt claimed",
            collapse_code != "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_OUTPUT_RECEIPT",
            False,
            collapse_code == "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_OUTPUT_RECEIPT",
            "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_OUTPUT_RECEIPT",
        ),
        _check(
            "no action receipt claimed",
            collapse_code != "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_ACTION_RECEIPT",
            False,
            collapse_code == "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_ACTION_RECEIPT",
            "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_ACTION_RECEIPT",
        ),
        _check(
            "no consequence receipt claimed",
            collapse_code != "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_CONSEQUENCE_RECEIPT",
            False,
            collapse_code == "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_CONSEQUENCE_RECEIPT",
            "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_CONSEQUENCE_RECEIPT",
        ),
        _check(
            "no conformance claimed",
            collapse_code != "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_CONFORMANCE",
            False,
            collapse_code == "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_CONFORMANCE",
            "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_CONFORMANCE",
        ),
        _check(
            "no closure claimed",
            collapse_code != "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_CLOSURE",
            False,
            collapse_code == "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_CLOSURE",
            "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_CLOSURE",
        ),
        _check(
            "no public readiness / final completion / follow-on work claimed",
            collapse_code
            not in {
                "RECEIPT_EXHAUSTION_REVIEW_CREATES_PUBLIC_READINESS",
                "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_FINAL_COMPLETION",
                "RECEIPT_EXHAUSTION_REVIEW_SCHEDULES_FOLLOW_ON_WORK",
            },
            False,
            collapse_code
            in {
                "RECEIPT_EXHAUSTION_REVIEW_CREATES_PUBLIC_READINESS",
                "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_FINAL_COMPLETION",
                "RECEIPT_EXHAUSTION_REVIEW_SCHEDULES_FOLLOW_ON_WORK",
            },
            collapse_code
            if collapse_code
            in {
                "RECEIPT_EXHAUSTION_REVIEW_CREATES_PUBLIC_READINESS",
                "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_FINAL_COMPLETION",
                "RECEIPT_EXHAUSTION_REVIEW_SCHEDULES_FOLLOW_ON_WORK",
            }
            else "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_FINAL_COMPLETION",
        ),
        _check(
            "no reusable permission created",
            collapse_code != "RECEIPT_EXHAUSTION_REVIEW_CREATES_REUSABLE_PERMISSION",
            False,
            collapse_code == "RECEIPT_EXHAUSTION_REVIEW_CREATES_REUSABLE_PERMISSION",
            "RECEIPT_EXHAUSTION_REVIEW_CREATES_REUSABLE_PERMISSION",
        ),
        _check(
            "no autonomous continuation authorized",
            collapse_code
            != "RECEIPT_EXHAUSTION_REVIEW_AUTHORIZES_AUTONOMOUS_CONTINUATION",
            False,
            collapse_code
            == "RECEIPT_EXHAUSTION_REVIEW_AUTHORIZES_AUTONOMOUS_CONTINUATION",
            "RECEIPT_EXHAUSTION_REVIEW_AUTHORIZES_AUTONOMOUS_CONTINUATION",
        ),
        _check(
            "no mutation/replay/merge",
            collapse_code != "MUTATION_REPLAY_OR_MERGE_DETECTED",
            False,
            collapse_code == "MUTATION_REPLAY_OR_MERGE_DETECTED",
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        ),
        _check(
            "non-claims remain false",
            _declared_non_claims_valid(request),
            "all required receipt / exhaustion non-claims false",
            _declared_non_claims(request),
            collapse_code or "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
    ]

    if collapse_code and all(
        check.get("passed") is True
        for check in checks
        if check["check_name"] != "non-claims remain false"
    ):
        checks.insert(
            -1,
            _check(
                "receipt / exhaustion collapse posture absent",
                False,
                "no collapse posture",
                collapse_code,
                collapse_code,
            ),
        )
    return checks


def _safe_component(value: Any) -> str:
    text = str(value or "receipt_exhaustion_result").strip()
    safe = "".join(char if char.isalnum() or char in "-_." else "_" for char in text)
    return safe.strip("_") or "receipt_exhaustion_result"


def _metadata(request: Mapping[str, Any], context: Mapping[str, Any]) -> dict[str, str]:
    basis = _first_present(
        request.get("receipt_exhaustion_request_id"),
        context.get("selected_action_consequence_result_id"),
        RESULT_ID_PREFIX,
    )
    return {
        "distributed_receipt_exhaustion_result_id": (
            f"{RESULT_ID_PREFIX}__{_safe_component(basis)}"
        ),
        "distributed_receipt_exhaustion_result_type": RESULT_TYPE,
        "distributed_receipt_exhaustion_result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
    }


def _declared_question_section(
    request: Mapping[str, Any],
    context: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "receipt_exhaustion_request_id": request.get("receipt_exhaustion_request_id"),
        "receipt_exhaustion_question": request.get("receipt_exhaustion_question"),
        "receipt_exhaustion_intent": request.get("receipt_exhaustion_intent"),
        "receipt_exhaustion_request_path": request.get("receipt_exhaustion_request_path"),
        "selected_action_consequence_result_id": context.get(
            "selected_action_consequence_result_id"
        ),
        "selected_action_consequence_result_outcome": context.get(
            "selected_action_consequence_result_outcome"
        ),
        "selected_action_consequence_result_path": context.get(
            "selected_action_consequence_result_path"
        ),
        "requested_receipt_exhaustion_outcome": request.get(
            "requested_receipt_exhaustion_outcome", OUTCOME_RECORDED
        ),
        "receipt_exhaustion_boundary_is_not_actual_receipt": True,
        "receipt_exhaustion_boundary_is_not_execution_receipt": True,
        "receipt_exhaustion_boundary_is_not_output_receipt": True,
        "receipt_exhaustion_boundary_is_not_action_receipt": True,
        "receipt_exhaustion_boundary_is_not_consequence_receipt": True,
        "receipt_exhaustion_boundary_is_not_conformance": True,
        "receipt_exhaustion_boundary_is_not_closure": True,
        "receipt_exhaustion_boundary_is_not_public_readiness": True,
        "receipt_exhaustion_boundary_is_not_final_completion": True,
    }


def _selected_action_result_section(
    action_result: Mapping[str, Any] | None,
    context: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "selected_action_consequence_result_id": context.get(
            "selected_action_consequence_result_id"
        ),
        "selected_action_consequence_result_outcome": context.get(
            "selected_action_consequence_result_outcome"
        ),
        "selected_action_consequence_result_path": context.get(
            "selected_action_consequence_result_path"
        ),
        "selected_action_consequence_result_preserved": action_result is not None,
        "selected_action_consequence_result_recorded": (
            context.get("selected_action_consequence_result_outcome")
            == EXPECTED_SELECTED_ACTION_CONSEQUENCE_OUTCOME
        ),
        "selected_action_consequence_result_failed_check_count_zero": (
            context.get("selected_action_consequence_failed_check_count") == 0
        ),
        "selected_action_consequence_boundary_preserved": context.get(
            "action_consequence_boundary_preserved"
        )
        is True,
        "selected_action_consequence_result_did_not_authorize_action": context.get(
            "action_result_action_unauthorized"
        )
        is True,
        "selected_action_consequence_result_did_not_create_consequence": context.get(
            "action_result_consequence_uncreated"
        )
        is True,
        "selected_action_consequence_result_did_not_execute_operation": context.get(
            "action_result_operation_unexecuted"
        )
        is True,
        "selected_action_consequence_result_did_not_emit_output": context.get(
            "action_result_output_unemitted"
        )
        is True,
        "selected_action_consequence_result": _deepcopy(action_result)
        if action_result is not None
        else None,
    }


def _selected_operation_context_section(
    action_result: Mapping[str, Any] | None,
    context: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "selected_action_consequence_result": _deepcopy(action_result)
        if action_result is not None
        else None,
        "selected_execution_emission_result": _deepcopy(
            context.get("selected_execution_emission_result")
        ),
        "selected_admission_transition_result": _deepcopy(
            context.get("selected_admission_transition_result")
        ),
        "selected_admitted_operation_context": _deepcopy(
            context.get("selected_operation_context")
        ),
        "selected_refusal_abort_result": _deepcopy(
            context.get("selected_refusal_abort_result")
        ),
        "selected_sync_non_sync_result": _deepcopy(
            context.get("selected_sync_non_sync_result")
        ),
        "selected_carrier_role_result": _deepcopy(
            context.get("selected_carrier_role_result")
        ),
        "selected_source_body_authority_result": _deepcopy(
            context.get("selected_source_body_authority_result")
        ),
        "selected_eligibility_result": _deepcopy(
            context.get("selected_eligibility_result")
        ),
        "selected_matter_declaration": _deepcopy(
            context.get("selected_matter_declaration")
        ),
        "selected_operation_candidate": _deepcopy(
            context.get("selected_operation_candidate")
        ),
        "selected_operation_matter": _deepcopy(context.get("selected_operation_matter")),
        "operation_admitted": context.get("operation_admitted") is True,
        "one_bounded_operation_context_admitted": context.get(
            "one_bounded_operation_context_admitted"
        )
        is True,
        "action_consequence_boundary_recorded": context.get(
            "action_consequence_boundary_preserved"
        )
        is True,
        "action_authorized": False,
        "consequence_created": False,
        "operation_executed": False,
        "output_emitted": False,
        "actual_operation_receipt_recorded": False,
        "conformance_claimed": False,
        "closure_claimed": False,
    }


def _receipt_exhaustion_basis_section(
    action_result: Mapping[str, Any] | None,
    request: Mapping[str, Any],
    context: Mapping[str, Any],
) -> dict[str, Any]:
    scope_flags = context.get("receipt_exhaustion_scope_flags") or {}
    return {
        "selected_action_consequence_result": _deepcopy(action_result)
        if action_result is not None
        else None,
        "selected_execution_emission_result": _deepcopy(
            context.get("selected_execution_emission_result")
        ),
        "selected_admission_transition_result": _deepcopy(
            context.get("selected_admission_transition_result")
        ),
        "selected_operation_context": _deepcopy(context.get("selected_operation_context")),
        "selected_refusal_abort_result": _deepcopy(
            context.get("selected_refusal_abort_result")
        ),
        "selected_sync_non_sync_result": _deepcopy(
            context.get("selected_sync_non_sync_result")
        ),
        "selected_carrier_role_result": _deepcopy(
            context.get("selected_carrier_role_result")
        ),
        "selected_source_body_authority_result": _deepcopy(
            context.get("selected_source_body_authority_result")
        ),
        "selected_eligibility_result": _deepcopy(
            context.get("selected_eligibility_result")
        ),
        "selected_matter_declaration": _deepcopy(
            context.get("selected_matter_declaration")
        ),
        "selected_operation_candidate": _deepcopy(
            context.get("selected_operation_candidate")
        ),
        "selected_operation_matter": _deepcopy(context.get("selected_operation_matter")),
        "selected_action_consequence_scope": _deepcopy(
            context.get("selected_action_consequence_scope")
        ),
        "proposed_output_family": _deepcopy(context.get("proposed_output_family")),
        "receipt_exhaustion_requirement": _deepcopy(
            context.get("receipt_exhaustion_requirement")
        ),
        "action_consequence_separation_requirement": _deepcopy(
            context.get("action_consequence_separation_requirement")
        ),
        "conformance_dependency": _deepcopy(context.get("conformance_dependency")),
        "closure_dependency": _deepcopy(context.get("closure_dependency")),
        "unperformed_non_consequential_posture": _deepcopy(
            context.get("unperformed_non_consequential_posture")
        ),
        "exhaustion_accounting_posture": _deepcopy(
            context.get("exhaustion_accounting_posture")
        ),
        "declared_receipt_exhaustion_scope": _deepcopy(
            context.get("selected_receipt_exhaustion_scope")
        ),
        "declared_receipt_exhaustion_request_basis": _deepcopy(_basis(request)),
        "boundary_chain_receipt_only": scope_flags.get("boundary_chain_receipt_only")
        is True,
        "no_actual_operation_receipt": scope_flags.get("no_actual_operation_receipt")
        is True,
        "no_execution_receipt": scope_flags.get("no_execution_receipt") is True,
        "no_output_receipt": scope_flags.get("no_output_receipt") is True,
        "no_action_receipt": scope_flags.get("no_action_receipt") is True,
        "no_consequence_receipt": scope_flags.get("no_consequence_receipt") is True,
        "no_conformance_claim": scope_flags.get("no_conformance_claim") is True,
        "no_closure_claim": scope_flags.get("no_closure_claim") is True,
        "no_public_readiness_claim": scope_flags.get("no_public_readiness_claim")
        is True,
        "no_final_completion_claim": scope_flags.get("no_final_completion_claim")
        is True,
        "no_reusable_permission_remains": scope_flags.get(
            "no_reusable_permission_remains"
        )
        is True,
        "no_autonomous_continuation_authorized": scope_flags.get(
            "no_autonomous_continuation_authorized"
        )
        is True,
        "future_execution_requires_fresh_receipt_exhaustion": scope_flags.get(
            "future_execution_requires_fresh_receipt_exhaustion"
        )
        is True,
        "conformance_requires_separate_boundary": scope_flags.get(
            "conformance_requires_separate_boundary"
        )
        is True,
        "closure_requires_separate_boundary": scope_flags.get(
            "closure_requires_separate_boundary"
        )
        is True,
    }


def _additional_basis_section(
    request: Mapping[str, Any],
    outcome: str,
) -> dict[str, Any]:
    context = request.get("additional_basis_context")
    context_mapping = context if isinstance(context, Mapping) else {}
    reason = _first_present(
        request.get("additional_basis_reason"),
        context_mapping.get("reason"),
        context_mapping.get("additional_basis_reason"),
        context_mapping.get("missing_basis_reason"),
    )
    missing_basis = context_mapping.get("missing_basis")
    if isinstance(missing_basis, str):
        missing_basis = [missing_basis]
    if not isinstance(missing_basis, Sequence) or isinstance(
        missing_basis, (str, bytes, bytearray)
    ):
        missing_basis = []
    return {
        "additional_basis_required": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "additional_basis_reason": reason,
        "additional_basis_context": _deepcopy(context_mapping),
        "missing_basis": list(missing_basis),
        "additional_basis_scheduled": False,
        "additional_basis_authorized": False,
        "additional_basis_executed": False,
        "additional_basis_creates_reusable_permission": False,
        "additional_basis_authorizes_autonomous_continuation": False,
        "additional_basis_creates_public_readiness": False,
        "additional_basis_claims_final_completion": False,
        "additional_basis_schedules_follow_on_work": False,
    }


def _statement(
    outcome: str,
    request: Mapping[str, Any],
    context: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    passed_count = sum(1 for check in checks if check.get("passed") is True)
    failed_count = sum(1 for check in checks if check.get("passed") is not True)
    recorded = outcome == OUTCOME_RECORDED
    not_ready = outcome == OUTCOME_NOT_READY
    additional = outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    scope_flags = context.get("receipt_exhaustion_scope_flags") or {}
    return {
        "distributed_operation_receipt_exhaustion_boundary_recorded": recorded,
        "receipt_exhaustion_boundary_recorded": recorded,
        "not_ready": not_ready,
        "requires_additional_basis": additional,
        "not_ready_reason": request.get("not_ready_reason") if not_ready else None,
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "selected_action_consequence_result_preserved": _is_present(
            context.get("selected_action_consequence_result_id")
        ),
        "selected_action_consequence_result_recorded": (
            context.get("selected_action_consequence_result_outcome")
            == EXPECTED_SELECTED_ACTION_CONSEQUENCE_OUTCOME
        ),
        "selected_action_consequence_result_failed_check_count_zero": (
            context.get("selected_action_consequence_failed_check_count") == 0
        ),
        "selected_execution_emission_result_preserved": _is_present(
            context.get("selected_execution_emission_result")
        ),
        "selected_admission_transition_result_preserved": _is_present(
            context.get("selected_admission_transition_result")
        ),
        "selected_admitted_operation_context_preserved": _is_present(
            context.get("selected_operation_context")
        ),
        "operation_admitted": context.get("operation_admitted") is True,
        "one_bounded_operation_context_admitted": context.get(
            "one_bounded_operation_context_admitted"
        )
        is True,
        "selected_refusal_abort_result_preserved": _is_present(
            context.get("selected_refusal_abort_result")
        ),
        "selected_sync_non_sync_result_preserved": _is_present(
            context.get("selected_sync_non_sync_result")
        ),
        "selected_carrier_role_result_preserved": _is_present(
            context.get("selected_carrier_role_result")
        ),
        "selected_source_body_authority_result_preserved": _is_present(
            context.get("selected_source_body_authority_result")
        ),
        "selected_eligibility_result_preserved": _is_present(
            context.get("selected_eligibility_result")
        ),
        "selected_matter_declaration_preserved": _is_present(
            context.get("selected_matter_declaration")
        ),
        "selected_operation_candidate_preserved": _is_present(
            context.get("selected_operation_candidate")
        ),
        "selected_operation_matter_preserved": _is_present(
            context.get("selected_operation_matter")
        ),
        "action_consequence_boundary_preserved": context.get(
            "action_consequence_boundary_preserved"
        )
        is True,
        "action_authorized": False,
        "consequence_created": False,
        "operation_executed": False,
        "output_emitted": False,
        "output_treated_as_consequence": False,
        "evidence_treated_as_consequence": False,
        "standing_treated_as_consequence": False,
        "receipt_treated_as_consequence": False,
        "receipt_exhaustion_requirement_present": _is_present(
            context.get("receipt_exhaustion_requirement")
        ),
        "conformance_dependency_present": _is_present(
            context.get("conformance_dependency")
        ),
        "closure_dependency_present": _is_present(context.get("closure_dependency")),
        "receipt_exhaustion_scope_supported": (
            bool(context.get("selected_receipt_exhaustion_scope"))
            and not context.get("unsupported_receipt_exhaustion_scope")
        ),
        "boundary_chain_receipt_only": scope_flags.get("boundary_chain_receipt_only")
        is True,
        "actual_operation_receipt_recorded": False,
        "execution_receipt_recorded": False,
        "output_receipt_recorded": False,
        "action_receipt_recorded": False,
        "consequence_receipt_recorded": False,
        "conformance_claimed": False,
        "closure_claimed": False,
        "public_launch_readiness_created": False,
        "final_completion_claimed": False,
        "follow_on_work_authorized": False,
        "reusable_permission_created": False,
        "autonomous_continuation_authorized": False,
        "repository_synchronization_authorized": False,
        "shared_live_state_created": False,
        "state_merge_authorized": False,
        "replay_authorized": False,
        "full_body_transfer_authorized": False,
        "second_body_created": False,
        "non_synchronized_operation_authorized": False,
        "carrier_autonomy_authorized": False,
        "stale_carrier_operation_authorized": False,
        "mutation_performed": False,
        "replay_performed": False,
        "merge_performed": False,
    }


def _block_section(code: str | None, reason: str | None) -> dict[str, str | None]:
    return {
        "code": code,
        "reason": reason,
        "block_code": code,
        "block_reason": reason,
    }


def _result_artifact(
    request: Mapping[str, Any],
    action_result: Mapping[str, Any] | None,
    context: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    outcome: str,
    block_code: str | None = None,
    block_reason: str | None = None,
) -> dict[str, Any]:
    result = {
        "distributed_receipt_exhaustion_metadata": _metadata(request, context),
        "declared_receipt_exhaustion_question": _declared_question_section(
            request, context
        ),
        "selected_action_consequence_result": _selected_action_result_section(
            action_result, context
        ),
        "selected_operation_context": _selected_operation_context_section(
            action_result, context
        ),
        "receipt_exhaustion_basis": _receipt_exhaustion_basis_section(
            action_result, request, context
        ),
        "receipt_exhaustion_scope": _deepcopy(
            context.get("receipt_exhaustion_scope_flags", {})
        ),
        "receipt_exhaustion_checks": list(_deepcopy(checks)),
        "receipt_exhaustion_statement": _statement(outcome, request, context, checks),
        "receipt_exhaustion_non_meaning": _non_meaning(),
        "additional_basis_required": _additional_basis_section(request, outcome),
        "what_remains_open": _what_remains_open(),
        "non_claims": _default_non_claims(outcome),
        "outcome": outcome,
        "block": _block_section(block_code, block_reason),
    }
    result["distributed_receipt_exhaustion_summary"] = (
        build_distributed_operation_receipt_exhaustion_summary(result)
    )
    return result


def _minimal_blocked_result(
    code: str,
    reason: str,
    request_path: str | None = None,
) -> dict[str, Any]:
    request: dict[str, Any] = {}
    if request_path is not None:
        request["receipt_exhaustion_request_path"] = request_path
    context: dict[str, Any] = {
        "selected_receipt_exhaustion_scope": [],
        "receipt_exhaustion_scope_flags": _normalize_scope([])[1],
        "unsupported_receipt_exhaustion_scope": [],
    }
    checks = [
        _check(
            "receipt / exhaustion request readable",
            False,
            "readable receipt / exhaustion request mapping",
            reason,
            code,
        )
    ]
    return _result_artifact(
        request,
        None,
        context,
        checks,
        OUTCOME_BLOCKED,
        code,
        reason,
    )


def resolve_distributed_operation_receipt_exhaustion_boundary(
    declared_receipt_exhaustion_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one bounded receipt / exhaustion boundary request."""

    if declared_receipt_exhaustion_request is None:
        return _minimal_blocked_result(
            "RECEIPT_EXHAUSTION_QUESTION_UNDECLARED",
            BLOCK_REASON_BY_CODE["RECEIPT_EXHAUSTION_QUESTION_UNDECLARED"],
        )
    if not isinstance(declared_receipt_exhaustion_request, Mapping):
        return _minimal_blocked_result(
            "DECLARED_RECEIPT_EXHAUSTION_REQUEST_MALFORMED",
            BLOCK_REASON_BY_CODE["DECLARED_RECEIPT_EXHAUSTION_REQUEST_MALFORMED"],
        )

    request = _deepcopy(dict(declared_receipt_exhaustion_request))
    action_result, load_code, load_reason, selected_path = _load_selected_action_result(
        request
    )
    context = _context(request, action_result, selected_path)
    checks = _build_checks(request, action_result, load_code, context)
    first_failure = load_code or _first_failed_code(checks)

    if first_failure is not None:
        outcome = OUTCOME_BLOCKED
        block_code = first_failure
        block_reason = _block_reason(block_code, request.get("block_reason") or load_reason)
    else:
        requested_outcome = request.get(
            "requested_receipt_exhaustion_outcome", OUTCOME_RECORDED
        )
        if requested_outcome in OUTCOME_FAMILY:
            outcome = requested_outcome
        else:
            outcome = OUTCOME_BLOCKED
            block_code = "RECEIPT_EXHAUSTION_INTENT_UNSUPPORTED"
            block_reason = f"Unsupported receipt / exhaustion outcome: {requested_outcome}"
            return _result_artifact(
                request,
                action_result,
                context,
                checks,
                outcome,
                block_code,
                block_reason,
            )
        block_code = None
        block_reason = None

        if request.get("receipt_exhaustion_intent") == INTENT_DO_NOT_RECORD:
            outcome = OUTCOME_NOT_READY

    return _result_artifact(
        request,
        action_result,
        context,
        checks,
        outcome,
        block_code,
        block_reason,
    )


def resolve_distributed_operation_receipt_exhaustion_boundary_from_path(
    declared_receipt_exhaustion_request_path: Path | str,
) -> dict:
    """Resolve one receipt / exhaustion request from a UTF-8 JSON object file."""

    return _load_request_path(declared_receipt_exhaustion_request_path)


def build_distributed_operation_receipt_exhaustion_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a bounded summary from a receipt / exhaustion result artifact."""

    statement = result.get("receipt_exhaustion_statement")
    if not isinstance(statement, Mapping):
        statement = {}
    declared = result.get("declared_receipt_exhaustion_question")
    if not isinstance(declared, Mapping):
        declared = {}
    selected = result.get("selected_action_consequence_result")
    if not isinstance(selected, Mapping):
        selected = {}
    operation_context = result.get("selected_operation_context")
    if not isinstance(operation_context, Mapping):
        operation_context = {}
    block = result.get("block")
    if not isinstance(block, Mapping):
        block = {}
    non_claims = result.get("non_claims")
    if not isinstance(non_claims, Mapping):
        non_claims = {}

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("code") or block.get("block_code"),
        "block_reason": block.get("reason") or block.get("block_reason"),
        "receipt_exhaustion_request_id": declared.get("receipt_exhaustion_request_id"),
        "receipt_exhaustion_question": declared.get("receipt_exhaustion_question"),
        "receipt_exhaustion_intent": declared.get("receipt_exhaustion_intent"),
        "selected_action_consequence_result_id": selected.get(
            "selected_action_consequence_result_id"
        ),
        "selected_action_consequence_result_outcome": selected.get(
            "selected_action_consequence_result_outcome"
        ),
        "selected_operation_candidate_id": _operation_candidate_id(
            operation_context.get("selected_operation_candidate")
        ),
        "selected_operation_matter_id": _operation_matter_id(
            operation_context.get("selected_operation_matter")
        ),
        "passed_check_count": statement.get("passed_check_count"),
        "failed_check_count": statement.get("failed_check_count"),
        "receipt_exhaustion_boundary_recorded": statement.get(
            "receipt_exhaustion_boundary_recorded"
        )
        is True,
        "not_ready": statement.get("not_ready") is True,
        "requires_additional_basis": statement.get("requires_additional_basis") is True,
        "selected_action_consequence_result_preserved": statement.get(
            "selected_action_consequence_result_preserved"
        )
        is True,
        "selected_action_consequence_result_recorded": statement.get(
            "selected_action_consequence_result_recorded"
        )
        is True,
        "selected_action_consequence_result_failed_check_count_zero": statement.get(
            "selected_action_consequence_result_failed_check_count_zero"
        )
        is True,
        "selected_execution_emission_result_preserved": statement.get(
            "selected_execution_emission_result_preserved"
        )
        is True,
        "selected_admission_transition_result_preserved": statement.get(
            "selected_admission_transition_result_preserved"
        )
        is True,
        "selected_admitted_operation_context_preserved": statement.get(
            "selected_admitted_operation_context_preserved"
        )
        is True,
        "operation_admitted": statement.get("operation_admitted") is True,
        "one_bounded_operation_context_admitted": statement.get(
            "one_bounded_operation_context_admitted"
        )
        is True,
        "selected_refusal_abort_result_preserved": statement.get(
            "selected_refusal_abort_result_preserved"
        )
        is True,
        "selected_sync_non_sync_result_preserved": statement.get(
            "selected_sync_non_sync_result_preserved"
        )
        is True,
        "selected_carrier_role_result_preserved": statement.get(
            "selected_carrier_role_result_preserved"
        )
        is True,
        "selected_source_body_authority_result_preserved": statement.get(
            "selected_source_body_authority_result_preserved"
        )
        is True,
        "selected_eligibility_result_preserved": statement.get(
            "selected_eligibility_result_preserved"
        )
        is True,
        "selected_matter_declaration_preserved": statement.get(
            "selected_matter_declaration_preserved"
        )
        is True,
        "selected_operation_candidate_preserved": statement.get(
            "selected_operation_candidate_preserved"
        )
        is True,
        "selected_operation_matter_preserved": statement.get(
            "selected_operation_matter_preserved"
        )
        is True,
        "action_consequence_boundary_preserved": statement.get(
            "action_consequence_boundary_preserved"
        )
        is True,
        "action_unauthorized": statement.get("action_authorized") is False,
        "consequence_uncreated": statement.get("consequence_created") is False,
        "operation_unexecuted": statement.get("operation_executed") is False,
        "output_un_emitted": statement.get("output_emitted") is False,
        "output_evidence_standing_receipt_non_consequence": (
            statement.get("output_treated_as_consequence") is False
            and statement.get("evidence_treated_as_consequence") is False
            and statement.get("standing_treated_as_consequence") is False
            and statement.get("receipt_treated_as_consequence") is False
        ),
        "receipt_exhaustion_requirement_present": statement.get(
            "receipt_exhaustion_requirement_present"
        )
        is True,
        "conformance_dependency_present": statement.get(
            "conformance_dependency_present"
        )
        is True,
        "closure_dependency_present": statement.get("closure_dependency_present") is True,
        "receipt_exhaustion_scope_supported": statement.get(
            "receipt_exhaustion_scope_supported"
        )
        is True,
        "boundary_chain_receipt_only": statement.get("boundary_chain_receipt_only")
        is True,
        "no_actual_operation_receipt_execution_receipt_output_receipt_action_receipt_consequence_receipt": (
            statement.get("actual_operation_receipt_recorded") is False
            and statement.get("execution_receipt_recorded") is False
            and statement.get("output_receipt_recorded") is False
            and statement.get("action_receipt_recorded") is False
            and statement.get("consequence_receipt_recorded") is False
        ),
        "no_conformance_closure": (
            statement.get("conformance_claimed") is False
            and statement.get("closure_claimed") is False
        ),
        "no_public_readiness_final_completion_follow_on_work": (
            statement.get("public_launch_readiness_created") is False
            and statement.get("final_completion_claimed") is False
            and statement.get("follow_on_work_authorized") is False
        ),
        "no_reusable_permission_autonomous_continuation": (
            statement.get("reusable_permission_created") is False
            and statement.get("autonomous_continuation_authorized") is False
        ),
        "key_non_claims": {
            key: non_claims.get(key)
            for key in (
                "actual_operation_receipt_recorded",
                "execution_receipt_recorded",
                "output_receipt_recorded",
                "action_receipt_recorded",
                "consequence_receipt_recorded",
                "conformance_claimed",
                "closure_claimed",
                "public_launch_readiness_created",
                "final_completion_claimed",
                "follow_on_work_authorized",
                "reusable_permission_created",
                "autonomous_continuation_authorized",
            )
        },
    }


def _default_output_path(result: Mapping[str, Any]) -> Path:
    declared = result.get("declared_receipt_exhaustion_question")
    selected = result.get("selected_action_consequence_result")
    request_id = None
    selected_id = None
    if isinstance(declared, Mapping):
        request_id = declared.get("receipt_exhaustion_request_id")
    if isinstance(selected, Mapping):
        selected_id = selected.get("selected_action_consequence_result_id")
    basis = _safe_component(_first_present(request_id, selected_id, RESULT_ID_PREFIX))
    return (
        DISTRIBUTED_OPERATION_RECEIPT_EXHAUSTION_BOUNDARY_ROOT
        / f"{basis}__distributed_receipt_exhaustion_result.json"
    )


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


def write_distributed_operation_receipt_exhaustion_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive receipt / exhaustion result artifact as UTF-8 JSON."""

    if not isinstance(result, Mapping):
        raise DistributedOperationReceiptExhaustionBoundaryError(
            "Receipt / exhaustion result must be a mapping."
        )
    path = Path(output_path) if output_path is not None else _default_output_path(result)
    if path.exists() and path.is_dir():
        path = path / _default_output_path(result).name
    if not path.suffix:
        path = path / _default_output_path(result).name
    path = _non_overwriting_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(dict(result), indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return path


def build_declared_distributed_operation_receipt_exhaustion_request(
    receipt_exhaustion_request_id: str,
    receipt_exhaustion_question: str,
    selected_action_consequence_result: Mapping[str, Any] | str,
    receipt_exhaustion_basis: Mapping[str, Any] | str,
    receipt_exhaustion_scope: Sequence[str] | Mapping[str, Any],
    receipt_exhaustion_intent: str = INTENT_RECORD,
    *,
    selected_action_consequence_result_path: str | None = None,
    selected_action_consequence_result_id: str | None = None,
    selected_action_consequence_result_outcome: str | None = None,
    requested_receipt_exhaustion_outcome: str = OUTCOME_RECORDED,
    conformance_dependency: Mapping[str, Any] | str | None = None,
    closure_dependency: Mapping[str, Any] | str | None = None,
    additional_basis_context: Mapping[str, Any] | None = None,
    not_ready_reason: str | None = None,
) -> dict:
    """Build a bounded declared receipt / exhaustion request."""

    basis: dict[str, Any]
    if isinstance(receipt_exhaustion_basis, Mapping):
        basis = _deepcopy(dict(receipt_exhaustion_basis))
    else:
        basis = {"receipt_exhaustion_basis": receipt_exhaustion_basis}

    if conformance_dependency is None:
        conformance_dependency = {
            "conformance_remains_future_work": True,
            "conformance_requires_separate_boundary": True,
            "conformance_claimed": False,
        }
    if closure_dependency is None:
        closure_dependency = {
            "closure_remains_future_work": True,
            "closure_requires_separate_boundary": True,
            "closure_claimed": False,
        }

    basis.setdefault("conformance_dependency", _deepcopy(conformance_dependency))
    basis.setdefault("closure_dependency", _deepcopy(closure_dependency))
    basis.setdefault(
        "unperformed_non_consequential_posture",
        {
            "operation_executed": False,
            "output_emitted": False,
            "action_authorized": False,
            "consequence_created": False,
        },
    )
    basis.setdefault(
        "exhaustion_accounting_posture",
        {
            "boundary_chain_receipt_only": True,
            "no_reusable_permission_remains": True,
            "future_execution_requires_fresh_receipt_exhaustion": True,
        },
    )

    request: dict[str, Any] = {
        "receipt_exhaustion_request_id": receipt_exhaustion_request_id,
        "receipt_exhaustion_question": receipt_exhaustion_question,
        "receipt_exhaustion_intent": receipt_exhaustion_intent,
        "receipt_exhaustion_basis": basis,
        "receipt_exhaustion_scope": _deepcopy(receipt_exhaustion_scope),
        "requested_receipt_exhaustion_outcome": requested_receipt_exhaustion_outcome,
        "declared_non_claims": _default_non_claims(
            requested_receipt_exhaustion_outcome
        ),
        "conformance_dependency": _deepcopy(conformance_dependency),
        "closure_dependency": _deepcopy(closure_dependency),
    }
    if isinstance(selected_action_consequence_result, Mapping):
        request["selected_action_consequence_result"] = _deepcopy(
            dict(selected_action_consequence_result)
        )
    else:
        request["selected_action_consequence_result_path"] = str(
            selected_action_consequence_result
        )
    if selected_action_consequence_result_path is not None:
        request["selected_action_consequence_result_path"] = (
            selected_action_consequence_result_path
        )
    if selected_action_consequence_result_id is not None:
        request["selected_action_consequence_result_id"] = (
            selected_action_consequence_result_id
        )
    if selected_action_consequence_result_outcome is not None:
        request["selected_action_consequence_result_outcome"] = (
            selected_action_consequence_result_outcome
        )
    if additional_basis_context is not None:
        request["additional_basis_context"] = _deepcopy(dict(additional_basis_context))
    if not_ready_reason is not None:
        request["not_ready_reason"] = not_ready_reason
    return request
