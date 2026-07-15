"""Bounded consumed-request command invocation boundary resolver.

This module records command invocation boundary conditions only. It may record
that a one-shot command invocation authorization token is preserved for one
future command invocation step, but it does not invoke a command, execute a
command, create command output, create command result, create command success,
create execution permission, create execution approval, spend the authorization
token, reopen the consumed request token, create a standing invocation lane, or
create repeat invocation permission.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class PortableSourceBodyVerificationConsumedSingleLiveCommandInvocationRequestCommandInvocationBoundaryError(
    Exception
):
    """Raised for hard command-invocation-boundary resolver failures."""


RESOLVER_MODULE = (
    "resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_"
    "command_invocation_boundary"
)
RESULT_VERSION = "0.1.0"
RESULT_TYPE = (
    "portable_source_body_verification_consumed_single_live_command_invocation_request_"
    "command_invocation_boundary_result"
)

PORTABLE_SOURCE_BODY_VERIFICATION_CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_BOUNDARY_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_boundary"
)
OUTPUT_ROOT = (
    PORTABLE_SOURCE_BODY_VERIFICATION_CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_BOUNDARY_ROOT
)

CORE_COMMAND_INVOCATION_BOUNDARY_QUESTION = (
    "Can the one-shot command invocation authorization token be bounded for one future command "
    "invocation step without invoking the command, executing the command, creating command "
    "output, command result, command success, execution permission, execution approval, standing "
    "invocation lane, repeat permission, authority, currentness, final completion, continuation, "
    "reusable permission, derivative reception, vessel relation, another reception request, or "
    "follow-on work?"
)

INTENT_RECORD = "RECORD_CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_BOUNDARY"
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_BOUNDARY"
)
INTENT_BLOCK = "BLOCK_CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_BOUNDARY"
SUPPORTED_INTENTS = frozenset({INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK})

OUTCOME_RECORDED = "CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_BOUNDARY_RECORDED"
OUTCOME_NOT_RECORDED = (
    "CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_BOUNDARY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_BOUNDARY_BLOCKED"
OUTCOME_FAMILY = frozenset(
    {
        OUTCOME_RECORDED,
        OUTCOME_NOT_RECORDED,
        OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        OUTCOME_BLOCKED,
    }
)

COMMAND_INVOCATION_AUTHORIZATION_OUTCOME = (
    "CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_AUTHORIZATION_RECORDED"
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

SUPPORTED_COMMAND_INVOCATION_BOUNDARY_SCOPE = (
    "COMMAND_INVOCATION_BOUNDARY_ONLY",
    "ONE_FUTURE_COMMAND_INVOCATION_STEP_ONLY",
    "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_PRESERVED",
    "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_NOT_SPENT",
    "COMMAND_INVOCATION_NOT_CREATED",
    "COMMAND_EXECUTION_NOT_PERFORMED",
    "COMMAND_OUTPUT_NOT_CREATED",
    "COMMAND_RESULT_NOT_CREATED",
    "COMMAND_SUCCESS_NOT_CREATED",
    "EXECUTION_PERMISSION_NOT_CREATED",
    "EXECUTION_APPROVAL_NOT_CREATED",
    "NO_STANDING_INVOCATION_LANE_CREATED",
    "NO_REPEAT_INVOCATION_PERMISSION_CREATED",
    "INVOCATION_BOUNDARY_IS_NOT_INVOCATION",
    "INVOCATION_BOUNDARY_IS_NOT_EXECUTION",
    "INVOCATION_BOUNDARY_IS_NOT_COMMAND_SUCCESS",
    "AUTHORIZATION_TOKEN_IS_NOT_INVOCATION",
    "AUTHORIZATION_TOKEN_IS_NOT_COMMAND_SUCCESS",
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
SUPPORTED_COMMAND_INVOCATION_BOUNDARY_SCOPE_SET = frozenset(
    SUPPORTED_COMMAND_INVOCATION_BOUNDARY_SCOPE
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
    "authorization_token_spent_here",
    "standing_invocation_lane_created",
    "repeat_invocation_permission_created",
    "invocation_boundary_treated_as_invocation",
    "invocation_boundary_treated_as_execution",
    "invocation_boundary_treated_as_command_success",
    "authorization_token_treated_as_invocation",
    "authorization_token_treated_as_command_success",
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
    "command_invocation_boundary_recorded",
    "one_future_command_invocation_step_declared",
    "command_invocation_authorization_token_preserved",
    "authorization_token_remains_one_shot",
    "authorization_token_not_spent",
    "invocation_still_not_created",
    "execution_still_not_performed",
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
FULL_BODY_OMISSION_MARKER = "[omitted: full prior artifact body is not returned]"

BLOCK_CODES = frozenset(
    {
        "DECLARED_COMMAND_INVOCATION_BOUNDARY_REQUEST_MALFORMED",
        "DECLARED_COMMAND_INVOCATION_BOUNDARY_REQUEST_UNREADABLE",
        "COMMAND_INVOCATION_BOUNDARY_QUESTION_UNDECLARED",
        "COMMAND_INVOCATION_BOUNDARY_INTENT_UNSUPPORTED",
        "COMMAND_INVOCATION_AUTHORIZATION_BASIS_MISSING",
        "COMMAND_INVOCATION_AUTHORIZATION_NOT_RECORDED",
        "COMMAND_INVOCATION_AUTHORIZATION_FAILED_CHECKS_PRESENT",
        "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_MISSING",
        "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_NOT_ONE_SHOT",
        "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_SPENT_HERE",
        "COMMAND_INVOCATION_AUTHORIZATION_TERMINAL_SUMMARY_MISSING",
        "COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_BASIS_MISSING",
        "COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_NOT_RECORDED",
        "COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_FAILED_CHECKS_PRESENT",
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
        "INVOCATION_BOUNDARY_ONLY_POSTURE_MISSING",
        "ONE_FUTURE_INVOCATION_STEP_POSTURE_MISSING",
        "AUTHORIZATION_TOKEN_PRESERVED_POSTURE_MISSING",
        "AUTHORIZATION_TOKEN_NOT_SPENT_POSTURE_MISSING",
        "NO_STANDING_LANE_POSTURE_MISSING",
        "NO_REPEAT_PERMISSION_POSTURE_MISSING",
        "UNSUPPORTED_COMMAND_INVOCATION_BOUNDARY_SCOPE",
        "COMMAND_INVOCATION_CREATED",
        "COMMAND_EXECUTION_PERFORMED",
        "COMMAND_OUTPUT_CREATED",
        "COMMAND_RESULT_CREATED",
        "COMMAND_SUCCESS_CREATED",
        "EXECUTION_PERMISSION_CREATED",
        "EXECUTION_APPROVAL_CREATED",
        "STANDING_INVOCATION_LANE_CREATED",
        "REPEAT_INVOCATION_PERMISSION_CREATED",
        "INVOCATION_BOUNDARY_TREATED_AS_INVOCATION",
        "INVOCATION_BOUNDARY_TREATED_AS_EXECUTION",
        "INVOCATION_BOUNDARY_TREATED_AS_COMMAND_SUCCESS",
        "AUTHORIZATION_TOKEN_TREATED_AS_INVOCATION",
        "AUTHORIZATION_TOKEN_TREATED_AS_COMMAND_SUCCESS",
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
        "COMMAND_INVOCATION_BOUNDARY_BLOCKED_BY_REQUEST",
    }
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _deepcopy(value: Any) -> Any:
    return copy.deepcopy(value)


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
    chars = [char if char.isalnum() or char in {"-", "_", "."} else "_" for char in text]
    return "".join(chars).strip("._") or fallback


def _contains_forbidden_full_body_key(value: Any) -> bool:
    if isinstance(value, Mapping):
        for key, item in value.items():
            if str(key) in FORBIDDEN_FULL_BODY_KEYS:
                return True
            if _contains_forbidden_full_body_key(item):
                return True
    elif isinstance(value, list):
        return any(_contains_forbidden_full_body_key(item) for item in value)
    return False


def _sanitize_reference_shape(value: Any) -> Any:
    if isinstance(value, Mapping):
        sanitized: dict[str, Any] = {}
        for key, item in value.items():
            key_text = str(key)
            if key_text in FORBIDDEN_FULL_BODY_KEYS:
                sanitized[key_text] = FULL_BODY_OMISSION_MARKER
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
        section = {"basis_reference": repr(value), "basis_malformed": True}
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


def _find_truthy(mapping: Mapping[str, Any], keys: Sequence[str]) -> bool:
    for key in keys:
        if _find_first(mapping, (key,)) is True:
            return True
    return False


def _basis_declared(value: Any) -> bool:
    return isinstance(value, Mapping) and bool(value)


def _basis_outcome(
    basis: Mapping[str, Any],
    request: Mapping[str, Any],
    request_keys: Sequence[str],
) -> Any:
    for key in request_keys:
        if key in request:
            return request[key]
    return _find_first(basis, ("outcome", "result_outcome", "selected_outcome", "selected_result_outcome"))


def _basis_failed_count(
    basis: Mapping[str, Any],
    request: Mapping[str, Any],
    request_keys: Sequence[str],
) -> int | None:
    for key in request_keys:
        if key in request:
            return _to_int(request[key])
    value = _find_first(
        basis,
        ("failed_check_count", "failed_checks_count", "failed_checks", "selected_failed_check_count"),
    )
    if isinstance(value, list):
        return len(value)
    return _to_int(value)


def _basis_version(
    basis: Mapping[str, Any],
    request: Mapping[str, Any],
    request_keys: Sequence[str],
) -> Any:
    for key in request_keys:
        if key in request:
            return request[key]
    return _find_first(basis, ("result_version", "version", "selected_version", "artifact_version"))


def _authorization_token_created(basis: Mapping[str, Any], request: Mapping[str, Any]) -> bool:
    if "selected_command_invocation_authorization_token_created" in request:
        return request["selected_command_invocation_authorization_token_created"] is True
    return _find_truthy(
        basis,
        (
            "command_invocation_authorization_token_created",
            "single_command_invocation_authorization_created",
            "authorization_token_created",
        ),
    )


def _authorization_token_one_shot(basis: Mapping[str, Any], request: Mapping[str, Any]) -> bool:
    if "selected_command_invocation_authorization_token_is_one_shot" in request:
        return request["selected_command_invocation_authorization_token_is_one_shot"] is True
    return _find_truthy(
        basis,
        (
            "authorization_token_is_one_shot",
            "command_invocation_authorization_token_is_one_shot",
            "authorization_token_one_shot",
        ),
    )


def _authorization_token_spent(value: Mapping[str, Any]) -> bool:
    return _find_truthy(
        value,
        (
            "authorization_token_spent_here",
            "authorization_token_spent",
            "command_invocation_authorization_token_spent",
            "authorization_token_consumed",
            "authorization_token_discharged",
            "authorization_token_reused",
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
        ("successor_metadata_preserved", "v2_successor_metadata_preserved", "successor_metadata_declared"),
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
        ("consumed_request_token_remains_closed", "consumption_token_closed", "consumed_token_closed", "token_closed"),
    )


def _consumed_request_not_reopened(basis: Mapping[str, Any]) -> bool:
    if _find_truthy(basis, ("consumed_request_reopened", "request_reopened", "token_reopened")):
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
    ) or _find_truthy(v2_basis, ("v2_claims_v1_passed", "v1_claimed_passed", "v1_passed"))


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
    return bool(values) and all(value in SUPPORTED_COMMAND_INVOCATION_BOUNDARY_SCOPE_SET for value in values)


def _default_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _declared_non_claims(request: Mapping[str, Any]) -> Mapping[str, Any]:
    value = request.get("declared_non_claims")
    if isinstance(value, Mapping):
        return value
    return {}


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
    ("authorization_token_spent_here", "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_SPENT_HERE"),
    ("authorization_token_spent", "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_SPENT_HERE"),
    ("command_invocation_authorization_token_spent", "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_SPENT_HERE"),
    ("standing_invocation_lane_created", "STANDING_INVOCATION_LANE_CREATED"),
    ("repeat_invocation_permission_created", "REPEAT_INVOCATION_PERMISSION_CREATED"),
    ("invocation_boundary_treated_as_invocation", "INVOCATION_BOUNDARY_TREATED_AS_INVOCATION"),
    ("invocation_boundary_treated_as_execution", "INVOCATION_BOUNDARY_TREATED_AS_EXECUTION"),
    ("invocation_boundary_treated_as_command_success", "INVOCATION_BOUNDARY_TREATED_AS_COMMAND_SUCCESS"),
    ("authorization_token_treated_as_invocation", "AUTHORIZATION_TOKEN_TREATED_AS_INVOCATION"),
    ("authorization_token_treated_as_command_success", "AUTHORIZATION_TOKEN_TREATED_AS_COMMAND_SUCCESS"),
    ("command_output_became_source", "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
    ("command_result_became_authority", "COMMAND_RESULT_TREATED_AS_AUTHORITY"),
    ("command_success_created_currentness", "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
    ("command_success_claimed_final_completion", "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
    ("prior_artifacts_mutated", "ARTIFACTS_MUTATED"),
    ("artifacts_mutated", "ARTIFACTS_MUTATED"),
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
            if any(_find_truthy(value, (key,)) for key in ("mutation_performed", "replay_performed", "merge_performed")):
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
    request_id = str(request.get("command_invocation_boundary_request_id") or "undeclared")
    result_id = (
        f"{request_id}__consumed_single_live_command_invocation_request_"
        "command_invocation_boundary_result"
    )
    return {
        "consumed_single_live_command_invocation_request_command_invocation_boundary_result_id": result_id,
        "consumed_single_live_command_invocation_request_command_invocation_boundary_result_type": RESULT_TYPE,
        "consumed_single_live_command_invocation_request_command_invocation_boundary_result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
        "command_invocation_boundary_request_id": request_id,
        "requested_outcome": request.get("requested_command_invocation_boundary_outcome"),
        "outcome": outcome,
    }


def _statement(outcome: str) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    statement = {key: recorded for key in ALLOWED_TRUE_RECORDED_FIELDS}
    statement.update(_default_non_claims())
    statement["command_invocation_boundary_not_recorded"] = outcome == OUTCOME_NOT_RECORDED
    statement["command_invocation_boundary_requires_additional_basis"] = (
        outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    )
    statement["command_invocation_boundary_blocked"] = outcome == OUTCOME_BLOCKED
    statement["command_invocation_boundary_is_not_command_invocation"] = True
    statement["command_invocation_boundary_is_not_command_execution"] = True
    statement["command_invocation_boundary_is_not_command_output"] = True
    statement["command_invocation_boundary_is_not_command_result"] = True
    statement["command_invocation_boundary_is_not_command_success"] = True
    statement["command_invocation_boundary_is_not_execution_permission"] = True
    statement["command_invocation_boundary_is_not_execution_approval"] = True
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
        "command_invocation_authorization_token_spent",
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
    return {f"command_invocation_boundary_does_not_mean_{name}": True for name in names}


def _additional_basis_required(outcome: str, request: Mapping[str, Any]) -> dict[str, Any]:
    requires = outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    return {
        "requires_additional_basis": requires,
        "additional_basis_context": _sanitize_reference_shape(request.get("additional_basis_context") or {}),
        "missing_basis_not_scheduled": True,
        "missing_basis_not_authorized": True,
        "missing_basis_not_executed": True,
    }


def _not_recorded_basis(outcome: str, request: Mapping[str, Any], checks: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    failed_checks = [check for check in checks if not check.get("passed")]
    return {
        "not_recorded": outcome == OUTCOME_NOT_RECORDED,
        "not_recorded_basis": _sanitize_reference_shape(request.get("not_recorded_basis") or {}),
        "failed_checks": _sanitize_reference_shape(failed_checks if outcome == OUTCOME_NOT_RECORDED else []),
        "not_recorded_does_not_mutate": True,
        "not_recorded_does_not_repair": True,
        "not_recorded_does_not_invoke_command": True,
        "not_recorded_does_not_execute_command": True,
        "not_recorded_does_not_spend_authorization_token": True,
        "not_recorded_does_not_authorize_next_work": True,
    }


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "command_invocation_boundary_test",
            "command_invocation_boundary_live_artifact",
            "actual_command_invocation",
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
        ],
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }


def _scope_section(scope: Any, outcome: str) -> dict[str, Any]:
    values = _scope_values(scope)
    unsupported = [value for value in values if value not in SUPPORTED_COMMAND_INVOCATION_BOUNDARY_SCOPE_SET]
    return {
        "selected_scope_values": values,
        "supported_scope_values": list(SUPPORTED_COMMAND_INVOCATION_BOUNDARY_SCOPE),
        "unsupported_scope_values": unsupported,
        "all_selected_scope_values_supported": not unsupported and bool(values),
        "command_invocation_boundary_only": "COMMAND_INVOCATION_BOUNDARY_ONLY" in values,
        "one_future_command_invocation_step_only": "ONE_FUTURE_COMMAND_INVOCATION_STEP_ONLY" in values,
        "command_invocation_authorization_token_preserved": outcome == OUTCOME_RECORDED,
        "command_invocation_authorization_token_not_spent": True,
        "command_invocation_not_created": True,
        "command_execution_not_performed": True,
        "command_output_result_success_not_created": True,
        "execution_permission_not_created": True,
        "execution_approval_not_created": True,
        "no_standing_invocation_lane": True,
        "no_repeat_invocation_permission": True,
        "invocation_boundary_is_not_invocation": True,
        "invocation_boundary_is_not_execution": True,
        "invocation_boundary_is_not_command_success": True,
        "authorization_token_is_not_invocation": True,
        "authorization_token_is_not_command_success": True,
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
            "declared command invocation boundary request mapping",
            False,
            "declared request is a mapping",
            "malformed",
            "DECLARED_COMMAND_INVOCATION_BOUNDARY_REQUEST_MALFORMED",
        )
        return checks

    auth_basis = _mapping_from_basis(request.get("selected_command_invocation_authorization_basis"))
    auth_summary = request.get("selected_command_invocation_authorization_terminal_summary_basis")
    auth_boundary_basis = _mapping_from_basis(request.get("selected_command_invocation_authorization_boundary_basis"))
    review_basis = _mapping_from_basis(request.get("selected_command_execution_review_basis"))
    consumption_basis = _mapping_from_basis(request.get("selected_request_consumption_basis"))
    consumed_basis = _mapping_from_basis(request.get("selected_consumed_request_basis"))
    v2_basis = _mapping_from_basis(request.get("selected_v2_admitted_request_basis"))
    v1_basis = _mapping_from_basis(request.get("selected_v1_predecessor_failure_basis"))

    question = request.get("command_invocation_boundary_question")
    intent = request.get("command_invocation_boundary_intent")
    _check(
        checks,
        "command invocation boundary question declared",
        isinstance(question, str) and bool(question.strip()),
        "question is declared",
        question,
        "COMMAND_INVOCATION_BOUNDARY_QUESTION_UNDECLARED",
    )
    _check(
        checks,
        "command invocation boundary intent supported",
        intent in SUPPORTED_INTENTS,
        "intent is supported",
        intent,
        "COMMAND_INVOCATION_BOUNDARY_INTENT_UNSUPPORTED",
    )
    _check(
        checks,
        "command invocation authorization terminal summary basis declared",
        _present(auth_summary),
        "terminal summary basis is declared",
        auth_summary,
        "COMMAND_INVOCATION_AUTHORIZATION_TERMINAL_SUMMARY_MISSING",
    )
    _check(
        checks,
        "command invocation authorization live artifact basis declared",
        _basis_declared(auth_basis),
        "authorization live artifact basis is declared",
        auth_basis,
        "COMMAND_INVOCATION_AUTHORIZATION_BASIS_MISSING",
    )
    auth_outcome = _basis_outcome(auth_basis, request, ("selected_command_invocation_authorization_result_outcome",))
    _check(
        checks,
        "command invocation authorization live artifact recorded outcome",
        auth_outcome == COMMAND_INVOCATION_AUTHORIZATION_OUTCOME,
        COMMAND_INVOCATION_AUTHORIZATION_OUTCOME,
        auth_outcome,
        "COMMAND_INVOCATION_AUTHORIZATION_NOT_RECORDED",
    )
    auth_failed = _basis_failed_count(
        auth_basis,
        request,
        ("selected_command_invocation_authorization_failed_check_count",),
    )
    _check(
        checks,
        "command invocation authorization live artifact failed check count zero",
        auth_failed == 0,
        "failed_check_count == 0",
        auth_failed,
        "COMMAND_INVOCATION_AUTHORIZATION_FAILED_CHECKS_PRESENT",
    )
    _check(
        checks,
        "command invocation authorization token created",
        _authorization_token_created(auth_basis, request),
        "authorization token is created by authorization basis",
        auth_basis,
        "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_MISSING",
    )
    _check(
        checks,
        "command invocation authorization token one-shot",
        _authorization_token_one_shot(auth_basis, request),
        "authorization token is one-shot",
        auth_basis,
        "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_NOT_ONE_SHOT",
    )

    _check(
        checks,
        "command invocation authorization boundary basis declared",
        _basis_declared(auth_boundary_basis),
        "authorization boundary basis is declared",
        auth_boundary_basis,
        "COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_BASIS_MISSING",
    )
    auth_boundary_outcome = _basis_outcome(
        auth_boundary_basis,
        request,
        ("selected_command_invocation_authorization_boundary_result_outcome",),
    )
    _check(
        checks,
        "command invocation authorization boundary live artifact recorded outcome",
        auth_boundary_outcome == COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_OUTCOME,
        COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_OUTCOME,
        auth_boundary_outcome,
        "COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_NOT_RECORDED",
    )
    auth_boundary_failed = _basis_failed_count(
        auth_boundary_basis,
        request,
        ("selected_command_invocation_authorization_boundary_failed_check_count",),
    )
    _check(
        checks,
        "command invocation authorization boundary live artifact failed check count zero",
        auth_boundary_failed == 0,
        "failed_check_count == 0",
        auth_boundary_failed,
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
    review_outcome = _basis_outcome(review_basis, request, ("selected_command_execution_review_result_outcome",))
    _check(
        checks,
        "command execution review live artifact recorded outcome",
        review_outcome == COMMAND_EXECUTION_REVIEW_OUTCOME,
        COMMAND_EXECUTION_REVIEW_OUTCOME,
        review_outcome,
        "COMMAND_EXECUTION_REVIEW_NOT_RECORDED",
    )
    review_failed = _basis_failed_count(review_basis, request, ("selected_command_execution_review_failed_check_count",))
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
    consumption_outcome = _basis_outcome(consumption_basis, request, ("selected_request_consumption_result_outcome",))
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
    v2_outcome = _basis_outcome(v2_basis, request, ("selected_v2_admitted_request_outcome",))
    _check(
        checks,
        "v2 admitted request outcome admitted",
        v2_outcome == V2_ADMITTED_REQUEST_OUTCOME,
        V2_ADMITTED_REQUEST_OUTCOME,
        v2_outcome,
        "V2_ADMITTED_REQUEST_NOT_ADMITTED",
    )
    v2_version = _basis_version(v2_basis, request, ("selected_v2_admitted_request_version",))
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

    for name, field, block_code in (
        ("command execution boundary basis declared", "selected_command_execution_boundary_basis", "COMMAND_EXECUTION_BOUNDARY_BASIS_MISSING"),
        ("command report basis declared", "selected_command_report_basis", "COMMAND_REPORT_BASIS_MISSING"),
        ("command implementation boundary basis declared", "selected_command_implementation_boundary_basis", "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING"),
        ("command boundary basis declared", "selected_command_boundary_basis", "COMMAND_BOUNDARY_BASIS_MISSING"),
        ("artifact emission containment basis declared", "selected_artifact_emission_containment_basis", "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING"),
        ("evidence-manifest basis declared", "selected_evidence_manifest_basis", "EVIDENCE_MANIFEST_BASIS_MISSING"),
        ("portable verification basis declared", "selected_portable_verification_basis", "PORTABLE_VERIFICATION_BASIS_MISSING"),
    ):
        value = request.get(field)
        _check(checks, name, _present(value), "basis is declared", value, block_code)

    for name, field, block_code in (
        ("invocation-boundary-only posture declared", "invocation_boundary_only_posture", "INVOCATION_BOUNDARY_ONLY_POSTURE_MISSING"),
        ("one-future-invocation-step posture declared", "one_future_invocation_step_posture", "ONE_FUTURE_INVOCATION_STEP_POSTURE_MISSING"),
        ("authorization-token-preserved posture declared", "authorization_token_preserved_posture", "AUTHORIZATION_TOKEN_PRESERVED_POSTURE_MISSING"),
        ("authorization-token-not-spent posture declared", "authorization_token_not_spent_posture", "AUTHORIZATION_TOKEN_NOT_SPENT_POSTURE_MISSING"),
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
    ):
        value = request.get(field)
        _check(checks, name, _present(value), "posture is declared", value, block_code)

    scope = request.get("command_invocation_boundary_scope")
    _check(
        checks,
        "reference-shaped input posture declared",
        _present(request.get("reference_shaped_input_posture"))
        or "REFERENCE_SHAPED_BASIS_REQUIRED" in _scope_values(scope),
        "reference-shaped input posture is declared or required by scope",
        request.get("reference_shaped_input_posture") or _scope_values(scope),
        "FULL_PRIOR_ARTIFACT_BODY_EMITTED",
    )
    _check(
        checks,
        "command invocation boundary scope supported",
        _supported_scope(scope),
        "all selected scope values are supported",
        _scope_values(scope),
        "UNSUPPORTED_COMMAND_INVOCATION_BOUNDARY_SCOPE",
    )

    all_values = [request] + [
        request.get(field)
        for field in (
            "selected_command_invocation_authorization_basis",
            "selected_command_invocation_authorization_terminal_summary_basis",
            "selected_command_invocation_authorization_boundary_basis",
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
            "invocation_boundary_only_posture",
            "one_future_invocation_step_posture",
            "authorization_token_preserved_posture",
            "authorization_token_not_spent_posture",
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

    for check_name, expected, block_code in (
        ("command invocation not created", "command invocation is not created", "COMMAND_INVOCATION_CREATED"),
        ("command execution not performed", "command execution is not performed", "COMMAND_EXECUTION_PERFORMED"),
        ("command output not created", "command output is not created", "COMMAND_OUTPUT_CREATED"),
        ("command result not created", "command result is not created", "COMMAND_RESULT_CREATED"),
        ("command success not created", "command success is not created", "COMMAND_SUCCESS_CREATED"),
        ("execution permission not created", "execution permission is not created", "EXECUTION_PERMISSION_CREATED"),
        ("execution approval not created", "execution approval is not created", "EXECUTION_APPROVAL_CREATED"),
        ("authorization token not spent", "authorization token is not spent", "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_SPENT_HERE"),
        ("standing invocation lane not created", "standing invocation lane is not created", "STANDING_INVOCATION_LANE_CREATED"),
        ("repeat invocation permission not created", "repeat invocation permission is not created", "REPEAT_INVOCATION_PERMISSION_CREATED"),
        ("invocation boundary not invocation", "invocation boundary is not invocation", "INVOCATION_BOUNDARY_TREATED_AS_INVOCATION"),
        ("invocation boundary not execution", "invocation boundary is not execution", "INVOCATION_BOUNDARY_TREATED_AS_EXECUTION"),
        ("invocation boundary not command success", "invocation boundary is not command success", "INVOCATION_BOUNDARY_TREATED_AS_COMMAND_SUCCESS"),
        ("authorization token not invocation", "authorization token is not invocation", "AUTHORIZATION_TOKEN_TREATED_AS_INVOCATION"),
        ("authorization token not command success", "authorization token is not command success", "AUTHORIZATION_TOKEN_TREATED_AS_COMMAND_SUCCESS"),
        ("command output not source", "command output is not source", "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
        ("command result not authority", "command result is not authority", "COMMAND_RESULT_TREATED_AS_AUTHORITY"),
        ("command success not currentness", "command success is not currentness", "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
        ("command success not final completion", "command success is not final completion", "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
    ):
        _check(checks, check_name, collapse_code != block_code, expected, collapse_key, block_code)

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
    _check(
        checks,
        "deployment/runtime/public release not created",
        collapse_code not in {"DEPLOYMENT_CREATED", "RUNTIME_HOSTING_CREATED", "PUBLIC_RELEASE_CREATED"},
        "deployment/runtime/public release are not created",
        collapse_key,
        collapse_code if collapse_code in {"DEPLOYMENT_CREATED", "RUNTIME_HOSTING_CREATED", "PUBLIC_RELEASE_CREATED"} else None,
    )
    _check(
        checks,
        "operation permission/public readiness/final completion not created",
        collapse_code not in {"OPERATION_PERMISSION_CREATED", "PUBLIC_READINESS_CREATED", "FINAL_COMPLETION_CLAIMED"},
        "operation permission/public readiness/final completion are not created",
        collapse_key,
        collapse_code if collapse_code in {"OPERATION_PERMISSION_CREATED", "PUBLIC_READINESS_CREATED", "FINAL_COMPLETION_CLAIMED"} else None,
    )
    _check(
        checks,
        "continuation/reusable permission/follow-on work not authorized",
        collapse_code not in {"CONTINUATION_AUTHORIZED", "REUSABLE_PERMISSION_CREATED", "FOLLOW_ON_WORK_AUTHORIZED"},
        "continuation/reusable permission/follow-on work are not authorized",
        collapse_key,
        collapse_code if collapse_code in {"CONTINUATION_AUTHORIZED", "REUSABLE_PERMISSION_CREATED", "FOLLOW_ON_WORK_AUTHORIZED"} else None,
    )
    _check(
        checks,
        "derivative reception/vessel relation/another reception request not authorized",
        collapse_code not in {"DERIVATIVE_RECEPTION_AUTHORIZED", "VESSEL_RELATION_AUTHORIZED", "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"},
        "derivative reception/vessel relation/another reception request are not authorized",
        collapse_key,
        collapse_code if collapse_code in {"DERIVATIVE_RECEPTION_AUTHORIZED", "VESSEL_RELATION_AUTHORIZED", "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"} else None,
    )
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
        return OUTCOME_BLOCKED, _block(
            request_malformed_code,
            "Declared command invocation boundary request is malformed or unreadable.",
        )
    if request.get("command_invocation_boundary_intent") == INTENT_BLOCK:
        return OUTCOME_BLOCKED, _block(
            request.get("block_code") or "COMMAND_INVOCATION_BOUNDARY_BLOCKED_BY_REQUEST",
            request.get("block_reason") or "Request explicitly selected blocked command invocation boundary posture.",
        )
    requested = request.get("requested_command_invocation_boundary_outcome")
    if requested is not None and requested not in OUTCOME_FAMILY:
        return OUTCOME_BLOCKED, _block(
            "COMMAND_INVOCATION_BOUNDARY_INTENT_UNSUPPORTED",
            "Requested command invocation boundary outcome is unsupported.",
        )
    if requested == OUTCOME_BLOCKED:
        return OUTCOME_BLOCKED, _block(
            request.get("block_code") or "COMMAND_INVOCATION_BOUNDARY_BLOCKED_BY_REQUEST",
            request.get("block_reason") or "Requested command invocation boundary outcome is blocked.",
        )
    failed_code = _first_failed_block(checks)
    if failed_code:
        return OUTCOME_BLOCKED, _block(failed_code, f"Command invocation boundary blocked by {failed_code}.")
    if requested in {OUTCOME_NOT_RECORDED, OUTCOME_REQUIRES_ADDITIONAL_BASIS}:
        return str(requested), _block(None, None)
    if request.get("command_invocation_boundary_intent") == INTENT_DO_NOT_RECORD:
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

    auth_basis = _mapping_from_basis(request.get("selected_command_invocation_authorization_basis"))
    auth_boundary_basis = _mapping_from_basis(request.get("selected_command_invocation_authorization_boundary_basis"))
    review_basis = _mapping_from_basis(request.get("selected_command_execution_review_basis"))
    consumption_basis = _mapping_from_basis(request.get("selected_request_consumption_basis"))
    v2_basis = _mapping_from_basis(request.get("selected_v2_admitted_request_basis"))

    result: dict[str, Any] = {
        "consumed_single_live_command_invocation_request_command_invocation_boundary_metadata": _build_metadata(
            request, outcome
        ),
        "declared_command_invocation_boundary_question": {
            "command_invocation_boundary_request_id": request.get("command_invocation_boundary_request_id"),
            "command_invocation_boundary_question": request.get("command_invocation_boundary_question"),
            "expected_question": CORE_COMMAND_INVOCATION_BOUNDARY_QUESTION,
            "command_invocation_boundary_intent": request.get("command_invocation_boundary_intent"),
            "request_path": request_path,
        },
        "selected_command_invocation_authorization_basis": _basis_section(
            request.get("selected_command_invocation_authorization_basis"),
            path=request.get("selected_command_invocation_authorization_result_path"),
            extra={
                "selected_command_invocation_authorization_result_id": request.get(
                    "selected_command_invocation_authorization_result_id"
                ),
                "selected_command_invocation_authorization_result_outcome": _basis_outcome(
                    auth_basis,
                    request,
                    ("selected_command_invocation_authorization_result_outcome",),
                ),
                "selected_command_invocation_authorization_failed_check_count": _basis_failed_count(
                    auth_basis,
                    request,
                    ("selected_command_invocation_authorization_failed_check_count",),
                ),
                "selected_command_invocation_authorization_token_created": _authorization_token_created(
                    auth_basis, request
                ),
                "selected_command_invocation_authorization_token_is_one_shot": _authorization_token_one_shot(
                    auth_basis, request
                ),
                "authorization_basis_preserved": True,
                "authorization_basis_remains_authorization_basis_only": True,
                "authorization_did_not_create_command_invocation": True,
                "authorization_did_not_execute_command": True,
                "authorization_did_not_create_output_result_success": True,
                "authorization_did_not_create_execution_permission_or_approval": True,
                "authorization_did_not_create_standing_lane_or_repeat_permission": True,
            },
        ),
        "selected_command_invocation_authorization_terminal_summary_basis": _basis_section(
            request.get("selected_command_invocation_authorization_terminal_summary_basis"),
            path=request.get("selected_command_invocation_authorization_terminal_summary_path"),
            extra={
                "terminal_summary_remains_readability_basis_only": True,
                "terminal_summary_does_not_create_command_invocation": True,
                "terminal_summary_does_not_authorize_command_execution": True,
                "terminal_summary_does_not_spend_authorization_token": True,
            },
        ),
        "selected_command_invocation_authorization_boundary_basis": _basis_section(
            request.get("selected_command_invocation_authorization_boundary_basis"),
            path=request.get("selected_command_invocation_authorization_boundary_result_path"),
            extra={
                "selected_command_invocation_authorization_boundary_result_id": request.get(
                    "selected_command_invocation_authorization_boundary_result_id"
                ),
                "selected_command_invocation_authorization_boundary_result_outcome": _basis_outcome(
                    auth_boundary_basis,
                    request,
                    ("selected_command_invocation_authorization_boundary_result_outcome",),
                ),
                "selected_command_invocation_authorization_boundary_failed_check_count": _basis_failed_count(
                    auth_boundary_basis,
                    request,
                    ("selected_command_invocation_authorization_boundary_failed_check_count",),
                ),
                "authorization_boundary_remains_pre_authorization_lineage_evidence": True,
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
                "command_execution_review_remains_review_basis_only": True,
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
                "consumed_request_basis_remains_basis_only": True,
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
                    v2_basis,
                    request,
                    ("selected_v2_failed_check_count",),
                ),
                "successor_metadata_preserved": _successor_metadata_preserved(v2_basis, request),
                "returned_result_containment_preserved": _returned_result_containment_preserved(v2_basis),
                "v2_remains_lineage_evidence_only": True,
                "v2_does_not_claim_v1_passed": not _v2_claims_v1_passed(
                    _mapping_from_basis(request.get("selected_v1_predecessor_failure_basis")),
                    v2_basis,
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
            extra={"basis_remains_command_execution_boundary_basis_only": True},
        ),
        "selected_command_report_basis": _basis_section(
            request.get("selected_command_report_basis"),
            path=request.get("selected_command_report_path"),
            extra={"basis_remains_non_authoritative_report_basis_only": True},
        ),
        "selected_command_implementation_boundary_basis": _basis_section(
            request.get("selected_command_implementation_boundary_basis"),
            path=request.get("selected_command_implementation_boundary_result_path"),
            extra={"basis_remains_command_implementation_boundary_basis_only": True},
        ),
        "selected_command_boundary_basis": _basis_section(
            request.get("selected_command_boundary_basis"),
            path=request.get("selected_command_boundary_result_path"),
            extra={"basis_remains_checker_only_command_boundary_basis": True},
        ),
        "selected_artifact_emission_containment_basis": _basis_section(
            request.get("selected_artifact_emission_containment_basis"),
            path=request.get("selected_artifact_emission_containment_result_path"),
            extra={"basis_remains_reference_shaped_containment_basis_only": True},
        ),
        "selected_evidence_manifest_basis": _basis_section(
            request.get("selected_evidence_manifest_basis"),
            path=request.get("selected_evidence_manifest_result_path"),
            extra={"basis_remains_evidence_definition_basis_only": True},
        ),
        "selected_portable_verification_basis": _basis_section(
            request.get("selected_portable_verification_basis"),
            path=request.get("selected_portable_verification_result_path"),
            extra={"basis_remains_carrier_independent_verification_basis_only": True},
        ),
        "invocation_boundary_only_posture": _posture_section(
            request.get("invocation_boundary_only_posture"),
            extra={"invocation_boundary_only_posture_declared": _present(request.get("invocation_boundary_only_posture"))},
        ),
        "one_future_invocation_step_posture": _posture_section(
            request.get("one_future_invocation_step_posture"),
            extra={"one_future_invocation_step_posture_declared": _present(request.get("one_future_invocation_step_posture"))},
        ),
        "authorization_token_preserved_posture": _posture_section(
            request.get("authorization_token_preserved_posture"),
            extra={"authorization_token_preserved_posture_declared": _present(request.get("authorization_token_preserved_posture"))},
        ),
        "authorization_token_not_spent_posture": _posture_section(
            request.get("authorization_token_not_spent_posture"),
            extra={
                "authorization_token_not_spent_posture_declared": _present(request.get("authorization_token_not_spent_posture")),
                "authorization_token_not_spent": True,
            },
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
            extra={"command_output_result_success_not_created": True},
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
        "command_invocation_boundary_scope": _scope_section(request.get("command_invocation_boundary_scope"), outcome),
        "command_invocation_boundary_checks": {
            "checks": checks,
            "passed_check_count": passed_count,
            "failed_check_count": failed_count,
        },
        "command_invocation_boundary_statement": _statement(outcome),
        "command_invocation_boundary_non_meaning": _non_meaning(),
        "additional_basis_required": _additional_basis_required(outcome, request),
        "not_recorded_basis": _not_recorded_basis(outcome, request, checks),
        "what_remains_open": _what_remains_open(),
        "non_claims": _default_non_claims(),
        "outcome": outcome,
        "block": block,
    }
    result["consumed_single_live_command_invocation_request_command_invocation_boundary_summary"] = (
        build_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_boundary_summary(
            result
        )
    )
    return result


def resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_boundary(
    declared_command_invocation_boundary_request: Mapping[str, Any] | None = None,
) -> dict:
    if declared_command_invocation_boundary_request is None:
        return _result_from_request({})
    if not isinstance(declared_command_invocation_boundary_request, Mapping):
        return _result_from_request(
            {"command_invocation_boundary_request_id": "malformed"},
            request_malformed_code="DECLARED_COMMAND_INVOCATION_BOUNDARY_REQUEST_MALFORMED",
        )
    return _result_from_request(_deepcopy(declared_command_invocation_boundary_request))


def resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_boundary_from_path(
    declared_command_invocation_boundary_request_path: Path | str,
) -> dict:
    path = Path(declared_command_invocation_boundary_request_path)
    base_request = {
        "command_invocation_boundary_request_id": "unreadable",
        "declared_command_invocation_boundary_request_path": str(path),
    }
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return _result_from_request(
            base_request,
            request_malformed_code="DECLARED_COMMAND_INVOCATION_BOUNDARY_REQUEST_UNREADABLE",
            request_path=str(path),
        )
    if not isinstance(data, Mapping):
        return _result_from_request(
            {
                "command_invocation_boundary_request_id": "malformed",
                "declared_command_invocation_boundary_request_path": str(path),
            },
            request_malformed_code="DECLARED_COMMAND_INVOCATION_BOUNDARY_REQUEST_MALFORMED",
            request_path=str(path),
        )
    request = _deepcopy(data)
    request.setdefault("declared_command_invocation_boundary_request_path", str(path))
    return _result_from_request(request, request_path=str(path))


def build_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_boundary_summary(
    result: Mapping[str, Any],
) -> dict:
    metadata = _mapping_from_basis(
        result.get("consumed_single_live_command_invocation_request_command_invocation_boundary_metadata")
    )
    declared = _mapping_from_basis(result.get("declared_command_invocation_boundary_question"))
    checks_section = _mapping_from_basis(result.get("command_invocation_boundary_checks"))
    statement = _mapping_from_basis(result.get("command_invocation_boundary_statement"))
    block = _mapping_from_basis(result.get("block"))
    auth_basis = _mapping_from_basis(result.get("selected_command_invocation_authorization_basis"))
    auth_boundary_basis = _mapping_from_basis(result.get("selected_command_invocation_authorization_boundary_basis"))
    review_basis = _mapping_from_basis(result.get("selected_command_execution_review_basis"))
    consumption_basis = _mapping_from_basis(result.get("selected_request_consumption_basis"))
    v2_basis = _mapping_from_basis(result.get("selected_v2_admitted_request_basis"))
    non_claims = _mapping_from_basis(result.get("non_claims"))
    outcome = result.get("outcome")
    return {
        "outcome": outcome,
        "block_code": block.get("code"),
        "block_reason": block.get("reason"),
        "command_invocation_boundary_request_id": declared.get("command_invocation_boundary_request_id")
        or metadata.get("command_invocation_boundary_request_id"),
        "command_invocation_boundary_question": declared.get("command_invocation_boundary_question"),
        "command_invocation_boundary_intent": declared.get("command_invocation_boundary_intent"),
        "passed_check_count": checks_section.get("passed_check_count", 0),
        "failed_check_count": checks_section.get("failed_check_count", 0),
        "command_invocation_boundary_recorded": statement.get("command_invocation_boundary_recorded", False),
        "one_future_command_invocation_step_declared": statement.get(
            "one_future_command_invocation_step_declared", False
        ),
        "command_invocation_authorization_token_preserved": statement.get(
            "command_invocation_authorization_token_preserved", False
        ),
        "authorization_token_remains_one_shot": statement.get("authorization_token_remains_one_shot", False),
        "authorization_token_not_spent": statement.get("authorization_token_not_spent", False),
        "invocation_still_not_created": statement.get("invocation_still_not_created", False),
        "execution_still_not_performed": statement.get("execution_still_not_performed", False),
        "consumed_request_token_remains_closed": statement.get("consumed_request_token_remains_closed", False),
        "v1_predecessor_failure_preserved": statement.get("v1_predecessor_failure_preserved", False),
        "returned_result_containment_preserved": statement.get("returned_result_containment_preserved", False),
        "not_recorded": outcome == OUTCOME_NOT_RECORDED,
        "requires_additional_basis": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "selected_command_invocation_authorization_outcome": auth_basis.get(
            "selected_command_invocation_authorization_result_outcome"
        )
        or auth_basis.get("outcome"),
        "selected_command_invocation_authorization_failed_check_count": auth_basis.get(
            "selected_command_invocation_authorization_failed_check_count"
        ),
        "selected_command_invocation_authorization_token_created": auth_basis.get(
            "selected_command_invocation_authorization_token_created"
        ),
        "selected_command_invocation_authorization_token_is_one_shot": auth_basis.get(
            "selected_command_invocation_authorization_token_is_one_shot"
        ),
        "selected_command_invocation_authorization_boundary_outcome": auth_boundary_basis.get(
            "selected_command_invocation_authorization_boundary_result_outcome"
        )
        or auth_boundary_basis.get("outcome"),
        "selected_command_invocation_authorization_boundary_failed_check_count": auth_boundary_basis.get(
            "selected_command_invocation_authorization_boundary_failed_check_count"
        ),
        "selected_command_execution_review_outcome": review_basis.get(
            "selected_command_execution_review_result_outcome"
        )
        or review_basis.get("outcome"),
        "selected_command_execution_review_failed_check_count": review_basis.get(
            "selected_command_execution_review_failed_check_count"
        ),
        "selected_request_consumption_outcome": consumption_basis.get("selected_request_consumption_result_outcome")
        or consumption_basis.get("outcome"),
        "selected_request_consumption_failed_check_count": consumption_basis.get(
            "selected_request_consumption_failed_check_count"
        ),
        "selected_v2_admitted_request_outcome": v2_basis.get("selected_v2_admitted_request_outcome")
        or v2_basis.get("outcome"),
        "selected_v2_admitted_request_version": v2_basis.get("selected_v2_admitted_request_version")
        or v2_basis.get("result_version"),
        "selected_v2_failed_check_count": v2_basis.get("selected_v2_failed_check_count"),
        "command_invocation_not_created": non_claims.get("command_invocation_created") is False,
        "command_execution_not_performed": non_claims.get("command_execution_performed") is False,
        "command_output_result_success_not_created": non_claims.get("command_output_created") is False
        and non_claims.get("command_result_created") is False
        and non_claims.get("command_success_created") is False,
        "execution_permission_not_created": non_claims.get("execution_permission_created") is False,
        "execution_approval_not_created": non_claims.get("execution_approval_created") is False,
        "authorization_token_not_spent_non_claim": non_claims.get("authorization_token_spent_here") is False,
        "no_standing_lane": non_claims.get("standing_invocation_lane_created") is False,
        "no_repeat_permission": non_claims.get("repeat_invocation_permission_created") is False,
        "consumed_request_not_reopened": non_claims.get("consumed_request_reopened") is False,
        "invocation_boundary_not_invocation": non_claims.get("invocation_boundary_treated_as_invocation") is False,
        "invocation_boundary_not_execution": non_claims.get("invocation_boundary_treated_as_execution") is False,
        "invocation_boundary_not_command_success": non_claims.get("invocation_boundary_treated_as_command_success")
        is False,
        "authorization_token_not_invocation": non_claims.get("authorization_token_treated_as_invocation") is False,
        "authorization_token_not_command_success": non_claims.get("authorization_token_treated_as_command_success")
        is False,
        "v1_not_repaired_hidden_or_claimed_passed": non_claims.get("v1_repaired") is False
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
        "key_non_claims": _sanitize_reference_shape(non_claims),
    }


def write_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_boundary_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    metadata = _mapping_from_basis(
        result.get("consumed_single_live_command_invocation_request_command_invocation_boundary_metadata")
    )
    request_id = metadata.get("command_invocation_boundary_request_id") or "command_invocation_boundary_result"
    filename = (
        f"{_safe_component(request_id, 'command_invocation_boundary_result')}__"
        "consumed_single_live_command_invocation_request_command_invocation_boundary_result.json"
    )
    if output_path is None:
        candidate = PORTABLE_SOURCE_BODY_VERIFICATION_CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_BOUNDARY_ROOT / filename
    else:
        path = Path(output_path)
        candidate = path if path.suffix else path / filename
    candidate.parent.mkdir(parents=True, exist_ok=True)
    final_path = candidate
    if final_path.exists():
        stem = candidate.stem
        suffix = candidate.suffix or ".json"
        for index in range(1, 1000):
            numbered = candidate.with_name(f"{stem}_{index:03d}{suffix}")
            if not numbered.exists():
                final_path = numbered
                break
        else:
            raise PortableSourceBodyVerificationConsumedSingleLiveCommandInvocationRequestCommandInvocationBoundaryError(
                "Could not choose a non-overwriting command invocation boundary result path."
            )
    final_path.write_text(
        json.dumps(_sanitize_reference_shape(dict(result)), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return final_path


def build_declared_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_boundary_request(
    command_invocation_boundary_request_id: str,
    command_invocation_boundary_question: str,
    selected_command_invocation_authorization_basis: Mapping[str, Any] | str,
    selected_command_invocation_authorization_terminal_summary_basis: Mapping[str, Any] | str,
    selected_command_invocation_authorization_boundary_basis: Mapping[str, Any] | str,
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
    invocation_boundary_only_posture: Mapping[str, Any] | str,
    one_future_invocation_step_posture: Mapping[str, Any] | str,
    authorization_token_preserved_posture: Mapping[str, Any] | str,
    authorization_token_not_spent_posture: Mapping[str, Any] | str,
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
    command_invocation_boundary_scope: Sequence[str] | Mapping[str, Any],
    command_invocation_boundary_intent: str = INTENT_RECORD,
    *,
    selected_command_invocation_authorization_result_path: str | None = None,
    selected_command_invocation_authorization_result_id: str | None = None,
    selected_command_invocation_authorization_result_outcome: str | None = None,
    selected_command_invocation_authorization_failed_check_count: int | None = None,
    selected_command_invocation_authorization_token_created: bool | None = None,
    selected_command_invocation_authorization_token_is_one_shot: bool | None = None,
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
    requested_command_invocation_boundary_outcome: str = OUTCOME_RECORDED,
    additional_basis_context: Mapping[str, Any] | None = None,
    not_recorded_basis: Mapping[str, Any] | str | None = None,
) -> dict:
    request = {
        "command_invocation_boundary_request_id": command_invocation_boundary_request_id,
        "command_invocation_boundary_question": command_invocation_boundary_question,
        "command_invocation_boundary_intent": command_invocation_boundary_intent,
        "selected_command_invocation_authorization_basis": _deepcopy(selected_command_invocation_authorization_basis),
        "selected_command_invocation_authorization_terminal_summary_basis": _deepcopy(
            selected_command_invocation_authorization_terminal_summary_basis
        ),
        "selected_command_invocation_authorization_boundary_basis": _deepcopy(
            selected_command_invocation_authorization_boundary_basis
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
        "invocation_boundary_only_posture": _deepcopy(invocation_boundary_only_posture),
        "one_future_invocation_step_posture": _deepcopy(one_future_invocation_step_posture),
        "authorization_token_preserved_posture": _deepcopy(authorization_token_preserved_posture),
        "authorization_token_not_spent_posture": _deepcopy(authorization_token_not_spent_posture),
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
        "command_invocation_boundary_scope": _deepcopy(command_invocation_boundary_scope),
        "reference_shaped_input_posture": {"reference_shaped_basis_required": True},
        "requested_command_invocation_boundary_outcome": requested_command_invocation_boundary_outcome,
        "additional_basis_context": _deepcopy(additional_basis_context or {}),
        "not_recorded_basis": _deepcopy(not_recorded_basis or {}),
        "declared_non_claims": _default_non_claims(),
    }
    optional_values = {
        "selected_command_invocation_authorization_result_path": selected_command_invocation_authorization_result_path,
        "selected_command_invocation_authorization_result_id": selected_command_invocation_authorization_result_id,
        "selected_command_invocation_authorization_result_outcome": selected_command_invocation_authorization_result_outcome,
        "selected_command_invocation_authorization_failed_check_count": selected_command_invocation_authorization_failed_check_count,
        "selected_command_invocation_authorization_token_created": selected_command_invocation_authorization_token_created,
        "selected_command_invocation_authorization_token_is_one_shot": selected_command_invocation_authorization_token_is_one_shot,
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
    }
    for key, value in optional_values.items():
        if value is not None:
            request[key] = value
    return request
