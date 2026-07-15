"""Bounded consumed-request command execution review resolver.

This module records one command execution review result over consumed request
basis and execution-review-boundary basis. Command execution review is not
command invocation, command execution, command output, command result, command
success, execution permission, execution approval, or command invocation
authorization. The consumed request token remains closed, no standing
invocation lane or repeat permission is created, and any actual invocation or
execution still requires a separate bounded step.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class PortableSourceBodyVerificationConsumedSingleLiveCommandInvocationRequestCommandExecutionReviewError(
    Exception
):
    """Raised only for impossible bounded resolver write-state failures."""


RESOLVER_MODULE = (
    "resolve_portable_source_body_verification_consumed_single_live_command_"
    "invocation_request_command_execution_review"
)
RESULT_VERSION = "0.1.0"

PORTABLE_SOURCE_BODY_VERIFICATION_CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_EXECUTION_REVIEW_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_"
    "consumed_single_live_command_invocation_request_command_execution_review"
)
OUTPUT_ROOT = (
    PORTABLE_SOURCE_BODY_VERIFICATION_CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_EXECUTION_REVIEW_ROOT
)

CORE_COMMAND_EXECUTION_REVIEW_QUESTION = (
    "Can the consumed single live command invocation request basis and recorded "
    "execution-review boundary be reviewed as one command execution review "
    "result without invoking or executing the command and without creating "
    "command output, command result, command success, execution permission, "
    "execution approval, command invocation authorization, standing invocation "
    "lane, repeat permission, authority, currentness, final completion, "
    "continuation, reusable permission, derivative reception, vessel relation, "
    "another reception request, or follow-on work?"
)

OUTCOME_RECORDED = (
    "CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_EXECUTION_REVIEW_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_EXECUTION_REVIEW_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_EXECUTION_REVIEW_"
    "REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_EXECUTION_REVIEW_BLOCKED"
)
OUTCOME_FAMILY = {
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
}

INTENT_RECORD = (
    "RECORD_CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_EXECUTION_REVIEW"
)
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_EXECUTION_REVIEW"
)
INTENT_BLOCK = (
    "BLOCK_CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_EXECUTION_REVIEW"
)
SUPPORTED_COMMAND_EXECUTION_REVIEW_INTENTS = {
    INTENT_RECORD,
    INTENT_DO_NOT_RECORD,
    INTENT_BLOCK,
}

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

SUPPORTED_COMMAND_EXECUTION_REVIEW_SCOPE = {
    "COMMAND_EXECUTION_REVIEW_ONLY",
    "REVIEWED_CONSUMED_REQUEST_BASIS_PRESERVED",
    "REVIEWED_EXECUTION_REVIEW_BOUNDARY_BASIS_PRESERVED",
    "CONSUMED_REQUEST_TOKEN_REMAINS_CLOSED",
    "CONSUMED_REQUEST_NOT_REOPENED",
    "COMMAND_INVOCATION_NOT_CREATED",
    "COMMAND_EXECUTION_NOT_PERFORMED",
    "COMMAND_OUTPUT_NOT_CREATED",
    "COMMAND_RESULT_NOT_CREATED",
    "COMMAND_SUCCESS_NOT_CREATED",
    "EXECUTION_PERMISSION_NOT_CREATED",
    "EXECUTION_APPROVAL_NOT_CREATED",
    "COMMAND_INVOCATION_AUTHORIZATION_NOT_CREATED",
    "NO_STANDING_INVOCATION_LANE_CREATED",
    "NO_REPEAT_INVOCATION_PERMISSION_CREATED",
    "COMMAND_EXECUTION_REVIEW_IS_NOT_EXECUTION",
    "REVIEWED_BASIS_IS_NOT_EXECUTION_PERMISSION",
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
    "command_invocation_created",
    "command_executed",
    "command_execution_performed",
    "command_output_created",
    "command_result_created",
    "command_success_created",
    "execution_permission_created",
    "execution_approval_created",
    "command_invocation_authorization_created",
    "standing_invocation_lane_created",
    "repeat_invocation_permission_created",
    "command_execution_review_treated_as_execution",
    "reviewed_basis_treated_as_execution_permission",
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
    "command_execution_review_recorded",
    "reviewed_consumed_request_basis_preserved",
    "reviewed_execution_review_boundary_basis_preserved",
    "consumed_request_token_remains_closed",
    "reviewed_basis_posture_declared",
    "execution_review_only",
    "execution_still_not_authorized",
    "execution_requires_separate_invocation_step",
    "v1_predecessor_failure_preserved",
    "returned_result_containment_preserved",
)

FORBIDDEN_FULL_BODY_KEYS = {
    "full_artifact_body",
    "raw_full_artifact_body",
    "artifact_body",
    "full_result",
    "raw_result",
    "raw_full_result",
    "full_prior_artifact_body",
    "raw_full_prior_artifact_body",
    "prior_artifact_body",
    "full_prior_artifacts",
}
FULL_BODY_OMISSION_MARKER = (
    "[omitted: full prior artifact body is outside command execution review scope]"
)

MUTATION_FLAGS = ("mutation_performed", "replay_performed", "merge_performed")

REQUIRED_BASIS_FIELDS = (
    (
        "execution-review boundary terminal summary basis declared",
        "selected_execution_review_boundary_terminal_summary_basis",
        "EXECUTION_REVIEW_BOUNDARY_TERMINAL_SUMMARY_MISSING",
    ),
    (
        "execution-review boundary live artifact basis declared",
        "selected_execution_review_boundary_basis",
        "EXECUTION_REVIEW_BOUNDARY_BASIS_MISSING",
    ),
    (
        "request-consumption live artifact basis declared",
        "selected_request_consumption_basis",
        "REQUEST_CONSUMPTION_BASIS_MISSING",
    ),
    (
        "request-consumption terminal summary basis declared",
        "selected_request_consumption_terminal_summary_basis",
        "REQUEST_CONSUMPTION_TERMINAL_SUMMARY_MISSING",
    ),
    (
        "consumed request basis declared",
        "selected_consumed_request_basis",
        "CONSUMED_REQUEST_BASIS_MISSING",
    ),
    (
        "selected v2 admitted request basis declared",
        "selected_v2_admitted_request_basis",
        "V2_ADMITTED_REQUEST_BASIS_MISSING",
    ),
    (
        "selected v1 predecessor/failure basis declared",
        "selected_v1_predecessor_failure_basis",
        "V1_PREDECESSOR_FAILURE_BASIS_MISSING",
    ),
    (
        "command execution boundary basis declared",
        "selected_command_execution_boundary_basis",
        "COMMAND_EXECUTION_BOUNDARY_BASIS_MISSING",
    ),
    (
        "command report basis declared",
        "selected_command_report_basis",
        "COMMAND_REPORT_BASIS_MISSING",
    ),
    (
        "command implementation boundary basis declared",
        "selected_command_implementation_boundary_basis",
        "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING",
    ),
    (
        "command boundary basis declared",
        "selected_command_boundary_basis",
        "COMMAND_BOUNDARY_BASIS_MISSING",
    ),
    (
        "artifact emission containment basis declared",
        "selected_artifact_emission_containment_basis",
        "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING",
    ),
    (
        "evidence-manifest basis declared",
        "selected_evidence_manifest_basis",
        "EVIDENCE_MANIFEST_BASIS_MISSING",
    ),
    (
        "portable verification basis declared",
        "selected_portable_verification_basis",
        "PORTABLE_VERIFICATION_BASIS_MISSING",
    ),
)

REQUIRED_POSTURE_FIELDS = (
    (
        "reviewed-basis posture declared",
        "reviewed_basis_posture",
        "REVIEWED_BASIS_POSTURE_MISSING",
    ),
    (
        "consumed-token-closed posture declared",
        "consumed_token_closed_posture",
        "CONSUMED_TOKEN_NOT_CLOSED",
    ),
    (
        "no-reopen-consumed-request posture declared",
        "no_reopen_consumed_request_posture",
        "CONSUMED_REQUEST_REOPENED",
    ),
    ("review-only posture declared", "review_only_posture", "REVIEW_ONLY_POSTURE_MISSING"),
    (
        "no-command-invocation posture declared",
        "no_command_invocation_posture",
        "COMMAND_INVOCATION_CREATED",
    ),
    (
        "no-command-execution posture declared",
        "no_command_execution_posture",
        "COMMAND_EXECUTION_PERFORMED",
    ),
    (
        "no-output/result/success posture declared",
        "no_output_result_success_posture",
        "COMMAND_OUTPUT_CREATED",
    ),
    (
        "no-execution-permission posture declared",
        "no_execution_permission_posture",
        "NO_EXECUTION_PERMISSION_POSTURE_MISSING",
    ),
    (
        "no-execution-approval posture declared",
        "no_execution_approval_posture",
        "NO_EXECUTION_APPROVAL_POSTURE_MISSING",
    ),
    (
        "no-command-invocation-authorization posture declared",
        "no_command_invocation_authorization_posture",
        "NO_COMMAND_INVOCATION_AUTHORIZATION_POSTURE_MISSING",
    ),
    (
        "no-standing-lane posture declared",
        "no_standing_lane_posture",
        "NO_STANDING_LANE_POSTURE_MISSING",
    ),
    (
        "no-repeat-permission posture declared",
        "no_repeat_permission_posture",
        "NO_REPEAT_PERMISSION_POSTURE_MISSING",
    ),
    (
        "returned-result containment posture declared",
        "returned_result_containment_posture",
        "V2_RETURNED_RESULT_CONTAINMENT_MISSING",
    ),
)

COLLAPSE_FIELD_CODES = (
    ("consumed_request_reopened", "CONSUMED_REQUEST_REOPENED"),
    ("consumed_token_reopened", "CONSUMED_REQUEST_REOPENED"),
    ("command_invocation_created", "COMMAND_INVOCATION_CREATED"),
    ("command_invocation_exists", "COMMAND_INVOCATION_CREATED"),
    ("command_executed", "COMMAND_EXECUTION_PERFORMED"),
    ("command_execution_performed", "COMMAND_EXECUTION_PERFORMED"),
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
    ("command_invocation_authorization_created", "COMMAND_INVOCATION_AUTHORIZATION_CREATED"),
    ("command_invocation_authorization_exists", "COMMAND_INVOCATION_AUTHORIZATION_CREATED"),
    ("standing_invocation_lane_created", "STANDING_INVOCATION_LANE_CREATED"),
    ("standing_invocation_lane_exists", "STANDING_INVOCATION_LANE_CREATED"),
    ("repeat_invocation_permission_created", "REPEAT_INVOCATION_PERMISSION_CREATED"),
    ("repeat_invocation_permission_exists", "REPEAT_INVOCATION_PERMISSION_CREATED"),
    ("command_execution_review_treated_as_execution", "COMMAND_EXECUTION_REVIEW_TREATED_AS_EXECUTION"),
    (
        "reviewed_basis_treated_as_execution_permission",
        "REVIEWED_BASIS_TREATED_AS_EXECUTION_PERMISSION",
    ),
    ("reviewed_basis_treated_as_command_success", "REVIEWED_BASIS_TREATED_AS_COMMAND_SUCCESS"),
    ("command_output_became_source", "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
    ("command_output_treated_as_source", "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
    ("command_result_became_authority", "COMMAND_RESULT_TREATED_AS_AUTHORITY"),
    ("command_result_treated_as_authority", "COMMAND_RESULT_TREATED_AS_AUTHORITY"),
    ("command_success_created_currentness", "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
    ("command_success_treated_as_currentness", "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
    (
        "command_success_claimed_final_completion",
        "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION",
    ),
    (
        "command_success_treated_as_final_completion",
        "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION",
    ),
    ("raw_full_prior_artifact_body_returned", "FULL_PRIOR_ARTIFACT_BODY_EMITTED"),
    ("full_prior_artifacts_embedded", "FULL_PRIOR_ARTIFACT_BODY_EMITTED"),
    ("prior_artifacts_mutated", "ARTIFACTS_MUTATED"),
    ("artifacts_mutated", "ARTIFACTS_MUTATED"),
    ("v2_treated_as_repairing_v1", "V2_TREATED_AS_REPAIRING_V1"),
    ("v2_successor_repairs_v1", "V2_TREATED_AS_REPAIRING_V1"),
    ("v1_repaired", "V2_TREATED_AS_REPAIRING_V1"),
    ("v1_hidden", "V1_FAILURE_HIDDEN"),
    ("v1_claimed_passed", "V1_CLAIMED_PASSED"),
    ("v1_passed", "V1_CLAIMED_PASSED"),
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

BLOCK_REASONS = {
    "DECLARED_COMMAND_EXECUTION_REVIEW_REQUEST_MALFORMED": (
        "Declared command execution review request is malformed."
    ),
    "DECLARED_COMMAND_EXECUTION_REVIEW_REQUEST_UNREADABLE": (
        "Declared command execution review request path is unreadable."
    ),
    "COMMAND_EXECUTION_REVIEW_EXPLICITLY_BLOCKED": (
        "Declared command execution review request explicitly selected blocked posture."
    ),
}


def _copy(value: Any) -> Any:
    return copy.deepcopy(value)


def _as_mapping(value: Any) -> dict[str, Any]:
    return dict(value) if isinstance(value, Mapping) else {}


def _generated_at() -> str:
    return datetime.now(timezone.utc).isoformat()


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
            "true",
            "yes",
            "1",
            "declared",
            "preserved",
            "recorded",
            "closed",
            "supported",
            "reviewed",
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


def _safe_component(value: Any, fallback: str) -> str:
    text = str(value).strip() if value is not None else ""
    if not text:
        text = fallback
    safe = []
    for char in text:
        safe.append(char if char.isalnum() or char in {"-", "_", "."} else "_")
    return "".join(safe).strip("._") or fallback


def _false_non_claims() -> dict[str, bool]:
    return {name: False for name in REQUIRED_FALSE_NON_CLAIMS}


def _sanitize(value: Any) -> Any:
    if isinstance(value, Mapping):
        result: dict[str, Any] = {}
        for key, item in value.items():
            key_text = str(key)
            if key_text.lower() in FORBIDDEN_FULL_BODY_KEYS:
                result[key_text] = FULL_BODY_OMISSION_MARKER
            else:
                result[key_text] = _sanitize(item)
        return result
    if isinstance(value, list):
        return [_sanitize(item) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item) for item in value]
    return _copy(value)


def _contains_forbidden_full_body_key(value: Any) -> bool:
    if isinstance(value, Mapping):
        for key, item in value.items():
            if str(key).lower() in FORBIDDEN_FULL_BODY_KEYS:
                return True
            if _contains_forbidden_full_body_key(item):
                return True
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return any(_contains_forbidden_full_body_key(item) for item in value)
    return False


def _forbidden_full_body_keys(value: Any) -> list[str]:
    found: list[str] = []

    def walk(item: Any) -> None:
        if isinstance(item, Mapping):
            for key, child in item.items():
                key_text = str(key)
                if key_text.lower() in FORBIDDEN_FULL_BODY_KEYS:
                    found.append(key_text)
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
            key_text = str(key)
            if key_text.lower() in names and _truthy(item):
                return key_text
            nested = _first_truthy_key(item, key_names)
            if nested is not None:
                return nested
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        for item in value:
            nested = _first_truthy_key(item, key_names)
            if nested is not None:
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
    names = {key.lower() for key in keys}
    if isinstance(value, Mapping):
        for key, item in value.items():
            if str(key).lower() in names and _truthy(item):
                return True
            if _find_truthy(item, keys):
                return True
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return any(_find_truthy(item, keys) for item in value)
    return False


def _scope_values(value: Any) -> list[str]:
    if isinstance(value, Mapping):
        for key in (
            "selected_scope_values",
            "scope_values",
            "command_execution_review_scope",
        ):
            selected = value.get(key)
            if isinstance(selected, str):
                return [selected]
            if isinstance(selected, Sequence) and not isinstance(
                selected, (str, bytes, bytearray)
            ):
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


def _declared_non_claims_false(request: Mapping[str, Any]) -> bool:
    non_claims = request.get("declared_non_claims")
    if not isinstance(non_claims, Mapping):
        return False
    return all(
        name in non_claims and non_claims[name] is False
        for name in REQUIRED_FALSE_NON_CLAIMS
    )


def _declared_non_claims_actual(request: Mapping[str, Any]) -> dict[str, Any]:
    non_claims = request.get("declared_non_claims")
    if not isinstance(non_claims, Mapping):
        return {
            "declared_non_claims_present": False,
            "missing_non_claims": list(REQUIRED_FALSE_NON_CLAIMS),
            "flipped_non_claims": [],
        }
    missing = [name for name in REQUIRED_FALSE_NON_CLAIMS if name not in non_claims]
    flipped = [
        name
        for name in REQUIRED_FALSE_NON_CLAIMS
        if name in non_claims and non_claims[name] is not False
    ]
    return {
        "declared_non_claims_present": True,
        "missing_non_claims": missing,
        "flipped_non_claims": flipped,
        "declared_non_claims": _sanitize(non_claims),
    }


def _selected_basis_value(value: Any) -> Any:
    if isinstance(value, Mapping):
        return _sanitize(value)
    if isinstance(value, (str, Path)):
        return {
            "selected_basis_reference": str(value),
            "selected_basis_is_path_reference": True,
        }
    return _sanitize(value)


def _basis_section(value: Any, label: str) -> dict[str, Any]:
    declared = _present(value)
    forbidden = _contains_forbidden_full_body_key(value)
    return {
        f"{label}_declared": declared,
        "selected_basis": _selected_basis_value(value) if declared else {},
        "selected_basis_is_reference_shaped": declared and not forbidden,
        "selected_basis_remains_basis_only": True,
        "selected_basis_does_not_invoke_command": True,
        "selected_basis_does_not_execute_command": True,
        "selected_basis_does_not_create_command_output": True,
        "selected_basis_does_not_create_command_result": True,
        "selected_basis_does_not_create_command_success": True,
        "selected_basis_does_not_create_execution_permission": True,
        "selected_basis_does_not_create_execution_approval": True,
        "selected_basis_does_not_create_command_invocation_authorization": True,
        "selected_basis_does_not_create_standing_lane": True,
        "selected_basis_does_not_create_repeat_permission": True,
        "selected_basis_does_not_reopen_consumed_request": True,
        "selected_basis_does_not_create_authority_currentness_final_completion": True,
        "selected_basis_does_not_authorize_continuation_or_follow_on_work": True,
        "full_prior_artifact_body_not_emitted": not forbidden,
        "prior_artifacts_not_mutated": True,
    }


def _execution_review_boundary_basis(request: Mapping[str, Any]) -> Any:
    return request.get("selected_execution_review_boundary_basis")


def _execution_review_boundary_outcome(request: Mapping[str, Any]) -> Any:
    basis = _execution_review_boundary_basis(request)
    return (
        request.get("selected_execution_review_boundary_result_outcome")
        or _find_first(
            basis,
            (
                "selected_execution_review_boundary_result_outcome",
                "selected_result_outcome",
                "outcome",
            ),
        )
    )


def _execution_review_boundary_failed_check_count(
    request: Mapping[str, Any]
) -> int | None:
    basis = _execution_review_boundary_basis(request)
    for value in (
        request.get("selected_execution_review_boundary_failed_check_count"),
        _find_first(
            basis,
            (
                "selected_execution_review_boundary_failed_check_count",
                "selected_result_failed_check_count",
                "failed_check_count",
            ),
        ),
    ):
        count = _to_int(value)
        if count is not None:
            return count
    return None


def _request_consumption_basis(request: Mapping[str, Any]) -> Any:
    return request.get("selected_request_consumption_basis")


def _request_consumption_outcome(request: Mapping[str, Any]) -> Any:
    basis = _request_consumption_basis(request)
    return (
        request.get("selected_request_consumption_result_outcome")
        or _find_first(
            basis,
            (
                "selected_request_consumption_result_outcome",
                "selected_result_outcome",
                "outcome",
            ),
        )
    )


def _request_consumption_failed_check_count(request: Mapping[str, Any]) -> int | None:
    basis = _request_consumption_basis(request)
    for value in (
        request.get("selected_request_consumption_failed_check_count"),
        _find_first(
            basis,
            (
                "selected_request_consumption_failed_check_count",
                "selected_result_failed_check_count",
                "failed_check_count",
            ),
        ),
    ):
        count = _to_int(value)
        if count is not None:
            return count
    return None


def _consumed_request_basis(request: Mapping[str, Any]) -> Any:
    return request.get("selected_consumed_request_basis")


def _consumed_token_closed(request: Mapping[str, Any]) -> bool:
    keys = (
        "consumption_token_closed",
        "consumed_request_token_remains_closed",
        "consumed_token_closed",
        "request_consumed",
        "admitted_single_live_command_invocation_request_consumed",
    )
    return (
        _find_truthy(_consumed_request_basis(request), keys)
        or _find_truthy(_request_consumption_basis(request), keys)
        or _find_truthy(request.get("consumed_token_closed_posture"), keys)
    )


def _consumed_request_reopened(request: Mapping[str, Any]) -> bool:
    return _contains_truthy_key(request, "consumed_request_reopened") or _contains_truthy_key(
        request, "consumed_token_reopened"
    )


def _v2_basis(request: Mapping[str, Any]) -> Any:
    return request.get("selected_v2_admitted_request_basis")


def _v2_outcome(request: Mapping[str, Any]) -> Any:
    basis = _v2_basis(request)
    return (
        request.get("selected_v2_admitted_request_outcome")
        or _find_first(
            basis,
            (
                "selected_v2_admitted_request_outcome",
                "selected_result_outcome",
                "outcome",
            ),
        )
    )


def _v2_version(request: Mapping[str, Any]) -> Any:
    basis = _v2_basis(request)
    return (
        request.get("selected_v2_admitted_request_version")
        or _find_first(
            basis,
            (
                "selected_v2_admitted_request_version",
                "single_live_command_invocation_request_admission_result_version",
                "selected_result_version",
                "result_version",
                "version",
            ),
        )
    )


def _v2_failed_check_count(request: Mapping[str, Any]) -> int | None:
    basis = _v2_basis(request)
    for value in (
        request.get("selected_v2_failed_check_count"),
        _find_first(
            basis,
            (
                "selected_v2_failed_check_count",
                "selected_result_failed_check_count",
                "failed_check_count",
            ),
        ),
    ):
        count = _to_int(value)
        if count is not None:
            return count
    return None


def _v2_successor_metadata(request: Mapping[str, Any]) -> dict[str, Any]:
    explicit = request.get("selected_v2_successor_metadata")
    basis = _v2_basis(request)
    metadata = _sanitize(explicit) if isinstance(explicit, Mapping) else {}
    successor_of = metadata.get("successor_of") or _find_first(basis, ("successor_of",))
    successor_reason = metadata.get("successor_reason") or _find_first(
        basis, ("successor_reason",)
    )
    resolver_module = metadata.get("resolver_module") or _find_first(
        basis, ("resolver_module",)
    )
    if successor_of is not None:
        metadata["successor_of"] = _sanitize(successor_of)
    if successor_reason is not None:
        metadata["successor_reason"] = _sanitize(successor_reason)
    if resolver_module is not None:
        metadata["resolver_module"] = _sanitize(resolver_module)
    return metadata


def _v2_successor_metadata_preserved(request: Mapping[str, Any]) -> bool:
    metadata = _v2_successor_metadata(request)
    return (
        metadata.get("successor_of") == V1_PREDECESSOR_RESOLVER_MODULE
        and _present(metadata.get("successor_reason"))
        and metadata.get("resolver_module") in {None, V2_RESOLVER_MODULE}
    )


def _v2_returned_result_containment_preserved(request: Mapping[str, Any]) -> bool:
    return _find_truthy(
        _v2_basis(request),
        (
            "returned_result_containment_preserved",
            "v2_raw_full_prior_artifact_values_omitted",
            "raw_full_prior_artifact_values_omitted",
            "full_prior_artifact_body_not_returned",
        ),
    )


def _returned_result_containment_posture_preserved(request: Mapping[str, Any]) -> bool:
    return _find_truthy(
        request.get("returned_result_containment_posture"),
        (
            "returned_result_containment_preserved",
            "full_prior_artifact_body_not_returned",
            "raw_full_prior_artifact_body_returned_false",
        ),
    )


def _selected_execution_review_boundary_section(
    request: Mapping[str, Any]
) -> dict[str, Any]:
    basis = request.get("selected_execution_review_boundary_basis")
    section = _basis_section(basis, "selected_execution_review_boundary_basis")
    outcome = _execution_review_boundary_outcome(request)
    failed_count = _execution_review_boundary_failed_check_count(request)
    section.update(
        {
            "selected_execution_review_boundary_result_path": _sanitize(
                request.get("selected_execution_review_boundary_result_path")
                or _find_first(
                    basis,
                    (
                        "selected_execution_review_boundary_result_path",
                        "selected_result_path",
                        "result_path",
                        "path",
                    ),
                )
            ),
            "selected_execution_review_boundary_result_id": _sanitize(
                request.get("selected_execution_review_boundary_result_id")
                or _find_first(
                    basis,
                    (
                        "selected_execution_review_boundary_result_id",
                        "selected_result_id",
                        "result_id",
                    ),
                )
            ),
            "selected_execution_review_boundary_result_outcome": _sanitize(outcome),
            "selected_execution_review_boundary_failed_check_count": failed_count,
            "selected_execution_review_boundary_outcome_recorded": (
                outcome == EXECUTION_REVIEW_BOUNDARY_OUTCOME
            ),
            "selected_execution_review_boundary_failed_check_count_zero": (
                failed_count == 0
            ),
            "execution_review_boundary_basis_remains_boundary_basis_only": True,
            "execution_review_boundary_did_not_perform_command_execution_review": True,
            "execution_review_boundary_did_not_authorize_invocation_execution_output_result_success": True,
            "execution_review_boundary_did_not_create_execution_permission_or_approval": True,
            "execution_review_boundary_did_not_create_command_invocation_authorization": True,
            "execution_review_boundary_did_not_create_standing_lane_repeat_permission_final_completion_continuation_reusable_permission_follow_on_work": True,
        }
    )
    return section


def _selected_execution_review_boundary_terminal_summary_section(
    request: Mapping[str, Any]
) -> dict[str, Any]:
    basis = request.get("selected_execution_review_boundary_terminal_summary_basis")
    section = _basis_section(
        basis,
        "selected_execution_review_boundary_terminal_summary_basis",
    )
    path = request.get("selected_execution_review_boundary_terminal_summary_path") or _find_first(
        basis,
        (
            "selected_execution_review_boundary_terminal_summary_path",
            "terminal_summary_path",
            "selected_terminal_summary_path",
            "path",
        ),
    )
    section.update(
        {
            "selected_execution_review_boundary_terminal_summary_path": _sanitize(path),
            "terminal_summary_remains_readability_basis_only": True,
            "terminal_summary_does_not_perform_command_execution_review": True,
            "terminal_summary_does_not_authorize_command_invocation": True,
            "terminal_summary_does_not_authorize_command_execution": True,
            "terminal_summary_does_not_create_command_output_result_success": True,
            "terminal_summary_does_not_create_execution_permission_approval_or_invocation_authorization": True,
        }
    )
    return section


def _selected_request_consumption_section(request: Mapping[str, Any]) -> dict[str, Any]:
    basis = request.get("selected_request_consumption_basis")
    section = _basis_section(basis, "selected_request_consumption_basis")
    outcome = _request_consumption_outcome(request)
    failed_count = _request_consumption_failed_check_count(request)
    section.update(
        {
            "selected_request_consumption_result_id": _sanitize(
                request.get("selected_request_consumption_result_id")
                or _find_first(
                    basis,
                    (
                        "selected_request_consumption_result_id",
                        "selected_result_id",
                        "result_id",
                    ),
                )
            ),
            "selected_request_consumption_result_path": _sanitize(
                request.get("selected_request_consumption_result_path")
                or _find_first(
                    basis,
                    (
                        "selected_request_consumption_result_path",
                        "selected_result_path",
                        "result_path",
                        "path",
                    ),
                )
            ),
            "selected_request_consumption_result_outcome": _sanitize(outcome),
            "selected_request_consumption_failed_check_count": failed_count,
            "selected_request_consumption_outcome_consumed": (
                outcome == REQUEST_CONSUMPTION_OUTCOME
            ),
            "selected_request_consumption_failed_check_count_zero": failed_count == 0,
            "request_consumed_exactly_once": _find_truthy(
                basis,
                (
                    "request_consumed_exactly_once",
                    "request_consumed",
                    "admitted_single_live_command_invocation_request_consumed",
                ),
            ),
            "consumption_token_closed": _find_truthy(
                basis,
                ("consumption_token_closed", "consumed_token_closed"),
            ),
            "consumed_request_basis_recorded": _find_truthy(
                basis,
                ("consumed_request_basis_recorded", "request_consumed"),
            ),
            "request_consumption_basis_does_not_authorize_invocation_execution_output_result_success": True,
            "request_consumption_basis_does_not_create_execution_permission_approval_or_invocation_authorization": True,
            "request_consumption_basis_does_not_create_standing_lane_or_repeat_permission": True,
            "request_consumption_basis_does_not_create_final_completion_continuation_reusable_permission_follow_on_work": True,
        }
    )
    return section


def _selected_request_consumption_terminal_summary_section(
    request: Mapping[str, Any]
) -> dict[str, Any]:
    basis = request.get("selected_request_consumption_terminal_summary_basis")
    section = _basis_section(basis, "selected_request_consumption_terminal_summary_basis")
    path = request.get("selected_request_consumption_terminal_summary_path") or _find_first(
        basis,
        (
            "selected_request_consumption_terminal_summary_path",
            "terminal_summary_path",
            "selected_terminal_summary_path",
            "path",
        ),
    )
    section.update(
        {
            "selected_request_consumption_terminal_summary_path": _sanitize(path),
            "terminal_summary_remains_readability_basis_only": True,
            "terminal_summary_does_not_authorize_command_invocation": True,
            "terminal_summary_does_not_authorize_command_execution": True,
            "terminal_summary_does_not_create_command_output_result_success": True,
            "terminal_summary_does_not_create_execution_permission_approval_or_invocation_authorization": True,
        }
    )
    return section


def _selected_consumed_request_section(request: Mapping[str, Any]) -> dict[str, Any]:
    basis = _consumed_request_basis(request)
    section = _basis_section(basis, "selected_consumed_request_basis")
    closed = _consumed_token_closed(request)
    reopened = _consumed_request_reopened(request)
    section.update(
        {
            "consumed_request_basis_recorded": _find_truthy(
                basis,
                (
                    "consumed_request_basis_recorded",
                    "request_consumed",
                    "admitted_single_live_command_invocation_request_consumed",
                ),
            )
            or _present(basis),
            "consumed_request_token_closed": closed,
            "consumed_request_token_remains_closed": closed and not reopened,
            "consumed_request_not_reopened": not reopened,
            "consumed_request_basis_is_not_execution_permission": True,
            "consumed_request_basis_is_not_command_success": True,
            "consumed_request_basis_for_one_command_execution_review_only": True,
        }
    )
    return section


def _selected_v2_basis_section(request: Mapping[str, Any]) -> dict[str, Any]:
    basis = _v2_basis(request)
    section = _basis_section(basis, "selected_v2_admitted_request_basis")
    outcome = _v2_outcome(request)
    version = _v2_version(request)
    failed_count = _v2_failed_check_count(request)
    section.update(
        {
            "selected_v2_admitted_request_artifact_path": _sanitize(
                request.get("selected_v2_admitted_request_artifact_path")
                or _find_first(
                    basis,
                    (
                        "selected_v2_admitted_request_artifact_path",
                        "selected_result_path",
                        "result_path",
                    ),
                )
            ),
            "selected_v2_admitted_request_artifact_id": _sanitize(
                request.get("selected_v2_admitted_request_artifact_id")
                or _find_first(
                    basis,
                    (
                        "selected_v2_admitted_request_artifact_id",
                        "selected_result_id",
                        "result_id",
                    ),
                )
            ),
            "selected_v2_admitted_request_outcome": _sanitize(outcome),
            "selected_v2_admitted_request_version": _sanitize(version),
            "selected_v2_failed_check_count": failed_count,
            "selected_v2_outcome_admitted": outcome == V2_ADMITTED_REQUEST_OUTCOME,
            "selected_v2_version_0_2_0": version == V2_ADMITTED_REQUEST_VERSION,
            "selected_v2_failed_check_count_zero": failed_count == 0,
            "selected_v2_successor_metadata": _v2_successor_metadata(request),
            "selected_v2_successor_metadata_preserved": _v2_successor_metadata_preserved(
                request
            ),
            "selected_v2_returned_result_containment_preserved": _v2_returned_result_containment_preserved(
                request
            ),
            "v2_remains_lineage_evidence_only": True,
            "v2_does_not_claim_v1_passed": not _contains_truthy_key(
                request, "v1_claimed_passed"
            )
            and not _contains_truthy_key(request, "v1_passed"),
        }
    )
    return section


def _selected_v1_predecessor_section(request: Mapping[str, Any]) -> dict[str, Any]:
    basis = request.get("selected_v1_predecessor_failure_basis")
    section = _basis_section(basis, "selected_v1_predecessor_failure_basis")
    section.update(
        {
            "selected_v1_predecessor_artifact_path": _sanitize(
                request.get("selected_v1_predecessor_artifact_path")
                or _find_first(
                    basis,
                    (
                        "selected_v1_predecessor_artifact_path",
                        "selected_result_path",
                        "result_path",
                    ),
                )
            ),
            "selected_v1_predecessor_artifact_id": _sanitize(
                request.get("selected_v1_predecessor_artifact_id")
                or _find_first(
                    basis,
                    (
                        "selected_v1_predecessor_artifact_id",
                        "selected_result_id",
                        "result_id",
                    ),
                )
            ),
            "selected_v1_predecessor_outcome": _sanitize(
                request.get("selected_v1_predecessor_outcome")
                or _find_first(
                    basis,
                    (
                        "selected_v1_predecessor_outcome",
                        "selected_result_outcome",
                        "outcome",
                    ),
                )
            ),
            "v1_predecessor_failure_remains_visible": _present(basis)
            and not _contains_truthy_key(request, "v1_hidden"),
            "v1_is_not_repaired": not _contains_truthy_key(request, "v1_repaired"),
            "v1_is_not_hidden": not _contains_truthy_key(request, "v1_hidden"),
            "v1_is_not_claimed_passed": not _contains_truthy_key(
                request, "v1_claimed_passed"
            )
            and not _contains_truthy_key(request, "v1_passed"),
            "v2_successor_does_not_erase_v1": not _contains_truthy_key(
                request, "v2_treated_as_repairing_v1"
            ),
            "predecessor_failure_evidence_is_lineage_evidence_only": True,
        }
    )
    return section


def _reference_basis_section(
    request: Mapping[str, Any],
    key: str,
    label: str,
    path_key: str | None = None,
) -> dict[str, Any]:
    basis = request.get(key)
    section = _basis_section(basis, label)
    if path_key is not None:
        section[path_key] = _sanitize(
            request.get(path_key)
            or _find_first(
                basis,
                (
                    path_key,
                    "selected_result_path",
                    "result_path",
                    "path",
                ),
            )
        )
    section.update(
        {
            "reference_basis_only": True,
            "does_not_create_command_invocation": True,
            "does_not_perform_command_execution": True,
            "does_not_create_command_output_result_success": True,
            "does_not_create_execution_permission_approval_or_invocation_authorization": True,
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
        "selected_posture": _selected_basis_value(value) if declared else {},
        "selected_posture_is_reference_shaped": declared and not forbidden,
        "command_execution_review_only": True,
        "command_invocation_not_created": True,
        "command_execution_not_performed": True,
        "command_output_not_created": True,
        "command_result_not_created": True,
        "command_success_not_created": True,
        "execution_permission_not_created": True,
        "execution_approval_not_created": True,
        "command_invocation_authorization_not_created": True,
        "consumed_request_not_reopened": True,
        "no_standing_invocation_lane": True,
        "no_repeat_invocation_permission": True,
        "full_prior_artifact_body_not_emitted": not forbidden,
    }


def _scope_section(value: Any) -> dict[str, Any]:
    values = _scope_values(value)
    unsupported = [item for item in values if item not in SUPPORTED_COMMAND_EXECUTION_REVIEW_SCOPE]
    value_set = set(values)
    return {
        "selected_scope_values": values,
        "unsupported_scope_values": unsupported,
        "all_selected_scope_values_supported": bool(values) and not unsupported,
        "supported_scope_values": sorted(SUPPORTED_COMMAND_EXECUTION_REVIEW_SCOPE),
        "command_execution_review_only": "COMMAND_EXECUTION_REVIEW_ONLY" in value_set,
        "reviewed_consumed_request_basis_preserved": (
            "REVIEWED_CONSUMED_REQUEST_BASIS_PRESERVED" in value_set
        ),
        "reviewed_execution_review_boundary_basis_preserved": (
            "REVIEWED_EXECUTION_REVIEW_BOUNDARY_BASIS_PRESERVED" in value_set
        ),
        "consumed_request_token_remains_closed": (
            "CONSUMED_REQUEST_TOKEN_REMAINS_CLOSED" in value_set
        ),
        "consumed_request_not_reopened": "CONSUMED_REQUEST_NOT_REOPENED" in value_set,
        "command_invocation_not_created": "COMMAND_INVOCATION_NOT_CREATED" in value_set,
        "command_execution_not_performed": "COMMAND_EXECUTION_NOT_PERFORMED" in value_set,
        "command_output_not_created": "COMMAND_OUTPUT_NOT_CREATED" in value_set,
        "command_result_not_created": "COMMAND_RESULT_NOT_CREATED" in value_set,
        "command_success_not_created": "COMMAND_SUCCESS_NOT_CREATED" in value_set,
        "execution_permission_not_created": "EXECUTION_PERMISSION_NOT_CREATED" in value_set,
        "execution_approval_not_created": "EXECUTION_APPROVAL_NOT_CREATED" in value_set,
        "command_invocation_authorization_not_created": (
            "COMMAND_INVOCATION_AUTHORIZATION_NOT_CREATED" in value_set
        ),
        "no_standing_invocation_lane_created": (
            "NO_STANDING_INVOCATION_LANE_CREATED" in value_set
        ),
        "no_repeat_invocation_permission_created": (
            "NO_REPEAT_INVOCATION_PERMISSION_CREATED" in value_set
        ),
        "command_execution_review_is_not_execution": (
            "COMMAND_EXECUTION_REVIEW_IS_NOT_EXECUTION" in value_set
        ),
        "reviewed_basis_is_not_execution_permission": (
            "REVIEWED_BASIS_IS_NOT_EXECUTION_PERMISSION" in value_set
        ),
        "reviewed_basis_is_not_command_success": (
            "REVIEWED_BASIS_IS_NOT_COMMAND_SUCCESS" in value_set
        ),
        "v1_predecessor_failure_remains_visible": (
            "V1_PREDECESSOR_FAILURE_REMAINS_VISIBLE" in value_set
        ),
        "v2_successor_does_not_repair_v1": (
            "V2_SUCCESSOR_DOES_NOT_REPAIR_V1" in value_set
        ),
        "returned_result_containment_preserved": (
            "RETURNED_RESULT_CONTAINMENT_PRESERVED" in value_set
        ),
        "reference_shaped_basis_required": "REFERENCE_SHAPED_BASIS_REQUIRED" in value_set,
        "full_prior_artifact_body_not_emitted": (
            "FULL_PRIOR_ARTIFACT_BODY_NOT_EMITTED" in value_set
        ),
        "no_authority_created": "NO_AUTHORITY_CREATED" in value_set,
        "no_currentness_created": "NO_CURRENTNESS_CREATED" in value_set,
        "no_final_completion": "NO_FINAL_COMPLETION" in value_set,
        "no_continuation_authorized": "NO_CONTINUATION_AUTHORIZED" in value_set,
        "no_reusable_permission": "NO_REUSABLE_PERMISSION" in value_set,
        "no_follow_on_work_authorized": "NO_FOLLOW_ON_WORK_AUTHORIZED" in value_set,
    }


def _check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str,
) -> dict[str, Any]:
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": _sanitize(expected_posture),
        "actual_posture": _sanitize(actual_posture),
        "block_code": None if passed else code,
        "failure_code": None if passed else code,
    }


def _build_checks(
    request: Mapping[str, Any],
    malformed_code: str | None,
) -> list[dict[str, Any]]:
    if malformed_code:
        return [
            _check(
                "declared command execution review request is a mapping",
                False,
                "mapping",
                malformed_code,
                malformed_code,
            )
        ]

    checks: list[dict[str, Any]] = []
    question = request.get("command_execution_review_question")
    checks.append(
        _check(
            "command execution review question declared",
            _present(question),
            "declared command execution review question",
            question,
            "COMMAND_EXECUTION_REVIEW_QUESTION_UNDECLARED",
        )
    )
    intent = request.get("command_execution_review_intent")
    checks.append(
        _check(
            "command execution review intent supported",
            intent in SUPPORTED_COMMAND_EXECUTION_REVIEW_INTENTS,
            sorted(SUPPORTED_COMMAND_EXECUTION_REVIEW_INTENTS),
            intent,
            "COMMAND_EXECUTION_REVIEW_INTENT_UNSUPPORTED",
        )
    )

    for name, key, code in REQUIRED_BASIS_FIELDS:
        checks.append(_check(name, _present(request.get(key)), "declared", request.get(key), code))

    checks.extend(
        [
            _check(
                "execution-review boundary live artifact recorded outcome",
                _execution_review_boundary_outcome(request) == EXECUTION_REVIEW_BOUNDARY_OUTCOME,
                EXECUTION_REVIEW_BOUNDARY_OUTCOME,
                _execution_review_boundary_outcome(request),
                "EXECUTION_REVIEW_BOUNDARY_NOT_RECORDED",
            ),
            _check(
                "execution-review boundary live artifact failed check count zero",
                _execution_review_boundary_failed_check_count(request) == 0,
                0,
                _execution_review_boundary_failed_check_count(request),
                "EXECUTION_REVIEW_BOUNDARY_FAILED_CHECKS_PRESENT",
            ),
            _check(
                "request-consumption live artifact consumed outcome",
                _request_consumption_outcome(request) == REQUEST_CONSUMPTION_OUTCOME,
                REQUEST_CONSUMPTION_OUTCOME,
                _request_consumption_outcome(request),
                "REQUEST_CONSUMPTION_NOT_CONSUMED",
            ),
            _check(
                "request-consumption live artifact failed check count zero",
                _request_consumption_failed_check_count(request) == 0,
                0,
                _request_consumption_failed_check_count(request),
                "REQUEST_CONSUMPTION_FAILED_CHECKS_PRESENT",
            ),
            _check(
                "consumed request token remains closed",
                _consumed_token_closed(request),
                "closed",
                {
                    "consumed_token_closed": _consumed_token_closed(request),
                    "consumed_request_reopened": _consumed_request_reopened(request),
                },
                "CONSUMED_TOKEN_NOT_CLOSED",
            ),
            _check(
                "consumed request not reopened",
                not _consumed_request_reopened(request),
                False,
                _first_truthy_key(request, ("consumed_request_reopened", "consumed_token_reopened")),
                "CONSUMED_REQUEST_REOPENED",
            ),
            _check(
                "v2 admitted request outcome admitted",
                _v2_outcome(request) == V2_ADMITTED_REQUEST_OUTCOME,
                V2_ADMITTED_REQUEST_OUTCOME,
                _v2_outcome(request),
                "V2_ADMITTED_REQUEST_NOT_ADMITTED",
            ),
            _check(
                "v2 admitted request version 0.2.0",
                _v2_version(request) == V2_ADMITTED_REQUEST_VERSION,
                V2_ADMITTED_REQUEST_VERSION,
                _v2_version(request),
                "V2_ADMITTED_REQUEST_VERSION_NOT_0_2_0",
            ),
            _check(
                "v2 admitted request failed check count zero",
                _v2_failed_check_count(request) == 0,
                0,
                _v2_failed_check_count(request),
                "V2_ADMITTED_REQUEST_FAILED_CHECKS_PRESENT",
            ),
            _check(
                "v2 successor metadata preserved",
                _v2_successor_metadata_preserved(request),
                {
                    "successor_of": V1_PREDECESSOR_RESOLVER_MODULE,
                    "successor_reason": "declared",
                },
                _v2_successor_metadata(request),
                "V2_SUCCESSOR_METADATA_MISSING",
            ),
            _check(
                "v2 returned-result containment preserved",
                _v2_returned_result_containment_preserved(request),
                "returned-result containment preserved in selected v2 basis",
                {
                    "selected_v2_returned_result_containment_preserved": _v2_returned_result_containment_preserved(
                        request
                    )
                },
                "V2_RETURNED_RESULT_CONTAINMENT_MISSING",
            ),
        ]
    )

    v1_basis = request.get("selected_v1_predecessor_failure_basis")
    checks.extend(
        [
            _check(
                "v1 predecessor failure remains visible",
                _present(v1_basis) and not _contains_truthy_key(request, "v1_hidden"),
                "visible predecessor failure evidence",
                {
                    "selected_v1_predecessor_failure_basis_declared": _present(v1_basis),
                    "v1_hidden": _contains_truthy_key(request, "v1_hidden"),
                },
                "V1_FAILURE_HIDDEN",
            ),
            _check(
                "v2 does not claim v1 passed",
                not _contains_truthy_key(request, "v1_claimed_passed")
                and not _contains_truthy_key(request, "v1_passed"),
                False,
                {
                    "v1_claimed_passed": _contains_truthy_key(request, "v1_claimed_passed"),
                    "v1_passed": _contains_truthy_key(request, "v1_passed"),
                },
                "V1_CLAIMED_PASSED",
            ),
            _check(
                "v2 does not repair v1",
                not _contains_truthy_key(request, "v2_treated_as_repairing_v1")
                and not _contains_truthy_key(request, "v2_successor_repairs_v1")
                and not _contains_truthy_key(request, "v1_repaired"),
                False,
                {
                    "v2_treated_as_repairing_v1": _contains_truthy_key(
                        request, "v2_treated_as_repairing_v1"
                    ),
                    "v2_successor_repairs_v1": _contains_truthy_key(
                        request, "v2_successor_repairs_v1"
                    ),
                    "v1_repaired": _contains_truthy_key(request, "v1_repaired"),
                },
                "V2_TREATED_AS_REPAIRING_V1",
            ),
        ]
    )

    for name, key, code in REQUIRED_POSTURE_FIELDS:
        checks.append(_check(name, _present(request.get(key)), "declared", request.get(key), code))

    scope = _scope_section(request.get("command_execution_review_scope"))
    checks.append(
        _check(
            "command-execution-review scope supported",
            scope["all_selected_scope_values_supported"],
            sorted(SUPPORTED_COMMAND_EXECUTION_REVIEW_SCOPE),
            scope["selected_scope_values"],
            "UNSUPPORTED_COMMAND_EXECUTION_REVIEW_SCOPE",
        )
    )
    checks.append(
        _check(
            "reference-shaped input posture declared or preserved",
            _present(request.get("reference_shaped_input_posture"))
            or scope["reference_shaped_basis_required"]
            or not _contains_forbidden_full_body_key(request),
            "reference-shaped input posture",
            {
                "reference_shaped_input_posture": request.get("reference_shaped_input_posture"),
                "scope_reference_shaped_basis_required": scope["reference_shaped_basis_required"],
                "forbidden_full_body_keys_detected": _forbidden_full_body_keys(request),
            },
            "FULL_PRIOR_ARTIFACT_BODY_EMITTED",
        )
    )
    checks.extend(
        [
            _check(
                "no-command-invocation posture declared",
                scope["command_invocation_not_created"]
                or not _contains_truthy_key(request, "command_invocation_created"),
                "command invocation not created",
                {
                    "scope_command_invocation_not_created": scope[
                        "command_invocation_not_created"
                    ],
                    "command_invocation_created": _contains_truthy_key(
                        request, "command_invocation_created"
                    ),
                },
                "COMMAND_INVOCATION_CREATED",
            ),
            _check(
                "no-command-execution posture declared",
                scope["command_execution_not_performed"]
                or (
                    not _contains_truthy_key(request, "command_execution_performed")
                    and not _contains_truthy_key(request, "command_executed")
                ),
                "command execution not performed",
                {
                    "scope_command_execution_not_performed": scope[
                        "command_execution_not_performed"
                    ],
                    "command_execution_performed": _contains_truthy_key(
                        request, "command_execution_performed"
                    ),
                    "command_executed": _contains_truthy_key(request, "command_executed"),
                },
                "COMMAND_EXECUTION_PERFORMED",
            ),
            _check(
                "no-output/result/success posture declared",
                (
                    scope["command_output_not_created"]
                    and scope["command_result_not_created"]
                    and scope["command_success_not_created"]
                )
                or not any(
                    _contains_truthy_key(request, key)
                    for key in (
                        "command_output_created",
                        "command_result_created",
                        "command_success_created",
                    )
                ),
                "command output/result/success not created",
                {
                    "scope_command_output_not_created": scope["command_output_not_created"],
                    "scope_command_result_not_created": scope["command_result_not_created"],
                    "scope_command_success_not_created": scope["command_success_not_created"],
                },
                "COMMAND_OUTPUT_CREATED",
            ),
        ]
    )

    for check_name, key_names, code in (
        (
            "command invocation not created",
            ("command_invocation_created", "command_invocation_exists"),
            "COMMAND_INVOCATION_CREATED",
        ),
        (
            "command execution not performed",
            ("command_execution_performed", "command_executed"),
            "COMMAND_EXECUTION_PERFORMED",
        ),
        (
            "command output not created",
            ("command_output_created", "command_output_exists"),
            "COMMAND_OUTPUT_CREATED",
        ),
        (
            "command result not created",
            ("command_result_created", "command_result_exists"),
            "COMMAND_RESULT_CREATED",
        ),
        (
            "command success not created",
            ("command_success_created", "command_success_exists"),
            "COMMAND_SUCCESS_CREATED",
        ),
        (
            "execution permission not created",
            ("execution_permission_created", "execution_permission_exists"),
            "EXECUTION_PERMISSION_CREATED",
        ),
        (
            "execution approval not created",
            ("execution_approval_created", "execution_approval_exists"),
            "EXECUTION_APPROVAL_CREATED",
        ),
        (
            "command invocation authorization not created",
            ("command_invocation_authorization_created", "command_invocation_authorization_exists"),
            "COMMAND_INVOCATION_AUTHORIZATION_CREATED",
        ),
        (
            "standing invocation lane not created",
            ("standing_invocation_lane_created", "standing_invocation_lane_exists"),
            "STANDING_INVOCATION_LANE_CREATED",
        ),
        (
            "repeat invocation permission not created",
            ("repeat_invocation_permission_created", "repeat_invocation_permission_exists"),
            "REPEAT_INVOCATION_PERMISSION_CREATED",
        ),
        (
            "command execution review not execution",
            ("command_execution_review_treated_as_execution",),
            "COMMAND_EXECUTION_REVIEW_TREATED_AS_EXECUTION",
        ),
        (
            "reviewed basis not execution permission",
            ("reviewed_basis_treated_as_execution_permission",),
            "REVIEWED_BASIS_TREATED_AS_EXECUTION_PERMISSION",
        ),
        (
            "reviewed basis not command success",
            ("reviewed_basis_treated_as_command_success",),
            "REVIEWED_BASIS_TREATED_AS_COMMAND_SUCCESS",
        ),
        (
            "command output not source",
            ("command_output_became_source", "command_output_treated_as_source"),
            "COMMAND_OUTPUT_TREATED_AS_SOURCE",
        ),
        (
            "command result not authority",
            ("command_result_became_authority", "command_result_treated_as_authority"),
            "COMMAND_RESULT_TREATED_AS_AUTHORITY",
        ),
        (
            "command success not currentness",
            ("command_success_created_currentness", "command_success_treated_as_currentness"),
            "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS",
        ),
        (
            "command success not final completion",
            (
                "command_success_claimed_final_completion",
                "command_success_treated_as_final_completion",
            ),
            "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION",
        ),
    ):
        checks.append(
            _check(
                check_name,
                not any(_contains_truthy_key(request, key) for key in key_names),
                False,
                _first_truthy_key(request, key_names),
                code,
            )
        )

    forbidden = _contains_forbidden_full_body_key(request)
    checks.append(
        _check(
            "raw full prior artifact body not emitted",
            not forbidden
            and not _contains_truthy_key(request, "raw_full_prior_artifact_body_returned"),
            "no forbidden full prior artifact body keys or posture",
            {
                "forbidden_full_body_keys_detected": _forbidden_full_body_keys(request),
                "raw_full_prior_artifact_body_returned": _contains_truthy_key(
                    request, "raw_full_prior_artifact_body_returned"
                ),
            },
            "FULL_PRIOR_ARTIFACT_BODY_EMITTED",
        )
    )
    checks.append(
        _check(
            "artifacts not mutated",
            not _contains_truthy_key(request, "prior_artifacts_mutated")
            and not _contains_truthy_key(request, "artifacts_mutated"),
            False,
            _first_truthy_key(request, ("prior_artifacts_mutated", "artifacts_mutated")),
            "ARTIFACTS_MUTATED",
        )
    )
    checks.append(
        _check(
            "deployment/runtime/public release not created",
            not any(
                _contains_truthy_key(request, key)
                for key in (
                    "deployment_created",
                    "runtime_hosting_created",
                    "public_release_created",
                )
            ),
            False,
            _first_truthy_key(
                request,
                ("deployment_created", "runtime_hosting_created", "public_release_created"),
            ),
            "DEPLOYMENT_CREATED",
        )
    )
    checks.append(
        _check(
            "operation permission/public readiness/final completion not created",
            not any(
                _contains_truthy_key(request, key)
                for key in (
                    "operation_permission_created",
                    "public_launch_readiness_created",
                    "public_readiness_created",
                    "final_completion_claimed",
                )
            ),
            False,
            _first_truthy_key(
                request,
                (
                    "operation_permission_created",
                    "public_launch_readiness_created",
                    "public_readiness_created",
                    "final_completion_claimed",
                ),
            ),
            "OPERATION_PERMISSION_CREATED",
        )
    )
    checks.append(
        _check(
            "continuation/reusable permission/follow-on work not authorized",
            not any(
                _contains_truthy_key(request, key)
                for key in (
                    "continuation_authorized",
                    "reusable_permission_created",
                    "follow_on_work_authorized",
                )
            ),
            False,
            _first_truthy_key(
                request,
                ("continuation_authorized", "reusable_permission_created", "follow_on_work_authorized"),
            ),
            "CONTINUATION_AUTHORIZED",
        )
    )
    checks.append(
        _check(
            "derivative reception/vessel relation/another reception request not authorized",
            not any(
                _contains_truthy_key(request, key)
                for key in (
                    "derivative_reception_authorized",
                    "vessel_relation_authorized",
                    "another_reception_request_authorized",
                )
            ),
            False,
            _first_truthy_key(
                request,
                (
                    "derivative_reception_authorized",
                    "vessel_relation_authorized",
                    "another_reception_request_authorized",
                ),
            ),
            "DERIVATIVE_RECEPTION_AUTHORIZED",
        )
    )
    checks.append(
        _check(
            "no mutation/replay/merge",
            not any(_contains_truthy_key(request, key) for key in MUTATION_FLAGS),
            False,
            _first_truthy_key(request, MUTATION_FLAGS),
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        )
    )
    checks.append(
        _check(
            "non-claims remain false",
            _declared_non_claims_false(request),
            _false_non_claims(),
            _declared_non_claims_actual(request),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    return checks


def _checks_summary(checks: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    records = [_sanitize(check) for check in checks]
    failed_codes = [
        str(check.get("block_code") or check.get("failure_code"))
        for check in records
        if check.get("passed") is not True
    ]
    return {
        "records": records,
        "passed_check_count": sum(1 for check in records if check.get("passed") is True),
        "failed_check_count": len(failed_codes),
        "failed_check_codes": failed_codes,
    }


def _first_failed_code(checks: Sequence[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is not True:
            return str(check.get("block_code") or check.get("failure_code"))
    return None


def _first_collapse_code(request: Mapping[str, Any]) -> str | None:
    for key, code in COLLAPSE_FIELD_CODES:
        if _contains_truthy_key(request, key):
            return code
    if any(_contains_truthy_key(request, key) for key in MUTATION_FLAGS):
        return "MUTATION_REPLAY_OR_MERGE_DETECTED"
    return None


def _determine_block_code(
    request: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    malformed_code: str | None,
) -> str | None:
    if malformed_code:
        return malformed_code
    if request.get("command_execution_review_intent") == INTENT_BLOCK:
        return "COMMAND_EXECUTION_REVIEW_EXPLICITLY_BLOCKED"
    if request.get("requested_command_execution_review_outcome") == OUTCOME_BLOCKED:
        return "COMMAND_EXECUTION_REVIEW_EXPLICITLY_BLOCKED"
    requested = request.get("requested_command_execution_review_outcome")
    if _present(requested) and requested not in OUTCOME_FAMILY:
        return "DECLARED_COMMAND_EXECUTION_REVIEW_REQUEST_MALFORMED"
    if _contains_forbidden_full_body_key(request) or _contains_truthy_key(
        request, "raw_full_prior_artifact_body_returned"
    ):
        return "FULL_PRIOR_ARTIFACT_BODY_EMITTED"
    collapse_code = _first_collapse_code(request)
    if collapse_code is not None:
        return collapse_code
    return _first_failed_code(checks)


def _determine_outcome(request: Mapping[str, Any], block_code: str | None) -> str:
    if block_code is not None:
        return OUTCOME_BLOCKED
    requested = request.get("requested_command_execution_review_outcome")
    if requested in {OUTCOME_RECORDED, OUTCOME_NOT_RECORDED, OUTCOME_REQUIRES_ADDITIONAL_BASIS}:
        return str(requested)
    if request.get("command_execution_review_intent") == INTENT_DO_NOT_RECORD:
        return OUTCOME_NOT_RECORDED
    if _present(request.get("additional_basis_context")):
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS
    if _present(request.get("not_recorded_basis")):
        return OUTCOME_NOT_RECORDED
    return OUTCOME_RECORDED


def _block(code: str | None, reason: str | None = None) -> dict[str, Any]:
    reason_value = reason if reason is not None else BLOCK_REASONS.get(code or "", code)
    return {
        "blocked": code is not None,
        "block_code": code,
        "block_reason": _sanitize(reason_value),
        "raw_full_prior_artifact_body_returned": False,
        "block_evidence_is_contained": True,
    }


def _statement(outcome: str) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    statement = {key: recorded for key in ALLOWED_RECORDED_TRUE_FIELDS}
    statement.update(
        {
            "command_execution_review_only": True,
            "consumed_request_not_reopened": True,
            "command_execution_review_is_not_execution": True,
            "reviewed_basis_is_not_execution_permission": True,
            "reviewed_basis_is_not_command_success": True,
            "command_invocation_not_created": True,
            "command_execution_not_performed": True,
            "command_output_not_created": True,
            "command_result_not_created": True,
            "command_success_not_created": True,
            "execution_permission_not_created": True,
            "execution_approval_not_created": True,
            "command_invocation_authorization_not_created": True,
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


def _command_execution_review_non_meaning() -> dict[str, bool]:
    return {
        "command_execution_review_does_not_mean_command_invocation_created": True,
        "command_execution_review_does_not_mean_command_executed": True,
        "command_execution_review_does_not_mean_command_output_exists": True,
        "command_execution_review_does_not_mean_command_result_exists": True,
        "command_execution_review_does_not_mean_command_success_exists": True,
        "command_execution_review_does_not_mean_execution_permission_exists": True,
        "command_execution_review_does_not_mean_execution_approval_exists": True,
        "command_execution_review_does_not_mean_command_invocation_authorization_exists": True,
        "command_execution_review_does_not_mean_command_success_creates_currentness": True,
        "command_execution_review_does_not_mean_command_success_claims_final_completion": True,
        "command_execution_review_does_not_mean_command_output_becomes_source": True,
        "command_execution_review_does_not_mean_command_result_becomes_authority": True,
        "command_execution_review_does_not_mean_standing_invocation_lane_exists": True,
        "command_execution_review_does_not_mean_repeat_invocation_permission_exists": True,
        "command_execution_review_does_not_mean_consumed_request_token_reopened": True,
        "command_execution_review_does_not_mean_v1_was_repaired": True,
        "command_execution_review_does_not_mean_v1_was_hidden": True,
        "command_execution_review_does_not_mean_v1_passed": True,
        "command_execution_review_does_not_mean_deployment_created": True,
        "command_execution_review_does_not_mean_runtime_hosting_created": True,
        "command_execution_review_does_not_mean_public_release_created": True,
        "command_execution_review_does_not_mean_public_readiness_created": True,
        "command_execution_review_does_not_mean_final_completion_claimed": True,
        "command_execution_review_does_not_mean_continuation_authorized": True,
        "command_execution_review_does_not_mean_reusable_permission_created": True,
        "command_execution_review_does_not_mean_derivative_reception_authorized": True,
        "command_execution_review_does_not_mean_vessel_relation_authorized": True,
        "command_execution_review_does_not_mean_another_reception_request_authorized": True,
        "command_execution_review_does_not_mean_follow_on_work_authorized": True,
    }


def _additional_basis_required(outcome: str, request: Mapping[str, Any]) -> dict[str, Any]:
    required = outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    context = request.get("additional_basis_context")
    return {
        "additional_basis_required": required,
        "additional_basis_context": _sanitize(context) if required else {},
        "missing_basis_not_scheduled": True,
        "missing_basis_not_authorized": True,
        "missing_basis_not_executed": True,
        "command_not_invoked": True,
        "command_not_executed": True,
        "command_output_result_success_not_created": True,
        "execution_permission_not_created": True,
        "execution_approval_not_created": True,
        "command_invocation_authorization_not_created": True,
        "consumed_request_not_reopened": True,
        "standing_lane_repeat_permission_not_created": True,
        "follow_on_work_not_authorized": True,
    }


def _not_recorded_basis(
    outcome: str,
    request: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    not_recorded = outcome == OUTCOME_NOT_RECORDED
    failed_checks = [_sanitize(check) for check in checks if check.get("passed") is not True]
    return {
        "not_recorded": not_recorded,
        "not_recorded_basis": _sanitize(request.get("not_recorded_basis"))
        if not_recorded
        else {},
        "failed_command_execution_review_checks": failed_checks if not_recorded else [],
        "not_recorded_does_not_mutate": True,
        "not_recorded_does_not_repair_prior_artifacts": True,
        "not_recorded_does_not_invoke_command": True,
        "not_recorded_does_not_execute_command": True,
        "not_recorded_does_not_emit_output": True,
        "not_recorded_does_not_create_result": True,
        "not_recorded_does_not_create_success": True,
        "not_recorded_does_not_create_execution_permission_approval_or_invocation_authorization": True,
        "not_recorded_does_not_reopen_consumed_request_token": True,
        "not_recorded_does_not_create_standing_lane_or_repeat_permission": True,
        "not_recorded_does_not_deploy_publish_host_currentize_complete_or_continue": True,
        "not_recorded_does_not_authorize_follow_on_work": True,
    }


def _what_remains_open() -> dict[str, Any]:
    open_items = [
        "command execution review test",
        "command execution review live artifact",
        "command invocation authorization boundary, if separately specified",
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
    ]
    return {
        "open_items": open_items,
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }


def _metadata(request: Mapping[str, Any]) -> dict[str, Any]:
    request_id = request.get("command_execution_review_request_id") or "unidentified"
    return {
        "consumed_single_live_command_invocation_request_command_execution_review_result_id": (
            f"{request_id}__consumed_single_live_command_invocation_request_"
            "command_execution_review_result"
        ),
        "consumed_single_live_command_invocation_request_command_execution_review_result_type": (
            "portable_source_body_verification_consumed_single_live_command_invocation_"
            "request_command_execution_review_result"
        ),
        "consumed_single_live_command_invocation_request_command_execution_review_result_version": RESULT_VERSION,
        "generated_at": _generated_at(),
        "resolver_module": RESOLVER_MODULE,
    }


def _declared_question(
    request: Mapping[str, Any],
    request_path: Path | str | None,
) -> dict[str, Any]:
    question = request.get("command_execution_review_question")
    return {
        "command_execution_review_request_id": request.get("command_execution_review_request_id"),
        "command_execution_review_question": question,
        "canonical_command_execution_review_question": CORE_COMMAND_EXECUTION_REVIEW_QUESTION,
        "command_execution_review_question_declared": _present(question),
        "command_execution_review_intent": request.get("command_execution_review_intent"),
        "command_execution_review_request_path": str(request_path)
        if request_path is not None
        else None,
        "request_is_command_execution_review_only": True,
        "request_does_not_invoke_or_execute_command": True,
    }


def _read_json_object(path_value: Path | str) -> tuple[dict[str, Any] | None, str | None, str | None]:
    path = Path(path_value)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return None, "DECLARED_COMMAND_EXECUTION_REVIEW_REQUEST_UNREADABLE", str(exc)
    try:
        value = json.loads(text)
    except json.JSONDecodeError as exc:
        return None, "DECLARED_COMMAND_EXECUTION_REVIEW_REQUEST_MALFORMED", str(exc)
    if not isinstance(value, Mapping):
        return (
            None,
            "DECLARED_COMMAND_EXECUTION_REVIEW_REQUEST_MALFORMED",
            "JSON root must be an object",
        )
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
        malformed_code = "DECLARED_COMMAND_EXECUTION_REVIEW_REQUEST_MALFORMED"

    checks = _build_checks(request, malformed_code)
    block_code = _determine_block_code(request, checks, malformed_code)
    outcome = _determine_outcome(request, block_code)
    statement = _statement(outcome)

    result: dict[str, Any] = {
        "consumed_single_live_command_invocation_request_command_execution_review_metadata": _metadata(
            request
        ),
        "declared_command_execution_review_question": _declared_question(
            request, request_path
        ),
        "selected_execution_review_boundary_basis": _selected_execution_review_boundary_section(
            request
        ),
        "selected_execution_review_boundary_terminal_summary_basis": _selected_execution_review_boundary_terminal_summary_section(
            request
        ),
        "selected_request_consumption_basis": _selected_request_consumption_section(request),
        "selected_request_consumption_terminal_summary_basis": _selected_request_consumption_terminal_summary_section(
            request
        ),
        "selected_consumed_request_basis": _selected_consumed_request_section(request),
        "selected_v2_admitted_request_basis": _selected_v2_basis_section(request),
        "selected_v1_predecessor_failure_basis": _selected_v1_predecessor_section(request),
        "selected_command_execution_boundary_basis": _reference_basis_section(
            request,
            "selected_command_execution_boundary_basis",
            "selected_command_execution_boundary_basis",
            "selected_command_execution_boundary_result_path",
        ),
        "selected_command_report_basis": _reference_basis_section(
            request,
            "selected_command_report_basis",
            "selected_command_report_basis",
            "selected_command_report_path",
        ),
        "selected_command_implementation_boundary_basis": _reference_basis_section(
            request,
            "selected_command_implementation_boundary_basis",
            "selected_command_implementation_boundary_basis",
            "selected_command_implementation_boundary_result_path",
        ),
        "selected_command_boundary_basis": _reference_basis_section(
            request,
            "selected_command_boundary_basis",
            "selected_command_boundary_basis",
            "selected_command_boundary_result_path",
        ),
        "selected_artifact_emission_containment_basis": _reference_basis_section(
            request,
            "selected_artifact_emission_containment_basis",
            "selected_artifact_emission_containment_basis",
            "selected_artifact_emission_containment_result_path",
        ),
        "selected_evidence_manifest_basis": _reference_basis_section(
            request,
            "selected_evidence_manifest_basis",
            "selected_evidence_manifest_basis",
            "selected_evidence_manifest_result_path",
        ),
        "selected_portable_verification_basis": _reference_basis_section(
            request,
            "selected_portable_verification_basis",
            "selected_portable_verification_basis",
            "selected_portable_verification_result_path",
        ),
        "reviewed_basis_posture": _posture_section(
            request.get("reviewed_basis_posture"),
            "reviewed_basis_posture",
        ),
        "consumed_token_closed_posture": _posture_section(
            request.get("consumed_token_closed_posture"),
            "consumed_token_closed_posture",
        ),
        "no_reopen_consumed_request_posture": _posture_section(
            request.get("no_reopen_consumed_request_posture"),
            "no_reopen_consumed_request_posture",
        ),
        "review_only_posture": _posture_section(
            request.get("review_only_posture"),
            "review_only_posture",
        ),
        "no_command_invocation_posture": _posture_section(
            request.get("no_command_invocation_posture"),
            "no_command_invocation_posture",
        ),
        "no_command_execution_posture": _posture_section(
            request.get("no_command_execution_posture"),
            "no_command_execution_posture",
        ),
        "no_output_result_success_posture": _posture_section(
            request.get("no_output_result_success_posture"),
            "no_output_result_success_posture",
        ),
        "no_execution_permission_posture": _posture_section(
            request.get("no_execution_permission_posture"),
            "no_execution_permission_posture",
        ),
        "no_execution_approval_posture": _posture_section(
            request.get("no_execution_approval_posture"),
            "no_execution_approval_posture",
        ),
        "no_command_invocation_authorization_posture": _posture_section(
            request.get("no_command_invocation_authorization_posture"),
            "no_command_invocation_authorization_posture",
        ),
        "no_standing_lane_posture": _posture_section(
            request.get("no_standing_lane_posture"),
            "no_standing_lane_posture",
        ),
        "no_repeat_permission_posture": _posture_section(
            request.get("no_repeat_permission_posture"),
            "no_repeat_permission_posture",
        ),
        "returned_result_containment_posture": _posture_section(
            request.get("returned_result_containment_posture"),
            "returned_result_containment_posture",
        ),
        "command_execution_review_scope": _scope_section(
            request.get("command_execution_review_scope")
        ),
        "command_execution_review_checks": _checks_summary(checks),
        "command_execution_review_statement": statement,
        "command_execution_review_non_meaning": _command_execution_review_non_meaning(),
        "additional_basis_required": _additional_basis_required(outcome, request),
        "not_recorded_basis": _not_recorded_basis(outcome, request, checks),
        "what_remains_open": _what_remains_open(),
        "non_claims": _false_non_claims(),
        "outcome": outcome,
        "block": _block(block_code, path_reason or request.get("block_reason")),
    }
    result[
        "consumed_single_live_command_invocation_request_command_execution_review_summary"
    ] = build_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_summary(
        result
    )
    return _sanitize(result)


def resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review(
    declared_command_execution_review_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one declared consumed-request command execution review mapping."""

    if declared_command_execution_review_request is None:
        return _build_result({})
    if not isinstance(declared_command_execution_review_request, Mapping):
        return _build_result(
            {},
            malformed_code="DECLARED_COMMAND_EXECUTION_REVIEW_REQUEST_MALFORMED",
        )
    return _build_result(declared_command_execution_review_request)


def resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_from_path(
    declared_command_execution_review_request_path: Path | str,
) -> dict:
    """Resolve one declared consumed-request command execution review JSON object."""

    request, error_code, error_reason = _read_json_object(
        declared_command_execution_review_request_path
    )
    if error_code:
        return _build_result(
            {},
            request_path=declared_command_execution_review_request_path,
            malformed_code=error_code,
            path_reason=error_reason,
        )
    return _build_result(
        request,
        request_path=declared_command_execution_review_request_path,
    )


def build_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_summary(
    result: Mapping[str, Any]
) -> dict:
    """Build a compact non-authoritative command execution review summary."""

    safe_result = _sanitize(result)
    statement = _as_mapping(safe_result.get("command_execution_review_statement"))
    checks = _as_mapping(safe_result.get("command_execution_review_checks"))
    block = _as_mapping(safe_result.get("block"))
    question = _as_mapping(safe_result.get("declared_command_execution_review_question"))
    non_claims = _as_mapping(safe_result.get("non_claims"))
    selected_boundary = _as_mapping(safe_result.get("selected_execution_review_boundary_basis"))
    selected_request_consumption = _as_mapping(
        safe_result.get("selected_request_consumption_basis")
    )
    selected_v2 = _as_mapping(safe_result.get("selected_v2_admitted_request_basis"))
    return {
        "outcome": safe_result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "command_execution_review_request_id": question.get(
            "command_execution_review_request_id"
        ),
        "command_execution_review_question": question.get("command_execution_review_question"),
        "command_execution_review_intent": question.get("command_execution_review_intent"),
        "passed_check_count": checks.get("passed_check_count", 0),
        "failed_check_count": checks.get("failed_check_count", 0),
        "command_execution_review_recorded": statement.get(
            "command_execution_review_recorded", False
        ),
        "reviewed_consumed_request_basis_preserved": statement.get(
            "reviewed_consumed_request_basis_preserved", False
        ),
        "reviewed_execution_review_boundary_basis_preserved": statement.get(
            "reviewed_execution_review_boundary_basis_preserved", False
        ),
        "consumed_request_token_remains_closed": statement.get(
            "consumed_request_token_remains_closed", False
        ),
        "reviewed_basis_posture_declared": statement.get(
            "reviewed_basis_posture_declared", False
        ),
        "execution_review_only": statement.get("execution_review_only", False),
        "execution_still_not_authorized": statement.get(
            "execution_still_not_authorized", False
        ),
        "execution_requires_separate_invocation_step": statement.get(
            "execution_requires_separate_invocation_step", False
        ),
        "v1_predecessor_failure_preserved": statement.get(
            "v1_predecessor_failure_preserved", False
        ),
        "returned_result_containment_preserved": statement.get(
            "returned_result_containment_preserved", False
        ),
        "not_recorded": safe_result.get("outcome") == OUTCOME_NOT_RECORDED,
        "requires_additional_basis": safe_result.get("outcome")
        == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "selected_execution_review_boundary_outcome": selected_boundary.get(
            "selected_execution_review_boundary_result_outcome"
        ),
        "selected_execution_review_boundary_failed_check_count": selected_boundary.get(
            "selected_execution_review_boundary_failed_check_count"
        ),
        "selected_request_consumption_outcome": selected_request_consumption.get(
            "selected_request_consumption_result_outcome"
        ),
        "selected_request_consumption_failed_check_count": selected_request_consumption.get(
            "selected_request_consumption_failed_check_count"
        ),
        "selected_v2_admitted_request_outcome": selected_v2.get(
            "selected_v2_admitted_request_outcome"
        ),
        "selected_v2_admitted_request_version": selected_v2.get(
            "selected_v2_admitted_request_version"
        ),
        "selected_v2_failed_check_count": selected_v2.get("selected_v2_failed_check_count"),
        "command_invocation_not_created": statement.get(
            "command_invocation_not_created", True
        ),
        "command_execution_not_performed": statement.get(
            "command_execution_not_performed", True
        ),
        "command_output_not_created": statement.get("command_output_not_created", True),
        "command_result_not_created": statement.get("command_result_not_created", True),
        "command_success_not_created": statement.get("command_success_not_created", True),
        "execution_permission_not_created": statement.get(
            "execution_permission_not_created", True
        ),
        "execution_approval_not_created": statement.get(
            "execution_approval_not_created", True
        ),
        "command_invocation_authorization_not_created": statement.get(
            "command_invocation_authorization_not_created", True
        ),
        "no_standing_lane": statement.get("no_standing_invocation_lane_created", True),
        "no_repeat_permission": statement.get(
            "no_repeat_invocation_permission_created", True
        ),
        "consumed_request_not_reopened": statement.get("consumed_request_not_reopened", True),
        "command_execution_review_not_execution": statement.get(
            "command_execution_review_is_not_execution", True
        ),
        "reviewed_basis_not_execution_permission": statement.get(
            "reviewed_basis_is_not_execution_permission", True
        ),
        "reviewed_basis_not_command_success": statement.get(
            "reviewed_basis_is_not_command_success", True
        ),
        "v1_not_repaired": not non_claims.get("v1_repaired", True),
        "v1_not_hidden": not non_claims.get("v1_hidden", True),
        "v1_not_claimed_passed": not non_claims.get("v1_claimed_passed", True),
        "no_raw_full_prior_artifact_body_returned": not non_claims.get(
            "raw_full_prior_artifact_body_returned", True
        ),
        "no_artifact_mutation": not non_claims.get("prior_artifacts_mutated", True),
        "no_deployment_runtime_public_release": (
            not non_claims.get("deployment_created", True)
            and not non_claims.get("runtime_hosting_created", True)
            and not non_claims.get("public_release_created", True)
        ),
        "no_operation_permission_public_readiness_final_completion": (
            not non_claims.get("operation_permission_created", True)
            and not non_claims.get("public_launch_readiness_created", True)
            and not non_claims.get("final_completion_claimed", True)
        ),
        "no_continuation_publication_flow_reusable_permission": (
            not non_claims.get("continuation_authorized", True)
            and not non_claims.get("publication_flow_opened", True)
            and not non_claims.get("reusable_permission_created", True)
        ),
        "no_derivative_reception_vessel_relation_another_reception_request_follow_on_work": (
            not non_claims.get("derivative_reception_authorized", True)
            and not non_claims.get("vessel_relation_authorized", True)
            and not non_claims.get("another_reception_request_authorized", True)
            and not non_claims.get("follow_on_work_authorized", True)
        ),
        "key_non_claims": _sanitize(non_claims),
    }


