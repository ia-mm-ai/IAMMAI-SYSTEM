"""Resolve one bounded post-self-continuation self-recursive-growth posture.

This module is downstream of the self-recursive-growth-boundary line. It records
one bounded self-recursive-growth posture and one bounded self-recursive-growth
envelope only. It does not create a daemon, loop, public API,
participant-facing interface, distributed network behavior, source transfer,
source receipt, reception authorization, source, authority, currentness,
deployment, public release, operation permission, broader reusable permission,
adoption, receiving-context governance, publication flow, or follow-on work.
"""

from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any, Mapping


class PostSelfContinuationSelfRecursiveGrowthError(Exception):
    """Bounded local resolver error."""


def _tokens(value: str) -> tuple[str, ...]:
    return tuple(value.split())


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_post_self_continuation_self_recursive_growth"

OUTCOME_RECORDED = "POST_SELF_CONTINUATION_SELF_RECURSIVE_GROWTH_RECORDED"
OUTCOME_NOT_RECORDED = "POST_SELF_CONTINUATION_SELF_RECURSIVE_GROWTH_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "POST_SELF_CONTINUATION_SELF_RECURSIVE_GROWTH_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "POST_SELF_CONTINUATION_SELF_RECURSIVE_GROWTH_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_post_self_continuation_self_recursive_growth"
)

INTENT_RECORD = "RECORD_POST_SELF_CONTINUATION_SELF_RECURSIVE_GROWTH"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_POST_SELF_CONTINUATION_SELF_RECURSIVE_GROWTH"
INTENT_BLOCK = "BLOCK_POST_SELF_CONTINUATION_SELF_RECURSIVE_GROWTH"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

CORE_QUESTION = (
    "Can the clean post-self-continuation self-recursive-growth-boundary basis "
    "be used to record one bounded self-recursive-growth posture without "
    "creating runtime daemon, runtime loop, public API, participant-facing "
    "interface, distributed network behavior, source transfer, source receipt, "
    "reception authorization, source, authority, currentness, deployment, "
    "public release, operation permission, broader reusable permission, "
    "derivative reception, vessel relation, another reception request, "
    "adoption, receiving-context governance, publication flow, or follow-on "
    "work?"
)

SUPPORTED_SCOPE_VALUES = _tokens(
    """
    SELF_RECURSIVE_GROWTH_SPEC_ONLY
    ONE_BOUNDED_SELF_RECURSIVE_GROWTH_POSTURE_RECORDED
    SELF_RECURSIVE_GROWTH_BOUNDARY_BASIS_PRESERVED
    SELF_CONTINUATION_BASIS_PRESERVED
    BOUNDED_SELF_CONTINUATION_ENVELOPE_PRESERVED
    BOUNDED_SELF_RECURSIVE_GROWTH_ENVELOPE_DECLARED
    SELF_RECURSIVE_GROWTH_NOT_DAEMON SELF_RECURSIVE_GROWTH_NOT_LOOP
    SELF_RECURSIVE_GROWTH_NOT_PUBLIC_API
    SELF_RECURSIVE_GROWTH_NOT_PARTICIPANT_FACING_INTERFACE
    SELF_RECURSIVE_GROWTH_NOT_DISTRIBUTED_NETWORK_BEHAVIOR
    RUNTIME_DAEMON_NOT_CREATED RUNTIME_LOOP_NOT_CREATED PUBLIC_API_NOT_CREATED
    PARTICIPANT_FACING_INTERFACE_NOT_CREATED DISTRIBUTED_NETWORK_BEHAVIOR_NOT_CREATED
    NO_SOURCE_TRANSFER NO_SOURCE_RECEIPT NO_RECEPTION_AUTHORIZATION
    NO_SOURCE_CREATED NO_AUTHORITY_CREATED NO_CURRENTNESS_CREATED NO_DEPLOYMENT_CREATED
    NO_PUBLIC_RELEASE_CREATED NO_OPERATION_PERMISSION_CREATED NO_BROADER_REUSABLE_PERMISSION
    NO_DERIVATIVE_RECEPTION NO_VESSEL_RELATION NO_ANOTHER_RECEPTION_REQUEST
    NO_ADOPTION NO_RECEIVING_CONTEXT_GOVERNANCE NO_PUBLICATION_FLOW
    NO_FOLLOW_ON_WORK_AUTHORIZED NO_DAEMON_INFERENCE NO_LOOP_INFERENCE
    NO_PUBLIC_API_INFERENCE NO_PARTICIPANT_INTERFACE_INFERENCE
    NO_DISTRIBUTED_NETWORK_INFERENCE NO_SOURCE_INFERENCE NO_AUTHORITY_INFERENCE
    NO_CURRENTNESS_INFERENCE NO_DEPLOYMENT_INFERENCE NO_PUBLIC_RELEASE_INFERENCE
    NO_OPERATION_PERMISSION_INFERENCE NO_FOLLOW_ON_WORK_INFERENCE
    NO_UNBOUNDED_PASS_FAIL_INFERENCE HIDDEN_REPO_STATE_EXCLUDED
    HIDDEN_REPO_STATE_NOT_USED_AS_SELF_RECURSIVE_GROWTH_AUTHORITY
    REPO_LOCAL_AVAILABILITY_NOT_SELF_RECURSIVE_GROWTH_AUTHORITY
    ARTIFACT_EXISTENCE_NOT_SELF_RECURSIVE_GROWTH_AUTHORITY
    LATEST_FILE_POSTURE_NOT_SELF_RECURSIVE_GROWTH_AUTHORITY
    SELECTED_BASIS_REFERENCE_SHAPE_PRESERVED RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED
    OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED HOSTILE_RAW_BODY_CONTENT_CONTAINED
    PREDECESSOR_FAILURE_EVIDENCE_PRESERVED AUTHORIZATION_TOKEN_REUSE_BLOCKED
    CONSUMED_REQUEST_TOKEN_REMAINS_CLOSED CONSUMED_REQUEST_NOT_REOPENED
    RESULT_LEVEL_NON_CLAIMS_CANONICAL_FALSE
    """
)
SUPPORTED_SELF_RECURSIVE_GROWTH_SCOPE = SUPPORTED_SCOPE_VALUES

REQUIRED_FALSE_NON_CLAIMS = _tokens(
    """
    runtime_daemon_created runtime_loop_created public_api_created
    participant_facing_interface_created distributed_network_behavior_created
    source_transfer_occurred source_receipt_occurred reception_authorization_created
    self_recursive_growth_treated_as_runtime_daemon
    self_recursive_growth_treated_as_runtime_loop
    self_recursive_growth_treated_as_public_api
    self_recursive_growth_treated_as_participant_facing_interface
    self_recursive_growth_treated_as_distributed_network_behavior
    self_recursive_growth_treated_as_source_transfer
    self_recursive_growth_treated_as_source_receipt
    self_recursive_growth_treated_as_reception_authorization
    self_recursive_growth_treated_as_source self_recursive_growth_treated_as_authority
    self_recursive_growth_treated_as_currentness
    self_recursive_growth_treated_as_deployment
    self_recursive_growth_treated_as_public_release
    self_recursive_growth_treated_as_operation_permission
    self_recursive_growth_treated_as_broader_reusable_permission
    self_recursive_growth_treated_as_follow_on_work
    self_recursive_growth_boundary_treated_as_self_recursive_growth_without_review
    self_continuation_treated_as_self_recursive_growth_without_review
    bounded_self_continuation_envelope_treated_as_self_recursive_growth_without_review
    artifact_existence_treated_as_self_recursive_growth_authority
    artifact_path_treated_as_currentness
    latest_file_posture_treated_as_self_recursive_growth_authority
    repo_local_availability_treated_as_self_recursive_growth_authority
    hidden_repo_state_used_as_self_recursive_growth_content
    hidden_repo_state_used_as_self_recursive_growth_authority
    source_created authority_created currentness_created deployment_created
    public_release_created operation_permission_created broader_reusable_permission_created
    derivative_reception_authorized vessel_relation_authorized
    another_reception_request_authorized adoption_created
    receiving_context_governance_created publication_flow_created follow_on_work_authorized
    raw_full_prior_artifact_body_returned prior_artifacts_mutated
    consumed_request_reopened authorization_token_reused predecessor_failure_repaired
    predecessor_failure_hidden predecessor_failure_claimed_passed
    runtime_hosting_boundary_v1_failure_repaired
    runtime_hosting_boundary_v1_failure_hidden
    runtime_hosting_boundary_v1_failure_claimed_passed
    """
)

ALLOWED_TRUE_RECORDED_FIELDS = _tokens(
    """
    self_recursive_growth_recorded bounded_self_recursive_growth_posture_recorded
    self_recursive_growth_boundary_basis_preserved self_continuation_basis_preserved
    bounded_self_continuation_envelope_preserved
    bounded_self_recursive_growth_envelope_declared self_recursive_growth_not_daemon
    self_recursive_growth_not_loop self_recursive_growth_not_public_api
    self_recursive_growth_not_participant_facing_interface
    self_recursive_growth_not_distributed_network_behavior runtime_daemon_not_created
    runtime_loop_not_created public_api_not_created participant_facing_interface_not_created
    distributed_network_behavior_not_created source_transfer_not_created
    source_receipt_not_created reception_authorization_not_created source_not_created
    authority_not_created currentness_not_created deployment_not_created
    public_release_not_created operation_permission_not_created
    broader_reusable_permission_not_created follow_on_work_not_authorized
    hidden_repo_state_excluded hidden_repo_state_not_used_as_self_recursive_growth_authority
    repo_local_availability_not_self_recursive_growth_authority
    artifact_existence_not_self_recursive_growth_authority
    latest_file_posture_not_self_recursive_growth_authority
    selected_basis_reference_shape_preserved raw_full_prior_artifact_body_not_returned
    official_enum_scope_strings_not_redacted hostile_raw_body_content_contained
    predecessor_failure_evidence_preserved authorization_token_reuse_blocked
    consumed_request_token_remains_closed result_level_non_claims_canonical_false
    """
)

