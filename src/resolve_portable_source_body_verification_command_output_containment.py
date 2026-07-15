"""Portable source-body verification command output containment resolver.

This module records command output containment only. It is downstream of the
recorded command output containment boundary and may record one bounded
containment event while preserving that command output, output capture,
output/report artifact, command result, and command success remain separately
bounded future work.

It does not create command output, capture output, create command output/report
artifacts, create command result, create command success, create authority,
create currentness, create final completion, reopen a consumed request token,
reuse a spent one-shot authorization token, mutate artifacts, or authorize
follow-on work.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class PortableSourceBodyVerificationCommandOutputContainmentError(Exception):
    """Raised for hard command output containment resolver failures."""


RESOLVER_MODULE = "resolve_portable_source_body_verification_command_output_containment"
RESULT_VERSION = "0.1.0"
RESULT_TYPE = "portable_source_body_verification_command_output_containment_result"

PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_CONTAINMENT_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_command_output_containment"
)
OUTPUT_ROOT = PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_CONTAINMENT_ROOT

CORE_COMMAND_OUTPUT_CONTAINMENT_QUESTION = (
    "Can the recorded command output containment boundary basis be used to record one bounded command "
    "output containment event without creating command output, output capture, command output/report "
    "artifact, command result, command success, source, authority, currentness, final completion, "
    "continuation, reusable permission, derivative reception, vessel relation, another reception request, "
    "or follow-on work?"
)

INTENT_RECORD = "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_CONTAINMENT"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_CONTAINMENT"
INTENT_BLOCK = "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_CONTAINMENT"
SUPPORTED_INTENTS = frozenset({INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK})

OUTCOME_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_CONTAINMENT_RECORDED"
OUTCOME_NOT_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_CONTAINMENT_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_CONTAINMENT_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_CONTAINMENT_BLOCKED"
COMMAND_OUTPUT_CONTAINMENT_OUTCOME = OUTCOME_RECORDED
OUTCOME_FAMILY = frozenset(
    {OUTCOME_RECORDED, OUTCOME_NOT_RECORDED, OUTCOME_REQUIRES_ADDITIONAL_BASIS, OUTCOME_BLOCKED}
)

COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_RECORDED"
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

SUPPORTED_COMMAND_OUTPUT_CONTAINMENT_SCOPE = (
    "COMMAND_OUTPUT_CONTAINMENT_ONLY",
    "ONE_BOUNDED_COMMAND_OUTPUT_CONTAINMENT_EVENT_RECORDED",
    "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_BASIS_PRESERVED",
    "RECORDED_COMMAND_EXECUTION_EVENT_PRESERVED",
    "EXECUTION_TRACE_AUDIT_ONLY_PRESERVED",
    "COMMAND_OUTPUT_NOT_CREATED",
    "COMMAND_OUTPUT_CAPTURE_NOT_CREATED",
    "COMMAND_OUTPUT_REPORT_ARTIFACT_NOT_CREATED",
    "COMMAND_RESULT_NOT_CREATED",
    "COMMAND_SUCCESS_NOT_CREATED",
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
SUPPORTED_COMMAND_OUTPUT_CONTAINMENT_SCOPE_SET = frozenset(SUPPORTED_COMMAND_OUTPUT_CONTAINMENT_SCOPE)

REQUIRED_FALSE_NON_CLAIMS = (
    "command_output_created",
    "output_capture_created",
    "command_output_report_artifact_created",
    "command_result_created",
    "command_success_created",
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
    "command_output_containment_recorded",
    "bounded_command_output_containment_event_recorded",
    "command_output_boundary_basis_preserved",
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

BLOCK_CODES = frozenset(
    {
        "DECLARED_COMMAND_OUTPUT_CONTAINMENT_REQUEST_MALFORMED",
        "DECLARED_COMMAND_OUTPUT_CONTAINMENT_REQUEST_UNREADABLE",
        "COMMAND_OUTPUT_CONTAINMENT_QUESTION_UNDECLARED",
        "COMMAND_OUTPUT_CONTAINMENT_INTENT_UNSUPPORTED",
        "COMMAND_OUTPUT_CONTAINMENT_BLOCKED_BY_REQUEST",
        "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_BASIS_MISSING",
        "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_NOT_RECORDED",
        "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_FAILED_CHECKS_PRESENT",
        "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_STEP_NOT_DECLARED",
        "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_ALREADY_CREATED_OUTPUT",
        "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_ALREADY_CREATED_OUTPUT_CAPTURE",
        "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_ALREADY_CREATED_OUTPUT_REPORT_ARTIFACT",
        "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_ALREADY_CREATED_RESULT",
        "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_ALREADY_CREATED_SUCCESS",
        "POST_INVOCATION_COMMAND_EXECUTION_BASIS_MISSING",
        "POST_INVOCATION_COMMAND_EXECUTION_NOT_RECORDED",
        "POST_INVOCATION_COMMAND_EXECUTION_FAILED_CHECKS_PRESENT",
        "POST_INVOCATION_COMMAND_EXECUTION_EVENT_NOT_RECORDED",
        "POST_INVOCATION_COMMAND_EXECUTION_TRACE_NOT_AUDIT_ONLY",
        "COMMAND_INVOCATION_BASIS_MISSING",
        "COMMAND_EXECUTION_REVIEW_BASIS_MISSING",
        "REQUEST_CONSUMPTION_BASIS_MISSING",
        "CONSUMED_REQUEST_BASIS_MISSING",
        "CONTAINMENT_TREATED_AS_OUTPUT",
        "CONTAINMENT_TREATED_AS_OUTPUT_CAPTURE",
        "CONTAINMENT_TREATED_AS_OUTPUT_REPORT_ARTIFACT",
        "CONTAINMENT_TREATED_AS_RESULT",
        "CONTAINMENT_TREATED_AS_SUCCESS",
        "COMMAND_OUTPUT_CREATED",
        "OUTPUT_CAPTURE_CREATED",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_CREATED",
        "COMMAND_RESULT_CREATED",
        "COMMAND_SUCCESS_CREATED",
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
        "OUTPUT_CONTAINMENT_ONLY_POSTURE_MISSING",
        "ONE_BOUNDED_COMMAND_OUTPUT_CONTAINMENT_EVENT_POSTURE_MISSING",
        "COMMAND_OUTPUT_BOUNDARY_BASIS_PRESERVED_POSTURE_MISSING",
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
        "UNSUPPORTED_COMMAND_OUTPUT_CONTAINMENT_SCOPE",
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


def _now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _copy(value: Any) -> Any:
    return copy.deepcopy(value)


def _mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


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


def _find(mapping: Mapping[str, Any], keys: Sequence[str]) -> Any:
    for key in keys:
        if key in mapping:
            return mapping[key]
    for value in mapping.values():
        if isinstance(value, Mapping):
            found = _find(value, keys)
            if found is not None:
                return found
    return None


def _truthy(mapping: Mapping[str, Any], keys: Sequence[str]) -> bool:
    return any(_find(mapping, (key,)) is True for key in keys)


def _explicit_false(mapping: Mapping[str, Any], keys: Sequence[str]) -> bool:
    return any(_find(mapping, (key,)) is False for key in keys)


def _contains_forbidden_body(value: Any) -> bool:
    if isinstance(value, Mapping):
        return any(str(key) in FORBIDDEN_FULL_BODY_KEYS or _contains_forbidden_body(item) for key, item in value.items())
    if isinstance(value, list):
        return any(_contains_forbidden_body(item) for item in value)
    return False


def _sanitize(value: Any) -> Any:
    if isinstance(value, Mapping):
        result: dict[str, Any] = {}
        for key, item in value.items():
            key_text = str(key)
            if key_text in FORBIDDEN_FULL_BODY_KEYS:
                result[key_text] = "[omitted: full prior artifact body is not returned]"
            else:
                result[key_text] = _sanitize(item)
        return result
    if isinstance(value, list):
        return [_sanitize(item) for item in value]
    return _copy(value)


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
    return _mapping(request.get("declared_non_claims"))


def _outcome(basis: Mapping[str, Any], request: Mapping[str, Any], *shortcut_keys: str) -> Any:
    for key in shortcut_keys:
        if key in request:
            return request[key]
    return _find(basis, ("outcome", "result_outcome", "selected_outcome", "selected_result_outcome"))


def _failed_count(basis: Mapping[str, Any], request: Mapping[str, Any], *shortcut_keys: str) -> int | None:
    for key in shortcut_keys:
        if key in request:
            return _to_int(request[key])
    value = _find(basis, ("failed_check_count", "failed_checks_count", "failed_checks", "selected_failed_check_count"))
    return len(value) if isinstance(value, list) else _to_int(value)


def _version(basis: Mapping[str, Any], request: Mapping[str, Any], *shortcut_keys: str) -> Any:
    for key in shortcut_keys:
        if key in request:
            return request[key]
    return _find(basis, ("result_version", "version", "selected_version", "artifact_version"))


def _not_created(
    basis: Mapping[str, Any],
    request: Mapping[str, Any],
    shortcut_key: str,
    positive_keys: Sequence[str],
    negative_keys: Sequence[str],
) -> bool:
    if shortcut_key in request:
        return request[shortcut_key] is False
    if _truthy(basis, positive_keys):
        return False
    return _truthy(basis, negative_keys) or _explicit_false(basis, positive_keys)


def _basis(value: Any, *, path: Any = None, extra: Mapping[str, Any] | None = None) -> dict[str, Any]:
    if isinstance(value, Mapping):
        section = _sanitize(value)
    elif isinstance(value, (str, Path)):
        section = {"basis_reference": str(value), "basis_is_path_reference": True}
    elif value is None:
        section = {}
    else:
        section = {"basis_reference": repr(value), "basis_malformed": True}
    if path:
        section.setdefault("selected_path", str(path))
    if extra:
        for key, item in extra.items():
            if item is not None:
                section[key] = _sanitize(item)
    return section


def _check(
    checks: list[dict[str, Any]],
    name: str,
    passed: bool,
    expected: str,
    actual: Any,
    code: str,
) -> None:
    checks.append(
        {
            "check_name": name,
            "passed": bool(passed),
            "expected_posture": expected,
            "actual_posture": _sanitize(actual),
            "block_code": None if passed else code,
            "failure_code": None if passed else code,
        }
    )


def _basis_declared(request: Mapping[str, Any], key: str) -> bool:
    return isinstance(request.get(key), Mapping) and bool(request.get(key))


def _posture_declared(value: Any, flags: Sequence[str]) -> bool:
    if not _present(value):
        return False
    mapping = _mapping(value)
    if not mapping:
        return True
    if mapping.get("declared") is False or mapping.get("posture_declared") is False:
        return False
    return (
        mapping.get("declared") is True
        or mapping.get("posture_declared") is True
        or mapping.get("basis_remains_basis_only") is True
        or _truthy(mapping, flags)
    )


def _reference_shaped(request: Mapping[str, Any]) -> bool:
    posture = _mapping(request.get("reference_shaped_input_posture"))
    if posture.get("reference_shaped_input_posture_declared") is True or posture.get("reference_shaped_basis_required") is True:
        return True
    basis_keys = (
        "selected_command_output_containment_boundary_basis",
        "selected_command_output_containment_boundary_terminal_summary_basis",
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
    mappings = [_mapping(request.get(key)) for key in basis_keys if isinstance(request.get(key), Mapping)]
    return bool(mappings) and all(
        _truthy(
            basis,
            (
                "reference_shaped_basis",
                "basis_remains_reference_shaped",
                "basis_reference_shape_preserved",
                "basis_remains_basis_only",
            ),
        )
        for basis in mappings
    )


def _lineage_as_current_execution(lineage: Mapping[str, Any]) -> bool:
    return _truthy(
        lineage,
        (
            "older_command_execution_boundary_lineage_treated_as_current_execution",
            "lineage_basis_treated_as_current_execution",
            "current_execution",
            "command_execution_performed",
        ),
    )


def _first_true_code(values: Sequence[Mapping[str, Any]], pairs: Sequence[tuple[str, str]]) -> str | None:
    for value in values:
        for key, code in pairs:
            if _truthy(value, (key,)):
                return code
    return None


COLLAPSE_BLOCKS = (
    ("containment_treated_as_output", "CONTAINMENT_TREATED_AS_OUTPUT"),
    ("command_output_containment_treated_as_output", "CONTAINMENT_TREATED_AS_OUTPUT"),
    ("containment_treated_as_output_capture", "CONTAINMENT_TREATED_AS_OUTPUT_CAPTURE"),
    ("containment_treated_as_output_report_artifact", "CONTAINMENT_TREATED_AS_OUTPUT_REPORT_ARTIFACT"),
    ("containment_treated_as_result", "CONTAINMENT_TREATED_AS_RESULT"),
    ("containment_treated_as_success", "CONTAINMENT_TREATED_AS_SUCCESS"),
    ("command_output_created", "COMMAND_OUTPUT_CREATED"),
    ("output_created", "COMMAND_OUTPUT_CREATED"),
    ("output_capture_created", "OUTPUT_CAPTURE_CREATED"),
    ("command_output_report_artifact_created", "COMMAND_OUTPUT_REPORT_ARTIFACT_CREATED"),
    ("command_result_created", "COMMAND_RESULT_CREATED"),
    ("command_success_created", "COMMAND_SUCCESS_CREATED"),
    ("command_output_became_source", "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
    ("command_output_treated_as_source", "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
    ("command_result_became_authority", "COMMAND_RESULT_TREATED_AS_AUTHORITY"),
    ("command_result_treated_as_authority", "COMMAND_RESULT_TREATED_AS_AUTHORITY"),
    ("command_success_created_currentness", "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
    ("command_success_treated_as_currentness", "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
    ("command_success_claimed_final_completion", "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
    ("command_success_treated_as_final_completion", "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
    ("authorization_token_reused", "AUTHORIZATION_TOKEN_REUSED"),
    ("consumed_request_reopened", "CONSUMED_REQUEST_REOPENED"),
    ("prior_artifacts_mutated", "ARTIFACTS_MUTATED"),
    ("artifacts_mutated", "ARTIFACTS_MUTATED"),
    ("deployment_created", "DEPLOYMENT_CREATED"),
    ("runtime_hosting_created", "RUNTIME_HOSTING_CREATED"),
    ("public_release_created", "PUBLIC_RELEASE_CREATED"),
    ("operation_permission_created", "OPERATION_CREATED"),
    ("operation_created", "OPERATION_CREATED"),
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

TRACE_OVERREAD_BLOCKS = (
    ("execution_trace_treated_as_output", "EXECUTION_TRACE_TREATED_AS_OUTPUT"),
    ("execution_trace_treated_as_result", "EXECUTION_TRACE_TREATED_AS_RESULT"),
    ("execution_trace_treated_as_success", "EXECUTION_TRACE_TREATED_AS_SUCCESS"),
    ("execution_trace_treated_as_source", "EXECUTION_TRACE_TREATED_AS_SOURCE"),
    ("execution_trace_treated_as_authority", "EXECUTION_TRACE_TREATED_AS_AUTHORITY"),
)


def _build_checks(request: Mapping[str, Any], malformed: bool = False) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    if malformed:
        _check(
            checks,
            "declared command output containment request mapping",
            False,
            "request is a mapping",
            "malformed",
            "DECLARED_COMMAND_OUTPUT_CONTAINMENT_REQUEST_MALFORMED",
        )
        return checks

    boundary = _mapping(request.get("selected_command_output_containment_boundary_basis"))
    execution = _mapping(request.get("selected_post_invocation_command_execution_basis"))
    consumed = _mapping(request.get("selected_consumed_request_basis"))
    v2 = _mapping(request.get("selected_v2_admitted_request_basis"))
    v1 = _mapping(request.get("selected_v1_predecessor_failure_basis"))
    lineage = _mapping(request.get("selected_older_command_execution_boundary_lineage_basis"))
    non_claims = _declared_non_claims(request)

    _check(
        checks,
        "command output containment question declared",
        isinstance(request.get("command_output_containment_question"), str)
        and bool(str(request.get("command_output_containment_question")).strip()),
        "question declared",
        request.get("command_output_containment_question"),
        "COMMAND_OUTPUT_CONTAINMENT_QUESTION_UNDECLARED",
    )
    _check(
        checks,
        "command output containment intent supported",
        request.get("command_output_containment_intent") in SUPPORTED_INTENTS,
        "supported intent",
        request.get("command_output_containment_intent"),
        "COMMAND_OUTPUT_CONTAINMENT_INTENT_UNSUPPORTED",
    )
    _check(
        checks,
        "command output containment boundary terminal summary basis declared",
        _present(request.get("selected_command_output_containment_boundary_terminal_summary_basis")),
        "boundary terminal summary basis declared",
        request.get("selected_command_output_containment_boundary_terminal_summary_basis"),
        "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_BASIS_MISSING",
    )
    _check(
        checks,
        "command output containment boundary live artifact basis declared",
        _basis_declared(request, "selected_command_output_containment_boundary_basis"),
        "boundary live artifact basis declared",
        request.get("selected_command_output_containment_boundary_basis"),
        "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_BASIS_MISSING",
    )
    _check(
        checks,
        "command output containment boundary outcome recorded",
        _outcome(boundary, request, "selected_command_output_containment_boundary_result_outcome")
        == COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_OUTCOME,
        COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_OUTCOME,
        _outcome(boundary, request, "selected_command_output_containment_boundary_result_outcome"),
        "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_NOT_RECORDED",
    )
    _check(
        checks,
        "command output containment boundary failed check count zero",
        _failed_count(boundary, request, "selected_command_output_containment_boundary_failed_check_count") == 0,
        "failed_check_count == 0",
        _failed_count(boundary, request, "selected_command_output_containment_boundary_failed_check_count"),
        "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_FAILED_CHECKS_PRESENT",
    )
    _check(
        checks,
        "command output containment boundary step declared",
        (
            request.get("selected_command_output_containment_boundary_step_declared") is True
            or _truthy(boundary, ("one_future_command_output_containment_step_declared", "one_future_output_containment_step_declared"))
        ),
        "one future output-containment step declared",
        boundary,
        "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_STEP_NOT_DECLARED",
    )
    for name, shortcut, positives, negatives, code in (
        (
            "command output containment boundary output not created",
            "selected_command_output_containment_boundary_output_created",
            ("command_output_created", "output_created"),
            ("command_output_still_not_created", "command_output_not_created", "output_not_created"),
            "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_ALREADY_CREATED_OUTPUT",
        ),
        (
            "command output containment boundary output capture not created",
            "selected_command_output_containment_boundary_output_capture_created",
            ("output_capture_created", "command_output_capture_created"),
            ("output_capture_not_created", "command_output_capture_not_created"),
            "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_ALREADY_CREATED_OUTPUT_CAPTURE",
        ),
        (
            "command output containment boundary output report artifact not created",
            "selected_command_output_containment_boundary_output_report_artifact_created",
            ("command_output_report_artifact_created", "output_report_artifact_created"),
            ("command_output_report_artifact_not_created", "output_report_artifact_not_created"),
            "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_ALREADY_CREATED_OUTPUT_REPORT_ARTIFACT",
        ),
        (
            "command output containment boundary result not created",
            "selected_command_output_containment_boundary_result_created",
            ("command_result_created", "result_created"),
            ("command_result_still_not_created", "command_result_not_created", "result_not_created"),
            "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_ALREADY_CREATED_RESULT",
        ),
        (
            "command output containment boundary success not created",
            "selected_command_output_containment_boundary_success_created",
            ("command_success_created", "success_created"),
            ("command_success_still_not_created", "command_success_not_created", "success_not_created"),
            "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_ALREADY_CREATED_SUCCESS",
        ),
    ):
        _check(checks, name, _not_created(boundary, request, shortcut, positives, negatives), "not created", boundary, code)

    _check(
        checks,
        "post-invocation command execution basis declared",
        _basis_declared(request, "selected_post_invocation_command_execution_basis"),
        "post-invocation execution basis declared",
        request.get("selected_post_invocation_command_execution_basis"),
        "POST_INVOCATION_COMMAND_EXECUTION_BASIS_MISSING",
    )
    _check(
        checks,
        "post-invocation command execution outcome recorded",
        _outcome(execution, request, "selected_post_invocation_command_execution_result_outcome")
        == POST_INVOCATION_COMMAND_EXECUTION_OUTCOME,
        POST_INVOCATION_COMMAND_EXECUTION_OUTCOME,
        _outcome(execution, request, "selected_post_invocation_command_execution_result_outcome"),
        "POST_INVOCATION_COMMAND_EXECUTION_NOT_RECORDED",
    )
    _check(
        checks,
        "post-invocation command execution failed check count zero",
        _failed_count(execution, request, "selected_post_invocation_command_execution_failed_check_count") == 0,
        "failed_check_count == 0",
        _failed_count(execution, request, "selected_post_invocation_command_execution_failed_check_count"),
        "POST_INVOCATION_COMMAND_EXECUTION_FAILED_CHECKS_PRESENT",
    )
    _check(
        checks,
        "post-invocation command execution event recorded",
        request.get("selected_post_invocation_command_execution_event_recorded") is True
        or _truthy(execution, ("bounded_command_execution_event_recorded", "execution_event_recorded", "one_bounded_command_execution_event_recorded")),
        "one bounded execution event recorded",
        execution,
        "POST_INVOCATION_COMMAND_EXECUTION_EVENT_NOT_RECORDED",
    )
    _check(
        checks,
        "post-invocation command execution trace audit-only",
        request.get("selected_post_invocation_command_execution_trace_audit_only") is True
        or _truthy(execution, ("execution_trace_recorded_as_audit_only", "execution_trace_audit_only", "execution_trace_audit_only_preserved")),
        "execution trace is audit-only",
        execution,
        "POST_INVOCATION_COMMAND_EXECUTION_TRACE_NOT_AUDIT_ONLY",
    )

    for name, key, code in (
        ("command invocation basis declared", "selected_command_invocation_basis", "COMMAND_INVOCATION_BASIS_MISSING"),
        ("command execution review basis declared", "selected_command_execution_review_basis", "COMMAND_EXECUTION_REVIEW_BASIS_MISSING"),
        ("request consumption basis declared", "selected_request_consumption_basis", "REQUEST_CONSUMPTION_BASIS_MISSING"),
        ("consumed request basis declared", "selected_consumed_request_basis", "CONSUMED_REQUEST_BASIS_MISSING"),
        ("v2 admitted request basis declared", "selected_v2_admitted_request_basis", "V2_ADMITTED_REQUEST_BASIS_MISSING"),
        ("v1 predecessor failure basis declared", "selected_v1_predecessor_failure_basis", "V1_PREDECESSOR_FAILURE_BASIS_MISSING"),
        ("command report basis declared", "selected_command_report_basis", "COMMAND_REPORT_BASIS_MISSING"),
        ("command implementation boundary basis declared", "selected_command_implementation_boundary_basis", "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING"),
        ("command boundary basis declared", "selected_command_boundary_basis", "COMMAND_BOUNDARY_BASIS_MISSING"),
        ("artifact emission containment basis declared", "selected_artifact_emission_containment_basis", "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING"),
        ("evidence-manifest basis declared", "selected_evidence_manifest_basis", "EVIDENCE_MANIFEST_BASIS_MISSING"),
        ("portable verification basis declared", "selected_portable_verification_basis", "PORTABLE_VERIFICATION_BASIS_MISSING"),
    ):
        _check(checks, name, _basis_declared(request, key), "basis declared", request.get(key), code)

    v2_failed = _failed_count(v2, request, "selected_v2_failed_check_count")
    if v2_failed is not None:
        _check(checks, "v2 admitted request failed check count zero", v2_failed == 0, "failed_check_count == 0", v2_failed, "V2_ADMITTED_REQUEST_FAILED_CHECKS_PRESENT")
    v2_outcome = _outcome(v2, request, "selected_v2_admitted_request_outcome")
    if v2_outcome is not None:
        _check(checks, "v2 admitted request outcome admitted", v2_outcome == V2_ADMITTED_REQUEST_OUTCOME, V2_ADMITTED_REQUEST_OUTCOME, v2_outcome, "V2_ADMITTED_REQUEST_BASIS_MISSING")
    v2_version = _version(v2, request, "selected_v2_admitted_request_version")
    if v2_version is not None:
        _check(checks, "v2 admitted request version 0.2.0", v2_version == V2_ADMITTED_REQUEST_VERSION, V2_ADMITTED_REQUEST_VERSION, v2_version, "V2_ADMITTED_REQUEST_BASIS_MISSING")

    _check(checks, "consumed request token remains closed", _truthy(consumed, ("consumed_request_token_remains_closed", "consumption_token_closed", "consumed_token_closed")), "consumed token closed", consumed, "CONSUMED_REQUEST_REOPENED")
    _check(checks, "consumed request not reopened", not _truthy(consumed, ("consumed_request_reopened", "request_reopened", "token_reopened")) and _truthy(consumed, ("consumed_request_not_reopened", "consumed_request_is_not_reopened", "no_reopen_consumed_request")), "consumed request not reopened", consumed, "CONSUMED_REQUEST_REOPENED")
    _check(checks, "v1 predecessor failure remains visible", _truthy(v1, ("v1_predecessor_failure_remains_visible", "v1_remains_visible_predecessor_failure_evidence", "v1_predecessor_failure_basis_declared")), "v1 failure visible", v1, "V1_PREDECESSOR_FAILURE_BASIS_MISSING")
    _check(checks, "v2 not treated as repairing v1", not (_truthy(v1, ("v2_treated_as_repairing_v1", "v1_repaired")) or _truthy(v2, ("v2_treated_as_repairing_v1", "v1_repaired"))), "v2 does not repair v1", {"v1": v1, "v2": v2}, "V2_TREATED_AS_REPAIRING_V1")
    _check(checks, "v1 failure not hidden", not _truthy(v1, ("v1_hidden", "v1_failure_hidden")), "v1 failure not hidden", v1, "V1_FAILURE_HIDDEN")
    _check(checks, "v1 not claimed passed", not (_truthy(v1, ("v1_claimed_passed", "v1_passed")) or _truthy(v2, ("v1_claimed_passed", "v1_passed", "v2_claims_v1_passed"))), "v1 not claimed passed", {"v1": v1, "v2": v2}, "V1_CLAIMED_PASSED")
    _check(checks, "older command execution boundary lineage basis declared", _basis_declared(request, "selected_older_command_execution_boundary_lineage_basis"), "older lineage basis declared", request.get("selected_older_command_execution_boundary_lineage_basis"), "OLDER_COMMAND_EXECUTION_BOUNDARY_LINEAGE_TREATED_AS_CURRENT_EXECUTION")
    _check(checks, "older command execution boundary lineage basis prior scaffolding only", not _lineage_as_current_execution(lineage), "lineage is prior scaffolding only", lineage, "OLDER_COMMAND_EXECUTION_BOUNDARY_LINEAGE_TREATED_AS_CURRENT_EXECUTION")

    for name, key, code, flags in (
        ("output-containment-only posture declared", "output_containment_only_posture", "OUTPUT_CONTAINMENT_ONLY_POSTURE_MISSING", ("output_containment_only", "command_output_containment_only")),
        ("one-bounded-command-output-containment-event posture declared", "one_bounded_command_output_containment_event_posture", "ONE_BOUNDED_COMMAND_OUTPUT_CONTAINMENT_EVENT_POSTURE_MISSING", ("one_bounded_command_output_containment_event_recorded", "one_bounded_command_output_containment_event")),
        ("command-output-boundary-basis-preserved posture declared", "command_output_boundary_basis_preserved_posture", "COMMAND_OUTPUT_BOUNDARY_BASIS_PRESERVED_POSTURE_MISSING", ("command_output_boundary_basis_preserved", "command_output_containment_boundary_basis_preserved")),
        ("execution-event-preserved posture declared", "execution_event_preserved_posture", "EXECUTION_EVENT_PRESERVED_POSTURE_MISSING", ("recorded_command_execution_event_preserved", "execution_event_preserved")),
        ("execution-trace-audit-only posture declared", "execution_trace_audit_only_posture", "EXECUTION_TRACE_AUDIT_ONLY_POSTURE_MISSING", ("execution_trace_audit_only_preserved", "execution_trace_audit_only")),
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

    scope = _scope_values(request.get("command_output_containment_scope"))
    _check(checks, "command output containment scope supported", bool(scope) and all(value in SUPPORTED_COMMAND_OUTPUT_CONTAINMENT_SCOPE_SET for value in scope), "supported scope", scope, "UNSUPPORTED_COMMAND_OUTPUT_CONTAINMENT_SCOPE")
    _check(checks, "reference-shaped input posture preserved", _reference_shaped(request), "reference-shaped selected basis", "reference-shaped" if _reference_shaped(request) else "not reference-shaped", "FULL_PRIOR_ARTIFACT_BODY_EMITTED")

    trace_code = _first_true_code((request, non_claims, execution), TRACE_OVERREAD_BLOCKS)
    _check(checks, "execution trace not output result success source authority", trace_code is None, "execution trace is not output/result/success/source/authority", trace_code, trace_code or "EXECUTION_TRACE_TREATED_AS_OUTPUT")
    collapse_code = _first_true_code((request, non_claims, boundary, execution, consumed, v2, v1, lineage), COLLAPSE_BLOCKS)
    replay_merge = any(_truthy(_mapping(value), ("mutation_performed", "replay_performed", "merge_performed")) for value in (request, non_claims))
    _check(checks, "collapse flags absent", collapse_code is None and not replay_merge, "no output/capture/report/result/success/authority/currentness/follow-on collapse", collapse_code or ("mutation/replay/merge" if replay_merge else None), collapse_code or "MUTATION_REPLAY_OR_MERGE_DETECTED")
    _check(checks, "raw full prior artifact body not emitted", not _contains_forbidden_body(request), "no raw full prior artifact body", "forbidden full-body key present" if _contains_forbidden_body(request) else "contained", "FULL_PRIOR_ARTIFACT_BODY_EMITTED")

    missing_non_claim = next((key for key in REQUIRED_FALSE_NON_CLAIMS if key not in non_claims or non_claims.get(key) is not False), None)
    _check(checks, "non-claims remain false", missing_non_claim is None, "required non-claims explicit and false", missing_non_claim, "NON_CLAIM_MISSING_OR_FLIPPED")
    return checks


def _counts(checks: Sequence[Mapping[str, Any]]) -> tuple[int, int]:
    passed = sum(1 for check in checks if check.get("passed") is True)
    return passed, len(checks) - passed


def _first_failed(checks: Sequence[Mapping[str, Any]]) -> Mapping[str, Any] | None:
    return next((check for check in checks if not check.get("passed")), None)


def _select_outcome(
    request: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    forced_block: str | None = None,
) -> tuple[str, str | None, str | None]:
    if forced_block:
        return OUTCOME_BLOCKED, forced_block, forced_block
    intent = request.get("command_output_containment_intent")
    if intent == INTENT_BLOCK:
        return OUTCOME_BLOCKED, "COMMAND_OUTPUT_CONTAINMENT_BLOCKED_BY_REQUEST", str(request.get("block_reason") or "blocked by request intent")
    if intent not in SUPPORTED_INTENTS:
        return OUTCOME_BLOCKED, "COMMAND_OUTPUT_CONTAINMENT_INTENT_UNSUPPORTED", "unsupported command output containment intent"
    requested = request.get("requested_command_output_containment_outcome", OUTCOME_RECORDED)
    if requested == OUTCOME_BLOCKED:
        return OUTCOME_BLOCKED, "COMMAND_OUTPUT_CONTAINMENT_BLOCKED_BY_REQUEST", str(request.get("block_reason") or "blocked by requested outcome")
    if requested not in OUTCOME_FAMILY:
        return OUTCOME_BLOCKED, "DECLARED_COMMAND_OUTPUT_CONTAINMENT_REQUEST_MALFORMED", "unsupported requested outcome"
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
            "command_output_containment_not_recorded": outcome == OUTCOME_NOT_RECORDED,
            "command_output_containment_requires_additional_basis": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "command_output_containment_blocked": outcome == OUTCOME_BLOCKED,
            "command_output_containment_is_not_command_output": True,
            "command_output_containment_is_not_output_capture": True,
            "command_output_containment_is_not_output_report_artifact": True,
            "command_output_containment_is_not_command_result": True,
            "command_output_containment_is_not_command_success": True,
            "containment_is_not_output": True,
            "containment_is_not_output_capture": True,
            "containment_is_not_output_report_artifact": True,
            "containment_is_not_result": True,
            "containment_is_not_success": True,
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
        "containment_is_output",
        "containment_is_output_capture",
        "containment_is_output_report_artifact",
        "containment_is_result",
        "containment_is_success",
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
    return {f"command_output_containment_does_not_mean_{name}": True for name in names}


def _open_items() -> dict[str, Any]:
    return {
        "open_items": [
            "command_output_containment_test",
            "command_output_containment_live_artifact",
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


def _metadata(request: Mapping[str, Any], outcome: str) -> dict[str, Any]:
    request_id = str(request.get("command_output_containment_request_id") or "undeclared")
    return {
        "portable_source_body_verification_command_output_containment_result_id": (
            f"{request_id}__portable_source_body_verification_command_output_containment_result"
        ),
        "portable_source_body_verification_command_output_containment_result_type": RESULT_TYPE,
        "portable_source_body_verification_command_output_containment_result_version": RESULT_VERSION,
        "generated_at": _now(),
        "resolver_module": RESOLVER_MODULE,
        "command_output_containment_request_id": request_id,
        "naming_containment": {
            "short_resolver_filename_used_intentionally": True,
            "short_filename_does_not_erase_upstream_lineage": True,
            "full_upstream_lineage_preserved_in_selected_basis": True,
        },
        "lineage_posture": {
            "downstream_of_recorded_command_output_containment_boundary": True,
            "downstream_of_recorded_post_invocation_command_execution": True,
            "older_command_execution_boundary_surfaces_remain_lineage_only": True,
        },
        "requested_outcome": request.get("requested_command_output_containment_outcome"),
        "outcome": outcome,
    }


def _scope_section(scope: Any, outcome: str) -> dict[str, Any]:
    values = _scope_values(scope)
    unsupported = [value for value in values if value not in SUPPORTED_COMMAND_OUTPUT_CONTAINMENT_SCOPE_SET]
    return {
        "selected_scope_values": values,
        "supported_scope_values": list(SUPPORTED_COMMAND_OUTPUT_CONTAINMENT_SCOPE),
        "unsupported_scope_values": unsupported,
        "all_selected_scope_values_supported": bool(values) and not unsupported,
        "command_output_containment_only": "COMMAND_OUTPUT_CONTAINMENT_ONLY" in values,
        "one_bounded_command_output_containment_event_recorded": outcome == OUTCOME_RECORDED,
        "command_output_containment_boundary_basis_preserved": outcome == OUTCOME_RECORDED,
        "recorded_command_execution_event_preserved": outcome == OUTCOME_RECORDED,
        "execution_trace_audit_only_preserved": True,
        "command_output_not_created": True,
        "output_capture_not_created": True,
        "command_output_report_artifact_not_created": True,
        "command_result_not_created": True,
        "command_success_not_created": True,
        "containment_is_not_output_capture_report_result_success": True,
        "execution_trace_is_not_output_result_success_source_authority": True,
        "authorization_token_reuse_blocked": True,
        "consumed_request_token_remains_closed": True,
        "consumed_request_not_reopened": True,
        "reference_shaped_basis_required": True,
        "full_prior_artifact_body_not_emitted": True,
    }


def build_portable_source_body_verification_command_output_containment_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Build a bounded summary for a command output containment result."""

    statement = _mapping(result.get("command_output_containment_statement"))
    block = _mapping(result.get("block"))
    metadata = _mapping(result.get("portable_source_body_verification_command_output_containment_metadata"))
    question = _mapping(result.get("declared_command_output_containment_question"))
    checks = [check for check in result.get("command_output_containment_checks", []) if isinstance(check, Mapping)]
    passed, failed = _counts(checks)
    non_claims = _mapping(result.get("non_claims"))
    boundary = _mapping(result.get("selected_command_output_containment_boundary_basis"))
    execution = _mapping(result.get("selected_post_invocation_command_execution_basis"))
    v2 = _mapping(result.get("selected_v2_admitted_request_basis"))
    lineage = _mapping(result.get("selected_older_command_execution_boundary_lineage_basis"))
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("code"),
        "block_reason": block.get("reason"),
        "request_id": metadata.get("command_output_containment_request_id"),
        "question": question.get("question"),
        "intent": question.get("intent"),
        "passed_check_count": passed,
        "failed_check_count": failed,
        "command_output_containment_recorded": statement.get("command_output_containment_recorded") is True,
        "bounded_output_containment_event_recorded": statement.get("bounded_command_output_containment_event_recorded") is True,
        "command_output_boundary_basis_preserved": statement.get("command_output_boundary_basis_preserved") is True,
        "recorded_command_execution_event_preserved": statement.get("recorded_command_execution_event_preserved") is True,
        "execution_trace_audit_only_preserved": statement.get("execution_trace_audit_only_preserved") is True,
        "command_output_still_not_created": statement.get("command_output_still_not_created") is True,
        "output_capture_not_created": statement.get("output_capture_not_created") is True,
        "output_report_artifact_not_created": statement.get("command_output_report_artifact_not_created") is True,
        "command_result_still_not_created": statement.get("command_result_still_not_created") is True,
        "command_success_still_not_created": statement.get("command_success_still_not_created") is True,
        "selected_output_containment_boundary_outcome": _find(boundary, ("outcome", "result_outcome", "selected_result_outcome")),
        "selected_output_containment_boundary_failed_check_count": _find(boundary, ("failed_check_count", "selected_failed_check_count")),
        "selected_post_invocation_execution_outcome": _find(execution, ("outcome", "result_outcome", "selected_result_outcome")),
        "selected_post_invocation_execution_failed_check_count": _find(execution, ("failed_check_count", "selected_failed_check_count")),
        "selected_v2_admitted_request_outcome": _find(v2, ("outcome", "result_outcome", "selected_outcome")),
        "selected_v2_admitted_request_version": _find(v2, ("result_version", "version", "selected_version")),
        "selected_v2_admitted_request_failed_check_count": _find(v2, ("failed_check_count", "selected_failed_check_count")),
        "containment_not_output_capture_output_report_result_success": all(
            statement.get(key) is True
            for key in ("containment_is_not_output", "containment_is_not_output_capture", "containment_is_not_output_report_artifact", "containment_is_not_result", "containment_is_not_success")
        ),
        "execution_trace_not_output_result_success_source_authority": all(
            statement.get(key) is True
            for key in ("execution_trace_is_not_command_output", "execution_trace_is_not_command_result", "execution_trace_is_not_command_success", "execution_trace_is_not_source", "execution_trace_is_not_authority")
        ),
        "output_not_source": statement.get("output_is_not_source") is True,
        "result_not_authority": statement.get("result_is_not_authority") is True,
        "success_not_currentness": statement.get("success_is_not_currentness") is True,
        "success_not_final_completion": statement.get("success_is_not_final_completion") is True,
        "older_command_execution_boundary_lineage_not_treated_as_current_execution": not _lineage_as_current_execution(lineage),
        "no_raw_full_prior_artifact_body": non_claims.get("raw_full_prior_artifact_body_returned") is False,
        "no_artifact_mutation": non_claims.get("prior_artifacts_mutated") is False,
        "no_deployment_runtime_public_release": all(non_claims.get(key) is False for key in ("deployment_created", "runtime_hosting_created", "public_release_created")),
        "no_operation_public_readiness_final_completion": all(non_claims.get(key) is False for key in ("operation_permission_created", "public_launch_readiness_created", "final_completion_claimed")),
        "no_continuation_publication_reusable_follow_on": all(non_claims.get(key) is False for key in ("continuation_authorized", "publication_flow_opened", "reusable_permission_created", "follow_on_work_authorized")),
        "key_non_claims": _sanitize(non_claims),
    }


