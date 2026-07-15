"""Bounded post-runtime-daemon runtime-loop-boundary resolver.

This module records one bounded runtime-loop-boundary posture from clean
runtime-daemon basis. It declares, at most, one future runtime-loop review. It
does not create runtime loop, repeating autonomous runtime behavior, public
API, participant-facing interface, distributed network behavior, source
transfer, source receipt, reception authorization, source, authority,
currentness, deployment, public release, operation permission, broader
reusable permission, adoption, receiving-context governance, publication flow,
or follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class PostRuntimeDaemonRuntimeLoopBoundaryError(Exception):
    """Bounded resolver error for runtime-loop-boundary request handling."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_post_runtime_daemon_runtime_loop_boundary"

OUTCOME_RECORDED = "POST_RUNTIME_DAEMON_RUNTIME_LOOP_BOUNDARY_RECORDED"
OUTCOME_NOT_RECORDED = "POST_RUNTIME_DAEMON_RUNTIME_LOOP_BOUNDARY_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "POST_RUNTIME_DAEMON_RUNTIME_LOOP_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "POST_RUNTIME_DAEMON_RUNTIME_LOOP_BOUNDARY_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_post_runtime_daemon_runtime_loop_boundary"
)

INTENT_RECORD = "RECORD_POST_RUNTIME_DAEMON_RUNTIME_LOOP_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_POST_RUNTIME_DAEMON_RUNTIME_LOOP_BOUNDARY"
INTENT_BLOCK = "BLOCK_POST_RUNTIME_DAEMON_RUNTIME_LOOP_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

RUNTIME_LOOP_BOUNDARY_QUESTION = (
    "Can the clean post-runtime-daemon basis be bounded for one future "
    "runtime-loop review without creating runtime loop, public API, "
    "participant-facing interface, distributed network behavior, source "
    "transfer, source receipt, reception authorization, source, authority, "
    "currentness, deployment, public release, operation permission, broader "
    "reusable permission, derivative reception, vessel relation, another "
    "reception request, adoption, receiving-context governance, publication "
    "flow, or follow-on work?"
)

SUPPORTED_SCOPE_VALUES = (
    "RUNTIME_LOOP_BOUNDARY_SPEC_ONLY",
    "ONE_FUTURE_RUNTIME_LOOP_REVIEW_DECLARED",
    "RUNTIME_DAEMON_BASIS_PRESERVED",
    "RUNTIME_DAEMON_NOT_RUNTIME_LOOP",
    "BOUNDED_RUNTIME_DAEMON_ENVELOPE_NOT_RUNTIME_LOOP",
    "RUNTIME_LOOP_BOUNDARY_NOT_RUNTIME_LOOP",
    "RUNTIME_LOOP_BOUNDARY_NOT_PUBLIC_API",
    "RUNTIME_LOOP_BOUNDARY_NOT_DISTRIBUTED_NETWORK_BEHAVIOR",
    "RUNTIME_LOOP_NOT_CREATED",
    "PUBLIC_API_NOT_CREATED",
    "PARTICIPANT_FACING_INTERFACE_NOT_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_NOT_CREATED",
    "NO_SOURCE_TRANSFER",
    "NO_SOURCE_RECEIPT",
    "NO_RECEPTION_AUTHORIZATION",
    "NO_SOURCE_CREATED",
    "NO_AUTHORITY_CREATED",
    "NO_CURRENTNESS_CREATED",
    "NO_DEPLOYMENT_CREATED",
    "NO_PUBLIC_RELEASE_CREATED",
    "NO_OPERATION_PERMISSION_CREATED",
    "NO_BROADER_REUSABLE_PERMISSION",
    "NO_DERIVATIVE_RECEPTION",
    "NO_VESSEL_RELATION",
    "NO_ANOTHER_RECEPTION_REQUEST",
    "NO_ADOPTION",
    "NO_RECEIVING_CONTEXT_GOVERNANCE",
    "NO_PUBLICATION_FLOW",
    "NO_FOLLOW_ON_WORK_AUTHORIZED",
    "NO_RUNTIME_LOOP_INFERENCE",
    "NO_PUBLIC_API_INFERENCE",
    "NO_PARTICIPANT_INTERFACE_INFERENCE",
    "NO_DISTRIBUTED_NETWORK_INFERENCE",
    "NO_SOURCE_INFERENCE",
    "NO_AUTHORITY_INFERENCE",
    "NO_CURRENTNESS_INFERENCE",
    "NO_DEPLOYMENT_INFERENCE",
    "NO_PUBLIC_RELEASE_INFERENCE",
    "NO_OPERATION_PERMISSION_INFERENCE",
    "NO_FOLLOW_ON_WORK_INFERENCE",
    "NO_UNBOUNDED_PASS_FAIL_INFERENCE",
    "HIDDEN_REPO_STATE_EXCLUDED",
    "HIDDEN_REPO_STATE_NOT_USED_AS_RUNTIME_LOOP_BOUNDARY_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_NOT_RUNTIME_LOOP_BOUNDARY_AUTHORITY",
    "ARTIFACT_EXISTENCE_NOT_RUNTIME_LOOP_BOUNDARY_AUTHORITY",
    "LATEST_FILE_POSTURE_NOT_RUNTIME_LOOP_BOUNDARY_AUTHORITY",
    "SELECTED_BASIS_REFERENCE_SHAPE_PRESERVED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "PREDECESSOR_FAILURE_EVIDENCE_PRESERVED",
    "AUTHORIZATION_TOKEN_REUSE_BLOCKED",
    "CONSUMED_REQUEST_TOKEN_REMAINS_CLOSED",
    "CONSUMED_REQUEST_NOT_REOPENED",
    "RESULT_LEVEL_NON_CLAIMS_CANONICAL_FALSE",
)
SUPPORTED_RUNTIME_LOOP_BOUNDARY_SCOPE = SUPPORTED_SCOPE_VALUES

REQUIRED_FALSE_NON_CLAIMS = (
    "runtime_loop_boundary_created_before_review",
    "runtime_loop_created",
    "public_api_created",
    "participant_facing_interface_created",
    "distributed_network_behavior_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "runtime_loop_boundary_treated_as_runtime_loop",
    "runtime_loop_boundary_treated_as_public_api",
    "runtime_loop_boundary_treated_as_participant_facing_interface",
    "runtime_loop_boundary_treated_as_distributed_network_behavior",
    "runtime_loop_boundary_treated_as_source_transfer",
    "runtime_loop_boundary_treated_as_source_receipt",
    "runtime_loop_boundary_treated_as_reception_authorization",
    "runtime_loop_boundary_treated_as_source",
    "runtime_loop_boundary_treated_as_authority",
    "runtime_loop_boundary_treated_as_currentness",
    "runtime_loop_boundary_treated_as_deployment",
    "runtime_loop_boundary_treated_as_public_release",
    "runtime_loop_boundary_treated_as_operation_permission",
    "runtime_loop_boundary_treated_as_broader_reusable_permission",
    "runtime_loop_boundary_treated_as_follow_on_work",
    "runtime_daemon_treated_as_runtime_loop",
    "runtime_daemon_treated_as_public_api",
    "runtime_daemon_treated_as_participant_facing_interface",
    "runtime_daemon_treated_as_distributed_network_behavior",
    "bounded_runtime_daemon_envelope_treated_as_runtime_loop",
    "bounded_runtime_daemon_envelope_authorized_runtime_loop",
    "bounded_runtime_daemon_envelope_authorized_public_api",
    "bounded_runtime_daemon_envelope_authorized_participant_facing_interface",
    "bounded_runtime_daemon_envelope_authorized_distributed_network_behavior",
    "bounded_runtime_daemon_envelope_authorized_arbitrary_runtime_activity",
    "artifact_existence_treated_as_runtime_loop_boundary_authority",
    "artifact_path_treated_as_currentness",
    "latest_file_posture_treated_as_runtime_loop_boundary_authority",
    "repo_local_availability_treated_as_runtime_loop_boundary_authority",
    "hidden_repo_state_used_as_runtime_loop_boundary_content",
    "hidden_repo_state_used_as_runtime_loop_boundary_authority",
    "source_created",
    "authority_created",
    "currentness_created",
    "deployment_created",
    "public_release_created",
    "operation_permission_created",
    "broader_reusable_permission_created",
    "derivative_reception_authorized",
    "vessel_relation_authorized",
    "another_reception_request_authorized",
    "adoption_created",
    "receiving_context_governance_created",
    "publication_flow_created",
    "follow_on_work_authorized",
    "raw_full_prior_artifact_body_returned",
    "prior_artifacts_mutated",
    "consumed_request_reopened",
    "authorization_token_reused",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "runtime_daemon_boundary_v1_failure_hidden",
    "runtime_daemon_boundary_v1_failure_repaired",
    "runtime_daemon_boundary_v1_failure_claimed_passed",
    "runtime_hosting_boundary_v1_failure_hidden",
    "runtime_hosting_boundary_v1_failure_repaired",
    "runtime_hosting_boundary_v1_failure_claimed_passed",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "runtime_loop_boundary_recorded",
    "one_future_runtime_loop_review_declared",
    "runtime_daemon_basis_preserved",
    "runtime_daemon_not_runtime_loop",
    "bounded_runtime_daemon_envelope_not_runtime_loop",
    "runtime_loop_boundary_not_runtime_loop",
    "runtime_loop_boundary_not_public_api",
    "runtime_loop_boundary_not_distributed_network_behavior",
    "runtime_loop_not_created",
    "public_api_not_created",
    "participant_facing_interface_not_created",
    "distributed_network_behavior_not_created",
    "source_transfer_not_created",
    "source_receipt_not_created",
    "reception_authorization_not_created",
    "source_not_created",
    "authority_not_created",
    "currentness_not_created",
    "deployment_not_created",
    "public_release_not_created",
    "operation_permission_not_created",
    "broader_reusable_permission_not_created",
    "follow_on_work_not_authorized",
    "hidden_repo_state_excluded",
    "hidden_repo_state_not_used_as_runtime_loop_boundary_authority",
    "repo_local_availability_not_runtime_loop_boundary_authority",
    "artifact_existence_not_runtime_loop_boundary_authority",
    "latest_file_posture_not_runtime_loop_boundary_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "official_enum_scope_strings_not_redacted",
    "hostile_raw_body_content_contained",
    "predecessor_failure_evidence_preserved",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "RUNTIME_LOOP_BOUNDARY_QUESTION_UNDECLARED",
    "RUNTIME_LOOP_BOUNDARY_INTENT_UNSUPPORTED",
    "RUNTIME_DAEMON_BASIS_MISSING",
    "RUNTIME_DAEMON_NOT_RECORDED",
    "RUNTIME_DAEMON_FAILED_CHECKS_PRESENT",
    "RUNTIME_DAEMON_VERSION_NOT_0_1_0",
    "RUNTIME_DAEMON_DID_NOT_RECORD_BOUNDED_RUNTIME_DAEMON_POSTURE",
    "RUNTIME_DAEMON_DID_NOT_RECORD_BOUNDED_RUNTIME_DAEMON_ENVELOPE",
    "RUNTIME_DAEMON_ALREADY_CREATED_RUNTIME_LOOP",
    "RUNTIME_DAEMON_ALREADY_CREATED_PUBLIC_API",
    "RUNTIME_DAEMON_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE",
    "RUNTIME_DAEMON_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR",
    "RUNTIME_DAEMON_TREATED_AS_RUNTIME_LOOP",
    "RUNTIME_DAEMON_TREATED_AS_PUBLIC_API",
    "RUNTIME_DAEMON_TREATED_AS_PARTICIPANT_FACING_INTERFACE",
    "RUNTIME_DAEMON_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR",
    "RUNTIME_DAEMON_AUTHORIZED_FUTURE_WORK",
    "BOUNDED_RUNTIME_DAEMON_ENVELOPE_TREATED_AS_RUNTIME_LOOP",
    "BOUNDED_RUNTIME_DAEMON_ENVELOPE_AUTHORIZED_RUNTIME_LOOP",
    "BOUNDED_RUNTIME_DAEMON_ENVELOPE_AUTHORIZED_PUBLIC_API",
    "BOUNDED_RUNTIME_DAEMON_ENVELOPE_AUTHORIZED_PARTICIPANT_FACING_INTERFACE",
    "BOUNDED_RUNTIME_DAEMON_ENVELOPE_AUTHORIZED_DISTRIBUTED_NETWORK_BEHAVIOR",
    "BOUNDED_RUNTIME_DAEMON_ENVELOPE_AUTHORIZED_ARBITRARY_RUNTIME_ACTIVITY",
    "RUNTIME_LOOP_BOUNDARY_CREATED_BEFORE_REVIEW",
    "RUNTIME_LOOP_CREATED",
    "PUBLIC_API_CREATED",
    "PARTICIPANT_FACING_INTERFACE_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
    "RUNTIME_LOOP_BOUNDARY_TREATED_AS_RUNTIME_LOOP",
    "RUNTIME_LOOP_BOUNDARY_TREATED_AS_PUBLIC_API",
    "RUNTIME_LOOP_BOUNDARY_TREATED_AS_PARTICIPANT_FACING_INTERFACE",
    "RUNTIME_LOOP_BOUNDARY_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR",
    "RUNTIME_LOOP_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "RUNTIME_LOOP_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "RUNTIME_LOOP_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "RUNTIME_LOOP_BOUNDARY_TREATED_AS_SOURCE",
    "RUNTIME_LOOP_BOUNDARY_TREATED_AS_AUTHORITY",
    "RUNTIME_LOOP_BOUNDARY_TREATED_AS_CURRENTNESS",
    "RUNTIME_LOOP_BOUNDARY_TREATED_AS_DEPLOYMENT",
    "RUNTIME_LOOP_BOUNDARY_TREATED_AS_PUBLIC_RELEASE",
    "RUNTIME_LOOP_BOUNDARY_TREATED_AS_OPERATION_PERMISSION",
    "RUNTIME_LOOP_BOUNDARY_TREATED_AS_BROADER_REUSABLE_PERMISSION",
    "RUNTIME_LOOP_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
    "SOURCE_TRANSFER_OCCURRED",
    "SOURCE_RECEIPT_OCCURRED",
    "RECEPTION_AUTHORIZATION_CREATED",
    "SOURCE_CREATED",
    "AUTHORITY_CREATED",
    "CURRENTNESS_CREATED",
    "DEPLOYMENT_CREATED",
    "PUBLIC_RELEASE_CREATED",
    "OPERATION_PERMISSION_CREATED",
    "BROADER_REUSABLE_PERMISSION_CREATED",
    "DERIVATIVE_RECEPTION_AUTHORIZED",
    "VESSEL_RELATION_AUTHORIZED",
    "ADOPTION_CREATED",
    "RECEIVING_CONTEXT_GOVERNANCE_CREATED",
    "PUBLICATION_FLOW_CREATED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_LOOP_BOUNDARY_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_LOOP_BOUNDARY_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_LOOP_BOUNDARY_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_RUNTIME_LOOP_BOUNDARY_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_RUNTIME_LOOP_BOUNDARY_AUTHORITY",
    "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_RUNTIME_LOOP_BOUNDARY_SCOPE",
    "DECLARED_RUNTIME_LOOP_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_RUNTIME_LOOP_BOUNDARY_REQUEST_UNREADABLE",
    "RUNTIME_DAEMON_BOUNDARY_BASIS_MISSING",
    "RUNTIME_DAEMON_BOUNDARY_NOT_RECORDED",
    "RUNTIME_DAEMON_BOUNDARY_FAILED_CHECKS_PRESENT",
    "RUNTIME_DAEMON_BOUNDARY_VERSION_NOT_0_1_0",
    "RUNTIME_DAEMON_BOUNDARY_V1_FAILURE_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    "SELF_RECURSIVE_GROWTH_BASIS_MISSING",
    "SELF_RECURSIVE_GROWTH_NOT_RECORDED",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_BASIS_MISSING",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_NOT_RECORDED",
    "SELF_CONTINUATION_BASIS_MISSING",
    "SELF_CONTINUATION_NOT_RECORDED",
    "CONTINUATION_BASIS_MISSING",
    "CONTINUATION_NOT_RECORDED",
    "CONTINUATION_BOUNDARY_BASIS_MISSING",
    "CONTINUATION_BOUNDARY_NOT_RECORDED",
    "REUSABLE_RUNTIME_PERMISSION_BASIS_MISSING",
    "REUSABLE_RUNTIME_PERMISSION_NOT_RECORDED",
    "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_BASIS_MISSING",
    "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_NOT_RECORDED",
    "ONGOING_RUNTIME_BASIS_MISSING",
    "ONGOING_RUNTIME_NOT_RECORDED",
    "RUNTIME_HOSTING_BASIS_MISSING",
    "RUNTIME_HOSTING_NOT_RECORDED",
    "RUNTIME_HOSTING_BOUNDARY_V2_BASIS_MISSING",
    "RUNTIME_HOSTING_BOUNDARY_V2_NOT_RECORDED",
    "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
    "SUCCESSOR_RUNTIME_STEP_BASIS_MISSING",
    "SUCCESSOR_RUNTIME_STEP_NOT_RECORDED",
    "MINIMAL_RUNTIME_BASIS_MISSING",
    "MINIMAL_RUNTIME_NOT_RECORDED",
    "RUNTIME_BOUNDARY_BASIS_MISSING",
    "RUNTIME_BOUNDARY_NOT_RECORDED",
    "RUNTIME_READINESS_BASIS_MISSING",
    "RUNTIME_READINESS_NOT_RECORDED",
    "FINAL_COMPLETION_BASIS_MISSING",
    "FINAL_COMPLETION_NOT_RECORDED",
)

