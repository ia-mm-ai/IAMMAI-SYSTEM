"""Post-runtime-hosting ongoing-runtime-boundary resolver.

This module records one bounded ongoing-runtime-boundary posture from a clean
runtime-hosting basis. It does not create ongoing runtime, reusable runtime
permission, continuation, self-continuation, daemon behavior, loop behavior,
public API behavior, participant-facing interface behavior, distributed network
behavior, source transfer, source receipt, reception authorization, source,
authority, currentness, deployment, public release, operation permission,
reusable permission, adoption, receiving-context governance, publication flow,
or follow-on work.
"""

from __future__ import annotations

import json
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class PostRuntimeHostingOngoingRuntimeBoundaryError(Exception):
    """Raised for bounded resolver I/O errors."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_post_runtime_hosting_ongoing_runtime_boundary"

OUTCOME_RECORDED = "POST_RUNTIME_HOSTING_ONGOING_RUNTIME_BOUNDARY_RECORDED"
OUTCOME_NOT_RECORDED = "POST_RUNTIME_HOSTING_ONGOING_RUNTIME_BOUNDARY_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "POST_RUNTIME_HOSTING_ONGOING_RUNTIME_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "POST_RUNTIME_HOSTING_ONGOING_RUNTIME_BOUNDARY_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_post_runtime_hosting_ongoing_runtime_boundary"
)

ONGOING_RUNTIME_BOUNDARY_QUESTION = (
    "Can the clean post-successor-runtime-step runtime-hosting basis be bounded "
    "for one future ongoing-runtime review without creating ongoing runtime, "
    "reusable runtime permission, continuation, self-continuation, "
    "self-recursive growth, runtime daemon, runtime loop, public API, "
    "participant-facing interface, distributed network behavior, source "
    "transfer, source receipt, reception authorization, source, authority, "
    "currentness, deployment, public release, operation permission, reusable "
    "permission, derivative reception, vessel relation, another reception "
    "request, adoption, receiving-context governance, publication flow, or "
    "follow-on work?"
)

INTENT_RECORD = "RECORD_POST_RUNTIME_HOSTING_ONGOING_RUNTIME_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_POST_RUNTIME_HOSTING_ONGOING_RUNTIME_BOUNDARY"
INTENT_BLOCK = "BLOCK_POST_RUNTIME_HOSTING_ONGOING_RUNTIME_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

SUPPORTED_SCOPE_VALUES = (
    "ONGOING_RUNTIME_BOUNDARY_SPEC_ONLY",
    "ONE_FUTURE_ONGOING_RUNTIME_REVIEW_DECLARED",
    "RUNTIME_HOSTING_BASIS_PRESERVED",
    "RUNTIME_HOSTING_NOT_ONGOING_RUNTIME",
    "RUNTIME_HOSTING_HOST_RELATION_NOT_CONTINUOUS_RUNTIME",
    "ONGOING_RUNTIME_BOUNDARY_NOT_ONGOING_RUNTIME",
    "ONGOING_RUNTIME_BOUNDARY_NOT_REUSABLE_RUNTIME_PERMISSION",
    "ONGOING_RUNTIME_BOUNDARY_NOT_CONTINUATION",
    "ONGOING_RUNTIME_NOT_CREATED",
    "REUSABLE_RUNTIME_PERMISSION_NOT_CREATED",
    "NO_CONTINUATION_AUTHORIZED",
    "SELF_CONTINUATION_NOT_AUTHORIZED",
    "SELF_RECURSIVE_GROWTH_NOT_CREATED",
    "RUNTIME_DAEMON_NOT_CREATED",
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
    "NO_REUSABLE_PERMISSION",
    "NO_DERIVATIVE_RECEPTION",
    "NO_VESSEL_RELATION",
    "NO_ANOTHER_RECEPTION_REQUEST",
    "NO_ADOPTION",
    "NO_RECEIVING_CONTEXT_GOVERNANCE",
    "NO_PUBLICATION_FLOW",
    "NO_FOLLOW_ON_WORK_AUTHORIZED",
    "NO_ONGOING_RUNTIME_INFERENCE",
    "NO_REUSABLE_RUNTIME_PERMISSION_INFERENCE",
    "NO_CONTINUATION_INFERENCE",
    "NO_SELF_CONTINUATION_INFERENCE",
    "NO_DAEMON_INFERENCE",
    "NO_LOOP_INFERENCE",
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
    "HIDDEN_REPO_STATE_NOT_USED_AS_ONGOING_RUNTIME_BOUNDARY_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_NOT_ONGOING_RUNTIME_BOUNDARY_AUTHORITY",
    "ARTIFACT_EXISTENCE_NOT_ONGOING_RUNTIME_BOUNDARY_AUTHORITY",
    "LATEST_FILE_POSTURE_NOT_ONGOING_RUNTIME_BOUNDARY_AUTHORITY",
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
SUPPORTED_ONGOING_RUNTIME_BOUNDARY_SCOPE = SUPPORTED_SCOPE_VALUES

REQUIRED_FALSE_NON_CLAIMS = (
    "ongoing_runtime_created",
    "reusable_runtime_permission_created",
    "continuation_authorized",
    "self_continuation_authorized",
    "self_recursive_growth_created",
    "runtime_daemon_created",
    "runtime_loop_created",
    "public_api_created",
    "participant_facing_interface_created",
    "distributed_network_behavior_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "ongoing_runtime_boundary_treated_as_ongoing_runtime",
    "ongoing_runtime_boundary_treated_as_reusable_runtime_permission",
    "ongoing_runtime_boundary_treated_as_continuation",
    "ongoing_runtime_boundary_treated_as_self_continuation",
    "ongoing_runtime_boundary_treated_as_source_transfer",
    "ongoing_runtime_boundary_treated_as_source_receipt",
    "ongoing_runtime_boundary_treated_as_reception_authorization",
    "ongoing_runtime_boundary_treated_as_source",
    "ongoing_runtime_boundary_treated_as_authority",
    "ongoing_runtime_boundary_treated_as_currentness",
    "ongoing_runtime_boundary_treated_as_deployment",
    "ongoing_runtime_boundary_treated_as_public_release",
    "ongoing_runtime_boundary_treated_as_operation_permission",
    "ongoing_runtime_boundary_treated_as_reusable_permission",
    "ongoing_runtime_boundary_treated_as_follow_on_work",
    "runtime_hosting_treated_as_ongoing_runtime",
    "runtime_hosting_treated_as_reusable_runtime_permission",
    "runtime_hosting_treated_as_continuation",
    "runtime_hosting_treated_as_self_continuation",
    "runtime_hosting_treated_as_runtime_daemon",
    "runtime_hosting_treated_as_runtime_loop",
    "runtime_hosting_treated_as_public_api",
    "runtime_hosting_treated_as_participant_facing_interface",
    "runtime_hosting_treated_as_distributed_network_behavior",
    "runtime_hosting_host_relation_ran_continuously",
    "runtime_hosting_host_relation_created_active_execution",
    "runtime_hosting_host_relation_authorized_follow_on_work",
    "artifact_existence_treated_as_ongoing_runtime_boundary_authority",
    "artifact_path_treated_as_currentness",
    "latest_file_posture_treated_as_ongoing_runtime_boundary_authority",
    "repo_local_availability_treated_as_ongoing_runtime_boundary_authority",
    "hidden_repo_state_used_as_ongoing_runtime_boundary_content",
    "hidden_repo_state_used_as_ongoing_runtime_boundary_authority",
    "source_created",
    "authority_created",
    "currentness_created",
    "deployment_created",
    "public_release_created",
    "operation_permission_created",
    "reusable_permission_created",
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
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "ongoing_runtime_boundary_recorded",
    "one_future_ongoing_runtime_review_declared",
    "runtime_hosting_basis_preserved",
    "runtime_hosting_not_ongoing_runtime",
    "runtime_hosting_host_relation_not_continuous_runtime",
    "ongoing_runtime_boundary_not_ongoing_runtime",
    "ongoing_runtime_boundary_not_reusable_runtime_permission",
    "ongoing_runtime_boundary_not_continuation",
    "ongoing_runtime_not_created",
    "reusable_runtime_permission_not_created",
    "continuation_not_authorized",
    "self_continuation_not_authorized",
    "self_recursive_growth_not_created",
    "runtime_daemon_not_created",
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
    "reusable_permission_not_created",
    "follow_on_work_not_authorized",
    "hidden_repo_state_excluded",
    "hidden_repo_state_not_used_as_ongoing_runtime_boundary_authority",
    "repo_local_availability_not_ongoing_runtime_boundary_authority",
    "artifact_existence_not_ongoing_runtime_boundary_authority",
    "latest_file_posture_not_ongoing_runtime_boundary_authority",
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
    "ONGOING_RUNTIME_BOUNDARY_QUESTION_UNDECLARED",
    "ONGOING_RUNTIME_BOUNDARY_INTENT_UNSUPPORTED",
    "ONGOING_RUNTIME_BOUNDARY_REQUEST_DECLARED_BLOCK",
    "RUNTIME_HOSTING_BASIS_MISSING",
    "RUNTIME_HOSTING_NOT_RECORDED",
    "RUNTIME_HOSTING_FAILED_CHECKS_PRESENT",
    "RUNTIME_HOSTING_VERSION_NOT_0_1_0",
    "RUNTIME_HOSTING_DID_NOT_RECORD_BOUNDED_RUNTIME_HOSTING_POSTURE",
    "RUNTIME_HOSTING_DID_NOT_RECORD_BOUNDED_HOST_RELATION",
    "RUNTIME_HOSTING_ALREADY_CREATED_ONGOING_RUNTIME",
    "RUNTIME_HOSTING_ALREADY_CREATED_REUSABLE_RUNTIME_PERMISSION",
    "RUNTIME_HOSTING_ALREADY_AUTHORIZED_CONTINUATION",
    "RUNTIME_HOSTING_ALREADY_AUTHORIZED_SELF_CONTINUATION",
    "RUNTIME_HOSTING_ALREADY_CREATED_RUNTIME_DAEMON",
    "RUNTIME_HOSTING_ALREADY_CREATED_RUNTIME_LOOP",
    "RUNTIME_HOSTING_ALREADY_CREATED_PUBLIC_API",
    "RUNTIME_HOSTING_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE",
    "RUNTIME_HOSTING_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR",
    "RUNTIME_HOSTING_TREATED_AS_ONGOING_RUNTIME",
    "RUNTIME_HOSTING_TREATED_AS_REUSABLE_RUNTIME_PERMISSION",
    "RUNTIME_HOSTING_TREATED_AS_CONTINUATION",
    "RUNTIME_HOSTING_TREATED_AS_SELF_CONTINUATION",
    "RUNTIME_HOSTING_TREATED_AS_RUNTIME_DAEMON",
    "RUNTIME_HOSTING_TREATED_AS_RUNTIME_LOOP",
    "RUNTIME_HOSTING_TREATED_AS_PUBLIC_API",
    "RUNTIME_HOSTING_TREATED_AS_PARTICIPANT_FACING_INTERFACE",
    "RUNTIME_HOSTING_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR",
    "RUNTIME_HOSTING_AUTHORIZED_FUTURE_WORK",
    "RUNTIME_HOSTING_HOST_RELATION_RAN_CONTINUOUSLY",
    "RUNTIME_HOSTING_HOST_RELATION_CREATED_ACTIVE_EXECUTION",
    "RUNTIME_HOSTING_HOST_RELATION_AUTHORIZED_FOLLOW_ON_WORK",
    "RUNTIME_HOSTING_DID_NOT_CANONICALIZE_NON_CLAIMS",
    "ONGOING_RUNTIME_BOUNDARY_CREATED_BEFORE_REVIEW",
    "ONGOING_RUNTIME_CREATED",
    "REUSABLE_RUNTIME_PERMISSION_CREATED",
    "CONTINUATION_AUTHORIZED",
    "SELF_CONTINUATION_AUTHORIZED",
    "SELF_RECURSIVE_GROWTH_CREATED",
    "RUNTIME_DAEMON_CREATED",
    "RUNTIME_LOOP_CREATED",
    "PUBLIC_API_CREATED",
    "PARTICIPANT_FACING_INTERFACE_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
    "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_ONGOING_RUNTIME",
    "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_REUSABLE_RUNTIME_PERMISSION",
    "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_CONTINUATION",
    "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_SELF_CONTINUATION",
    "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_SOURCE",
    "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_AUTHORITY",
    "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_CURRENTNESS",
    "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_DEPLOYMENT",
    "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_PUBLIC_RELEASE",
    "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_OPERATION_PERMISSION",
    "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION",
    "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
    "SOURCE_TRANSFER_OCCURRED",
    "SOURCE_RECEIPT_OCCURRED",
    "RECEPTION_AUTHORIZATION_CREATED",
    "SOURCE_CREATED",
    "AUTHORITY_CREATED",
    "CURRENTNESS_CREATED",
    "DEPLOYMENT_CREATED",
    "PUBLIC_RELEASE_CREATED",
    "OPERATION_PERMISSION_CREATED",
    "REUSABLE_PERMISSION_CREATED",
    "DERIVATIVE_RECEPTION_AUTHORIZED",
    "VESSEL_RELATION_AUTHORIZED",
    "ANOTHER_RECEPTION_REQUEST_AUTHORIZED",
    "ADOPTION_CREATED",
    "RECEIVING_CONTEXT_GOVERNANCE_CREATED",
    "PUBLICATION_FLOW_CREATED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "ARTIFACT_EXISTENCE_TREATED_AS_ONGOING_RUNTIME_BOUNDARY_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "LATEST_FILE_POSTURE_TREATED_AS_ONGOING_RUNTIME_BOUNDARY_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_ONGOING_RUNTIME_BOUNDARY_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_ONGOING_RUNTIME_BOUNDARY_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_ONGOING_RUNTIME_BOUNDARY_AUTHORITY",
    "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_ONGOING_RUNTIME_BOUNDARY_SCOPE",
    "ONGOING_RUNTIME_BOUNDARY_REQUIRED_POSTURE_MISSING",
    "DECLARED_ONGOING_RUNTIME_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_ONGOING_RUNTIME_BOUNDARY_REQUEST_UNREADABLE",
)

_SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_ongoing_runtime_boundary_body",
    "raw_ongoing_runtime_body",
    "raw_reusable_runtime_permission_body",
    "raw_continuation_body",
    "raw_self_continuation_body",
    "raw_runtime_daemon_body",
    "raw_runtime_loop_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "raw_runtime_body",
    "ongoing_runtime_boundary_body",
    "ongoing_runtime_body",
    "runtime_body",
    "source_body",
    "authority_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
}

_HOSTILE_SENTINELS = (
    "RAW_ONGOING_RUNTIME_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_ONGOING_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_REUSABLE_RUNTIME_PERMISSION_BODY_MUST_NOT_RETURN",
    "RAW_CONTINUATION_BODY_MUST_NOT_RETURN",
    "RAW_SELF_CONTINUATION_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_DAEMON_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_LOOP_BODY_MUST_NOT_RETURN",
    "RAW_PUBLIC_API_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPANT_FACING_INTERFACE_BODY_MUST_NOT_RETURN",
    "RAW_DISTRIBUTED_NETWORK_BEHAVIOR_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)

_REDACTED_RAW_OR_HIDDEN_STATE = "[bounded-redacted-raw-or-hidden-state]"
_DEFAULT_REQUEST_ID = "post_runtime_hosting_ongoing_runtime_boundary_reference_review_001"


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _canonical_false_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _contains_hostile_sentinel(value: str) -> bool:
    return any(sentinel in value for sentinel in _HOSTILE_SENTINELS)


def _sanitize(value: Any, key_hint: str | None = None) -> Any:
    if key_hint:
        lowered = key_hint.lower()
        if lowered in _SENSITIVE_CONTENT_KEYS or lowered.endswith("_body"):
            return _REDACTED_RAW_OR_HIDDEN_STATE
    if isinstance(value, Mapping):
        return {str(key): _sanitize(item, str(key)) for key, item in value.items()}
    if isinstance(value, list):
        return [_sanitize(item) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item) for item in value]
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, str) and _contains_hostile_sentinel(value):
        return _REDACTED_RAW_OR_HIDDEN_STATE
    return deepcopy(value)


def _is_declared(value: Any) -> bool:
    if value is None:
        return False
    if value is False:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, Mapping):
        return bool(value)
    if isinstance(value, (list, tuple, set)):
        return bool(value)
    return True


def _flag_true(value: Any) -> bool:
    return value is True


def _basis_value(request: Mapping[str, Any], field: str) -> Any:
    return request.get(field)


def _safe_get(mapping: Any, key: str, default: Any = None) -> Any:
    if isinstance(mapping, Mapping):
        return mapping.get(key, default)
    return default


def _basis_detail(
    request: Mapping[str, Any],
    basis_field: str,
    outcome_field: str | None = None,
    version_field: str | None = None,
    failed_count_field: str | None = None,
    path_field: str | None = None,
) -> dict[str, Any]:
    basis = request.get(basis_field)
    detail: dict[str, Any] = {
        "declared": _is_declared(basis),
        "basis": _sanitize(basis),
    }
    if outcome_field:
        detail["selected_outcome"] = _sanitize(request.get(outcome_field))
    if version_field:
        detail["selected_result_version"] = _sanitize(request.get(version_field))
    if failed_count_field:
        detail["selected_failed_check_count"] = _sanitize(request.get(failed_count_field))
    if path_field:
        detail["selected_result_path"] = _sanitize(request.get(path_field))
    return detail


def _check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str,
) -> None:
    checks.append(
        {
            "check_name": check_name,
            "passed": bool(passed),
            "expected_posture": expected_posture,
            "actual_posture": _sanitize(actual_posture),
            "block_code": None if passed else code,
            "failure_code": None if passed else code,
        }
    )


def _posture_declared(request: Mapping[str, Any], field: str) -> bool:
    value = request.get(field)
    if isinstance(value, Mapping):
        if not value:
            return False
        if value.get("declared") is False:
            return False
        if value.get("recorded") is False:
            return False
        return True
    return value is True or _is_declared(value)


def _validate_scope(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    scope = request.get("ongoing_runtime_boundary_scope")
    if isinstance(scope, str):
        scope_values = [scope]
    elif isinstance(scope, (list, tuple, set)):
        scope_values = list(scope)
    else:
        scope_values = []
    unsupported = [value for value in scope_values if value not in SUPPORTED_SCOPE_VALUES]
    missing = [value for value in SUPPORTED_SCOPE_VALUES if value not in scope_values]
    _check(
        checks,
        "ongoing_runtime_boundary_scope_supported",
        bool(scope_values) and not unsupported and not missing,
        {
            "all_scope_values_supported": True,
            "required_scope_values": list(SUPPORTED_SCOPE_VALUES),
        },
        {"scope": scope_values, "unsupported": unsupported, "missing": missing},
        "UNSUPPORTED_ONGOING_RUNTIME_BOUNDARY_SCOPE",
    )


def _runtime_hosting_checks(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> None:
    _check(
        checks,
        "runtime_hosting_basis_declared",
        _is_declared(_basis_value(request, "selected_runtime_hosting_basis")),
        "selected runtime-hosting basis declared",
        _basis_value(request, "selected_runtime_hosting_basis"),
        "RUNTIME_HOSTING_BASIS_MISSING",
    )
    _check(
        checks,
        "runtime_hosting_outcome_recorded",
        request.get("selected_runtime_hosting_result_outcome")
        == "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_RECORDED",
        "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_RECORDED",
        request.get("selected_runtime_hosting_result_outcome"),
        "RUNTIME_HOSTING_NOT_RECORDED",
    )
    _check(
        checks,
        "runtime_hosting_version_0_1_0",
        request.get("selected_runtime_hosting_result_version") == "0.1.0",
        "0.1.0",
        request.get("selected_runtime_hosting_result_version"),
        "RUNTIME_HOSTING_VERSION_NOT_0_1_0",
    )
    _check(
        checks,
        "runtime_hosting_failed_checks_zero",
        request.get("selected_runtime_hosting_failed_check_count") == 0,
        0,
        request.get("selected_runtime_hosting_failed_check_count"),
        "RUNTIME_HOSTING_FAILED_CHECKS_PRESENT",
    )
    _check(
        checks,
        "runtime_hosting_recorded_bounded_runtime_hosting_posture",
        request.get("selected_runtime_hosting_bounded_runtime_hosting_posture_recorded")
        is True,
        True,
        request.get("selected_runtime_hosting_bounded_runtime_hosting_posture_recorded"),
        "RUNTIME_HOSTING_DID_NOT_RECORD_BOUNDED_RUNTIME_HOSTING_POSTURE",
    )
    _check(
        checks,
        "runtime_hosting_recorded_bounded_host_relation",
        request.get("selected_runtime_hosting_bounded_host_relation_recorded") is True,
        True,
        request.get("selected_runtime_hosting_bounded_host_relation_recorded"),
        "RUNTIME_HOSTING_DID_NOT_RECORD_BOUNDED_HOST_RELATION",
    )
    runtime_hosting_false_flags = (
        (
            "selected_runtime_hosting_host_relation_ran_continuously",
            "runtime_hosting_host_relation_did_not_run_continuously",
            "RUNTIME_HOSTING_HOST_RELATION_RAN_CONTINUOUSLY",
        ),
        (
            "selected_runtime_hosting_host_relation_created_active_execution",
            "runtime_hosting_host_relation_did_not_create_active_execution",
            "RUNTIME_HOSTING_HOST_RELATION_CREATED_ACTIVE_EXECUTION",
        ),
        (
            "selected_runtime_hosting_host_relation_authorized_follow_on_work",
            "runtime_hosting_host_relation_did_not_authorize_follow_on_work",
            "RUNTIME_HOSTING_HOST_RELATION_AUTHORIZED_FOLLOW_ON_WORK",
        ),
        (
            "selected_runtime_hosting_already_created_ongoing_runtime",
            "runtime_hosting_did_not_create_ongoing_runtime",
            "RUNTIME_HOSTING_ALREADY_CREATED_ONGOING_RUNTIME",
        ),
        (
            "selected_runtime_hosting_already_created_reusable_runtime_permission",
            "runtime_hosting_did_not_create_reusable_runtime_permission",
            "RUNTIME_HOSTING_ALREADY_CREATED_REUSABLE_RUNTIME_PERMISSION",
        ),
        (
            "selected_runtime_hosting_already_authorized_continuation",
            "runtime_hosting_did_not_authorize_continuation",
            "RUNTIME_HOSTING_ALREADY_AUTHORIZED_CONTINUATION",
        ),
        (
            "selected_runtime_hosting_already_authorized_self_continuation",
            "runtime_hosting_did_not_authorize_self_continuation",
            "RUNTIME_HOSTING_ALREADY_AUTHORIZED_SELF_CONTINUATION",
        ),
        (
            "selected_runtime_hosting_already_created_runtime_daemon",
            "runtime_hosting_did_not_create_runtime_daemon",
            "RUNTIME_HOSTING_ALREADY_CREATED_RUNTIME_DAEMON",
        ),
        (
            "selected_runtime_hosting_already_created_runtime_loop",
            "runtime_hosting_did_not_create_runtime_loop",
            "RUNTIME_HOSTING_ALREADY_CREATED_RUNTIME_LOOP",
        ),
        (
            "selected_runtime_hosting_already_created_public_api",
            "runtime_hosting_did_not_create_public_api",
            "RUNTIME_HOSTING_ALREADY_CREATED_PUBLIC_API",
        ),
        (
            "selected_runtime_hosting_already_created_participant_facing_interface",
            "runtime_hosting_did_not_create_participant_facing_interface",
            "RUNTIME_HOSTING_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE",
        ),
        (
            "selected_runtime_hosting_already_created_distributed_network_behavior",
            "runtime_hosting_did_not_create_distributed_network_behavior",
            "RUNTIME_HOSTING_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR",
        ),
        (
            "selected_runtime_hosting_treated_as_ongoing_runtime",
            "runtime_hosting_not_treated_as_ongoing_runtime",
            "RUNTIME_HOSTING_TREATED_AS_ONGOING_RUNTIME",
        ),
        (
            "selected_runtime_hosting_treated_as_reusable_runtime_permission",
            "runtime_hosting_not_treated_as_reusable_runtime_permission",
            "RUNTIME_HOSTING_TREATED_AS_REUSABLE_RUNTIME_PERMISSION",
        ),
        (
            "selected_runtime_hosting_treated_as_continuation",
            "runtime_hosting_not_treated_as_continuation",
            "RUNTIME_HOSTING_TREATED_AS_CONTINUATION",
        ),
        (
            "selected_runtime_hosting_treated_as_self_continuation",
            "runtime_hosting_not_treated_as_self_continuation",
            "RUNTIME_HOSTING_TREATED_AS_SELF_CONTINUATION",
        ),
        (
            "selected_runtime_hosting_treated_as_runtime_daemon",
            "runtime_hosting_not_treated_as_runtime_daemon",
            "RUNTIME_HOSTING_TREATED_AS_RUNTIME_DAEMON",
        ),
        (
            "selected_runtime_hosting_treated_as_runtime_loop",
            "runtime_hosting_not_treated_as_runtime_loop",
            "RUNTIME_HOSTING_TREATED_AS_RUNTIME_LOOP",
        ),
        (
            "selected_runtime_hosting_treated_as_public_api",
            "runtime_hosting_not_treated_as_public_api",
            "RUNTIME_HOSTING_TREATED_AS_PUBLIC_API",
        ),
        (
            "selected_runtime_hosting_treated_as_participant_facing_interface",
            "runtime_hosting_not_treated_as_participant_facing_interface",
            "RUNTIME_HOSTING_TREATED_AS_PARTICIPANT_FACING_INTERFACE",
        ),
        (
            "selected_runtime_hosting_treated_as_distributed_network_behavior",
            "runtime_hosting_not_treated_as_distributed_network_behavior",
            "RUNTIME_HOSTING_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR",
        ),
        (
            "selected_runtime_hosting_authorized_future_work",
            "runtime_hosting_did_not_authorize_future_work",
            "RUNTIME_HOSTING_AUTHORIZED_FUTURE_WORK",
        ),
    )
    for field, check_name, code in runtime_hosting_false_flags:
        _check(checks, check_name, not _flag_true(request.get(field)), False, request.get(field), code)
    _check(
        checks,
        "runtime_hosting_canonicalized_result_level_non_claims",
        request.get("selected_runtime_hosting_non_claims_canonicalized") is True,
        True,
        request.get("selected_runtime_hosting_non_claims_canonicalized"),
        "RUNTIME_HOSTING_DID_NOT_CANONICALIZE_NON_CLAIMS",
    )


def _upstream_basis_checks(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> None:
    upstream = (
        (
            "runtime_hosting_boundary_v2",
            "selected_runtime_hosting_boundary_v2_basis",
            "selected_runtime_hosting_boundary_v2_result_outcome",
            "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_BOUNDARY_RECORDED",
            "selected_runtime_hosting_boundary_v2_result_version",
            "0.2.0",
            "selected_runtime_hosting_boundary_v2_failed_check_count",
            "RUNTIME_HOSTING_BASIS_MISSING",
            "RUNTIME_HOSTING_NOT_RECORDED",
            "RUNTIME_HOSTING_VERSION_NOT_0_1_0",
            "RUNTIME_HOSTING_FAILED_CHECKS_PRESENT",
        ),
        (
            "successor_runtime_step",
            "selected_successor_runtime_step_basis",
            "selected_successor_runtime_step_result_outcome",
            "POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_RECORDED",
            "selected_successor_runtime_step_result_version",
            "0.1.0",
            "selected_successor_runtime_step_failed_check_count",
            "RUNTIME_HOSTING_BASIS_MISSING",
            "RUNTIME_HOSTING_NOT_RECORDED",
            "RUNTIME_HOSTING_VERSION_NOT_0_1_0",
            "RUNTIME_HOSTING_FAILED_CHECKS_PRESENT",
        ),
        (
            "minimal_runtime",
            "selected_minimal_runtime_basis",
            "selected_minimal_runtime_result_outcome",
            "POST_PORTABLE_VERIFICATION_MINIMAL_RUNTIME_RECORDED",
            "selected_minimal_runtime_result_version",
            "0.1.0",
            "selected_minimal_runtime_failed_check_count",
            "RUNTIME_HOSTING_BASIS_MISSING",
            "RUNTIME_HOSTING_NOT_RECORDED",
            "RUNTIME_HOSTING_VERSION_NOT_0_1_0",
            "RUNTIME_HOSTING_FAILED_CHECKS_PRESENT",
        ),
        (
            "runtime_boundary",
            "selected_runtime_boundary_basis",
            "selected_runtime_boundary_result_outcome",
            "POST_PORTABLE_VERIFICATION_RUNTIME_BOUNDARY_RECORDED",
            "selected_runtime_boundary_result_version",
            "0.1.0",
            "selected_runtime_boundary_failed_check_count",
            "RUNTIME_HOSTING_BASIS_MISSING",
            "RUNTIME_HOSTING_NOT_RECORDED",
            "RUNTIME_HOSTING_VERSION_NOT_0_1_0",
            "RUNTIME_HOSTING_FAILED_CHECKS_PRESENT",
        ),
        (
            "runtime_readiness",
            "selected_runtime_readiness_basis",
            "selected_runtime_readiness_result_outcome",
            "POST_PORTABLE_VERIFICATION_RUNTIME_READINESS_RECORDED",
            "selected_runtime_readiness_result_version",
            "0.1.0",
            "selected_runtime_readiness_failed_check_count",
            "RUNTIME_HOSTING_BASIS_MISSING",
            "RUNTIME_HOSTING_NOT_RECORDED",
            "RUNTIME_HOSTING_VERSION_NOT_0_1_0",
            "RUNTIME_HOSTING_FAILED_CHECKS_PRESENT",
        ),
        (
            "portable_verification_final_completion",
            "selected_portable_verification_final_completion_basis",
            "selected_portable_verification_final_completion_result_outcome",
            "PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_RECORDED",
            "selected_portable_verification_final_completion_result_version",
            "0.1.0",
            "selected_portable_verification_final_completion_failed_check_count",
            "RUNTIME_HOSTING_BASIS_MISSING",
            "RUNTIME_HOSTING_NOT_RECORDED",
            "RUNTIME_HOSTING_VERSION_NOT_0_1_0",
            "RUNTIME_HOSTING_FAILED_CHECKS_PRESENT",
        ),
    )
    for (
        label,
        basis_field,
        outcome_field,
        expected_outcome,
        version_field,
        expected_version,
        failed_field,
        basis_code,
        outcome_code,
        version_code,
        failed_code,
    ) in upstream:
        _check(
            checks,
            f"{label}_basis_declared",
            _is_declared(request.get(basis_field)),
            f"selected {label} basis declared",
            request.get(basis_field),
            basis_code,
        )
        _check(
            checks,
            f"{label}_outcome_recorded",
            request.get(outcome_field) == expected_outcome,
            expected_outcome,
            request.get(outcome_field),
            outcome_code,
        )
        _check(
            checks,
            f"{label}_version_expected",
            request.get(version_field) == expected_version,
            expected_version,
            request.get(version_field),
            version_code,
        )
        _check(
            checks,
            f"{label}_failed_checks_zero",
            request.get(failed_field) == 0,
            0,
            request.get(failed_field),
            failed_code,
        )


def _lineage_and_currentness_checks(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> None:
    _check(
        checks,
        "runtime_hosting_boundary_v1_failure_lineage_declared",
        _is_declared(request.get("selected_runtime_hosting_boundary_v1_failure_lineage_basis")),
        "runtime-hosting-boundary v1 failure lineage preserved as predecessor evidence",
        request.get("selected_runtime_hosting_boundary_v1_failure_lineage_basis"),
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    )
    for field in (
        "selected_runtime_hosting_boundary_v1_failure_repaired",
        "selected_runtime_hosting_boundary_v1_failure_hidden",
        "selected_runtime_hosting_boundary_v1_failure_claimed_passed",
    ):
        _check(
            checks,
            f"{field}_false",
            not _flag_true(request.get(field)),
            False,
            request.get(field),
            "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        )
    _check(
        checks,
        "post_portable_currentness_surface_basis_declared",
        _is_declared(request.get("selected_post_portable_verification_currentness_basis")),
        "post-portable-verification currentness surface basis declared",
        request.get("selected_post_portable_verification_currentness_basis"),
        "RUNTIME_HOSTING_BASIS_MISSING",
    )
    _check(
        checks,
        "post_portable_currentness_surface_checkability_not_continuation",
        request.get(
            "selected_post_portable_currentness_surface_states_checkability_not_continuation"
        )
        is True,
        True,
        request.get(
            "selected_post_portable_currentness_surface_states_checkability_not_continuation"
        ),
        "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_CONTINUATION",
    )
    _check(
        checks,
        "post_portable_currentness_surface_does_not_authorize_next_work",
        not _flag_true(
            request.get("selected_post_portable_currentness_surface_authorized_next_work")
        ),
        False,
        request.get("selected_post_portable_currentness_surface_authorized_next_work"),
        "FOLLOW_ON_WORK_AUTHORIZED",
    )
    _check(
        checks,
        "returned_second_carrier_capture_lineage_basis_declared",
        _is_declared(request.get("selected_returned_second_carrier_capture_lineage_basis")),
        "returned second-carrier capture intake basis declared as lineage only",
        request.get("selected_returned_second_carrier_capture_lineage_basis"),
        "RUNTIME_HOSTING_BASIS_MISSING",
    )


def _posture_checks(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    posture_fields = (
        "ongoing_runtime_boundary_spec_only_posture",
        "one_future_ongoing_runtime_review_posture",
        "runtime_hosting_basis_preserved_posture",
        "runtime_hosting_not_ongoing_runtime_posture",
        "runtime_hosting_host_relation_not_continuous_runtime_posture",
        "ongoing_runtime_boundary_not_ongoing_runtime_posture",
        "ongoing_runtime_boundary_not_reusable_runtime_permission_posture",
        "ongoing_runtime_boundary_not_continuation_posture",
        "ongoing_runtime_not_created_posture",
        "reusable_runtime_permission_not_created_posture",
        "continuation_not_authorized_posture",
        "self_continuation_not_authorized_posture",
        "self_recursive_growth_not_created_posture",
        "runtime_daemon_not_created_posture",
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
        "reusable_permission_not_created_posture",
        "follow_on_work_not_authorized_posture",
        "hidden_repo_state_excluded_posture",
        "repo_local_availability_not_ongoing_runtime_boundary_authority_posture",
        "artifact_existence_not_ongoing_runtime_boundary_authority_posture",
        "latest_file_posture_not_ongoing_runtime_boundary_authority_posture",
        "selected_basis_reference_shape_posture",
        "raw_full_prior_artifact_body_not_returned_posture",
        "official_enum_scope_strings_not_redacted_posture",
        "hostile_raw_body_content_contained_posture",
        "predecessor_failure_evidence_preserved_posture",
        "result_level_non_claims_canonical_false_posture",
    )
    for field in posture_fields:
        _check(
            checks,
            f"{field}_declared",
            _posture_declared(request, field),
            "bounded ongoing-runtime-boundary posture declared",
            request.get(field),
            "ONGOING_RUNTIME_BOUNDARY_REQUIRED_POSTURE_MISSING",
        )


def _overreach_checks(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    overreach_fields = (
        (
            "ongoing_runtime_boundary_created_before_review",
            "ongoing_runtime_boundary_not_created_before_review",
            "ONGOING_RUNTIME_BOUNDARY_CREATED_BEFORE_REVIEW",
        ),
        ("ongoing_runtime_created", "ongoing_runtime_not_created", "ONGOING_RUNTIME_CREATED"),
        (
            "reusable_runtime_permission_created",
            "reusable_runtime_permission_not_created",
            "REUSABLE_RUNTIME_PERMISSION_CREATED",
        ),
        (
            "continuation_authorized",
            "continuation_not_authorized",
            "CONTINUATION_AUTHORIZED",
        ),
        (
            "self_continuation_authorized",
            "self_continuation_not_authorized",
            "SELF_CONTINUATION_AUTHORIZED",
        ),
        (
            "self_recursive_growth_created",
            "self_recursive_growth_not_created",
            "SELF_RECURSIVE_GROWTH_CREATED",
        ),
        ("runtime_daemon_created", "runtime_daemon_not_created", "RUNTIME_DAEMON_CREATED"),
        ("runtime_loop_created", "runtime_loop_not_created", "RUNTIME_LOOP_CREATED"),
        ("public_api_created", "public_api_not_created", "PUBLIC_API_CREATED"),
        (
            "participant_facing_interface_created",
            "participant_facing_interface_not_created",
            "PARTICIPANT_FACING_INTERFACE_CREATED",
        ),
        (
            "distributed_network_behavior_created",
            "distributed_network_behavior_not_created",
            "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
        ),
        (
            "ongoing_runtime_boundary_treated_as_ongoing_runtime",
            "ongoing_runtime_boundary_not_treated_as_ongoing_runtime",
            "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_ONGOING_RUNTIME",
        ),
        (
            "ongoing_runtime_boundary_treated_as_reusable_runtime_permission",
            "ongoing_runtime_boundary_not_treated_as_reusable_runtime_permission",
            "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_REUSABLE_RUNTIME_PERMISSION",
        ),
        (
            "ongoing_runtime_boundary_treated_as_continuation",
            "ongoing_runtime_boundary_not_treated_as_continuation",
            "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_CONTINUATION",
        ),
        (
            "ongoing_runtime_boundary_treated_as_self_continuation",
            "ongoing_runtime_boundary_not_treated_as_self_continuation",
            "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_SELF_CONTINUATION",
        ),
        (
            "ongoing_runtime_boundary_treated_as_source_transfer",
            "ongoing_runtime_boundary_not_treated_as_source_transfer",
            "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
        ),
        (
            "ongoing_runtime_boundary_treated_as_source_receipt",
            "ongoing_runtime_boundary_not_treated_as_source_receipt",
            "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
        ),
        (
            "ongoing_runtime_boundary_treated_as_reception_authorization",
            "ongoing_runtime_boundary_not_treated_as_reception_authorization",
            "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
        ),
        (
            "ongoing_runtime_boundary_treated_as_source",
            "ongoing_runtime_boundary_not_treated_as_source",
            "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_SOURCE",
        ),
        (
            "ongoing_runtime_boundary_treated_as_authority",
            "ongoing_runtime_boundary_not_treated_as_authority",
            "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_AUTHORITY",
        ),
        (
            "ongoing_runtime_boundary_treated_as_currentness",
            "ongoing_runtime_boundary_not_treated_as_currentness",
            "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_CURRENTNESS",
        ),
        (
            "ongoing_runtime_boundary_treated_as_deployment",
            "ongoing_runtime_boundary_not_treated_as_deployment",
            "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_DEPLOYMENT",
        ),
        (
            "ongoing_runtime_boundary_treated_as_public_release",
            "ongoing_runtime_boundary_not_treated_as_public_release",
            "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_PUBLIC_RELEASE",
        ),
        (
            "ongoing_runtime_boundary_treated_as_operation_permission",
            "ongoing_runtime_boundary_not_treated_as_operation_permission",
            "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_OPERATION_PERMISSION",
        ),
        (
            "ongoing_runtime_boundary_treated_as_reusable_permission",
            "ongoing_runtime_boundary_not_treated_as_reusable_permission",
            "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION",
        ),
        (
            "ongoing_runtime_boundary_treated_as_follow_on_work",
            "ongoing_runtime_boundary_not_treated_as_follow_on_work",
            "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
        ),
        ("source_transfer_occurred", "source_transfer_not_created", "SOURCE_TRANSFER_OCCURRED"),
        ("source_receipt_occurred", "source_receipt_not_created", "SOURCE_RECEIPT_OCCURRED"),
        (
            "reception_authorization_created",
            "reception_authorization_not_created",
            "RECEPTION_AUTHORIZATION_CREATED",
        ),
        ("source_created", "source_not_created", "SOURCE_CREATED"),
        ("authority_created", "authority_not_created", "AUTHORITY_CREATED"),
        ("currentness_created", "currentness_not_created", "CURRENTNESS_CREATED"),
        ("deployment_created", "deployment_not_created", "DEPLOYMENT_CREATED"),
        ("public_release_created", "public_release_not_created", "PUBLIC_RELEASE_CREATED"),
        (
            "operation_permission_created",
            "operation_permission_not_created",
            "OPERATION_PERMISSION_CREATED",
        ),
        ("reusable_permission_created", "reusable_permission_not_created", "REUSABLE_PERMISSION_CREATED"),
        (
            "derivative_reception_authorized",
            "derivative_reception_not_authorized",
            "DERIVATIVE_RECEPTION_AUTHORIZED",
        ),
        ("vessel_relation_authorized", "vessel_relation_not_authorized", "VESSEL_RELATION_AUTHORIZED"),
        (
            "another_reception_request_authorized",
            "another_reception_request_not_authorized",
            "ANOTHER_RECEPTION_REQUEST_AUTHORIZED",
        ),
        ("adoption_created", "adoption_not_created", "ADOPTION_CREATED"),
        (
            "receiving_context_governance_created",
            "receiving_context_governance_not_created",
            "RECEIVING_CONTEXT_GOVERNANCE_CREATED",
        ),
        ("publication_flow_created", "publication_flow_not_created", "PUBLICATION_FLOW_CREATED"),
        ("follow_on_work_authorized", "follow_on_work_not_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
        (
            "artifact_existence_treated_as_ongoing_runtime_boundary_authority",
            "artifact_existence_not_ongoing_runtime_boundary_authority",
            "ARTIFACT_EXISTENCE_TREATED_AS_ONGOING_RUNTIME_BOUNDARY_AUTHORITY",
        ),
        ("artifact_path_treated_as_currentness", "artifact_path_not_currentness", "ARTIFACT_PATH_TREATED_AS_CURRENTNESS"),
        (
            "latest_file_posture_treated_as_ongoing_runtime_boundary_authority",
            "latest_file_posture_not_ongoing_runtime_boundary_authority",
            "LATEST_FILE_POSTURE_TREATED_AS_ONGOING_RUNTIME_BOUNDARY_AUTHORITY",
        ),
        (
            "repo_local_availability_treated_as_ongoing_runtime_boundary_authority",
            "repo_local_availability_not_ongoing_runtime_boundary_authority",
            "REPO_LOCAL_AVAILABILITY_TREATED_AS_ONGOING_RUNTIME_BOUNDARY_AUTHORITY",
        ),
        (
            "hidden_repo_state_used_as_ongoing_runtime_boundary_content",
            "hidden_repo_state_not_used_as_ongoing_runtime_boundary_content",
            "HIDDEN_REPO_STATE_USED_AS_ONGOING_RUNTIME_BOUNDARY_CONTENT",
        ),
        (
            "hidden_repo_state_used_as_ongoing_runtime_boundary_authority",
            "hidden_repo_state_not_used_as_ongoing_runtime_boundary_authority",
            "HIDDEN_REPO_STATE_USED_AS_ONGOING_RUNTIME_BOUNDARY_AUTHORITY",
        ),
        ("selected_basis_not_reference_shaped", "selected_basis_reference_shaped", "SELECTED_BASIS_NOT_REFERENCE_SHAPED"),
        (
            "raw_full_prior_artifact_body_returned",
            "raw_full_prior_artifact_body_not_returned",
            "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
        ),
        (
            "predecessor_failure_repaired",
            "predecessor_failure_not_repaired",
            "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        ),
        (
            "predecessor_failure_hidden",
            "predecessor_failure_not_hidden",
            "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        ),
        (
            "predecessor_failure_claimed_passed",
            "predecessor_failure_not_claimed_passed",
            "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        ),
        ("consumed_request_reopened", "consumed_request_token_remains_closed", "CONSUMED_REQUEST_REOPENED"),
        ("authorization_token_reused", "authorization_token_reuse_blocked", "AUTHORIZATION_TOKEN_REUSED"),
    )
    for field, check_name, code in overreach_fields:
        _check(checks, check_name, not _flag_true(request.get(field)), False, request.get(field), code)
    reference_shape = request.get("reference_shaped_input_posture", True)
    _check(
        checks,
        "selected_basis_reference_shaped",
        reference_shape is not False and not _flag_true(request.get("selected_basis_not_reference_shaped")),
        True,
        reference_shape,
        "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    )


def _non_claim_checks(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    declared = request.get("declared_non_claims")
    missing_or_flipped: dict[str, Any] = {}
    if not isinstance(declared, Mapping):
        missing_or_flipped["declared_non_claims"] = declared
    else:
        for key in REQUIRED_FALSE_NON_CLAIMS:
            if key not in declared or declared.get(key) is not False:
                missing_or_flipped[key] = declared.get(key)
    _check(
        checks,
        "result_level_required_false_non_claims_canonical_false",
        not missing_or_flipped,
        {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
        missing_or_flipped,
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )


def _build_checks(request: Mapping[str, Any], malformed_code: str | None = None) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    if malformed_code:
        _check(
            checks,
            "declared_ongoing_runtime_boundary_request_mapping",
            False,
            "mapping request",
            request,
            malformed_code,
        )
        return checks

    question = request.get("ongoing_runtime_boundary_question")
    _check(
        checks,
        "ongoing_runtime_boundary_question_declared",
        isinstance(question, str) and question.strip() == ONGOING_RUNTIME_BOUNDARY_QUESTION,
        ONGOING_RUNTIME_BOUNDARY_QUESTION,
        question,
        "ONGOING_RUNTIME_BOUNDARY_QUESTION_UNDECLARED",
    )
    intent = request.get("ongoing_runtime_boundary_intent")
    _check(
        checks,
        "ongoing_runtime_boundary_intent_supported",
        intent in SUPPORTED_INTENTS,
        list(SUPPORTED_INTENTS),
        intent,
        "ONGOING_RUNTIME_BOUNDARY_INTENT_UNSUPPORTED",
    )
    _check(
        checks,
        "ongoing_runtime_boundary_intent_not_explicit_block",
        intent != INTENT_BLOCK,
        "record or do-not-record intent",
        intent,
        "ONGOING_RUNTIME_BOUNDARY_REQUEST_DECLARED_BLOCK",
    )

    _validate_scope(request, checks)
    _runtime_hosting_checks(request, checks)
    _upstream_basis_checks(request, checks)
    _lineage_and_currentness_checks(request, checks)
    _posture_checks(request, checks)
    _overreach_checks(request, checks)
    _non_claim_checks(request, checks)
    return checks


def _first_failed_code(checks: list[dict[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is False:
            return check.get("block_code") or check.get("failure_code")
    return None


def _statement(outcome: str) -> dict[str, bool]:
    statement = {key: True for key in ALLOWED_TRUE_RECORDED_FIELDS}
    if outcome != OUTCOME_RECORDED:
        statement["ongoing_runtime_boundary_recorded"] = False
        statement["one_future_ongoing_runtime_review_declared"] = False
    return statement


def _posture(title: str, recorded: bool = True) -> dict[str, Any]:
    return {
        "declared": True,
        "recorded": recorded,
        "posture": title,
        "creates_ongoing_runtime": False,
        "creates_reusable_runtime_permission": False,
        "authorizes_continuation": False,
        "authorizes_self_continuation": False,
        "creates_self_recursive_growth": False,
        "creates_runtime_daemon": False,
        "creates_runtime_loop": False,
        "creates_public_api": False,
        "creates_participant_facing_interface": False,
        "creates_distributed_network_behavior": False,
        "creates_source": False,
        "creates_authority": False,
        "creates_currentness": False,
        "creates_deployment": False,
        "creates_public_release": False,
        "creates_operation_permission": False,
        "authorizes_follow_on_work": False,
    }


def _non_meaning() -> dict[str, bool]:
    return {
        "ongoing_runtime_boundary_is_ongoing_runtime": False,
        "ongoing_runtime_boundary_is_reusable_runtime_permission": False,
        "ongoing_runtime_boundary_is_continuation": False,
        "ongoing_runtime_boundary_is_self_continuation": False,
        "ongoing_runtime_boundary_is_self_recursive_growth": False,
        "ongoing_runtime_boundary_is_runtime_daemon": False,
        "ongoing_runtime_boundary_is_runtime_loop": False,
        "ongoing_runtime_boundary_is_public_api": False,
        "ongoing_runtime_boundary_is_participant_facing_interface": False,
        "ongoing_runtime_boundary_is_distributed_network_behavior": False,
        "ongoing_runtime_boundary_is_source_transfer": False,
        "ongoing_runtime_boundary_is_source_receipt": False,
        "ongoing_runtime_boundary_is_reception_authorization": False,
        "ongoing_runtime_boundary_is_source": False,
        "ongoing_runtime_boundary_is_authority": False,
        "ongoing_runtime_boundary_is_currentness": False,
        "ongoing_runtime_boundary_is_deployment": False,
        "ongoing_runtime_boundary_is_public_release": False,
        "ongoing_runtime_boundary_is_operation_permission": False,
        "ongoing_runtime_boundary_is_follow_on_work": False,
        "runtime_hosting_became_ongoing_runtime": False,
        "runtime_hosting_host_relation_became_continuous_runtime": False,
    }


def _what_remains_open() -> list[str]:
    return [
        "ongoing-runtime-boundary resolver tests, if separately selected",
        "ongoing-runtime-boundary live artifact, if separately selected",
        "ongoing-runtime-boundary terminal summary, if separately selected",
        "ongoing runtime",
        "reusable runtime permission",
        "continuation beyond bounded steps",
        "self-continuation",
        "self-recursive growth",
        "runtime daemon",
        "runtime loop",
        "public API",
        "participant-facing interface",
        "distributed network behavior",
        "source transfer",
        "source receipt",
        "reception authorization",
        "derivative reception",
        "vessel relation",
        "adoption",
        "authority creation",
        "currentness creation",
        "operation permission",
        "receiving-context governance",
        "deployment",
        "public release",
        "publication flow",
        "reusable permission",
        "successor reception request",
        "follow-on work",
    ]


def build_post_runtime_hosting_ongoing_runtime_boundary_summary(
    result: Mapping[str, Any]
) -> dict[str, Any]:
    checks = list(result.get("ongoing_runtime_boundary_checks", []))
    passed_count = sum(1 for check in checks if check.get("passed") is True)
    failed_count = sum(1 for check in checks if check.get("passed") is False)
    statement = dict(result.get("ongoing_runtime_boundary_statement", {}))
    question = result.get("declared_ongoing_runtime_boundary_question", {})
    runtime_hosting_basis = result.get("selected_runtime_hosting_basis", {})
    runtime_hosting_v2_basis = result.get("selected_runtime_hosting_boundary_v2_basis", {})
    successor_basis = result.get("selected_successor_runtime_step_basis", {})
    minimal_basis = result.get("selected_minimal_runtime_basis", {})
    runtime_boundary_basis = result.get("selected_runtime_boundary_basis", {})
    runtime_readiness_basis = result.get("selected_runtime_readiness_basis", {})
    final_completion_basis = result.get("selected_portable_verification_final_completion_basis", {})
    currentness_basis = result.get("selected_post_portable_verification_currentness_basis", {})
    block = result.get("block")

    return {
        "outcome": result.get("outcome"),
        "block_code": _safe_get(block, "block_code"),
        "block_reason": _safe_get(block, "block_reason"),
        "request_id": _safe_get(question, "ongoing_runtime_boundary_request_id"),
        "question": _safe_get(question, "ongoing_runtime_boundary_question"),
        "intent": _safe_get(question, "ongoing_runtime_boundary_intent"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "ongoing_runtime_boundary_recorded": statement.get(
            "ongoing_runtime_boundary_recorded", False
        ),
        "one_future_ongoing_runtime_review_declared": statement.get(
            "one_future_ongoing_runtime_review_declared", False
        ),
        "runtime_hosting_basis_preserved": statement.get(
            "runtime_hosting_basis_preserved", False
        ),
        "runtime_hosting_not_ongoing_runtime": statement.get(
            "runtime_hosting_not_ongoing_runtime", False
        ),
        "runtime_hosting_host_relation_not_continuous_runtime": statement.get(
            "runtime_hosting_host_relation_not_continuous_runtime", False
        ),
        "ongoing_runtime_boundary_not_ongoing_runtime": statement.get(
            "ongoing_runtime_boundary_not_ongoing_runtime", False
        ),
        "ongoing_runtime_boundary_not_reusable_runtime_permission": statement.get(
            "ongoing_runtime_boundary_not_reusable_runtime_permission", False
        ),
        "ongoing_runtime_boundary_not_continuation": statement.get(
            "ongoing_runtime_boundary_not_continuation", False
        ),
        "ongoing_runtime_not_created": statement.get("ongoing_runtime_not_created", False),
        "reusable_runtime_permission_not_created": statement.get(
            "reusable_runtime_permission_not_created", False
        ),
        "continuation_not_authorized": statement.get(
            "continuation_not_authorized", False
        ),
        "self_continuation_not_authorized": statement.get(
            "self_continuation_not_authorized", False
        ),
        "self_recursive_growth_not_created": statement.get(
            "self_recursive_growth_not_created", False
        ),
        "runtime_daemon_not_created": statement.get("runtime_daemon_not_created", False),
        "runtime_loop_not_created": statement.get("runtime_loop_not_created", False),
        "public_api_not_created": statement.get("public_api_not_created", False),
        "participant_facing_interface_not_created": statement.get(
            "participant_facing_interface_not_created", False
        ),
        "distributed_network_behavior_not_created": statement.get(
            "distributed_network_behavior_not_created", False
        ),
        "source_transfer_source_receipt_reception_authorization_not_created": all(
            statement.get(key, False)
            for key in (
                "source_transfer_not_created",
                "source_receipt_not_created",
                "reception_authorization_not_created",
            )
        ),
        "source_authority_currentness_deployment_public_release_operation_permission_follow_on_not_created": all(
            statement.get(key, False)
            for key in (
                "source_not_created",
                "authority_not_created",
                "currentness_not_created",
                "deployment_not_created",
                "public_release_not_created",
                "operation_permission_not_created",
                "follow_on_work_not_authorized",
            )
        ),
        "hidden_repo_state_excluded": statement.get("hidden_repo_state_excluded", False),
        "hidden_repo_state_not_used_as_ongoing_runtime_boundary_authority": statement.get(
            "hidden_repo_state_not_used_as_ongoing_runtime_boundary_authority", False
        ),
        "repo_local_availability_not_ongoing_runtime_boundary_authority": statement.get(
            "repo_local_availability_not_ongoing_runtime_boundary_authority", False
        ),
        "artifact_existence_not_ongoing_runtime_boundary_authority": statement.get(
            "artifact_existence_not_ongoing_runtime_boundary_authority", False
        ),
        "latest_file_posture_not_ongoing_runtime_boundary_authority": statement.get(
            "latest_file_posture_not_ongoing_runtime_boundary_authority", False
        ),
        "selected_basis_reference_shape_preserved": statement.get(
            "selected_basis_reference_shape_preserved", False
        ),
        "raw_full_prior_artifact_body_not_returned": statement.get(
            "raw_full_prior_artifact_body_not_returned", False
        ),
        "official_enum_scope_strings_not_redacted": statement.get(
            "official_enum_scope_strings_not_redacted", False
        ),
        "hostile_raw_body_content_contained": statement.get(
            "hostile_raw_body_content_contained", False
        ),
        "result_level_non_claims_canonical_false": statement.get(
            "result_level_non_claims_canonical_false", False
        ),
        "selected_runtime_hosting_outcome": runtime_hosting_basis.get("selected_outcome"),
        "selected_runtime_hosting_result_version": runtime_hosting_basis.get(
            "selected_result_version"
        ),
        "selected_runtime_hosting_failed_check_count": runtime_hosting_basis.get(
            "selected_failed_check_count"
        ),
        "selected_runtime_hosting_boundary_v2_outcome": runtime_hosting_v2_basis.get(
            "selected_outcome"
        ),
        "selected_runtime_hosting_boundary_v2_result_version": runtime_hosting_v2_basis.get(
            "selected_result_version"
        ),
        "selected_runtime_hosting_boundary_v2_failed_check_count": runtime_hosting_v2_basis.get(
            "selected_failed_check_count"
        ),
        "selected_successor_runtime_step_outcome": successor_basis.get("selected_outcome"),
        "selected_successor_runtime_step_result_version": successor_basis.get(
            "selected_result_version"
        ),
        "selected_successor_runtime_step_failed_check_count": successor_basis.get(
            "selected_failed_check_count"
        ),
        "selected_minimal_runtime_outcome": minimal_basis.get("selected_outcome"),
        "selected_minimal_runtime_result_version": minimal_basis.get(
            "selected_result_version"
        ),
        "selected_minimal_runtime_failed_check_count": minimal_basis.get(
            "selected_failed_check_count"
        ),
        "selected_runtime_boundary_outcome": runtime_boundary_basis.get("selected_outcome"),
        "selected_runtime_boundary_result_version": runtime_boundary_basis.get(
            "selected_result_version"
        ),
        "selected_runtime_boundary_failed_check_count": runtime_boundary_basis.get(
            "selected_failed_check_count"
        ),
        "selected_runtime_readiness_outcome": runtime_readiness_basis.get(
            "selected_outcome"
        ),
        "selected_runtime_readiness_result_version": runtime_readiness_basis.get(
            "selected_result_version"
        ),
        "selected_runtime_readiness_failed_check_count": runtime_readiness_basis.get(
            "selected_failed_check_count"
        ),
        "selected_final_completion_outcome": final_completion_basis.get("selected_outcome"),
        "selected_final_completion_result_version": final_completion_basis.get(
            "selected_result_version"
        ),
        "selected_final_completion_failed_check_count": final_completion_basis.get(
            "selected_failed_check_count"
        ),
        "selected_post_portable_currentness_surface_path": currentness_basis.get(
            "selected_result_path"
        )
        or _safe_get(currentness_basis.get("basis"), "path"),
        "no_ongoing_runtime_reusable_runtime_permission_continuation_self_continuation_daemon_loop_api_interface_distributed_network_source_authority_currentness_deployment_public_release_follow_on": True,
        "key_non_claims": result.get("non_claims", {}),
        "predecessor_failure_evidence_preserved": statement.get(
            "predecessor_failure_evidence_preserved", False
        ),
        "consumed_request_token_remains_closed": statement.get(
            "consumed_request_token_remains_closed", False
        ),
        "authorization_token_reuse_blocked": statement.get(
            "authorization_token_reuse_blocked", False
        ),
    }


def _build_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    outcome: str,
    block_code: str | None,
) -> dict[str, Any]:
    request_id = str(request.get("ongoing_runtime_boundary_request_id") or _DEFAULT_REQUEST_ID)
    statement = _statement(outcome)
    block = None
    if block_code:
        block = {
            "block_code": block_code,
            "block_reason": _sanitize(
                request.get("block_reason")
                or "ongoing-runtime-boundary review blocked by bounded membrane check"
            ),
        }

    result: dict[str, Any] = {
        "post_runtime_hosting_ongoing_runtime_boundary_metadata": {
            "post_runtime_hosting_ongoing_runtime_boundary_id": _sanitize(request_id),
            "post_runtime_hosting_ongoing_runtime_boundary_type": (
                "post_runtime_hosting_ongoing_runtime_boundary"
            ),
            "post_runtime_hosting_ongoing_runtime_boundary_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_ongoing_runtime_boundary_question": {
            "ongoing_runtime_boundary_request_id": _sanitize(request_id),
            "ongoing_runtime_boundary_question": _sanitize(
                request.get("ongoing_runtime_boundary_question")
            ),
            "ongoing_runtime_boundary_intent": _sanitize(
                request.get("ongoing_runtime_boundary_intent")
            ),
        },
        "selected_runtime_hosting_basis": _basis_detail(
            request,
            "selected_runtime_hosting_basis",
            "selected_runtime_hosting_result_outcome",
            "selected_runtime_hosting_result_version",
            "selected_runtime_hosting_failed_check_count",
            "selected_runtime_hosting_result_path",
        ),
        "selected_runtime_hosting_terminal_summary_basis": _basis_detail(
            request, "selected_runtime_hosting_terminal_summary_basis"
        ),
        "selected_runtime_hosting_boundary_v2_basis": _basis_detail(
            request,
            "selected_runtime_hosting_boundary_v2_basis",
            "selected_runtime_hosting_boundary_v2_result_outcome",
            "selected_runtime_hosting_boundary_v2_result_version",
            "selected_runtime_hosting_boundary_v2_failed_check_count",
            "selected_runtime_hosting_boundary_v2_result_path",
        ),
        "selected_runtime_hosting_boundary_v1_failure_lineage_basis": _basis_detail(
            request, "selected_runtime_hosting_boundary_v1_failure_lineage_basis"
        ),
        "selected_successor_runtime_step_basis": _basis_detail(
            request,
            "selected_successor_runtime_step_basis",
            "selected_successor_runtime_step_result_outcome",
            "selected_successor_runtime_step_result_version",
            "selected_successor_runtime_step_failed_check_count",
            "selected_successor_runtime_step_result_path",
        ),
        "selected_minimal_runtime_basis": _basis_detail(
            request,
            "selected_minimal_runtime_basis",
            "selected_minimal_runtime_result_outcome",
            "selected_minimal_runtime_result_version",
            "selected_minimal_runtime_failed_check_count",
            "selected_minimal_runtime_result_path",
        ),
        "selected_runtime_boundary_basis": _basis_detail(
            request,
            "selected_runtime_boundary_basis",
            "selected_runtime_boundary_result_outcome",
            "selected_runtime_boundary_result_version",
            "selected_runtime_boundary_failed_check_count",
            "selected_runtime_boundary_result_path",
        ),
        "selected_runtime_readiness_basis": _basis_detail(
            request,
            "selected_runtime_readiness_basis",
            "selected_runtime_readiness_result_outcome",
            "selected_runtime_readiness_result_version",
            "selected_runtime_readiness_failed_check_count",
            "selected_runtime_readiness_result_path",
        ),
        "selected_portable_verification_final_completion_basis": _basis_detail(
            request,
            "selected_portable_verification_final_completion_basis",
            "selected_portable_verification_final_completion_result_outcome",
            "selected_portable_verification_final_completion_result_version",
            "selected_portable_verification_final_completion_failed_check_count",
            "selected_portable_verification_final_completion_result_path",
        ),
        "selected_post_portable_verification_currentness_basis": _basis_detail(
            request,
            "selected_post_portable_verification_currentness_basis",
            path_field="selected_post_portable_currentness_surface_path",
        ),
        "selected_returned_second_carrier_capture_lineage_basis": _basis_detail(
            request, "selected_returned_second_carrier_capture_lineage_basis"
        ),
        "ongoing_runtime_boundary_spec_only_posture": _sanitize(
            request.get("ongoing_runtime_boundary_spec_only_posture")
        ),
        "one_future_ongoing_runtime_review_posture": _sanitize(
            request.get("one_future_ongoing_runtime_review_posture")
        ),
        "runtime_hosting_basis_preserved_posture": _sanitize(
            request.get("runtime_hosting_basis_preserved_posture")
        ),
        "runtime_hosting_not_ongoing_runtime_posture": _sanitize(
            request.get("runtime_hosting_not_ongoing_runtime_posture")
        ),
        "runtime_hosting_host_relation_not_continuous_runtime_posture": _sanitize(
            request.get("runtime_hosting_host_relation_not_continuous_runtime_posture")
        ),
        "ongoing_runtime_boundary_not_ongoing_runtime_posture": _sanitize(
            request.get("ongoing_runtime_boundary_not_ongoing_runtime_posture")
        ),
        "ongoing_runtime_boundary_not_reusable_runtime_permission_posture": _sanitize(
            request.get("ongoing_runtime_boundary_not_reusable_runtime_permission_posture")
        ),
        "ongoing_runtime_boundary_not_continuation_posture": _sanitize(
            request.get("ongoing_runtime_boundary_not_continuation_posture")
        ),
        "ongoing_runtime_not_created_posture": _sanitize(
            request.get("ongoing_runtime_not_created_posture")
        ),
        "reusable_runtime_permission_not_created_posture": _sanitize(
            request.get("reusable_runtime_permission_not_created_posture")
        ),
        "continuation_not_authorized_posture": _sanitize(
            request.get("continuation_not_authorized_posture")
        ),
        "self_continuation_not_authorized_posture": _sanitize(
            request.get("self_continuation_not_authorized_posture")
        ),
        "self_recursive_growth_not_created_posture": _sanitize(
            request.get("self_recursive_growth_not_created_posture")
        ),
        "runtime_daemon_not_created_posture": _sanitize(
            request.get("runtime_daemon_not_created_posture")
        ),
        "runtime_loop_not_created_posture": _sanitize(
            request.get("runtime_loop_not_created_posture")
        ),
        "public_api_not_created_posture": _sanitize(
            request.get("public_api_not_created_posture")
        ),
        "participant_facing_interface_not_created_posture": _sanitize(
            request.get("participant_facing_interface_not_created_posture")
        ),
        "distributed_network_behavior_not_created_posture": _sanitize(
            request.get("distributed_network_behavior_not_created_posture")
        ),
        "source_transfer_not_created_posture": _sanitize(
            request.get("source_transfer_not_created_posture")
        ),
        "source_receipt_not_created_posture": _sanitize(
            request.get("source_receipt_not_created_posture")
        ),
        "reception_authorization_not_created_posture": _sanitize(
            request.get("reception_authorization_not_created_posture")
        ),
        "source_not_created_posture": _sanitize(request.get("source_not_created_posture")),
        "authority_not_created_posture": _sanitize(
            request.get("authority_not_created_posture")
        ),
        "currentness_not_created_posture": _sanitize(
            request.get("currentness_not_created_posture")
        ),
        "deployment_not_created_posture": _sanitize(
            request.get("deployment_not_created_posture")
        ),
        "public_release_not_created_posture": _sanitize(
            request.get("public_release_not_created_posture")
        ),
        "operation_permission_not_created_posture": _sanitize(
            request.get("operation_permission_not_created_posture")
        ),
        "reusable_permission_not_created_posture": _sanitize(
            request.get("reusable_permission_not_created_posture")
        ),
        "follow_on_work_not_authorized_posture": _sanitize(
            request.get("follow_on_work_not_authorized_posture")
        ),
        "hidden_repo_state_excluded_posture": _sanitize(
            request.get("hidden_repo_state_excluded_posture")
        ),
        "repo_local_availability_not_ongoing_runtime_boundary_authority_posture": _sanitize(
            request.get(
                "repo_local_availability_not_ongoing_runtime_boundary_authority_posture"
            )
        ),
        "artifact_existence_not_ongoing_runtime_boundary_authority_posture": _sanitize(
            request.get("artifact_existence_not_ongoing_runtime_boundary_authority_posture")
        ),
        "latest_file_posture_not_ongoing_runtime_boundary_authority_posture": _sanitize(
            request.get("latest_file_posture_not_ongoing_runtime_boundary_authority_posture")
        ),
        "selected_basis_reference_shape_posture": _sanitize(
            request.get("selected_basis_reference_shape_posture")
        ),
        "raw_full_prior_artifact_body_not_returned_posture": _sanitize(
            request.get("raw_full_prior_artifact_body_not_returned_posture")
        ),
        "official_enum_scope_strings_not_redacted_posture": _sanitize(
            request.get("official_enum_scope_strings_not_redacted_posture")
        ),
        "hostile_raw_body_content_contained_posture": _sanitize(
            request.get("hostile_raw_body_content_contained_posture")
        ),
        "predecessor_failure_evidence_preserved_posture": _sanitize(
            request.get("predecessor_failure_evidence_preserved_posture")
        ),
        "result_level_non_claims_canonical_false_posture": _sanitize(
            request.get("result_level_non_claims_canonical_false_posture")
        ),
        "ongoing_runtime_boundary_scope": _sanitize(
            list(request.get("ongoing_runtime_boundary_scope", []))
        )
        if isinstance(request.get("ongoing_runtime_boundary_scope"), (list, tuple, set))
        else _sanitize(request.get("ongoing_runtime_boundary_scope")),
        "ongoing_runtime_boundary_checks": checks,
        "ongoing_runtime_boundary_statement": statement,
        "ongoing_runtime_boundary_non_meaning": _non_meaning(),
        "additional_basis_required": _sanitize(request.get("additional_basis_context", [])),
        "not_recorded_basis": _sanitize(request.get("not_recorded_basis", [])),
        "what_remains_open": _what_remains_open(),
        "non_claims": _canonical_false_non_claims(),
        "outcome": outcome,
        "block": block,
    }
    result["post_runtime_hosting_ongoing_runtime_boundary_summary"] = (
        build_post_runtime_hosting_ongoing_runtime_boundary_summary(result)
    )
    return result


def resolve_post_runtime_hosting_ongoing_runtime_boundary(
    declared_ongoing_runtime_boundary_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    malformed_code: str | None = None
    if declared_ongoing_runtime_boundary_request is None:
        request: Mapping[str, Any] = {}
        malformed_code = "DECLARED_ONGOING_RUNTIME_BOUNDARY_REQUEST_MALFORMED"
    elif not isinstance(declared_ongoing_runtime_boundary_request, Mapping):
        request = {}
        malformed_code = "DECLARED_ONGOING_RUNTIME_BOUNDARY_REQUEST_MALFORMED"
    else:
        request = deepcopy(dict(declared_ongoing_runtime_boundary_request))

    checks = _build_checks(request, malformed_code)
    first_failed_code = _first_failed_code(checks)
    if first_failed_code:
        outcome = OUTCOME_BLOCKED
    elif request.get("ongoing_runtime_boundary_intent") == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_RECORDED
    elif _is_declared(request.get("additional_basis_context")):
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
    elif _is_declared(request.get("not_recorded_basis")):
        outcome = OUTCOME_NOT_RECORDED
    else:
        outcome = OUTCOME_RECORDED

    return _build_result(request, checks, outcome, first_failed_code)


def resolve_post_runtime_hosting_ongoing_runtime_boundary_from_path(
    declared_ongoing_runtime_boundary_request_path: Path | str,
) -> dict[str, Any]:
    path = Path(declared_ongoing_runtime_boundary_request_path)
    try:
        loaded = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        checks = _build_checks({}, "DECLARED_ONGOING_RUNTIME_BOUNDARY_REQUEST_UNREADABLE")
        return _build_result(
            {},
            checks,
            OUTCOME_BLOCKED,
            "DECLARED_ONGOING_RUNTIME_BOUNDARY_REQUEST_UNREADABLE",
        )
    if not isinstance(loaded, Mapping):
        checks = _build_checks({}, "DECLARED_ONGOING_RUNTIME_BOUNDARY_REQUEST_MALFORMED")
        return _build_result(
            {},
            checks,
            OUTCOME_BLOCKED,
            "DECLARED_ONGOING_RUNTIME_BOUNDARY_REQUEST_MALFORMED",
        )
    return resolve_post_runtime_hosting_ongoing_runtime_boundary(loaded)


def _json_safe(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_safe(item) for item in value]
    if isinstance(value, Path):
        return str(value)
    return value


def _candidate_output_path(base_path: Path) -> Path:
    if not base_path.exists():
        return base_path
    stem = base_path.stem
    suffix = base_path.suffix
    parent = base_path.parent
    counter = 1
    while True:
        candidate = parent / f"{stem}_{counter:03d}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def write_post_runtime_hosting_ongoing_runtime_boundary_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    if not isinstance(result, Mapping):
        raise PostRuntimeHostingOngoingRuntimeBoundaryError("result must be a mapping")
    if output_path is None:
        question = result.get("declared_ongoing_runtime_boundary_question", {})
        request_id = _safe_get(question, "ongoing_runtime_boundary_request_id") or _DEFAULT_REQUEST_ID
        output_path = OUTPUT_ROOT / (
            f"{request_id}__post_runtime_hosting_ongoing_runtime_boundary_result.json"
        )
    path = _candidate_output_path(Path(output_path))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(_json_safe(result), indent=2, sort_keys=True, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    return path


def build_declared_post_runtime_hosting_ongoing_runtime_boundary_request(
    **overrides: Any,
) -> dict[str, Any]:
    posture_text = (
        "one bounded ongoing-runtime-boundary posture from clean runtime-hosting "
        "basis; one future ongoing-runtime review may be approached only by a "
        "separate bounded step"
    )
    request: dict[str, Any] = {
        "ongoing_runtime_boundary_request_id": _DEFAULT_REQUEST_ID,
        "ongoing_runtime_boundary_question": ONGOING_RUNTIME_BOUNDARY_QUESTION,
        "ongoing_runtime_boundary_intent": INTENT_RECORD,
        "selected_runtime_hosting_basis": {
            "path": "artifacts/integrity_host_v0_min_coexistence_post_successor_runtime_step_runtime_hosting/post_successor_runtime_step_runtime_hosting_reference_review_001__post_successor_runtime_step_runtime_hosting_result.json",
            "basis_kind": "standing runtime-hosting live artifact",
        },
        "selected_runtime_hosting_terminal_summary_basis": {
            "path": "spec/POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_TERMINAL_SUMMARY_V0.md",
            "basis_kind": "standing runtime-hosting terminal summary",
        },
        "selected_runtime_hosting_boundary_v2_basis": {
            "path": "artifacts/integrity_host_v0_min_coexistence_post_successor_runtime_step_runtime_hosting_boundary_v2/post_successor_runtime_step_runtime_hosting_boundary_v2_reference_review_001__post_successor_runtime_step_runtime_hosting_boundary_v2_result.json",
            "basis_kind": "standing runtime-hosting-boundary v2 live artifact",
        },
        "selected_runtime_hosting_boundary_v1_failure_lineage_basis": {
            "paths": [
                "src/resolve_post_successor_runtime_step_runtime_hosting_boundary.py",
                "tests/test_resolve_post_successor_runtime_step_runtime_hosting_boundary.py",
            ],
            "basis_kind": "preserved failed predecessor evidence",
            "repaired": False,
            "hidden": False,
            "claimed_passed": False,
        },
        "selected_successor_runtime_step_basis": {
            "path": "artifacts/integrity_host_v0_min_coexistence_post_minimal_runtime_successor_runtime_step/post_minimal_runtime_successor_runtime_step_reference_review_001__post_minimal_runtime_successor_runtime_step_result.json",
            "basis_kind": "standing successor-runtime-step live artifact",
        },
        "selected_minimal_runtime_basis": {
            "path": "artifacts/integrity_host_v0_min_coexistence_post_portable_verification_minimal_runtime/post_portable_verification_minimal_runtime_reference_review_001__post_portable_verification_minimal_runtime_result.json",
            "basis_kind": "standing minimal-runtime live artifact",
        },
        "selected_runtime_boundary_basis": {
            "path": "spec/POST_PORTABLE_VERIFICATION_RUNTIME_BOUNDARY_TERMINAL_SUMMARY_V0.md",
            "basis_kind": "standing runtime-boundary basis",
        },
        "selected_runtime_readiness_basis": {
            "path": "spec/POST_PORTABLE_VERIFICATION_RUNTIME_READINESS_TERMINAL_SUMMARY_V0.md",
            "basis_kind": "standing runtime-readiness basis",
        },
        "selected_portable_verification_final_completion_basis": {
            "path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_TERMINAL_SUMMARY_V0.md",
            "basis_kind": "standing final-completion basis",
        },
        "selected_post_portable_verification_currentness_basis": {
            "path": "spec/POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_V0.md",
            "basis_kind": "currentness-compression surface only",
        },
        "selected_returned_second_carrier_capture_lineage_basis": {
            "basis_kind": "lineage only",
            "creates_continuation": False,
        },
        "ongoing_runtime_boundary_spec_only_posture": _posture(posture_text),
        "one_future_ongoing_runtime_review_posture": _posture(
            "one future ongoing-runtime review declared only"
        ),
        "runtime_hosting_basis_preserved_posture": _posture(
            "runtime-hosting basis preserved"
        ),
        "runtime_hosting_not_ongoing_runtime_posture": _posture(
            "runtime hosting remains not ongoing runtime"
        ),
        "runtime_hosting_host_relation_not_continuous_runtime_posture": _posture(
            "runtime-hosting host relation remains non-continuous runtime"
        ),
        "ongoing_runtime_boundary_not_ongoing_runtime_posture": _posture(
            "ongoing-runtime boundary is not ongoing runtime"
        ),
        "ongoing_runtime_boundary_not_reusable_runtime_permission_posture": _posture(
            "ongoing-runtime boundary is not reusable runtime permission"
        ),
        "ongoing_runtime_boundary_not_continuation_posture": _posture(
            "ongoing-runtime boundary is not continuation"
        ),
        "ongoing_runtime_not_created_posture": _posture("ongoing runtime not created"),
        "reusable_runtime_permission_not_created_posture": _posture(
            "reusable runtime permission not created"
        ),
        "continuation_not_authorized_posture": _posture("continuation not authorized"),
        "self_continuation_not_authorized_posture": _posture(
            "self-continuation not authorized"
        ),
        "self_recursive_growth_not_created_posture": _posture(
            "self-recursive growth not created"
        ),
        "runtime_daemon_not_created_posture": _posture("runtime daemon not created"),
        "runtime_loop_not_created_posture": _posture("runtime loop not created"),
        "public_api_not_created_posture": _posture("public API not created"),
        "participant_facing_interface_not_created_posture": _posture(
            "participant-facing interface not created"
        ),
        "distributed_network_behavior_not_created_posture": _posture(
            "distributed network behavior not created"
        ),
        "source_transfer_not_created_posture": _posture("source transfer not created"),
        "source_receipt_not_created_posture": _posture("source receipt not created"),
        "reception_authorization_not_created_posture": _posture(
            "reception authorization not created"
        ),
        "source_not_created_posture": _posture("source not created"),
        "authority_not_created_posture": _posture("authority not created"),
        "currentness_not_created_posture": _posture("currentness not created"),
        "deployment_not_created_posture": _posture("deployment not created"),
        "public_release_not_created_posture": _posture("public release not created"),
        "operation_permission_not_created_posture": _posture(
            "operation permission not created"
        ),
        "reusable_permission_not_created_posture": _posture(
            "reusable permission not created"
        ),
        "follow_on_work_not_authorized_posture": _posture(
            "follow-on work not authorized"
        ),
        "hidden_repo_state_excluded_posture": _posture("hidden repo state excluded"),
        "repo_local_availability_not_ongoing_runtime_boundary_authority_posture": _posture(
            "repo-local availability is not ongoing-runtime-boundary authority"
        ),
        "artifact_existence_not_ongoing_runtime_boundary_authority_posture": _posture(
            "artifact existence is not ongoing-runtime-boundary authority"
        ),
        "latest_file_posture_not_ongoing_runtime_boundary_authority_posture": _posture(
            "latest file posture is not ongoing-runtime-boundary authority"
        ),
        "selected_basis_reference_shape_posture": _posture(
            "selected basis remains reference-shaped"
        ),
        "raw_full_prior_artifact_body_not_returned_posture": _posture(
            "raw full prior artifact body not returned"
        ),
        "official_enum_scope_strings_not_redacted_posture": _posture(
            "official enum, scope, and block-code strings are not redacted"
        ),
        "hostile_raw_body_content_contained_posture": _posture(
            "hostile raw body content contained"
        ),
        "predecessor_failure_evidence_preserved_posture": _posture(
            "predecessor failure evidence preserved"
        ),
        "result_level_non_claims_canonical_false_posture": _posture(
            "result-level non-claims canonical false"
        ),
        "ongoing_runtime_boundary_scope": list(SUPPORTED_SCOPE_VALUES),
        "declared_non_claims": _canonical_false_non_claims(),
        "selected_runtime_hosting_result_path": "artifacts/integrity_host_v0_min_coexistence_post_successor_runtime_step_runtime_hosting/post_successor_runtime_step_runtime_hosting_reference_review_001__post_successor_runtime_step_runtime_hosting_result.json",
        "selected_runtime_hosting_result_outcome": "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_RECORDED",
        "selected_runtime_hosting_result_version": "0.1.0",
        "selected_runtime_hosting_failed_check_count": 0,
        "selected_runtime_hosting_bounded_runtime_hosting_posture_recorded": True,
        "selected_runtime_hosting_bounded_host_relation_recorded": True,
        "selected_runtime_hosting_host_relation_ran_continuously": False,
        "selected_runtime_hosting_host_relation_created_active_execution": False,
        "selected_runtime_hosting_host_relation_authorized_follow_on_work": False,
        "selected_runtime_hosting_already_created_ongoing_runtime": False,
        "selected_runtime_hosting_already_created_reusable_runtime_permission": False,
        "selected_runtime_hosting_already_authorized_continuation": False,
        "selected_runtime_hosting_already_authorized_self_continuation": False,
        "selected_runtime_hosting_already_created_runtime_daemon": False,
        "selected_runtime_hosting_already_created_runtime_loop": False,
        "selected_runtime_hosting_already_created_public_api": False,
        "selected_runtime_hosting_already_created_participant_facing_interface": False,
        "selected_runtime_hosting_already_created_distributed_network_behavior": False,
        "selected_runtime_hosting_treated_as_ongoing_runtime": False,
        "selected_runtime_hosting_treated_as_reusable_runtime_permission": False,
        "selected_runtime_hosting_treated_as_continuation": False,
        "selected_runtime_hosting_treated_as_self_continuation": False,
        "selected_runtime_hosting_treated_as_runtime_daemon": False,
        "selected_runtime_hosting_treated_as_runtime_loop": False,
        "selected_runtime_hosting_treated_as_public_api": False,
        "selected_runtime_hosting_treated_as_participant_facing_interface": False,
        "selected_runtime_hosting_treated_as_distributed_network_behavior": False,
        "selected_runtime_hosting_authorized_future_work": False,
        "selected_runtime_hosting_non_claims_canonicalized": True,
        "selected_runtime_hosting_boundary_v2_result_path": "artifacts/integrity_host_v0_min_coexistence_post_successor_runtime_step_runtime_hosting_boundary_v2/post_successor_runtime_step_runtime_hosting_boundary_v2_reference_review_001__post_successor_runtime_step_runtime_hosting_boundary_v2_result.json",
        "selected_runtime_hosting_boundary_v2_result_outcome": "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_BOUNDARY_RECORDED",
        "selected_runtime_hosting_boundary_v2_result_version": "0.2.0",
        "selected_runtime_hosting_boundary_v2_failed_check_count": 0,
        "selected_runtime_hosting_boundary_v1_failure_repaired": False,
        "selected_runtime_hosting_boundary_v1_failure_hidden": False,
        "selected_runtime_hosting_boundary_v1_failure_claimed_passed": False,
        "selected_successor_runtime_step_result_path": "artifacts/integrity_host_v0_min_coexistence_post_minimal_runtime_successor_runtime_step/post_minimal_runtime_successor_runtime_step_reference_review_001__post_minimal_runtime_successor_runtime_step_result.json",
        "selected_successor_runtime_step_result_outcome": "POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_RECORDED",
        "selected_successor_runtime_step_result_version": "0.1.0",
        "selected_successor_runtime_step_failed_check_count": 0,
        "selected_minimal_runtime_result_path": "artifacts/integrity_host_v0_min_coexistence_post_portable_verification_minimal_runtime/post_portable_verification_minimal_runtime_reference_review_001__post_portable_verification_minimal_runtime_result.json",
        "selected_minimal_runtime_result_outcome": "POST_PORTABLE_VERIFICATION_MINIMAL_RUNTIME_RECORDED",
        "selected_minimal_runtime_result_version": "0.1.0",
        "selected_minimal_runtime_failed_check_count": 0,
        "selected_runtime_boundary_result_path": "spec/POST_PORTABLE_VERIFICATION_RUNTIME_BOUNDARY_TERMINAL_SUMMARY_V0.md",
        "selected_runtime_boundary_result_outcome": "POST_PORTABLE_VERIFICATION_RUNTIME_BOUNDARY_RECORDED",
        "selected_runtime_boundary_result_version": "0.1.0",
        "selected_runtime_boundary_failed_check_count": 0,
        "selected_runtime_readiness_result_path": "spec/POST_PORTABLE_VERIFICATION_RUNTIME_READINESS_TERMINAL_SUMMARY_V0.md",
        "selected_runtime_readiness_result_outcome": "POST_PORTABLE_VERIFICATION_RUNTIME_READINESS_RECORDED",
        "selected_runtime_readiness_result_version": "0.1.0",
        "selected_runtime_readiness_failed_check_count": 0,
        "selected_portable_verification_final_completion_result_path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_TERMINAL_SUMMARY_V0.md",
        "selected_portable_verification_final_completion_result_outcome": "PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_RECORDED",
        "selected_portable_verification_final_completion_result_version": "0.1.0",
        "selected_portable_verification_final_completion_failed_check_count": 0,
        "selected_post_portable_currentness_surface_path": "spec/POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_V0.md",
        "selected_post_portable_currentness_surface_states_checkability_not_continuation": True,
        "selected_post_portable_currentness_surface_authorized_next_work": False,
        "ongoing_runtime_boundary_created_before_review": False,
        "ongoing_runtime_created": False,
        "reusable_runtime_permission_created": False,
        "continuation_authorized": False,
        "self_continuation_authorized": False,
        "self_recursive_growth_created": False,
        "runtime_daemon_created": False,
        "runtime_loop_created": False,
        "public_api_created": False,
        "participant_facing_interface_created": False,
        "distributed_network_behavior_created": False,
        "ongoing_runtime_boundary_treated_as_ongoing_runtime": False,
        "ongoing_runtime_boundary_treated_as_reusable_runtime_permission": False,
        "ongoing_runtime_boundary_treated_as_continuation": False,
        "ongoing_runtime_boundary_treated_as_self_continuation": False,
        "reference_shaped_input_posture": True,
        "additional_basis_context": [],
        "not_recorded_basis": [],
    }
    for key in REQUIRED_FALSE_NON_CLAIMS:
        request.setdefault(key, False)
    request.update(deepcopy(overrides))
    return request