def _unique_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 10000):
        candidate = path.with_name(f"{path.stem}_{index:03d}{path.suffix}")
        if not candidate.exists():
            return candidate
    raise PortableSourceBodyVerificationConsumedSingleLiveCommandInvocationRequestCommandExecutionReviewError(
        f"Could not allocate non-overwriting output path for {path}"
    )


def write_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive bounded command execution review result JSON file."""

    safe_result = _sanitize(result)
    question = _as_mapping(safe_result.get("declared_command_execution_review_question"))
    request_id = _safe_component(
        question.get("command_execution_review_request_id"), "unidentified"
    )
    filename = (
        f"{request_id}__consumed_single_live_command_invocation_request_"
        "command_execution_review_result.json"
    )
    if output_path is None:
        target = (
            PORTABLE_SOURCE_BODY_VERIFICATION_CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_EXECUTION_REVIEW_ROOT
            / filename
        )
    else:
        target = Path(output_path)
        if target.suffix == "":
            target = target / filename
    target.parent.mkdir(parents=True, exist_ok=True)
    target = _unique_path(target)
    target.write_text(
        json.dumps(safe_result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return target


def build_declared_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_request(
    command_execution_review_request_id: str,
    command_execution_review_question: str,
    selected_execution_review_boundary_basis: Mapping[str, Any] | str,
    selected_execution_review_boundary_terminal_summary_basis: Mapping[str, Any] | str,
    selected_request_consumption_basis: Mapping[str, Any] | str,
    selected_request_consumption_terminal_summary_basis: Mapping[str, Any] | str,
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
    reviewed_basis_posture: Mapping[str, Any] | str,
    consumed_token_closed_posture: Mapping[str, Any] | str,
    no_reopen_consumed_request_posture: Mapping[str, Any] | str,
    review_only_posture: Mapping[str, Any] | str,
    no_command_invocation_posture: Mapping[str, Any] | str,
    no_command_execution_posture: Mapping[str, Any] | str,
    no_output_result_success_posture: Mapping[str, Any] | str,
    no_execution_permission_posture: Mapping[str, Any] | str,
    no_execution_approval_posture: Mapping[str, Any] | str,
    no_command_invocation_authorization_posture: Mapping[str, Any] | str,
    no_standing_lane_posture: Mapping[str, Any] | str,
    no_repeat_permission_posture: Mapping[str, Any] | str,
    returned_result_containment_posture: Mapping[str, Any] | str,
    command_execution_review_scope: Sequence[str] | Mapping[str, Any],
    command_execution_review_intent: str = INTENT_RECORD,
    *,
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
    requested_command_execution_review_outcome: str = OUTCOME_RECORDED,
    additional_basis_context: Mapping[str, Any] | None = None,
    not_recorded_basis: Mapping[str, Any] | str | None = None,
) -> dict:
    """Build a declared command execution review request with false non-claims."""

    request: dict[str, Any] = {
        "command_execution_review_request_id": command_execution_review_request_id,
        "command_execution_review_question": command_execution_review_question,
        "command_execution_review_intent": command_execution_review_intent,
        "selected_execution_review_boundary_basis": _copy(
            selected_execution_review_boundary_basis
        ),
        "selected_execution_review_boundary_terminal_summary_basis": _copy(
            selected_execution_review_boundary_terminal_summary_basis
        ),
        "selected_request_consumption_basis": _copy(selected_request_consumption_basis),
        "selected_request_consumption_terminal_summary_basis": _copy(
            selected_request_consumption_terminal_summary_basis
        ),
        "selected_consumed_request_basis": _copy(selected_consumed_request_basis),
        "selected_v2_admitted_request_basis": _copy(selected_v2_admitted_request_basis),
        "selected_v1_predecessor_failure_basis": _copy(
            selected_v1_predecessor_failure_basis
        ),
        "selected_command_execution_boundary_basis": _copy(
            selected_command_execution_boundary_basis
        ),
        "selected_command_report_basis": _copy(selected_command_report_basis),
        "selected_command_implementation_boundary_basis": _copy(
            selected_command_implementation_boundary_basis
        ),
        "selected_command_boundary_basis": _copy(selected_command_boundary_basis),
        "selected_artifact_emission_containment_basis": _copy(
            selected_artifact_emission_containment_basis
        ),
        "selected_evidence_manifest_basis": _copy(selected_evidence_manifest_basis),
        "selected_portable_verification_basis": _copy(selected_portable_verification_basis),
        "reviewed_basis_posture": _copy(reviewed_basis_posture),
        "consumed_token_closed_posture": _copy(consumed_token_closed_posture),
        "no_reopen_consumed_request_posture": _copy(no_reopen_consumed_request_posture),
        "review_only_posture": _copy(review_only_posture),
        "no_command_invocation_posture": _copy(no_command_invocation_posture),
        "no_command_execution_posture": _copy(no_command_execution_posture),
        "no_output_result_success_posture": _copy(no_output_result_success_posture),
        "no_execution_permission_posture": _copy(no_execution_permission_posture),
        "no_execution_approval_posture": _copy(no_execution_approval_posture),
        "no_command_invocation_authorization_posture": _copy(
            no_command_invocation_authorization_posture
        ),
        "no_standing_lane_posture": _copy(no_standing_lane_posture),
        "no_repeat_permission_posture": _copy(no_repeat_permission_posture),
        "returned_result_containment_posture": _copy(returned_result_containment_posture),
        "command_execution_review_scope": _copy(command_execution_review_scope),
        "requested_command_execution_review_outcome": requested_command_execution_review_outcome,
        "declared_non_claims": _false_non_claims(),
    }
    optional_values = {
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
