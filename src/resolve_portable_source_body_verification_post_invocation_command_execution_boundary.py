"""Bounded post-invocation command execution boundary resolver.

This resolver is downstream of a recorded command invocation. It may preserve
one recorded command invocation basis for one future command execution step,
but it does not execute the command, create command output, create command
result, create command success, create execution permission, create execution
approval, create standing execution lane, create repeat execution permission,
reuse the spent authorization token, reopen the consumed request token, or
authorize follow-on work.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class PortableSourceBodyVerificationPostInvocationCommandExecutionBoundaryError(Exception):
    """Raised for hard post-invocation command-execution-boundary failures."""


RESOLVER_MODULE = (
    "resolve_portable_source_body_verification_post_invocation_command_execution_boundary"
)
RESULT_VERSION = "0.1.0"
RESULT_TYPE = (
    "portable_source_body_verification_post_invocation_command_execution_boundary_result"
)
PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_"
    "post_invocation_command_execution_boundary"
)
OUTPUT_ROOT = PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_ROOT

CORE_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_QUESTION = (
    "Can the recorded portable source-body verification command invocation basis be bounded "
    "for one future command execution step without executing the command, creating command "
    "output, command result, command success, execution permission, execution approval, "
    "standing execution lane, repeat execution permission, source, authority, currentness, "
    "final completion, continuation, reusable permission, derivative reception, vessel "
    "relation, another reception request, or follow-on work?"
)

INTENT_RECORD = (
    "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY"
)
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY"
)
INTENT_BLOCK = (
    "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY"
)
SUPPORTED_INTENTS = frozenset({INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK})

OUTCOME_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_BLOCKED"
)
OUTCOME_FAMILY = frozenset(
    {OUTCOME_RECORDED, OUTCOME_NOT_RECORDED, OUTCOME_REQUIRES_ADDITIONAL_BASIS, OUTCOME_BLOCKED}
)

COMMAND_INVOCATION_OUTCOME = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_INVOCATION_RECORDED"
COMMAND_INVOCATION_BOUNDARY_OUTCOME = (
    "CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_BOUNDARY_RECORDED"
)
COMMAND_INVOCATION_AUTHORIZATION_OUTCOME = (
    "CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_AUTHORIZATION_RECORDED"
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

SUPPORTED_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_SCOPE = (
    "POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_ONLY",
    "ONE_FUTURE_COMMAND_EXECUTION_STEP_ONLY",
    "RECORDED_COMMAND_INVOCATION_BASIS_PRESERVED",
    "AUTHORIZATION_TOKEN_SPENT_EXACTLY_ONCE_PRESERVED",
    "AUTHORIZATION_TOKEN_REUSE_BLOCKED",
    "COMMAND_EXECUTION_NOT_PERFORMED",
    "COMMAND_OUTPUT_NOT_CREATED",
    "COMMAND_RESULT_NOT_CREATED",
    "COMMAND_SUCCESS_NOT_CREATED",
    "EXECUTION_PERMISSION_NOT_CREATED",
    "EXECUTION_APPROVAL_NOT_CREATED",
    "NO_STANDING_EXECUTION_LANE_CREATED",
    "NO_REPEAT_EXECUTION_PERMISSION_CREATED",
    "NO_STANDING_INVOCATION_LANE_CREATED",
    "NO_REPEAT_INVOCATION_PERMISSION_CREATED",
    "EXECUTION_BOUNDARY_IS_NOT_EXECUTION",
    "EXECUTION_BOUNDARY_IS_NOT_COMMAND_OUTPUT",
    "EXECUTION_BOUNDARY_IS_NOT_COMMAND_RESULT",
    "EXECUTION_BOUNDARY_IS_NOT_COMMAND_SUCCESS",
    "INVOCATION_BASIS_IS_NOT_EXECUTION",
    "INVOCATION_BASIS_IS_NOT_COMMAND_SUCCESS",
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
SUPPORTED_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_SCOPE_SET = frozenset(
    SUPPORTED_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_SCOPE
)

REQUIRED_FALSE_NON_CLAIMS = (
    "command_executed",
    "command_execution_performed",
    "command_output_created",
    "command_result_created",
    "command_success_created",
    "execution_permission_created",
    "execution_approval_created",
    "standing_execution_lane_created",
    "repeat_execution_permission_created",
    "standing_invocation_lane_created",
    "repeat_invocation_permission_created",
    "authorization_token_reused",
    "consumed_request_reopened",
    "execution_boundary_treated_as_execution",
    "execution_boundary_treated_as_command_output",
    "execution_boundary_treated_as_command_result",
    "execution_boundary_treated_as_command_success",
    "invocation_basis_treated_as_execution",
    "invocation_basis_treated_as_command_success",
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
    "post_invocation_command_execution_boundary_recorded",
    "recorded_command_invocation_basis_preserved",
    "one_future_command_execution_step_declared",
    "authorization_token_spent_exactly_once_preserved",
    "authorization_token_reuse_blocked",
    "command_execution_still_not_performed",
    "command_output_still_not_created",
    "command_result_still_not_created",
    "command_success_still_not_created",
    "execution_permission_not_created",
    "execution_approval_not_created",
    "consumed_request_token_remains_closed",
    "v1_predecessor_failure_preserved",
    "returned_result_containment_preserved",
)

FORBIDDEN_FULL_BODY_KEYS = frozenset(
    {
        "artifact_body",
        "complete_artifact_body",
        "complete_result",
        "embedded_artifact",
        "full_artifact_body",
        "full_body",
        "full_prior_artifact_body",
        "full_prior_artifacts",
        "full_result",
        "prior_artifact_body",
        "raw_artifact",
        "raw_body",
        "raw_full_artifact_body",
        "raw_full_prior_artifact_body",
        "raw_full_result",
        "raw_result",
        "selected_full_artifact",
    }
)
FULL_BODY_OMISSION_MARKER = "[omitted: full prior artifact body is not returned]"

BLOCK_CODES = frozenset(
    {
        "DECLARED_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_REQUEST_MALFORMED",
        "DECLARED_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_REQUEST_UNREADABLE",
        "POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_QUESTION_UNDECLARED",
        "POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_INTENT_UNSUPPORTED",
        "COMMAND_INVOCATION_BASIS_MISSING",
        "COMMAND_INVOCATION_NOT_RECORDED",
        "COMMAND_INVOCATION_FAILED_CHECKS_PRESENT",
        "COMMAND_INVOCATION_EVENT_NOT_RECORDED",
        "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_NOT_SPENT_EXACTLY_ONCE",
        "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_REUSE_NOT_BLOCKED",
        "COMMAND_INVOCATION_BOUNDARY_BASIS_MISSING",
        "COMMAND_INVOCATION_BOUNDARY_NOT_RECORDED",
        "COMMAND_INVOCATION_BOUNDARY_FAILED_CHECKS_PRESENT",
        "COMMAND_INVOCATION_AUTHORIZATION_BASIS_MISSING",
        "COMMAND_INVOCATION_AUTHORIZATION_NOT_RECORDED",
        "COMMAND_INVOCATION_AUTHORIZATION_FAILED_CHECKS_PRESENT",
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
        "COMMAND_EXECUTION_BOUNDARY_LINEAGE_BASIS_TREATED_AS_CURRENT_EXECUTION",
        "COMMAND_REPORT_BASIS_MISSING",
        "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING",
        "COMMAND_BOUNDARY_BASIS_MISSING",
        "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING",
        "EVIDENCE_MANIFEST_BASIS_MISSING",
        "PORTABLE_VERIFICATION_BASIS_MISSING",
        "POST_INVOCATION_EXECUTION_BOUNDARY_ONLY_POSTURE_MISSING",
        "ONE_FUTURE_COMMAND_EXECUTION_STEP_POSTURE_MISSING",
        "INVOCATION_BASIS_PRESERVED_POSTURE_MISSING",
        "AUTHORIZATION_TOKEN_SPENT_EXACTLY_ONCE_POSTURE_MISSING",
        "AUTHORIZATION_TOKEN_REUSE_BLOCKED_POSTURE_MISSING",
        "NO_STANDING_EXECUTION_LANE_POSTURE_MISSING",
        "NO_REPEAT_EXECUTION_PERMISSION_POSTURE_MISSING",
        "UNSUPPORTED_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_SCOPE",
        "COMMAND_EXECUTION_PERFORMED",
        "COMMAND_OUTPUT_CREATED",
        "COMMAND_RESULT_CREATED",
        "COMMAND_SUCCESS_CREATED",
        "EXECUTION_PERMISSION_CREATED",
        "EXECUTION_APPROVAL_CREATED",
        "STANDING_EXECUTION_LANE_CREATED",
        "REPEAT_EXECUTION_PERMISSION_CREATED",
        "STANDING_INVOCATION_LANE_CREATED",
        "REPEAT_INVOCATION_PERMISSION_CREATED",
        "EXECUTION_BOUNDARY_TREATED_AS_EXECUTION",
        "EXECUTION_BOUNDARY_TREATED_AS_COMMAND_OUTPUT",
        "EXECUTION_BOUNDARY_TREATED_AS_COMMAND_RESULT",
        "EXECUTION_BOUNDARY_TREATED_AS_COMMAND_SUCCESS",
        "INVOCATION_BASIS_TREATED_AS_EXECUTION",
        "INVOCATION_BASIS_TREATED_AS_COMMAND_SUCCESS",
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
        "POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_BLOCKED_BY_REQUEST",
    }
)

COLLAPSE_TRUE_BLOCKS = (
    ("command_executed", "COMMAND_EXECUTION_PERFORMED"),
    ("command_execution_performed", "COMMAND_EXECUTION_PERFORMED"),
    ("command_output_created", "COMMAND_OUTPUT_CREATED"),
    ("command_result_created", "COMMAND_RESULT_CREATED"),
    ("command_success_created", "COMMAND_SUCCESS_CREATED"),
    ("execution_permission_created", "EXECUTION_PERMISSION_CREATED"),
    ("execution_approval_created", "EXECUTION_APPROVAL_CREATED"),
    ("standing_execution_lane_created", "STANDING_EXECUTION_LANE_CREATED"),
    ("repeat_execution_permission_created", "REPEAT_EXECUTION_PERMISSION_CREATED"),
    ("standing_invocation_lane_created", "STANDING_INVOCATION_LANE_CREATED"),
    ("repeat_invocation_permission_created", "REPEAT_INVOCATION_PERMISSION_CREATED"),
    ("authorization_token_reused", "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_REUSE_NOT_BLOCKED"),
    ("authorization_token_reuse_created", "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_REUSE_NOT_BLOCKED"),
    ("authorization_token_reuse_permitted", "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_REUSE_NOT_BLOCKED"),
    ("authorization_token_revived", "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_REUSE_NOT_BLOCKED"),
    ("authorization_token_respawned", "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_REUSE_NOT_BLOCKED"),
    ("spent_authorization_token_reused", "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_REUSE_NOT_BLOCKED"),
    ("consumed_request_reopened", "CONSUMED_REQUEST_REOPENED"),
    ("execution_boundary_treated_as_execution", "EXECUTION_BOUNDARY_TREATED_AS_EXECUTION"),
    ("execution_boundary_treated_as_command_output", "EXECUTION_BOUNDARY_TREATED_AS_COMMAND_OUTPUT"),
    ("execution_boundary_treated_as_command_result", "EXECUTION_BOUNDARY_TREATED_AS_COMMAND_RESULT"),
    ("execution_boundary_treated_as_command_success", "EXECUTION_BOUNDARY_TREATED_AS_COMMAND_SUCCESS"),
    ("invocation_basis_treated_as_execution", "INVOCATION_BASIS_TREATED_AS_EXECUTION"),
    ("invocation_basis_treated_as_command_success", "INVOCATION_BASIS_TREATED_AS_COMMAND_SUCCESS"),
    (
        "command_execution_boundary_lineage_treated_as_current_execution",
        "COMMAND_EXECUTION_BOUNDARY_LINEAGE_BASIS_TREATED_AS_CURRENT_EXECUTION",
    ),
    (
        "selected_command_execution_boundary_lineage_basis_treated_as_current_execution",
        "COMMAND_EXECUTION_BOUNDARY_LINEAGE_BASIS_TREATED_AS_CURRENT_EXECUTION",
    ),
    ("lineage_basis_treated_as_current_execution", "COMMAND_EXECUTION_BOUNDARY_LINEAGE_BASIS_TREATED_AS_CURRENT_EXECUTION"),
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
    return "".join(char if char.isalnum() or char in {"-", "_", "."} else "_" for char in text).strip("._") or fallback


def _contains_forbidden_full_body_key(value: Any) -> bool:
    if isinstance(value, Mapping):
        return any(
            str(key) in FORBIDDEN_FULL_BODY_KEYS or _contains_forbidden_full_body_key(item)
            for key, item in value.items()
        )
    if isinstance(value, list):
        return any(_contains_forbidden_full_body_key(item) for item in value)
    return False


def _sanitize_reference_shape(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {
            str(key): FULL_BODY_OMISSION_MARKER
            if str(key) in FORBIDDEN_FULL_BODY_KEYS
            else _sanitize_reference_shape(item)
            for key, item in value.items()
        }
    if isinstance(value, list):
        return [_sanitize_reference_shape(item) for item in value]
    return _deepcopy(value)


def _mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


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
    for key, item in (extra or {}).items():
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


def _truthy(mapping: Mapping[str, Any], keys: Sequence[str]) -> bool:
    return any(_find_first(mapping, (key,)) is True for key in keys)


def _declared(value: Any) -> bool:
    return bool(value) if isinstance(value, Mapping) else isinstance(value, (str, Path)) and bool(str(value).strip())


def _outcome(basis: Mapping[str, Any], request: Mapping[str, Any], keys: Sequence[str]) -> Any:
    for key in keys:
        if key in request:
            return request[key]
    return _find_first(basis, ("outcome", "result_outcome", "selected_outcome", "selected_result_outcome"))


def _failed_count(basis: Mapping[str, Any], request: Mapping[str, Any], keys: Sequence[str]) -> int | None:
    for key in keys:
        if key in request:
            return _to_int(request[key])
    value = _find_first(basis, ("failed_check_count", "failed_checks_count", "failed_checks", "selected_failed_check_count"))
    return len(value) if isinstance(value, list) else _to_int(value)


def _version(basis: Mapping[str, Any], request: Mapping[str, Any], keys: Sequence[str]) -> Any:
    for key in keys:
        if key in request:
            return request[key]
    return _find_first(basis, ("result_version", "version", "selected_version", "artifact_version"))


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


def _default_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _declared_non_claims(request: Mapping[str, Any]) -> Mapping[str, Any]:
    return request.get("declared_non_claims") if isinstance(request.get("declared_non_claims"), Mapping) else {}


def _first_non_claim_failure(request: Mapping[str, Any]) -> str | None:
    declared = _declared_non_claims(request)
    for key in REQUIRED_FALSE_NON_CLAIMS:
        if key not in declared or declared.get(key) is not False:
            return key
    return None


def _first_collapse(values: Sequence[Any]) -> tuple[str, str] | None:
    for value in values:
        if isinstance(value, Mapping):
            for key, code in COLLAPSE_TRUE_BLOCKS:
                if _truthy(value, (key,)):
                    return key, code
            if any(_truthy(value, (key,)) for key in ("mutation_performed", "replay_performed", "merge_performed")):
                return "mutation_replay_or_merge", "MUTATION_REPLAY_OR_MERGE_DETECTED"
    return None


def _check(checks: list[dict[str, Any]], name: str, passed: bool, expected: str, actual: Any, code: str) -> None:
    checks.append(
        {
            "check_name": name,
            "passed": bool(passed),
            "expected_posture": expected,
            "actual_posture": _sanitize_reference_shape(actual),
            "block_code": None if passed else code,
            "failure_code": None if passed else code,
        }
    )


def _successor_metadata_preserved(basis: Mapping[str, Any], request: Mapping[str, Any]) -> bool:
    explicit = request.get("selected_v2_successor_metadata")
    if isinstance(explicit, Mapping) and explicit:
        return True
    if _find_first(basis, ("successor_of", "predecessor_resolver_module")) and _find_first(
        basis, ("successor_reason", "successor_transition_reason")
    ) and _find_first(basis, ("resolver_module",)):
        return True
    return _truthy(basis, ("successor_metadata_preserved", "v2_successor_metadata_preserved", "successor_metadata_declared"))


def _returned_result_containment_preserved(basis: Mapping[str, Any]) -> bool:
    return _truthy(
        basis,
        (
            "returned_result_containment_preserved",
            "returned_result_containment_posture_preserved",
            "returned_result_containment_declared",
            "no_raw_full_prior_artifact_body_returned",
        ),
    )


def _consumed_token_closed(basis: Mapping[str, Any]) -> bool:
    return _truthy(basis, ("consumed_request_token_remains_closed", "consumed_request_token_closed", "consumption_token_closed", "consumed_token_closed", "token_closed"))


def _consumed_not_reopened(basis: Mapping[str, Any]) -> bool:
    return not _truthy(basis, ("consumed_request_reopened", "request_reopened", "token_reopened")) and _truthy(
        basis,
        ("consumed_request_is_not_reopened", "consumed_request_not_reopened", "no_reopen_consumed_request", "request_not_reopened"),
    )


def _v1_failure_visible(basis: Mapping[str, Any]) -> bool:
    return _truthy(
        basis,
        (
            "v1_predecessor_failure_remains_visible",
            "v1_remains_visible_predecessor_failure_evidence",
            "visible_predecessor_failure_evidence",
            "v1_predecessor_failure_basis_declared",
        ),
    )


def _authorization_token_reused(value: Mapping[str, Any]) -> bool:
    return _truthy(
        value,
        (
            "authorization_token_reused",
            "authorization_token_reuse_created",
            "authorization_token_reuse_permitted",
            "authorization_token_revived",
            "authorization_token_respawned",
            "spent_authorization_token_reused",
        ),
    )


def _lineage_as_current_execution(basis: Mapping[str, Any]) -> bool:
    return _truthy(
        basis,
        (
            "command_execution_boundary_lineage_treated_as_current_execution",
            "selected_command_execution_boundary_lineage_basis_treated_as_current_execution",
            "lineage_basis_treated_as_current_execution",
            "lineage_basis_is_current_execution",
            "basis_treated_as_current_execution",
            "current_execution",
            "command_execution_performed",
        ),
    )


def _build_checks(request: Mapping[str, Any], malformed: bool = False) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    if malformed:
        _check(checks, "declared post-invocation command execution boundary request mapping", False, "request is a mapping", "malformed", "DECLARED_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_REQUEST_MALFORMED")
        return checks

    invocation = _mapping(request.get("selected_command_invocation_basis"))
    boundary = _mapping(request.get("selected_command_invocation_boundary_basis"))
    authorization = _mapping(request.get("selected_command_invocation_authorization_basis"))
    review = _mapping(request.get("selected_command_execution_review_basis"))
    consumption = _mapping(request.get("selected_request_consumption_basis"))
    consumed = _mapping(request.get("selected_consumed_request_basis"))
    v2 = _mapping(request.get("selected_v2_admitted_request_basis"))
    v1 = _mapping(request.get("selected_v1_predecessor_failure_basis"))
    lineage = _mapping(request.get("selected_command_execution_boundary_lineage_basis"))
    declared = _declared_non_claims(request)

    _check(checks, "post-invocation command execution boundary question declared", isinstance(request.get("post_invocation_command_execution_boundary_question"), str) and bool(request.get("post_invocation_command_execution_boundary_question", "").strip()), "question declared", request.get("post_invocation_command_execution_boundary_question"), "POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_QUESTION_UNDECLARED")
    _check(checks, "post-invocation command execution boundary intent supported", request.get("post_invocation_command_execution_boundary_intent") in SUPPORTED_INTENTS, "supported intent", request.get("post_invocation_command_execution_boundary_intent"), "POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_INTENT_UNSUPPORTED")
    _check(checks, "command invocation terminal summary basis declared", _present(request.get("selected_command_invocation_terminal_summary_basis")), "terminal summary declared", request.get("selected_command_invocation_terminal_summary_basis"), "COMMAND_INVOCATION_BASIS_MISSING")
    _check(checks, "command invocation live artifact basis declared", _declared(request.get("selected_command_invocation_basis")), "command invocation basis declared", request.get("selected_command_invocation_basis"), "COMMAND_INVOCATION_BASIS_MISSING")
    _check(checks, "command invocation live artifact recorded", _outcome(invocation, request, ("selected_command_invocation_result_outcome",)) == COMMAND_INVOCATION_OUTCOME, COMMAND_INVOCATION_OUTCOME, _outcome(invocation, request, ("selected_command_invocation_result_outcome",)), "COMMAND_INVOCATION_NOT_RECORDED")
    _check(checks, "command invocation failed check count zero", _failed_count(invocation, request, ("selected_command_invocation_failed_check_count",)) == 0, "failed_check_count == 0", _failed_count(invocation, request, ("selected_command_invocation_failed_check_count",)), "COMMAND_INVOCATION_FAILED_CHECKS_PRESENT")
    _check(checks, "command invocation event recorded", request.get("selected_command_invocation_event_recorded") is True or _truthy(invocation, ("bounded_command_invocation_event_recorded", "command_invocation_recorded", "command_invocation_event_recorded")), "bounded invocation event recorded", invocation, "COMMAND_INVOCATION_EVENT_NOT_RECORDED")
    _check(checks, "authorization token spent exactly once", request.get("selected_command_invocation_authorization_token_spent_exactly_once") is True or _truthy(invocation, ("authorization_token_spent_exactly_once", "authorization_token_spent_exactly_once_preserved", "one_shot_authorization_token_spent_exactly_once")), "token spent exactly once", invocation, "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_NOT_SPENT_EXACTLY_ONCE")
    _check(checks, "authorization token reuse blocked", (request.get("selected_command_invocation_authorization_token_reuse_blocked") is True or _truthy(invocation, ("authorization_token_reuse_blocked", "authorization_token_reuse_not_created", "authorization_token_not_reused"))) and not _authorization_token_reused(invocation), "token reuse blocked", invocation, "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_REUSE_NOT_BLOCKED")

    outcome_checks = (
        ("command invocation boundary basis declared", "selected_command_invocation_boundary_basis", boundary, ("selected_command_invocation_boundary_result_outcome",), COMMAND_INVOCATION_BOUNDARY_OUTCOME, "COMMAND_INVOCATION_BOUNDARY_BASIS_MISSING", "COMMAND_INVOCATION_BOUNDARY_NOT_RECORDED", "selected_command_invocation_boundary_failed_check_count", "COMMAND_INVOCATION_BOUNDARY_FAILED_CHECKS_PRESENT"),
        ("command invocation authorization basis declared", "selected_command_invocation_authorization_basis", authorization, ("selected_command_invocation_authorization_result_outcome",), COMMAND_INVOCATION_AUTHORIZATION_OUTCOME, "COMMAND_INVOCATION_AUTHORIZATION_BASIS_MISSING", "COMMAND_INVOCATION_AUTHORIZATION_NOT_RECORDED", "selected_command_invocation_authorization_failed_check_count", "COMMAND_INVOCATION_AUTHORIZATION_FAILED_CHECKS_PRESENT"),
        ("command execution review basis declared", "selected_command_execution_review_basis", review, ("selected_command_execution_review_result_outcome",), COMMAND_EXECUTION_REVIEW_OUTCOME, "COMMAND_EXECUTION_REVIEW_BASIS_MISSING", "COMMAND_EXECUTION_REVIEW_NOT_RECORDED", "selected_command_execution_review_failed_check_count", "COMMAND_EXECUTION_REVIEW_FAILED_CHECKS_PRESENT"),
        ("request consumption basis declared", "selected_request_consumption_basis", consumption, ("selected_request_consumption_result_outcome",), REQUEST_CONSUMPTION_OUTCOME, "REQUEST_CONSUMPTION_BASIS_MISSING", "REQUEST_CONSUMPTION_NOT_CONSUMED", "selected_request_consumption_failed_check_count", "REQUEST_CONSUMPTION_FAILED_CHECKS_PRESENT"),
    )
    for name, key, basis, outcome_keys, expected, missing, not_recorded, failed_key, failed_code in outcome_checks:
        _check(checks, name, _declared(request.get(key)), "basis declared", request.get(key), missing)
        _check(checks, name.replace("basis declared", "recorded outcome"), _outcome(basis, request, outcome_keys) == expected, expected, _outcome(basis, request, outcome_keys), not_recorded)
        _check(checks, name.replace("basis declared", "failed check count zero"), _failed_count(basis, request, (failed_key,)) == 0, "failed_check_count == 0", _failed_count(basis, request, (failed_key,)), failed_code)

    _check(checks, "consumed request basis declared", _declared(request.get("selected_consumed_request_basis")), "consumed request basis declared", request.get("selected_consumed_request_basis"), "CONSUMED_REQUEST_BASIS_MISSING")
    _check(checks, "consumed request token remains closed", _consumed_token_closed(consumed), "consumed token closed", consumed, "CONSUMED_TOKEN_NOT_CLOSED")
    _check(checks, "consumed request not reopened", _consumed_not_reopened(consumed), "consumed request not reopened", consumed, "CONSUMED_REQUEST_REOPENED")

    _check(checks, "v2 admitted request basis declared", _declared(request.get("selected_v2_admitted_request_basis")), "v2 basis declared", request.get("selected_v2_admitted_request_basis"), "V2_ADMITTED_REQUEST_BASIS_MISSING")
    _check(checks, "v2 admitted request outcome admitted", _outcome(v2, request, ("selected_v2_admitted_request_outcome",)) == V2_ADMITTED_REQUEST_OUTCOME, V2_ADMITTED_REQUEST_OUTCOME, _outcome(v2, request, ("selected_v2_admitted_request_outcome",)), "V2_ADMITTED_REQUEST_NOT_ADMITTED")
    _check(checks, "v2 admitted request version 0.2.0", _version(v2, request, ("selected_v2_admitted_request_version",)) == V2_ADMITTED_REQUEST_VERSION, V2_ADMITTED_REQUEST_VERSION, _version(v2, request, ("selected_v2_admitted_request_version",)), "V2_ADMITTED_REQUEST_VERSION_NOT_0_2_0")
    _check(checks, "v2 admitted request failed check count zero", _failed_count(v2, request, ("selected_v2_failed_check_count",)) == 0, "failed_check_count == 0", _failed_count(v2, request, ("selected_v2_failed_check_count",)), "V2_ADMITTED_REQUEST_FAILED_CHECKS_PRESENT")
    _check(checks, "v2 successor metadata preserved", _successor_metadata_preserved(v2, request), "successor metadata preserved", v2, "V2_SUCCESSOR_METADATA_MISSING")
    _check(checks, "v2 returned-result containment preserved", _returned_result_containment_preserved(v2), "returned-result containment preserved", v2, "V2_RETURNED_RESULT_CONTAINMENT_MISSING")
    _check(checks, "v1 predecessor failure basis declared", _declared(request.get("selected_v1_predecessor_failure_basis")), "v1 basis declared", request.get("selected_v1_predecessor_failure_basis"), "V1_PREDECESSOR_FAILURE_BASIS_MISSING")
    _check(checks, "v1 predecessor failure remains visible", _v1_failure_visible(v1), "v1 failure visible", v1, "V1_PREDECESSOR_FAILURE_BASIS_MISSING")
    _check(checks, "v2 does not claim v1 passed", not (_truthy(v1, ("v1_claimed_passed", "v1_passed")) or _truthy(v2, ("v2_claims_v1_passed", "v1_claimed_passed", "v1_passed"))), "v1 not claimed passed", {"v1": v1, "v2": v2}, "V1_CLAIMED_PASSED")
    _check(checks, "v2 not treated as repairing v1", not (_truthy(v1, ("v2_treated_as_repairing_v1", "v1_repaired")) or _truthy(v2, ("v2_treated_as_repairing_v1", "v1_repaired"))), "v2 does not repair v1", {"v1": v1, "v2": v2}, "V2_TREATED_AS_REPAIRING_V1")
    _check(checks, "v1 failure not hidden", not _truthy(v1, ("v1_hidden", "v1_failure_hidden")), "v1 failure not hidden", v1, "V1_FAILURE_HIDDEN")

    _check(checks, "command execution boundary lineage basis declared", _declared(request.get("selected_command_execution_boundary_lineage_basis")), "lineage basis declared", request.get("selected_command_execution_boundary_lineage_basis"), "COMMAND_EXECUTION_BOUNDARY_LINEAGE_BASIS_TREATED_AS_CURRENT_EXECUTION")
    _check(checks, "command execution boundary lineage basis not treated as current execution", not _lineage_as_current_execution(lineage), "lineage basis is prior scaffolding only", lineage, "COMMAND_EXECUTION_BOUNDARY_LINEAGE_BASIS_TREATED_AS_CURRENT_EXECUTION")
    for name, key, code in (
        ("command report basis declared", "selected_command_report_basis", "COMMAND_REPORT_BASIS_MISSING"),
        ("command implementation boundary basis declared", "selected_command_implementation_boundary_basis", "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING"),
        ("command boundary basis declared", "selected_command_boundary_basis", "COMMAND_BOUNDARY_BASIS_MISSING"),
        ("artifact emission containment basis declared", "selected_artifact_emission_containment_basis", "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING"),
        ("evidence-manifest basis declared", "selected_evidence_manifest_basis", "EVIDENCE_MANIFEST_BASIS_MISSING"),
        ("portable verification basis declared", "selected_portable_verification_basis", "PORTABLE_VERIFICATION_BASIS_MISSING"),
    ):
        _check(checks, name, _declared(request.get(key)), "basis declared", request.get(key), code)
    for name, key, code in (
        ("post-invocation-execution-boundary-only posture declared", "post_invocation_execution_boundary_only_posture", "POST_INVOCATION_EXECUTION_BOUNDARY_ONLY_POSTURE_MISSING"),
        ("one-future-command-execution-step posture declared", "one_future_command_execution_step_posture", "ONE_FUTURE_COMMAND_EXECUTION_STEP_POSTURE_MISSING"),
        ("invocation-basis-preserved posture declared", "invocation_basis_preserved_posture", "INVOCATION_BASIS_PRESERVED_POSTURE_MISSING"),
        ("authorization-token-spent-exactly-once posture declared", "authorization_token_spent_exactly_once_posture", "AUTHORIZATION_TOKEN_SPENT_EXACTLY_ONCE_POSTURE_MISSING"),
        ("authorization-token-reuse-blocked posture declared", "authorization_token_reuse_blocked_posture", "AUTHORIZATION_TOKEN_REUSE_BLOCKED_POSTURE_MISSING"),
        ("no-command-execution posture declared", "no_command_execution_posture", "COMMAND_EXECUTION_PERFORMED"),
        ("no-output/result/success posture declared", "no_output_result_success_posture", "COMMAND_OUTPUT_CREATED"),
        ("no-execution-permission posture declared", "no_execution_permission_posture", "EXECUTION_PERMISSION_CREATED"),
        ("no-execution-approval posture declared", "no_execution_approval_posture", "EXECUTION_APPROVAL_CREATED"),
        ("no-standing-execution-lane posture declared", "no_standing_execution_lane_posture", "NO_STANDING_EXECUTION_LANE_POSTURE_MISSING"),
        ("no-repeat-execution-permission posture declared", "no_repeat_execution_permission_posture", "NO_REPEAT_EXECUTION_PERMISSION_POSTURE_MISSING"),
        ("no-standing-invocation-lane posture declared", "no_standing_invocation_lane_posture", "STANDING_INVOCATION_LANE_CREATED"),
        ("no-repeat-invocation-permission posture declared", "no_repeat_invocation_permission_posture", "REPEAT_INVOCATION_PERMISSION_CREATED"),
        ("consumed-token-closed posture declared", "consumed_token_closed_posture", "CONSUMED_TOKEN_NOT_CLOSED"),
        ("no-reopen-consumed-request posture declared", "no_reopen_consumed_request_posture", "CONSUMED_REQUEST_REOPENED"),
        ("returned-result containment posture declared", "returned_result_containment_posture", "V2_RETURNED_RESULT_CONTAINMENT_MISSING"),
    ):
        _check(checks, name, _present(request.get(key)), "posture declared", request.get(key), code)

    _check(checks, "authorization token spent exactly once posture preserves spend", _truthy(_mapping(request.get("authorization_token_spent_exactly_once_posture")), ("authorization_token_spent_exactly_once_preserved", "authorization_token_spent_exactly_once")), "spend preserved", request.get("authorization_token_spent_exactly_once_posture"), "AUTHORIZATION_TOKEN_SPENT_EXACTLY_ONCE_POSTURE_MISSING")
    _check(checks, "authorization token reuse blocked posture preserves block", _truthy(_mapping(request.get("authorization_token_reuse_blocked_posture")), ("authorization_token_reuse_blocked", "authorization_token_not_reused", "no_token_reuse")) and not _authorization_token_reused(_mapping(request.get("authorization_token_reuse_blocked_posture"))), "reuse blocked", request.get("authorization_token_reuse_blocked_posture"), "AUTHORIZATION_TOKEN_REUSE_BLOCKED_POSTURE_MISSING")
    scope = _scope_values(request.get("post_invocation_command_execution_boundary_scope"))
    _check(checks, "post-invocation command execution boundary scope supported", bool(scope) and all(value in SUPPORTED_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_SCOPE_SET for value in scope), "supported scope", scope, "UNSUPPORTED_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_SCOPE")

    for key, code in (
        ("command_execution_performed", "COMMAND_EXECUTION_PERFORMED"),
        ("command_output_created", "COMMAND_OUTPUT_CREATED"),
        ("command_result_created", "COMMAND_RESULT_CREATED"),
        ("command_success_created", "COMMAND_SUCCESS_CREATED"),
        ("execution_permission_created", "EXECUTION_PERMISSION_CREATED"),
        ("execution_approval_created", "EXECUTION_APPROVAL_CREATED"),
        ("standing_execution_lane_created", "STANDING_EXECUTION_LANE_CREATED"),
        ("repeat_execution_permission_created", "REPEAT_EXECUTION_PERMISSION_CREATED"),
        ("standing_invocation_lane_created", "STANDING_INVOCATION_LANE_CREATED"),
        ("repeat_invocation_permission_created", "REPEAT_INVOCATION_PERMISSION_CREATED"),
        ("authorization_token_reused", "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_REUSE_NOT_BLOCKED"),
        ("execution_boundary_treated_as_execution", "EXECUTION_BOUNDARY_TREATED_AS_EXECUTION"),
        ("execution_boundary_treated_as_command_output", "EXECUTION_BOUNDARY_TREATED_AS_COMMAND_OUTPUT"),
        ("execution_boundary_treated_as_command_result", "EXECUTION_BOUNDARY_TREATED_AS_COMMAND_RESULT"),
        ("execution_boundary_treated_as_command_success", "EXECUTION_BOUNDARY_TREATED_AS_COMMAND_SUCCESS"),
        ("invocation_basis_treated_as_execution", "INVOCATION_BASIS_TREATED_AS_EXECUTION"),
        ("invocation_basis_treated_as_command_success", "INVOCATION_BASIS_TREATED_AS_COMMAND_SUCCESS"),
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
        ("final_completion_claimed", "FINAL_COMPLETION_CLAIMED"),
        ("continuation_authorized", "CONTINUATION_AUTHORIZED"),
        ("reusable_permission_created", "REUSABLE_PERMISSION_CREATED"),
        ("derivative_reception_authorized", "DERIVATIVE_RECEPTION_AUTHORIZED"),
        ("vessel_relation_authorized", "VESSEL_RELATION_AUTHORIZED"),
        ("another_reception_request_authorized", "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"),
        ("follow_on_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
    ):
        _check(checks, key.replace("_", " "), declared.get(key) is False, f"{key} is false", declared.get(key), code)

    collapse = _first_collapse((request, declared, invocation, boundary, authorization, review, consumption, consumed, lineage))
    _check(checks, "collapse flags absent", collapse is None, "no collapse flags", collapse, collapse[1] if collapse else "MUTATION_REPLAY_OR_MERGE_DETECTED")
    full_body_present = _contains_forbidden_full_body_key(request)
    _check(checks, "raw full prior artifact body not emitted", not full_body_present, "no full prior artifact body", "forbidden full-body key present" if full_body_present else "contained", "FULL_PRIOR_ARTIFACT_BODY_EMITTED")
    non_claim_failure = _first_non_claim_failure(request)
    _check(checks, "non-claims remain false", non_claim_failure is None, "required non-claims false", non_claim_failure, "NON_CLAIM_MISSING_OR_FLIPPED")
    return checks


def _first_failed(checks: Sequence[Mapping[str, Any]]) -> Mapping[str, Any] | None:
    return next((check for check in checks if not check.get("passed")), None)


def _select_outcome(request: Mapping[str, Any], checks: Sequence[Mapping[str, Any]], forced_block: str | None = None) -> tuple[str, str | None, str | None]:
    if forced_block:
        return OUTCOME_BLOCKED, forced_block, forced_block
    intent = request.get("post_invocation_command_execution_boundary_intent")
    if intent == INTENT_BLOCK:
        return OUTCOME_BLOCKED, "POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_BLOCKED_BY_REQUEST", str(request.get("block_reason") or "blocked by request intent")
    if intent not in SUPPORTED_INTENTS:
        return OUTCOME_BLOCKED, "POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_INTENT_UNSUPPORTED", "unsupported post-invocation command execution boundary intent"
    requested = request.get("requested_post_invocation_command_execution_boundary_outcome", OUTCOME_RECORDED)
    if requested == OUTCOME_BLOCKED:
        return OUTCOME_BLOCKED, "POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_BLOCKED_BY_REQUEST", str(request.get("block_reason") or "blocked by requested outcome")
    if requested not in OUTCOME_FAMILY:
        return OUTCOME_BLOCKED, "DECLARED_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_REQUEST_MALFORMED", "unsupported requested outcome"
    failed = _first_failed(checks)
    if failed is not None:
        return OUTCOME_BLOCKED, str(failed.get("block_code")), str(failed.get("check_name"))
    if intent == INTENT_DO_NOT_RECORD or requested == OUTCOME_NOT_RECORDED:
        return OUTCOME_NOT_RECORDED, None, None
    if requested == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS, None, None
    return OUTCOME_RECORDED, None, None


def _statement(outcome: str) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    statement = {key: recorded for key in ALLOWED_TRUE_RECORDED_FIELDS}
    statement.update(_default_non_claims())
    statement.update(
        {
            "post_invocation_command_execution_boundary_not_recorded": outcome == OUTCOME_NOT_RECORDED,
            "post_invocation_command_execution_boundary_requires_additional_basis": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "post_invocation_command_execution_boundary_blocked": outcome == OUTCOME_BLOCKED,
            "post_invocation_command_execution_boundary_is_not_command_execution": True,
            "post_invocation_command_execution_boundary_is_not_command_output": True,
            "post_invocation_command_execution_boundary_is_not_command_result": True,
            "post_invocation_command_execution_boundary_is_not_command_success": True,
            "post_invocation_command_execution_boundary_is_not_execution_permission": True,
            "post_invocation_command_execution_boundary_is_not_execution_approval": True,
            "older_command_execution_boundary_lineage_is_not_current_execution": True,
        }
    )
    return statement


def _non_meaning() -> dict[str, bool]:
    names = (
        "command_executed",
        "command_output_exists",
        "command_result_exists",
        "command_success_exists",
        "execution_permission_exists",
        "execution_approval_exists",
        "authorization_token_reusable",
        "command_success_creates_currentness",
        "command_success_claims_final_completion",
        "command_output_becomes_source",
        "command_result_becomes_authority",
        "standing_execution_lane_exists",
        "repeat_execution_permission_exists",
        "standing_invocation_lane_exists",
        "repeat_invocation_permission_exists",
        "consumed_request_token_reopened",
        "v1_repaired_hidden_or_passed",
        "deployment_runtime_public_release",
        "public_readiness",
        "final_completion",
        "continuation",
        "reusable_permission",
        "derivative_reception",
        "vessel_relation",
        "another_reception_request",
        "follow_on_work",
    )
    return {f"post_invocation_command_execution_boundary_does_not_mean_{name}": True for name in names}


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "post_invocation_command_execution_boundary_test",
            "post_invocation_command_execution_boundary_live_artifact",
            "command_execution_step_if_separately_specified",
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
    unsupported = [value for value in values if value not in SUPPORTED_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_SCOPE_SET]
    return {
        "selected_scope_values": values,
        "supported_scope_values": list(SUPPORTED_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_SCOPE),
        "unsupported_scope_values": unsupported,
        "all_selected_scope_values_supported": bool(values) and not unsupported,
        "post_invocation_command_execution_boundary_only": "POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_ONLY" in values,
        "one_future_command_execution_step_only": "ONE_FUTURE_COMMAND_EXECUTION_STEP_ONLY" in values,
        "recorded_command_invocation_basis_preserved": outcome == OUTCOME_RECORDED,
        "authorization_token_spent_exactly_once_preserved": outcome == OUTCOME_RECORDED,
        "authorization_token_reuse_blocked": True,
        "command_execution_not_performed": True,
        "command_output_result_success_not_created": True,
        "execution_permission_not_created": True,
        "execution_approval_not_created": True,
        "no_standing_execution_lane": True,
        "no_repeat_execution_permission": True,
        "no_standing_invocation_lane": True,
        "no_repeat_invocation_permission": True,
        "execution_boundary_is_not_execution_output_result_success": True,
        "invocation_basis_is_not_execution_or_command_success": True,
        "consumed_request_token_remains_closed": True,
        "consumed_request_not_reopened": True,
        "v1_predecessor_failure_remains_visible": True,
        "v2_successor_does_not_repair_v1": True,
        "returned_result_containment_preserved": True,
        "reference_shaped_basis_required": True,
        "full_prior_artifact_body_not_emitted": True,
        "no_authority_currentness_final_completion_continuation_reusable_follow_on": True,
    }


def _counts(checks: Sequence[Mapping[str, Any]]) -> tuple[int, int]:
    passed = sum(1 for check in checks if check.get("passed") is True)
    return passed, len(checks) - passed


def build_portable_source_body_verification_post_invocation_command_execution_boundary_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Build a bounded summary for a post-invocation command execution boundary result."""

    statement = _mapping(result.get("post_invocation_command_execution_boundary_statement"))
    block = _mapping(result.get("block"))
    metadata = _mapping(result.get("portable_source_body_verification_post_invocation_command_execution_boundary_metadata"))
    question = _mapping(result.get("declared_post_invocation_command_execution_boundary_question"))
    non_claims = _mapping(result.get("non_claims"))
    checks = [check for check in result.get("post_invocation_command_execution_boundary_checks", []) if isinstance(check, Mapping)]
    passed, failed = _counts(checks)
    invocation = _mapping(result.get("selected_command_invocation_basis"))
    review = _mapping(result.get("selected_command_execution_review_basis"))
    consumption = _mapping(result.get("selected_request_consumption_basis"))
    v2 = _mapping(result.get("selected_v2_admitted_request_basis"))
    lineage = _mapping(result.get("selected_command_execution_boundary_lineage_basis"))
    outcome = result.get("outcome")
    return {
        "outcome": outcome,
        "block_code": block.get("code"),
        "block_reason": block.get("reason"),
        "request_id": metadata.get("post_invocation_command_execution_boundary_request_id"),
        "question": question.get("question"),
        "intent": question.get("intent"),
        "passed_check_count": passed,
        "failed_check_count": failed,
        "post_invocation_boundary_recorded": statement.get("post_invocation_command_execution_boundary_recorded") is True,
        "recorded_command_invocation_basis_preserved": statement.get("recorded_command_invocation_basis_preserved") is True,
        "one_future_command_execution_step_declared": statement.get("one_future_command_execution_step_declared") is True,
        "authorization_token_spent_exactly_once_preserved": statement.get("authorization_token_spent_exactly_once_preserved") is True,
        "authorization_token_reuse_blocked": statement.get("authorization_token_reuse_blocked") is True,
        "command_execution_still_not_performed": statement.get("command_execution_still_not_performed") is True,
        "command_output_result_success_still_not_created": all(statement.get(key) is True for key in ("command_output_still_not_created", "command_result_still_not_created", "command_success_still_not_created")),
        "execution_permission_not_created": statement.get("execution_permission_not_created") is True,
        "execution_approval_not_created": statement.get("execution_approval_not_created") is True,
        "consumed_request_token_remains_closed": statement.get("consumed_request_token_remains_closed") is True,
        "v1_predecessor_failure_preserved": statement.get("v1_predecessor_failure_preserved") is True,
        "returned_result_containment_preserved": statement.get("returned_result_containment_preserved") is True,
        "not_recorded": outcome == OUTCOME_NOT_RECORDED,
        "requires_additional_basis": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "selected_command_invocation_outcome": _find_first(invocation, ("outcome", "result_outcome")),
        "selected_command_invocation_failed_check_count": _find_first(invocation, ("failed_check_count", "selected_failed_check_count")),
        "selected_command_execution_review_outcome": _find_first(review, ("outcome", "result_outcome")),
        "selected_command_execution_review_failed_check_count": _find_first(review, ("failed_check_count", "selected_failed_check_count")),
        "selected_request_consumption_outcome": _find_first(consumption, ("outcome", "result_outcome")),
        "selected_request_consumption_failed_check_count": _find_first(consumption, ("failed_check_count", "selected_failed_check_count")),
        "selected_v2_admitted_request_outcome": _find_first(v2, ("outcome", "result_outcome")),
        "selected_v2_admitted_request_version": _find_first(v2, ("result_version", "version")),
        "selected_v2_admitted_request_failed_check_count": _find_first(v2, ("failed_check_count", "selected_failed_check_count")),
        "no_standing_repeat_execution_lane": all(non_claims.get(key) is False for key in ("standing_execution_lane_created", "repeat_execution_permission_created")),
        "no_standing_repeat_invocation_lane": all(non_claims.get(key) is False for key in ("standing_invocation_lane_created", "repeat_invocation_permission_created")),
        "older_command_execution_boundary_lineage_not_treated_as_current_execution": not _lineage_as_current_execution(lineage),
        "no_raw_full_prior_artifact_body": non_claims.get("raw_full_prior_artifact_body_returned") is False,
        "no_artifact_mutation": non_claims.get("prior_artifacts_mutated") is False,
        "no_deployment_runtime_public_release": all(non_claims.get(key) is False for key in ("deployment_created", "runtime_hosting_created", "public_release_created")),
        "no_operation_public_readiness_final_completion": all(non_claims.get(key) is False for key in ("operation_permission_created", "public_launch_readiness_created", "final_completion_claimed")),
        "no_continuation_publication_reusable_follow_on": all(non_claims.get(key) is False for key in ("continuation_authorized", "publication_flow_opened", "reusable_permission_created", "follow_on_work_authorized")),
        "key_non_claims": _sanitize_reference_shape(non_claims),
    }