def _build_result(
    request: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    outcome: str,
    block_code: str | None,
    block_reason: str | None,
    request_path: str | None = None,
) -> dict[str, Any]:
    metadata = _metadata(request, outcome)
    if request_path:
        metadata["declared_command_output_containment_request_path"] = request_path
    statement = _statement(outcome)
    additional_basis_required = {
        "requires_additional_basis": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "additional_basis_context": _sanitize(request.get("additional_basis_context") or {}),
        "missing_basis_not_scheduled": True,
        "missing_basis_not_authorized": True,
        "missing_basis_not_executed": True,
    }
    not_recorded_basis = {
        "not_recorded": outcome == OUTCOME_NOT_RECORDED,
        "not_recorded_basis": _sanitize(request.get("not_recorded_basis") or {}),
        "not_recorded_does_not_mutate": True,
        "not_recorded_does_not_repair": True,
        "not_recorded_does_not_authorize_next_work": True,
    }
    result = {
        "portable_source_body_verification_command_output_containment_metadata": metadata,
        "declared_command_output_containment_question": {
            "question": request.get("command_output_containment_question"),
            "expected_question": CORE_COMMAND_OUTPUT_CONTAINMENT_QUESTION,
            "intent": request.get("command_output_containment_intent"),
            "command_output_containment_is_not_command_output": True,
            "command_output_containment_is_not_output_capture": True,
            "command_output_containment_is_not_output_report_artifact": True,
            "command_output_containment_is_not_command_result": True,
            "command_output_containment_is_not_command_success": True,
        },
        "selected_command_output_containment_boundary_basis": _basis(
            request.get("selected_command_output_containment_boundary_basis"),
            path=request.get("selected_command_output_containment_boundary_result_path"),
            extra={
                "selected_result_id": request.get("selected_command_output_containment_boundary_result_id"),
                "selected_result_outcome": request.get("selected_command_output_containment_boundary_result_outcome"),
                "selected_failed_check_count": request.get("selected_command_output_containment_boundary_failed_check_count"),
                "selected_step_declared": request.get("selected_command_output_containment_boundary_step_declared"),
                "boundary_basis_remains_boundary_basis_only": True,
            },
        ),
        "selected_command_output_containment_boundary_terminal_summary_basis": _basis(
            request.get("selected_command_output_containment_boundary_terminal_summary_basis"),
            path=request.get("selected_command_output_containment_boundary_terminal_summary_path"),
            extra={"terminal_summary_remains_readability_basis_only": True},
        ),
        "selected_post_invocation_command_execution_basis": _basis(
            request.get("selected_post_invocation_command_execution_basis"),
            path=request.get("selected_post_invocation_command_execution_result_path"),
            extra={
                "selected_result_id": request.get("selected_post_invocation_command_execution_result_id"),
                "selected_result_outcome": request.get("selected_post_invocation_command_execution_result_outcome"),
                "selected_failed_check_count": request.get("selected_post_invocation_command_execution_failed_check_count"),
                "selected_execution_event_recorded": request.get("selected_post_invocation_command_execution_event_recorded"),
                "selected_execution_trace_audit_only": request.get("selected_post_invocation_command_execution_trace_audit_only"),
                "execution_trace_remains_audit_only": True,
            },
        ),
        "selected_post_invocation_command_execution_terminal_summary_basis": _basis(request.get("selected_post_invocation_command_execution_terminal_summary_basis"), path=request.get("selected_post_invocation_command_execution_terminal_summary_path"), extra={"terminal_summary_remains_readability_basis_only": True}),
        "selected_post_invocation_command_execution_boundary_basis": _basis(request.get("selected_post_invocation_command_execution_boundary_basis"), path=request.get("selected_post_invocation_command_execution_boundary_result_path"), extra={"post_invocation_execution_boundary_basis_remains_boundary_basis_only": True}),
        "selected_command_invocation_basis": _basis(request.get("selected_command_invocation_basis"), path=request.get("selected_command_invocation_result_path"), extra={"command_invocation_basis_remains_invocation_basis_only": True}),
        "selected_command_execution_review_basis": _basis(request.get("selected_command_execution_review_basis"), path=request.get("selected_command_execution_review_result_path"), extra={"review_basis_remains_review_basis_only": True}),
        "selected_request_consumption_basis": _basis(request.get("selected_request_consumption_basis"), path=request.get("selected_request_consumption_result_path"), extra={"request_consumption_basis_only": True}),
        "selected_consumed_request_basis": _basis(request.get("selected_consumed_request_basis"), extra={"consumed_request_token_remains_closed": True, "consumed_request_not_reopened": True}),
        "selected_v2_admitted_request_basis": _basis(request.get("selected_v2_admitted_request_basis"), path=request.get("selected_v2_admitted_request_artifact_path"), extra={"selected_outcome": request.get("selected_v2_admitted_request_outcome"), "selected_version": request.get("selected_v2_admitted_request_version"), "selected_failed_check_count": request.get("selected_v2_failed_check_count"), "v2_remains_lineage_evidence_only": True, "v2_does_not_claim_v1_passed": True}),
        "selected_v1_predecessor_failure_basis": _basis(request.get("selected_v1_predecessor_failure_basis"), path=request.get("selected_v1_predecessor_artifact_path"), extra={"v1_predecessor_failure_remains_visible": True, "v1_is_not_repaired": True, "v1_is_not_hidden": True, "v1_is_not_claimed_passed": True}),
        "selected_older_command_execution_boundary_lineage_basis": _basis(request.get("selected_older_command_execution_boundary_lineage_basis"), path=request.get("selected_older_command_execution_boundary_lineage_result_path"), extra={"older_command_execution_boundary_surfaces_remain_lineage_only": True, "lineage_basis_is_not_current_execution": True}),
        "selected_command_report_basis": _basis(request.get("selected_command_report_basis"), path=request.get("selected_command_report_path")),
        "selected_command_implementation_boundary_basis": _basis(request.get("selected_command_implementation_boundary_basis"), path=request.get("selected_command_implementation_boundary_result_path")),
        "selected_command_boundary_basis": _basis(request.get("selected_command_boundary_basis"), path=request.get("selected_command_boundary_result_path")),
        "selected_artifact_emission_containment_basis": _basis(request.get("selected_artifact_emission_containment_basis"), path=request.get("selected_artifact_emission_containment_result_path")),
        "selected_evidence_manifest_basis": _basis(request.get("selected_evidence_manifest_basis"), path=request.get("selected_evidence_manifest_result_path")),
        "selected_portable_verification_basis": _basis(request.get("selected_portable_verification_basis"), path=request.get("selected_portable_verification_result_path")),
        "output_containment_only_posture": _basis(request.get("output_containment_only_posture"), extra={"output_containment_only": True, "containment_is_not_output_capture_report_result_success": True}),
        "one_bounded_command_output_containment_event_posture": _basis(request.get("one_bounded_command_output_containment_event_posture"), extra={"one_bounded_command_output_containment_event_recorded": outcome == OUTCOME_RECORDED}),
        "command_output_boundary_basis_preserved_posture": _basis(request.get("command_output_boundary_basis_preserved_posture"), extra={"command_output_boundary_basis_preserved": outcome == OUTCOME_RECORDED}),
        "execution_event_preserved_posture": _basis(request.get("execution_event_preserved_posture"), extra={"recorded_command_execution_event_preserved": outcome == OUTCOME_RECORDED}),
        "execution_trace_audit_only_posture": _basis(request.get("execution_trace_audit_only_posture"), extra={"execution_trace_audit_only_preserved": outcome == OUTCOME_RECORDED}),
        "no_command_output_posture": _basis(request.get("no_command_output_posture"), extra={"command_output_created": False}),
        "no_output_capture_posture": _basis(request.get("no_output_capture_posture"), extra={"output_capture_created": False}),
        "no_output_report_artifact_posture": _basis(request.get("no_output_report_artifact_posture"), extra={"command_output_report_artifact_created": False}),
        "no_command_result_posture": _basis(request.get("no_command_result_posture"), extra={"command_result_created": False}),
        "no_command_success_posture": _basis(request.get("no_command_success_posture"), extra={"command_success_created": False}),
        "no_output_as_source_posture": _basis(request.get("no_output_as_source_posture"), extra={"command_output_became_source": False}),
        "no_result_as_authority_posture": _basis(request.get("no_result_as_authority_posture"), extra={"command_result_became_authority": False}),
        "no_success_as_currentness_posture": _basis(request.get("no_success_as_currentness_posture"), extra={"command_success_created_currentness": False}),
        "no_final_completion_posture": _basis(request.get("no_final_completion_posture"), extra={"command_success_claimed_final_completion": False, "final_completion_claimed": False}),
        "authorization_token_reuse_blocked_posture": _basis(request.get("authorization_token_reuse_blocked_posture"), extra={"authorization_token_reuse_blocked": True, "authorization_token_reused": False}),
        "consumed_token_closed_posture": _basis(request.get("consumed_token_closed_posture"), extra={"consumed_request_token_remains_closed": True}),
        "no_reopen_consumed_request_posture": _basis(request.get("no_reopen_consumed_request_posture"), extra={"consumed_request_reopened": False}),
        "returned_result_containment_posture": _basis(request.get("returned_result_containment_posture"), extra={"returned_result_containment_preserved": True, "raw_full_prior_artifact_body_returned": False}),
        "command_output_containment_scope": _scope_section(request.get("command_output_containment_scope"), outcome),
        "command_output_containment_checks": _sanitize(list(checks)),
        "command_output_containment_statement": statement,
        "command_output_containment_non_meaning": _non_meaning(),
        "additional_basis_required": additional_basis_required,
        "not_recorded_basis": not_recorded_basis,
        "what_remains_open": _open_items(),
        "non_claims": _default_non_claims(),
        "outcome": outcome,
        "block": {"code": block_code, "reason": block_reason},
    }
    result["portable_source_body_verification_command_output_containment_summary"] = build_portable_source_body_verification_command_output_containment_summary(result)
    return result


