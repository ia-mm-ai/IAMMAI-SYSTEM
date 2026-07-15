"""Portable source-body verification output capture boundary resolver.

This module records output-capture-boundary posture only. It is downstream of
the recorded command output line and may preserve one clean command output
basis for one future output capture step. It does not capture stdout, stderr,
process output, or raw command output body. It does not create output capture,
a command output/report artifact, command result, command success, source,
authority, currentness, final completion, continuation, reusable permission,
derivative reception, vessel relation, another reception request, or follow-on
work.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping


class PortableSourceBodyVerificationOutputCaptureBoundaryError(Exception):
    """Raised only for impossible output-capture-boundary resolver failures."""


RESOLVER_MODULE = "resolve_portable_source_body_verification_output_capture_boundary"
RESULT_VERSION = "0.1.0"
RESULT_TYPE = "portable_source_body_verification_output_capture_boundary_result"
OUTPUT_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_output_capture_boundary"
)
PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_BOUNDARY_ROOT = OUTPUT_ROOT

CORE_QUESTION = (
    "Can the recorded command output basis be bounded for one future output "
    "capture step without capturing stdout, stderr, process output, raw "
    "command output body, creating output capture, creating command "
    "output/report artifact, creating command result, creating command "
    "success, source, authority, currentness, final completion, continuation, "
    "reusable permission, derivative reception, vessel relation, another "
    "reception request, or follow-on work?"
)
CORE_OUTPUT_CAPTURE_BOUNDARY_QUESTION = CORE_QUESTION

OUTCOME_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_BOUNDARY_RECORDED"
OUTCOME_NOT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_BOUNDARY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_BOUNDARY_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)
OUTPUT_CAPTURE_BOUNDARY_OUTCOME = OUTCOME_RECORDED

INTENT_RECORD = "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_BOUNDARY"
INTENT_BLOCK = "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

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

SUPPORTED_OUTPUT_CAPTURE_BOUNDARY_SCOPE = (
    "OUTPUT_CAPTURE_BOUNDARY_ONLY",
    "ONE_FUTURE_OUTPUT_CAPTURE_STEP_ONLY",
    "COMMAND_OUTPUT_BASIS_PRESERVED",
    "BOUNDED_COMMAND_OUTPUT_EVENT_PRESERVED",
    "COMMAND_OUTPUT_BOUNDARY_BASIS_PRESERVED",
    "COMMAND_OUTPUT_CONTAINMENT_BASIS_PRESERVED",
    "RECORDED_COMMAND_EXECUTION_EVENT_PRESERVED",
    "EXECUTION_TRACE_AUDIT_ONLY_PRESERVED",
    "STDOUT_NOT_CAPTURED",
    "STDERR_NOT_CAPTURED",
    "PROCESS_OUTPUT_NOT_CAPTURED",
    "RAW_OUTPUT_BODY_NOT_CAPTURED",
    "OUTPUT_CAPTURE_NOT_CREATED",
    "COMMAND_OUTPUT_REPORT_ARTIFACT_NOT_CREATED",
    "COMMAND_RESULT_NOT_CREATED",
    "COMMAND_SUCCESS_NOT_CREATED",
    "OUTPUT_CAPTURE_BOUNDARY_IS_NOT_STDOUT_CAPTURE",
    "OUTPUT_CAPTURE_BOUNDARY_IS_NOT_STDERR_CAPTURE",
    "OUTPUT_CAPTURE_BOUNDARY_IS_NOT_PROCESS_OUTPUT_CAPTURE",
    "OUTPUT_CAPTURE_BOUNDARY_IS_NOT_RAW_OUTPUT_BODY_CAPTURE",
    "OUTPUT_CAPTURE_BOUNDARY_IS_NOT_OUTPUT_CAPTURE",
    "OUTPUT_CAPTURE_BOUNDARY_IS_NOT_OUTPUT_REPORT_ARTIFACT",
    "OUTPUT_CAPTURE_BOUNDARY_IS_NOT_RESULT",
    "OUTPUT_CAPTURE_BOUNDARY_IS_NOT_SUCCESS",
    "COMMAND_OUTPUT_IS_NOT_OUTPUT_CAPTURE",
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
SUPPORTED_OUTPUT_CAPTURE_BOUNDARY_SCOPE_SET = set(SUPPORTED_OUTPUT_CAPTURE_BOUNDARY_SCOPE)

REQUIRED_FALSE_NON_CLAIMS = (
    "stdout_captured",
    "stderr_captured",
    "process_output_captured",
    "raw_output_body_captured",
    "output_capture_created",
    "command_output_report_artifact_created",
    "command_result_created",
    "command_success_created",
    "output_capture_boundary_treated_as_stdout_capture",
    "output_capture_boundary_treated_as_stderr_capture",
    "output_capture_boundary_treated_as_process_output_capture",
    "output_capture_boundary_treated_as_raw_output_body_capture",
    "output_capture_boundary_treated_as_output_capture",
    "output_capture_boundary_treated_as_output_report_artifact",
    "output_capture_boundary_treated_as_result",
    "output_capture_boundary_treated_as_success",
    "command_output_treated_as_output_capture",
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
    "output_capture_boundary_recorded",
    "one_future_output_capture_step_declared",
    "command_output_basis_preserved",
    "bounded_command_output_event_preserved",
    "command_output_boundary_basis_preserved",
    "command_output_containment_basis_preserved",
    "recorded_command_execution_event_preserved",
    "execution_trace_audit_only_preserved",
    "stdout_still_not_captured",
    "stderr_still_not_captured",
    "process_output_still_not_captured",
    "raw_output_body_still_not_captured",
    "output_capture_not_created",
    "command_output_report_artifact_not_created",
    "command_result_still_not_created",
    "command_success_still_not_created",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
    "v1_predecessor_failure_preserved",
    "returned_result_containment_preserved",
)

FORBIDDEN_FULL_BODY_KEYS = {
    "full_prior_artifact_body",
    "raw_full_prior_artifact_body",
    "prior_artifact_body",
    "artifact_body",
    "raw_artifact_body",
    "full_artifact_body",
    "embedded_prior_artifact",
    "embedded_prior_artifacts",
}

FORBIDDEN_RAW_OUTPUT_KEYS = {
    "stdout",
    "stderr",
    "process_output",
    "command_output_body",
    "raw_command_output_body",
    "raw_output_body",
    "output_body",
    "captured_stdout",
    "captured_stderr",
    "captured_process_output",
    "captured_output",
    "result_body",
    "success_body",
    "source_body",
    "authority_body",
    "currentness_claim",
    "final_completion_claim",
}

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_output_capture_boundary_metadata",
    "declared_output_capture_boundary_question",
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
    "output_capture_boundary_only_posture",
    "one_future_output_capture_step_posture",
    "command_output_basis_preserved_posture",
    "bounded_command_output_event_preserved_posture",
    "command_output_boundary_basis_preserved_posture",
    "execution_trace_audit_only_posture",
    "no_stdout_capture_posture",
    "no_stderr_capture_posture",
    "no_process_output_capture_posture",
    "no_raw_output_body_capture_posture",
    "no_output_capture_posture",
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
    "output_capture_boundary_scope",
    "output_capture_boundary_checks",
    "output_capture_boundary_statement",
    "output_capture_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_output_capture_boundary_summary",
)


def _copy(value: Any) -> Any:
    return copy.deepcopy(value)


def _now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _mapping(value: Any) -> dict[str, Any]:
    if isinstance(value, Mapping):
        return dict(value)
    return {}


def _present(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, tuple, set, dict)):
        return bool(value)
    return True


def _truthy(value: Any) -> bool:
    if value is True:
        return True
    if isinstance(value, str):
        return value.strip().lower() in {"true", "yes", "1"}
    return bool(value) if isinstance(value, (int, float)) and not isinstance(value, bool) else False


def _explicit_false(value: Any) -> bool:
    if value is False:
        return True
    if isinstance(value, str):
        return value.strip().lower() in {"false", "no", "0"}
    return False


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


def _find(mapping: Mapping[str, Any], keys: Iterable[str], default: Any = None) -> Any:
    for key in keys:
        if key in mapping:
            return mapping[key]
    return default


def _contains_key(value: Any, keys: set[str]) -> bool:
    if isinstance(value, Mapping):
        for key, nested in value.items():
            if str(key) in keys:
                return True
            if _contains_key(nested, keys):
                return True
    elif isinstance(value, (list, tuple)):
        return any(_contains_key(item, keys) for item in value)
    return False


def _contains_truthy_key(value: Any, keys: Iterable[str]) -> bool:
    key_set = set(keys)
    if isinstance(value, Mapping):
        for key, nested in value.items():
            if str(key) in key_set and _truthy(nested):
                return True
            if _contains_truthy_key(nested, key_set):
                return True
    elif isinstance(value, (list, tuple)):
        return any(_contains_truthy_key(item, key_set) for item in value)
    return False


def _sanitize(value: Any) -> Any:
    if isinstance(value, Mapping):
        sanitized: dict[str, Any] = {}
        for key, nested in value.items():
            text_key = str(key)
            if text_key in FORBIDDEN_FULL_BODY_KEYS:
                sanitized[text_key] = {
                    "omitted": True,
                    "reason": "raw_full_prior_artifact_body_not_returned",
                }
            elif text_key in FORBIDDEN_RAW_OUTPUT_KEYS:
                sanitized[text_key] = {
                    "omitted": True,
                    "reason": "raw_output_body_not_returned",
                }
            else:
                sanitized[text_key] = _sanitize(nested)
        return sanitized
    if isinstance(value, list):
        return [_sanitize(item) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item) for item in value]
    return _copy(value)


def _scope_values(scope: Any) -> list[str]:
    if isinstance(scope, str):
        return [scope]
    if isinstance(scope, Mapping):
        values: list[str] = []
        for key, value in scope.items():
            if isinstance(value, (list, tuple, set)):
                values.extend(str(item) for item in value)
            elif _truthy(value):
                values.append(str(key))
        return values
    if isinstance(scope, (list, tuple, set)):
        return [str(item) for item in scope]
    return []


def _default_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _declared_non_claims(request: Mapping[str, Any]) -> dict[str, Any]:
    declared = _mapping(request.get("declared_non_claims"))
    return {key: declared.get(key) for key in REQUIRED_FALSE_NON_CLAIMS}


def _outcome(basis: Mapping[str, Any]) -> Any:
    return _find(
        basis,
        (
            "outcome",
            "result_outcome",
            "selected_outcome",
            "portable_source_body_verification_outcome",
        ),
    )


def _failed_count(basis: Mapping[str, Any]) -> int | None:
    value = _find(
        basis,
        (
            "failed_check_count",
            "failed_checks",
            "selected_failed_check_count",
            "portable_source_body_verification_failed_check_count",
        ),
    )
    if isinstance(value, list):
        return len(value)
    return _to_int(value)


def _passed_count(basis: Mapping[str, Any]) -> int | None:
    value = _find(basis, ("passed_check_count", "passed_checks", "selected_passed_check_count"))
    if isinstance(value, list):
        return len(value)
    return _to_int(value)


def _version(basis: Mapping[str, Any]) -> Any:
    return _find(basis, ("result_version", "version", "selected_version"))


def _basis(request: Mapping[str, Any], key: str) -> dict[str, Any]:
    value = request.get(key)
    if isinstance(value, Mapping):
        return _copy(dict(value))
    return {}


def _basis_declared(request: Mapping[str, Any], key: str) -> bool:
    return isinstance(request.get(key), Mapping) and bool(request.get(key))


def _posture_declared(request: Mapping[str, Any], key: str) -> bool:
    value = request.get(key)
    if not isinstance(value, Mapping) or not value:
        return False
    declared = _find(value, ("declared", "posture_declared", key, "basis_declared"))
    return _truthy(declared) or bool(value)


def _reference_shaped(value: Mapping[str, Any]) -> bool:
    if _contains_key(value, FORBIDDEN_FULL_BODY_KEYS) or _contains_key(value, FORBIDDEN_RAW_OUTPUT_KEYS):
        return False
    return any(
        _truthy(value.get(key))
        for key in (
            "reference_shaped",
            "reference_shaped_basis",
            "basis_remains_reference_shaped",
            "basis_reference_shape_preserved",
            "basis_remains_basis_only",
            "selected_basis_is_reference_shaped",
        )
    ) or bool(value)


def _flag_true(request: Mapping[str, Any], keys: Iterable[str]) -> bool:
    key_tuple = tuple(keys)
    if _contains_truthy_key(request, key_tuple):
        return True
    declared = _mapping(request.get("declared_non_claims"))
    return _contains_truthy_key(declared, key_tuple)


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


def _check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    block_code: str | None,
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
    value = request.get("requested_output_capture_boundary_outcome")
    if value in OUTCOME_FAMILY:
        return str(value)
    return None


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
        (
            "process_output_captured",
            "process_output_capture_created",
            "process_output_already_captured",
        ),
    )
    raw_output_body_captured = _created_flag(
        request,
        basis,
        ("selected_command_output_raw_output_body_captured",),
        (
            "raw_output_body_captured",
            "raw_command_output_body_captured",
            "raw_output_body_capture_created",
        ),
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
        "selected_post_invocation_command_execution_basis": "selected_post_invocation_command_execution_result_outcome",
        "selected_command_invocation_basis": "selected_command_invocation_result_outcome",
        "selected_command_execution_review_basis": "selected_command_execution_review_result_outcome",
        "selected_request_consumption_basis": "selected_request_consumption_result_outcome",
        "selected_v2_admitted_request_basis": "selected_v2_admitted_request_outcome",
    }
    failed_shortcuts = {
        "selected_post_invocation_command_execution_basis": "selected_post_invocation_command_execution_failed_check_count",
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
        or _truthy(basis.get("execution_trace_audit_only_preserved")),
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
    return {
        "basis": _sanitize(_basis(request, key)),
        "declared": _basis_declared(request, key),
        "readability_basis_only": True,
        "terminal_summary_does_not_capture_stdout": True,
        "terminal_summary_does_not_capture_stderr": True,
        "terminal_summary_does_not_capture_process_output": True,
        "terminal_summary_does_not_capture_raw_output_body": True,
        "does_not_create_output_capture": True,
        "does_not_create_output_report_artifact": True,
        "does_not_create_command_result": True,
        "does_not_create_command_success": True,
    }


def _posture_section(request: Mapping[str, Any], key: str) -> dict[str, Any]:
    posture = _basis(request, key)
    return {
        "basis": _sanitize(posture),
        "declared": _posture_declared(request, key),
        "stdout_captured": _truthy(posture.get("stdout_captured")),
        "stderr_captured": _truthy(posture.get("stderr_captured")),
        "process_output_captured": _truthy(posture.get("process_output_captured")),
        "raw_output_body_captured": _truthy(posture.get("raw_output_body_captured")),
        "stdout_not_captured": not _truthy(posture.get("stdout_captured")),
        "stderr_not_captured": not _truthy(posture.get("stderr_captured")),
        "process_output_not_captured": not _truthy(posture.get("process_output_captured")),
        "raw_output_body_not_captured": not _truthy(posture.get("raw_output_body_captured")),
        "output_capture_not_created": not _truthy(posture.get("output_capture_created")),
        "command_output_report_artifact_not_created": not (
            _truthy(posture.get("command_output_report_artifact_created"))
            or _truthy(posture.get("output_report_artifact_created"))
        ),
        "command_result_not_created": not _truthy(posture.get("command_result_created")),
        "command_success_not_created": not _truthy(posture.get("command_success_created")),
        "output_capture_boundary_not_stdout_capture": not _truthy(
            posture.get("output_capture_boundary_treated_as_stdout_capture")
        ),
        "output_capture_boundary_not_stderr_capture": not _truthy(
            posture.get("output_capture_boundary_treated_as_stderr_capture")
        ),
        "output_capture_boundary_not_process_output_capture": not _truthy(
            posture.get("output_capture_boundary_treated_as_process_output_capture")
        ),
        "output_capture_boundary_not_raw_output_body_capture": not _truthy(
            posture.get("output_capture_boundary_treated_as_raw_output_body_capture")
        ),
        "output_capture_boundary_not_output_capture": not _truthy(
            posture.get("output_capture_boundary_treated_as_output_capture")
        ),
        "output_capture_boundary_not_output_report_artifact": not _truthy(
            posture.get("output_capture_boundary_treated_as_output_report_artifact")
        ),
        "output_capture_boundary_not_result": not _truthy(
            posture.get("output_capture_boundary_treated_as_result")
        ),
        "output_capture_boundary_not_success": not _truthy(
            posture.get("output_capture_boundary_treated_as_success")
        ),
        "command_output_not_output_capture": not _truthy(
            posture.get("command_output_treated_as_output_capture")
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
        "success_not_currentness": not _truthy(posture.get("command_success_created_currentness")),
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


def _build_checks(
    request: Mapping[str, Any],
    forced_block_code: str | None = None,
    forced_block_reason: str | None = None,
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    command_output = _selected_command_output_basis(request)
    post_invocation = _basis(request, "selected_post_invocation_command_execution_basis")
    command_invocation = _basis(request, "selected_command_invocation_basis")
    command_execution_review = _basis(request, "selected_command_execution_review_basis")
    request_consumption = _basis(request, "selected_request_consumption_basis")
    consumed_request = _basis(request, "selected_consumed_request_basis")
    v2 = _basis(request, "selected_v2_admitted_request_basis")
    v1 = _basis(request, "selected_v1_predecessor_failure_basis")
    older_lineage = _basis(request, "selected_older_command_execution_boundary_lineage_basis")
    scope_values = _scope_values(request.get("output_capture_boundary_scope"))
    declared_non_claims = _declared_non_claims(request)

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

    question = request.get("output_capture_boundary_question")
    intent = request.get("output_capture_boundary_intent")
    checks.extend(
        [
            _check(
                "output capture boundary question declared",
                _present(question),
                "declared output capture boundary question",
                question,
                "OUTPUT_CAPTURE_BOUNDARY_QUESTION_UNDECLARED",
            ),
            _check(
                "output capture boundary intent supported",
                intent in SUPPORTED_INTENTS,
                SUPPORTED_INTENTS,
                intent,
                "OUTPUT_CAPTURE_BOUNDARY_INTENT_UNSUPPORTED",
            ),
            _check(
                "command output terminal summary basis declared",
                _basis_declared(request, "selected_command_output_terminal_summary_basis"),
                "selected command output terminal summary basis declared",
                request.get("selected_command_output_terminal_summary_basis"),
                "COMMAND_OUTPUT_BASIS_MISSING",
            ),
            _check(
                "command output live artifact basis declared",
                _basis_declared(request, "selected_command_output_basis"),
                "selected command output basis declared",
                request.get("selected_command_output_basis"),
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
                "stdout not captured",
                command_output.get("stdout_captured"),
                "COMMAND_OUTPUT_ALREADY_CAPTURED_STDOUT",
            ),
            _check(
                "command output stderr not captured",
                not _truthy(command_output.get("stderr_captured")),
                "stderr not captured",
                command_output.get("stderr_captured"),
                "COMMAND_OUTPUT_ALREADY_CAPTURED_STDERR",
            ),
            _check(
                "command output process output not captured",
                not _truthy(command_output.get("process_output_captured")),
                "process output not captured",
                command_output.get("process_output_captured"),
                "COMMAND_OUTPUT_ALREADY_CAPTURED_PROCESS_OUTPUT",
            ),
            _check(
                "command output raw output body not captured",
                not _truthy(command_output.get("raw_output_body_captured")),
                "raw output body not captured",
                command_output.get("raw_output_body_captured"),
                "COMMAND_OUTPUT_ALREADY_CAPTURED_RAW_OUTPUT_BODY",
            ),
            _check(
                "command output output capture not created",
                not _truthy(command_output.get("output_capture_created")),
                "output capture not created by command output",
                command_output.get("output_capture_created"),
                "COMMAND_OUTPUT_ALREADY_CREATED_OUTPUT_CAPTURE",
            ),
            _check(
                "command output output report artifact not created",
                not _truthy(command_output.get("command_output_report_artifact_created")),
                "command output/report artifact not created by command output",
                command_output.get("command_output_report_artifact_created"),
                "COMMAND_OUTPUT_ALREADY_CREATED_OUTPUT_REPORT_ARTIFACT",
            ),
            _check(
                "command output result not created",
                not _truthy(command_output.get("command_result_created")),
                "command result not created by command output",
                command_output.get("command_result_created"),
                "COMMAND_OUTPUT_ALREADY_CREATED_RESULT",
            ),
            _check(
                "command output success not created",
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
                "command output containment basis declared",
                _basis_declared(request, "selected_command_output_containment_basis"),
                "selected command output containment basis declared",
                request.get("selected_command_output_containment_basis"),
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
                "post-invocation command execution recorded",
                (
                    request.get("selected_post_invocation_command_execution_result_outcome")
                    or _outcome(post_invocation)
                )
                == POST_INVOCATION_COMMAND_EXECUTION_OUTCOME,
                POST_INVOCATION_COMMAND_EXECUTION_OUTCOME,
                request.get("selected_post_invocation_command_execution_result_outcome")
                or _outcome(post_invocation),
                "POST_INVOCATION_COMMAND_EXECUTION_NOT_RECORDED",
            ),
            _check(
                "post-invocation command execution failed check count zero",
                _to_int(
                    request.get("selected_post_invocation_command_execution_failed_check_count")
                    if "selected_post_invocation_command_execution_failed_check_count" in request
                    else _failed_count(post_invocation)
                )
                == 0,
                0,
                request.get("selected_post_invocation_command_execution_failed_check_count")
                if "selected_post_invocation_command_execution_failed_check_count" in request
                else _failed_count(post_invocation),
                "POST_INVOCATION_COMMAND_EXECUTION_FAILED_CHECKS_PRESENT",
            ),
            _check(
                "post-invocation command execution event recorded",
                _truthy(post_invocation.get("one_bounded_command_execution_event_recorded"))
                or _truthy(post_invocation.get("bounded_command_execution_event_recorded"))
                or _truthy(post_invocation.get("recorded_command_execution_event_preserved")),
                "one bounded command execution event recorded",
                post_invocation,
                "POST_INVOCATION_COMMAND_EXECUTION_NOT_RECORDED",
            ),
            _check(
                "post-invocation command execution trace audit-only",
                _truthy(request.get("selected_post_invocation_command_execution_trace_audit_only"))
                or _truthy(post_invocation.get("execution_trace_audit_only"))
                or _truthy(post_invocation.get("execution_trace_audit_only_preserved")),
                "execution trace audit-only",
                request.get("selected_post_invocation_command_execution_trace_audit_only")
                or post_invocation.get("execution_trace_audit_only")
                or post_invocation.get("execution_trace_audit_only_preserved"),
                "POST_INVOCATION_COMMAND_EXECUTION_TRACE_NOT_AUDIT_ONLY",
            ),
            _check(
                "command invocation basis declared",
                _basis_declared(request, "selected_command_invocation_basis"),
                "selected command invocation basis declared",
                request.get("selected_command_invocation_basis"),
                "COMMAND_OUTPUT_BASIS_MISSING",
            ),
            _check(
                "command invocation outcome recorded",
                _outcome(command_invocation) in (COMMAND_INVOCATION_OUTCOME, None)
                and bool(command_invocation),
                COMMAND_INVOCATION_OUTCOME,
                _outcome(command_invocation),
                "COMMAND_OUTPUT_BASIS_MISSING",
            ),
            _check(
                "command execution review basis declared",
                _basis_declared(request, "selected_command_execution_review_basis"),
                "selected command execution review basis declared",
                request.get("selected_command_execution_review_basis"),
                "COMMAND_OUTPUT_BASIS_MISSING",
            ),
            _check(
                "command execution review outcome recorded",
                _outcome(command_execution_review) in (COMMAND_EXECUTION_REVIEW_OUTCOME, None)
                and bool(command_execution_review),
                COMMAND_EXECUTION_REVIEW_OUTCOME,
                _outcome(command_execution_review),
                "COMMAND_OUTPUT_BASIS_MISSING",
            ),
            _check(
                "request consumption basis declared",
                _basis_declared(request, "selected_request_consumption_basis"),
                "selected request-consumption basis declared",
                request.get("selected_request_consumption_basis"),
                "COMMAND_OUTPUT_BASIS_MISSING",
            ),
            _check(
                "request consumption outcome recorded",
                _outcome(request_consumption) in (REQUEST_CONSUMPTION_OUTCOME, None)
                and bool(request_consumption),
                REQUEST_CONSUMPTION_OUTCOME,
                _outcome(request_consumption),
                "COMMAND_OUTPUT_BASIS_MISSING",
            ),
            _check(
                "consumed request basis declared",
                _basis_declared(request, "selected_consumed_request_basis"),
                "selected consumed request basis declared",
                request.get("selected_consumed_request_basis"),
                "CONSUMED_REQUEST_REOPENED",
            ),
            _check(
                "consumed request token remains closed",
                not (
                    _truthy(consumed_request.get("consumed_request_reopened"))
                    or _truthy(consumed_request.get("request_reopened"))
                    or _flag_true(request, ("consumed_request_reopened",))
                ),
                "consumed request token closed",
                consumed_request,
                "CONSUMED_REQUEST_REOPENED",
            ),
            _check(
                "v2 admitted request basis declared",
                _basis_declared(request, "selected_v2_admitted_request_basis"),
                "selected v2 admitted request basis declared",
                request.get("selected_v2_admitted_request_basis"),
                "V2_ADMITTED_REQUEST_BASIS_MISSING",
            ),
            _check(
                "v2 admitted request outcome recorded",
                (request.get("selected_v2_admitted_request_outcome") or _outcome(v2))
                in (V2_ADMITTED_REQUEST_OUTCOME, None)
                and bool(v2),
                V2_ADMITTED_REQUEST_OUTCOME,
                request.get("selected_v2_admitted_request_outcome") or _outcome(v2),
                "V2_ADMITTED_REQUEST_BASIS_MISSING",
            ),
            _check(
                "v2 admitted request failed check count zero",
                _to_int(
                    request.get("selected_v2_failed_check_count")
                    if "selected_v2_failed_check_count" in request
                    else _failed_count(v2)
                )
                in (0, None),
                0,
                request.get("selected_v2_failed_check_count")
                if "selected_v2_failed_check_count" in request
                else _failed_count(v2),
                "V2_ADMITTED_REQUEST_FAILED_CHECKS_PRESENT",
            ),
            _check(
                "v2 admitted request version preserved",
                (request.get("selected_v2_admitted_request_version") or _version(v2))
                in (V2_ADMITTED_REQUEST_VERSION, None),
                V2_ADMITTED_REQUEST_VERSION,
                request.get("selected_v2_admitted_request_version") or _version(v2),
                "V2_ADMITTED_REQUEST_BASIS_MISSING",
            ),
            _check(
                "v1 predecessor/failure basis declared",
                _basis_declared(request, "selected_v1_predecessor_failure_basis"),
                "selected v1 predecessor/failure basis declared",
                request.get("selected_v1_predecessor_failure_basis"),
                "V1_PREDECESSOR_FAILURE_BASIS_MISSING",
            ),
            _check(
                "v2 does not repair v1",
                not (
                    _truthy(v2.get("v2_treated_as_repairing_v1"))
                    or _truthy(v2.get("v2_repairs_v1"))
                    or _flag_true(request, ("v1_repaired",))
                ),
                "v2 successor does not repair v1",
                v2,
                "V2_TREATED_AS_REPAIRING_V1",
            ),
            _check(
                "v1 failure remains visible",
                not (_truthy(v1.get("v1_hidden")) or _flag_true(request, ("v1_hidden",))),
                "v1 failure visible",
                v1,
                "V1_FAILURE_HIDDEN",
            ),
            _check(
                "v1 not claimed passed",
                not (
                    _truthy(v1.get("v1_claimed_passed"))
                    or _flag_true(request, ("v1_claimed_passed",))
                ),
                "v1 not claimed passed",
                v1,
                "V1_CLAIMED_PASSED",
            ),
            _check(
                "older command execution boundary lineage basis prior scaffolding only",
                bool(older_lineage) and not _lineage_as_current_execution(older_lineage),
                "older lineage not current execution",
                older_lineage,
                "OLDER_COMMAND_EXECUTION_BOUNDARY_LINEAGE_TREATED_AS_CURRENT_EXECUTION",
            ),
        ]
    )

    prior_basis_checks = (
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
        (
            "evidence manifest basis declared",
            "selected_evidence_manifest_basis",
            "EVIDENCE_MANIFEST_BASIS_MISSING",
        ),
        (
            "portable verification basis declared",
            "selected_portable_verification_basis",
            "PORTABLE_VERIFICATION_BASIS_MISSING",
        ),
    )
    for name, key, code in prior_basis_checks:
        checks.append(_check(name, _basis_declared(request, key), "basis declared", request.get(key), code))

    posture_checks = (
        (
            "output capture boundary only posture declared",
            "output_capture_boundary_only_posture",
            "OUTPUT_CAPTURE_BOUNDARY_ONLY_POSTURE_MISSING",
        ),
        (
            "one future output capture step posture declared",
            "one_future_output_capture_step_posture",
            "ONE_FUTURE_OUTPUT_CAPTURE_STEP_POSTURE_MISSING",
        ),
        (
            "command output basis preserved posture declared",
            "command_output_basis_preserved_posture",
            "COMMAND_OUTPUT_BASIS_PRESERVED_POSTURE_MISSING",
        ),
        (
            "bounded command output event preserved posture declared",
            "bounded_command_output_event_preserved_posture",
            "BOUNDED_COMMAND_OUTPUT_EVENT_PRESERVED_POSTURE_MISSING",
        ),
        (
            "command output boundary basis preserved posture declared",
            "command_output_boundary_basis_preserved_posture",
            "COMMAND_OUTPUT_BOUNDARY_BASIS_PRESERVED_POSTURE_MISSING",
        ),
        ("execution trace audit-only posture declared", "execution_trace_audit_only_posture", "EXECUTION_TRACE_AUDIT_ONLY_POSTURE_MISSING"),
        ("no stdout capture posture declared", "no_stdout_capture_posture", "NO_STDOUT_CAPTURE_POSTURE_MISSING"),
        ("no stderr capture posture declared", "no_stderr_capture_posture", "NO_STDERR_CAPTURE_POSTURE_MISSING"),
        (
            "no process output capture posture declared",
            "no_process_output_capture_posture",
            "NO_PROCESS_OUTPUT_CAPTURE_POSTURE_MISSING",
        ),
        (
            "no raw output body capture posture declared",
            "no_raw_output_body_capture_posture",
            "NO_RAW_OUTPUT_BODY_CAPTURE_POSTURE_MISSING",
        ),
        ("no output capture posture declared", "no_output_capture_posture", "NO_OUTPUT_CAPTURE_POSTURE_MISSING"),
        ("no output report artifact posture declared", "no_output_report_artifact_posture", "NO_OUTPUT_REPORT_ARTIFACT_POSTURE_MISSING"),
        ("no command result posture declared", "no_command_result_posture", "NO_COMMAND_RESULT_POSTURE_MISSING"),
        ("no command success posture declared", "no_command_success_posture", "NO_COMMAND_SUCCESS_POSTURE_MISSING"),
        ("no output as source posture declared", "no_output_as_source_posture", "NO_OUTPUT_AS_SOURCE_POSTURE_MISSING"),
        ("no result as authority posture declared", "no_result_as_authority_posture", "NO_RESULT_AS_AUTHORITY_POSTURE_MISSING"),
        ("no success as currentness posture declared", "no_success_as_currentness_posture", "NO_SUCCESS_AS_CURRENTNESS_POSTURE_MISSING"),
        ("no final completion posture declared", "no_final_completion_posture", "NO_FINAL_COMPLETION_POSTURE_MISSING"),
        (
            "authorization token reuse blocked posture declared",
            "authorization_token_reuse_blocked_posture",
            "AUTHORIZATION_TOKEN_REUSED",
        ),
        ("consumed token closed posture declared", "consumed_token_closed_posture", "CONSUMED_REQUEST_REOPENED"),
        ("no reopen consumed request posture declared", "no_reopen_consumed_request_posture", "CONSUMED_REQUEST_REOPENED"),
        ("returned result containment posture declared", "returned_result_containment_posture", "NON_CLAIM_MISSING_OR_FLIPPED"),
    )
    for name, key, code in posture_checks:
        checks.append(_check(name, _posture_declared(request, key), "posture declared", request.get(key), code))

    checks.append(
        _check(
            "reference-shaped input posture declared",
            _posture_declared(request, "reference_shaped_input_posture"),
            "reference-shaped input posture declared",
            request.get("reference_shaped_input_posture"),
            "REFERENCE_SHAPED_INPUT_POSTURE_MISSING",
        )
    )

    checks.append(
        _check(
            "output capture boundary scope supported",
            bool(scope_values)
            and all(value in SUPPORTED_OUTPUT_CAPTURE_BOUNDARY_SCOPE_SET for value in scope_values),
            SUPPORTED_OUTPUT_CAPTURE_BOUNDARY_SCOPE,
            scope_values,
            "UNSUPPORTED_OUTPUT_CAPTURE_BOUNDARY_SCOPE",
        )
    )

    collapse_specs = (
        (
            ("output_capture_boundary_treated_as_stdout_capture",),
            "OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_STDOUT_CAPTURE",
            "output capture boundary not stdout capture",
        ),
        (
            ("output_capture_boundary_treated_as_stderr_capture",),
            "OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_STDERR_CAPTURE",
            "output capture boundary not stderr capture",
        ),
        (
            ("output_capture_boundary_treated_as_process_output_capture",),
            "OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_PROCESS_OUTPUT_CAPTURE",
            "output capture boundary not process-output capture",
        ),
        (
            ("output_capture_boundary_treated_as_raw_output_body_capture",),
            "OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_RAW_OUTPUT_BODY_CAPTURE",
            "output capture boundary not raw-output-body capture",
        ),
        (
            ("output_capture_boundary_treated_as_output_capture",),
            "OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_OUTPUT_CAPTURE",
            "output capture boundary not output capture",
        ),
        (
            ("output_capture_boundary_treated_as_output_report_artifact",),
            "OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_OUTPUT_REPORT_ARTIFACT",
            "output capture boundary not output/report artifact",
        ),
        (
            ("output_capture_boundary_treated_as_result",),
            "OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_RESULT",
            "output capture boundary not result",
        ),
        (
            ("output_capture_boundary_treated_as_success",),
            "OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_SUCCESS",
            "output capture boundary not success",
        ),
        (("stdout_captured",), "STDOUT_CAPTURED", "stdout not captured"),
        (("stderr_captured",), "STDERR_CAPTURED", "stderr not captured"),
        (("process_output_captured",), "PROCESS_OUTPUT_CAPTURED", "process output not captured"),
        (("raw_output_body_captured",), "RAW_OUTPUT_BODY_CAPTURED", "raw output body not captured"),
        (
            ("command_output_treated_as_output_capture",),
            "COMMAND_OUTPUT_TREATED_AS_OUTPUT_CAPTURE",
            "command output not output capture",
        ),
        (
            ("command_output_treated_as_output_report_artifact",),
            "COMMAND_OUTPUT_TREATED_AS_OUTPUT_REPORT_ARTIFACT",
            "command output not output/report artifact",
        ),
        (("command_output_treated_as_result",), "COMMAND_OUTPUT_TREATED_AS_RESULT", "command output not result"),
        (("command_output_treated_as_success",), "COMMAND_OUTPUT_TREATED_AS_SUCCESS", "command output not success"),
        (("command_output_treated_as_source",), "COMMAND_OUTPUT_TREATED_AS_SOURCE", "command output not source"),
        (("command_output_treated_as_authority",), "COMMAND_OUTPUT_TREATED_AS_AUTHORITY", "command output not authority"),
        (
            ("command_output_treated_as_currentness",),
            "COMMAND_OUTPUT_TREATED_AS_CURRENTNESS",
            "command output not currentness",
        ),
        (
            ("command_output_treated_as_final_completion",),
            "COMMAND_OUTPUT_TREATED_AS_FINAL_COMPLETION",
            "command output not final completion",
        ),
        (("output_capture_created",), "OUTPUT_CAPTURE_CREATED", "output capture not created"),
        (
            ("command_output_report_artifact_created", "output_report_artifact_created"),
            "COMMAND_OUTPUT_REPORT_ARTIFACT_CREATED",
            "command output/report artifact not created",
        ),
        (("command_result_created",), "COMMAND_RESULT_CREATED", "command result not created"),
        (("command_success_created",), "COMMAND_SUCCESS_CREATED", "command success not created"),
        (
            ("execution_trace_treated_as_output_capture",),
            "EXECUTION_TRACE_TREATED_AS_OUTPUT_CAPTURE",
            "execution trace not output capture",
        ),
        (("execution_trace_treated_as_result",), "EXECUTION_TRACE_TREATED_AS_RESULT", "execution trace not result"),
        (("execution_trace_treated_as_success",), "EXECUTION_TRACE_TREATED_AS_SUCCESS", "execution trace not success"),
        (("execution_trace_treated_as_source",), "EXECUTION_TRACE_TREATED_AS_SOURCE", "execution trace not source"),
        (("execution_trace_treated_as_authority",), "EXECUTION_TRACE_TREATED_AS_AUTHORITY", "execution trace not authority"),
        (
            ("command_result_became_authority", "command_result_treated_as_authority"),
            "COMMAND_RESULT_TREATED_AS_AUTHORITY",
            "command result not authority",
        ),
        (
            ("command_success_created_currentness", "command_success_treated_as_currentness"),
            "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS",
            "command success not currentness",
        ),
        (
            ("command_success_claimed_final_completion", "command_success_treated_as_final_completion"),
            "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION",
            "command success not final completion",
        ),
        (("consumed_request_reopened",), "CONSUMED_REQUEST_REOPENED", "consumed request not reopened"),
        (("authorization_token_reused",), "AUTHORIZATION_TOKEN_REUSED", "authorization token not reused"),
        (("prior_artifacts_mutated", "artifacts_mutated"), "ARTIFACTS_MUTATED", "artifacts not mutated"),
        (("deployment_created",), "DEPLOYMENT_CREATED", "deployment not created"),
        (("runtime_hosting_created",), "RUNTIME_HOSTING_CREATED", "runtime hosting not created"),
        (("public_release_created",), "PUBLIC_RELEASE_CREATED", "public release not created"),
        (("operation_permission_created", "operation_created"), "OPERATION_CREATED", "operation not created"),
        (("public_launch_readiness_created", "public_readiness_created"), "PUBLIC_READINESS_CREATED", "public readiness not created"),
        (("final_completion_claimed",), "FINAL_COMPLETION_CLAIMED", "final completion not claimed"),
        (("continuation_authorized",), "CONTINUATION_AUTHORIZED", "continuation not authorized"),
        (("reusable_permission_created",), "REUSABLE_PERMISSION_CREATED", "reusable permission not created"),
        (
            ("derivative_reception_authorized",),
            "DERIVATIVE_RECEPTION_AUTHORIZED",
            "derivative reception not authorized",
        ),
        (("vessel_relation_authorized",), "VESSEL_RELATION_AUTHORIZED", "vessel relation not authorized"),
        (
            ("another_reception_request_authorized",),
            "ANOTHER_RECEPTION_REQUEST_AUTHORIZED",
            "another reception request not authorized",
        ),
        (("follow_on_work_authorized",), "FOLLOW_ON_WORK_AUTHORIZED", "follow-on work not authorized"),
        (
            ("mutation_performed", "replay_performed", "merge_performed"),
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
            "mutation/replay/merge not performed",
        ),
    )
    for keys, code, expected in collapse_specs:
        checks.append(
            _check(
                expected,
                not _flag_true(request, keys),
                expected,
                {key: _flag_true(request, (key,)) for key in keys},
                code,
            )
        )

    checks.extend(
        [
            _check(
                "raw stdout/stderr/process/raw output body not included",
                not _contains_key(request, FORBIDDEN_RAW_OUTPUT_KEYS),
                "no raw output body fields",
                "raw output field present"
                if _contains_key(request, FORBIDDEN_RAW_OUTPUT_KEYS)
                else "no raw output field",
                "RAW_OUTPUT_BODY_CAPTURED",
            ),
            _check(
                "raw full prior artifact body not emitted",
                not _contains_key(request, FORBIDDEN_FULL_BODY_KEYS),
                "no raw full prior artifact body",
                "raw prior body field present"
                if _contains_key(request, FORBIDDEN_FULL_BODY_KEYS)
                else "no raw prior body field",
                "FULL_PRIOR_ARTIFACT_BODY_EMITTED",
            ),
            _check(
                "required non-claims explicit and false",
                all(_explicit_false(declared_non_claims.get(key)) for key in REQUIRED_FALSE_NON_CLAIMS),
                {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
                declared_non_claims,
                "NON_CLAIM_MISSING_OR_FLIPPED",
            ),
        ]
    )
    return checks


def _statement(recorded: bool) -> dict[str, Any]:
    statement = {key: bool(recorded) for key in ALLOWED_TRUE_RECORDED_FIELDS}
    statement.update({key: False for key in REQUIRED_FALSE_NON_CLAIMS})
    statement.update(
        {
            "output_report_artifact_created": False,
            "raw_command_output_body_captured": False,
            "command_result_treated_as_authority": False,
            "command_success_treated_as_currentness": False,
            "command_success_treated_as_final_completion": False,
        }
    )
    return statement


def _non_meaning() -> dict[str, bool]:
    return {
        "stdout_captured": False,
        "stderr_captured": False,
        "process_output_captured": False,
        "raw_output_body_captured": False,
        "output_capture_exists": False,
        "command_output_report_artifact_exists": False,
        "command_result_exists": False,
        "command_success_exists": False,
        "boundary_is_stdout_capture": False,
        "boundary_is_stderr_capture": False,
        "boundary_is_process_output_capture": False,
        "boundary_is_raw_output_body_capture": False,
        "boundary_is_output_capture": False,
        "boundary_is_output_report_artifact": False,
        "boundary_is_result": False,
        "boundary_is_success": False,
        "command_output_is_output_capture": False,
        "command_output_is_output_report_artifact": False,
        "command_output_is_result": False,
        "command_output_is_success": False,
        "command_output_is_source": False,
        "command_output_is_authority": False,
        "command_output_is_currentness": False,
        "command_output_is_final_completion": False,
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


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "output capture boundary test",
            "output capture boundary live artifact",
            "output capture step, if separately specified",
            "stdout capture",
            "stderr capture",
            "process-output capture",
            "raw output body capture",
            "output capture",
            "command output/report artifact",
            "command result",
            "command success",
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


def _block_object(blocked: bool, code: str | None, reason: str | None) -> dict[str, Any]:
    return {"blocked": blocked, "block_code": code, "block_reason": reason}


def _result_id(request_id: Any) -> str:
    base = (
        str(request_id).strip()
        if _present(request_id)
        else "undeclared_output_capture_boundary_request"
    )
    return f"{base}__portable_source_body_verification_output_capture_boundary_result"


def _determine_outcome(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    forced_block_code: str | None,
    forced_block_reason: str | None,
) -> tuple[str, dict[str, Any]]:
    intent = request.get("output_capture_boundary_intent")
    requested = _requested_outcome(request)
    failed = [check for check in checks if not check.get("passed")]

    if forced_block_code:
        return OUTCOME_BLOCKED, _block_object(True, forced_block_code, forced_block_reason)
    if intent == INTENT_BLOCK:
        return OUTCOME_BLOCKED, _block_object(
            True,
            "OUTPUT_CAPTURE_BOUNDARY_BLOCKED_BY_REQUEST",
            request.get("block_reason") or "output capture boundary block intent declared",
        )
    if failed:
        first_code = failed[0].get("block_code") or "DECLARED_OUTPUT_CAPTURE_BOUNDARY_REQUEST_MALFORMED"
        severe_codes = {
            "COMMAND_OUTPUT_ALREADY_CAPTURED_STDOUT",
            "COMMAND_OUTPUT_ALREADY_CAPTURED_STDERR",
            "COMMAND_OUTPUT_ALREADY_CAPTURED_PROCESS_OUTPUT",
            "COMMAND_OUTPUT_ALREADY_CAPTURED_RAW_OUTPUT_BODY",
            "COMMAND_OUTPUT_ALREADY_CREATED_OUTPUT_CAPTURE",
            "COMMAND_OUTPUT_ALREADY_CREATED_OUTPUT_REPORT_ARTIFACT",
            "COMMAND_OUTPUT_ALREADY_CREATED_RESULT",
            "COMMAND_OUTPUT_ALREADY_CREATED_SUCCESS",
            "STDOUT_CAPTURED",
            "STDERR_CAPTURED",
            "PROCESS_OUTPUT_CAPTURED",
            "RAW_OUTPUT_BODY_CAPTURED",
            "OUTPUT_CAPTURE_CREATED",
            "COMMAND_OUTPUT_REPORT_ARTIFACT_CREATED",
            "COMMAND_RESULT_CREATED",
            "COMMAND_SUCCESS_CREATED",
            "FULL_PRIOR_ARTIFACT_BODY_EMITTED",
            "ARTIFACTS_MUTATED",
            "FINAL_COMPLETION_CLAIMED",
            "FOLLOW_ON_WORK_AUTHORIZED",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        }
        if requested == OUTCOME_REQUIRES_ADDITIONAL_BASIS and not any(
            check.get("block_code") in severe_codes for check in failed
        ):
            return OUTCOME_REQUIRES_ADDITIONAL_BASIS, _block_object(False, None, None)
        return OUTCOME_BLOCKED, _block_object(
            True,
            str(first_code),
            "output capture boundary review blocked",
        )
    if requested == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS, _block_object(False, None, None)
    if intent == INTENT_DO_NOT_RECORD or requested == OUTCOME_NOT_RECORDED:
        return OUTCOME_NOT_RECORDED, _block_object(False, None, None)
    return OUTCOME_RECORDED, _block_object(False, None, None)


def _base_result(
    request: Mapping[str, Any],
    forced_block_code: str | None = None,
    forced_block_reason: str | None = None,
) -> dict[str, Any]:
    checks = _build_checks(request, forced_block_code, forced_block_reason)
    outcome, block = _determine_outcome(request, checks, forced_block_code, forced_block_reason)
    recorded = outcome == OUTCOME_RECORDED
    request_id = request.get("output_capture_boundary_request_id")
    failed_checks = [check for check in checks if not check.get("passed")]
    passed_checks = [check for check in checks if check.get("passed")]

    result: dict[str, Any] = {
        "portable_source_body_verification_output_capture_boundary_metadata": {
            "portable_source_body_verification_output_capture_boundary_result_id": _result_id(
                request_id
            ),
            "portable_source_body_verification_output_capture_boundary_result_type": RESULT_TYPE,
            "portable_source_body_verification_output_capture_boundary_result_version": RESULT_VERSION,
            "generated_at": _now(),
            "resolver_module": RESOLVER_MODULE,
            "short_resolver_filename": "resolve_portable_source_body_verification_output_capture_boundary.py",
            "full_upstream_lineage_preserved_inside_selected_basis": True,
        },
        "declared_output_capture_boundary_question": {
            "output_capture_boundary_request_id": request_id,
            "question": request.get("output_capture_boundary_question"),
            "core_question": CORE_QUESTION,
            "intent": request.get("output_capture_boundary_intent"),
        },
        "selected_command_output_basis": _selected_command_output_basis(request),
        "selected_command_output_terminal_summary_basis": _terminal_summary_basis(
            request,
            "selected_command_output_terminal_summary_basis",
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
            request,
            "selected_post_invocation_command_execution_terminal_summary_basis",
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
            request,
            "selected_consumed_request_basis",
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
            request,
            "selected_command_report_basis",
            "selected_command_report_path",
        ),
        "selected_command_implementation_boundary_basis": _selected_prior_basis(
            request,
            "selected_command_implementation_boundary_basis",
            "selected_command_implementation_boundary_result_path",
        ),
        "selected_command_boundary_basis": _selected_prior_basis(
            request,
            "selected_command_boundary_basis",
            "selected_command_boundary_result_path",
        ),
        "selected_artifact_emission_containment_basis": _selected_prior_basis(
            request,
            "selected_artifact_emission_containment_basis",
            "selected_artifact_emission_containment_result_path",
        ),
        "selected_evidence_manifest_basis": _selected_prior_basis(
            request,
            "selected_evidence_manifest_basis",
            "selected_evidence_manifest_result_path",
        ),
        "selected_portable_verification_basis": _selected_prior_basis(
            request,
            "selected_portable_verification_basis",
            "selected_portable_verification_result_path",
        ),
    }

    for key in (
        "output_capture_boundary_only_posture",
        "one_future_output_capture_step_posture",
        "command_output_basis_preserved_posture",
        "bounded_command_output_event_preserved_posture",
        "command_output_boundary_basis_preserved_posture",
        "execution_trace_audit_only_posture",
        "no_stdout_capture_posture",
        "no_stderr_capture_posture",
        "no_process_output_capture_posture",
        "no_raw_output_body_capture_posture",
        "no_output_capture_posture",
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
    ):
        result[key] = _posture_section(request, key)

    scope_values = _scope_values(request.get("output_capture_boundary_scope"))
    result.update(
        {
            "output_capture_boundary_scope": {
                "declared_scope": scope_values,
                "supported_scope": list(SUPPORTED_OUTPUT_CAPTURE_BOUNDARY_SCOPE),
                "unsupported_scope_values": [
                    value
                    for value in scope_values
                    if value not in SUPPORTED_OUTPUT_CAPTURE_BOUNDARY_SCOPE_SET
                ],
            },
            "output_capture_boundary_checks": checks,
            "output_capture_boundary_statement": _statement(recorded),
            "output_capture_boundary_non_meaning": _non_meaning(),
            "additional_basis_required": {
                "required": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                "basis": _sanitize(request.get("additional_basis_context", {}))
                if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
                else {},
                "missing_basis_not_scheduled": True,
                "missing_basis_not_authorized": True,
                "missing_basis_not_executed": True,
            },
            "not_recorded_basis": {
                "not_recorded": outcome == OUTCOME_NOT_RECORDED,
                "basis": _sanitize(request.get("not_recorded_basis", {}))
                if outcome == OUTCOME_NOT_RECORDED
                else {},
                "failed_review_reason": request.get("not_recorded_basis")
                or (
                    "recording declined by declared intent"
                    if outcome == OUTCOME_NOT_RECORDED
                    else None
                ),
            },
            "what_remains_open": _what_remains_open(),
            "non_claims": _default_non_claims(),
            "outcome": outcome,
            "block": block,
        }
    )
    result["portable_source_body_verification_output_capture_boundary_summary"] = (
        build_portable_source_body_verification_output_capture_boundary_summary(result)
    )

    expected = set(TOP_LEVEL_SECTIONS)
    actual = set(result)
    if not expected.issubset(actual):
        missing = sorted(expected - actual)
        raise PortableSourceBodyVerificationOutputCaptureBoundaryError(
            f"internal result shape missing sections: {missing}"
        )
    result["portable_source_body_verification_output_capture_boundary_summary"][
        "passed_check_count"
    ] = len(passed_checks)
    result["portable_source_body_verification_output_capture_boundary_summary"][
        "failed_check_count"
    ] = len(failed_checks)
    return result


def resolve_portable_source_body_verification_output_capture_boundary(
    declared_output_capture_boundary_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one bounded output-capture-boundary request mapping."""

    if declared_output_capture_boundary_request is None:
        return _base_result(
            {},
            "OUTPUT_CAPTURE_BOUNDARY_QUESTION_UNDECLARED",
            "declared output capture boundary request missing",
        )
    if not isinstance(declared_output_capture_boundary_request, Mapping):
        return _base_result(
            {},
            "DECLARED_OUTPUT_CAPTURE_BOUNDARY_REQUEST_MALFORMED",
            "declared output capture boundary request must be a mapping",
        )
    request = _copy(dict(declared_output_capture_boundary_request))
    return _base_result(request)


