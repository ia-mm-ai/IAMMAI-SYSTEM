"""Resolve one bounded post-continuation self-continuation posture.

This module is downstream of the post-continuation self-continuation-boundary
line. It records, at most, one bounded self-continuation posture and one
bounded self-continuation envelope. Self-continuation here is not
self-recursive growth, runtime daemon or loop behavior, public API,
participant-facing interface, distributed network behavior, source transfer,
source receipt, reception authorization, source, authority, currentness,
deployment, public release, operation permission, broader reusable permission,
or follow-on work.
"""

from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any


class PostContinuationSelfContinuationError(Exception):
    """Raised for bounded self-continuation resolver I/O errors."""


def _tokens(value: str) -> tuple[str, ...]:
    return tuple(value.split())


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_post_continuation_self_continuation"

OUTCOME_RECORDED = "POST_CONTINUATION_SELF_CONTINUATION_RECORDED"
OUTCOME_NOT_RECORDED = "POST_CONTINUATION_SELF_CONTINUATION_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "POST_CONTINUATION_SELF_CONTINUATION_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "POST_CONTINUATION_SELF_CONTINUATION_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_post_continuation_self_continuation"
)

INTENT_RECORD = "RECORD_POST_CONTINUATION_SELF_CONTINUATION"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_POST_CONTINUATION_SELF_CONTINUATION"
INTENT_BLOCK = "BLOCK_POST_CONTINUATION_SELF_CONTINUATION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

CORE_QUESTION = (
    "Can the clean post-continuation self-continuation-boundary basis be used "
    "to record one bounded self-continuation posture without creating "
    "self-recursive growth, runtime daemon, runtime loop, public API, "
    "participant-facing interface, distributed network behavior, source "
    "transfer, source receipt, reception authorization, source, authority, "
    "currentness, deployment, public release, operation permission, broader "
    "reusable permission, derivative reception, vessel relation, another "
    "reception request, adoption, receiving-context governance, publication "
    "flow, or follow-on work?"
)

EXPECTED_SELF_CONTINUATION_BOUNDARY_OUTCOME = (
    "POST_CONTINUATION_SELF_CONTINUATION_BOUNDARY_RECORDED"
)
EXPECTED_CONTINUATION_OUTCOME = "POST_REUSABLE_RUNTIME_PERMISSION_CONTINUATION_RECORDED"
EXPECTED_CONTINUATION_BOUNDARY_OUTCOME = (
    "POST_REUSABLE_RUNTIME_PERMISSION_CONTINUATION_BOUNDARY_RECORDED"
)
EXPECTED_REUSABLE_RUNTIME_PERMISSION_OUTCOME = (
    "POST_ONGOING_RUNTIME_REUSABLE_RUNTIME_PERMISSION_RECORDED"
)
EXPECTED_REUSABLE_RUNTIME_PERMISSION_BOUNDARY_OUTCOME = (
    "POST_ONGOING_RUNTIME_REUSABLE_RUNTIME_PERMISSION_BOUNDARY_RECORDED"
)
EXPECTED_ONGOING_RUNTIME_OUTCOME = "POST_RUNTIME_HOSTING_ONGOING_RUNTIME_RECORDED"
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
    SELF_CONTINUATION_SPEC_ONLY
    ONE_BOUNDED_SELF_CONTINUATION_POSTURE_RECORDED
    SELF_CONTINUATION_BOUNDARY_BASIS_PRESERVED
    CONTINUATION_BASIS_PRESERVED
    BOUNDED_CONTINUATION_ENVELOPE_PRESERVED
    BOUNDED_SELF_CONTINUATION_ENVELOPE_DECLARED
    SELF_CONTINUATION_NOT_SELF_RECURSIVE_GROWTH
    SELF_CONTINUATION_NOT_DAEMON
    SELF_CONTINUATION_NOT_LOOP
    SELF_CONTINUATION_NOT_PUBLIC_API
    SELF_CONTINUATION_NOT_PARTICIPANT_FACING_INTERFACE
    SELF_CONTINUATION_NOT_DISTRIBUTED_NETWORK_BEHAVIOR
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
    NO_SELF_RECURSIVE_GROWTH_INFERENCE
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
    HIDDEN_REPO_STATE_NOT_USED_AS_SELF_CONTINUATION_AUTHORITY
    REPO_LOCAL_AVAILABILITY_NOT_SELF_CONTINUATION_AUTHORITY
    ARTIFACT_EXISTENCE_NOT_SELF_CONTINUATION_AUTHORITY
    LATEST_FILE_POSTURE_NOT_SELF_CONTINUATION_AUTHORITY
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
SUPPORTED_SELF_CONTINUATION_SCOPE = SUPPORTED_SCOPE_VALUES

