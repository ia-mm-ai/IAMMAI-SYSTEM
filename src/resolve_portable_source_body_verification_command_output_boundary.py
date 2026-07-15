"""Portable source-body verification command output boundary resolver.

This module records command output boundary posture only. It is downstream of
recorded command output containment and may preserve one containment basis for
one future command output step. It does not create command output, capture
output, create a command output/report artifact, create command result, or
create command success.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping


class PortableSourceBodyVerificationCommandOutputBoundaryError(Exception):
    """Raised for impossible command output boundary resolver failures."""


RESOLVER_MODULE = "resolve_portable_source_body_verification_command_output_boundary"
RESULT_VERSION = "0.1.0"
RESULT_TYPE = "portable_source_body_verification_command_output_boundary_result"
PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_BOUNDARY_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_command_output_boundary"
)

CORE_COMMAND_OUTPUT_BOUNDARY_QUESTION = (
    "Can the recorded command output containment basis be bounded for one future "
    "command output step without creating command output, output capture, command "
    "output/report artifact, command result, command success, source, authority, "
    "currentness, final completion, continuation, reusable permission, derivative "
    "reception, vessel relation, another reception request, or follow-on work?"
)

INTENT_RECORD = "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_BOUNDARY"
INTENT_BLOCK = "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

OUTCOME_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_BOUNDARY_RECORDED"
OUTCOME_NOT_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_BOUNDARY_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_BOUNDARY_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

COMMAND_OUTPUT_BOUNDARY_OUTCOME = OUTCOME_RECORDED
COMMAND_OUTPUT_CONTAINMENT_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_CONTAINMENT_RECORDED"
)
COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_RECORDED"
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

SUPPORTED_COMMAND_OUTPUT_BOUNDARY_SCOPE = (
    "COMMAND_OUTPUT_BOUNDARY_ONLY",
    "ONE_FUTURE_COMMAND_OUTPUT_STEP_ONLY",
    "COMMAND_OUTPUT_CONTAINMENT_BASIS_PRESERVED",
    "BOUNDED_COMMAND_OUTPUT_CONTAINMENT_EVENT_PRESERVED",
    "RECORDED_COMMAND_EXECUTION_EVENT_PRESERVED",
    "EXECUTION_TRACE_AUDIT_ONLY_PRESERVED",
    "COMMAND_OUTPUT_NOT_CREATED",
    "COMMAND_OUTPUT_CAPTURE_NOT_CREATED",
    "COMMAND_OUTPUT_REPORT_ARTIFACT_NOT_CREATED",
    "COMMAND_RESULT_NOT_CREATED",
    "COMMAND_SUCCESS_NOT_CREATED",
    "OUTPUT_BOUNDARY_IS_NOT_OUTPUT",
    "OUTPUT_BOUNDARY_IS_NOT_OUTPUT_CAPTURE",
    "OUTPUT_BOUNDARY_IS_NOT_OUTPUT_REPORT_ARTIFACT",
    "OUTPUT_BOUNDARY_IS_NOT_RESULT",
    "OUTPUT_BOUNDARY_IS_NOT_SUCCESS",
    "CONTAINMENT_IS_NOT_OUTPUT",
    "CONTAINMENT_IS_NOT_OUTPUT_CAPTURE",
    "CONTAINMENT_IS_NOT_OUTPUT_REPORT_ARTIFACT",
    "CONTAINMENT_IS_NOT_RESULT",
    "CONTAINMENT_IS_NOT_SUCCESS",
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
SUPPORTED_COMMAND_OUTPUT_BOUNDARY_SCOPE_SET = set(SUPPORTED_COMMAND_OUTPUT_BOUNDARY_SCOPE)

REQUIRED_FALSE_NON_CLAIMS = (
    "command_output_created",
    "output_capture_created",
    "command_output_report_artifact_created",
    "command_result_created",
    "command_success_created",
    "boundary_treated_as_output",
    "boundary_treated_as_output_capture",
    "boundary_treated_as_output_report_artifact",
    "boundary_treated_as_result",
    "boundary_treated_as_success",
    "containment_treated_as_output",
    "containment_treated_as_output_capture",
    "containment_treated_as_output_report_artifact",
    "containment_treated_as_result",
    "containment_treated_as_success",
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
    "command_output_boundary_recorded",
    "one_future_command_output_step_declared",
    "command_output_containment_basis_preserved",
    "bounded_output_containment_event_preserved",
    "recorded_command_execution_event_preserved",
    "execution_trace_audit_only_preserved",
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

FORBIDDEN_FULL_BODY_KEYS = {
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


def _find(mapping: Mapping[str, Any], keys: Iterable[str], default: Any = None) -> Any:
    for key in keys:
        if key in mapping:
            return mapping[key]
    return default


def _truthy(value: Any) -> bool:
    if value is True:
        return True
    if isinstance(value, str):
        return value.strip().lower() in {"true", "yes", "1", "recorded", "declared", "preserved"}
    return False


def _explicit_false(value: Any) -> bool:
    if value is False:
        return True
    if isinstance(value, str):
        return value.strip().lower() in {"false", "no", "0"}
    return False


def _contains_forbidden_body(value: Any) -> bool:
    if isinstance(value, Mapping):
        for key, nested in value.items():
            if str(key) in FORBIDDEN_FULL_BODY_KEYS:
                return True
            if _contains_forbidden_body(nested):
                return True
    elif isinstance(value, (list, tuple)):
        return any(_contains_forbidden_body(item) for item in value)
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
            if _truthy(value):
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


def _not_created(mapping: Mapping[str, Any], created_keys: Iterable[str], not_created_keys: Iterable[str]) -> bool:
    for key in created_keys:
        if _truthy(mapping.get(key)):
            return False
    for key in not_created_keys:
        if _truthy(mapping.get(key)):
            return True
    return False


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
    if _contains_forbidden_body(value):
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
        "expected_posture": expected_posture,
        "actual_posture": actual_posture,
        "block_code": code,
        "failure_code": None if passed else (failure_code or block_code),
    }


def _requested_outcome(request: Mapping[str, Any]) -> str | None:
    value = request.get("requested_command_output_boundary_outcome")
    if value in OUTCOME_FAMILY:
        return str(value)
    return None


def _selected_command_output_containment_basis(request: Mapping[str, Any]) -> dict[str, Any]:
    basis = _basis(request, "selected_command_output_containment_basis")
    command_output_created = _truthy(
        request.get("selected_command_output_containment_output_created")
    ) or _truthy(basis.get("command_output_created"))
    output_capture_created = _truthy(
        request.get("selected_command_output_containment_output_capture_created")
    ) or _truthy(basis.get("output_capture_created"))
    output_report_created = _truthy(
        request.get("selected_command_output_containment_output_report_artifact_created")
    ) or _truthy(basis.get("command_output_report_artifact_created")) or _truthy(
        basis.get("output_report_artifact_created")
    )
    command_result_created = _truthy(
        request.get("selected_command_output_containment_result_created")
    ) or _truthy(basis.get("command_result_created"))
    command_success_created = _truthy(
        request.get("selected_command_output_containment_success_created")
    ) or _truthy(basis.get("command_success_created"))
    return {
        "basis": _sanitize(basis),
        "selected_command_output_containment_result_path": request.get(
            "selected_command_output_containment_result_path"
        )
        or basis.get("path")
        or basis.get("artifact_path")
        or basis.get("result_path"),
        "selected_command_output_containment_result_id": request.get(
            "selected_command_output_containment_result_id"
        )
        or basis.get("result_id")
        or basis.get("portable_source_body_verification_command_output_containment_result_id"),
        "outcome": request.get("selected_command_output_containment_result_outcome")
        or _outcome(basis),
        "failed_check_count": _find(
            request,
            ("selected_command_output_containment_failed_check_count",),
            _failed_count(basis),
        ),
        "passed_check_count": _passed_count(basis),
        "bounded_output_containment_event_recorded": _truthy(
            request.get("selected_command_output_containment_event_recorded")
        )
        or _truthy(basis.get("bounded_command_output_containment_event_recorded"))
        or _truthy(basis.get("command_output_containment_recorded"))
        or _truthy(basis.get("one_bounded_command_output_containment_event_recorded")),
        "command_output_boundary_basis_preserved": _truthy(
            request.get("selected_command_output_containment_boundary_basis_preserved")
        )
        or _truthy(basis.get("command_output_boundary_basis_preserved")),
        "command_output_created": command_output_created,
        "output_capture_created": output_capture_created,
        "command_output_report_artifact_created": output_report_created,
        "command_result_created": command_result_created,
        "command_success_created": command_success_created,
        "command_output_not_created": not command_output_created,
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
        "selected_v2_admitted_request_basis": "selected_v2_admitted_request_outcome",
    }
    failed_count_shortcuts = {
        "selected_post_invocation_command_execution_basis": "selected_post_invocation_command_execution_failed_check_count",
        "selected_v2_admitted_request_basis": "selected_v2_failed_check_count",
    }
    outcome_value = request.get(outcome_shortcuts.get(key, "")) or _outcome(basis)
    failed_value = request.get(failed_count_shortcuts.get(key, "")) if failed_count_shortcuts.get(key, "") in request else _failed_count(basis)
    selected: dict[str, Any] = {
        "basis": _sanitize(basis),
        "declared": bool(basis),
        "reference_shaped_basis": _reference_shaped(basis),
        "outcome": outcome_value,
        "failed_check_count": failed_value,
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
        "command_output_not_created": not _truthy(basis.get("command_output_created")),
        "command_result_not_created": not _truthy(basis.get("command_result_created")),
        "command_success_not_created": not _truthy(basis.get("command_success_created")),
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


def _posture_section(request: Mapping[str, Any], key: str) -> dict[str, Any]:
    posture = _basis(request, key)
    return {
        "basis": _sanitize(posture),
        "declared": _posture_declared(request, key),
        "command_output_not_created": _not_created(
            posture,
            ("command_output_created", "output_created"),
            ("command_output_not_created", "command_output_still_not_created"),
        ),
        "output_capture_not_created": _not_created(
            posture,
            ("output_capture_created",),
            ("output_capture_not_created",),
        ),
        "command_output_report_artifact_not_created": _not_created(
            posture,
            ("command_output_report_artifact_created", "output_report_artifact_created"),
            (
                "command_output_report_artifact_not_created",
                "output_report_artifact_not_created",
            ),
        ),
        "command_result_not_created": _not_created(
            posture,
            ("command_result_created",),
            ("command_result_not_created", "command_result_still_not_created"),
        ),
        "command_success_not_created": _not_created(
            posture,
            ("command_success_created",),
            ("command_success_not_created", "command_success_still_not_created"),
        ),
        "boundary_not_output": not _truthy(posture.get("boundary_treated_as_output")),
        "boundary_not_output_capture": not _truthy(posture.get("boundary_treated_as_output_capture")),
        "boundary_not_output_report_artifact": not _truthy(
            posture.get("boundary_treated_as_output_report_artifact")
        ),
        "boundary_not_result": not _truthy(posture.get("boundary_treated_as_result")),
        "boundary_not_success": not _truthy(posture.get("boundary_treated_as_success")),
        "containment_not_output": not _truthy(posture.get("containment_treated_as_output")),
        "containment_not_output_capture": not _truthy(
            posture.get("containment_treated_as_output_capture")
        ),
        "containment_not_output_report_artifact": not _truthy(
            posture.get("containment_treated_as_output_report_artifact")
        ),
        "containment_not_result": not _truthy(posture.get("containment_treated_as_result")),
        "containment_not_success": not _truthy(posture.get("containment_treated_as_success")),
        "execution_trace_audit_only": _truthy(posture.get("execution_trace_audit_only"))
        or _truthy(posture.get("execution_trace_audit_only_preserved")),
        "execution_trace_not_output": not _truthy(posture.get("execution_trace_treated_as_output")),
        "execution_trace_not_result": not _truthy(posture.get("execution_trace_treated_as_result")),
        "execution_trace_not_success": not _truthy(posture.get("execution_trace_treated_as_success")),
        "execution_trace_not_source": not _truthy(posture.get("execution_trace_treated_as_source")),
        "execution_trace_not_authority": not _truthy(
            posture.get("execution_trace_treated_as_authority")
        ),
        "output_not_source": not _truthy(posture.get("command_output_became_source")),
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


def _request_bool(request: Mapping[str, Any], keys: Iterable[str]) -> bool:
    for key in keys:
        if _truthy(request.get(key)):
            return True
    non_claims = _mapping(request.get("declared_non_claims"))
    for key in keys:
        if _truthy(non_claims.get(key)):
            return True
    return False


def _basis_bool(request: Mapping[str, Any], basis_key: str, keys: Iterable[str]) -> bool:
    basis = _basis(request, basis_key)
    return any(_truthy(basis.get(key)) for key in keys)


def _first_true_code(request: Mapping[str, Any], specs: Iterable[tuple[Iterable[str], str]]) -> str | None:
    for keys, code in specs:
        if _request_bool(request, keys):
            return code
    return None


def _build_checks(
    request: Mapping[str, Any],
    forced_block_code: str | None = None,
    forced_block_reason: str | None = None,
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    containment = _selected_command_output_containment_basis(request)
    containment_basis = _basis(request, "selected_command_output_containment_basis")
    post_invocation = _basis(request, "selected_post_invocation_command_execution_basis")
    v2 = _basis(request, "selected_v2_admitted_request_basis")
    v1 = _basis(request, "selected_v1_predecessor_failure_basis")
    older_lineage = _basis(request, "selected_older_command_execution_boundary_lineage_basis")
    consumed_request = _basis(request, "selected_consumed_request_basis")
    scope_values = _scope_values(request.get("command_output_boundary_scope"))
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

    question = request.get("command_output_boundary_question")
    intent = request.get("command_output_boundary_intent")
    checks.extend(
        [
            _check(
                "command output boundary question declared",
                _present(question),
                "declared command output boundary question",
                question,
                "COMMAND_OUTPUT_BOUNDARY_QUESTION_UNDECLARED",
            ),
            _check(
                "command output boundary intent supported",
                intent in SUPPORTED_INTENTS,
                SUPPORTED_INTENTS,
                intent,
                "COMMAND_OUTPUT_BOUNDARY_INTENT_UNSUPPORTED",
            ),
            _check(
                "command output containment terminal summary basis declared",
                _basis_declared(request, "selected_command_output_containment_terminal_summary_basis"),
                "selected terminal summary basis declared",
                request.get("selected_command_output_containment_terminal_summary_basis"),
                "COMMAND_OUTPUT_CONTAINMENT_BASIS_MISSING",
            ),
            _check(
                "command output containment live artifact basis declared",
                _basis_declared(request, "selected_command_output_containment_basis"),
                "selected command output containment basis declared",
                request.get("selected_command_output_containment_basis"),
                "COMMAND_OUTPUT_CONTAINMENT_BASIS_MISSING",
            ),
            _check(
                "command output containment outcome recorded",
                containment.get("outcome") == COMMAND_OUTPUT_CONTAINMENT_OUTCOME,
                COMMAND_OUTPUT_CONTAINMENT_OUTCOME,
                containment.get("outcome"),
                "COMMAND_OUTPUT_CONTAINMENT_NOT_RECORDED",
            ),
            _check(
                "command output containment failed check count zero",
                _to_int(containment.get("failed_check_count")) == 0,
                0,
                containment.get("failed_check_count"),
                "COMMAND_OUTPUT_CONTAINMENT_FAILED_CHECKS_PRESENT",
            ),
            _check(
                "command output containment event recorded",
                _truthy(containment.get("bounded_output_containment_event_recorded")),
                "one bounded output containment event recorded",
                containment.get("bounded_output_containment_event_recorded"),
                "COMMAND_OUTPUT_CONTAINMENT_EVENT_NOT_RECORDED",
            ),
            _check(
                "command output containment boundary basis preserved",
                _truthy(containment.get("command_output_boundary_basis_preserved")),
                "command output boundary basis preserved",
                containment.get("command_output_boundary_basis_preserved"),
                "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_BASIS_NOT_PRESERVED",
            ),
            _check(
                "command output containment output not created",
                not _truthy(containment.get("command_output_created")),
                "command output not created",
                containment.get("command_output_created"),
                "COMMAND_OUTPUT_CONTAINMENT_ALREADY_CREATED_OUTPUT",
            ),
            _check(
                "command output containment output capture not created",
                not _truthy(containment.get("output_capture_created")),
                "output capture not created",
                containment.get("output_capture_created"),
                "COMMAND_OUTPUT_CONTAINMENT_ALREADY_CREATED_OUTPUT_CAPTURE",
            ),
            _check(
                "command output containment output report artifact not created",
                not _truthy(containment.get("command_output_report_artifact_created")),
                "command output/report artifact not created",
                containment.get("command_output_report_artifact_created"),
                "COMMAND_OUTPUT_CONTAINMENT_ALREADY_CREATED_OUTPUT_REPORT_ARTIFACT",
            ),
            _check(
                "command output containment result not created",
                not _truthy(containment.get("command_result_created")),
                "command result not created",
                containment.get("command_result_created"),
                "COMMAND_OUTPUT_CONTAINMENT_ALREADY_CREATED_RESULT",
            ),
            _check(
                "command output containment success not created",
                not _truthy(containment.get("command_success_created")),
                "command success not created",
                containment.get("command_success_created"),
                "COMMAND_OUTPUT_CONTAINMENT_ALREADY_CREATED_SUCCESS",
            ),
            _check(
                "command output containment boundary basis declared",
                _basis_declared(request, "selected_command_output_containment_boundary_basis"),
                "selected command output containment boundary basis declared",
                request.get("selected_command_output_containment_boundary_basis"),
                "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_BASIS_MISSING",
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
        ]
    )

    prior_basis_checks = (
        ("command invocation basis declared", "selected_command_invocation_basis", "POST_INVOCATION_COMMAND_EXECUTION_BASIS_MISSING"),
        ("command execution review basis declared", "selected_command_execution_review_basis", "POST_INVOCATION_COMMAND_EXECUTION_BASIS_MISSING"),
        ("request consumption basis declared", "selected_request_consumption_basis", "POST_INVOCATION_COMMAND_EXECUTION_BASIS_MISSING"),
        ("consumed request basis declared", "selected_consumed_request_basis", "POST_INVOCATION_COMMAND_EXECUTION_BASIS_MISSING"),
        ("v2 admitted request basis declared", "selected_v2_admitted_request_basis", "V2_ADMITTED_REQUEST_BASIS_MISSING"),
        ("v1 predecessor/failure basis declared", "selected_v1_predecessor_failure_basis", "V1_PREDECESSOR_FAILURE_BASIS_MISSING"),
        (
            "older command execution boundary lineage basis declared",
            "selected_older_command_execution_boundary_lineage_basis",
            "OLDER_COMMAND_EXECUTION_BOUNDARY_LINEAGE_TREATED_AS_CURRENT_EXECUTION",
        ),
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
        checks.append(
            _check(name, _basis_declared(request, key), "basis declared", request.get(key), code)
        )

    checks.extend(
        [
            _check(
                "v2 admitted request failed check count zero",
                _to_int(request.get("selected_v2_failed_check_count") if "selected_v2_failed_check_count" in request else _failed_count(v2))
                in (0, None),
                0,
                request.get("selected_v2_failed_check_count")
                if "selected_v2_failed_check_count" in request
                else _failed_count(v2),
                "V2_ADMITTED_REQUEST_FAILED_CHECKS_PRESENT",
            ),
            _check(
                "v2 does not repair v1",
                not (
                    _truthy(v2.get("v2_treated_as_repairing_v1"))
                    or _truthy(v2.get("v2_repairs_v1"))
                    or _request_bool(request, ("v1_repaired",))
                ),
                "v2 successor does not repair v1",
                v2,
                "V2_TREATED_AS_REPAIRING_V1",
            ),
            _check(
                "v1 failure remains visible",
                not (_truthy(v1.get("v1_hidden")) or _request_bool(request, ("v1_hidden",))),
                "v1 failure visible",
                v1,
                "V1_FAILURE_HIDDEN",
            ),
            _check(
                "v1 not claimed passed",
                not (_truthy(v1.get("v1_claimed_passed")) or _request_bool(request, ("v1_claimed_passed",))),
                "v1 not claimed passed",
                v1,
                "V1_CLAIMED_PASSED",
            ),
            _check(
                "older command execution boundary lineage remains prior scaffolding only",
                bool(older_lineage) and not _lineage_as_current_execution(older_lineage),
                "older lineage not current execution",
                older_lineage,
                "OLDER_COMMAND_EXECUTION_BOUNDARY_LINEAGE_TREATED_AS_CURRENT_EXECUTION",
            ),
            _check(
                "consumed request token remains closed",
                not (
                    _truthy(consumed_request.get("consumed_request_reopened"))
                    or _truthy(consumed_request.get("request_reopened"))
                    or _request_bool(request, ("consumed_request_reopened",))
                ),
                "consumed request token closed",
                consumed_request,
                "CONSUMED_REQUEST_REOPENED",
            ),
        ]
    )

    posture_checks = (
        ("command output boundary only posture declared", "command_output_boundary_only_posture", "COMMAND_OUTPUT_BOUNDARY_ONLY_POSTURE_MISSING"),
        ("one future command output step posture declared", "one_future_command_output_step_posture", "ONE_FUTURE_COMMAND_OUTPUT_STEP_POSTURE_MISSING"),
        (
            "command output containment basis preserved posture declared",
            "command_output_containment_basis_preserved_posture",
            "COMMAND_OUTPUT_CONTAINMENT_BASIS_PRESERVED_POSTURE_MISSING",
        ),
        (
            "bounded output containment event preserved posture declared",
            "bounded_output_containment_event_preserved_posture",
            "BOUNDED_OUTPUT_CONTAINMENT_EVENT_PRESERVED_POSTURE_MISSING",
        ),
        ("execution trace audit-only posture declared", "execution_trace_audit_only_posture", "EXECUTION_TRACE_AUDIT_ONLY_POSTURE_MISSING"),
        ("no command output posture declared", "no_command_output_posture", "NO_COMMAND_OUTPUT_POSTURE_MISSING"),
        ("no output capture posture declared", "no_output_capture_posture", "NO_OUTPUT_CAPTURE_POSTURE_MISSING"),
        ("no output report artifact posture declared", "no_output_report_artifact_posture", "NO_OUTPUT_REPORT_ARTIFACT_POSTURE_MISSING"),
        ("no command result posture declared", "no_command_result_posture", "NO_COMMAND_RESULT_POSTURE_MISSING"),
        ("no command success posture declared", "no_command_success_posture", "NO_COMMAND_SUCCESS_POSTURE_MISSING"),
        ("no output as source posture declared", "no_output_as_source_posture", "NO_OUTPUT_AS_SOURCE_POSTURE_MISSING"),
        ("no result as authority posture declared", "no_result_as_authority_posture", "NO_RESULT_AS_AUTHORITY_POSTURE_MISSING"),
        ("no success as currentness posture declared", "no_success_as_currentness_posture", "NO_SUCCESS_AS_CURRENTNESS_POSTURE_MISSING"),
        ("no final completion posture declared", "no_final_completion_posture", "NO_FINAL_COMPLETION_POSTURE_MISSING"),
    )
    for name, key, code in posture_checks:
        checks.append(
            _check(name, _posture_declared(request, key), "posture declared", request.get(key), code)
        )

    remaining_postures = (
        "authorization_token_reuse_blocked_posture",
        "consumed_token_closed_posture",
        "no_reopen_consumed_request_posture",
        "returned_result_containment_posture",
    )
    for key in remaining_postures:
        checks.append(
            _check(
                key.replace("_", " ") + " declared",
                _posture_declared(request, key),
                "posture declared",
                request.get(key),
                "NON_CLAIM_MISSING_OR_FLIPPED",
            )
        )

    checks.append(
        _check(
            "command output boundary scope supported",
            bool(scope_values) and all(value in SUPPORTED_COMMAND_OUTPUT_BOUNDARY_SCOPE_SET for value in scope_values),
            SUPPORTED_COMMAND_OUTPUT_BOUNDARY_SCOPE,
            scope_values,
            "UNSUPPORTED_COMMAND_OUTPUT_BOUNDARY_SCOPE",
        )
    )

    collapse_specs = (
        (("boundary_treated_as_output",), "BOUNDARY_TREATED_AS_OUTPUT"),
        (("boundary_treated_as_output_capture",), "BOUNDARY_TREATED_AS_OUTPUT_CAPTURE"),
        (("boundary_treated_as_output_report_artifact",), "BOUNDARY_TREATED_AS_OUTPUT_REPORT_ARTIFACT"),
        (("boundary_treated_as_result",), "BOUNDARY_TREATED_AS_RESULT"),
        (("boundary_treated_as_success",), "BOUNDARY_TREATED_AS_SUCCESS"),
        (("containment_treated_as_output",), "CONTAINMENT_TREATED_AS_OUTPUT"),
        (("containment_treated_as_output_capture",), "CONTAINMENT_TREATED_AS_OUTPUT_CAPTURE"),
        (("containment_treated_as_output_report_artifact",), "CONTAINMENT_TREATED_AS_OUTPUT_REPORT_ARTIFACT"),
        (("containment_treated_as_result",), "CONTAINMENT_TREATED_AS_RESULT"),
        (("containment_treated_as_success",), "CONTAINMENT_TREATED_AS_SUCCESS"),
        (("command_output_created", "output_created"), "COMMAND_OUTPUT_CREATED"),
        (("output_capture_created",), "OUTPUT_CAPTURE_CREATED"),
        (
            ("command_output_report_artifact_created", "output_report_artifact_created"),
            "COMMAND_OUTPUT_REPORT_ARTIFACT_CREATED",
        ),
        (("command_result_created",), "COMMAND_RESULT_CREATED"),
        (("command_success_created",), "COMMAND_SUCCESS_CREATED"),
        (("execution_trace_treated_as_output",), "EXECUTION_TRACE_TREATED_AS_OUTPUT"),
        (("execution_trace_treated_as_result",), "EXECUTION_TRACE_TREATED_AS_RESULT"),
        (("execution_trace_treated_as_success",), "EXECUTION_TRACE_TREATED_AS_SUCCESS"),
        (("execution_trace_treated_as_source",), "EXECUTION_TRACE_TREATED_AS_SOURCE"),
        (("execution_trace_treated_as_authority",), "EXECUTION_TRACE_TREATED_AS_AUTHORITY"),
        (("command_output_became_source", "command_output_treated_as_source"), "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
        (("command_result_became_authority", "command_result_treated_as_authority"), "COMMAND_RESULT_TREATED_AS_AUTHORITY"),
        (
            ("command_success_created_currentness", "command_success_treated_as_currentness"),
            "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS",
        ),
        (
            ("command_success_claimed_final_completion", "command_success_treated_as_final_completion"),
            "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION",
        ),
        (("consumed_request_reopened",), "CONSUMED_REQUEST_REOPENED"),
        (("authorization_token_reused",), "AUTHORIZATION_TOKEN_REUSED"),
        (("prior_artifacts_mutated", "artifacts_mutated"), "ARTIFACTS_MUTATED"),
        (("deployment_created",), "DEPLOYMENT_CREATED"),
        (("runtime_hosting_created",), "RUNTIME_HOSTING_CREATED"),
        (("public_release_created",), "PUBLIC_RELEASE_CREATED"),
        (("operation_permission_created", "operation_created"), "OPERATION_CREATED"),
        (("public_launch_readiness_created", "public_readiness_created"), "PUBLIC_READINESS_CREATED"),
        (("final_completion_claimed",), "FINAL_COMPLETION_CLAIMED"),
        (("continuation_authorized",), "CONTINUATION_AUTHORIZED"),
        (("reusable_permission_created",), "REUSABLE_PERMISSION_CREATED"),
        (("derivative_reception_authorized",), "DERIVATIVE_RECEPTION_AUTHORIZED"),
        (("vessel_relation_authorized",), "VESSEL_RELATION_AUTHORIZED"),
        (("another_reception_request_authorized",), "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"),
        (("follow_on_work_authorized",), "FOLLOW_ON_WORK_AUTHORIZED"),
    )
    collapse_code = _first_true_code(request, collapse_specs)
    checks.append(
        _check(
            "boundary collapse flags absent",
            collapse_code is None,
            "all collapse flags explicit false",
            collapse_code,
            collapse_code or "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )

    replay_merge = _request_bool(request, ("mutation_performed", "replay_performed", "merge_performed"))
    checks.append(
        _check(
            "mutation replay merge not performed",
            not replay_merge,
            "mutation/replay/merge false",
            replay_merge,
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        )
    )

    full_body_emitted = _contains_forbidden_body(request)
    checks.append(
        _check(
            "raw full prior artifact body not emitted",
            not full_body_emitted,
            "no raw full prior artifact body",
            full_body_emitted,
            "FULL_PRIOR_ARTIFACT_BODY_EMITTED",
        )
    )

    checks.append(
        _check(
            "reference shaped input posture preserved",
            _truthy(_find(_mapping(request.get("reference_shaped_input_posture")), ("declared", "reference_shaped_input_posture"), False))
            or _reference_shaped(containment_basis),
            "reference-shaped input posture",
            request.get("reference_shaped_input_posture") or containment_basis,
            "FULL_PRIOR_ARTIFACT_BODY_EMITTED",
        )
    )

    non_claim_failures = [
        key for key, value in declared_non_claims.items() if not _explicit_false(value)
    ]
    checks.append(
        _check(
            "required non-claims explicit and false",
            not non_claim_failures,
            {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
            non_claim_failures,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )

    if _basis_bool(request, "selected_post_invocation_command_execution_basis", ("execution_trace_treated_as_output",)):
        checks.append(
            _check(
                "selected execution trace not output",
                False,
                "execution trace not output",
                True,
                "EXECUTION_TRACE_TREATED_AS_OUTPUT",
            )
        )
    if _basis_bool(request, "selected_post_invocation_command_execution_basis", ("execution_trace_treated_as_authority",)):
        checks.append(
            _check(
                "selected execution trace not authority",
                False,
                "execution trace not authority",
                True,
                "EXECUTION_TRACE_TREATED_AS_AUTHORITY",
            )
        )

    return checks


def _counts(checks: Iterable[Mapping[str, Any]]) -> tuple[int, int]:
    checks_list = list(checks)
    passed = sum(1 for check in checks_list if check.get("passed") is True)
    failed = sum(1 for check in checks_list if check.get("passed") is not True)
    return passed, failed


def _first_failed(checks: Iterable[Mapping[str, Any]]) -> Mapping[str, Any] | None:
    for check in checks:
        if check.get("passed") is not True:
            return check
    return None


def _select_outcome(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    forced_block_code: str | None = None,
) -> tuple[str, dict[str, Any]]:
    first_failed = _first_failed(checks)
    intent = request.get("command_output_boundary_intent")
    requested = _requested_outcome(request)
    if forced_block_code or first_failed:
        failed = first_failed or {}
        return OUTCOME_BLOCKED, {
            "blocked": True,
            "code": forced_block_code or failed.get("block_code"),
            "reason": request.get("block_reason")
            or failed.get("check_name")
            or forced_block_code,
        }
    if intent == INTENT_BLOCK:
        return OUTCOME_BLOCKED, {
            "blocked": True,
            "code": "COMMAND_OUTPUT_BOUNDARY_BLOCKED_BY_REQUEST",
            "reason": request.get("block_reason") or "request blocked command output boundary recording",
        }
    if intent == INTENT_DO_NOT_RECORD or requested == OUTCOME_NOT_RECORDED:
        return OUTCOME_NOT_RECORDED, {"blocked": False, "code": None, "reason": None}
    if requested == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS, {"blocked": False, "code": None, "reason": None}
    if requested == OUTCOME_BLOCKED:
        return OUTCOME_BLOCKED, {
            "blocked": True,
            "code": "COMMAND_OUTPUT_BOUNDARY_BLOCKED_BY_REQUEST",
            "reason": request.get("block_reason") or "requested blocked outcome",
        }
    return OUTCOME_RECORDED, {"blocked": False, "code": None, "reason": None}


def _statement(outcome: str) -> dict[str, bool]:
    recorded = outcome == OUTCOME_RECORDED
    return {
        "command_output_boundary_recorded": recorded,
        "one_future_command_output_step_declared": recorded,
        "command_output_containment_basis_preserved": recorded,
        "bounded_output_containment_event_preserved": recorded,
        "recorded_command_execution_event_preserved": recorded,
        "execution_trace_audit_only_preserved": recorded,
        "command_output_still_not_created": recorded,
        "output_capture_not_created": recorded,
        "command_output_report_artifact_not_created": recorded,
        "command_result_still_not_created": recorded,
        "command_success_still_not_created": recorded,
        "authorization_token_reuse_blocked": recorded,
        "consumed_request_token_remains_closed": recorded,
        "v1_predecessor_failure_preserved": recorded,
        "returned_result_containment_preserved": recorded,
        "command_output_created": False,
        "output_capture_created": False,
        "command_output_report_artifact_created": False,
        "command_result_created": False,
        "command_success_created": False,
        "boundary_treated_as_output": False,
        "boundary_treated_as_output_capture": False,
        "boundary_treated_as_output_report_artifact": False,
        "boundary_treated_as_result": False,
        "boundary_treated_as_success": False,
        "containment_treated_as_output": False,
        "containment_treated_as_output_capture": False,
        "containment_treated_as_output_report_artifact": False,
        "containment_treated_as_result": False,
        "containment_treated_as_success": False,
        "execution_trace_treated_as_output": False,
        "execution_trace_treated_as_result": False,
        "execution_trace_treated_as_success": False,
        "execution_trace_treated_as_source": False,
        "execution_trace_treated_as_authority": False,
        "command_output_became_source": False,
        "command_result_became_authority": False,
        "command_success_created_currentness": False,
        "command_success_claimed_final_completion": False,
        "authorization_token_reused": False,
        "consumed_request_reopened": False,
        "v1_repaired": False,
        "v1_hidden": False,
        "v1_claimed_passed": False,
        "deployment_created": False,
        "runtime_hosting_created": False,
        "public_release_created": False,
        "operation_permission_created": False,
        "public_launch_readiness_created": False,
        "final_completion_claimed": False,
        "continuation_authorized": False,
        "publication_flow_opened": False,
        "reusable_permission_created": False,
        "derivative_reception_authorized": False,
        "vessel_relation_authorized": False,
        "another_reception_request_authorized": False,
        "follow_on_work_authorized": False,
        "mutation_performed": False,
        "replay_performed": False,
        "merge_performed": False,
    }


def _non_meaning() -> dict[str, bool]:
    return {
        "command_output_exists": False,
        "output_was_captured": False,
        "command_output_report_artifact_exists": False,
        "command_result_exists": False,
        "command_success_exists": False,
        "boundary_is_output": False,
        "boundary_is_output_capture": False,
        "boundary_is_output_report_artifact": False,
        "boundary_is_result": False,
        "boundary_is_success": False,
        "containment_is_output": False,
        "containment_is_output_capture": False,
        "containment_is_output_report_artifact": False,
        "containment_is_result": False,
        "containment_is_success": False,
        "execution_trace_is_output": False,
        "execution_trace_is_result": False,
        "execution_trace_is_success": False,
        "execution_trace_is_source": False,
        "execution_trace_is_authority": False,
        "output_is_source": False,
        "result_is_authority": False,
        "success_is_currentness": False,
        "success_is_final_completion": False,
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


def _open_items() -> dict[str, Any]:
    return {
        "items": [
            "command output boundary test",
            "command output boundary live artifact",
            "command output step, if separately specified",
            "command output",
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


def _metadata(request: Mapping[str, Any]) -> dict[str, Any]:
    request_id = str(request.get("command_output_boundary_request_id") or "command_output_boundary_request")
    return {
        "portable_source_body_verification_command_output_boundary_result_id": (
            f"{request_id}__portable_source_body_verification_command_output_boundary_result"
        ),
        "portable_source_body_verification_command_output_boundary_result_type": RESULT_TYPE,
        "portable_source_body_verification_command_output_boundary_result_version": RESULT_VERSION,
        "generated_at": _now(),
        "resolver_module": RESOLVER_MODULE,
        "short_resolver_filename_preserved": True,
        "full_upstream_lineage_preserved_in_selected_basis": True,
    }


def _scope_section(request: Mapping[str, Any]) -> dict[str, Any]:
    values = _scope_values(request.get("command_output_boundary_scope"))
    return {
        "declared_scope_values": values,
        "supported_scope_values": list(SUPPORTED_COMMAND_OUTPUT_BOUNDARY_SCOPE),
        "unsupported_scope_values": [
            value for value in values if value not in SUPPORTED_COMMAND_OUTPUT_BOUNDARY_SCOPE_SET
        ],
        "scope_is_command_output_boundary_only": "COMMAND_OUTPUT_BOUNDARY_ONLY" in values,
        "one_future_command_output_step_only": "ONE_FUTURE_COMMAND_OUTPUT_STEP_ONLY" in values,
    }


def build_portable_source_body_verification_command_output_boundary_summary(
    result: Mapping[str, Any]
) -> dict[str, Any]:
    statement = _mapping(result.get("command_output_boundary_statement"))
    block = _mapping(result.get("block"))
    checks = result.get("command_output_boundary_checks") or []
    passed, failed = _counts(checks if isinstance(checks, list) else [])
    question = _mapping(result.get("declared_command_output_boundary_question"))
    containment = _mapping(result.get("selected_command_output_containment_basis"))
    post_invocation = _mapping(result.get("selected_post_invocation_command_execution_basis"))
    v2 = _mapping(result.get("selected_v2_admitted_request_basis"))
    older = _mapping(result.get("selected_older_command_execution_boundary_lineage_basis"))
    non_claims = _mapping(result.get("non_claims"))
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("code"),
        "block_reason": block.get("reason"),
        "request_id": question.get("command_output_boundary_request_id"),
        "question": question.get("command_output_boundary_question"),
        "intent": question.get("command_output_boundary_intent"),
        "passed_check_count": passed,
        "failed_check_count": failed,
        "command_output_boundary_recorded": statement.get("command_output_boundary_recorded", False),
        "one_future_command_output_step_declared": statement.get(
            "one_future_command_output_step_declared", False
        ),
        "command_output_containment_basis_preserved": statement.get(
            "command_output_containment_basis_preserved", False
        ),
        "bounded_output_containment_event_preserved": statement.get(
            "bounded_output_containment_event_preserved", False
        ),
        "recorded_command_execution_event_preserved": statement.get(
            "recorded_command_execution_event_preserved", False
        ),
        "execution_trace_audit_only_preserved": statement.get(
            "execution_trace_audit_only_preserved", False
        ),
        "command_output_still_not_created": statement.get(
            "command_output_still_not_created", False
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
        "selected_command_output_containment_outcome": containment.get("outcome"),
        "selected_command_output_containment_failed_check_count": containment.get(
            "failed_check_count"
        ),
        "selected_post_invocation_execution_outcome": post_invocation.get("outcome"),
        "selected_post_invocation_execution_failed_check_count": post_invocation.get(
            "failed_check_count"
        ),
        "selected_v2_outcome": v2.get("outcome"),
        "selected_v2_version": v2.get("version"),
        "selected_v2_failed_check_count": v2.get("failed_check_count"),
        "boundary_not_output_capture_output_report_result_success": all(
            not statement.get(key, False)
            for key in (
                "boundary_treated_as_output",
                "boundary_treated_as_output_capture",
                "boundary_treated_as_output_report_artifact",
                "boundary_treated_as_result",
                "boundary_treated_as_success",
            )
        ),
        "containment_not_output_capture_output_report_result_success": all(
            not statement.get(key, False)
            for key in (
                "containment_treated_as_output",
                "containment_treated_as_output_capture",
                "containment_treated_as_output_report_artifact",
                "containment_treated_as_result",
                "containment_treated_as_success",
            )
        ),
        "execution_trace_not_output_result_success_source_authority": all(
            not statement.get(key, False)
            for key in (
                "execution_trace_treated_as_output",
                "execution_trace_treated_as_result",
                "execution_trace_treated_as_success",
                "execution_trace_treated_as_source",
                "execution_trace_treated_as_authority",
            )
        ),
        "output_not_source": not statement.get("command_output_became_source", False),
        "result_not_authority": not statement.get("command_result_became_authority", False),
        "success_not_currentness_or_final_completion": not statement.get(
            "command_success_created_currentness", False
        )
        and not statement.get("command_success_claimed_final_completion", False),
        "older_command_execution_boundary_lineage_not_treated_as_current_execution": not _lineage_as_current_execution(
            _mapping(older.get("basis"))
        ),
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
        "key_non_claims": {
            key: non_claims.get(key, False)
            for key in REQUIRED_FALSE_NON_CLAIMS
        },
    }


def _build_result(
    request: Mapping[str, Any],
    forced_block_code: str | None = None,
    forced_block_reason: str | None = None,
) -> dict[str, Any]:
    safe_request = _copy(dict(request))
    checks = _build_checks(safe_request, forced_block_code, forced_block_reason)
    outcome, block = _select_outcome(safe_request, checks, forced_block_code)
    passed_check_count, failed_check_count = _counts(checks)
    statement = _statement(outcome)

    additional_requested = outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    not_recorded = outcome == OUTCOME_NOT_RECORDED
    result: dict[str, Any] = {
        "portable_source_body_verification_command_output_boundary_metadata": _metadata(safe_request),
        "declared_command_output_boundary_question": {
            "command_output_boundary_request_id": safe_request.get("command_output_boundary_request_id"),
            "command_output_boundary_question": safe_request.get("command_output_boundary_question"),
            "canonical_command_output_boundary_question": CORE_COMMAND_OUTPUT_BOUNDARY_QUESTION,
            "command_output_boundary_intent": safe_request.get("command_output_boundary_intent"),
            "requested_command_output_boundary_outcome": safe_request.get(
                "requested_command_output_boundary_outcome"
            ),
            "declared_request_path": safe_request.get("declared_request_path"),
        },
        "selected_command_output_containment_basis": _selected_command_output_containment_basis(
            safe_request
        ),
        "selected_command_output_containment_terminal_summary_basis": {
            "basis": _sanitize(_basis(safe_request, "selected_command_output_containment_terminal_summary_basis")),
            "declared": _basis_declared(
                safe_request, "selected_command_output_containment_terminal_summary_basis"
            ),
            "readability_basis_only": True,
            "does_not_create_command_output": True,
            "does_not_create_output_capture": True,
            "does_not_create_command_output_report_artifact": True,
            "does_not_create_command_result": True,
            "does_not_create_command_success": True,
            "does_not_authorize_follow_on_work": True,
        },
        "selected_command_output_containment_boundary_basis": _selected_prior_basis(
            safe_request,
            "selected_command_output_containment_boundary_basis",
            "selected_command_output_containment_boundary_result_path",
            COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_OUTCOME,
        ),
        "selected_post_invocation_command_execution_basis": _selected_prior_basis(
            safe_request,
            "selected_post_invocation_command_execution_basis",
            "selected_post_invocation_command_execution_result_path",
            POST_INVOCATION_COMMAND_EXECUTION_OUTCOME,
        ),
        "selected_post_invocation_command_execution_terminal_summary_basis": {
            "basis": _sanitize(
                _basis(safe_request, "selected_post_invocation_command_execution_terminal_summary_basis")
            ),
            "declared": _basis_declared(
                safe_request, "selected_post_invocation_command_execution_terminal_summary_basis"
            ),
            "readability_basis_only": True,
            "does_not_create_command_output": True,
            "does_not_create_command_result": True,
            "does_not_create_command_success": True,
            "does_not_authorize_follow_on_work": True,
        },
        "selected_command_invocation_basis": _selected_prior_basis(
            safe_request,
            "selected_command_invocation_basis",
            "selected_command_invocation_result_path",
            COMMAND_INVOCATION_OUTCOME,
        ),
        "selected_command_execution_review_basis": _selected_prior_basis(
            safe_request,
            "selected_command_execution_review_basis",
            "selected_command_execution_review_result_path",
            COMMAND_EXECUTION_REVIEW_OUTCOME,
        ),
        "selected_request_consumption_basis": _selected_prior_basis(
            safe_request,
            "selected_request_consumption_basis",
            "selected_request_consumption_result_path",
            REQUEST_CONSUMPTION_OUTCOME,
        ),
        "selected_consumed_request_basis": _selected_prior_basis(
            safe_request, "selected_consumed_request_basis"
        ),
        "selected_v2_admitted_request_basis": _selected_prior_basis(
            safe_request,
            "selected_v2_admitted_request_basis",
            "selected_v2_admitted_request_artifact_path",
            V2_ADMITTED_REQUEST_OUTCOME,
            V2_ADMITTED_REQUEST_VERSION,
        ),
        "selected_v1_predecessor_failure_basis": _selected_prior_basis(
            safe_request,
            "selected_v1_predecessor_failure_basis",
            "selected_v1_predecessor_artifact_path",
        ),
        "selected_older_command_execution_boundary_lineage_basis": _selected_prior_basis(
            safe_request,
            "selected_older_command_execution_boundary_lineage_basis",
            "selected_older_command_execution_boundary_lineage_result_path",
        ),
        "selected_command_report_basis": _selected_prior_basis(
            safe_request, "selected_command_report_basis", "selected_command_report_path"
        ),
        "selected_command_implementation_boundary_basis": _selected_prior_basis(
            safe_request,
            "selected_command_implementation_boundary_basis",
            "selected_command_implementation_boundary_result_path",
        ),
        "selected_command_boundary_basis": _selected_prior_basis(
            safe_request, "selected_command_boundary_basis", "selected_command_boundary_result_path"
        ),
        "selected_artifact_emission_containment_basis": _selected_prior_basis(
            safe_request,
            "selected_artifact_emission_containment_basis",
            "selected_artifact_emission_containment_result_path",
        ),
        "selected_evidence_manifest_basis": _selected_prior_basis(
            safe_request, "selected_evidence_manifest_basis", "selected_evidence_manifest_result_path"
        ),
        "selected_portable_verification_basis": _selected_prior_basis(
            safe_request, "selected_portable_verification_basis", "selected_portable_verification_result_path"
        ),
        "command_output_boundary_only_posture": _posture_section(
            safe_request, "command_output_boundary_only_posture"
        ),
        "one_future_command_output_step_posture": _posture_section(
            safe_request, "one_future_command_output_step_posture"
        ),
        "command_output_containment_basis_preserved_posture": _posture_section(
            safe_request, "command_output_containment_basis_preserved_posture"
        ),
        "bounded_output_containment_event_preserved_posture": _posture_section(
            safe_request, "bounded_output_containment_event_preserved_posture"
        ),
        "execution_trace_audit_only_posture": _posture_section(
            safe_request, "execution_trace_audit_only_posture"
        ),
        "no_command_output_posture": _posture_section(safe_request, "no_command_output_posture"),
        "no_output_capture_posture": _posture_section(safe_request, "no_output_capture_posture"),
        "no_output_report_artifact_posture": _posture_section(
            safe_request, "no_output_report_artifact_posture"
        ),
        "no_command_result_posture": _posture_section(safe_request, "no_command_result_posture"),
        "no_command_success_posture": _posture_section(safe_request, "no_command_success_posture"),
        "no_output_as_source_posture": _posture_section(safe_request, "no_output_as_source_posture"),
        "no_result_as_authority_posture": _posture_section(
            safe_request, "no_result_as_authority_posture"
        ),
        "no_success_as_currentness_posture": _posture_section(
            safe_request, "no_success_as_currentness_posture"
        ),
        "no_final_completion_posture": _posture_section(safe_request, "no_final_completion_posture"),
        "authorization_token_reuse_blocked_posture": _posture_section(
            safe_request, "authorization_token_reuse_blocked_posture"
        ),
        "consumed_token_closed_posture": _posture_section(
            safe_request, "consumed_token_closed_posture"
        ),
        "no_reopen_consumed_request_posture": _posture_section(
            safe_request, "no_reopen_consumed_request_posture"
        ),
        "returned_result_containment_posture": _posture_section(
            safe_request, "returned_result_containment_posture"
        ),
        "command_output_boundary_scope": _scope_section(safe_request),
        "command_output_boundary_checks": checks,
        "command_output_boundary_statement": statement,
        "command_output_boundary_non_meaning": _non_meaning(),
        "additional_basis_required": {
            "required": additional_requested,
            "context": _sanitize(safe_request.get("additional_basis_context") or {}),
            "missing_basis_not_scheduled": True,
            "missing_basis_not_authorized": True,
            "missing_basis_not_executed": True,
        },
        "not_recorded_basis": {
            "not_recorded": not_recorded,
            "reason": _sanitize(safe_request.get("not_recorded_basis") or safe_request.get("block_reason") or {}),
            "no_repair_authorized": True,
            "no_next_work_authorized": True,
        },
        "what_remains_open": _open_items(),
        "non_claims": _default_non_claims(),
        "outcome": outcome,
        "block": block,
    }
    result["portable_source_body_verification_command_output_boundary_summary"] = (
        build_portable_source_body_verification_command_output_boundary_summary(result)
    )
    result["portable_source_body_verification_command_output_boundary_summary"][
        "passed_check_count"
    ] = passed_check_count
    result["portable_source_body_verification_command_output_boundary_summary"][
        "failed_check_count"
    ] = failed_check_count
    return result


def resolve_portable_source_body_verification_command_output_boundary(
    declared_command_output_boundary_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded command output boundary request."""

    if declared_command_output_boundary_request is None:
        return _build_result(
            {},
            forced_block_code="COMMAND_OUTPUT_BOUNDARY_QUESTION_UNDECLARED",
            forced_block_reason="declared command output boundary request missing",
        )
    if not isinstance(declared_command_output_boundary_request, Mapping):
        return _build_result(
            {},
            forced_block_code="DECLARED_COMMAND_OUTPUT_BOUNDARY_REQUEST_MALFORMED",
            forced_block_reason="declared command output boundary request is not a mapping",
        )
    return _build_result(declared_command_output_boundary_request)


