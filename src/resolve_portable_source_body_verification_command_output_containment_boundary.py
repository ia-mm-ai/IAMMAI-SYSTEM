"""Bounded portable source-body verification command output containment boundary.

This module records command output containment boundary conditions only. It is
downstream of recorded post-invocation command execution and preserves one
recorded command execution event plus audit-only execution trace for one future
command output containment step.

It does not create command output, capture output, create a command output/report
artifact, create command result, create command success, create authority,
create currentness, create final completion, reopen the consumed request token,
reuse the spent one-shot authorization token, mutate artifacts, or authorize
follow-on work.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class PortableSourceBodyVerificationCommandOutputContainmentBoundaryError(Exception):
    """Raised for hard command output containment boundary resolver failures."""


RESOLVER_MODULE = "resolve_portable_source_body_verification_command_output_containment_boundary"
RESULT_VERSION = "0.1.0"
RESULT_TYPE = "portable_source_body_verification_command_output_containment_boundary_result"

PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_command_output_containment_boundary"
)
OUTPUT_ROOT = PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_ROOT

CORE_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_QUESTION = (
    "Can the recorded post-invocation command execution event and audit-only execution trace be "
    "bounded for one future command output containment step without creating command output, command "
    "result, command success, output capture, command output/report artifact, source, authority, "
    "currentness, final completion, continuation, reusable permission, derivative reception, vessel "
    "relation, another reception request, or follow-on work?"
)

INTENT_RECORD = "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY"
INTENT_BLOCK = "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY"
SUPPORTED_INTENTS = frozenset({INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK})

OUTCOME_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_RECORDED"
OUTCOME_NOT_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_BLOCKED"
COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_OUTCOME = OUTCOME_RECORDED
OUTCOME_FAMILY = frozenset(
    {
        OUTCOME_RECORDED,
        OUTCOME_NOT_RECORDED,
        OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        OUTCOME_BLOCKED,
    }
)

POST_INVOCATION_COMMAND_EXECUTION_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_RECORDED"
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

SUPPORTED_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_SCOPE = (
    "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_ONLY",
    "ONE_FUTURE_COMMAND_OUTPUT_CONTAINMENT_STEP_ONLY",
    "RECORDED_COMMAND_EXECUTION_EVENT_PRESERVED",
    "EXECUTION_TRACE_AUDIT_ONLY_PRESERVED",
    "COMMAND_OUTPUT_NOT_CREATED",
    "COMMAND_OUTPUT_CAPTURE_NOT_CREATED",
    "COMMAND_OUTPUT_REPORT_ARTIFACT_NOT_CREATED",
    "COMMAND_RESULT_NOT_CREATED",
    "COMMAND_SUCCESS_NOT_CREATED",
    "EXECUTION_TRACE_IS_NOT_OUTPUT",
    "EXECUTION_TRACE_IS_NOT_RESULT",
    "EXECUTION_TRACE_IS_NOT_SUCCESS",
    "EXECUTION_TRACE_IS_NOT_SOURCE",
    "EXECUTION_TRACE_IS_NOT_AUTHORITY",
    "COMMAND_OUTPUT_NOT_SOURCE",
    "COMMAND_RESULT_NOT_AUTHORITY",
    "COMMAND_SUCCESS_NOT_CURRENTNESS",
    "COMMAND_SUCCESS_NOT_FINAL_COMPLETION",
    "AUTHORIZATION_TOKEN_REUSE_BLOCKED",
    "CONSUMED_REQUEST_TOKEN_REMAINS_CLOSED",
    "CONSUMED_REQUEST_NOT_REOPENED",
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
SUPPORTED_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_SCOPE_SET = frozenset(
    SUPPORTED_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_SCOPE
)

REQUIRED_FALSE_NON_CLAIMS = (
    "command_output_created",
    "output_capture_created",
    "command_output_report_artifact_created",
    "command_result_created",
    "command_success_created",
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
    "authorization_token_reused",
    "consumed_request_reopened",
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
    "command_output_containment_boundary_recorded",
    "recorded_command_execution_event_preserved",
    "execution_trace_audit_only_preserved",
    "one_future_command_output_containment_step_declared",
    "command_output_still_not_created",
    "output_capture_not_created",
    "command_output_report_artifact_not_created",
    "command_result_still_not_created",
    "command_success_still_not_created",
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
        "output_body",
        "prior_artifact_body",
        "raw_full_artifact_body",
        "raw_full_prior_artifact_body",
        "raw_full_result",
        "raw_result",
        "result_body",
        "source_body",
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
        "output_body",
        "command_result",
        "command_result_body",
        "command_success",
        "command_success_body",
        "result_body",
        "success_body",
        "source_body",
        "authority_body",
        "currentness_claim",
        "final_completion_claim",
    }
)
EXECUTION_TRACE_BODY_OMISSION_MARKER = "[omitted: execution trace remains audit-only]"

BLOCK_CODES = frozenset(
    {
        "DECLARED_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_REQUEST_MALFORMED",
        "DECLARED_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_REQUEST_UNREADABLE",
        "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_QUESTION_UNDECLARED",
        "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_INTENT_UNSUPPORTED",
        "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_BLOCKED_BY_REQUEST",
        "POST_INVOCATION_COMMAND_EXECUTION_BASIS_MISSING",
        "POST_INVOCATION_COMMAND_EXECUTION_NOT_RECORDED",
        "POST_INVOCATION_COMMAND_EXECUTION_FAILED_CHECKS_PRESENT",
        "POST_INVOCATION_COMMAND_EXECUTION_EVENT_NOT_RECORDED",
        "POST_INVOCATION_COMMAND_EXECUTION_TRACE_NOT_AUDIT_ONLY",
        "POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_BASIS_MISSING",
        "POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_NOT_RECORDED",
        "COMMAND_INVOCATION_BASIS_MISSING",
        "COMMAND_EXECUTION_REVIEW_BASIS_MISSING",
        "REQUEST_CONSUMPTION_BASIS_MISSING",
        "CONSUMED_REQUEST_BASIS_MISSING",
        "COMMAND_OUTPUT_ALREADY_CREATED",
        "OUTPUT_CAPTURE_ALREADY_CREATED",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_ALREADY_CREATED",
        "COMMAND_RESULT_ALREADY_CREATED",
        "COMMAND_SUCCESS_ALREADY_CREATED",
        "EXECUTION_TRACE_TREATED_AS_OUTPUT",
        "EXECUTION_TRACE_TREATED_AS_RESULT",
        "EXECUTION_TRACE_TREATED_AS_SUCCESS",
        "EXECUTION_TRACE_TREATED_AS_SOURCE",
        "EXECUTION_TRACE_TREATED_AS_AUTHORITY",
        "COMMAND_OUTPUT_TREATED_AS_SOURCE",
        "COMMAND_RESULT_TREATED_AS_AUTHORITY",
        "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS",
        "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION",
        "CONSUMED_REQUEST_REOPENED",
        "AUTHORIZATION_TOKEN_REUSED",
        "V2_ADMITTED_REQUEST_BASIS_MISSING",
        "V2_ADMITTED_REQUEST_NOT_ADMITTED",
        "V2_ADMITTED_REQUEST_VERSION_NOT_0_2_0",
        "V2_ADMITTED_REQUEST_FAILED_CHECKS_PRESENT",
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
        "OUTPUT_CONTAINMENT_BOUNDARY_ONLY_POSTURE_MISSING",
        "ONE_FUTURE_COMMAND_OUTPUT_CONTAINMENT_STEP_POSTURE_MISSING",
        "EXECUTION_EVENT_PRESERVED_POSTURE_MISSING",
        "EXECUTION_TRACE_AUDIT_ONLY_POSTURE_MISSING",
        "NO_COMMAND_OUTPUT_POSTURE_MISSING",
        "NO_OUTPUT_CAPTURE_POSTURE_MISSING",
        "NO_OUTPUT_REPORT_ARTIFACT_POSTURE_MISSING",
        "NO_COMMAND_RESULT_POSTURE_MISSING",
        "NO_COMMAND_SUCCESS_POSTURE_MISSING",
        "NO_OUTPUT_AS_SOURCE_POSTURE_MISSING",
        "NO_RESULT_AS_AUTHORITY_POSTURE_MISSING",
        "NO_SUCCESS_AS_CURRENTNESS_POSTURE_MISSING",
        "NO_FINAL_COMPLETION_POSTURE_MISSING",
        "UNSUPPORTED_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_SCOPE",
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


def _mapping(value: Any) -> Mapping[str, Any]:
    if isinstance(value, Mapping):
        return value
    return {}


def _declared(value: Any) -> bool:
    return isinstance(value, Mapping) and bool(value)


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
                section[key] = _sanitize_reference_shape(item)
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


def _explicit_false(mapping: Mapping[str, Any], keys: Sequence[str]) -> bool:
    for key in keys:
        found = _find_first(mapping, (key,))
        if found is False:
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


def _reference_shaped_inputs_preserved(request: Mapping[str, Any]) -> bool:
    explicit = request.get("reference_shaped_input_posture")
    if isinstance(explicit, Mapping):
        if explicit.get("reference_shaped_input_posture_declared") is True:
            return True
        if explicit.get("reference_shaped_basis_required") is True:
            return True
    selected_keys = (
        "selected_post_invocation_command_execution_basis",
        "selected_post_invocation_command_execution_terminal_summary_basis",
        "selected_post_invocation_command_execution_boundary_basis",
        "selected_command_invocation_basis",
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


def _post_invocation_execution_event_recorded(
    execution: Mapping[str, Any],
    request: Mapping[str, Any],
) -> bool:
    if "selected_post_invocation_command_execution_event_recorded" in request:
        return request["selected_post_invocation_command_execution_event_recorded"] is True
    return _truthy(
        execution,
        (
            "post_invocation_command_execution_recorded",
            "bounded_command_execution_event_recorded",
            "execution_event_recorded",
            "one_bounded_command_execution_event_recorded",
        ),
    )


def _post_invocation_execution_trace_audit_only(
    execution: Mapping[str, Any],
    request: Mapping[str, Any],
) -> bool:
    if "selected_post_invocation_command_execution_trace_audit_only" in request:
        return request["selected_post_invocation_command_execution_trace_audit_only"] is True
    trace = _find_first(execution, ("execution_trace", "trace"))
    if _contains_forbidden_execution_trace_body_key(trace):
        return False
    if _truthy(
        execution,
        (
            "execution_trace_treated_as_output",
            "execution_trace_treated_as_result",
            "execution_trace_treated_as_success",
            "execution_trace_treated_as_source",
            "execution_trace_treated_as_authority",
        ),
    ):
        return False
    return _truthy(
        execution,
        (
            "execution_trace_recorded_as_audit_only",
            "execution_trace_audit_only_preserved",
            "execution_trace_audit_only",
            "trace_is_audit_only",
            "trace_is_not_output",
        ),
    )


def _not_created(
    basis: Mapping[str, Any],
    request: Mapping[str, Any],
    request_key: str,
    positive_keys: Sequence[str],
    negative_keys: Sequence[str],
) -> bool:
    if request_key in request:
        return request[request_key] is False
    if _truthy(basis, positive_keys):
        return False
    return _truthy(basis, negative_keys) or _explicit_false(basis, positive_keys)


def _execution_output_not_created(execution: Mapping[str, Any], request: Mapping[str, Any]) -> bool:
    return _not_created(
        execution,
        request,
        "selected_post_invocation_command_execution_output_created",
        ("command_output_created", "output_created"),
        ("command_output_still_not_created", "command_output_not_created", "output_not_created"),
    )


def _execution_result_not_created(execution: Mapping[str, Any], request: Mapping[str, Any]) -> bool:
    return _not_created(
        execution,
        request,
        "selected_post_invocation_command_execution_result_created",
        ("command_result_created", "result_created"),
        ("command_result_still_not_created", "command_result_not_created", "result_not_created"),
    )


def _execution_success_not_created(execution: Mapping[str, Any], request: Mapping[str, Any]) -> bool:
    return _not_created(
        execution,
        request,
        "selected_post_invocation_command_execution_success_created",
        ("command_success_created", "success_created"),
        ("command_success_still_not_created", "command_success_not_created", "success_not_created"),
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


def _v2_successor_metadata_present(v2_basis: Mapping[str, Any], request: Mapping[str, Any]) -> bool:
    explicit = request.get("selected_v2_successor_metadata")
    if isinstance(explicit, Mapping) and explicit:
        return True
    if _truthy(v2_basis, ("successor_metadata_preserved", "v2_successor_metadata_preserved")):
        return True
    successor_of = _find_first(v2_basis, ("successor_of", "predecessor_resolver_module"))
    successor_reason = _find_first(v2_basis, ("successor_reason", "successor_transition_reason"))
    resolver_module = _find_first(v2_basis, ("resolver_module",))
    return bool(successor_of and successor_reason and resolver_module)


def _execution_trace_not_overread(request: Mapping[str, Any], execution: Mapping[str, Any]) -> bool:
    trace = _find_first(execution, ("execution_trace", "trace"))
    if _contains_forbidden_execution_trace_body_key(trace):
        return False
    if _contains_forbidden_execution_trace_body_key(request.get("execution_trace")):
        return False
    overread_keys = (
        "execution_trace_treated_as_output",
        "execution_trace_treated_as_result",
        "execution_trace_treated_as_success",
        "execution_trace_treated_as_source",
        "execution_trace_treated_as_authority",
    )
    return not (
        _truthy(execution, overread_keys)
        or _truthy(_mapping(request.get("execution_trace")), overread_keys)
        or _truthy(request, overread_keys)
    )


COLLAPSE_TRUE_BLOCKS = (
    ("command_output_created", "COMMAND_OUTPUT_ALREADY_CREATED"),
    ("output_created", "COMMAND_OUTPUT_ALREADY_CREATED"),
    ("output_capture_created", "OUTPUT_CAPTURE_ALREADY_CREATED"),
    ("command_output_capture_created", "OUTPUT_CAPTURE_ALREADY_CREATED"),
    ("command_output_report_artifact_created", "COMMAND_OUTPUT_REPORT_ARTIFACT_ALREADY_CREATED"),
    ("output_report_artifact_created", "COMMAND_OUTPUT_REPORT_ARTIFACT_ALREADY_CREATED"),
    ("command_result_created", "COMMAND_RESULT_ALREADY_CREATED"),
    ("command_success_created", "COMMAND_SUCCESS_ALREADY_CREATED"),
    ("execution_trace_treated_as_output", "EXECUTION_TRACE_TREATED_AS_OUTPUT"),
    ("execution_trace_treated_as_result", "EXECUTION_TRACE_TREATED_AS_RESULT"),
    ("execution_trace_treated_as_success", "EXECUTION_TRACE_TREATED_AS_SUCCESS"),
    ("execution_trace_treated_as_source", "EXECUTION_TRACE_TREATED_AS_SOURCE"),
    ("execution_trace_treated_as_authority", "EXECUTION_TRACE_TREATED_AS_AUTHORITY"),
    ("command_output_became_source", "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
    ("command_output_treated_as_source", "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
    ("command_result_became_authority", "COMMAND_RESULT_TREATED_AS_AUTHORITY"),
    ("command_result_treated_as_authority", "COMMAND_RESULT_TREATED_AS_AUTHORITY"),
    ("command_success_created_currentness", "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
    ("command_success_treated_as_currentness", "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
    ("command_success_claimed_final_completion", "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
    ("command_success_treated_as_final_completion", "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
    ("authorization_token_reused", "AUTHORIZATION_TOKEN_REUSED"),
    ("authorization_token_reuse_created", "AUTHORIZATION_TOKEN_REUSED"),
    ("authorization_token_reuse_permitted", "AUTHORIZATION_TOKEN_REUSED"),
    ("consumed_request_reopened", "CONSUMED_REQUEST_REOPENED"),
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
            "declared command output containment boundary request mapping",
            False,
            "request is a mapping",
            "malformed",
            "DECLARED_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_REQUEST_MALFORMED",
        )
        return checks

    execution = _mapping(request.get("selected_post_invocation_command_execution_basis"))
    terminal_summary = request.get("selected_post_invocation_command_execution_terminal_summary_basis")
    boundary = _mapping(request.get("selected_post_invocation_command_execution_boundary_basis"))
    invocation = _mapping(request.get("selected_command_invocation_basis"))
    review = _mapping(request.get("selected_command_execution_review_basis"))
    consumption = _mapping(request.get("selected_request_consumption_basis"))
    consumed = _mapping(request.get("selected_consumed_request_basis"))
    v2 = _mapping(request.get("selected_v2_admitted_request_basis"))
    v1 = _mapping(request.get("selected_v1_predecessor_failure_basis"))
    lineage = _mapping(request.get("selected_older_command_execution_boundary_lineage_basis"))
    declared = _declared_non_claims(request)

    question = request.get("command_output_containment_boundary_question")
    intent = request.get("command_output_containment_boundary_intent")
    _check(
        checks,
        "command output containment boundary question declared",
        isinstance(question, str) and bool(question.strip()),
        "question declared",
        question,
        "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_QUESTION_UNDECLARED",
    )
    _check(
        checks,
        "command output containment boundary intent supported",
        intent in SUPPORTED_INTENTS,
        "supported intent",
        intent,
        "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_INTENT_UNSUPPORTED",
    )
    _check(
        checks,
        "post-invocation command execution terminal summary basis declared",
        _present(terminal_summary),
        "post-invocation command execution terminal summary basis declared",
        terminal_summary,
        "POST_INVOCATION_COMMAND_EXECUTION_BASIS_MISSING",
    )
    _check(
        checks,
        "post-invocation command execution live artifact basis declared",
        _declared(request.get("selected_post_invocation_command_execution_basis")),
        "post-invocation command execution live artifact basis declared",
        request.get("selected_post_invocation_command_execution_basis"),
        "POST_INVOCATION_COMMAND_EXECUTION_BASIS_MISSING",
    )
    execution_outcome = _outcome(
        execution,
        request,
        ("selected_post_invocation_command_execution_result_outcome",),
    )
    _check(
        checks,
        "post-invocation command execution outcome recorded",
        execution_outcome == POST_INVOCATION_COMMAND_EXECUTION_OUTCOME,
        POST_INVOCATION_COMMAND_EXECUTION_OUTCOME,
        execution_outcome,
        "POST_INVOCATION_COMMAND_EXECUTION_NOT_RECORDED",
    )
    execution_failed = _failed_count(
        execution,
        request,
        ("selected_post_invocation_command_execution_failed_check_count",),
    )
    _check(
        checks,
        "post-invocation command execution failed check count zero",
        execution_failed == 0,
        "failed_check_count == 0",
        execution_failed,
        "POST_INVOCATION_COMMAND_EXECUTION_FAILED_CHECKS_PRESENT",
    )
    _check(
        checks,
        "post-invocation command execution event recorded",
        _post_invocation_execution_event_recorded(execution, request),
        "one bounded execution event recorded",
        execution,
        "POST_INVOCATION_COMMAND_EXECUTION_EVENT_NOT_RECORDED",
    )
    _check(
        checks,
        "post-invocation command execution trace audit-only",
        _post_invocation_execution_trace_audit_only(execution, request),
        "execution trace recorded as audit-only",
        execution,
        "POST_INVOCATION_COMMAND_EXECUTION_TRACE_NOT_AUDIT_ONLY",
    )
    _check(
        checks,
        "post-invocation command execution command output not created",
        _execution_output_not_created(execution, request),
        "command output not created",
        execution,
        "COMMAND_OUTPUT_ALREADY_CREATED",
    )
    _check(
        checks,
        "post-invocation command execution command result not created",
        _execution_result_not_created(execution, request),
        "command result not created",
        execution,
        "COMMAND_RESULT_ALREADY_CREATED",
    )
    _check(
        checks,
        "post-invocation command execution command success not created",
        _execution_success_not_created(execution, request),
        "command success not created",
        execution,
        "COMMAND_SUCCESS_ALREADY_CREATED",
    )
    _check(
        checks,
        "post-invocation command execution boundary basis declared",
        _declared(request.get("selected_post_invocation_command_execution_boundary_basis")),
        "post-invocation command execution boundary basis declared",
        request.get("selected_post_invocation_command_execution_boundary_basis"),
        "POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_BASIS_MISSING",
    )
    boundary_outcome = _outcome(
        boundary,
        request,
        ("selected_post_invocation_command_execution_boundary_result_outcome",),
    )
    if boundary_outcome is not None:
        _check(
            checks,
            "post-invocation command execution boundary outcome recorded",
            boundary_outcome == POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_OUTCOME,
            POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_OUTCOME,
            boundary_outcome,
            "POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_NOT_RECORDED",
        )

    for name, key, code in (
        ("command invocation basis declared", "selected_command_invocation_basis", "COMMAND_INVOCATION_BASIS_MISSING"),
        (
            "command execution review basis declared",
            "selected_command_execution_review_basis",
            "COMMAND_EXECUTION_REVIEW_BASIS_MISSING",
        ),
        ("request consumption basis declared", "selected_request_consumption_basis", "REQUEST_CONSUMPTION_BASIS_MISSING"),
        ("consumed request basis declared", "selected_consumed_request_basis", "CONSUMED_REQUEST_BASIS_MISSING"),
    ):
        _check(checks, name, _declared(request.get(key)), "basis declared", request.get(key), code)

    _check(
        checks,
        "consumed request token remains closed",
        _consumed_token_closed(consumed),
        "consumed token closed",
        consumed,
        "CONSUMED_REQUEST_REOPENED",
    )
    _check(
        checks,
        "consumed request not reopened",
        _consumed_not_reopened(consumed),
        "consumed request not reopened",
        consumed,
        "CONSUMED_REQUEST_REOPENED",
    )

    _check(
        checks,
        "v2 admitted request basis declared",
        _declared(request.get("selected_v2_admitted_request_basis")),
        "v2 admitted request basis declared",
        request.get("selected_v2_admitted_request_basis"),
        "V2_ADMITTED_REQUEST_BASIS_MISSING",
    )
    v2_outcome = _outcome(v2, request, ("selected_v2_admitted_request_outcome",))
    if v2_outcome is not None:
        _check(
            checks,
            "v2 admitted request outcome admitted",
            v2_outcome == V2_ADMITTED_REQUEST_OUTCOME,
            V2_ADMITTED_REQUEST_OUTCOME,
            v2_outcome,
            "V2_ADMITTED_REQUEST_NOT_ADMITTED",
        )
    v2_version = _version(v2, request, ("selected_v2_admitted_request_version",))
    if v2_version is not None:
        _check(
            checks,
            "v2 admitted request version 0.2.0",
            v2_version == V2_ADMITTED_REQUEST_VERSION,
            V2_ADMITTED_REQUEST_VERSION,
            v2_version,
            "V2_ADMITTED_REQUEST_VERSION_NOT_0_2_0",
        )
    v2_failed = _failed_count(v2, request, ("selected_v2_failed_check_count",))
    if v2_failed is not None:
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
        "v2 successor metadata present",
        _v2_successor_metadata_present(v2, request)
        or _declared(request.get("selected_v2_admitted_request_basis")),
        "v2 successor metadata preserved",
        v2,
        "V2_ADMITTED_REQUEST_BASIS_MISSING",
    )

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
        "v2 not treated as repairing v1",
        not (_truthy(v1, ("v2_treated_as_repairing_v1", "v1_repaired")) or _truthy(v2, ("v2_treated_as_repairing_v1", "v1_repaired"))),
        "v2 does not repair v1",
        {"v1": v1, "v2": v2},
        "V2_TREATED_AS_REPAIRING_V1",
    )
    _check(checks, "v1 failure not hidden", not _truthy(v1, ("v1_hidden", "v1_failure_hidden")), "v1 failure not hidden", v1, "V1_FAILURE_HIDDEN")
    _check(
        checks,
        "v1 not claimed passed",
        not (_truthy(v1, ("v1_claimed_passed", "v1_passed")) or _truthy(v2, ("v2_claims_v1_passed", "v1_claimed_passed", "v1_passed"))),
        "v1 not claimed passed",
        {"v1": v1, "v2": v2},
        "V1_CLAIMED_PASSED",
    )

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
        "older command execution boundary lineage basis prior scaffolding only",
        not _lineage_as_current_execution(lineage),
        "older command execution boundary lineage remains prior scaffolding only",
        lineage,
        "OLDER_COMMAND_EXECUTION_BOUNDARY_LINEAGE_TREATED_AS_CURRENT_EXECUTION",
    )

    for name, key, code in (
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
    ):
        _check(checks, name, _declared(request.get(key)), "basis declared", request.get(key), code)

    for name, key, code, flags in (
        ("output-containment-boundary-only posture declared", "output_containment_boundary_only_posture", "OUTPUT_CONTAINMENT_BOUNDARY_ONLY_POSTURE_MISSING", ("output_containment_boundary_only", "command_output_containment_boundary_only")),
        ("one-future-command-output-containment-step posture declared", "one_future_command_output_containment_step_posture", "ONE_FUTURE_COMMAND_OUTPUT_CONTAINMENT_STEP_POSTURE_MISSING", ("one_future_command_output_containment_step_declared", "one_future_command_output_containment_step_only")),
        ("execution-event-preserved posture declared", "execution_event_preserved_posture", "EXECUTION_EVENT_PRESERVED_POSTURE_MISSING", ("recorded_command_execution_event_preserved", "execution_event_preserved")),
        ("execution-trace-audit-only posture declared", "execution_trace_audit_only_posture", "EXECUTION_TRACE_AUDIT_ONLY_POSTURE_MISSING", ("execution_trace_audit_only_preserved", "execution_trace_audit_only", "trace_is_audit_only")),
        ("no-command-output posture declared", "no_command_output_posture", "NO_COMMAND_OUTPUT_POSTURE_MISSING", ("command_output_not_created", "command_output_still_not_created")),
        ("no-output-capture posture declared", "no_output_capture_posture", "NO_OUTPUT_CAPTURE_POSTURE_MISSING", ("output_capture_not_created", "command_output_capture_not_created")),
        ("no-output-report-artifact posture declared", "no_output_report_artifact_posture", "NO_OUTPUT_REPORT_ARTIFACT_POSTURE_MISSING", ("command_output_report_artifact_not_created", "output_report_artifact_not_created")),
        ("no-command-result posture declared", "no_command_result_posture", "NO_COMMAND_RESULT_POSTURE_MISSING", ("command_result_not_created", "command_result_still_not_created")),
        ("no-command-success posture declared", "no_command_success_posture", "NO_COMMAND_SUCCESS_POSTURE_MISSING", ("command_success_not_created", "command_success_still_not_created")),
        ("no-output-as-source posture declared", "no_output_as_source_posture", "NO_OUTPUT_AS_SOURCE_POSTURE_MISSING", ("command_output_not_source", "output_not_source")),
        ("no-result-as-authority posture declared", "no_result_as_authority_posture", "NO_RESULT_AS_AUTHORITY_POSTURE_MISSING", ("command_result_not_authority", "result_not_authority")),
        ("no-success-as-currentness posture declared", "no_success_as_currentness_posture", "NO_SUCCESS_AS_CURRENTNESS_POSTURE_MISSING", ("command_success_not_currentness", "success_not_currentness")),
        ("no-final-completion posture declared", "no_final_completion_posture", "NO_FINAL_COMPLETION_POSTURE_MISSING", ("no_final_completion", "final_completion_not_claimed")),
        ("authorization-token-reuse-blocked posture declared", "authorization_token_reuse_blocked_posture", "AUTHORIZATION_TOKEN_REUSED", ("authorization_token_reuse_blocked", "authorization_token_not_reused")),
        ("consumed-token-closed posture declared", "consumed_token_closed_posture", "CONSUMED_REQUEST_REOPENED", ("consumed_request_token_remains_closed", "consumed_token_closed")),
        ("no-reopen-consumed-request posture declared", "no_reopen_consumed_request_posture", "CONSUMED_REQUEST_REOPENED", ("consumed_request_not_reopened", "no_reopen_consumed_request")),
        ("returned-result containment posture declared", "returned_result_containment_posture", "FULL_PRIOR_ARTIFACT_BODY_EMITTED", ("returned_result_containment_preserved", "no_raw_full_prior_artifact_body_returned")),
    ):
        _check(checks, name, _posture_declared(request.get(key), flags), "posture declared", request.get(key), code)

    scope = _scope_values(request.get("command_output_containment_boundary_scope"))
    _check(
        checks,
        "command output containment boundary scope supported",
        bool(scope) and all(value in SUPPORTED_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_SCOPE_SET for value in scope),
        "supported scope",
        scope,
        "UNSUPPORTED_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_SCOPE",
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
        "execution trace not output result success source authority",
        _execution_trace_not_overread(request, execution),
        "execution trace is audit-only and not output/result/success/source/authority",
        execution,
        "EXECUTION_TRACE_TREATED_AS_OUTPUT",
    )

    collapse = _first_collapse(
        (
            request,
            declared,
            execution,
            boundary,
            invocation,
            review,
            consumption,
            consumed,
            v2,
            v1,
            lineage,
            _mapping(request.get("output_containment_boundary_only_posture")),
            _mapping(request.get("one_future_command_output_containment_step_posture")),
            _mapping(request.get("execution_event_preserved_posture")),
            _mapping(request.get("execution_trace_audit_only_posture")),
            _mapping(request.get("no_command_output_posture")),
            _mapping(request.get("no_output_capture_posture")),
            _mapping(request.get("no_output_report_artifact_posture")),
            _mapping(request.get("no_command_result_posture")),
            _mapping(request.get("no_command_success_posture")),
            _mapping(request.get("no_output_as_source_posture")),
            _mapping(request.get("no_result_as_authority_posture")),
            _mapping(request.get("no_success_as_currentness_posture")),
            _mapping(request.get("no_final_completion_posture")),
            _mapping(request.get("authorization_token_reuse_blocked_posture")),
            _mapping(request.get("no_reopen_consumed_request_posture")),
        )
    )
    _check(
        checks,
        "collapse flags absent",
        collapse is None,
        "no output/capture/report/result/success/source/authority/currentness/final-completion/follow-on flags",
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
    intent = request.get("command_output_containment_boundary_intent")
    if intent == INTENT_BLOCK:
        return OUTCOME_BLOCKED, "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_BLOCKED_BY_REQUEST", str(
            request.get("block_reason") or "blocked by request intent"
        )
    if intent not in SUPPORTED_INTENTS:
        return OUTCOME_BLOCKED, "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_INTENT_UNSUPPORTED", (
            "unsupported command output containment boundary intent"
        )
    requested = request.get("requested_command_output_containment_boundary_outcome", OUTCOME_RECORDED)
    if requested == OUTCOME_BLOCKED:
        return OUTCOME_BLOCKED, "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_BLOCKED_BY_REQUEST", str(
            request.get("block_reason") or "blocked by requested outcome"
        )
    if requested not in OUTCOME_FAMILY:
        return OUTCOME_BLOCKED, "DECLARED_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_REQUEST_MALFORMED", (
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
            "command_output_containment_boundary_not_recorded": outcome == OUTCOME_NOT_RECORDED,
            "command_output_containment_boundary_requires_additional_basis": outcome
            == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "command_output_containment_boundary_blocked": outcome == OUTCOME_BLOCKED,
            "command_output_containment_boundary_is_not_command_output": True,
            "command_output_containment_boundary_is_not_command_result": True,
            "command_output_containment_boundary_is_not_command_success": True,
            "command_output_containment_boundary_is_not_output_capture": True,
            "command_output_containment_boundary_is_not_output_report_artifact": True,
            "execution_trace_is_audit_only": True,
            "execution_trace_is_not_command_output": True,
            "execution_trace_is_not_command_result": True,
            "execution_trace_is_not_command_success": True,
            "execution_trace_is_not_source": True,
            "execution_trace_is_not_authority": True,
            "output_is_not_source": True,
            "result_is_not_authority": True,
            "success_is_not_currentness": True,
            "success_is_not_final_completion": True,
            "older_command_execution_boundary_lineage_is_not_current_execution": True,
        }
    )
    return statement


def _non_meaning() -> dict[str, bool]:
    names = (
        "command_output_exists",
        "output_was_captured",
        "command_output_report_artifact_exists",
        "command_result_exists",
        "command_success_exists",
        "execution_trace_is_output",
        "execution_trace_is_result",
        "execution_trace_is_success",
        "execution_trace_is_source",
        "execution_trace_is_authority",
        "output_is_source",
        "result_is_authority",
        "success_is_currentness",
        "success_is_final_completion",
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
    return {f"command_output_containment_boundary_does_not_mean_{name}": True for name in names}


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "command_output_containment_boundary_test",
            "command_output_containment_boundary_live_artifact",
            "command_output_step_if_separately_specified",
            "command_output",
            "output_capture",
            "command_output_report_artifact",
            "command_result",
            "command_success",
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
    unsupported = [value for value in values if value not in SUPPORTED_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_SCOPE_SET]
    return {
        "selected_scope_values": values,
        "supported_scope_values": list(SUPPORTED_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_SCOPE),
        "unsupported_scope_values": unsupported,
        "all_selected_scope_values_supported": bool(values) and not unsupported,
        "command_output_containment_boundary_only": "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_ONLY" in values,
        "one_future_command_output_containment_step_declared": outcome == OUTCOME_RECORDED,
        "recorded_command_execution_event_preserved": outcome == OUTCOME_RECORDED,
        "execution_trace_audit_only_preserved": True,
        "command_output_not_created": True,
        "output_capture_not_created": True,
        "command_output_report_artifact_not_created": True,
        "command_result_not_created": True,
        "command_success_not_created": True,
        "execution_trace_is_not_output_result_success_source_authority": True,
        "command_output_not_source": True,
        "command_result_not_authority": True,
        "command_success_not_currentness": True,
        "command_success_not_final_completion": True,
        "authorization_token_reuse_blocked": True,
        "consumed_request_token_remains_closed": True,
        "consumed_request_not_reopened": True,
        "no_authority_currentness_final_completion_continuation_reusable_follow_on": True,
        "v1_predecessor_failure_remains_visible": True,
        "v2_successor_does_not_repair_v1": True,
        "returned_result_containment_preserved": True,
        "reference_shaped_basis_required": True,
        "full_prior_artifact_body_not_emitted": True,
    }


def _metadata(request: Mapping[str, Any], outcome: str) -> dict[str, Any]:
    request_id = str(request.get("command_output_containment_boundary_request_id") or "undeclared")
    return {
        "portable_source_body_verification_command_output_containment_boundary_result_id": (
            f"{request_id}__portable_source_body_verification_command_output_containment_boundary_result"
        ),
        "portable_source_body_verification_command_output_containment_boundary_result_type": RESULT_TYPE,
        "portable_source_body_verification_command_output_containment_boundary_result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
        "command_output_containment_boundary_request_id": request_id,
        "naming_containment": {
            "short_resolver_filename_used_intentionally": True,
            "short_filename_does_not_erase_upstream_lineage": True,
            "full_upstream_lineage_preserved_in_selected_basis": True,
            "command_output_containment_boundary_filename_distinct_from_execution_and_output_surfaces": True,
        },
        "lineage_posture": {
            "downstream_of_recorded_post_invocation_command_execution": True,
            "downstream_of_recorded_command_invocation": True,
            "downstream_of_post_invocation_command_execution_boundary": True,
            "older_command_execution_boundary_surfaces_remain_lineage_only": True,
        },
        "requested_outcome": request.get("requested_command_output_containment_boundary_outcome"),
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
        "additional_basis_does_not_create_output_capture_report_result_success": True,
        "additional_basis_does_not_create_authority_currentness_final_completion": True,
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
        "not_recorded_does_not_create_command_output": True,
        "not_recorded_does_not_capture_output": True,
        "not_recorded_does_not_create_output_report_artifact": True,
        "not_recorded_does_not_create_command_result": True,
        "not_recorded_does_not_create_command_success": True,
        "not_recorded_does_not_authorize_next_work": True,
    }
    return additional, not_recorded


def build_portable_source_body_verification_command_output_containment_boundary_summary(
    result: Mapping[str, Any]
) -> dict[str, Any]:
    """Build a bounded command output containment boundary summary."""

    statement = _mapping(result.get("command_output_containment_boundary_statement"))
    block = _mapping(result.get("block"))
    metadata = _mapping(result.get("portable_source_body_verification_command_output_containment_boundary_metadata"))
    question = _mapping(result.get("declared_command_output_containment_boundary_question"))
    non_claims = _mapping(result.get("non_claims"))
    checks = [
        check for check in result.get("command_output_containment_boundary_checks", []) if isinstance(check, Mapping)
    ]
    passed, failed = _counts(checks)
    execution = _mapping(result.get("selected_post_invocation_command_execution_basis"))
    v2 = _mapping(result.get("selected_v2_admitted_request_basis"))
    lineage = _mapping(result.get("selected_older_command_execution_boundary_lineage_basis"))
    outcome = result.get("outcome")
    return {
        "outcome": outcome,
        "block_code": block.get("code"),
        "block_reason": block.get("reason"),
        "request_id": metadata.get("command_output_containment_boundary_request_id"),
        "question": question.get("question"),
        "intent": question.get("intent"),
        "passed_check_count": passed,
        "failed_check_count": failed,
        "command_output_containment_boundary_recorded": statement.get(
            "command_output_containment_boundary_recorded"
        )
        is True,
        "recorded_command_execution_event_preserved": statement.get(
            "recorded_command_execution_event_preserved"
        )
        is True,
        "execution_trace_audit_only_preserved": statement.get("execution_trace_audit_only_preserved") is True,
        "one_future_output_containment_step_declared": statement.get(
            "one_future_command_output_containment_step_declared"
        )
        is True,
        "command_output_still_not_created": statement.get("command_output_still_not_created") is True,
        "output_capture_not_created": statement.get("output_capture_not_created") is True,
        "output_report_artifact_not_created": statement.get("command_output_report_artifact_not_created") is True,
        "command_result_still_not_created": statement.get("command_result_still_not_created") is True,
        "command_success_still_not_created": statement.get("command_success_still_not_created") is True,
        "not_recorded": outcome == OUTCOME_NOT_RECORDED,
        "requires_additional_basis": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "selected_post_invocation_execution_outcome": _find_first(execution, ("outcome", "result_outcome")),
        "selected_post_invocation_execution_failed_check_count": _find_first(
            execution, ("failed_check_count", "selected_failed_check_count")
        ),
        "selected_v2_admitted_request_outcome": _find_first(v2, ("outcome", "result_outcome", "selected_outcome")),
        "selected_v2_admitted_request_version": _find_first(v2, ("result_version", "version", "selected_version")),
        "selected_v2_admitted_request_failed_check_count": _find_first(
            v2, ("failed_check_count", "selected_failed_check_count")
        ),
        "execution_trace_not_output_result_success_source_authority": all(
            statement.get(key) is True
            for key in (
                "execution_trace_is_not_command_output",
                "execution_trace_is_not_command_result",
                "execution_trace_is_not_command_success",
                "execution_trace_is_not_source",
                "execution_trace_is_not_authority",
            )
        ),
        "output_not_source": statement.get("output_is_not_source") is True,
        "result_not_authority": statement.get("result_is_not_authority") is True,
        "success_not_currentness": statement.get("success_is_not_currentness") is True,
        "success_not_final_completion": statement.get("success_is_not_final_completion") is True,
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
        metadata["declared_command_output_containment_boundary_request_path"] = request_path
    statement = _statement(outcome)
    non_claims = _default_non_claims()
    additional, not_recorded = _open_posture(outcome, request, checks)
    result = {
        "portable_source_body_verification_command_output_containment_boundary_metadata": metadata,
        "declared_command_output_containment_boundary_question": {
            "question": request.get("command_output_containment_boundary_question"),
            "expected_question": CORE_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_QUESTION,
            "intent": request.get("command_output_containment_boundary_intent"),
            "command_output_containment_boundary_is_not_command_output": True,
            "command_output_containment_boundary_is_not_command_result": True,
            "command_output_containment_boundary_is_not_command_success": True,
            "command_output_containment_boundary_is_not_output_capture": True,
            "command_output_containment_boundary_is_not_output_report_artifact": True,
        },
        "selected_post_invocation_command_execution_basis": _basis_section(
            request.get("selected_post_invocation_command_execution_basis"),
            path=request.get("selected_post_invocation_command_execution_result_path"),
            extra={
                "selected_result_id": request.get("selected_post_invocation_command_execution_result_id"),
                "selected_result_outcome": request.get("selected_post_invocation_command_execution_result_outcome"),
                "selected_failed_check_count": request.get(
                    "selected_post_invocation_command_execution_failed_check_count"
                ),
                "selected_execution_event_recorded": request.get(
                    "selected_post_invocation_command_execution_event_recorded"
                ),
                "selected_execution_trace_audit_only": request.get(
                    "selected_post_invocation_command_execution_trace_audit_only"
                ),
                "selected_command_output_created": request.get(
                    "selected_post_invocation_command_execution_output_created"
                ),
                "selected_command_result_created": request.get(
                    "selected_post_invocation_command_execution_result_created"
                ),
                "selected_command_success_created": request.get(
                    "selected_post_invocation_command_execution_success_created"
                ),
                "execution_basis_remains_execution_basis_only": True,
                "execution_trace_remains_audit_only": True,
                "execution_trace_is_not_output_result_success_source_authority": True,
            },
        ),
        "selected_post_invocation_command_execution_terminal_summary_basis": _basis_section(
            request.get("selected_post_invocation_command_execution_terminal_summary_basis"),
            path=request.get("selected_post_invocation_command_execution_terminal_summary_path"),
            extra={"terminal_summary_remains_readability_basis_only": True},
        ),
        "selected_post_invocation_command_execution_boundary_basis": _basis_section(
            request.get("selected_post_invocation_command_execution_boundary_basis"),
            path=request.get("selected_post_invocation_command_execution_boundary_result_path"),
            extra={"boundary_basis_remains_boundary_basis_only": True},
        ),
        "selected_command_invocation_basis": _basis_section(
            request.get("selected_command_invocation_basis"),
            path=request.get("selected_command_invocation_result_path"),
            extra={"command_invocation_basis_remains_invocation_basis_only": True},
        ),
        "selected_command_execution_review_basis": _basis_section(
            request.get("selected_command_execution_review_basis"),
            path=request.get("selected_command_execution_review_result_path"),
            extra={"review_basis_remains_review_basis_only": True},
        ),
        "selected_request_consumption_basis": _basis_section(
            request.get("selected_request_consumption_basis"),
            path=request.get("selected_request_consumption_result_path"),
            extra={"request_consumption_basis_only": True},
        ),
        "selected_consumed_request_basis": _basis_section(
            request.get("selected_consumed_request_basis"),
            extra={"consumed_request_token_remains_closed": True, "consumed_request_not_reopened": True},
        ),
        "selected_v2_admitted_request_basis": _basis_section(
            request.get("selected_v2_admitted_request_basis"),
            path=request.get("selected_v2_admitted_request_artifact_path"),
            extra={
                "selected_outcome": request.get("selected_v2_admitted_request_outcome"),
                "selected_version": request.get("selected_v2_admitted_request_version"),
                "selected_failed_check_count": request.get("selected_v2_failed_check_count"),
                "v2_remains_lineage_evidence_only": True,
                "v2_does_not_claim_v1_passed": True,
            },
        ),
        "selected_v1_predecessor_failure_basis": _basis_section(
            request.get("selected_v1_predecessor_failure_basis"),
            path=request.get("selected_v1_predecessor_artifact_path"),
            extra={
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
        "output_containment_boundary_only_posture": _basis_section(
            request.get("output_containment_boundary_only_posture"),
            extra={"output_containment_boundary_only": True, "boundary_is_not_output_result_success": True},
        ),
        "one_future_command_output_containment_step_posture": _basis_section(
            request.get("one_future_command_output_containment_step_posture"),
            extra={"one_future_command_output_containment_step_declared": outcome == OUTCOME_RECORDED},
        ),
        "execution_event_preserved_posture": _basis_section(
            request.get("execution_event_preserved_posture"),
            extra={"recorded_command_execution_event_preserved": outcome == OUTCOME_RECORDED},
        ),
        "execution_trace_audit_only_posture": _basis_section(
            request.get("execution_trace_audit_only_posture"),
            extra={"execution_trace_audit_only_preserved": outcome == OUTCOME_RECORDED},
        ),
        "no_command_output_posture": _basis_section(
            request.get("no_command_output_posture"), extra={"command_output_created": False}
        ),
        "no_output_capture_posture": _basis_section(
            request.get("no_output_capture_posture"), extra={"output_capture_created": False}
        ),
        "no_output_report_artifact_posture": _basis_section(
            request.get("no_output_report_artifact_posture"),
            extra={"command_output_report_artifact_created": False},
        ),
        "no_command_result_posture": _basis_section(
            request.get("no_command_result_posture"), extra={"command_result_created": False}
        ),
        "no_command_success_posture": _basis_section(
            request.get("no_command_success_posture"), extra={"command_success_created": False}
        ),
        "no_output_as_source_posture": _basis_section(
            request.get("no_output_as_source_posture"), extra={"command_output_became_source": False}
        ),
        "no_result_as_authority_posture": _basis_section(
            request.get("no_result_as_authority_posture"), extra={"command_result_became_authority": False}
        ),
        "no_success_as_currentness_posture": _basis_section(
            request.get("no_success_as_currentness_posture"),
            extra={"command_success_created_currentness": False},
        ),
        "no_final_completion_posture": _basis_section(
            request.get("no_final_completion_posture"),
            extra={"command_success_claimed_final_completion": False, "final_completion_claimed": False},
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
        "command_output_containment_boundary_scope": _scope_section(
            request.get("command_output_containment_boundary_scope"), outcome
        ),
        "command_output_containment_boundary_checks": _sanitize_reference_shape(list(checks)),
        "command_output_containment_boundary_statement": statement,
        "command_output_containment_boundary_non_meaning": _non_meaning(),
        "additional_basis_required": additional,
        "not_recorded_basis": not_recorded,
        "what_remains_open": _what_remains_open(),
        "non_claims": non_claims,
        "outcome": outcome,
        "block": {"code": block_code, "reason": block_reason},
    }
    result["portable_source_body_verification_command_output_containment_boundary_summary"] = (
        build_portable_source_body_verification_command_output_containment_boundary_summary(result)
    )
    return result


def resolve_portable_source_body_verification_command_output_containment_boundary(
    declared_command_output_containment_boundary_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded command output containment boundary request."""

    if declared_command_output_containment_boundary_request is None:
        request: Mapping[str, Any] = {}
        checks = _build_checks(request)
        outcome, code, reason = _select_outcome(
            request,
            checks,
            "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_QUESTION_UNDECLARED",
        )
        return _build_result(request, checks=checks, outcome=outcome, block_code=code, block_reason=reason)
    if not isinstance(declared_command_output_containment_boundary_request, Mapping):
        request = {}
        checks = _build_checks(request, malformed=True)
        outcome, code, reason = _select_outcome(
            request,
            checks,
            "DECLARED_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_REQUEST_MALFORMED",
        )
        return _build_result(request, checks=checks, outcome=outcome, block_code=code, block_reason=reason)
    request = _deepcopy(declared_command_output_containment_boundary_request)
    checks = _build_checks(request)
    outcome, code, reason = _select_outcome(request, checks)
    return _build_result(request, checks=checks, outcome=outcome, block_code=code, block_reason=reason)