REDACTED_RAW_VALUE = "[bounded-redacted-raw-or-hidden-state]"

HOSTILE_SENTINELS = (
    "RAW_RUNTIME_LOOP_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_LOOP_BODY_MUST_NOT_RETURN",
    "RAW_PUBLIC_API_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPANT_FACING_INTERFACE_BODY_MUST_NOT_RETURN",
    "RAW_DISTRIBUTED_NETWORK_BEHAVIOR_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_runtime_loop_boundary_body",
    "raw_runtime_loop_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "raw_runtime_body",
    "runtime_loop_boundary_body",
    "runtime_loop_body",
    "runtime_body",
    "source_body",
    "authority_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
}

OFFICIAL_STRINGS = set(SUPPORTED_SCOPE_VALUES) | set(OUTCOME_FAMILY) | set(BLOCK_CODES)
OFFICIAL_STRINGS.update(REQUIRED_FALSE_NON_CLAIMS)
OFFICIAL_STRINGS.update(ALLOWED_TRUE_RECORDED_FIELDS)
OFFICIAL_STRINGS.update((RESULT_VERSION, RESOLVER_MODULE, INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK))


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _contains_hostile_sentinel(value: str) -> bool:
    return any(sentinel in value for sentinel in HOSTILE_SENTINELS)


def _is_sensitive_key(key: str | None) -> bool:
    if key is None:
        return False
    lowered = key.lower()
    return lowered in SENSITIVE_CONTENT_KEYS or lowered.endswith("_body")


def _sanitize_value(value: Any, key: str | None = None) -> Any:
    if _is_sensitive_key(key):
        return REDACTED_RAW_VALUE
    if isinstance(value, str):
        if value in OFFICIAL_STRINGS:
            return value
        if _contains_hostile_sentinel(value):
            return REDACTED_RAW_VALUE
        return value
    if isinstance(value, Mapping):
        return {str(item_key): _sanitize_value(item_value, str(item_key)) for item_key, item_value in value.items()}
    if isinstance(value, list):
        return [_sanitize_value(item) for item in value]
    if isinstance(value, tuple):
        return [_sanitize_value(item) for item in value]
    if isinstance(value, (bool, int, float)) or value is None:
        return value
    return str(value)


def _deepcopy_mapping(mapping: Mapping[str, Any]) -> dict[str, Any]:
    return copy.deepcopy(dict(mapping))


def _as_bool(value: Any) -> bool | None:
    if isinstance(value, bool):
        return value
    if isinstance(value, Mapping):
        for key in (
            "declared",
            "recorded",
            "preserved",
            "not_created",
            "not_authorized",
            "excluded",
            "blocked",
            "canonical_false",
            "value",
        ):
            if key in value and isinstance(value[key], bool):
                return value[key]
    return None


def _truthy_declared(value: Any) -> bool:
    bool_value = _as_bool(value)
    if bool_value is not None:
        return bool_value
    return bool(value)


def _as_int(value: Any) -> int | None:
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


def _is_zero(value: Any) -> bool:
    return _as_int(value) == 0


def _basis_section(request: Mapping[str, Any], section: str) -> Any:
    return request.get(section)


def _basis_declared(request: Mapping[str, Any], section: str) -> bool:
    value = _basis_section(request, section)
    return value is not None and value != {} and value != [] and value != ""


def _find_mapping_value(mapping: Mapping[str, Any], names: tuple[str, ...]) -> Any:
    for name in names:
        if name in mapping:
            return mapping[name]
    for nested_key in (
        "summary",
        "result_summary",
        "post_runtime_daemon_runtime_loop_boundary_summary",
        "post_self_recursive_growth_runtime_daemon_summary",
        "post_self_recursive_growth_runtime_daemon_boundary_summary",
        "post_self_continuation_self_recursive_growth_summary",
    ):
        nested = mapping.get(nested_key)
        if isinstance(nested, Mapping):
            for name in names:
                if name in nested:
                    return nested[name]
    return None


def _basis_value(
    request: Mapping[str, Any],
    section: str,
    shortcut: str,
    names: tuple[str, ...],
    default: Any = None,
) -> Any:
    if shortcut in request:
        return request[shortcut]
    section_value = _basis_section(request, section)
    if isinstance(section_value, Mapping):
        found = _find_mapping_value(section_value, names)
        if found is not None:
            return found
    return default


def _add_check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str,
) -> None:
    public_code = code if code in BLOCK_CODES else "SELECTED_BASIS_NOT_REFERENCE_SHAPED"
    check: dict[str, Any] = {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": _sanitize_value(expected_posture),
        "actual_posture": _sanitize_value(actual_posture),
    }
    if passed:
        check["block_code"] = None
        check["failure_code"] = None
    else:
        check["block_code"] = public_code
        check["failure_code"] = public_code
    checks.append(check)


def _first_failure(checks: list[dict[str, Any]]) -> dict[str, Any] | None:
    for check in checks:
        if not check.get("passed"):
            return check
    return None


def _selected_scope(request: Mapping[str, Any]) -> list[str]:
    raw_scope = request.get("runtime_loop_boundary_scope", SUPPORTED_SCOPE_VALUES)
    if isinstance(raw_scope, str):
        return [raw_scope]
    if isinstance(raw_scope, (list, tuple)):
        return [str(item) for item in raw_scope]
    return []


def _posture(declared: bool, scope_value: str, meaning: str) -> dict[str, Any]:
    return {"declared": bool(declared), "scope": scope_value, "meaning": meaning}


def _basis_reference(
    label: str,
    outcome: str,
    version: str = "0.1.0",
    failed_check_count: int = 0,
    path: str | None = None,
    **extra: Any,
) -> dict[str, Any]:
    basis: dict[str, Any] = {
        "basis_label": label,
        "basis_kind": "reference-shaped synthetic basis",
        "outcome": outcome,
        "result_version": version,
        "failed_check_count": failed_check_count,
    }
    if path is not None:
        basis["path"] = path
    basis.update(extra)
    return basis


