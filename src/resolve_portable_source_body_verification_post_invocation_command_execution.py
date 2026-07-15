"""Bounded portable source-body verification post-invocation command execution.

This module records one declared post-invocation command execution event only.
It is downstream of recorded command invocation and the post-invocation command
execution boundary. It does not run a shell command, spawn a subprocess, invoke
Python modules, call external APIs, perform network work, create command output,
create command result, create command success, create execution permission,
create execution approval, create a standing execution lane, or create repeat
execution permission.

Execution trace, when present, is audit-only. It is not command output, command
result, command success, source, authority, currentness, or final completion.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class PortableSourceBodyVerificationPostInvocationCommandExecutionError(Exception):
    """Raised for hard post-invocation command execution resolver failures."""


RESOLVER_MODULE = "resolve_portable_source_body_verification_post_invocation_command_execution"
RESULT_VERSION = "0.1.0"
RESULT_TYPE = "portable_source_body_verification_post_invocation_command_execution_result"

PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_post_invocation_command_execution"
)
OUTPUT_ROOT = PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_ROOT

CORE_POST_INVOCATION_COMMAND_EXECUTION_QUESTION = (
    "Can the recorded post-invocation command execution boundary basis be used to perform one "
    "bounded command execution event without creating command output, command result, command "
    "success, execution permission, execution approval, standing execution lane, repeat execution "
    "permission, source, authority, currentness, final completion, continuation, reusable "
    "permission, derivative reception, vessel relation, another reception request, or follow-on work?"
)

INTENT_RECORD = "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION"
INTENT_BLOCK = "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION"
SUPPORTED_INTENTS = frozenset({INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK})

OUTCOME_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_RECORDED"
OUTCOME_NOT_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_BLOCKED"
OUTCOME_FAMILY = frozenset(
    {
        OUTCOME_RECORDED,
        OUTCOME_NOT_RECORDED,
        OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        OUTCOME_BLOCKED,
    }
)

POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_RECORDED"
)
COMMAND_INVOCATION_OUTCOME = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_INVOCATION_RECORDED"
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

SUPPORTED_POST_INVOCATION_COMMAND_EXECUTION_SCOPE = (
    "POST_INVOCATION_COMMAND_EXECUTION_ONLY",
    "ONE_BOUNDED_COMMAND_EXECUTION_EVENT_RECORDED",
    "EXECUTION_TRACE_IS_AUDIT_ONLY",
    "COMMAND_OUTPUT_NOT_CREATED",
    "COMMAND_RESULT_NOT_CREATED",
    "COMMAND_SUCCESS_NOT_CREATED",
    "EXECUTION_PERMISSION_NOT_CREATED",
    "EXECUTION_APPROVAL_NOT_CREATED",
    "NO_STANDING_EXECUTION_LANE_CREATED",
    "NO_REPEAT_EXECUTION_PERMISSION_CREATED",
    "AUTHORIZATION_TOKEN_REUSE_BLOCKED",
    "CONSUMED_REQUEST_TOKEN_REMAINS_CLOSED",
    "CONSUMED_REQUEST_NOT_REOPENED",
    "EXECUTION_IS_NOT_COMMAND_OUTPUT",
    "EXECUTION_IS_NOT_COMMAND_RESULT",
    "EXECUTION_IS_NOT_COMMAND_SUCCESS",
    "EXECUTION_TRACE_IS_NOT_OUTPUT",
    "EXECUTION_TRACE_IS_NOT_RESULT",
    "EXECUTION_TRACE_IS_NOT_SUCCESS",
    "EXECUTION_TRACE_IS_NOT_SOURCE",
    "EXECUTION_TRACE_IS_NOT_AUTHORITY",
    "NO_AUTHORITY_CREATED",
    "NO_CURRENTNESS_CREATED",
    "NO_FINAL_COMPLETION",
    "NO_CONTINUATION_AUTHORIZED",
    "NO_REUSABLE_PERMISSION",
    "NO_FOLLOW_ON_WORK_AUTHORIZED",
    "V1_PREDECESSOR_FAILURE_REMAINS_VISIBLE",
    "V2_SUCCESSOR_DOES_NOT_REPAIR_V1",
    "RETURNED_RESULT_CONTAINMENT_PRESERVED",
    "REFERENCE_SHAPED_BASIS_REQUIRED",
    "FULL_PRIOR_ARTIFACT_BODY_NOT_EMITTED",
)
SUPPORTED_POST_INVOCATION_COMMAND_EXECUTION_SCOPE_SET = frozenset(
    SUPPORTED_POST_INVOCATION_COMMAND_EXECUTION_SCOPE
)

REQUIRED_FALSE_NON_CLAIMS = (
    "command_output_created",
    "command_result_created",
    "command_success_created",
    "execution_permission_created",
    "execution_approval_created",
    "standing_execution_lane_created",
    "repeat_execution_permission_created",
    "authorization_token_reused",
    "consumed_request_reopened",
    "execution_treated_as_output",
    "execution_treated_as_result",
    "execution_treated_as_success",
    "execution_trace_treated_as_output",
    "execution_trace_treated_as_result",
    "execution_trace_treated_as_success",
    "execution_trace_treated_as_source",
    "execution_trace_treated_as_authority",
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
    "post_invocation_command_execution_recorded",
    "bounded_command_execution_event_recorded",
    "execution_trace_recorded_as_audit_only",
    "command_output_still_not_created",
    "command_result_still_not_created",
    "command_success_still_not_created",
    "execution_permission_not_created",
    "execution_approval_not_created",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
    "v1_predecessor_failure_preserved",
    "returned_result_containment_preserved",
)

FORBIDDEN_FULL_BODY_KEYS = frozenset(
    {
        "artifact_body",
        "command_output_body",
        "command_result_body",
        "command_success_body",
        "full_artifact_body",
        "full_prior_artifact_body",
        "full_prior_artifacts",
        "full_result",
        "prior_artifact_body",
        "raw_full_artifact_body",
        "raw_full_prior_artifact_body",
        "raw_full_result",
        "raw_result",
        "result_body",
        "success_body",
    }
)
FULL_BODY_OMISSION_MARKER = "[omitted: full prior artifact body is not returned]"

FORBIDDEN_EXECUTION_TRACE_BODY_KEYS = frozenset(
    {
        "stdout",
        "stderr",
        "stdin",
        "output",
        "process_output",
        "shell_output",
        "command_output",
        "command_output_body",
        "command_result",
        "command_result_body",
        "command_success",
        "command_success_body",
        "result_body",
        "success_body",
    }
)
EXECUTION_TRACE_BODY_OMISSION_MARKER = "[omitted: execution trace is audit-only]"

BLOCK_CODES = frozenset(
    {
        "DECLARED_POST_INVOCATION_COMMAND_EXECUTION_REQUEST_MALFORMED",
        "DECLARED_POST_INVOCATION_COMMAND_EXECUTION_REQUEST_UNREADABLE",
        "POST_INVOCATION_COMMAND_EXECUTION_QUESTION_UNDECLARED",
        "POST_INVOCATION_COMMAND_EXECUTION_INTENT_UNSUPPORTED",
        "POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_BASIS_MISSING",
        "POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_NOT_RECORDED",
        "POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_FAILED_CHECKS_PRESENT",
        "POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_STEP_NOT_DECLARED",
        "COMMAND_INVOCATION_BASIS_MISSING",
        "COMMAND_INVOCATION_NOT_RECORDED",
        "COMMAND_INVOCATION_FAILED_CHECKS_PRESENT",
        "COMMAND_INVOCATION_EVENT_NOT_RECORDED",
        "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_NOT_SPENT_EXACTLY_ONCE",
        "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_REUSE_NOT_BLOCKED",
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
        "OLDER_COMMAND_EXECUTION_BOUNDARY_LINEAGE_TREATED_AS_CURRENT_EXECUTION",
        "COMMAND_REPORT_BASIS_MISSING",
        "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING",
        "COMMAND_BOUNDARY_BASIS_MISSING",
        "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING",
        "EVIDENCE_MANIFEST_BASIS_MISSING",
        "PORTABLE_VERIFICATION_BASIS_MISSING",
        "POST_INVOCATION_COMMAND_EXECUTION_ONLY_POSTURE_MISSING",
        "ONE_BOUNDED_COMMAND_EXECUTION_EVENT_POSTURE_MISSING",
        "EXECUTION_TRACE_AUDIT_ONLY_POSTURE_MISSING",
        "NO_COMMAND_OUTPUT_POSTURE_MISSING",
        "NO_COMMAND_RESULT_POSTURE_MISSING",
        "NO_COMMAND_SUCCESS_POSTURE_MISSING",
        "NO_STANDING_EXECUTION_LANE_POSTURE_MISSING",
        "NO_REPEAT_EXECUTION_PERMISSION_POSTURE_MISSING",
        "UNSUPPORTED_POST_INVOCATION_COMMAND_EXECUTION_SCOPE",
        "COMMAND_OUTPUT_CREATED",
        "COMMAND_RESULT_CREATED",
        "COMMAND_SUCCESS_CREATED",
        "EXECUTION_PERMISSION_CREATED",
        "EXECUTION_APPROVAL_CREATED",
        "STANDING_EXECUTION_LANE_CREATED",
        "REPEAT_EXECUTION_PERMISSION_CREATED",
        "AUTHORIZATION_TOKEN_REUSED",
        "CONSUMED_REQUEST_REOPENED",
        "EXECUTION_TREATED_AS_OUTPUT",
        "EXECUTION_TREATED_AS_RESULT",
        "EXECUTION_TREATED_AS_SUCCESS",
        "EXECUTION_TRACE_TREATED_AS_OUTPUT",
        "EXECUTION_TRACE_TREATED_AS_RESULT",
        "EXECUTION_TRACE_TREATED_AS_SUCCESS",
        "EXECUTION_TRACE_TREATED_AS_SOURCE",
        "EXECUTION_TRACE_TREATED_AS_AUTHORITY",
        "COMMAND_OUTPUT_TREATED_AS_SOURCE",
        "COMMAND_RESULT_TREATED_AS_AUTHORITY",
        "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS",
        "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION",
        "FULL_PRIOR_ARTIFACT_BODY_EMITTED",
        "ARTIFACTS_MUTATED",
        "DEPLOYMENT_CREATED",
        "RUNTIME_HOSTING_CREATED",
        "PUBLIC_RELEASE_CREATED",
        "OPERATION_CREATED",
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
        "REAL_COMMAND_EXECUTION_ATTEMPTED",
        "POST_INVOCATION_COMMAND_EXECUTION_BLOCKED_BY_REQUEST",
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


def _contains_forbidden_key(value: Any, forbidden_keys: frozenset[str]) -> bool:
    if isinstance(value, Mapping):
        for key, item in value.items():
            if str(key) in forbidden_keys:
                return True
            if _contains_forbidden_key(item, forbidden_keys):
                return True
    elif isinstance(value, list):
        return any(_contains_forbidden_key(item, forbidden_keys) for item in value)
    return False


def _contains_forbidden_full_body_key(value: Any) -> bool:
    return _contains_forbidden_key(value, FORBIDDEN_FULL_BODY_KEYS)


def _contains_forbidden_execution_trace_body_key(value: Any) -> bool:
    return _contains_forbidden_key(value, FORBIDDEN_EXECUTION_TRACE_BODY_KEYS)


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


def _sanitize_execution_trace(value: Any) -> Any:
    if isinstance(value, Mapping):
        sanitized: dict[str, Any] = {}
        for key, item in value.items():
            key_text = str(key)
            if key_text in FORBIDDEN_FULL_BODY_KEYS:
                sanitized[key_text] = FULL_BODY_OMISSION_MARKER
            elif key_text in FORBIDDEN_EXECUTION_TRACE_BODY_KEYS:
                sanitized[key_text] = EXECUTION_TRACE_BODY_OMISSION_MARKER
            else:
                sanitized[key_text] = _sanitize_execution_trace(item)
        return sanitized
    if isinstance(value, list):
        return [_sanitize_execution_trace(item) for item in value]
    return _deepcopy(value)


def _mapping(value: Any) -> Mapping[str, Any]:
    if isinstance(value, Mapping):
        return value
    return {}


def _declared(value: Any) -> bool:
    return isinstance(value, Mapping) and bool(value)


def _basis_section(
    value: Any,
    *,
    path: str | None = None,
    extra: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
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


def _truthy(mapping: Mapping[str, Any], keys: Sequence[str]) -> bool:
    for key in keys:
        if _find_first(mapping, (key,)) is True:
            return True
    return False


def _outcome(
    basis: Mapping[str, Any],
    request: Mapping[str, Any],
    request_keys: Sequence[str],
) -> Any:
    for key in request_keys:
        if key in request:
            return request[key]
    return _find_first(basis, ("outcome", "result_outcome", "selected_outcome", "selected_result_outcome"))


def _failed_count(
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


def _version(
    basis: Mapping[str, Any],
    request: Mapping[str, Any],
    request_keys: Sequence[str],
) -> Any:
    for key in request_keys:
        if key in request:
            return request[key]
    return _find_first(basis, ("result_version", "version", "selected_version", "artifact_version"))


def _posture_declared(value: Any, keys: Sequence[str] = ()) -> bool:
    if not _present(value):
        return False
    posture = _mapping(value)
    if not posture:
        return True
    if posture.get("declared") is False or posture.get("posture_declared") is False:
        return False
    if not keys:
        return True
    return (
        _truthy(posture, keys)
        or posture.get("declared") is True
        or posture.get("posture_declared") is True
        or posture.get("basis_remains_basis_only") is True
    )


def _scope_values(scope: Any) -> list[str]:
    if isinstance(scope, Mapping):
        values = scope.get("selected_scope_values", scope.get("scope_values", scope.get("values")))
        if values is None:
            values = [key for key, item in scope.items() if item is True]
    else:
        values = scope
    if isinstance(values, str):
        return [values]
    if isinstance(values, Sequence) and not isinstance(values, (str, bytes, bytearray)):
        return [str(value) for value in values]
    return []


def _supported_scope(scope: Any) -> bool:
    values = _scope_values(scope)
    return bool(values) and all(value in SUPPORTED_POST_INVOCATION_COMMAND_EXECUTION_SCOPE_SET for value in values)


def _default_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _declared_non_claims(request: Mapping[str, Any]) -> Mapping[str, Any]:
    value = request.get("declared_non_claims")
    if isinstance(value, Mapping):
        return value
    return {}


def _first_non_claim_failure(request: Mapping[str, Any]) -> str | None:
    declared = _declared_non_claims(request)
    for key in REQUIRED_FALSE_NON_CLAIMS:
        if key not in declared or declared.get(key) is not False:
            return key
    return None


def _boundary_step_declared(boundary: Mapping[str, Any], request: Mapping[str, Any]) -> bool:
    if "selected_post_invocation_command_execution_boundary_step_declared" in request:
        return request["selected_post_invocation_command_execution_boundary_step_declared"] is True
    return _truthy(
        boundary,
        (
            "one_future_command_execution_step_declared",
            "one_future_command_execution_step_posture_declared",
            "one_future_command_execution_step_only",
            "one_future_command_execution_step_preserved",
        ),
    )


def _command_invocation_event_recorded(invocation: Mapping[str, Any], request: Mapping[str, Any]) -> bool:
    if "selected_command_invocation_event_recorded" in request:
        return request["selected_command_invocation_event_recorded"] is True
    return _truthy(
        invocation,
        (
            "bounded_command_invocation_event_recorded",
            "command_invocation_recorded",
            "command_invocation_event_recorded",
        ),
    )


def _token_spent_exactly_once(invocation: Mapping[str, Any], request: Mapping[str, Any]) -> bool:
    if "selected_command_invocation_authorization_token_spent_exactly_once" in request:
        return request["selected_command_invocation_authorization_token_spent_exactly_once"] is True
    return _truthy(
        invocation,
        (
            "authorization_token_spent_exactly_once",
            "authorization_token_spent_exactly_once_preserved",
            "one_shot_authorization_token_spent_exactly_once",
        ),
    )


def _authorization_token_reused(value: Mapping[str, Any]) -> bool:
    return _truthy(
        value,
        (
            "authorization_token_reused",
            "authorization_token_reuse_created",
            "authorization_token_reuse_permitted",
            "command_invocation_authorization_token_reused",
        ),
    )


def _token_reuse_blocked(invocation: Mapping[str, Any], request: Mapping[str, Any]) -> bool:
    if "selected_command_invocation_authorization_token_reuse_blocked" in request:
        return request["selected_command_invocation_authorization_token_reuse_blocked"] is True
    return (
        _truthy(
            invocation,
            (
                "authorization_token_reuse_blocked",
                "authorization_token_reuse_not_created",
                "authorization_token_not_reused",
                "authorization_token_reuse_blocked_preserved",
            ),
        )
        and not _authorization_token_reused(invocation)
    )


def _successor_metadata_preserved(v2_basis: Mapping[str, Any], request: Mapping[str, Any]) -> bool:
    explicit = request.get("selected_v2_successor_metadata")
    if isinstance(explicit, Mapping) and explicit:
        return True
    successor_of = _find_first(v2_basis, ("successor_of", "predecessor_resolver_module"))
    successor_reason = _find_first(v2_basis, ("successor_reason", "successor_transition_reason"))
    resolver_module = _find_first(v2_basis, ("resolver_module",))
    if successor_of and successor_reason and resolver_module:
        return True
    return _truthy(
        v2_basis,
        ("successor_metadata_preserved", "v2_successor_metadata_preserved", "successor_metadata_declared"),
    )


def _returned_result_containment_preserved(value: Mapping[str, Any]) -> bool:
    return _truthy(
        value,
        (
            "returned_result_containment_preserved",
            "returned_result_containment_posture_preserved",
            "returned_result_containment_declared",
            "no_raw_full_prior_artifact_body_returned",
        ),
    )


def _consumed_token_closed(consumed: Mapping[str, Any]) -> bool:
    return _truthy(
        consumed,
        (
            "consumed_request_token_remains_closed",
            "consumption_token_closed",
            "consumed_token_closed",
            "token_closed",
        ),
    )


def _consumed_not_reopened(consumed: Mapping[str, Any]) -> bool:
    if _truthy(consumed, ("consumed_request_reopened", "request_reopened", "token_reopened")):
        return False
    return _truthy(
        consumed,
        (
            "consumed_request_is_not_reopened",
            "consumed_request_not_reopened",
            "no_reopen_consumed_request",
            "request_not_reopened",
        ),
    )


def _v1_failure_visible(v1_basis: Mapping[str, Any]) -> bool:
    return _truthy(
        v1_basis,
        (
            "v1_predecessor_failure_remains_visible",
            "v1_remains_visible_predecessor_failure_evidence",
            "visible_predecessor_failure_evidence",
            "v1_predecessor_failure_basis_declared",
        ),
    )


def _lineage_as_current_execution(lineage: Mapping[str, Any]) -> bool:
    return _truthy(
        lineage,
        (
            "older_command_execution_boundary_lineage_treated_as_current_execution",
            "command_execution_boundary_lineage_basis_treated_as_current_execution",
            "lineage_basis_treated_as_current_execution",
            "current_execution",
            "command_execution_performed",
        ),
    )


def _reference_shaped_inputs_preserved(request: Mapping[str, Any]) -> bool:
    explicit = request.get("reference_shaped_input_posture")
    if isinstance(explicit, Mapping):
        if explicit.get("reference_shaped_input_posture_declared") is True:
            return True
        if explicit.get("reference_shaped_basis_required") is True:
            return True
    selected_keys = (
        "selected_post_invocation_command_execution_boundary_basis",
        "selected_post_invocation_command_execution_boundary_terminal_summary_basis",
        "selected_command_invocation_basis",
        "selected_command_invocation_terminal_summary_basis",
        "selected_command_execution_review_basis",
        "selected_request_consumption_basis",
        "selected_consumed_request_basis",
        "selected_v2_admitted_request_basis",
        "selected_v1_predecessor_failure_basis",
        "selected_older_command_execution_boundary_lineage_basis",
        "selected_command_report_basis",
        "selected_command_implementation_boundary_basis",
        "selected_command_boundary_basis",
        "selected_artifact_emission_containment_basis",
        "selected_evidence_manifest_basis",
        "selected_portable_verification_basis",
    )
    declared_mappings = [_mapping(request.get(key)) for key in selected_keys if _declared(request.get(key))]
    if not declared_mappings:
        return False
    return all(
        _truthy(
            basis,
            (
                "reference_shaped_basis",
                "basis_remains_reference_shaped",
                "basis_reference_shape_preserved",
                "basis_remains_basis_only",
            ),
        )
        for basis in declared_mappings
    )


def _execution_trace_audit_only(request: Mapping[str, Any]) -> bool:
    trace = request.get("execution_trace")
    if _contains_forbidden_execution_trace_body_key(trace):
        return False
    if trace is None:
        return True
    if isinstance(trace, Mapping):
        if _truthy(
            trace,
            (
                "execution_trace_treated_as_output",
                "execution_trace_treated_as_result",
                "execution_trace_treated_as_success",
                "execution_trace_treated_as_source",
                "execution_trace_treated_as_authority",
            ),
        ):
            return False
        return (
            _truthy(
                trace,
                (
                    "execution_trace_recorded_as_audit_only",
                    "execution_trace_audit_only",
                    "trace_is_audit_only",
                    "trace_is_not_output",
                ),
            )
            or trace.get("trace_type") == "EXECUTION_TRACE_AUDIT_ONLY"
        )
    return isinstance(trace, str) and bool(trace.strip())


COLLAPSE_TRUE_BLOCKS = (
    ("command_output_created", "COMMAND_OUTPUT_CREATED"),
    ("command_result_created", "COMMAND_RESULT_CREATED"),
    ("command_success_created", "COMMAND_SUCCESS_CREATED"),
    ("execution_permission_created", "EXECUTION_PERMISSION_CREATED"),
    ("execution_approval_created", "EXECUTION_APPROVAL_CREATED"),
    ("standing_execution_lane_created", "STANDING_EXECUTION_LANE_CREATED"),
    ("repeat_execution_permission_created", "REPEAT_EXECUTION_PERMISSION_CREATED"),
    ("authorization_token_reused", "AUTHORIZATION_TOKEN_REUSED"),
    ("authorization_token_reuse_created", "AUTHORIZATION_TOKEN_REUSED"),
    ("authorization_token_reuse_permitted", "AUTHORIZATION_TOKEN_REUSED"),
    ("consumed_request_reopened", "CONSUMED_REQUEST_REOPENED"),
    ("execution_treated_as_output", "EXECUTION_TREATED_AS_OUTPUT"),
    ("execution_treated_as_result", "EXECUTION_TREATED_AS_RESULT"),
    ("execution_treated_as_success", "EXECUTION_TREATED_AS_SUCCESS"),
    ("execution_trace_treated_as_output", "EXECUTION_TRACE_TREATED_AS_OUTPUT"),
    ("execution_trace_treated_as_result", "EXECUTION_TRACE_TREATED_AS_RESULT"),
    ("execution_trace_treated_as_success", "EXECUTION_TRACE_TREATED_AS_SUCCESS"),
    ("execution_trace_treated_as_source", "EXECUTION_TRACE_TREATED_AS_SOURCE"),
    ("execution_trace_treated_as_authority", "EXECUTION_TRACE_TREATED_AS_AUTHORITY"),
    ("command_output_became_source", "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
    ("command_result_became_authority", "COMMAND_RESULT_TREATED_AS_AUTHORITY"),
    ("command_success_created_currentness", "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
    ("command_success_claimed_final_completion", "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
    ("prior_artifacts_mutated", "ARTIFACTS_MUTATED"),
    ("artifacts_mutated", "ARTIFACTS_MUTATED"),
    ("deployment_created", "DEPLOYMENT_CREATED"),
    ("runtime_hosting_created", "RUNTIME_HOSTING_CREATED"),
    ("public_release_created", "PUBLIC_RELEASE_CREATED"),
    ("operation_created", "OPERATION_CREATED"),
    ("operation_permission_created", "OPERATION_CREATED"),
    ("public_launch_readiness_created", "PUBLIC_READINESS_CREATED"),
    ("public_readiness_created", "PUBLIC_READINESS_CREATED"),
    ("final_completion_claimed", "FINAL_COMPLETION_CLAIMED"),
    ("continuation_authorized", "CONTINUATION_AUTHORIZED"),
    ("reusable_permission_created", "REUSABLE_PERMISSION_CREATED"),
    ("derivative_reception_authorized", "DERIVATIVE_RECEPTION_AUTHORIZED"),
    ("vessel_relation_authorized", "VESSEL_RELATION_AUTHORIZED"),
    ("another_reception_request_authorized", "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"),
    ("follow_on_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
    ("real_command_run", "REAL_COMMAND_EXECUTION_ATTEMPTED"),
    ("real_command_execution_performed", "REAL_COMMAND_EXECUTION_ATTEMPTED"),
    ("physical_command_execution_performed", "REAL_COMMAND_EXECUTION_ATTEMPTED"),
    ("real_os_process_execution_performed", "REAL_COMMAND_EXECUTION_ATTEMPTED"),
    ("shell_command_run", "REAL_COMMAND_EXECUTION_ATTEMPTED"),
    ("subprocess_run", "REAL_COMMAND_EXECUTION_ATTEMPTED"),
    ("python_module_executed", "REAL_COMMAND_EXECUTION_ATTEMPTED"),
    ("external_api_call_performed", "REAL_COMMAND_EXECUTION_ATTEMPTED"),
    ("network_call_performed", "REAL_COMMAND_EXECUTION_ATTEMPTED"),
)


def _first_collapse(values: Sequence[Any]) -> tuple[str, str] | None:
    for value in values:
        if isinstance(value, Mapping):
            for key, block_code in COLLAPSE_TRUE_BLOCKS:
                if _truthy(value, (key,)):
                    return key, block_code
            if any(_truthy(value, (key,)) for key in ("mutation_performed", "replay_performed", "merge_performed")):
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


def _build_checks(request: Mapping[str, Any], malformed: bool = False) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    if malformed:
        _check(
            checks,
            "declared post-invocation command execution request mapping",
            False,
            "request is a mapping",
            "malformed",
            "DECLARED_POST_INVOCATION_COMMAND_EXECUTION_REQUEST_MALFORMED",
        )
        return checks

    boundary = _mapping(request.get("selected_post_invocation_command_execution_boundary_basis"))
    invocation = _mapping(request.get("selected_command_invocation_basis"))
    review = _mapping(request.get("selected_command_execution_review_basis"))
    consumption = _mapping(request.get("selected_request_consumption_basis"))
    consumed = _mapping(request.get("selected_consumed_request_basis"))
    v2 = _mapping(request.get("selected_v2_admitted_request_basis"))
    v1 = _mapping(request.get("selected_v1_predecessor_failure_basis"))
    lineage = _mapping(request.get("selected_older_command_execution_boundary_lineage_basis"))
    declared = _declared_non_claims(request)

    question = request.get("post_invocation_command_execution_question")
    intent = request.get("post_invocation_command_execution_intent")
    _check(
        checks,
        "post-invocation command execution question declared",
        isinstance(question, str) and bool(question.strip()),
        "question declared",
        question,
        "POST_INVOCATION_COMMAND_EXECUTION_QUESTION_UNDECLARED",
    )
    _check(
        checks,
        "post-invocation command execution intent supported",
        intent in SUPPORTED_INTENTS,
        "supported intent",
        intent,
        "POST_INVOCATION_COMMAND_EXECUTION_INTENT_UNSUPPORTED",
    )
    _check(
        checks,
        "post-invocation command execution boundary terminal summary basis declared",
        _present(request.get("selected_post_invocation_command_execution_boundary_terminal_summary_basis")),
        "boundary terminal summary basis declared",
        request.get("selected_post_invocation_command_execution_boundary_terminal_summary_basis"),
        "POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_BASIS_MISSING",
    )
    _check(
        checks,
        "post-invocation command execution boundary live artifact basis declared",
        _declared(request.get("selected_post_invocation_command_execution_boundary_basis")),
        "boundary live artifact basis declared",
        request.get("selected_post_invocation_command_execution_boundary_basis"),
        "POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_BASIS_MISSING",
    )
    boundary_outcome = _outcome(
        boundary,
        request,
        ("selected_post_invocation_command_execution_boundary_result_outcome",),
    )
    _check(
        checks,
        "post-invocation command execution boundary outcome recorded",
        boundary_outcome == POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_OUTCOME,
        POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_OUTCOME,
        boundary_outcome,
        "POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_NOT_RECORDED",
    )
    boundary_failed = _failed_count(
        boundary,
        request,
        ("selected_post_invocation_command_execution_boundary_failed_check_count",),
    )
    _check(
        checks,
        "post-invocation command execution boundary failed check count zero",
        boundary_failed == 0,
        "failed_check_count == 0",
        boundary_failed,
        "POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_FAILED_CHECKS_PRESENT",
    )
    _check(
        checks,
        "post-invocation command execution boundary one future execution step declared",
        _boundary_step_declared(boundary, request),
        "one future command execution step declared",
        boundary,
        "POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_STEP_NOT_DECLARED",
    )

    _check(
        checks,
        "command invocation terminal summary basis declared",
        _present(request.get("selected_command_invocation_terminal_summary_basis")),
        "command invocation terminal summary basis declared",
        request.get("selected_command_invocation_terminal_summary_basis"),
        "COMMAND_INVOCATION_BASIS_MISSING",
    )
    _check(
        checks,
        "command invocation basis declared",
        _declared(request.get("selected_command_invocation_basis")),
        "command invocation basis declared",
        request.get("selected_command_invocation_basis"),
        "COMMAND_INVOCATION_BASIS_MISSING",
    )
    invocation_outcome = _outcome(invocation, request, ("selected_command_invocation_result_outcome",))
    _check(
        checks,
        "command invocation outcome recorded",
        invocation_outcome == COMMAND_INVOCATION_OUTCOME,
        COMMAND_INVOCATION_OUTCOME,
        invocation_outcome,
        "COMMAND_INVOCATION_NOT_RECORDED",
    )
    invocation_failed = _failed_count(invocation, request, ("selected_command_invocation_failed_check_count",))
    _check(
        checks,
        "command invocation failed check count zero",
        invocation_failed == 0,
        "failed_check_count == 0",
        invocation_failed,
        "COMMAND_INVOCATION_FAILED_CHECKS_PRESENT",
    )
    _check(
        checks,
        "command invocation event recorded",
        _command_invocation_event_recorded(invocation, request),
        "bounded command invocation event recorded",
        invocation,
        "COMMAND_INVOCATION_EVENT_NOT_RECORDED",
    )
    _check(
        checks,
        "command invocation authorization token spent exactly once",
        _token_spent_exactly_once(invocation, request),
        "authorization token spent exactly once",
        invocation,
        "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_NOT_SPENT_EXACTLY_ONCE",
    )
    _check(
        checks,
        "command invocation authorization token reuse blocked",
        _token_reuse_blocked(invocation, request),
        "authorization token reuse blocked",
        invocation,
        "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_REUSE_NOT_BLOCKED",
    )

    for name, key, basis, outcome_keys, expected, missing, not_recorded, failed_key, failed_code in (
        (
            "command execution review basis declared",
            "selected_command_execution_review_basis",
            review,
            ("selected_command_execution_review_result_outcome",),
            COMMAND_EXECUTION_REVIEW_OUTCOME,
            "COMMAND_EXECUTION_REVIEW_BASIS_MISSING",
            "COMMAND_EXECUTION_REVIEW_NOT_RECORDED",
            "selected_command_execution_review_failed_check_count",
            "COMMAND_EXECUTION_REVIEW_FAILED_CHECKS_PRESENT",
        ),
        (
            "request consumption basis declared",
            "selected_request_consumption_basis",
            consumption,
            ("selected_request_consumption_result_outcome",),
            REQUEST_CONSUMPTION_OUTCOME,
            "REQUEST_CONSUMPTION_BASIS_MISSING",
            "REQUEST_CONSUMPTION_NOT_CONSUMED",
            "selected_request_consumption_failed_check_count",
            "REQUEST_CONSUMPTION_FAILED_CHECKS_PRESENT",
        ),
    ):
        _check(checks, name, _declared(request.get(key)), "basis declared", request.get(key), missing)
        _check(
            checks,
            name.replace("basis declared", "recorded outcome"),
            _outcome(basis, request, outcome_keys) == expected,
            expected,
            _outcome(basis, request, outcome_keys),
            not_recorded,
        )
        _check(
            checks,
            name.replace("basis declared", "failed check count zero"),
            _failed_count(basis, request, (failed_key,)) == 0,
            "failed_check_count == 0",
            _failed_count(basis, request, (failed_key,)),
            failed_code,
        )

    _check(
        checks,
        "consumed request basis declared",
        _declared(request.get("selected_consumed_request_basis")),
        "consumed request basis declared",
        request.get("selected_consumed_request_basis"),
        "CONSUMED_REQUEST_BASIS_MISSING",
    )
    _check(checks, "consumed request token remains closed", _consumed_token_closed(consumed), "consumed token closed", consumed, "CONSUMED_TOKEN_NOT_CLOSED")
    _check(checks, "consumed request not reopened", _consumed_not_reopened(consumed), "consumed request not reopened", consumed, "CONSUMED_REQUEST_REOPENED")

    _check(
        checks,
        "v2 admitted request basis declared",
        _declared(request.get("selected_v2_admitted_request_basis")),
        "v2 admitted request basis declared",
        request.get("selected_v2_admitted_request_basis"),
        "V2_ADMITTED_REQUEST_BASIS_MISSING",
    )
    v2_outcome = _outcome(v2, request, ("selected_v2_admitted_request_outcome",))
    _check(checks, "v2 admitted request outcome admitted", v2_outcome == V2_ADMITTED_REQUEST_OUTCOME, V2_ADMITTED_REQUEST_OUTCOME, v2_outcome, "V2_ADMITTED_REQUEST_NOT_ADMITTED")
    v2_version = _version(v2, request, ("selected_v2_admitted_request_version",))
    _check(checks, "v2 admitted request version 0.2.0", v2_version == V2_ADMITTED_REQUEST_VERSION, V2_ADMITTED_REQUEST_VERSION, v2_version, "V2_ADMITTED_REQUEST_VERSION_NOT_0_2_0")
    v2_failed = _failed_count(v2, request, ("selected_v2_failed_check_count",))
    _check(checks, "v2 admitted request failed check count zero", v2_failed == 0, "failed_check_count == 0", v2_failed, "V2_ADMITTED_REQUEST_FAILED_CHECKS_PRESENT")
    _check(checks, "v2 successor metadata preserved", _successor_metadata_preserved(v2, request), "successor metadata preserved", v2, "V2_SUCCESSOR_METADATA_MISSING")
    _check(checks, "v2 returned-result containment preserved", _returned_result_containment_preserved(v2), "returned-result containment preserved", v2, "V2_RETURNED_RESULT_CONTAINMENT_MISSING")
    _check(
        checks,
        "v1 predecessor failure basis declared",
        _declared(request.get("selected_v1_predecessor_failure_basis")),
        "v1 predecessor failure basis declared",
        request.get("selected_v1_predecessor_failure_basis"),
        "V1_PREDECESSOR_FAILURE_BASIS_MISSING",
    )
    _check(checks, "v1 predecessor failure remains visible", _v1_failure_visible(v1), "v1 failure visible", v1, "V1_PREDECESSOR_FAILURE_BASIS_MISSING")
    _check(
        checks,
        "v2 does not claim v1 passed",
        not (_truthy(v1, ("v1_claimed_passed", "v1_passed")) or _truthy(v2, ("v2_claims_v1_passed", "v1_claimed_passed", "v1_passed"))),
        "v1 not claimed passed",
        {"v1": v1, "v2": v2},
        "V1_CLAIMED_PASSED",
    )
    _check(
        checks,
        "v2 not treated as repairing v1",
        not (_truthy(v1, ("v2_treated_as_repairing_v1", "v1_repaired")) or _truthy(v2, ("v2_treated_as_repairing_v1", "v1_repaired"))),
        "v2 does not repair v1",
        {"v1": v1, "v2": v2},
        "V2_TREATED_AS_REPAIRING_V1",
    )
    _check(checks, "v1 failure not hidden", not _truthy(v1, ("v1_hidden", "v1_failure_hidden")), "v1 failure not hidden", v1, "V1_FAILURE_HIDDEN")

    _check(
        checks,
        "older command execution boundary lineage basis declared",
        _declared(request.get("selected_older_command_execution_boundary_lineage_basis")),
        "older command execution boundary lineage basis declared",
        request.get("selected_older_command_execution_boundary_lineage_basis"),
        "OLDER_COMMAND_EXECUTION_BOUNDARY_LINEAGE_TREATED_AS_CURRENT_EXECUTION",
    )
    _check(
        checks,
        "older command execution boundary lineage basis not current execution",
        not _lineage_as_current_execution(lineage),
        "older command execution boundary lineage remains prior scaffolding only",
        lineage,
        "OLDER_COMMAND_EXECUTION_BOUNDARY_LINEAGE_TREATED_AS_CURRENT_EXECUTION",
    )

    for name, key, code in (
        ("command report basis declared", "selected_command_report_basis", "COMMAND_REPORT_BASIS_MISSING"),
        ("command implementation boundary basis declared", "selected_command_implementation_boundary_basis", "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING"),
        ("command boundary basis declared", "selected_command_boundary_basis", "COMMAND_BOUNDARY_BASIS_MISSING"),
        ("artifact emission containment basis declared", "selected_artifact_emission_containment_basis", "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING"),
        ("evidence-manifest basis declared", "selected_evidence_manifest_basis", "EVIDENCE_MANIFEST_BASIS_MISSING"),
        ("portable verification basis declared", "selected_portable_verification_basis", "PORTABLE_VERIFICATION_BASIS_MISSING"),
    ):
        _check(checks, name, _declared(request.get(key)), "basis declared", request.get(key), code)

    for name, key, code, flags in (
        ("post-invocation-command-execution-only posture declared", "post_invocation_command_execution_only_posture", "POST_INVOCATION_COMMAND_EXECUTION_ONLY_POSTURE_MISSING", ("post_invocation_command_execution_only", "post_invocation_command_execution_only_posture_declared")),
        ("one-bounded-command-execution-event posture declared", "one_bounded_command_execution_event_posture", "ONE_BOUNDED_COMMAND_EXECUTION_EVENT_POSTURE_MISSING", ("one_bounded_command_execution_event_recorded", "one_bounded_command_execution_event_posture_declared")),
        ("execution-trace-audit-only posture declared", "execution_trace_audit_only_posture", "EXECUTION_TRACE_AUDIT_ONLY_POSTURE_MISSING", ("execution_trace_recorded_as_audit_only", "execution_trace_audit_only", "trace_is_audit_only")),
        ("no-command-output posture declared", "no_command_output_posture", "NO_COMMAND_OUTPUT_POSTURE_MISSING", ("command_output_not_created", "command_output_still_not_created")),
        ("no-command-result posture declared", "no_command_result_posture", "NO_COMMAND_RESULT_POSTURE_MISSING", ("command_result_not_created", "command_result_still_not_created")),
        ("no-command-success posture declared", "no_command_success_posture", "NO_COMMAND_SUCCESS_POSTURE_MISSING", ("command_success_not_created", "command_success_still_not_created")),
        ("no-execution-permission posture declared", "no_execution_permission_posture", "EXECUTION_PERMISSION_CREATED", ("execution_permission_not_created",)),
        ("no-execution-approval posture declared", "no_execution_approval_posture", "EXECUTION_APPROVAL_CREATED", ("execution_approval_not_created",)),
        ("no-standing-execution-lane posture declared", "no_standing_execution_lane_posture", "NO_STANDING_EXECUTION_LANE_POSTURE_MISSING", ("no_standing_execution_lane", "standing_execution_lane_not_created")),
        ("no-repeat-execution-permission posture declared", "no_repeat_execution_permission_posture", "NO_REPEAT_EXECUTION_PERMISSION_POSTURE_MISSING", ("no_repeat_execution_permission", "repeat_execution_permission_not_created")),
        ("authorization-token-reuse-blocked posture declared", "authorization_token_reuse_blocked_posture", "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_REUSE_NOT_BLOCKED", ("authorization_token_reuse_blocked", "authorization_token_not_reused")),
        ("consumed-token-closed posture declared", "consumed_token_closed_posture", "CONSUMED_TOKEN_NOT_CLOSED", ("consumed_request_token_remains_closed", "consumed_token_closed")),
        ("no-reopen-consumed-request posture declared", "no_reopen_consumed_request_posture", "CONSUMED_REQUEST_REOPENED", ("consumed_request_not_reopened", "no_reopen_consumed_request")),
        ("returned-result containment posture declared", "returned_result_containment_posture", "V2_RETURNED_RESULT_CONTAINMENT_MISSING", ("returned_result_containment_preserved", "no_raw_full_prior_artifact_body_returned")),
    ):
        _check(checks, name, _posture_declared(request.get(key), flags), "posture declared", request.get(key), code)

    scope = _scope_values(request.get("post_invocation_command_execution_scope"))
    _check(
        checks,
        "post-invocation command execution scope supported",
        bool(scope) and all(value in SUPPORTED_POST_INVOCATION_COMMAND_EXECUTION_SCOPE_SET for value in scope),
        "supported scope",
        scope,
        "UNSUPPORTED_POST_INVOCATION_COMMAND_EXECUTION_SCOPE",
    )
    _check(
        checks,
        "reference-shaped input posture preserved",
        _reference_shaped_inputs_preserved(request),
        "selected basis is reference-shaped and no full prior artifact body is embedded",
        "reference-shaped" if _reference_shaped_inputs_preserved(request) else "not reference-shaped",
        "FULL_PRIOR_ARTIFACT_BODY_EMITTED",
    )
    _check(
        checks,
        "execution trace is audit only",
        _execution_trace_audit_only(request),
        "execution trace is audit-only if present",
        request.get("execution_trace"),
        "EXECUTION_TRACE_TREATED_AS_OUTPUT",
    )

    collapse = _first_collapse(
        (
            request,
            declared,
            boundary,
            invocation,
            review,
            consumption,
            consumed,
            v2,
            v1,
            lineage,
            _mapping(request.get("execution_trace")),
            _mapping(request.get("no_command_output_posture")),
            _mapping(request.get("no_command_result_posture")),
            _mapping(request.get("no_command_success_posture")),
            _mapping(request.get("no_execution_permission_posture")),
            _mapping(request.get("no_execution_approval_posture")),
            _mapping(request.get("no_standing_execution_lane_posture")),
            _mapping(request.get("no_repeat_execution_permission_posture")),
            _mapping(request.get("authorization_token_reuse_blocked_posture")),
            _mapping(request.get("no_reopen_consumed_request_posture")),
        )
    )
    _check(
        checks,
        "collapse flags absent",
        collapse is None,
        "no output/result/success/permission/reuse/mutation/overread flags",
        collapse,
        collapse[1] if collapse else "MUTATION_REPLAY_OR_MERGE_DETECTED",
    )
    full_body_present = _contains_forbidden_full_body_key(request)
    _check(
        checks,
        "raw full prior artifact body not emitted",
        not full_body_present,
        "no full prior artifact body emitted",
        "forbidden full-body key present" if full_body_present else "contained",
        "FULL_PRIOR_ARTIFACT_BODY_EMITTED",
    )
    non_claim_failure = _first_non_claim_failure(request)
    _check(
        checks,
        "non-claims remain false",
        non_claim_failure is None,
        "required non-claims are explicit and false",
        non_claim_failure,
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    return checks


def _first_failed(checks: Sequence[Mapping[str, Any]]) -> Mapping[str, Any] | None:
    return next((check for check in checks if not check.get("passed")), None)


def _select_outcome(
    request: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    forced_block: str | None = None,
) -> tuple[str, str | None, str | None]:
    if forced_block:
        return OUTCOME_BLOCKED, forced_block, forced_block
    intent = request.get("post_invocation_command_execution_intent")
    if intent == INTENT_BLOCK:
        return OUTCOME_BLOCKED, "POST_INVOCATION_COMMAND_EXECUTION_BLOCKED_BY_REQUEST", str(
            request.get("block_reason") or "blocked by request intent"
        )
    if intent not in SUPPORTED_INTENTS:
        return OUTCOME_BLOCKED, "POST_INVOCATION_COMMAND_EXECUTION_INTENT_UNSUPPORTED", (
            "unsupported post-invocation command execution intent"
        )
    requested = request.get("requested_post_invocation_command_execution_outcome", OUTCOME_RECORDED)
    if requested == OUTCOME_BLOCKED:
        return OUTCOME_BLOCKED, "POST_INVOCATION_COMMAND_EXECUTION_BLOCKED_BY_REQUEST", str(
            request.get("block_reason") or "blocked by requested outcome"
        )
    if requested not in OUTCOME_FAMILY:
        return OUTCOME_BLOCKED, "DECLARED_POST_INVOCATION_COMMAND_EXECUTION_REQUEST_MALFORMED", (
            "unsupported requested outcome"
        )
    failed = _first_failed(checks)
    if failed is not None:
        return OUTCOME_BLOCKED, str(failed.get("block_code")), str(failed.get("check_name"))
    if intent == INTENT_DO_NOT_RECORD or requested == OUTCOME_NOT_RECORDED:
        return OUTCOME_NOT_RECORDED, None, None
    if requested == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS, None, None
    return OUTCOME_RECORDED, None, None


def _counts(checks: Sequence[Mapping[str, Any]]) -> tuple[int, int]:
    passed = sum(1 for check in checks if check.get("passed") is True)
    return passed, len(checks) - passed


def _statement(outcome: str) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    statement = {key: recorded for key in ALLOWED_TRUE_RECORDED_FIELDS}
    statement.update(_default_non_claims())
    statement.update(
        {
            "post_invocation_command_execution_not_recorded": outcome == OUTCOME_NOT_RECORDED,
            "post_invocation_command_execution_requires_additional_basis": outcome
            == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "post_invocation_command_execution_blocked": outcome == OUTCOME_BLOCKED,
            "post_invocation_command_execution_is_not_command_output": True,
            "post_invocation_command_execution_is_not_command_result": True,
            "post_invocation_command_execution_is_not_command_success": True,
            "post_invocation_command_execution_is_not_execution_permission": True,
            "post_invocation_command_execution_is_not_execution_approval": True,
            "execution_trace_is_audit_only": True,
            "execution_trace_is_not_command_output": True,
            "execution_trace_is_not_command_result": True,
            "execution_trace_is_not_command_success": True,
            "execution_trace_is_not_source": True,
            "execution_trace_is_not_authority": True,
            "real_command_not_run_by_resolver": True,
            "subprocess_not_run_by_resolver": True,
            "network_not_called_by_resolver": True,
            "older_command_execution_boundary_lineage_is_not_current_execution": True,
        }
    )
    return statement


def _non_meaning() -> dict[str, bool]:
    names = (
        "command_output_exists",
        "command_result_exists",
        "command_success_exists",
        "execution_permission_exists",
        "execution_approval_exists",
        "execution_trace_is_output",
        "execution_trace_is_result",
        "execution_trace_is_success",
        "execution_trace_is_source",
        "execution_trace_is_authority",
        "standing_execution_lane_exists",
        "repeat_execution_permission_exists",
        "consumed_request_token_reopened",
        "authorization_token_reusable",
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
    return {f"post_invocation_command_execution_does_not_mean_{name}": True for name in names}


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "post_invocation_command_execution_test",
            "post_invocation_command_execution_live_artifact",
            "command_output_boundary_or_output_containment_if_separately_specified",
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
    unsupported = [value for value in values if value not in SUPPORTED_POST_INVOCATION_COMMAND_EXECUTION_SCOPE_SET]
    return {
        "selected_scope_values": values,
        "supported_scope_values": list(SUPPORTED_POST_INVOCATION_COMMAND_EXECUTION_SCOPE),
        "unsupported_scope_values": unsupported,
        "all_selected_scope_values_supported": bool(values) and not unsupported,
        "post_invocation_command_execution_only": "POST_INVOCATION_COMMAND_EXECUTION_ONLY" in values,
        "one_bounded_command_execution_event_recorded": outcome == OUTCOME_RECORDED,
        "execution_trace_is_audit_only": True,
        "command_output_not_created": True,
        "command_result_not_created": True,
        "command_success_not_created": True,
        "execution_permission_not_created": True,
        "execution_approval_not_created": True,
        "no_standing_execution_lane": True,
        "no_repeat_execution_permission": True,
        "authorization_token_reuse_blocked": True,
        "consumed_request_token_remains_closed": True,
        "consumed_request_not_reopened": True,
        "execution_is_not_command_output_result_success": True,
        "execution_trace_is_not_output_result_success_source_authority": True,
        "v1_predecessor_failure_remains_visible": True,
        "v2_successor_does_not_repair_v1": True,
        "returned_result_containment_preserved": True,
        "reference_shaped_basis_required": True,
        "full_prior_artifact_body_not_emitted": True,
        "no_authority_currentness_final_completion_continuation_reusable_follow_on": True,
    }


def _execution_trace_section(request: Mapping[str, Any], outcome: str) -> dict[str, Any]:
    raw_trace = request.get("execution_trace")
    if isinstance(raw_trace, Mapping):
        section = _sanitize_execution_trace(raw_trace)
    elif isinstance(raw_trace, (str, Path)):
        section = {"trace_reference": str(raw_trace), "trace_reference_only": True}
    else:
        section = {}
    request_id = str(request.get("post_invocation_command_execution_request_id") or "undeclared")
    section["trace_id"] = section.get("trace_id") or f"{request_id}__execution_trace_audit_only"
    section["trace_type"] = "EXECUTION_TRACE_AUDIT_ONLY"
    section["execution_event_recorded"] = outcome == OUTCOME_RECORDED
    section["execution_trace_recorded_as_audit_only"] = outcome == OUTCOME_RECORDED
    section["command_output_created"] = False
    section["command_result_created"] = False
    section["command_success_created"] = False
    section["trace_is_not_output"] = True
    section["trace_is_not_result"] = True
    section["trace_is_not_success"] = True
    section["trace_is_not_source"] = True
    section["trace_is_not_authority"] = True
    section["trace_is_not_currentness"] = True
    section["trace_is_not_final_completion"] = True
    section["stdout_not_recorded"] = True
    section["stderr_not_recorded"] = True
    section["process_output_not_recorded"] = True
    section["real_command_not_run_by_resolver"] = True
    section["subprocess_not_run_by_resolver"] = True
    section["network_not_called_by_resolver"] = True
    return section


def _metadata(request: Mapping[str, Any], outcome: str) -> dict[str, Any]:
    request_id = str(request.get("post_invocation_command_execution_request_id") or "undeclared")
    return {
        "portable_source_body_verification_post_invocation_command_execution_result_id": (
            f"{request_id}__portable_source_body_verification_post_invocation_command_execution_result"
        ),
        "portable_source_body_verification_post_invocation_command_execution_result_type": RESULT_TYPE,
        "portable_source_body_verification_post_invocation_command_execution_result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
        "post_invocation_command_execution_request_id": request_id,
        "naming_containment": {
            "short_resolver_filename_used_intentionally": True,
            "short_filename_does_not_erase_upstream_lineage": True,
            "full_upstream_lineage_preserved_in_selected_basis": True,
            "post_invocation_execution_filename_distinct_from_boundary_and_older_execution_surfaces": True,
        },
        "lineage_posture": {
            "downstream_of_recorded_command_invocation": True,
            "downstream_of_post_invocation_command_execution_boundary": True,
            "older_command_execution_boundary_surfaces_remain_lineage_only": True,
        },
        "requested_outcome": request.get("requested_post_invocation_command_execution_outcome"),
        "outcome": outcome,
    }


def _open_posture(
    outcome: str,
    request: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
) -> tuple[dict[str, Any], dict[str, Any]]:
    additional = {
        "requires_additional_basis": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "additional_basis_context": _sanitize_reference_shape(request.get("additional_basis_context") or {}),
        "missing_basis_not_scheduled": True,
        "missing_basis_not_authorized": True,
        "missing_basis_not_executed": True,
        "additional_basis_does_not_run_real_command": True,
        "additional_basis_does_not_create_output_result_success": True,
        "additional_basis_does_not_create_execution_permission_or_approval": True,
        "additional_basis_does_not_create_follow_on_work": True,
    }
    not_recorded = {
        "not_recorded": outcome == OUTCOME_NOT_RECORDED,
        "not_recorded_basis": _sanitize_reference_shape(request.get("not_recorded_basis") or {}),
        "failed_checks": _sanitize_reference_shape(
            [check for check in checks if not check.get("passed")] if outcome == OUTCOME_NOT_RECORDED else []
        ),
        "not_recorded_does_not_mutate": True,
        "not_recorded_does_not_repair": True,
        "not_recorded_does_not_run_real_command": True,
        "not_recorded_does_not_emit_output": True,
        "not_recorded_does_not_create_command_result": True,
        "not_recorded_does_not_create_command_success": True,
        "not_recorded_does_not_authorize_next_work": True,
    }
    return additional, not_recorded


def build_portable_source_body_verification_post_invocation_command_execution_summary(
    result: Mapping[str, Any]
) -> dict[str, Any]:
    """Build a bounded summary for a post-invocation command execution result."""

    statement = _mapping(result.get("post_invocation_command_execution_statement"))
    block = _mapping(result.get("block"))
    metadata = _mapping(result.get("portable_source_body_verification_post_invocation_command_execution_metadata"))
    question = _mapping(result.get("declared_post_invocation_command_execution_question"))
    non_claims = _mapping(result.get("non_claims"))
    checks = [
        check for check in result.get("post_invocation_command_execution_checks", []) if isinstance(check, Mapping)
    ]
    passed, failed = _counts(checks)
    boundary = _mapping(result.get("selected_post_invocation_command_execution_boundary_basis"))
    invocation = _mapping(result.get("selected_command_invocation_basis"))
    review = _mapping(result.get("selected_command_execution_review_basis"))
    consumption = _mapping(result.get("selected_request_consumption_basis"))
    v2 = _mapping(result.get("selected_v2_admitted_request_basis"))
    lineage = _mapping(result.get("selected_older_command_execution_boundary_lineage_basis"))
    trace = _mapping(result.get("execution_trace"))
    outcome = result.get("outcome")
    return {
        "outcome": outcome,
        "block_code": block.get("code"),
        "block_reason": block.get("reason"),
        "request_id": metadata.get("post_invocation_command_execution_request_id"),
        "question": question.get("question"),
        "intent": question.get("intent"),
        "passed_check_count": passed,
        "failed_check_count": failed,
        "post_invocation_execution_recorded": statement.get("post_invocation_command_execution_recorded") is True,
        "bounded_command_execution_event_recorded": statement.get("bounded_command_execution_event_recorded") is True,
        "execution_trace_audit_only": statement.get("execution_trace_recorded_as_audit_only") is True,
        "command_output_result_success_still_not_created": all(
            statement.get(key) is True
            for key in (
                "command_output_still_not_created",
                "command_result_still_not_created",
                "command_success_still_not_created",
            )
        ),
        "execution_permission_not_created": statement.get("execution_permission_not_created") is True,
        "execution_approval_not_created": statement.get("execution_approval_not_created") is True,
        "authorization_token_reuse_blocked": statement.get("authorization_token_reuse_blocked") is True,
        "consumed_request_token_remains_closed": statement.get("consumed_request_token_remains_closed") is True,
        "v1_predecessor_failure_preserved": statement.get("v1_predecessor_failure_preserved") is True,
        "returned_result_containment_preserved": statement.get("returned_result_containment_preserved") is True,
        "not_recorded": outcome == OUTCOME_NOT_RECORDED,
        "requires_additional_basis": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "selected_boundary_outcome": _find_first(boundary, ("outcome", "result_outcome", "selected_result_outcome")),
        "selected_boundary_failed_check_count": _find_first(
            boundary, ("failed_check_count", "selected_failed_check_count")
        ),
        "selected_command_invocation_outcome": _find_first(invocation, ("outcome", "result_outcome")),
        "selected_command_invocation_failed_check_count": _find_first(
            invocation, ("failed_check_count", "selected_failed_check_count")
        ),
        "selected_command_execution_review_outcome": _find_first(review, ("outcome", "result_outcome")),
        "selected_command_execution_review_failed_check_count": _find_first(
            review, ("failed_check_count", "selected_failed_check_count")
        ),
        "selected_request_consumption_outcome": _find_first(consumption, ("outcome", "result_outcome")),
        "selected_request_consumption_failed_check_count": _find_first(
            consumption, ("failed_check_count", "selected_failed_check_count")
        ),
        "selected_v2_admitted_request_outcome": _find_first(v2, ("outcome", "result_outcome")),
        "selected_v2_admitted_request_version": _find_first(v2, ("result_version", "version")),
        "selected_v2_admitted_request_failed_check_count": _find_first(
            v2, ("failed_check_count", "selected_failed_check_count")
        ),
        "execution_trace_not_output_result_success_source_authority": all(
            trace.get(key) is True
            for key in (
                "trace_is_not_output",
                "trace_is_not_result",
                "trace_is_not_success",
                "trace_is_not_source",
                "trace_is_not_authority",
            )
        ),
        "no_standing_repeat_execution_lane": all(
            non_claims.get(key) is False
            for key in ("standing_execution_lane_created", "repeat_execution_permission_created")
        ),
        "older_command_execution_boundary_lineage_not_treated_as_current_execution": not _lineage_as_current_execution(
            lineage
        ),
        "no_raw_full_prior_artifact_body": non_claims.get("raw_full_prior_artifact_body_returned") is False,
        "no_artifact_mutation": non_claims.get("prior_artifacts_mutated") is False,
        "no_deployment_runtime_public_release": all(
            non_claims.get(key) is False
            for key in ("deployment_created", "runtime_hosting_created", "public_release_created")
        ),
        "no_operation_public_readiness_final_completion": all(
            non_claims.get(key) is False
            for key in (
                "operation_permission_created",
                "public_launch_readiness_created",
                "final_completion_claimed",
            )
        ),
        "no_continuation_publication_reusable_follow_on": all(
            non_claims.get(key) is False
            for key in (
                "continuation_authorized",
                "publication_flow_opened",
                "reusable_permission_created",
                "follow_on_work_authorized",
            )
        ),
        "key_non_claims": _sanitize_reference_shape(non_claims),
    }


def _build_result(
    request: Mapping[str, Any],
    *,
    checks: Sequence[Mapping[str, Any]],
    outcome: str,
    block_code: str | None,
    block_reason: str | None,
    request_path: str | None = None,
) -> dict[str, Any]:
    metadata = _metadata(request, outcome)
    if request_path:
        metadata["declared_post_invocation_command_execution_request_path"] = request_path
    statement = _statement(outcome)
    non_claims = _default_non_claims()
    additional, not_recorded = _open_posture(outcome, request, checks)
    result = {
        "portable_source_body_verification_post_invocation_command_execution_metadata": metadata,
        "declared_post_invocation_command_execution_question": {
            "question": request.get("post_invocation_command_execution_question"),
            "expected_question": CORE_POST_INVOCATION_COMMAND_EXECUTION_QUESTION,
            "intent": request.get("post_invocation_command_execution_intent"),
            "post_invocation_command_execution_is_not_command_output": True,
            "post_invocation_command_execution_is_not_command_result": True,
            "post_invocation_command_execution_is_not_command_success": True,
            "post_invocation_command_execution_is_not_execution_permission": True,
            "post_invocation_command_execution_is_not_execution_approval": True,
        },
        "selected_post_invocation_command_execution_boundary_basis": _basis_section(
            request.get("selected_post_invocation_command_execution_boundary_basis"),
            path=request.get("selected_post_invocation_command_execution_boundary_result_path"),
            extra={
                "selected_result_id": request.get("selected_post_invocation_command_execution_boundary_result_id"),
                "selected_result_outcome": request.get(
                    "selected_post_invocation_command_execution_boundary_result_outcome"
                ),
                "selected_failed_check_count": request.get(
                    "selected_post_invocation_command_execution_boundary_failed_check_count"
                ),
                "one_future_command_execution_step_declared": request.get(
                    "selected_post_invocation_command_execution_boundary_step_declared"
                ),
                "boundary_did_not_execute_command": True,
                "boundary_did_not_create_output_result_success": True,
                "boundary_did_not_create_execution_permission_or_approval": True,
                "boundary_basis_remains_boundary_basis_only": True,
            },
        ),
        "selected_post_invocation_command_execution_boundary_terminal_summary_basis": _basis_section(
            request.get("selected_post_invocation_command_execution_boundary_terminal_summary_basis"),
            path=request.get("selected_post_invocation_command_execution_boundary_terminal_summary_path"),
            extra={"terminal_summary_remains_readability_basis_only": True},
        ),
        "selected_command_invocation_basis": _basis_section(
            request.get("selected_command_invocation_basis"),
            path=request.get("selected_command_invocation_result_path"),
            extra={
                "selected_result_id": request.get("selected_command_invocation_result_id"),
                "selected_result_outcome": request.get("selected_command_invocation_result_outcome"),
                "selected_failed_check_count": request.get("selected_command_invocation_failed_check_count"),
                "selected_command_invocation_event_recorded": request.get(
                    "selected_command_invocation_event_recorded"
                ),
                "selected_authorization_token_spent_exactly_once": request.get(
                    "selected_command_invocation_authorization_token_spent_exactly_once"
                ),
                "selected_authorization_token_reuse_blocked": request.get(
                    "selected_command_invocation_authorization_token_reuse_blocked"
                ),
                "command_invocation_basis_remains_invocation_basis_only": True,
            },
        ),
        "selected_command_invocation_terminal_summary_basis": _basis_section(
            request.get("selected_command_invocation_terminal_summary_basis"),
            path=request.get("selected_command_invocation_terminal_summary_path"),
            extra={"terminal_summary_remains_readability_basis_only": True},
        ),
        "selected_command_execution_review_basis": _basis_section(
            request.get("selected_command_execution_review_basis"),
            path=request.get("selected_command_execution_review_result_path"),
            extra={
                "selected_result_id": request.get("selected_command_execution_review_result_id"),
                "selected_result_outcome": request.get("selected_command_execution_review_result_outcome"),
                "selected_failed_check_count": request.get("selected_command_execution_review_failed_check_count"),
                "review_basis_remains_review_basis_only": True,
            },
        ),
        "selected_request_consumption_basis": _basis_section(
            request.get("selected_request_consumption_basis"),
            path=request.get("selected_request_consumption_result_path"),
            extra={
                "selected_result_id": request.get("selected_request_consumption_result_id"),
                "selected_result_outcome": request.get("selected_request_consumption_result_outcome"),
                "selected_failed_check_count": request.get("selected_request_consumption_failed_check_count"),
                "request_consumption_basis_only": True,
            },
        ),
        "selected_consumed_request_basis": _basis_section(
            request.get("selected_consumed_request_basis"),
            extra={"consumed_request_token_remains_closed": True, "consumed_request_not_reopened": True},
        ),
        "selected_v2_admitted_request_basis": _basis_section(
            request.get("selected_v2_admitted_request_basis"),
            path=request.get("selected_v2_admitted_request_artifact_path"),
            extra={
                "selected_artifact_id": request.get("selected_v2_admitted_request_artifact_id"),
                "selected_outcome": request.get("selected_v2_admitted_request_outcome"),
                "selected_version": request.get("selected_v2_admitted_request_version"),
                "selected_failed_check_count": request.get("selected_v2_failed_check_count"),
                "selected_v2_successor_metadata": request.get("selected_v2_successor_metadata"),
                "v2_remains_lineage_evidence_only": True,
                "v2_does_not_claim_v1_passed": True,
            },
        ),
        "selected_v1_predecessor_failure_basis": _basis_section(
            request.get("selected_v1_predecessor_failure_basis"),
            path=request.get("selected_v1_predecessor_artifact_path"),
            extra={
                "selected_artifact_id": request.get("selected_v1_predecessor_artifact_id"),
                "selected_outcome": request.get("selected_v1_predecessor_outcome"),
                "v1_predecessor_failure_remains_visible": True,
                "v1_is_not_repaired": True,
                "v1_is_not_hidden": True,
                "v1_is_not_claimed_passed": True,
            },
        ),
        "selected_older_command_execution_boundary_lineage_basis": _basis_section(
            request.get("selected_older_command_execution_boundary_lineage_basis"),
            path=request.get("selected_older_command_execution_boundary_lineage_result_path"),
            extra={
                "older_command_execution_boundary_surfaces_remain_lineage_only": True,
                "lineage_basis_is_not_current_execution": True,
            },
        ),
        "selected_command_report_basis": _basis_section(
            request.get("selected_command_report_basis"), path=request.get("selected_command_report_path")
        ),
        "selected_command_implementation_boundary_basis": _basis_section(
            request.get("selected_command_implementation_boundary_basis"),
            path=request.get("selected_command_implementation_boundary_result_path"),
        ),
        "selected_command_boundary_basis": _basis_section(
            request.get("selected_command_boundary_basis"), path=request.get("selected_command_boundary_result_path")
        ),
        "selected_artifact_emission_containment_basis": _basis_section(
            request.get("selected_artifact_emission_containment_basis"),
            path=request.get("selected_artifact_emission_containment_result_path"),
        ),
        "selected_evidence_manifest_basis": _basis_section(
            request.get("selected_evidence_manifest_basis"),
            path=request.get("selected_evidence_manifest_result_path"),
        ),
        "selected_portable_verification_basis": _basis_section(
            request.get("selected_portable_verification_basis"),
            path=request.get("selected_portable_verification_result_path"),
        ),
        "post_invocation_command_execution_only_posture": _basis_section(
            request.get("post_invocation_command_execution_only_posture"),
            extra={"post_invocation_command_execution_only": True, "execution_is_not_output_result_success": True},
        ),
        "one_bounded_command_execution_event_posture": _basis_section(
            request.get("one_bounded_command_execution_event_posture"),
            extra={"bounded_command_execution_event_recorded": outcome == OUTCOME_RECORDED},
        ),
        "execution_trace_audit_only_posture": _basis_section(
            request.get("execution_trace_audit_only_posture"),
            extra={"execution_trace_recorded_as_audit_only": outcome == OUTCOME_RECORDED},
        ),
        "no_command_output_posture": _basis_section(
            request.get("no_command_output_posture"), extra={"command_output_created": False}
        ),
        "no_command_result_posture": _basis_section(
            request.get("no_command_result_posture"), extra={"command_result_created": False}
        ),
        "no_command_success_posture": _basis_section(
            request.get("no_command_success_posture"), extra={"command_success_created": False}
        ),
        "no_execution_permission_posture": _basis_section(
            request.get("no_execution_permission_posture"), extra={"execution_permission_created": False}
        ),
        "no_execution_approval_posture": _basis_section(
            request.get("no_execution_approval_posture"), extra={"execution_approval_created": False}
        ),
        "no_standing_execution_lane_posture": _basis_section(
            request.get("no_standing_execution_lane_posture"), extra={"standing_execution_lane_created": False}
        ),
        "no_repeat_execution_permission_posture": _basis_section(
            request.get("no_repeat_execution_permission_posture"), extra={"repeat_execution_permission_created": False}
        ),
        "authorization_token_reuse_blocked_posture": _basis_section(
            request.get("authorization_token_reuse_blocked_posture"),
            extra={"authorization_token_reuse_blocked": True, "authorization_token_reused": False},
        ),
        "consumed_token_closed_posture": _basis_section(
            request.get("consumed_token_closed_posture"), extra={"consumed_request_token_remains_closed": True}
        ),
        "no_reopen_consumed_request_posture": _basis_section(
            request.get("no_reopen_consumed_request_posture"), extra={"consumed_request_reopened": False}
        ),
        "returned_result_containment_posture": _basis_section(
            request.get("returned_result_containment_posture"),
            extra={"returned_result_containment_preserved": True, "raw_full_prior_artifact_body_returned": False},
        ),
        "post_invocation_command_execution_scope": _scope_section(
            request.get("post_invocation_command_execution_scope"), outcome
        ),
        "post_invocation_command_execution_checks": _sanitize_reference_shape(list(checks)),
        "post_invocation_command_execution_statement": statement,
        "post_invocation_command_execution_non_meaning": _non_meaning(),
        "execution_trace": _execution_trace_section(request, outcome),
        "additional_basis_required": additional,
        "not_recorded_basis": not_recorded,
        "what_remains_open": _what_remains_open(),
        "non_claims": non_claims,
        "outcome": outcome,
        "block": {"code": block_code, "reason": block_reason},
    }
    result["portable_source_body_verification_post_invocation_command_execution_summary"] = (
        build_portable_source_body_verification_post_invocation_command_execution_summary(result)
    )
    return result


def resolve_portable_source_body_verification_post_invocation_command_execution(
    declared_post_invocation_command_execution_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded post-invocation command execution request."""

    if declared_post_invocation_command_execution_request is None:
        request: Mapping[str, Any] = {}
        checks = _build_checks(request)
        outcome, code, reason = _select_outcome(
            request,
            checks,
            "POST_INVOCATION_COMMAND_EXECUTION_QUESTION_UNDECLARED",
        )
        return _build_result(request, checks=checks, outcome=outcome, block_code=code, block_reason=reason)
    if not isinstance(declared_post_invocation_command_execution_request, Mapping):
        request = {}
        checks = _build_checks(request, malformed=True)
        outcome, code, reason = _select_outcome(
            request,
            checks,
            "DECLARED_POST_INVOCATION_COMMAND_EXECUTION_REQUEST_MALFORMED",
        )
        return _build_result(request, checks=checks, outcome=outcome, block_code=code, block_reason=reason)
    request = _deepcopy(declared_post_invocation_command_execution_request)
    checks = _build_checks(request)
    outcome, code, reason = _select_outcome(request, checks)
    return _build_result(request, checks=checks, outcome=outcome, block_code=code, block_reason=reason)