def _metadata(request: Mapping[str, Any], outcome: str) -> dict[str, Any]:
    request_id = str(request.get("post_invocation_command_execution_boundary_request_id") or "undeclared")
    return {
        "portable_source_body_verification_post_invocation_command_execution_boundary_result_id": f"{request_id}__portable_source_body_verification_post_invocation_command_execution_boundary_result",
        "portable_source_body_verification_post_invocation_command_execution_boundary_result_type": RESULT_TYPE,
        "portable_source_body_verification_post_invocation_command_execution_boundary_result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
        "post_invocation_command_execution_boundary_request_id": request_id,
        "naming_containment": {
            "short_resolver_filename_used_intentionally": True,
            "short_filename_does_not_erase_upstream_lineage": True,
            "full_upstream_lineage_preserved_in_selected_basis": True,
            "post_invocation_filename_distinct_from_older_execution_boundary_surfaces": True,
        },
        "lineage_posture": {
            "downstream_of_recorded_command_invocation": True,
            "older_command_execution_boundary_surfaces_remain_lineage_only": True,
        },
        "requested_outcome": request.get("requested_post_invocation_command_execution_boundary_outcome"),
        "outcome": outcome,
    }


def _open_posture(outcome: str, request: Mapping[str, Any], checks: Sequence[Mapping[str, Any]]) -> tuple[dict, dict]:
    additional = {
        "requires_additional_basis": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "additional_basis_context": _sanitize_reference_shape(request.get("additional_basis_context") or {}),
        "missing_basis_not_scheduled": True,
        "missing_basis_not_authorized": True,
        "missing_basis_not_executed": True,
        "additional_basis_does_not_execute_command": True,
        "additional_basis_does_not_create_output_result_success": True,
        "additional_basis_does_not_create_execution_permission_or_approval": True,
        "additional_basis_does_not_create_follow_on_work": True,
    }
    not_recorded = {
        "not_recorded": outcome == OUTCOME_NOT_RECORDED,
        "not_recorded_basis": _sanitize_reference_shape(request.get("not_recorded_basis") or {}),
        "failed_checks": _sanitize_reference_shape([check for check in checks if not check.get("passed")] if outcome == OUTCOME_NOT_RECORDED else []),
        "not_recorded_does_not_mutate": True,
        "not_recorded_does_not_repair": True,
        "not_recorded_does_not_execute_command": True,
        "not_recorded_does_not_emit_output": True,
        "not_recorded_does_not_create_command_result": True,
        "not_recorded_does_not_create_command_success": True,
        "not_recorded_does_not_authorize_next_work": True,
    }
    return additional, not_recorded