def resolve_portable_source_body_verification_command_output_containment(
    declared_command_output_containment_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded command output containment request."""

    if declared_command_output_containment_request is None:
        request: Mapping[str, Any] = {}
        checks = _build_checks(request)
        outcome, code, reason = _select_outcome(request, checks, "COMMAND_OUTPUT_CONTAINMENT_QUESTION_UNDECLARED")
        return _build_result(request, checks, outcome, code, reason)
    if not isinstance(declared_command_output_containment_request, Mapping):
        request = {}
        checks = _build_checks(request, malformed=True)
        outcome, code, reason = _select_outcome(request, checks, "DECLARED_COMMAND_OUTPUT_CONTAINMENT_REQUEST_MALFORMED")
        return _build_result(request, checks, outcome, code, reason)
    request = _copy(declared_command_output_containment_request)
    checks = _build_checks(request)
    outcome, code, reason = _select_outcome(request, checks)
    return _build_result(request, checks, outcome, code, reason)


def resolve_portable_source_body_verification_command_output_containment_from_path(
    declared_command_output_containment_request_path: Path | str,
) -> dict[str, Any]:
    """Resolve one command output containment request from a JSON object path."""

    path = Path(declared_command_output_containment_request_path)
    try:
        loaded = json.loads(path.read_text(encoding="utf-8"))
    except OSError:
        request = {"command_output_containment_request_id": "unreadable_path"}
        checks = _build_checks(request)
        outcome, code, reason = _select_outcome(request, checks, "DECLARED_COMMAND_OUTPUT_CONTAINMENT_REQUEST_UNREADABLE")
        return _build_result(request, checks, outcome, code, reason, request_path=str(path))
    except json.JSONDecodeError:
        request = {"command_output_containment_request_id": "malformed_json"}
        checks = _build_checks(request)
        outcome, code, reason = _select_outcome(request, checks, "DECLARED_COMMAND_OUTPUT_CONTAINMENT_REQUEST_MALFORMED")
        return _build_result(request, checks, outcome, code, reason, request_path=str(path))
    if not isinstance(loaded, Mapping):
        request = {"command_output_containment_request_id": "non_object_json"}
        checks = _build_checks(request, malformed=True)
        outcome, code, reason = _select_outcome(request, checks, "DECLARED_COMMAND_OUTPUT_CONTAINMENT_REQUEST_MALFORMED")
        return _build_result(request, checks, outcome, code, reason, request_path=str(path))
    request = _copy(loaded)
    checks = _build_checks(request)
    outcome, code, reason = _select_outcome(request, checks)
    return _build_result(request, checks, outcome, code, reason, request_path=str(path))


def _safe_component(value: Any, fallback: str) -> str:
    text = str(value or "").strip() or fallback
    chars = [char if char.isalnum() or char in {"-", "_", "."} else "_" for char in text]
    return "".join(chars).strip("._") or fallback


def _deduplicated_output_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 1000000):
        candidate = path.parent / f"{path.stem}_{index:03d}{path.suffix}"
        if not candidate.exists():
            return candidate
    raise PortableSourceBodyVerificationCommandOutputContainmentError(
        "unable to allocate non-overwriting command output containment result path"
    )


def write_portable_source_body_verification_command_output_containment_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a bounded command output containment result JSON additively."""

    if output_path is None:
        metadata = _mapping(result.get("portable_source_body_verification_command_output_containment_metadata"))
        request_id = metadata.get("command_output_containment_request_id") or "undeclared_command_output_containment_request"
        filename = (
            f"{_safe_component(request_id, 'undeclared_command_output_containment_request')}"
            "__portable_source_body_verification_command_output_containment_result.json"
        )
        path = PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_CONTAINMENT_ROOT / filename
    else:
        path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    final_path = _deduplicated_output_path(path)
    final_path.write_text(json.dumps(_sanitize(dict(result)), indent=2, sort_keys=True, ensure_ascii=True) + "\n", encoding="utf-8")
    return final_path


def build_declared_portable_source_body_verification_command_output_containment_request(
    command_output_containment_request_id: str,
    command_output_containment_question: str,
    selected_command_output_containment_boundary_basis: Mapping[str, Any] | str,
    selected_command_output_containment_boundary_terminal_summary_basis: Mapping[str, Any] | str,
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
    output_containment_only_posture: Mapping[str, Any] | str,
    one_bounded_command_output_containment_event_posture: Mapping[str, Any] | str,
    command_output_boundary_basis_preserved_posture: Mapping[str, Any] | str,
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
    command_output_containment_scope: Sequence[str] | Mapping[str, Any],
    command_output_containment_intent: str = INTENT_RECORD,
    **optional_fields: Any,
) -> dict[str, Any]:
    """Build a declared containment request with explicit false non-claims."""

    request = {
        "command_output_containment_request_id": command_output_containment_request_id,
        "command_output_containment_question": command_output_containment_question,
        "command_output_containment_intent": command_output_containment_intent,
        "selected_command_output_containment_boundary_basis": _copy(selected_command_output_containment_boundary_basis),
        "selected_command_output_containment_boundary_terminal_summary_basis": _copy(selected_command_output_containment_boundary_terminal_summary_basis),
        "selected_post_invocation_command_execution_basis": _copy(selected_post_invocation_command_execution_basis),
        "selected_post_invocation_command_execution_terminal_summary_basis": _copy(selected_post_invocation_command_execution_terminal_summary_basis),
        "selected_post_invocation_command_execution_boundary_basis": _copy(selected_post_invocation_command_execution_boundary_basis),
        "selected_command_invocation_basis": _copy(selected_command_invocation_basis),
        "selected_command_execution_review_basis": _copy(selected_command_execution_review_basis),
        "selected_request_consumption_basis": _copy(selected_request_consumption_basis),
        "selected_consumed_request_basis": _copy(selected_consumed_request_basis),
        "selected_v2_admitted_request_basis": _copy(selected_v2_admitted_request_basis),
        "selected_v1_predecessor_failure_basis": _copy(selected_v1_predecessor_failure_basis),
        "selected_older_command_execution_boundary_lineage_basis": _copy(selected_older_command_execution_boundary_lineage_basis),
        "selected_command_report_basis": _copy(selected_command_report_basis),
        "selected_command_implementation_boundary_basis": _copy(selected_command_implementation_boundary_basis),
        "selected_command_boundary_basis": _copy(selected_command_boundary_basis),
        "selected_artifact_emission_containment_basis": _copy(selected_artifact_emission_containment_basis),
        "selected_evidence_manifest_basis": _copy(selected_evidence_manifest_basis),
        "selected_portable_verification_basis": _copy(selected_portable_verification_basis),
        "output_containment_only_posture": _copy(output_containment_only_posture),
        "one_bounded_command_output_containment_event_posture": _copy(one_bounded_command_output_containment_event_posture),
        "command_output_boundary_basis_preserved_posture": _copy(command_output_boundary_basis_preserved_posture),
        "execution_event_preserved_posture": _copy(execution_event_preserved_posture),
        "execution_trace_audit_only_posture": _copy(execution_trace_audit_only_posture),
        "no_command_output_posture": _copy(no_command_output_posture),
        "no_output_capture_posture": _copy(no_output_capture_posture),
        "no_output_report_artifact_posture": _copy(no_output_report_artifact_posture),
        "no_command_result_posture": _copy(no_command_result_posture),
        "no_command_success_posture": _copy(no_command_success_posture),
        "no_output_as_source_posture": _copy(no_output_as_source_posture),
        "no_result_as_authority_posture": _copy(no_result_as_authority_posture),
        "no_success_as_currentness_posture": _copy(no_success_as_currentness_posture),
        "no_final_completion_posture": _copy(no_final_completion_posture),
        "authorization_token_reuse_blocked_posture": _copy(authorization_token_reuse_blocked_posture),
        "consumed_token_closed_posture": _copy(consumed_token_closed_posture),
        "no_reopen_consumed_request_posture": _copy(no_reopen_consumed_request_posture),
        "returned_result_containment_posture": _copy(returned_result_containment_posture),
        "command_output_containment_scope": _copy(command_output_containment_scope),
        "requested_command_output_containment_outcome": optional_fields.pop("requested_command_output_containment_outcome", OUTCOME_RECORDED),
        "declared_non_claims": _default_non_claims(),
    }
    for key, value in optional_fields.items():
        if value is not None:
            request[key] = _copy(value)
    return request