def resolve_portable_source_body_verification_post_invocation_command_execution_from_path(
    declared_post_invocation_command_execution_request_path: Path | str,
) -> dict[str, Any]:
    """Resolve one post-invocation command execution request loaded from a JSON object path."""

    path = Path(declared_post_invocation_command_execution_request_path)
    try:
        loaded = json.loads(path.read_text(encoding="utf-8"))
    except OSError:
        request = {"post_invocation_command_execution_request_id": "unreadable_path"}
        checks = _build_checks(request)
        outcome, code, reason = _select_outcome(
            request,
            checks,
            "DECLARED_POST_INVOCATION_COMMAND_EXECUTION_REQUEST_UNREADABLE",
        )
        return _build_result(
            request,
            checks=checks,
            outcome=outcome,
            block_code=code,
            block_reason=reason,
            request_path=str(path),
        )
    except json.JSONDecodeError:
        request = {"post_invocation_command_execution_request_id": "malformed_json"}
        checks = _build_checks(request)
        outcome, code, reason = _select_outcome(
            request,
            checks,
            "DECLARED_POST_INVOCATION_COMMAND_EXECUTION_REQUEST_MALFORMED",
        )
        return _build_result(
            request,
            checks=checks,
            outcome=outcome,
            block_code=code,
            block_reason=reason,
            request_path=str(path),
        )
    if not isinstance(loaded, Mapping):
        request = {"post_invocation_command_execution_request_id": "non_object_json"}
        checks = _build_checks(request, malformed=True)
        outcome, code, reason = _select_outcome(
            request,
            checks,
            "DECLARED_POST_INVOCATION_COMMAND_EXECUTION_REQUEST_MALFORMED",
        )
        return _build_result(
            request,
            checks=checks,
            outcome=outcome,
            block_code=code,
            block_reason=reason,
            request_path=str(path),
        )
    request = _deepcopy(loaded)
    checks = _build_checks(request)
    outcome, code, reason = _select_outcome(request, checks)
    return _build_result(
        request,
        checks=checks,
        outcome=outcome,
        block_code=code,
        block_reason=reason,
        request_path=str(path),
    )