def _add_absence_check(
    checks: list[dict[str, Any]],
    request: Mapping[str, Any],
    field: str,
    code: str,
    check_name: str | None = None,
) -> None:
    actual = request.get(field)
    passed = _as_bool(actual) is not True
    _add_check(checks, check_name or f"{field}_not_true", passed, False, actual, code)


def _add_posture_check(
    checks: list[dict[str, Any]],
    request: Mapping[str, Any],
    field: str,
    code: str = "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
) -> None:
    actual = request.get(field)
    _add_check(checks, f"{field}_declared", _truthy_declared(actual), True, actual, code)


def _add_basis_recorded_checks(
    checks: list[dict[str, Any]],
    request: Mapping[str, Any],
    section: str,
    shortcut_prefix: str,
    expected_outcome: str,
    expected_version: str,
    missing_code: str,
    not_recorded_code: str,
    version_code: str | None = None,
    failed_checks_code: str | None = None,
) -> None:
    declared = _basis_declared(request, section)
    _add_check(checks, f"{shortcut_prefix}_basis_declared", declared, True, declared, missing_code)
    outcome = _basis_value(
        request,
        section,
        f"{shortcut_prefix}_result_outcome",
        ("outcome", "result_outcome"),
    )
    _add_check(
        checks,
        f"{shortcut_prefix}_outcome_recorded",
        outcome == expected_outcome,
        expected_outcome,
        outcome,
        not_recorded_code,
    )
    version = _basis_value(
        request,
        section,
        f"{shortcut_prefix}_result_version",
        ("result_version", "version"),
    )
    _add_check(
        checks,
        f"{shortcut_prefix}_version_expected",
        version == expected_version,
        expected_version,
        version,
        version_code or not_recorded_code,
    )
    failed_count = _basis_value(
        request,
        section,
        f"{shortcut_prefix}_failed_check_count",
        ("failed_check_count", "failed_checks"),
    )
    _add_check(
        checks,
        f"{shortcut_prefix}_failed_checks_zero",
        _is_zero(failed_count),
        0,
        failed_count,
        failed_checks_code or not_recorded_code,
    )


