"""Resolve the distributed operation conformance boundary.

This resolver records boundary-chain conformance only. It does not claim
executed-operation conformance, actual operation receipt, operation closure,
public readiness, final completion, reusable permission, autonomous
continuation, action, consequence, execution, emission, synchronization, full
body transfer, second body, or follow-on work.
"""

from __future__ import annotations

import copy
import datetime
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any


class DistributedOperationConformanceBoundaryError(Exception):
    """Raised for hard conformance boundary failures."""


RESOLVER_MODULE = "resolve_distributed_operation_conformance_boundary"
RESULT_VERSION = "0.1.0"
RESULT_TYPE = "distributed_operation_conformance_boundary_result"
RESULT_ID_PREFIX = "distributed_operation_conformance_boundary"

DISTRIBUTED_OPERATION_CONFORMANCE_BOUNDARY_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_distributed_operation_conformance_boundary"
)

EXPECTED_SELECTED_RECEIPT_EXHAUSTION_OUTCOME = (
    "DISTRIBUTED_OPERATION_RECEIPT_EXHAUSTION_BOUNDARY_RECORDED"
)

OUTCOME_RECORDED = "DISTRIBUTED_OPERATION_CONFORMANCE_BOUNDARY_RECORDED"
OUTCOME_NOT_CONFORMANT = "DISTRIBUTED_OPERATION_CONFORMANCE_NOT_CONFORMANT"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "DISTRIBUTED_OPERATION_CONFORMANCE_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "DISTRIBUTED_OPERATION_CONFORMANCE_REVIEW_BLOCKED"
OUTCOME_FAMILY = {
    OUTCOME_RECORDED,
    OUTCOME_NOT_CONFORMANT,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
}

INTENT_RECORD = "RECORD_DISTRIBUTED_OPERATION_CONFORMANCE_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_DISTRIBUTED_OPERATION_CONFORMANCE_BOUNDARY"
INTENT_BLOCK = "BLOCK_DISTRIBUTED_OPERATION_CONFORMANCE_REVIEW"
SUPPORTED_INTENTS = {INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK}

SUPPORTED_CONFORMANCE_SCOPE = (
    "BOUNDARY_CHAIN_CONFORMANCE_ONLY",
    "NO_EXECUTED_OPERATION_CONFORMANCE_CLAIM",
    "NO_ACTUAL_OPERATION_RECEIPT_CLAIM",
    "NO_CONFORMANCE_AS_CLOSURE",
    "NO_PUBLIC_READINESS_CLAIM",
    "NO_FINAL_COMPLETION_CLAIM",
    "NON_CLAIMS_MUST_REMAIN_FALSE",
    "BOUNDARY_SCOPES_MUST_REMAIN_BOUNDED",
    "NO_LAYER_OVERREAD_ALLOWED",
    "CLOSURE_REQUIRES_SEPARATE_BOUNDARY",
)