def _build_result(request: Mapping[str, Any], *, checks: Sequence[Mapping[str, Any]], outcome: str, block_code: str | None, block_reason: str | None, request_path: str | None = None) -> dict[str, Any]:
    metadata = _metadata(request, outcome)
    if request_path:
        metadata["declared_post_invocation_command_execution_boundary_request_path"] = request_path
    statement = _statement(outcome)
    non_claims = _default_non_claims()
    additional, not_recorded = _open_posture(outcome, request, checks)
    result = {
        "portable_source_body_verification_post_invocation_command_execution_boundary_metadata": metadata,
        "declared_post_invocation_command_execution_boundary_question": {
            "question": request.get("post_invocation_command_execution_boundary_question"),
            "expected_question": CORE_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_QUESTION,
            "intent": request.get("post_invocation_command_execution_boundary_intent"),
            "post_invocation_command_execution_boundary_is_not_command_execution": True,
            "post_invocation_command_execution_boundary_is_not_command_output": True,
            "post_invocation_command_execution_boundary_is_not_command_result": True,
            "post_invocation_command_execution_boundary_is_not_command_success": True,
        },
        "selected_command_invocation_basis": _basis_section(request.get("selected_command_invocation_basis"), path=request.get("selected_command_invocation_result_path"), extra={"selected_result_id": request.get("selected_command_invocation_result_id"), "selected_result_outcome": request.get("selected_command_invocation_result_outcome"), "selected_failed_check_count": request.get("selected_command_invocation_failed_check_count"), "command_invocation_basis_remains_invocation_basis_only": True}),
        "selected_command_invocation_terminal_summary_basis": _basis_section(request.get("selected_command_invocation_terminal_summary_basis"), path=request.get("selected_command_invocation_terminal_summary_path"), extra={"terminal_summary_remains_readability_basis_only": True}),
        "selected_command_invocation_boundary_basis": _basis_section(request.get("selected_command_invocation_boundary_basis"), path=request.get("selected_command_invocation_boundary_result_path"), extra={"selected_result_id": request.get("selected_command_invocation_boundary_result_id"), "selected_result_outcome": request.get("selected_command_invocation_boundary_result_outcome"), "selected_failed_check_count": request.get("selected_command_invocation_boundary_failed_check_count"), "boundary_basis_remains_boundary_basis_only": True}),
        "selected_command_invocation_authorization_basis": _basis_section(request.get("selected_command_invocation_authorization_basis"), path=request.get("selected_command_invocation_authorization_result_path"), extra={"selected_result_id": request.get("selected_command_invocation_authorization_result_id"), "selected_result_outcome": request.get("selected_command_invocation_authorization_result_outcome"), "selected_failed_check_count": request.get("selected_command_invocation_authorization_failed_check_count"), "authorization_basis_remains_authorization_basis_only": True}),
        "selected_command_execution_review_basis": _basis_section(request.get("selected_command_execution_review_basis"), path=request.get("selected_command_execution_review_result_path"), extra={"selected_result_id": request.get("selected_command_execution_review_result_id"), "selected_result_outcome": request.get("selected_command_execution_review_result_outcome"), "selected_failed_check_count": request.get("selected_command_execution_review_failed_check_count"), "review_basis_remains_review_basis_only": True}),
        "selected_request_consumption_basis": _basis_section(request.get("selected_request_consumption_basis"), path=request.get("selected_request_consumption_result_path"), extra={"selected_result_id": request.get("selected_request_consumption_result_id"), "selected_result_outcome": request.get("selected_request_consumption_result_outcome"), "selected_failed_check_count": request.get("selected_request_consumption_failed_check_count"), "request_consumption_basis_only": True}),
        "selected_consumed_request_basis": _basis_section(request.get("selected_consumed_request_basis"), extra={"consumed_request_token_remains_closed": True, "consumed_request_not_reopened": True}),
        "selected_v2_admitted_request_basis": _basis_section(request.get("selected_v2_admitted_request_basis"), path=request.get("selected_v2_admitted_request_artifact_path"), extra={"selected_artifact_id": request.get("selected_v2_admitted_request_artifact_id"), "selected_outcome": request.get("selected_v2_admitted_request_outcome"), "selected_version": request.get("selected_v2_admitted_request_version"), "selected_failed_check_count": request.get("selected_v2_failed_check_count"), "selected_v2_successor_metadata": request.get("selected_v2_successor_metadata"), "v2_remains_lineage_evidence_only": True, "v2_does_not_claim_v1_passed": True}),
        "selected_v1_predecessor_failure_basis": _basis_section(request.get("selected_v1_predecessor_failure_basis"), path=request.get("selected_v1_predecessor_artifact_path"), extra={"selected_artifact_id": request.get("selected_v1_predecessor_artifact_id"), "selected_outcome": request.get("selected_v1_predecessor_outcome"), "v1_predecessor_failure_remains_visible": True, "v1_is_not_repaired": True, "v1_is_not_hidden": True, "v1_is_not_claimed_passed": True}),
        "selected_command_execution_boundary_lineage_basis": _basis_section(request.get("selected_command_execution_boundary_lineage_basis"), path=request.get("selected_command_execution_boundary_lineage_result_path"), extra={"older_command_execution_boundary_surfaces_remain_lineage_only": True, "lineage_basis_is_not_current_execution": True}),
        "selected_command_report_basis": _basis_section(request.get("selected_command_report_basis"), path=request.get("selected_command_report_path")),
        "selected_command_implementation_boundary_basis": _basis_section(request.get("selected_command_implementation_boundary_basis"), path=request.get("selected_command_implementation_boundary_result_path")),
        "selected_command_boundary_basis": _basis_section(request.get("selected_command_boundary_basis"), path=request.get("selected_command_boundary_result_path")),
        "selected_artifact_emission_containment_basis": _basis_section(request.get("selected_artifact_emission_containment_basis"), path=request.get("selected_artifact_emission_containment_result_path")),
        "selected_evidence_manifest_basis": _basis_section(request.get("selected_evidence_manifest_basis"), path=request.get("selected_evidence_manifest_result_path")),
        "selected_portable_verification_basis": _basis_section(request.get("selected_portable_verification_basis"), path=request.get("selected_portable_verification_result_path")),
        "post_invocation_execution_boundary_only_posture": _basis_section(request.get("post_invocation_execution_boundary_only_posture"), extra={"post_invocation_command_execution_boundary_only": True, "boundary_is_not_command_execution": True}),
        "one_future_command_execution_step_posture": _basis_section(request.get("one_future_command_execution_step_posture"), extra={"one_future_command_execution_step_declared": outcome == OUTCOME_RECORDED}),
        "invocation_basis_preserved_posture": _basis_section(request.get("invocation_basis_preserved_posture"), extra={"recorded_command_invocation_basis_preserved": outcome == OUTCOME_RECORDED}),
        "authorization_token_spent_exactly_once_posture": _basis_section(request.get("authorization_token_spent_exactly_once_posture"), extra={"authorization_token_spent_exactly_once_preserved": outcome == OUTCOME_RECORDED}),
        "authorization_token_reuse_blocked_posture": _basis_section(request.get("authorization_token_reuse_blocked_posture"), extra={"authorization_token_reuse_blocked": True, "authorization_token_reused": False}),
        "no_command_execution_posture": _basis_section(request.get("no_command_execution_posture"), extra={"command_execution_not_performed": True}),
        "no_output_result_success_posture": _basis_section(request.get("no_output_result_success_posture"), extra={"command_output_not_created": True, "command_result_not_created": True, "command_success_not_created": True}),
        "no_execution_permission_posture": _basis_section(request.get("no_execution_permission_posture"), extra={"execution_permission_not_created": True}),
        "no_execution_approval_posture": _basis_section(request.get("no_execution_approval_posture"), extra={"execution_approval_not_created": True}),
        "no_standing_execution_lane_posture": _basis_section(request.get("no_standing_execution_lane_posture"), extra={"standing_execution_lane_created": False}),
        "no_repeat_execution_permission_posture": _basis_section(request.get("no_repeat_execution_permission_posture"), extra={"repeat_execution_permission_created": False}),
        "no_standing_invocation_lane_posture": _basis_section(request.get("no_standing_invocation_lane_posture"), extra={"standing_invocation_lane_created": False}),
        "no_repeat_invocation_permission_posture": _basis_section(request.get("no_repeat_invocation_permission_posture"), extra={"repeat_invocation_permission_created": False}),
        "consumed_token_closed_posture": _basis_section(request.get("consumed_token_closed_posture"), extra={"consumed_request_token_remains_closed": True}),
        "no_reopen_consumed_request_posture": _basis_section(request.get("no_reopen_consumed_request_posture"), extra={"consumed_request_reopened": False}),
        "returned_result_containment_posture": _basis_section(request.get("returned_result_containment_posture"), extra={"returned_result_containment_preserved": True, "raw_full_prior_artifact_body_returned": False}),
        "post_invocation_command_execution_boundary_scope": _scope_section(request.get("post_invocation_command_execution_boundary_scope"), outcome),
        "post_invocation_command_execution_boundary_checks": _sanitize_reference_shape(list(checks)),
        "post_invocation_command_execution_boundary_statement": statement,
        "post_invocation_command_execution_boundary_non_meaning": _non_meaning(),
        "additional_basis_required": additional,
        "not_recorded_basis": not_recorded,
        "what_remains_open": _what_remains_open(),
        "non_claims": non_claims,
        "outcome": outcome,
        "block": {"code": block_code, "reason": block_reason},
    }
    result["portable_source_body_verification_post_invocation_command_execution_boundary_summary"] = build_portable_source_body_verification_post_invocation_command_execution_boundary_summary(result)
    return result


