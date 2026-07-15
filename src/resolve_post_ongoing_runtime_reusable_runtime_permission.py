"""Bounded post-ongoing-runtime reusable-runtime-permission resolver.

This resolver is downstream of the reusable-runtime-permission-boundary line.
It records one bounded reusable-runtime-permission posture and one bounded
runtime-reuse envelope only. Reusable runtime permission here is not
continuation, self-continuation, self-recursive growth, daemon, loop, public
API, participant-facing interface, distributed network behavior, source
transfer, source receipt, reception authorization, source, authority,
currentness, deployment, public release, operation permission, broader
reusable permission, derivative reception, vessel relation, adoption,
receiving-context governance, publication flow, or follow-on work.
"""

from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any


class PostOngoingRuntimeReusableRuntimePermissionError(Exception):
    """Bounded resolver error for reusable-runtime-permission handling."""


def _tokens(value: str) -> tuple[str, ...]:
    return tuple(value.split())


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_post_ongoing_runtime_reusable_runtime_permission"

OUTCOME_RECORDED = "POST_ONGOING_RUNTIME_REUSABLE_RUNTIME_PERMISSION_RECORDED"
OUTCOME_NOT_RECORDED = "POST_ONGOING_RUNTIME_REUSABLE_RUNTIME_PERMISSION_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "POST_ONGOING_RUNTIME_REUSABLE_RUNTIME_PERMISSION_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "POST_ONGOING_RUNTIME_REUSABLE_RUNTIME_PERMISSION_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = "RECORD_POST_ONGOING_RUNTIME_REUSABLE_RUNTIME_PERMISSION"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_POST_ONGOING_RUNTIME_REUSABLE_RUNTIME_PERMISSION"
INTENT_BLOCK = "BLOCK_POST_ONGOING_RUNTIME_REUSABLE_RUNTIME_PERMISSION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_post_ongoing_runtime_"
    "reusable_runtime_permission"
)

CORE_QUESTION = (
    "Can the clean post-ongoing-runtime reusable-runtime-permission-boundary "
    "basis be used to record one bounded reusable-runtime-permission posture "
    "without authorizing continuation, self-continuation, self-recursive "
    "growth, runtime daemon, runtime loop, public API, participant-facing "
    "interface, distributed network behavior, source transfer, source receipt, "
    "reception authorization, source, authority, currentness, deployment, "
    "public release, operation permission, broader reusable permission, "
    "derivative reception, vessel relation, another reception request, "
    "adoption, receiving-context governance, publication flow, or follow-on "
    "work?"
)

EXPECTED_REUSABLE_RUNTIME_PERMISSION_BOUNDARY_OUTCOME = (
    "POST_ONGOING_RUNTIME_REUSABLE_RUNTIME_PERMISSION_BOUNDARY_RECORDED"
)
EXPECTED_ONGOING_RUNTIME_OUTCOME = "POST_RUNTIME_HOSTING_ONGOING_RUNTIME_RECORDED"
EXPECTED_ONGOING_RUNTIME_BOUNDARY_OUTCOME = (
    "POST_RUNTIME_HOSTING_ONGOING_RUNTIME_BOUNDARY_RECORDED"
)
EXPECTED_RUNTIME_HOSTING_OUTCOME = "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_RECORDED"
EXPECTED_RUNTIME_HOSTING_BOUNDARY_V2_OUTCOME = (
    "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_BOUNDARY_RECORDED"
)
EXPECTED_SUCCESSOR_RUNTIME_STEP_OUTCOME = (
    "POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_RECORDED"
)
EXPECTED_MINIMAL_RUNTIME_OUTCOME = "POST_PORTABLE_VERIFICATION_MINIMAL_RUNTIME_RECORDED"
EXPECTED_RUNTIME_BOUNDARY_OUTCOME = "POST_PORTABLE_VERIFICATION_RUNTIME_BOUNDARY_RECORDED"
EXPECTED_RUNTIME_READINESS_OUTCOME = (
    "POST_PORTABLE_VERIFICATION_RUNTIME_READINESS_RECORDED"
)
EXPECTED_FINAL_COMPLETION_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_RECORDED"
)

SUPPORTED_SCOPE_VALUES = _tokens(
    """
    REUSABLE_RUNTIME_PERMISSION_SPEC_ONLY
    ONE_BOUNDED_REUSABLE_RUNTIME_PERMISSION_POSTURE_RECORDED
    REUSABLE_RUNTIME_PERMISSION_BOUNDARY_BASIS_PRESERVED
    ONGOING_RUNTIME_BASIS_PRESERVED
    ONGOING_RUNTIME_PERSISTENCE_NOT_REPEATABILITY_WITHOUT_PERMISSION
    BOUNDED_RUNTIME_REUSE_ENVELOPE_DECLARED
    REUSABLE_RUNTIME_PERMISSION_NOT_CONTINUATION
    REUSABLE_RUNTIME_PERMISSION_NOT_SELF_CONTINUATION
    REUSABLE_RUNTIME_PERMISSION_NOT_DAEMON
    REUSABLE_RUNTIME_PERMISSION_NOT_LOOP
    REUSABLE_RUNTIME_PERMISSION_NOT_PUBLIC_API
    REUSABLE_RUNTIME_PERMISSION_NOT_PARTICIPANT_FACING_INTERFACE
    REUSABLE_RUNTIME_PERMISSION_NOT_DISTRIBUTED_NETWORK_BEHAVIOR
    NO_CONTINUATION_AUTHORIZED
    SELF_CONTINUATION_NOT_AUTHORIZED
    SELF_RECURSIVE_GROWTH_NOT_CREATED
    RUNTIME_DAEMON_NOT_CREATED
    RUNTIME_LOOP_NOT_CREATED
    PUBLIC_API_NOT_CREATED
    PARTICIPANT_FACING_INTERFACE_NOT_CREATED
    DISTRIBUTED_NETWORK_BEHAVIOR_NOT_CREATED
    NO_SOURCE_TRANSFER
    NO_SOURCE_RECEIPT
    NO_RECEPTION_AUTHORIZATION
    NO_SOURCE_CREATED
    NO_AUTHORITY_CREATED
    NO_CURRENTNESS_CREATED
    NO_DEPLOYMENT_CREATED
    NO_PUBLIC_RELEASE_CREATED
    NO_OPERATION_PERMISSION_CREATED
    NO_BROADER_REUSABLE_PERMISSION
    NO_DERIVATIVE_RECEPTION
    NO_VESSEL_RELATION
    NO_ANOTHER_RECEPTION_REQUEST
    NO_ADOPTION
    NO_RECEIVING_CONTEXT_GOVERNANCE
    NO_PUBLICATION_FLOW
    NO_FOLLOW_ON_WORK_AUTHORIZED
    NO_CONTINUATION_INFERENCE
    NO_SELF_CONTINUATION_INFERENCE
    NO_DAEMON_INFERENCE
    NO_LOOP_INFERENCE
    NO_PUBLIC_API_INFERENCE
    NO_PARTICIPANT_INTERFACE_INFERENCE
    NO_DISTRIBUTED_NETWORK_INFERENCE
    NO_SOURCE_INFERENCE
    NO_AUTHORITY_INFERENCE
    NO_CURRENTNESS_INFERENCE
    NO_DEPLOYMENT_INFERENCE
    NO_PUBLIC_RELEASE_INFERENCE
    NO_OPERATION_PERMISSION_INFERENCE
    NO_FOLLOW_ON_WORK_INFERENCE
    NO_UNBOUNDED_PASS_FAIL_INFERENCE
    HIDDEN_REPO_STATE_EXCLUDED
    HIDDEN_REPO_STATE_NOT_USED_AS_REUSABLE_RUNTIME_PERMISSION_AUTHORITY
    REPO_LOCAL_AVAILABILITY_NOT_REUSABLE_RUNTIME_PERMISSION_AUTHORITY
    ARTIFACT_EXISTENCE_NOT_REUSABLE_RUNTIME_PERMISSION_AUTHORITY
    LATEST_FILE_POSTURE_NOT_REUSABLE_RUNTIME_PERMISSION_AUTHORITY
    SELECTED_BASIS_REFERENCE_SHAPE_PRESERVED
    RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED
    OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED
    HOSTILE_RAW_BODY_CONTENT_CONTAINED
    PREDECESSOR_FAILURE_EVIDENCE_PRESERVED
    AUTHORIZATION_TOKEN_REUSE_BLOCKED
    CONSUMED_REQUEST_TOKEN_REMAINS_CLOSED
    CONSUMED_REQUEST_NOT_REOPENED
    RESULT_LEVEL_NON_CLAIMS_CANONICAL_FALSE
    """
)
SUPPORTED_REUSABLE_RUNTIME_PERMISSION_SCOPE = SUPPORTED_SCOPE_VALUES

REQUIRED_FALSE_NON_CLAIMS = _tokens(
    """
    continuation_authorized
    self_continuation_authorized
    self_recursive_growth_created
    runtime_daemon_created
    runtime_loop_created
    public_api_created
    participant_facing_interface_created
    distributed_network_behavior_created
    source_transfer_occurred
    source_receipt_occurred
    reception_authorization_created
    reusable_runtime_permission_treated_as_continuation
    reusable_runtime_permission_treated_as_self_continuation
    reusable_runtime_permission_treated_as_self_recursive_growth
    reusable_runtime_permission_treated_as_runtime_daemon
    reusable_runtime_permission_treated_as_runtime_loop
    reusable_runtime_permission_treated_as_public_api
    reusable_runtime_permission_treated_as_participant_facing_interface
    reusable_runtime_permission_treated_as_distributed_network_behavior
    reusable_runtime_permission_treated_as_source_transfer
    reusable_runtime_permission_treated_as_source_receipt
    reusable_runtime_permission_treated_as_reception_authorization
    reusable_runtime_permission_treated_as_source
    reusable_runtime_permission_treated_as_authority
    reusable_runtime_permission_treated_as_currentness
    reusable_runtime_permission_treated_as_deployment
    reusable_runtime_permission_treated_as_public_release
    reusable_runtime_permission_treated_as_operation_permission
    reusable_runtime_permission_treated_as_broader_reusable_permission
    reusable_runtime_permission_treated_as_follow_on_work
    reusable_runtime_permission_boundary_treated_as_reusable_runtime_permission_without_review
    ongoing_runtime_treated_as_reusable_runtime_permission_without_review
    ongoing_runtime_persistence_treated_as_unbounded_repeatability
    artifact_existence_treated_as_reusable_runtime_permission_authority
    artifact_path_treated_as_currentness
    latest_file_posture_treated_as_reusable_runtime_permission_authority
    repo_local_availability_treated_as_reusable_runtime_permission_authority
    hidden_repo_state_used_as_reusable_runtime_permission_content
    hidden_repo_state_used_as_reusable_runtime_permission_authority
    source_created
    authority_created
    currentness_created
    deployment_created
    public_release_created
    operation_permission_created
    broader_reusable_permission_created
    derivative_reception_authorized
    vessel_relation_authorized
    another_reception_request_authorized
    adoption_created
    receiving_context_governance_created
    publication_flow_created
    follow_on_work_authorized
    raw_full_prior_artifact_body_returned
    prior_artifacts_mutated
    consumed_request_reopened
    authorization_token_reused
    predecessor_failure_repaired
    predecessor_failure_hidden
    predecessor_failure_claimed_passed
    reusable_runtime_permission_created_before_review
    runtime_hosting_boundary_v1_failure_repaired
    runtime_hosting_boundary_v1_failure_hidden
    runtime_hosting_boundary_v1_failure_claimed_passed
    """
)

ALLOWED_TRUE_RECORDED_FIELDS = _tokens(
    """
    reusable_runtime_permission_recorded
    bounded_reusable_runtime_permission_posture_recorded
    reusable_runtime_permission_boundary_basis_preserved
    ongoing_runtime_basis_preserved
    ongoing_runtime_persistence_not_repeatability_without_permission
    bounded_runtime_reuse_envelope_declared
    reusable_runtime_permission_not_continuation
    reusable_runtime_permission_not_self_continuation
    reusable_runtime_permission_not_daemon
    reusable_runtime_permission_not_loop
    reusable_runtime_permission_not_public_api
    reusable_runtime_permission_not_participant_facing_interface
    reusable_runtime_permission_not_distributed_network_behavior
    continuation_not_authorized
    self_continuation_not_authorized
    self_recursive_growth_not_created
    runtime_daemon_not_created
    runtime_loop_not_created
    public_api_not_created
    participant_facing_interface_not_created
    distributed_network_behavior_not_created
    source_transfer_not_created
    source_receipt_not_created
    reception_authorization_not_created
    source_not_created
    authority_not_created
    currentness_not_created
    deployment_not_created
    public_release_not_created
    operation_permission_not_created
    broader_reusable_permission_not_created
    follow_on_work_not_authorized
    hidden_repo_state_excluded
    hidden_repo_state_not_used_as_reusable_runtime_permission_authority
    repo_local_availability_not_reusable_runtime_permission_authority
    artifact_existence_not_reusable_runtime_permission_authority
    latest_file_posture_not_reusable_runtime_permission_authority
    selected_basis_reference_shape_preserved
    raw_full_prior_artifact_body_not_returned
    official_enum_scope_strings_not_redacted
    hostile_raw_body_content_contained
    predecessor_failure_evidence_preserved
    authorization_token_reuse_blocked
    consumed_request_token_remains_closed
    result_level_non_claims_canonical_false
    """
)