def resolve_portable_source_body_verification_command_output_boundary_from_path(
    declared_command_output_boundary_request_path: Path | str,
) -> dict[str, Any]:
    """Load a declared command output boundary request JSON object from a path."""

    path = Path(declared_command_output_boundary_request_path)
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        return _build_result(
            {"declared_request_path": str(path)},
            forced_block_code="DECLARED_COMMAND_OUTPUT_BOUNDARY_REQUEST_UNREADABLE",
            forced_block_reason=str(exc),
        )
    try:
        loaded = json.loads(raw)
    except json.JSONDecodeError as exc:
        return _build_result(
            {"declared_request_path": str(path)},
            forced_block_code="DECLARED_COMMAND_OUTPUT_BOUNDARY_REQUEST_MALFORMED",
            forced_block_reason=str(exc),
        )
    if not isinstance(loaded, Mapping):
        return _build_result(
            {"declared_request_path": str(path)},
            forced_block_code="DECLARED_COMMAND_OUTPUT_BOUNDARY_REQUEST_MALFORMED",
            forced_block_reason="declared command output boundary request JSON is not an object",
        )
    loaded_dict = dict(loaded)
    loaded_dict["declared_request_path"] = str(path)
    return _build_result(loaded_dict)


def _safe_component(value: Any) -> str:
    text = str(value or "command_output_boundary_request")
    safe = []
    for char in text:
        if char.isalnum() or char in {"-", "_", "."}:
            safe.append(char)
        else:
            safe.append("_")
    return "".join(safe).strip("_") or "command_output_boundary_request"