def resolve_portable_source_body_verification_post_invocation_command_execution_boundary(
    declared_post_invocation_command_execution_boundary_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one bounded post-invocation command execution boundary request."""

    if declared_post_invocation_command_execution_boundary_request is None:
        request: Mapping[str, Any] = {}
        checks = _build_checks(request)
        outcome, code, reason = _select_outcome(request, checks, "POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_QUESTION_UNDECLARED")
        return _build_result(request, checks=checks, outcome=outcome, block_code=code, block_reason=reason)
    if not isinstance(declared_post_invocation_command_execution_boundary_request, Mapping):
        request = {}
        checks = _build_checks(request, malformed=True)
        outcome, code, reason = _select_outcome(request, checks, "DECLARED_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_REQUEST_MALFORMED")
        return _build_result(request, checks=checks, outcome=outcome, block_code=code, block_reason=reason)
    request = _deepcopy(declared_post_invocation_command_execution_boundary_request)
    checks = _build_checks(request)
    outcome, code, reason = _select_outcome(request, checks)
    return _build_result(request, checks=checks, outcome=outcome, block_code=code, block_reason=reason)


def resolve_portable_source_body_verification_post_invocation_command_execution_boundary_from_path(
    declared_post_invocation_command_execution_boundary_request_path: Path | str,
) -> dict:
    """Resolve one post-invocation boundary request loaded from a JSON object path."""

    path = Path(declared_post_invocation_command_execution_boundary_request_path)
    try:
        loaded = json.loads(path.read_text(encoding="utf-8"))
    except OSError:
        request = {"post_invocation_command_execution_boundary_request_id": "unreadable_path"}
        checks = _build_checks(request)
        outcome, code, reason = _select_outcome(request, checks, "DECLARED_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_REQUEST_UNREADABLE")
        return _build_result(request, checks=checks, outcome=outcome, block_code=code, block_reason=reason, request_path=str(path))
    except json.JSONDecodeError:
        request = {"post_invocation_command_execution_boundary_request_id": "malformed_json"}
        checks = _build_checks(request)
        outcome, code, reason = _select_outcome(request, checks, "DECLARED_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_REQUEST_MALFORMED")
        return _build_result(request, checks=checks, outcome=outcome, block_code=code, block_reason=reason, request_path=str(path))
    if not isinstance(loaded, Mapping):
        request = {"post_invocation_command_execution_boundary_request_id": "non_object_json"}
        checks = _build_checks(request, malformed=True)
        outcome, code, reason = _select_outcome(request, checks, "DECLARED_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_REQUEST_MALFORMED")
        return _build_result(request, checks=checks, outcome=outcome, block_code=code, block_reason=reason, request_path=str(path))
    request = _deepcopy(loaded)
    checks = _build_checks(request)
    outcome, code, reason = _select_outcome(request, checks)
    return _build_result(request, checks=checks, outcome=outcome, block_code=code, block_reason=reason, request_path=str(path))


def _deduplicated_output_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 1000000):
        candidate = path.parent / f"{path.stem}_{index:03d}{path.suffix}"
        if not candidate.exists():
            return candidate
    raise PortableSourceBodyVerificationPostInvocationCommandExecutionBoundaryError(
        "unable to allocate non-overwriting post-invocation boundary result path"
    )


def write_portable_source_body_verification_post_invocation_command_execution_boundary_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write a post-invocation boundary result JSON without silently overwriting."""

    if output_path is None:
        metadata = _mapping(result.get("portable_source_body_verification_post_invocation_command_execution_boundary_metadata"))
        request_id = metadata.get("post_invocation_command_execution_boundary_request_id") or "undeclared_post_invocation_command_execution_boundary_request"
        filename = f"{_safe_component(request_id, 'undeclared_post_invocation_command_execution_boundary_request')}__portable_source_body_verification_post_invocation_command_execution_boundary_result.json"
        path = PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_ROOT / filename
    else:
        path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    final_path = _deduplicated_output_path(path)
    final_path.write_text(json.dumps(_sanitize_reference_shape(dict(result)), indent=2, sort_keys=True, ensure_ascii=True) + "\n", encoding="utf-8")
    return final_path


def build_declared_portable_source_body_verification_post_invocation_command_execution_boundary_request(
    post_invocation_command_execution_boundary_request_id: str,
    post_invocation_command_execution_boundary_question: str,
    selected_command_invocation_basis: Mapping[str, Any] | str,
    selected_command_invocation_terminal_summary_basis: Mapping[str, Any] | str,
    selected_command_invocation_boundary_basis: Mapping[str, Any] | str,
    selected_command_invocation_authorization_basis: Mapping[str, Any] | str,
    selected_command_execution_review_basis: Mapping[str, Any] | str,
    selected_request_consumption_basis: Mapping[str, Any] | str,
    selected_consumed_request_basis: Mapping[str, Any] | str,
    selected_v2_admitted_request_basis: Mapping[str, Any] | str,
    selected_v1_predecessor_failure_basis: Mapping[str, Any] | str,
    selected_command_execution_boundary_lineage_basis: Mapping[str, Any] | str,
    selected_command_report_basis: Mapping[str, Any] | str,
    selected_command_implementation_boundary_basis: Mapping[str, Any] | str,
    selected_command_boundary_basis: Mapping[str, Any] | str,
    selected_artifact_emission_containment_basis: Mapping[str, Any] | str,
    selected_evidence_manifest_basis: Mapping[str, Any] | str,
    selected_portable_verification_basis: Mapping[str, Any] | str,
    post_invocation_execution_boundary_only_posture: Mapping[str, Any] | str,
    one_future_command_execution_step_posture: Mapping[str, Any] | str,
    invocation_basis_preserved_posture: Mapping[str, Any] | str,
    authorization_token_spent_exactly_once_posture: Mapping[str, Any] | str,
    authorization_token_reuse_blocked_posture: Mapping[str, Any] | str,
    no_command_execution_posture: Mapping[str, Any] | str,
    no_output_result_success_posture: Mapping[str, Any] | str,
    no_execution_permission_posture: Mapping[str, Any] | str,
    no_execution_approval_posture: Mapping[str, Any] | str,
    no_standing_execution_lane_posture: Mapping[str, Any] | str,
    no_repeat_execution_permission_posture: Mapping[str, Any] | str,
    no_standing_invocation_lane_posture: Mapping[str, Any] | str,
    no_repeat_invocation_permission_posture: Mapping[str, Any] | str,
    consumed_token_closed_posture: Mapping[str, Any] | str,
    no_reopen_consumed_request_posture: Mapping[str, Any] | str,
    returned_result_containment_posture: Mapping[str, Any] | str,
    post_invocation_command_execution_boundary_scope: Sequence[str] | Mapping[str, Any],
    post_invocation_command_execution_boundary_intent: str = INTENT_RECORD,
    **optional_fields: Any,
) -> dict:
    """Build a declared request with explicit false non-claims and no execution inference."""

    request = {
        "post_invocation_command_execution_boundary_request_id": post_invocation_command_execution_boundary_request_id,
        "post_invocation_command_execution_boundary_question": post_invocation_command_execution_boundary_question,
        "post_invocation_command_execution_boundary_intent": post_invocation_command_execution_boundary_intent,
        "selected_command_invocation_basis": _deepcopy(selected_command_invocation_basis),
        "selected_command_invocation_terminal_summary_basis": _deepcopy(selected_command_invocation_terminal_summary_basis),
        "selected_command_invocation_boundary_basis": _deepcopy(selected_command_invocation_boundary_basis),
        "selected_command_invocation_authorization_basis": _deepcopy(selected_command_invocation_authorization_basis),
        "selected_command_execution_review_basis": _deepcopy(selected_command_execution_review_basis),
        "selected_request_consumption_basis": _deepcopy(selected_request_consumption_basis),
        "selected_consumed_request_basis": _deepcopy(selected_consumed_request_basis),
        "selected_v2_admitted_request_basis": _deepcopy(selected_v2_admitted_request_basis),
        "selected_v1_predecessor_failure_basis": _deepcopy(selected_v1_predecessor_failure_basis),
        "selected_command_execution_boundary_lineage_basis": _deepcopy(selected_command_execution_boundary_lineage_basis),
        "selected_command_report_basis": _deepcopy(selected_command_report_basis),
        "selected_command_implementation_boundary_basis": _deepcopy(selected_command_implementation_boundary_basis),
        "selected_command_boundary_basis": _deepcopy(selected_command_boundary_basis),
        "selected_artifact_emission_containment_basis": _deepcopy(selected_artifact_emission_containment_basis),
        "selected_evidence_manifest_basis": _deepcopy(selected_evidence_manifest_basis),
        "selected_portable_verification_basis": _deepcopy(selected_portable_verification_basis),
        "post_invocation_execution_boundary_only_posture": _deepcopy(post_invocation_execution_boundary_only_posture),
        "one_future_command_execution_step_posture": _deepcopy(one_future_command_execution_step_posture),
        "invocation_basis_preserved_posture": _deepcopy(invocation_basis_preserved_posture),
        "authorization_token_spent_exactly_once_posture": _deepcopy(authorization_token_spent_exactly_once_posture),
        "authorization_token_reuse_blocked_posture": _deepcopy(authorization_token_reuse_blocked_posture),
        "no_command_execution_posture": _deepcopy(no_command_execution_posture),
        "no_output_result_success_posture": _deepcopy(no_output_result_success_posture),
        "no_execution_permission_posture": _deepcopy(no_execution_permission_posture),
        "no_execution_approval_posture": _deepcopy(no_execution_approval_posture),
        "no_standing_execution_lane_posture": _deepcopy(no_standing_execution_lane_posture),
        "no_repeat_execution_permission_posture": _deepcopy(no_repeat_execution_permission_posture),
        "no_standing_invocation_lane_posture": _deepcopy(no_standing_invocation_lane_posture),
        "no_repeat_invocation_permission_posture": _deepcopy(no_repeat_invocation_permission_posture),
        "consumed_token_closed_posture": _deepcopy(consumed_token_closed_posture),
        "no_reopen_consumed_request_posture": _deepcopy(no_reopen_consumed_request_posture),
        "returned_result_containment_posture": _deepcopy(returned_result_containment_posture),
        "post_invocation_command_execution_boundary_scope": _deepcopy(post_invocation_command_execution_boundary_scope),
        "requested_post_invocation_command_execution_boundary_outcome": optional_fields.pop("requested_post_invocation_command_execution_boundary_outcome", OUTCOME_RECORDED),
        "declared_non_claims": _default_non_claims(),
    }
    for key, value in optional_fields.items():
        if value is not None:
            request[key] = _deepcopy(value)
    return request