def resolve_portable_source_body_verification_command_output_containment_boundary_from_path(
    declared_command_output_containment_boundary_request_path: Path | str,
) -> dict[str, Any]:
    """Resolve one command output containment boundary request loaded from a JSON object path."""

    path = Path(declared_command_output_containment_boundary_request_path)
    try:
        loaded = json.loads(path.read_text(encoding="utf-8"))
    except OSError:
        request = {"command_output_containment_boundary_request_id": "unreadable_path"}
        checks = _build_checks(request)
        outcome, code, reason = _select_outcome(
            request,
            checks,
            "DECLARED_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_REQUEST_UNREADABLE",
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
        request = {"command_output_containment_boundary_request_id": "malformed_json"}
        checks = _build_checks(request)
        outcome, code, reason = _select_outcome(
            request,
            checks,
            "DECLARED_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_REQUEST_MALFORMED",
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
        request = {"command_output_containment_boundary_request_id": "non_object_json"}
        checks = _build_checks(request, malformed=True)
        outcome, code, reason = _select_outcome(
            request,
            checks,
            "DECLARED_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_REQUEST_MALFORMED",
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
    raise PortableSourceBodyVerificationCommandOutputContainmentBoundaryError(
        "unable to allocate non-overwriting command output containment boundary result path"
    )


def write_portable_source_body_verification_command_output_containment_boundary_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a command output containment boundary result JSON without silently overwriting."""

    if output_path is None:
        metadata = _mapping(result.get("portable_source_body_verification_command_output_containment_boundary_metadata"))
        request_id = (
            metadata.get("command_output_containment_boundary_request_id")
            or "undeclared_command_output_containment_boundary_request"
        )
        filename = (
            f"{_safe_component(request_id, 'undeclared_command_output_containment_boundary_request')}"
            "__portable_source_body_verification_command_output_containment_boundary_result.json"
        )
        path = PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_ROOT / filename
    else:
        path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    final_path = _deduplicated_output_path(path)
    final_path.write_text(
        json.dumps(_sanitize_reference_shape(dict(result)), indent=2, sort_keys=True, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    return final_path


def build_declared_portable_source_body_verification_command_output_containment_boundary_request(
    command_output_containment_boundary_request_id: str,
    command_output_containment_boundary_question: str,
    selected_post_invocation_command_execution_basis: Mapping[str, Any] | str,
    selected_post_invocation_command_execution_terminal_summary_basis: Mapping[str, Any] | str,
    selected_post_invocation_command_execution_boundary_basis: Mapping[str, Any] | str,
    selected_command_invocation_basis: Mapping[str, Any] | str,
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
    output_containment_boundary_only_posture: Mapping[str, Any] | str,
    one_future_command_output_containment_step_posture: Mapping[str, Any] | str,
    execution_event_preserved_posture: Mapping[str, Any] | str,
    execution_trace_audit_only_posture: Mapping[str, Any] | str,
    no_command_output_posture: Mapping[str, Any] | str,
    no_output_capture_posture: Mapping[str, Any] | str,
    no_output_report_artifact_posture: Mapping[str, Any] | str,
    no_command_result_posture: Mapping[str, Any] | str,
    no_command_success_posture: Mapping[str, Any] | str,
    no_output_as_source_posture: Mapping[str, Any] | str,
    no_result_as_authority_posture: Mapping[str, Any] | str,
    no_success_as_currentness_posture: Mapping[str, Any] | str,
    no_final_completion_posture: Mapping[str, Any] | str,
    authorization_token_reuse_blocked_posture: Mapping[str, Any] | str,
    consumed_token_closed_posture: Mapping[str, Any] | str,
    no_reopen_consumed_request_posture: Mapping[str, Any] | str,
    returned_result_containment_posture: Mapping[str, Any] | str,
    command_output_containment_boundary_scope: Sequence[str] | Mapping[str, Any],
    command_output_containment_boundary_intent: str = INTENT_RECORD,
    **optional_fields: Any,
) -> dict[str, Any]:
    """Build a declared request with explicit false non-claims and no output/result/success inference."""

    request = {
        "command_output_containment_boundary_request_id": command_output_containment_boundary_request_id,
        "command_output_containment_boundary_question": command_output_containment_boundary_question,
        "command_output_containment_boundary_intent": command_output_containment_boundary_intent,
        "selected_post_invocation_command_execution_basis": _deepcopy(
            selected_post_invocation_command_execution_basis
        ),
        "selected_post_invocation_command_execution_terminal_summary_basis": _deepcopy(
            selected_post_invocation_command_execution_terminal_summary_basis
        ),
        "selected_post_invocation_command_execution_boundary_basis": _deepcopy(
            selected_post_invocation_command_execution_boundary_basis
        ),
        "selected_command_invocation_basis": _deepcopy(selected_command_invocation_basis),
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
        "output_containment_boundary_only_posture": _deepcopy(output_containment_boundary_only_posture),
        "one_future_command_output_containment_step_posture": _deepcopy(
            one_future_command_output_containment_step_posture
        ),
        "execution_event_preserved_posture": _deepcopy(execution_event_preserved_posture),
        "execution_trace_audit_only_posture": _deepcopy(execution_trace_audit_only_posture),
        "no_command_output_posture": _deepcopy(no_command_output_posture),
        "no_output_capture_posture": _deepcopy(no_output_capture_posture),
        "no_output_report_artifact_posture": _deepcopy(no_output_report_artifact_posture),
        "no_command_result_posture": _deepcopy(no_command_result_posture),
        "no_command_success_posture": _deepcopy(no_command_success_posture),
        "no_output_as_source_posture": _deepcopy(no_output_as_source_posture),
        "no_result_as_authority_posture": _deepcopy(no_result_as_authority_posture),
        "no_success_as_currentness_posture": _deepcopy(no_success_as_currentness_posture),
        "no_final_completion_posture": _deepcopy(no_final_completion_posture),
        "authorization_token_reuse_blocked_posture": _deepcopy(authorization_token_reuse_blocked_posture),
        "consumed_token_closed_posture": _deepcopy(consumed_token_closed_posture),
        "no_reopen_consumed_request_posture": _deepcopy(no_reopen_consumed_request_posture),
        "returned_result_containment_posture": _deepcopy(returned_result_containment_posture),
        "command_output_containment_boundary_scope": _deepcopy(command_output_containment_boundary_scope),
        "requested_command_output_containment_boundary_outcome": optional_fields.pop(
            "requested_command_output_containment_boundary_outcome",
            OUTCOME_RECORDED,
        ),
        "declared_non_claims": _default_non_claims(),
    }
    for key, value in optional_fields.items():
        if value is not None:
            request[key] = _deepcopy(value)
    return request