def _deduplicated_output_path(path: Path) -> Path:
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


def write_portable_source_body_verification_command_output_boundary_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a bounded command output boundary result JSON artifact additively."""

    if not isinstance(result, Mapping):
        raise PortableSourceBodyVerificationCommandOutputBoundaryError(
            "command output boundary result must be a mapping"
        )
    if output_path is None:
        question = _mapping(result.get("declared_command_output_boundary_question"))
        request_id = _safe_component(question.get("command_output_boundary_request_id"))
        output_path = (
            PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_BOUNDARY_ROOT
            / f"{request_id}__portable_source_body_verification_command_output_boundary_result.json"
        )
    path = _deduplicated_output_path(Path(output_path))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(_sanitize(dict(result)), indent=2, sort_keys=True, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    return path


def build_declared_portable_source_body_verification_command_output_boundary_request(
    *,
    command_output_boundary_request_id: str,
    command_output_boundary_question: str = CORE_COMMAND_OUTPUT_BOUNDARY_QUESTION,
    command_output_boundary_intent: str = INTENT_RECORD,
    selected_command_output_containment_basis: Mapping[str, Any],
    selected_command_output_containment_terminal_summary_basis: Mapping[str, Any],
    selected_command_output_containment_boundary_basis: Mapping[str, Any],
    selected_post_invocation_command_execution_basis: Mapping[str, Any],
    selected_post_invocation_command_execution_terminal_summary_basis: Mapping[str, Any],
    selected_command_invocation_basis: Mapping[str, Any],
    selected_command_execution_review_basis: Mapping[str, Any],
    selected_request_consumption_basis: Mapping[str, Any],
    selected_consumed_request_basis: Mapping[str, Any],
    selected_v2_admitted_request_basis: Mapping[str, Any],
    selected_v1_predecessor_failure_basis: Mapping[str, Any],
    selected_older_command_execution_boundary_lineage_basis: Mapping[str, Any],
    selected_command_report_basis: Mapping[str, Any],
    selected_command_implementation_boundary_basis: Mapping[str, Any],
    selected_command_boundary_basis: Mapping[str, Any],
    selected_artifact_emission_containment_basis: Mapping[str, Any],
    selected_evidence_manifest_basis: Mapping[str, Any],
    selected_portable_verification_basis: Mapping[str, Any],
    command_output_boundary_only_posture: Mapping[str, Any],
    one_future_command_output_step_posture: Mapping[str, Any],
    command_output_containment_basis_preserved_posture: Mapping[str, Any],
    bounded_output_containment_event_preserved_posture: Mapping[str, Any],
    execution_trace_audit_only_posture: Mapping[str, Any],
    no_command_output_posture: Mapping[str, Any],
    no_output_capture_posture: Mapping[str, Any],
    no_output_report_artifact_posture: Mapping[str, Any],
    no_command_result_posture: Mapping[str, Any],
    no_command_success_posture: Mapping[str, Any],
    no_output_as_source_posture: Mapping[str, Any],
    no_result_as_authority_posture: Mapping[str, Any],
    no_success_as_currentness_posture: Mapping[str, Any],
    no_final_completion_posture: Mapping[str, Any],
    authorization_token_reuse_blocked_posture: Mapping[str, Any],
    consumed_token_closed_posture: Mapping[str, Any],
    no_reopen_consumed_request_posture: Mapping[str, Any],
    returned_result_containment_posture: Mapping[str, Any],
    command_output_boundary_scope: Iterable[str] | Mapping[str, Any] | str = SUPPORTED_COMMAND_OUTPUT_BOUNDARY_SCOPE,
    requested_command_output_boundary_outcome: str = OUTCOME_RECORDED,
    additional_basis_context: Mapping[str, Any] | None = None,
    not_recorded_basis: Mapping[str, Any] | None = None,
    declared_non_claims: Mapping[str, Any] | None = None,
    **shortcut_fields: Any,
) -> dict[str, Any]:
    """Build a declared command output boundary request without inferring output."""

    request: dict[str, Any] = {
        "command_output_boundary_request_id": command_output_boundary_request_id,
        "command_output_boundary_question": command_output_boundary_question,
        "command_output_boundary_intent": command_output_boundary_intent,
        "selected_command_output_containment_basis": _copy(dict(selected_command_output_containment_basis)),
        "selected_command_output_containment_terminal_summary_basis": _copy(
            dict(selected_command_output_containment_terminal_summary_basis)
        ),
        "selected_command_output_containment_boundary_basis": _copy(
            dict(selected_command_output_containment_boundary_basis)
        ),
        "selected_post_invocation_command_execution_basis": _copy(
            dict(selected_post_invocation_command_execution_basis)
        ),
        "selected_post_invocation_command_execution_terminal_summary_basis": _copy(
            dict(selected_post_invocation_command_execution_terminal_summary_basis)
        ),
        "selected_command_invocation_basis": _copy(dict(selected_command_invocation_basis)),
        "selected_command_execution_review_basis": _copy(dict(selected_command_execution_review_basis)),
        "selected_request_consumption_basis": _copy(dict(selected_request_consumption_basis)),
        "selected_consumed_request_basis": _copy(dict(selected_consumed_request_basis)),
        "selected_v2_admitted_request_basis": _copy(dict(selected_v2_admitted_request_basis)),
        "selected_v1_predecessor_failure_basis": _copy(dict(selected_v1_predecessor_failure_basis)),
        "selected_older_command_execution_boundary_lineage_basis": _copy(
            dict(selected_older_command_execution_boundary_lineage_basis)
        ),
        "selected_command_report_basis": _copy(dict(selected_command_report_basis)),
        "selected_command_implementation_boundary_basis": _copy(
            dict(selected_command_implementation_boundary_basis)
        ),
        "selected_command_boundary_basis": _copy(dict(selected_command_boundary_basis)),
        "selected_artifact_emission_containment_basis": _copy(
            dict(selected_artifact_emission_containment_basis)
        ),
        "selected_evidence_manifest_basis": _copy(dict(selected_evidence_manifest_basis)),
        "selected_portable_verification_basis": _copy(dict(selected_portable_verification_basis)),
        "command_output_boundary_only_posture": _copy(dict(command_output_boundary_only_posture)),
        "one_future_command_output_step_posture": _copy(dict(one_future_command_output_step_posture)),
        "command_output_containment_basis_preserved_posture": _copy(
            dict(command_output_containment_basis_preserved_posture)
        ),
        "bounded_output_containment_event_preserved_posture": _copy(
            dict(bounded_output_containment_event_preserved_posture)
        ),
        "execution_trace_audit_only_posture": _copy(dict(execution_trace_audit_only_posture)),
        "no_command_output_posture": _copy(dict(no_command_output_posture)),
        "no_output_capture_posture": _copy(dict(no_output_capture_posture)),
        "no_output_report_artifact_posture": _copy(dict(no_output_report_artifact_posture)),
        "no_command_result_posture": _copy(dict(no_command_result_posture)),
        "no_command_success_posture": _copy(dict(no_command_success_posture)),
        "no_output_as_source_posture": _copy(dict(no_output_as_source_posture)),
        "no_result_as_authority_posture": _copy(dict(no_result_as_authority_posture)),
        "no_success_as_currentness_posture": _copy(dict(no_success_as_currentness_posture)),
        "no_final_completion_posture": _copy(dict(no_final_completion_posture)),
        "authorization_token_reuse_blocked_posture": _copy(
            dict(authorization_token_reuse_blocked_posture)
        ),
        "consumed_token_closed_posture": _copy(dict(consumed_token_closed_posture)),
        "no_reopen_consumed_request_posture": _copy(dict(no_reopen_consumed_request_posture)),
        "returned_result_containment_posture": _copy(dict(returned_result_containment_posture)),
        "command_output_boundary_scope": _copy(command_output_boundary_scope),
        "requested_command_output_boundary_outcome": requested_command_output_boundary_outcome,
        "additional_basis_context": _copy(dict(additional_basis_context or {})),
        "not_recorded_basis": _copy(dict(not_recorded_basis or {})),
        "declared_non_claims": _default_non_claims(),
    }
    if declared_non_claims is not None:
        request["declared_non_claims"].update(_copy(dict(declared_non_claims)))
    for key, value in shortcut_fields.items():
        request[key] = _copy(value)
    return request
