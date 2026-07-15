"""Bounded consumed-request command invocation authorization resolver.

This module records one command invocation authorization result only. It may
record a one-shot authorization token as authorization basis, but it does not
invoke a command, execute a command, create command output, create command
result, create command success, create execution permission, create execution
approval, reopen the consumed request token, create a standing invocation lane,
or create repeat invocation permission.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class PortableSourceBodyVerificationConsumedSingleLiveCommandInvocationRequestCommandInvocationAuthorizationError(
    Exception
):
    """Raised for hard command-invocation-authorization resolver failures."""


RESOLVER_MODULE = (
    "resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_"
    "command_invocation_authorization"
)
RESULT_VERSION = "0.1.0"
RESULT_TYPE = (
    "portable_source_body_verification_consumed_single_live_command_invocation_request_"
    "command_invocation_authorization_result"
)

PORTABLE_SOURCE_BODY_VERIFICATION_CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_AUTHORIZATION_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization"
)

CORE_COMMAND_INVOCATION_AUTHORIZATION_QUESTION = (
    "Can the recorded command invocation authorization boundary basis be reviewed as one bounded "
    "command invocation authorization result without invoking the command, executing the command, "
    "creating command output, command result, command success, execution permission, execution "
    "approval, standing invocation lane, repeat permission, authority, currentness, final completion, "
    "continuation, reusable permission, derivative reception, vessel relation, another reception "
    "request, or follow-on work?"
)

INTENT_RECORD = "RECORD_CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_AUTHORIZATION"
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_AUTHORIZATION"
)
INTENT_BLOCK = "BLOCK_CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_AUTHORIZATION"
SUPPORTED_INTENTS = frozenset({INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK})

OUTCOME_RECORDED = (
    "CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_AUTHORIZATION_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_AUTHORIZATION_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_AUTHORIZATION_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_AUTHORIZATION_BLOCKED"
)
OUTCOME_FAMILY = frozenset(
    {
        OUTCOME_RECORDED,
        OUTCOME_NOT_RECORDED,
        OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        OUTCOME_BLOCKED,
    }
)

COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_OUTCOME = (
    "CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_RECORDED"
)
COMMAND_EXECUTION_REVIEW_OUTCOME = (
    "CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_EXECUTION_REVIEW_RECORDED"
)
REQUEST_CONSUMPTION_OUTCOME = "ADMITTED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_CONSUMED"
V2_ADMITTED_REQUEST_OUTCOME = "SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_ADMITTED"
V2_ADMITTED_REQUEST_VERSION = "0.2.0"
V2_ADMITTED_REQUEST_RESOLVER_MODULE = (
    "resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2"
)
V1_PREDECESSOR_RESOLVER_MODULE = (
    "resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary"
)

SUPPORTED_COMMAND_INVOCATION_AUTHORIZATION_SCOPE = (
    "COMMAND_INVOCATION_AUTHORIZATION_ONLY",
    "COMMAND_INVOCATION_AUTHORIZATION_RECORDED_AS_ONE_SHOT_BASIS",
    "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_CREATED",
    "COMMAND_INVOCATION_NOT_CREATED",
    "COMMAND_EXECUTION_NOT_PERFORMED",
    "COMMAND_OUTPUT_NOT_CREATED",
    "COMMAND_RESULT_NOT_CREATED",
    "COMMAND_SUCCESS_NOT_CREATED",
    "EXECUTION_PERMISSION_NOT_CREATED",
    "EXECUTION_APPROVAL_NOT_CREATED",
    "NO_STANDING_INVOCATION_LANE_CREATED",
    "NO_REPEAT_INVOCATION_PERMISSION_CREATED",
    "AUTHORIZATION_IS_NOT_INVOCATION",
    "AUTHORIZATION_IS_NOT_EXECUTION",
    "AUTHORIZATION_IS_NOT_COMMAND_SUCCESS",
    "INVOCATION_REQUIRES_SEPARATE_BOUNDED_STEP",
    "CONSUMED_REQUEST_TOKEN_REMAINS_CLOSED",
    "CONSUMED_REQUEST_NOT_REOPENED",
    "V1_PREDECESSOR_FAILURE_REMAINS_VISIBLE",
    "V2_SUCCESSOR_DOES_NOT_REPAIR_V1",
    "RETURNED_RESULT_CONTAINMENT_PRESERVED",
    "REFERENCE_SHAPED_BASIS_REQUIRED",
    "FULL_PRIOR_ARTIFACT_BODY_NOT_EMITTED",
    "NO_AUTHORITY_CREATED",
    "NO_CURRENTNESS_CREATED",
    "NO_FINAL_COMPLETION",
    "NO_CONTINUATION_AUTHORIZED",
    "NO_REUSABLE_PERMISSION",
    "NO_FOLLOW_ON_WORK_AUTHORIZED",
)
SUPPORTED_COMMAND_INVOCATION_AUTHORIZATION_SCOPE_SET = frozenset(
    SUPPORTED_COMMAND_INVOCATION_AUTHORIZATION_SCOPE
)

REQUIRED_FALSE_NON_CLAIMS = (
    "consumed_request_reopened",
    "command_invocation_created",
    "command_executed",
    "command_execution_performed",
    "command_output_created",
    "command_result_created",
    "command_success_created",
    "execution_permission_created",
    "execution_approval_created",
    "standing_invocation_lane_created",
    "repeat_invocation_permission_created",
    "authorization_treated_as_invocation",
    "authorization_treated_as_execution",
    "authorization_treated_as_command_success",
    "command_output_became_source",
    "command_result_became_authority",
    "command_success_created_currentness",
    "command_success_claimed_final_completion",
    "command_became_authority",
    "full_prior_artifacts_embedded",
    "raw_full_prior_artifact_body_returned",
    "prior_artifacts_mutated",
    "v1_repaired",
    "v1_hidden",
    "v1_claimed_passed",
    "deployment_created",
    "runtime_hosting_created",
    "public_release_created",
    "operation_permission_created",
    "public_launch_readiness_created",
    "final_completion_claimed",
    "continuation_authorized",
    "publication_flow_opened",
    "reusable_permission_created",
    "derivative_reception_authorized",
    "vessel_relation_authorized",
    "another_reception_request_authorized",
    "follow_on_work_authorized",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "command_invocation_authorization_recorded",
    "command_invocation_authorization_created",
    "single_command_invocation_authorization_created",
    "command_invocation_authorization_token_created",
    "authorization_token_is_one_shot",
    "authorization_basis_preserved",
    "invocation_requires_separate_bounded_step",
    "execution_still_not_authorized",
    "consumed_request_token_remains_closed",
    "v1_predecessor_failure_preserved",
    "returned_result_containment_preserved",
)

FORBIDDEN_FULL_BODY_KEYS = frozenset(
    {
        "artifact_body",
        "full_artifact_body",
        "full_prior_artifact_body",
        "full_prior_artifacts",
        "full_result",
        "prior_artifact_body",
        "raw_full_artifact_body",
        "raw_full_prior_artifact_body",
        "raw_full_result",
        "raw_result",
    }
)

BLOCK_CODES = frozenset(
    {
        "DECLARED_COMMAND_INVOCATION_AUTHORIZATION_REQUEST_MALFORMED",
        "DECLARED_COMMAND_INVOCATION_AUTHORIZATION_REQUEST_UNREADABLE",
        "COMMAND_INVOCATION_AUTHORIZATION_QUESTION_UNDECLARED",
        "COMMAND_INVOCATION_AUTHORIZATION_INTENT_UNSUPPORTED",
        "COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_BASIS_MISSING",
        "COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_NOT_RECORDED",
        "COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_FAILED_CHECKS_PRESENT",
        "COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_TERMINAL_SUMMARY_MISSING",
        "COMMAND_EXECUTION_REVIEW_BASIS_MISSING",
        "COMMAND_EXECUTION_REVIEW_NOT_RECORDED",
        "COMMAND_EXECUTION_REVIEW_FAILED_CHECKS_PRESENT",
        "REQUEST_CONSUMPTION_BASIS_MISSING",
        "REQUEST_CONSUMPTION_NOT_CONSUMED",
        "REQUEST_CONSUMPTION_FAILED_CHECKS_PRESENT",
        "CONSUMED_REQUEST_BASIS_MISSING",
        "CONSUMED_TOKEN_NOT_CLOSED",
        "CONSUMED_REQUEST_REOPENED",
        "V2_ADMITTED_REQUEST_BASIS_MISSING",
        "V2_ADMITTED_REQUEST_NOT_ADMITTED",
        "V2_ADMITTED_REQUEST_VERSION_NOT_0_2_0",
        "V2_ADMITTED_REQUEST_FAILED_CHECKS_PRESENT",
        "V2_SUCCESSOR_METADATA_MISSING",
        "V2_RETURNED_RESULT_CONTAINMENT_MISSING",
        "V1_PREDECESSOR_FAILURE_BASIS_MISSING",
        "V2_TREATED_AS_REPAIRING_V1",
        "V1_FAILURE_HIDDEN",
        "V1_CLAIMED_PASSED",
        "COMMAND_EXECUTION_BOUNDARY_BASIS_MISSING",
        "COMMAND_REPORT_BASIS_MISSING",
        "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING",
        "COMMAND_BOUNDARY_BASIS_MISSING",
        "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING",
        "EVIDENCE_MANIFEST_BASIS_MISSING",
        "PORTABLE_VERIFICATION_BASIS_MISSING",
        "AUTHORIZATION_ONLY_POSTURE_MISSING",
        "ONE_SHOT_AUTHORIZATION_POSTURE_MISSING",
        "AUTHORIZATION_TOKEN_POSTURE_MISSING",
        "NO_STANDING_LANE_POSTURE_MISSING",
        "NO_REPEAT_PERMISSION_POSTURE_MISSING",
        "UNSUPPORTED_COMMAND_INVOCATION_AUTHORIZATION_SCOPE",
        "COMMAND_INVOCATION_CREATED",
        "COMMAND_EXECUTION_PERFORMED",
        "COMMAND_OUTPUT_CREATED",
        "COMMAND_RESULT_CREATED",
        "COMMAND_SUCCESS_CREATED",
        "EXECUTION_PERMISSION_CREATED",
        "EXECUTION_APPROVAL_CREATED",
        "STANDING_INVOCATION_LANE_CREATED",
        "REPEAT_INVOCATION_PERMISSION_CREATED",
        "AUTHORIZATION_TREATED_AS_INVOCATION",
        "AUTHORIZATION_TREATED_AS_EXECUTION",
        "AUTHORIZATION_TREATED_AS_COMMAND_SUCCESS",
        "COMMAND_OUTPUT_TREATED_AS_SOURCE",
        "COMMAND_RESULT_TREATED_AS_AUTHORITY",
        "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS",
        "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION",
        "FULL_PRIOR_ARTIFACT_BODY_EMITTED",
        "ARTIFACTS_MUTATED",
        "DEPLOYMENT_CREATED",
        "RUNTIME_HOSTING_CREATED",
        "PUBLIC_RELEASE_CREATED",
        "OPERATION_PERMISSION_CREATED",
        "PUBLIC_READINESS_CREATED",
        "FINAL_COMPLETION_CLAIMED",
        "CONTINUATION_AUTHORIZED",
        "REUSABLE_PERMISSION_CREATED",
        "DERIVATIVE_RECEPTION_AUTHORIZED",
        "VESSEL_RELATION_AUTHORIZED",
        "ANOTHER_RECEPTION_REQUEST_AUTHORIZED",
        "FOLLOW_ON_WORK_AUTHORIZED",
        "MUTATION_REPLAY_OR_MERGE_DETECTED",
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "COMMAND_INVOCATION_AUTHORIZATION_BLOCKED_BY_REQUEST",
    }
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _deepcopy(value: Any) -> Any:
    return copy.deepcopy(value)


def _is_mapping(value: Any) -> bool:
    return isinstance(value, Mapping)


def _truthy(value: Any) -> bool:
    return value is True


def _present(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, Mapping):
        return bool(value)
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return bool(value)
    return True


def _to_int(value: Any) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            return None
    return None


def _safe_component(value: Any, fallback: str) -> str:
    text = str(value or "").strip() or fallback
    safe = []
    for char in text:
        if char.isalnum() or char in {"-", "_", "."}:
            safe.append(char)
        else:
            safe.append("_")
    cleaned = "".join(safe).strip("._")
    return cleaned or fallback


def _contains_forbidden_full_body_key(value: Any) -> bool:
    if isinstance(value, Mapping):
        for key, item in value.items():
            if str(key) in FORBIDDEN_FULL_BODY_KEYS:
                return True
            if _contains_forbidden_full_body_key(item):
                return True
    elif isinstance(value, list):
        for item in value:
            if _contains_forbidden_full_body_key(item):
                return True
    return False


def _sanitize_reference_shape(value: Any) -> Any:
    if isinstance(value, Mapping):
        sanitized: dict[str, Any] = {}
        for key, item in value.items():
            key_text = str(key)
            if key_text in FORBIDDEN_FULL_BODY_KEYS:
                sanitized[key_text] = "[omitted: full prior artifact body is not returned]"
            else:
                sanitized[key_text] = _sanitize_reference_shape(item)
        return sanitized
    if isinstance(value, list):
        return [_sanitize_reference_shape(item) for item in value]
    return _deepcopy(value)


def _mapping_from_basis(value: Any) -> Mapping[str, Any]:
    if isinstance(value, Mapping):
        return value
    return {}


def _basis_section(value: Any, *, path: str | None = None, extra: Mapping[str, Any] | None = None) -> dict:
    if isinstance(value, Mapping):
        section = _sanitize_reference_shape(value)
    elif isinstance(value, (str, Path)):
        section = {"basis_reference": str(value), "basis_is_path_reference": True}
    elif value is None:
        section = {}
    else:
        section = {
            "basis_reference": repr(value),
            "basis_malformed": True,
        }
    if path:
        section.setdefault("selected_path", path)
    if extra:
        for key, item in extra.items():
            if item is not None:
                section.setdefault(key, _sanitize_reference_shape(item))
    return section


def _find_first(mapping: Mapping[str, Any], keys: Sequence[str]) -> Any:
    for key in keys:
        if key in mapping:
            return mapping[key]
    for value in mapping.values():
        if isinstance(value, Mapping):
            found = _find_first(value, keys)
            if found is not None:
                return found
    return None


def _first_not_none(*values: Any) -> Any:
    for value in values:
        if value is not None:
            return value
    return None


def _find_truthy(mapping: Mapping[str, Any], keys: Sequence[str]) -> bool:
    for key in keys:
        value = _find_first(mapping, (key,))
        if value is True:
            return True
    return False


def _basis_declared(value: Any) -> bool:
    return isinstance(value, Mapping) and bool(value)


def _basis_outcome(
    basis: Mapping[str, Any],
    request: Mapping[str, Any],
    request_keys: Sequence[str],
) -> Any:
    request_value = _find_first(request, request_keys)
    if request_value is not None:
        return request_value
    return _find_first(
        basis,
        (
            "outcome",
            "result_outcome",
            "selected_outcome",
            "selected_result_outcome",
        ),
    )


def _basis_failed_count(
    basis: Mapping[str, Any],
    request: Mapping[str, Any],
    request_keys: Sequence[str],
) -> int | None:
    request_value = _find_first(request, request_keys)
    if request_value is not None:
        return _to_int(request_value)
    value = _find_first(
        basis,
        (
            "failed_check_count",
            "failed_checks_count",
            "failed_checks",
            "selected_failed_check_count",
        ),
    )
    if isinstance(value, list):
        return len(value)
    return _to_int(value)


def _basis_version(
    basis: Mapping[str, Any],
    request: Mapping[str, Any],
    request_keys: Sequence[str],
) -> Any:
    request_value = _find_first(request, request_keys)
    if request_value is not None:
        return request_value
    return _find_first(
        basis,
        (
            "result_version",
            "version",
            "selected_version",
            "artifact_version",
        ),
    )


def _successor_metadata_preserved(basis: Mapping[str, Any], request: Mapping[str, Any]) -> bool:
    explicit = request.get("selected_v2_successor_metadata")
    if isinstance(explicit, Mapping) and explicit:
        return True
    successor_of = _find_first(basis, ("successor_of", "predecessor_resolver_module"))
    successor_reason = _find_first(basis, ("successor_reason", "successor_transition_reason"))
    resolver_module = _find_first(basis, ("resolver_module",))
    if successor_of and successor_reason and resolver_module:
        return True
    return _find_truthy(
        basis,
        (
            "successor_metadata_preserved",
            "v2_successor_metadata_preserved",
            "successor_metadata_declared",
        ),
    )


def _returned_result_containment_preserved(basis: Mapping[str, Any]) -> bool:
    return _find_truthy(
        basis,
        (
            "returned_result_containment_preserved",
            "returned_result_containment_posture_preserved",
            "returned_result_containment_declared",
            "no_raw_full_prior_artifact_body_returned",
        ),
    )


def _consumed_token_closed(basis: Mapping[str, Any]) -> bool:
    return _find_truthy(
        basis,
        (
            "consumed_request_token_remains_closed",
            "consumption_token_closed",
            "consumed_token_closed",
            "token_closed",
        ),
    )


def _consumed_request_not_reopened(basis: Mapping[str, Any]) -> bool:
    if _find_truthy(
        basis,
        (
            "consumed_request_reopened",
            "request_reopened",
            "token_reopened",
        ),
    ):
        return False
    return _find_truthy(
        basis,
        (
            "consumed_request_is_not_reopened",
            "consumed_request_not_reopened",
            "no_reopen_consumed_request",
            "request_not_reopened",
        ),
    )


def _v1_failure_visible(basis: Mapping[str, Any]) -> bool:
    return _find_truthy(
        basis,
        (
            "v1_predecessor_failure_remains_visible",
            "v1_remains_visible_predecessor_failure_evidence",
            "visible_predecessor_failure_evidence",
            "v1_predecessor_failure_basis_declared",
        ),
    )


def _v2_claims_v1_passed(v1_basis: Mapping[str, Any], v2_basis: Mapping[str, Any]) -> bool:
    return _find_truthy(
        v1_basis,
        ("v1_claimed_passed", "v1_passed", "v1_predecessor_claimed_passed"),
    ) or _find_truthy(
        v2_basis,
        ("v2_claims_v1_passed", "v1_claimed_passed", "v1_passed"),
    )


def _scope_values(scope: Any) -> list[str]:
    if isinstance(scope, Mapping):
        values = scope.get("selected_scope_values", scope.get("scope_values", scope.get("values")))
        if values is None:
            values = [key for key, value in scope.items() if value is True]
    else:
        values = scope
    if isinstance(values, str):
        return [values]
    if isinstance(values, Sequence) and not isinstance(values, (bytes, bytearray)):
        return [str(value) for value in values]
    return []


def _supported_scope(scope: Any) -> bool:
    values = _scope_values(scope)
    return bool(values) and all(value in SUPPORTED_COMMAND_INVOCATION_AUTHORIZATION_SCOPE_SET for value in values)


def _default_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _declared_non_claims(request: Mapping[str, Any]) -> Mapping[str, Any]:
    value = request.get("declared_non_claims")
    if isinstance(value, Mapping):
        return value
    return {}


def _declared_non_claims_false(request: Mapping[str, Any]) -> bool:
    declared = _declared_non_claims(request)
    if not declared:
        return False
    return all(key in declared and declared.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS)


def _first_declared_non_claim_failure(request: Mapping[str, Any]) -> str | None:
    declared = _declared_non_claims(request)
    for key in REQUIRED_FALSE_NON_CLAIMS:
        if key not in declared or declared.get(key) is not False:
            return key
    return None


COLLAPSE_TRUE_BLOCKS = (
    ("command_invocation_created", "COMMAND_INVOCATION_CREATED"),
    ("command_invocation_permission_created", "COMMAND_INVOCATION_CREATED"),
    ("command_executed", "COMMAND_EXECUTION_PERFORMED"),
    ("command_execution_performed", "COMMAND_EXECUTION_PERFORMED"),
    ("command_output_created", "COMMAND_OUTPUT_CREATED"),
    ("command_result_created", "COMMAND_RESULT_CREATED"),
    ("command_success_created", "COMMAND_SUCCESS_CREATED"),
    ("execution_permission_created", "EXECUTION_PERMISSION_CREATED"),
    ("execution_approval_created", "EXECUTION_APPROVAL_CREATED"),
    ("standing_invocation_lane_created", "STANDING_INVOCATION_LANE_CREATED"),
    ("repeat_invocation_permission_created", "REPEAT_INVOCATION_PERMISSION_CREATED"),
    ("authorization_treated_as_invocation", "AUTHORIZATION_TREATED_AS_INVOCATION"),
    ("authorization_treated_as_execution", "AUTHORIZATION_TREATED_AS_EXECUTION"),
    ("authorization_treated_as_command_success", "AUTHORIZATION_TREATED_AS_COMMAND_SUCCESS"),
    ("command_output_became_source", "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
    ("command_result_became_authority", "COMMAND_RESULT_TREATED_AS_AUTHORITY"),
    ("command_success_created_currentness", "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
    ("command_success_claimed_final_completion", "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
    ("prior_artifacts_mutated", "ARTIFACTS_MUTATED"),
    ("deployment_created", "DEPLOYMENT_CREATED"),
    ("runtime_hosting_created", "RUNTIME_HOSTING_CREATED"),
    ("public_release_created", "PUBLIC_RELEASE_CREATED"),
    ("operation_permission_created", "OPERATION_PERMISSION_CREATED"),
    ("public_launch_readiness_created", "PUBLIC_READINESS_CREATED"),
    ("public_readiness_created", "PUBLIC_READINESS_CREATED"),
    ("final_completion_claimed", "FINAL_COMPLETION_CLAIMED"),
    ("continuation_authorized", "CONTINUATION_AUTHORIZED"),
    ("reusable_permission_created", "REUSABLE_PERMISSION_CREATED"),
    ("derivative_reception_authorized", "DERIVATIVE_RECEPTION_AUTHORIZED"),
    ("vessel_relation_authorized", "VESSEL_RELATION_AUTHORIZED"),
    ("another_reception_request_authorized", "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"),
    ("follow_on_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
)


def _first_collapse_block(values: Sequence[Any]) -> tuple[str, str] | None:
    for value in values:
        if isinstance(value, Mapping):
            for key, block_code in COLLAPSE_TRUE_BLOCKS:
                if _find_truthy(value, (key,)):
                    return key, block_code
            if any(
                _find_truthy(value, (key,))
                for key in ("mutation_performed", "replay_performed", "merge_performed")
            ):
                return "mutation_replay_or_merge", "MUTATION_REPLAY_OR_MERGE_DETECTED"
    return None


def _check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: str,
    actual_posture: Any,
    block_code: str | None,
) -> None:
    checks.append(
        {
            "check_name": check_name,
            "passed": bool(passed),
            "expected_posture": expected_posture,
            "actual_posture": _sanitize_reference_shape(actual_posture),
            "block_code": None if passed else block_code,
            "failure_code": None if passed else block_code,
        }
    )


def _block(code: str | None, reason: str | None = None) -> dict[str, Any]:
    return {"code": code, "reason": reason}


def _build_metadata(request: Mapping[str, Any], outcome: str) -> dict[str, Any]:
    request_id = str(request.get("command_invocation_authorization_request_id") or "undeclared")
    result_id = (
        f"{request_id}__consumed_single_live_command_invocation_request_"
        "command_invocation_authorization_result"
    )
    return {
        "consumed_single_live_command_invocation_request_command_invocation_authorization_result_id": result_id,
        "consumed_single_live_command_invocation_request_command_invocation_authorization_result_type": RESULT_TYPE,
        "consumed_single_live_command_invocation_request_command_invocation_authorization_result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
        "command_invocation_authorization_request_id": request_id,
        "requested_outcome": request.get("requested_command_invocation_authorization_outcome"),
        "outcome": outcome,
    }


def _statement(outcome: str) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    statement = {key: recorded for key in ALLOWED_TRUE_RECORDED_FIELDS}
    statement.update(_default_non_claims())
    statement["command_invocation_authorization_not_recorded"] = outcome == OUTCOME_NOT_RECORDED
    statement["command_invocation_authorization_requires_additional_basis"] = (
        outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    )
    statement["command_invocation_authorization_blocked"] = outcome == OUTCOME_BLOCKED
    statement["authorization_is_not_command_invocation"] = True
    statement["authorization_is_not_command_execution"] = True
    statement["authorization_is_not_command_output"] = True
    statement["authorization_is_not_command_result"] = True
    statement["authorization_is_not_command_success"] = True
    statement["authorization_is_not_execution_permission"] = True
    statement["authorization_is_not_execution_approval"] = True
    return statement


def _non_meaning() -> dict[str, bool]:
    names = (
        "command_invocation_created",
        "command_executed",
        "command_output_exists",
        "command_result_exists",
        "command_success_exists",
        "execution_permission_exists",
        "execution_approval_exists",
        "command_success_creates_currentness",
        "command_success_claims_final_completion",
        "command_output_becomes_source",
        "command_result_becomes_authority",
        "standing_invocation_lane_exists",
        "repeat_invocation_permission_exists",
        "consumed_request_token_reopened",
        "v1_was_repaired",
        "v1_was_hidden",
        "v1_passed",
        "deployment_created",
        "runtime_hosting_created",
        "public_release_created",
        "public_readiness_created",
        "final_completion_claimed",
        "continuation_authorized",
        "reusable_permission_created",
        "derivative_reception_authorized",
        "vessel_relation_authorized",
        "another_reception_request_authorized",
        "follow_on_work_authorized",
    )
    return {f"command_invocation_authorization_does_not_mean_{name}": True for name in names}


def _additional_basis_required(outcome: str, request: Mapping[str, Any]) -> dict[str, Any]:
    context = request.get("additional_basis_context")
    requires = outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    return {
        "requires_additional_basis": requires,
        "additional_basis_context": _sanitize_reference_shape(context or {}),
        "missing_basis_not_scheduled": True,
        "missing_basis_not_authorized": True,
        "missing_basis_not_executed": True,
    }


def _not_recorded_basis(outcome: str, request: Mapping[str, Any], checks: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    basis = request.get("not_recorded_basis")
    failed_checks = [check for check in checks if not check.get("passed")]
    return {
        "not_recorded": outcome == OUTCOME_NOT_RECORDED,
        "not_recorded_basis": _sanitize_reference_shape(basis or {}),
        "failed_checks": _sanitize_reference_shape(failed_checks if outcome == OUTCOME_NOT_RECORDED else []),
        "not_recorded_does_not_mutate": True,
        "not_recorded_does_not_repair": True,
        "not_recorded_does_not_invoke_command": True,
        "not_recorded_does_not_execute_command": True,
        "not_recorded_does_not_authorize_next_work": True,
    }


def _what_remains_open() -> dict[str, Any]:
    open_items = (
        "command_invocation_authorization_test",
        "command_invocation_authorization_live_artifact",
        "command_invocation_boundary_if_separately_specified",
        "command_invocation",
        "command_execution",
        "command_output",
        "command_result",
        "command_success",
        "command_output_report_artifact_from_live_execution",
        "manifest_implementation",
        "checksum_implementation",
        "signature_implementation",
        "source_body_packet_implementation",
        "reproducible_environment_declaration",
        "runtime_hosting",
        "deployment",
        "public_release",
        "source_transfer",
        "source_migration",
        "source_receipt",
        "reception_authorization",
        "derivative_reception",
        "vessel_relation",
        "adoption",
        "authority_creation",
        "currentness_creation",
        "operation_permission",
        "public_readiness",
        "final_completion",
        "continuation",
        "publication_flow",
        "reusable_permission",
        "successor_reception_request",
        "follow_on_work",
    )
    return {
        "open_items": list(open_items),
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }


def _scope_section(scope: Any, outcome: str) -> dict[str, Any]:
    values = _scope_values(scope)
    unsupported = [value for value in values if value not in SUPPORTED_COMMAND_INVOCATION_AUTHORIZATION_SCOPE_SET]
    return {
        "selected_scope_values": values,
        "supported_scope_values": list(SUPPORTED_COMMAND_INVOCATION_AUTHORIZATION_SCOPE),
        "unsupported_scope_values": unsupported,
        "all_selected_scope_values_supported": not unsupported and bool(values),
        "command_invocation_authorization_only": "COMMAND_INVOCATION_AUTHORIZATION_ONLY" in values,
        "authorization_recorded_as_one_shot_basis": outcome == OUTCOME_RECORDED,
        "authorization_token_created_only_in_recorded_outcome": outcome == OUTCOME_RECORDED,
        "command_invocation_not_created": True,
        "command_execution_not_performed": True,
        "command_output_result_success_not_created": True,
        "execution_permission_not_created": True,
        "execution_approval_not_created": True,
        "no_standing_invocation_lane": True,
        "no_repeat_invocation_permission": True,
        "authorization_is_not_invocation": True,
        "authorization_is_not_execution": True,
        "authorization_is_not_command_success": True,
        "invocation_requires_separate_bounded_step": True,
        "consumed_request_token_remains_closed": True,
        "consumed_request_not_reopened": True,
        "v1_predecessor_failure_remains_visible": True,
        "v2_successor_does_not_repair_v1": True,
        "returned_result_containment_preserved": True,
        "reference_shaped_basis_required": True,
        "full_prior_artifact_body_not_emitted": True,
        "no_authority_created": True,
        "no_currentness_created": True,
        "no_final_completion": True,
        "no_continuation_authorized": True,
        "no_reusable_permission": True,
        "no_follow_on_work_authorized": True,
    }


def _posture_section(value: Any, *, extra: Mapping[str, Any] | None = None) -> dict[str, Any]:
    section = _basis_section(value)
    if extra:
        section.update(extra)
    return section


def _build_checks(request: Mapping[str, Any], request_malformed: bool = False) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    if request_malformed:
        _check(
            checks,
            "declared command invocation authorization request mapping",
            False,
            "declared request is a mapping",
            "malformed",
            "DECLARED_COMMAND_INVOCATION_AUTHORIZATION_REQUEST_MALFORMED",
        )
        return checks

    boundary_basis = _mapping_from_basis(request.get("selected_command_invocation_authorization_boundary_basis"))
    boundary_summary = request.get("selected_command_invocation_authorization_boundary_terminal_summary_basis")
    review_basis = _mapping_from_basis(request.get("selected_command_execution_review_basis"))
    consumption_basis = _mapping_from_basis(request.get("selected_request_consumption_basis"))
    consumed_basis = _mapping_from_basis(request.get("selected_consumed_request_basis"))
    v2_basis = _mapping_from_basis(request.get("selected_v2_admitted_request_basis"))
    v1_basis = _mapping_from_basis(request.get("selected_v1_predecessor_failure_basis"))

    question = request.get("command_invocation_authorization_question")
    intent = request.get("command_invocation_authorization_intent")
    _check(
        checks,
        "command invocation authorization question declared",
        isinstance(question, str) and bool(question.strip()),
        "question is declared",
        question,
        "COMMAND_INVOCATION_AUTHORIZATION_QUESTION_UNDECLARED",
    )
    _check(
        checks,
        "command invocation authorization intent supported",
        intent in SUPPORTED_INTENTS,
        "intent is supported",
        intent,
        "COMMAND_INVOCATION_AUTHORIZATION_INTENT_UNSUPPORTED",
    )
    _check(
        checks,
        "command invocation authorization boundary terminal summary basis declared",
        _present(boundary_summary),
        "terminal summary basis is declared",
        boundary_summary,
        "COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_TERMINAL_SUMMARY_MISSING",
    )
    _check(
        checks,
        "command invocation authorization boundary live artifact basis declared",
        _basis_declared(boundary_basis),
        "boundary live artifact basis is declared",
        boundary_basis,
        "COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_BASIS_MISSING",
    )
    boundary_outcome = _basis_outcome(
        boundary_basis,
        request,
        ("selected_command_invocation_authorization_boundary_result_outcome",),
    )
    _check(
        checks,
        "command invocation authorization boundary live artifact recorded outcome",
        boundary_outcome == COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_OUTCOME,
        COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_OUTCOME,
        boundary_outcome,
        "COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_NOT_RECORDED",
    )
    boundary_failed = _basis_failed_count(
        boundary_basis,
        request,
        ("selected_command_invocation_authorization_boundary_failed_check_count",),
    )
    _check(
        checks,
        "command invocation authorization boundary live artifact failed check count zero",
        boundary_failed == 0,
        "failed_check_count == 0",
        boundary_failed,
        "COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_FAILED_CHECKS_PRESENT",
    )

    _check(
        checks,
        "command execution review basis declared",
        _basis_declared(review_basis),
        "command execution review basis is declared",
        review_basis,
        "COMMAND_EXECUTION_REVIEW_BASIS_MISSING",
    )
    review_outcome = _basis_outcome(
        review_basis,
        request,
        ("selected_command_execution_review_result_outcome",),
    )
    _check(
        checks,
        "command execution review live artifact recorded outcome",
        review_outcome == COMMAND_EXECUTION_REVIEW_OUTCOME,
        COMMAND_EXECUTION_REVIEW_OUTCOME,
        review_outcome,
        "COMMAND_EXECUTION_REVIEW_NOT_RECORDED",
    )
    review_failed = _basis_failed_count(
        review_basis,
        request,
        ("selected_command_execution_review_failed_check_count",),
    )
    _check(
        checks,
        "command execution review live artifact failed check count zero",
        review_failed == 0,
        "failed_check_count == 0",
        review_failed,
        "COMMAND_EXECUTION_REVIEW_FAILED_CHECKS_PRESENT",
    )

    _check(
        checks,
        "request-consumption basis declared",
        _basis_declared(consumption_basis),
        "request-consumption basis is declared",
        consumption_basis,
        "REQUEST_CONSUMPTION_BASIS_MISSING",
    )
    consumption_outcome = _basis_outcome(
        consumption_basis,
        request,
        ("selected_request_consumption_result_outcome",),
    )
    _check(
        checks,
        "request-consumption live artifact consumed outcome",
        consumption_outcome == REQUEST_CONSUMPTION_OUTCOME,
        REQUEST_CONSUMPTION_OUTCOME,
        consumption_outcome,
        "REQUEST_CONSUMPTION_NOT_CONSUMED",
    )
    consumption_failed = _basis_failed_count(
        consumption_basis,
        request,
        ("selected_request_consumption_failed_check_count",),
    )
    _check(
        checks,
        "request-consumption live artifact failed check count zero",
        consumption_failed == 0,
        "failed_check_count == 0",
        consumption_failed,
        "REQUEST_CONSUMPTION_FAILED_CHECKS_PRESENT",
    )

    _check(
        checks,
        "consumed request basis declared",
        _basis_declared(consumed_basis),
        "consumed request basis is declared",
        consumed_basis,
        "CONSUMED_REQUEST_BASIS_MISSING",
    )
    _check(
        checks,
        "consumed request token remains closed",
        _consumed_token_closed(consumed_basis),
        "consumed request token remains closed",
        consumed_basis,
        "CONSUMED_TOKEN_NOT_CLOSED",
    )
    _check(
        checks,
        "consumed request not reopened",
        _consumed_request_not_reopened(consumed_basis),
        "consumed request is not reopened",
        consumed_basis,
        "CONSUMED_REQUEST_REOPENED",
    )

    _check(
        checks,
        "selected v2 admitted request basis declared",
        _basis_declared(v2_basis),
        "v2 admitted request basis is declared",
        v2_basis,
        "V2_ADMITTED_REQUEST_BASIS_MISSING",
    )
    v2_outcome = _basis_outcome(
        v2_basis,
        request,
        ("selected_v2_admitted_request_outcome",),
    )
    _check(
        checks,
        "v2 admitted request outcome admitted",
        v2_outcome == V2_ADMITTED_REQUEST_OUTCOME,
        V2_ADMITTED_REQUEST_OUTCOME,
        v2_outcome,
        "V2_ADMITTED_REQUEST_NOT_ADMITTED",
    )
    v2_version = _basis_version(
        v2_basis,
        request,
        ("selected_v2_admitted_request_version",),
    )
    _check(
        checks,
        "v2 admitted request version 0.2.0",
        v2_version == V2_ADMITTED_REQUEST_VERSION,
        V2_ADMITTED_REQUEST_VERSION,
        v2_version,
        "V2_ADMITTED_REQUEST_VERSION_NOT_0_2_0",
    )
    v2_failed = _basis_failed_count(v2_basis, request, ("selected_v2_failed_check_count",))
    _check(
        checks,
        "v2 admitted request failed check count zero",
        v2_failed == 0,
        "failed_check_count == 0",
        v2_failed,
        "V2_ADMITTED_REQUEST_FAILED_CHECKS_PRESENT",
    )
    _check(
        checks,
        "v2 successor metadata preserved",
        _successor_metadata_preserved(v2_basis, request),
        "successor metadata is preserved",
        v2_basis,
        "V2_SUCCESSOR_METADATA_MISSING",
    )
    _check(
        checks,
        "v2 returned-result containment preserved",
        _returned_result_containment_preserved(v2_basis),
        "returned-result containment is preserved",
        v2_basis,
        "V2_RETURNED_RESULT_CONTAINMENT_MISSING",
    )

    _check(
        checks,
        "selected v1 predecessor/failure basis declared",
        _basis_declared(v1_basis),
        "v1 predecessor/failure basis is declared",
        v1_basis,
        "V1_PREDECESSOR_FAILURE_BASIS_MISSING",
    )
    _check(
        checks,
        "v1 predecessor failure remains visible",
        _v1_failure_visible(v1_basis),
        "v1 predecessor failure remains visible",
        v1_basis,
        "V1_PREDECESSOR_FAILURE_BASIS_MISSING",
    )
    _check(
        checks,
        "v2 does not repair v1",
        not _find_truthy(v1_basis, ("v1_repaired", "v2_treated_as_repairing_v1"))
        and not _find_truthy(v2_basis, ("v2_treated_as_repairing_v1", "v1_repaired")),
        "v2 does not repair v1",
        {"v1_basis": v1_basis, "v2_basis": v2_basis},
        "V2_TREATED_AS_REPAIRING_V1",
    )
    _check(
        checks,
        "v1 failure not hidden",
        not _find_truthy(v1_basis, ("v1_hidden", "v1_failure_hidden")),
        "v1 failure is not hidden",
        v1_basis,
        "V1_FAILURE_HIDDEN",
    )
    _check(
        checks,
        "v2 does not claim v1 passed",
        not _v2_claims_v1_passed(v1_basis, v2_basis),
        "v1 is not claimed passed",
        {"v1_basis": v1_basis, "v2_basis": v2_basis},
        "V1_CLAIMED_PASSED",
    )

    basis_presence_checks = (
        ("command execution boundary basis declared", "selected_command_execution_boundary_basis", "COMMAND_EXECUTION_BOUNDARY_BASIS_MISSING"),
        ("command report basis declared", "selected_command_report_basis", "COMMAND_REPORT_BASIS_MISSING"),
        (
            "command implementation boundary basis declared",
            "selected_command_implementation_boundary_basis",
            "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING",
        ),
        ("command boundary basis declared", "selected_command_boundary_basis", "COMMAND_BOUNDARY_BASIS_MISSING"),
        (
            "artifact emission containment basis declared",
            "selected_artifact_emission_containment_basis",
            "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING",
        ),
        ("evidence-manifest basis declared", "selected_evidence_manifest_basis", "EVIDENCE_MANIFEST_BASIS_MISSING"),
        ("portable verification basis declared", "selected_portable_verification_basis", "PORTABLE_VERIFICATION_BASIS_MISSING"),
    )
    for name, field, block_code in basis_presence_checks:
        value = request.get(field)
        _check(checks, name, _present(value), "basis is declared", value, block_code)

    posture_checks = (
        ("authorization-only posture declared", "authorization_only_posture", "AUTHORIZATION_ONLY_POSTURE_MISSING"),
        ("one-shot-authorization posture declared", "one_shot_authorization_posture", "ONE_SHOT_AUTHORIZATION_POSTURE_MISSING"),
        ("authorization-token posture declared", "authorization_token_posture", "AUTHORIZATION_TOKEN_POSTURE_MISSING"),
        ("no-command-invocation posture declared", "no_command_invocation_posture", "COMMAND_INVOCATION_CREATED"),
        ("no-command-execution posture declared", "no_command_execution_posture", "COMMAND_EXECUTION_PERFORMED"),
        ("no-output/result/success posture declared", "no_output_result_success_posture", "COMMAND_OUTPUT_CREATED"),
        ("no-execution-permission posture declared", "no_execution_permission_posture", "EXECUTION_PERMISSION_CREATED"),
        ("no-execution-approval posture declared", "no_execution_approval_posture", "EXECUTION_APPROVAL_CREATED"),
        ("no-standing-lane posture declared", "no_standing_lane_posture", "NO_STANDING_LANE_POSTURE_MISSING"),
        ("no-repeat-permission posture declared", "no_repeat_permission_posture", "NO_REPEAT_PERMISSION_POSTURE_MISSING"),
        ("consumed-token-closed posture declared", "consumed_token_closed_posture", "CONSUMED_TOKEN_NOT_CLOSED"),
        ("no-reopen-consumed-request posture declared", "no_reopen_consumed_request_posture", "CONSUMED_REQUEST_REOPENED"),
        ("returned-result containment posture declared", "returned_result_containment_posture", "V2_RETURNED_RESULT_CONTAINMENT_MISSING"),
    )
    for name, field, block_code in posture_checks:
        value = request.get(field)
        _check(checks, name, _present(value), "posture is declared", value, block_code)

    _check(
        checks,
        "reference-shaped input posture declared",
        _present(request.get("reference_shaped_input_posture"))
        or "REFERENCE_SHAPED_BASIS_REQUIRED" in _scope_values(request.get("command_invocation_authorization_scope")),
        "reference-shaped input posture is declared or required by scope",
        request.get("reference_shaped_input_posture")
        or _scope_values(request.get("command_invocation_authorization_scope")),
        "FULL_PRIOR_ARTIFACT_BODY_EMITTED",
    )

    _check(
        checks,
        "command invocation authorization scope supported",
        _supported_scope(request.get("command_invocation_authorization_scope")),
        "all selected scope values are supported",
        _scope_values(request.get("command_invocation_authorization_scope")),
        "UNSUPPORTED_COMMAND_INVOCATION_AUTHORIZATION_SCOPE",
    )

    all_values = [request] + [
        request.get(field)
        for field in (
            "selected_command_invocation_authorization_boundary_basis",
            "selected_command_invocation_authorization_boundary_terminal_summary_basis",
            "selected_command_execution_review_basis",
            "selected_request_consumption_basis",
            "selected_consumed_request_basis",
            "selected_v2_admitted_request_basis",
            "selected_v1_predecessor_failure_basis",
            "selected_command_execution_boundary_basis",
            "selected_command_report_basis",
            "selected_command_implementation_boundary_basis",
            "selected_command_boundary_basis",
            "selected_artifact_emission_containment_basis",
            "selected_evidence_manifest_basis",
            "selected_portable_verification_basis",
            "authorization_only_posture",
            "one_shot_authorization_posture",
            "authorization_token_posture",
            "no_command_invocation_posture",
            "no_command_execution_posture",
            "no_output_result_success_posture",
            "no_execution_permission_posture",
            "no_execution_approval_posture",
            "no_standing_lane_posture",
            "no_repeat_permission_posture",
            "consumed_token_closed_posture",
            "no_reopen_consumed_request_posture",
            "returned_result_containment_posture",
        )
    ]
    collapse = _first_collapse_block(all_values)
    collapse_key, collapse_code = collapse if collapse else (None, None)
    _check(
        checks,
        "command invocation not created",
        collapse_code != "COMMAND_INVOCATION_CREATED",
        "command invocation is not created",
        collapse_key,
        "COMMAND_INVOCATION_CREATED",
    )
    _check(
        checks,
        "command execution not performed",
        collapse_code != "COMMAND_EXECUTION_PERFORMED",
        "command execution is not performed",
        collapse_key,
        "COMMAND_EXECUTION_PERFORMED",
    )
    _check(checks, "command output not created", collapse_code != "COMMAND_OUTPUT_CREATED", "command output is not created", collapse_key, "COMMAND_OUTPUT_CREATED")
    _check(checks, "command result not created", collapse_code != "COMMAND_RESULT_CREATED", "command result is not created", collapse_key, "COMMAND_RESULT_CREATED")
    _check(checks, "command success not created", collapse_code != "COMMAND_SUCCESS_CREATED", "command success is not created", collapse_key, "COMMAND_SUCCESS_CREATED")
    _check(checks, "execution permission not created", collapse_code != "EXECUTION_PERMISSION_CREATED", "execution permission is not created", collapse_key, "EXECUTION_PERMISSION_CREATED")
    _check(checks, "execution approval not created", collapse_code != "EXECUTION_APPROVAL_CREATED", "execution approval is not created", collapse_key, "EXECUTION_APPROVAL_CREATED")
    _check(checks, "standing invocation lane not created", collapse_code != "STANDING_INVOCATION_LANE_CREATED", "standing invocation lane is not created", collapse_key, "STANDING_INVOCATION_LANE_CREATED")
    _check(checks, "repeat invocation permission not created", collapse_code != "REPEAT_INVOCATION_PERMISSION_CREATED", "repeat invocation permission is not created", collapse_key, "REPEAT_INVOCATION_PERMISSION_CREATED")
    _check(checks, "authorization not invocation", collapse_code != "AUTHORIZATION_TREATED_AS_INVOCATION", "authorization is not invocation", collapse_key, "AUTHORIZATION_TREATED_AS_INVOCATION")
    _check(checks, "authorization not execution", collapse_code != "AUTHORIZATION_TREATED_AS_EXECUTION", "authorization is not execution", collapse_key, "AUTHORIZATION_TREATED_AS_EXECUTION")
    _check(checks, "authorization not command success", collapse_code != "AUTHORIZATION_TREATED_AS_COMMAND_SUCCESS", "authorization is not command success", collapse_key, "AUTHORIZATION_TREATED_AS_COMMAND_SUCCESS")
    _check(checks, "command output not source", collapse_code != "COMMAND_OUTPUT_TREATED_AS_SOURCE", "command output is not source", collapse_key, "COMMAND_OUTPUT_TREATED_AS_SOURCE")
    _check(checks, "command result not authority", collapse_code != "COMMAND_RESULT_TREATED_AS_AUTHORITY", "command result is not authority", collapse_key, "COMMAND_RESULT_TREATED_AS_AUTHORITY")
    _check(checks, "command success not currentness", collapse_code != "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS", "command success is not currentness", collapse_key, "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS")
    _check(checks, "command success not final completion", collapse_code != "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION", "command success is not final completion", collapse_key, "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION")

    full_body_present = any(_contains_forbidden_full_body_key(value) for value in all_values)
    _check(
        checks,
        "raw full prior artifact body not emitted",
        not full_body_present,
        "raw full prior artifact body is not emitted",
        "forbidden full-body key present" if full_body_present else "absent",
        "FULL_PRIOR_ARTIFACT_BODY_EMITTED",
    )
    _check(checks, "artifacts not mutated", collapse_code != "ARTIFACTS_MUTATED", "artifacts are not mutated", collapse_key, "ARTIFACTS_MUTATED")
    _check(checks, "deployment/runtime/public release not created", collapse_code not in {"DEPLOYMENT_CREATED", "RUNTIME_HOSTING_CREATED", "PUBLIC_RELEASE_CREATED"}, "deployment/runtime/public release are not created", collapse_key, collapse_code if collapse_code in {"DEPLOYMENT_CREATED", "RUNTIME_HOSTING_CREATED", "PUBLIC_RELEASE_CREATED"} else None)
    _check(checks, "operation permission/public readiness/final completion not created", collapse_code not in {"OPERATION_PERMISSION_CREATED", "PUBLIC_READINESS_CREATED", "FINAL_COMPLETION_CLAIMED"}, "operation permission/public readiness/final completion are not created", collapse_key, collapse_code if collapse_code in {"OPERATION_PERMISSION_CREATED", "PUBLIC_READINESS_CREATED", "FINAL_COMPLETION_CLAIMED"} else None)
    _check(checks, "continuation/reusable permission/follow-on work not authorized", collapse_code not in {"CONTINUATION_AUTHORIZED", "REUSABLE_PERMISSION_CREATED", "FOLLOW_ON_WORK_AUTHORIZED"}, "continuation/reusable permission/follow-on work are not authorized", collapse_key, collapse_code if collapse_code in {"CONTINUATION_AUTHORIZED", "REUSABLE_PERMISSION_CREATED", "FOLLOW_ON_WORK_AUTHORIZED"} else None)
    _check(checks, "derivative reception/vessel relation/another reception request not authorized", collapse_code not in {"DERIVATIVE_RECEPTION_AUTHORIZED", "VESSEL_RELATION_AUTHORIZED", "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"}, "derivative reception/vessel relation/another reception request are not authorized", collapse_key, collapse_code if collapse_code in {"DERIVATIVE_RECEPTION_AUTHORIZED", "VESSEL_RELATION_AUTHORIZED", "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"} else None)
    _check(checks, "no mutation/replay/merge", collapse_code != "MUTATION_REPLAY_OR_MERGE_DETECTED", "no mutation, replay, or merge", collapse_key, "MUTATION_REPLAY_OR_MERGE_DETECTED")

    non_claim_failure = _first_declared_non_claim_failure(request)
    _check(
        checks,
        "non-claims remain false",
        non_claim_failure is None,
        "required non-claims are present and false",
        non_claim_failure,
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    return checks


def _first_failed_block(checks: Sequence[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if not check.get("passed"):
            code = check.get("block_code") or check.get("failure_code")
            if code:
                return str(code)
    return None


def _determine_outcome_and_block(
    request: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    request_malformed_code: str | None = None,
) -> tuple[str, dict[str, Any]]:
    if request_malformed_code:
        return OUTCOME_BLOCKED, _block(request_malformed_code, "Declared command invocation authorization request is malformed or unreadable.")
    if request.get("command_invocation_authorization_intent") == INTENT_BLOCK:
        return OUTCOME_BLOCKED, _block(
            request.get("block_code") or "COMMAND_INVOCATION_AUTHORIZATION_BLOCKED_BY_REQUEST",
            request.get("block_reason") or "Request explicitly selected blocked command invocation authorization posture.",
        )
    requested = request.get("requested_command_invocation_authorization_outcome")
    if requested is not None and requested not in OUTCOME_FAMILY:
        return OUTCOME_BLOCKED, _block(
            "COMMAND_INVOCATION_AUTHORIZATION_INTENT_UNSUPPORTED",
            "Requested command invocation authorization outcome is unsupported.",
        )
    if requested == OUTCOME_BLOCKED:
        return OUTCOME_BLOCKED, _block(
            request.get("block_code") or "COMMAND_INVOCATION_AUTHORIZATION_BLOCKED_BY_REQUEST",
            request.get("block_reason") or "Requested command invocation authorization outcome is blocked.",
        )
    failed_code = _first_failed_block(checks)
    if failed_code:
        return OUTCOME_BLOCKED, _block(failed_code, f"Command invocation authorization blocked by {failed_code}.")
    if requested in {OUTCOME_NOT_RECORDED, OUTCOME_REQUIRES_ADDITIONAL_BASIS}:
        return str(requested), _block(None, None)
    if request.get("command_invocation_authorization_intent") == INTENT_DO_NOT_RECORD:
        return OUTCOME_NOT_RECORDED, _block(None, None)
    if _present(request.get("additional_basis_context")):
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS, _block(None, None)
    if _present(request.get("not_recorded_basis")):
        return OUTCOME_NOT_RECORDED, _block(None, None)
    return OUTCOME_RECORDED, _block(None, None)


def _counts(checks: Sequence[Mapping[str, Any]]) -> tuple[int, int]:
    passed = sum(1 for check in checks if check.get("passed") is True)
    failed = sum(1 for check in checks if check.get("passed") is not True)
    return passed, failed


def _result_from_request(
    request: Mapping[str, Any],
    *,
    request_malformed_code: str | None = None,
    request_path: str | None = None,
) -> dict[str, Any]:
    checks = _build_checks(request, request_malformed=bool(request_malformed_code))
    outcome, block = _determine_outcome_and_block(request, checks, request_malformed_code)
    passed_count, failed_count = _counts(checks)

    boundary_basis = _mapping_from_basis(request.get("selected_command_invocation_authorization_boundary_basis"))
    review_basis = _mapping_from_basis(request.get("selected_command_execution_review_basis"))
    consumption_basis = _mapping_from_basis(request.get("selected_request_consumption_basis"))
    v2_basis = _mapping_from_basis(request.get("selected_v2_admitted_request_basis"))

    result: dict[str, Any] = {
        "consumed_single_live_command_invocation_request_command_invocation_authorization_metadata": _build_metadata(
            request, outcome
        ),
        "declared_command_invocation_authorization_question": {
            "command_invocation_authorization_request_id": request.get("command_invocation_authorization_request_id"),
            "command_invocation_authorization_question": request.get("command_invocation_authorization_question"),
            "expected_question": CORE_COMMAND_INVOCATION_AUTHORIZATION_QUESTION,
            "command_invocation_authorization_intent": request.get("command_invocation_authorization_intent"),
            "request_path": request_path,
        },
        "selected_command_invocation_authorization_boundary_basis": _basis_section(
            request.get("selected_command_invocation_authorization_boundary_basis"),
            path=request.get("selected_command_invocation_authorization_boundary_result_path"),
            extra={
                "selected_command_invocation_authorization_boundary_result_id": request.get(
                    "selected_command_invocation_authorization_boundary_result_id"
                ),
                "selected_command_invocation_authorization_boundary_result_outcome": _basis_outcome(
                    boundary_basis,
                    request,
                    ("selected_command_invocation_authorization_boundary_result_outcome",),
                ),
                "selected_command_invocation_authorization_boundary_failed_check_count": _basis_failed_count(
                    boundary_basis,
                    request,
                    ("selected_command_invocation_authorization_boundary_failed_check_count",),
                ),
                "authorization_boundary_did_not_create_command_invocation_authorization": True,
                "authorization_boundary_basis_remains_boundary_basis_only": True,
                "authorization_boundary_did_not_create_invocation_execution_output_result_success": True,
                "authorization_boundary_did_not_create_execution_permission_or_approval": True,
                "authorization_boundary_did_not_create_standing_lane_or_repeat_permission": True,
            },
        ),
        "selected_command_invocation_authorization_boundary_terminal_summary_basis": _basis_section(
            request.get("selected_command_invocation_authorization_boundary_terminal_summary_basis"),
            path=request.get("selected_command_invocation_authorization_boundary_terminal_summary_path"),
            extra={
                "terminal_summary_remains_readability_basis_only": True,
                "terminal_summary_does_not_create_command_invocation_authorization": True,
                "terminal_summary_does_not_authorize_invocation_or_execution": True,
            },
        ),
        "selected_command_execution_review_basis": _basis_section(
            request.get("selected_command_execution_review_basis"),
            path=request.get("selected_command_execution_review_result_path"),
            extra={
                "selected_command_execution_review_result_id": request.get("selected_command_execution_review_result_id"),
                "selected_command_execution_review_result_outcome": _basis_outcome(
                    review_basis,
                    request,
                    ("selected_command_execution_review_result_outcome",),
                ),
                "selected_command_execution_review_failed_check_count": _basis_failed_count(
                    review_basis,
                    request,
                    ("selected_command_execution_review_failed_check_count",),
                ),
                "command_execution_review_remains_post_review_pre_authorization_pre_invocation_pre_execution": True,
            },
        ),
        "selected_request_consumption_basis": _basis_section(
            request.get("selected_request_consumption_basis"),
            path=request.get("selected_request_consumption_result_path"),
            extra={
                "selected_request_consumption_result_id": request.get("selected_request_consumption_result_id"),
                "selected_request_consumption_result_outcome": _basis_outcome(
                    consumption_basis,
                    request,
                    ("selected_request_consumption_result_outcome",),
                ),
                "selected_request_consumption_failed_check_count": _basis_failed_count(
                    consumption_basis,
                    request,
                    ("selected_request_consumption_failed_check_count",),
                ),
                "request_consumption_remains_consumed_basis_only": True,
            },
        ),
        "selected_consumed_request_basis": _basis_section(
            request.get("selected_consumed_request_basis"),
            extra={
                "consumed_request_token_remains_closed": _consumed_token_closed(
                    _mapping_from_basis(request.get("selected_consumed_request_basis"))
                ),
                "consumed_request_not_reopened": _consumed_request_not_reopened(
                    _mapping_from_basis(request.get("selected_consumed_request_basis"))
                ),
                "consumed_request_basis_is_not_reusable_permission": True,
                "consumed_request_basis_is_not_command_success": True,
            },
        ),
        "selected_v2_admitted_request_basis": _basis_section(
            request.get("selected_v2_admitted_request_basis"),
            path=request.get("selected_v2_admitted_request_artifact_path"),
            extra={
                "selected_v2_admitted_request_artifact_id": request.get("selected_v2_admitted_request_artifact_id"),
                "selected_v2_admitted_request_outcome": _basis_outcome(
                    v2_basis,
                    request,
                    ("selected_v2_admitted_request_outcome",),
                ),
                "selected_v2_admitted_request_version": _basis_version(
                    v2_basis,
                    request,
                    ("selected_v2_admitted_request_version",),
                ),
                "selected_v2_failed_check_count": _basis_failed_count(
                    v2_basis, request, ("selected_v2_failed_check_count",)
                ),
                "successor_metadata_preserved": _successor_metadata_preserved(v2_basis, request),
                "returned_result_containment_preserved": _returned_result_containment_preserved(v2_basis),
                "v2_remains_lineage_evidence_only": True,
                "v2_does_not_claim_v1_passed": not _v2_claims_v1_passed(
                    _mapping_from_basis(request.get("selected_v1_predecessor_failure_basis")), v2_basis
                ),
            },
        ),
        "selected_v1_predecessor_failure_basis": _basis_section(
            request.get("selected_v1_predecessor_failure_basis"),
            path=request.get("selected_v1_predecessor_artifact_path"),
            extra={
                "selected_v1_predecessor_artifact_id": request.get("selected_v1_predecessor_artifact_id"),
                "selected_v1_predecessor_outcome": request.get("selected_v1_predecessor_outcome"),
                "v1_predecessor_failure_remains_visible": _v1_failure_visible(
                    _mapping_from_basis(request.get("selected_v1_predecessor_failure_basis"))
                ),
                "v1_is_not_repaired": True,
                "v1_is_not_hidden": True,
                "v1_is_not_claimed_passed": True,
                "predecessor_failure_evidence_remains_lineage_evidence_only": True,
            },
        ),
        "selected_command_execution_boundary_basis": _basis_section(
            request.get("selected_command_execution_boundary_basis"),
            path=request.get("selected_command_execution_boundary_result_path"),
            extra={"command_execution_boundary_remains_basis_only": True},
        ),
        "selected_command_report_basis": _basis_section(
            request.get("selected_command_report_basis"),
            path=request.get("selected_command_report_path"),
            extra={"command_report_remains_non_authoritative_report_basis_only": True},
        ),
        "selected_command_implementation_boundary_basis": _basis_section(
            request.get("selected_command_implementation_boundary_basis"),
            path=request.get("selected_command_implementation_boundary_result_path"),
            extra={"command_implementation_boundary_remains_implementation_boundary_basis_only": True},
        ),
        "selected_command_boundary_basis": _basis_section(
            request.get("selected_command_boundary_basis"),
            path=request.get("selected_command_boundary_result_path"),
            extra={"command_boundary_remains_checker_only_boundary_basis": True},
        ),
        "selected_artifact_emission_containment_basis": _basis_section(
            request.get("selected_artifact_emission_containment_basis"),
            path=request.get("selected_artifact_emission_containment_result_path"),
            extra={"artifact_containment_remains_reference_shaped_containment_basis_only": True},
        ),
        "selected_evidence_manifest_basis": _basis_section(
            request.get("selected_evidence_manifest_basis"),
            path=request.get("selected_evidence_manifest_result_path"),
            extra={"evidence_manifest_remains_evidence_definition_basis_only": True},
        ),
        "selected_portable_verification_basis": _basis_section(
            request.get("selected_portable_verification_basis"),
            path=request.get("selected_portable_verification_result_path"),
            extra={"portable_verification_remains_carrier_independent_verification_basis_only": True},
        ),
        "authorization_only_posture": _posture_section(
            request.get("authorization_only_posture"),
            extra={"authorization_only_posture_declared": _present(request.get("authorization_only_posture"))},
        ),
        "one_shot_authorization_posture": _posture_section(
            request.get("one_shot_authorization_posture"),
            extra={"one_shot_authorization_posture_declared": _present(request.get("one_shot_authorization_posture"))},
        ),
        "authorization_token_posture": _posture_section(
            request.get("authorization_token_posture"),
            extra={"authorization_token_posture_declared": _present(request.get("authorization_token_posture"))},
        ),
        "no_command_invocation_posture": _posture_section(
            request.get("no_command_invocation_posture"),
            extra={"command_invocation_not_created": True},
        ),
        "no_command_execution_posture": _posture_section(
            request.get("no_command_execution_posture"),
            extra={"command_execution_not_performed": True},
        ),
        "no_output_result_success_posture": _posture_section(
            request.get("no_output_result_success_posture"),
            extra={"output_result_success_not_created": True},
        ),
        "no_execution_permission_posture": _posture_section(
            request.get("no_execution_permission_posture"),
            extra={"execution_permission_not_created": True},
        ),
        "no_execution_approval_posture": _posture_section(
            request.get("no_execution_approval_posture"),
            extra={"execution_approval_not_created": True},
        ),
        "no_standing_lane_posture": _posture_section(
            request.get("no_standing_lane_posture"),
            extra={"no_standing_invocation_lane": True},
        ),
        "no_repeat_permission_posture": _posture_section(
            request.get("no_repeat_permission_posture"),
            extra={"no_repeat_invocation_permission": True},
        ),
        "consumed_token_closed_posture": _posture_section(
            request.get("consumed_token_closed_posture"),
            extra={"consumed_request_token_remains_closed": True},
        ),
        "no_reopen_consumed_request_posture": _posture_section(
            request.get("no_reopen_consumed_request_posture"),
            extra={"consumed_request_not_reopened": True},
        ),
        "returned_result_containment_posture": _posture_section(
            request.get("returned_result_containment_posture"),
            extra={
                "returned_result_containment_preserved": True,
                "no_raw_full_prior_artifact_body_returned": True,
            },
        ),
        "command_invocation_authorization_scope": _scope_section(
            request.get("command_invocation_authorization_scope"), outcome
        ),
        "command_invocation_authorization_checks": {
            "passed_check_count": passed_count,
            "failed_check_count": failed_count,
            "checks": checks,
        },
        "command_invocation_authorization_statement": _statement(outcome),
        "command_invocation_authorization_non_meaning": _non_meaning(),
        "additional_basis_required": _additional_basis_required(outcome, request),
        "not_recorded_basis": _not_recorded_basis(outcome, request, checks),
        "what_remains_open": _what_remains_open(),
        "non_claims": _default_non_claims(),
        "outcome": outcome,
        "block": block,
    }
    result[
        "consumed_single_live_command_invocation_request_command_invocation_authorization_summary"
    ] = build_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_summary(
        result
    )
    return result


def resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization(
    declared_command_invocation_authorization_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one bounded command invocation authorization request mapping."""
    if declared_command_invocation_authorization_request is None:
        request = {
            "command_invocation_authorization_request_id": "undeclared",
            "command_invocation_authorization_intent": INTENT_RECORD,
            "declared_non_claims": {},
        }
        return _result_from_request(request)
    if not isinstance(declared_command_invocation_authorization_request, Mapping):
        request = {
            "command_invocation_authorization_request_id": "malformed",
            "command_invocation_authorization_intent": INTENT_BLOCK,
            "declared_non_claims": {},
        }
        return _result_from_request(
            request,
            request_malformed_code="DECLARED_COMMAND_INVOCATION_AUTHORIZATION_REQUEST_MALFORMED",
        )
    request = _deepcopy(dict(declared_command_invocation_authorization_request))
    return _result_from_request(request)


def resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_from_path(
    declared_command_invocation_authorization_request_path: Path | str,
) -> dict:
    """Resolve one bounded command invocation authorization request JSON object from a path."""
    path = Path(declared_command_invocation_authorization_request_path)
    try:
        raw = path.read_text(encoding="utf-8")
        loaded = json.loads(raw)
    except (OSError, json.JSONDecodeError) as exc:
        request = {
            "command_invocation_authorization_request_id": path.stem or "unreadable",
            "command_invocation_authorization_intent": INTENT_BLOCK,
            "declared_non_claims": {},
            "block_reason": str(exc),
        }
        return _result_from_request(
            request,
            request_malformed_code="DECLARED_COMMAND_INVOCATION_AUTHORIZATION_REQUEST_UNREADABLE",
            request_path=str(path),
        )
    if not isinstance(loaded, Mapping):
        request = {
            "command_invocation_authorization_request_id": path.stem or "malformed",
            "command_invocation_authorization_intent": INTENT_BLOCK,
            "declared_non_claims": {},
        }
        return _result_from_request(
            request,
            request_malformed_code="DECLARED_COMMAND_INVOCATION_AUTHORIZATION_REQUEST_MALFORMED",
            request_path=str(path),
        )
    request = _deepcopy(dict(loaded))
    return _result_from_request(request, request_path=str(path))