def _deduplicated_output_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 1000000):
        candidate = path.parent / f"{path.stem}_{index:03d}{path.suffix}"
        if not candidate.exists():
            return candidate
    raise PortableSourceBodyVerificationPostInvocationCommandExecutionError(
        "unable to allocate non-overwriting post-invocation command execution result path"
    )


def write_portable_source_body_verification_post_invocation_command_execution_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a post-invocation command execution result JSON without silently overwriting."""

    if output_path is None:
        metadata = _mapping(result.get("portable_source_body_verification_post_invocation_command_execution_metadata"))
        request_id = (
            metadata.get("post_invocation_command_execution_request_id")
            or "undeclared_post_invocation_command_execution_request"
        )
        filename = (
            f"{_safe_component(request_id, 'undeclared_post_invocation_command_execution_request')}"
            "__portable_source_body_verification_post_invocation_command_execution_result.json"
        )
        path = PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_ROOT / filename
    else:
        path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    final_path = _deduplicated_output_path(path)
    final_path.write_text(
        json.dumps(_sanitize_reference_shape(dict(result)), indent=2, sort_keys=True, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    return final_path


def build_declared_portable_source_body_verification_post_invocation_command_execution_request(
    post_invocation_command_execution_request_id: str,
    post_invocation_command_execution_question: str,
    selected_post_invocation_command_execution_boundary_basis: Mapping[str, Any] | str,
    selected_post_invocation_command_execution_boundary_terminal_summary_basis: Mapping[str, Any] | str,
    selected_command_invocation_basis: Mapping[str, Any] | str,
    selected_command_invocation_terminal_summary_basis: Mapping[str, Any] | str,
    selected_command_execution_review_basis: Mapping[str, Any] | str,
    selected_request_consumption_basis: Mapping[str, Any] | str,
    selected_consumed_request_basis: Mapping[str, Any] | str,
    selected_v2_admitted_request_basis: Mapping[str, Any] | str,
    selected_v1_predecessor_failure_basis: Mapping[str, Any] | str,
    selected_older_command_execution_boundary_lineage_basis: Mapping[str, Any] | str,
    selected_command_report_basis: Mapping[str, Any] | str,
    selected_command_implementation_boundary_basis: Mapping[str, Any] | str,
    selected_command_boundary_basis: Mapping[str, Any] | str,
    selected_artifact_emission_containment_basis: Mapping[str, Any] | str,
    selected_evidence_manifest_basis: Mapping[str, Any] | str,
    selected_portable_verification_basis: Mapping[str, Any] | str,
    post_invocation_command_execution_only_posture: Mapping[str, Any] | str,
    one_bounded_command_execution_event_posture: Mapping[str, Any] | str,
    execution_trace_audit_only_posture: Mapping[str, Any] | str,
    no_command_output_posture: Mapping[str, Any] | str,
    no_command_result_posture: Mapping[str, Any] | str,
    no_command_success_posture: Mapping[str, Any] | str,
    no_execution_permission_posture: Mapping[str, Any] | str,
    no_execution_approval_posture: Mapping[str, Any] | str,
    no_standing_execution_lane_posture: Mapping[str, Any] | str,
    no_repeat_execution_permission_posture: Mapping[str, Any] | str,
    authorization_token_reuse_blocked_posture: Mapping[str, Any] | str,
    consumed_token_closed_posture: Mapping[str, Any] | str,
    no_reopen_consumed_request_posture: Mapping[str, Any] | str,
    returned_result_containment_posture: Mapping[str, Any] | str,
    post_invocation_command_execution_scope: Sequence[str] | Mapping[str, Any],
    post_invocation_command_execution_intent: str = INTENT_RECORD,
    **optional_fields: Any,
) -> dict[str, Any]:
    """Build a declared request with explicit false non-claims and no output/result/success inference."""

    request = {
        "post_invocation_command_execution_request_id": post_invocation_command_execution_request_id,
        "post_invocation_command_execution_question": post_invocation_command_execution_question,
        "post_invocation_command_execution_intent": post_invocation_command_execution_intent,
        "selected_post_invocation_command_execution_boundary_basis": _deepcopy(
            selected_post_invocation_command_execution_boundary_basis
        ),
        "selected_post_invocation_command_execution_boundary_terminal_summary_basis": _deepcopy(
            selected_post_invocation_command_execution_boundary_terminal_summary_basis
        ),
        "selected_command_invocation_basis": _deepcopy(selected_command_invocation_basis),
        "selected_command_invocation_terminal_summary_basis": _deepcopy(
            selected_command_invocation_terminal_summary_basis
        ),
        "selected_command_execution_review_basis": _deepcopy(selected_command_execution_review_basis),
        "selected_request_consumption_basis": _deepcopy(selected_request_consumption_basis),
        "selected_consumed_request_basis": _deepcopy(selected_consumed_request_basis),
        "selected_v2_admitted_request_basis": _deepcopy(selected_v2_admitted_request_basis),
        "selected_v1_predecessor_failure_basis": _deepcopy(selected_v1_predecessor_failure_basis),
        "selected_older_command_execution_boundary_lineage_basis": _deepcopy(
            selected_older_command_execution_boundary_lineage_basis
        ),
        "selected_command_report_basis": _deepcopy(selected_command_report_basis),
        "selected_command_implementation_boundary_basis": _deepcopy(
            selected_command_implementation_boundary_basis
        ),
        "selected_command_boundary_basis": _deepcopy(selected_command_boundary_basis),
        "selected_artifact_emission_containment_basis": _deepcopy(selected_artifact_emission_containment_basis),
        "selected_evidence_manifest_basis": _deepcopy(selected_evidence_manifest_basis),
        "selected_portable_verification_basis": _deepcopy(selected_portable_verification_basis),
        "post_invocation_command_execution_only_posture": _deepcopy(
            post_invocation_command_execution_only_posture
        ),
        "one_bounded_command_execution_event_posture": _deepcopy(one_bounded_command_execution_event_posture),
        "execution_trace_audit_only_posture": _deepcopy(execution_trace_audit_only_posture),
        "no_command_output_posture": _deepcopy(no_command_output_posture),
        "no_command_result_posture": _deepcopy(no_command_result_posture),
        "no_command_success_posture": _deepcopy(no_command_success_posture),
        "no_execution_permission_posture": _deepcopy(no_execution_permission_posture),
        "no_execution_approval_posture": _deepcopy(no_execution_approval_posture),
        "no_standing_execution_lane_posture": _deepcopy(no_standing_execution_lane_posture),
        "no_repeat_execution_permission_posture": _deepcopy(no_repeat_execution_permission_posture),
        "authorization_token_reuse_blocked_posture": _deepcopy(authorization_token_reuse_blocked_posture),
        "consumed_token_closed_posture": _deepcopy(consumed_token_closed_posture),
        "no_reopen_consumed_request_posture": _deepcopy(no_reopen_consumed_request_posture),
        "returned_result_containment_posture": _deepcopy(returned_result_containment_posture),
        "post_invocation_command_execution_scope": _deepcopy(post_invocation_command_execution_scope),
        "requested_post_invocation_command_execution_outcome": optional_fields.pop(
            "requested_post_invocation_command_execution_outcome",
            OUTCOME_RECORDED,
        ),
        "declared_non_claims": _default_non_claims(),
    }
    for key, value in optional_fields.items():
        if value is not None:
            request[key] = _deepcopy(value)
    return request