BLOCK_CODES = _tokens(
    """
    REUSABLE_RUNTIME_PERMISSION_QUESTION_UNDECLARED
    REUSABLE_RUNTIME_PERMISSION_INTENT_UNSUPPORTED
    REUSABLE_RUNTIME_PERMISSION_EXPLICIT_BLOCK_REQUESTED
    REUSABLE_RUNTIME_PERMISSION_BOUNDARY_BASIS_MISSING
    REUSABLE_RUNTIME_PERMISSION_BOUNDARY_NOT_RECORDED
    REUSABLE_RUNTIME_PERMISSION_BOUNDARY_FAILED_CHECKS_PRESENT
    REUSABLE_RUNTIME_PERMISSION_BOUNDARY_VERSION_NOT_0_1_0
    REUSABLE_RUNTIME_PERMISSION_BOUNDARY_DID_NOT_DECLARE_FUTURE_REUSABLE_RUNTIME_PERMISSION_REVIEW
    REUSABLE_RUNTIME_PERMISSION_BOUNDARY_ALREADY_CREATED_REUSABLE_RUNTIME_PERMISSION
    REUSABLE_RUNTIME_PERMISSION_BOUNDARY_ALREADY_AUTHORIZED_CONTINUATION
    REUSABLE_RUNTIME_PERMISSION_BOUNDARY_ALREADY_AUTHORIZED_SELF_CONTINUATION
    REUSABLE_RUNTIME_PERMISSION_BOUNDARY_ALREADY_CREATED_RUNTIME_DAEMON
    REUSABLE_RUNTIME_PERMISSION_BOUNDARY_ALREADY_CREATED_RUNTIME_LOOP
    REUSABLE_RUNTIME_PERMISSION_BOUNDARY_ALREADY_CREATED_PUBLIC_API
    REUSABLE_RUNTIME_PERMISSION_BOUNDARY_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE
    REUSABLE_RUNTIME_PERMISSION_BOUNDARY_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR
    REUSABLE_RUNTIME_PERMISSION_BOUNDARY_TREATED_AS_REUSABLE_RUNTIME_PERMISSION
    REUSABLE_RUNTIME_PERMISSION_BOUNDARY_TREATED_AS_CONTINUATION
    REUSABLE_RUNTIME_PERMISSION_BOUNDARY_TREATED_AS_SELF_CONTINUATION
    REUSABLE_RUNTIME_PERMISSION_BOUNDARY_AUTHORIZED_FUTURE_WORK
    ONGOING_RUNTIME_BASIS_MISSING
    ONGOING_RUNTIME_NOT_RECORDED
    ONGOING_RUNTIME_FAILED_CHECKS_PRESENT
    ONGOING_RUNTIME_VERSION_NOT_0_1_0
    ONGOING_RUNTIME_DID_NOT_RECORD_BOUNDED_ONGOING_RUNTIME_POSTURE
    ONGOING_RUNTIME_DID_NOT_RECORD_BOUNDED_PERSISTENCE_POSTURE
    ONGOING_RUNTIME_PERSISTENCE_TREATED_AS_REPEATABILITY_BEFORE_PERMISSION
    ONGOING_RUNTIME_PERSISTENCE_AUTHORIZED_REUSE_BEFORE_PERMISSION
    ONGOING_RUNTIME_ALREADY_AUTHORIZED_CONTINUATION
    ONGOING_RUNTIME_ALREADY_AUTHORIZED_SELF_CONTINUATION
    ONGOING_RUNTIME_BOUNDARY_BASIS_MISSING
    ONGOING_RUNTIME_BOUNDARY_NOT_RECORDED
    ONGOING_RUNTIME_BOUNDARY_VERSION_NOT_0_1_0
    ONGOING_RUNTIME_BOUNDARY_FAILED_CHECKS_PRESENT
    RUNTIME_HOSTING_BASIS_MISSING
    RUNTIME_HOSTING_NOT_RECORDED
    RUNTIME_HOSTING_VERSION_NOT_0_1_0
    RUNTIME_HOSTING_FAILED_CHECKS_PRESENT
    RUNTIME_HOSTING_BOUNDARY_V2_BASIS_MISSING
    RUNTIME_HOSTING_BOUNDARY_V2_NOT_RECORDED
    RUNTIME_HOSTING_BOUNDARY_V2_VERSION_NOT_0_2_0
    RUNTIME_HOSTING_BOUNDARY_V2_FAILED_CHECKS_PRESENT
    RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED
    SUCCESSOR_RUNTIME_STEP_BASIS_MISSING
    SUCCESSOR_RUNTIME_STEP_NOT_RECORDED
    SUCCESSOR_RUNTIME_STEP_VERSION_NOT_0_1_0
    SUCCESSOR_RUNTIME_STEP_FAILED_CHECKS_PRESENT
    MINIMAL_RUNTIME_BASIS_MISSING
    MINIMAL_RUNTIME_NOT_RECORDED
    MINIMAL_RUNTIME_VERSION_NOT_0_1_0
    MINIMAL_RUNTIME_FAILED_CHECKS_PRESENT
    RUNTIME_BOUNDARY_BASIS_MISSING
    RUNTIME_BOUNDARY_NOT_RECORDED
    RUNTIME_BOUNDARY_VERSION_NOT_0_1_0
    RUNTIME_BOUNDARY_FAILED_CHECKS_PRESENT
    RUNTIME_READINESS_BASIS_MISSING
    RUNTIME_READINESS_NOT_RECORDED
    RUNTIME_READINESS_VERSION_NOT_0_1_0
    RUNTIME_READINESS_FAILED_CHECKS_PRESENT
    FINAL_COMPLETION_BASIS_MISSING
    FINAL_COMPLETION_NOT_RECORDED
    FINAL_COMPLETION_VERSION_NOT_0_1_0
    FINAL_COMPLETION_FAILED_CHECKS_PRESENT
    CURRENTNESS_SURFACE_BASIS_MISSING
    CURRENTNESS_SURFACE_TREATED_CHECKABILITY_AS_CONTINUATION
    CURRENTNESS_SURFACE_AUTHORIZED_NEXT_WORK
    REUSABLE_RUNTIME_PERMISSION_CREATED_BEFORE_REVIEW
    REUSABLE_RUNTIME_PERMISSION_TREATED_AS_CONTINUATION
    REUSABLE_RUNTIME_PERMISSION_TREATED_AS_SELF_CONTINUATION
    REUSABLE_RUNTIME_PERMISSION_TREATED_AS_SELF_RECURSIVE_GROWTH
    REUSABLE_RUNTIME_PERMISSION_TREATED_AS_RUNTIME_DAEMON
    REUSABLE_RUNTIME_PERMISSION_TREATED_AS_RUNTIME_LOOP
    REUSABLE_RUNTIME_PERMISSION_TREATED_AS_PUBLIC_API
    REUSABLE_RUNTIME_PERMISSION_TREATED_AS_PARTICIPANT_FACING_INTERFACE
    REUSABLE_RUNTIME_PERMISSION_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR
    REUSABLE_RUNTIME_PERMISSION_TREATED_AS_SOURCE_TRANSFER
    REUSABLE_RUNTIME_PERMISSION_TREATED_AS_SOURCE_RECEIPT
    REUSABLE_RUNTIME_PERMISSION_TREATED_AS_RECEPTION_AUTHORIZATION
    REUSABLE_RUNTIME_PERMISSION_TREATED_AS_SOURCE
    REUSABLE_RUNTIME_PERMISSION_TREATED_AS_AUTHORITY
    REUSABLE_RUNTIME_PERMISSION_TREATED_AS_CURRENTNESS
    REUSABLE_RUNTIME_PERMISSION_TREATED_AS_DEPLOYMENT
    REUSABLE_RUNTIME_PERMISSION_TREATED_AS_PUBLIC_RELEASE
    REUSABLE_RUNTIME_PERMISSION_TREATED_AS_OPERATION_PERMISSION
    REUSABLE_RUNTIME_PERMISSION_TREATED_AS_BROADER_REUSABLE_PERMISSION
    REUSABLE_RUNTIME_PERMISSION_TREATED_AS_FOLLOW_ON_WORK
    CONTINUATION_AUTHORIZED
    SELF_CONTINUATION_AUTHORIZED
    SELF_RECURSIVE_GROWTH_CREATED
    RUNTIME_DAEMON_CREATED
    RUNTIME_LOOP_CREATED
    PUBLIC_API_CREATED
    PARTICIPANT_FACING_INTERFACE_CREATED
    DISTRIBUTED_NETWORK_BEHAVIOR_CREATED
    SOURCE_TRANSFER_OCCURRED
    SOURCE_RECEIPT_OCCURRED
    RECEPTION_AUTHORIZATION_CREATED
    SOURCE_CREATED
    AUTHORITY_CREATED
    CURRENTNESS_CREATED
    DEPLOYMENT_CREATED
    PUBLIC_RELEASE_CREATED
    OPERATION_PERMISSION_CREATED
    BROADER_REUSABLE_PERMISSION_CREATED
    DERIVATIVE_RECEPTION_AUTHORIZED
    VESSEL_RELATION_AUTHORIZED
    ADOPTION_CREATED
    RECEIVING_CONTEXT_GOVERNANCE_CREATED
    PUBLICATION_FLOW_CREATED
    FOLLOW_ON_WORK_AUTHORIZED
    ARTIFACT_EXISTENCE_TREATED_AS_REUSABLE_RUNTIME_PERMISSION_AUTHORITY
    ARTIFACT_PATH_TREATED_AS_CURRENTNESS
    LATEST_FILE_POSTURE_TREATED_AS_REUSABLE_RUNTIME_PERMISSION_AUTHORITY
    REPO_LOCAL_AVAILABILITY_TREATED_AS_REUSABLE_RUNTIME_PERMISSION_AUTHORITY
    HIDDEN_REPO_STATE_USED_AS_REUSABLE_RUNTIME_PERMISSION_CONTENT
    HIDDEN_REPO_STATE_USED_AS_REUSABLE_RUNTIME_PERMISSION_AUTHORITY
    SELECTED_BASIS_NOT_REFERENCE_SHAPED
    RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED
    PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED
    CONSUMED_REQUEST_REOPENED
    AUTHORIZATION_TOKEN_REUSED
    REUSABLE_RUNTIME_PERMISSION_REQUIRED_POSTURE_MISSING
    NON_CLAIM_MISSING_OR_FLIPPED
    UNSUPPORTED_REUSABLE_RUNTIME_PERMISSION_SCOPE
    DECLARED_REUSABLE_RUNTIME_PERMISSION_REQUEST_MALFORMED
    DECLARED_REUSABLE_RUNTIME_PERMISSION_REQUEST_UNREADABLE
    """
)

_DEFAULT_REQUEST_ID = "post_ongoing_runtime_reusable_runtime_permission_reference_review_001"
_REDACTED_RAW_OR_HIDDEN_STATE = "[bounded-redacted-raw-or-hidden-state]"
_REDACTED_PERMISSION_PLACEHOLDER = "[bounded-reusable-runtime-permission-redacted]"

_SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_reusable_runtime_permission_body",
    "raw_bounded_runtime_reuse_envelope_body",
    "raw_runtime_reuse_body",
    "raw_continuation_body",
    "raw_self_continuation_body",
    "raw_runtime_daemon_body",
    "raw_runtime_loop_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "raw_runtime_body",
    "reusable_runtime_permission_body",
    "bounded_runtime_reuse_envelope_body",
    "runtime_reuse_body",
    "runtime_body",
    "source_body",
    "authority_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
}