def resolve_portable_source_body_verification_output_capture_boundary_from_path(
    declared_output_capture_boundary_request_path: Path | str,
) -> dict:
    """Resolve one bounded output-capture-boundary request from a JSON object path."""

    path = Path(declared_output_capture_boundary_request_path)
    try:
        raw = path.read_text(encoding="utf-8")
        parsed = json.loads(raw)
    except (OSError, json.JSONDecodeError):
        return _base_result(
            {},
            "DECLARED_OUTPUT_CAPTURE_BOUNDARY_REQUEST_UNREADABLE",
            "declared output capture boundary request path unreadable or malformed",
        )
    if not isinstance(parsed, Mapping):
        return _base_result(
            {},
            "DECLARED_OUTPUT_CAPTURE_BOUNDARY_REQUEST_MALFORMED",
            "declared output capture boundary request JSON must be an object",
        )
    return resolve_portable_source_body_verification_output_capture_boundary(parsed)


def build_portable_source_body_verification_output_capture_boundary_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a compact summary for a bounded output-capture-boundary result."""

    checks = list(result.get("output_capture_boundary_checks", []))
    passed = [check for check in checks if check.get("passed")]
    failed = [check for check in checks if not check.get("passed")]
    metadata = _mapping(result.get("portable_source_body_verification_output_capture_boundary_metadata"))
    question = _mapping(result.get("declared_output_capture_boundary_question"))
    statement = _mapping(result.get("output_capture_boundary_statement"))
    command_output = _mapping(result.get("selected_command_output_basis"))
    post_invocation = _mapping(result.get("selected_post_invocation_command_execution_basis"))
    v2 = _mapping(result.get("selected_v2_admitted_request_basis"))
    non_claims = _mapping(result.get("non_claims"))
    block = _mapping(result.get("block"))

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "request_id": question.get("output_capture_boundary_request_id"),
        "question": question.get("question"),
        "intent": question.get("intent"),
        "result_version": metadata.get(
            "portable_source_body_verification_output_capture_boundary_result_version"
        ),
        "resolver_module": metadata.get("resolver_module"),
        "passed_check_count": len(passed),
        "failed_check_count": len(failed),
        "output_capture_boundary_recorded": statement.get(
            "output_capture_boundary_recorded", False
        ),
        "one_future_output_capture_step_declared": statement.get(
            "one_future_output_capture_step_declared", False
        ),
        "command_output_basis_preserved": statement.get("command_output_basis_preserved", False),
        "bounded_command_output_event_preserved": statement.get(
            "bounded_command_output_event_preserved", False
        ),
        "command_output_boundary_basis_preserved": statement.get(
            "command_output_boundary_basis_preserved", False
        ),
        "command_output_containment_basis_preserved": statement.get(
            "command_output_containment_basis_preserved", False
        ),
        "recorded_command_execution_event_preserved": statement.get(
            "recorded_command_execution_event_preserved", False
        ),
        "execution_trace_audit_only_preserved": statement.get(
            "execution_trace_audit_only_preserved", False
        ),
        "stdout_still_not_captured": statement.get("stdout_still_not_captured", False),
        "stderr_still_not_captured": statement.get("stderr_still_not_captured", False),
        "process_output_still_not_captured": statement.get(
            "process_output_still_not_captured", False
        ),
        "raw_output_body_still_not_captured": statement.get(
            "raw_output_body_still_not_captured", False
        ),
        "output_capture_not_created": statement.get("output_capture_not_created", False),
        "output_report_artifact_not_created": statement.get(
            "command_output_report_artifact_not_created", False
        ),
        "command_result_still_not_created": statement.get(
            "command_result_still_not_created", False
        ),
        "command_success_still_not_created": statement.get(
            "command_success_still_not_created", False
        ),
        "selected_command_output_outcome": command_output.get("outcome"),
        "selected_command_output_failed_check_count": command_output.get("failed_check_count"),
        "selected_post_invocation_execution_outcome": post_invocation.get("outcome"),
        "selected_post_invocation_execution_failed_check_count": post_invocation.get(
            "failed_check_count"
        ),
        "selected_v2_outcome": v2.get("outcome"),
        "selected_v2_version": v2.get("version"),
        "selected_v2_failed_check_count": v2.get("failed_check_count"),
        "output_capture_boundary_not_stdout_stderr_process_raw_capture_report_result_success": all(
            non_claims.get(key) is False
            for key in (
                "output_capture_boundary_treated_as_stdout_capture",
                "output_capture_boundary_treated_as_stderr_capture",
                "output_capture_boundary_treated_as_process_output_capture",
                "output_capture_boundary_treated_as_raw_output_body_capture",
                "output_capture_boundary_treated_as_output_capture",
                "output_capture_boundary_treated_as_output_report_artifact",
                "output_capture_boundary_treated_as_result",
                "output_capture_boundary_treated_as_success",
            )
        ),
        "command_output_not_capture_report_result_success_source_authority_currentness_final_completion": all(
            non_claims.get(key) is False
            for key in (
                "command_output_treated_as_output_capture",
                "command_output_treated_as_output_report_artifact",
                "command_output_treated_as_result",
                "command_output_treated_as_success",
                "command_output_treated_as_source",
                "command_output_treated_as_authority",
                "command_output_treated_as_currentness",
                "command_output_treated_as_final_completion",
            )
        ),
        "execution_trace_not_output_capture_result_success_source_authority": all(
            non_claims.get(key) is False
            for key in (
                "execution_trace_treated_as_output_capture",
                "execution_trace_treated_as_result",
                "execution_trace_treated_as_success",
                "execution_trace_treated_as_source",
                "execution_trace_treated_as_authority",
            )
        ),
        "result_not_authority": non_claims.get("command_result_became_authority") is False,
        "success_not_currentness_final_completion": (
            non_claims.get("command_success_created_currentness") is False
            and non_claims.get("command_success_claimed_final_completion") is False
        ),
        "older_command_execution_boundary_lineage_not_treated_as_current_execution": (
            _mapping(result.get("selected_older_command_execution_boundary_lineage_basis")).get(
                "lineage_basis_not_treated_as_current_execution"
            )
            is True
        ),
        "no_raw_full_prior_artifact_body": non_claims.get("raw_full_prior_artifact_body_returned")
        is False,
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
        "key_non_claims": {key: non_claims.get(key) for key in REQUIRED_FALSE_NON_CLAIMS},
    }


def _safe_filename_part(value: Any) -> str:
    text = (
        str(value).strip()
        if _present(value)
        else "undeclared_output_capture_boundary_request"
    )
    cleaned = []
    for char in text:
        if char.isalnum() or char in {"-", "_", "."}:
            cleaned.append(char)
        else:
            cleaned.append("_")
    return "".join(cleaned).strip("_") or "undeclared_output_capture_boundary_request"


def _unique_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    counter = 1
    while True:
        candidate = parent / f"{stem}_{counter:03d}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def write_portable_source_body_verification_output_capture_boundary_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive output-capture-boundary result JSON without overwriting."""

    result_copy = _copy(dict(result))
    if output_path is None:
        question = _mapping(result_copy.get("declared_output_capture_boundary_question"))
        request_id = _safe_filename_part(question.get("output_capture_boundary_request_id"))
        path = OUTPUT_ROOT / (
            f"{request_id}__portable_source_body_verification_output_capture_boundary_result.json"
        )
    else:
        path = Path(output_path)
        if path.suffix.lower() != ".json":
            question = _mapping(result_copy.get("declared_output_capture_boundary_question"))
            request_id = _safe_filename_part(question.get("output_capture_boundary_request_id"))
            path = path / (
                f"{request_id}__portable_source_body_verification_output_capture_boundary_result.json"
            )
    path.parent.mkdir(parents=True, exist_ok=True)
    final_path = _unique_path(path)
    final_path.write_text(
        json.dumps(result_copy, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return final_path


def _default_reference_basis(name: str) -> dict[str, Any]:
    return {
        "basis_id": name,
        "declared": True,
        "reference_shaped_basis": True,
        "basis_remains_reference_shaped": True,
        "basis_remains_basis_only": True,
        "not_stdout_capture": True,
        "not_stderr_capture": True,
        "not_process_output_capture": True,
        "not_raw_output_body_capture": True,
        "not_output_capture": True,
        "not_command_output_report_artifact": True,
        "not_command_result": True,
        "not_command_success": True,
        "not_source": True,
        "not_authority": True,
        "not_currentness": True,
        "not_final_completion": True,
        "not_follow_on_work": True,
        "full_upstream_lineage_preserved": True,
    }


def _default_posture(name: str) -> dict[str, Any]:
    return {
        "posture_id": name,
        "declared": True,
        "posture_declared": True,
        "stdout_captured": False,
        "stderr_captured": False,
        "process_output_captured": False,
        "raw_output_body_captured": False,
        "output_capture_created": False,
        "command_output_report_artifact_created": False,
        "command_result_created": False,
        "command_success_created": False,
        "output_capture_boundary_treated_as_stdout_capture": False,
        "output_capture_boundary_treated_as_stderr_capture": False,
        "output_capture_boundary_treated_as_process_output_capture": False,
        "output_capture_boundary_treated_as_raw_output_body_capture": False,
        "output_capture_boundary_treated_as_output_capture": False,
        "output_capture_boundary_treated_as_output_report_artifact": False,
        "output_capture_boundary_treated_as_result": False,
        "output_capture_boundary_treated_as_success": False,
        "command_output_treated_as_output_capture": False,
        "command_output_treated_as_output_report_artifact": False,
        "command_output_treated_as_result": False,
        "command_output_treated_as_success": False,
        "command_output_treated_as_source": False,
        "command_output_treated_as_authority": False,
        "command_output_treated_as_currentness": False,
        "command_output_treated_as_final_completion": False,
        "execution_trace_audit_only": True,
        "execution_trace_treated_as_output_capture": False,
        "execution_trace_treated_as_result": False,
        "execution_trace_treated_as_success": False,
        "execution_trace_treated_as_source": False,
        "execution_trace_treated_as_authority": False,
        "command_result_became_authority": False,
        "command_success_created_currentness": False,
        "command_success_claimed_final_completion": False,
        "authorization_token_reuse_blocked": True,
        "authorization_token_reused": False,
        "consumed_request_token_remains_closed": True,
        "consumed_request_reopened": False,
        "returned_result_containment_preserved": True,
        "raw_full_prior_artifact_body_returned": False,
    }


def build_declared_portable_source_body_verification_output_capture_boundary_request(
    output_capture_boundary_request_id: str = (
        "portable_source_body_verification_output_capture_boundary_reference_review_001"
    ),
    output_capture_boundary_question: str = CORE_QUESTION,
    output_capture_boundary_intent: str = INTENT_RECORD,
    **overrides: Any,
) -> dict[str, Any]:
    """Build a bounded declared output-capture-boundary request with false non-claims."""

    request: dict[str, Any] = {
        "output_capture_boundary_request_id": output_capture_boundary_request_id,
        "output_capture_boundary_question": output_capture_boundary_question,
        "output_capture_boundary_intent": output_capture_boundary_intent,
        "selected_command_output_basis": {
            **_default_reference_basis("selected_command_output_basis"),
            "outcome": COMMAND_OUTPUT_OUTCOME,
            "failed_check_count": 0,
            "passed_check_count": 109,
            "command_output_recorded": True,
            "bounded_command_output_event_recorded": True,
            "command_output_event_recorded": True,
            "stdout_captured": False,
            "stderr_captured": False,
            "process_output_captured": False,
            "raw_output_body_captured": False,
            "output_capture_created": False,
            "command_output_report_artifact_created": False,
            "command_result_created": False,
            "command_success_created": False,
            "output_capture_not_created": True,
            "command_output_report_artifact_not_created": True,
            "command_result_still_not_created": True,
            "command_success_still_not_created": True,
            "command_output_is_not_output_capture": True,
            "command_output_is_not_output_report_artifact": True,
            "command_output_is_not_result": True,
            "command_output_is_not_success": True,
            "command_output_is_not_source": True,
            "command_output_is_not_authority": True,
            "command_output_is_not_currentness": True,
            "command_output_is_not_final_completion": True,
        },
        "selected_command_output_terminal_summary_basis": {
            **_default_reference_basis("selected_command_output_terminal_summary_basis"),
            "terminal_summary_declared": True,
            "terminal_summary_remains_readability_basis_only": True,
        },
        "selected_command_output_boundary_basis": {
            **_default_reference_basis("selected_command_output_boundary_basis"),
            "outcome": COMMAND_OUTPUT_BOUNDARY_OUTCOME,
            "failed_check_count": 0,
            "one_future_command_output_step_declared": True,
            "command_output_created": False,
            "output_capture_created": False,
            "command_output_report_artifact_created": False,
            "command_result_created": False,
            "command_success_created": False,
        },
        "selected_command_output_containment_basis": {
            **_default_reference_basis("selected_command_output_containment_basis"),
            "outcome": COMMAND_OUTPUT_CONTAINMENT_OUTCOME,
            "failed_check_count": 0,
            "bounded_command_output_containment_event_recorded": True,
            "command_output_boundary_basis_preserved": True,
        },
        "selected_post_invocation_command_execution_basis": {
            **_default_reference_basis("selected_post_invocation_command_execution_basis"),
            "outcome": POST_INVOCATION_COMMAND_EXECUTION_OUTCOME,
            "failed_check_count": 0,
            "one_bounded_command_execution_event_recorded": True,
            "execution_trace_audit_only": True,
        },
        "selected_post_invocation_command_execution_terminal_summary_basis": {
            **_default_reference_basis(
                "selected_post_invocation_command_execution_terminal_summary_basis"
            ),
            "terminal_summary_declared": True,
            "execution_trace_audit_only_preserved": True,
        },
        "selected_command_invocation_basis": {
            **_default_reference_basis("selected_command_invocation_basis"),
            "outcome": COMMAND_INVOCATION_OUTCOME,
            "failed_check_count": 0,
            "authorization_token_spent_exactly_once": True,
            "authorization_token_reuse_blocked": True,
        },
        "selected_command_execution_review_basis": {
            **_default_reference_basis("selected_command_execution_review_basis"),
            "outcome": COMMAND_EXECUTION_REVIEW_OUTCOME,
            "failed_check_count": 0,
            "review_basis_only": True,
        },
        "selected_request_consumption_basis": {
            **_default_reference_basis("selected_request_consumption_basis"),
            "outcome": REQUEST_CONSUMPTION_OUTCOME,
            "failed_check_count": 0,
            "request_consumed_exactly_once": True,
            "consumption_token_closed": True,
        },
        "selected_consumed_request_basis": {
            **_default_reference_basis("selected_consumed_request_basis"),
            "consumed_request_basis_declared": True,
            "consumed_request_token_remains_closed": True,
            "consumed_request_reopened": False,
        },
        "selected_v2_admitted_request_basis": {
            **_default_reference_basis("selected_v2_admitted_request_basis"),
            "outcome": V2_ADMITTED_REQUEST_OUTCOME,
            "result_version": V2_ADMITTED_REQUEST_VERSION,
            "failed_check_count": 0,
            "successor_metadata_preserved": True,
            "returned_result_containment_preserved": True,
            "v2_treated_as_repairing_v1": False,
        },
        "selected_v1_predecessor_failure_basis": {
            **_default_reference_basis("selected_v1_predecessor_failure_basis"),
            "v1_predecessor_failure_basis_declared": True,
            "v1_remains_visible_predecessor_failure_evidence": True,
            "v1_repaired": False,
            "v1_hidden": False,
            "v1_claimed_passed": False,
        },
        "selected_older_command_execution_boundary_lineage_basis": {
            **_default_reference_basis("selected_older_command_execution_boundary_lineage_basis"),
            "basis_remains_prior_scaffolding_only": True,
            "older_command_execution_boundary_lineage_treated_as_current_execution": False,
        },
        "selected_command_report_basis": _default_reference_basis("selected_command_report_basis"),
        "selected_command_implementation_boundary_basis": _default_reference_basis(
            "selected_command_implementation_boundary_basis"
        ),
        "selected_command_boundary_basis": _default_reference_basis("selected_command_boundary_basis"),
        "selected_artifact_emission_containment_basis": _default_reference_basis(
            "selected_artifact_emission_containment_basis"
        ),
        "selected_evidence_manifest_basis": _default_reference_basis(
            "selected_evidence_manifest_basis"
        ),
        "selected_portable_verification_basis": _default_reference_basis(
            "selected_portable_verification_basis"
        ),
        "output_capture_boundary_scope": list(SUPPORTED_OUTPUT_CAPTURE_BOUNDARY_SCOPE),
        "declared_non_claims": _default_non_claims(),
        "requested_output_capture_boundary_outcome": OUTCOME_RECORDED,
        "reference_shaped_input_posture": {
            "declared": True,
            "reference_shaped_input_posture": True,
            "full_prior_artifact_body_not_emitted": True,
        },
    }
    for key in (
        "output_capture_boundary_only_posture",
        "one_future_output_capture_step_posture",
        "command_output_basis_preserved_posture",
        "bounded_command_output_event_preserved_posture",
        "command_output_boundary_basis_preserved_posture",
        "execution_trace_audit_only_posture",
        "no_stdout_capture_posture",
        "no_stderr_capture_posture",
        "no_process_output_capture_posture",
        "no_raw_output_body_capture_posture",
        "no_output_capture_posture",
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
    ):
        request[key] = _default_posture(key)
    request.update(overrides)
    return request