BLOCK_CODES = _tokens(
    """
    SELF_RECURSIVE_GROWTH_QUESTION_UNDECLARED SELF_RECURSIVE_GROWTH_INTENT_UNSUPPORTED
    SELF_RECURSIVE_GROWTH_EXPLICIT_BLOCK_REQUESTED
    SELF_RECURSIVE_GROWTH_BOUNDARY_BASIS_MISSING
    SELF_RECURSIVE_GROWTH_BOUNDARY_TERMINAL_SUMMARY_BASIS_MISSING
    SELF_RECURSIVE_GROWTH_BOUNDARY_NOT_RECORDED
    SELF_RECURSIVE_GROWTH_BOUNDARY_FAILED_CHECKS_PRESENT
    SELF_RECURSIVE_GROWTH_BOUNDARY_VERSION_NOT_0_1_0
    SELF_RECURSIVE_GROWTH_BOUNDARY_DID_NOT_DECLARE_FUTURE_SELF_RECURSIVE_GROWTH_REVIEW
    SELF_RECURSIVE_GROWTH_BOUNDARY_ALREADY_CREATED_SELF_RECURSIVE_GROWTH
    SELF_RECURSIVE_GROWTH_BOUNDARY_ALREADY_CREATED_RUNTIME_DAEMON
    SELF_RECURSIVE_GROWTH_BOUNDARY_ALREADY_CREATED_RUNTIME_LOOP
    SELF_RECURSIVE_GROWTH_BOUNDARY_ALREADY_CREATED_PUBLIC_API
    SELF_RECURSIVE_GROWTH_BOUNDARY_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE
    SELF_RECURSIVE_GROWTH_BOUNDARY_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR
    SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_SELF_RECURSIVE_GROWTH
    SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_RUNTIME_DAEMON
    SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_RUNTIME_LOOP
    SELF_RECURSIVE_GROWTH_BOUNDARY_AUTHORIZED_FUTURE_WORK
    SELF_RECURSIVE_GROWTH_BOUNDARY_NON_CLAIMS_NOT_CANONICAL_FALSE
    SELF_RECURSIVE_GROWTH_BOUNDARY_TERMINAL_SUMMARY_DID_NOT_PRESERVE_NO_SELF_RECURSIVE_GROWTH
    SELF_RECURSIVE_GROWTH_BOUNDARY_TERMINAL_SUMMARY_DID_NOT_PRESERVE_NO_SELF_RECURSIVE_GROWTH_SELECTED
    SELF_RECURSIVE_GROWTH_BOUNDARY_TERMINAL_SUMMARY_DID_NOT_REQUIRE_SEPARATE_REVIEW
    SELF_CONTINUATION_BASIS_MISSING SELF_CONTINUATION_TERMINAL_SUMMARY_BASIS_MISSING
    SELF_CONTINUATION_NOT_RECORDED SELF_CONTINUATION_FAILED_CHECKS_PRESENT
    SELF_CONTINUATION_VERSION_NOT_0_1_0
    SELF_CONTINUATION_DID_NOT_RECORD_BOUNDED_SELF_CONTINUATION_POSTURE
    SELF_CONTINUATION_DID_NOT_RECORD_BOUNDED_SELF_CONTINUATION_ENVELOPE
    SELF_CONTINUATION_ALREADY_CREATED_RUNTIME_DAEMON
    SELF_CONTINUATION_ALREADY_CREATED_RUNTIME_LOOP
    SELF_CONTINUATION_ALREADY_CREATED_PUBLIC_API
    SELF_CONTINUATION_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE
    SELF_CONTINUATION_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR
    BOUNDED_SELF_CONTINUATION_ENVELOPE_TREATED_AS_SELF_RECURSIVE_GROWTH_BEFORE_REVIEW
    BOUNDED_SELF_CONTINUATION_ENVELOPE_AUTHORIZED_ARBITRARY_RUNTIME_ACTIVITY_BEFORE_REVIEW
    SELF_CONTINUATION_BOUNDARY_BASIS_MISSING SELF_CONTINUATION_BOUNDARY_NOT_RECORDED
    SELF_CONTINUATION_BOUNDARY_FAILED_CHECKS_PRESENT
    SELF_CONTINUATION_BOUNDARY_VERSION_NOT_0_1_0
    CONTINUATION_BASIS_MISSING CONTINUATION_NOT_RECORDED CONTINUATION_FAILED_CHECKS_PRESENT
    CONTINUATION_VERSION_NOT_0_1_0 CONTINUATION_BOUNDARY_BASIS_MISSING
    CONTINUATION_BOUNDARY_NOT_RECORDED CONTINUATION_BOUNDARY_FAILED_CHECKS_PRESENT
    CONTINUATION_BOUNDARY_VERSION_NOT_0_1_0 REUSABLE_RUNTIME_PERMISSION_BASIS_MISSING
    REUSABLE_RUNTIME_PERMISSION_NOT_RECORDED REUSABLE_RUNTIME_PERMISSION_FAILED_CHECKS_PRESENT
    REUSABLE_RUNTIME_PERMISSION_VERSION_NOT_0_1_0
    REUSABLE_RUNTIME_PERMISSION_BOUNDARY_BASIS_MISSING
    REUSABLE_RUNTIME_PERMISSION_BOUNDARY_NOT_RECORDED
    REUSABLE_RUNTIME_PERMISSION_BOUNDARY_FAILED_CHECKS_PRESENT
    REUSABLE_RUNTIME_PERMISSION_BOUNDARY_VERSION_NOT_0_1_0
    ONGOING_RUNTIME_BASIS_MISSING ONGOING_RUNTIME_NOT_RECORDED
    ONGOING_RUNTIME_FAILED_CHECKS_PRESENT ONGOING_RUNTIME_VERSION_NOT_0_1_0
    RUNTIME_HOSTING_BASIS_MISSING RUNTIME_HOSTING_NOT_RECORDED
    RUNTIME_HOSTING_FAILED_CHECKS_PRESENT RUNTIME_HOSTING_VERSION_NOT_0_1_0
    RUNTIME_HOSTING_BOUNDARY_V2_BASIS_MISSING RUNTIME_HOSTING_BOUNDARY_V2_NOT_RECORDED
    RUNTIME_HOSTING_BOUNDARY_V2_FAILED_CHECKS_PRESENT
    RUNTIME_HOSTING_BOUNDARY_V2_VERSION_NOT_0_2_0
    RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_LINEAGE_MISSING
    RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED
    SUCCESSOR_RUNTIME_STEP_BASIS_MISSING SUCCESSOR_RUNTIME_STEP_NOT_RECORDED
    SUCCESSOR_RUNTIME_STEP_FAILED_CHECKS_PRESENT SUCCESSOR_RUNTIME_STEP_VERSION_NOT_0_1_0
    MINIMAL_RUNTIME_BASIS_MISSING MINIMAL_RUNTIME_NOT_RECORDED
    MINIMAL_RUNTIME_FAILED_CHECKS_PRESENT MINIMAL_RUNTIME_VERSION_NOT_0_1_0
    RUNTIME_BOUNDARY_BASIS_MISSING RUNTIME_BOUNDARY_NOT_RECORDED
    RUNTIME_BOUNDARY_FAILED_CHECKS_PRESENT RUNTIME_BOUNDARY_VERSION_NOT_0_1_0
    RUNTIME_READINESS_BASIS_MISSING RUNTIME_READINESS_NOT_RECORDED
    RUNTIME_READINESS_FAILED_CHECKS_PRESENT RUNTIME_READINESS_VERSION_NOT_0_1_0
    PORTABLE_VERIFICATION_FINAL_COMPLETION_BASIS_MISSING
    PORTABLE_VERIFICATION_FINAL_COMPLETION_NOT_RECORDED
    PORTABLE_VERIFICATION_FINAL_COMPLETION_FAILED_CHECKS_PRESENT
    PORTABLE_VERIFICATION_FINAL_COMPLETION_VERSION_NOT_0_1_0
    POST_PORTABLE_CURRENTNESS_SURFACE_BASIS_MISSING
    POST_PORTABLE_CURRENTNESS_SURFACE_TREATED_CHECKABILITY_AS_CONTINUATION
    POST_PORTABLE_CURRENTNESS_SURFACE_AUTHORIZED_NEXT_WORK
    RETURNED_SECOND_CARRIER_CAPTURE_LINEAGE_BASIS_MISSING
    PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED
    SELF_RECURSIVE_GROWTH_REQUIRED_POSTURE_MISSING
    SELF_RECURSIVE_GROWTH_CREATED_BEFORE_REVIEW
    SELF_RECURSIVE_GROWTH_TREATED_AS_RUNTIME_DAEMON
    SELF_RECURSIVE_GROWTH_TREATED_AS_RUNTIME_LOOP
    SELF_RECURSIVE_GROWTH_TREATED_AS_PUBLIC_API
    SELF_RECURSIVE_GROWTH_TREATED_AS_PARTICIPANT_FACING_INTERFACE
    SELF_RECURSIVE_GROWTH_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR
    SELF_RECURSIVE_GROWTH_TREATED_AS_SOURCE_TRANSFER
    SELF_RECURSIVE_GROWTH_TREATED_AS_SOURCE_RECEIPT
    SELF_RECURSIVE_GROWTH_TREATED_AS_RECEPTION_AUTHORIZATION
    SELF_RECURSIVE_GROWTH_TREATED_AS_SOURCE SELF_RECURSIVE_GROWTH_TREATED_AS_AUTHORITY
    SELF_RECURSIVE_GROWTH_TREATED_AS_CURRENTNESS
    SELF_RECURSIVE_GROWTH_TREATED_AS_DEPLOYMENT
    SELF_RECURSIVE_GROWTH_TREATED_AS_PUBLIC_RELEASE
    SELF_RECURSIVE_GROWTH_TREATED_AS_OPERATION_PERMISSION
    SELF_RECURSIVE_GROWTH_TREATED_AS_BROADER_REUSABLE_PERMISSION
    SELF_RECURSIVE_GROWTH_TREATED_AS_FOLLOW_ON_WORK
    RUNTIME_DAEMON_CREATED RUNTIME_LOOP_CREATED PUBLIC_API_CREATED
    PARTICIPANT_FACING_INTERFACE_CREATED DISTRIBUTED_NETWORK_BEHAVIOR_CREATED
    SOURCE_TRANSFER_OCCURRED SOURCE_RECEIPT_OCCURRED RECEPTION_AUTHORIZATION_CREATED
    SOURCE_CREATED AUTHORITY_CREATED CURRENTNESS_CREATED DEPLOYMENT_CREATED
    PUBLIC_RELEASE_CREATED OPERATION_PERMISSION_CREATED BROADER_REUSABLE_PERMISSION_CREATED
    DERIVATIVE_RECEPTION_AUTHORIZED VESSEL_RELATION_AUTHORIZED
    ANOTHER_RECEPTION_REQUEST_AUTHORIZED ADOPTION_CREATED
    RECEIVING_CONTEXT_GOVERNANCE_CREATED PUBLICATION_FLOW_CREATED FOLLOW_ON_WORK_AUTHORIZED
    ARTIFACT_EXISTENCE_TREATED_AS_SELF_RECURSIVE_GROWTH_AUTHORITY
    ARTIFACT_PATH_TREATED_AS_CURRENTNESS
    LATEST_FILE_POSTURE_TREATED_AS_SELF_RECURSIVE_GROWTH_AUTHORITY
    REPO_LOCAL_AVAILABILITY_TREATED_AS_SELF_RECURSIVE_GROWTH_AUTHORITY
    HIDDEN_REPO_STATE_USED_AS_SELF_RECURSIVE_GROWTH_CONTENT
    HIDDEN_REPO_STATE_USED_AS_SELF_RECURSIVE_GROWTH_AUTHORITY
    SELECTED_BASIS_NOT_REFERENCE_SHAPED RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED
    PRIOR_ARTIFACTS_MUTATED CONSUMED_REQUEST_REOPENED AUTHORIZATION_TOKEN_REUSED
    NON_CLAIM_MISSING_OR_FLIPPED UNSUPPORTED_SELF_RECURSIVE_GROWTH_SCOPE
    OFFICIAL_ENUM_SCOPE_STRINGS_REDACTED HOSTILE_RAW_BODY_CONTENT_NOT_CONTAINED
    DECLARED_SELF_RECURSIVE_GROWTH_REQUEST_MALFORMED
    DECLARED_SELF_RECURSIVE_GROWTH_REQUEST_UNREADABLE
    """
)

