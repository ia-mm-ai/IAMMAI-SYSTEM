"""Portable source-body verification output capture resolver.

This module records one bounded output-capture event/posture downstream of the
recorded output capture boundary. It may preserve explicit absence/null posture
for stdout, stderr, process output, and raw output body. It does not invent raw
output content, create a command output/report artifact, create command result,
create command success, create source, create authority, create currentness,
create final completion, reopen a consumed request token, reuse a spent
one-shot authorization token, mutate artifacts, or authorize follow-on work.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


class PortableSourceBodyVerificationOutputCaptureError(Exception):
    """Raised for hard output-capture resolver failures."""


RESOLVER_MODULE = "resolve_portable_source_body_verification_output_capture"
RESULT_VERSION = "0.1.0"
RESULT_TYPE = "portable_source_body_verification_output_capture_result"

PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_output_capture"
)
OUTPUT_ROOT = PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_ROOT

CORE_OUTPUT_CAPTURE_QUESTION = (
    "Can the recorded output capture boundary basis be used to record one bounded output "
    "capture event without inventing stdout, stderr, process output, raw command output body, "
    "creating command output/report artifact, creating command result, creating command success, "
    "source, authority, currentness, final completion, continuation, reusable permission, "
    "derivative reception, vessel relation, another reception request, or follow-on work?"
)

INTENT_RECORD = "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE"
INTENT_BLOCK = "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE"
SUPPORTED_INTENTS = frozenset({INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK})

OUTCOME_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_RECORDED"
OUTCOME_NOT_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_BLOCKED"
OUTPUT_CAPTURE_OUTCOME = OUTCOME_RECORDED
OUTCOME_FAMILY = frozenset(
    {OUTCOME_RECORDED, OUTCOME_NOT_RECORDED, OUTCOME_REQUIRES_ADDITIONAL_BASIS, OUTCOME_BLOCKED}
)

OUTPUT_CAPTURE_BOUNDARY_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_BOUNDARY_RECORDED"
)
COMMAND_OUTPUT_OUTCOME = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_RECORDED"
COMMAND_OUTPUT_BOUNDARY_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_BOUNDARY_RECORDED"
)
COMMAND_OUTPUT_CONTAINMENT_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_CONTAINMENT_RECORDED"
)
POST_INVOCATION_COMMAND_EXECUTION_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_RECORDED"
)
COMMAND_INVOCATION_OUTCOME = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_INVOCATION_RECORDED"
COMMAND_EXECUTION_REVIEW_OUTCOME = (
    "CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_EXECUTION_REVIEW_RECORDED"
)
REQUEST_CONSUMPTION_OUTCOME = "ADMITTED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_CONSUMED"
V2_ADMITTED_REQUEST_OUTCOME = "SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_ADMITTED"
V2_ADMITTED_REQUEST_VERSION = "0.2.0"

SUPPORTED_OUTPUT_CAPTURE_SCOPE = (
    "OUTPUT_CAPTURE_ONLY",
    "ONE_BOUNDED_OUTPUT_CAPTURE_EVENT_RECORDED",
    "OUTPUT_CAPTURE_BOUNDARY_BASIS_PRESERVED",
    "COMMAND_OUTPUT_BASIS_PRESERVED",
    "BOUNDED_COMMAND_OUTPUT_EVENT_PRESERVED",
    "COMMAND_OUTPUT_BOUNDARY_BASIS_PRESERVED",
    "COMMAND_OUTPUT_CONTAINMENT_BASIS_PRESERVED",
    "RECORDED_COMMAND_EXECUTION_EVENT_PRESERVED",
    "EXECUTION_TRACE_AUDIT_ONLY_PRESERVED",
    "STDOUT_CONTENT_NOT_INVENTED",
    "STDERR_CONTENT_NOT_INVENTED",
    "PROCESS_OUTPUT_CONTENT_NOT_INVENTED",
    "RAW_OUTPUT_BODY_CONTENT_NOT_INVENTED",
    "STDOUT_CONTENT_PRESENT_FALSE_ALLOWED",
    "STDERR_CONTENT_PRESENT_FALSE_ALLOWED",
    "PROCESS_OUTPUT_CONTENT_PRESENT_FALSE_ALLOWED",
    "RAW_OUTPUT_BODY_CONTENT_PRESENT_FALSE_ALLOWED",
    "OUTPUT_REPORT_ARTIFACT_NOT_CREATED",
    "COMMAND_RESULT_NOT_CREATED",
    "COMMAND_SUCCESS_NOT_CREATED",
    "OUTPUT_CAPTURE_IS_NOT_OUTPUT_REPORT_ARTIFACT",
    "OUTPUT_CAPTURE_IS_NOT_RESULT",
    "OUTPUT_CAPTURE_IS_NOT_SUCCESS",
    "OUTPUT_CAPTURE_IS_NOT_SOURCE",
    "OUTPUT_CAPTURE_IS_NOT_AUTHORITY",
    "OUTPUT_CAPTURE_IS_NOT_CURRENTNESS",
    "OUTPUT_CAPTURE_IS_NOT_FINAL_COMPLETION",
    "COMMAND_OUTPUT_IS_NOT_OUTPUT_REPORT_ARTIFACT",
    "COMMAND_OUTPUT_IS_NOT_RESULT",
    "COMMAND_OUTPUT_IS_NOT_SUCCESS",
    "COMMAND_OUTPUT_IS_NOT_SOURCE",
    "COMMAND_OUTPUT_IS_NOT_AUTHORITY",
    "COMMAND_OUTPUT_IS_NOT_CURRENTNESS",
    "COMMAND_OUTPUT_IS_NOT_FINAL_COMPLETION",
    "EXECUTION_TRACE_IS_NOT_OUTPUT_CAPTURE",
    "EXECUTION_TRACE_IS_NOT_RESULT",
    "EXECUTION_TRACE_IS_NOT_SUCCESS",
    "EXECUTION_TRACE_IS_NOT_SOURCE",
    "EXECUTION_TRACE_IS_NOT_AUTHORITY",
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
SUPPORTED_OUTPUT_CAPTURE_SCOPE_SET = frozenset(SUPPORTED_OUTPUT_CAPTURE_SCOPE)

REQUIRED_FALSE_NON_CLAIMS = (
    "stdout_content_invented",
    "stderr_content_invented",
    "process_output_content_invented",
    "raw_output_body_content_invented",
    "command_output_report_artifact_created",
    "command_result_created",
    "command_success_created",
    "output_capture_treated_as_output_report_artifact",
    "output_capture_treated_as_result",
    "output_capture_treated_as_success",
    "output_capture_treated_as_source",
    "output_capture_treated_as_authority",
    "output_capture_treated_as_currentness",
    "output_capture_treated_as_final_completion",
    "command_output_treated_as_output_report_artifact",
    "command_output_treated_as_result",
    "command_output_treated_as_success",
    "command_output_treated_as_source",
    "command_output_treated_as_authority",
    "command_output_treated_as_currentness",
    "command_output_treated_as_final_completion",
    "execution_trace_treated_as_output_capture",
    "execution_trace_treated_as_result",
    "execution_trace_treated_as_success",
    "execution_trace_treated_as_source",
    "execution_trace_treated_as_authority",
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
    "output_capture_recorded",
    "bounded_output_capture_event_recorded",
    "output_capture_boundary_basis_preserved",
    "command_output_basis_preserved",
    "bounded_command_output_event_preserved",
    "command_output_boundary_basis_preserved",
    "command_output_containment_basis_preserved",
    "recorded_command_execution_event_preserved",
    "execution_trace_audit_only_preserved",
    "stdout_content_absent_without_invention",
    "stderr_content_absent_without_invention",
    "process_output_content_absent_without_invention",
    "raw_output_body_content_absent_without_invention",
    "command_output_report_artifact_not_created",
    "command_result_still_not_created",
    "command_success_still_not_created",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
    "v1_predecessor_failure_preserved",
    "returned_result_containment_preserved",
)

ALLOWED_FALSE_RECORDED_FIELDS = (
    "stdout_content_present",
    "stderr_content_present",
    "process_output_content_present",
    "raw_output_body_content_present",
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
        "output_body",
        "raw_full_prior_artifact_body",
        "raw_full_result",
        "raw_result",
        "result_body",
        "source_body",
        "success_body",
    }
)

FORBIDDEN_RAW_OUTPUT_CONTENT_KEYS = frozenset(
    {
        "actual_stdout",
        "actual_stderr",
        "captured_output",
        "captured_process_output",
        "captured_raw_output_body",
        "captured_stderr",
        "captured_stdout",
        "command_output_content",
        "process_output",
        "process_output_body",
        "process_output_content",
        "raw_command_output_body",
        "raw_output_body",
        "raw_output_body_content",
        "stderr",
        "stderr_body",
        "stderr_content",
        "stdout",
        "stdout_body",
        "stdout_content",
    }
)

BLOCK_CODES = frozenset(
    {
        "DECLARED_OUTPUT_CAPTURE_REQUEST_MALFORMED",
        "DECLARED_OUTPUT_CAPTURE_REQUEST_UNREADABLE",
        "OUTPUT_CAPTURE_QUESTION_UNDECLARED",
        "OUTPUT_CAPTURE_INTENT_UNSUPPORTED",
        "OUTPUT_CAPTURE_BLOCKED_BY_REQUEST",
        "OUTPUT_CAPTURE_BOUNDARY_BASIS_MISSING",
        "OUTPUT_CAPTURE_BOUNDARY_NOT_RECORDED",
        "OUTPUT_CAPTURE_BOUNDARY_FAILED_CHECKS_PRESENT",
        "OUTPUT_CAPTURE_BOUNDARY_STEP_NOT_DECLARED",
        "OUTPUT_CAPTURE_BOUNDARY_ALREADY_CAPTURED_STDOUT",
        "OUTPUT_CAPTURE_BOUNDARY_ALREADY_CAPTURED_STDERR",
        "OUTPUT_CAPTURE_BOUNDARY_ALREADY_CAPTURED_PROCESS_OUTPUT",
        "OUTPUT_CAPTURE_BOUNDARY_ALREADY_CAPTURED_RAW_OUTPUT_BODY",
        "OUTPUT_CAPTURE_BOUNDARY_ALREADY_CREATED_OUTPUT_CAPTURE",
        "OUTPUT_CAPTURE_BOUNDARY_ALREADY_CREATED_OUTPUT_REPORT_ARTIFACT",
        "OUTPUT_CAPTURE_BOUNDARY_ALREADY_CREATED_RESULT",
        "OUTPUT_CAPTURE_BOUNDARY_ALREADY_CREATED_SUCCESS",
        "COMMAND_OUTPUT_BASIS_MISSING",
        "COMMAND_OUTPUT_NOT_RECORDED",
        "COMMAND_OUTPUT_FAILED_CHECKS_PRESENT",
        "COMMAND_OUTPUT_EVENT_NOT_RECORDED",
        "COMMAND_OUTPUT_ALREADY_CAPTURED_STDOUT",
        "COMMAND_OUTPUT_ALREADY_CAPTURED_STDERR",
        "COMMAND_OUTPUT_ALREADY_CAPTURED_PROCESS_OUTPUT",
        "COMMAND_OUTPUT_ALREADY_CAPTURED_RAW_OUTPUT_BODY",
        "COMMAND_OUTPUT_ALREADY_CREATED_OUTPUT_CAPTURE",
        "COMMAND_OUTPUT_ALREADY_CREATED_OUTPUT_REPORT_ARTIFACT",
        "COMMAND_OUTPUT_ALREADY_CREATED_RESULT",
        "COMMAND_OUTPUT_ALREADY_CREATED_SUCCESS",
        "COMMAND_OUTPUT_BOUNDARY_BASIS_MISSING",
        "COMMAND_OUTPUT_CONTAINMENT_BASIS_MISSING",
        "POST_INVOCATION_COMMAND_EXECUTION_BASIS_MISSING",
        "POST_INVOCATION_COMMAND_EXECUTION_NOT_RECORDED",
        "POST_INVOCATION_COMMAND_EXECUTION_FAILED_CHECKS_PRESENT",
        "POST_INVOCATION_COMMAND_EXECUTION_TRACE_NOT_AUDIT_ONLY",
        "STDOUT_CONTENT_INVENTED",
        "STDERR_CONTENT_INVENTED",
        "PROCESS_OUTPUT_CONTENT_INVENTED",
        "RAW_OUTPUT_BODY_CONTENT_INVENTED",
        "OUTPUT_CAPTURE_TREATED_AS_OUTPUT_REPORT_ARTIFACT",
        "OUTPUT_CAPTURE_TREATED_AS_RESULT",
        "OUTPUT_CAPTURE_TREATED_AS_SUCCESS",
        "OUTPUT_CAPTURE_TREATED_AS_SOURCE",
        "OUTPUT_CAPTURE_TREATED_AS_AUTHORITY",
        "OUTPUT_CAPTURE_TREATED_AS_CURRENTNESS",
        "OUTPUT_CAPTURE_TREATED_AS_FINAL_COMPLETION",
        "COMMAND_OUTPUT_TREATED_AS_OUTPUT_REPORT_ARTIFACT",
        "COMMAND_OUTPUT_TREATED_AS_RESULT",
        "COMMAND_OUTPUT_TREATED_AS_SUCCESS",
        "COMMAND_OUTPUT_TREATED_AS_SOURCE",
        "COMMAND_OUTPUT_TREATED_AS_AUTHORITY",
        "COMMAND_OUTPUT_TREATED_AS_CURRENTNESS",
        "COMMAND_OUTPUT_TREATED_AS_FINAL_COMPLETION",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_CREATED",
        "COMMAND_RESULT_CREATED",
        "COMMAND_SUCCESS_CREATED",
        "EXECUTION_TRACE_TREATED_AS_OUTPUT_CAPTURE",
        "EXECUTION_TRACE_TREATED_AS_RESULT",
        "EXECUTION_TRACE_TREATED_AS_SUCCESS",
        "EXECUTION_TRACE_TREATED_AS_SOURCE",
        "EXECUTION_TRACE_TREATED_AS_AUTHORITY",
        "COMMAND_RESULT_TREATED_AS_AUTHORITY",
        "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS",
        "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION",
        "CONSUMED_REQUEST_REOPENED",
        "AUTHORIZATION_TOKEN_REUSED",
        "V2_ADMITTED_REQUEST_BASIS_MISSING",
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
        "OUTPUT_CAPTURE_ONLY_POSTURE_MISSING",
        "ONE_BOUNDED_OUTPUT_CAPTURE_EVENT_POSTURE_MISSING",
        "OUTPUT_CAPTURE_BOUNDARY_BASIS_PRESERVED_POSTURE_MISSING",
        "COMMAND_OUTPUT_BASIS_PRESERVED_POSTURE_MISSING",
        "BOUNDED_COMMAND_OUTPUT_EVENT_PRESERVED_POSTURE_MISSING",
        "EXECUTION_TRACE_AUDIT_ONLY_POSTURE_MISSING",
        "NO_STDOUT_CONTENT_INVENTED_POSTURE_MISSING",
        "NO_STDERR_CONTENT_INVENTED_POSTURE_MISSING",
        "NO_PROCESS_OUTPUT_CONTENT_INVENTED_POSTURE_MISSING",
        "NO_RAW_OUTPUT_BODY_CONTENT_INVENTED_POSTURE_MISSING",
        "NO_OUTPUT_REPORT_ARTIFACT_POSTURE_MISSING",
        "NO_COMMAND_RESULT_POSTURE_MISSING",
        "NO_COMMAND_SUCCESS_POSTURE_MISSING",
        "NO_OUTPUT_AS_SOURCE_POSTURE_MISSING",
        "NO_RESULT_AS_AUTHORITY_POSTURE_MISSING",
        "NO_SUCCESS_AS_CURRENTNESS_POSTURE_MISSING",
        "NO_FINAL_COMPLETION_POSTURE_MISSING",
        "REFERENCE_SHAPED_INPUT_POSTURE_MISSING",
        "UNSUPPORTED_OUTPUT_CAPTURE_SCOPE",
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

SELECTED_BASIS_KEYS = (
    "selected_output_capture_boundary_basis",
    "selected_output_capture_boundary_terminal_summary_basis",
    "selected_command_output_basis",
    "selected_command_output_terminal_summary_basis",
    "selected_command_output_boundary_basis",
    "selected_command_output_containment_basis",
    "selected_post_invocation_command_execution_basis",
    "selected_post_invocation_command_execution_terminal_summary_basis",
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

POSTURE_KEYS = (
    "output_capture_only_posture",
    "one_bounded_output_capture_event_posture",
    "output_capture_boundary_basis_preserved_posture",
    "command_output_basis_preserved_posture",
    "bounded_command_output_event_preserved_posture",
    "execution_trace_audit_only_posture",
    "no_stdout_content_invented_posture",
    "no_stderr_content_invented_posture",
    "no_process_output_content_invented_posture",
    "no_raw_output_body_content_invented_posture",
    "no_output_report_artifact_posture",
    "no_command_result_posture",
    "no_command_success_posture",
    "no_output_as_source_posture",
    "no_result_as_authority_posture",
    "no_success_as_currentness_posture",
    "no_final_completion_posture",
    "authorization_token_reuse_blocked_posture",
    "consumed_token_closed_posture",
    "no_reopen_consumed_request_posture",
    "returned_result_containment_posture",
    "reference_shaped_input_posture",
)

OPEN_ITEMS = (
    "output_capture_test",
    "output_capture_live_artifact",
    "command_output_report_artifact_boundary_or_artifact_step_if_separately_specified",
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
)


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _copy(value: Any) -> Any:
    return copy.deepcopy(value)


def _mapping(value: Any) -> dict[str, Any]:
    if isinstance(value, Mapping):
        return dict(value)
    return {}


def _present(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (Mapping, list, tuple, set)):
        return bool(value)
    return True


def _to_int(value: Any) -> int | None:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value.strip())
        except ValueError:
            return None
    return None


def _truthy(value: Any) -> bool:
    if value is True:
        return True
    if isinstance(value, str):
        return value.strip().lower() in {
            "true",
            "yes",
            "1",
            "recorded",
            "declared",
            "preserved",
            "blocked",
            "created",
            "invented",
        }
    return False


def _explicit_false(value: Any) -> bool:
    if value is False:
        return True
    if isinstance(value, str):
        return value.strip().lower() in {"false", "no", "0", "not_created", "not_invented"}
    return False


def _find(mapping: Mapping[str, Any], keys: Iterable[str], default: Any = None) -> Any:
    for key in keys:
        if key in mapping:
            return mapping[key]
    return default


def _basis(request: Mapping[str, Any], key: str) -> dict[str, Any]:
    return _mapping(request.get(key))


def _basis_declared(request: Mapping[str, Any], key: str) -> bool:
    return bool(_basis(request, key))


def _posture_declared(request: Mapping[str, Any], key: str) -> bool:
    posture = _basis(request, key)
    return bool(posture)


def _declared_non_claims(request: Mapping[str, Any]) -> dict[str, Any]:
    return _mapping(request.get("declared_non_claims"))


def _outcome(basis: Mapping[str, Any]) -> Any:
    metadata = _mapping(basis.get("metadata")) or _mapping(
        basis.get("portable_source_body_verification_output_capture_metadata")
    )
    return (
        basis.get("outcome")
        or basis.get("result_outcome")
        or basis.get("selected_outcome")
        or metadata.get("outcome")
    )


def _version(basis: Mapping[str, Any]) -> Any:
    metadata = _mapping(basis.get("metadata")) or _mapping(
        basis.get("portable_source_body_verification_output_capture_metadata")
    )
    return (
        basis.get("result_version")
        or basis.get("version")
        or metadata.get("result_version")
        or metadata.get("portable_source_body_verification_output_capture_result_version")
    )


def _failed_count(basis: Mapping[str, Any]) -> Any:
    summary = _mapping(
        basis.get("portable_source_body_verification_output_capture_summary")
        or basis.get("summary")
    )
    checks = _mapping(
        basis.get("output_capture_checks")
        or basis.get("output_capture_boundary_checks")
        or basis.get("command_output_checks")
    )
    for source in (basis, summary, checks):
        if "failed_check_count" in source:
            return source.get("failed_check_count")
    return None


def _passed_count(basis: Mapping[str, Any]) -> Any:
    summary = _mapping(
        basis.get("portable_source_body_verification_output_capture_summary")
        or basis.get("summary")
    )
    checks = _mapping(
        basis.get("output_capture_checks")
        or basis.get("output_capture_boundary_checks")
        or basis.get("command_output_checks")
    )
    for source in (basis, summary, checks):
        if "passed_check_count" in source:
            return source.get("passed_check_count")
    return None


def _contains_truthy_key(value: Any, keys: Iterable[str]) -> bool:
    key_set = {key.lower() for key in keys}
    if isinstance(value, Mapping):
        for key, item in value.items():
            if str(key).lower() in key_set and _truthy(item):
                return True
            if _contains_truthy_key(item, keys):
                return True
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return any(_contains_truthy_key(item, keys) for item in value)
    return False


def _contains_present_key(value: Any, keys: Iterable[str]) -> bool:
    key_set = {key.lower() for key in keys}
    if isinstance(value, Mapping):
        for key, item in value.items():
            if str(key).lower() in key_set and _present(item):
                return True
            if _contains_present_key(item, keys):
                return True
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return any(_contains_present_key(item, keys) for item in value)
    return False


def _sanitize(value: Any) -> Any:
    if isinstance(value, Mapping):
        sanitized: dict[str, Any] = {}
        for key, item in value.items():
            lower = str(key).lower()
            if lower in FORBIDDEN_FULL_BODY_KEYS:
                sanitized[f"{key}_omitted"] = True
                sanitized[f"{key}_omission_reason"] = "full prior artifact body not emitted"
                continue
            if lower in FORBIDDEN_RAW_OUTPUT_CONTENT_KEYS:
                sanitized[f"{key}_omitted"] = True
                sanitized[f"{key}_omission_reason"] = "raw output content not emitted"
                continue
            sanitized[str(key)] = _sanitize(item)
        return sanitized
    if isinstance(value, list):
        return [_sanitize(item) for item in value]
    if isinstance(value, tuple):
        return tuple(_sanitize(item) for item in value)
    return _copy(value)


def _reference_shaped(basis: Mapping[str, Any]) -> bool:
    if not basis:
        return False
    if _contains_present_key(basis, FORBIDDEN_FULL_BODY_KEYS | FORBIDDEN_RAW_OUTPUT_CONTENT_KEYS):
        return False
    explicit = (
        _truthy(basis.get("reference_shaped_basis"))
        or _truthy(basis.get("basis_remains_reference_shaped"))
        or _truthy(basis.get("basis_reference_shape_preserved"))
    )
    return explicit or any(key in basis for key in ("path", "artifact_path", "result_path", "basis_reference"))


def _created_flag(
    request: Mapping[str, Any],
    basis: Mapping[str, Any],
    shortcut_keys: Iterable[str],
    created_keys: Iterable[str],
) -> bool:
    for key in shortcut_keys:
        if _truthy(request.get(key)):
            return True
    for key in created_keys:
        if _truthy(basis.get(key)):
            return True
    return False


def _lineage_as_current_execution(value: Mapping[str, Any]) -> bool:
    return any(
        _truthy(value.get(key))
        for key in (
            "older_command_execution_boundary_lineage_treated_as_current_execution",
            "treated_as_current_execution",
            "current_execution",
            "current_command_execution",
        )
    )


def _scope_values(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, Mapping):
        for key in ("values", "scope_values", "output_capture_scope"):
            if key in value:
                return _scope_values(value[key])
        return [str(key) for key, item in value.items() if _truthy(item)]
    if isinstance(value, Sequence) and not isinstance(value, (bytes, bytearray)):
        return [str(item) for item in value]
    return [str(value)]


def _flag_true(request: Mapping[str, Any], keys: Iterable[str]) -> bool:
    if _contains_truthy_key(request, keys):
        return True
    declared = _declared_non_claims(request)
    return _contains_truthy_key(declared, keys)


def _check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    block_code: str,
    failure_code: str | None = None,
) -> dict[str, Any]:
    code = None if passed else block_code
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": _sanitize(expected_posture),
        "actual_posture": _sanitize(actual_posture),
        "block_code": code,
        "failure_code": None if passed else (failure_code or block_code),
    }


def _requested_outcome(request: Mapping[str, Any]) -> str | None:
    value = request.get("requested_output_capture_outcome")
    if value in OUTCOME_FAMILY:
        return str(value)
    return None


def _selected_output_capture_boundary_basis(request: Mapping[str, Any]) -> dict[str, Any]:
    basis = _basis(request, "selected_output_capture_boundary_basis")
    stdout_captured = _created_flag(
        request,
        basis,
        ("selected_output_capture_boundary_stdout_captured",),
        ("stdout_captured", "stdout_capture_created", "stdout_already_captured"),
    )
    stderr_captured = _created_flag(
        request,
        basis,
        ("selected_output_capture_boundary_stderr_captured",),
        ("stderr_captured", "stderr_capture_created", "stderr_already_captured"),
    )
    process_output_captured = _created_flag(
        request,
        basis,
        ("selected_output_capture_boundary_process_output_captured",),
        ("process_output_captured", "process_output_capture_created", "process_output_already_captured"),
    )
    raw_output_body_captured = _created_flag(
        request,
        basis,
        ("selected_output_capture_boundary_raw_output_body_captured",),
        ("raw_output_body_captured", "raw_command_output_body_captured", "raw_output_body_capture_created"),
    )
    output_capture_created = _created_flag(
        request,
        basis,
        ("selected_output_capture_boundary_output_capture_created",),
        ("output_capture_created",),
    )
    output_report_created = _created_flag(
        request,
        basis,
        ("selected_output_capture_boundary_output_report_artifact_created",),
        ("command_output_report_artifact_created", "output_report_artifact_created"),
    )
    command_result_created = _created_flag(
        request,
        basis,
        ("selected_output_capture_boundary_result_created",),
        ("command_result_created",),
    )
    command_success_created = _created_flag(
        request,
        basis,
        ("selected_output_capture_boundary_success_created",),
        ("command_success_created",),
    )
    step_declared = (
        _truthy(request.get("selected_output_capture_boundary_step_declared"))
        or _truthy(basis.get("one_future_output_capture_step_declared"))
        or _truthy(basis.get("output_capture_boundary_recorded"))
    )
    return {
        "basis": _sanitize(basis),
        "declared": bool(basis),
        "selected_output_capture_boundary_result_path": request.get(
            "selected_output_capture_boundary_result_path"
        )
        or basis.get("path")
        or basis.get("artifact_path")
        or basis.get("result_path"),
        "selected_output_capture_boundary_result_id": request.get(
            "selected_output_capture_boundary_result_id"
        )
        or basis.get("result_id")
        or basis.get("portable_source_body_verification_output_capture_boundary_result_id"),
        "outcome": request.get("selected_output_capture_boundary_result_outcome") or _outcome(basis),
        "failed_check_count": _find(
            request,
            ("selected_output_capture_boundary_failed_check_count",),
            _failed_count(basis),
        ),
        "passed_check_count": _passed_count(basis),
        "one_future_output_capture_step_declared": step_declared,
        "stdout_captured": stdout_captured,
        "stderr_captured": stderr_captured,
        "process_output_captured": process_output_captured,
        "raw_output_body_captured": raw_output_body_captured,
        "output_capture_created": output_capture_created,
        "command_output_report_artifact_created": output_report_created,
        "command_result_created": command_result_created,
        "command_success_created": command_success_created,
        "stdout_not_captured": not stdout_captured,
        "stderr_not_captured": not stderr_captured,
        "process_output_not_captured": not process_output_captured,
        "raw_output_body_not_captured": not raw_output_body_captured,
        "output_capture_not_created": not output_capture_created,
        "command_output_report_artifact_not_created": not output_report_created,
        "command_result_not_created": not command_result_created,
        "command_success_not_created": not command_success_created,
        "reference_shaped_basis": _reference_shaped(basis),
    }


def _selected_command_output_basis(request: Mapping[str, Any]) -> dict[str, Any]:
    basis = _basis(request, "selected_command_output_basis")
    stdout_captured = _created_flag(
        request,
        basis,
        ("selected_command_output_stdout_captured",),
        ("stdout_captured", "stdout_capture_created", "stdout_already_captured"),
    )
    stderr_captured = _created_flag(
        request,
        basis,
        ("selected_command_output_stderr_captured",),
        ("stderr_captured", "stderr_capture_created", "stderr_already_captured"),
    )
    process_output_captured = _created_flag(
        request,
        basis,
        ("selected_command_output_process_output_captured",),
        ("process_output_captured", "process_output_capture_created", "process_output_already_captured"),
    )
    raw_output_body_captured = _created_flag(
        request,
        basis,
        ("selected_command_output_raw_output_body_captured",),
        ("raw_output_body_captured", "raw_command_output_body_captured", "raw_output_body_capture_created"),
    )
    output_capture_created = _created_flag(
        request,
        basis,
        ("selected_command_output_output_capture_created",),
        ("output_capture_created",),
    )
    output_report_created = _created_flag(
        request,
        basis,
        ("selected_command_output_output_report_artifact_created",),
        ("command_output_report_artifact_created", "output_report_artifact_created"),
    )
    command_result_created = _created_flag(
        request,
        basis,
        ("selected_command_output_result_created",),
        ("command_result_created",),
    )
    command_success_created = _created_flag(
        request,
        basis,
        ("selected_command_output_success_created",),
        ("command_success_created",),
    )
    event_recorded = (
        _truthy(request.get("selected_command_output_event_recorded"))
        or _truthy(basis.get("bounded_command_output_event_recorded"))
        or _truthy(basis.get("command_output_event_recorded"))
        or _truthy(basis.get("command_output_recorded"))
    )
    return {
        "basis": _sanitize(basis),
        "declared": bool(basis),
        "selected_command_output_result_path": request.get("selected_command_output_result_path")
        or basis.get("path")
        or basis.get("artifact_path")
        or basis.get("result_path"),
        "selected_command_output_result_id": request.get("selected_command_output_result_id")
        or basis.get("result_id")
        or basis.get("portable_source_body_verification_command_output_result_id"),
        "outcome": request.get("selected_command_output_result_outcome") or _outcome(basis),
        "failed_check_count": _find(
            request,
            ("selected_command_output_failed_check_count",),
            _failed_count(basis),
        ),
        "passed_check_count": _passed_count(basis),
        "bounded_command_output_event_recorded": event_recorded,
        "command_output_recorded": _truthy(basis.get("command_output_recorded")) or event_recorded,
        "stdout_captured": stdout_captured,
        "stderr_captured": stderr_captured,
        "process_output_captured": process_output_captured,
        "raw_output_body_captured": raw_output_body_captured,
        "output_capture_created": output_capture_created,
        "command_output_report_artifact_created": output_report_created,
        "command_result_created": command_result_created,
        "command_success_created": command_success_created,
        "stdout_not_captured": not stdout_captured,
        "stderr_not_captured": not stderr_captured,
        "process_output_not_captured": not process_output_captured,
        "raw_output_body_not_captured": not raw_output_body_captured,
        "output_capture_not_created": not output_capture_created,
        "command_output_report_artifact_not_created": not output_report_created,
        "command_result_not_created": not command_result_created,
        "command_success_not_created": not command_success_created,
        "reference_shaped_basis": _reference_shaped(basis),
    }


def _selected_prior_basis(
    request: Mapping[str, Any],
    key: str,
    path_key: str | None = None,
    expected_outcome: str | None = None,
    expected_version: str | None = None,
) -> dict[str, Any]:
    basis = _basis(request, key)
    outcome_shortcuts = {
        "selected_post_invocation_command_execution_basis": (
            "selected_post_invocation_command_execution_result_outcome"
        ),
        "selected_command_invocation_basis": "selected_command_invocation_result_outcome",
        "selected_command_execution_review_basis": "selected_command_execution_review_result_outcome",
        "selected_request_consumption_basis": "selected_request_consumption_result_outcome",
        "selected_v2_admitted_request_basis": "selected_v2_admitted_request_outcome",
    }
    failed_shortcuts = {
        "selected_post_invocation_command_execution_basis": (
            "selected_post_invocation_command_execution_failed_check_count"
        ),
        "selected_command_invocation_basis": "selected_command_invocation_failed_check_count",
        "selected_command_execution_review_basis": "selected_command_execution_review_failed_check_count",
        "selected_request_consumption_basis": "selected_request_consumption_failed_check_count",
        "selected_v2_admitted_request_basis": "selected_v2_failed_check_count",
    }
    outcome_key = outcome_shortcuts.get(key)
    failed_key = failed_shortcuts.get(key)
    selected: dict[str, Any] = {
        "basis": _sanitize(basis),
        "declared": bool(basis),
        "reference_shaped_basis": _reference_shaped(basis),
        "outcome": request.get(outcome_key, _outcome(basis)) if outcome_key else _outcome(basis),
        "failed_check_count": request.get(failed_key, _failed_count(basis))
        if failed_key
        else _failed_count(basis),
        "passed_check_count": _passed_count(basis),
        "bounded_command_execution_event_recorded": _truthy(
            basis.get("one_bounded_command_execution_event_recorded")
        )
        or _truthy(basis.get("bounded_command_execution_event_recorded"))
        or _truthy(basis.get("recorded_command_execution_event_preserved")),
        "execution_trace_audit_only": _truthy(
            request.get("selected_post_invocation_command_execution_trace_audit_only")
        )
        or _truthy(basis.get("execution_trace_audit_only"))
        or _truthy(basis.get("execution_trace_audit_only_preserved"))
        or _truthy(basis.get("execution_trace_recorded_as_audit_only")),
        "lineage_basis_not_treated_as_current_execution": not _lineage_as_current_execution(basis),
    }
    if path_key:
        selected[path_key] = request.get(path_key) or basis.get("path") or basis.get("result_path")
    if expected_outcome is not None:
        selected["expected_outcome"] = expected_outcome
    if expected_version is not None:
        selected["expected_version"] = expected_version
        selected["version"] = request.get("selected_v2_admitted_request_version") or _version(basis)
    return selected


def _terminal_summary_basis(request: Mapping[str, Any], key: str) -> dict[str, Any]:
    summary = _basis(request, key)
    return {
        "basis": _sanitize(summary),
        "declared": bool(summary),
        "readability_basis_only": True,
        "terminal_summary_does_not_invent_stdout": True,
        "terminal_summary_does_not_invent_stderr": True,
        "terminal_summary_does_not_invent_process_output": True,
        "terminal_summary_does_not_invent_raw_output_body": True,
        "terminal_summary_does_not_create_output_report_artifact": True,
        "terminal_summary_does_not_create_command_result": True,
        "terminal_summary_does_not_create_command_success": True,
        "terminal_summary_does_not_authorize_follow_on_work": True,
    }


def _posture_section(request: Mapping[str, Any], key: str) -> dict[str, Any]:
    posture = _basis(request, key)
    section = _mapping(_sanitize(posture))
    section.update(
        {
            "declared": bool(posture),
            "posture_name": key,
            "stdout_content_invented": _truthy(posture.get("stdout_content_invented")),
            "stderr_content_invented": _truthy(posture.get("stderr_content_invented")),
            "process_output_content_invented": _truthy(
                posture.get("process_output_content_invented")
            ),
            "raw_output_body_content_invented": _truthy(
                posture.get("raw_output_body_content_invented")
            ),
            "stdout_content_present": _truthy(posture.get("stdout_content_present")),
            "stderr_content_present": _truthy(posture.get("stderr_content_present")),
            "process_output_content_present": _truthy(posture.get("process_output_content_present")),
            "raw_output_body_content_present": _truthy(posture.get("raw_output_body_content_present")),
            "stdout_content_absent_without_invention": not _truthy(
                posture.get("stdout_content_invented")
            ),
            "stderr_content_absent_without_invention": not _truthy(
                posture.get("stderr_content_invented")
            ),
            "process_output_content_absent_without_invention": not _truthy(
                posture.get("process_output_content_invented")
            ),
            "raw_output_body_content_absent_without_invention": not _truthy(
                posture.get("raw_output_body_content_invented")
            ),
            "command_output_report_artifact_not_created": not (
                _truthy(posture.get("command_output_report_artifact_created"))
                or _truthy(posture.get("output_report_artifact_created"))
            ),
            "command_result_not_created": not _truthy(posture.get("command_result_created")),
            "command_success_not_created": not _truthy(posture.get("command_success_created")),
            "output_capture_not_output_report_artifact": not _truthy(
                posture.get("output_capture_treated_as_output_report_artifact")
            ),
            "output_capture_not_result": not _truthy(
                posture.get("output_capture_treated_as_result")
            ),
            "output_capture_not_success": not _truthy(
                posture.get("output_capture_treated_as_success")
            ),
            "output_capture_not_source": not _truthy(
                posture.get("output_capture_treated_as_source")
            ),
            "output_capture_not_authority": not _truthy(
                posture.get("output_capture_treated_as_authority")
            ),
            "output_capture_not_currentness": not _truthy(
                posture.get("output_capture_treated_as_currentness")
            ),
            "output_capture_not_final_completion": not _truthy(
                posture.get("output_capture_treated_as_final_completion")
            ),
            "command_output_not_output_report_artifact": not _truthy(
                posture.get("command_output_treated_as_output_report_artifact")
            ),
            "command_output_not_result": not _truthy(posture.get("command_output_treated_as_result")),
            "command_output_not_success": not _truthy(posture.get("command_output_treated_as_success")),
            "command_output_not_source": not _truthy(posture.get("command_output_treated_as_source")),
            "command_output_not_authority": not _truthy(
                posture.get("command_output_treated_as_authority")
            ),
            "command_output_not_currentness": not _truthy(
                posture.get("command_output_treated_as_currentness")
            ),
            "command_output_not_final_completion": not _truthy(
                posture.get("command_output_treated_as_final_completion")
            ),
            "execution_trace_audit_only": _truthy(posture.get("execution_trace_audit_only"))
            or _truthy(posture.get("execution_trace_audit_only_preserved")),
            "execution_trace_not_output_capture": not _truthy(
                posture.get("execution_trace_treated_as_output_capture")
            ),
            "execution_trace_not_result": not _truthy(posture.get("execution_trace_treated_as_result")),
            "execution_trace_not_success": not _truthy(posture.get("execution_trace_treated_as_success")),
            "execution_trace_not_source": not _truthy(posture.get("execution_trace_treated_as_source")),
            "execution_trace_not_authority": not _truthy(
                posture.get("execution_trace_treated_as_authority")
            ),
            "result_not_authority": not _truthy(posture.get("command_result_became_authority")),
            "success_not_currentness": not _truthy(
                posture.get("command_success_created_currentness")
            ),
            "success_not_final_completion": not _truthy(
                posture.get("command_success_claimed_final_completion")
            ),
            "authorization_token_reuse_blocked": _truthy(
                posture.get("authorization_token_reuse_blocked")
            )
            or not _truthy(posture.get("authorization_token_reused")),
            "consumed_request_token_remains_closed": _truthy(
                posture.get("consumed_request_token_remains_closed")
            )
            or not _truthy(posture.get("consumed_request_reopened")),
            "consumed_request_not_reopened": not _truthy(posture.get("consumed_request_reopened")),
            "returned_result_containment_preserved": _truthy(
                posture.get("returned_result_containment_preserved")
            )
            or not _truthy(posture.get("raw_full_prior_artifact_body_returned")),
            "raw_full_prior_artifact_body_returned": _truthy(
                posture.get("raw_full_prior_artifact_body_returned")
            ),
        }
    )
    return section


def _output_capture_event(outcome: str) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    return {
        "output_capture_event_recorded": recorded,
        "event_type": "OUTPUT_CAPTURE_EVENT_BOUNDED" if recorded else None,
        "stdout_content_present": False,
        "stderr_content_present": False,
        "process_output_content_present": False,
        "raw_output_body_content_present": False,
        "stdout_content_absent_without_invention": recorded,
        "stderr_content_absent_without_invention": recorded,
        "process_output_content_absent_without_invention": recorded,
        "raw_output_body_content_absent_without_invention": recorded,
        "stdout_content_invented": False,
        "stderr_content_invented": False,
        "process_output_content_invented": False,
        "raw_output_body_content_invented": False,
        "command_output_report_artifact_created": False,
        "command_result_created": False,
        "command_success_created": False,
        "output_capture_is_not_output_report_artifact": True,
        "output_capture_is_not_result": True,
        "output_capture_is_not_success": True,
        "output_capture_is_not_source": True,
        "output_capture_is_not_authority": True,
        "output_capture_is_not_currentness": True,
        "output_capture_is_not_final_completion": True,
    }


def _statement_for_outcome(outcome: str) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    statement = {field: recorded for field in ALLOWED_TRUE_RECORDED_FIELDS}
    statement.update({field: False for field in ALLOWED_FALSE_RECORDED_FIELDS})
    statement.update({field: False for field in REQUIRED_FALSE_NON_CLAIMS})
    return statement


def _non_meaning() -> dict[str, bool]:
    return {
        "stdout_content_was_invented": False,
        "stderr_content_was_invented": False,
        "process_output_content_was_invented": False,
        "raw_output_body_content_was_invented": False,
        "output_report_artifact_exists": False,
        "command_result_exists": False,
        "command_success_exists": False,
        "output_capture_is_output_report_artifact": False,
        "output_capture_is_result": False,
        "output_capture_is_success": False,
        "output_capture_is_source": False,
        "output_capture_is_authority": False,
        "output_capture_is_currentness": False,
        "output_capture_is_final_completion": False,
        "command_output_is_output_report_artifact": False,
        "command_output_is_result": False,
        "command_output_is_success": False,
        "execution_trace_is_output_capture": False,
        "execution_trace_is_result": False,
        "execution_trace_is_success": False,
        "execution_trace_is_source": False,
        "execution_trace_is_authority": False,
        "consumed_request_token_reopened": False,
        "authorization_token_reusable": False,
        "v1_repaired": False,
        "v1_hidden": False,
        "v1_passed": False,
        "deployment_created": False,
        "runtime_hosting_created": False,
        "public_release_created": False,
        "public_readiness_created": False,
        "final_completion_claimed": False,
        "continuation_authorized": False,
        "reusable_permission_created": False,
        "derivative_reception_authorized": False,
        "vessel_relation_authorized": False,
        "another_reception_request_authorized": False,
        "follow_on_work_authorized": False,
    }


def _block_object(blocked: bool, code: str | None, reason: str | None) -> dict[str, Any]:
    return {
        "blocked": bool(blocked),
        "block_code": code,
        "block_reason": reason,
        "code": code,
        "reason": reason,
    }


def _scope_section(request: Mapping[str, Any]) -> dict[str, Any]:
    values = _scope_values(request.get("output_capture_scope"))
    unsupported = [value for value in values if value not in SUPPORTED_OUTPUT_CAPTURE_SCOPE_SET]
    return {
        "declared": bool(values),
        "values": values,
        "supported_values": list(SUPPORTED_OUTPUT_CAPTURE_SCOPE),
        "unsupported_values": unsupported,
        "scope_family": "portable_source_body_verification_output_capture",
    }


def _build_checks(
    request: Mapping[str, Any],
    forced_block_code: str | None = None,
    forced_block_reason: str | None = None,
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    boundary = _selected_output_capture_boundary_basis(request)
    command_output = _selected_command_output_basis(request)
    command_output_boundary = _selected_prior_basis(
        request,
        "selected_command_output_boundary_basis",
        "selected_command_output_boundary_result_path",
        COMMAND_OUTPUT_BOUNDARY_OUTCOME,
    )
    command_output_containment = _selected_prior_basis(
        request,
        "selected_command_output_containment_basis",
        "selected_command_output_containment_result_path",
        COMMAND_OUTPUT_CONTAINMENT_OUTCOME,
    )
    post_invocation = _selected_prior_basis(
        request,
        "selected_post_invocation_command_execution_basis",
        "selected_post_invocation_command_execution_result_path",
        POST_INVOCATION_COMMAND_EXECUTION_OUTCOME,
    )
    command_invocation = _basis(request, "selected_command_invocation_basis")
    command_execution_review = _basis(request, "selected_command_execution_review_basis")
    request_consumption = _basis(request, "selected_request_consumption_basis")
    consumed_request = _basis(request, "selected_consumed_request_basis")
    v2 = _selected_prior_basis(
        request,
        "selected_v2_admitted_request_basis",
        "selected_v2_admitted_request_artifact_path",
        V2_ADMITTED_REQUEST_OUTCOME,
        V2_ADMITTED_REQUEST_VERSION,
    )
    v1 = _basis(request, "selected_v1_predecessor_failure_basis")
    older_lineage = _basis(request, "selected_older_command_execution_boundary_lineage_basis")
    declared_non_claims = _declared_non_claims(request)
    scope_values = _scope_values(request.get("output_capture_scope"))
    unsupported_scope = [value for value in scope_values if value not in SUPPORTED_OUTPUT_CAPTURE_SCOPE_SET]

    if forced_block_code:
        checks.append(
            _check(
                "forced block posture",
                False,
                "no forced block",
                forced_block_reason or forced_block_code,
                forced_block_code,
            )
        )

    question = request.get("output_capture_question")
    intent = request.get("output_capture_intent")
    checks.extend(
        [
            _check(
                "output capture question declared",
                _present(question),
                "declared output capture question",
                question,
                "OUTPUT_CAPTURE_QUESTION_UNDECLARED",
            ),
            _check(
                "output capture intent supported",
                intent in SUPPORTED_INTENTS,
                SUPPORTED_INTENTS,
                intent,
                "OUTPUT_CAPTURE_INTENT_UNSUPPORTED",
            ),
            _check(
                "output capture boundary terminal summary basis declared",
                _basis_declared(request, "selected_output_capture_boundary_terminal_summary_basis"),
                "selected output capture boundary terminal summary basis declared",
                request.get("selected_output_capture_boundary_terminal_summary_basis"),
                "OUTPUT_CAPTURE_BOUNDARY_BASIS_MISSING",
            ),
            _check(
                "output capture boundary live artifact basis declared",
                _basis_declared(request, "selected_output_capture_boundary_basis"),
                "selected output capture boundary basis declared",
                request.get("selected_output_capture_boundary_basis"),
                "OUTPUT_CAPTURE_BOUNDARY_BASIS_MISSING",
            ),
            _check(
                "output capture boundary outcome recorded",
                boundary.get("outcome") == OUTPUT_CAPTURE_BOUNDARY_OUTCOME,
                OUTPUT_CAPTURE_BOUNDARY_OUTCOME,
                boundary.get("outcome"),
                "OUTPUT_CAPTURE_BOUNDARY_NOT_RECORDED",
            ),
            _check(
                "output capture boundary failed check count zero",
                _to_int(boundary.get("failed_check_count")) == 0,
                0,
                boundary.get("failed_check_count"),
                "OUTPUT_CAPTURE_BOUNDARY_FAILED_CHECKS_PRESENT",
            ),
            _check(
                "output capture boundary step declared",
                _truthy(boundary.get("one_future_output_capture_step_declared")),
                "one future output capture step declared",
                boundary.get("one_future_output_capture_step_declared"),
                "OUTPUT_CAPTURE_BOUNDARY_STEP_NOT_DECLARED",
            ),
            _check(
                "output capture boundary stdout not captured",
                not _truthy(boundary.get("stdout_captured")),
                "stdout not captured by boundary",
                boundary.get("stdout_captured"),
                "OUTPUT_CAPTURE_BOUNDARY_ALREADY_CAPTURED_STDOUT",
            ),
            _check(
                "output capture boundary stderr not captured",
                not _truthy(boundary.get("stderr_captured")),
                "stderr not captured by boundary",
                boundary.get("stderr_captured"),
                "OUTPUT_CAPTURE_BOUNDARY_ALREADY_CAPTURED_STDERR",
            ),
            _check(
                "output capture boundary process output not captured",
                not _truthy(boundary.get("process_output_captured")),
                "process output not captured by boundary",
                boundary.get("process_output_captured"),
                "OUTPUT_CAPTURE_BOUNDARY_ALREADY_CAPTURED_PROCESS_OUTPUT",
            ),
            _check(
                "output capture boundary raw output body not captured",
                not _truthy(boundary.get("raw_output_body_captured")),
                "raw output body not captured by boundary",
                boundary.get("raw_output_body_captured"),
                "OUTPUT_CAPTURE_BOUNDARY_ALREADY_CAPTURED_RAW_OUTPUT_BODY",
            ),
            _check(
                "output capture boundary did not create output capture",
                not _truthy(boundary.get("output_capture_created")),
                "output capture not created by boundary",
                boundary.get("output_capture_created"),
                "OUTPUT_CAPTURE_BOUNDARY_ALREADY_CREATED_OUTPUT_CAPTURE",
            ),
            _check(
                "output capture boundary did not create output report artifact",
                not _truthy(boundary.get("command_output_report_artifact_created")),
                "output report artifact not created by boundary",
                boundary.get("command_output_report_artifact_created"),
                "OUTPUT_CAPTURE_BOUNDARY_ALREADY_CREATED_OUTPUT_REPORT_ARTIFACT",
            ),
            _check(
                "output capture boundary did not create command result",
                not _truthy(boundary.get("command_result_created")),
                "command result not created by boundary",
                boundary.get("command_result_created"),
                "OUTPUT_CAPTURE_BOUNDARY_ALREADY_CREATED_RESULT",
            ),
            _check(
                "output capture boundary did not create command success",
                not _truthy(boundary.get("command_success_created")),
                "command success not created by boundary",
                boundary.get("command_success_created"),
                "OUTPUT_CAPTURE_BOUNDARY_ALREADY_CREATED_SUCCESS",
            ),
            _check(
                "command output basis declared",
                _basis_declared(request, "selected_command_output_basis"),
                "selected command output basis declared",
                request.get("selected_command_output_basis"),
                "COMMAND_OUTPUT_BASIS_MISSING",
            ),
            _check(
                "command output terminal summary basis declared",
                _basis_declared(request, "selected_command_output_terminal_summary_basis"),
                "selected command output terminal summary basis declared",
                request.get("selected_command_output_terminal_summary_basis"),
                "COMMAND_OUTPUT_BASIS_MISSING",
            ),
            _check(
                "command output outcome recorded",
                command_output.get("outcome") == COMMAND_OUTPUT_OUTCOME,
                COMMAND_OUTPUT_OUTCOME,
                command_output.get("outcome"),
                "COMMAND_OUTPUT_NOT_RECORDED",
            ),
            _check(
                "command output failed check count zero",
                _to_int(command_output.get("failed_check_count")) == 0,
                0,
                command_output.get("failed_check_count"),
                "COMMAND_OUTPUT_FAILED_CHECKS_PRESENT",
            ),
            _check(
                "command output bounded event recorded",
                _truthy(command_output.get("bounded_command_output_event_recorded")),
                "one bounded command output event recorded",
                command_output.get("bounded_command_output_event_recorded"),
                "COMMAND_OUTPUT_EVENT_NOT_RECORDED",
            ),
            _check(
                "command output stdout not captured",
                not _truthy(command_output.get("stdout_captured")),
                "stdout not captured by command output",
                command_output.get("stdout_captured"),
                "COMMAND_OUTPUT_ALREADY_CAPTURED_STDOUT",
            ),
            _check(
                "command output stderr not captured",
                not _truthy(command_output.get("stderr_captured")),
                "stderr not captured by command output",
                command_output.get("stderr_captured"),
                "COMMAND_OUTPUT_ALREADY_CAPTURED_STDERR",
            ),
            _check(
                "command output process output not captured",
                not _truthy(command_output.get("process_output_captured")),
                "process output not captured by command output",
                command_output.get("process_output_captured"),
                "COMMAND_OUTPUT_ALREADY_CAPTURED_PROCESS_OUTPUT",
            ),
            _check(
                "command output raw output body not captured",
                not _truthy(command_output.get("raw_output_body_captured")),
                "raw output body not captured by command output",
                command_output.get("raw_output_body_captured"),
                "COMMAND_OUTPUT_ALREADY_CAPTURED_RAW_OUTPUT_BODY",
            ),
            _check(
                "command output did not create output capture",
                not _truthy(command_output.get("output_capture_created")),
                "output capture not created by command output",
                command_output.get("output_capture_created"),
                "COMMAND_OUTPUT_ALREADY_CREATED_OUTPUT_CAPTURE",
            ),
            _check(
                "command output did not create output report artifact",
                not _truthy(command_output.get("command_output_report_artifact_created")),
                "output report artifact not created by command output",
                command_output.get("command_output_report_artifact_created"),
                "COMMAND_OUTPUT_ALREADY_CREATED_OUTPUT_REPORT_ARTIFACT",
            ),
            _check(
                "command output did not create command result",
                not _truthy(command_output.get("command_result_created")),
                "command result not created by command output",
                command_output.get("command_result_created"),
                "COMMAND_OUTPUT_ALREADY_CREATED_RESULT",
            ),
            _check(
                "command output did not create command success",
                not _truthy(command_output.get("command_success_created")),
                "command success not created by command output",
                command_output.get("command_success_created"),
                "COMMAND_OUTPUT_ALREADY_CREATED_SUCCESS",
            ),
            _check(
                "command output boundary basis declared",
                _basis_declared(request, "selected_command_output_boundary_basis"),
                "selected command output boundary basis declared",
                request.get("selected_command_output_boundary_basis"),
                "COMMAND_OUTPUT_BOUNDARY_BASIS_MISSING",
            ),
            _check(
                "command output boundary outcome recorded",
                command_output_boundary.get("outcome") in (None, COMMAND_OUTPUT_BOUNDARY_OUTCOME),
                COMMAND_OUTPUT_BOUNDARY_OUTCOME,
                command_output_boundary.get("outcome"),
                "COMMAND_OUTPUT_BOUNDARY_BASIS_MISSING",
            ),
            _check(
                "command output containment basis declared",
                _basis_declared(request, "selected_command_output_containment_basis"),
                "selected command output containment basis declared",
                request.get("selected_command_output_containment_basis"),
                "COMMAND_OUTPUT_CONTAINMENT_BASIS_MISSING",
            ),
            _check(
                "command output containment outcome recorded",
                command_output_containment.get("outcome") in (None, COMMAND_OUTPUT_CONTAINMENT_OUTCOME),
                COMMAND_OUTPUT_CONTAINMENT_OUTCOME,
                command_output_containment.get("outcome"),
                "COMMAND_OUTPUT_CONTAINMENT_BASIS_MISSING",
            ),
            _check(
                "post-invocation command execution basis declared",
                _basis_declared(request, "selected_post_invocation_command_execution_basis"),
                "selected post-invocation command execution basis declared",
                request.get("selected_post_invocation_command_execution_basis"),
                "POST_INVOCATION_COMMAND_EXECUTION_BASIS_MISSING",
            ),
            _check(
                "post-invocation command execution terminal summary basis declared",
                _basis_declared(
                    request, "selected_post_invocation_command_execution_terminal_summary_basis"
                ),
                "selected post-invocation command execution terminal summary basis declared",
                request.get("selected_post_invocation_command_execution_terminal_summary_basis"),
                "POST_INVOCATION_COMMAND_EXECUTION_BASIS_MISSING",
            ),
            _check(
                "post-invocation command execution outcome recorded",
                post_invocation.get("outcome") == POST_INVOCATION_COMMAND_EXECUTION_OUTCOME,
                POST_INVOCATION_COMMAND_EXECUTION_OUTCOME,
                post_invocation.get("outcome"),
                "POST_INVOCATION_COMMAND_EXECUTION_NOT_RECORDED",
            ),
            _check(
                "post-invocation command execution failed check count zero",
                _to_int(post_invocation.get("failed_check_count")) in (None, 0),
                0,
                post_invocation.get("failed_check_count"),
                "POST_INVOCATION_COMMAND_EXECUTION_FAILED_CHECKS_PRESENT",
            ),
            _check(
                "post-invocation command execution trace audit-only",
                _truthy(post_invocation.get("execution_trace_audit_only")),
                "execution trace audit-only",
                post_invocation.get("execution_trace_audit_only"),
                "POST_INVOCATION_COMMAND_EXECUTION_TRACE_NOT_AUDIT_ONLY",
            ),
            _check(
                "command invocation basis declared",
                bool(command_invocation),
                "selected command invocation basis declared",
                command_invocation,
                "COMMAND_OUTPUT_BASIS_MISSING",
            ),
            _check(
                "command execution review basis declared",
                bool(command_execution_review),
                "selected command execution review basis declared",
                command_execution_review,
                "COMMAND_OUTPUT_BASIS_MISSING",
            ),
            _check(
                "request-consumption basis declared",
                bool(request_consumption),
                "selected request-consumption basis declared",
                request_consumption,
                "COMMAND_OUTPUT_BASIS_MISSING",
            ),
            _check(
                "consumed request basis declared",
                bool(consumed_request),
                "selected consumed request basis declared",
                consumed_request,
                "CONSUMED_REQUEST_REOPENED",
            ),
            _check(
                "v2 admitted request basis declared",
                bool(v2.get("declared")),
                "selected v2 admitted request basis declared",
                v2,
                "V2_ADMITTED_REQUEST_BASIS_MISSING",
            ),
            _check(
                "v2 admitted request failed check count zero",
                _to_int(v2.get("failed_check_count")) in (None, 0),
                0,
                v2.get("failed_check_count"),
                "V2_ADMITTED_REQUEST_FAILED_CHECKS_PRESENT",
            ),
            _check(
                "v1 predecessor failure basis declared",
                bool(v1),
                "selected v1 predecessor/failure basis declared",
                v1,
                "V1_PREDECESSOR_FAILURE_BASIS_MISSING",
            ),
            _check(
                "older command execution boundary lineage prior scaffolding only",
                bool(older_lineage) and not _lineage_as_current_execution(older_lineage),
                "older lineage basis remains prior scaffolding only",
                older_lineage,
                "OLDER_COMMAND_EXECUTION_BOUNDARY_LINEAGE_TREATED_AS_CURRENT_EXECUTION",
            ),
            _check(
                "command report basis declared",
                _basis_declared(request, "selected_command_report_basis"),
                "selected command report basis declared",
                request.get("selected_command_report_basis"),
                "COMMAND_REPORT_BASIS_MISSING",
            ),
            _check(
                "command implementation boundary basis declared",
                _basis_declared(request, "selected_command_implementation_boundary_basis"),
                "selected command implementation boundary basis declared",
                request.get("selected_command_implementation_boundary_basis"),
                "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING",
            ),
            _check(
                "command boundary basis declared",
                _basis_declared(request, "selected_command_boundary_basis"),
                "selected command boundary basis declared",
                request.get("selected_command_boundary_basis"),
                "COMMAND_BOUNDARY_BASIS_MISSING",
            ),
            _check(
                "artifact emission containment basis declared",
                _basis_declared(request, "selected_artifact_emission_containment_basis"),
                "selected artifact emission containment basis declared",
                request.get("selected_artifact_emission_containment_basis"),
                "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING",
            ),
            _check(
                "evidence-manifest basis declared",
                _basis_declared(request, "selected_evidence_manifest_basis"),
                "selected evidence-manifest basis declared",
                request.get("selected_evidence_manifest_basis"),
                "EVIDENCE_MANIFEST_BASIS_MISSING",
            ),
            _check(
                "portable verification basis declared",
                _basis_declared(request, "selected_portable_verification_basis"),
                "selected portable verification basis declared",
                request.get("selected_portable_verification_basis"),
                "PORTABLE_VERIFICATION_BASIS_MISSING",
            ),
        ]
    )

    posture_codes = {
        "output_capture_only_posture": "OUTPUT_CAPTURE_ONLY_POSTURE_MISSING",
        "one_bounded_output_capture_event_posture": "ONE_BOUNDED_OUTPUT_CAPTURE_EVENT_POSTURE_MISSING",
        "output_capture_boundary_basis_preserved_posture": (
            "OUTPUT_CAPTURE_BOUNDARY_BASIS_PRESERVED_POSTURE_MISSING"
        ),
        "command_output_basis_preserved_posture": "COMMAND_OUTPUT_BASIS_PRESERVED_POSTURE_MISSING",
        "bounded_command_output_event_preserved_posture": (
            "BOUNDED_COMMAND_OUTPUT_EVENT_PRESERVED_POSTURE_MISSING"
        ),
        "execution_trace_audit_only_posture": "EXECUTION_TRACE_AUDIT_ONLY_POSTURE_MISSING",
        "no_stdout_content_invented_posture": "NO_STDOUT_CONTENT_INVENTED_POSTURE_MISSING",
        "no_stderr_content_invented_posture": "NO_STDERR_CONTENT_INVENTED_POSTURE_MISSING",
        "no_process_output_content_invented_posture": (
            "NO_PROCESS_OUTPUT_CONTENT_INVENTED_POSTURE_MISSING"
        ),
        "no_raw_output_body_content_invented_posture": (
            "NO_RAW_OUTPUT_BODY_CONTENT_INVENTED_POSTURE_MISSING"
        ),
        "no_output_report_artifact_posture": "NO_OUTPUT_REPORT_ARTIFACT_POSTURE_MISSING",
        "no_command_result_posture": "NO_COMMAND_RESULT_POSTURE_MISSING",
        "no_command_success_posture": "NO_COMMAND_SUCCESS_POSTURE_MISSING",
        "no_output_as_source_posture": "NO_OUTPUT_AS_SOURCE_POSTURE_MISSING",
        "no_result_as_authority_posture": "NO_RESULT_AS_AUTHORITY_POSTURE_MISSING",
        "no_success_as_currentness_posture": "NO_SUCCESS_AS_CURRENTNESS_POSTURE_MISSING",
        "no_final_completion_posture": "NO_FINAL_COMPLETION_POSTURE_MISSING",
        "authorization_token_reuse_blocked_posture": "AUTHORIZATION_TOKEN_REUSED",
        "consumed_token_closed_posture": "CONSUMED_REQUEST_REOPENED",
        "no_reopen_consumed_request_posture": "CONSUMED_REQUEST_REOPENED",
        "returned_result_containment_posture": "NON_CLAIM_MISSING_OR_FLIPPED",
        "reference_shaped_input_posture": "REFERENCE_SHAPED_INPUT_POSTURE_MISSING",
    }
    for key in POSTURE_KEYS:
        checks.append(
            _check(
                f"{key} declared",
                _posture_declared(request, key),
                f"{key} declared",
                request.get(key),
                posture_codes.get(key, "OUTPUT_CAPTURE_ONLY_POSTURE_MISSING"),
            )
        )

    checks.extend(
        [
            _check(
                "output capture scope supported",
                bool(scope_values) and not unsupported_scope,
                SUPPORTED_OUTPUT_CAPTURE_SCOPE,
                scope_values,
                "UNSUPPORTED_OUTPUT_CAPTURE_SCOPE",
            ),
            _check(
                "output capture not output report artifact",
                not _flag_true(request, ("output_capture_treated_as_output_report_artifact",)),
                "output capture is not output report artifact",
                request.get("output_capture_treated_as_output_report_artifact"),
                "OUTPUT_CAPTURE_TREATED_AS_OUTPUT_REPORT_ARTIFACT",
            ),
            _check(
                "output capture not result",
                not _flag_true(request, ("output_capture_treated_as_result",)),
                "output capture is not result",
                request.get("output_capture_treated_as_result"),
                "OUTPUT_CAPTURE_TREATED_AS_RESULT",
            ),
            _check(
                "output capture not success",
                not _flag_true(request, ("output_capture_treated_as_success",)),
                "output capture is not success",
                request.get("output_capture_treated_as_success"),
                "OUTPUT_CAPTURE_TREATED_AS_SUCCESS",
            ),
            _check(
                "output capture not source",
                not _flag_true(request, ("output_capture_treated_as_source",)),
                "output capture is not source",
                request.get("output_capture_treated_as_source"),
                "OUTPUT_CAPTURE_TREATED_AS_SOURCE",
            ),
            _check(
                "output capture not authority",
                not _flag_true(request, ("output_capture_treated_as_authority",)),
                "output capture is not authority",
                request.get("output_capture_treated_as_authority"),
                "OUTPUT_CAPTURE_TREATED_AS_AUTHORITY",
            ),
            _check(
                "output capture not currentness",
                not _flag_true(request, ("output_capture_treated_as_currentness",)),
                "output capture is not currentness",
                request.get("output_capture_treated_as_currentness"),
                "OUTPUT_CAPTURE_TREATED_AS_CURRENTNESS",
            ),
            _check(
                "output capture not final completion",
                not _flag_true(request, ("output_capture_treated_as_final_completion",)),
                "output capture is not final completion",
                request.get("output_capture_treated_as_final_completion"),
                "OUTPUT_CAPTURE_TREATED_AS_FINAL_COMPLETION",
            ),
            _check(
                "command output not output report artifact",
                not _flag_true(request, ("command_output_treated_as_output_report_artifact",)),
                "command output is not output report artifact",
                request.get("command_output_treated_as_output_report_artifact"),
                "COMMAND_OUTPUT_TREATED_AS_OUTPUT_REPORT_ARTIFACT",
            ),
            _check(
                "command output not result",
                not _flag_true(request, ("command_output_treated_as_result",)),
                "command output is not result",
                request.get("command_output_treated_as_result"),
                "COMMAND_OUTPUT_TREATED_AS_RESULT",
            ),
            _check(
                "command output not success",
                not _flag_true(request, ("command_output_treated_as_success",)),
                "command output is not success",
                request.get("command_output_treated_as_success"),
                "COMMAND_OUTPUT_TREATED_AS_SUCCESS",
            ),
            _check(
                "command output not source",
                not _flag_true(request, ("command_output_treated_as_source",)),
                "command output is not source",
                request.get("command_output_treated_as_source"),
                "COMMAND_OUTPUT_TREATED_AS_SOURCE",
            ),
            _check(
                "command output not authority",
                not _flag_true(request, ("command_output_treated_as_authority",)),
                "command output is not authority",
                request.get("command_output_treated_as_authority"),
                "COMMAND_OUTPUT_TREATED_AS_AUTHORITY",
            ),
            _check(
                "command output not currentness",
                not _flag_true(request, ("command_output_treated_as_currentness",)),
                "command output is not currentness",
                request.get("command_output_treated_as_currentness"),
                "COMMAND_OUTPUT_TREATED_AS_CURRENTNESS",
            ),
            _check(
                "command output not final completion",
                not _flag_true(request, ("command_output_treated_as_final_completion",)),
                "command output is not final completion",
                request.get("command_output_treated_as_final_completion"),
                "COMMAND_OUTPUT_TREATED_AS_FINAL_COMPLETION",
            ),
            _check(
                "execution trace not output capture",
                not _flag_true(request, ("execution_trace_treated_as_output_capture",)),
                "execution trace is not output capture",
                request.get("execution_trace_treated_as_output_capture"),
                "EXECUTION_TRACE_TREATED_AS_OUTPUT_CAPTURE",
            ),
            _check(
                "execution trace not result",
                not _flag_true(request, ("execution_trace_treated_as_result",)),
                "execution trace is not result",
                request.get("execution_trace_treated_as_result"),
                "EXECUTION_TRACE_TREATED_AS_RESULT",
            ),
            _check(
                "execution trace not success",
                not _flag_true(request, ("execution_trace_treated_as_success",)),
                "execution trace is not success",
                request.get("execution_trace_treated_as_success"),
                "EXECUTION_TRACE_TREATED_AS_SUCCESS",
            ),
            _check(
                "execution trace not source",
                not _flag_true(request, ("execution_trace_treated_as_source",)),
                "execution trace is not source",
                request.get("execution_trace_treated_as_source"),
                "EXECUTION_TRACE_TREATED_AS_SOURCE",
            ),
            _check(
                "execution trace not authority",
                not _flag_true(request, ("execution_trace_treated_as_authority",)),
                "execution trace is not authority",
                request.get("execution_trace_treated_as_authority"),
                "EXECUTION_TRACE_TREATED_AS_AUTHORITY",
            ),
            _check(
                "stdout content not invented",
                not _flag_true(request, ("stdout_content_invented",))
                and not _contains_present_key(request, ("stdout_content", "stdout_body", "actual_stdout")),
                "stdout content not invented",
                request.get("stdout_content_invented"),
                "STDOUT_CONTENT_INVENTED",
            ),
            _check(
                "stderr content not invented",
                not _flag_true(request, ("stderr_content_invented",))
                and not _contains_present_key(request, ("stderr_content", "stderr_body", "actual_stderr")),
                "stderr content not invented",
                request.get("stderr_content_invented"),
                "STDERR_CONTENT_INVENTED",
            ),
            _check(
                "process-output content not invented",
                not _flag_true(request, ("process_output_content_invented",))
                and not _contains_present_key(
                    request,
                    ("process_output_content", "process_output_body", "actual_process_output"),
                ),
                "process-output content not invented",
                request.get("process_output_content_invented"),
                "PROCESS_OUTPUT_CONTENT_INVENTED",
            ),
            _check(
                "raw output body content not invented",
                not _flag_true(request, ("raw_output_body_content_invented",))
                and not _contains_present_key(
                    request,
                    ("raw_output_body_content", "raw_command_output_body", "raw_output_body"),
                ),
                "raw output body content not invented",
                request.get("raw_output_body_content_invented"),
                "RAW_OUTPUT_BODY_CONTENT_INVENTED",
            ),
            _check(
                "output report artifact not created",
                not _flag_true(
                    request,
                    ("command_output_report_artifact_created", "output_report_artifact_created"),
                ),
                "output report artifact not created",
                request.get("command_output_report_artifact_created"),
                "COMMAND_OUTPUT_REPORT_ARTIFACT_CREATED",
            ),
            _check(
                "command result not created",
                not _flag_true(request, ("command_result_created",)),
                "command result not created",
                request.get("command_result_created"),
                "COMMAND_RESULT_CREATED",
            ),
            _check(
                "command success not created",
                not _flag_true(request, ("command_success_created",)),
                "command success not created",
                request.get("command_success_created"),
                "COMMAND_SUCCESS_CREATED",
            ),
            _check(
                "result not authority",
                not _flag_true(request, ("command_result_became_authority",)),
                "command result not authority",
                request.get("command_result_became_authority"),
                "COMMAND_RESULT_TREATED_AS_AUTHORITY",
            ),
            _check(
                "success not currentness",
                not _flag_true(request, ("command_success_created_currentness",)),
                "command success not currentness",
                request.get("command_success_created_currentness"),
                "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS",
            ),
            _check(
                "success not final completion",
                not _flag_true(request, ("command_success_claimed_final_completion",)),
                "command success not final completion",
                request.get("command_success_claimed_final_completion"),
                "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION",
            ),
            _check(
                "consumed request not reopened",
                not _flag_true(request, ("consumed_request_reopened",)),
                "consumed request token remains closed",
                request.get("consumed_request_reopened"),
                "CONSUMED_REQUEST_REOPENED",
            ),
            _check(
                "authorization token not reused",
                not _flag_true(request, ("authorization_token_reused",)),
                "authorization token reuse blocked",
                request.get("authorization_token_reused"),
                "AUTHORIZATION_TOKEN_REUSED",
            ),
            _check(
                "v1 not repaired",
                not _flag_true(request, ("v1_repaired",)),
                "v1 predecessor failure not repaired",
                request.get("v1_repaired"),
                "V2_TREATED_AS_REPAIRING_V1",
            ),
            _check(
                "v1 failure not hidden",
                not _flag_true(request, ("v1_hidden",)),
                "v1 predecessor failure not hidden",
                request.get("v1_hidden"),
                "V1_FAILURE_HIDDEN",
            ),
            _check(
                "v1 not claimed passed",
                not _flag_true(request, ("v1_claimed_passed",)),
                "v1 predecessor failure not claimed passed",
                request.get("v1_claimed_passed"),
                "V1_CLAIMED_PASSED",
            ),
            _check(
                "full prior artifact body not emitted",
                not _contains_present_key(request, FORBIDDEN_FULL_BODY_KEYS),
                "full prior artifact body not emitted",
                "declared reference-shaped input posture",
                "FULL_PRIOR_ARTIFACT_BODY_EMITTED",
            ),
            _check(
                "artifacts not mutated",
                not _flag_true(request, ("prior_artifacts_mutated", "artifacts_mutated")),
                "artifacts not mutated",
                request.get("prior_artifacts_mutated"),
                "ARTIFACTS_MUTATED",
            ),
            _check(
                "deployment not created",
                not _flag_true(request, ("deployment_created",)),
                "deployment not created",
                request.get("deployment_created"),
                "DEPLOYMENT_CREATED",
            ),
            _check(
                "runtime hosting not created",
                not _flag_true(request, ("runtime_hosting_created",)),
                "runtime hosting not created",
                request.get("runtime_hosting_created"),
                "RUNTIME_HOSTING_CREATED",
            ),
            _check(
                "public release not created",
                not _flag_true(request, ("public_release_created",)),
                "public release not created",
                request.get("public_release_created"),
                "PUBLIC_RELEASE_CREATED",
            ),
            _check(
                "operation permission not created",
                not _flag_true(request, ("operation_permission_created",)),
                "operation permission not created",
                request.get("operation_permission_created"),
                "OPERATION_CREATED",
            ),
            _check(
                "public readiness not created",
                not _flag_true(
                    request, ("public_launch_readiness_created", "public_readiness_created")
                ),
                "public readiness not created",
                request.get("public_launch_readiness_created"),
                "PUBLIC_READINESS_CREATED",
            ),
            _check(
                "final completion not claimed",
                not _flag_true(request, ("final_completion_claimed",)),
                "final completion not claimed",
                request.get("final_completion_claimed"),
                "FINAL_COMPLETION_CLAIMED",
            ),
            _check(
                "continuation not authorized",
                not _flag_true(request, ("continuation_authorized",)),
                "continuation not authorized",
                request.get("continuation_authorized"),
                "CONTINUATION_AUTHORIZED",
            ),
            _check(
                "publication flow not opened",
                not _flag_true(request, ("publication_flow_opened",)),
                "publication flow not opened",
                request.get("publication_flow_opened"),
                "CONTINUATION_AUTHORIZED",
            ),
            _check(
                "reusable permission not created",
                not _flag_true(request, ("reusable_permission_created",)),
                "reusable permission not created",
                request.get("reusable_permission_created"),
                "REUSABLE_PERMISSION_CREATED",
            ),
            _check(
                "follow-on work not authorized",
                not _flag_true(request, ("follow_on_work_authorized",)),
                "follow-on work not authorized",
                request.get("follow_on_work_authorized"),
                "FOLLOW_ON_WORK_AUTHORIZED",
            ),
            _check(
                "derivative reception not authorized",
                not _flag_true(request, ("derivative_reception_authorized",)),
                "derivative reception not authorized",
                request.get("derivative_reception_authorized"),
                "DERIVATIVE_RECEPTION_AUTHORIZED",
            ),
            _check(
                "vessel relation not authorized",
                not _flag_true(request, ("vessel_relation_authorized",)),
                "vessel relation not authorized",
                request.get("vessel_relation_authorized"),
                "VESSEL_RELATION_AUTHORIZED",
            ),
            _check(
                "another reception request not authorized",
                not _flag_true(request, ("another_reception_request_authorized",)),
                "another reception request not authorized",
                request.get("another_reception_request_authorized"),
                "ANOTHER_RECEPTION_REQUEST_AUTHORIZED",
            ),
            _check(
                "mutation/replay/merge not detected",
                not _flag_true(request, ("mutation_performed", "replay_performed", "merge_performed")),
                "mutation/replay/merge not performed",
                "declared mutation/replay/merge posture",
                "MUTATION_REPLAY_OR_MERGE_DETECTED",
            ),
            _check(
                "required non-claims explicit and false",
                all(
                    key in declared_non_claims and _explicit_false(declared_non_claims.get(key))
                    for key in REQUIRED_FALSE_NON_CLAIMS
                ),
                "all required non-claims explicit false",
                declared_non_claims,
                "NON_CLAIM_MISSING_OR_FLIPPED",
            ),
        ]
    )
    return checks


def _first_failed_check(checks: Sequence[Mapping[str, Any]]) -> Mapping[str, Any] | None:
    for check in checks:
        if not check.get("passed"):
            return check
    return None


def _determine_outcome(
    request: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    forced_block_code: str | None = None,
) -> tuple[str, dict[str, Any]]:
    requested = _requested_outcome(request)
    intent = request.get("output_capture_intent")

    if forced_block_code:
        return OUTCOME_BLOCKED, _block_object(True, forced_block_code, request.get("block_reason"))

    if intent == INTENT_BLOCK:
        return OUTCOME_BLOCKED, _block_object(
            True, "OUTPUT_CAPTURE_BLOCKED_BY_REQUEST", request.get("block_reason")
        )

    failed = _first_failed_check(checks)
    if failed:
        code = str(failed.get("block_code") or "DECLARED_OUTPUT_CAPTURE_REQUEST_MALFORMED")
        reason = f"{failed.get('check_name')}: {failed.get('actual_posture')}"
        if requested == OUTCOME_REQUIRES_ADDITIONAL_BASIS and code.endswith("_MISSING"):
            return OUTCOME_REQUIRES_ADDITIONAL_BASIS, _block_object(False, None, None)
        if requested == OUTCOME_NOT_RECORDED:
            return OUTCOME_NOT_RECORDED, _block_object(False, None, None)
        return OUTCOME_BLOCKED, _block_object(True, code, reason)

    if intent == INTENT_DO_NOT_RECORD or requested == OUTCOME_NOT_RECORDED:
        return OUTCOME_NOT_RECORDED, _block_object(False, None, None)

    if requested == OUTCOME_REQUIRES_ADDITIONAL_BASIS or _present(
        request.get("additional_basis_context")
    ):
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS, _block_object(False, None, None)

    return OUTCOME_RECORDED, _block_object(False, None, None)


def _additional_basis_required(outcome: str, request: Mapping[str, Any]) -> dict[str, Any]:
    required = outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    return {
        "required": required,
        "basis": _sanitize(request.get("additional_basis_context")) if required else {},
        "missing_basis_not_scheduled": True,
        "missing_basis_not_authorized": True,
        "missing_basis_not_executed": True,
    }


def _not_recorded_basis(outcome: str, request: Mapping[str, Any]) -> dict[str, Any]:
    not_recorded = outcome == OUTCOME_NOT_RECORDED
    return {
        "not_recorded": not_recorded,
        "basis": _sanitize(request.get("not_recorded_basis")) if not_recorded else {},
        "reason": request.get("block_reason") if not_recorded else None,
        "prior_artifacts_mutated": False,
        "next_work_authorized": False,
    }


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": list(OPEN_ITEMS),
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }


def build_portable_source_body_verification_output_capture_summary(
    result: Mapping[str, Any]
) -> dict[str, Any]:
    checks = list(result.get("output_capture_checks", []))
    passed = sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed"))
    failed = sum(1 for check in checks if isinstance(check, Mapping) and not check.get("passed"))
    statement = _mapping(result.get("output_capture_statement"))
    non_claims = _mapping(result.get("non_claims"))
    boundary = _mapping(result.get("selected_output_capture_boundary_basis"))
    command_output = _mapping(result.get("selected_command_output_basis"))
    post_invocation = _mapping(result.get("selected_post_invocation_command_execution_basis"))
    v2 = _mapping(result.get("selected_v2_admitted_request_basis"))
    declared_question = _mapping(result.get("declared_output_capture_question"))
    block = _mapping(result.get("block"))
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") or block.get("code"),
        "block_reason": block.get("block_reason") or block.get("reason"),
        "output_capture_request_id": declared_question.get("output_capture_request_id"),
        "question": declared_question.get("output_capture_question"),
        "intent": declared_question.get("output_capture_intent"),
        "passed_check_count": passed,
        "failed_check_count": failed,
        "output_capture_recorded": statement.get("output_capture_recorded", False),
        "bounded_output_capture_event_recorded": statement.get(
            "bounded_output_capture_event_recorded", False
        ),
        "output_capture_boundary_basis_preserved": statement.get(
            "output_capture_boundary_basis_preserved", False
        ),
        "command_output_basis_preserved": statement.get("command_output_basis_preserved", False),
        "bounded_command_output_event_preserved": statement.get(
            "bounded_command_output_event_preserved", False
        ),
        "recorded_command_execution_event_preserved": statement.get(
            "recorded_command_execution_event_preserved", False
        ),
        "execution_trace_audit_only_preserved": statement.get(
            "execution_trace_audit_only_preserved", False
        ),
        "stdout_content_present": statement.get("stdout_content_present", False),
        "stderr_content_present": statement.get("stderr_content_present", False),
        "process_output_content_present": statement.get("process_output_content_present", False),
        "raw_output_body_content_present": statement.get("raw_output_body_content_present", False),
        "stdout_content_absent_without_invention": statement.get(
            "stdout_content_absent_without_invention", False
        ),
        "stderr_content_absent_without_invention": statement.get(
            "stderr_content_absent_without_invention", False
        ),
        "process_output_content_absent_without_invention": statement.get(
            "process_output_content_absent_without_invention", False
        ),
        "raw_output_body_content_absent_without_invention": statement.get(
            "raw_output_body_content_absent_without_invention", False
        ),
        "command_output_report_artifact_not_created": statement.get(
            "command_output_report_artifact_not_created", False
        ),
        "command_result_still_not_created": statement.get("command_result_still_not_created", False),
        "command_success_still_not_created": statement.get(
            "command_success_still_not_created", False
        ),
        "selected_output_capture_boundary_outcome": boundary.get("outcome"),
        "selected_output_capture_boundary_failed_check_count": boundary.get("failed_check_count"),
        "selected_command_output_outcome": command_output.get("outcome"),
        "selected_command_output_failed_check_count": command_output.get("failed_check_count"),
        "selected_post_invocation_execution_outcome": post_invocation.get("outcome"),
        "selected_post_invocation_execution_failed_check_count": post_invocation.get(
            "failed_check_count"
        ),
        "selected_v2_outcome": v2.get("outcome"),
        "selected_v2_version": v2.get("version"),
        "selected_v2_failed_check_count": v2.get("failed_check_count"),
        "output_capture_not_report_result_success_source_authority_currentness_final_completion": not any(
            non_claims.get(key, False)
            for key in (
                "output_capture_treated_as_output_report_artifact",
                "output_capture_treated_as_result",
                "output_capture_treated_as_success",
                "output_capture_treated_as_source",
                "output_capture_treated_as_authority",
                "output_capture_treated_as_currentness",
                "output_capture_treated_as_final_completion",
            )
        ),
        "command_output_not_report_result_success_source_authority_currentness_final_completion": not any(
            non_claims.get(key, False)
            for key in (
                "command_output_treated_as_output_report_artifact",
                "command_output_treated_as_result",
                "command_output_treated_as_success",
                "command_output_treated_as_source",
                "command_output_treated_as_authority",
                "command_output_treated_as_currentness",
                "command_output_treated_as_final_completion",
            )
        ),
        "execution_trace_not_output_capture_result_success_source_authority": not any(
            non_claims.get(key, False)
            for key in (
                "execution_trace_treated_as_output_capture",
                "execution_trace_treated_as_result",
                "execution_trace_treated_as_success",
                "execution_trace_treated_as_source",
                "execution_trace_treated_as_authority",
            )
        ),
        "result_not_authority": not non_claims.get("command_result_became_authority", False),
        "success_not_currentness_final_completion": not (
            non_claims.get("command_success_created_currentness", False)
            or non_claims.get("command_success_claimed_final_completion", False)
        ),
        "older_command_execution_boundary_lineage_not_treated_as_current_execution": _mapping(
            result.get("selected_older_command_execution_boundary_lineage_basis")
        ).get("lineage_basis_not_treated_as_current_execution", False),
        "no_raw_full_prior_artifact_body": not non_claims.get(
            "raw_full_prior_artifact_body_returned", False
        ),
        "no_artifact_mutation": not non_claims.get("prior_artifacts_mutated", False),
        "no_deployment_runtime_public_release": not any(
            non_claims.get(key, False)
            for key in ("deployment_created", "runtime_hosting_created", "public_release_created")
        ),
        "no_operation_public_readiness_final_completion": not any(
            non_claims.get(key, False)
            for key in (
                "operation_permission_created",
                "public_launch_readiness_created",
                "final_completion_claimed",
            )
        ),
        "no_continuation_publication_reusable_follow_on": not any(
            non_claims.get(key, False)
            for key in (
                "continuation_authorized",
                "publication_flow_opened",
                "reusable_permission_created",
                "follow_on_work_authorized",
            )
        ),
        "key_non_claims": _sanitize(non_claims),
    }


def _result_metadata(request: Mapping[str, Any]) -> dict[str, Any]:
    request_id = str(request.get("output_capture_request_id") or "output_capture_request")
    return {
        "portable_source_body_verification_output_capture_result_id": (
            f"{request_id}__portable_source_body_verification_output_capture_result"
        ),
        "portable_source_body_verification_output_capture_result_type": RESULT_TYPE,
        "portable_source_body_verification_output_capture_result_version": RESULT_VERSION,
        "generated_at": _now(),
        "resolver_module": RESOLVER_MODULE,
        "short_resolver_filename": "resolve_portable_source_body_verification_output_capture.py",
        "full_upstream_lineage_preserved_inside_selected_basis": True,
    }


def _base_result(
    request: Mapping[str, Any],
    outcome: str,
    block: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    result: dict[str, Any] = {
        "portable_source_body_verification_output_capture_metadata": _result_metadata(request),
        "declared_output_capture_question": {
            "output_capture_request_id": request.get("output_capture_request_id"),
            "output_capture_question": request.get("output_capture_question"),
            "core_output_capture_question": CORE_OUTPUT_CAPTURE_QUESTION,
            "output_capture_intent": request.get("output_capture_intent"),
            "requested_output_capture_outcome": request.get("requested_output_capture_outcome"),
        },
        "selected_output_capture_boundary_basis": _selected_output_capture_boundary_basis(request),
        "selected_output_capture_boundary_terminal_summary_basis": _terminal_summary_basis(
            request, "selected_output_capture_boundary_terminal_summary_basis"
        ),
        "selected_command_output_basis": _selected_command_output_basis(request),
        "selected_command_output_terminal_summary_basis": _terminal_summary_basis(
            request, "selected_command_output_terminal_summary_basis"
        ),
        "selected_command_output_boundary_basis": _selected_prior_basis(
            request,
            "selected_command_output_boundary_basis",
            "selected_command_output_boundary_result_path",
            COMMAND_OUTPUT_BOUNDARY_OUTCOME,
        ),
        "selected_command_output_containment_basis": _selected_prior_basis(
            request,
            "selected_command_output_containment_basis",
            "selected_command_output_containment_result_path",
            COMMAND_OUTPUT_CONTAINMENT_OUTCOME,
        ),
        "selected_post_invocation_command_execution_basis": _selected_prior_basis(
            request,
            "selected_post_invocation_command_execution_basis",
            "selected_post_invocation_command_execution_result_path",
            POST_INVOCATION_COMMAND_EXECUTION_OUTCOME,
        ),
        "selected_post_invocation_command_execution_terminal_summary_basis": _terminal_summary_basis(
            request, "selected_post_invocation_command_execution_terminal_summary_basis"
        ),
        "selected_command_invocation_basis": _selected_prior_basis(
            request,
            "selected_command_invocation_basis",
            "selected_command_invocation_result_path",
            COMMAND_INVOCATION_OUTCOME,
        ),
        "selected_command_execution_review_basis": _selected_prior_basis(
            request,
            "selected_command_execution_review_basis",
            "selected_command_execution_review_result_path",
            COMMAND_EXECUTION_REVIEW_OUTCOME,
        ),
        "selected_request_consumption_basis": _selected_prior_basis(
            request,
            "selected_request_consumption_basis",
            "selected_request_consumption_result_path",
            REQUEST_CONSUMPTION_OUTCOME,
        ),
        "selected_consumed_request_basis": _selected_prior_basis(
            request, "selected_consumed_request_basis"
        ),
        "selected_v2_admitted_request_basis": _selected_prior_basis(
            request,
            "selected_v2_admitted_request_basis",
            "selected_v2_admitted_request_artifact_path",
            V2_ADMITTED_REQUEST_OUTCOME,
            V2_ADMITTED_REQUEST_VERSION,
        ),
        "selected_v1_predecessor_failure_basis": _selected_prior_basis(
            request,
            "selected_v1_predecessor_failure_basis",
            "selected_v1_predecessor_artifact_path",
        ),
        "selected_older_command_execution_boundary_lineage_basis": _selected_prior_basis(
            request,
            "selected_older_command_execution_boundary_lineage_basis",
            "selected_older_command_execution_boundary_lineage_result_path",
        ),
        "selected_command_report_basis": _selected_prior_basis(
            request, "selected_command_report_basis", "selected_command_report_path"
        ),
        "selected_command_implementation_boundary_basis": _selected_prior_basis(
            request,
            "selected_command_implementation_boundary_basis",
            "selected_command_implementation_boundary_result_path",
        ),
        "selected_command_boundary_basis": _selected_prior_basis(
            request, "selected_command_boundary_basis", "selected_command_boundary_result_path"
        ),
        "selected_artifact_emission_containment_basis": _selected_prior_basis(
            request,
            "selected_artifact_emission_containment_basis",
            "selected_artifact_emission_containment_result_path",
        ),
        "selected_evidence_manifest_basis": _selected_prior_basis(
            request, "selected_evidence_manifest_basis", "selected_evidence_manifest_result_path"
        ),
        "selected_portable_verification_basis": _selected_prior_basis(
            request, "selected_portable_verification_basis", "selected_portable_verification_result_path"
        ),
        "output_capture_scope": _scope_section(request),
        "output_capture_checks": list(checks),
        "output_capture_statement": _statement_for_outcome(outcome),
        "output_capture_non_meaning": _non_meaning(),
        "output_capture_event": _output_capture_event(outcome),
        "additional_basis_required": _additional_basis_required(outcome, request),
        "not_recorded_basis": _not_recorded_basis(outcome, request),
        "what_remains_open": _what_remains_open(),
        "non_claims": {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
        "outcome": outcome,
        "block": dict(block),
    }
    for key in POSTURE_KEYS:
        result[key] = _posture_section(request, key)
    result["portable_source_body_verification_output_capture_summary"] = (
        build_portable_source_body_verification_output_capture_summary(result)
    )
    return result


def resolve_portable_source_body_verification_output_capture(
    declared_output_capture_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    if declared_output_capture_request is None:
        request: dict[str, Any] = {
            "output_capture_request_id": "missing_output_capture_request",
            "output_capture_question": None,
            "output_capture_intent": None,
            "declared_non_claims": {},
        }
        checks = _build_checks(request)
        outcome, block = _determine_outcome(request, checks)
        return _base_result(request, outcome, block, checks)

    if not isinstance(declared_output_capture_request, Mapping):
        request: dict[str, Any] = {
            "output_capture_request_id": "malformed_output_capture_request",
            "output_capture_question": None,
            "output_capture_intent": None,
            "declared_non_claims": {},
        }
        checks = _build_checks(
            request,
            "DECLARED_OUTPUT_CAPTURE_REQUEST_MALFORMED",
            "declared output capture request must be a mapping",
        )
        outcome = OUTCOME_BLOCKED
        block = _block_object(
            True,
            "DECLARED_OUTPUT_CAPTURE_REQUEST_MALFORMED",
            "declared output capture request must be a mapping",
        )
        return _base_result(request, outcome, block, checks)

    request = _mapping(_copy(declared_output_capture_request))
    checks = _build_checks(request)
    outcome, block = _determine_outcome(request, checks)
    return _base_result(request, outcome, block, checks)


def resolve_portable_source_body_verification_output_capture_from_path(
    declared_output_capture_request_path: Path | str,
) -> dict[str, Any]:
    path = Path(declared_output_capture_request_path)
    try:
        raw = path.read_text(encoding="utf-8")
        loaded = json.loads(raw)
    except OSError as exc:
        request = {
            "output_capture_request_id": "unreadable_output_capture_request",
            "output_capture_question": None,
            "output_capture_intent": None,
            "declared_non_claims": {},
            "block_reason": str(exc),
        }
        checks = _build_checks(
            request,
            "DECLARED_OUTPUT_CAPTURE_REQUEST_UNREADABLE",
            f"unable to read declared output capture request path: {path}",
        )
        return _base_result(
            request,
            OUTCOME_BLOCKED,
            _block_object(True, "DECLARED_OUTPUT_CAPTURE_REQUEST_UNREADABLE", str(exc)),
            checks,
        )
    except json.JSONDecodeError as exc:
        request = {
            "output_capture_request_id": "malformed_output_capture_request",
            "output_capture_question": None,
            "output_capture_intent": None,
            "declared_non_claims": {},
            "block_reason": str(exc),
        }
        checks = _build_checks(
            request,
            "DECLARED_OUTPUT_CAPTURE_REQUEST_MALFORMED",
            f"malformed declared output capture request JSON: {path}",
        )
        return _base_result(
            request,
            OUTCOME_BLOCKED,
            _block_object(True, "DECLARED_OUTPUT_CAPTURE_REQUEST_MALFORMED", str(exc)),
            checks,
        )

    if not isinstance(loaded, Mapping):
        request = {
            "output_capture_request_id": "malformed_output_capture_request",
            "output_capture_question": None,
            "output_capture_intent": None,
            "declared_non_claims": {},
            "block_reason": "declared output capture request JSON must be an object",
        }
        checks = _build_checks(
            request,
            "DECLARED_OUTPUT_CAPTURE_REQUEST_MALFORMED",
            "declared output capture request JSON must be an object",
        )
        return _base_result(
            request,
            OUTCOME_BLOCKED,
            _block_object(
                True,
                "DECLARED_OUTPUT_CAPTURE_REQUEST_MALFORMED",
                "declared output capture request JSON must be an object",
            ),
            checks,
        )
    return resolve_portable_source_body_verification_output_capture(loaded)


def _safe_filename_part(value: Any) -> str:
    text = str(value or "output_capture_request").strip()
    safe = "".join(char if char.isalnum() or char in {"-", "_", "."} else "_" for char in text)
    return safe or "output_capture_request"


def _with_suffix_if_exists(path: Path) -> Path:
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


def write_portable_source_body_verification_output_capture_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    if output_path is None:
        declared = _mapping(result.get("declared_output_capture_question"))
        request_id = declared.get("output_capture_request_id")
        filename = (
            f"{_safe_filename_part(request_id)}__portable_source_body_verification_output_capture_result.json"
        )
        path = OUTPUT_ROOT / filename
    else:
        path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    final_path = _with_suffix_if_exists(path)
    final_path.write_text(
        json.dumps(_sanitize(result), indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return final_path


def build_declared_portable_source_body_verification_output_capture_request(
    output_capture_request_id: str,
    *,
    output_capture_question: str = CORE_OUTPUT_CAPTURE_QUESTION,
    output_capture_intent: str = INTENT_RECORD,
    output_capture_scope: Sequence[str] = SUPPORTED_OUTPUT_CAPTURE_SCOPE,
    requested_output_capture_outcome: str = OUTCOME_RECORDED,
    declared_non_claims: Mapping[str, Any] | None = None,
    **selected_basis_and_posture: Any,
) -> dict[str, Any]:
    request: dict[str, Any] = {
        "output_capture_request_id": output_capture_request_id,
        "output_capture_question": output_capture_question,
        "output_capture_intent": output_capture_intent,
        "output_capture_scope": list(output_capture_scope),
        "requested_output_capture_outcome": requested_output_capture_outcome,
        "declared_non_claims": {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
    }
    if declared_non_claims is not None:
        request["declared_non_claims"].update({key: _copy(value) for key, value in declared_non_claims.items()})
    for key in SELECTED_BASIS_KEYS:
        request.setdefault(key, selected_basis_and_posture.pop(key, {}))
    for key in POSTURE_KEYS:
        request.setdefault(key, selected_basis_and_posture.pop(key, {}))
    request.update(selected_basis_and_posture)
    return request