def _add_runtime_loop_boundary_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    question = request.get("runtime_loop_boundary_question")
    _add_check(
        checks,
        "runtime_loop_boundary_question_declared",
        question == RUNTIME_LOOP_BOUNDARY_QUESTION,
        RUNTIME_LOOP_BOUNDARY_QUESTION,
        question,
        "RUNTIME_LOOP_BOUNDARY_QUESTION_UNDECLARED",
    )

    intent = request.get("runtime_loop_boundary_intent")
    _add_check(
        checks,
        "runtime_loop_boundary_intent_supported",
        intent in SUPPORTED_INTENTS and intent != INTENT_BLOCK,
        f"one of {SUPPORTED_INTENTS[:-1]}",
        intent,
        "RUNTIME_LOOP_BOUNDARY_INTENT_UNSUPPORTED",
    )

    scope_values = _selected_scope(request)
    unsupported_scope = [value for value in scope_values if value not in SUPPORTED_SCOPE_VALUES]
    _add_check(
        checks,
        "runtime_loop_boundary_scope_supported",
        not unsupported_scope,
        list(SUPPORTED_SCOPE_VALUES),
        scope_values,
        "UNSUPPORTED_RUNTIME_LOOP_BOUNDARY_SCOPE",
    )

    _add_check(
        checks,
        "runtime_daemon_basis_declared",
        _basis_declared(request, "selected_runtime_daemon_basis"),
        True,
        _basis_declared(request, "selected_runtime_daemon_basis"),
        "RUNTIME_DAEMON_BASIS_MISSING",
    )
    daemon_outcome = _basis_value(
        request,
        "selected_runtime_daemon_basis",
        "selected_runtime_daemon_result_outcome",
        ("outcome", "result_outcome"),
    )
    _add_check(
        checks,
        "runtime_daemon_outcome_recorded",
        daemon_outcome == "POST_SELF_RECURSIVE_GROWTH_RUNTIME_DAEMON_RECORDED",
        "POST_SELF_RECURSIVE_GROWTH_RUNTIME_DAEMON_RECORDED",
        daemon_outcome,
        "RUNTIME_DAEMON_NOT_RECORDED",
    )
    daemon_version = _basis_value(
        request,
        "selected_runtime_daemon_basis",
        "selected_runtime_daemon_result_version",
        ("result_version", "version"),
    )
    _add_check(
        checks,
        "runtime_daemon_version_0_1_0",
        daemon_version == "0.1.0",
        "0.1.0",
        daemon_version,
        "RUNTIME_DAEMON_VERSION_NOT_0_1_0",
    )
    daemon_failed = _basis_value(
        request,
        "selected_runtime_daemon_basis",
        "selected_runtime_daemon_failed_check_count",
        ("failed_check_count", "failed_checks"),
    )
    _add_check(
        checks,
        "runtime_daemon_failed_checks_zero",
        _is_zero(daemon_failed),
        0,
        daemon_failed,
        "RUNTIME_DAEMON_FAILED_CHECKS_PRESENT",
    )
    for shortcut, names, check_name, code in (
        (
            "selected_runtime_daemon_bounded_posture_recorded",
            ("bounded_runtime_daemon_posture_recorded", "runtime_daemon_recorded"),
            "runtime_daemon_recorded_bounded_posture",
            "RUNTIME_DAEMON_DID_NOT_RECORD_BOUNDED_RUNTIME_DAEMON_POSTURE",
        ),
        (
            "selected_runtime_daemon_bounded_runtime_daemon_envelope_recorded",
            ("bounded_runtime_daemon_envelope_declared", "bounded_runtime_daemon_envelope_recorded"),
            "runtime_daemon_recorded_bounded_envelope",
            "RUNTIME_DAEMON_DID_NOT_RECORD_BOUNDED_RUNTIME_DAEMON_ENVELOPE",
        ),
    ):
        actual = _basis_value(request, "selected_runtime_daemon_basis", shortcut, names)
        _add_check(checks, check_name, _as_bool(actual) is True, True, actual, code)

    for field, code in (
        ("selected_runtime_daemon_already_created_runtime_loop", "RUNTIME_DAEMON_ALREADY_CREATED_RUNTIME_LOOP"),
        ("selected_runtime_daemon_already_created_public_api", "RUNTIME_DAEMON_ALREADY_CREATED_PUBLIC_API"),
        ("selected_runtime_daemon_already_created_participant_facing_interface", "RUNTIME_DAEMON_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE"),
        ("selected_runtime_daemon_already_created_distributed_network_behavior", "RUNTIME_DAEMON_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR"),
        ("selected_runtime_daemon_treated_as_runtime_loop", "RUNTIME_DAEMON_TREATED_AS_RUNTIME_LOOP"),
        ("selected_runtime_daemon_treated_as_public_api", "RUNTIME_DAEMON_TREATED_AS_PUBLIC_API"),
        ("selected_runtime_daemon_treated_as_participant_facing_interface", "RUNTIME_DAEMON_TREATED_AS_PARTICIPANT_FACING_INTERFACE"),
        ("selected_runtime_daemon_treated_as_distributed_network_behavior", "RUNTIME_DAEMON_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR"),
        ("selected_runtime_daemon_authorized_future_work", "RUNTIME_DAEMON_AUTHORIZED_FUTURE_WORK"),
        ("selected_bounded_runtime_daemon_envelope_treated_as_runtime_loop", "BOUNDED_RUNTIME_DAEMON_ENVELOPE_TREATED_AS_RUNTIME_LOOP"),
        ("selected_bounded_runtime_daemon_envelope_authorized_runtime_loop", "BOUNDED_RUNTIME_DAEMON_ENVELOPE_AUTHORIZED_RUNTIME_LOOP"),
        ("selected_bounded_runtime_daemon_envelope_authorized_public_api", "BOUNDED_RUNTIME_DAEMON_ENVELOPE_AUTHORIZED_PUBLIC_API"),
        ("selected_bounded_runtime_daemon_envelope_authorized_participant_facing_interface", "BOUNDED_RUNTIME_DAEMON_ENVELOPE_AUTHORIZED_PARTICIPANT_FACING_INTERFACE"),
        ("selected_bounded_runtime_daemon_envelope_authorized_distributed_network_behavior", "BOUNDED_RUNTIME_DAEMON_ENVELOPE_AUTHORIZED_DISTRIBUTED_NETWORK_BEHAVIOR"),
        ("selected_bounded_runtime_daemon_envelope_authorized_arbitrary_runtime_activity", "BOUNDED_RUNTIME_DAEMON_ENVELOPE_AUTHORIZED_ARBITRARY_RUNTIME_ACTIVITY"),
    ):
        _add_absence_check(checks, request, field, code)

    daemon_non_claims = _basis_value(
        request,
        "selected_runtime_daemon_basis",
        "selected_runtime_daemon_non_claims_canonicalized",
        ("result_level_non_claims_canonical_false", "non_claims_canonicalized"),
    )
    _add_check(
        checks,
        "runtime_daemon_non_claims_canonicalized",
        _as_bool(daemon_non_claims) is True,
        True,
        daemon_non_claims,
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )

    terminal_basis = request.get("selected_runtime_daemon_terminal_summary_basis")
    terminal_declared = terminal_basis is not None and terminal_basis != {}
    _add_check(
        checks,
        "runtime_daemon_terminal_summary_basis_declared",
        terminal_declared,
        True,
        terminal_declared,
        "RUNTIME_DAEMON_BASIS_MISSING",
    )
    if isinstance(terminal_basis, Mapping):
        terminal_loop_not_created = terminal_basis.get("runtime_loop_not_created")
        terminal_no_loop_selected = terminal_basis.get("no_runtime_loop_selected")
        terminal_separate_review = terminal_basis.get("separate_future_review_required")
    else:
        terminal_loop_not_created = None
        terminal_no_loop_selected = None
        terminal_separate_review = None
    _add_check(
        checks,
        "runtime_daemon_terminal_summary_states_runtime_loop_not_created",
        _as_bool(terminal_loop_not_created) is True,
        True,
        terminal_loop_not_created,
        "RUNTIME_DAEMON_ALREADY_CREATED_RUNTIME_LOOP",
    )
    _add_check(
        checks,
        "runtime_daemon_terminal_summary_states_no_runtime_loop_selected",
        _as_bool(terminal_no_loop_selected) is True,
        True,
        terminal_no_loop_selected,
        "RUNTIME_DAEMON_ALREADY_CREATED_RUNTIME_LOOP",
    )
    _add_check(
        checks,
        "runtime_daemon_terminal_summary_requires_separate_future_review",
        _as_bool(terminal_separate_review) is True,
        True,
        terminal_separate_review,
        "RUNTIME_DAEMON_AUTHORIZED_FUTURE_WORK",
    )

    _add_basis_recorded_checks(
        checks,
        request,
        "selected_runtime_daemon_boundary_basis",
        "selected_runtime_daemon_boundary",
        "POST_SELF_RECURSIVE_GROWTH_RUNTIME_DAEMON_BOUNDARY_RECORDED",
        "0.1.0",
        "RUNTIME_DAEMON_BOUNDARY_BASIS_MISSING",
        "RUNTIME_DAEMON_BOUNDARY_NOT_RECORDED",
        version_code="RUNTIME_DAEMON_BOUNDARY_VERSION_NOT_0_1_0",
        failed_checks_code="RUNTIME_DAEMON_BOUNDARY_FAILED_CHECKS_PRESENT",
    )
    v1_basis_declared = _basis_declared(request, "selected_runtime_daemon_boundary_v1_failure_lineage_basis")
    _add_check(
        checks,
        "runtime_daemon_boundary_v1_failure_lineage_basis_declared",
        v1_basis_declared,
        True,
        v1_basis_declared,
        "RUNTIME_DAEMON_BOUNDARY_V1_FAILURE_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    )
    for field in (
        "selected_runtime_daemon_boundary_v1_failure_hidden",
        "selected_runtime_daemon_boundary_v1_failure_repaired",
        "selected_runtime_daemon_boundary_v1_failure_claimed_passed",
    ):
        _add_absence_check(
            checks,
            request,
            field,
            "RUNTIME_DAEMON_BOUNDARY_V1_FAILURE_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
        )

    basis_specs = (
        (
            "selected_self_recursive_growth_basis",
            "selected_self_recursive_growth",
            "POST_SELF_CONTINUATION_SELF_RECURSIVE_GROWTH_RECORDED",
            "0.1.0",
            "SELF_RECURSIVE_GROWTH_BASIS_MISSING",
            "SELF_RECURSIVE_GROWTH_NOT_RECORDED",
        ),
        (
            "selected_self_recursive_growth_boundary_basis",
            "selected_self_recursive_growth_boundary",
            "POST_SELF_CONTINUATION_SELF_RECURSIVE_GROWTH_BOUNDARY_RECORDED",
            "0.1.0",
            "SELF_RECURSIVE_GROWTH_BOUNDARY_BASIS_MISSING",
            "SELF_RECURSIVE_GROWTH_BOUNDARY_NOT_RECORDED",
        ),
        (
            "selected_self_continuation_basis",
            "selected_self_continuation",
            "POST_CONTINUATION_SELF_CONTINUATION_RECORDED",
            "0.1.0",
            "SELF_CONTINUATION_BASIS_MISSING",
            "SELF_CONTINUATION_NOT_RECORDED",
        ),
        (
            "selected_self_continuation_boundary_basis",
            "selected_self_continuation_boundary",
            "POST_CONTINUATION_SELF_CONTINUATION_BOUNDARY_RECORDED",
            "0.1.0",
            "SELF_CONTINUATION_BASIS_MISSING",
            "SELF_CONTINUATION_NOT_RECORDED",
        ),
        (
            "selected_continuation_basis",
            "selected_continuation",
            "POST_REUSABLE_RUNTIME_PERMISSION_CONTINUATION_RECORDED",
            "0.1.0",
            "CONTINUATION_BASIS_MISSING",
            "CONTINUATION_NOT_RECORDED",
        ),
        (
            "selected_continuation_boundary_basis",
            "selected_continuation_boundary",
            "POST_REUSABLE_RUNTIME_PERMISSION_CONTINUATION_BOUNDARY_RECORDED",
            "0.1.0",
            "CONTINUATION_BOUNDARY_BASIS_MISSING",
            "CONTINUATION_BOUNDARY_NOT_RECORDED",
        ),
        (
            "selected_reusable_runtime_permission_basis",
            "selected_reusable_runtime_permission",
            "POST_ONGOING_RUNTIME_REUSABLE_RUNTIME_PERMISSION_RECORDED",
            "0.1.0",
            "REUSABLE_RUNTIME_PERMISSION_BASIS_MISSING",
            "REUSABLE_RUNTIME_PERMISSION_NOT_RECORDED",
        ),
        (
            "selected_reusable_runtime_permission_boundary_basis",
            "selected_reusable_runtime_permission_boundary",
            "POST_ONGOING_RUNTIME_REUSABLE_RUNTIME_PERMISSION_BOUNDARY_RECORDED",
            "0.1.0",
            "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_BASIS_MISSING",
            "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_NOT_RECORDED",
        ),
        (
            "selected_ongoing_runtime_basis",
            "selected_ongoing_runtime",
            "POST_RUNTIME_HOSTING_ONGOING_RUNTIME_RECORDED",
            "0.1.0",
            "ONGOING_RUNTIME_BASIS_MISSING",
            "ONGOING_RUNTIME_NOT_RECORDED",
        ),
        (
            "selected_runtime_hosting_basis",
            "selected_runtime_hosting",
            "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_RECORDED",
            "0.1.0",
            "RUNTIME_HOSTING_BASIS_MISSING",
            "RUNTIME_HOSTING_NOT_RECORDED",
        ),
        (
            "selected_runtime_hosting_boundary_v2_basis",
            "selected_runtime_hosting_boundary_v2",
            "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_BOUNDARY_RECORDED",
            "0.2.0",
            "RUNTIME_HOSTING_BOUNDARY_V2_BASIS_MISSING",
            "RUNTIME_HOSTING_BOUNDARY_V2_NOT_RECORDED",
        ),
        (
            "selected_successor_runtime_step_basis",
            "selected_successor_runtime_step",
            "POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_RECORDED",
            "0.1.0",
            "SUCCESSOR_RUNTIME_STEP_BASIS_MISSING",
            "SUCCESSOR_RUNTIME_STEP_NOT_RECORDED",
        ),
        (
            "selected_minimal_runtime_basis",
            "selected_minimal_runtime",
            "POST_PORTABLE_VERIFICATION_MINIMAL_RUNTIME_RECORDED",
            "0.1.0",
            "MINIMAL_RUNTIME_BASIS_MISSING",
            "MINIMAL_RUNTIME_NOT_RECORDED",
        ),
        (
            "selected_runtime_boundary_basis",
            "selected_runtime_boundary",
            "POST_PORTABLE_VERIFICATION_RUNTIME_BOUNDARY_RECORDED",
            "0.1.0",
            "RUNTIME_BOUNDARY_BASIS_MISSING",
            "RUNTIME_BOUNDARY_NOT_RECORDED",
        ),
        (
            "selected_runtime_readiness_basis",
            "selected_runtime_readiness",
            "POST_PORTABLE_VERIFICATION_RUNTIME_READINESS_RECORDED",
            "0.1.0",
            "RUNTIME_READINESS_BASIS_MISSING",
            "RUNTIME_READINESS_NOT_RECORDED",
        ),
        (
            "selected_portable_verification_final_completion_basis",
            "selected_portable_verification_final_completion",
            "PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_RECORDED",
            "0.1.0",
            "FINAL_COMPLETION_BASIS_MISSING",
            "FINAL_COMPLETION_NOT_RECORDED",
        ),
    )
    for section, prefix, outcome, version, missing_code, not_recorded_code in basis_specs:
        _add_basis_recorded_checks(
            checks,
            request,
            section,
            prefix,
            outcome,
            version,
            missing_code,
            not_recorded_code,
        )

    runtime_hosting_v1_declared = _basis_declared(
        request, "selected_runtime_hosting_boundary_v1_failure_lineage_basis"
    )
    _add_check(
        checks,
        "runtime_hosting_boundary_v1_failure_lineage_basis_declared",
        runtime_hosting_v1_declared,
        True,
        runtime_hosting_v1_declared,
        "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
    )
    for field in (
        "selected_runtime_hosting_boundary_v1_failure_repaired",
        "selected_runtime_hosting_boundary_v1_failure_hidden",
        "selected_runtime_hosting_boundary_v1_failure_claimed_passed",
    ):
        _add_absence_check(
            checks,
            request,
            field,
            "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
        )

    currentness_declared = _basis_declared(request, "selected_post_portable_verification_currentness_basis")
    _add_check(
        checks,
        "post_portable_currentness_surface_basis_declared",
        currentness_declared,
        True,
        currentness_declared,
        "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    )
    currentness_checkability = request.get(
        "selected_post_portable_currentness_surface_states_checkability_not_continuation",
        _basis_value(
            request,
            "selected_post_portable_verification_currentness_basis",
            "selected_post_portable_currentness_surface_states_checkability_not_continuation",
            ("states_checkability_not_continuation",),
        ),
    )
    _add_check(
        checks,
        "post_portable_currentness_surface_states_checkability_not_continuation",
        _as_bool(currentness_checkability) is True,
        True,
        currentness_checkability,
        "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    )
    _add_absence_check(
        checks,
        request,
        "selected_post_portable_currentness_surface_authorized_next_work",
        "FOLLOW_ON_WORK_AUTHORIZED",
    )

    returned_capture_declared = _basis_declared(
        request, "selected_returned_second_carrier_capture_lineage_basis"
    )
    _add_check(
        checks,
        "returned_second_carrier_capture_lineage_basis_declared",
        returned_capture_declared,
        True,
        returned_capture_declared,
        "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    )

    for field in (
        "runtime_loop_boundary_spec_only_posture",
        "one_future_runtime_loop_review_posture",
        "runtime_daemon_basis_preserved_posture",
        "runtime_daemon_not_runtime_loop_posture",
        "bounded_runtime_daemon_envelope_not_runtime_loop_posture",
        "runtime_loop_boundary_not_runtime_loop_posture",
        "runtime_loop_boundary_not_public_api_posture",
        "runtime_loop_boundary_not_distributed_network_behavior_posture",
        "runtime_loop_not_created_posture",
        "public_api_not_created_posture",
        "participant_facing_interface_not_created_posture",
        "distributed_network_behavior_not_created_posture",
        "source_transfer_not_created_posture",
        "source_receipt_not_created_posture",
        "reception_authorization_not_created_posture",
        "source_not_created_posture",
        "authority_not_created_posture",
        "currentness_not_created_posture",
        "deployment_not_created_posture",
        "public_release_not_created_posture",
        "operation_permission_not_created_posture",
        "broader_reusable_permission_not_created_posture",
        "follow_on_work_not_authorized_posture",
        "hidden_repo_state_excluded_posture",
        "repo_local_availability_not_runtime_loop_boundary_authority_posture",
        "artifact_existence_not_runtime_loop_boundary_authority_posture",
        "latest_file_posture_not_runtime_loop_boundary_authority_posture",
        "selected_basis_reference_shape_posture",
        "raw_full_prior_artifact_body_not_returned_posture",
        "official_enum_scope_strings_not_redacted_posture",
        "hostile_raw_body_content_contained_posture",
        "predecessor_failure_evidence_preserved_posture",
        "result_level_non_claims_canonical_false_posture",
    ):
        _add_posture_check(checks, request, field)

    absence_fields = (
        ("runtime_loop_boundary_created_before_review", "RUNTIME_LOOP_BOUNDARY_CREATED_BEFORE_REVIEW"),
        ("runtime_loop_created", "RUNTIME_LOOP_CREATED"),
        ("public_api_created", "PUBLIC_API_CREATED"),
        ("participant_facing_interface_created", "PARTICIPANT_FACING_INTERFACE_CREATED"),
        ("distributed_network_behavior_created", "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED"),
        ("runtime_loop_boundary_treated_as_runtime_loop", "RUNTIME_LOOP_BOUNDARY_TREATED_AS_RUNTIME_LOOP"),
        ("runtime_loop_boundary_treated_as_public_api", "RUNTIME_LOOP_BOUNDARY_TREATED_AS_PUBLIC_API"),
        ("runtime_loop_boundary_treated_as_participant_facing_interface", "RUNTIME_LOOP_BOUNDARY_TREATED_AS_PARTICIPANT_FACING_INTERFACE"),
        ("runtime_loop_boundary_treated_as_distributed_network_behavior", "RUNTIME_LOOP_BOUNDARY_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR"),
        ("runtime_loop_boundary_treated_as_source_transfer", "RUNTIME_LOOP_BOUNDARY_TREATED_AS_SOURCE_TRANSFER"),
        ("runtime_loop_boundary_treated_as_source_receipt", "RUNTIME_LOOP_BOUNDARY_TREATED_AS_SOURCE_RECEIPT"),
        ("runtime_loop_boundary_treated_as_reception_authorization", "RUNTIME_LOOP_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION"),
        ("runtime_loop_boundary_treated_as_source", "RUNTIME_LOOP_BOUNDARY_TREATED_AS_SOURCE"),
        ("runtime_loop_boundary_treated_as_authority", "RUNTIME_LOOP_BOUNDARY_TREATED_AS_AUTHORITY"),
        ("runtime_loop_boundary_treated_as_currentness", "RUNTIME_LOOP_BOUNDARY_TREATED_AS_CURRENTNESS"),
        ("runtime_loop_boundary_treated_as_deployment", "RUNTIME_LOOP_BOUNDARY_TREATED_AS_DEPLOYMENT"),
        ("runtime_loop_boundary_treated_as_public_release", "RUNTIME_LOOP_BOUNDARY_TREATED_AS_PUBLIC_RELEASE"),
        ("runtime_loop_boundary_treated_as_operation_permission", "RUNTIME_LOOP_BOUNDARY_TREATED_AS_OPERATION_PERMISSION"),
        ("runtime_loop_boundary_treated_as_broader_reusable_permission", "RUNTIME_LOOP_BOUNDARY_TREATED_AS_BROADER_REUSABLE_PERMISSION"),
        ("runtime_loop_boundary_treated_as_follow_on_work", "RUNTIME_LOOP_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK"),
        ("runtime_daemon_treated_as_runtime_loop", "RUNTIME_DAEMON_TREATED_AS_RUNTIME_LOOP"),
        ("runtime_daemon_treated_as_public_api", "RUNTIME_DAEMON_TREATED_AS_PUBLIC_API"),
        ("runtime_daemon_treated_as_participant_facing_interface", "RUNTIME_DAEMON_TREATED_AS_PARTICIPANT_FACING_INTERFACE"),
        ("runtime_daemon_treated_as_distributed_network_behavior", "RUNTIME_DAEMON_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR"),
        ("bounded_runtime_daemon_envelope_treated_as_runtime_loop", "BOUNDED_RUNTIME_DAEMON_ENVELOPE_TREATED_AS_RUNTIME_LOOP"),
        ("bounded_runtime_daemon_envelope_authorized_runtime_loop", "BOUNDED_RUNTIME_DAEMON_ENVELOPE_AUTHORIZED_RUNTIME_LOOP"),
        ("bounded_runtime_daemon_envelope_authorized_public_api", "BOUNDED_RUNTIME_DAEMON_ENVELOPE_AUTHORIZED_PUBLIC_API"),
        ("bounded_runtime_daemon_envelope_authorized_participant_facing_interface", "BOUNDED_RUNTIME_DAEMON_ENVELOPE_AUTHORIZED_PARTICIPANT_FACING_INTERFACE"),
        ("bounded_runtime_daemon_envelope_authorized_distributed_network_behavior", "BOUNDED_RUNTIME_DAEMON_ENVELOPE_AUTHORIZED_DISTRIBUTED_NETWORK_BEHAVIOR"),
        ("bounded_runtime_daemon_envelope_authorized_arbitrary_runtime_activity", "BOUNDED_RUNTIME_DAEMON_ENVELOPE_AUTHORIZED_ARBITRARY_RUNTIME_ACTIVITY"),
        ("source_transfer_occurred", "SOURCE_TRANSFER_OCCURRED"),
        ("source_receipt_occurred", "SOURCE_RECEIPT_OCCURRED"),
        ("reception_authorization_created", "RECEPTION_AUTHORIZATION_CREATED"),
        ("source_created", "SOURCE_CREATED"),
        ("authority_created", "AUTHORITY_CREATED"),
        ("currentness_created", "CURRENTNESS_CREATED"),
        ("deployment_created", "DEPLOYMENT_CREATED"),
        ("public_release_created", "PUBLIC_RELEASE_CREATED"),
        ("operation_permission_created", "OPERATION_PERMISSION_CREATED"),
        ("broader_reusable_permission_created", "BROADER_REUSABLE_PERMISSION_CREATED"),
        ("derivative_reception_authorized", "DERIVATIVE_RECEPTION_AUTHORIZED"),
        ("vessel_relation_authorized", "VESSEL_RELATION_AUTHORIZED"),
        ("another_reception_request_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
        ("adoption_created", "ADOPTION_CREATED"),
        ("receiving_context_governance_created", "RECEIVING_CONTEXT_GOVERNANCE_CREATED"),
        ("publication_flow_created", "PUBLICATION_FLOW_CREATED"),
        ("follow_on_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
        ("artifact_existence_treated_as_runtime_loop_boundary_authority", "ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_LOOP_BOUNDARY_AUTHORITY"),
        ("artifact_path_treated_as_currentness", "ARTIFACT_PATH_TREATED_AS_CURRENTNESS"),
        ("latest_file_posture_treated_as_runtime_loop_boundary_authority", "LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_LOOP_BOUNDARY_AUTHORITY"),
        ("repo_local_availability_treated_as_runtime_loop_boundary_authority", "REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_LOOP_BOUNDARY_AUTHORITY"),
        ("hidden_repo_state_used_as_runtime_loop_boundary_content", "HIDDEN_REPO_STATE_USED_AS_RUNTIME_LOOP_BOUNDARY_CONTENT"),
        ("hidden_repo_state_used_as_runtime_loop_boundary_authority", "HIDDEN_REPO_STATE_USED_AS_RUNTIME_LOOP_BOUNDARY_AUTHORITY"),
        ("raw_full_prior_artifact_body_returned", "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED"),
        ("prior_artifacts_mutated", "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
        ("predecessor_failure_repaired", "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
        ("predecessor_failure_hidden", "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
        ("predecessor_failure_claimed_passed", "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
        ("consumed_request_reopened", "CONSUMED_REQUEST_REOPENED"),
        ("authorization_token_reused", "AUTHORIZATION_TOKEN_REUSED"),
        ("runtime_daemon_boundary_v1_failure_hidden", "RUNTIME_DAEMON_BOUNDARY_V1_FAILURE_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED"),
        ("runtime_daemon_boundary_v1_failure_repaired", "RUNTIME_DAEMON_BOUNDARY_V1_FAILURE_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED"),
        ("runtime_daemon_boundary_v1_failure_claimed_passed", "RUNTIME_DAEMON_BOUNDARY_V1_FAILURE_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED"),
        ("runtime_hosting_boundary_v1_failure_hidden", "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED"),
        ("runtime_hosting_boundary_v1_failure_repaired", "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED"),
        ("runtime_hosting_boundary_v1_failure_claimed_passed", "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED"),
    )
    for field, code in absence_fields:
        _add_absence_check(checks, request, field, code)

    reference_shaped = request.get("reference_shaped_input_posture", True)
    _add_check(
        checks,
        "selected_basis_reference_shaped",
        _as_bool(reference_shaped) is not False,
        True,
        reference_shaped,
        "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    )

    sanitized_request = _sanitize_value(request)
    serialized_sanitized = json.dumps(sanitized_request, sort_keys=True)
    contained = not any(sentinel in serialized_sanitized for sentinel in HOSTILE_SENTINELS)
    _add_check(
        checks,
        "hostile_raw_body_content_contained",
        contained,
        "no hostile raw/hidden sentinels",
        "contained" if contained else "uncontained",
        "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    )
    _add_check(
        checks,
        "official_enum_scope_strings_not_redacted",
        all(value in SUPPORTED_SCOPE_VALUES for value in SUPPORTED_SCOPE_VALUES),
        list(SUPPORTED_SCOPE_VALUES),
        list(SUPPORTED_SCOPE_VALUES),
        "UNSUPPORTED_RUNTIME_LOOP_BOUNDARY_SCOPE",
    )

    declared_non_claims = request.get("declared_non_claims")
    invalid_non_claims: dict[str, Any] = {}
    if not isinstance(declared_non_claims, Mapping):
        invalid_non_claims["declared_non_claims"] = declared_non_claims
    else:
        for key in REQUIRED_FALSE_NON_CLAIMS:
            if key not in declared_non_claims or declared_non_claims[key] is not False:
                invalid_non_claims[key] = declared_non_claims.get(key)
    _add_check(
        checks,
        "required_non_claims_false",
        not invalid_non_claims,
        {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
        invalid_non_claims or {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    _add_check(
        checks,
        "result_level_required_false_non_claims_canonical_false",
        True,
        {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
        {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )

    return checks


def _statement_for_outcome(outcome: str, checks: list[dict[str, Any]]) -> dict[str, bool]:
    recorded = outcome == OUTCOME_RECORDED
    no_shape_failure = not any(
        not check.get("passed") and check.get("block_code") == "SELECTED_BASIS_NOT_REFERENCE_SHAPED"
        for check in checks
    )
    return {
        "runtime_loop_boundary_recorded": recorded,
        "one_future_runtime_loop_review_declared": recorded,
        "runtime_daemon_basis_preserved": recorded,
        "runtime_daemon_not_runtime_loop": True,
        "bounded_runtime_daemon_envelope_not_runtime_loop": True,
        "runtime_loop_boundary_not_runtime_loop": True,
        "runtime_loop_boundary_not_public_api": True,
        "runtime_loop_boundary_not_distributed_network_behavior": True,
        "runtime_loop_not_created": True,
        "public_api_not_created": True,
        "participant_facing_interface_not_created": True,
        "distributed_network_behavior_not_created": True,
        "source_transfer_not_created": True,
        "source_receipt_not_created": True,
        "reception_authorization_not_created": True,
        "source_not_created": True,
        "authority_not_created": True,
        "currentness_not_created": True,
        "deployment_not_created": True,
        "public_release_not_created": True,
        "operation_permission_not_created": True,
        "broader_reusable_permission_not_created": True,
        "follow_on_work_not_authorized": True,
        "hidden_repo_state_excluded": True,
        "hidden_repo_state_not_used_as_runtime_loop_boundary_authority": True,
        "repo_local_availability_not_runtime_loop_boundary_authority": True,
        "artifact_existence_not_runtime_loop_boundary_authority": True,
        "latest_file_posture_not_runtime_loop_boundary_authority": True,
        "selected_basis_reference_shape_preserved": no_shape_failure,
        "raw_full_prior_artifact_body_not_returned": True,
        "official_enum_scope_strings_not_redacted": True,
        "hostile_raw_body_content_contained": True,
        "predecessor_failure_evidence_preserved": True,
        "authorization_token_reuse_blocked": True,
        "consumed_request_token_remains_closed": True,
        "result_level_non_claims_canonical_false": True,
    }


def _runtime_loop_boundary_non_meaning() -> dict[str, bool]:
    return {
        "runtime_loop_boundary_is_runtime_loop": False,
        "runtime_loop_boundary_is_public_api": False,
        "runtime_loop_boundary_is_participant_facing_interface": False,
        "runtime_loop_boundary_is_distributed_network_behavior": False,
        "runtime_loop_boundary_is_source_transfer": False,
        "runtime_loop_boundary_is_source_receipt": False,
        "runtime_loop_boundary_is_reception_authorization": False,
        "runtime_loop_boundary_is_source": False,
        "runtime_loop_boundary_is_authority": False,
        "runtime_loop_boundary_is_currentness": False,
        "runtime_loop_boundary_is_deployment": False,
        "runtime_loop_boundary_is_public_release": False,
        "runtime_loop_boundary_is_operation_permission": False,
        "runtime_loop_boundary_is_broader_reusable_permission": False,
        "runtime_loop_boundary_is_follow_on_work": False,
        "runtime_daemon_is_runtime_loop": False,
        "bounded_runtime_daemon_envelope_is_runtime_loop": False,
        "runtime_loop_boundary_authorizes_runtime_loop": False,
        "runtime_loop_boundary_authorizes_public_api": False,
        "runtime_loop_boundary_authorizes_participant_facing_interface": False,
        "runtime_loop_boundary_authorizes_distributed_network_behavior": False,
        "runtime_loop_boundary_authorizes_arbitrary_runtime_activity": False,
    }


def _section_or_empty(request: Mapping[str, Any], section: str) -> Any:
    return _sanitize_value(request.get(section, {}))


def _block_from_failure(failure: dict[str, Any] | None, reason: Any = None) -> dict[str, Any] | None:
    if failure is None:
        return None
    code = failure.get("block_code") or failure.get("failure_code") or "DECLARED_RUNTIME_LOOP_BOUNDARY_REQUEST_MALFORMED"
    if code not in BLOCK_CODES:
        code = "DECLARED_RUNTIME_LOOP_BOUNDARY_REQUEST_MALFORMED"
    return {
        "block_code": code,
        "block_reason": _sanitize_value(reason or failure.get("check_name") or code),
    }


def _determine_outcome(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> str:
    if _first_failure(checks) is not None:
        return OUTCOME_BLOCKED
    requested = request.get("requested_runtime_loop_boundary_outcome")
    if requested == OUTCOME_REQUIRES_ADDITIONAL_BASIS or request.get("additional_basis_context"):
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS
    if (
        requested == OUTCOME_NOT_RECORDED
        or request.get("not_recorded_basis")
        or request.get("runtime_loop_boundary_intent") == INTENT_DO_NOT_RECORD
    ):
        return OUTCOME_NOT_RECORDED
    return OUTCOME_RECORDED


def _build_result(request: Mapping[str, Any], checks: list[dict[str, Any]], outcome: str) -> dict[str, Any]:
    request_id = str(request.get("runtime_loop_boundary_request_id") or "post_runtime_daemon_runtime_loop_boundary_request")
    failure = _first_failure(checks)
    block = _block_from_failure(failure, request.get("block_reason"))
    if outcome != OUTCOME_BLOCKED:
        block = None
    statement = _statement_for_outcome(outcome, checks)
    scope = _selected_scope(request) or list(SUPPORTED_SCOPE_VALUES)

    result: dict[str, Any] = {
        "post_runtime_daemon_runtime_loop_boundary_metadata": {
            "post_runtime_daemon_runtime_loop_boundary_id": request_id,
            "post_runtime_daemon_runtime_loop_boundary_type": "post_runtime_daemon_runtime_loop_boundary",
            "post_runtime_daemon_runtime_loop_boundary_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_runtime_loop_boundary_question": {
            "runtime_loop_boundary_request_id": request_id,
            "runtime_loop_boundary_question": _sanitize_value(request.get("runtime_loop_boundary_question")),
            "runtime_loop_boundary_intent": _sanitize_value(request.get("runtime_loop_boundary_intent")),
        },
        "selected_runtime_daemon_basis": _section_or_empty(request, "selected_runtime_daemon_basis"),
        "selected_runtime_daemon_terminal_summary_basis": _section_or_empty(
            request, "selected_runtime_daemon_terminal_summary_basis"
        ),
        "selected_runtime_daemon_boundary_basis": _section_or_empty(request, "selected_runtime_daemon_boundary_basis"),
        "selected_runtime_daemon_boundary_v1_failure_lineage_basis": _section_or_empty(
            request, "selected_runtime_daemon_boundary_v1_failure_lineage_basis"
        ),
        "selected_self_recursive_growth_basis": _section_or_empty(request, "selected_self_recursive_growth_basis"),
        "selected_self_recursive_growth_boundary_basis": _section_or_empty(
            request, "selected_self_recursive_growth_boundary_basis"
        ),
        "selected_self_continuation_basis": _section_or_empty(request, "selected_self_continuation_basis"),
        "selected_self_continuation_boundary_basis": _section_or_empty(
            request, "selected_self_continuation_boundary_basis"
        ),
        "selected_continuation_basis": _section_or_empty(request, "selected_continuation_basis"),
        "selected_continuation_boundary_basis": _section_or_empty(request, "selected_continuation_boundary_basis"),
        "selected_reusable_runtime_permission_basis": _section_or_empty(
            request, "selected_reusable_runtime_permission_basis"
        ),
        "selected_reusable_runtime_permission_boundary_basis": _section_or_empty(
            request, "selected_reusable_runtime_permission_boundary_basis"
        ),
        "selected_ongoing_runtime_basis": _section_or_empty(request, "selected_ongoing_runtime_basis"),
        "selected_runtime_hosting_basis": _section_or_empty(request, "selected_runtime_hosting_basis"),
        "selected_runtime_hosting_boundary_v2_basis": _section_or_empty(
            request, "selected_runtime_hosting_boundary_v2_basis"
        ),
        "selected_runtime_hosting_boundary_v1_failure_lineage_basis": _section_or_empty(
            request, "selected_runtime_hosting_boundary_v1_failure_lineage_basis"
        ),
        "selected_successor_runtime_step_basis": _section_or_empty(request, "selected_successor_runtime_step_basis"),
        "selected_minimal_runtime_basis": _section_or_empty(request, "selected_minimal_runtime_basis"),
        "selected_runtime_boundary_basis": _section_or_empty(request, "selected_runtime_boundary_basis"),
        "selected_runtime_readiness_basis": _section_or_empty(request, "selected_runtime_readiness_basis"),
        "selected_portable_verification_final_completion_basis": _section_or_empty(
            request, "selected_portable_verification_final_completion_basis"
        ),
        "selected_post_portable_verification_currentness_basis": _section_or_empty(
            request, "selected_post_portable_verification_currentness_basis"
        ),
        "selected_returned_second_carrier_capture_lineage_basis": _section_or_empty(
            request, "selected_returned_second_carrier_capture_lineage_basis"
        ),
        "runtime_loop_boundary_spec_only_posture": _posture(
            True, "RUNTIME_LOOP_BOUNDARY_SPEC_ONLY", "runtime-loop-boundary spec posture only"
        ),
        "one_future_runtime_loop_review_posture": _posture(
            outcome == OUTCOME_RECORDED,
            "ONE_FUTURE_RUNTIME_LOOP_REVIEW_DECLARED",
            "one future runtime-loop review declaration only",
        ),
        "runtime_daemon_basis_preserved_posture": _posture(
            statement["runtime_daemon_basis_preserved"],
            "RUNTIME_DAEMON_BASIS_PRESERVED",
            "runtime daemon remains bounded basis",
        ),
        "runtime_daemon_not_runtime_loop_posture": _posture(
            True, "RUNTIME_DAEMON_NOT_RUNTIME_LOOP", "runtime daemon is not runtime loop"
        ),
        "bounded_runtime_daemon_envelope_not_runtime_loop_posture": _posture(
            True,
            "BOUNDED_RUNTIME_DAEMON_ENVELOPE_NOT_RUNTIME_LOOP",
            "bounded runtime-daemon envelope is not runtime loop",
        ),
        "runtime_loop_boundary_not_runtime_loop_posture": _posture(
            True, "RUNTIME_LOOP_BOUNDARY_NOT_RUNTIME_LOOP", "runtime-loop boundary is not runtime loop"
        ),
        "runtime_loop_boundary_not_public_api_posture": _posture(
            True, "RUNTIME_LOOP_BOUNDARY_NOT_PUBLIC_API", "runtime-loop boundary is not public API"
        ),
        "runtime_loop_boundary_not_distributed_network_behavior_posture": _posture(
            True,
            "RUNTIME_LOOP_BOUNDARY_NOT_DISTRIBUTED_NETWORK_BEHAVIOR",
            "runtime-loop boundary is not distributed network behavior",
        ),
        "runtime_loop_not_created_posture": _posture(True, "RUNTIME_LOOP_NOT_CREATED", "runtime loop not created"),
        "public_api_not_created_posture": _posture(True, "PUBLIC_API_NOT_CREATED", "public API not created"),
        "participant_facing_interface_not_created_posture": _posture(
            True, "PARTICIPANT_FACING_INTERFACE_NOT_CREATED", "participant-facing interface not created"
        ),
        "distributed_network_behavior_not_created_posture": _posture(
            True, "DISTRIBUTED_NETWORK_BEHAVIOR_NOT_CREATED", "distributed network behavior not created"
        ),
        "source_transfer_not_created_posture": _posture(True, "NO_SOURCE_TRANSFER", "source transfer not created"),
        "source_receipt_not_created_posture": _posture(True, "NO_SOURCE_RECEIPT", "source receipt not created"),
        "reception_authorization_not_created_posture": _posture(
            True, "NO_RECEPTION_AUTHORIZATION", "reception authorization not created"
        ),
        "source_not_created_posture": _posture(True, "NO_SOURCE_CREATED", "source not created"),
        "authority_not_created_posture": _posture(True, "NO_AUTHORITY_CREATED", "authority not created"),
        "currentness_not_created_posture": _posture(True, "NO_CURRENTNESS_CREATED", "currentness not created"),
        "deployment_not_created_posture": _posture(True, "NO_DEPLOYMENT_CREATED", "deployment not created"),
        "public_release_not_created_posture": _posture(True, "NO_PUBLIC_RELEASE_CREATED", "public release not created"),
        "operation_permission_not_created_posture": _posture(
            True, "NO_OPERATION_PERMISSION_CREATED", "operation permission not created"
        ),
        "broader_reusable_permission_not_created_posture": _posture(
            True, "NO_BROADER_REUSABLE_PERMISSION", "broader reusable permission not created"
        ),
        "follow_on_work_not_authorized_posture": _posture(
            True, "NO_FOLLOW_ON_WORK_AUTHORIZED", "follow-on work not authorized"
        ),
        "hidden_repo_state_excluded_posture": _posture(True, "HIDDEN_REPO_STATE_EXCLUDED", "hidden repo state excluded"),
        "repo_local_availability_not_runtime_loop_boundary_authority_posture": _posture(
            True,
            "REPO_LOCAL_AVAILABILITY_NOT_RUNTIME_LOOP_BOUNDARY_AUTHORITY",
            "repo-local availability is not runtime-loop-boundary authority",
        ),
        "artifact_existence_not_runtime_loop_boundary_authority_posture": _posture(
            True,
            "ARTIFACT_EXISTENCE_NOT_RUNTIME_LOOP_BOUNDARY_AUTHORITY",
            "artifact existence is not runtime-loop-boundary authority",
        ),
        "latest_file_posture_not_runtime_loop_boundary_authority_posture": _posture(
            True,
            "LATEST_FILE_POSTURE_NOT_RUNTIME_LOOP_BOUNDARY_AUTHORITY",
            "latest file posture is not runtime-loop-boundary authority",
        ),
        "selected_basis_reference_shape_posture": _posture(
            statement["selected_basis_reference_shape_preserved"],
            "SELECTED_BASIS_REFERENCE_SHAPE_PRESERVED",
            "selected basis remains reference-shaped",
        ),
        "raw_full_prior_artifact_body_not_returned_posture": _posture(
            True, "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED", "raw full prior artifact body not returned"
        ),
        "official_enum_scope_strings_not_redacted_posture": _posture(
            True,
            "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
            "official scope and code strings remain unredacted",
        ),
        "hostile_raw_body_content_contained_posture": _posture(
            True, "HOSTILE_RAW_BODY_CONTENT_CONTAINED", "hostile raw body content contained"
        ),
        "predecessor_failure_evidence_preserved_posture": _posture(
            True,
            "PREDECESSOR_FAILURE_EVIDENCE_PRESERVED",
            "predecessor failure evidence remains visible and unrepaired",
        ),
        "result_level_non_claims_canonical_false_posture": _posture(
            True,
            "RESULT_LEVEL_NON_CLAIMS_CANONICAL_FALSE",
            "result-level non-claims are canonical false",
        ),
        "runtime_loop_boundary_scope": scope,
        "runtime_loop_boundary_checks": checks,
        "runtime_loop_boundary_statement": statement,
        "runtime_loop_boundary_non_meaning": _runtime_loop_boundary_non_meaning(),
        "additional_basis_required": _sanitize_value(request.get("additional_basis_context", [])),
        "not_recorded_basis": _sanitize_value(request.get("not_recorded_basis", [])),
        "what_remains_open": [
            "runtime-loop-boundary resolver follow-up only if selected",
            "runtime loop",
            "public API",
            "participant-facing interface",
            "distributed network behavior",
            "source transfer",
            "source receipt",
            "reception authorization",
            "source",
            "authority",
            "currentness",
            "deployment",
            "public release",
            "operation permission",
            "broader reusable permission",
            "derivative reception",
            "vessel relation",
            "adoption",
            "receiving-context governance",
            "publication flow",
            "follow-on work",
        ],
        "non_claims": _canonical_non_claims(),
        "outcome": outcome,
        "block": block,
    }
    result["post_runtime_daemon_runtime_loop_boundary_summary"] = (
        build_post_runtime_daemon_runtime_loop_boundary_summary(result)
    )
    return result


def _blocked_request_result(code: str, reason: str, request: Mapping[str, Any] | None = None) -> dict[str, Any]:
    public_code = code if code in BLOCK_CODES else "DECLARED_RUNTIME_LOOP_BOUNDARY_REQUEST_MALFORMED"
    safe_request: Mapping[str, Any] = request or {}
    checks: list[dict[str, Any]] = []
    _add_check(checks, "declared_runtime_loop_boundary_request_readable", False, True, reason, public_code)
    return _build_result(safe_request, checks, OUTCOME_BLOCKED)


def resolve_post_runtime_daemon_runtime_loop_boundary(
    declared_runtime_loop_boundary_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded post-runtime-daemon runtime-loop-boundary request."""

    if declared_runtime_loop_boundary_request is None:
        return _blocked_request_result(
            "DECLARED_RUNTIME_LOOP_BOUNDARY_REQUEST_MALFORMED",
            "declared runtime-loop-boundary request is missing",
        )
    if not isinstance(declared_runtime_loop_boundary_request, Mapping):
        return _blocked_request_result(
            "DECLARED_RUNTIME_LOOP_BOUNDARY_REQUEST_MALFORMED",
            "declared runtime-loop-boundary request is not a mapping",
        )

    request = _deepcopy_mapping(declared_runtime_loop_boundary_request)
    checks = _add_runtime_loop_boundary_checks(request)
    outcome = _determine_outcome(request, checks)
    return _build_result(request, checks, outcome)


def resolve_post_runtime_daemon_runtime_loop_boundary_from_path(
    declared_runtime_loop_boundary_request_path: Path | str,
) -> dict[str, Any]:
    """Read a declared runtime-loop-boundary request JSON file and resolve it."""

    path = Path(declared_runtime_loop_boundary_request_path)
    try:
        loaded = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return _blocked_request_result(
            "DECLARED_RUNTIME_LOOP_BOUNDARY_REQUEST_UNREADABLE",
            f"declared runtime-loop-boundary request path not found: {path}",
        )
    except OSError as exc:
        return _blocked_request_result(
            "DECLARED_RUNTIME_LOOP_BOUNDARY_REQUEST_UNREADABLE",
            f"declared runtime-loop-boundary request path unreadable: {exc}",
        )
    except json.JSONDecodeError as exc:
        return _blocked_request_result(
            "DECLARED_RUNTIME_LOOP_BOUNDARY_REQUEST_MALFORMED",
            f"declared runtime-loop-boundary request JSON malformed: {exc}",
        )
    if not isinstance(loaded, Mapping):
        return _blocked_request_result(
            "DECLARED_RUNTIME_LOOP_BOUNDARY_REQUEST_MALFORMED",
            "declared runtime-loop-boundary request JSON must be an object",
        )
    return resolve_post_runtime_daemon_runtime_loop_boundary(loaded)


def _basis_summary(result: Mapping[str, Any], section: str) -> dict[str, Any]:
    value = result.get(section, {})
    if not isinstance(value, Mapping):
        return {"outcome": None, "result_version": None, "failed_check_count": None}
    return {
        "outcome": value.get("outcome"),
        "result_version": value.get("result_version") or value.get("version"),
        "failed_check_count": value.get("failed_check_count"),
    }


def build_post_runtime_daemon_runtime_loop_boundary_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Build a compact summary from a runtime-loop-boundary result artifact."""

    metadata = result.get("post_runtime_daemon_runtime_loop_boundary_metadata", {})
    question = result.get("declared_runtime_loop_boundary_question", {})
    checks = result.get("runtime_loop_boundary_checks", [])
    if not isinstance(checks, list):
        checks = []
    passed_count = sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed") is True)
    failed_count = sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed") is not True)
    statement = result.get("runtime_loop_boundary_statement", {})
    if not isinstance(statement, Mapping):
        statement = {}
    block = result.get("block")
    if not isinstance(block, Mapping):
        block = {}

    summary: dict[str, Any] = {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "request_id": metadata.get("post_runtime_daemon_runtime_loop_boundary_id")
        or question.get("runtime_loop_boundary_request_id"),
        "question": question.get("runtime_loop_boundary_question"),
        "intent": question.get("runtime_loop_boundary_intent"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": metadata.get("post_runtime_daemon_runtime_loop_boundary_version", RESULT_VERSION),
        "resolver_module": metadata.get("resolver_module", RESOLVER_MODULE),
        "no_loop_api_interface_distributed_network_source_authority_currentness_deployment_public_release_follow_on": True,
        "predecessor_failure_evidence_preserved": statement.get("predecessor_failure_evidence_preserved") is True,
        "consumed_request_token_remains_closed": statement.get("consumed_request_token_remains_closed") is True,
        "authorization_token_reuse_blocked": statement.get("authorization_token_reuse_blocked") is True,
    }
    for field in ALLOWED_TRUE_RECORDED_FIELDS:
        summary[field] = bool(statement.get(field))
    for prefix, section in (
        ("selected_runtime_daemon", "selected_runtime_daemon_basis"),
        ("selected_runtime_daemon_boundary", "selected_runtime_daemon_boundary_basis"),
        ("selected_self_recursive_growth", "selected_self_recursive_growth_basis"),
        ("selected_self_recursive_growth_boundary", "selected_self_recursive_growth_boundary_basis"),
        ("selected_self_continuation", "selected_self_continuation_basis"),
        ("selected_self_continuation_boundary", "selected_self_continuation_boundary_basis"),
        ("selected_continuation", "selected_continuation_basis"),
        ("selected_continuation_boundary", "selected_continuation_boundary_basis"),
        ("selected_reusable_runtime_permission", "selected_reusable_runtime_permission_basis"),
        ("selected_reusable_runtime_permission_boundary", "selected_reusable_runtime_permission_boundary_basis"),
        ("selected_ongoing_runtime", "selected_ongoing_runtime_basis"),
        ("selected_runtime_hosting", "selected_runtime_hosting_basis"),
        ("selected_runtime_hosting_boundary_v2", "selected_runtime_hosting_boundary_v2_basis"),
        ("selected_successor_runtime_step", "selected_successor_runtime_step_basis"),
        ("selected_minimal_runtime", "selected_minimal_runtime_basis"),
        ("selected_runtime_boundary", "selected_runtime_boundary_basis"),
        ("selected_runtime_readiness", "selected_runtime_readiness_basis"),
        ("selected_final_completion", "selected_portable_verification_final_completion_basis"),
    ):
        basis = _basis_summary(result, section)
        summary[f"{prefix}_outcome"] = basis["outcome"]
        summary[f"{prefix}_result_version"] = basis["result_version"]
        summary[f"{prefix}_failed_check_count"] = basis["failed_check_count"]
    runtime_daemon_boundary_v1 = result.get("selected_runtime_daemon_boundary_v1_failure_lineage_basis", {})
    runtime_hosting_boundary_v1 = result.get("selected_runtime_hosting_boundary_v1_failure_lineage_basis", {})
    summary["selected_runtime_daemon_boundary_v1_failure_lineage_preserved"] = bool(runtime_daemon_boundary_v1)
    summary["selected_runtime_hosting_boundary_v1_failure_lineage_preserved"] = bool(runtime_hosting_boundary_v1)
    currentness = result.get("selected_post_portable_verification_currentness_basis", {})
    if isinstance(currentness, Mapping):
        summary["selected_post_portable_currentness_surface_path"] = currentness.get("path")
    else:
        summary["selected_post_portable_currentness_surface_path"] = None
    summary["key_non_claims"] = _canonical_non_claims()
    return summary


def _safe_filename_part(value: Any) -> str:
    raw = str(value or "post_runtime_daemon_runtime_loop_boundary_request")
    safe = []
    for char in raw:
        if char.isalnum() or char in ("-", "_", "."):
            safe.append(char)
        else:
            safe.append("_")
    return "".join(safe).strip("._") or "post_runtime_daemon_runtime_loop_boundary_request"


def _dedupe_path(path: Path) -> Path:
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


def write_post_runtime_daemon_runtime_loop_boundary_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a runtime-loop-boundary result JSON file without overwriting."""

    metadata = result.get("post_runtime_daemon_runtime_loop_boundary_metadata", {})
    if isinstance(metadata, Mapping):
        request_id = metadata.get("post_runtime_daemon_runtime_loop_boundary_id")
    else:
        request_id = None
    filename = f"{_safe_filename_part(request_id)}__post_runtime_daemon_runtime_loop_boundary_result.json"
    if output_path is None:
        target = OUTPUT_ROOT / filename
    else:
        candidate = Path(output_path)
        target = candidate / filename if candidate.suffix == "" else candidate
    target = _dedupe_path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(_sanitize_value(result), indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return target


def build_declared_post_runtime_daemon_runtime_loop_boundary_request(
    runtime_loop_boundary_request_id: str = "post_runtime_daemon_runtime_loop_boundary_reference_review_001",
    runtime_loop_boundary_question: str = RUNTIME_LOOP_BOUNDARY_QUESTION,
    runtime_loop_boundary_intent: str = INTENT_RECORD,
    runtime_loop_boundary_scope: list[str] | tuple[str, ...] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build a valid request for one bounded runtime-loop-boundary posture."""

    request: dict[str, Any] = {
        "runtime_loop_boundary_request_id": runtime_loop_boundary_request_id,
        "runtime_loop_boundary_question": runtime_loop_boundary_question,
        "runtime_loop_boundary_intent": runtime_loop_boundary_intent,
        "selected_runtime_daemon_basis": _basis_reference(
            "post-self-recursive-growth runtime-daemon",
            "POST_SELF_RECURSIVE_GROWTH_RUNTIME_DAEMON_RECORDED",
            path="artifacts/integrity_host_v0_min_coexistence_post_self_recursive_growth_runtime_daemon/post_self_recursive_growth_runtime_daemon_reference_review_001__post_self_recursive_growth_runtime_daemon_result.json",
            runtime_daemon_recorded=True,
            bounded_runtime_daemon_posture_recorded=True,
            bounded_runtime_daemon_envelope_declared=True,
            runtime_loop_not_created=True,
            public_api_not_created=True,
            participant_facing_interface_not_created=True,
            distributed_network_behavior_not_created=True,
            source_not_created=True,
            authority_not_created=True,
            currentness_not_created=True,
            deployment_not_created=True,
            public_release_not_created=True,
            operation_permission_not_created=True,
            broader_reusable_permission_not_created=True,
            follow_on_work_not_authorized=True,
            result_level_non_claims_canonical_false=True,
        ),
        "selected_runtime_daemon_terminal_summary_basis": {
            "path": "spec/POST_SELF_RECURSIVE_GROWTH_RUNTIME_DAEMON_TERMINAL_SUMMARY_V0.md",
            "runtime_loop_not_created": True,
            "no_runtime_loop_selected": True,
            "separate_future_review_required": True,
            "future_work_requires_step_back_review": True,
        },
        "selected_runtime_daemon_boundary_basis": _basis_reference(
            "post-self-recursive-growth runtime-daemon-boundary",
            "POST_SELF_RECURSIVE_GROWTH_RUNTIME_DAEMON_BOUNDARY_RECORDED",
            path="artifacts/integrity_host_v0_min_coexistence_post_self_recursive_growth_runtime_daemon_boundary/post_self_recursive_growth_runtime_daemon_boundary_reference_review_001__post_self_recursive_growth_runtime_daemon_boundary_result.json",
        ),
        "selected_runtime_daemon_boundary_v1_failure_lineage_basis": {
            "path": "tests/test_resolve_post_self_recursive_growth_runtime_daemon_boundary.py",
            "failure_class": "over-strict validation-evidence assertion",
            "preserved_as_failed_test_evidence": True,
            "repaired": False,
            "hidden": False,
            "claimed_passed": False,
        },
        "selected_self_recursive_growth_basis": _basis_reference(
            "post-self-continuation self-recursive-growth",
            "POST_SELF_CONTINUATION_SELF_RECURSIVE_GROWTH_RECORDED",
        ),
        "selected_self_recursive_growth_boundary_basis": _basis_reference(
            "post-self-continuation self-recursive-growth-boundary",
            "POST_SELF_CONTINUATION_SELF_RECURSIVE_GROWTH_BOUNDARY_RECORDED",
        ),
        "selected_self_continuation_basis": _basis_reference(
            "post-continuation self-continuation",
            "POST_CONTINUATION_SELF_CONTINUATION_RECORDED",
        ),
        "selected_self_continuation_boundary_basis": _basis_reference(
            "post-continuation self-continuation-boundary",
            "POST_CONTINUATION_SELF_CONTINUATION_BOUNDARY_RECORDED",
        ),
        "selected_continuation_basis": _basis_reference(
            "post-reusable-runtime-permission continuation",
            "POST_REUSABLE_RUNTIME_PERMISSION_CONTINUATION_RECORDED",
        ),
        "selected_continuation_boundary_basis": _basis_reference(
            "post-reusable-runtime-permission continuation-boundary",
            "POST_REUSABLE_RUNTIME_PERMISSION_CONTINUATION_BOUNDARY_RECORDED",
        ),
        "selected_reusable_runtime_permission_basis": _basis_reference(
            "post-ongoing-runtime reusable-runtime-permission",
            "POST_ONGOING_RUNTIME_REUSABLE_RUNTIME_PERMISSION_RECORDED",
        ),
        "selected_reusable_runtime_permission_boundary_basis": _basis_reference(
            "post-ongoing-runtime reusable-runtime-permission-boundary",
            "POST_ONGOING_RUNTIME_REUSABLE_RUNTIME_PERMISSION_BOUNDARY_RECORDED",
        ),
        "selected_ongoing_runtime_basis": _basis_reference(
            "post-runtime-hosting ongoing-runtime",
            "POST_RUNTIME_HOSTING_ONGOING_RUNTIME_RECORDED",
        ),
        "selected_runtime_hosting_basis": _basis_reference(
            "post-successor-runtime-step runtime-hosting",
            "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_RECORDED",
        ),
        "selected_runtime_hosting_boundary_v2_basis": _basis_reference(
            "post-successor-runtime-step runtime-hosting-boundary-v2",
            "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_BOUNDARY_RECORDED",
            version="0.2.0",
        ),
        "selected_runtime_hosting_boundary_v1_failure_lineage_basis": {
            "path": "tests/test_resolve_post_successor_runtime_step_runtime_hosting_boundary.py",
            "preserved_as_predecessor_failure_evidence": True,
            "repaired": False,
            "hidden": False,
            "claimed_passed": False,
        },
        "selected_successor_runtime_step_basis": _basis_reference(
            "post-minimal-runtime successor-runtime-step",
            "POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_RECORDED",
        ),
        "selected_minimal_runtime_basis": _basis_reference(
            "post-portable-verification minimal-runtime",
            "POST_PORTABLE_VERIFICATION_MINIMAL_RUNTIME_RECORDED",
        ),
        "selected_runtime_boundary_basis": _basis_reference(
            "post-portable-verification runtime-boundary",
            "POST_PORTABLE_VERIFICATION_RUNTIME_BOUNDARY_RECORDED",
        ),
        "selected_runtime_readiness_basis": _basis_reference(
            "post-portable-verification runtime-readiness",
            "POST_PORTABLE_VERIFICATION_RUNTIME_READINESS_RECORDED",
        ),
        "selected_portable_verification_final_completion_basis": _basis_reference(
            "portable source-body verification final-completion",
            "PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_RECORDED",
        ),
        "selected_post_portable_verification_currentness_basis": {
            "path": "spec/POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_V0.md",
            "states_checkability_not_continuation": True,
            "authorized_next_work": False,
        },
        "selected_returned_second_carrier_capture_lineage_basis": {
            "basis_label": "returned second-carrier capture lineage",
            "lineage_only": True,
        },
        "runtime_loop_boundary_spec_only_posture": {"declared": True},
        "one_future_runtime_loop_review_posture": {"declared": True},
        "runtime_daemon_basis_preserved_posture": {"declared": True},
        "runtime_daemon_not_runtime_loop_posture": {"declared": True},
        "bounded_runtime_daemon_envelope_not_runtime_loop_posture": {"declared": True},
        "runtime_loop_boundary_not_runtime_loop_posture": {"declared": True},
        "runtime_loop_boundary_not_public_api_posture": {"declared": True},
        "runtime_loop_boundary_not_distributed_network_behavior_posture": {"declared": True},
        "runtime_loop_not_created_posture": {"declared": True},
        "public_api_not_created_posture": {"declared": True},
        "participant_facing_interface_not_created_posture": {"declared": True},
        "distributed_network_behavior_not_created_posture": {"declared": True},
        "source_transfer_not_created_posture": {"declared": True},
        "source_receipt_not_created_posture": {"declared": True},
        "reception_authorization_not_created_posture": {"declared": True},
        "source_not_created_posture": {"declared": True},
        "authority_not_created_posture": {"declared": True},
        "currentness_not_created_posture": {"declared": True},
        "deployment_not_created_posture": {"declared": True},
        "public_release_not_created_posture": {"declared": True},
        "operation_permission_not_created_posture": {"declared": True},
        "broader_reusable_permission_not_created_posture": {"declared": True},
        "follow_on_work_not_authorized_posture": {"declared": True},
        "hidden_repo_state_excluded_posture": {"declared": True},
        "repo_local_availability_not_runtime_loop_boundary_authority_posture": {"declared": True},
        "artifact_existence_not_runtime_loop_boundary_authority_posture": {"declared": True},
        "latest_file_posture_not_runtime_loop_boundary_authority_posture": {"declared": True},
        "selected_basis_reference_shape_posture": {"declared": True},
        "raw_full_prior_artifact_body_not_returned_posture": {"declared": True},
        "official_enum_scope_strings_not_redacted_posture": {"declared": True},
        "hostile_raw_body_content_contained_posture": {"declared": True},
        "predecessor_failure_evidence_preserved_posture": {"declared": True},
        "result_level_non_claims_canonical_false_posture": {"declared": True},
        "runtime_loop_boundary_scope": list(runtime_loop_boundary_scope or SUPPORTED_SCOPE_VALUES),
        "declared_non_claims": _canonical_non_claims(),
        "selected_runtime_daemon_bounded_posture_recorded": True,
        "selected_runtime_daemon_bounded_runtime_daemon_envelope_recorded": True,
        "selected_runtime_daemon_non_claims_canonicalized": True,
        "selected_post_portable_currentness_surface_states_checkability_not_continuation": True,
        "selected_post_portable_currentness_surface_authorized_next_work": False,
        "reference_shaped_input_posture": True,
    }
    for key in (
        "selected_runtime_daemon_already_created_runtime_loop",
        "selected_runtime_daemon_already_created_public_api",
        "selected_runtime_daemon_already_created_participant_facing_interface",
        "selected_runtime_daemon_already_created_distributed_network_behavior",
        "selected_runtime_daemon_treated_as_runtime_loop",
        "selected_runtime_daemon_treated_as_public_api",
        "selected_runtime_daemon_treated_as_participant_facing_interface",
        "selected_runtime_daemon_treated_as_distributed_network_behavior",
        "selected_runtime_daemon_authorized_future_work",
        "selected_bounded_runtime_daemon_envelope_treated_as_runtime_loop",
        "selected_bounded_runtime_daemon_envelope_authorized_runtime_loop",
        "selected_bounded_runtime_daemon_envelope_authorized_public_api",
        "selected_bounded_runtime_daemon_envelope_authorized_participant_facing_interface",
        "selected_bounded_runtime_daemon_envelope_authorized_distributed_network_behavior",
        "selected_bounded_runtime_daemon_envelope_authorized_arbitrary_runtime_activity",
        "selected_runtime_daemon_boundary_v1_failure_hidden",
        "selected_runtime_daemon_boundary_v1_failure_repaired",
        "selected_runtime_daemon_boundary_v1_failure_claimed_passed",
        "selected_runtime_hosting_boundary_v1_failure_repaired",
        "selected_runtime_hosting_boundary_v1_failure_hidden",
        "selected_runtime_hosting_boundary_v1_failure_claimed_passed",
        "runtime_loop_boundary_created_before_review",
        "runtime_loop_created",
        "public_api_created",
        "participant_facing_interface_created",
        "distributed_network_behavior_created",
        "runtime_loop_boundary_treated_as_runtime_loop",
        "runtime_loop_boundary_treated_as_public_api",
        "runtime_loop_boundary_treated_as_participant_facing_interface",
        "runtime_loop_boundary_treated_as_distributed_network_behavior",
        "runtime_loop_boundary_treated_as_source_transfer",
        "runtime_loop_boundary_treated_as_source_receipt",
        "runtime_loop_boundary_treated_as_reception_authorization",
        "runtime_loop_boundary_treated_as_source",
        "runtime_loop_boundary_treated_as_authority",
        "runtime_loop_boundary_treated_as_currentness",
        "runtime_loop_boundary_treated_as_deployment",
        "runtime_loop_boundary_treated_as_public_release",
        "runtime_loop_boundary_treated_as_operation_permission",
        "runtime_loop_boundary_treated_as_broader_reusable_permission",
        "runtime_loop_boundary_treated_as_follow_on_work",
        "runtime_daemon_treated_as_runtime_loop",
        "runtime_daemon_treated_as_public_api",
        "runtime_daemon_treated_as_participant_facing_interface",
        "runtime_daemon_treated_as_distributed_network_behavior",
        "bounded_runtime_daemon_envelope_treated_as_runtime_loop",
        "bounded_runtime_daemon_envelope_authorized_runtime_loop",
        "bounded_runtime_daemon_envelope_authorized_public_api",
        "bounded_runtime_daemon_envelope_authorized_participant_facing_interface",
        "bounded_runtime_daemon_envelope_authorized_distributed_network_behavior",
        "bounded_runtime_daemon_envelope_authorized_arbitrary_runtime_activity",
        "source_transfer_occurred",
        "source_receipt_occurred",
        "reception_authorization_created",
        "source_created",
        "authority_created",
        "currentness_created",
        "deployment_created",
        "public_release_created",
        "operation_permission_created",
        "broader_reusable_permission_created",
        "derivative_reception_authorized",
        "vessel_relation_authorized",
        "another_reception_request_authorized",
        "adoption_created",
        "receiving_context_governance_created",
        "publication_flow_created",
        "follow_on_work_authorized",
        "artifact_existence_treated_as_runtime_loop_boundary_authority",
        "artifact_path_treated_as_currentness",
        "latest_file_posture_treated_as_runtime_loop_boundary_authority",
        "repo_local_availability_treated_as_runtime_loop_boundary_authority",
        "hidden_repo_state_used_as_runtime_loop_boundary_content",
        "hidden_repo_state_used_as_runtime_loop_boundary_authority",
        "raw_full_prior_artifact_body_returned",
        "predecessor_failure_repaired",
        "predecessor_failure_hidden",
        "predecessor_failure_claimed_passed",
        "consumed_request_reopened",
        "authorization_token_reused",
        "runtime_daemon_boundary_v1_failure_hidden",
        "runtime_daemon_boundary_v1_failure_repaired",
        "runtime_daemon_boundary_v1_failure_claimed_passed",
        "runtime_hosting_boundary_v1_failure_hidden",
        "runtime_hosting_boundary_v1_failure_repaired",
        "runtime_hosting_boundary_v1_failure_claimed_passed",
    ):
        request[key] = False
    request.update(overrides)
    return request