_HOSTILE_SENTINELS = (
    "RAW_REUSABLE_RUNTIME_PERMISSION_BODY_MUST_NOT_RETURN",
    "RAW_BOUNDED_RUNTIME_REUSE_ENVELOPE_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_REUSE_BODY_MUST_NOT_RETURN",
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

_POSTURE_FIELDS = _tokens(
    """
    reusable_runtime_permission_spec_only_posture
    one_bounded_reusable_runtime_permission_posture
    reusable_runtime_permission_boundary_basis_preserved_posture
    ongoing_runtime_basis_preserved_posture
    ongoing_runtime_persistence_not_repeatability_without_permission_posture
    bounded_runtime_reuse_envelope_declared_posture
    reusable_runtime_permission_not_continuation_posture
    reusable_runtime_permission_not_self_continuation_posture
    reusable_runtime_permission_not_daemon_posture
    reusable_runtime_permission_not_loop_posture
    reusable_runtime_permission_not_public_api_posture
    reusable_runtime_permission_not_participant_facing_interface_posture
    reusable_runtime_permission_not_distributed_network_behavior_posture
    continuation_not_authorized_posture
    self_continuation_not_authorized_posture
    self_recursive_growth_not_created_posture
    runtime_daemon_not_created_posture
    runtime_loop_not_created_posture
    public_api_not_created_posture
    participant_facing_interface_not_created_posture
    distributed_network_behavior_not_created_posture
    source_transfer_not_created_posture
    source_receipt_not_created_posture
    reception_authorization_not_created_posture
    source_not_created_posture
    authority_not_created_posture
    currentness_not_created_posture
    deployment_not_created_posture
    public_release_not_created_posture
    operation_permission_not_created_posture
    broader_reusable_permission_not_created_posture
    follow_on_work_not_authorized_posture
    hidden_repo_state_excluded_posture
    repo_local_availability_not_reusable_runtime_permission_authority_posture
    artifact_existence_not_reusable_runtime_permission_authority_posture
    latest_file_posture_not_reusable_runtime_permission_authority_posture
    selected_basis_reference_shape_posture
    raw_full_prior_artifact_body_not_returned_posture
    official_enum_scope_strings_not_redacted_posture
    hostile_raw_body_content_contained_posture
    predecessor_failure_evidence_preserved_posture
    result_level_non_claims_canonical_false_posture
    """
)

_OPEN_ITEMS = (
    "reusable-runtime-permission test",
    "reusable-runtime-permission live artifact",
    "reusable-runtime-permission terminal summary, if needed",
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
    "broader reusable permission",
    "successor reception request",
    "follow-on work",
)


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
    if value is None or value is False:
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
        if value.get("declared") is False or value.get("recorded") is False:
            return False
        return True
    return value is True or _is_declared(value)


def _first_failed_code(checks: list[dict[str, Any]]) -> str | None:
    for check in checks:
        if not check.get("passed"):
            return check.get("block_code") or check.get("failure_code")
    return None


def _basis_detail(
    request: Mapping[str, Any],
    basis_field: str,
    outcome_field: str | None = None,
    version_field: str | None = None,
    failed_count_field: str | None = None,
    path_field: str | None = None,
    extra_fields: tuple[str, ...] = (),
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
        detail["selected_failed_check_count"] = _sanitize(
            request.get(failed_count_field)
        )
    if path_field:
        detail["selected_result_path"] = _sanitize(request.get(path_field))
    for field in extra_fields:
        detail[field] = _sanitize(request.get(field))
    return detail


def _posture_section(request: Mapping[str, Any], field: str) -> dict[str, Any]:
    value = request.get(field)
    if isinstance(value, Mapping):
        section = dict(_sanitize(value))
        section.setdefault("declared", _posture_declared(request, field))
        return section
    return {"declared": _posture_declared(request, field), "posture": _sanitize(value)}


def _scope_values(request: Mapping[str, Any]) -> list[Any]:
    scope = request.get("reusable_runtime_permission_scope")
    if isinstance(scope, str):
        return [scope]
    if isinstance(scope, (list, tuple, set)):
        return list(scope)
    return []


def _validate_scope(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    scope_values = _scope_values(request)
    unsupported = [value for value in scope_values if value not in SUPPORTED_SCOPE_VALUES]
    missing = [value for value in SUPPORTED_SCOPE_VALUES if value not in scope_values]
    redaction_values = {
        _REDACTED_PERMISSION_PLACEHOLDER,
        _REDACTED_RAW_OR_HIDDEN_STATE,
        "[bounded-reusable-runtime-permission-boundary-redacted]",
    }
    redacted = [value for value in scope_values if value in redaction_values]
    _check(
        checks,
        "reusable_runtime_permission_scope_supported",
        bool(scope_values) and not unsupported and not missing and not redacted,
        {
            "all_scope_values_supported": True,
            "required_scope_values": list(SUPPORTED_SCOPE_VALUES),
        },
        {"scope": scope_values, "unsupported": unsupported, "missing": missing},
        "UNSUPPORTED_REUSABLE_RUNTIME_PERMISSION_SCOPE",
    )


def _base_request_checks(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> None:
    question = request.get("reusable_runtime_permission_question")
    intent = request.get("reusable_runtime_permission_intent")
    _check(
        checks,
        "reusable_runtime_permission_question_declared",
        isinstance(question, str) and question.strip() == CORE_QUESTION,
        CORE_QUESTION,
        question,
        "REUSABLE_RUNTIME_PERMISSION_QUESTION_UNDECLARED",
    )
    _check(
        checks,
        "reusable_runtime_permission_intent_supported",
        intent in SUPPORTED_INTENTS,
        list(SUPPORTED_INTENTS),
        intent,
        "REUSABLE_RUNTIME_PERMISSION_INTENT_UNSUPPORTED",
    )
    _check(
        checks,
        "reusable_runtime_permission_intent_not_explicit_block",
        intent != INTENT_BLOCK,
        f"intent is not {INTENT_BLOCK}",
        intent,
        "REUSABLE_RUNTIME_PERMISSION_EXPLICIT_BLOCK_REQUESTED",
    )
    _validate_scope(request, checks)


def _reusable_runtime_permission_boundary_checks(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> None:
    _check(
        checks,
        "reusable_runtime_permission_boundary_basis_declared",
        _is_declared(request.get("selected_reusable_runtime_permission_boundary_basis")),
        "selected reusable-runtime-permission-boundary live artifact basis declared",
        request.get("selected_reusable_runtime_permission_boundary_basis"),
        "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_BASIS_MISSING",
    )
    _check(
        checks,
        "reusable_runtime_permission_boundary_terminal_summary_basis_declared",
        _is_declared(
            request.get("selected_reusable_runtime_permission_boundary_terminal_summary_basis")
        ),
        "selected reusable-runtime-permission-boundary terminal summary basis declared",
        request.get("selected_reusable_runtime_permission_boundary_terminal_summary_basis"),
        "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_BASIS_MISSING",
    )
    _check(
        checks,
        "reusable_runtime_permission_boundary_outcome_recorded",
        request.get("selected_reusable_runtime_permission_boundary_result_outcome")
        == EXPECTED_REUSABLE_RUNTIME_PERMISSION_BOUNDARY_OUTCOME,
        EXPECTED_REUSABLE_RUNTIME_PERMISSION_BOUNDARY_OUTCOME,
        request.get("selected_reusable_runtime_permission_boundary_result_outcome"),
        "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_NOT_RECORDED",
    )
    _check(
        checks,
        "reusable_runtime_permission_boundary_version_0_1_0",
        request.get("selected_reusable_runtime_permission_boundary_result_version")
        == "0.1.0",
        "0.1.0",
        request.get("selected_reusable_runtime_permission_boundary_result_version"),
        "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_VERSION_NOT_0_1_0",
    )
    _check(
        checks,
        "reusable_runtime_permission_boundary_failed_checks_zero",
        request.get("selected_reusable_runtime_permission_boundary_failed_check_count") == 0,
        0,
        request.get("selected_reusable_runtime_permission_boundary_failed_check_count"),
        "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_FAILED_CHECKS_PRESENT",
    )
    _check(
        checks,
        "reusable_runtime_permission_boundary_declared_future_review",
        request.get("selected_reusable_runtime_permission_boundary_declared_future_review")
        is True,
        True,
        request.get("selected_reusable_runtime_permission_boundary_declared_future_review"),
        "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_DID_NOT_DECLARE_FUTURE_REUSABLE_RUNTIME_PERMISSION_REVIEW",
    )
    false_flags = (
        (
            "selected_reusable_runtime_permission_boundary_already_created_reusable_runtime_permission",
            "reusable_runtime_permission_boundary_did_not_create_reusable_runtime_permission",
            "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_ALREADY_CREATED_REUSABLE_RUNTIME_PERMISSION",
        ),
        (
            "selected_reusable_runtime_permission_boundary_already_authorized_continuation",
            "reusable_runtime_permission_boundary_did_not_authorize_continuation",
            "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_ALREADY_AUTHORIZED_CONTINUATION",
        ),
        (
            "selected_reusable_runtime_permission_boundary_already_authorized_self_continuation",
            "reusable_runtime_permission_boundary_did_not_authorize_self_continuation",
            "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_ALREADY_AUTHORIZED_SELF_CONTINUATION",
        ),
        (
            "selected_reusable_runtime_permission_boundary_already_created_runtime_daemon",
            "reusable_runtime_permission_boundary_did_not_create_runtime_daemon",
            "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_ALREADY_CREATED_RUNTIME_DAEMON",
        ),
        (
            "selected_reusable_runtime_permission_boundary_already_created_runtime_loop",
            "reusable_runtime_permission_boundary_did_not_create_runtime_loop",
            "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_ALREADY_CREATED_RUNTIME_LOOP",
        ),
        (
            "selected_reusable_runtime_permission_boundary_already_created_public_api",
            "reusable_runtime_permission_boundary_did_not_create_public_api",
            "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_ALREADY_CREATED_PUBLIC_API",
        ),
        (
            "selected_reusable_runtime_permission_boundary_already_created_participant_facing_interface",
            "reusable_runtime_permission_boundary_did_not_create_participant_facing_interface",
            "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE",
        ),
        (
            "selected_reusable_runtime_permission_boundary_already_created_distributed_network_behavior",
            "reusable_runtime_permission_boundary_did_not_create_distributed_network_behavior",
            "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR",
        ),
        (
            "selected_reusable_runtime_permission_boundary_treated_as_reusable_runtime_permission",
            "reusable_runtime_permission_boundary_not_treated_as_reusable_runtime_permission",
            "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_TREATED_AS_REUSABLE_RUNTIME_PERMISSION",
        ),
        (
            "selected_reusable_runtime_permission_boundary_treated_as_continuation",
            "reusable_runtime_permission_boundary_not_treated_as_continuation",
            "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_TREATED_AS_CONTINUATION",
        ),
        (
            "selected_reusable_runtime_permission_boundary_treated_as_self_continuation",
            "reusable_runtime_permission_boundary_not_treated_as_self_continuation",
            "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_TREATED_AS_SELF_CONTINUATION",
        ),
        (
            "selected_reusable_runtime_permission_boundary_authorized_future_work",
            "reusable_runtime_permission_boundary_did_not_authorize_future_work",
            "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_AUTHORIZED_FUTURE_WORK",
        ),
    )
    for field, check_name, code in false_flags:
        _check(checks, check_name, not _flag_true(request.get(field)), False, request.get(field), code)
    _check(
        checks,
        "reusable_runtime_permission_boundary_canonicalized_result_level_non_claims",
        request.get("selected_reusable_runtime_permission_boundary_non_claims_canonicalized")
        is True,
        True,
        request.get("selected_reusable_runtime_permission_boundary_non_claims_canonicalized"),
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )


def _ongoing_runtime_checks(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> None:
    _check(
        checks,
        "ongoing_runtime_basis_declared",
        _is_declared(request.get("selected_ongoing_runtime_basis")),
        "selected ongoing-runtime live artifact basis declared",
        request.get("selected_ongoing_runtime_basis"),
        "ONGOING_RUNTIME_BASIS_MISSING",
    )
    _check(
        checks,
        "ongoing_runtime_terminal_summary_basis_declared",
        _is_declared(request.get("selected_ongoing_runtime_terminal_summary_basis")),
        "selected ongoing-runtime terminal summary basis declared",
        request.get("selected_ongoing_runtime_terminal_summary_basis"),
        "ONGOING_RUNTIME_BASIS_MISSING",
    )
    _check(
        checks,
        "ongoing_runtime_outcome_recorded",
        request.get("selected_ongoing_runtime_result_outcome")
        == EXPECTED_ONGOING_RUNTIME_OUTCOME,
        EXPECTED_ONGOING_RUNTIME_OUTCOME,
        request.get("selected_ongoing_runtime_result_outcome"),
        "ONGOING_RUNTIME_NOT_RECORDED",
    )
    _check(
        checks,
        "ongoing_runtime_version_0_1_0",
        request.get("selected_ongoing_runtime_result_version") == "0.1.0",
        "0.1.0",
        request.get("selected_ongoing_runtime_result_version"),
        "ONGOING_RUNTIME_VERSION_NOT_0_1_0",
    )
    _check(
        checks,
        "ongoing_runtime_failed_checks_zero",
        request.get("selected_ongoing_runtime_failed_check_count") == 0,
        0,
        request.get("selected_ongoing_runtime_failed_check_count"),
        "ONGOING_RUNTIME_FAILED_CHECKS_PRESENT",
    )
    _check(
        checks,
        "ongoing_runtime_recorded_bounded_ongoing_runtime_posture",
        request.get("selected_ongoing_runtime_bounded_ongoing_runtime_posture_recorded")
        is True,
        True,
        request.get("selected_ongoing_runtime_bounded_ongoing_runtime_posture_recorded"),
        "ONGOING_RUNTIME_DID_NOT_RECORD_BOUNDED_ONGOING_RUNTIME_POSTURE",
    )
    _check(
        checks,
        "ongoing_runtime_recorded_bounded_persistence_posture",
        request.get("selected_ongoing_runtime_bounded_persistence_posture_recorded")
        is True,
        True,
        request.get("selected_ongoing_runtime_bounded_persistence_posture_recorded"),
        "ONGOING_RUNTIME_DID_NOT_RECORD_BOUNDED_PERSISTENCE_POSTURE",
    )
    ongoing_false_flags = (
        (
            "selected_ongoing_runtime_persistence_treated_as_repeatability_before_permission",
            "ongoing_runtime_persistence_not_repeatability_before_permission",
            "ONGOING_RUNTIME_PERSISTENCE_TREATED_AS_REPEATABILITY_BEFORE_PERMISSION",
        ),
        (
            "selected_ongoing_runtime_persistence_authorized_reuse_before_permission",
            "ongoing_runtime_persistence_did_not_authorize_reuse_before_permission",
            "ONGOING_RUNTIME_PERSISTENCE_AUTHORIZED_REUSE_BEFORE_PERMISSION",
        ),
        (
            "selected_ongoing_runtime_already_authorized_continuation",
            "ongoing_runtime_did_not_authorize_continuation",
            "ONGOING_RUNTIME_ALREADY_AUTHORIZED_CONTINUATION",
        ),
        (
            "selected_ongoing_runtime_already_authorized_self_continuation",
            "ongoing_runtime_did_not_authorize_self_continuation",
            "ONGOING_RUNTIME_ALREADY_AUTHORIZED_SELF_CONTINUATION",
        ),
    )
    for field, check_name, code in ongoing_false_flags:
        _check(checks, check_name, not _flag_true(request.get(field)), False, request.get(field), code)


def _upstream_basis_checks(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> None:
    upstream = (
        (
            "ongoing_runtime_boundary",
            "selected_ongoing_runtime_boundary_basis",
            "selected_ongoing_runtime_boundary_result_outcome",
            EXPECTED_ONGOING_RUNTIME_BOUNDARY_OUTCOME,
            "selected_ongoing_runtime_boundary_result_version",
            "0.1.0",
            "selected_ongoing_runtime_boundary_failed_check_count",
            "ONGOING_RUNTIME_BOUNDARY_BASIS_MISSING",
            "ONGOING_RUNTIME_BOUNDARY_NOT_RECORDED",
            "ONGOING_RUNTIME_BOUNDARY_VERSION_NOT_0_1_0",
            "ONGOING_RUNTIME_BOUNDARY_FAILED_CHECKS_PRESENT",
        ),
        (
            "runtime_hosting",
            "selected_runtime_hosting_basis",
            "selected_runtime_hosting_result_outcome",
            EXPECTED_RUNTIME_HOSTING_OUTCOME,
            "selected_runtime_hosting_result_version",
            "0.1.0",
            "selected_runtime_hosting_failed_check_count",
            "RUNTIME_HOSTING_BASIS_MISSING",
            "RUNTIME_HOSTING_NOT_RECORDED",
            "RUNTIME_HOSTING_VERSION_NOT_0_1_0",
            "RUNTIME_HOSTING_FAILED_CHECKS_PRESENT",
        ),
        (
            "runtime_hosting_boundary_v2",
            "selected_runtime_hosting_boundary_v2_basis",
            "selected_runtime_hosting_boundary_v2_result_outcome",
            EXPECTED_RUNTIME_HOSTING_BOUNDARY_V2_OUTCOME,
            "selected_runtime_hosting_boundary_v2_result_version",
            "0.2.0",
            "selected_runtime_hosting_boundary_v2_failed_check_count",
            "RUNTIME_HOSTING_BOUNDARY_V2_BASIS_MISSING",
            "RUNTIME_HOSTING_BOUNDARY_V2_NOT_RECORDED",
            "RUNTIME_HOSTING_BOUNDARY_V2_VERSION_NOT_0_2_0",
            "RUNTIME_HOSTING_BOUNDARY_V2_FAILED_CHECKS_PRESENT",
        ),
        (
            "successor_runtime_step",
            "selected_successor_runtime_step_basis",
            "selected_successor_runtime_step_result_outcome",
            EXPECTED_SUCCESSOR_RUNTIME_STEP_OUTCOME,
            "selected_successor_runtime_step_result_version",
            "0.1.0",
            "selected_successor_runtime_step_failed_check_count",
            "SUCCESSOR_RUNTIME_STEP_BASIS_MISSING",
            "SUCCESSOR_RUNTIME_STEP_NOT_RECORDED",
            "SUCCESSOR_RUNTIME_STEP_VERSION_NOT_0_1_0",
            "SUCCESSOR_RUNTIME_STEP_FAILED_CHECKS_PRESENT",
        ),
        (
            "minimal_runtime",
            "selected_minimal_runtime_basis",
            "selected_minimal_runtime_result_outcome",
            EXPECTED_MINIMAL_RUNTIME_OUTCOME,
            "selected_minimal_runtime_result_version",
            "0.1.0",
            "selected_minimal_runtime_failed_check_count",
            "MINIMAL_RUNTIME_BASIS_MISSING",
            "MINIMAL_RUNTIME_NOT_RECORDED",
            "MINIMAL_RUNTIME_VERSION_NOT_0_1_0",
            "MINIMAL_RUNTIME_FAILED_CHECKS_PRESENT",
        ),
        (
            "runtime_boundary",
            "selected_runtime_boundary_basis",
            "selected_runtime_boundary_result_outcome",
            EXPECTED_RUNTIME_BOUNDARY_OUTCOME,
            "selected_runtime_boundary_result_version",
            "0.1.0",
            "selected_runtime_boundary_failed_check_count",
            "RUNTIME_BOUNDARY_BASIS_MISSING",
            "RUNTIME_BOUNDARY_NOT_RECORDED",
            "RUNTIME_BOUNDARY_VERSION_NOT_0_1_0",
            "RUNTIME_BOUNDARY_FAILED_CHECKS_PRESENT",
        ),
        (
            "runtime_readiness",
            "selected_runtime_readiness_basis",
            "selected_runtime_readiness_result_outcome",
            EXPECTED_RUNTIME_READINESS_OUTCOME,
            "selected_runtime_readiness_result_version",
            "0.1.0",
            "selected_runtime_readiness_failed_check_count",
            "RUNTIME_READINESS_BASIS_MISSING",
            "RUNTIME_READINESS_NOT_RECORDED",
            "RUNTIME_READINESS_VERSION_NOT_0_1_0",
            "RUNTIME_READINESS_FAILED_CHECKS_PRESENT",
        ),
        (
            "portable_verification_final_completion",
            "selected_portable_verification_final_completion_basis",
            "selected_portable_verification_final_completion_result_outcome",
            EXPECTED_FINAL_COMPLETION_OUTCOME,
            "selected_portable_verification_final_completion_result_version",
            "0.1.0",
            "selected_portable_verification_final_completion_failed_check_count",
            "FINAL_COMPLETION_BASIS_MISSING",
            "FINAL_COMPLETION_NOT_RECORDED",
            "FINAL_COMPLETION_VERSION_NOT_0_1_0",
            "FINAL_COMPLETION_FAILED_CHECKS_PRESENT",
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
        _is_declared(
            request.get("selected_runtime_hosting_boundary_v1_failure_lineage_basis")
        ),
        "runtime-hosting-boundary v1 failure lineage preserved as predecessor evidence",
        request.get("selected_runtime_hosting_boundary_v1_failure_lineage_basis"),
        "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
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
            "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
        )
    _check(
        checks,
        "post_portable_currentness_surface_basis_declared",
        _is_declared(request.get("selected_post_portable_verification_currentness_basis")),
        "post-portable-verification currentness surface basis declared",
        request.get("selected_post_portable_verification_currentness_basis"),
        "CURRENTNESS_SURFACE_BASIS_MISSING",
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
        "CURRENTNESS_SURFACE_TREATED_CHECKABILITY_AS_CONTINUATION",
    )
    _check(
        checks,
        "post_portable_currentness_surface_does_not_authorize_next_work",
        not _flag_true(
            request.get("selected_post_portable_currentness_surface_authorized_next_work")
        ),
        False,
        request.get("selected_post_portable_currentness_surface_authorized_next_work"),
        "CURRENTNESS_SURFACE_AUTHORIZED_NEXT_WORK",
    )
    _check(
        checks,
        "returned_second_carrier_capture_lineage_basis_declared",
        _is_declared(request.get("selected_returned_second_carrier_capture_lineage_basis")),
        "returned second-carrier capture intake basis declared as lineage only",
        request.get("selected_returned_second_carrier_capture_lineage_basis"),
        "FINAL_COMPLETION_BASIS_MISSING",
    )


def _posture_checks(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    for field in _POSTURE_FIELDS:
        _check(
            checks,
            f"{field}_declared",
            _posture_declared(request, field),
            "bounded reusable-runtime-permission posture declared",
            request.get(field),
            "REUSABLE_RUNTIME_PERMISSION_REQUIRED_POSTURE_MISSING",
        )


def _false_field_checks(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> None:
    false_fields = (
        (
            "reusable_runtime_permission_created_before_review",
            "REUSABLE_RUNTIME_PERMISSION_CREATED_BEFORE_REVIEW",
        ),
        (
            "reusable_runtime_permission_treated_as_continuation",
            "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_CONTINUATION",
        ),
        (
            "reusable_runtime_permission_treated_as_self_continuation",
            "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_SELF_CONTINUATION",
        ),
        (
            "reusable_runtime_permission_treated_as_self_recursive_growth",
            "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_SELF_RECURSIVE_GROWTH",
        ),
        (
            "reusable_runtime_permission_treated_as_runtime_daemon",
            "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_RUNTIME_DAEMON",
        ),
        (
            "reusable_runtime_permission_treated_as_runtime_loop",
            "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_RUNTIME_LOOP",
        ),
        (
            "reusable_runtime_permission_treated_as_public_api",
            "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_PUBLIC_API",
        ),
        (
            "reusable_runtime_permission_treated_as_participant_facing_interface",
            "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_PARTICIPANT_FACING_INTERFACE",
        ),
        (
            "reusable_runtime_permission_treated_as_distributed_network_behavior",
            "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR",
        ),
        (
            "reusable_runtime_permission_treated_as_source_transfer",
            "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_SOURCE_TRANSFER",
        ),
        (
            "reusable_runtime_permission_treated_as_source_receipt",
            "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_SOURCE_RECEIPT",
        ),
        (
            "reusable_runtime_permission_treated_as_reception_authorization",
            "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_RECEPTION_AUTHORIZATION",
        ),
        ("reusable_runtime_permission_treated_as_source", "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_SOURCE"),
        (
            "reusable_runtime_permission_treated_as_authority",
            "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_AUTHORITY",
        ),
        (
            "reusable_runtime_permission_treated_as_currentness",
            "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_CURRENTNESS",
        ),
        (
            "reusable_runtime_permission_treated_as_deployment",
            "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_DEPLOYMENT",
        ),
        (
            "reusable_runtime_permission_treated_as_public_release",
            "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_PUBLIC_RELEASE",
        ),
        (
            "reusable_runtime_permission_treated_as_operation_permission",
            "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_OPERATION_PERMISSION",
        ),
        (
            "reusable_runtime_permission_treated_as_broader_reusable_permission",
            "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_BROADER_REUSABLE_PERMISSION",
        ),
        (
            "reusable_runtime_permission_treated_as_follow_on_work",
            "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_FOLLOW_ON_WORK",
        ),
        ("continuation_authorized", "CONTINUATION_AUTHORIZED"),
        ("self_continuation_authorized", "SELF_CONTINUATION_AUTHORIZED"),
        ("self_recursive_growth_created", "SELF_RECURSIVE_GROWTH_CREATED"),
        ("runtime_daemon_created", "RUNTIME_DAEMON_CREATED"),
        ("runtime_loop_created", "RUNTIME_LOOP_CREATED"),
        ("public_api_created", "PUBLIC_API_CREATED"),
        ("participant_facing_interface_created", "PARTICIPANT_FACING_INTERFACE_CREATED"),
        ("distributed_network_behavior_created", "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED"),
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
        ("adoption_created", "ADOPTION_CREATED"),
        ("receiving_context_governance_created", "RECEIVING_CONTEXT_GOVERNANCE_CREATED"),
        ("publication_flow_created", "PUBLICATION_FLOW_CREATED"),
        ("follow_on_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
        (
            "artifact_existence_treated_as_reusable_runtime_permission_authority",
            "ARTIFACT_EXISTENCE_TREATED_AS_REUSABLE_RUNTIME_PERMISSION_AUTHORITY",
        ),
        ("artifact_path_treated_as_currentness", "ARTIFACT_PATH_TREATED_AS_CURRENTNESS"),
        (
            "latest_file_posture_treated_as_reusable_runtime_permission_authority",
            "LATEST_FILE_POSTURE_TREATED_AS_REUSABLE_RUNTIME_PERMISSION_AUTHORITY",
        ),
        (
            "repo_local_availability_treated_as_reusable_runtime_permission_authority",
            "REPO_LOCAL_AVAILABILITY_TREATED_AS_REUSABLE_RUNTIME_PERMISSION_AUTHORITY",
        ),
        (
            "hidden_repo_state_used_as_reusable_runtime_permission_content",
            "HIDDEN_REPO_STATE_USED_AS_REUSABLE_RUNTIME_PERMISSION_CONTENT",
        ),
        (
            "hidden_repo_state_used_as_reusable_runtime_permission_authority",
            "HIDDEN_REPO_STATE_USED_AS_REUSABLE_RUNTIME_PERMISSION_AUTHORITY",
        ),
        ("selected_basis_not_reference_shaped", "SELECTED_BASIS_NOT_REFERENCE_SHAPED"),
        ("raw_full_prior_artifact_body_returned", "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED"),
        (
            "predecessor_failure_evidence_hidden_or_repaired",
            "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        ),
        (
            "selected_runtime_hosting_boundary_v1_failure_repaired",
            "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
        ),
        (
            "selected_runtime_hosting_boundary_v1_failure_hidden",
            "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
        ),
        (
            "selected_runtime_hosting_boundary_v1_failure_claimed_passed",
            "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
        ),
        ("consumed_request_reopened", "CONSUMED_REQUEST_REOPENED"),
        ("authorization_token_reused", "AUTHORIZATION_TOKEN_REUSED"),
    )
    for field, code in false_fields:
        _check(
            checks,
            f"{field}_false",
            not _flag_true(request.get(field)),
            False,
            request.get(field),
            code,
        )
    explicitly_checked = {field for field, _code in false_fields}
    for field in REQUIRED_FALSE_NON_CLAIMS:
        if field in explicitly_checked:
            continue
        _check(
            checks,
            f"{field}_top_level_false",
            not _flag_true(request.get(field)),
            False,
            request.get(field),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )


def _boundary_authority_checks(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> None:
    _check(
        checks,
        "selected_basis_reference_shaped",
        request.get("reference_shaped_input_posture") is not False
        and not _flag_true(request.get("selected_basis_not_reference_shaped")),
        True,
        request.get("reference_shaped_input_posture"),
        "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    )
    _check(
        checks,
        "raw_full_prior_artifact_body_not_returned",
        not _flag_true(request.get("raw_full_prior_artifact_body_returned")),
        False,
        request.get("raw_full_prior_artifact_body_returned"),
        "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    )
    sanitized = _sanitize(request)
    serialized = json.dumps(sanitized, sort_keys=True, ensure_ascii=False)
    hostile_absent = not any(sentinel in serialized for sentinel in _HOSTILE_SENTINELS)
    _check(
        checks,
        "hostile_raw_body_content_contained",
        hostile_absent,
        "hostile raw body sentinel absent from sanitized result material",
        "contained" if hostile_absent else "uncontained",
        "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    )
    _check(
        checks,
        "official_enum_scope_strings_not_redacted",
        all(value in SUPPORTED_SCOPE_VALUES for value in SUPPORTED_SCOPE_VALUES),
        "official enum/scope strings preserved",
        list(SUPPORTED_SCOPE_VALUES),
        "UNSUPPORTED_REUSABLE_RUNTIME_PERMISSION_SCOPE",
    )
    _check(
        checks,
        "consumed_request_token_remains_closed",
        not _flag_true(request.get("consumed_request_reopened")),
        False,
        request.get("consumed_request_reopened"),
        "CONSUMED_REQUEST_REOPENED",
    )
    _check(
        checks,
        "authorization_token_reuse_blocked",
        not _flag_true(request.get("authorization_token_reused")),
        False,
        request.get("authorization_token_reused"),
        "AUTHORIZATION_TOKEN_REUSED",
    )


def _bounded_runtime_reuse_envelope_checks(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> None:
    envelope = request.get("requested_bounded_runtime_reuse_envelope")
    _check(
        checks,
        "bounded_runtime_reuse_envelope_declared",
        isinstance(envelope, Mapping) and bool(envelope),
        "bounded runtime-reuse envelope declared",
        envelope,
        "REUSABLE_RUNTIME_PERMISSION_REQUIRED_POSTURE_MISSING",
    )
    if not isinstance(envelope, Mapping):
        return
    for field in (
        "authorizes_continuation",
        "authorizes_self_continuation",
        "creates_self_recursive_growth",
        "creates_runtime_daemon",
        "creates_runtime_loop",
        "creates_public_api",
        "creates_participant_facing_interface",
        "creates_distributed_network_behavior",
        "creates_source_transfer",
        "creates_source_receipt",
        "creates_reception_authorization",
        "creates_source",
        "creates_authority",
        "creates_currentness",
        "creates_deployment",
        "creates_public_release",
        "creates_operation_permission",
        "creates_broader_reusable_permission",
        "creates_derivative_reception",
        "creates_vessel_relation",
        "creates_another_reception_request",
        "creates_adoption",
        "creates_receiving_context_governance",
        "creates_publication_flow",
        "authorizes_follow_on_work",
    ):
        _check(
            checks,
            f"bounded_runtime_reuse_envelope_{field}_false",
            not _flag_true(envelope.get(field)),
            False,
            envelope.get(field),
            "REUSABLE_RUNTIME_PERMISSION_REQUIRED_POSTURE_MISSING",
        )
    _check(
        checks,
        "bounded_runtime_reuse_envelope_requires_fresh_admission_outside_envelope",
        envelope.get("anything_outside_envelope_requires_fresh_admission") is True,
        True,
        envelope.get("anything_outside_envelope_requires_fresh_admission"),
        "REUSABLE_RUNTIME_PERMISSION_REQUIRED_POSTURE_MISSING",
    )


def _non_claim_checks(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> None:
    declared = request.get("declared_non_claims")
    _check(
        checks,
        "declared_non_claims_mapping_present",
        isinstance(declared, Mapping),
        "declared_non_claims mapping with canonical false values",
        declared,
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    if not isinstance(declared, Mapping):
        return
    for key in REQUIRED_FALSE_NON_CLAIMS:
        _check(
            checks,
            f"declared_non_claim_{key}_false",
            key in declared and declared.get(key) is False,
            False,
            declared.get(key, "<missing>"),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )


def _build_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    _base_request_checks(request, checks)
    _reusable_runtime_permission_boundary_checks(request, checks)
    _ongoing_runtime_checks(request, checks)
    _upstream_basis_checks(request, checks)
    _lineage_and_currentness_checks(request, checks)
    _posture_checks(request, checks)
    _false_field_checks(request, checks)
    _boundary_authority_checks(request, checks)
    _bounded_runtime_reuse_envelope_checks(request, checks)
    _non_claim_checks(request, checks)
    return checks


def _determine_outcome(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> str:
    if any(not check.get("passed") for check in checks):
        return OUTCOME_BLOCKED
    requested = request.get("requested_reusable_runtime_permission_outcome")
    if requested == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS
    if (
        requested == OUTCOME_NOT_RECORDED
        or request.get("reusable_runtime_permission_intent") == INTENT_DO_NOT_RECORD
    ):
        return OUTCOME_NOT_RECORDED
    return OUTCOME_RECORDED


def _reusable_runtime_permission_statement(outcome: str) -> dict[str, bool]:
    statement: dict[str, bool] = {}
    recorded_only = {
        "reusable_runtime_permission_recorded",
        "bounded_reusable_runtime_permission_posture_recorded",
        "bounded_runtime_reuse_envelope_declared",
    }
    for field in ALLOWED_TRUE_RECORDED_FIELDS:
        statement[field] = outcome == OUTCOME_RECORDED if field in recorded_only else True
    return statement


def _reusable_runtime_permission_non_meaning() -> dict[str, bool]:
    return {
        "reusable_runtime_permission_is_continuation": False,
        "reusable_runtime_permission_is_self_continuation": False,
        "reusable_runtime_permission_is_self_recursive_growth": False,
        "reusable_runtime_permission_is_runtime_daemon": False,
        "reusable_runtime_permission_is_runtime_loop": False,
        "reusable_runtime_permission_is_public_api": False,
        "reusable_runtime_permission_is_participant_facing_interface": False,
        "reusable_runtime_permission_is_distributed_network_behavior": False,
        "reusable_runtime_permission_is_source_transfer": False,
        "reusable_runtime_permission_is_source_receipt": False,
        "reusable_runtime_permission_is_reception_authorization": False,
        "reusable_runtime_permission_is_source": False,
        "reusable_runtime_permission_is_authority": False,
        "reusable_runtime_permission_is_currentness": False,
        "reusable_runtime_permission_is_deployment": False,
        "reusable_runtime_permission_is_public_release": False,
        "reusable_runtime_permission_is_operation_permission": False,
        "reusable_runtime_permission_is_broader_reusable_permission": False,
        "reusable_runtime_permission_is_follow_on_work": False,
        "reusable_runtime_permission_boundary_is_reusable_runtime_permission_without_review": False,
        "ongoing_runtime_is_reusable_runtime_permission_without_review": False,
        "ongoing_runtime_persistence_is_unbounded_repeatability": False,
    }


def _bounded_runtime_reuse_envelope(
    request: Mapping[str, Any], outcome: str
) -> dict[str, Any]:
    incoming = request.get("requested_bounded_runtime_reuse_envelope")
    envelope: dict[str, Any] = {
        "declared": outcome == OUTCOME_RECORDED,
        "envelope_type": "bounded_runtime_reuse_envelope",
        "scope": (
            "one bounded reusable-runtime-permission posture recorded from selected "
            "standing reusable-runtime-permission-boundary and ongoing-runtime basis"
        ),
        "runtime_reuse_limited_to_declared_envelope": True,
        "arbitrary_runtime_activity_authorized": False,
        "authorizes_continuation": False,
        "authorizes_self_continuation": False,
        "creates_self_recursive_growth": False,
        "creates_runtime_daemon": False,
        "creates_runtime_loop": False,
        "creates_public_api": False,
        "creates_participant_facing_interface": False,
        "creates_distributed_network_behavior": False,
        "creates_source_transfer": False,
        "creates_source_receipt": False,
        "creates_reception_authorization": False,
        "creates_source": False,
        "creates_authority": False,
        "creates_currentness": False,
        "creates_deployment": False,
        "creates_public_release": False,
        "creates_operation_permission": False,
        "creates_broader_reusable_permission": False,
        "creates_derivative_reception": False,
        "creates_vessel_relation": False,
        "creates_another_reception_request": False,
        "creates_adoption": False,
        "creates_receiving_context_governance": False,
        "creates_publication_flow": False,
        "authorizes_follow_on_work": False,
        "anything_outside_envelope_requires_fresh_admission": True,
    }
    if isinstance(incoming, Mapping):
        envelope["declared_request"] = _sanitize(incoming)
    return envelope


def _selected_basis_metadata(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "selected_reusable_runtime_permission_boundary_outcome": _sanitize(
            request.get("selected_reusable_runtime_permission_boundary_result_outcome")
        ),
        "selected_reusable_runtime_permission_boundary_result_version": _sanitize(
            request.get("selected_reusable_runtime_permission_boundary_result_version")
        ),
        "selected_reusable_runtime_permission_boundary_failed_check_count": _sanitize(
            request.get("selected_reusable_runtime_permission_boundary_failed_check_count")
        ),
        "selected_ongoing_runtime_outcome": _sanitize(
            request.get("selected_ongoing_runtime_result_outcome")
        ),
        "selected_ongoing_runtime_result_version": _sanitize(
            request.get("selected_ongoing_runtime_result_version")
        ),
        "selected_ongoing_runtime_failed_check_count": _sanitize(
            request.get("selected_ongoing_runtime_failed_check_count")
        ),
        "selected_ongoing_runtime_boundary_outcome": _sanitize(
            request.get("selected_ongoing_runtime_boundary_result_outcome")
        ),
        "selected_ongoing_runtime_boundary_result_version": _sanitize(
            request.get("selected_ongoing_runtime_boundary_result_version")
        ),
        "selected_ongoing_runtime_boundary_failed_check_count": _sanitize(
            request.get("selected_ongoing_runtime_boundary_failed_check_count")
        ),
        "selected_runtime_hosting_outcome": _sanitize(
            request.get("selected_runtime_hosting_result_outcome")
        ),
        "selected_runtime_hosting_result_version": _sanitize(
            request.get("selected_runtime_hosting_result_version")
        ),
        "selected_runtime_hosting_failed_check_count": _sanitize(
            request.get("selected_runtime_hosting_failed_check_count")
        ),
        "selected_runtime_hosting_boundary_v2_outcome": _sanitize(
            request.get("selected_runtime_hosting_boundary_v2_result_outcome")
        ),
        "selected_runtime_hosting_boundary_v2_result_version": _sanitize(
            request.get("selected_runtime_hosting_boundary_v2_result_version")
        ),
        "selected_runtime_hosting_boundary_v2_failed_check_count": _sanitize(
            request.get("selected_runtime_hosting_boundary_v2_failed_check_count")
        ),
        "selected_successor_runtime_step_outcome": _sanitize(
            request.get("selected_successor_runtime_step_result_outcome")
        ),
        "selected_successor_runtime_step_result_version": _sanitize(
            request.get("selected_successor_runtime_step_result_version")
        ),
        "selected_successor_runtime_step_failed_check_count": _sanitize(
            request.get("selected_successor_runtime_step_failed_check_count")
        ),
        "selected_minimal_runtime_outcome": _sanitize(
            request.get("selected_minimal_runtime_result_outcome")
        ),
        "selected_minimal_runtime_result_version": _sanitize(
            request.get("selected_minimal_runtime_result_version")
        ),
        "selected_minimal_runtime_failed_check_count": _sanitize(
            request.get("selected_minimal_runtime_failed_check_count")
        ),
        "selected_runtime_boundary_outcome": _sanitize(
            request.get("selected_runtime_boundary_result_outcome")
        ),
        "selected_runtime_boundary_result_version": _sanitize(
            request.get("selected_runtime_boundary_result_version")
        ),
        "selected_runtime_boundary_failed_check_count": _sanitize(
            request.get("selected_runtime_boundary_failed_check_count")
        ),
        "selected_runtime_readiness_outcome": _sanitize(
            request.get("selected_runtime_readiness_result_outcome")
        ),
        "selected_runtime_readiness_result_version": _sanitize(
            request.get("selected_runtime_readiness_result_version")
        ),
        "selected_runtime_readiness_failed_check_count": _sanitize(
            request.get("selected_runtime_readiness_failed_check_count")
        ),
        "selected_final_completion_outcome": _sanitize(
            request.get("selected_portable_verification_final_completion_result_outcome")
        ),
        "selected_final_completion_result_version": _sanitize(
            request.get("selected_portable_verification_final_completion_result_version")
        ),
        "selected_final_completion_failed_check_count": _sanitize(
            request.get("selected_portable_verification_final_completion_failed_check_count")
        ),
        "selected_post_portable_currentness_surface_path": _sanitize(
            request.get("selected_post_portable_currentness_surface_path")
        ),
    }


def _build_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    outcome: str,
    block_reason: str | None = None,
) -> dict[str, Any]:
    request_id = str(request.get("reusable_runtime_permission_request_id") or _DEFAULT_REQUEST_ID)
    metadata = {
        "post_ongoing_runtime_reusable_runtime_permission_id": request_id,
        "post_ongoing_runtime_reusable_runtime_permission_type": (
            "post_ongoing_runtime_reusable_runtime_permission"
        ),
        "post_ongoing_runtime_reusable_runtime_permission_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
        "request_intent": _sanitize(request.get("reusable_runtime_permission_intent")),
        "selected_basis_summary": _selected_basis_metadata(request),
    }
    first_failed_code = _first_failed_code(checks)
    block = None
    if outcome == OUTCOME_BLOCKED:
        block = {
            "blocked": True,
            "block_code": first_failed_code
            or "DECLARED_REUSABLE_RUNTIME_PERMISSION_REQUEST_MALFORMED",
            "block_reason": _sanitize(
                block_reason
                or request.get("block_reason")
                or "reusable-runtime-permission review blocked by bounded resolver check"
            ),
        }

    result: dict[str, Any] = {
        "post_ongoing_runtime_reusable_runtime_permission_metadata": metadata,
        "declared_reusable_runtime_permission_question": {
            "request_id": request_id,
            "question": _sanitize(request.get("reusable_runtime_permission_question")),
            "intent": _sanitize(request.get("reusable_runtime_permission_intent")),
        },
        "selected_reusable_runtime_permission_boundary_basis": _basis_detail(
            request,
            "selected_reusable_runtime_permission_boundary_basis",
            "selected_reusable_runtime_permission_boundary_result_outcome",
            "selected_reusable_runtime_permission_boundary_result_version",
            "selected_reusable_runtime_permission_boundary_failed_check_count",
            "selected_reusable_runtime_permission_boundary_result_path",
            (
                "selected_reusable_runtime_permission_boundary_declared_future_review",
                "selected_reusable_runtime_permission_boundary_non_claims_canonicalized",
            ),
        ),
        "selected_reusable_runtime_permission_boundary_terminal_summary_basis": _basis_detail(
            request, "selected_reusable_runtime_permission_boundary_terminal_summary_basis"
        ),
        "selected_ongoing_runtime_basis": _basis_detail(
            request,
            "selected_ongoing_runtime_basis",
            "selected_ongoing_runtime_result_outcome",
            "selected_ongoing_runtime_result_version",
            "selected_ongoing_runtime_failed_check_count",
            "selected_ongoing_runtime_result_path",
            (
                "selected_ongoing_runtime_bounded_ongoing_runtime_posture_recorded",
                "selected_ongoing_runtime_bounded_persistence_posture_recorded",
            ),
        ),
        "selected_ongoing_runtime_terminal_summary_basis": _basis_detail(
            request, "selected_ongoing_runtime_terminal_summary_basis"
        ),
        "selected_ongoing_runtime_boundary_basis": _basis_detail(
            request,
            "selected_ongoing_runtime_boundary_basis",
            "selected_ongoing_runtime_boundary_result_outcome",
            "selected_ongoing_runtime_boundary_result_version",
            "selected_ongoing_runtime_boundary_failed_check_count",
            "selected_ongoing_runtime_boundary_result_path",
        ),
        "selected_runtime_hosting_basis": _basis_detail(
            request,
            "selected_runtime_hosting_basis",
            "selected_runtime_hosting_result_outcome",
            "selected_runtime_hosting_result_version",
            "selected_runtime_hosting_failed_check_count",
            "selected_runtime_hosting_result_path",
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
            request, "selected_post_portable_verification_currentness_basis"
        ),
        "selected_returned_second_carrier_capture_lineage_basis": _basis_detail(
            request, "selected_returned_second_carrier_capture_lineage_basis"
        ),
        "reusable_runtime_permission_scope": _sanitize(_scope_values(request)),
        "reusable_runtime_permission_checks": checks,
        "reusable_runtime_permission_statement": _reusable_runtime_permission_statement(
            outcome
        ),
        "reusable_runtime_permission_non_meaning": _reusable_runtime_permission_non_meaning(),
        "bounded_runtime_reuse_envelope": _bounded_runtime_reuse_envelope(
            request, outcome
        ),
        "additional_basis_required": _sanitize(
            request.get("additional_basis_context")
            if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
            else []
        ),
        "not_recorded_basis": _sanitize(
            request.get("not_recorded_basis") if outcome == OUTCOME_NOT_RECORDED else []
        ),
        "what_remains_open": list(_OPEN_ITEMS),
        "non_claims": _canonical_false_non_claims(),
        "outcome": outcome,
        "block": block,
    }
    for field in _POSTURE_FIELDS:
        result[field] = _posture_section(request, field)
    result["post_ongoing_runtime_reusable_runtime_permission_summary"] = (
        build_post_ongoing_runtime_reusable_runtime_permission_summary(result)
    )
    return result


def _malformed_result(code: str, reason: str) -> dict[str, Any]:
    request = {
        "reusable_runtime_permission_request_id": _DEFAULT_REQUEST_ID,
        "reusable_runtime_permission_question": None,
        "reusable_runtime_permission_intent": None,
        "reusable_runtime_permission_scope": [],
    }
    checks: list[dict[str, Any]] = []
    _check(
        checks,
        "declared_reusable_runtime_permission_request_readable",
        False,
        "readable mapping",
        reason,
        code,
    )
    return _build_result(request, checks, OUTCOME_BLOCKED, reason)


def resolve_post_ongoing_runtime_reusable_runtime_permission(
    declared_reusable_runtime_permission_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one bounded reusable-runtime-permission request."""

    if declared_reusable_runtime_permission_request is None:
        return _malformed_result(
            "DECLARED_REUSABLE_RUNTIME_PERMISSION_REQUEST_MALFORMED",
            "declared reusable-runtime-permission request is missing",
        )
    if not isinstance(declared_reusable_runtime_permission_request, Mapping):
        return _malformed_result(
            "DECLARED_REUSABLE_RUNTIME_PERMISSION_REQUEST_MALFORMED",
            "declared reusable-runtime-permission request is not a mapping",
        )

    request = deepcopy(dict(declared_reusable_runtime_permission_request))
    checks = _build_checks(request)
    outcome = _determine_outcome(request, checks)
    return _build_result(request, checks, outcome)


def resolve_post_ongoing_runtime_reusable_runtime_permission_from_path(
    declared_reusable_runtime_permission_request_path: Path | str,
) -> dict:
    """Read and resolve a declared reusable-runtime-permission request path."""

    path = Path(declared_reusable_runtime_permission_request_path)
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        return _malformed_result(
            "DECLARED_REUSABLE_RUNTIME_PERMISSION_REQUEST_UNREADABLE",
            f"declared reusable-runtime-permission request could not be read: {exc}",
        )
    try:
        request = json.loads(raw)
    except json.JSONDecodeError as exc:
        return _malformed_result(
            "DECLARED_REUSABLE_RUNTIME_PERMISSION_REQUEST_UNREADABLE",
            f"declared reusable-runtime-permission request JSON could not be decoded: {exc}",
        )
    if not isinstance(request, Mapping):
        return _malformed_result(
            "DECLARED_REUSABLE_RUNTIME_PERMISSION_REQUEST_MALFORMED",
            "declared reusable-runtime-permission request JSON is not an object",
        )
    return resolve_post_ongoing_runtime_reusable_runtime_permission(request)


def build_post_ongoing_runtime_reusable_runtime_permission_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a deterministic summary for one reusable-runtime-permission result."""

    checks = list(result.get("reusable_runtime_permission_checks", []))
    passed_count = sum(1 for check in checks if check.get("passed") is True)
    failed_count = sum(1 for check in checks if check.get("passed") is not True)
    metadata = result.get("post_ongoing_runtime_reusable_runtime_permission_metadata", {})
    selected = metadata.get("selected_basis_summary", {}) if isinstance(metadata, Mapping) else {}
    question = result.get("declared_reusable_runtime_permission_question", {})
    statement = result.get("reusable_runtime_permission_statement", {})
    block = result.get("block")
    block_code = block.get("block_code") if isinstance(block, Mapping) else None
    block_reason = block.get("block_reason") if isinstance(block, Mapping) else None
    key_non_claims = result.get("non_claims", {})
    no_source_authority_currentness_release_follow_on = all(
        statement.get(key) is True
        for key in (
            "source_not_created",
            "authority_not_created",
            "currentness_not_created",
            "deployment_not_created",
            "public_release_not_created",
            "operation_permission_not_created",
            "follow_on_work_not_authorized",
        )
    )
    return {
        "outcome": result.get("outcome"),
        "block_code": block_code,
        "block_reason": block_reason,
        "request_id": question.get("request_id") if isinstance(question, Mapping) else None,
        "question": question.get("question") if isinstance(question, Mapping) else None,
        "intent": question.get("intent") if isinstance(question, Mapping) else None,
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "reusable_runtime_permission_recorded": statement.get(
            "reusable_runtime_permission_recorded"
        )
        is True,
        "bounded_reusable_runtime_permission_posture_recorded": statement.get(
            "bounded_reusable_runtime_permission_posture_recorded"
        )
        is True,
        "reusable_runtime_permission_boundary_basis_preserved": statement.get(
            "reusable_runtime_permission_boundary_basis_preserved"
        )
        is True,
        "ongoing_runtime_basis_preserved": statement.get("ongoing_runtime_basis_preserved")
        is True,
        "ongoing_runtime_persistence_not_repeatability_without_permission": statement.get(
            "ongoing_runtime_persistence_not_repeatability_without_permission"
        )
        is True,
        "bounded_runtime_reuse_envelope_declared": statement.get(
            "bounded_runtime_reuse_envelope_declared"
        )
        is True,
        "reusable_runtime_permission_not_continuation": statement.get(
            "reusable_runtime_permission_not_continuation"
        )
        is True,
        "reusable_runtime_permission_not_self_continuation": statement.get(
            "reusable_runtime_permission_not_self_continuation"
        )
        is True,
        "reusable_runtime_permission_not_daemon": statement.get(
            "reusable_runtime_permission_not_daemon"
        )
        is True,
        "reusable_runtime_permission_not_loop": statement.get(
            "reusable_runtime_permission_not_loop"
        )
        is True,
        "reusable_runtime_permission_not_public_api": statement.get(
            "reusable_runtime_permission_not_public_api"
        )
        is True,
        "reusable_runtime_permission_not_participant_facing_interface": statement.get(
            "reusable_runtime_permission_not_participant_facing_interface"
        )
        is True,
        "reusable_runtime_permission_not_distributed_network_behavior": statement.get(
            "reusable_runtime_permission_not_distributed_network_behavior"
        )
        is True,
        "continuation_not_authorized": statement.get("continuation_not_authorized")
        is True,
        "self_continuation_not_authorized": statement.get("self_continuation_not_authorized")
        is True,
        "self_recursive_growth_not_created": statement.get("self_recursive_growth_not_created")
        is True,
        "runtime_daemon_not_created": statement.get("runtime_daemon_not_created") is True,
        "runtime_loop_not_created": statement.get("runtime_loop_not_created") is True,
        "public_api_not_created": statement.get("public_api_not_created") is True,
        "participant_facing_interface_not_created": statement.get(
            "participant_facing_interface_not_created"
        )
        is True,
        "distributed_network_behavior_not_created": statement.get(
            "distributed_network_behavior_not_created"
        )
        is True,
        "source_transfer_source_receipt_reception_authorization_not_created": all(
            statement.get(key) is True
            for key in (
                "source_transfer_not_created",
                "source_receipt_not_created",
                "reception_authorization_not_created",
            )
        ),
        "source_authority_currentness_deployment_public_release_operation_permission_follow_on_not_created": no_source_authority_currentness_release_follow_on,
        "hidden_repo_state_excluded": statement.get("hidden_repo_state_excluded") is True,
        "hidden_repo_state_not_used_as_reusable_runtime_permission_authority": statement.get(
            "hidden_repo_state_not_used_as_reusable_runtime_permission_authority"
        )
        is True,
        "repo_local_availability_not_reusable_runtime_permission_authority": statement.get(
            "repo_local_availability_not_reusable_runtime_permission_authority"
        )
        is True,
        "artifact_existence_not_reusable_runtime_permission_authority": statement.get(
            "artifact_existence_not_reusable_runtime_permission_authority"
        )
        is True,
        "latest_file_posture_not_reusable_runtime_permission_authority": statement.get(
            "latest_file_posture_not_reusable_runtime_permission_authority"
        )
        is True,
        "selected_basis_reference_shape_preserved": statement.get(
            "selected_basis_reference_shape_preserved"
        )
        is True,
        "raw_full_prior_artifact_body_not_returned": statement.get(
            "raw_full_prior_artifact_body_not_returned"
        )
        is True,
        "official_enum_scope_strings_not_redacted": statement.get(
            "official_enum_scope_strings_not_redacted"
        )
        is True,
        "hostile_raw_body_content_contained": statement.get(
            "hostile_raw_body_content_contained"
        )
        is True,
        "result_level_non_claims_canonical_false": statement.get(
            "result_level_non_claims_canonical_false"
        )
        is True,
        "selected_reusable_runtime_permission_boundary_outcome": selected.get(
            "selected_reusable_runtime_permission_boundary_outcome"
        ),
        "selected_reusable_runtime_permission_boundary_result_version": selected.get(
            "selected_reusable_runtime_permission_boundary_result_version"
        ),
        "selected_reusable_runtime_permission_boundary_failed_check_count": selected.get(
            "selected_reusable_runtime_permission_boundary_failed_check_count"
        ),
        "selected_ongoing_runtime_outcome": selected.get(
            "selected_ongoing_runtime_outcome"
        ),
        "selected_ongoing_runtime_result_version": selected.get(
            "selected_ongoing_runtime_result_version"
        ),
        "selected_ongoing_runtime_failed_check_count": selected.get(
            "selected_ongoing_runtime_failed_check_count"
        ),
        "selected_ongoing_runtime_boundary_outcome": selected.get(
            "selected_ongoing_runtime_boundary_outcome"
        ),
        "selected_ongoing_runtime_boundary_result_version": selected.get(
            "selected_ongoing_runtime_boundary_result_version"
        ),
        "selected_ongoing_runtime_boundary_failed_check_count": selected.get(
            "selected_ongoing_runtime_boundary_failed_check_count"
        ),
        "selected_runtime_hosting_outcome": selected.get("selected_runtime_hosting_outcome"),
        "selected_runtime_hosting_result_version": selected.get(
            "selected_runtime_hosting_result_version"
        ),
        "selected_runtime_hosting_failed_check_count": selected.get(
            "selected_runtime_hosting_failed_check_count"
        ),
        "selected_runtime_hosting_boundary_v2_outcome": selected.get(
            "selected_runtime_hosting_boundary_v2_outcome"
        ),
        "selected_runtime_hosting_boundary_v2_result_version": selected.get(
            "selected_runtime_hosting_boundary_v2_result_version"
        ),
        "selected_runtime_hosting_boundary_v2_failed_check_count": selected.get(
            "selected_runtime_hosting_boundary_v2_failed_check_count"
        ),
        "selected_successor_runtime_step_outcome": selected.get(
            "selected_successor_runtime_step_outcome"
        ),
        "selected_successor_runtime_step_result_version": selected.get(
            "selected_successor_runtime_step_result_version"
        ),
        "selected_successor_runtime_step_failed_check_count": selected.get(
            "selected_successor_runtime_step_failed_check_count"
        ),
        "selected_minimal_runtime_outcome": selected.get("selected_minimal_runtime_outcome"),
        "selected_minimal_runtime_result_version": selected.get(
            "selected_minimal_runtime_result_version"
        ),
        "selected_minimal_runtime_failed_check_count": selected.get(
            "selected_minimal_runtime_failed_check_count"
        ),
        "selected_runtime_boundary_outcome": selected.get("selected_runtime_boundary_outcome"),
        "selected_runtime_boundary_result_version": selected.get(
            "selected_runtime_boundary_result_version"
        ),
        "selected_runtime_boundary_failed_check_count": selected.get(
            "selected_runtime_boundary_failed_check_count"
        ),
        "selected_runtime_readiness_outcome": selected.get("selected_runtime_readiness_outcome"),
        "selected_runtime_readiness_result_version": selected.get(
            "selected_runtime_readiness_result_version"
        ),
        "selected_runtime_readiness_failed_check_count": selected.get(
            "selected_runtime_readiness_failed_check_count"
        ),
        "selected_final_completion_outcome": selected.get("selected_final_completion_outcome"),
        "selected_final_completion_result_version": selected.get(
            "selected_final_completion_result_version"
        ),
        "selected_final_completion_failed_check_count": selected.get(
            "selected_final_completion_failed_check_count"
        ),
        "selected_post_portable_currentness_surface_path": selected.get(
            "selected_post_portable_currentness_surface_path"
        ),
        "bounded_runtime_reuse_envelope_posture": _sanitize(
            result.get("bounded_runtime_reuse_envelope")
        ),
        "no_continuation_self_continuation_daemon_loop_api_interface_distributed_network_source_authority_currentness_deployment_public_release_follow_on": all(
            value is False for value in key_non_claims.values()
        )
        if isinstance(key_non_claims, Mapping)
        else False,
        "key_non_claims": _sanitize(key_non_claims),
        "predecessor_failure_evidence_preserved": statement.get(
            "predecessor_failure_evidence_preserved"
        )
        is True,
        "consumed_request_token_remains_closed": statement.get(
            "consumed_request_token_remains_closed"
        )
        is True,
        "authorization_token_reuse_blocked": statement.get(
            "authorization_token_reuse_blocked"
        )
        is True,
    }


def _unique_output_path(path: Path) -> Path:
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


def write_post_ongoing_runtime_reusable_runtime_permission_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write a bounded reusable-runtime-permission result JSON without overwriting."""

    metadata = result.get("post_ongoing_runtime_reusable_runtime_permission_metadata", {})
    request_id = (
        metadata.get("post_ongoing_runtime_reusable_runtime_permission_id")
        if isinstance(metadata, Mapping)
        else None
    )
    request_id = str(request_id or _DEFAULT_REQUEST_ID)
    filename = f"{request_id}__post_ongoing_runtime_reusable_runtime_permission_result.json"
    if output_path is None:
        target = OUTPUT_ROOT / filename
    else:
        supplied = Path(output_path)
        target = supplied / filename if supplied.suffix == "" else supplied
    target = _unique_output_path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(_sanitize(dict(result)), indent=2, sort_keys=True, ensure_ascii=False)
        + "\n",
        encoding="utf-8",
    )
    return target


def _basis(name: str, path: str) -> dict[str, Any]:
    return {
        "basis_name": name,
        "reference_shape": True,
        "path": path,
        "basis_only": True,
    }


def _declared_posture(statement: str) -> dict[str, Any]:
    return {"declared": True, "posture": statement}


def _default_bounded_runtime_reuse_envelope() -> dict[str, Any]:
    return {
        "envelope_type": "bounded_runtime_reuse_envelope",
        "scope": (
            "one bounded reusable-runtime-permission posture recorded from selected "
            "standing reusable-runtime-permission-boundary and ongoing-runtime basis"
        ),
        "runtime_reuse_limited_to_declared_envelope": True,
        "arbitrary_runtime_activity_authorized": False,
        "authorizes_continuation": False,
        "authorizes_self_continuation": False,
        "creates_self_recursive_growth": False,
        "creates_runtime_daemon": False,
        "creates_runtime_loop": False,
        "creates_public_api": False,
        "creates_participant_facing_interface": False,
        "creates_distributed_network_behavior": False,
        "creates_source_transfer": False,
        "creates_source_receipt": False,
        "creates_reception_authorization": False,
        "creates_source": False,
        "creates_authority": False,
        "creates_currentness": False,
        "creates_deployment": False,
        "creates_public_release": False,
        "creates_operation_permission": False,
        "creates_broader_reusable_permission": False,
        "creates_derivative_reception": False,
        "creates_vessel_relation": False,
        "creates_another_reception_request": False,
        "creates_adoption": False,
        "creates_receiving_context_governance": False,
        "creates_publication_flow": False,
        "authorizes_follow_on_work": False,
        "anything_outside_envelope_requires_fresh_admission": True,
    }


def build_declared_post_ongoing_runtime_reusable_runtime_permission_request(
    reusable_runtime_permission_request_id: str = _DEFAULT_REQUEST_ID,
    reusable_runtime_permission_scope: list[str] | tuple[str, ...] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build a clean declared reusable-runtime-permission request."""

    scope = list(reusable_runtime_permission_scope or SUPPORTED_SCOPE_VALUES)
    request: dict[str, Any] = {
        "reusable_runtime_permission_request_id": reusable_runtime_permission_request_id,
        "reusable_runtime_permission_question": CORE_QUESTION,
        "reusable_runtime_permission_intent": INTENT_RECORD,
        "selected_reusable_runtime_permission_boundary_basis": _basis(
            "post_ongoing_runtime_reusable_runtime_permission_boundary",
            "artifacts/integrity_host_v0_min_coexistence_post_ongoing_runtime_reusable_runtime_permission_boundary/post_ongoing_runtime_reusable_runtime_permission_boundary_reference_review_001__post_ongoing_runtime_reusable_runtime_permission_boundary_result.json",
        ),
        "selected_reusable_runtime_permission_boundary_terminal_summary_basis": _basis(
            "post_ongoing_runtime_reusable_runtime_permission_boundary_terminal_summary",
            "spec/POST_ONGOING_RUNTIME_REUSABLE_RUNTIME_PERMISSION_BOUNDARY_TERMINAL_SUMMARY_V0.md",
        ),
        "selected_reusable_runtime_permission_boundary_result_path": "artifacts/integrity_host_v0_min_coexistence_post_ongoing_runtime_reusable_runtime_permission_boundary/post_ongoing_runtime_reusable_runtime_permission_boundary_reference_review_001__post_ongoing_runtime_reusable_runtime_permission_boundary_result.json",
        "selected_reusable_runtime_permission_boundary_result_outcome": EXPECTED_REUSABLE_RUNTIME_PERMISSION_BOUNDARY_OUTCOME,
        "selected_reusable_runtime_permission_boundary_result_version": "0.1.0",
        "selected_reusable_runtime_permission_boundary_failed_check_count": 0,
        "selected_reusable_runtime_permission_boundary_declared_future_review": True,
        "selected_reusable_runtime_permission_boundary_already_created_reusable_runtime_permission": False,
        "selected_reusable_runtime_permission_boundary_already_authorized_continuation": False,
        "selected_reusable_runtime_permission_boundary_already_authorized_self_continuation": False,
        "selected_reusable_runtime_permission_boundary_already_created_runtime_daemon": False,
        "selected_reusable_runtime_permission_boundary_already_created_runtime_loop": False,
        "selected_reusable_runtime_permission_boundary_already_created_public_api": False,
        "selected_reusable_runtime_permission_boundary_already_created_participant_facing_interface": False,
        "selected_reusable_runtime_permission_boundary_already_created_distributed_network_behavior": False,
        "selected_reusable_runtime_permission_boundary_treated_as_reusable_runtime_permission": False,
        "selected_reusable_runtime_permission_boundary_treated_as_continuation": False,
        "selected_reusable_runtime_permission_boundary_treated_as_self_continuation": False,
        "selected_reusable_runtime_permission_boundary_authorized_future_work": False,
        "selected_reusable_runtime_permission_boundary_non_claims_canonicalized": True,
        "selected_ongoing_runtime_basis": _basis(
            "post_runtime_hosting_ongoing_runtime",
            "artifacts/integrity_host_v0_min_coexistence_post_runtime_hosting_ongoing_runtime/post_runtime_hosting_ongoing_runtime_reference_review_001__post_runtime_hosting_ongoing_runtime_result.json",
        ),
        "selected_ongoing_runtime_terminal_summary_basis": _basis(
            "post_runtime_hosting_ongoing_runtime_terminal_summary",
            "spec/POST_RUNTIME_HOSTING_ONGOING_RUNTIME_TERMINAL_SUMMARY_V0.md",
        ),
        "selected_ongoing_runtime_result_path": "artifacts/integrity_host_v0_min_coexistence_post_runtime_hosting_ongoing_runtime/post_runtime_hosting_ongoing_runtime_reference_review_001__post_runtime_hosting_ongoing_runtime_result.json",
        "selected_ongoing_runtime_result_outcome": EXPECTED_ONGOING_RUNTIME_OUTCOME,
        "selected_ongoing_runtime_result_version": "0.1.0",
        "selected_ongoing_runtime_failed_check_count": 0,
        "selected_ongoing_runtime_bounded_ongoing_runtime_posture_recorded": True,
        "selected_ongoing_runtime_bounded_persistence_posture_recorded": True,
        "selected_ongoing_runtime_persistence_treated_as_repeatability_before_permission": False,
        "selected_ongoing_runtime_persistence_authorized_reuse_before_permission": False,
        "selected_ongoing_runtime_already_authorized_continuation": False,
        "selected_ongoing_runtime_already_authorized_self_continuation": False,
        "selected_ongoing_runtime_boundary_basis": _basis(
            "post_runtime_hosting_ongoing_runtime_boundary",
            "artifacts/integrity_host_v0_min_coexistence_post_runtime_hosting_ongoing_runtime_boundary/post_runtime_hosting_ongoing_runtime_boundary_reference_review_001__post_runtime_hosting_ongoing_runtime_boundary_result.json",
        ),
        "selected_ongoing_runtime_boundary_result_path": "artifacts/integrity_host_v0_min_coexistence_post_runtime_hosting_ongoing_runtime_boundary/post_runtime_hosting_ongoing_runtime_boundary_reference_review_001__post_runtime_hosting_ongoing_runtime_boundary_result.json",
        "selected_ongoing_runtime_boundary_result_outcome": EXPECTED_ONGOING_RUNTIME_BOUNDARY_OUTCOME,
        "selected_ongoing_runtime_boundary_result_version": "0.1.0",
        "selected_ongoing_runtime_boundary_failed_check_count": 0,
        "selected_runtime_hosting_basis": _basis(
            "post_successor_runtime_step_runtime_hosting",
            "artifacts/integrity_host_v0_min_coexistence_post_successor_runtime_step_runtime_hosting/post_successor_runtime_step_runtime_hosting_reference_review_001__post_successor_runtime_step_runtime_hosting_result.json",
        ),
        "selected_runtime_hosting_result_path": "artifacts/integrity_host_v0_min_coexistence_post_successor_runtime_step_runtime_hosting/post_successor_runtime_step_runtime_hosting_reference_review_001__post_successor_runtime_step_runtime_hosting_result.json",
        "selected_runtime_hosting_result_outcome": EXPECTED_RUNTIME_HOSTING_OUTCOME,
        "selected_runtime_hosting_result_version": "0.1.0",
        "selected_runtime_hosting_failed_check_count": 0,
        "selected_runtime_hosting_boundary_v2_basis": _basis(
            "post_successor_runtime_step_runtime_hosting_boundary_v2",
            "artifacts/integrity_host_v0_min_coexistence_post_successor_runtime_step_runtime_hosting_boundary_v2/post_successor_runtime_step_runtime_hosting_boundary_v2_reference_review_001__post_successor_runtime_step_runtime_hosting_boundary_v2_result.json",
        ),
        "selected_runtime_hosting_boundary_v2_result_path": "artifacts/integrity_host_v0_min_coexistence_post_successor_runtime_step_runtime_hosting_boundary_v2/post_successor_runtime_step_runtime_hosting_boundary_v2_reference_review_001__post_successor_runtime_step_runtime_hosting_boundary_v2_result.json",
        "selected_runtime_hosting_boundary_v2_result_outcome": EXPECTED_RUNTIME_HOSTING_BOUNDARY_V2_OUTCOME,
        "selected_runtime_hosting_boundary_v2_result_version": "0.2.0",
        "selected_runtime_hosting_boundary_v2_failed_check_count": 0,
        "selected_runtime_hosting_boundary_v1_failure_lineage_basis": _basis(
            "post_successor_runtime_step_runtime_hosting_boundary_v1_failure_lineage",
            "src/resolve_post_successor_runtime_step_runtime_hosting_boundary.py",
        ),
        "selected_runtime_hosting_boundary_v1_failure_repaired": False,
        "selected_runtime_hosting_boundary_v1_failure_hidden": False,
        "selected_runtime_hosting_boundary_v1_failure_claimed_passed": False,
        "selected_successor_runtime_step_basis": _basis(
            "post_minimal_runtime_successor_runtime_step",
            "artifacts/integrity_host_v0_min_coexistence_post_minimal_runtime_successor_runtime_step/post_minimal_runtime_successor_runtime_step_reference_review_001__post_minimal_runtime_successor_runtime_step_result.json",
        ),
        "selected_successor_runtime_step_result_path": "artifacts/integrity_host_v0_min_coexistence_post_minimal_runtime_successor_runtime_step/post_minimal_runtime_successor_runtime_step_reference_review_001__post_minimal_runtime_successor_runtime_step_result.json",
        "selected_successor_runtime_step_result_outcome": EXPECTED_SUCCESSOR_RUNTIME_STEP_OUTCOME,
        "selected_successor_runtime_step_result_version": "0.1.0",
        "selected_successor_runtime_step_failed_check_count": 0,
        "selected_minimal_runtime_basis": _basis(
            "post_portable_verification_minimal_runtime",
            "artifacts/integrity_host_v0_min_coexistence_post_portable_verification_minimal_runtime/post_portable_verification_minimal_runtime_reference_review_001__post_portable_verification_minimal_runtime_result.json",
        ),
        "selected_minimal_runtime_result_path": "artifacts/integrity_host_v0_min_coexistence_post_portable_verification_minimal_runtime/post_portable_verification_minimal_runtime_reference_review_001__post_portable_verification_minimal_runtime_result.json",
        "selected_minimal_runtime_result_outcome": EXPECTED_MINIMAL_RUNTIME_OUTCOME,
        "selected_minimal_runtime_result_version": "0.1.0",
        "selected_minimal_runtime_failed_check_count": 0,
        "selected_runtime_boundary_basis": _basis(
            "post_portable_verification_runtime_boundary",
            "artifacts/integrity_host_v0_min_coexistence_post_portable_verification_runtime_boundary/post_portable_verification_runtime_boundary_reference_review_001__post_portable_verification_runtime_boundary_result.json",
        ),
        "selected_runtime_boundary_result_path": "artifacts/integrity_host_v0_min_coexistence_post_portable_verification_runtime_boundary/post_portable_verification_runtime_boundary_reference_review_001__post_portable_verification_runtime_boundary_result.json",
        "selected_runtime_boundary_result_outcome": EXPECTED_RUNTIME_BOUNDARY_OUTCOME,
        "selected_runtime_boundary_result_version": "0.1.0",
        "selected_runtime_boundary_failed_check_count": 0,
        "selected_runtime_readiness_basis": _basis(
            "post_portable_verification_runtime_readiness",
            "artifacts/integrity_host_v0_min_coexistence_post_portable_verification_runtime_readiness/post_portable_verification_runtime_readiness_reference_review_001__post_portable_verification_runtime_readiness_result.json",
        ),
        "selected_runtime_readiness_result_path": "artifacts/integrity_host_v0_min_coexistence_post_portable_verification_runtime_readiness/post_portable_verification_runtime_readiness_reference_review_001__post_portable_verification_runtime_readiness_result.json",
        "selected_runtime_readiness_result_outcome": EXPECTED_RUNTIME_READINESS_OUTCOME,
        "selected_runtime_readiness_result_version": "0.1.0",
        "selected_runtime_readiness_failed_check_count": 0,
        "selected_portable_verification_final_completion_basis": _basis(
            "portable_source_body_verification_final_completion",
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_TERMINAL_SUMMARY_V0.md",
        ),
        "selected_portable_verification_final_completion_result_path": "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_final_completion/portable_source_body_verification_final_completion_reference_review_001__portable_source_body_verification_final_completion_result.json",
        "selected_portable_verification_final_completion_result_outcome": EXPECTED_FINAL_COMPLETION_OUTCOME,
        "selected_portable_verification_final_completion_result_version": "0.1.0",
        "selected_portable_verification_final_completion_failed_check_count": 0,
        "selected_post_portable_verification_currentness_basis": _basis(
            "post_portable_verification_currentness_surface",
            "spec/POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_V0.md",
        ),
        "selected_post_portable_currentness_surface_path": "spec/POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_V0.md",
        "selected_post_portable_currentness_surface_states_checkability_not_continuation": True,
        "selected_post_portable_currentness_surface_authorized_next_work": False,
        "selected_returned_second_carrier_capture_lineage_basis": _basis(
            "returned_second_carrier_capture_lineage",
            "reference-shaped lineage basis only",
        ),
        "reusable_runtime_permission_scope": scope,
        "requested_bounded_runtime_reuse_envelope": _default_bounded_runtime_reuse_envelope(),
        "declared_non_claims": _canonical_false_non_claims(),
        "reference_shaped_input_posture": True,
        "requested_reusable_runtime_permission_outcome": OUTCOME_RECORDED,
    }
    for field in _POSTURE_FIELDS:
        request[field] = _declared_posture(field)
    for key in REQUIRED_FALSE_NON_CLAIMS:
        request.setdefault(key, False)
    request.update(overrides)
    return request
