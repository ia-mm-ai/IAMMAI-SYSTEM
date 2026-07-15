"""Bounded consumed-request command invocation authorization boundary resolver.

This module records authorization-boundary conditions only. It does not create
command invocation authorization, command invocation, command execution, command
output, command result, command success, execution permission, execution
approval, a standing invocation lane, repeat permission, authority, currentness,
final completion, continuation, reusable permission, derivative reception,
vessel relation, another reception request, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class PortableSourceBodyVerificationConsumedSingleLiveCommandInvocationRequestCommandInvocationAuthorizationBoundaryError(
    Exception
):
    """Raised for impossible bounded resolver write-state failures."""


RESOLVER_MODULE = (
    "resolve_portable_source_body_verification_consumed_single_live_command_"
    "invocation_request_command_invocation_authorization_boundary"
)
RESULT_VERSION = "0.1.0"
PORTABLE_SOURCE_BODY_VERIFICATION_CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_"
    "consumed_single_live_command_invocation_request_command_invocation_authorization_boundary"
)
OUTPUT_ROOT = (
    PORTABLE_SOURCE_BODY_VERIFICATION_CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_ROOT
)

CORE_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_QUESTION = (
    "Can the recorded command execution review basis be bounded for one future "
    "command invocation authorization review without creating command invocation "
    "authorization, command invocation, command execution, command output, command "
    "result, command success, execution permission, execution approval, standing "
    "invocation lane, repeat permission, authority, currentness, final completion, "
    "continuation, reusable permission, derivative reception, vessel relation, "
    "another reception request, or follow-on work?"
)

OUTCOME_RECORDED = (
    "CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_AUTHORIZATION_"
    "BOUNDARY_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_AUTHORIZATION_"
    "BOUNDARY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_AUTHORIZATION_"
    "BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_AUTHORIZATION_"
    "BOUNDARY_BLOCKED"
)
OUTCOME_FAMILY = {
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
}

INTENT_RECORD = (
    "RECORD_CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_"
    "AUTHORIZATION_BOUNDARY"
)
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_"
    "AUTHORIZATION_BOUNDARY"
)
INTENT_BLOCK = (
    "BLOCK_CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_"
    "AUTHORIZATION_BOUNDARY"
)
SUPPORTED_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_INTENTS = {
    INTENT_RECORD,
    INTENT_DO_NOT_RECORD,
    INTENT_BLOCK,
}

COMMAND_EXECUTION_REVIEW_OUTCOME = (
    "CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_EXECUTION_REVIEW_RECORDED"
)
EXECUTION_REVIEW_BOUNDARY_OUTCOME = (
    "CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_EXECUTION_REVIEW_"
    "BOUNDARY_RECORDED"
)
REQUEST_CONSUMPTION_OUTCOME = "ADMITTED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_CONSUMED"
V2_ADMITTED_REQUEST_OUTCOME = "SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_ADMITTED"
V2_ADMITTED_REQUEST_VERSION = "0.2.0"
V2_RESOLVER_MODULE = (
    "resolve_portable_source_body_verification_single_live_command_invocation_"
    "request_admission_boundary_v2"
)
V1_PREDECESSOR_RESOLVER_MODULE = (
    "resolve_portable_source_body_verification_single_live_command_invocation_"
    "request_admission_boundary"
)

SUPPORTED_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_SCOPE = {
    "COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_ONLY",
    "COMMAND_INVOCATION_AUTHORIZATION_NOT_CREATED",
    "ONE_FUTURE_AUTHORIZATION_REVIEW_ONLY",
    "REVIEWED_COMMAND_EXECUTION_REVIEW_BASIS_PRESERVED",
    "REVIEWED_CONSUMED_REQUEST_BASIS_PRESERVED",
    "CONSUMED_REQUEST_TOKEN_REMAINS_CLOSED",
    "CONSUMED_REQUEST_NOT_REOPENED",
    "COMMAND_INVOCATION_NOT_CREATED",
    "COMMAND_EXECUTION_NOT_PERFORMED",
    "COMMAND_OUTPUT_NOT_CREATED",
    "COMMAND_RESULT_NOT_CREATED",
    "COMMAND_SUCCESS_NOT_CREATED",
    "EXECUTION_PERMISSION_NOT_CREATED",
    "EXECUTION_APPROVAL_NOT_CREATED",
    "NO_STANDING_INVOCATION_LANE_CREATED",
    "NO_REPEAT_INVOCATION_PERMISSION_CREATED",
    "AUTHORIZATION_BOUNDARY_IS_NOT_AUTHORIZATION",
    "AUTHORIZATION_BOUNDARY_IS_NOT_INVOCATION",
    "REVIEWED_BASIS_IS_NOT_COMMAND_INVOCATION_AUTHORIZATION",
    "REVIEWED_BASIS_IS_NOT_COMMAND_SUCCESS",
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
}

REQUIRED_FALSE_NON_CLAIMS = (
    "consumed_request_reopened",
    "command_invocation_authorization_created",
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
    "authorization_boundary_treated_as_authorization",
    "authorization_boundary_treated_as_invocation",
    "reviewed_basis_treated_as_command_invocation_authorization",
    "reviewed_basis_treated_as_command_success",
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

ALLOWED_RECORDED_TRUE_FIELDS = (
    "command_invocation_authorization_boundary_recorded",
    "reviewed_command_execution_review_basis_preserved",
    "consumed_request_token_remains_closed",
    "single_authorization_review_conditions_declared",
    "authorization_still_not_created",
    "invocation_still_not_authorized",
    "invocation_requires_separate_authorization_result",
    "execution_still_not_authorized",
    "v1_predecessor_failure_preserved",
    "returned_result_containment_preserved",
)

FORBIDDEN_FULL_BODY_KEYS = {
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
FULL_BODY_OMISSION_MARKER = (
    "[omitted: full prior artifact body is outside command invocation "
    "authorization boundary scope]"
)

BASIS_FIELD_CHECKS = (
    ("command execution review terminal summary basis declared", "selected_command_execution_review_terminal_summary_basis", "COMMAND_EXECUTION_REVIEW_TERMINAL_SUMMARY_MISSING"),
    ("command execution review live artifact basis declared", "selected_command_execution_review_basis", "COMMAND_EXECUTION_REVIEW_BASIS_MISSING"),
    ("execution-review boundary basis declared", "selected_execution_review_boundary_basis", "EXECUTION_REVIEW_BOUNDARY_BASIS_MISSING"),
    ("request-consumption basis declared", "selected_request_consumption_basis", "REQUEST_CONSUMPTION_BASIS_MISSING"),
    ("consumed request basis declared", "selected_consumed_request_basis", "CONSUMED_REQUEST_BASIS_MISSING"),
    ("selected v2 admitted request basis declared", "selected_v2_admitted_request_basis", "V2_ADMITTED_REQUEST_BASIS_MISSING"),
    ("selected v1 predecessor/failure basis declared", "selected_v1_predecessor_failure_basis", "V1_PREDECESSOR_FAILURE_BASIS_MISSING"),
    ("command execution boundary basis declared", "selected_command_execution_boundary_basis", "COMMAND_EXECUTION_BOUNDARY_BASIS_MISSING"),
    ("command report basis declared", "selected_command_report_basis", "COMMAND_REPORT_BASIS_MISSING"),
    ("command implementation boundary basis declared", "selected_command_implementation_boundary_basis", "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING"),
    ("command boundary basis declared", "selected_command_boundary_basis", "COMMAND_BOUNDARY_BASIS_MISSING"),
    ("artifact emission containment basis declared", "selected_artifact_emission_containment_basis", "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING"),
    ("evidence-manifest basis declared", "selected_evidence_manifest_basis", "EVIDENCE_MANIFEST_BASIS_MISSING"),
    ("portable verification basis declared", "selected_portable_verification_basis", "PORTABLE_VERIFICATION_BASIS_MISSING"),
)

POSTURE_FIELD_CHECKS = (
    ("authorization-boundary-only posture declared", "authorization_boundary_only_posture", "AUTHORIZATION_BOUNDARY_ONLY_POSTURE_MISSING"),
    ("one-future-authorization-review posture declared", "one_future_authorization_review_posture", "ONE_FUTURE_AUTHORIZATION_REVIEW_POSTURE_MISSING"),
    ("reviewed-command-execution-review-basis posture declared", "reviewed_command_execution_review_basis_posture", "COMMAND_EXECUTION_REVIEW_BASIS_MISSING"),
    ("consumed-token-closed posture declared", "consumed_token_closed_posture", "CONSUMED_TOKEN_NOT_CLOSED"),
    ("no-reopen-consumed-request posture declared", "no_reopen_consumed_request_posture", "CONSUMED_REQUEST_REOPENED"),
    ("no-command-invocation-authorization posture declared", "no_command_invocation_authorization_posture", "NO_COMMAND_INVOCATION_AUTHORIZATION_POSTURE_MISSING"),
    ("no-command-invocation posture declared", "no_command_invocation_posture", "COMMAND_INVOCATION_CREATED"),
    ("no-command-execution posture declared", "no_command_execution_posture", "COMMAND_EXECUTION_PERFORMED"),
    ("no-output/result/success posture declared", "no_output_result_success_posture", "COMMAND_OUTPUT_CREATED"),
    ("no-execution-permission posture declared", "no_execution_permission_posture", "NO_EXECUTION_PERMISSION_POSTURE_MISSING"),
    ("no-execution-approval posture declared", "no_execution_approval_posture", "NO_EXECUTION_APPROVAL_POSTURE_MISSING"),
    ("no-standing-lane posture declared", "no_standing_lane_posture", "NO_STANDING_LANE_POSTURE_MISSING"),
    ("no-repeat-permission posture declared", "no_repeat_permission_posture", "NO_REPEAT_PERMISSION_POSTURE_MISSING"),
    ("returned-result containment posture declared", "returned_result_containment_posture", "V2_RETURNED_RESULT_CONTAINMENT_MISSING"),
)

COLLAPSE_CHECKS = (
    ("command invocation authorization not created", ("command_invocation_authorization_created", "command_invocation_authorization_exists", "command_invocation_permission_created"), "COMMAND_INVOCATION_AUTHORIZATION_CREATED"),
    ("command invocation not created", ("command_invocation_created", "command_invocation_exists"), "COMMAND_INVOCATION_CREATED"),
    ("command execution not performed", ("command_execution_performed", "command_executed"), "COMMAND_EXECUTION_PERFORMED"),
    ("command output not created", ("command_output_created", "command_output_exists"), "COMMAND_OUTPUT_CREATED"),
    ("command result not created", ("command_result_created", "command_result_exists"), "COMMAND_RESULT_CREATED"),
    ("command success not created", ("command_success_created", "command_success_exists"), "COMMAND_SUCCESS_CREATED"),
    ("execution permission not created", ("execution_permission_created", "execution_permission_exists"), "EXECUTION_PERMISSION_CREATED"),
    ("execution approval not created", ("execution_approval_created", "execution_approval_exists"), "EXECUTION_APPROVAL_CREATED"),
    ("standing invocation lane not created", ("standing_invocation_lane_created", "standing_invocation_lane_exists"), "STANDING_INVOCATION_LANE_CREATED"),
    ("repeat invocation permission not created", ("repeat_invocation_permission_created", "repeat_invocation_permission_exists"), "REPEAT_INVOCATION_PERMISSION_CREATED"),
    ("authorization boundary not authorization", ("authorization_boundary_treated_as_authorization",), "AUTHORIZATION_BOUNDARY_TREATED_AS_AUTHORIZATION"),
    ("authorization boundary not invocation", ("authorization_boundary_treated_as_invocation",), "AUTHORIZATION_BOUNDARY_TREATED_AS_INVOCATION"),
    ("reviewed basis not command invocation authorization", ("reviewed_basis_treated_as_command_invocation_authorization",), "REVIEWED_BASIS_TREATED_AS_COMMAND_INVOCATION_AUTHORIZATION"),
    ("reviewed basis not command success", ("reviewed_basis_treated_as_command_success",), "REVIEWED_BASIS_TREATED_AS_COMMAND_SUCCESS"),
    ("command output not source", ("command_output_became_source", "command_output_treated_as_source"), "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
    ("command result not authority", ("command_result_became_authority", "command_result_treated_as_authority"), "COMMAND_RESULT_TREATED_AS_AUTHORITY"),
    ("command success not currentness", ("command_success_created_currentness", "command_success_treated_as_currentness"), "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
    ("command success not final completion", ("command_success_claimed_final_completion", "command_success_treated_as_final_completion"), "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
    ("artifacts not mutated", ("prior_artifacts_mutated", "artifacts_mutated"), "ARTIFACTS_MUTATED"),
    ("deployment/runtime/public release not created", ("deployment_created", "runtime_hosting_created", "public_release_created"), "DEPLOYMENT_CREATED"),
    ("operation permission/public readiness/final completion not created", ("operation_permission_created", "public_launch_readiness_created", "public_readiness_created", "final_completion_claimed"), "OPERATION_PERMISSION_CREATED"),
    ("continuation/reusable permission/follow-on work not authorized", ("continuation_authorized", "reusable_permission_created", "follow_on_work_authorized"), "CONTINUATION_AUTHORIZED"),
    ("derivative reception/vessel relation/another reception request not authorized", ("derivative_reception_authorized", "vessel_relation_authorized", "another_reception_request_authorized"), "DERIVATIVE_RECEPTION_AUTHORIZED"),
)

COLLAPSE_CODE_BY_KEY = (
    ("command_invocation_authorization_created", "COMMAND_INVOCATION_AUTHORIZATION_CREATED"),
    ("command_invocation_authorization_exists", "COMMAND_INVOCATION_AUTHORIZATION_CREATED"),
    ("command_invocation_permission_created", "COMMAND_INVOCATION_AUTHORIZATION_CREATED"),
    ("command_invocation_created", "COMMAND_INVOCATION_CREATED"),
    ("command_invocation_exists", "COMMAND_INVOCATION_CREATED"),
    ("command_execution_performed", "COMMAND_EXECUTION_PERFORMED"),
    ("command_executed", "COMMAND_EXECUTION_PERFORMED"),
    ("command_output_created", "COMMAND_OUTPUT_CREATED"),
    ("command_output_exists", "COMMAND_OUTPUT_CREATED"),
    ("command_result_created", "COMMAND_RESULT_CREATED"),
    ("command_result_exists", "COMMAND_RESULT_CREATED"),
    ("command_success_created", "COMMAND_SUCCESS_CREATED"),
    ("command_success_exists", "COMMAND_SUCCESS_CREATED"),
    ("execution_permission_created", "EXECUTION_PERMISSION_CREATED"),
    ("execution_permission_exists", "EXECUTION_PERMISSION_CREATED"),
    ("execution_approval_created", "EXECUTION_APPROVAL_CREATED"),
    ("execution_approval_exists", "EXECUTION_APPROVAL_CREATED"),
    ("standing_invocation_lane_created", "STANDING_INVOCATION_LANE_CREATED"),
    ("standing_invocation_lane_exists", "STANDING_INVOCATION_LANE_CREATED"),
    ("repeat_invocation_permission_created", "REPEAT_INVOCATION_PERMISSION_CREATED"),
    ("repeat_invocation_permission_exists", "REPEAT_INVOCATION_PERMISSION_CREATED"),
    ("authorization_boundary_treated_as_authorization", "AUTHORIZATION_BOUNDARY_TREATED_AS_AUTHORIZATION"),
    ("authorization_boundary_treated_as_invocation", "AUTHORIZATION_BOUNDARY_TREATED_AS_INVOCATION"),
    ("reviewed_basis_treated_as_command_invocation_authorization", "REVIEWED_BASIS_TREATED_AS_COMMAND_INVOCATION_AUTHORIZATION"),
    ("reviewed_basis_treated_as_command_success", "REVIEWED_BASIS_TREATED_AS_COMMAND_SUCCESS"),
    ("command_output_became_source", "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
    ("command_output_treated_as_source", "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
    ("command_result_became_authority", "COMMAND_RESULT_TREATED_AS_AUTHORITY"),
    ("command_result_treated_as_authority", "COMMAND_RESULT_TREATED_AS_AUTHORITY"),
    ("command_success_created_currentness", "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
    ("command_success_treated_as_currentness", "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
    ("command_success_claimed_final_completion", "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
    ("command_success_treated_as_final_completion", "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
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


def _copy(value: Any) -> Any:
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


def _truthy(value: Any) -> bool:
    if value is True:
        return True
    if isinstance(value, str):
        return value.strip().lower() in {
            "1",
            "bounded",
            "closed",
            "declared",
            "preserved",
            "recorded",
            "supported",
            "true",
            "yes",
        }
    return False


def _to_int(value: Any) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value.strip())
        except ValueError:
            return None
    return None


def _as_mapping(value: Any) -> dict[str, Any]:
    return dict(value) if isinstance(value, Mapping) else {}


def _sanitize(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {
            str(key): (
                FULL_BODY_OMISSION_MARKER
                if str(key).lower() in FORBIDDEN_FULL_BODY_KEYS
                else _sanitize(item)
            )
            for key, item in value.items()
        }
    if isinstance(value, (list, tuple)):
        return [_sanitize(item) for item in value]
    return _copy(value)


def _contains_forbidden_full_body_key(value: Any) -> bool:
    if isinstance(value, Mapping):
        return any(
            str(key).lower() in FORBIDDEN_FULL_BODY_KEYS
            or _contains_forbidden_full_body_key(item)
            for key, item in value.items()
        )
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return any(_contains_forbidden_full_body_key(item) for item in value)
    return False


def _forbidden_full_body_keys(value: Any) -> list[str]:
    found: list[str] = []

    def walk(item: Any) -> None:
        if isinstance(item, Mapping):
            for key, child in item.items():
                if str(key).lower() in FORBIDDEN_FULL_BODY_KEYS:
                    found.append(str(key))
                walk(child)
        elif isinstance(item, Sequence) and not isinstance(item, (str, bytes, bytearray)):
            for child in item:
                walk(child)

    walk(value)
    return sorted(dict.fromkeys(found))


def _contains_truthy_key(value: Any, key_name: str) -> bool:
    key_name = key_name.lower()
    if isinstance(value, Mapping):
        for key, item in value.items():
            if str(key).lower() == key_name and _truthy(item):
                return True
            if _contains_truthy_key(item, key_name):
                return True
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return any(_contains_truthy_key(item, key_name) for item in value)
    return False


def _first_truthy_key(value: Any, key_names: Sequence[str]) -> str | None:
    names = {name.lower() for name in key_names}
    if isinstance(value, Mapping):
        for key, item in value.items():
            if str(key).lower() in names and _truthy(item):
                return str(key)
            nested = _first_truthy_key(item, key_names)
            if nested:
                return nested
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        for item in value:
            nested = _first_truthy_key(item, key_names)
            if nested:
                return nested
    return None


def _find_first(value: Any, keys: Sequence[str]) -> Any:
    names = {key.lower() for key in keys}
    if isinstance(value, Mapping):
        for key, item in value.items():
            if str(key).lower() in names and _present(item):
                return item
        for item in value.values():
            found = _find_first(item, keys)
            if _present(found):
                return found
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        for item in value:
            found = _find_first(item, keys)
            if _present(found):
                return found
    return None


def _find_truthy(value: Any, keys: Sequence[str]) -> bool:
    return any(_contains_truthy_key(value, key) for key in keys)


def _safe_component(value: Any, fallback: str) -> str:
    text = str(value).strip() if value is not None else fallback
    safe = "".join(char if char.isalnum() or char in {"-", "_", "."} else "_" for char in text)
    return safe.strip("._") or fallback


def _false_non_claims() -> dict[str, bool]:
    return {name: False for name in REQUIRED_FALSE_NON_CLAIMS}


def _declared_non_claims_actual(request: Mapping[str, Any]) -> dict[str, Any]:
    non_claims = request.get("declared_non_claims")
    if not isinstance(non_claims, Mapping):
        return {
            "declared_non_claims_present": False,
            "missing_non_claims": list(REQUIRED_FALSE_NON_CLAIMS),
            "flipped_non_claims": [],
        }
    return {
        "declared_non_claims_present": True,
        "missing_non_claims": [
            name for name in REQUIRED_FALSE_NON_CLAIMS if name not in non_claims
        ],
        "flipped_non_claims": [
            name
            for name in REQUIRED_FALSE_NON_CLAIMS
            if name in non_claims and non_claims[name] is not False
        ],
        "declared_non_claims": _sanitize(non_claims),
    }


def _declared_non_claims_false(request: Mapping[str, Any]) -> bool:
    non_claims = request.get("declared_non_claims")
    return isinstance(non_claims, Mapping) and all(
        name in non_claims and non_claims[name] is False
        for name in REQUIRED_FALSE_NON_CLAIMS
    )


def _basis_value(value: Any) -> Any:
    if isinstance(value, Mapping):
        return _sanitize(value)
    if isinstance(value, (str, Path)):
        return {"selected_basis_reference": str(value), "selected_basis_is_path_reference": True}
    return _sanitize(value)


def _basis_section(value: Any, label: str) -> dict[str, Any]:
    declared = _present(value)
    forbidden = _contains_forbidden_full_body_key(value)
    return {
        f"{label}_declared": declared,
        "selected_basis": _basis_value(value) if declared else {},
        "selected_basis_is_reference_shaped": declared and not forbidden,
        "selected_basis_remains_basis_only": True,
        "selected_basis_does_not_create_command_invocation_authorization": True,
        "selected_basis_does_not_invoke_command": True,
        "selected_basis_does_not_execute_command": True,
        "selected_basis_does_not_create_command_output": True,
        "selected_basis_does_not_create_command_result": True,
        "selected_basis_does_not_create_command_success": True,
        "selected_basis_does_not_create_execution_permission": True,
        "selected_basis_does_not_create_execution_approval": True,
        "selected_basis_does_not_create_standing_lane": True,
        "selected_basis_does_not_create_repeat_permission": True,
        "selected_basis_does_not_reopen_consumed_request": True,
        "selected_basis_does_not_create_authority_currentness_final_completion": True,
        "selected_basis_does_not_authorize_continuation_or_follow_on_work": True,
        "full_prior_artifact_body_not_emitted": not forbidden,
        "prior_artifacts_not_mutated": True,
    }


def _request_outcome(request: Mapping[str, Any], request_key: str, basis_key: str) -> Any:
    return request.get(request_key) or _find_first(
        request.get(basis_key),
        (request_key, "selected_result_outcome", "result_outcome", "outcome"),
    )


def _request_failed_count(request: Mapping[str, Any], request_key: str, basis_key: str) -> int | None:
    for value in (
        request.get(request_key),
        _find_first(
            request.get(basis_key),
            (request_key, "selected_result_failed_check_count", "failed_check_count"),
        ),
    ):
        count = _to_int(value)
        if count is not None:
            return count
    return None


def _command_execution_review_outcome(request: Mapping[str, Any]) -> Any:
    return _request_outcome(
        request,
        "selected_command_execution_review_result_outcome",
        "selected_command_execution_review_basis",
    )


def _command_execution_review_failed_check_count(request: Mapping[str, Any]) -> int | None:
    return _request_failed_count(
        request,
        "selected_command_execution_review_failed_check_count",
        "selected_command_execution_review_basis",
    )


def _execution_review_boundary_outcome(request: Mapping[str, Any]) -> Any:
    return _request_outcome(
        request,
        "selected_execution_review_boundary_result_outcome",
        "selected_execution_review_boundary_basis",
    )


def _execution_review_boundary_failed_check_count(request: Mapping[str, Any]) -> int | None:
    return _request_failed_count(
        request,
        "selected_execution_review_boundary_failed_check_count",
        "selected_execution_review_boundary_basis",
    )


def _request_consumption_outcome(request: Mapping[str, Any]) -> Any:
    return _request_outcome(
        request,
        "selected_request_consumption_result_outcome",
        "selected_request_consumption_basis",
    )


def _request_consumption_failed_check_count(request: Mapping[str, Any]) -> int | None:
    return _request_failed_count(
        request,
        "selected_request_consumption_failed_check_count",
        "selected_request_consumption_basis",
    )


def _v2_outcome(request: Mapping[str, Any]) -> Any:
    return _request_outcome(
        request,
        "selected_v2_admitted_request_outcome",
        "selected_v2_admitted_request_basis",
    )


def _v2_version(request: Mapping[str, Any]) -> Any:
    return request.get("selected_v2_admitted_request_version") or _find_first(
        request.get("selected_v2_admitted_request_basis"),
        (
            "selected_v2_admitted_request_version",
            "single_live_command_invocation_request_admission_result_version",
            "selected_result_version",
            "result_version",
            "version",
        ),
    )


def _v2_failed_check_count(request: Mapping[str, Any]) -> int | None:
    return _request_failed_count(
        request,
        "selected_v2_failed_check_count",
        "selected_v2_admitted_request_basis",
    )


def _v2_successor_metadata(request: Mapping[str, Any]) -> dict[str, Any]:
    explicit = request.get("selected_v2_successor_metadata")
    basis = request.get("selected_v2_admitted_request_basis")
    metadata = _sanitize(explicit) if isinstance(explicit, Mapping) else {}
    for key in ("successor_of", "successor_reason", "resolver_module"):
        value = metadata.get(key) or _find_first(basis, (key,))
        if value is not None:
            metadata[key] = _sanitize(value)
    return metadata


def _v2_successor_metadata_preserved(request: Mapping[str, Any]) -> bool:
    metadata = _v2_successor_metadata(request)
    return (
        metadata.get("successor_of") == V1_PREDECESSOR_RESOLVER_MODULE
        and _present(metadata.get("successor_reason"))
        and metadata.get("resolver_module") in {None, V2_RESOLVER_MODULE}
    )


def _v2_returned_result_containment_preserved(request: Mapping[str, Any]) -> bool:
    keys = (
        "returned_result_containment_preserved",
        "v2_raw_full_prior_artifact_values_omitted",
        "raw_full_prior_artifact_values_omitted",
        "full_prior_artifact_body_not_returned",
    )
    return _find_truthy(request.get("selected_v2_admitted_request_basis"), keys) or _find_truthy(
        request.get("returned_result_containment_posture"), keys
    )


def _consumed_token_closed(request: Mapping[str, Any]) -> bool:
    keys = (
        "consumption_token_closed",
        "consumed_request_token_remains_closed",
        "consumed_token_closed",
        "request_consumed",
        "admitted_single_live_command_invocation_request_consumed",
    )
    return (
        _find_truthy(request.get("selected_consumed_request_basis"), keys)
        or _find_truthy(request.get("selected_request_consumption_basis"), keys)
        or _find_truthy(request.get("consumed_token_closed_posture"), keys)
    )


def _consumed_request_reopened(request: Mapping[str, Any]) -> bool:
    return _contains_truthy_key(request, "consumed_request_reopened") or _contains_truthy_key(
        request, "consumed_token_reopened"
    )


def _scope_values(value: Any) -> list[str]:
    if isinstance(value, Mapping):
        for key in (
            "selected_scope_values",
            "scope_values",
            "command_invocation_authorization_boundary_scope",
        ):
            selected = value.get(key)
            if isinstance(selected, str):
                return [selected]
            if isinstance(selected, Sequence) and not isinstance(selected, (str, bytes, bytearray)):
                return [str(item) for item in selected]
        return [
            str(key)
            for key, item in value.items()
            if isinstance(key, str) and key.upper() == key and _truthy(item)
        ]
    if isinstance(value, str):
        return [value]
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return [str(item) for item in value]
    return []


def _result_basis_section(
    request: Mapping[str, Any],
    basis_key: str,
    path_key: str,
    id_key: str,
    outcome_key: str,
    failed_key: str,
    expected_outcome: str,
) -> dict[str, Any]:
    basis = request.get(basis_key)
    outcome = _request_outcome(request, outcome_key, basis_key)
    failed_count = _request_failed_count(request, failed_key, basis_key)
    section = _basis_section(basis, basis_key)
    section.update(
        {
            path_key: _sanitize(request.get(path_key) or _find_first(basis, (path_key, "selected_result_path", "result_path", "path"))),
            id_key: _sanitize(request.get(id_key) or _find_first(basis, (id_key, "selected_result_id", "result_id"))),
            outcome_key: _sanitize(outcome),
            failed_key: failed_count,
            f"{basis_key}_outcome_expected": outcome == expected_outcome,
            f"{basis_key}_failed_check_count_zero": failed_count == 0,
        }
    )
    return section


def _selected_command_execution_review_section(request: Mapping[str, Any]) -> dict[str, Any]:
    section = _result_basis_section(
        request,
        "selected_command_execution_review_basis",
        "selected_command_execution_review_result_path",
        "selected_command_execution_review_result_id",
        "selected_command_execution_review_result_outcome",
        "selected_command_execution_review_failed_check_count",
        COMMAND_EXECUTION_REVIEW_OUTCOME,
    )
    section.update(
        {
            "command_execution_review_basis_remains_review_basis_only": True,
            "command_execution_review_did_not_create_command_invocation_authorization": True,
            "command_execution_review_did_not_authorize_invocation_execution_output_result_success": True,
            "command_execution_review_did_not_create_execution_permission_or_approval": True,
            "command_execution_review_did_not_create_standing_lane_repeat_permission_final_completion_continuation_reusable_permission_follow_on_work": True,
        }
    )
    return section


def _selected_command_execution_review_terminal_summary_section(request: Mapping[str, Any]) -> dict[str, Any]:
    basis = request.get("selected_command_execution_review_terminal_summary_basis")
    section = _basis_section(basis, "selected_command_execution_review_terminal_summary_basis")
    section.update(
        {
            "selected_command_execution_review_terminal_summary_path": _sanitize(
                request.get("selected_command_execution_review_terminal_summary_path")
                or _find_first(basis, ("selected_command_execution_review_terminal_summary_path", "terminal_summary_path", "path"))
            ),
            "terminal_summary_remains_readability_basis_only": True,
            "terminal_summary_does_not_create_command_invocation_authorization": True,
            "terminal_summary_does_not_authorize_command_invocation": True,
            "terminal_summary_does_not_authorize_command_execution": True,
            "terminal_summary_does_not_create_command_output_result_success": True,
            "terminal_summary_does_not_create_execution_permission_or_approval": True,
        }
    )
    return section


def _selected_execution_review_boundary_section(request: Mapping[str, Any]) -> dict[str, Any]:
    section = _result_basis_section(
        request,
        "selected_execution_review_boundary_basis",
        "selected_execution_review_boundary_result_path",
        "selected_execution_review_boundary_result_id",
        "selected_execution_review_boundary_result_outcome",
        "selected_execution_review_boundary_failed_check_count",
        EXECUTION_REVIEW_BOUNDARY_OUTCOME,
    )
    section.update(
        {
            "execution_review_boundary_basis_remains_boundary_basis_only": True,
            "execution_review_boundary_did_not_perform_command_execution_review": True,
            "execution_review_boundary_did_not_create_command_invocation_authorization": True,
            "execution_review_boundary_did_not_authorize_invocation_execution_output_result_success": True,
            "execution_review_boundary_did_not_create_execution_permission_or_approval": True,
        }
    )
    return section


def _selected_request_consumption_section(request: Mapping[str, Any]) -> dict[str, Any]:
    basis = request.get("selected_request_consumption_basis")
    section = _result_basis_section(
        request,
        "selected_request_consumption_basis",
        "selected_request_consumption_result_path",
        "selected_request_consumption_result_id",
        "selected_request_consumption_result_outcome",
        "selected_request_consumption_failed_check_count",
        REQUEST_CONSUMPTION_OUTCOME,
    )
    section.update(
        {
            "selected_request_consumption_outcome_consumed": _request_consumption_outcome(request) == REQUEST_CONSUMPTION_OUTCOME,
            "selected_request_consumption_failed_check_count_zero": _request_consumption_failed_check_count(request) == 0,
            "request_consumed_exactly_once": _find_truthy(basis, ("request_consumed_exactly_once", "request_consumed", "admitted_single_live_command_invocation_request_consumed")),
            "consumption_token_closed": _find_truthy(basis, ("consumption_token_closed", "consumed_token_closed")),
            "consumed_request_basis_recorded": _find_truthy(basis, ("consumed_request_basis_recorded", "request_consumed")),
            "request_consumption_basis_does_not_create_command_invocation_authorization": True,
            "request_consumption_basis_does_not_authorize_invocation_execution_output_result_success": True,
            "request_consumption_basis_does_not_create_execution_permission_or_approval": True,
            "request_consumption_basis_does_not_create_standing_lane_or_repeat_permission": True,
        }
    )
    return section


def _selected_consumed_request_section(request: Mapping[str, Any]) -> dict[str, Any]:
    basis = request.get("selected_consumed_request_basis")
    closed = _consumed_token_closed(request)
    reopened = _consumed_request_reopened(request)
    section = _basis_section(basis, "selected_consumed_request_basis")
    section.update(
        {
            "consumed_request_basis_recorded": _present(basis),
            "consumed_request_token_closed": closed,
            "consumed_request_token_remains_closed": closed and not reopened,
            "consumed_request_not_reopened": not reopened,
            "consumed_request_basis_is_not_command_invocation_authorization": True,
            "consumed_request_basis_is_not_command_success": True,
            "consumed_request_basis_for_one_future_authorization_review_only": True,
        }
    )
    return section


def _selected_v2_basis_section(request: Mapping[str, Any]) -> dict[str, Any]:
    basis = request.get("selected_v2_admitted_request_basis")
    outcome = _v2_outcome(request)
    version = _v2_version(request)
    failed_count = _v2_failed_check_count(request)
    section = _basis_section(basis, "selected_v2_admitted_request_basis")
    section.update(
        {
            "selected_v2_admitted_request_artifact_path": _sanitize(request.get("selected_v2_admitted_request_artifact_path") or _find_first(basis, ("selected_v2_admitted_request_artifact_path", "selected_result_path", "result_path"))),
            "selected_v2_admitted_request_artifact_id": _sanitize(request.get("selected_v2_admitted_request_artifact_id") or _find_first(basis, ("selected_v2_admitted_request_artifact_id", "selected_result_id", "result_id"))),
            "selected_v2_admitted_request_outcome": _sanitize(outcome),
            "selected_v2_admitted_request_version": _sanitize(version),
            "selected_v2_failed_check_count": failed_count,
            "selected_v2_outcome_admitted": outcome == V2_ADMITTED_REQUEST_OUTCOME,
            "selected_v2_version_0_2_0": version == V2_ADMITTED_REQUEST_VERSION,
            "selected_v2_failed_check_count_zero": failed_count == 0,
            "selected_v2_successor_metadata": _v2_successor_metadata(request),
            "selected_v2_successor_metadata_preserved": _v2_successor_metadata_preserved(request),
            "selected_v2_returned_result_containment_preserved": _v2_returned_result_containment_preserved(request),
            "v2_remains_lineage_evidence_only": True,
            "v2_does_not_claim_v1_passed": not _contains_truthy_key(request, "v1_claimed_passed") and not _contains_truthy_key(request, "v1_passed"),
        }
    )
    return section


def _selected_v1_predecessor_section(request: Mapping[str, Any]) -> dict[str, Any]:
    basis = request.get("selected_v1_predecessor_failure_basis")
    section = _basis_section(basis, "selected_v1_predecessor_failure_basis")
    section.update(
        {
            "selected_v1_predecessor_artifact_path": _sanitize(request.get("selected_v1_predecessor_artifact_path") or _find_first(basis, ("selected_v1_predecessor_artifact_path", "selected_result_path", "result_path"))),
            "selected_v1_predecessor_artifact_id": _sanitize(request.get("selected_v1_predecessor_artifact_id") or _find_first(basis, ("selected_v1_predecessor_artifact_id", "selected_result_id", "result_id"))),
            "selected_v1_predecessor_outcome": _sanitize(request.get("selected_v1_predecessor_outcome") or _find_first(basis, ("selected_v1_predecessor_outcome", "selected_result_outcome", "outcome"))),
            "v1_predecessor_failure_remains_visible": _present(basis) and not _contains_truthy_key(request, "v1_hidden"),
            "v1_is_not_repaired": not _contains_truthy_key(request, "v1_repaired"),
            "v1_is_not_hidden": not _contains_truthy_key(request, "v1_hidden"),
            "v1_is_not_claimed_passed": not _contains_truthy_key(request, "v1_claimed_passed") and not _contains_truthy_key(request, "v1_passed"),
            "v2_successor_does_not_erase_v1": not _contains_truthy_key(request, "v2_treated_as_repairing_v1"),
            "predecessor_failure_evidence_is_lineage_evidence_only": True,
        }
    )
    return section


def _reference_basis_section(request: Mapping[str, Any], key: str, label: str, path_key: str) -> dict[str, Any]:
    basis = request.get(key)
    section = _basis_section(basis, label)
    section[path_key] = _sanitize(
        request.get(path_key) or _find_first(basis, (path_key, "selected_result_path", "result_path", "path"))
    )
    section.update(
        {
            "reference_basis_only": True,
            "does_not_create_command_invocation_authorization": True,
            "does_not_create_command_invocation": True,
            "does_not_perform_command_execution": True,
            "does_not_create_command_output_result_success": True,
            "does_not_create_execution_permission_or_approval": True,
            "does_not_create_standing_invocation_lane_or_repeat_permission": True,
            "does_not_create_authority_currentness_final_completion": True,
            "does_not_authorize_continuation_reusable_permission_follow_on_work": True,
        }
    )
    return section


def _posture_section(value: Any, label: str) -> dict[str, Any]:
    declared = _present(value)
    forbidden = _contains_forbidden_full_body_key(value)
    return {
        f"{label}_declared": declared,
        "selected_posture": _basis_value(value) if declared else {},
        "selected_posture_is_reference_shaped": declared and not forbidden,
        "command_invocation_authorization_boundary_only": True,
        "one_future_authorization_review_only": True,
        "command_invocation_authorization_not_created": True,
        "command_invocation_not_created": True,
        "command_execution_not_performed": True,
        "command_output_result_success_not_created": True,
        "execution_permission_not_created": True,
        "execution_approval_not_created": True,
        "consumed_request_not_reopened": True,
        "no_standing_invocation_lane": True,
        "no_repeat_invocation_permission": True,
        "returned_result_containment_preserved": True,
        "full_prior_artifact_body_not_emitted": not forbidden,
    }


def _scope_section(value: Any) -> dict[str, Any]:
    values = _scope_values(value)
    value_set = set(values)
    unsupported = [item for item in values if item not in SUPPORTED_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_SCOPE]
    return {
        "selected_scope_values": values,
        "unsupported_scope_values": unsupported,
        "all_selected_scope_values_supported": bool(values) and not unsupported,
        "supported_scope_values": sorted(SUPPORTED_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_SCOPE),
        "command_invocation_authorization_boundary_only": "COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_ONLY" in value_set,
        "command_invocation_authorization_not_created": "COMMAND_INVOCATION_AUTHORIZATION_NOT_CREATED" in value_set,
        "one_future_authorization_review_only": "ONE_FUTURE_AUTHORIZATION_REVIEW_ONLY" in value_set,
        "reviewed_command_execution_review_basis_preserved": "REVIEWED_COMMAND_EXECUTION_REVIEW_BASIS_PRESERVED" in value_set,
        "reviewed_consumed_request_basis_preserved": "REVIEWED_CONSUMED_REQUEST_BASIS_PRESERVED" in value_set,
        "consumed_request_token_remains_closed": "CONSUMED_REQUEST_TOKEN_REMAINS_CLOSED" in value_set,
        "consumed_request_not_reopened": "CONSUMED_REQUEST_NOT_REOPENED" in value_set,
        "command_invocation_not_created": "COMMAND_INVOCATION_NOT_CREATED" in value_set,
        "command_execution_not_performed": "COMMAND_EXECUTION_NOT_PERFORMED" in value_set,
        "command_output_not_created": "COMMAND_OUTPUT_NOT_CREATED" in value_set,
        "command_result_not_created": "COMMAND_RESULT_NOT_CREATED" in value_set,
        "command_success_not_created": "COMMAND_SUCCESS_NOT_CREATED" in value_set,
        "execution_permission_not_created": "EXECUTION_PERMISSION_NOT_CREATED" in value_set,
        "execution_approval_not_created": "EXECUTION_APPROVAL_NOT_CREATED" in value_set,
        "no_standing_invocation_lane_created": "NO_STANDING_INVOCATION_LANE_CREATED" in value_set,
        "no_repeat_invocation_permission_created": "NO_REPEAT_INVOCATION_PERMISSION_CREATED" in value_set,
        "authorization_boundary_is_not_authorization": "AUTHORIZATION_BOUNDARY_IS_NOT_AUTHORIZATION" in value_set,
        "authorization_boundary_is_not_invocation": "AUTHORIZATION_BOUNDARY_IS_NOT_INVOCATION" in value_set,
        "reviewed_basis_is_not_command_invocation_authorization": "REVIEWED_BASIS_IS_NOT_COMMAND_INVOCATION_AUTHORIZATION" in value_set,
        "reviewed_basis_is_not_command_success": "REVIEWED_BASIS_IS_NOT_COMMAND_SUCCESS" in value_set,
        "v1_predecessor_failure_remains_visible": "V1_PREDECESSOR_FAILURE_REMAINS_VISIBLE" in value_set,
        "v2_successor_does_not_repair_v1": "V2_SUCCESSOR_DOES_NOT_REPAIR_V1" in value_set,
        "returned_result_containment_preserved": "RETURNED_RESULT_CONTAINMENT_PRESERVED" in value_set,
        "reference_shaped_basis_required": "REFERENCE_SHAPED_BASIS_REQUIRED" in value_set,
        "full_prior_artifact_body_not_emitted": "FULL_PRIOR_ARTIFACT_BODY_NOT_EMITTED" in value_set,
        "no_authority_created": "NO_AUTHORITY_CREATED" in value_set,
        "no_currentness_created": "NO_CURRENTNESS_CREATED" in value_set,
        "no_final_completion": "NO_FINAL_COMPLETION" in value_set,
        "no_continuation_authorized": "NO_CONTINUATION_AUTHORIZED" in value_set,
        "no_reusable_permission": "NO_REUSABLE_PERMISSION" in value_set,
        "no_follow_on_work_authorized": "NO_FOLLOW_ON_WORK_AUTHORIZED" in value_set,
    }


def _check(check_name: str, passed: bool, expected_posture: Any, actual_posture: Any, code: str) -> dict[str, Any]:
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": _sanitize(expected_posture),
        "actual_posture": _sanitize(actual_posture),
        "block_code": None if passed else code,
        "failure_code": None if passed else code,
    }


def _build_checks(request: Mapping[str, Any], malformed_code: str | None) -> list[dict[str, Any]]:
    if malformed_code:
        return [
            _check(
                "declared command invocation authorization boundary request is a mapping",
                False,
                "mapping",
                malformed_code,
                malformed_code,
            )
        ]
    checks: list[dict[str, Any]] = []
    question = request.get("command_invocation_authorization_boundary_question")
    intent = request.get("command_invocation_authorization_boundary_intent")
    checks.append(_check("command invocation authorization boundary question declared", _present(question), "declared", question, "COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_QUESTION_UNDECLARED"))
    checks.append(_check("command invocation authorization boundary intent supported", intent in SUPPORTED_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_INTENTS, sorted(SUPPORTED_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_INTENTS), intent, "COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_INTENT_UNSUPPORTED"))
    for name, key, code in BASIS_FIELD_CHECKS:
        checks.append(_check(name, _present(request.get(key)), "declared", request.get(key), code))
    checks.extend(
        [
            _check("command execution review live artifact recorded outcome", _command_execution_review_outcome(request) == COMMAND_EXECUTION_REVIEW_OUTCOME, COMMAND_EXECUTION_REVIEW_OUTCOME, _command_execution_review_outcome(request), "COMMAND_EXECUTION_REVIEW_NOT_RECORDED"),
            _check("command execution review live artifact failed check count zero", _command_execution_review_failed_check_count(request) == 0, 0, _command_execution_review_failed_check_count(request), "COMMAND_EXECUTION_REVIEW_FAILED_CHECKS_PRESENT"),
            _check("execution-review boundary live artifact recorded outcome", _execution_review_boundary_outcome(request) == EXECUTION_REVIEW_BOUNDARY_OUTCOME, EXECUTION_REVIEW_BOUNDARY_OUTCOME, _execution_review_boundary_outcome(request), "EXECUTION_REVIEW_BOUNDARY_NOT_RECORDED"),
            _check("execution-review boundary live artifact failed check count zero", _execution_review_boundary_failed_check_count(request) == 0, 0, _execution_review_boundary_failed_check_count(request), "EXECUTION_REVIEW_BOUNDARY_FAILED_CHECKS_PRESENT"),
            _check("request-consumption live artifact consumed outcome", _request_consumption_outcome(request) == REQUEST_CONSUMPTION_OUTCOME, REQUEST_CONSUMPTION_OUTCOME, _request_consumption_outcome(request), "REQUEST_CONSUMPTION_NOT_CONSUMED"),
            _check("request-consumption live artifact failed check count zero", _request_consumption_failed_check_count(request) == 0, 0, _request_consumption_failed_check_count(request), "REQUEST_CONSUMPTION_FAILED_CHECKS_PRESENT"),
            _check("consumed request token remains closed", _consumed_token_closed(request), "closed", {"consumed_token_closed": _consumed_token_closed(request), "consumed_request_reopened": _consumed_request_reopened(request)}, "CONSUMED_TOKEN_NOT_CLOSED"),
            _check("consumed request not reopened", not _consumed_request_reopened(request), False, _first_truthy_key(request, ("consumed_request_reopened", "consumed_token_reopened")), "CONSUMED_REQUEST_REOPENED"),
            _check("v2 admitted request outcome admitted", _v2_outcome(request) == V2_ADMITTED_REQUEST_OUTCOME, V2_ADMITTED_REQUEST_OUTCOME, _v2_outcome(request), "V2_ADMITTED_REQUEST_NOT_ADMITTED"),
            _check("v2 admitted request version 0.2.0", _v2_version(request) == V2_ADMITTED_REQUEST_VERSION, V2_ADMITTED_REQUEST_VERSION, _v2_version(request), "V2_ADMITTED_REQUEST_VERSION_NOT_0_2_0"),
            _check("v2 admitted request failed check count zero", _v2_failed_check_count(request) == 0, 0, _v2_failed_check_count(request), "V2_ADMITTED_REQUEST_FAILED_CHECKS_PRESENT"),
            _check("v2 successor metadata preserved", _v2_successor_metadata_preserved(request), {"successor_of": V1_PREDECESSOR_RESOLVER_MODULE, "successor_reason": "declared"}, _v2_successor_metadata(request), "V2_SUCCESSOR_METADATA_MISSING"),
            _check("v2 returned-result containment preserved", _v2_returned_result_containment_preserved(request), "preserved", _v2_returned_result_containment_preserved(request), "V2_RETURNED_RESULT_CONTAINMENT_MISSING"),
            _check("v1 predecessor failure remains visible", _present(request.get("selected_v1_predecessor_failure_basis")) and not _contains_truthy_key(request, "v1_hidden"), "visible", {"declared": _present(request.get("selected_v1_predecessor_failure_basis")), "v1_hidden": _contains_truthy_key(request, "v1_hidden")}, "V1_FAILURE_HIDDEN"),
            _check("v2 does not claim v1 passed", not _contains_truthy_key(request, "v1_claimed_passed") and not _contains_truthy_key(request, "v1_passed"), False, _first_truthy_key(request, ("v1_claimed_passed", "v1_passed")), "V1_CLAIMED_PASSED"),
            _check("v2 does not repair v1", not any(_contains_truthy_key(request, key) for key in ("v2_treated_as_repairing_v1", "v2_successor_repairs_v1", "v1_repaired")), False, _first_truthy_key(request, ("v2_treated_as_repairing_v1", "v2_successor_repairs_v1", "v1_repaired")), "V2_TREATED_AS_REPAIRING_V1"),
        ]
    )
    for name, key, code in POSTURE_FIELD_CHECKS:
        checks.append(_check(name, _present(request.get(key)), "declared", request.get(key), code))
    scope = _scope_section(request.get("command_invocation_authorization_boundary_scope"))
    checks.append(_check("command invocation authorization boundary scope supported", scope["all_selected_scope_values_supported"], sorted(SUPPORTED_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_SCOPE), scope["selected_scope_values"], "UNSUPPORTED_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_SCOPE"))
    checks.append(_check("reference-shaped input posture declared or preserved", _present(request.get("reference_shaped_input_posture")) or scope["reference_shaped_basis_required"] or not _contains_forbidden_full_body_key(request), "reference-shaped", {"reference_shaped_input_posture": request.get("reference_shaped_input_posture"), "forbidden_full_body_keys_detected": _forbidden_full_body_keys(request)}, "FULL_PRIOR_ARTIFACT_BODY_EMITTED"))
    checks.append(_check("raw full prior artifact body not emitted", not _contains_forbidden_full_body_key(request) and not _contains_truthy_key(request, "raw_full_prior_artifact_body_returned"), False, {"forbidden_full_body_keys_detected": _forbidden_full_body_keys(request), "raw_full_prior_artifact_body_returned": _contains_truthy_key(request, "raw_full_prior_artifact_body_returned")}, "FULL_PRIOR_ARTIFACT_BODY_EMITTED"))
    for name, keys, code in COLLAPSE_CHECKS:
        checks.append(_check(name, not any(_contains_truthy_key(request, key) for key in keys), False, _first_truthy_key(request, keys), code))
    checks.append(_check("no mutation/replay/merge", not any(_contains_truthy_key(request, key) for key in ("mutation_performed", "replay_performed", "merge_performed")), False, _first_truthy_key(request, ("mutation_performed", "replay_performed", "merge_performed")), "MUTATION_REPLAY_OR_MERGE_DETECTED"))
    checks.append(_check("non-claims remain false", _declared_non_claims_false(request), _false_non_claims(), _declared_non_claims_actual(request), "NON_CLAIM_MISSING_OR_FLIPPED"))
    return checks


def _checks_summary(checks: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    records = [_sanitize(check) for check in checks]
    failed = [
        str(check.get("block_code") or check.get("failure_code"))
        for check in records
        if check.get("passed") is not True
    ]
    return {
        "records": records,
        "passed_check_count": sum(1 for check in records if check.get("passed") is True),
        "failed_check_count": len(failed),
        "failed_check_codes": failed,
    }


def _first_failed_code(checks: Sequence[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is not True:
            return str(check.get("block_code") or check.get("failure_code"))
    return None


def _first_collapse_code(request: Mapping[str, Any]) -> str | None:
    if _consumed_request_reopened(request):
        return "CONSUMED_REQUEST_REOPENED"
    for key, code in COLLAPSE_CODE_BY_KEY:
        if _contains_truthy_key(request, key):
            return code
    if any(_contains_truthy_key(request, key) for key in ("mutation_performed", "replay_performed", "merge_performed")):
        return "MUTATION_REPLAY_OR_MERGE_DETECTED"
    return None


def _determine_block_code(request: Mapping[str, Any], checks: Sequence[Mapping[str, Any]], malformed_code: str | None) -> str | None:
    if malformed_code:
        return malformed_code
    if request.get("command_invocation_authorization_boundary_intent") == INTENT_BLOCK:
        return "COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_EXPLICITLY_BLOCKED"
    if request.get("requested_command_invocation_authorization_boundary_outcome") == OUTCOME_BLOCKED:
        return "COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_EXPLICITLY_BLOCKED"
    requested = request.get("requested_command_invocation_authorization_boundary_outcome")
    if _present(requested) and requested not in OUTCOME_FAMILY:
        return "DECLARED_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_REQUEST_MALFORMED"
    if _contains_forbidden_full_body_key(request) or _contains_truthy_key(request, "raw_full_prior_artifact_body_returned"):
        return "FULL_PRIOR_ARTIFACT_BODY_EMITTED"
    return _first_collapse_code(request) or _first_failed_code(checks)


def _determine_outcome(request: Mapping[str, Any], block_code: str | None) -> str:
    if block_code is not None:
        return OUTCOME_BLOCKED
    requested = request.get("requested_command_invocation_authorization_boundary_outcome")
    if requested in {OUTCOME_RECORDED, OUTCOME_NOT_RECORDED, OUTCOME_REQUIRES_ADDITIONAL_BASIS}:
        return str(requested)
    if request.get("command_invocation_authorization_boundary_intent") == INTENT_DO_NOT_RECORD:
        return OUTCOME_NOT_RECORDED
    if _present(request.get("additional_basis_context")):
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS
    if _present(request.get("not_recorded_basis")):
        return OUTCOME_NOT_RECORDED
    return OUTCOME_RECORDED


def _block(code: str | None, reason: str | None = None) -> dict[str, Any]:
    return {
        "blocked": code is not None,
        "block_code": code,
        "block_reason": _sanitize(reason if reason is not None else code),
        "raw_full_prior_artifact_body_returned": False,
        "block_evidence_is_contained": True,
    }


def _statement(outcome: str) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    statement = {key: recorded for key in ALLOWED_RECORDED_TRUE_FIELDS}
    statement.update(
        {
            "command_invocation_authorization_boundary_only": True,
            "authorization_boundary_is_not_authorization": True,
            "authorization_boundary_is_not_invocation": True,
            "reviewed_basis_is_not_command_invocation_authorization": True,
            "reviewed_basis_is_not_command_success": True,
            "consumed_request_not_reopened": True,
            "command_invocation_authorization_not_created": True,
            "command_invocation_not_created": True,
            "command_execution_not_performed": True,
            "command_output_not_created": True,
            "command_result_not_created": True,
            "command_success_not_created": True,
            "execution_permission_not_created": True,
            "execution_approval_not_created": True,
            "no_standing_invocation_lane_created": True,
            "no_repeat_invocation_permission_created": True,
            "command_output_not_source": True,
            "command_result_not_authority": True,
            "command_success_not_currentness": True,
            "command_success_not_final_completion": True,
            "full_prior_artifact_body_not_emitted": True,
            "artifacts_not_mutated": True,
            "deployment_runtime_public_release_not_created": True,
            "operation_permission_public_readiness_final_completion_not_created": True,
            "continuation_reusable_permission_follow_on_work_not_authorized": True,
            "derivative_reception_vessel_relation_another_reception_request_not_authorized": True,
        }
    )
    statement.update({key: False for key in REQUIRED_FALSE_NON_CLAIMS})
    return statement


def _command_invocation_authorization_boundary_non_meaning() -> dict[str, bool]:
    return {
        "authorization_boundary_does_not_mean_command_invocation_authorization_exists": True,
        "authorization_boundary_does_not_mean_command_invocation_permission_exists": True,
        "authorization_boundary_does_not_mean_command_invocation_created": True,
        "authorization_boundary_does_not_mean_command_executed": True,
        "authorization_boundary_does_not_mean_command_output_exists": True,
        "authorization_boundary_does_not_mean_command_result_exists": True,
        "authorization_boundary_does_not_mean_command_success_exists": True,
        "authorization_boundary_does_not_mean_execution_permission_exists": True,
        "authorization_boundary_does_not_mean_execution_approval_exists": True,
        "authorization_boundary_does_not_mean_command_success_creates_currentness": True,
        "authorization_boundary_does_not_mean_command_success_claims_final_completion": True,
        "authorization_boundary_does_not_mean_command_output_becomes_source": True,
        "authorization_boundary_does_not_mean_command_result_becomes_authority": True,
        "authorization_boundary_does_not_mean_standing_invocation_lane_exists": True,
        "authorization_boundary_does_not_mean_repeat_invocation_permission_exists": True,
        "authorization_boundary_does_not_mean_consumed_request_token_reopened": True,
        "authorization_boundary_does_not_mean_v1_was_repaired": True,
        "authorization_boundary_does_not_mean_v1_was_hidden": True,
        "authorization_boundary_does_not_mean_v1_passed": True,
        "authorization_boundary_does_not_mean_deployment_created": True,
        "authorization_boundary_does_not_mean_runtime_hosting_created": True,
        "authorization_boundary_does_not_mean_public_release_created": True,
        "authorization_boundary_does_not_mean_public_readiness_created": True,
        "authorization_boundary_does_not_mean_final_completion_claimed": True,
        "authorization_boundary_does_not_mean_continuation_authorized": True,
        "authorization_boundary_does_not_mean_reusable_permission_created": True,
        "authorization_boundary_does_not_mean_derivative_reception_authorized": True,
        "authorization_boundary_does_not_mean_vessel_relation_authorized": True,
        "authorization_boundary_does_not_mean_another_reception_request_authorized": True,
        "authorization_boundary_does_not_mean_follow_on_work_authorized": True,
    }


def _additional_basis_required(outcome: str, request: Mapping[str, Any]) -> dict[str, Any]:
    required = outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    return {
        "additional_basis_required": required,
        "additional_basis_context": _sanitize(request.get("additional_basis_context")) if required else {},
        "missing_basis_not_scheduled": True,
        "missing_basis_not_authorized": True,
        "missing_basis_not_executed": True,
        "command_invocation_authorization_not_created": True,
        "command_not_invoked": True,
        "command_not_executed": True,
        "command_output_result_success_not_created": True,
        "execution_permission_not_created": True,
        "execution_approval_not_created": True,
        "consumed_request_not_reopened": True,
        "standing_lane_repeat_permission_not_created": True,
        "follow_on_work_not_authorized": True,
    }


def _not_recorded_basis(outcome: str, request: Mapping[str, Any], checks: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    not_recorded = outcome == OUTCOME_NOT_RECORDED
    return {
        "not_recorded": not_recorded,
        "not_recorded_basis": _sanitize(request.get("not_recorded_basis")) if not_recorded else {},
        "failed_command_invocation_authorization_boundary_checks": [_sanitize(check) for check in checks if check.get("passed") is not True] if not_recorded else [],
        "not_recorded_does_not_mutate": True,
        "not_recorded_does_not_repair_prior_artifacts": True,
        "not_recorded_does_not_create_command_invocation_authorization": True,
        "not_recorded_does_not_invoke_command": True,
        "not_recorded_does_not_execute_command": True,
        "not_recorded_does_not_emit_output": True,
        "not_recorded_does_not_create_result": True,
        "not_recorded_does_not_create_success": True,
        "not_recorded_does_not_create_execution_permission_or_approval": True,
        "not_recorded_does_not_reopen_consumed_request_token": True,
        "not_recorded_does_not_create_standing_lane_or_repeat_permission": True,
        "not_recorded_does_not_deploy_publish_host_currentize_complete_or_continue": True,
        "not_recorded_does_not_authorize_follow_on_work": True,
    }


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "command invocation authorization boundary test",
            "command invocation authorization boundary live artifact",
            "actual command invocation authorization review",
            "command invocation authorization",
            "command invocation",
            "command execution",
            "command output",
            "command result",
            "command success",
            "command output/report artifact from live execution",
            "manifest implementation",
            "checksum implementation",
            "signature implementation",
            "source-body packet implementation",
            "reproducible environment declaration",
            "runtime hosting",
            "deployment",
            "public release",
            "source transfer",
            "source migration",
            "source receipt",
            "reception authorization",
            "derivative reception",
            "vessel relation",
            "adoption",
            "authority creation",
            "currentness creation",
            "operation permission",
            "public readiness",
            "final completion",
            "continuation",
            "publication flow",
            "reusable permission",
            "successor reception request",
            "follow-on work",
        ],
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }


def _metadata(request: Mapping[str, Any]) -> dict[str, Any]:
    request_id = request.get("command_invocation_authorization_boundary_request_id") or "unidentified"
    return {
        "consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_result_id": f"{request_id}__consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_result",
        "consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_result_type": "portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_result",
        "consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_result_version": RESULT_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "resolver_module": RESOLVER_MODULE,
    }


def _declared_question(request: Mapping[str, Any], request_path: Path | str | None) -> dict[str, Any]:
    question = request.get("command_invocation_authorization_boundary_question")
    return {
        "command_invocation_authorization_boundary_request_id": request.get("command_invocation_authorization_boundary_request_id"),
        "command_invocation_authorization_boundary_question": question,
        "canonical_command_invocation_authorization_boundary_question": CORE_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_QUESTION,
        "command_invocation_authorization_boundary_question_declared": _present(question),
        "command_invocation_authorization_boundary_intent": request.get("command_invocation_authorization_boundary_intent"),
        "command_invocation_authorization_boundary_request_path": str(request_path) if request_path is not None else None,
        "request_is_command_invocation_authorization_boundary_only": True,
        "request_does_not_create_authorization_invoke_or_execute_command": True,
    }


def _read_json_object(path_value: Path | str) -> tuple[dict[str, Any] | None, str | None, str | None]:
    path = Path(path_value)
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        return None, "DECLARED_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_REQUEST_UNREADABLE", str(exc)
    except json.JSONDecodeError as exc:
        return None, "DECLARED_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_REQUEST_MALFORMED", str(exc)
    if not isinstance(value, Mapping):
        return None, "DECLARED_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_REQUEST_MALFORMED", "JSON root must be an object"
    return dict(value), None, None


def _build_result(
    request_value: Any,
    *,
    request_path: Path | str | None = None,
    malformed_code: str | None = None,
    path_reason: str | None = None,
) -> dict[str, Any]:
    request = _copy(request_value) if isinstance(request_value, Mapping) else {}
    if not isinstance(request_value, Mapping) and malformed_code is None:
        malformed_code = "DECLARED_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_REQUEST_MALFORMED"
    checks = _build_checks(request, malformed_code)
    block_code = _determine_block_code(request, checks, malformed_code)
    outcome = _determine_outcome(request, block_code)
    result: dict[str, Any] = {
        "consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_metadata": _metadata(request),
        "declared_command_invocation_authorization_boundary_question": _declared_question(request, request_path),
        "selected_command_execution_review_basis": _selected_command_execution_review_section(request),
        "selected_command_execution_review_terminal_summary_basis": _selected_command_execution_review_terminal_summary_section(request),
        "selected_execution_review_boundary_basis": _selected_execution_review_boundary_section(request),
        "selected_request_consumption_basis": _selected_request_consumption_section(request),
        "selected_consumed_request_basis": _selected_consumed_request_section(request),
        "selected_v2_admitted_request_basis": _selected_v2_basis_section(request),
        "selected_v1_predecessor_failure_basis": _selected_v1_predecessor_section(request),
        "selected_command_execution_boundary_basis": _reference_basis_section(request, "selected_command_execution_boundary_basis", "selected_command_execution_boundary_basis", "selected_command_execution_boundary_result_path"),
        "selected_command_report_basis": _reference_basis_section(request, "selected_command_report_basis", "selected_command_report_basis", "selected_command_report_path"),
        "selected_command_implementation_boundary_basis": _reference_basis_section(request, "selected_command_implementation_boundary_basis", "selected_command_implementation_boundary_basis", "selected_command_implementation_boundary_result_path"),
        "selected_command_boundary_basis": _reference_basis_section(request, "selected_command_boundary_basis", "selected_command_boundary_basis", "selected_command_boundary_result_path"),
        "selected_artifact_emission_containment_basis": _reference_basis_section(request, "selected_artifact_emission_containment_basis", "selected_artifact_emission_containment_basis", "selected_artifact_emission_containment_result_path"),
        "selected_evidence_manifest_basis": _reference_basis_section(request, "selected_evidence_manifest_basis", "selected_evidence_manifest_basis", "selected_evidence_manifest_result_path"),
        "selected_portable_verification_basis": _reference_basis_section(request, "selected_portable_verification_basis", "selected_portable_verification_basis", "selected_portable_verification_result_path"),
        "authorization_boundary_only_posture": _posture_section(request.get("authorization_boundary_only_posture"), "authorization_boundary_only_posture"),
        "one_future_authorization_review_posture": _posture_section(request.get("one_future_authorization_review_posture"), "one_future_authorization_review_posture"),
        "reviewed_command_execution_review_basis_posture": _posture_section(request.get("reviewed_command_execution_review_basis_posture"), "reviewed_command_execution_review_basis_posture"),
        "consumed_token_closed_posture": _posture_section(request.get("consumed_token_closed_posture"), "consumed_token_closed_posture"),
        "no_reopen_consumed_request_posture": _posture_section(request.get("no_reopen_consumed_request_posture"), "no_reopen_consumed_request_posture"),
        "no_command_invocation_authorization_posture": _posture_section(request.get("no_command_invocation_authorization_posture"), "no_command_invocation_authorization_posture"),
        "no_command_invocation_posture": _posture_section(request.get("no_command_invocation_posture"), "no_command_invocation_posture"),
        "no_command_execution_posture": _posture_section(request.get("no_command_execution_posture"), "no_command_execution_posture"),
        "no_output_result_success_posture": _posture_section(request.get("no_output_result_success_posture"), "no_output_result_success_posture"),
        "no_execution_permission_posture": _posture_section(request.get("no_execution_permission_posture"), "no_execution_permission_posture"),
        "no_execution_approval_posture": _posture_section(request.get("no_execution_approval_posture"), "no_execution_approval_posture"),
        "no_standing_lane_posture": _posture_section(request.get("no_standing_lane_posture"), "no_standing_lane_posture"),
        "no_repeat_permission_posture": _posture_section(request.get("no_repeat_permission_posture"), "no_repeat_permission_posture"),
        "returned_result_containment_posture": _posture_section(request.get("returned_result_containment_posture"), "returned_result_containment_posture"),
        "command_invocation_authorization_boundary_scope": _scope_section(request.get("command_invocation_authorization_boundary_scope")),
        "command_invocation_authorization_boundary_checks": _checks_summary(checks),
        "command_invocation_authorization_boundary_statement": _statement(outcome),
        "command_invocation_authorization_boundary_non_meaning": _command_invocation_authorization_boundary_non_meaning(),
        "additional_basis_required": _additional_basis_required(outcome, request),
        "not_recorded_basis": _not_recorded_basis(outcome, request, checks),
        "what_remains_open": _what_remains_open(),
        "non_claims": _false_non_claims(),
        "outcome": outcome,
        "block": _block(block_code, path_reason or request.get("block_reason")),
    }
    result["consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_summary"] = build_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_summary(result)
    return _sanitize(result)


def resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_boundary(
    declared_command_invocation_authorization_boundary_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one declared consumed-request command invocation authorization boundary mapping."""

    if declared_command_invocation_authorization_boundary_request is None:
        return _build_result({})
    if not isinstance(declared_command_invocation_authorization_boundary_request, Mapping):
        return _build_result({}, malformed_code="DECLARED_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_REQUEST_MALFORMED")
    return _build_result(declared_command_invocation_authorization_boundary_request)


def resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_from_path(
    declared_command_invocation_authorization_boundary_request_path: Path | str,
) -> dict:
    """Resolve one declared consumed-request command invocation authorization boundary JSON object."""

    request, error_code, error_reason = _read_json_object(declared_command_invocation_authorization_boundary_request_path)
    if error_code:
        return _build_result(
            {},
            request_path=declared_command_invocation_authorization_boundary_request_path,
            malformed_code=error_code,
            path_reason=error_reason,
        )
    return _build_result(request, request_path=declared_command_invocation_authorization_boundary_request_path)


def build_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_summary(
    result: Mapping[str, Any]
) -> dict:
    """Build a compact non-authoritative command invocation authorization boundary summary."""

    safe_result = _sanitize(result)
    statement = _as_mapping(safe_result.get("command_invocation_authorization_boundary_statement"))
    checks = _as_mapping(safe_result.get("command_invocation_authorization_boundary_checks"))
    block = _as_mapping(safe_result.get("block"))
    question = _as_mapping(safe_result.get("declared_command_invocation_authorization_boundary_question"))
    non_claims = _as_mapping(safe_result.get("non_claims"))
    execution_review = _as_mapping(safe_result.get("selected_command_execution_review_basis"))
    boundary = _as_mapping(safe_result.get("selected_execution_review_boundary_basis"))
    consumption = _as_mapping(safe_result.get("selected_request_consumption_basis"))
    v2 = _as_mapping(safe_result.get("selected_v2_admitted_request_basis"))
    return {
        "outcome": safe_result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "command_invocation_authorization_boundary_request_id": question.get("command_invocation_authorization_boundary_request_id"),
        "command_invocation_authorization_boundary_question": question.get("command_invocation_authorization_boundary_question"),
        "command_invocation_authorization_boundary_intent": question.get("command_invocation_authorization_boundary_intent"),
        "passed_check_count": checks.get("passed_check_count", 0),
        "failed_check_count": checks.get("failed_check_count", 0),
        "command_invocation_authorization_boundary_recorded": statement.get("command_invocation_authorization_boundary_recorded", False),
        "reviewed_command_execution_review_basis_preserved": statement.get("reviewed_command_execution_review_basis_preserved", False),
        "consumed_request_token_remains_closed": statement.get("consumed_request_token_remains_closed", False),
        "single_authorization_review_conditions_declared": statement.get("single_authorization_review_conditions_declared", False),
        "authorization_still_not_created": statement.get("authorization_still_not_created", False),
        "invocation_still_not_authorized": statement.get("invocation_still_not_authorized", False),
        "invocation_requires_separate_authorization_result": statement.get("invocation_requires_separate_authorization_result", False),
        "execution_still_not_authorized": statement.get("execution_still_not_authorized", False),
        "v1_predecessor_failure_preserved": statement.get("v1_predecessor_failure_preserved", False),
        "returned_result_containment_preserved": statement.get("returned_result_containment_preserved", False),
        "not_recorded": safe_result.get("outcome") == OUTCOME_NOT_RECORDED,
        "requires_additional_basis": safe_result.get("outcome") == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "selected_command_execution_review_outcome": execution_review.get("selected_command_execution_review_result_outcome"),
        "selected_command_execution_review_failed_check_count": execution_review.get("selected_command_execution_review_failed_check_count"),
        "selected_execution_review_boundary_outcome": boundary.get("selected_execution_review_boundary_result_outcome"),
        "selected_execution_review_boundary_failed_check_count": boundary.get("selected_execution_review_boundary_failed_check_count"),
        "selected_request_consumption_outcome": consumption.get("selected_request_consumption_result_outcome"),
        "selected_request_consumption_failed_check_count": consumption.get("selected_request_consumption_failed_check_count"),
        "selected_v2_admitted_request_outcome": v2.get("selected_v2_admitted_request_outcome"),
        "selected_v2_admitted_request_version": v2.get("selected_v2_admitted_request_version"),
        "selected_v2_failed_check_count": v2.get("selected_v2_failed_check_count"),
        "command_invocation_authorization_not_created": statement.get("command_invocation_authorization_not_created", True),
        "command_invocation_not_created": statement.get("command_invocation_not_created", True),
        "command_execution_not_performed": statement.get("command_execution_not_performed", True),
        "command_output_not_created": statement.get("command_output_not_created", True),
        "command_result_not_created": statement.get("command_result_not_created", True),
        "command_success_not_created": statement.get("command_success_not_created", True),
        "execution_permission_not_created": statement.get("execution_permission_not_created", True),
        "execution_approval_not_created": statement.get("execution_approval_not_created", True),
        "no_standing_lane": statement.get("no_standing_invocation_lane_created", True),
        "no_repeat_permission": statement.get("no_repeat_invocation_permission_created", True),
        "consumed_request_not_reopened": statement.get("consumed_request_not_reopened", True),
        "authorization_boundary_not_authorization": statement.get("authorization_boundary_is_not_authorization", True),
        "authorization_boundary_not_invocation": statement.get("authorization_boundary_is_not_invocation", True),
        "reviewed_basis_not_command_invocation_authorization": statement.get("reviewed_basis_is_not_command_invocation_authorization", True),
        "reviewed_basis_not_command_success": statement.get("reviewed_basis_is_not_command_success", True),
        "v1_not_repaired": not non_claims.get("v1_repaired", True),
        "v1_not_hidden": not non_claims.get("v1_hidden", True),
        "v1_not_claimed_passed": not non_claims.get("v1_claimed_passed", True),
        "no_raw_full_prior_artifact_body_returned": not non_claims.get("raw_full_prior_artifact_body_returned", True),
        "no_artifact_mutation": not non_claims.get("prior_artifacts_mutated", True),
        "no_deployment_runtime_public_release": not non_claims.get("deployment_created", True) and not non_claims.get("runtime_hosting_created", True) and not non_claims.get("public_release_created", True),
        "no_operation_permission_public_readiness_final_completion": not non_claims.get("operation_permission_created", True) and not non_claims.get("public_launch_readiness_created", True) and not non_claims.get("final_completion_claimed", True),
        "no_continuation_publication_flow_reusable_permission": not non_claims.get("continuation_authorized", True) and not non_claims.get("publication_flow_opened", True) and not non_claims.get("reusable_permission_created", True),
        "no_derivative_reception_vessel_relation_another_reception_request_follow_on_work": not non_claims.get("derivative_reception_authorized", True) and not non_claims.get("vessel_relation_authorized", True) and not non_claims.get("another_reception_request_authorized", True) and not non_claims.get("follow_on_work_authorized", True),
        "key_non_claims": _sanitize(non_claims),
    }