ALLOWED_TRUE_RECORDED_FIELDS = _tokens(
    """
    self_continuation_recorded
    bounded_self_continuation_posture_recorded
    self_continuation_boundary_basis_preserved
    continuation_basis_preserved
    bounded_continuation_envelope_preserved
    bounded_self_continuation_envelope_declared
    self_continuation_not_self_recursive_growth
    self_continuation_not_daemon
    self_continuation_not_loop
    self_continuation_not_public_api
    self_continuation_not_participant_facing_interface
    self_continuation_not_distributed_network_behavior
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
    hidden_repo_state_not_used_as_self_continuation_authority
    repo_local_availability_not_self_continuation_authority
    artifact_existence_not_self_continuation_authority
    latest_file_posture_not_self_continuation_authority
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

REQUIRED_FALSE_NON_CLAIMS = _tokens(
    """
    self_continuation_created_before_review
    self_recursive_growth_created
    runtime_daemon_created
    runtime_loop_created
    public_api_created
    participant_facing_interface_created
    distributed_network_behavior_created
    source_transfer_occurred
    source_receipt_occurred
    reception_authorization_created
    self_continuation_treated_as_self_recursive_growth
    self_continuation_treated_as_runtime_daemon
    self_continuation_treated_as_runtime_loop
    self_continuation_treated_as_public_api
    self_continuation_treated_as_participant_facing_interface
    self_continuation_treated_as_distributed_network_behavior
    self_continuation_treated_as_source_transfer
    self_continuation_treated_as_source_receipt
    self_continuation_treated_as_reception_authorization
    self_continuation_treated_as_source
    self_continuation_treated_as_authority
    self_continuation_treated_as_currentness
    self_continuation_treated_as_deployment
    self_continuation_treated_as_public_release
    self_continuation_treated_as_operation_permission
    self_continuation_treated_as_broader_reusable_permission
    self_continuation_treated_as_follow_on_work
    self_continuation_boundary_treated_as_self_continuation_without_review
    continuation_treated_as_self_continuation_without_review
    bounded_continuation_envelope_treated_as_self_continuation_without_review
    bounded_continuation_envelope_authorized_arbitrary_runtime_activity_before_review
    artifact_existence_treated_as_self_continuation_authority
    artifact_path_treated_as_currentness
    latest_file_posture_treated_as_self_continuation_authority
    repo_local_availability_treated_as_self_continuation_authority
    hidden_repo_state_used_as_self_continuation_content
    hidden_repo_state_used_as_self_continuation_authority
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
    runtime_hosting_boundary_v1_failure_repaired
    runtime_hosting_boundary_v1_failure_hidden
    runtime_hosting_boundary_v1_failure_claimed_passed
    """
)

BLOCK_CODES = _tokens(
    """
    SELF_CONTINUATION_QUESTION_UNDECLARED
    SELF_CONTINUATION_INTENT_UNSUPPORTED
    SELF_CONTINUATION_EXPLICIT_BLOCK_REQUESTED
    SELF_CONTINUATION_BOUNDARY_BASIS_MISSING
    SELF_CONTINUATION_BOUNDARY_TERMINAL_SUMMARY_BASIS_MISSING
    SELF_CONTINUATION_BOUNDARY_NOT_RECORDED
    SELF_CONTINUATION_BOUNDARY_FAILED_CHECKS_PRESENT
    SELF_CONTINUATION_BOUNDARY_VERSION_NOT_0_1_0
    SELF_CONTINUATION_BOUNDARY_DID_NOT_DECLARE_FUTURE_SELF_CONTINUATION_REVIEW
    SELF_CONTINUATION_BOUNDARY_ALREADY_AUTHORIZED_SELF_CONTINUATION
    SELF_CONTINUATION_BOUNDARY_ALREADY_CREATED_SELF_RECURSIVE_GROWTH
    SELF_CONTINUATION_BOUNDARY_ALREADY_CREATED_RUNTIME_DAEMON
    SELF_CONTINUATION_BOUNDARY_ALREADY_CREATED_RUNTIME_LOOP
    SELF_CONTINUATION_BOUNDARY_ALREADY_CREATED_PUBLIC_API
    SELF_CONTINUATION_BOUNDARY_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE
    SELF_CONTINUATION_BOUNDARY_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR
    SELF_CONTINUATION_BOUNDARY_TREATED_AS_SELF_CONTINUATION
    SELF_CONTINUATION_BOUNDARY_TREATED_AS_SELF_RECURSIVE_GROWTH
    SELF_CONTINUATION_BOUNDARY_AUTHORIZED_FUTURE_WORK
    SELF_CONTINUATION_BOUNDARY_DID_NOT_CANONICALIZE_NON_CLAIMS
    SELF_CONTINUATION_BOUNDARY_TERMINAL_SUMMARY_DID_NOT_PRESERVE_NO_SELF_CONTINUATION
    SELF_CONTINUATION_BOUNDARY_TERMINAL_SUMMARY_DID_NOT_REQUIRE_SEPARATE_REVIEW
    CONTINUATION_BASIS_MISSING
    CONTINUATION_TERMINAL_SUMMARY_BASIS_MISSING
    CONTINUATION_NOT_RECORDED
    CONTINUATION_FAILED_CHECKS_PRESENT
    CONTINUATION_VERSION_NOT_0_1_0
    CONTINUATION_DID_NOT_RECORD_BOUNDED_CONTINUATION_POSTURE
    CONTINUATION_DID_NOT_RECORD_BOUNDED_CONTINUATION_ENVELOPE
    CONTINUATION_ALREADY_CREATED_SELF_RECURSIVE_GROWTH
    CONTINUATION_ALREADY_CREATED_RUNTIME_DAEMON
    CONTINUATION_ALREADY_CREATED_RUNTIME_LOOP
    CONTINUATION_ALREADY_CREATED_PUBLIC_API
    CONTINUATION_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE
    CONTINUATION_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR
    BOUNDED_CONTINUATION_ENVELOPE_TREATED_AS_SELF_CONTINUATION_BEFORE_REVIEW
    BOUNDED_CONTINUATION_ENVELOPE_AUTHORIZED_ARBITRARY_RUNTIME_ACTIVITY_BEFORE_REVIEW
    CONTINUATION_BOUNDARY_BASIS_MISSING
    CONTINUATION_BOUNDARY_NOT_RECORDED
    CONTINUATION_BOUNDARY_FAILED_CHECKS_PRESENT
    CONTINUATION_BOUNDARY_VERSION_NOT_0_1_0
    REUSABLE_RUNTIME_PERMISSION_BASIS_MISSING
    REUSABLE_RUNTIME_PERMISSION_NOT_RECORDED
    REUSABLE_RUNTIME_PERMISSION_FAILED_CHECKS_PRESENT
    REUSABLE_RUNTIME_PERMISSION_VERSION_NOT_0_1_0
    REUSABLE_RUNTIME_PERMISSION_BOUNDARY_BASIS_MISSING
    REUSABLE_RUNTIME_PERMISSION_BOUNDARY_NOT_RECORDED
    REUSABLE_RUNTIME_PERMISSION_BOUNDARY_FAILED_CHECKS_PRESENT
    REUSABLE_RUNTIME_PERMISSION_BOUNDARY_VERSION_NOT_0_1_0
    ONGOING_RUNTIME_BASIS_MISSING
    ONGOING_RUNTIME_NOT_RECORDED
    ONGOING_RUNTIME_FAILED_CHECKS_PRESENT
    ONGOING_RUNTIME_VERSION_NOT_0_1_0
    RUNTIME_HOSTING_BASIS_MISSING
    RUNTIME_HOSTING_NOT_RECORDED
    RUNTIME_HOSTING_FAILED_CHECKS_PRESENT
    RUNTIME_HOSTING_VERSION_NOT_0_1_0
    RUNTIME_HOSTING_BOUNDARY_V2_BASIS_MISSING
    RUNTIME_HOSTING_BOUNDARY_V2_NOT_RECORDED
    RUNTIME_HOSTING_BOUNDARY_V2_FAILED_CHECKS_PRESENT
    RUNTIME_HOSTING_BOUNDARY_V2_VERSION_NOT_0_2_0
    RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_LINEAGE_MISSING
    RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED
    SUCCESSOR_RUNTIME_STEP_BASIS_MISSING
    SUCCESSOR_RUNTIME_STEP_NOT_RECORDED
    SUCCESSOR_RUNTIME_STEP_FAILED_CHECKS_PRESENT
    SUCCESSOR_RUNTIME_STEP_VERSION_NOT_0_1_0
    MINIMAL_RUNTIME_BASIS_MISSING
    MINIMAL_RUNTIME_NOT_RECORDED
    MINIMAL_RUNTIME_FAILED_CHECKS_PRESENT
    MINIMAL_RUNTIME_VERSION_NOT_0_1_0
    RUNTIME_BOUNDARY_BASIS_MISSING
    RUNTIME_BOUNDARY_NOT_RECORDED
    RUNTIME_BOUNDARY_FAILED_CHECKS_PRESENT
    RUNTIME_BOUNDARY_VERSION_NOT_0_1_0
    RUNTIME_READINESS_BASIS_MISSING
    RUNTIME_READINESS_NOT_RECORDED
    RUNTIME_READINESS_FAILED_CHECKS_PRESENT
    RUNTIME_READINESS_VERSION_NOT_0_1_0
    PORTABLE_VERIFICATION_FINAL_COMPLETION_BASIS_MISSING
    PORTABLE_VERIFICATION_FINAL_COMPLETION_NOT_RECORDED
    PORTABLE_VERIFICATION_FINAL_COMPLETION_FAILED_CHECKS_PRESENT
    PORTABLE_VERIFICATION_FINAL_COMPLETION_VERSION_NOT_0_1_0
    POST_PORTABLE_CURRENTNESS_SURFACE_BASIS_MISSING
    POST_PORTABLE_CURRENTNESS_SURFACE_TREATED_CHECKABILITY_AS_CONTINUATION
    POST_PORTABLE_CURRENTNESS_SURFACE_AUTHORIZED_NEXT_WORK
    RETURNED_SECOND_CARRIER_CAPTURE_LINEAGE_BASIS_MISSING
    SELF_CONTINUATION_REQUIRED_POSTURE_MISSING
    BOUNDED_SELF_CONTINUATION_ENVELOPE_UNDECLARED
    BOUNDED_SELF_CONTINUATION_ENVELOPE_OVERBROAD
    SELF_CONTINUATION_CREATED_BEFORE_REVIEW
    SELF_CONTINUATION_TREATED_AS_SELF_RECURSIVE_GROWTH
    SELF_CONTINUATION_TREATED_AS_RUNTIME_DAEMON
    SELF_CONTINUATION_TREATED_AS_RUNTIME_LOOP
    SELF_CONTINUATION_TREATED_AS_PUBLIC_API
    SELF_CONTINUATION_TREATED_AS_PARTICIPANT_FACING_INTERFACE
    SELF_CONTINUATION_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR
    SELF_CONTINUATION_TREATED_AS_SOURCE_TRANSFER
    SELF_CONTINUATION_TREATED_AS_SOURCE_RECEIPT
    SELF_CONTINUATION_TREATED_AS_RECEPTION_AUTHORIZATION
    SELF_CONTINUATION_TREATED_AS_SOURCE
    SELF_CONTINUATION_TREATED_AS_AUTHORITY
    SELF_CONTINUATION_TREATED_AS_CURRENTNESS
    SELF_CONTINUATION_TREATED_AS_DEPLOYMENT
    SELF_CONTINUATION_TREATED_AS_PUBLIC_RELEASE
    SELF_CONTINUATION_TREATED_AS_OPERATION_PERMISSION
    SELF_CONTINUATION_TREATED_AS_BROADER_REUSABLE_PERMISSION
    SELF_CONTINUATION_TREATED_AS_FOLLOW_ON_WORK
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
    ANOTHER_RECEPTION_REQUEST_AUTHORIZED
    ADOPTION_CREATED
    RECEIVING_CONTEXT_GOVERNANCE_CREATED
    PUBLICATION_FLOW_CREATED
    FOLLOW_ON_WORK_AUTHORIZED
    ARTIFACT_EXISTENCE_TREATED_AS_SELF_CONTINUATION_AUTHORITY
    ARTIFACT_PATH_TREATED_AS_CURRENTNESS
    LATEST_FILE_POSTURE_TREATED_AS_SELF_CONTINUATION_AUTHORITY
    REPO_LOCAL_AVAILABILITY_TREATED_AS_SELF_CONTINUATION_AUTHORITY
    HIDDEN_REPO_STATE_USED_AS_SELF_CONTINUATION_CONTENT
    HIDDEN_REPO_STATE_USED_AS_SELF_CONTINUATION_AUTHORITY
    SELECTED_BASIS_NOT_REFERENCE_SHAPED
    RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED
    OFFICIAL_ENUM_SCOPE_STRINGS_REDACTED
    HOSTILE_RAW_BODY_CONTENT_NOT_CONTAINED
    PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED
    CONSUMED_REQUEST_REOPENED
    AUTHORIZATION_TOKEN_REUSED
    NON_CLAIM_MISSING_OR_FLIPPED
    UNSUPPORTED_SELF_CONTINUATION_SCOPE
    DECLARED_SELF_CONTINUATION_REQUEST_MALFORMED
    DECLARED_SELF_CONTINUATION_REQUEST_UNREADABLE
    """
)

POSTURE_FIELD_TO_STATEMENT_FIELD = {
    "self_continuation_spec_only_posture": "self_continuation_recorded",
    "one_bounded_self_continuation_posture": "bounded_self_continuation_posture_recorded",
    "self_continuation_boundary_basis_preserved_posture": (
        "self_continuation_boundary_basis_preserved"
    ),
    "continuation_basis_preserved_posture": "continuation_basis_preserved",
    "bounded_continuation_envelope_preserved_posture": (
        "bounded_continuation_envelope_preserved"
    ),
    "bounded_self_continuation_envelope_declared_posture": (
        "bounded_self_continuation_envelope_declared"
    ),
    "self_continuation_not_self_recursive_growth_posture": (
        "self_continuation_not_self_recursive_growth"
    ),
    "self_continuation_not_daemon_posture": "self_continuation_not_daemon",
    "self_continuation_not_loop_posture": "self_continuation_not_loop",
    "self_continuation_not_public_api_posture": "self_continuation_not_public_api",
    "self_continuation_not_participant_facing_interface_posture": (
        "self_continuation_not_participant_facing_interface"
    ),
    "self_continuation_not_distributed_network_behavior_posture": (
        "self_continuation_not_distributed_network_behavior"
    ),
    "self_recursive_growth_not_created_posture": "self_recursive_growth_not_created",
    "runtime_daemon_not_created_posture": "runtime_daemon_not_created",
    "runtime_loop_not_created_posture": "runtime_loop_not_created",
    "public_api_not_created_posture": "public_api_not_created",
    "participant_facing_interface_not_created_posture": (
        "participant_facing_interface_not_created"
    ),
    "distributed_network_behavior_not_created_posture": (
        "distributed_network_behavior_not_created"
    ),
    "source_transfer_not_created_posture": "source_transfer_not_created",
    "source_receipt_not_created_posture": "source_receipt_not_created",
    "reception_authorization_not_created_posture": "reception_authorization_not_created",
    "source_not_created_posture": "source_not_created",
    "authority_not_created_posture": "authority_not_created",
    "currentness_not_created_posture": "currentness_not_created",
    "deployment_not_created_posture": "deployment_not_created",
    "public_release_not_created_posture": "public_release_not_created",
    "operation_permission_not_created_posture": "operation_permission_not_created",
    "broader_reusable_permission_not_created_posture": (
        "broader_reusable_permission_not_created"
    ),
    "follow_on_work_not_authorized_posture": "follow_on_work_not_authorized",
    "hidden_repo_state_excluded_posture": "hidden_repo_state_excluded",
    "repo_local_availability_not_self_continuation_authority_posture": (
        "repo_local_availability_not_self_continuation_authority"
    ),
    "artifact_existence_not_self_continuation_authority_posture": (
        "artifact_existence_not_self_continuation_authority"
    ),
    "latest_file_posture_not_self_continuation_authority_posture": (
        "latest_file_posture_not_self_continuation_authority"
    ),
    "selected_basis_reference_shape_posture": "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned_posture": (
        "raw_full_prior_artifact_body_not_returned"
    ),
    "official_enum_scope_strings_not_redacted_posture": (
        "official_enum_scope_strings_not_redacted"
    ),
    "hostile_raw_body_content_contained_posture": "hostile_raw_body_content_contained",
    "predecessor_failure_evidence_preserved_posture": (
        "predecessor_failure_evidence_preserved"
    ),
    "result_level_non_claims_canonical_false_posture": (
        "result_level_non_claims_canonical_false"
    ),
}
POSTURE_FIELDS = tuple(POSTURE_FIELD_TO_STATEMENT_FIELD)

SELECTED_BASIS_FIELDS = (
    "selected_self_continuation_boundary_basis",
    "selected_self_continuation_boundary_terminal_summary_basis",
    "selected_continuation_basis",
    "selected_continuation_terminal_summary_basis",
    "selected_continuation_boundary_basis",
    "selected_reusable_runtime_permission_basis",
    "selected_reusable_runtime_permission_boundary_basis",
    "selected_ongoing_runtime_basis",
    "selected_runtime_hosting_basis",
    "selected_runtime_hosting_boundary_v2_basis",
    "selected_runtime_hosting_boundary_v1_failure_lineage_basis",
    "selected_successor_runtime_step_basis",
    "selected_minimal_runtime_basis",
    "selected_runtime_boundary_basis",
    "selected_runtime_readiness_basis",
    "selected_portable_verification_final_completion_basis",
    "selected_post_portable_verification_currentness_basis",
    "selected_returned_second_carrier_capture_lineage_basis",
)

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_self_continuation_body",
    "raw_bounded_self_continuation_envelope_body",
    "raw_self_recursive_growth_body",
    "raw_runtime_daemon_body",
    "raw_runtime_loop_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "raw_runtime_body",
    "self_continuation_body",
    "bounded_self_continuation_envelope_body",
    "runtime_body",
    "source_body",
    "authority_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
}

HOSTILE_SENTINELS = (
    "RAW_SELF_CONTINUATION_BODY_MUST_NOT_RETURN",
    "RAW_BOUNDED_SELF_CONTINUATION_ENVELOPE_BODY_MUST_NOT_RETURN",
    "RAW_SELF_RECURSIVE_GROWTH_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_DAEMON_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_LOOP_BODY_MUST_NOT_RETURN",
    "RAW_PUBLIC_API_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPANT_FACING_INTERFACE_BODY_MUST_NOT_RETURN",
    "RAW_DISTRIBUTED_NETWORK_BEHAVIOR_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)

FALSE_INPUT_CHECKS = (
    ("self_continuation_created_before_review", "SELF_CONTINUATION_CREATED_BEFORE_REVIEW"),
    ("self_continuation_treated_as_self_recursive_growth", "SELF_CONTINUATION_TREATED_AS_SELF_RECURSIVE_GROWTH"),
    ("self_continuation_treated_as_runtime_daemon", "SELF_CONTINUATION_TREATED_AS_RUNTIME_DAEMON"),
    ("self_continuation_treated_as_runtime_loop", "SELF_CONTINUATION_TREATED_AS_RUNTIME_LOOP"),
    ("self_continuation_treated_as_public_api", "SELF_CONTINUATION_TREATED_AS_PUBLIC_API"),
    ("self_continuation_treated_as_participant_facing_interface", "SELF_CONTINUATION_TREATED_AS_PARTICIPANT_FACING_INTERFACE"),
    ("self_continuation_treated_as_distributed_network_behavior", "SELF_CONTINUATION_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR"),
    ("self_continuation_treated_as_source_transfer", "SELF_CONTINUATION_TREATED_AS_SOURCE_TRANSFER"),
    ("self_continuation_treated_as_source_receipt", "SELF_CONTINUATION_TREATED_AS_SOURCE_RECEIPT"),
    ("self_continuation_treated_as_reception_authorization", "SELF_CONTINUATION_TREATED_AS_RECEPTION_AUTHORIZATION"),
    ("self_continuation_treated_as_source", "SELF_CONTINUATION_TREATED_AS_SOURCE"),
    ("self_continuation_treated_as_authority", "SELF_CONTINUATION_TREATED_AS_AUTHORITY"),
    ("self_continuation_treated_as_currentness", "SELF_CONTINUATION_TREATED_AS_CURRENTNESS"),
    ("self_continuation_treated_as_deployment", "SELF_CONTINUATION_TREATED_AS_DEPLOYMENT"),
    ("self_continuation_treated_as_public_release", "SELF_CONTINUATION_TREATED_AS_PUBLIC_RELEASE"),
    ("self_continuation_treated_as_operation_permission", "SELF_CONTINUATION_TREATED_AS_OPERATION_PERMISSION"),
    ("self_continuation_treated_as_broader_reusable_permission", "SELF_CONTINUATION_TREATED_AS_BROADER_REUSABLE_PERMISSION"),
    ("self_continuation_treated_as_follow_on_work", "SELF_CONTINUATION_TREATED_AS_FOLLOW_ON_WORK"),
    (
        "self_continuation_boundary_treated_as_self_continuation_without_review",
        "SELF_CONTINUATION_BOUNDARY_TREATED_AS_SELF_CONTINUATION",
    ),
    (
        "continuation_treated_as_self_continuation_without_review",
        "BOUNDED_CONTINUATION_ENVELOPE_TREATED_AS_SELF_CONTINUATION_BEFORE_REVIEW",
    ),
    (
        "bounded_continuation_envelope_treated_as_self_continuation_without_review",
        "BOUNDED_CONTINUATION_ENVELOPE_TREATED_AS_SELF_CONTINUATION_BEFORE_REVIEW",
    ),
    (
        "bounded_continuation_envelope_authorized_arbitrary_runtime_activity_before_review",
        "BOUNDED_CONTINUATION_ENVELOPE_AUTHORIZED_ARBITRARY_RUNTIME_ACTIVITY_BEFORE_REVIEW",
    ),
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
    ("another_reception_request_authorized", "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"),
    ("adoption_created", "ADOPTION_CREATED"),
    ("receiving_context_governance_created", "RECEIVING_CONTEXT_GOVERNANCE_CREATED"),
    ("publication_flow_created", "PUBLICATION_FLOW_CREATED"),
    ("follow_on_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
    ("artifact_existence_treated_as_self_continuation_authority", "ARTIFACT_EXISTENCE_TREATED_AS_SELF_CONTINUATION_AUTHORITY"),
    ("artifact_path_treated_as_currentness", "ARTIFACT_PATH_TREATED_AS_CURRENTNESS"),
    ("latest_file_posture_treated_as_self_continuation_authority", "LATEST_FILE_POSTURE_TREATED_AS_SELF_CONTINUATION_AUTHORITY"),
    ("repo_local_availability_treated_as_self_continuation_authority", "REPO_LOCAL_AVAILABILITY_TREATED_AS_SELF_CONTINUATION_AUTHORITY"),
    ("hidden_repo_state_used_as_self_continuation_content", "HIDDEN_REPO_STATE_USED_AS_SELF_CONTINUATION_CONTENT"),
    ("hidden_repo_state_used_as_self_continuation_authority", "HIDDEN_REPO_STATE_USED_AS_SELF_CONTINUATION_AUTHORITY"),
    ("raw_full_prior_artifact_body_returned", "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED"),
    ("consumed_request_reopened", "CONSUMED_REQUEST_REOPENED"),
    ("authorization_token_reused", "AUTHORIZATION_TOKEN_REUSED"),
)

REDACTED_RAW_VALUE = "[bounded-redacted-raw-or-hidden-state]"
DEFAULT_REQUEST_ID = "post_continuation_self_continuation_reference_review_001"


def _now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _canonical_false_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _deepcopy_mapping(value: Mapping[str, Any]) -> dict[str, Any]:
    return deepcopy(dict(value))


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


def _flag_true(request: Mapping[str, Any], key: str) -> bool:
    return request.get(key) is True


def _safe_int(value: Any, default: int = 0) -> int:
    if isinstance(value, bool):
        return default
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            return default
    return default


def _scope_list(value: Any) -> list[str]:
    if value is None:
        return list(SUPPORTED_SCOPE_VALUES)
    if isinstance(value, str):
        return [value]
    if isinstance(value, Mapping):
        return [str(key) for key, enabled in value.items() if enabled is True]
    if isinstance(value, (list, tuple, set)):
        return [str(item) for item in value]
    return [str(value)]


def _contains_hostile_sentinel(value: str) -> bool:
    return any(sentinel in value for sentinel in HOSTILE_SENTINELS)


def _sanitize(value: Any, *, key: str | None = None) -> Any:
    key_text = key or ""
    key_lower = key_text.lower()
    if key_lower in SENSITIVE_CONTENT_KEYS or key_lower.endswith("_body"):
        return REDACTED_RAW_VALUE
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, str):
        if _contains_hostile_sentinel(value):
            return REDACTED_RAW_VALUE
        return value
    if isinstance(value, Mapping):
        return {
            str(item_key): _sanitize(item_value, key=str(item_key))
            for item_key, item_value in value.items()
        }
    if isinstance(value, list):
        return [_sanitize(item) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item) for item in value]
    if isinstance(value, set):
        return [_sanitize(item) for item in sorted(value, key=str)]
    return deepcopy(value)


def _check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str,
) -> None:
    record = {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": _sanitize(expected_posture),
        "actual_posture": _sanitize(actual_posture),
    }
    if passed:
        record["block_code"] = None
        record["failure_code"] = None
    else:
        record["block_code"] = code
        record["failure_code"] = code
    checks.append(record)


def _first_failed_code(checks: list[dict[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is not True:
            code = check.get("block_code") or check.get("failure_code")
            return str(code) if code else "DECLARED_SELF_CONTINUATION_REQUEST_MALFORMED"
    return None


def _basis_summary(request: Mapping[str, Any], field: str, *, basis_only: bool = True) -> dict[str, Any]:
    value = request.get(field, {})
    if isinstance(value, Mapping):
        summary = _sanitize(value)
    elif _is_declared(value):
        summary = {"declared": True, "value": _sanitize(value)}
    else:
        summary = {"declared": False}
    if isinstance(summary, dict):
        summary.setdefault("basis_only", basis_only)
        summary.setdefault(
            "selected_basis_reference_shape",
            bool(request.get("reference_shaped_input_posture", True)),
        )
    return summary


def _posture_section(request: Mapping[str, Any], field: str) -> dict[str, Any]:
    return {
        "declared": _is_declared(request.get(field)),
        "posture": _sanitize(request.get(field)),
        "basis_only": True,
    }


def _declared_posture(name: str) -> dict[str, Any]:
    return {"declared": True, "posture": name, "basis_only": True}


def _validate_base_request(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    question = request.get("self_continuation_question")
    _check(
        checks,
        "self-continuation question declared",
        question == CORE_QUESTION,
        CORE_QUESTION,
        question,
        "SELF_CONTINUATION_QUESTION_UNDECLARED",
    )

    intent = request.get("self_continuation_intent")
    _check(
        checks,
        "self-continuation intent supported",
        intent in SUPPORTED_INTENTS,
        list(SUPPORTED_INTENTS),
        intent,
        "SELF_CONTINUATION_INTENT_UNSUPPORTED",
    )
    _check(
        checks,
        "explicit block intent absent",
        intent != INTENT_BLOCK,
        f"not {INTENT_BLOCK}",
        intent,
        "SELF_CONTINUATION_EXPLICIT_BLOCK_REQUESTED",
    )

    scopes = _scope_list(request.get("self_continuation_scope"))
    unsupported = [scope for scope in scopes if scope not in SUPPORTED_SCOPE_VALUES]
    _check(
        checks,
        "self-continuation scope supported",
        not unsupported,
        list(SUPPORTED_SCOPE_VALUES),
        scopes,
        "UNSUPPORTED_SELF_CONTINUATION_SCOPE",
    )


def _validate_self_continuation_boundary_basis(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> None:
    _check(
        checks,
        "self-continuation-boundary basis declared",
        _is_declared(request.get("selected_self_continuation_boundary_basis")),
        "selected self-continuation-boundary basis",
        request.get("selected_self_continuation_boundary_basis"),
        "SELF_CONTINUATION_BOUNDARY_BASIS_MISSING",
    )
    _check(
        checks,
        "self-continuation-boundary terminal summary basis declared",
        _is_declared(
            request.get("selected_self_continuation_boundary_terminal_summary_basis")
        ),
        "selected self-continuation-boundary terminal summary basis",
        request.get("selected_self_continuation_boundary_terminal_summary_basis"),
        "SELF_CONTINUATION_BOUNDARY_TERMINAL_SUMMARY_BASIS_MISSING",
    )
    _check(
        checks,
        "self-continuation-boundary outcome recorded",
        request.get("selected_self_continuation_boundary_result_outcome")
        == EXPECTED_SELF_CONTINUATION_BOUNDARY_OUTCOME,
        EXPECTED_SELF_CONTINUATION_BOUNDARY_OUTCOME,
        request.get("selected_self_continuation_boundary_result_outcome"),
        "SELF_CONTINUATION_BOUNDARY_NOT_RECORDED",
    )
    _check(
        checks,
        "self-continuation-boundary version 0.1.0",
        request.get("selected_self_continuation_boundary_result_version") == "0.1.0",
        "0.1.0",
        request.get("selected_self_continuation_boundary_result_version"),
        "SELF_CONTINUATION_BOUNDARY_VERSION_NOT_0_1_0",
    )
    _check(
        checks,
        "self-continuation-boundary failed checks zero",
        _safe_int(request.get("selected_self_continuation_boundary_failed_check_count"))
        == 0,
        0,
        request.get("selected_self_continuation_boundary_failed_check_count"),
        "SELF_CONTINUATION_BOUNDARY_FAILED_CHECKS_PRESENT",
    )
    _check(
        checks,
        "self-continuation-boundary declared future self-continuation review",
        request.get("selected_self_continuation_boundary_declared_future_review")
        is True,
        True,
        request.get("selected_self_continuation_boundary_declared_future_review"),
        "SELF_CONTINUATION_BOUNDARY_DID_NOT_DECLARE_FUTURE_SELF_CONTINUATION_REVIEW",
    )

    false_checks = (
        (
            "selected_self_continuation_boundary_already_authorized_self_continuation",
            "SELF_CONTINUATION_BOUNDARY_ALREADY_AUTHORIZED_SELF_CONTINUATION",
        ),
        (
            "selected_self_continuation_boundary_already_created_self_recursive_growth",
            "SELF_CONTINUATION_BOUNDARY_ALREADY_CREATED_SELF_RECURSIVE_GROWTH",
        ),
        (
            "selected_self_continuation_boundary_already_created_runtime_daemon",
            "SELF_CONTINUATION_BOUNDARY_ALREADY_CREATED_RUNTIME_DAEMON",
        ),
        (
            "selected_self_continuation_boundary_already_created_runtime_loop",
            "SELF_CONTINUATION_BOUNDARY_ALREADY_CREATED_RUNTIME_LOOP",
        ),
        (
            "selected_self_continuation_boundary_already_created_public_api",
            "SELF_CONTINUATION_BOUNDARY_ALREADY_CREATED_PUBLIC_API",
        ),
        (
            "selected_self_continuation_boundary_already_created_participant_facing_interface",
            "SELF_CONTINUATION_BOUNDARY_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE",
        ),
        (
            "selected_self_continuation_boundary_already_created_distributed_network_behavior",
            "SELF_CONTINUATION_BOUNDARY_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR",
        ),
        (
            "selected_self_continuation_boundary_treated_as_self_continuation",
            "SELF_CONTINUATION_BOUNDARY_TREATED_AS_SELF_CONTINUATION",
        ),
        (
            "selected_self_continuation_boundary_treated_as_self_recursive_growth",
            "SELF_CONTINUATION_BOUNDARY_TREATED_AS_SELF_RECURSIVE_GROWTH",
        ),
        (
            "selected_self_continuation_boundary_authorized_future_work",
            "SELF_CONTINUATION_BOUNDARY_AUTHORIZED_FUTURE_WORK",
        ),
    )
    for field, code in false_checks:
        _check(checks, field.replace("_", " "), not _flag_true(request, field), False, request.get(field), code)

    _check(
        checks,
        "self-continuation-boundary canonicalized result-level non-claims",
        request.get("selected_self_continuation_boundary_non_claims_canonicalized")
        is True,
        True,
        request.get("selected_self_continuation_boundary_non_claims_canonicalized"),
        "SELF_CONTINUATION_BOUNDARY_DID_NOT_CANONICALIZE_NON_CLAIMS",
    )
    _check(
        checks,
        "self-continuation-boundary terminal summary preserves no self-continuation",
        request.get(
            "selected_self_continuation_boundary_terminal_summary_self_continuation_not_authorized"
        )
        is True
        and request.get(
            "selected_self_continuation_boundary_terminal_summary_no_self_continuation_selected"
        )
        is True,
        True,
        {
            "self_continuation_not_authorized": request.get(
                "selected_self_continuation_boundary_terminal_summary_self_continuation_not_authorized"
            ),
            "no_self_continuation_selected": request.get(
                "selected_self_continuation_boundary_terminal_summary_no_self_continuation_selected"
            ),
        },
        "SELF_CONTINUATION_BOUNDARY_TERMINAL_SUMMARY_DID_NOT_PRESERVE_NO_SELF_CONTINUATION",
    )
    _check(
        checks,
        "self-continuation-boundary terminal summary requires separate future review",
        request.get(
            "selected_self_continuation_boundary_terminal_summary_future_work_requires_separate_step_back_review"
        )
        is True,
        True,
        request.get(
            "selected_self_continuation_boundary_terminal_summary_future_work_requires_separate_step_back_review"
        ),
        "SELF_CONTINUATION_BOUNDARY_TERMINAL_SUMMARY_DID_NOT_REQUIRE_SEPARATE_REVIEW",
    )


def _validate_continuation_basis(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    _check(
        checks,
        "continuation basis declared",
        _is_declared(request.get("selected_continuation_basis")),
        "selected continuation basis",
        request.get("selected_continuation_basis"),
        "CONTINUATION_BASIS_MISSING",
    )
    _check(
        checks,
        "continuation terminal summary basis declared",
        _is_declared(request.get("selected_continuation_terminal_summary_basis")),
        "selected continuation terminal summary basis",
        request.get("selected_continuation_terminal_summary_basis"),
        "CONTINUATION_TERMINAL_SUMMARY_BASIS_MISSING",
    )
    _check(
        checks,
        "continuation outcome recorded",
        request.get("selected_continuation_result_outcome") == EXPECTED_CONTINUATION_OUTCOME,
        EXPECTED_CONTINUATION_OUTCOME,
        request.get("selected_continuation_result_outcome"),
        "CONTINUATION_NOT_RECORDED",
    )
    _check(
        checks,
        "continuation version 0.1.0",
        request.get("selected_continuation_result_version") == "0.1.0",
        "0.1.0",
        request.get("selected_continuation_result_version"),
        "CONTINUATION_VERSION_NOT_0_1_0",
    )
    _check(
        checks,
        "continuation failed checks zero",
        _safe_int(request.get("selected_continuation_failed_check_count")) == 0,
        0,
        request.get("selected_continuation_failed_check_count"),
        "CONTINUATION_FAILED_CHECKS_PRESENT",
    )
    _check(
        checks,
        "continuation recorded bounded continuation posture",
        request.get("selected_continuation_bounded_posture_recorded") is True,
        True,
        request.get("selected_continuation_bounded_posture_recorded"),
        "CONTINUATION_DID_NOT_RECORD_BOUNDED_CONTINUATION_POSTURE",
    )
    _check(
        checks,
        "continuation recorded bounded continuation envelope",
        request.get("selected_continuation_bounded_continuation_envelope_recorded")
        is True,
        True,
        request.get("selected_continuation_bounded_continuation_envelope_recorded"),
        "CONTINUATION_DID_NOT_RECORD_BOUNDED_CONTINUATION_ENVELOPE",
    )

    continuation_false_checks = (
        (
            "selected_continuation_already_created_self_recursive_growth",
            "CONTINUATION_ALREADY_CREATED_SELF_RECURSIVE_GROWTH",
        ),
        (
            "selected_continuation_already_created_runtime_daemon",
            "CONTINUATION_ALREADY_CREATED_RUNTIME_DAEMON",
        ),
        (
            "selected_continuation_already_created_runtime_loop",
            "CONTINUATION_ALREADY_CREATED_RUNTIME_LOOP",
        ),
        (
            "selected_continuation_already_created_public_api",
            "CONTINUATION_ALREADY_CREATED_PUBLIC_API",
        ),
        (
            "selected_continuation_already_created_participant_facing_interface",
            "CONTINUATION_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE",
        ),
        (
            "selected_continuation_already_created_distributed_network_behavior",
            "CONTINUATION_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR",
        ),
        (
            "selected_bounded_continuation_envelope_treated_as_self_continuation_before_review",
            "BOUNDED_CONTINUATION_ENVELOPE_TREATED_AS_SELF_CONTINUATION_BEFORE_REVIEW",
        ),
        (
            "selected_bounded_continuation_envelope_authorized_arbitrary_runtime_activity_before_review",
            "BOUNDED_CONTINUATION_ENVELOPE_AUTHORIZED_ARBITRARY_RUNTIME_ACTIVITY_BEFORE_REVIEW",
        ),
    )
    for field, code in continuation_false_checks:
        _check(checks, field.replace("_", " "), not _flag_true(request, field), False, request.get(field), code)


def _validate_upstream_basis(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    *,
    basis_field: str,
    label: str,
    outcome_field: str,
    expected_outcome: str,
    version_field: str,
    expected_version: str,
    failed_count_field: str,
    missing_code: str,
    outcome_code: str,
    version_code: str,
    failed_code: str,
) -> None:
    _check(
        checks,
        f"{label} basis declared",
        _is_declared(request.get(basis_field)),
        f"selected {label} basis",
        request.get(basis_field),
        missing_code,
    )
    _check(
        checks,
        f"{label} outcome recorded",
        request.get(outcome_field) == expected_outcome,
        expected_outcome,
        request.get(outcome_field),
        outcome_code,
    )
    _check(
        checks,
        f"{label} version {expected_version}",
        request.get(version_field) == expected_version,
        expected_version,
        request.get(version_field),
        version_code,
    )
    _check(
        checks,
        f"{label} failed checks zero",
        _safe_int(request.get(failed_count_field)) == 0,
        0,
        request.get(failed_count_field),
        failed_code,
    )


def _validate_all_upstream_basis(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    _validate_upstream_basis(
        request,
        checks,
        basis_field="selected_continuation_boundary_basis",
        label="continuation-boundary",
        outcome_field="selected_continuation_boundary_result_outcome",
        expected_outcome=EXPECTED_CONTINUATION_BOUNDARY_OUTCOME,
        version_field="selected_continuation_boundary_result_version",
        expected_version="0.1.0",
        failed_count_field="selected_continuation_boundary_failed_check_count",
        missing_code="CONTINUATION_BOUNDARY_BASIS_MISSING",
        outcome_code="CONTINUATION_BOUNDARY_NOT_RECORDED",
        version_code="CONTINUATION_BOUNDARY_VERSION_NOT_0_1_0",
        failed_code="CONTINUATION_BOUNDARY_FAILED_CHECKS_PRESENT",
    )
    _validate_upstream_basis(
        request,
        checks,
        basis_field="selected_reusable_runtime_permission_basis",
        label="reusable-runtime-permission",
        outcome_field="selected_reusable_runtime_permission_result_outcome",
        expected_outcome=EXPECTED_REUSABLE_RUNTIME_PERMISSION_OUTCOME,
        version_field="selected_reusable_runtime_permission_result_version",
        expected_version="0.1.0",
        failed_count_field="selected_reusable_runtime_permission_failed_check_count",
        missing_code="REUSABLE_RUNTIME_PERMISSION_BASIS_MISSING",
        outcome_code="REUSABLE_RUNTIME_PERMISSION_NOT_RECORDED",
        version_code="REUSABLE_RUNTIME_PERMISSION_VERSION_NOT_0_1_0",
        failed_code="REUSABLE_RUNTIME_PERMISSION_FAILED_CHECKS_PRESENT",
    )
    _validate_upstream_basis(
        request,
        checks,
        basis_field="selected_reusable_runtime_permission_boundary_basis",
        label="reusable-runtime-permission-boundary",
        outcome_field="selected_reusable_runtime_permission_boundary_result_outcome",
        expected_outcome=EXPECTED_REUSABLE_RUNTIME_PERMISSION_BOUNDARY_OUTCOME,
        version_field="selected_reusable_runtime_permission_boundary_result_version",
        expected_version="0.1.0",
        failed_count_field="selected_reusable_runtime_permission_boundary_failed_check_count",
        missing_code="REUSABLE_RUNTIME_PERMISSION_BOUNDARY_BASIS_MISSING",
        outcome_code="REUSABLE_RUNTIME_PERMISSION_BOUNDARY_NOT_RECORDED",
        version_code="REUSABLE_RUNTIME_PERMISSION_BOUNDARY_VERSION_NOT_0_1_0",
        failed_code="REUSABLE_RUNTIME_PERMISSION_BOUNDARY_FAILED_CHECKS_PRESENT",
    )
    _validate_upstream_basis(
        request,
        checks,
        basis_field="selected_ongoing_runtime_basis",
        label="ongoing-runtime",
        outcome_field="selected_ongoing_runtime_result_outcome",
        expected_outcome=EXPECTED_ONGOING_RUNTIME_OUTCOME,
        version_field="selected_ongoing_runtime_result_version",
        expected_version="0.1.0",
        failed_count_field="selected_ongoing_runtime_failed_check_count",
        missing_code="ONGOING_RUNTIME_BASIS_MISSING",
        outcome_code="ONGOING_RUNTIME_NOT_RECORDED",
        version_code="ONGOING_RUNTIME_VERSION_NOT_0_1_0",
        failed_code="ONGOING_RUNTIME_FAILED_CHECKS_PRESENT",
    )
    _validate_upstream_basis(
        request,
        checks,
        basis_field="selected_runtime_hosting_basis",
        label="runtime-hosting",
        outcome_field="selected_runtime_hosting_result_outcome",
        expected_outcome=EXPECTED_RUNTIME_HOSTING_OUTCOME,
        version_field="selected_runtime_hosting_result_version",
        expected_version="0.1.0",
        failed_count_field="selected_runtime_hosting_failed_check_count",
        missing_code="RUNTIME_HOSTING_BASIS_MISSING",
        outcome_code="RUNTIME_HOSTING_NOT_RECORDED",
        version_code="RUNTIME_HOSTING_VERSION_NOT_0_1_0",
        failed_code="RUNTIME_HOSTING_FAILED_CHECKS_PRESENT",
    )
    _validate_upstream_basis(
        request,
        checks,
        basis_field="selected_runtime_hosting_boundary_v2_basis",
        label="runtime-hosting-boundary v2",
        outcome_field="selected_runtime_hosting_boundary_v2_result_outcome",
        expected_outcome=EXPECTED_RUNTIME_HOSTING_BOUNDARY_V2_OUTCOME,
        version_field="selected_runtime_hosting_boundary_v2_result_version",
        expected_version="0.2.0",
        failed_count_field="selected_runtime_hosting_boundary_v2_failed_check_count",
        missing_code="RUNTIME_HOSTING_BOUNDARY_V2_BASIS_MISSING",
        outcome_code="RUNTIME_HOSTING_BOUNDARY_V2_NOT_RECORDED",
        version_code="RUNTIME_HOSTING_BOUNDARY_V2_VERSION_NOT_0_2_0",
        failed_code="RUNTIME_HOSTING_BOUNDARY_V2_FAILED_CHECKS_PRESENT",
    )
    _validate_upstream_basis(
        request,
        checks,
        basis_field="selected_successor_runtime_step_basis",
        label="successor-runtime-step",
        outcome_field="selected_successor_runtime_step_result_outcome",
        expected_outcome=EXPECTED_SUCCESSOR_RUNTIME_STEP_OUTCOME,
        version_field="selected_successor_runtime_step_result_version",
        expected_version="0.1.0",
        failed_count_field="selected_successor_runtime_step_failed_check_count",
        missing_code="SUCCESSOR_RUNTIME_STEP_BASIS_MISSING",
        outcome_code="SUCCESSOR_RUNTIME_STEP_NOT_RECORDED",
        version_code="SUCCESSOR_RUNTIME_STEP_VERSION_NOT_0_1_0",
        failed_code="SUCCESSOR_RUNTIME_STEP_FAILED_CHECKS_PRESENT",
    )
    _validate_upstream_basis(
        request,
        checks,
        basis_field="selected_minimal_runtime_basis",
        label="minimal-runtime",
        outcome_field="selected_minimal_runtime_result_outcome",
        expected_outcome=EXPECTED_MINIMAL_RUNTIME_OUTCOME,
        version_field="selected_minimal_runtime_result_version",
        expected_version="0.1.0",
        failed_count_field="selected_minimal_runtime_failed_check_count",
        missing_code="MINIMAL_RUNTIME_BASIS_MISSING",
        outcome_code="MINIMAL_RUNTIME_NOT_RECORDED",
        version_code="MINIMAL_RUNTIME_VERSION_NOT_0_1_0",
        failed_code="MINIMAL_RUNTIME_FAILED_CHECKS_PRESENT",
    )
    _validate_upstream_basis(
        request,
        checks,
        basis_field="selected_runtime_boundary_basis",
        label="runtime-boundary",
        outcome_field="selected_runtime_boundary_result_outcome",
        expected_outcome=EXPECTED_RUNTIME_BOUNDARY_OUTCOME,
        version_field="selected_runtime_boundary_result_version",
        expected_version="0.1.0",
        failed_count_field="selected_runtime_boundary_failed_check_count",
        missing_code="RUNTIME_BOUNDARY_BASIS_MISSING",
        outcome_code="RUNTIME_BOUNDARY_NOT_RECORDED",
        version_code="RUNTIME_BOUNDARY_VERSION_NOT_0_1_0",
        failed_code="RUNTIME_BOUNDARY_FAILED_CHECKS_PRESENT",
    )
    _validate_upstream_basis(
        request,
        checks,
        basis_field="selected_runtime_readiness_basis",
        label="runtime-readiness",
        outcome_field="selected_runtime_readiness_result_outcome",
        expected_outcome=EXPECTED_RUNTIME_READINESS_OUTCOME,
        version_field="selected_runtime_readiness_result_version",
        expected_version="0.1.0",
        failed_count_field="selected_runtime_readiness_failed_check_count",
        missing_code="RUNTIME_READINESS_BASIS_MISSING",
        outcome_code="RUNTIME_READINESS_NOT_RECORDED",
        version_code="RUNTIME_READINESS_VERSION_NOT_0_1_0",
        failed_code="RUNTIME_READINESS_FAILED_CHECKS_PRESENT",
    )
    _validate_upstream_basis(
        request,
        checks,
        basis_field="selected_portable_verification_final_completion_basis",
        label="portable verification final-completion",
        outcome_field="selected_portable_verification_final_completion_result_outcome",
        expected_outcome=EXPECTED_FINAL_COMPLETION_OUTCOME,
        version_field="selected_portable_verification_final_completion_result_version",
        expected_version="0.1.0",
        failed_count_field="selected_portable_verification_final_completion_failed_check_count",
        missing_code="PORTABLE_VERIFICATION_FINAL_COMPLETION_BASIS_MISSING",
        outcome_code="PORTABLE_VERIFICATION_FINAL_COMPLETION_NOT_RECORDED",
        version_code="PORTABLE_VERIFICATION_FINAL_COMPLETION_VERSION_NOT_0_1_0",
        failed_code="PORTABLE_VERIFICATION_FINAL_COMPLETION_FAILED_CHECKS_PRESENT",
    )


def _validate_lineage_and_currentness(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    _check(
        checks,
        "runtime-hosting-boundary v1 failure lineage declared",
        _is_declared(request.get("selected_runtime_hosting_boundary_v1_failure_lineage_basis")),
        "selected runtime-hosting-boundary v1 failure lineage",
        request.get("selected_runtime_hosting_boundary_v1_failure_lineage_basis"),
        "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_LINEAGE_MISSING",
    )
    v1_failure_visible = not (
        _flag_true(request, "selected_runtime_hosting_boundary_v1_failure_repaired")
        or _flag_true(request, "selected_runtime_hosting_boundary_v1_failure_hidden")
        or _flag_true(request, "selected_runtime_hosting_boundary_v1_failure_claimed_passed")
    )
    _check(
        checks,
        "runtime-hosting-boundary v1 failure lineage preserved and not repaired hidden claimed passed",
        v1_failure_visible,
        "failure visible and unrepaired",
        {
            "repaired": request.get("selected_runtime_hosting_boundary_v1_failure_repaired"),
            "hidden": request.get("selected_runtime_hosting_boundary_v1_failure_hidden"),
            "claimed_passed": request.get("selected_runtime_hosting_boundary_v1_failure_claimed_passed"),
        },
        "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
    )
    _check(
        checks,
        "post-portable currentness surface basis declared",
        _is_declared(request.get("selected_post_portable_verification_currentness_basis")),
        "selected post-portable currentness surface basis",
        request.get("selected_post_portable_verification_currentness_basis"),
        "POST_PORTABLE_CURRENTNESS_SURFACE_BASIS_MISSING",
    )
    _check(
        checks,
        "post-portable currentness surface states checkability not continuation",
        request.get("selected_post_portable_currentness_surface_states_checkability_not_continuation")
        is True,
        True,
        request.get("selected_post_portable_currentness_surface_states_checkability_not_continuation"),
        "POST_PORTABLE_CURRENTNESS_SURFACE_TREATED_CHECKABILITY_AS_CONTINUATION",
    )
    _check(
        checks,
        "post-portable currentness surface does not authorize next work",
        not _flag_true(request, "selected_post_portable_currentness_surface_authorized_next_work"),
        False,
        request.get("selected_post_portable_currentness_surface_authorized_next_work"),
        "POST_PORTABLE_CURRENTNESS_SURFACE_AUTHORIZED_NEXT_WORK",
    )
    _check(
        checks,
        "returned second-carrier capture lineage basis declared",
        _is_declared(request.get("selected_returned_second_carrier_capture_lineage_basis")),
        "selected returned second-carrier capture lineage basis",
        request.get("selected_returned_second_carrier_capture_lineage_basis"),
        "RETURNED_SECOND_CARRIER_CAPTURE_LINEAGE_BASIS_MISSING",
    )


def _validate_postures(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    for field in POSTURE_FIELDS:
        _check(
            checks,
            f"{field} declared",
            _is_declared(request.get(field)),
            f"declared {field}",
            request.get(field),
            "SELF_CONTINUATION_REQUIRED_POSTURE_MISSING",
        )


def _validate_bounded_self_continuation_envelope(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> None:
    envelope = request.get("requested_bounded_self_continuation_envelope")
    _check(
        checks,
        "bounded self-continuation envelope declared",
        _is_declared(envelope),
        "declared narrow bounded self-continuation envelope",
        envelope,
        "BOUNDED_SELF_CONTINUATION_ENVELOPE_UNDECLARED",
    )
    overbroad = False
    if isinstance(envelope, Mapping):
        overbroad_keys = (
            "authorizes_arbitrary_runtime_activity",
            "authorizes_self_recursive_growth",
            "authorizes_follow_on_work",
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
        )
        overbroad = any(envelope.get(key) is True for key in overbroad_keys)
    _check(
        checks,
        "bounded self-continuation envelope narrow",
        not overbroad,
        "no arbitrary runtime activity, no self-recursive growth, no follow-on work",
        envelope,
        "BOUNDED_SELF_CONTINUATION_ENVELOPE_OVERBROAD",
    )


def _validate_false_inputs(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    for field, code in FALSE_INPUT_CHECKS:
        _check(checks, field.replace("_", " "), not _flag_true(request, field), False, request.get(field), code)

    _check(
        checks,
        "selected basis reference-shaped",
        request.get("reference_shaped_input_posture", True) is True,
        True,
        request.get("reference_shaped_input_posture"),
        "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    )
    _check(
        checks,
        "predecessor failure evidence visible and unrepaired",
        not (
            _flag_true(request, "predecessor_failure_repaired")
            or _flag_true(request, "predecessor_failure_hidden")
            or _flag_true(request, "predecessor_failure_claimed_passed")
        ),
        "not repaired hidden or claimed passed",
        {
            "repaired": request.get("predecessor_failure_repaired"),
            "hidden": request.get("predecessor_failure_hidden"),
            "claimed_passed": request.get("predecessor_failure_claimed_passed"),
        },
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    )
    _check(
        checks,
        "official enum scope strings not redacted",
        all(scope in SUPPORTED_SCOPE_VALUES for scope in SUPPORTED_SCOPE_VALUES),
        "official scope strings preserved",
        list(SUPPORTED_SCOPE_VALUES),
        "OFFICIAL_ENUM_SCOPE_STRINGS_REDACTED",
    )
    _check(
        checks,
        "hostile raw body content contained",
        not _flag_true(request, "hostile_raw_body_content_returned"),
        False,
        request.get("hostile_raw_body_content_returned"),
        "HOSTILE_RAW_BODY_CONTENT_NOT_CONTAINED",
    )


def _validate_declared_non_claims(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    declared = request.get("declared_non_claims")
    if not isinstance(declared, Mapping):
        _check(
            checks,
            "declared non-claims mapping present",
            False,
            "mapping with all required false non-claims",
            declared,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
        return

    for key in REQUIRED_FALSE_NON_CLAIMS:
        _check(
            checks,
            f"required non-claim {key} false",
            declared.get(key) is False,
            False,
            declared.get(key),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )


def _run_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    _validate_base_request(request, checks)
    _validate_self_continuation_boundary_basis(request, checks)
    _validate_continuation_basis(request, checks)
    _validate_all_upstream_basis(request, checks)
    _validate_lineage_and_currentness(request, checks)
    _validate_postures(request, checks)
    _validate_bounded_self_continuation_envelope(request, checks)
    _validate_false_inputs(request, checks)
    _validate_declared_non_claims(request, checks)
    return checks


def _determine_outcome(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> str:
    if any(check.get("passed") is not True for check in checks):
        return OUTCOME_BLOCKED
    requested = request.get("requested_self_continuation_outcome")
    if requested == OUTCOME_NOT_RECORDED or request.get("self_continuation_intent") == INTENT_DO_NOT_RECORD:
        return OUTCOME_NOT_RECORDED
    if requested == OUTCOME_REQUIRES_ADDITIONAL_BASIS or _is_declared(request.get("additional_basis_context")):
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS
    return OUTCOME_RECORDED


def _statement_for_outcome(outcome: str) -> dict[str, bool]:
    recorded = outcome == OUTCOME_RECORDED
    statement = {field: True for field in ALLOWED_TRUE_RECORDED_FIELDS}
    statement["self_continuation_recorded"] = recorded
    statement["bounded_self_continuation_posture_recorded"] = recorded
    statement["bounded_self_continuation_envelope_declared"] = recorded
    return statement


def _bounded_self_continuation_envelope(
    outcome: str, request: Mapping[str, Any]
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    requested = request.get("requested_bounded_self_continuation_envelope")
    return {
        "recorded": recorded,
        "declared": recorded,
        "envelope_name": "one_bounded_post_continuation_self_continuation_envelope",
        "self_continuation_posture": (
            "one bounded self-continuation posture from selected standing "
            "self-continuation-boundary and continuation basis"
        ),
        "requested_envelope": _sanitize(requested),
        "anything_outside_requires_fresh_admission": True,
        "authorizes_arbitrary_runtime_activity": False,
        "authorizes_self_recursive_growth": False,
        "authorizes_follow_on_work": False,
        "creates_daemon_loop_api_interface_or_distributed_network": False,
        "creates_source_authority_currentness_deployment_public_release_or_operation_permission": False,
        "creates_source_transfer_source_receipt_or_reception_authorization": False,
    }


def _non_meaning() -> dict[str, bool]:
    return {
        "creates_self_recursive_growth": False,
        "creates_runtime_daemon": False,
        "creates_runtime_loop": False,
        "creates_public_api": False,
        "creates_participant_facing_interface": False,
        "creates_distributed_network_behavior": False,
        "performs_source_transfer": False,
        "performs_source_receipt": False,
        "creates_reception_authorization": False,
        "creates_source": False,
        "creates_authority": False,
        "creates_currentness": False,
        "creates_deployment": False,
        "creates_public_release": False,
        "creates_operation_permission": False,
        "creates_broader_reusable_permission": False,
        "authorizes_derivative_reception": False,
        "authorizes_vessel_relation": False,
        "authorizes_another_reception_request": False,
        "creates_adoption": False,
        "creates_receiving_context_governance": False,
        "creates_publication_flow": False,
        "authorizes_follow_on_work": False,
        "authorizes_arbitrary_runtime_activity": False,
        "treats_self_continuation_as_self_recursive_growth": False,
        "treats_artifact_existence_as_authority": False,
        "treats_repo_local_availability_as_authority": False,
        "treats_latest_file_posture_as_authority": False,
    }


def _additional_basis_required(outcome: str, request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "required": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "basis": _sanitize(request.get("additional_basis_context")),
        "does_not_create_self_recursive_growth": True,
        "does_not_authorize_follow_on_work": True,
    }


def _not_recorded_basis(outcome: str, request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "not_recorded": outcome == OUTCOME_NOT_RECORDED,
        "basis": _sanitize(request.get("not_recorded_basis")),
        "does_not_mutate_prior_artifacts": True,
        "does_not_authorize_next_work": True,
    }


def _what_remains_open() -> list[str]:
    return [
        "self-continuation test",
        "self-continuation live artifact",
        "self-continuation terminal summary, if separately selected",
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
    ]


def _block_for_outcome(outcome: str, checks: list[dict[str, Any]], request: Mapping[str, Any]) -> dict[str, Any] | None:
    if outcome != OUTCOME_BLOCKED:
        return None
    code = _first_failed_code(checks) or "DECLARED_SELF_CONTINUATION_REQUEST_MALFORMED"
    return {
        "blocked": True,
        "block_code": code,
        "block_reason": _sanitize(request.get("block_reason")) or code,
        "does_not_create_self_recursive_growth": True,
        "does_not_reopen_consumed_request": True,
        "does_not_reuse_authorization_token": True,
    }


def _build_metadata(request: Mapping[str, Any]) -> dict[str, Any]:
    request_id = str(request.get("self_continuation_request_id") or DEFAULT_REQUEST_ID)
    return {
        "post_continuation_self_continuation_id": request_id,
        "post_continuation_self_continuation_type": "post_continuation_self_continuation",
        "post_continuation_self_continuation_version": RESULT_VERSION,
        "generated_at": _now_iso(),
        "resolver_module": RESOLVER_MODULE,
    }


def _build_result(request: Mapping[str, Any], checks: list[dict[str, Any]], outcome: str) -> dict[str, Any]:
    metadata = _build_metadata(request)
    statement = _statement_for_outcome(outcome)
    result: dict[str, Any] = {
        "post_continuation_self_continuation_metadata": metadata,
        "declared_self_continuation_question": {
            "self_continuation_request_id": metadata["post_continuation_self_continuation_id"],
            "question": request.get("self_continuation_question"),
            "intent": request.get("self_continuation_intent"),
            "bounded_question_only": True,
        },
    }

    for field in SELECTED_BASIS_FIELDS:
        result[field] = _basis_summary(request, field)
    for posture_field in POSTURE_FIELDS:
        result[posture_field] = _posture_section(request, posture_field)

    result.update(
        {
            "self_continuation_scope": _scope_list(request.get("self_continuation_scope")),
            "self_continuation_checks": checks,
            "self_continuation_statement": statement,
            "self_continuation_non_meaning": _non_meaning(),
            "bounded_self_continuation_envelope": _bounded_self_continuation_envelope(
                outcome, request
            ),
            "additional_basis_required": _additional_basis_required(outcome, request),
            "not_recorded_basis": _not_recorded_basis(outcome, request),
            "what_remains_open": _what_remains_open(),
            "non_claims": _canonical_false_non_claims(),
            "outcome": outcome,
            "block": _block_for_outcome(outcome, checks, request),
        }
    )
    result["post_continuation_self_continuation_summary"] = (
        build_post_continuation_self_continuation_summary(result)
    )
    return result


def _malformed_result(code: str, reason: str, *, request_id: str = DEFAULT_REQUEST_ID) -> dict[str, Any]:
    request = build_declared_post_continuation_self_continuation_request(
        self_continuation_request_id=request_id
    )
    request["block_reason"] = reason
    checks = [
        {
            "check_name": "declared self-continuation request readable and mapping-shaped",
            "passed": False,
            "expected_posture": "readable mapping request",
            "actual_posture": reason,
            "block_code": code,
            "failure_code": code,
        }
    ]
    return _build_result(request, checks, OUTCOME_BLOCKED)


def resolve_post_continuation_self_continuation(
    declared_self_continuation_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve a declared self-continuation request."""

    if declared_self_continuation_request is None:
        return _malformed_result(
            "DECLARED_SELF_CONTINUATION_REQUEST_MALFORMED",
            "Declared self-continuation request is missing.",
        )
    if not isinstance(declared_self_continuation_request, Mapping):
        return _malformed_result(
            "DECLARED_SELF_CONTINUATION_REQUEST_MALFORMED",
            "Declared self-continuation request is not a mapping.",
        )

    request = _deepcopy_mapping(declared_self_continuation_request)
    checks = _run_checks(request)
    outcome = _determine_outcome(request, checks)
    return _build_result(request, checks, outcome)


def resolve_post_continuation_self_continuation_from_path(
    declared_self_continuation_request_path: Path | str,
) -> dict[str, Any]:
    """Read and resolve a declared self-continuation request JSON file."""

    path = Path(declared_self_continuation_request_path)
    try:
        loaded = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        return _malformed_result(
            "DECLARED_SELF_CONTINUATION_REQUEST_UNREADABLE",
            f"Declared self-continuation request could not be read: {exc}",
        )
    except json.JSONDecodeError as exc:
        return _malformed_result(
            "DECLARED_SELF_CONTINUATION_REQUEST_MALFORMED",
            f"Declared self-continuation request JSON is malformed: {exc}",
        )
    if not isinstance(loaded, Mapping):
        return _malformed_result(
            "DECLARED_SELF_CONTINUATION_REQUEST_MALFORMED",
            "Declared self-continuation request JSON is not an object.",
        )
    return resolve_post_continuation_self_continuation(loaded)


def build_post_continuation_self_continuation_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact summary for a self-continuation result."""

    metadata = result.get("post_continuation_self_continuation_metadata", {})
    if not isinstance(metadata, Mapping):
        metadata = {}
    declared_question = result.get("declared_self_continuation_question", {})
    if not isinstance(declared_question, Mapping):
        declared_question = {}
    statement = result.get("self_continuation_statement", {})
    if not isinstance(statement, Mapping):
        statement = {}
    block = result.get("block")
    if not isinstance(block, Mapping):
        block = {}
    checks = result.get("self_continuation_checks", [])
    if not isinstance(checks, list):
        checks = []

    passed_count = sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed") is True)
    failed_count = sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed") is not True)

    summary: dict[str, Any] = {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "request_id": declared_question.get("self_continuation_request_id")
        or metadata.get("post_continuation_self_continuation_id"),
        "question": declared_question.get("question"),
        "intent": declared_question.get("intent"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": metadata.get("post_continuation_self_continuation_version"),
        "resolver_module": metadata.get("resolver_module"),
        "bounded_self_continuation_envelope_posture": result.get(
            "bounded_self_continuation_envelope"
        ),
        "key_non_claims": _canonical_false_non_claims(),
        "no_self_recursive_growth_daemon_loop_api_interface_distributed_network_source_authority_currentness_deployment_public_release_follow_on": True,
    }

    for field in ALLOWED_TRUE_RECORDED_FIELDS:
        summary[field] = bool(statement.get(field))

    summary.update(
        {
            "selected_self_continuation_boundary_outcome": _basis_value(
                result, "selected_self_continuation_boundary_basis", "outcome"
            ),
            "selected_self_continuation_boundary_version": _basis_value(
                result, "selected_self_continuation_boundary_basis", "result_version"
            ),
            "selected_self_continuation_boundary_failed_check_count": _basis_value(
                result, "selected_self_continuation_boundary_basis", "failed_check_count"
            ),
            "selected_continuation_outcome": _basis_value(
                result, "selected_continuation_basis", "outcome"
            ),
            "selected_continuation_version": _basis_value(
                result, "selected_continuation_basis", "result_version"
            ),
            "selected_continuation_failed_check_count": _basis_value(
                result, "selected_continuation_basis", "failed_check_count"
            ),
            "selected_continuation_boundary_outcome": _basis_value(
                result, "selected_continuation_boundary_basis", "outcome"
            ),
            "selected_continuation_boundary_version": _basis_value(
                result, "selected_continuation_boundary_basis", "result_version"
            ),
            "selected_continuation_boundary_failed_check_count": _basis_value(
                result, "selected_continuation_boundary_basis", "failed_check_count"
            ),
            "selected_reusable_runtime_permission_outcome": _basis_value(
                result, "selected_reusable_runtime_permission_basis", "outcome"
            ),
            "selected_reusable_runtime_permission_version": _basis_value(
                result, "selected_reusable_runtime_permission_basis", "result_version"
            ),
            "selected_reusable_runtime_permission_failed_check_count": _basis_value(
                result, "selected_reusable_runtime_permission_basis", "failed_check_count"
            ),
            "selected_reusable_runtime_permission_boundary_outcome": _basis_value(
                result, "selected_reusable_runtime_permission_boundary_basis", "outcome"
            ),
            "selected_reusable_runtime_permission_boundary_version": _basis_value(
                result,
                "selected_reusable_runtime_permission_boundary_basis",
                "result_version",
            ),
            "selected_reusable_runtime_permission_boundary_failed_check_count": _basis_value(
                result,
                "selected_reusable_runtime_permission_boundary_basis",
                "failed_check_count",
            ),
            "selected_ongoing_runtime_outcome": _basis_value(
                result, "selected_ongoing_runtime_basis", "outcome"
            ),
            "selected_ongoing_runtime_version": _basis_value(
                result, "selected_ongoing_runtime_basis", "result_version"
            ),
            "selected_ongoing_runtime_failed_check_count": _basis_value(
                result, "selected_ongoing_runtime_basis", "failed_check_count"
            ),
            "selected_runtime_hosting_outcome": _basis_value(
                result, "selected_runtime_hosting_basis", "outcome"
            ),
            "selected_runtime_hosting_version": _basis_value(
                result, "selected_runtime_hosting_basis", "result_version"
            ),
            "selected_runtime_hosting_failed_check_count": _basis_value(
                result, "selected_runtime_hosting_basis", "failed_check_count"
            ),
            "selected_runtime_hosting_boundary_v2_outcome": _basis_value(
                result, "selected_runtime_hosting_boundary_v2_basis", "outcome"
            ),
            "selected_runtime_hosting_boundary_v2_version": _basis_value(
                result, "selected_runtime_hosting_boundary_v2_basis", "result_version"
            ),
            "selected_runtime_hosting_boundary_v2_failed_check_count": _basis_value(
                result, "selected_runtime_hosting_boundary_v2_basis", "failed_check_count"
            ),
            "selected_successor_runtime_step_outcome": _basis_value(
                result, "selected_successor_runtime_step_basis", "outcome"
            ),
            "selected_successor_runtime_step_version": _basis_value(
                result, "selected_successor_runtime_step_basis", "result_version"
            ),
            "selected_successor_runtime_step_failed_check_count": _basis_value(
                result, "selected_successor_runtime_step_basis", "failed_check_count"
            ),
            "selected_minimal_runtime_outcome": _basis_value(
                result, "selected_minimal_runtime_basis", "outcome"
            ),
            "selected_minimal_runtime_version": _basis_value(
                result, "selected_minimal_runtime_basis", "result_version"
            ),
            "selected_minimal_runtime_failed_check_count": _basis_value(
                result, "selected_minimal_runtime_basis", "failed_check_count"
            ),
            "selected_runtime_boundary_outcome": _basis_value(
                result, "selected_runtime_boundary_basis", "outcome"
            ),
            "selected_runtime_boundary_version": _basis_value(
                result, "selected_runtime_boundary_basis", "result_version"
            ),
            "selected_runtime_boundary_failed_check_count": _basis_value(
                result, "selected_runtime_boundary_basis", "failed_check_count"
            ),
            "selected_runtime_readiness_outcome": _basis_value(
                result, "selected_runtime_readiness_basis", "outcome"
            ),
            "selected_runtime_readiness_version": _basis_value(
                result, "selected_runtime_readiness_basis", "result_version"
            ),
            "selected_runtime_readiness_failed_check_count": _basis_value(
                result, "selected_runtime_readiness_basis", "failed_check_count"
            ),
            "selected_final_completion_outcome": _basis_value(
                result, "selected_portable_verification_final_completion_basis", "outcome"
            ),
            "selected_final_completion_version": _basis_value(
                result,
                "selected_portable_verification_final_completion_basis",
                "result_version",
            ),
            "selected_final_completion_failed_check_count": _basis_value(
                result,
                "selected_portable_verification_final_completion_basis",
                "failed_check_count",
            ),
            "selected_post_portable_currentness_surface_path": _basis_value(
                result, "selected_post_portable_verification_currentness_basis", "path"
            ),
            "predecessor_failure_evidence_preserved": bool(
                statement.get("predecessor_failure_evidence_preserved")
            ),
            "consumed_request_token_remains_closed": bool(
                statement.get("consumed_request_token_remains_closed")
            ),
            "authorization_token_reuse_blocked": bool(
                statement.get("authorization_token_reuse_blocked")
            ),
        }
    )
    return summary


def _basis_value(result: Mapping[str, Any], section: str, key: str) -> Any:
    value = result.get(section)
    if isinstance(value, Mapping):
        return value.get(key)
    return None


def write_post_continuation_self_continuation_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a self-continuation result JSON file without overwriting."""

    if not isinstance(result, Mapping):
        raise PostContinuationSelfContinuationError("Result must be a mapping.")
    metadata = result.get("post_continuation_self_continuation_metadata", {})
    request_id = DEFAULT_REQUEST_ID
    if isinstance(metadata, Mapping):
        request_id = str(metadata.get("post_continuation_self_continuation_id") or request_id)
    filename = f"{request_id}__post_continuation_self_continuation_result.json"
    target = Path(output_path) if output_path is not None else OUTPUT_ROOT / filename
    if output_path is not None and (target.suffix == "" or (target.exists() and target.is_dir())):
        target = target / filename
    if target.exists():
        target = _with_numeric_suffix(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(_sanitize(result), ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return target


def _with_numeric_suffix(path: Path) -> Path:
    counter = 1
    while True:
        candidate = path.with_name(f"{path.stem}_{counter:03d}{path.suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


def _basis(
    *,
    name: str,
    outcome: str | None = None,
    result_version: str | None = "0.1.0",
    failed_check_count: int = 0,
    path: str | None = None,
) -> dict[str, Any]:
    basis = {
        "basis_name": name,
        "basis_only": True,
        "selected_basis_reference_shape": True,
        "failed_check_count": failed_check_count,
    }
    if outcome is not None:
        basis["outcome"] = outcome
    if result_version is not None:
        basis["result_version"] = result_version
    if path is not None:
        basis["path"] = path
    return basis


def _default_bounded_self_continuation_envelope() -> dict[str, Any]:
    return {
        "envelope_name": "one_bounded_post_continuation_self_continuation_envelope",
        "posture": (
            "one bounded self-continuation posture from selected standing "
            "self-continuation-boundary and continuation basis"
        ),
        "anything_outside_requires_fresh_admission": True,
        "authorizes_arbitrary_runtime_activity": False,
        "authorizes_self_recursive_growth": False,
        "authorizes_follow_on_work": False,
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
    }


def build_declared_post_continuation_self_continuation_request(
    *,
    self_continuation_request_id: str = DEFAULT_REQUEST_ID,
    self_continuation_question: str = CORE_QUESTION,
    self_continuation_intent: str = INTENT_RECORD,
    self_continuation_scope: Any = SUPPORTED_SCOPE_VALUES,
    requested_bounded_self_continuation_envelope: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build a declared self-continuation request that records cleanly."""

    envelope = (
        _default_bounded_self_continuation_envelope()
        if requested_bounded_self_continuation_envelope is None
        else deepcopy(dict(requested_bounded_self_continuation_envelope))
    )
    request: dict[str, Any] = {
        "self_continuation_request_id": self_continuation_request_id,
        "self_continuation_question": self_continuation_question,
        "self_continuation_intent": self_continuation_intent,
        "selected_self_continuation_boundary_basis": _basis(
            name="post-continuation self-continuation boundary",
            outcome=EXPECTED_SELF_CONTINUATION_BOUNDARY_OUTCOME,
            path=(
                "artifacts/integrity_host_v0_min_coexistence_post_continuation_self_continuation_boundary/"
                "post_continuation_self_continuation_boundary_reference_review_001__"
                "post_continuation_self_continuation_boundary_result.json"
            ),
        ),
        "selected_self_continuation_boundary_terminal_summary_basis": _basis(
            name="post-continuation self-continuation boundary terminal summary",
            outcome=None,
            path="spec/POST_CONTINUATION_SELF_CONTINUATION_BOUNDARY_TERMINAL_SUMMARY_V0.md",
        ),
        "selected_continuation_basis": _basis(
            name="post-reusable-runtime-permission continuation",
            outcome=EXPECTED_CONTINUATION_OUTCOME,
            path=(
                "artifacts/integrity_host_v0_min_coexistence_post_reusable_runtime_permission_continuation/"
                "post_reusable_runtime_permission_continuation_reference_review_001__"
                "post_reusable_runtime_permission_continuation_result.json"
            ),
        ),
        "selected_continuation_terminal_summary_basis": _basis(
            name="post-reusable-runtime-permission continuation terminal summary",
            outcome=None,
            path="spec/POST_REUSABLE_RUNTIME_PERMISSION_CONTINUATION_TERMINAL_SUMMARY_V0.md",
        ),
        "selected_continuation_boundary_basis": _basis(
            name="post-reusable-runtime-permission continuation boundary",
            outcome=EXPECTED_CONTINUATION_BOUNDARY_OUTCOME,
        ),
        "selected_reusable_runtime_permission_basis": _basis(
            name="post-ongoing-runtime reusable-runtime-permission",
            outcome=EXPECTED_REUSABLE_RUNTIME_PERMISSION_OUTCOME,
        ),
        "selected_reusable_runtime_permission_boundary_basis": _basis(
            name="post-ongoing-runtime reusable-runtime-permission boundary",
            outcome=EXPECTED_REUSABLE_RUNTIME_PERMISSION_BOUNDARY_OUTCOME,
        ),
        "selected_ongoing_runtime_basis": _basis(
            name="post-runtime-hosting ongoing-runtime",
            outcome=EXPECTED_ONGOING_RUNTIME_OUTCOME,
        ),
        "selected_runtime_hosting_basis": _basis(
            name="post-successor-runtime-step runtime-hosting",
            outcome=EXPECTED_RUNTIME_HOSTING_OUTCOME,
        ),
        "selected_runtime_hosting_boundary_v2_basis": _basis(
            name="post-successor-runtime-step runtime-hosting-boundary v2",
            outcome=EXPECTED_RUNTIME_HOSTING_BOUNDARY_V2_OUTCOME,
            result_version="0.2.0",
        ),
        "selected_runtime_hosting_boundary_v1_failure_lineage_basis": {
            "basis_name": "post-successor-runtime-step runtime-hosting-boundary v1 failure",
            "basis_only": True,
            "preserved_failed_lineage": True,
            "repaired": False,
            "hidden": False,
            "claimed_passed": False,
        },
        "selected_successor_runtime_step_basis": _basis(
            name="post-minimal-runtime successor-runtime-step",
            outcome=EXPECTED_SUCCESSOR_RUNTIME_STEP_OUTCOME,
        ),
        "selected_minimal_runtime_basis": _basis(
            name="post-portable-verification minimal-runtime",
            outcome=EXPECTED_MINIMAL_RUNTIME_OUTCOME,
        ),
        "selected_runtime_boundary_basis": _basis(
            name="post-portable-verification runtime-boundary",
            outcome=EXPECTED_RUNTIME_BOUNDARY_OUTCOME,
        ),
        "selected_runtime_readiness_basis": _basis(
            name="post-portable-verification runtime-readiness",
            outcome=EXPECTED_RUNTIME_READINESS_OUTCOME,
        ),
        "selected_portable_verification_final_completion_basis": _basis(
            name="portable source-body verification final completion",
            outcome=EXPECTED_FINAL_COMPLETION_OUTCOME,
        ),
        "selected_post_portable_verification_currentness_basis": _basis(
            name="post-portable-verification currentness surface",
            outcome=None,
            path="spec/POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_V0.md",
        ),
        "selected_returned_second_carrier_capture_lineage_basis": {
            "basis_name": "returned second-carrier capture intake lineage",
            "basis_only": True,
            "lineage_only": True,
        },
        "self_continuation_scope": list(self_continuation_scope)
        if not isinstance(self_continuation_scope, str)
        else self_continuation_scope,
        "requested_bounded_self_continuation_envelope": envelope,
        "selected_self_continuation_boundary_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_post_continuation_self_continuation_boundary/"
            "post_continuation_self_continuation_boundary_reference_review_001__"
            "post_continuation_self_continuation_boundary_result.json"
        ),
        "selected_self_continuation_boundary_result_outcome": (
            EXPECTED_SELF_CONTINUATION_BOUNDARY_OUTCOME
        ),
        "selected_self_continuation_boundary_result_version": "0.1.0",
        "selected_self_continuation_boundary_failed_check_count": 0,
        "selected_self_continuation_boundary_declared_future_review": True,
        "selected_self_continuation_boundary_already_authorized_self_continuation": False,
        "selected_self_continuation_boundary_already_created_self_recursive_growth": False,
        "selected_self_continuation_boundary_already_created_runtime_daemon": False,
        "selected_self_continuation_boundary_already_created_runtime_loop": False,
        "selected_self_continuation_boundary_already_created_public_api": False,
        "selected_self_continuation_boundary_already_created_participant_facing_interface": False,
        "selected_self_continuation_boundary_already_created_distributed_network_behavior": False,
        "selected_self_continuation_boundary_treated_as_self_continuation": False,
        "selected_self_continuation_boundary_treated_as_self_recursive_growth": False,
        "selected_self_continuation_boundary_authorized_future_work": False,
        "selected_self_continuation_boundary_non_claims_canonicalized": True,
        "selected_self_continuation_boundary_terminal_summary_self_continuation_not_authorized": True,
        "selected_self_continuation_boundary_terminal_summary_no_self_continuation_selected": True,
        "selected_self_continuation_boundary_terminal_summary_future_work_requires_separate_step_back_review": True,
        "selected_continuation_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_post_reusable_runtime_permission_continuation/"
            "post_reusable_runtime_permission_continuation_reference_review_001__"
            "post_reusable_runtime_permission_continuation_result.json"
        ),
        "selected_continuation_result_outcome": EXPECTED_CONTINUATION_OUTCOME,
        "selected_continuation_result_version": "0.1.0",
        "selected_continuation_failed_check_count": 0,
        "selected_continuation_bounded_posture_recorded": True,
        "selected_continuation_bounded_continuation_envelope_recorded": True,
        "selected_continuation_already_created_self_recursive_growth": False,
        "selected_continuation_already_created_runtime_daemon": False,
        "selected_continuation_already_created_runtime_loop": False,
        "selected_continuation_already_created_public_api": False,
        "selected_continuation_already_created_participant_facing_interface": False,
        "selected_continuation_already_created_distributed_network_behavior": False,
        "selected_bounded_continuation_envelope_treated_as_self_continuation_before_review": False,
        "selected_bounded_continuation_envelope_authorized_arbitrary_runtime_activity_before_review": False,
        "selected_continuation_boundary_result_outcome": EXPECTED_CONTINUATION_BOUNDARY_OUTCOME,
        "selected_continuation_boundary_result_version": "0.1.0",
        "selected_continuation_boundary_failed_check_count": 0,
        "selected_reusable_runtime_permission_result_outcome": EXPECTED_REUSABLE_RUNTIME_PERMISSION_OUTCOME,
        "selected_reusable_runtime_permission_result_version": "0.1.0",
        "selected_reusable_runtime_permission_failed_check_count": 0,
        "selected_reusable_runtime_permission_boundary_result_outcome": (
            EXPECTED_REUSABLE_RUNTIME_PERMISSION_BOUNDARY_OUTCOME
        ),
        "selected_reusable_runtime_permission_boundary_result_version": "0.1.0",
        "selected_reusable_runtime_permission_boundary_failed_check_count": 0,
        "selected_ongoing_runtime_result_outcome": EXPECTED_ONGOING_RUNTIME_OUTCOME,
        "selected_ongoing_runtime_result_version": "0.1.0",
        "selected_ongoing_runtime_failed_check_count": 0,
        "selected_runtime_hosting_result_outcome": EXPECTED_RUNTIME_HOSTING_OUTCOME,
        "selected_runtime_hosting_result_version": "0.1.0",
        "selected_runtime_hosting_failed_check_count": 0,
        "selected_runtime_hosting_boundary_v2_result_outcome": EXPECTED_RUNTIME_HOSTING_BOUNDARY_V2_OUTCOME,
        "selected_runtime_hosting_boundary_v2_result_version": "0.2.0",
        "selected_runtime_hosting_boundary_v2_failed_check_count": 0,
        "selected_runtime_hosting_boundary_v1_failure_repaired": False,
        "selected_runtime_hosting_boundary_v1_failure_hidden": False,
        "selected_runtime_hosting_boundary_v1_failure_claimed_passed": False,
        "selected_successor_runtime_step_result_outcome": EXPECTED_SUCCESSOR_RUNTIME_STEP_OUTCOME,
        "selected_successor_runtime_step_result_version": "0.1.0",
        "selected_successor_runtime_step_failed_check_count": 0,
        "selected_minimal_runtime_result_outcome": EXPECTED_MINIMAL_RUNTIME_OUTCOME,
        "selected_minimal_runtime_result_version": "0.1.0",
        "selected_minimal_runtime_failed_check_count": 0,
        "selected_runtime_boundary_result_outcome": EXPECTED_RUNTIME_BOUNDARY_OUTCOME,
        "selected_runtime_boundary_result_version": "0.1.0",
        "selected_runtime_boundary_failed_check_count": 0,
        "selected_runtime_readiness_result_outcome": EXPECTED_RUNTIME_READINESS_OUTCOME,
        "selected_runtime_readiness_result_version": "0.1.0",
        "selected_runtime_readiness_failed_check_count": 0,
        "selected_portable_verification_final_completion_result_outcome": (
            EXPECTED_FINAL_COMPLETION_OUTCOME
        ),
        "selected_portable_verification_final_completion_result_version": "0.1.0",
        "selected_portable_verification_final_completion_failed_check_count": 0,
        "selected_post_portable_currentness_surface_path": (
            "spec/POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_V0.md"
        ),
        "selected_post_portable_currentness_surface_states_checkability_not_continuation": True,
        "selected_post_portable_currentness_surface_authorized_next_work": False,
        "reference_shaped_input_posture": True,
        "declared_non_claims": _canonical_false_non_claims(),
    }

    for posture_field in POSTURE_FIELDS:
        request[posture_field] = _declared_posture(posture_field.removesuffix("_posture"))

    for key in REQUIRED_FALSE_NON_CLAIMS:
        request[key] = False
    for field, _code in FALSE_INPUT_CHECKS:
        request[field] = False

    request.update(overrides)
    return request