SELECTED_BASIS_FIELDS = (
    "selected_self_recursive_growth_boundary_basis",
    "selected_self_recursive_growth_boundary_terminal_summary_basis",
    "selected_self_continuation_basis",
    "selected_self_continuation_terminal_summary_basis",
    "selected_self_continuation_boundary_basis",
    "selected_continuation_basis",
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

POSTURE_FIELDS = (
    "self_recursive_growth_spec_only_posture",
    "one_bounded_self_recursive_growth_posture",
    "self_recursive_growth_boundary_basis_preserved_posture",
    "self_continuation_basis_preserved_posture",
    "bounded_self_continuation_envelope_preserved_posture",
    "bounded_self_recursive_growth_envelope_declared_posture",
    "self_recursive_growth_not_daemon_posture",
    "self_recursive_growth_not_loop_posture",
    "self_recursive_growth_not_public_api_posture",
    "self_recursive_growth_not_participant_facing_interface_posture",
    "self_recursive_growth_not_distributed_network_behavior_posture",
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
    "broader_reusable_permission_not_created_posture",
    "follow_on_work_not_authorized_posture",
    "hidden_repo_state_excluded_posture",
    "repo_local_availability_not_self_recursive_growth_authority_posture",
    "artifact_existence_not_self_recursive_growth_authority_posture",
    "latest_file_posture_not_self_recursive_growth_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
    "result_level_non_claims_canonical_false_posture",
)

BASIS_SHORTCUT_PREFIXES = {
    "selected_self_recursive_growth_boundary_basis": "self_recursive_growth_boundary",
    "selected_self_continuation_basis": "self_continuation",
    "selected_self_continuation_boundary_basis": "self_continuation_boundary",
    "selected_continuation_basis": "continuation",
    "selected_continuation_boundary_basis": "continuation_boundary",
    "selected_reusable_runtime_permission_basis": "reusable_runtime_permission",
    "selected_reusable_runtime_permission_boundary_basis": "reusable_runtime_permission_boundary",
    "selected_ongoing_runtime_basis": "ongoing_runtime",
    "selected_runtime_hosting_basis": "runtime_hosting",
    "selected_runtime_hosting_boundary_v2_basis": "runtime_hosting_boundary_v2",
    "selected_successor_runtime_step_basis": "successor_runtime_step",
    "selected_minimal_runtime_basis": "minimal_runtime",
    "selected_runtime_boundary_basis": "runtime_boundary",
    "selected_runtime_readiness_basis": "runtime_readiness",
    "selected_portable_verification_final_completion_basis": "portable_verification_final_completion",
}

UPSTREAM_EXPECTATIONS = (
    (
        "selected_self_continuation_boundary_basis",
        "self_continuation_boundary",
        "POST_CONTINUATION_SELF_CONTINUATION_BOUNDARY_RECORDED",
        "0.1.0",
        "SELF_CONTINUATION_BOUNDARY_BASIS_MISSING",
        "SELF_CONTINUATION_BOUNDARY_NOT_RECORDED",
        "SELF_CONTINUATION_BOUNDARY_VERSION_NOT_0_1_0",
        "SELF_CONTINUATION_BOUNDARY_FAILED_CHECKS_PRESENT",
    ),
    (
        "selected_continuation_basis",
        "continuation",
        "POST_REUSABLE_RUNTIME_PERMISSION_CONTINUATION_RECORDED",
        "0.1.0",
        "CONTINUATION_BASIS_MISSING",
        "CONTINUATION_NOT_RECORDED",
        "CONTINUATION_VERSION_NOT_0_1_0",
        "CONTINUATION_FAILED_CHECKS_PRESENT",
    ),
    (
        "selected_continuation_boundary_basis",
        "continuation_boundary",
        "POST_REUSABLE_RUNTIME_PERMISSION_CONTINUATION_BOUNDARY_RECORDED",
        "0.1.0",
        "CONTINUATION_BOUNDARY_BASIS_MISSING",
        "CONTINUATION_BOUNDARY_NOT_RECORDED",
        "CONTINUATION_BOUNDARY_VERSION_NOT_0_1_0",
        "CONTINUATION_BOUNDARY_FAILED_CHECKS_PRESENT",
    ),
    (
        "selected_reusable_runtime_permission_basis",
        "reusable_runtime_permission",
        "POST_ONGOING_RUNTIME_REUSABLE_RUNTIME_PERMISSION_RECORDED",
        "0.1.0",
        "REUSABLE_RUNTIME_PERMISSION_BASIS_MISSING",
        "REUSABLE_RUNTIME_PERMISSION_NOT_RECORDED",
        "REUSABLE_RUNTIME_PERMISSION_VERSION_NOT_0_1_0",
        "REUSABLE_RUNTIME_PERMISSION_FAILED_CHECKS_PRESENT",
    ),
    (
        "selected_reusable_runtime_permission_boundary_basis",
        "reusable_runtime_permission_boundary",
        "POST_ONGOING_RUNTIME_REUSABLE_RUNTIME_PERMISSION_BOUNDARY_RECORDED",
        "0.1.0",
        "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_BASIS_MISSING",
        "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_NOT_RECORDED",
        "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_VERSION_NOT_0_1_0",
        "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_FAILED_CHECKS_PRESENT",
    ),
    (
        "selected_ongoing_runtime_basis",
        "ongoing_runtime",
        "POST_RUNTIME_HOSTING_ONGOING_RUNTIME_RECORDED",
        "0.1.0",
        "ONGOING_RUNTIME_BASIS_MISSING",
        "ONGOING_RUNTIME_NOT_RECORDED",
        "ONGOING_RUNTIME_VERSION_NOT_0_1_0",
        "ONGOING_RUNTIME_FAILED_CHECKS_PRESENT",
    ),
    (
        "selected_runtime_hosting_basis",
        "runtime_hosting",
        "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_RECORDED",
        "0.1.0",
        "RUNTIME_HOSTING_BASIS_MISSING",
        "RUNTIME_HOSTING_NOT_RECORDED",
        "RUNTIME_HOSTING_VERSION_NOT_0_1_0",
        "RUNTIME_HOSTING_FAILED_CHECKS_PRESENT",
    ),
    (
        "selected_runtime_hosting_boundary_v2_basis",
        "runtime_hosting_boundary_v2",
        "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_BOUNDARY_RECORDED",
        "0.2.0",
        "RUNTIME_HOSTING_BOUNDARY_V2_BASIS_MISSING",
        "RUNTIME_HOSTING_BOUNDARY_V2_NOT_RECORDED",
        "RUNTIME_HOSTING_BOUNDARY_V2_VERSION_NOT_0_2_0",
        "RUNTIME_HOSTING_BOUNDARY_V2_FAILED_CHECKS_PRESENT",
    ),
    (
        "selected_successor_runtime_step_basis",
        "successor_runtime_step",
        "POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_RECORDED",
        "0.1.0",
        "SUCCESSOR_RUNTIME_STEP_BASIS_MISSING",
        "SUCCESSOR_RUNTIME_STEP_NOT_RECORDED",
        "SUCCESSOR_RUNTIME_STEP_VERSION_NOT_0_1_0",
        "SUCCESSOR_RUNTIME_STEP_FAILED_CHECKS_PRESENT",
    ),
    (
        "selected_minimal_runtime_basis",
        "minimal_runtime",
        "POST_PORTABLE_VERIFICATION_MINIMAL_RUNTIME_RECORDED",
        "0.1.0",
        "MINIMAL_RUNTIME_BASIS_MISSING",
        "MINIMAL_RUNTIME_NOT_RECORDED",
        "MINIMAL_RUNTIME_VERSION_NOT_0_1_0",
        "MINIMAL_RUNTIME_FAILED_CHECKS_PRESENT",
    ),
    (
        "selected_runtime_boundary_basis",
        "runtime_boundary",
        "POST_PORTABLE_VERIFICATION_RUNTIME_BOUNDARY_RECORDED",
        "0.1.0",
        "RUNTIME_BOUNDARY_BASIS_MISSING",
        "RUNTIME_BOUNDARY_NOT_RECORDED",
        "RUNTIME_BOUNDARY_VERSION_NOT_0_1_0",
        "RUNTIME_BOUNDARY_FAILED_CHECKS_PRESENT",
    ),
    (
        "selected_runtime_readiness_basis",
        "runtime_readiness",
        "POST_PORTABLE_VERIFICATION_RUNTIME_READINESS_RECORDED",
        "0.1.0",
        "RUNTIME_READINESS_BASIS_MISSING",
        "RUNTIME_READINESS_NOT_RECORDED",
        "RUNTIME_READINESS_VERSION_NOT_0_1_0",
        "RUNTIME_READINESS_FAILED_CHECKS_PRESENT",
    ),
    (
        "selected_portable_verification_final_completion_basis",
        "portable_verification_final_completion",
        "PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_RECORDED",
        "0.1.0",
        "PORTABLE_VERIFICATION_FINAL_COMPLETION_BASIS_MISSING",
        "PORTABLE_VERIFICATION_FINAL_COMPLETION_NOT_RECORDED",
        "PORTABLE_VERIFICATION_FINAL_COMPLETION_VERSION_NOT_0_1_0",
        "PORTABLE_VERIFICATION_FINAL_COMPLETION_FAILED_CHECKS_PRESENT",
    ),
)

FALSE_INPUT_CHECKS = (
    ("self_recursive_growth_created_before_review", "SELF_RECURSIVE_GROWTH_CREATED_BEFORE_REVIEW"),
    ("self_recursive_growth_treated_as_runtime_daemon", "SELF_RECURSIVE_GROWTH_TREATED_AS_RUNTIME_DAEMON"),
    ("self_recursive_growth_treated_as_runtime_loop", "SELF_RECURSIVE_GROWTH_TREATED_AS_RUNTIME_LOOP"),
    ("self_recursive_growth_treated_as_public_api", "SELF_RECURSIVE_GROWTH_TREATED_AS_PUBLIC_API"),
    (
        "self_recursive_growth_treated_as_participant_facing_interface",
        "SELF_RECURSIVE_GROWTH_TREATED_AS_PARTICIPANT_FACING_INTERFACE",
    ),
    (
        "self_recursive_growth_treated_as_distributed_network_behavior",
        "SELF_RECURSIVE_GROWTH_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR",
    ),
    ("self_recursive_growth_treated_as_source_transfer", "SELF_RECURSIVE_GROWTH_TREATED_AS_SOURCE_TRANSFER"),
    ("self_recursive_growth_treated_as_source_receipt", "SELF_RECURSIVE_GROWTH_TREATED_AS_SOURCE_RECEIPT"),
    (
        "self_recursive_growth_treated_as_reception_authorization",
        "SELF_RECURSIVE_GROWTH_TREATED_AS_RECEPTION_AUTHORIZATION",
    ),
    ("self_recursive_growth_treated_as_source", "SELF_RECURSIVE_GROWTH_TREATED_AS_SOURCE"),
    ("self_recursive_growth_treated_as_authority", "SELF_RECURSIVE_GROWTH_TREATED_AS_AUTHORITY"),
    ("self_recursive_growth_treated_as_currentness", "SELF_RECURSIVE_GROWTH_TREATED_AS_CURRENTNESS"),
    ("self_recursive_growth_treated_as_deployment", "SELF_RECURSIVE_GROWTH_TREATED_AS_DEPLOYMENT"),
    ("self_recursive_growth_treated_as_public_release", "SELF_RECURSIVE_GROWTH_TREATED_AS_PUBLIC_RELEASE"),
    (
        "self_recursive_growth_treated_as_operation_permission",
        "SELF_RECURSIVE_GROWTH_TREATED_AS_OPERATION_PERMISSION",
    ),
    (
        "self_recursive_growth_treated_as_broader_reusable_permission",
        "SELF_RECURSIVE_GROWTH_TREATED_AS_BROADER_REUSABLE_PERMISSION",
    ),
    ("self_recursive_growth_treated_as_follow_on_work", "SELF_RECURSIVE_GROWTH_TREATED_AS_FOLLOW_ON_WORK"),
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
    ("artifact_existence_treated_as_self_recursive_growth_authority", "ARTIFACT_EXISTENCE_TREATED_AS_SELF_RECURSIVE_GROWTH_AUTHORITY"),
    ("artifact_path_treated_as_currentness", "ARTIFACT_PATH_TREATED_AS_CURRENTNESS"),
    ("latest_file_posture_treated_as_self_recursive_growth_authority", "LATEST_FILE_POSTURE_TREATED_AS_SELF_RECURSIVE_GROWTH_AUTHORITY"),
    ("repo_local_availability_treated_as_self_recursive_growth_authority", "REPO_LOCAL_AVAILABILITY_TREATED_AS_SELF_RECURSIVE_GROWTH_AUTHORITY"),
    ("hidden_repo_state_used_as_self_recursive_growth_content", "HIDDEN_REPO_STATE_USED_AS_SELF_RECURSIVE_GROWTH_CONTENT"),
    ("hidden_repo_state_used_as_self_recursive_growth_authority", "HIDDEN_REPO_STATE_USED_AS_SELF_RECURSIVE_GROWTH_AUTHORITY"),
    ("raw_full_prior_artifact_body_returned", "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED"),
    ("prior_artifacts_mutated", "PRIOR_ARTIFACTS_MUTATED"),
    ("consumed_request_reopened", "CONSUMED_REQUEST_REOPENED"),
    ("authorization_token_reused", "AUTHORIZATION_TOKEN_REUSED"),
    ("predecessor_failure_repaired", "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
    ("predecessor_failure_hidden", "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
    ("predecessor_failure_claimed_passed", "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
)

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_self_recursive_growth_body",
    "raw_bounded_self_recursive_growth_envelope_body",
    "raw_runtime_daemon_body",
    "raw_runtime_loop_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "raw_runtime_body",
    "self_recursive_growth_body",
    "bounded_self_recursive_growth_envelope_body",
    "runtime_body",
    "source_body",
    "authority_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
}

HOSTILE_SENTINELS = (
    "RAW_SELF_RECURSIVE_GROWTH_BODY_MUST_NOT_RETURN",
    "RAW_BOUNDED_SELF_RECURSIVE_GROWTH_ENVELOPE_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_DAEMON_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_LOOP_BODY_MUST_NOT_RETURN",
    "RAW_PUBLIC_API_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPANT_FACING_INTERFACE_BODY_MUST_NOT_RETURN",
    "RAW_DISTRIBUTED_NETWORK_BEHAVIOR_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)

REDACTED_RAW_VALUE = "[bounded-redacted-raw-or-hidden-state]"
DEFAULT_REQUEST_ID = "post_self_continuation_self_recursive_growth_reference_review_001"


def _now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _canonical_false_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _is_declared(value: Any) -> bool:
    if value is None or value is False:
        return False
    if isinstance(value, str) and not value.strip():
        return False
    if isinstance(value, Mapping) and not value:
        return False
    if isinstance(value, (list, tuple, set)) and not value:
        return False
    return True


def _flag_true(value: Any) -> bool:
    return value is True


def _safe_int(value: Any) -> int | None:
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


def _scope_list(value: Any) -> list[str]:
    if value is None:
        return list(SUPPORTED_SCOPE_VALUES)
    if isinstance(value, str):
        return [value]
    if isinstance(value, (list, tuple, set)):
        return [item for item in value if isinstance(item, str)]
    return []


def _contains_hostile_sentinel(value: Any) -> bool:
    if isinstance(value, str):
        return any(sentinel in value for sentinel in HOSTILE_SENTINELS)
    if isinstance(value, Mapping):
        return any(_contains_hostile_sentinel(item) for item in value.values())
    if isinstance(value, (list, tuple, set)):
        return any(_contains_hostile_sentinel(item) for item in value)
    return False


def _is_sensitive_key(key: Any) -> bool:
    return isinstance(key, str) and (key in SENSITIVE_CONTENT_KEYS or key.endswith("_body"))


def _sanitize(value: Any, *, key: str | None = None) -> Any:
    if key is not None and _is_sensitive_key(key):
        return REDACTED_RAW_VALUE
    if isinstance(value, str):
        if any(sentinel in value for sentinel in HOSTILE_SENTINELS):
            return REDACTED_RAW_VALUE
        return value
    if isinstance(value, Mapping):
        return {str(item_key): _sanitize(item_value, key=str(item_key)) for item_key, item_value in value.items()}
    if isinstance(value, list):
        return [_sanitize(item) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item) for item in value]
    if isinstance(value, set):
        return sorted(_sanitize(item) for item in value)
    return value


def _check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str,
) -> None:
    record: dict[str, Any] = {
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
        if not check.get("passed"):
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str):
                return code
    return None


def _basis_value(request: Mapping[str, Any], basis_field: str, key: str) -> Any:
    value = request.get(basis_field)
    if isinstance(value, Mapping) and key in value:
        return value.get(key)
    prefix = BASIS_SHORTCUT_PREFIXES.get(basis_field)
    if not prefix:
        return None
    if key == "path":
        return request.get(f"selected_{prefix}_result_path")
    if key == "outcome":
        return request.get(f"selected_{prefix}_result_outcome")
    if key == "result_version":
        return request.get(f"selected_{prefix}_result_version")
    if key == "failed_check_count":
        return request.get(f"selected_{prefix}_failed_check_count")
    return request.get(f"selected_{prefix}_{key}")


def _basis_summary(request: Mapping[str, Any], basis_field: str) -> dict[str, Any]:
    value = request.get(basis_field)
    if isinstance(value, Mapping):
        summary = _sanitize(value)
    else:
        summary = {"basis_value": _sanitize(value)}
    summary["basis_declared"] = _is_declared(value)
    prefix = BASIS_SHORTCUT_PREFIXES.get(basis_field)
    if prefix:
        for key in ("path", "outcome", "result_version", "failed_check_count"):
            if key == "path":
                shortcut_key = f"selected_{prefix}_result_path"
            elif key == "failed_check_count":
                shortcut_key = f"selected_{prefix}_failed_check_count"
            else:
                shortcut_key = f"selected_{prefix}_{key}"
            if shortcut_key in request:
                summary[key] = _sanitize(request.get(shortcut_key))
    if basis_field == "selected_post_portable_verification_currentness_basis":
        if "selected_post_portable_currentness_surface_path" in request:
            summary["path"] = _sanitize(request.get("selected_post_portable_currentness_surface_path"))
    return summary


def _posture_section(name: str, request: Mapping[str, Any]) -> dict[str, Any]:
    value = request.get(name)
    if isinstance(value, Mapping):
        section = _sanitize(value)
    else:
        section = {"declared_value": _sanitize(value)}
    section["declared"] = _is_declared(value)
    section["posture_only"] = True
    section["creates_runtime_daemon"] = False
    section["creates_runtime_loop"] = False
    section["creates_public_api"] = False
    section["creates_participant_facing_interface"] = False
    section["creates_distributed_network_behavior"] = False
    section["creates_source_authority_currentness_deployment_public_release_or_operation_permission"] = False
    section["authorizes_follow_on_work"] = False
    return section


def _declared_posture(name: str) -> dict[str, Any]:
    return {
        "posture_name": name,
        "declared": True,
        "posture_only": True,
        "creates_runtime_daemon": False,
        "creates_runtime_loop": False,
        "creates_public_api": False,
        "creates_participant_facing_interface": False,
        "creates_distributed_network_behavior": False,
        "creates_source_authority_currentness_deployment_public_release_or_operation_permission": False,
        "authorizes_follow_on_work": False,
    }


def _validate_declared_request(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    question = request.get("self_recursive_growth_question")
    _check(
        checks,
        "self-recursive-growth question declared",
        question == CORE_QUESTION,
        CORE_QUESTION,
        question,
        "SELF_RECURSIVE_GROWTH_QUESTION_UNDECLARED",
    )

    intent = request.get("self_recursive_growth_intent")
    _check(
        checks,
        "self-recursive-growth intent supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "SELF_RECURSIVE_GROWTH_INTENT_UNSUPPORTED",
    )
    _check(
        checks,
        "explicit self-recursive-growth block intent absent",
        intent != INTENT_BLOCK,
        f"intent not {INTENT_BLOCK}",
        intent,
        "SELF_RECURSIVE_GROWTH_EXPLICIT_BLOCK_REQUESTED",
    )

    scope = _scope_list(request.get("self_recursive_growth_scope"))
    unsupported_scope = [item for item in scope if item not in SUPPORTED_SCOPE_VALUES]
    _check(
        checks,
        "self-recursive-growth scope supported",
        not unsupported_scope and bool(scope),
        SUPPORTED_SCOPE_VALUES,
        scope,
        "UNSUPPORTED_SELF_RECURSIVE_GROWTH_SCOPE",
    )


def _validate_self_recursive_growth_boundary_basis(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> None:
    _check(
        checks,
        "self-recursive-growth-boundary basis declared",
        _is_declared(request.get("selected_self_recursive_growth_boundary_basis")),
        "declared selected self-recursive-growth-boundary basis",
        request.get("selected_self_recursive_growth_boundary_basis"),
        "SELF_RECURSIVE_GROWTH_BOUNDARY_BASIS_MISSING",
    )
    _check(
        checks,
        "self-recursive-growth-boundary terminal summary basis declared",
        _is_declared(request.get("selected_self_recursive_growth_boundary_terminal_summary_basis")),
        "declared selected self-recursive-growth-boundary terminal summary basis",
        request.get("selected_self_recursive_growth_boundary_terminal_summary_basis"),
        "SELF_RECURSIVE_GROWTH_BOUNDARY_TERMINAL_SUMMARY_BASIS_MISSING",
    )
    _check(
        checks,
        "self-recursive-growth-boundary outcome recorded",
        _basis_value(request, "selected_self_recursive_growth_boundary_basis", "outcome")
        == "POST_SELF_CONTINUATION_SELF_RECURSIVE_GROWTH_BOUNDARY_RECORDED",
        "POST_SELF_CONTINUATION_SELF_RECURSIVE_GROWTH_BOUNDARY_RECORDED",
        _basis_value(request, "selected_self_recursive_growth_boundary_basis", "outcome"),
        "SELF_RECURSIVE_GROWTH_BOUNDARY_NOT_RECORDED",
    )
    _check(
        checks,
        "self-recursive-growth-boundary version 0.1.0",
        _basis_value(request, "selected_self_recursive_growth_boundary_basis", "result_version") == "0.1.0",
        "0.1.0",
        _basis_value(request, "selected_self_recursive_growth_boundary_basis", "result_version"),
        "SELF_RECURSIVE_GROWTH_BOUNDARY_VERSION_NOT_0_1_0",
    )
    _check(
        checks,
        "self-recursive-growth-boundary failed checks zero",
        _safe_int(_basis_value(request, "selected_self_recursive_growth_boundary_basis", "failed_check_count")) == 0,
        0,
        _basis_value(request, "selected_self_recursive_growth_boundary_basis", "failed_check_count"),
        "SELF_RECURSIVE_GROWTH_BOUNDARY_FAILED_CHECKS_PRESENT",
    )
    _check(
        checks,
        "self-recursive-growth-boundary declared future review",
        _flag_true(request.get("selected_self_recursive_growth_boundary_declared_future_review")),
        True,
        request.get("selected_self_recursive_growth_boundary_declared_future_review"),
        "SELF_RECURSIVE_GROWTH_BOUNDARY_DID_NOT_DECLARE_FUTURE_SELF_RECURSIVE_GROWTH_REVIEW",
    )

    false_boundary_checks = (
        (
            "selected_self_recursive_growth_boundary_already_created_self_recursive_growth",
            "SELF_RECURSIVE_GROWTH_BOUNDARY_ALREADY_CREATED_SELF_RECURSIVE_GROWTH",
        ),
        (
            "selected_self_recursive_growth_boundary_already_created_runtime_daemon",
            "SELF_RECURSIVE_GROWTH_BOUNDARY_ALREADY_CREATED_RUNTIME_DAEMON",
        ),
        (
            "selected_self_recursive_growth_boundary_already_created_runtime_loop",
            "SELF_RECURSIVE_GROWTH_BOUNDARY_ALREADY_CREATED_RUNTIME_LOOP",
        ),
        (
            "selected_self_recursive_growth_boundary_already_created_public_api",
            "SELF_RECURSIVE_GROWTH_BOUNDARY_ALREADY_CREATED_PUBLIC_API",
        ),
        (
            "selected_self_recursive_growth_boundary_already_created_participant_facing_interface",
            "SELF_RECURSIVE_GROWTH_BOUNDARY_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE",
        ),
        (
            "selected_self_recursive_growth_boundary_already_created_distributed_network_behavior",
            "SELF_RECURSIVE_GROWTH_BOUNDARY_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR",
        ),
        (
            "selected_self_recursive_growth_boundary_treated_as_self_recursive_growth",
            "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_SELF_RECURSIVE_GROWTH",
        ),
        (
            "selected_self_recursive_growth_boundary_treated_as_runtime_daemon",
            "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_RUNTIME_DAEMON",
        ),
        (
            "selected_self_recursive_growth_boundary_treated_as_runtime_loop",
            "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_RUNTIME_LOOP",
        ),
        (
            "selected_self_recursive_growth_boundary_authorized_future_work",
            "SELF_RECURSIVE_GROWTH_BOUNDARY_AUTHORIZED_FUTURE_WORK",
        ),
    )
    for field, code in false_boundary_checks:
        _check(checks, field, request.get(field) is not True, False, request.get(field), code)

    _check(
        checks,
        "self-recursive-growth-boundary canonicalized result-level non-claims",
        _flag_true(request.get("selected_self_recursive_growth_boundary_non_claims_canonicalized")),
        True,
        request.get("selected_self_recursive_growth_boundary_non_claims_canonicalized"),
        "SELF_RECURSIVE_GROWTH_BOUNDARY_NON_CLAIMS_NOT_CANONICAL_FALSE",
    )
    _check(
        checks,
        "self-recursive-growth-boundary terminal summary states self-recursive growth not created",
        _flag_true(
            request.get(
                "selected_self_recursive_growth_boundary_terminal_summary_states_self_recursive_growth_not_created"
            )
        ),
        True,
        request.get("selected_self_recursive_growth_boundary_terminal_summary_states_self_recursive_growth_not_created"),
        "SELF_RECURSIVE_GROWTH_BOUNDARY_TERMINAL_SUMMARY_DID_NOT_PRESERVE_NO_SELF_RECURSIVE_GROWTH",
    )
    _check(
        checks,
        "self-recursive-growth-boundary terminal summary states no self-recursive growth selected",
        _flag_true(
            request.get(
                "selected_self_recursive_growth_boundary_terminal_summary_states_no_self_recursive_growth_selected"
            )
        ),
        True,
        request.get(
            "selected_self_recursive_growth_boundary_terminal_summary_states_no_self_recursive_growth_selected"
        ),
        "SELF_RECURSIVE_GROWTH_BOUNDARY_TERMINAL_SUMMARY_DID_NOT_PRESERVE_NO_SELF_RECURSIVE_GROWTH_SELECTED",
    )
    _check(
        checks,
        "self-recursive-growth-boundary terminal summary requires separate future review",
        _flag_true(request.get("selected_self_recursive_growth_boundary_terminal_summary_requires_separate_future_review")),
        True,
        request.get("selected_self_recursive_growth_boundary_terminal_summary_requires_separate_future_review"),
        "SELF_RECURSIVE_GROWTH_BOUNDARY_TERMINAL_SUMMARY_DID_NOT_REQUIRE_SEPARATE_REVIEW",
    )


def _validate_self_continuation_basis(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    _check(
        checks,
        "self-continuation basis declared",
        _is_declared(request.get("selected_self_continuation_basis")),
        "declared selected self-continuation basis",
        request.get("selected_self_continuation_basis"),
        "SELF_CONTINUATION_BASIS_MISSING",
    )
    _check(
        checks,
        "self-continuation terminal summary basis declared",
        _is_declared(request.get("selected_self_continuation_terminal_summary_basis")),
        "declared selected self-continuation terminal summary basis",
        request.get("selected_self_continuation_terminal_summary_basis"),
        "SELF_CONTINUATION_TERMINAL_SUMMARY_BASIS_MISSING",
    )
    _check(
        checks,
        "self-continuation outcome recorded",
        _basis_value(request, "selected_self_continuation_basis", "outcome")
        == "POST_CONTINUATION_SELF_CONTINUATION_RECORDED",
        "POST_CONTINUATION_SELF_CONTINUATION_RECORDED",
        _basis_value(request, "selected_self_continuation_basis", "outcome"),
        "SELF_CONTINUATION_NOT_RECORDED",
    )
    _check(
        checks,
        "self-continuation version 0.1.0",
        _basis_value(request, "selected_self_continuation_basis", "result_version") == "0.1.0",
        "0.1.0",
        _basis_value(request, "selected_self_continuation_basis", "result_version"),
        "SELF_CONTINUATION_VERSION_NOT_0_1_0",
    )
    _check(
        checks,
        "self-continuation failed checks zero",
        _safe_int(_basis_value(request, "selected_self_continuation_basis", "failed_check_count")) == 0,
        0,
        _basis_value(request, "selected_self_continuation_basis", "failed_check_count"),
        "SELF_CONTINUATION_FAILED_CHECKS_PRESENT",
    )
    _check(
        checks,
        "self-continuation recorded bounded self-continuation posture",
        _flag_true(request.get("selected_self_continuation_bounded_posture_recorded")),
        True,
        request.get("selected_self_continuation_bounded_posture_recorded"),
        "SELF_CONTINUATION_DID_NOT_RECORD_BOUNDED_SELF_CONTINUATION_POSTURE",
    )
    _check(
        checks,
        "self-continuation recorded bounded self-continuation envelope",
        _flag_true(request.get("selected_self_continuation_bounded_self_continuation_envelope_recorded")),
        True,
        request.get("selected_self_continuation_bounded_self_continuation_envelope_recorded"),
        "SELF_CONTINUATION_DID_NOT_RECORD_BOUNDED_SELF_CONTINUATION_ENVELOPE",
    )

    self_continuation_false_checks = (
        ("selected_self_continuation_already_created_runtime_daemon", "SELF_CONTINUATION_ALREADY_CREATED_RUNTIME_DAEMON"),
        ("selected_self_continuation_already_created_runtime_loop", "SELF_CONTINUATION_ALREADY_CREATED_RUNTIME_LOOP"),
        ("selected_self_continuation_already_created_public_api", "SELF_CONTINUATION_ALREADY_CREATED_PUBLIC_API"),
        (
            "selected_self_continuation_already_created_participant_facing_interface",
            "SELF_CONTINUATION_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE",
        ),
        (
            "selected_self_continuation_already_created_distributed_network_behavior",
            "SELF_CONTINUATION_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR",
        ),
        (
            "selected_bounded_self_continuation_envelope_treated_as_self_recursive_growth_before_review",
            "BOUNDED_SELF_CONTINUATION_ENVELOPE_TREATED_AS_SELF_RECURSIVE_GROWTH_BEFORE_REVIEW",
        ),
        (
            "selected_bounded_self_continuation_envelope_authorized_arbitrary_runtime_activity_before_review",
            "BOUNDED_SELF_CONTINUATION_ENVELOPE_AUTHORIZED_ARBITRARY_RUNTIME_ACTIVITY_BEFORE_REVIEW",
        ),
    )
    for field, code in self_continuation_false_checks:
        _check(checks, field, request.get(field) is not True, False, request.get(field), code)


def _validate_upstream_basis(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    for basis_field, _prefix, outcome, version, missing_code, outcome_code, version_code, failed_code in UPSTREAM_EXPECTATIONS:
        _check(
            checks,
            f"{basis_field} declared",
            _is_declared(request.get(basis_field)),
            "declared selected basis",
            request.get(basis_field),
            missing_code,
        )
        _check(
            checks,
            f"{basis_field} outcome recorded",
            _basis_value(request, basis_field, "outcome") == outcome,
            outcome,
            _basis_value(request, basis_field, "outcome"),
            outcome_code,
        )
        _check(
            checks,
            f"{basis_field} version {version}",
            _basis_value(request, basis_field, "result_version") == version,
            version,
            _basis_value(request, basis_field, "result_version"),
            version_code,
        )
        _check(
            checks,
            f"{basis_field} failed checks zero",
            _safe_int(_basis_value(request, basis_field, "failed_check_count")) == 0,
            0,
            _basis_value(request, basis_field, "failed_check_count"),
            failed_code,
        )


def _validate_lineage_and_currentness(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    _check(
        checks,
        "runtime-hosting-boundary v1 failure lineage basis declared",
        _is_declared(request.get("selected_runtime_hosting_boundary_v1_failure_lineage_basis")),
        "declared v1 failure lineage basis",
        request.get("selected_runtime_hosting_boundary_v1_failure_lineage_basis"),
        "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_LINEAGE_MISSING",
    )
    for field in (
        "selected_runtime_hosting_boundary_v1_failure_repaired",
        "selected_runtime_hosting_boundary_v1_failure_hidden",
        "selected_runtime_hosting_boundary_v1_failure_claimed_passed",
    ):
        _check(
            checks,
            field,
            request.get(field) is not True,
            False,
            request.get(field),
            "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
        )

    _check(
        checks,
        "post-portable currentness surface basis declared",
        _is_declared(request.get("selected_post_portable_verification_currentness_basis"))
        or _is_declared(request.get("selected_post_portable_currentness_surface_path")),
        "declared post-portable currentness surface basis",
        request.get("selected_post_portable_verification_currentness_basis")
        or request.get("selected_post_portable_currentness_surface_path"),
        "POST_PORTABLE_CURRENTNESS_SURFACE_BASIS_MISSING",
    )
    _check(
        checks,
        "post-portable currentness surface states checkability is not continuation",
        _flag_true(request.get("selected_post_portable_currentness_surface_states_checkability_not_continuation")),
        True,
        request.get("selected_post_portable_currentness_surface_states_checkability_not_continuation"),
        "POST_PORTABLE_CURRENTNESS_SURFACE_TREATED_CHECKABILITY_AS_CONTINUATION",
    )
    _check(
        checks,
        "post-portable currentness surface does not authorize next work",
        request.get("selected_post_portable_currentness_surface_authorized_next_work") is not True,
        False,
        request.get("selected_post_portable_currentness_surface_authorized_next_work"),
        "POST_PORTABLE_CURRENTNESS_SURFACE_AUTHORIZED_NEXT_WORK",
    )
    _check(
        checks,
        "returned second-carrier capture lineage basis declared",
        _is_declared(request.get("selected_returned_second_carrier_capture_lineage_basis")),
        "declared returned second-carrier capture lineage basis",
        request.get("selected_returned_second_carrier_capture_lineage_basis"),
        "RETURNED_SECOND_CARRIER_CAPTURE_LINEAGE_BASIS_MISSING",
    )
    _check(
        checks,
        "predecessor failure evidence remains visible and unrepaired",
        request.get("predecessor_failure_evidence_visible") is not False,
        "visible predecessor failure evidence",
        request.get("predecessor_failure_evidence_visible"),
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    )


def _validate_postures(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    for field in POSTURE_FIELDS:
        _check(
            checks,
            f"{field} declared",
            _is_declared(request.get(field)),
            "declared posture section",
            request.get(field),
            "SELF_RECURSIVE_GROWTH_REQUIRED_POSTURE_MISSING",
        )


def _validate_false_inputs(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    for field, code in FALSE_INPUT_CHECKS:
        _check(checks, field, request.get(field) is not True, False, request.get(field), code)

    _check(
        checks,
        "selected basis reference-shaped",
        request.get("reference_shaped_input_posture") is not False,
        True,
        request.get("reference_shaped_input_posture"),
        "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    )

    for field in (
        "runtime_hosting_boundary_v1_failure_repaired",
        "runtime_hosting_boundary_v1_failure_hidden",
        "runtime_hosting_boundary_v1_failure_claimed_passed",
    ):
        _check(
            checks,
            field,
            request.get(field) is not True,
            False,
            request.get(field),
            "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
        )


def _validate_declared_non_claims(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    declared = request.get("declared_non_claims")
    _check(
        checks,
        "declared non-claims mapping present",
        isinstance(declared, Mapping),
        "mapping with every required non-claim false",
        declared,
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    declared_mapping = declared if isinstance(declared, Mapping) else {}
    for key in REQUIRED_FALSE_NON_CLAIMS:
        _check(
            checks,
            f"declared non-claim {key} is false",
            key in declared_mapping and declared_mapping.get(key) is False,
            False,
            declared_mapping.get(key, None),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )


def _run_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    _validate_declared_request(request, checks)
    _validate_self_recursive_growth_boundary_basis(request, checks)
    _validate_self_continuation_basis(request, checks)
    _validate_upstream_basis(request, checks)
    _validate_lineage_and_currentness(request, checks)
    _validate_postures(request, checks)
    _validate_false_inputs(request, checks)
    _validate_declared_non_claims(request, checks)
    _check(
        checks,
        "official enum scope strings not redacted",
        all(item in SUPPORTED_SCOPE_VALUES for item in SUPPORTED_SCOPE_VALUES),
        "official scope strings preserved",
        SUPPORTED_SCOPE_VALUES,
        "OFFICIAL_ENUM_SCOPE_STRINGS_REDACTED",
    )
    _check(
        checks,
        "hostile raw body content contained",
        not _contains_hostile_sentinel(_sanitize(request)),
        "no hostile sentinel in emitted result",
        "contained" if not _contains_hostile_sentinel(_sanitize(request)) else "hostile sentinel present",
        "HOSTILE_RAW_BODY_CONTENT_NOT_CONTAINED",
    )
    return checks


def _determine_outcome(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> str:
    if _first_failed_code(checks):
        return OUTCOME_BLOCKED
    requested = request.get("requested_self_recursive_growth_outcome")
    if requested in (OUTCOME_NOT_RECORDED, OUTCOME_REQUIRES_ADDITIONAL_BASIS):
        return str(requested)
    if request.get("self_recursive_growth_intent") == INTENT_DO_NOT_RECORD:
        return OUTCOME_NOT_RECORDED
    return OUTCOME_RECORDED


def _statement_for_outcome(outcome: str) -> dict[str, bool]:
    recorded = outcome == OUTCOME_RECORDED
    return {
        "self_recursive_growth_recorded": recorded,
        "bounded_self_recursive_growth_posture_recorded": recorded,
        "self_recursive_growth_boundary_basis_preserved": recorded,
        "self_continuation_basis_preserved": recorded,
        "bounded_self_continuation_envelope_preserved": recorded,
        "bounded_self_recursive_growth_envelope_declared": recorded,
        "self_recursive_growth_not_daemon": True,
        "self_recursive_growth_not_loop": True,
        "self_recursive_growth_not_public_api": True,
        "self_recursive_growth_not_participant_facing_interface": True,
        "self_recursive_growth_not_distributed_network_behavior": True,
        "runtime_daemon_not_created": True,
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
        "hidden_repo_state_not_used_as_self_recursive_growth_authority": True,
        "repo_local_availability_not_self_recursive_growth_authority": True,
        "artifact_existence_not_self_recursive_growth_authority": True,
        "latest_file_posture_not_self_recursive_growth_authority": True,
        "selected_basis_reference_shape_preserved": True,
        "raw_full_prior_artifact_body_not_returned": True,
        "official_enum_scope_strings_not_redacted": True,
        "hostile_raw_body_content_contained": True,
        "predecessor_failure_evidence_preserved": True,
        "authorization_token_reuse_blocked": True,
        "consumed_request_token_remains_closed": True,
        "result_level_non_claims_canonical_false": True,
    }


def _non_meaning() -> dict[str, bool]:
    return {
        "self_recursive_growth_is_runtime_daemon": False,
        "self_recursive_growth_is_runtime_loop": False,
        "self_recursive_growth_is_public_api": False,
        "self_recursive_growth_is_participant_facing_interface": False,
        "self_recursive_growth_is_distributed_network_behavior": False,
        "self_recursive_growth_is_source_transfer": False,
        "self_recursive_growth_is_source_receipt": False,
        "self_recursive_growth_is_reception_authorization": False,
        "self_recursive_growth_is_source": False,
        "self_recursive_growth_is_authority": False,
        "self_recursive_growth_is_currentness": False,
        "self_recursive_growth_is_deployment": False,
        "self_recursive_growth_is_public_release": False,
        "self_recursive_growth_is_operation_permission": False,
        "self_recursive_growth_is_broader_reusable_permission": False,
        "self_recursive_growth_is_derivative_reception": False,
        "self_recursive_growth_is_vessel_relation": False,
        "self_recursive_growth_is_adoption": False,
        "self_recursive_growth_is_receiving_context_governance": False,
        "self_recursive_growth_is_publication_flow": False,
        "self_recursive_growth_is_follow_on_work": False,
        "self_recursive_growth_authorizes_arbitrary_runtime_activity": False,
        "self_recursive_growth_authorizes_its_own_successor": False,
    }


def _default_bounded_envelope(recorded: bool) -> dict[str, Any]:
    return {
        "declared": recorded,
        "envelope_type": "bounded_self_recursive_growth_envelope",
        "envelope_name": "one_bounded_post_self_continuation_self_recursive_growth_envelope",
        "posture": (
            "one bounded self-recursive-growth posture from selected clean "
            "self-recursive-growth-boundary and self-continuation basis"
        ),
        "self_recursive_growth_limited_to_declared_envelope": recorded,
        "self_continuation_basis_preserved": True,
        "bounded_self_continuation_envelope_preserved": True,
        "authorizes_arbitrary_runtime_activity": False,
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
        "authorizes_follow_on_work": False,
        "anything_outside_envelope_requires_fresh_admission": True,
    }


def _bounded_envelope(request: Mapping[str, Any], outcome: str) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    envelope = request.get("requested_bounded_self_recursive_growth_envelope")
    if isinstance(envelope, Mapping):
        result = _sanitize(envelope)
        result.setdefault("declared", recorded)
        result.setdefault("envelope_type", "bounded_self_recursive_growth_envelope")
        result.setdefault("authorizes_arbitrary_runtime_activity", False)
        result.setdefault("creates_runtime_daemon", False)
        result.setdefault("creates_runtime_loop", False)
        result.setdefault("creates_public_api", False)
        result.setdefault("creates_participant_facing_interface", False)
        result.setdefault("creates_distributed_network_behavior", False)
        result.setdefault("authorizes_follow_on_work", False)
        result.setdefault("anything_outside_envelope_requires_fresh_admission", True)
        return result
    return _default_bounded_envelope(recorded)


def _additional_basis_required(outcome: str, request: Mapping[str, Any]) -> list[Any]:
    if outcome != OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        return []
    value = request.get("additional_basis_context")
    if isinstance(value, list):
        return _sanitize(value)
    if _is_declared(value):
        return [_sanitize(value)]
    return ["additional bounded self-recursive-growth basis required before recording"]


def _not_recorded_basis(outcome: str, request: Mapping[str, Any]) -> list[Any]:
    if outcome != OUTCOME_NOT_RECORDED:
        return []
    value = request.get("not_recorded_basis")
    if isinstance(value, list):
        return _sanitize(value)
    if _is_declared(value):
        return [_sanitize(value)]
    return ["self-recursive growth not recorded by declared request posture"]


def _what_remains_open() -> list[str]:
    return [
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


def _block_for_outcome(
    outcome: str, checks: list[dict[str, Any]], request: Mapping[str, Any]
) -> dict[str, Any] | None:
    if outcome != OUTCOME_BLOCKED:
        return None
    code = _first_failed_code(checks) or "DECLARED_SELF_RECURSIVE_GROWTH_REQUEST_MALFORMED"
    return {
        "block_code": code,
        "block_reason": _sanitize(request.get("block_reason") or code),
        "preserves_prior_artifacts": True,
        "creates_runtime_daemon_loop_api_interface_or_distributed_network": False,
        "authorizes_follow_on_work": False,
    }


def _build_metadata(request: Mapping[str, Any]) -> dict[str, Any]:
    request_id = request.get("self_recursive_growth_request_id") or DEFAULT_REQUEST_ID
    return {
        "post_self_continuation_self_recursive_growth_id": request_id,
        "post_self_continuation_self_recursive_growth_type": "post_self_continuation_self_recursive_growth",
        "post_self_continuation_self_recursive_growth_version": RESULT_VERSION,
        "generated_at": _now_iso(),
        "resolver_module": RESOLVER_MODULE,
    }


def _build_result(request: Mapping[str, Any], checks: list[dict[str, Any]], outcome: str) -> dict[str, Any]:
    result: dict[str, Any] = {
        "post_self_continuation_self_recursive_growth_metadata": _build_metadata(request),
        "declared_self_recursive_growth_question": {
            "self_recursive_growth_request_id": request.get("self_recursive_growth_request_id") or DEFAULT_REQUEST_ID,
            "question": _sanitize(request.get("self_recursive_growth_question")),
            "intent": _sanitize(request.get("self_recursive_growth_intent")),
        },
        "self_recursive_growth_scope": _scope_list(request.get("self_recursive_growth_scope")),
        "self_recursive_growth_checks": checks,
        "self_recursive_growth_statement": _statement_for_outcome(outcome),
        "self_recursive_growth_non_meaning": _non_meaning(),
        "bounded_self_recursive_growth_envelope": _bounded_envelope(request, outcome),
        "additional_basis_required": _additional_basis_required(outcome, request),
        "not_recorded_basis": _not_recorded_basis(outcome, request),
        "what_remains_open": _what_remains_open(),
        "non_claims": _canonical_false_non_claims(),
        "outcome": outcome,
        "block": _block_for_outcome(outcome, checks, request),
    }
    for field in SELECTED_BASIS_FIELDS:
        result[field] = _basis_summary(request, field)
    for field in POSTURE_FIELDS:
        result[field] = _posture_section(field, request)
    result["post_self_continuation_self_recursive_growth_summary"] = (
        build_post_self_continuation_self_recursive_growth_summary(result)
    )
    return _sanitize(result)


def _malformed_result(code: str, reason: str, actual: Any = None) -> dict[str, Any]:
    request = build_declared_post_self_continuation_self_recursive_growth_request(
        self_recursive_growth_request_id="malformed_post_self_continuation_self_recursive_growth_request",
        block_reason=reason,
    )
    checks: list[dict[str, Any]] = []
    _check(checks, reason, False, "declared self-recursive-growth request mapping", actual, code)
    return _build_result(request, checks, OUTCOME_BLOCKED)


def resolve_post_self_continuation_self_recursive_growth(
    declared_self_recursive_growth_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one declared bounded self-recursive-growth request."""

    if declared_self_recursive_growth_request is None:
        return _malformed_result(
            "DECLARED_SELF_RECURSIVE_GROWTH_REQUEST_MALFORMED",
            "declared self-recursive-growth request missing",
            None,
        )
    if not isinstance(declared_self_recursive_growth_request, Mapping):
        return _malformed_result(
            "DECLARED_SELF_RECURSIVE_GROWTH_REQUEST_MALFORMED",
            "declared self-recursive-growth request is not a mapping",
            declared_self_recursive_growth_request,
        )

    request = deepcopy(dict(declared_self_recursive_growth_request))
    checks = _run_checks(request)
    outcome = _determine_outcome(request, checks)
    return _build_result(request, checks, outcome)


def resolve_post_self_continuation_self_recursive_growth_from_path(
    declared_self_recursive_growth_request_path: Path | str,
) -> dict:
    """Load a declared request JSON file and resolve it without mutating it."""

    path = Path(declared_self_recursive_growth_request_path)
    try:
        with path.open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except json.JSONDecodeError as exc:
        return _malformed_result(
            "DECLARED_SELF_RECURSIVE_GROWTH_REQUEST_MALFORMED",
            "declared self-recursive-growth request JSON malformed",
            str(exc),
        )
    except OSError as exc:
        return _malformed_result(
            "DECLARED_SELF_RECURSIVE_GROWTH_REQUEST_UNREADABLE",
            "declared self-recursive-growth request path unreadable",
            str(exc),
        )
    if not isinstance(loaded, Mapping):
        return _malformed_result(
            "DECLARED_SELF_RECURSIVE_GROWTH_REQUEST_MALFORMED",
            "declared self-recursive-growth request JSON is not an object",
            loaded,
        )
    return resolve_post_self_continuation_self_recursive_growth(loaded)


def _summary_basis(result: Mapping[str, Any], section: str, key: str) -> Any:
    value = result.get(section)
    if isinstance(value, Mapping):
        return value.get(key)
    return None


def build_post_self_continuation_self_recursive_growth_summary(result: Mapping[str, Any]) -> dict:
    """Build a compact JSON-safe summary for a resolver result."""

    checks = result.get("self_recursive_growth_checks", [])
    check_list = list(checks) if isinstance(checks, list) else []
    passed = sum(1 for check in check_list if isinstance(check, Mapping) and check.get("passed") is True)
    failed = sum(1 for check in check_list if isinstance(check, Mapping) and check.get("passed") is False)
    metadata = result.get("post_self_continuation_self_recursive_growth_metadata", {})
    question = result.get("declared_self_recursive_growth_question", {})
    statement = result.get("self_recursive_growth_statement", {})
    block = result.get("block")
    envelope = result.get("bounded_self_recursive_growth_envelope", {})

    summary: dict[str, Any] = {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") if isinstance(block, Mapping) else None,
        "block_reason": block.get("block_reason") if isinstance(block, Mapping) else None,
        "request_id": metadata.get("post_self_continuation_self_recursive_growth_id")
        if isinstance(metadata, Mapping)
        else None,
        "question": question.get("question") if isinstance(question, Mapping) else None,
        "intent": question.get("intent") if isinstance(question, Mapping) else None,
        "passed_check_count": passed,
        "failed_check_count": failed,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "bounded_self_recursive_growth_envelope_posture": _sanitize(envelope),
        "key_non_claims": result.get("non_claims", {}),
        "predecessor_failure_evidence_preserved": statement.get("predecessor_failure_evidence_preserved"),
        "consumed_request_token_remains_closed": statement.get("consumed_request_token_remains_closed"),
        "authorization_token_reuse_blocked": statement.get("authorization_token_reuse_blocked"),
        "no_daemon_loop_api_interface_distributed_network_source_authority_currentness_deployment_public_release_follow_on": (
            statement.get("runtime_daemon_not_created") is True
            and statement.get("runtime_loop_not_created") is True
            and statement.get("public_api_not_created") is True
            and statement.get("participant_facing_interface_not_created") is True
            and statement.get("distributed_network_behavior_not_created") is True
            and statement.get("source_not_created") is True
            and statement.get("authority_not_created") is True
            and statement.get("currentness_not_created") is True
            and statement.get("deployment_not_created") is True
            and statement.get("public_release_not_created") is True
            and statement.get("follow_on_work_not_authorized") is True
        ),
    }
    for key in ALLOWED_TRUE_RECORDED_FIELDS:
        summary[key] = statement.get(key)

    basis_sections = (
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
    )
    for prefix, section in basis_sections:
        summary[f"{prefix}_outcome"] = _summary_basis(result, section, "outcome")
        summary[f"{prefix}_result_version"] = _summary_basis(result, section, "result_version")
        summary[f"{prefix}_failed_check_count"] = _summary_basis(result, section, "failed_check_count")
    summary["selected_post_portable_currentness_surface_path"] = _summary_basis(
        result, "selected_post_portable_verification_currentness_basis", "path"
    )
    return _sanitize(summary)


def _non_overwriting_path(path: Path) -> Path:
    if not path.exists():
        return path
    suffix = path.suffix
    stem = path.stem
    parent = path.parent
    for index in range(1, 10000):
        candidate = parent / f"{stem}_{index:03d}{suffix}"
        if not candidate.exists():
            return candidate
    raise PostSelfContinuationSelfRecursiveGrowthError("could not find non-overwriting output path")


def write_post_self_continuation_self_recursive_growth_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write a resolver result as stable UTF-8 JSON without overwriting."""

    if output_path is None:
        metadata = result.get("post_self_continuation_self_recursive_growth_metadata", {})
        request_id = DEFAULT_REQUEST_ID
        if isinstance(metadata, Mapping):
            request_id = str(metadata.get("post_self_continuation_self_recursive_growth_id") or request_id)
        target = OUTPUT_ROOT / f"{request_id}__post_self_continuation_self_recursive_growth_result.json"
    else:
        supplied = Path(output_path)
        if supplied.suffix:
            target = supplied
        else:
            metadata = result.get("post_self_continuation_self_recursive_growth_metadata", {})
            request_id = DEFAULT_REQUEST_ID
            if isinstance(metadata, Mapping):
                request_id = str(metadata.get("post_self_continuation_self_recursive_growth_id") or request_id)
            target = supplied / f"{request_id}__post_self_continuation_self_recursive_growth_result.json"

    target = _non_overwriting_path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8") as handle:
        json.dump(_sanitize(dict(result)), handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
    return target


def _basis(name: str, outcome: str, version: str, path: str, failed_check_count: int = 0) -> dict[str, Any]:
    return {
        "basis_type": name,
        "reference_shape": True,
        "path": path,
        "outcome": outcome,
        "result_version": version,
        "failed_check_count": failed_check_count,
    }


def _default_request_envelope() -> dict[str, Any]:
    return _default_bounded_envelope(True)


def build_declared_post_self_continuation_self_recursive_growth_request(**overrides: Any) -> dict[str, Any]:
    """Build a small valid declared request for the bounded resolver."""

    request: dict[str, Any] = {
        "self_recursive_growth_request_id": DEFAULT_REQUEST_ID,
        "self_recursive_growth_question": CORE_QUESTION,
        "self_recursive_growth_intent": INTENT_RECORD,
        "self_recursive_growth_scope": list(SUPPORTED_SCOPE_VALUES),
        "selected_self_recursive_growth_boundary_basis": _basis(
            "post_self_continuation_self_recursive_growth_boundary",
            "POST_SELF_CONTINUATION_SELF_RECURSIVE_GROWTH_BOUNDARY_RECORDED",
            "0.1.0",
            "artifacts/integrity_host_v0_min_coexistence_post_self_continuation_self_recursive_growth_boundary/"
            "post_self_continuation_self_recursive_growth_boundary_reference_review_001__"
            "post_self_continuation_self_recursive_growth_boundary_result.json",
        ),
        "selected_self_recursive_growth_boundary_terminal_summary_basis": {
            "basis_type": "post_self_continuation_self_recursive_growth_boundary_terminal_summary",
            "reference_shape": True,
            "path": "spec/POST_SELF_CONTINUATION_SELF_RECURSIVE_GROWTH_BOUNDARY_TERMINAL_SUMMARY_V0.md",
            "states_self_recursive_growth_not_created": True,
            "states_no_self_recursive_growth_selected": True,
            "requires_separate_future_review": True,
        },
        "selected_self_continuation_basis": _basis(
            "post_continuation_self_continuation",
            "POST_CONTINUATION_SELF_CONTINUATION_RECORDED",
            "0.1.0",
            "artifacts/integrity_host_v0_min_coexistence_post_continuation_self_continuation/"
            "post_continuation_self_continuation_reference_review_001__"
            "post_continuation_self_continuation_result.json",
        ),
        "selected_self_continuation_terminal_summary_basis": {
            "basis_type": "post_continuation_self_continuation_terminal_summary",
            "reference_shape": True,
            "path": "spec/POST_CONTINUATION_SELF_CONTINUATION_TERMINAL_SUMMARY_V0.md",
        },
        "selected_self_continuation_boundary_basis": _basis(
            "post_continuation_self_continuation_boundary",
            "POST_CONTINUATION_SELF_CONTINUATION_BOUNDARY_RECORDED",
            "0.1.0",
            "artifacts/integrity_host_v0_min_coexistence_post_continuation_self_continuation_boundary/"
            "post_continuation_self_continuation_boundary_reference_review_001__"
            "post_continuation_self_continuation_boundary_result.json",
        ),
        "selected_continuation_basis": _basis(
            "post_reusable_runtime_permission_continuation",
            "POST_REUSABLE_RUNTIME_PERMISSION_CONTINUATION_RECORDED",
            "0.1.0",
            "artifacts/integrity_host_v0_min_coexistence_post_reusable_runtime_permission_continuation/"
            "post_reusable_runtime_permission_continuation_reference_review_001__"
            "post_reusable_runtime_permission_continuation_result.json",
        ),
        "selected_continuation_boundary_basis": _basis(
            "post_reusable_runtime_permission_continuation_boundary",
            "POST_REUSABLE_RUNTIME_PERMISSION_CONTINUATION_BOUNDARY_RECORDED",
            "0.1.0",
            "artifacts/integrity_host_v0_min_coexistence_post_reusable_runtime_permission_continuation_boundary/"
            "post_reusable_runtime_permission_continuation_boundary_reference_review_001__"
            "post_reusable_runtime_permission_continuation_boundary_result.json",
        ),
        "selected_reusable_runtime_permission_basis": _basis(
            "post_ongoing_runtime_reusable_runtime_permission",
            "POST_ONGOING_RUNTIME_REUSABLE_RUNTIME_PERMISSION_RECORDED",
            "0.1.0",
            "artifacts/integrity_host_v0_min_coexistence_post_ongoing_runtime_reusable_runtime_permission/"
            "post_ongoing_runtime_reusable_runtime_permission_reference_review_001__"
            "post_ongoing_runtime_reusable_runtime_permission_result.json",
        ),
        "selected_reusable_runtime_permission_boundary_basis": _basis(
            "post_ongoing_runtime_reusable_runtime_permission_boundary",
            "POST_ONGOING_RUNTIME_REUSABLE_RUNTIME_PERMISSION_BOUNDARY_RECORDED",
            "0.1.0",
            "artifacts/integrity_host_v0_min_coexistence_post_ongoing_runtime_reusable_runtime_permission_boundary/"
            "post_ongoing_runtime_reusable_runtime_permission_boundary_reference_review_001__"
            "post_ongoing_runtime_reusable_runtime_permission_boundary_result.json",
        ),
        "selected_ongoing_runtime_basis": _basis(
            "post_runtime_hosting_ongoing_runtime",
            "POST_RUNTIME_HOSTING_ONGOING_RUNTIME_RECORDED",
            "0.1.0",
            "artifacts/integrity_host_v0_min_coexistence_post_runtime_hosting_ongoing_runtime/"
            "post_runtime_hosting_ongoing_runtime_reference_review_001__"
            "post_runtime_hosting_ongoing_runtime_result.json",
        ),
        "selected_runtime_hosting_basis": _basis(
            "post_successor_runtime_step_runtime_hosting",
            "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_RECORDED",
            "0.1.0",
            "artifacts/integrity_host_v0_min_coexistence_post_successor_runtime_step_runtime_hosting/"
            "post_successor_runtime_step_runtime_hosting_reference_review_001__"
            "post_successor_runtime_step_runtime_hosting_result.json",
        ),
        "selected_runtime_hosting_boundary_v2_basis": _basis(
            "post_successor_runtime_step_runtime_hosting_boundary_v2",
            "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_BOUNDARY_RECORDED",
            "0.2.0",
            "artifacts/integrity_host_v0_min_coexistence_post_successor_runtime_step_runtime_hosting_boundary_v2/"
            "post_successor_runtime_step_runtime_hosting_boundary_v2_reference_review_001__"
            "post_successor_runtime_step_runtime_hosting_boundary_v2_result.json",
        ),
        "selected_runtime_hosting_boundary_v1_failure_lineage_basis": {
            "basis_type": "post_successor_runtime_step_runtime_hosting_boundary_v1_failure_lineage",
            "reference_shape": True,
            "preserved_as_failure_evidence": True,
            "repaired": False,
            "hidden": False,
            "claimed_passed": False,
            "resolver_path": "src/resolve_post_successor_runtime_step_runtime_hosting_boundary.py",
            "test_path": "tests/test_resolve_post_successor_runtime_step_runtime_hosting_boundary.py",
        },
        "selected_successor_runtime_step_basis": _basis(
            "post_minimal_runtime_successor_runtime_step",
            "POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_RECORDED",
            "0.1.0",
            "artifacts/integrity_host_v0_min_coexistence_post_minimal_runtime_successor_runtime_step/"
            "post_minimal_runtime_successor_runtime_step_reference_review_001__"
            "post_minimal_runtime_successor_runtime_step_result.json",
        ),
        "selected_minimal_runtime_basis": _basis(
            "post_portable_verification_minimal_runtime",
            "POST_PORTABLE_VERIFICATION_MINIMAL_RUNTIME_RECORDED",
            "0.1.0",
            "artifacts/integrity_host_v0_min_coexistence_post_portable_verification_minimal_runtime/"
            "post_portable_verification_minimal_runtime_reference_review_001__"
            "post_portable_verification_minimal_runtime_result.json",
        ),
        "selected_runtime_boundary_basis": _basis(
            "post_portable_verification_runtime_boundary",
            "POST_PORTABLE_VERIFICATION_RUNTIME_BOUNDARY_RECORDED",
            "0.1.0",
            "artifacts/integrity_host_v0_min_coexistence_post_portable_verification_runtime_boundary/"
            "post_portable_verification_runtime_boundary_reference_review_001__"
            "post_portable_verification_runtime_boundary_result.json",
        ),
        "selected_runtime_readiness_basis": _basis(
            "post_portable_verification_runtime_readiness",
            "POST_PORTABLE_VERIFICATION_RUNTIME_READINESS_RECORDED",
            "0.1.0",
            "artifacts/integrity_host_v0_min_coexistence_post_portable_verification_runtime_readiness/"
            "post_portable_verification_runtime_readiness_reference_review_001__"
            "post_portable_verification_runtime_readiness_result.json",
        ),
        "selected_portable_verification_final_completion_basis": _basis(
            "portable_source_body_verification_final_completion",
            "PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_RECORDED",
            "0.1.0",
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_final_completion/"
            "portable_source_body_verification_final_completion_reference_review_001__"
            "portable_source_body_verification_final_completion_result.json",
        ),
        "selected_post_portable_verification_currentness_basis": {
            "basis_type": "post_portable_verification_currentness_surface",
            "reference_shape": True,
            "path": "spec/POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_V0.md",
            "states_checkability_not_continuation": True,
            "authorizes_next_work": False,
        },
        "selected_returned_second_carrier_capture_lineage_basis": {
            "basis_type": "returned_second_carrier_capture_lineage",
            "reference_shape": True,
            "lineage_only": True,
        },
        "selected_self_recursive_growth_boundary_result_outcome": "POST_SELF_CONTINUATION_SELF_RECURSIVE_GROWTH_BOUNDARY_RECORDED",
        "selected_self_recursive_growth_boundary_result_version": "0.1.0",
        "selected_self_recursive_growth_boundary_failed_check_count": 0,
        "selected_self_recursive_growth_boundary_declared_future_review": True,
        "selected_self_recursive_growth_boundary_non_claims_canonicalized": True,
        "selected_self_recursive_growth_boundary_terminal_summary_states_self_recursive_growth_not_created": True,
        "selected_self_recursive_growth_boundary_terminal_summary_states_no_self_recursive_growth_selected": True,
        "selected_self_recursive_growth_boundary_terminal_summary_requires_separate_future_review": True,
        "selected_self_continuation_result_outcome": "POST_CONTINUATION_SELF_CONTINUATION_RECORDED",
        "selected_self_continuation_result_version": "0.1.0",
        "selected_self_continuation_failed_check_count": 0,
        "selected_self_continuation_bounded_posture_recorded": True,
        "selected_self_continuation_bounded_self_continuation_envelope_recorded": True,
        "selected_post_portable_currentness_surface_path": "spec/POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_V0.md",
        "selected_post_portable_currentness_surface_states_checkability_not_continuation": True,
        "selected_post_portable_currentness_surface_authorized_next_work": False,
        "predecessor_failure_evidence_visible": True,
        "reference_shaped_input_posture": True,
        "requested_bounded_self_recursive_growth_envelope": _default_request_envelope(),
        "declared_non_claims": _canonical_false_non_claims(),
    }

    for field in POSTURE_FIELDS:
        request[field] = _declared_posture(field)
    for field, _code in FALSE_INPUT_CHECKS:
        request.setdefault(field, False)
    for field in (
        "selected_self_recursive_growth_boundary_already_created_self_recursive_growth",
        "selected_self_recursive_growth_boundary_already_created_runtime_daemon",
        "selected_self_recursive_growth_boundary_already_created_runtime_loop",
        "selected_self_recursive_growth_boundary_already_created_public_api",
        "selected_self_recursive_growth_boundary_already_created_participant_facing_interface",
        "selected_self_recursive_growth_boundary_already_created_distributed_network_behavior",
        "selected_self_recursive_growth_boundary_treated_as_self_recursive_growth",
        "selected_self_recursive_growth_boundary_treated_as_runtime_daemon",
        "selected_self_recursive_growth_boundary_treated_as_runtime_loop",
        "selected_self_recursive_growth_boundary_authorized_future_work",
        "selected_self_continuation_already_created_runtime_daemon",
        "selected_self_continuation_already_created_runtime_loop",
        "selected_self_continuation_already_created_public_api",
        "selected_self_continuation_already_created_participant_facing_interface",
        "selected_self_continuation_already_created_distributed_network_behavior",
        "selected_bounded_self_continuation_envelope_treated_as_self_recursive_growth_before_review",
        "selected_bounded_self_continuation_envelope_authorized_arbitrary_runtime_activity_before_review",
        "selected_runtime_hosting_boundary_v1_failure_repaired",
        "selected_runtime_hosting_boundary_v1_failure_hidden",
        "selected_runtime_hosting_boundary_v1_failure_claimed_passed",
        "runtime_hosting_boundary_v1_failure_repaired",
        "runtime_hosting_boundary_v1_failure_hidden",
        "runtime_hosting_boundary_v1_failure_claimed_passed",
    ):
        request.setdefault(field, False)

    for basis_field, prefix in BASIS_SHORTCUT_PREFIXES.items():
        basis = request.get(basis_field)
        if isinstance(basis, Mapping):
            request.setdefault(f"selected_{prefix}_result_path", basis.get("path"))
            request.setdefault(f"selected_{prefix}_result_outcome", basis.get("outcome"))
            request.setdefault(f"selected_{prefix}_result_version", basis.get("result_version"))
            request.setdefault(f"selected_{prefix}_failed_check_count", basis.get("failed_check_count"))

    request.update(overrides)
    return deepcopy(request)