def build_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a compact summary from a command invocation authorization result."""
    metadata = _mapping_from_basis(
        result.get("consumed_single_live_command_invocation_request_command_invocation_authorization_metadata")
    )
    question = _mapping_from_basis(result.get("declared_command_invocation_authorization_question"))
    checks = _mapping_from_basis(result.get("command_invocation_authorization_checks"))
    statement = _mapping_from_basis(result.get("command_invocation_authorization_statement"))
    block = _mapping_from_basis(result.get("block"))
    boundary_basis = _mapping_from_basis(result.get("selected_command_invocation_authorization_boundary_basis"))
    review_basis = _mapping_from_basis(result.get("selected_command_execution_review_basis"))
    consumption_basis = _mapping_from_basis(result.get("selected_request_consumption_basis"))
    v2_basis = _mapping_from_basis(result.get("selected_v2_admitted_request_basis"))
    non_claims = _mapping_from_basis(result.get("non_claims"))

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("code"),
        "block_reason": block.get("reason"),
        "command_invocation_authorization_request_id": question.get("command_invocation_authorization_request_id")
        or metadata.get("command_invocation_authorization_request_id"),
        "command_invocation_authorization_question": question.get("command_invocation_authorization_question"),
        "command_invocation_authorization_intent": question.get("command_invocation_authorization_intent"),
        "passed_check_count": checks.get("passed_check_count", 0),
        "failed_check_count": checks.get("failed_check_count", 0),
        "command_invocation_authorization_recorded": statement.get("command_invocation_authorization_recorded", False),
        "command_invocation_authorization_created": statement.get("command_invocation_authorization_created", False),
        "single_command_invocation_authorization_created": statement.get(
            "single_command_invocation_authorization_created", False
        ),
        "command_invocation_authorization_token_created": statement.get(
            "command_invocation_authorization_token_created", False
        ),
        "authorization_token_is_one_shot": statement.get("authorization_token_is_one_shot", False),
        "authorization_basis_preserved": statement.get("authorization_basis_preserved", False),
        "invocation_requires_separate_bounded_step": statement.get(
            "invocation_requires_separate_bounded_step", False
        ),
        "execution_still_not_authorized": statement.get("execution_still_not_authorized", False),
        "consumed_request_token_remains_closed": statement.get("consumed_request_token_remains_closed", False),
        "v1_predecessor_failure_preserved": statement.get("v1_predecessor_failure_preserved", False),
        "returned_result_containment_preserved": statement.get("returned_result_containment_preserved", False),
        "not_recorded": result.get("outcome") == OUTCOME_NOT_RECORDED,
        "requires_additional_basis": result.get("outcome") == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "selected_command_invocation_authorization_boundary_outcome": boundary_basis.get(
            "selected_command_invocation_authorization_boundary_result_outcome"
        )
        or _find_first(boundary_basis, ("outcome",)),
        "selected_command_invocation_authorization_boundary_failed_check_count": _first_not_none(
            boundary_basis.get("selected_command_invocation_authorization_boundary_failed_check_count"),
            _find_first(boundary_basis, ("failed_check_count",)),
        ),
        "selected_command_execution_review_outcome": review_basis.get("selected_command_execution_review_result_outcome")
        or _find_first(review_basis, ("outcome",)),
        "selected_command_execution_review_failed_check_count": _first_not_none(
            review_basis.get("selected_command_execution_review_failed_check_count"),
            _find_first(review_basis, ("failed_check_count",)),
        ),
        "selected_request_consumption_outcome": consumption_basis.get("selected_request_consumption_result_outcome")
        or _find_first(consumption_basis, ("outcome",)),
        "selected_request_consumption_failed_check_count": _first_not_none(
            consumption_basis.get("selected_request_consumption_failed_check_count"),
            _find_first(consumption_basis, ("failed_check_count",)),
        ),
        "selected_v2_admitted_request_outcome": v2_basis.get("selected_v2_admitted_request_outcome")
        or _find_first(v2_basis, ("outcome",)),
        "selected_v2_admitted_request_version": v2_basis.get("selected_v2_admitted_request_version")
        or _find_first(v2_basis, ("result_version", "version")),
        "selected_v2_failed_check_count": _first_not_none(
            v2_basis.get("selected_v2_failed_check_count"),
            _find_first(v2_basis, ("failed_check_count",)),
        ),
        "command_invocation_not_created": non_claims.get("command_invocation_created") is False,
        "command_execution_not_performed": non_claims.get("command_execution_performed") is False,
        "command_output_result_success_not_created": non_claims.get("command_output_created") is False
        and non_claims.get("command_result_created") is False
        and non_claims.get("command_success_created") is False,
        "execution_permission_not_created": non_claims.get("execution_permission_created") is False,
        "execution_approval_not_created": non_claims.get("execution_approval_created") is False,
        "no_standing_lane": non_claims.get("standing_invocation_lane_created") is False,
        "no_repeat_permission": non_claims.get("repeat_invocation_permission_created") is False,
        "consumed_request_not_reopened": non_claims.get("consumed_request_reopened") is False,
        "authorization_not_invocation": non_claims.get("authorization_treated_as_invocation") is False,
        "authorization_not_execution": non_claims.get("authorization_treated_as_execution") is False,
        "authorization_not_command_success": non_claims.get("authorization_treated_as_command_success") is False,
        "v1_not_repaired_hidden_claimed_passed": non_claims.get("v1_repaired") is False
        and non_claims.get("v1_hidden") is False
        and non_claims.get("v1_claimed_passed") is False,
        "no_raw_full_prior_artifact_body_returned": non_claims.get("raw_full_prior_artifact_body_returned") is False,
        "no_artifact_mutation": non_claims.get("prior_artifacts_mutated") is False,
        "no_deployment_runtime_public_release": non_claims.get("deployment_created") is False
        and non_claims.get("runtime_hosting_created") is False
        and non_claims.get("public_release_created") is False,
        "no_operation_permission_public_readiness_final_completion": non_claims.get("operation_permission_created")
        is False
        and non_claims.get("public_launch_readiness_created") is False
        and non_claims.get("final_completion_claimed") is False,
        "no_continuation_publication_flow_reusable_permission": non_claims.get("continuation_authorized") is False
        and non_claims.get("publication_flow_opened") is False
        and non_claims.get("reusable_permission_created") is False,
        "no_derivative_reception_vessel_relation_another_reception_request_follow_on_work": non_claims.get(
            "derivative_reception_authorized"
        )
        is False
        and non_claims.get("vessel_relation_authorized") is False
        and non_claims.get("another_reception_request_authorized") is False
        and non_claims.get("follow_on_work_authorized") is False,
        "key_non_claims": _sanitize_reference_shape(dict(non_claims)),
    }


def _unique_output_path(path: Path) -> Path:
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


def write_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive command invocation authorization result JSON file."""
    if not isinstance(result, Mapping):
        raise PortableSourceBodyVerificationConsumedSingleLiveCommandInvocationRequestCommandInvocationAuthorizationError(
            "Command invocation authorization result must be a mapping."
        )
    result_copy = _sanitize_reference_shape(result)
    if output_path is None:
        metadata = _mapping_from_basis(
            result_copy.get(
                "consumed_single_live_command_invocation_request_command_invocation_authorization_metadata"
            )
        )
        request_id = metadata.get("command_invocation_authorization_request_id")
        if not request_id:
            question = _mapping_from_basis(result_copy.get("declared_command_invocation_authorization_question"))
            request_id = question.get("command_invocation_authorization_request_id")
        filename = (
            f"{_safe_component(request_id, 'command_invocation_authorization_request')}__"
            "consumed_single_live_command_invocation_request_command_invocation_authorization_result.json"
        )
        path = PORTABLE_SOURCE_BODY_VERIFICATION_CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_AUTHORIZATION_ROOT / filename
    else:
        path = Path(output_path)
        if path.is_dir():
            metadata = _mapping_from_basis(
                result_copy.get(
                    "consumed_single_live_command_invocation_request_command_invocation_authorization_metadata"
                )
            )
            filename = (
                f"{_safe_component(metadata.get('command_invocation_authorization_request_id'), 'command_invocation_authorization_request')}__"
                "consumed_single_live_command_invocation_request_command_invocation_authorization_result.json"
            )
            path = path / filename
    path = _unique_output_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result_copy, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def build_declared_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_request(
    command_invocation_authorization_request_id: str,
    command_invocation_authorization_question: str,
    selected_command_invocation_authorization_boundary_basis: Mapping[str, Any] | str,
    selected_command_invocation_authorization_boundary_terminal_summary_basis: Mapping[str, Any] | str,
    selected_command_execution_review_basis: Mapping[str, Any] | str,
    selected_request_consumption_basis: Mapping[str, Any] | str,
    selected_consumed_request_basis: Mapping[str, Any] | str,
    selected_v2_admitted_request_basis: Mapping[str, Any] | str,
    selected_v1_predecessor_failure_basis: Mapping[str, Any] | str,
    selected_command_execution_boundary_basis: Mapping[str, Any] | str,
    selected_command_report_basis: Mapping[str, Any] | str,
    selected_command_implementation_boundary_basis: Mapping[str, Any] | str,
    selected_command_boundary_basis: Mapping[str, Any] | str,
    selected_artifact_emission_containment_basis: Mapping[str, Any] | str,
    selected_evidence_manifest_basis: Mapping[str, Any] | str,
    selected_portable_verification_basis: Mapping[str, Any] | str,
    authorization_only_posture: Mapping[str, Any] | str,
    one_shot_authorization_posture: Mapping[str, Any] | str,
    authorization_token_posture: Mapping[str, Any] | str,
    no_command_invocation_posture: Mapping[str, Any] | str,
    no_command_execution_posture: Mapping[str, Any] | str,
    no_output_result_success_posture: Mapping[str, Any] | str,
    no_execution_permission_posture: Mapping[str, Any] | str,
    no_execution_approval_posture: Mapping[str, Any] | str,
    no_standing_lane_posture: Mapping[str, Any] | str,
    no_repeat_permission_posture: Mapping[str, Any] | str,
    consumed_token_closed_posture: Mapping[str, Any] | str,
    no_reopen_consumed_request_posture: Mapping[str, Any] | str,
    returned_result_containment_posture: Mapping[str, Any] | str,
    command_invocation_authorization_scope: Sequence[str] | Mapping[str, Any],
    command_invocation_authorization_intent: str = INTENT_RECORD,
    *,
    selected_command_invocation_authorization_boundary_result_path: str | None = None,
    selected_command_invocation_authorization_boundary_result_id: str | None = None,
    selected_command_invocation_authorization_boundary_result_outcome: str | None = None,
    selected_command_invocation_authorization_boundary_failed_check_count: int | None = None,
    selected_command_execution_review_result_path: str | None = None,
    selected_command_execution_review_result_id: str | None = None,
    selected_command_execution_review_result_outcome: str | None = None,
    selected_command_execution_review_failed_check_count: int | None = None,
    selected_request_consumption_result_path: str | None = None,
    selected_request_consumption_result_id: str | None = None,
    selected_request_consumption_result_outcome: str | None = None,
    selected_request_consumption_failed_check_count: int | None = None,
    selected_v2_admitted_request_artifact_path: str | None = None,
    selected_v2_admitted_request_artifact_id: str | None = None,
    selected_v2_admitted_request_outcome: str | None = None,
    selected_v2_admitted_request_version: str | None = None,
    selected_v2_failed_check_count: int | None = None,
    requested_command_invocation_authorization_outcome: str = OUTCOME_RECORDED,
    additional_basis_context: Mapping[str, Any] | None = None,
    not_recorded_basis: Mapping[str, Any] | str | None = None,
) -> dict:
    """Build a declared command invocation authorization request with false non-claims."""
    request = {
        "command_invocation_authorization_request_id": command_invocation_authorization_request_id,
        "command_invocation_authorization_question": command_invocation_authorization_question,
        "command_invocation_authorization_intent": command_invocation_authorization_intent,
        "selected_command_invocation_authorization_boundary_basis": _deepcopy(
            selected_command_invocation_authorization_boundary_basis
        ),
        "selected_command_invocation_authorization_boundary_terminal_summary_basis": _deepcopy(
            selected_command_invocation_authorization_boundary_terminal_summary_basis
        ),
        "selected_command_execution_review_basis": _deepcopy(selected_command_execution_review_basis),
        "selected_request_consumption_basis": _deepcopy(selected_request_consumption_basis),
        "selected_consumed_request_basis": _deepcopy(selected_consumed_request_basis),
        "selected_v2_admitted_request_basis": _deepcopy(selected_v2_admitted_request_basis),
        "selected_v1_predecessor_failure_basis": _deepcopy(selected_v1_predecessor_failure_basis),
        "selected_command_execution_boundary_basis": _deepcopy(selected_command_execution_boundary_basis),
        "selected_command_report_basis": _deepcopy(selected_command_report_basis),
        "selected_command_implementation_boundary_basis": _deepcopy(
            selected_command_implementation_boundary_basis
        ),
        "selected_command_boundary_basis": _deepcopy(selected_command_boundary_basis),
        "selected_artifact_emission_containment_basis": _deepcopy(selected_artifact_emission_containment_basis),
        "selected_evidence_manifest_basis": _deepcopy(selected_evidence_manifest_basis),
        "selected_portable_verification_basis": _deepcopy(selected_portable_verification_basis),
        "authorization_only_posture": _deepcopy(authorization_only_posture),
        "one_shot_authorization_posture": _deepcopy(one_shot_authorization_posture),
        "authorization_token_posture": _deepcopy(authorization_token_posture),
        "no_command_invocation_posture": _deepcopy(no_command_invocation_posture),
        "no_command_execution_posture": _deepcopy(no_command_execution_posture),
        "no_output_result_success_posture": _deepcopy(no_output_result_success_posture),
        "no_execution_permission_posture": _deepcopy(no_execution_permission_posture),
        "no_execution_approval_posture": _deepcopy(no_execution_approval_posture),
        "no_standing_lane_posture": _deepcopy(no_standing_lane_posture),
        "no_repeat_permission_posture": _deepcopy(no_repeat_permission_posture),
        "consumed_token_closed_posture": _deepcopy(consumed_token_closed_posture),
        "no_reopen_consumed_request_posture": _deepcopy(no_reopen_consumed_request_posture),
        "returned_result_containment_posture": _deepcopy(returned_result_containment_posture),
        "command_invocation_authorization_scope": _deepcopy(command_invocation_authorization_scope),
        "declared_non_claims": _default_non_claims(),
        "requested_command_invocation_authorization_outcome": requested_command_invocation_authorization_outcome,
    }
    optional_values = {
        "selected_command_invocation_authorization_boundary_result_path": selected_command_invocation_authorization_boundary_result_path,
        "selected_command_invocation_authorization_boundary_result_id": selected_command_invocation_authorization_boundary_result_id,
        "selected_command_invocation_authorization_boundary_result_outcome": selected_command_invocation_authorization_boundary_result_outcome,
        "selected_command_invocation_authorization_boundary_failed_check_count": selected_command_invocation_authorization_boundary_failed_check_count,
        "selected_command_execution_review_result_path": selected_command_execution_review_result_path,
        "selected_command_execution_review_result_id": selected_command_execution_review_result_id,
        "selected_command_execution_review_result_outcome": selected_command_execution_review_result_outcome,
        "selected_command_execution_review_failed_check_count": selected_command_execution_review_failed_check_count,
        "selected_request_consumption_result_path": selected_request_consumption_result_path,
        "selected_request_consumption_result_id": selected_request_consumption_result_id,
        "selected_request_consumption_result_outcome": selected_request_consumption_result_outcome,
        "selected_request_consumption_failed_check_count": selected_request_consumption_failed_check_count,
        "selected_v2_admitted_request_artifact_path": selected_v2_admitted_request_artifact_path,
        "selected_v2_admitted_request_artifact_id": selected_v2_admitted_request_artifact_id,
        "selected_v2_admitted_request_outcome": selected_v2_admitted_request_outcome,
        "selected_v2_admitted_request_version": selected_v2_admitted_request_version,
        "selected_v2_failed_check_count": selected_v2_failed_check_count,
        "additional_basis_context": _deepcopy(additional_basis_context) if additional_basis_context is not None else None,
        "not_recorded_basis": _deepcopy(not_recorded_basis) if not_recorded_basis is not None else None,
    }
    for key, value in optional_values.items():
        if value is not None:
            request[key] = value
    return request