def _unique_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 10000):
        candidate = path.with_name(f"{path.stem}_{index:03d}{path.suffix}")
        if not candidate.exists():
            return candidate
    raise PortableSourceBodyVerificationConsumedSingleLiveCommandInvocationRequestCommandInvocationAuthorizationBoundaryError(
        f"Could not allocate non-overwriting output path for {path}"
    )


def write_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive bounded command invocation authorization boundary result JSON file."""

    safe_result = _sanitize(result)
    question = _as_mapping(safe_result.get("declared_command_invocation_authorization_boundary_question"))
    request_id = _safe_component(question.get("command_invocation_authorization_boundary_request_id"), "unidentified")
    filename = f"{request_id}__consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_result.json"
    target = (
        PORTABLE_SOURCE_BODY_VERIFICATION_CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_ROOT
        / filename
        if output_path is None
        else Path(output_path)
    )
    if target.suffix == "":
        target = target / filename
    target.parent.mkdir(parents=True, exist_ok=True)
    target = _unique_path(target)
    target.write_text(json.dumps(safe_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return target


def build_declared_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_request(
    command_invocation_authorization_boundary_request_id: str,
    command_invocation_authorization_boundary_question: str,
    selected_command_execution_review_basis: Mapping[str, Any] | str,
    selected_command_execution_review_terminal_summary_basis: Mapping[str, Any] | str,
    selected_execution_review_boundary_basis: Mapping[str, Any] | str,
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
    authorization_boundary_only_posture: Mapping[str, Any] | str,
    one_future_authorization_review_posture: Mapping[str, Any] | str,
    reviewed_command_execution_review_basis_posture: Mapping[str, Any] | str,
    consumed_token_closed_posture: Mapping[str, Any] | str,
    no_reopen_consumed_request_posture: Mapping[str, Any] | str,
    no_command_invocation_authorization_posture: Mapping[str, Any] | str,
    no_command_invocation_posture: Mapping[str, Any] | str,
    no_command_execution_posture: Mapping[str, Any] | str,
    no_output_result_success_posture: Mapping[str, Any] | str,
    no_execution_permission_posture: Mapping[str, Any] | str,
    no_execution_approval_posture: Mapping[str, Any] | str,
    no_standing_lane_posture: Mapping[str, Any] | str,
    no_repeat_permission_posture: Mapping[str, Any] | str,
    returned_result_containment_posture: Mapping[str, Any] | str,
    command_invocation_authorization_boundary_scope: Sequence[str] | Mapping[str, Any],
    command_invocation_authorization_boundary_intent: str = INTENT_RECORD,
    *,
    selected_command_execution_review_result_path: str | None = None,
    selected_command_execution_review_result_id: str | None = None,
    selected_command_execution_review_result_outcome: str | None = None,
    selected_command_execution_review_failed_check_count: int | None = None,
    selected_execution_review_boundary_result_path: str | None = None,
    selected_execution_review_boundary_result_id: str | None = None,
    selected_execution_review_boundary_result_outcome: str | None = None,
    selected_execution_review_boundary_failed_check_count: int | None = None,
    selected_request_consumption_result_path: str | None = None,
    selected_request_consumption_result_id: str | None = None,
    selected_request_consumption_result_outcome: str | None = None,
    selected_request_consumption_failed_check_count: int | None = None,
    selected_v2_admitted_request_artifact_path: str | None = None,
    selected_v2_admitted_request_artifact_id: str | None = None,
    selected_v2_admitted_request_outcome: str | None = None,
    selected_v2_admitted_request_version: str | None = None,
    selected_v2_failed_check_count: int | None = None,
    requested_command_invocation_authorization_boundary_outcome: str = OUTCOME_RECORDED,
    additional_basis_context: Mapping[str, Any] | None = None,
    not_recorded_basis: Mapping[str, Any] | str | None = None,
) -> dict:
    """Build a declared command invocation authorization boundary request with false non-claims."""

    request: dict[str, Any] = {
        "command_invocation_authorization_boundary_request_id": command_invocation_authorization_boundary_request_id,
        "command_invocation_authorization_boundary_question": command_invocation_authorization_boundary_question,
        "command_invocation_authorization_boundary_intent": command_invocation_authorization_boundary_intent,
        "selected_command_execution_review_basis": _copy(selected_command_execution_review_basis),
        "selected_command_execution_review_terminal_summary_basis": _copy(selected_command_execution_review_terminal_summary_basis),
        "selected_execution_review_boundary_basis": _copy(selected_execution_review_boundary_basis),
        "selected_request_consumption_basis": _copy(selected_request_consumption_basis),
        "selected_consumed_request_basis": _copy(selected_consumed_request_basis),
        "selected_v2_admitted_request_basis": _copy(selected_v2_admitted_request_basis),
        "selected_v1_predecessor_failure_basis": _copy(selected_v1_predecessor_failure_basis),
        "selected_command_execution_boundary_basis": _copy(selected_command_execution_boundary_basis),
        "selected_command_report_basis": _copy(selected_command_report_basis),
        "selected_command_implementation_boundary_basis": _copy(selected_command_implementation_boundary_basis),
        "selected_command_boundary_basis": _copy(selected_command_boundary_basis),
        "selected_artifact_emission_containment_basis": _copy(selected_artifact_emission_containment_basis),
        "selected_evidence_manifest_basis": _copy(selected_evidence_manifest_basis),
        "selected_portable_verification_basis": _copy(selected_portable_verification_basis),
        "authorization_boundary_only_posture": _copy(authorization_boundary_only_posture),
        "one_future_authorization_review_posture": _copy(one_future_authorization_review_posture),
        "reviewed_command_execution_review_basis_posture": _copy(reviewed_command_execution_review_basis_posture),
        "consumed_token_closed_posture": _copy(consumed_token_closed_posture),
        "no_reopen_consumed_request_posture": _copy(no_reopen_consumed_request_posture),
        "no_command_invocation_authorization_posture": _copy(no_command_invocation_authorization_posture),
        "no_command_invocation_posture": _copy(no_command_invocation_posture),
        "no_command_execution_posture": _copy(no_command_execution_posture),
        "no_output_result_success_posture": _copy(no_output_result_success_posture),
        "no_execution_permission_posture": _copy(no_execution_permission_posture),
        "no_execution_approval_posture": _copy(no_execution_approval_posture),
        "no_standing_lane_posture": _copy(no_standing_lane_posture),
        "no_repeat_permission_posture": _copy(no_repeat_permission_posture),
        "returned_result_containment_posture": _copy(returned_result_containment_posture),
        "command_invocation_authorization_boundary_scope": _copy(command_invocation_authorization_boundary_scope),
        "requested_command_invocation_authorization_boundary_outcome": requested_command_invocation_authorization_boundary_outcome,
        "declared_non_claims": _false_non_claims(),
    }
    optional_values = {
        "selected_command_execution_review_result_path": selected_command_execution_review_result_path,
        "selected_command_execution_review_result_id": selected_command_execution_review_result_id,
        "selected_command_execution_review_result_outcome": selected_command_execution_review_result_outcome,
        "selected_command_execution_review_failed_check_count": selected_command_execution_review_failed_check_count,
        "selected_execution_review_boundary_result_path": selected_execution_review_boundary_result_path,
        "selected_execution_review_boundary_result_id": selected_execution_review_boundary_result_id,
        "selected_execution_review_boundary_result_outcome": selected_execution_review_boundary_result_outcome,
        "selected_execution_review_boundary_failed_check_count": selected_execution_review_boundary_failed_check_count,
        "selected_request_consumption_result_path": selected_request_consumption_result_path,
        "selected_request_consumption_result_id": selected_request_consumption_result_id,
        "selected_request_consumption_result_outcome": selected_request_consumption_result_outcome,
        "selected_request_consumption_failed_check_count": selected_request_consumption_failed_check_count,
        "selected_v2_admitted_request_artifact_path": selected_v2_admitted_request_artifact_path,
        "selected_v2_admitted_request_artifact_id": selected_v2_admitted_request_artifact_id,
        "selected_v2_admitted_request_outcome": selected_v2_admitted_request_outcome,
        "selected_v2_admitted_request_version": selected_v2_admitted_request_version,
        "selected_v2_failed_check_count": selected_v2_failed_check_count,
        "additional_basis_context": additional_basis_context,
        "not_recorded_basis": not_recorded_basis,
    }
    for key, value in optional_values.items():
        if value is not None:
            request[key] = _copy(value)
    return request