REQUIRED_NON_CLAIMS = (
    "executed_operation_conformance_claimed",
    "actual_operation_receipt_recorded",
    "operation_executed",
    "output_emitted",
    "action_authorized",
    "consequence_created",
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

PRIOR_RECEIPT_NON_CLAIMS = REQUIRED_NON_CLAIMS + (
    "execution_receipt_recorded",
    "output_receipt_recorded",
    "action_receipt_recorded",
    "consequence_receipt_recorded",
    "receipt_treated_as_consequence",
    "conformance_claimed",
)

COLLAPSE_FIELDS = {
    "CONFORMANCE_REVIEW_CLAIMS_EXECUTED_OPERATION_CONFORMANCE": (
        "executed_operation_conformance_claimed",
        "executed_operation_conformance_recorded",
        "operation_conformance_claimed",
        "operation_conformance_recorded",
        "conformance_claimed",
        "conformance_achieved",
    ),
    "CONFORMANCE_REVIEW_CLAIMS_ACTUAL_OPERATION_RECEIPT": (
        "actual_operation_receipt_recorded",
        "actual_operation_receipt_claimed",
        "operation_receipt_recorded",
        "operation_receipt_claimed",
        "execution_receipt_recorded",
        "output_receipt_recorded",
        "action_receipt_recorded",
        "consequence_receipt_recorded",
    ),
    "CONFORMANCE_REVIEW_CLAIMS_CLOSURE": (
        "closure_claimed",
        "closure_achieved",
        "operation_closed",
        "operation_closure_claimed",
        "conformance_as_closure",
    ),
    "CONFORMANCE_REVIEW_CREATES_PUBLIC_READINESS": (
        "public_launch_readiness_created",
        "public_readiness_created",
        "public_launch_ready",
    ),
    "CONFORMANCE_REVIEW_CLAIMS_FINAL_COMPLETION": (
        "final_completion_claimed",
        "final_governance_completed",
        "final_continuity_completed",
        "final_system_identity_completed",
    ),
    "CONFORMANCE_REVIEW_SCHEDULES_FOLLOW_ON_WORK": (
        "follow_on_work_authorized",
        "follow_on_work_scheduled",
        "self_orientation_successor_scheduled",
    ),
    "CONFORMANCE_REVIEW_CREATES_REUSABLE_PERMISSION": (
        "reusable_permission_created",
        "permission_created",
        "standing_permission_created",
    ),
    "CONFORMANCE_REVIEW_AUTHORIZES_AUTONOMOUS_CONTINUATION": (
        "autonomous_continuation_authorized",
        "continuation_authorized",
        "autonomous_operation_authorized",
    ),
    "CONFORMANCE_REVIEW_AUTHORIZES_ACTION": (
        "action_authorized",
        "action_created",
        "truth_action_created",
        "action_permission_created",
    ),
    "CONFORMANCE_REVIEW_CREATES_CONSEQUENCE": (
        "consequence_created",
        "consequence_action_created",
        "operation_consequence_created",
    ),
    "CONFORMANCE_REVIEW_EXECUTES_OPERATION": (
        "operation_executed",
        "operation_execution_started",
        "distributed_operation_executed",
    ),
    "CONFORMANCE_REVIEW_EMITS_OUTPUT": (
        "output_emitted",
        "emission_created",
        "operation_output_emitted",
        "output_generated",
        "proposed_output_family_emitted",
    ),
    "CONFORMANCE_REVIEW_AUTHORIZES_SYNCHRONIZATION": (
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
    "CONFORMANCE_REVIEW_AUTHORIZES_NON_SYNCHRONIZED_OPERATION": (
        "non_synchronized_operation_authorized",
        "non_sync_operation_authorized",
        "carrier_autonomy_authorized",
        "stale_carrier_operation_authorized",
        "divergent_live_operation_authorized",
        "independent_carrier_operation_authorized",
    ),
    "CONFORMANCE_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER": (
        "full_body_transfer_authorized",
        "full_body_transfer_created",
    ),
    "CONFORMANCE_REVIEW_CREATES_SECOND_BODY": (
        "second_body_created",
        "second_body_authorized",
    ),
    "CONFORMANCE_REVIEW_ERASES_REFUSAL_ABORT": (
        "refusal_abort_erased",
        "refusal_abort_conditions_erased",
        "non_admission_conditions_erased",
        "abort_conditions_erased",
    ),
    "CONFORMANCE_REVIEW_ERASES_EVIDENCE_OR_REFUSAL": (
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
    "CONFORMANCE_REVIEW_RESOLVES_DIVERGENCE": ("divergence_resolved",),
    "MUTATION_REPLAY_OR_MERGE_DETECTED": (
        "mutation_performed",
        "replay_performed",
        "merge_performed",
    ),
}

NON_CONFORMANT_FAILURE_CODES = {
    "BOUNDARY_CHAIN_NOT_CONFORMANT",
    "LAYER_OVERREAD_PRIOR_LAYER",
    "BOUNDARY_SCOPES_NOT_BOUNDED",
}

BLOCK_REASON_BY_CODE = {
    "DECLARED_CONFORMANCE_REQUEST_MALFORMED": (
        "Declared conformance request is not a mapping."
    ),
    "DECLARED_CONFORMANCE_REQUEST_UNREADABLE": (
        "Declared conformance request path is unreadable."
    ),
    "CONFORMANCE_REVIEW_REQUEST_EXPLICITLY_BLOCKED": (
        "Declared conformance request explicitly blocks review."
    ),
    "CONFORMANCE_QUESTION_UNDECLARED": "Conformance question is undeclared.",
    "CONFORMANCE_INTENT_UNSUPPORTED": "Conformance intent is unsupported.",
    "RECEIPT_EXHAUSTION_RESULT_MISSING": (
        "Selected receipt / exhaustion result is missing."
    ),
    "RECEIPT_EXHAUSTION_RESULT_UNREADABLE": (
        "Selected receipt / exhaustion result path is unreadable."
    ),
    "RECEIPT_EXHAUSTION_RESULT_MALFORMED": (
        "Selected receipt / exhaustion result is malformed."
    ),
    "RECEIPT_EXHAUSTION_RESULT_OUTCOME_MISSING": (
        "Selected receipt / exhaustion result outcome is missing."
    ),
    "RECEIPT_EXHAUSTION_RESULT_NOT_RECORDED": (
        "Selected receipt / exhaustion result is not recorded."
    ),
    "RECEIPT_EXHAUSTION_RESULT_HAS_FAILED_CHECKS": (
        "Selected receipt / exhaustion result has failed checks."
    ),
    "ACTION_CONSEQUENCE_RESULT_MISSING": (
        "Selected action / consequence result is missing."
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
    "CONFORMANCE_SCOPE_MISSING": "Declared conformance scope is missing.",
    "CLOSURE_DEPENDENCY_MISSING": "Closure dependency is missing.",
    "UNSUPPORTED_CONFORMANCE_SCOPE": (
        "Conformance scope contains an unsupported value."
    ),
    "NON_CLAIM_MISSING_OR_FLIPPED": (
        "A required conformance non-claim is missing or true."
    ),
    "BOUNDARY_CHAIN_NOT_CONFORMANT": (
        "Readable boundary chain failed conformance to its declared limits."
    ),
    "LAYER_OVERREAD_PRIOR_LAYER": "A layer overread a prior boundary layer.",
    "BOUNDARY_SCOPES_NOT_BOUNDED": "Boundary scopes did not remain bounded.",
}


def _utc_now() -> str:
    return datetime.datetime.now(datetime.UTC).replace(microsecond=0).isoformat()


def _copy(value: Any) -> Any:
    return copy.deepcopy(value)


def _present(value: Any) -> bool:
    if value is None or value == "":
        return False
    if isinstance(value, (list, tuple, set, dict)) and not value:
        return False
    return True


def _get(mapping: Any, path: Sequence[str], default: Any = None) -> Any:
    current = mapping
    for key in path:
        if not isinstance(current, Mapping) or key not in current:
            return default
        current = current[key]
    return current


def _first(*values: Any) -> Any:
    for value in values:
        if _present(value):
            return value
    return None


def _first_key(mapping: Any, keys: Sequence[str]) -> Any:
    if not isinstance(mapping, Mapping):
        return None
    for key in keys:
        if _present(mapping.get(key)):
            return mapping.get(key)
    return None


def _mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _any_true(mapping: Any, keys: Sequence[str]) -> bool:
    return isinstance(mapping, Mapping) and any(mapping.get(key) is True for key in keys)


def _read_json_object(path: Path | str) -> tuple[dict[str, Any] | None, str | None, str | None]:
    resolved = Path(path)
    try:
        with resolved.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
    except FileNotFoundError:
        return None, "unreadable", f"Path not found: {resolved}"
    except OSError as exc:
        return None, "unreadable", str(exc)
    except json.JSONDecodeError as exc:
        return None, "malformed", str(exc)
    if not isinstance(payload, dict):
        return None, "malformed", "JSON payload is not an object."
    return payload, None, None


def _result_sections(result: Any) -> list[Mapping[str, Any]]:
    if not isinstance(result, Mapping):
        return []
    return [
        result,
        _mapping(result.get("receipt_exhaustion_statement")),
        _mapping(result.get("distributed_receipt_exhaustion_summary")),
        _mapping(result.get("non_claims")),
        _mapping(result.get("receipt_exhaustion_basis")),
        _mapping(result.get("receipt_exhaustion_scope")),
        _mapping(result.get("selected_operation_context")),
    ]


def _result_true(result: Any, key: str) -> bool:
    return any(section.get(key) is True for section in _result_sections(result))


def _result_not_true(result: Any, key: str) -> bool:
    return not _result_true(result, key)


def _failed_check_count(result: Any) -> int | None:
    if not isinstance(result, Mapping):
        return None
    direct = result.get("failed_check_count")
    if isinstance(direct, int):
        return direct
    for section in ("receipt_exhaustion_statement", "distributed_receipt_exhaustion_summary"):
        value = _get(result, (section, "failed_check_count"))
        if isinstance(value, int):
            return value
    checks = result.get("receipt_exhaustion_checks")
    if isinstance(checks, Sequence) and not isinstance(checks, (str, bytes, bytearray)):
        return sum(
            1
            for check in checks
            if isinstance(check, Mapping) and check.get("passed") is not True
        )
    return None


def _result_id(result: Any) -> str | None:
    return _first(
        _get(result, ("distributed_receipt_exhaustion_metadata", "distributed_receipt_exhaustion_result_id")),
        _get(result, ("metadata", "result_id")),
        _first_key(
            result,
            (
                "distributed_receipt_exhaustion_result_id",
                "receipt_exhaustion_result_id",
                "result_id",
            ),
        ),
    )


def _outcome(result: Any) -> str | None:
    return _first(
        result.get("outcome") if isinstance(result, Mapping) else None,
        _get(result, ("distributed_receipt_exhaustion_summary", "outcome")),
    )


def _load_request_path(path: Path | str) -> dict[str, Any]:
    payload, error, detail = _read_json_object(path)
    if error == "unreadable":
        return _minimal_blocked_result(
            "DECLARED_CONFORMANCE_REQUEST_UNREADABLE",
            detail,
            request_path=str(path),
        )
    if error == "malformed":
        return _minimal_blocked_result(
            "DECLARED_CONFORMANCE_REQUEST_MALFORMED",
            detail,
            request_path=str(path),
        )
    assert payload is not None
    request = _copy(payload)
    request["conformance_request_path"] = str(path)
    return resolve_distributed_operation_conformance_boundary(request)


def _load_selected_receipt_result(
    request: Mapping[str, Any],
) -> tuple[dict[str, Any] | None, str | None, str | None, str | None]:
    path = request.get("selected_receipt_exhaustion_result_path")
    if _present(path):
        payload, error, detail = _read_json_object(str(path))
        if error == "unreadable":
            return None, "RECEIPT_EXHAUSTION_RESULT_UNREADABLE", detail, str(path)
        if error == "malformed":
            return None, "RECEIPT_EXHAUSTION_RESULT_MALFORMED", detail, str(path)
        assert payload is not None
        return _copy(payload), None, None, str(path)

    selected = request.get("selected_receipt_exhaustion_result")
    if not _present(selected):
        return None, None, None, None
    if not isinstance(selected, Mapping):
        return (
            None,
            "RECEIPT_EXHAUSTION_RESULT_MALFORMED",
            "Selected receipt / exhaustion result is not a mapping.",
            None,
        )
    return _copy(dict(selected)), None, None, None


def _basis(request: Mapping[str, Any]) -> Mapping[str, Any]:
    return _mapping(request.get("conformance_basis"))


def _from_sources(
    request: Mapping[str, Any],
    receipt_result: Mapping[str, Any] | None,
    key: str,
    paths: Sequence[Sequence[str]],
) -> Any:
    basis = _basis(request)
    value = _first(request.get(key), basis.get(key))
    if _present(value):
        return _copy(value)
    for path in paths:
        value = _get(receipt_result, path)
        if _present(value):
            return _copy(value)
    return None


def _basis_value(
    request: Mapping[str, Any],
    receipt_result: Mapping[str, Any] | None,
    key: str,
) -> Any:
    return _first(
        request.get(key),
        _basis(request).get(key),
        _get(receipt_result, ("receipt_exhaustion_basis", key)),
        _get(receipt_result, ("selected_operation_context", key)),
    )


def _candidate_id(candidate: Any) -> str | None:
    if isinstance(candidate, str):
        return candidate
    return _first_key(
        candidate,
        ("operation_candidate_id", "selected_operation_candidate_id", "candidate_id", "id"),
    )


def _matter_id(matter: Any) -> str | None:
    if isinstance(matter, str):
        return matter
    return _first_key(matter, ("operation_matter_id", "selected_operation_matter_id", "matter_id", "id"))


def _normalize_scope(scope: Any) -> tuple[list[str], dict[str, Any], list[str]]:
    if isinstance(scope, Mapping):
        values = _first(
            scope.get("selected_conformance_scope"),
            scope.get("conformance_scope"),
            scope.get("scope"),
        )
        if values is None:
            values = [key for key, selected in scope.items() if selected is True]
    else:
        values = scope

    if isinstance(values, str):
        selected = [values]
    elif isinstance(values, Sequence) and not isinstance(values, (str, bytes, bytearray)):
        selected = [str(value) for value in values]
    else:
        selected = []

    unsupported = [value for value in selected if value not in SUPPORTED_CONFORMANCE_SCOPE]
    selected_set = set(selected)
    flags = {
        "selected_conformance_scope": selected,
        "supported_conformance_scope": list(SUPPORTED_CONFORMANCE_SCOPE),
        "unsupported_conformance_scope": unsupported,
        "all_selected_conformance_scope_supported": not unsupported,
        "boundary_chain_conformance_only": "BOUNDARY_CHAIN_CONFORMANCE_ONLY" in selected_set,
        "no_executed_operation_conformance_claim": (
            "NO_EXECUTED_OPERATION_CONFORMANCE_CLAIM" in selected_set
        ),
        "no_actual_operation_receipt_claim": (
            "NO_ACTUAL_OPERATION_RECEIPT_CLAIM" in selected_set
        ),
        "no_conformance_as_closure": "NO_CONFORMANCE_AS_CLOSURE" in selected_set,
        "no_public_readiness_claim": "NO_PUBLIC_READINESS_CLAIM" in selected_set,
        "no_final_completion_claim": "NO_FINAL_COMPLETION_CLAIM" in selected_set,
        "non_claims_must_remain_false": "NON_CLAIMS_MUST_REMAIN_FALSE" in selected_set,
        "boundary_scopes_must_remain_bounded": (
            "BOUNDARY_SCOPES_MUST_REMAIN_BOUNDED" in selected_set
        ),
        "no_layer_overread_allowed": "NO_LAYER_OVERREAD_ALLOWED" in selected_set,
        "closure_requires_separate_boundary": (
            "CLOSURE_REQUIRES_SEPARATE_BOUNDARY" in selected_set
        ),
    }
    return selected, flags, unsupported


def _declared_non_claims(request: Mapping[str, Any]) -> Mapping[str, Any]:
    return _mapping(request.get("declared_non_claims"))


def _declared_non_claims_valid(request: Mapping[str, Any]) -> bool:
    non_claims = _declared_non_claims(request)
    if not non_claims:
        return False
    for key in REQUIRED_NON_CLAIMS:
        if key not in non_claims or non_claims.get(key) is not False:
            return False
    status = non_claims.get("boundary_chain_conformance_recorded")
    requested = request.get("requested_conformance_outcome", OUTCOME_RECORDED)
    return not (status is True and requested != OUTCOME_RECORDED)


def _collapse_code(
    request: Mapping[str, Any],
    receipt_result: Mapping[str, Any] | None,
) -> str | None:
    candidates: list[Mapping[str, Any]] = [
        request,
        _basis(request),
        _declared_non_claims(request),
        _mapping(request.get("conformance_scope")),
    ]
    candidates.extend(_result_sections(receipt_result))
    for code, fields in COLLAPSE_FIELDS.items():
        for candidate in candidates:
            if _any_true(candidate, fields):
                return code
    return None


def _prior_non_claims_preserved(receipt_result: Mapping[str, Any] | None) -> bool:
    if not isinstance(receipt_result, Mapping):
        return False
    return all(
        not any(section.get(key) is True for section in _result_sections(receipt_result))
        for key in PRIOR_RECEIPT_NON_CLAIMS
    )


def _context(
    request: Mapping[str, Any],
    receipt_result: Mapping[str, Any] | None,
    selected_path: str | None,
) -> dict[str, Any]:
    selected = {
        "selected_action_consequence_result": _from_sources(
            request,
            receipt_result,
            "selected_action_consequence_result",
            (
                ("selected_operation_context", "selected_action_consequence_result"),
                ("receipt_exhaustion_basis", "selected_action_consequence_result"),
                ("selected_action_consequence_result",),
            ),
        ),
        "selected_execution_emission_result": _from_sources(
            request,
            receipt_result,
            "selected_execution_emission_result",
            (
                ("selected_operation_context", "selected_execution_emission_result"),
                ("receipt_exhaustion_basis", "selected_execution_emission_result"),
                ("selected_execution_emission_result",),
            ),
        ),
        "selected_admission_transition_result": _from_sources(
            request,
            receipt_result,
            "selected_admission_transition_result",
            (
                ("selected_operation_context", "selected_admission_transition_result"),
                ("receipt_exhaustion_basis", "selected_admission_transition_result"),
            ),
        ),
        "selected_operation_context": _from_sources(
            request,
            receipt_result,
            "selected_operation_context",
            (
                ("selected_operation_context", "selected_admitted_operation_context"),
                ("selected_operation_context", "admitted_operation_context"),
                ("receipt_exhaustion_basis", "selected_operation_context"),
                ("selected_operation_context",),
            ),
        ),
        "selected_refusal_abort_result": _from_sources(
            request,
            receipt_result,
            "selected_refusal_abort_result",
            (
                ("selected_operation_context", "selected_refusal_abort_result"),
                ("receipt_exhaustion_basis", "selected_refusal_abort_result"),
            ),
        ),
        "selected_sync_non_sync_result": _from_sources(
            request,
            receipt_result,
            "selected_sync_non_sync_result",
            (
                ("selected_operation_context", "selected_sync_non_sync_result"),
                ("receipt_exhaustion_basis", "selected_sync_non_sync_result"),
            ),
        ),
        "selected_carrier_role_result": _from_sources(
            request,
            receipt_result,
            "selected_carrier_role_result",
            (
                ("selected_operation_context", "selected_carrier_role_result"),
                ("receipt_exhaustion_basis", "selected_carrier_role_result"),
            ),
        ),
        "selected_source_body_authority_result": _from_sources(
            request,
            receipt_result,
            "selected_source_body_authority_result",
            (
                ("selected_operation_context", "selected_source_body_authority_result"),
                ("receipt_exhaustion_basis", "selected_source_body_authority_result"),
            ),
        ),
        "selected_eligibility_result": _from_sources(
            request,
            receipt_result,
            "selected_eligibility_result",
            (
                ("selected_operation_context", "selected_eligibility_result"),
                ("receipt_exhaustion_basis", "selected_eligibility_result"),
            ),
        ),
        "selected_matter_declaration": _from_sources(
            request,
            receipt_result,
            "selected_matter_declaration",
            (
                ("selected_operation_context", "selected_matter_declaration"),
                ("receipt_exhaustion_basis", "selected_matter_declaration"),
            ),
        ),
        "selected_operation_candidate": _from_sources(
            request,
            receipt_result,
            "selected_operation_candidate",
            (
                ("selected_operation_context", "selected_operation_candidate"),
                ("receipt_exhaustion_basis", "selected_operation_candidate"),
            ),
        ),
        "selected_operation_matter": _from_sources(
            request,
            receipt_result,
            "selected_operation_matter",
            (
                ("selected_operation_context", "selected_operation_matter"),
                ("receipt_exhaustion_basis", "selected_operation_matter"),
            ),
        ),
    }
    selected_scope, scope_flags, unsupported_scope = _normalize_scope(
        _first(
            request.get("conformance_scope"),
            _basis(request).get("declared_conformance_scope"),
            _basis(request).get("conformance_scope"),
        )
    )
    source_maps = [
        request,
        _basis(request),
        *_result_sections(receipt_result),
        _mapping(selected["selected_operation_context"]),
    ]
    operation_admitted = any(item.get("operation_admitted") is True for item in source_maps)
    one_context = any(
        item.get("one_bounded_operation_context_admitted") is True
        or item.get("one_bounded_operation_context_only") is True
        for item in source_maps
    )
    boundary_preserved = any(
        item.get("distributed_operation_receipt_exhaustion_boundary_recorded") is True
        or item.get("receipt_exhaustion_boundary_recorded") is True
        or item.get("receipt_exhaustion_boundary_preserved") is True
        for item in source_maps
    )
    accounting_only = any(
        item.get("boundary_chain_receipt_only") is True
        or item.get("receipt_exhaustion_boundary_chain_accounting_only") is True
        or item.get("receipt_exhaustion_accounting_only") is True
        for item in source_maps
    )
    no_overread = not any(
        item.get("layer_overread_prior_layer") is True
        or item.get("no_layer_overread_prior_layer") is False
        or item.get("admission_overread_as_execution") is True
        or item.get("execution_emission_boundary_overread_as_execution") is True
        or item.get("execution_emission_boundary_overread_as_output_emission") is True
        or item.get("action_consequence_boundary_overread_as_action") is True
        or item.get("action_consequence_boundary_overread_as_consequence") is True
        or item.get("receipt_exhaustion_boundary_overread_as_actual_receipt") is True
        or item.get("receipt_exhaustion_boundary_overread_as_conformance") is True
        or item.get("receipt_exhaustion_boundary_overread_as_closure") is True
        for item in source_maps
    )
    scopes_bounded = not any(
        item.get("boundary_scopes_remained_bounded") is False
        or item.get("boundary_scope_expanded") is True
        or item.get("operation_scope_expanded") is True
        for item in source_maps
    )
    context = {
        **selected,
        "selected_receipt_exhaustion_result_id": _first(
            request.get("selected_receipt_exhaustion_result_id"),
            _result_id(receipt_result),
        ),
        "selected_receipt_exhaustion_result_outcome": _first(
            request.get("selected_receipt_exhaustion_result_outcome"),
            _outcome(receipt_result),
        ),
        "selected_receipt_exhaustion_result_path": selected_path,
        "selected_receipt_exhaustion_failed_check_count": _failed_check_count(
            receipt_result
        ),
        "selected_operation_candidate_id": _candidate_id(
            selected["selected_operation_candidate"]
        ),
        "selected_operation_matter_id": _matter_id(selected["selected_operation_matter"]),
        "receipt_exhaustion_scope": _basis_value(
            request, receipt_result, "receipt_exhaustion_scope"
        ),
        "action_consequence_scope": _basis_value(
            request, receipt_result, "action_consequence_scope"
        ),
        "execution_emission_scope": _basis_value(
            request, receipt_result, "execution_emission_scope"
        ),
        "admission_scope": _basis_value(request, receipt_result, "admission_scope"),
        "refusal_abort_posture_basis": _basis_value(
            request, receipt_result, "refusal_abort_posture_basis"
        ),
        "sync_non_sync_posture_basis": _basis_value(
            request, receipt_result, "sync_non_sync_posture_basis"
        ),
        "carrier_role_basis": _basis_value(request, receipt_result, "carrier_role_basis"),
        "source_body_authority_basis": _basis_value(
            request, receipt_result, "source_body_authority_basis"
        ),
        "non_claim_preservation_basis": _basis_value(
            request, receipt_result, "non_claim_preservation_basis"
        ),
        "overread_prevention_basis": _basis_value(
            request, receipt_result, "overread_prevention_basis"
        ),
        "scope_preservation_basis": _basis_value(
            request, receipt_result, "scope_preservation_basis"
        ),
        "prior_boundary_preservation_basis": _basis_value(
            request, receipt_result, "prior_boundary_preservation_basis"
        ),
        "closure_dependency": _basis_value(request, receipt_result, "closure_dependency"),
        "selected_conformance_scope": selected_scope,
        "conformance_scope_flags": scope_flags,
        "unsupported_conformance_scope": unsupported_scope,
        "operation_admitted": operation_admitted,
        "one_bounded_operation_context_admitted": one_context,
        "receipt_exhaustion_boundary_preserved": boundary_preserved,
        "receipt_exhaustion_boundary_chain_accounting_only": accounting_only,
        "all_required_prior_non_claims_preserved": _prior_non_claims_preserved(
            receipt_result
        ),
        "no_layer_overread_prior_layer": no_overread,
        "boundary_scopes_remained_bounded": scopes_bounded,
    }
    for key in (
        "actual_operation_receipt_recorded",
        "execution_receipt_recorded",
        "output_receipt_recorded",
        "action_receipt_recorded",
        "consequence_receipt_recorded",
        "executed_operation_conformance_claimed",
        "conformance_claimed",
        "closure_claimed",
        "public_launch_readiness_created",
        "final_completion_claimed",
        "follow_on_work_authorized",
        "reusable_permission_created",
        "autonomous_continuation_authorized",
        "operation_executed",
        "output_emitted",
        "action_authorized",
        "consequence_created",
    ):
        context[f"no_{key}"] = _result_not_true(receipt_result, key)
    return context


def _check(
    name: str,
    passed: bool,
    expected: Any,
    actual: Any,
    code: str | None,
) -> dict[str, Any]:
    return {
        "check_name": name,
        "passed": bool(passed),
        "expected_posture": expected,
        "actual_posture": actual,
        "block_code": None if passed else code,
        "failure_code": None if passed else code,
    }


def _build_checks(
    request: Mapping[str, Any],
    receipt_result: Mapping[str, Any] | None,
    load_code: str | None,
    context: Mapping[str, Any],
) -> list[dict[str, Any]]:
    collapse_code = _collapse_code(request, receipt_result)
    selected_scope = context.get("selected_conformance_scope")
    unsupported_scope = context.get("unsupported_conformance_scope") or []
    checks = [
        _check(
            "conformance question declared",
            _present(request.get("conformance_question")),
            "declared conformance question",
            request.get("conformance_question"),
            "CONFORMANCE_QUESTION_UNDECLARED",
        ),
        _check(
            "conformance intent supported",
            request.get("conformance_intent") in SUPPORTED_INTENTS,
            sorted(SUPPORTED_INTENTS),
            request.get("conformance_intent"),
            "CONFORMANCE_INTENT_UNSUPPORTED",
        ),
        _check(
            "conformance review not explicitly blocked",
            request.get("conformance_intent") != INTENT_BLOCK,
            "not BLOCK_DISTRIBUTED_OPERATION_CONFORMANCE_REVIEW",
            request.get("conformance_intent"),
            "CONFORMANCE_REVIEW_REQUEST_EXPLICITLY_BLOCKED",
        ),
        _check(
            "selected receipt / exhaustion result present",
            receipt_result is not None and load_code is None,
            "selected receipt / exhaustion result mapping",
            "present" if receipt_result is not None else "missing",
            load_code or "RECEIPT_EXHAUSTION_RESULT_MISSING",
        ),
        _check(
            "selected receipt / exhaustion result outcome declared",
            _present(context.get("selected_receipt_exhaustion_result_outcome")),
            "selected receipt / exhaustion outcome declared",
            context.get("selected_receipt_exhaustion_result_outcome"),
            "RECEIPT_EXHAUSTION_RESULT_OUTCOME_MISSING",
        ),
        _check(
            "selected receipt / exhaustion result outcome recorded",
            context.get("selected_receipt_exhaustion_result_outcome")
            == EXPECTED_SELECTED_RECEIPT_EXHAUSTION_OUTCOME,
            EXPECTED_SELECTED_RECEIPT_EXHAUSTION_OUTCOME,
            context.get("selected_receipt_exhaustion_result_outcome"),
            "RECEIPT_EXHAUSTION_RESULT_NOT_RECORDED",
        ),
        _check(
            "selected receipt / exhaustion result failed check count zero",
            context.get("selected_receipt_exhaustion_failed_check_count") == 0,
            0,
            context.get("selected_receipt_exhaustion_failed_check_count"),
            "RECEIPT_EXHAUSTION_RESULT_HAS_FAILED_CHECKS",
        ),
    ]
    required_present = (
        ("selected action / consequence result preserved", "selected_action_consequence_result", "ACTION_CONSEQUENCE_RESULT_MISSING"),
        ("selected execution / emission result preserved", "selected_execution_emission_result", "EXECUTION_EMISSION_RESULT_MISSING"),
        ("selected admission / transition result preserved", "selected_admission_transition_result", "ADMISSION_TRANSITION_RESULT_MISSING"),
        ("selected admitted operation context preserved", "selected_operation_context", "ADMITTED_OPERATION_CONTEXT_MISSING"),
        ("selected refusal / abort result preserved", "selected_refusal_abort_result", "REFUSAL_ABORT_RESULT_MISSING"),
        ("selected sync/non-sync result preserved", "selected_sync_non_sync_result", "SYNC_NON_SYNC_RESULT_MISSING"),
        ("selected carrier role result preserved", "selected_carrier_role_result", "CARRIER_ROLE_RESULT_MISSING"),
        ("selected source-body authority result preserved", "selected_source_body_authority_result", "SOURCE_BODY_AUTHORITY_RESULT_MISSING"),
        ("selected eligibility result preserved", "selected_eligibility_result", "SELECTED_ELIGIBILITY_RESULT_MISSING"),
        ("selected matter declaration preserved", "selected_matter_declaration", "SELECTED_MATTER_DECLARATION_MISSING"),
        ("selected operation candidate preserved", "selected_operation_candidate", "SELECTED_OPERATION_CANDIDATE_MISSING"),
        ("selected operation matter preserved", "selected_operation_matter", "SELECTED_OPERATION_MATTER_MISSING"),
    )
    checks.extend(
        _check(name, _present(context.get(key)), key, context.get(key), code)
        for name, key, code in required_present
    )
    bool_checks = (
        ("operation admitted true", "operation_admitted", True, "OPERATION_NOT_ADMITTED"),
        ("one bounded operation context admitted true", "one_bounded_operation_context_admitted", True, "ONE_BOUNDED_OPERATION_CONTEXT_NOT_ADMITTED"),
        ("receipt / exhaustion boundary preserved", "receipt_exhaustion_boundary_preserved", True, "RECEIPT_EXHAUSTION_RESULT_NOT_RECORDED"),
        ("receipt / exhaustion boundary-chain accounting only", "receipt_exhaustion_boundary_chain_accounting_only", True, "RECEIPT_EXHAUSTION_RESULT_NOT_RECORDED"),
        ("all required prior non-claims false", "all_required_prior_non_claims_preserved", True, collapse_code or "NON_CLAIM_MISSING_OR_FLIPPED"),
        ("no layer overread prior layer", "no_layer_overread_prior_layer", True, "LAYER_OVERREAD_PRIOR_LAYER"),
        ("boundary scopes remained bounded", "boundary_scopes_remained_bounded", True, "BOUNDARY_SCOPES_NOT_BOUNDED"),
    )
    checks.extend(
        _check(name, context.get(key) is expected, expected, context.get(key), code)
        for name, key, expected, code in bool_checks
    )
    false_checks = (
        ("no actual operation receipt claimed", "actual_operation_receipt_recorded", "CONFORMANCE_REVIEW_CLAIMS_ACTUAL_OPERATION_RECEIPT"),
        ("no execution receipt claimed", "execution_receipt_recorded", "CONFORMANCE_REVIEW_CLAIMS_ACTUAL_OPERATION_RECEIPT"),
        ("no output receipt claimed", "output_receipt_recorded", "CONFORMANCE_REVIEW_CLAIMS_ACTUAL_OPERATION_RECEIPT"),
        ("no action receipt claimed", "action_receipt_recorded", "CONFORMANCE_REVIEW_CLAIMS_ACTUAL_OPERATION_RECEIPT"),
        ("no consequence receipt claimed", "consequence_receipt_recorded", "CONFORMANCE_REVIEW_CLAIMS_ACTUAL_OPERATION_RECEIPT"),
        ("no executed-operation conformance already claimed", "executed_operation_conformance_claimed", "CONFORMANCE_REVIEW_CLAIMS_EXECUTED_OPERATION_CONFORMANCE"),
        ("no closure claimed", "closure_claimed", "CONFORMANCE_REVIEW_CLAIMS_CLOSURE"),
        ("no public readiness", "public_launch_readiness_created", "CONFORMANCE_REVIEW_CREATES_PUBLIC_READINESS"),
        ("no final completion", "final_completion_claimed", "CONFORMANCE_REVIEW_CLAIMS_FINAL_COMPLETION"),
        ("no follow-on work", "follow_on_work_authorized", "CONFORMANCE_REVIEW_SCHEDULES_FOLLOW_ON_WORK"),
        ("no reusable permission", "reusable_permission_created", "CONFORMANCE_REVIEW_CREATES_REUSABLE_PERMISSION"),
        ("no autonomous continuation", "autonomous_continuation_authorized", "CONFORMANCE_REVIEW_AUTHORIZES_AUTONOMOUS_CONTINUATION"),
        ("operation unexecuted", "operation_executed", "CONFORMANCE_REVIEW_EXECUTES_OPERATION"),
        ("output un-emitted", "output_emitted", "CONFORMANCE_REVIEW_EMITS_OUTPUT"),
        ("action unauthorized", "action_authorized", "CONFORMANCE_REVIEW_AUTHORIZES_ACTION"),
        ("consequence uncreated", "consequence_created", "CONFORMANCE_REVIEW_CREATES_CONSEQUENCE"),
    )
    checks.extend(
        _check(
            name,
            context.get(f"no_{key}") is True and collapse_code != code,
            False,
            collapse_code == code,
            code,
        )
        for name, key, code in false_checks
    )
    checks.extend(
        [
            _check(
                "closure dependency present",
                _present(context.get("closure_dependency")),
                "closure dependency",
                context.get("closure_dependency"),
                "CLOSURE_DEPENDENCY_MISSING",
            ),
            _check(
                "conformance scope declared",
                bool(selected_scope),
                "declared conformance scope",
                selected_scope,
                "CONFORMANCE_SCOPE_MISSING",
            ),
            _check(
                "conformance scope supported",
                bool(selected_scope) and not unsupported_scope,
                "all selected conformance scope values supported",
                unsupported_scope,
                "UNSUPPORTED_CONFORMANCE_SCOPE",
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
                "all required conformance non-claims false",
                _declared_non_claims(request),
                collapse_code or "NON_CLAIM_MISSING_OR_FLIPPED",
            ),
        ]
    )
    if request.get("requested_conformance_outcome") == OUTCOME_NOT_CONFORMANT or _present(
        request.get("not_conformant_basis")
    ):
        checks.append(
            _check(
                "boundary chain conforms to its own declared limits",
                False,
                "boundary chain conforms to declared limits",
                _copy(request.get("not_conformant_basis")) or "declared not conformant",
                "BOUNDARY_CHAIN_NOT_CONFORMANT",
            )
        )
    if collapse_code and all(check["passed"] for check in checks if check["check_name"] != "non-claims remain false"):
        checks.insert(
            -1,
            _check("conformance collapse posture absent", False, "no collapse posture", collapse_code, collapse_code),
        )
    return checks


def _first_failed_code(checks: Sequence[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is not True:
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str) and code:
                return code
    return None


def _first_blocking_code(checks: Sequence[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is not True:
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str) and code and code not in NON_CONFORMANT_FAILURE_CODES:
                return code
    return None


def _block_reason(code: str | None, explicit: Any = None) -> str | None:
    if explicit:
        return str(explicit)
    if code is None:
        return None
    return BLOCK_REASON_BY_CODE.get(code, code.replace("_", " ").lower())


def _safe_component(value: Any) -> str:
    text = str(value or "conformance_result").strip()
    safe = "".join(char if char.isalnum() or char in "-_." else "_" for char in text)
    return safe.strip("_") or "conformance_result"


def _default_non_claims(outcome: str) -> dict[str, bool]:
    non_claims = {key: False for key in REQUIRED_NON_CLAIMS}
    non_claims["boundary_chain_conformance_recorded"] = outcome == OUTCOME_RECORDED
    non_claims["distributed_operation_conformance_boundary_recorded"] = (
        outcome == OUTCOME_RECORDED
    )
    return non_claims


def _metadata(request: Mapping[str, Any], context: Mapping[str, Any]) -> dict[str, str]:
    basis = _first(
        request.get("conformance_request_id"),
        context.get("selected_receipt_exhaustion_result_id"),
        RESULT_ID_PREFIX,
    )
    return {
        "distributed_operation_conformance_result_id": (
            f"{RESULT_ID_PREFIX}__{_safe_component(basis)}"
        ),
        "distributed_operation_conformance_result_type": RESULT_TYPE,
        "distributed_operation_conformance_result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
    }


def _non_meaning() -> dict[str, bool]:
    meanings = {
        "executed_operation_conformance_claimed": True,
        "actual_operation_receipt_recorded": True,
        "operation_executed": True,
        "output_emitted": True,
        "action_authorized": True,
        "consequence_created": True,
        "operation_closed": True,
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


def _declared_question_section(
    request: Mapping[str, Any],
    context: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "conformance_request_id": request.get("conformance_request_id"),
        "conformance_question": request.get("conformance_question"),
        "conformance_intent": request.get("conformance_intent"),
        "conformance_request_path": request.get("conformance_request_path"),
        "selected_receipt_exhaustion_result_id": context.get(
            "selected_receipt_exhaustion_result_id"
        ),
        "selected_receipt_exhaustion_result_outcome": context.get(
            "selected_receipt_exhaustion_result_outcome"
        ),
        "selected_receipt_exhaustion_result_path": context.get(
            "selected_receipt_exhaustion_result_path"
        ),
        "requested_conformance_outcome": request.get(
            "requested_conformance_outcome", OUTCOME_RECORDED
        ),
        "conformance_boundary_is_not_executed_operation_conformance": True,
        "conformance_boundary_is_not_actual_receipt": True,
        "conformance_boundary_is_not_closure": True,
        "conformance_boundary_is_not_public_readiness": True,
        "conformance_boundary_is_not_final_completion": True,
        "conformance_boundary_is_not_action": True,
        "conformance_boundary_is_not_consequence": True,
        "conformance_boundary_is_not_execution": True,
        "conformance_boundary_is_not_emission": True,
    }


def _selected_receipt_section(
    receipt_result: Mapping[str, Any] | None,
    context: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "selected_receipt_exhaustion_result_id": context.get(
            "selected_receipt_exhaustion_result_id"
        ),
        "selected_receipt_exhaustion_result_outcome": context.get(
            "selected_receipt_exhaustion_result_outcome"
        ),
        "selected_receipt_exhaustion_result_path": context.get(
            "selected_receipt_exhaustion_result_path"
        ),
        "selected_receipt_exhaustion_result_preserved": receipt_result is not None,
        "selected_receipt_exhaustion_result_recorded": (
            context.get("selected_receipt_exhaustion_result_outcome")
            == EXPECTED_SELECTED_RECEIPT_EXHAUSTION_OUTCOME
        ),
        "selected_receipt_exhaustion_result_failed_check_count_zero": (
            context.get("selected_receipt_exhaustion_failed_check_count") == 0
        ),
        "selected_receipt_exhaustion_boundary_preserved": context.get(
            "receipt_exhaustion_boundary_preserved"
        )
        is True,
        "selected_receipt_exhaustion_result_recorded_boundary_chain_accounting_only": (
            context.get("receipt_exhaustion_boundary_chain_accounting_only") is True
        ),
        "selected_receipt_exhaustion_result": _copy(receipt_result)
        if receipt_result is not None
        else None,
    }


def _selected_operation_context_section(
    receipt_result: Mapping[str, Any] | None,
    context: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "selected_receipt_exhaustion_result": _copy(receipt_result)
        if receipt_result is not None
        else None,
        **{key: _copy(context.get(key)) for key in (
            "selected_action_consequence_result",
            "selected_execution_emission_result",
            "selected_admission_transition_result",
            "selected_refusal_abort_result",
            "selected_sync_non_sync_result",
            "selected_carrier_role_result",
            "selected_source_body_authority_result",
            "selected_eligibility_result",
            "selected_matter_declaration",
            "selected_operation_candidate",
            "selected_operation_matter",
        )},
        "selected_admitted_operation_context": _copy(
            context.get("selected_operation_context")
        ),
        "operation_admitted": context.get("operation_admitted") is True,
        "one_bounded_operation_context_admitted": context.get(
            "one_bounded_operation_context_admitted"
        )
        is True,
        "receipt_exhaustion_boundary_recorded": context.get(
            "receipt_exhaustion_boundary_preserved"
        )
        is True,
        "boundary_chain_accounting_only": context.get(
            "receipt_exhaustion_boundary_chain_accounting_only"
        )
        is True,
        "actual_operation_receipt_recorded": False,
        "executed_operation_conformance_claimed": False,
        "closure_claimed": False,
        "public_launch_readiness_created": False,
        "final_completion_claimed": False,
    }


def _conformance_basis_section(
    receipt_result: Mapping[str, Any] | None,
    request: Mapping[str, Any],
    context: Mapping[str, Any],
) -> dict[str, Any]:
    scope_flags = _mapping(context.get("conformance_scope_flags"))
    section = {
        "selected_receipt_exhaustion_result": _copy(receipt_result)
        if receipt_result is not None
        else None,
        "selected_operation_context": _copy(context.get("selected_operation_context")),
        "declared_conformance_request_basis": _copy(_basis(request)),
        "declared_conformance_scope": _copy(context.get("selected_conformance_scope")),
    }
    for key in (
        "selected_action_consequence_result",
        "selected_execution_emission_result",
        "selected_admission_transition_result",
        "selected_refusal_abort_result",
        "selected_sync_non_sync_result",
        "selected_carrier_role_result",
        "selected_source_body_authority_result",
        "selected_eligibility_result",
        "selected_matter_declaration",
        "selected_operation_candidate",
        "selected_operation_matter",
        "receipt_exhaustion_scope",
        "action_consequence_scope",
        "execution_emission_scope",
        "admission_scope",
        "refusal_abort_posture_basis",
        "sync_non_sync_posture_basis",
        "carrier_role_basis",
        "source_body_authority_basis",
        "non_claim_preservation_basis",
        "overread_prevention_basis",
        "scope_preservation_basis",
        "prior_boundary_preservation_basis",
        "closure_dependency",
    ):
        section[key] = _copy(context.get(key))
    for key in (
        "boundary_chain_conformance_only",
        "no_executed_operation_conformance_claim",
        "no_actual_operation_receipt_claim",
        "no_conformance_as_closure",
        "no_public_readiness_claim",
        "no_final_completion_claim",
        "non_claims_must_remain_false",
        "boundary_scopes_must_remain_bounded",
        "no_layer_overread_allowed",
        "closure_requires_separate_boundary",
    ):
        section[key] = scope_flags.get(key) is True
    return section


def _additional_basis_section(
    request: Mapping[str, Any],
    outcome: str,
) -> dict[str, Any]:
    context = _mapping(request.get("additional_basis_context"))
    missing = context.get("missing_basis")
    if isinstance(missing, str):
        missing = [missing]
    if not isinstance(missing, Sequence) or isinstance(missing, (str, bytes, bytearray)):
        missing = []
    return {
        "additional_basis_required": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "additional_basis_reason": _first(
            request.get("additional_basis_reason"),
            context.get("reason"),
            context.get("additional_basis_reason"),
            context.get("missing_basis_reason"),
        ),
        "additional_basis_context": _copy(context),
        "missing_basis": list(missing),
        "additional_basis_scheduled": False,
        "additional_basis_authorized": False,
        "additional_basis_executed": False,
        "additional_basis_creates_closure": False,
        "additional_basis_creates_public_readiness": False,
        "additional_basis_claims_final_completion": False,
        "additional_basis_creates_reusable_permission": False,
        "additional_basis_authorizes_autonomous_continuation": False,
        "additional_basis_schedules_follow_on_work": False,
    }


def _not_conformant_basis_section(
    request: Mapping[str, Any],
    outcome: str,
    checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    basis = _mapping(request.get("not_conformant_basis"))
    return {
        "not_conformant": outcome == OUTCOME_NOT_CONFORMANT,
        "not_conformant_reason": _first(
            request.get("not_conformant_reason"),
            basis.get("reason"),
            basis.get("not_conformant_reason"),
            basis.get("failed_conformance_reason"),
        ),
        "not_conformant_basis": _copy(basis),
        "failed_conformance_checks": [
            _copy(check) for check in checks if check.get("passed") is not True
        ]
        if outcome == OUTCOME_NOT_CONFORMANT
        else [],
        "not_conformant_erases_boundary_chain": False,
        "not_conformant_mutates_prior_artifacts": False,
        "not_conformant_authorizes_repair": False,
        "not_conformant_authorizes_action": False,
        "not_conformant_executes_operation": False,
        "not_conformant_closes_operation": False,
        "not_conformant_schedules_follow_on_work": False,
    }


def _statement(
    outcome: str,
    request: Mapping[str, Any],
    context: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    passed = sum(1 for check in checks if check.get("passed") is True)
    failed = sum(1 for check in checks if check.get("passed") is not True)
    recorded = outcome == OUTCOME_RECORDED
    scope_flags = _mapping(context.get("conformance_scope_flags"))
    return {
        "distributed_operation_conformance_boundary_recorded": recorded,
        "boundary_chain_conformance_recorded": recorded,
        "not_conformant": outcome == OUTCOME_NOT_CONFORMANT,
        "requires_additional_basis": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "not_conformant_reason": request.get("not_conformant_reason")
        if outcome == OUTCOME_NOT_CONFORMANT
        else None,
        "passed_check_count": passed,
        "failed_check_count": failed,
        "selected_receipt_exhaustion_result_preserved": _present(
            context.get("selected_receipt_exhaustion_result_id")
        ),
        "selected_receipt_exhaustion_result_recorded": (
            context.get("selected_receipt_exhaustion_result_outcome")
            == EXPECTED_SELECTED_RECEIPT_EXHAUSTION_OUTCOME
        ),
        "selected_receipt_exhaustion_result_failed_check_count_zero": (
            context.get("selected_receipt_exhaustion_failed_check_count") == 0
        ),
        "operation_admitted": context.get("operation_admitted") is True,
        "one_bounded_operation_context_admitted": context.get(
            "one_bounded_operation_context_admitted"
        )
        is True,
        "receipt_exhaustion_boundary_preserved": context.get(
            "receipt_exhaustion_boundary_preserved"
        )
        is True,
        "receipt_exhaustion_boundary_chain_accounting_only": context.get(
            "receipt_exhaustion_boundary_chain_accounting_only"
        )
        is True,
        "actual_operation_receipt_recorded": False,
        "execution_receipt_recorded": False,
        "output_receipt_recorded": False,
        "action_receipt_recorded": False,
        "consequence_receipt_recorded": False,
        "executed_operation_conformance_claimed": False,
        "closure_claimed": False,
        "public_launch_readiness_created": False,
        "final_completion_claimed": False,
        "follow_on_work_authorized": False,
        "reusable_permission_created": False,
        "autonomous_continuation_authorized": False,
        "operation_executed": False,
        "output_emitted": False,
        "action_authorized": False,
        "consequence_created": False,
        "all_required_prior_non_claims_preserved": context.get(
            "all_required_prior_non_claims_preserved"
        )
        is True,
        "no_layer_overread_prior_layer": context.get("no_layer_overread_prior_layer")
        is True,
        "boundary_scopes_remained_bounded": context.get(
            "boundary_scopes_remained_bounded"
        )
        is True,
        "closure_requires_separate_boundary": scope_flags.get(
            "closure_requires_separate_boundary"
        )
        is True,
        "conformance_scope_supported": (
            bool(context.get("selected_conformance_scope"))
            and not context.get("unsupported_conformance_scope")
        ),
        **{
            f"{key}_preserved": _present(context.get(key))
            for key in (
                "selected_action_consequence_result",
                "selected_execution_emission_result",
                "selected_admission_transition_result",
                "selected_operation_context",
                "selected_refusal_abort_result",
                "selected_sync_non_sync_result",
                "selected_carrier_role_result",
                "selected_source_body_authority_result",
                "selected_eligibility_result",
                "selected_matter_declaration",
                "selected_operation_candidate",
                "selected_operation_matter",
            )
        },
        "selected_admitted_operation_context_preserved": _present(
            context.get("selected_operation_context")
        ),
    }


def _block_section(code: str | None, reason: str | None) -> dict[str, str | None]:
    return {"code": code, "reason": reason, "block_code": code, "block_reason": reason}


def _result_artifact(
    request: Mapping[str, Any],
    receipt_result: Mapping[str, Any] | None,
    context: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    outcome: str,
    block_code: str | None = None,
    block_reason: str | None = None,
) -> dict[str, Any]:
    result = {
        "distributed_operation_conformance_metadata": _metadata(request, context),
        "declared_conformance_question": _declared_question_section(request, context),
        "selected_receipt_exhaustion_result": _selected_receipt_section(
            receipt_result, context
        ),
        "selected_operation_context": _selected_operation_context_section(
            receipt_result, context
        ),
        "conformance_basis": _conformance_basis_section(receipt_result, request, context),
        "conformance_scope": _copy(context.get("conformance_scope_flags", {})),
        "conformance_checks": [_copy(check) for check in checks],
        "conformance_statement": _statement(outcome, request, context, checks),
        "conformance_non_meaning": _non_meaning(),
        "additional_basis_required": _additional_basis_section(request, outcome),
        "not_conformant_basis": _not_conformant_basis_section(
            request, outcome, checks
        ),
        "what_remains_open": _what_remains_open(),
        "non_claims": _default_non_claims(outcome),
        "outcome": outcome,
        "block": _block_section(block_code, block_reason),
    }
    result["distributed_operation_conformance_summary"] = (
        build_distributed_operation_conformance_summary(result)
    )
    return result


def _minimal_blocked_result(
    block_code: str,
    block_reason: str | None = None,
    *,
    request_path: str | None = None,
) -> dict[str, Any]:
    request: dict[str, Any] = {}
    if request_path is not None:
        request["conformance_request_path"] = request_path
    context = {
        "selected_conformance_scope": [],
        "conformance_scope_flags": _normalize_scope([])[1],
        "unsupported_conformance_scope": [],
    }
    checks = [
        _check(
            "conformance review blocked before full evaluation",
            False,
            "readable declared conformance request",
            block_reason or block_code,
            block_code,
        )
    ]
    return _result_artifact(
        request,
        None,
        context,
        checks,
        OUTCOME_BLOCKED,
        block_code,
        _block_reason(block_code, block_reason),
    )


def resolve_distributed_operation_conformance_boundary(
    declared_conformance_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one declared distributed operation conformance boundary request."""

    if declared_conformance_request is None:
        request: dict[str, Any] = {}
    elif not isinstance(declared_conformance_request, Mapping):
        return _minimal_blocked_result(
            "DECLARED_CONFORMANCE_REQUEST_MALFORMED",
            "Declared conformance request is not a mapping.",
        )
    else:
        request = _copy(dict(declared_conformance_request))

    receipt_result, load_code, load_reason, selected_path = _load_selected_receipt_result(
        request
    )
    context = _context(request, receipt_result, selected_path)
    checks = _build_checks(request, receipt_result, load_code, context)
    blocking_code = _first_blocking_code(checks)
    requested = request.get("requested_conformance_outcome", OUTCOME_RECORDED)

    if blocking_code is not None:
        outcome = OUTCOME_BLOCKED
        block_code = blocking_code
        block_reason = _block_reason(block_code, request.get("block_reason") or load_reason)
    elif requested == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
        block_code = None
        block_reason = None
    elif requested == OUTCOME_NOT_CONFORMANT or _first_failed_code(checks) in NON_CONFORMANT_FAILURE_CODES:
        outcome = OUTCOME_NOT_CONFORMANT
        block_code = None
        block_reason = None
    elif request.get("conformance_intent") == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
        block_code = None
        block_reason = None
    else:
        outcome = OUTCOME_RECORDED
        block_code = None
        block_reason = None

    return _result_artifact(
        request,
        receipt_result,
        context,
        checks,
        outcome,
        block_code,
        block_reason,
    )


def resolve_distributed_operation_conformance_boundary_from_path(
    declared_conformance_request_path: Path | str,
) -> dict:
    """Resolve one declared conformance request from a UTF-8 JSON object path."""

    return _load_request_path(declared_conformance_request_path)


def build_distributed_operation_conformance_summary(result: Mapping[str, Any]) -> dict:
    """Build a bounded summary of a distributed operation conformance result."""

    statement = _mapping(result.get("conformance_statement"))
    declared = _mapping(result.get("declared_conformance_question"))
    selected = _mapping(result.get("selected_receipt_exhaustion_result"))
    block = _mapping(result.get("block"))
    non_claims = _mapping(result.get("non_claims"))
    outcome = result.get("outcome")
    no_receipts = all(
        statement.get(key) is False
        for key in (
            "actual_operation_receipt_recorded",
            "execution_receipt_recorded",
            "output_receipt_recorded",
            "action_receipt_recorded",
            "consequence_receipt_recorded",
        )
    )
    no_operation = all(
        statement.get(key) is False
        for key in ("operation_executed", "output_emitted", "action_authorized", "consequence_created")
    )
    no_public_final = all(
        statement.get(key) is False
        for key in (
            "public_launch_readiness_created",
            "final_completion_claimed",
            "follow_on_work_authorized",
        )
    )
    no_permission = all(
        statement.get(key) is False
        for key in ("reusable_permission_created", "autonomous_continuation_authorized")
    )
    return {
        "outcome": outcome,
        "block_code": block.get("code") or block.get("block_code"),
        "block_reason": block.get("reason") or block.get("block_reason"),
        "conformance_request_id": declared.get("conformance_request_id"),
        "conformance_question": declared.get("conformance_question"),
        "conformance_intent": declared.get("conformance_intent"),
        "selected_receipt_exhaustion_result_id": selected.get(
            "selected_receipt_exhaustion_result_id"
        )
        or declared.get("selected_receipt_exhaustion_result_id"),
        "selected_receipt_exhaustion_result_outcome": selected.get(
            "selected_receipt_exhaustion_result_outcome"
        )
        or declared.get("selected_receipt_exhaustion_result_outcome"),
        "selected_operation_candidate_id": _get(
            result,
            ("selected_operation_context", "selected_operation_candidate", "operation_candidate_id"),
        ),
        "selected_operation_matter_id": _get(
            result,
            ("selected_operation_context", "selected_operation_matter", "operation_matter_id"),
        ),
        "passed_check_count": statement.get("passed_check_count"),
        "failed_check_count": statement.get("failed_check_count"),
        "conformance_boundary_recorded": statement.get(
            "distributed_operation_conformance_boundary_recorded"
        )
        is True,
        "boundary_chain_conformance_recorded": statement.get(
            "boundary_chain_conformance_recorded"
        )
        is True,
        "not_conformant": outcome == OUTCOME_NOT_CONFORMANT,
        "requires_additional_basis": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "selected_receipt_exhaustion_result_preserved": statement.get(
            "selected_receipt_exhaustion_result_preserved"
        )
        is True,
        "selected_receipt_exhaustion_result_recorded": statement.get(
            "selected_receipt_exhaustion_result_recorded"
        )
        is True,
        "selected_receipt_exhaustion_result_failed_check_count_zero": statement.get(
            "selected_receipt_exhaustion_result_failed_check_count_zero"
        )
        is True,
        "selected_action_consequence_result_preserved": statement.get(
            "selected_action_consequence_result_preserved"
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
        "receipt_exhaustion_boundary_preserved": statement.get(
            "receipt_exhaustion_boundary_preserved"
        )
        is True,
        "receipt_exhaustion_boundary_chain_accounting_only": statement.get(
            "receipt_exhaustion_boundary_chain_accounting_only"
        )
        is True,
        "no_actual_receipt_execution_receipt_output_receipt_action_receipt_consequence_receipt": no_receipts,
        "no_executed_operation_conformance": statement.get(
            "executed_operation_conformance_claimed"
        )
        is False,
        "no_closure": statement.get("closure_claimed") is False,
        "no_public_readiness_final_completion_follow_on_work": no_public_final,
        "no_reusable_permission_autonomous_continuation": no_permission,
        "operation_unexecuted": statement.get("operation_executed") is False,
        "output_un_emitted": statement.get("output_emitted") is False,
        "action_unauthorized": statement.get("action_authorized") is False,
        "consequence_uncreated": statement.get("consequence_created") is False,
        "no_operation_execution_emission_action_consequence": no_operation,
        "all_required_prior_non_claims_preserved": statement.get(
            "all_required_prior_non_claims_preserved"
        )
        is True,
        "no_layer_overread_prior_layer": statement.get("no_layer_overread_prior_layer")
        is True,
        "boundary_scopes_remained_bounded": statement.get(
            "boundary_scopes_remained_bounded"
        )
        is True,
        "closure_requires_separate_boundary": statement.get(
            "closure_requires_separate_boundary"
        )
        is True,
        "conformance_scope_supported": statement.get("conformance_scope_supported")
        is True,
        "key_non_claims": {
            key: non_claims.get(key)
            for key in REQUIRED_NON_CLAIMS
            if key in non_claims
        },
    }


def _result_filename_basis(result: Mapping[str, Any]) -> str:
    return _first(
        _get(result, ("declared_conformance_question", "conformance_request_id")),
        _get(
            result,
            (
                "selected_receipt_exhaustion_result",
                "selected_receipt_exhaustion_result_id",
            ),
        ),
        _get(
            result,
            (
                "distributed_operation_conformance_metadata",
                "distributed_operation_conformance_result_id",
            ),
        ),
        RESULT_ID_PREFIX,
    )


def _unique_output_path(path: Path) -> Path:
    if not path.exists():
        return path
    counter = 1
    while True:
        candidate = path.parent / f"{path.stem}_{counter:03d}{path.suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def write_distributed_operation_conformance_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive conformance result artifact as stable UTF-8 JSON."""

    if not isinstance(result, Mapping):
        raise DistributedOperationConformanceBoundaryError(
            "Conformance result must be a mapping."
        )
    filename = (
        f"{_safe_component(_result_filename_basis(result))}"
        "__distributed_operation_conformance_result.json"
    )
    if output_path is None:
        path = DISTRIBUTED_OPERATION_CONFORMANCE_BOUNDARY_ROOT / filename
    else:
        path = Path(output_path)
        if (path.exists() and path.is_dir()) or path.suffix == "":
            path = path / filename
    path = _unique_output_path(path)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as handle:
            json.dump(result, handle, indent=2, sort_keys=True, ensure_ascii=False)
            handle.write("\n")
    except OSError as exc:
        raise DistributedOperationConformanceBoundaryError(
            f"Could not write distributed operation conformance result: {exc}"
        ) from exc
    return path


def build_declared_distributed_operation_conformance_request(
    conformance_request_id: str,
    conformance_question: str,
    selected_receipt_exhaustion_result: Mapping[str, Any] | str,
    conformance_basis: Mapping[str, Any] | str,
    conformance_scope: Sequence[str] | Mapping[str, Any],
    conformance_intent: str = INTENT_RECORD,
    *,
    selected_receipt_exhaustion_result_path: str | None = None,
    selected_receipt_exhaustion_result_id: str | None = None,
    selected_receipt_exhaustion_result_outcome: str | None = None,
    requested_conformance_outcome: str = OUTCOME_RECORDED,
    closure_dependency: Mapping[str, Any] | str | None = None,
    additional_basis_context: Mapping[str, Any] | None = None,
    not_conformant_basis: Mapping[str, Any] | str | None = None,
) -> dict:
    """Build a bounded declared conformance request with required non-claims."""

    basis = _copy(dict(conformance_basis)) if isinstance(conformance_basis, Mapping) else {
        "conformance_basis_id": str(conformance_basis)
    }
    if closure_dependency is None:
        closure_dependency = basis.get(
            "closure_dependency",
            {"closure_requires_separate_boundary": True},
        )
    request: dict[str, Any] = {
        "conformance_request_id": conformance_request_id,
        "conformance_question": conformance_question,
        "conformance_intent": conformance_intent,
        "conformance_basis": basis,
        "conformance_scope": _copy(conformance_scope),
        "requested_conformance_outcome": requested_conformance_outcome,
        "closure_dependency": _copy(closure_dependency),
        "declared_non_claims": _default_non_claims(requested_conformance_outcome),
    }
    if isinstance(selected_receipt_exhaustion_result, Mapping):
        request["selected_receipt_exhaustion_result"] = _copy(
            dict(selected_receipt_exhaustion_result)
        )
    else:
        request["selected_receipt_exhaustion_result_path"] = (
            selected_receipt_exhaustion_result_path
            or str(selected_receipt_exhaustion_result)
        )
    if selected_receipt_exhaustion_result_path is not None:
        request["selected_receipt_exhaustion_result_path"] = (
            selected_receipt_exhaustion_result_path
        )
    if selected_receipt_exhaustion_result_id is not None:
        request["selected_receipt_exhaustion_result_id"] = (
            selected_receipt_exhaustion_result_id
        )
    if selected_receipt_exhaustion_result_outcome is not None:
        request["selected_receipt_exhaustion_result_outcome"] = (
            selected_receipt_exhaustion_result_outcome
        )
    if additional_basis_context is not None:
        request["additional_basis_context"] = _copy(dict(additional_basis_context))
    if not_conformant_basis is not None:
        request["not_conformant_basis"] = _copy(not_conformant_basis)
    return request
