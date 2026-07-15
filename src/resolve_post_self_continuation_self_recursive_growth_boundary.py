"""Resolve one bounded post-self-continuation self-recursive-growth boundary.

This module is downstream of post-continuation self-continuation. It records
one bounded self-recursive-growth-boundary posture only: one future
self-recursive-growth review may later be approached from clean
self-continuation basis. It does not create self-recursive growth, daemon or
loop behavior, public API, participant-facing interface, distributed network
behavior, source transfer, source receipt, reception authorization, source,
authority, currentness, deployment, public release, operation permission,
broader reusable permission, adoption, receiving-context governance,
publication flow, or follow-on work.
"""

from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any


class PostSelfContinuationSelfRecursiveGrowthBoundaryError(Exception):
    """Bounded resolver error for unreadable or malformed request inputs."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_post_self_continuation_self_recursive_growth_boundary"

OUTCOME_RECORDED = "POST_SELF_CONTINUATION_SELF_RECURSIVE_GROWTH_BOUNDARY_RECORDED"
OUTCOME_NOT_RECORDED = "POST_SELF_CONTINUATION_SELF_RECURSIVE_GROWTH_BOUNDARY_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "POST_SELF_CONTINUATION_SELF_RECURSIVE_GROWTH_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "POST_SELF_CONTINUATION_SELF_RECURSIVE_GROWTH_BOUNDARY_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = "RECORD_POST_SELF_CONTINUATION_SELF_RECURSIVE_GROWTH_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_POST_SELF_CONTINUATION_SELF_RECURSIVE_GROWTH_BOUNDARY"
INTENT_BLOCK = "BLOCK_POST_SELF_CONTINUATION_SELF_RECURSIVE_GROWTH_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = (
    PROJECT_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_post_self_continuation_self_recursive_growth_boundary"
)

CORE_QUESTION = (
    "Can the clean post-self-continuation basis be bounded for one future "
    "self-recursive-growth review without creating self-recursive growth, runtime daemon, "
    "runtime loop, public API, participant-facing interface, distributed network behavior, "
    "source transfer, source receipt, reception authorization, source, authority, "
    "currentness, deployment, public release, operation permission, broader reusable "
    "permission, derivative reception, vessel relation, another reception request, "
    "adoption, receiving-context governance, publication flow, or follow-on work?"
)

SUPPORTED_SCOPE_VALUES = (
    "SELF_RECURSIVE_GROWTH_BOUNDARY_SPEC_ONLY",
    "ONE_FUTURE_SELF_RECURSIVE_GROWTH_REVIEW_DECLARED",
    "SELF_CONTINUATION_BASIS_PRESERVED",
    "SELF_CONTINUATION_NOT_SELF_RECURSIVE_GROWTH",
    "BOUNDED_SELF_CONTINUATION_ENVELOPE_NOT_SELF_RECURSIVE_GROWTH",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_NOT_SELF_RECURSIVE_GROWTH",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_NOT_DAEMON",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_NOT_LOOP",
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
    "NO_BROADER_REUSABLE_PERMISSION",
    "NO_DERIVATIVE_RECEPTION",
    "NO_VESSEL_RELATION",
    "NO_ANOTHER_RECEPTION_REQUEST",
    "NO_ADOPTION",
    "NO_RECEIVING_CONTEXT_GOVERNANCE",
    "NO_PUBLICATION_FLOW",
    "NO_FOLLOW_ON_WORK_AUTHORIZED",
    "NO_SELF_RECURSIVE_GROWTH_INFERENCE",
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
    "HIDDEN_REPO_STATE_NOT_USED_AS_SELF_RECURSIVE_GROWTH_BOUNDARY_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_NOT_SELF_RECURSIVE_GROWTH_BOUNDARY_AUTHORITY",
    "ARTIFACT_EXISTENCE_NOT_SELF_RECURSIVE_GROWTH_BOUNDARY_AUTHORITY",
    "LATEST_FILE_POSTURE_NOT_SELF_RECURSIVE_GROWTH_BOUNDARY_AUTHORITY",
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
SUPPORTED_SELF_RECURSIVE_GROWTH_BOUNDARY_SCOPE = SUPPORTED_SCOPE_VALUES

ALLOWED_TRUE_RECORDED_FIELDS = (
    "self_recursive_growth_boundary_recorded",
    "one_future_self_recursive_growth_review_declared",
    "self_continuation_basis_preserved",
    "self_continuation_not_self_recursive_growth",
    "bounded_self_continuation_envelope_not_self_recursive_growth",
    "self_recursive_growth_boundary_not_self_recursive_growth",
    "self_recursive_growth_boundary_not_daemon",
    "self_recursive_growth_boundary_not_loop",
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
    "broader_reusable_permission_not_created",
    "follow_on_work_not_authorized",
    "hidden_repo_state_excluded",
    "hidden_repo_state_not_used_as_self_recursive_growth_boundary_authority",
    "repo_local_availability_not_self_recursive_growth_boundary_authority",
    "artifact_existence_not_self_recursive_growth_boundary_authority",
    "latest_file_posture_not_self_recursive_growth_boundary_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "official_enum_scope_strings_not_redacted",
    "hostile_raw_body_content_contained",
    "predecessor_failure_evidence_preserved",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
    "result_level_non_claims_canonical_false",
)

REQUIRED_FALSE_NON_CLAIMS = (
    "self_recursive_growth_created",
    "runtime_daemon_created",
    "runtime_loop_created",
    "public_api_created",
    "participant_facing_interface_created",
    "distributed_network_behavior_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "self_recursive_growth_boundary_treated_as_self_recursive_growth",
    "self_recursive_growth_boundary_treated_as_runtime_daemon",
    "self_recursive_growth_boundary_treated_as_runtime_loop",
    "self_recursive_growth_boundary_treated_as_source_transfer",
    "self_recursive_growth_boundary_treated_as_source_receipt",
    "self_recursive_growth_boundary_treated_as_reception_authorization",
    "self_recursive_growth_boundary_treated_as_source",
    "self_recursive_growth_boundary_treated_as_authority",
    "self_recursive_growth_boundary_treated_as_currentness",
    "self_recursive_growth_boundary_treated_as_deployment",
    "self_recursive_growth_boundary_treated_as_public_release",
    "self_recursive_growth_boundary_treated_as_operation_permission",
    "self_recursive_growth_boundary_treated_as_broader_reusable_permission",
    "self_recursive_growth_boundary_treated_as_follow_on_work",
    "self_continuation_treated_as_self_recursive_growth",
    "self_continuation_treated_as_runtime_daemon",
    "self_continuation_treated_as_runtime_loop",
    "self_continuation_treated_as_public_api",
    "self_continuation_treated_as_participant_facing_interface",
    "self_continuation_treated_as_distributed_network_behavior",
    "bounded_self_continuation_envelope_treated_as_self_recursive_growth",
    "bounded_self_continuation_envelope_authorized_self_recursive_growth",
    "bounded_self_continuation_envelope_authorized_runtime_daemon",
    "bounded_self_continuation_envelope_authorized_runtime_loop",
    "bounded_self_continuation_envelope_authorized_arbitrary_runtime_activity",
    "artifact_existence_treated_as_self_recursive_growth_boundary_authority",
    "artifact_path_treated_as_currentness",
    "latest_file_posture_treated_as_self_recursive_growth_boundary_authority",
    "repo_local_availability_treated_as_self_recursive_growth_boundary_authority",
    "hidden_repo_state_used_as_self_recursive_growth_boundary_content",
    "hidden_repo_state_used_as_self_recursive_growth_boundary_authority",
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
    "runtime_hosting_boundary_v1_failure_repaired",
    "runtime_hosting_boundary_v1_failure_hidden",
    "runtime_hosting_boundary_v1_failure_claimed_passed",
)

BLOCK_CODES = (
    "SELF_RECURSIVE_GROWTH_BOUNDARY_QUESTION_UNDECLARED",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_INTENT_UNSUPPORTED",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_EXPLICIT_BLOCK_REQUESTED",
    "SELF_CONTINUATION_BASIS_MISSING",
    "SELF_CONTINUATION_TERMINAL_SUMMARY_BASIS_MISSING",
    "SELF_CONTINUATION_NOT_RECORDED",
    "SELF_CONTINUATION_FAILED_CHECKS_PRESENT",
    "SELF_CONTINUATION_VERSION_NOT_0_1_0",
    "SELF_CONTINUATION_DID_NOT_RECORD_BOUNDED_SELF_CONTINUATION_POSTURE",
    "SELF_CONTINUATION_DID_NOT_RECORD_BOUNDED_SELF_CONTINUATION_ENVELOPE",
    "SELF_CONTINUATION_ALREADY_CREATED_SELF_RECURSIVE_GROWTH",
    "SELF_CONTINUATION_ALREADY_CREATED_RUNTIME_DAEMON",
    "SELF_CONTINUATION_ALREADY_CREATED_RUNTIME_LOOP",
    "SELF_CONTINUATION_ALREADY_CREATED_PUBLIC_API",
    "SELF_CONTINUATION_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE",
    "SELF_CONTINUATION_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR",
    "SELF_CONTINUATION_TREATED_AS_SELF_RECURSIVE_GROWTH",
    "SELF_CONTINUATION_TREATED_AS_RUNTIME_DAEMON",
    "SELF_CONTINUATION_TREATED_AS_RUNTIME_LOOP",
    "SELF_CONTINUATION_TREATED_AS_PUBLIC_API",
    "SELF_CONTINUATION_TREATED_AS_PARTICIPANT_FACING_INTERFACE",
    "SELF_CONTINUATION_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR",
    "SELF_CONTINUATION_AUTHORIZED_FUTURE_WORK",
    "SELF_CONTINUATION_NON_CLAIMS_NOT_CANONICAL_FALSE",
    "SELF_CONTINUATION_TERMINAL_SUMMARY_DID_NOT_PRESERVE_NO_SELF_RECURSIVE_GROWTH",
    "SELF_CONTINUATION_TERMINAL_SUMMARY_DID_NOT_PRESERVE_NO_SELF_RECURSIVE_GROWTH_SELECTED",
    "SELF_CONTINUATION_TERMINAL_SUMMARY_DID_NOT_REQUIRE_SEPARATE_REVIEW",
    "BOUNDED_SELF_CONTINUATION_ENVELOPE_TREATED_AS_SELF_RECURSIVE_GROWTH",
    "BOUNDED_SELF_CONTINUATION_ENVELOPE_AUTHORIZED_SELF_RECURSIVE_GROWTH",
    "BOUNDED_SELF_CONTINUATION_ENVELOPE_AUTHORIZED_RUNTIME_DAEMON",
    "BOUNDED_SELF_CONTINUATION_ENVELOPE_AUTHORIZED_RUNTIME_LOOP",
    "BOUNDED_SELF_CONTINUATION_ENVELOPE_AUTHORIZED_ARBITRARY_RUNTIME_ACTIVITY",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_CREATED_BEFORE_REVIEW",
    "SELF_RECURSIVE_GROWTH_CREATED",
    "RUNTIME_DAEMON_CREATED",
    "RUNTIME_LOOP_CREATED",
    "PUBLIC_API_CREATED",
    "PARTICIPANT_FACING_INTERFACE_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_SELF_RECURSIVE_GROWTH",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_RUNTIME_DAEMON",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_RUNTIME_LOOP",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_SOURCE",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_AUTHORITY",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_CURRENTNESS",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_DEPLOYMENT",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_PUBLIC_RELEASE",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_OPERATION_PERMISSION",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_BROADER_REUSABLE_PERMISSION",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
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
    "ANOTHER_RECEPTION_REQUEST_AUTHORIZED",
    "ADOPTION_CREATED",
    "RECEIVING_CONTEXT_GOVERNANCE_CREATED",
    "PUBLICATION_FLOW_CREATED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "ARTIFACT_EXISTENCE_TREATED_AS_SELF_RECURSIVE_GROWTH_BOUNDARY_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "LATEST_FILE_POSTURE_TREATED_AS_SELF_RECURSIVE_GROWTH_BOUNDARY_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_SELF_RECURSIVE_GROWTH_BOUNDARY_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_SELF_RECURSIVE_GROWTH_BOUNDARY_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_SELF_RECURSIVE_GROWTH_BOUNDARY_AUTHORITY",
    "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_SELF_RECURSIVE_GROWTH_BOUNDARY_SCOPE",
    "SELF_CONTINUATION_BOUNDARY_BASIS_MISSING",
    "SELF_CONTINUATION_BOUNDARY_NOT_RECORDED",
    "SELF_CONTINUATION_BOUNDARY_FAILED_CHECKS_PRESENT",
    "SELF_CONTINUATION_BOUNDARY_VERSION_NOT_0_1_0",
    "CONTINUATION_BASIS_MISSING",
    "CONTINUATION_NOT_RECORDED",
    "CONTINUATION_FAILED_CHECKS_PRESENT",
    "CONTINUATION_VERSION_NOT_0_1_0",
    "CONTINUATION_BOUNDARY_BASIS_MISSING",
    "CONTINUATION_BOUNDARY_NOT_RECORDED",
    "CONTINUATION_BOUNDARY_FAILED_CHECKS_PRESENT",
    "CONTINUATION_BOUNDARY_VERSION_NOT_0_1_0",
    "REUSABLE_RUNTIME_PERMISSION_BASIS_MISSING",
    "REUSABLE_RUNTIME_PERMISSION_NOT_RECORDED",
    "REUSABLE_RUNTIME_PERMISSION_FAILED_CHECKS_PRESENT",
    "REUSABLE_RUNTIME_PERMISSION_VERSION_NOT_0_1_0",
    "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_BASIS_MISSING",
    "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_NOT_RECORDED",
    "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_FAILED_CHECKS_PRESENT",
    "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_VERSION_NOT_0_1_0",
    "ONGOING_RUNTIME_BASIS_MISSING",
    "ONGOING_RUNTIME_NOT_RECORDED",
    "ONGOING_RUNTIME_FAILED_CHECKS_PRESENT",
    "ONGOING_RUNTIME_VERSION_NOT_0_1_0",
    "RUNTIME_HOSTING_BASIS_MISSING",
    "RUNTIME_HOSTING_NOT_RECORDED",
    "RUNTIME_HOSTING_FAILED_CHECKS_PRESENT",
    "RUNTIME_HOSTING_VERSION_NOT_0_1_0",
    "RUNTIME_HOSTING_BOUNDARY_V2_BASIS_MISSING",
    "RUNTIME_HOSTING_BOUNDARY_V2_NOT_RECORDED",
    "RUNTIME_HOSTING_BOUNDARY_V2_FAILED_CHECKS_PRESENT",
    "RUNTIME_HOSTING_BOUNDARY_V2_VERSION_NOT_0_2_0",
    "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_LINEAGE_MISSING",
    "SUCCESSOR_RUNTIME_STEP_BASIS_MISSING",
    "SUCCESSOR_RUNTIME_STEP_NOT_RECORDED",
    "SUCCESSOR_RUNTIME_STEP_FAILED_CHECKS_PRESENT",
    "SUCCESSOR_RUNTIME_STEP_VERSION_NOT_0_1_0",
    "MINIMAL_RUNTIME_BASIS_MISSING",
    "MINIMAL_RUNTIME_NOT_RECORDED",
    "MINIMAL_RUNTIME_FAILED_CHECKS_PRESENT",
    "MINIMAL_RUNTIME_VERSION_NOT_0_1_0",
    "RUNTIME_BOUNDARY_BASIS_MISSING",
    "RUNTIME_BOUNDARY_NOT_RECORDED",
    "RUNTIME_BOUNDARY_FAILED_CHECKS_PRESENT",
    "RUNTIME_BOUNDARY_VERSION_NOT_0_1_0",
    "RUNTIME_READINESS_BASIS_MISSING",
    "RUNTIME_READINESS_NOT_RECORDED",
    "RUNTIME_READINESS_FAILED_CHECKS_PRESENT",
    "RUNTIME_READINESS_VERSION_NOT_0_1_0",
    "PORTABLE_VERIFICATION_FINAL_COMPLETION_BASIS_MISSING",
    "PORTABLE_VERIFICATION_FINAL_COMPLETION_NOT_RECORDED",
    "PORTABLE_VERIFICATION_FINAL_COMPLETION_FAILED_CHECKS_PRESENT",
    "PORTABLE_VERIFICATION_FINAL_COMPLETION_VERSION_NOT_0_1_0",
    "POST_PORTABLE_CURRENTNESS_SURFACE_BASIS_MISSING",
    "POST_PORTABLE_CURRENTNESS_SURFACE_TREATED_CHECKABILITY_AS_CONTINUATION",
    "POST_PORTABLE_CURRENTNESS_SURFACE_AUTHORIZED_NEXT_WORK",
    "RETURNED_SECOND_CARRIER_CAPTURE_LINEAGE_BASIS_MISSING",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_REQUIRED_POSTURE_MISSING",
    "OFFICIAL_ENUM_SCOPE_STRINGS_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_NOT_CONTAINED",
    "DECLARED_SELF_RECURSIVE_GROWTH_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_SELF_RECURSIVE_GROWTH_BOUNDARY_REQUEST_UNREADABLE",
)

SELECTED_BASIS_FIELDS = (
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
    "self_recursive_growth_boundary_spec_only_posture",
    "one_future_self_recursive_growth_review_posture",
    "self_continuation_basis_preserved_posture",
    "self_continuation_not_self_recursive_growth_posture",
    "bounded_self_continuation_envelope_not_self_recursive_growth_posture",
    "self_recursive_growth_boundary_not_self_recursive_growth_posture",
    "self_recursive_growth_boundary_not_daemon_posture",
    "self_recursive_growth_boundary_not_loop_posture",
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
    "broader_reusable_permission_not_created_posture",
    "follow_on_work_not_authorized_posture",
    "hidden_repo_state_excluded_posture",
    "repo_local_availability_not_self_recursive_growth_boundary_authority_posture",
    "artifact_existence_not_self_recursive_growth_boundary_authority_posture",
    "latest_file_posture_not_self_recursive_growth_boundary_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
    "result_level_non_claims_canonical_false_posture",
)

BASIS_SHORTCUT_PREFIXES = {
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
    ("self_recursive_growth_boundary_created_before_review", "SELF_RECURSIVE_GROWTH_BOUNDARY_CREATED_BEFORE_REVIEW"),
    ("self_recursive_growth_created", "SELF_RECURSIVE_GROWTH_CREATED"),
    ("runtime_daemon_created", "RUNTIME_DAEMON_CREATED"),
    ("runtime_loop_created", "RUNTIME_LOOP_CREATED"),
    ("public_api_created", "PUBLIC_API_CREATED"),
    ("participant_facing_interface_created", "PARTICIPANT_FACING_INTERFACE_CREATED"),
    ("distributed_network_behavior_created", "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED"),
    (
        "self_recursive_growth_boundary_treated_as_self_recursive_growth",
        "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_SELF_RECURSIVE_GROWTH",
    ),
    ("self_recursive_growth_boundary_treated_as_runtime_daemon", "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_RUNTIME_DAEMON"),
    ("self_recursive_growth_boundary_treated_as_runtime_loop", "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_RUNTIME_LOOP"),
    ("self_recursive_growth_boundary_treated_as_source_transfer", "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_SOURCE_TRANSFER"),
    ("self_recursive_growth_boundary_treated_as_source_receipt", "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_SOURCE_RECEIPT"),
    (
        "self_recursive_growth_boundary_treated_as_reception_authorization",
        "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    ),
    ("self_recursive_growth_boundary_treated_as_source", "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_SOURCE"),
    ("self_recursive_growth_boundary_treated_as_authority", "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_AUTHORITY"),
    ("self_recursive_growth_boundary_treated_as_currentness", "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_CURRENTNESS"),
    ("self_recursive_growth_boundary_treated_as_deployment", "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_DEPLOYMENT"),
    ("self_recursive_growth_boundary_treated_as_public_release", "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_PUBLIC_RELEASE"),
    (
        "self_recursive_growth_boundary_treated_as_operation_permission",
        "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_OPERATION_PERMISSION",
    ),
    (
        "self_recursive_growth_boundary_treated_as_broader_reusable_permission",
        "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_BROADER_REUSABLE_PERMISSION",
    ),
    ("self_recursive_growth_boundary_treated_as_follow_on_work", "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK"),
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
    ("artifact_existence_treated_as_self_recursive_growth_boundary_authority", "ARTIFACT_EXISTENCE_TREATED_AS_SELF_RECURSIVE_GROWTH_BOUNDARY_AUTHORITY"),
    ("artifact_path_treated_as_currentness", "ARTIFACT_PATH_TREATED_AS_CURRENTNESS"),
    ("latest_file_posture_treated_as_self_recursive_growth_boundary_authority", "LATEST_FILE_POSTURE_TREATED_AS_SELF_RECURSIVE_GROWTH_BOUNDARY_AUTHORITY"),
    ("repo_local_availability_treated_as_self_recursive_growth_boundary_authority", "REPO_LOCAL_AVAILABILITY_TREATED_AS_SELF_RECURSIVE_GROWTH_BOUNDARY_AUTHORITY"),
    ("hidden_repo_state_used_as_self_recursive_growth_boundary_content", "HIDDEN_REPO_STATE_USED_AS_SELF_RECURSIVE_GROWTH_BOUNDARY_CONTENT"),
    ("hidden_repo_state_used_as_self_recursive_growth_boundary_authority", "HIDDEN_REPO_STATE_USED_AS_SELF_RECURSIVE_GROWTH_BOUNDARY_AUTHORITY"),
    ("raw_full_prior_artifact_body_returned", "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED"),
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
    "raw_self_recursive_growth_boundary_body",
    "raw_self_recursive_growth_body",
    "raw_runtime_daemon_body",
    "raw_runtime_loop_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "raw_runtime_body",
    "self_recursive_growth_boundary_body",
    "self_recursive_growth_body",
    "runtime_body",
    "source_body",
    "authority_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
}

HOSTILE_SENTINELS = (
    "RAW_SELF_RECURSIVE_GROWTH_BOUNDARY_BODY_MUST_NOT_RETURN",
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

REDACTED_RAW_VALUE = "[bounded-redacted-raw-or-hidden-state]"
DEFAULT_REQUEST_ID = "post_self_continuation_self_recursive_growth_boundary_reference_review_001"


def _now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _canonical_false_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _is_declared(value: Any) -> bool:
    if value is None:
        return False
    if value is False:
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
    summary: dict[str, Any]
    if isinstance(value, Mapping):
        summary = _sanitize(value)
    else:
        summary = {"basis_value": _sanitize(value)}
    summary["basis_declared"] = _is_declared(value)
    prefix = BASIS_SHORTCUT_PREFIXES.get(basis_field)
    if prefix:
        for key in ("path", "outcome", "result_version", "failed_check_count"):
            shortcut_key = f"selected_{prefix}_result_path" if key == "path" else f"selected_{prefix}_{key}"
            if key == "failed_check_count":
                shortcut_key = f"selected_{prefix}_failed_check_count"
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
    section["creates_self_recursive_growth"] = False
    section["creates_daemon_loop_api_interface_or_distributed_network"] = False
    section["creates_source_authority_currentness_deployment_public_release_or_operation_permission"] = False
    section["authorizes_follow_on_work"] = False
    return section


def _declared_posture(name: str) -> dict[str, Any]:
    return {
        "posture_name": name,
        "declared": True,
        "posture_only": True,
        "creates_self_recursive_growth": False,
        "creates_daemon_loop_api_interface_or_distributed_network": False,
        "creates_source_authority_currentness_deployment_public_release_or_operation_permission": False,
        "authorizes_follow_on_work": False,
    }


def _validate_declared_request(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    question = request.get("self_recursive_growth_boundary_question")
    _check(
        checks,
        "self-recursive-growth-boundary question declared",
        question == CORE_QUESTION,
        CORE_QUESTION,
        question,
        "SELF_RECURSIVE_GROWTH_BOUNDARY_QUESTION_UNDECLARED",
    )

    intent = request.get("self_recursive_growth_boundary_intent")
    _check(
        checks,
        "self-recursive-growth-boundary intent supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "SELF_RECURSIVE_GROWTH_BOUNDARY_INTENT_UNSUPPORTED",
    )
    _check(
        checks,
        "explicit self-recursive-growth-boundary block intent absent",
        intent != INTENT_BLOCK,
        f"intent not {INTENT_BLOCK}",
        intent,
        "SELF_RECURSIVE_GROWTH_BOUNDARY_EXPLICIT_BLOCK_REQUESTED",
    )

    scope = _scope_list(request.get("self_recursive_growth_boundary_scope"))
    unsupported_scope = [item for item in scope if item not in SUPPORTED_SCOPE_VALUES]
    _check(
        checks,
        "self-recursive-growth-boundary scope supported",
        not unsupported_scope and bool(scope),
        SUPPORTED_SCOPE_VALUES,
        scope,
        "UNSUPPORTED_SELF_RECURSIVE_GROWTH_BOUNDARY_SCOPE",
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
        ("selected_self_continuation_already_created_self_recursive_growth", "SELF_CONTINUATION_ALREADY_CREATED_SELF_RECURSIVE_GROWTH"),
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
        ("selected_self_continuation_treated_as_self_recursive_growth", "SELF_CONTINUATION_TREATED_AS_SELF_RECURSIVE_GROWTH"),
        ("selected_self_continuation_treated_as_runtime_daemon", "SELF_CONTINUATION_TREATED_AS_RUNTIME_DAEMON"),
        ("selected_self_continuation_treated_as_runtime_loop", "SELF_CONTINUATION_TREATED_AS_RUNTIME_LOOP"),
        ("selected_self_continuation_treated_as_public_api", "SELF_CONTINUATION_TREATED_AS_PUBLIC_API"),
        (
            "selected_self_continuation_treated_as_participant_facing_interface",
            "SELF_CONTINUATION_TREATED_AS_PARTICIPANT_FACING_INTERFACE",
        ),
        (
            "selected_self_continuation_treated_as_distributed_network_behavior",
            "SELF_CONTINUATION_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR",
        ),
        ("selected_self_continuation_authorized_future_work", "SELF_CONTINUATION_AUTHORIZED_FUTURE_WORK"),
        (
            "selected_bounded_self_continuation_envelope_treated_as_self_recursive_growth",
            "BOUNDED_SELF_CONTINUATION_ENVELOPE_TREATED_AS_SELF_RECURSIVE_GROWTH",
        ),
        (
            "selected_bounded_self_continuation_envelope_authorized_self_recursive_growth",
            "BOUNDED_SELF_CONTINUATION_ENVELOPE_AUTHORIZED_SELF_RECURSIVE_GROWTH",
        ),
        (
            "selected_bounded_self_continuation_envelope_authorized_runtime_daemon",
            "BOUNDED_SELF_CONTINUATION_ENVELOPE_AUTHORIZED_RUNTIME_DAEMON",
        ),
        (
            "selected_bounded_self_continuation_envelope_authorized_runtime_loop",
            "BOUNDED_SELF_CONTINUATION_ENVELOPE_AUTHORIZED_RUNTIME_LOOP",
        ),
        (
            "selected_bounded_self_continuation_envelope_authorized_arbitrary_runtime_activity",
            "BOUNDED_SELF_CONTINUATION_ENVELOPE_AUTHORIZED_ARBITRARY_RUNTIME_ACTIVITY",
        ),
    )
    for field, code in self_continuation_false_checks:
        _check(checks, field, request.get(field) is not True, False, request.get(field), code)

    _check(
        checks,
        "self-continuation canonicalized result-level non-claims",
        _flag_true(request.get("selected_self_continuation_non_claims_canonicalized")),
        True,
        request.get("selected_self_continuation_non_claims_canonicalized"),
        "SELF_CONTINUATION_NON_CLAIMS_NOT_CANONICAL_FALSE",
    )
    _check(
        checks,
        "self-continuation terminal summary states self-recursive growth not created",
        _flag_true(request.get("selected_self_continuation_terminal_summary_self_recursive_growth_not_created")),
        True,
        request.get("selected_self_continuation_terminal_summary_self_recursive_growth_not_created"),
        "SELF_CONTINUATION_TERMINAL_SUMMARY_DID_NOT_PRESERVE_NO_SELF_RECURSIVE_GROWTH",
    )
    _check(
        checks,
        "self-continuation terminal summary states no self-recursive growth selected",
        _flag_true(request.get("selected_self_continuation_terminal_summary_no_self_recursive_growth_selected")),
        True,
        request.get("selected_self_continuation_terminal_summary_no_self_recursive_growth_selected"),
        "SELF_CONTINUATION_TERMINAL_SUMMARY_DID_NOT_PRESERVE_NO_SELF_RECURSIVE_GROWTH_SELECTED",
    )
    _check(
        checks,
        "self-continuation terminal summary requires separate future review",
        _flag_true(request.get("selected_self_continuation_terminal_summary_future_work_requires_separate_step_back_review")),
        True,
        request.get("selected_self_continuation_terminal_summary_future_work_requires_separate_step_back_review"),
        "SELF_CONTINUATION_TERMINAL_SUMMARY_DID_NOT_REQUIRE_SEPARATE_REVIEW",
    )


def _validate_upstream_basis(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    for basis_field, prefix, expected_outcome, expected_version, missing_code, outcome_code, version_code, failed_code in UPSTREAM_EXPECTATIONS:
        _check(
            checks,
            f"{basis_field} declared",
            _is_declared(request.get(basis_field)),
            f"declared {basis_field}",
            request.get(basis_field),
            missing_code,
        )
        _check(
            checks,
            f"{prefix} outcome recorded",
            _basis_value(request, basis_field, "outcome") == expected_outcome,
            expected_outcome,
            _basis_value(request, basis_field, "outcome"),
            outcome_code,
        )
        _check(
            checks,
            f"{prefix} version expected",
            _basis_value(request, basis_field, "result_version") == expected_version,
            expected_version,
            _basis_value(request, basis_field, "result_version"),
            version_code,
        )
        _check(
            checks,
            f"{prefix} failed checks zero",
            _safe_int(_basis_value(request, basis_field, "failed_check_count")) == 0,
            0,
            _basis_value(request, basis_field, "failed_check_count"),
            failed_code,
        )


def _validate_lineage_and_currentness(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    _check(
        checks,
        "runtime-hosting-boundary v1 failure lineage declared",
        _is_declared(request.get("selected_runtime_hosting_boundary_v1_failure_lineage_basis")),
        "declared preserved v1 failure lineage",
        request.get("selected_runtime_hosting_boundary_v1_failure_lineage_basis"),
        "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_LINEAGE_MISSING",
    )
    v1_repaired = request.get("selected_runtime_hosting_boundary_v1_failure_repaired") is True
    v1_hidden = request.get("selected_runtime_hosting_boundary_v1_failure_hidden") is True
    v1_claimed = request.get("selected_runtime_hosting_boundary_v1_failure_claimed_passed") is True
    _check(
        checks,
        "runtime-hosting-boundary v1 failure preserved and not repaired hidden or claimed passed",
        not (v1_repaired or v1_hidden or v1_claimed),
        "v1 failure remains preserved predecessor evidence",
        {
            "repaired": v1_repaired,
            "hidden": v1_hidden,
            "claimed_passed": v1_claimed,
        },
        "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
    )
    _check(
        checks,
        "post-portable currentness surface basis declared",
        _is_declared(request.get("selected_post_portable_verification_currentness_basis")),
        "declared post-portable currentness surface basis",
        request.get("selected_post_portable_verification_currentness_basis"),
        "POST_PORTABLE_CURRENTNESS_SURFACE_BASIS_MISSING",
    )
    _check(
        checks,
        "post-portable currentness surface states checkability not continuation",
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


def _validate_postures(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    for field in POSTURE_FIELDS:
        _check(
            checks,
            f"{field} declared",
            _is_declared(request.get(field)),
            f"declared {field}",
            request.get(field),
            "SELF_RECURSIVE_GROWTH_BOUNDARY_REQUIRED_POSTURE_MISSING",
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
    _check(
        checks,
        "raw full prior artifact body not returned",
        request.get("raw_full_prior_artifact_body_returned") is not True,
        False,
        request.get("raw_full_prior_artifact_body_returned"),
        "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    )
    _check(
        checks,
        "official enum scope strings not redacted",
        "[bounded-self-continuation-redacted]" not in _scope_list(request.get("self_recursive_growth_boundary_scope"))
        and "[bounded-redacted-raw-or-hidden-state]" not in _scope_list(request.get("self_recursive_growth_boundary_scope")),
        "official scope strings preserved",
        _scope_list(request.get("self_recursive_growth_boundary_scope")),
        "OFFICIAL_ENUM_SCOPE_STRINGS_REDACTED",
    )
    _check(
        checks,
        "hostile raw body content contained",
        not _contains_hostile_sentinel(_sanitize(request)),
        "no hostile raw sentinel returned after sanitization",
        "contained" if not _contains_hostile_sentinel(_sanitize(request)) else "not contained",
        "HOSTILE_RAW_BODY_CONTENT_NOT_CONTAINED",
    )


def _validate_declared_non_claims(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    declared = request.get("declared_non_claims")
    declared_mapping = declared if isinstance(declared, Mapping) else {}
    for key in REQUIRED_FALSE_NON_CLAIMS:
        _check(
            checks,
            f"required non-claim false: {key}",
            key in declared_mapping and declared_mapping.get(key) is False,
            {key: False},
            {key: declared_mapping.get(key, None)} if isinstance(declared_mapping, Mapping) else declared,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )


def _run_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    _validate_declared_request(request, checks)
    _validate_self_continuation_basis(request, checks)
    _validate_upstream_basis(request, checks)
    _validate_lineage_and_currentness(request, checks)
    _validate_postures(request, checks)
    _validate_false_inputs(request, checks)
    _validate_declared_non_claims(request, checks)
    return checks


def _determine_outcome(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> str:
    if any(not check.get("passed") for check in checks):
        return OUTCOME_BLOCKED
    requested = request.get("requested_self_recursive_growth_boundary_outcome")
    if requested == OUTCOME_NOT_RECORDED or request.get("self_recursive_growth_boundary_intent") == INTENT_DO_NOT_RECORD:
        return OUTCOME_NOT_RECORDED
    if requested == OUTCOME_REQUIRES_ADDITIONAL_BASIS or _is_declared(request.get("additional_basis_context")):
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS
    return OUTCOME_RECORDED


def _statement_for_outcome(outcome: str) -> dict[str, bool]:
    recorded = outcome == OUTCOME_RECORDED
    statement = {field: True for field in ALLOWED_TRUE_RECORDED_FIELDS}
    statement["self_recursive_growth_boundary_recorded"] = recorded
    statement["one_future_self_recursive_growth_review_declared"] = recorded
    return statement


def _non_meaning() -> dict[str, bool]:
    return {
        "self_recursive_growth_exists": False,
        "runtime_daemon_exists": False,
        "runtime_loop_exists": False,
        "public_api_exists": False,
        "participant_facing_interface_exists": False,
        "distributed_network_behavior_exists": False,
        "source_transfer_occurred": False,
        "source_receipt_occurred": False,
        "reception_authorization_exists": False,
        "source_exists": False,
        "authority_exists": False,
        "currentness_exists": False,
        "deployment_exists": False,
        "public_release_exists": False,
        "operation_permission_exists": False,
        "broader_reusable_permission_exists": False,
        "derivative_reception_exists": False,
        "vessel_relation_exists": False,
        "adoption_exists": False,
        "receiving_context_governance_exists": False,
        "publication_flow_exists": False,
        "follow_on_work_authorized": False,
        "self_recursive_growth_boundary_became_self_recursive_growth": False,
        "self_recursive_growth_boundary_became_daemon_loop_api_interface_or_distributed_behavior": False,
        "self_continuation_became_self_recursive_growth": False,
        "bounded_self_continuation_envelope_became_self_recursive_growth": False,
        "artifact_existence_became_self_recursive_growth_boundary_authority": False,
        "repo_local_availability_became_self_recursive_growth_boundary_authority": False,
        "latest_file_posture_became_self_recursive_growth_boundary_authority": False,
        "predecessor_failure_evidence_was_repaired_hidden_erased_or_claimed_passed": False,
    }


def _additional_basis_required(outcome: str, request: Mapping[str, Any]) -> list[str]:
    if outcome != OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        return []
    context = request.get("additional_basis_context")
    if isinstance(context, list):
        return [_sanitize(item) for item in context]
    if _is_declared(context):
        return [_sanitize(context)]
    return ["additional bounded self-recursive-growth-boundary basis required"]


def _not_recorded_basis(outcome: str, request: Mapping[str, Any]) -> list[str]:
    if outcome != OUTCOME_NOT_RECORDED:
        return []
    basis = request.get("not_recorded_basis")
    if isinstance(basis, list):
        return [_sanitize(item) for item in basis]
    if _is_declared(basis):
        return [_sanitize(basis)]
    return ["self-recursive-growth boundary was not recorded by declared request posture"]


def _what_remains_open() -> list[str]:
    return [
        "self-recursive-growth-boundary test",
        "self-recursive-growth-boundary live artifact",
        "self-recursive-growth-boundary terminal summary, if needed",
        "self-recursive growth specification",
        "self-recursive growth resolver/test/live artifact",
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
    code = _first_failed_code(checks) or "DECLARED_SELF_RECURSIVE_GROWTH_BOUNDARY_REQUEST_MALFORMED"
    return {
        "block_code": code,
        "block_reason": _sanitize(request.get("block_reason"))
        or "self-recursive-growth-boundary request did not preserve the bounded membrane",
    }


def _build_metadata(request: Mapping[str, Any]) -> dict[str, Any]:
    request_id = request.get("self_recursive_growth_boundary_request_id") or DEFAULT_REQUEST_ID
    return {
        "post_self_continuation_self_recursive_growth_boundary_id": str(request_id),
        "post_self_continuation_self_recursive_growth_boundary_type": "post_self_continuation_self_recursive_growth_boundary_result",
        "post_self_continuation_self_recursive_growth_boundary_version": RESULT_VERSION,
        "generated_at": _now_iso(),
        "resolver_module": RESOLVER_MODULE,
    }


def _build_result(request: Mapping[str, Any], checks: list[dict[str, Any]], outcome: str) -> dict[str, Any]:
    statement = _statement_for_outcome(outcome)
    block = _block_for_outcome(outcome, checks, request)
    result: dict[str, Any] = {
        "post_self_continuation_self_recursive_growth_boundary_metadata": _build_metadata(request),
        "declared_self_recursive_growth_boundary_question": {
            "self_recursive_growth_boundary_request_id": _sanitize(
                request.get("self_recursive_growth_boundary_request_id") or DEFAULT_REQUEST_ID
            ),
            "question": _sanitize(request.get("self_recursive_growth_boundary_question")),
            "intent": _sanitize(request.get("self_recursive_growth_boundary_intent")),
            "core_question": CORE_QUESTION,
        },
    }
    for field in SELECTED_BASIS_FIELDS:
        result[field] = _basis_summary(request, field)
    for field in POSTURE_FIELDS:
        result[field] = _posture_section(field, request)
    result.update(
        {
            "self_recursive_growth_boundary_scope": _scope_list(request.get("self_recursive_growth_boundary_scope")),
            "self_recursive_growth_boundary_checks": checks,
            "self_recursive_growth_boundary_statement": statement,
            "self_recursive_growth_boundary_non_meaning": _non_meaning(),
            "additional_basis_required": _additional_basis_required(outcome, request),
            "not_recorded_basis": _not_recorded_basis(outcome, request),
            "what_remains_open": _what_remains_open(),
            "non_claims": _canonical_false_non_claims(),
            "outcome": outcome,
            "block": block,
        }
    )
    result["post_self_continuation_self_recursive_growth_boundary_summary"] = (
        build_post_self_continuation_self_recursive_growth_boundary_summary(result)
    )
    return result


def _malformed_result(code: str, reason: str, actual: Any = None) -> dict[str, Any]:
    request = build_declared_post_self_continuation_self_recursive_growth_boundary_request()
    request["self_recursive_growth_boundary_request_id"] = "malformed_self_recursive_growth_boundary_request"
    checks: list[dict[str, Any]] = []
    _check(checks, "declared self-recursive-growth-boundary request readable", False, "mapping request", actual, code)
    request["block_reason"] = reason
    return _build_result(request, checks, OUTCOME_BLOCKED)


def resolve_post_self_continuation_self_recursive_growth_boundary(
    declared_self_recursive_growth_boundary_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one bounded self-recursive-growth-boundary request mapping."""

    if declared_self_recursive_growth_boundary_request is None:
        return _malformed_result(
            "DECLARED_SELF_RECURSIVE_GROWTH_BOUNDARY_REQUEST_MALFORMED",
            "declared self-recursive-growth-boundary request is missing",
            None,
        )
    if not isinstance(declared_self_recursive_growth_boundary_request, Mapping):
        return _malformed_result(
            "DECLARED_SELF_RECURSIVE_GROWTH_BOUNDARY_REQUEST_MALFORMED",
            "declared self-recursive-growth-boundary request must be a mapping",
            type(declared_self_recursive_growth_boundary_request).__name__,
        )
    request = deepcopy(dict(declared_self_recursive_growth_boundary_request))
    checks = _run_checks(request)
    outcome = _determine_outcome(request, checks)
    return _build_result(request, checks, outcome)


def resolve_post_self_continuation_self_recursive_growth_boundary_from_path(
    declared_self_recursive_growth_boundary_request_path: Path | str,
) -> dict:
    """Resolve one bounded self-recursive-growth-boundary request from a JSON file."""

    path = Path(declared_self_recursive_growth_boundary_request_path)
    try:
        with path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
    except json.JSONDecodeError as exc:
        return _malformed_result(
            "DECLARED_SELF_RECURSIVE_GROWTH_BOUNDARY_REQUEST_MALFORMED",
            f"declared self-recursive-growth-boundary request JSON is malformed: {exc.msg}",
            str(path),
        )
    except OSError as exc:
        return _malformed_result(
            "DECLARED_SELF_RECURSIVE_GROWTH_BOUNDARY_REQUEST_UNREADABLE",
            f"declared self-recursive-growth-boundary request is unreadable: {exc}",
            str(path),
        )
    if not isinstance(payload, Mapping):
        return _malformed_result(
            "DECLARED_SELF_RECURSIVE_GROWTH_BOUNDARY_REQUEST_MALFORMED",
            "declared self-recursive-growth-boundary request JSON must be an object",
            type(payload).__name__,
        )
    return resolve_post_self_continuation_self_recursive_growth_boundary(payload)


def _summary_basis(result: Mapping[str, Any], section: str, key: str) -> Any:
    value = result.get(section)
    if isinstance(value, Mapping):
        return value.get(key)
    return None


def build_post_self_continuation_self_recursive_growth_boundary_summary(result: Mapping[str, Any]) -> dict:
    """Build a compact summary without changing the bounded result artifact."""

    checks = result.get("self_recursive_growth_boundary_checks", [])
    if not isinstance(checks, list):
        checks = []
    statement = result.get("self_recursive_growth_boundary_statement", {})
    if not isinstance(statement, Mapping):
        statement = {}
    block = result.get("block")
    if not isinstance(block, Mapping):
        block = {}
    metadata = result.get("post_self_continuation_self_recursive_growth_boundary_metadata", {})
    if not isinstance(metadata, Mapping):
        metadata = {}
    question = result.get("declared_self_recursive_growth_boundary_question", {})
    if not isinstance(question, Mapping):
        question = {}

    summary: dict[str, Any] = {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "request_id": question.get("self_recursive_growth_boundary_request_id")
        or metadata.get("post_self_continuation_self_recursive_growth_boundary_id"),
        "question": question.get("question"),
        "intent": question.get("intent"),
        "passed_check_count": sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed") is True),
        "failed_check_count": sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed") is not True),
        "result_version": metadata.get("post_self_continuation_self_recursive_growth_boundary_version"),
        "resolver_module": metadata.get("resolver_module"),
        "selected_post_portable_currentness_surface_path": _summary_basis(
            result, "selected_post_portable_verification_currentness_basis", "path"
        ),
        "no_self_recursive_growth_daemon_loop_api_interface_distributed_network_source_authority_currentness_deployment_public_release_follow_on": True,
        "key_non_claims": result.get("non_claims"),
        "predecessor_failure_evidence_preserved": statement.get("predecessor_failure_evidence_preserved"),
        "consumed_request_token_remains_closed": statement.get("consumed_request_token_remains_closed"),
        "authorization_token_reuse_blocked": statement.get("authorization_token_reuse_blocked"),
    }
    for field in ALLOWED_TRUE_RECORDED_FIELDS:
        summary[field] = statement.get(field) is True

    basis_summary_names = {
        "selected_self_continuation": "selected_self_continuation_basis",
        "selected_self_continuation_boundary": "selected_self_continuation_boundary_basis",
        "selected_continuation": "selected_continuation_basis",
        "selected_continuation_boundary": "selected_continuation_boundary_basis",
        "selected_reusable_runtime_permission": "selected_reusable_runtime_permission_basis",
        "selected_reusable_runtime_permission_boundary": "selected_reusable_runtime_permission_boundary_basis",
        "selected_ongoing_runtime": "selected_ongoing_runtime_basis",
        "selected_runtime_hosting": "selected_runtime_hosting_basis",
        "selected_runtime_hosting_boundary_v2": "selected_runtime_hosting_boundary_v2_basis",
        "selected_successor_runtime_step": "selected_successor_runtime_step_basis",
        "selected_minimal_runtime": "selected_minimal_runtime_basis",
        "selected_runtime_boundary": "selected_runtime_boundary_basis",
        "selected_runtime_readiness": "selected_runtime_readiness_basis",
        "selected_final_completion": "selected_portable_verification_final_completion_basis",
    }
    for summary_prefix, section in basis_summary_names.items():
        summary[f"{summary_prefix}_outcome"] = _summary_basis(result, section, "outcome")
        summary[f"{summary_prefix}_version"] = _summary_basis(result, section, "result_version")
        summary[f"{summary_prefix}_failed_check_count"] = _summary_basis(result, section, "failed_check_count")
    return summary


def _non_overwriting_path(path: Path) -> Path:
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


def write_post_self_continuation_self_recursive_growth_boundary_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a bounded self-recursive-growth-boundary result as stable UTF-8 JSON."""

    metadata = result.get("post_self_continuation_self_recursive_growth_boundary_metadata", {})
    if not isinstance(metadata, Mapping):
        metadata = {}
    request_id = metadata.get("post_self_continuation_self_recursive_growth_boundary_id") or DEFAULT_REQUEST_ID
    filename = f"{request_id}__post_self_continuation_self_recursive_growth_boundary_result.json"

    if output_path is None:
        destination = OUTPUT_ROOT / filename
    else:
        supplied = Path(output_path)
        destination = supplied if supplied.suffix == ".json" else supplied / filename
    destination = _non_overwriting_path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8") as handle:
        json.dump(_sanitize(result), handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
    return destination


def _basis(
    basis_name: str,
    path: str,
    outcome: str | None = None,
    result_version: str | None = None,
    failed_check_count: int | None = None,
) -> dict[str, Any]:
    basis = {
        "basis_name": basis_name,
        "path": path,
        "basis_only": True,
        "reference_shape_preserved": True,
        "creates_self_recursive_growth": False,
        "creates_daemon_loop_api_interface_or_distributed_network": False,
        "creates_source_authority_currentness_deployment_public_release_or_operation_permission": False,
        "authorizes_follow_on_work": False,
    }
    if outcome is not None:
        basis["outcome"] = outcome
    if result_version is not None:
        basis["result_version"] = result_version
    if failed_check_count is not None:
        basis["failed_check_count"] = failed_check_count
    return basis


def build_declared_post_self_continuation_self_recursive_growth_boundary_request(**overrides: Any) -> dict[str, Any]:
    """Build a clean bounded request that records with no arguments."""

    request: dict[str, Any] = {
        "self_recursive_growth_boundary_request_id": DEFAULT_REQUEST_ID,
        "self_recursive_growth_boundary_question": CORE_QUESTION,
        "self_recursive_growth_boundary_intent": INTENT_RECORD,
        "selected_self_continuation_basis": _basis(
            "post-continuation self-continuation live artifact",
            "artifacts/integrity_host_v0_min_coexistence_post_continuation_self_continuation/"
            "post_continuation_self_continuation_reference_review_001__post_continuation_self_continuation_result.json",
            "POST_CONTINUATION_SELF_CONTINUATION_RECORDED",
            "0.1.0",
            0,
        ),
        "selected_self_continuation_terminal_summary_basis": _basis(
            "post-continuation self-continuation terminal summary",
            "spec/POST_CONTINUATION_SELF_CONTINUATION_TERMINAL_SUMMARY_V0.md",
        ),
        "selected_self_continuation_boundary_basis": _basis(
            "post-continuation self-continuation-boundary live artifact",
            "artifacts/integrity_host_v0_min_coexistence_post_continuation_self_continuation_boundary/"
            "post_continuation_self_continuation_boundary_reference_review_001__post_continuation_self_continuation_boundary_result.json",
            "POST_CONTINUATION_SELF_CONTINUATION_BOUNDARY_RECORDED",
            "0.1.0",
            0,
        ),
        "selected_continuation_basis": _basis(
            "post-reusable-runtime-permission continuation live artifact",
            "artifacts/integrity_host_v0_min_coexistence_post_reusable_runtime_permission_continuation/"
            "post_reusable_runtime_permission_continuation_reference_review_001__post_reusable_runtime_permission_continuation_result.json",
            "POST_REUSABLE_RUNTIME_PERMISSION_CONTINUATION_RECORDED",
            "0.1.0",
            0,
        ),
        "selected_continuation_boundary_basis": _basis(
            "post-reusable-runtime-permission continuation-boundary basis",
            "artifacts/integrity_host_v0_min_coexistence_post_reusable_runtime_permission_continuation_boundary/"
            "post_reusable_runtime_permission_continuation_boundary_reference_review_001__post_reusable_runtime_permission_continuation_boundary_result.json",
            "POST_REUSABLE_RUNTIME_PERMISSION_CONTINUATION_BOUNDARY_RECORDED",
            "0.1.0",
            0,
        ),
        "selected_reusable_runtime_permission_basis": _basis(
            "post-ongoing-runtime reusable-runtime-permission basis",
            "artifacts/integrity_host_v0_min_coexistence_post_ongoing_runtime_reusable_runtime_permission/"
            "post_ongoing_runtime_reusable_runtime_permission_reference_review_001__post_ongoing_runtime_reusable_runtime_permission_result.json",
            "POST_ONGOING_RUNTIME_REUSABLE_RUNTIME_PERMISSION_RECORDED",
            "0.1.0",
            0,
        ),
        "selected_reusable_runtime_permission_boundary_basis": _basis(
            "post-ongoing-runtime reusable-runtime-permission-boundary basis",
            "artifacts/integrity_host_v0_min_coexistence_post_ongoing_runtime_reusable_runtime_permission_boundary/"
            "post_ongoing_runtime_reusable_runtime_permission_boundary_reference_review_001__post_ongoing_runtime_reusable_runtime_permission_boundary_result.json",
            "POST_ONGOING_RUNTIME_REUSABLE_RUNTIME_PERMISSION_BOUNDARY_RECORDED",
            "0.1.0",
            0,
        ),
        "selected_ongoing_runtime_basis": _basis(
            "post-runtime-hosting ongoing-runtime basis",
            "artifacts/integrity_host_v0_min_coexistence_post_runtime_hosting_ongoing_runtime/"
            "post_runtime_hosting_ongoing_runtime_reference_review_001__post_runtime_hosting_ongoing_runtime_result.json",
            "POST_RUNTIME_HOSTING_ONGOING_RUNTIME_RECORDED",
            "0.1.0",
            0,
        ),
        "selected_runtime_hosting_basis": _basis(
            "post-successor-runtime-step runtime-hosting basis",
            "artifacts/integrity_host_v0_min_coexistence_post_successor_runtime_step_runtime_hosting/"
            "post_successor_runtime_step_runtime_hosting_reference_review_001__post_successor_runtime_step_runtime_hosting_result.json",
            "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_RECORDED",
            "0.1.0",
            0,
        ),
        "selected_runtime_hosting_boundary_v2_basis": _basis(
            "post-successor-runtime-step runtime-hosting-boundary v2 basis",
            "artifacts/integrity_host_v0_min_coexistence_post_successor_runtime_step_runtime_hosting_boundary_v2/"
            "post_successor_runtime_step_runtime_hosting_boundary_v2_reference_review_001__post_successor_runtime_step_runtime_hosting_boundary_v2_result.json",
            "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_BOUNDARY_RECORDED",
            "0.2.0",
            0,
        ),
        "selected_runtime_hosting_boundary_v1_failure_lineage_basis": _basis(
            "runtime-hosting-boundary v1 preserved failure lineage",
            "src/resolve_post_successor_runtime_step_runtime_hosting_boundary.py",
        ),
        "selected_successor_runtime_step_basis": _basis(
            "post-minimal-runtime successor-runtime-step basis",
            "artifacts/integrity_host_v0_min_coexistence_post_minimal_runtime_successor_runtime_step/"
            "post_minimal_runtime_successor_runtime_step_reference_review_001__post_minimal_runtime_successor_runtime_step_result.json",
            "POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_RECORDED",
            "0.1.0",
            0,
        ),
        "selected_minimal_runtime_basis": _basis(
            "post-portable-verification minimal-runtime basis",
            "artifacts/integrity_host_v0_min_coexistence_post_portable_verification_minimal_runtime/"
            "post_portable_verification_minimal_runtime_reference_review_001__post_portable_verification_minimal_runtime_result.json",
            "POST_PORTABLE_VERIFICATION_MINIMAL_RUNTIME_RECORDED",
            "0.1.0",
            0,
        ),
        "selected_runtime_boundary_basis": _basis(
            "post-portable-verification runtime-boundary basis",
            "artifacts/integrity_host_v0_min_coexistence_post_portable_verification_runtime_boundary/"
            "post_portable_verification_runtime_boundary_reference_review_001__post_portable_verification_runtime_boundary_result.json",
            "POST_PORTABLE_VERIFICATION_RUNTIME_BOUNDARY_RECORDED",
            "0.1.0",
            0,
        ),
        "selected_runtime_readiness_basis": _basis(
            "post-portable-verification runtime-readiness basis",
            "artifacts/integrity_host_v0_min_coexistence_post_portable_verification_runtime_readiness/"
            "post_portable_verification_runtime_readiness_reference_review_001__post_portable_verification_runtime_readiness_result.json",
            "POST_PORTABLE_VERIFICATION_RUNTIME_READINESS_RECORDED",
            "0.1.0",
            0,
        ),
        "selected_portable_verification_final_completion_basis": _basis(
            "portable source-body verification final-completion basis",
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_final_completion/"
            "portable_source_body_verification_final_completion_reference_review_001__portable_source_body_verification_final_completion_result.json",
            "PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_RECORDED",
            "0.1.0",
            0,
        ),
        "selected_post_portable_verification_currentness_basis": _basis(
            "post-portable-verification currentness surface basis",
            "spec/POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_V0.md",
        ),
        "selected_returned_second_carrier_capture_lineage_basis": _basis(
            "returned second-carrier capture intake lineage only",
            "reference/IAMMAI/lineage/returned_second_carrier_capture_intake_lineage",
        ),
        "self_recursive_growth_boundary_scope": list(SUPPORTED_SCOPE_VALUES),
        "declared_non_claims": _canonical_false_non_claims(),
        "selected_self_continuation_bounded_posture_recorded": True,
        "selected_self_continuation_bounded_self_continuation_envelope_recorded": True,
        "selected_self_continuation_non_claims_canonicalized": True,
        "selected_self_continuation_terminal_summary_self_recursive_growth_not_created": True,
        "selected_self_continuation_terminal_summary_no_self_recursive_growth_selected": True,
        "selected_self_continuation_terminal_summary_future_work_requires_separate_step_back_review": True,
        "selected_post_portable_currentness_surface_path": "spec/POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_V0.md",
        "selected_post_portable_currentness_surface_states_checkability_not_continuation": True,
        "selected_post_portable_currentness_surface_authorized_next_work": False,
        "reference_shaped_input_posture": True,
    }

    for field in POSTURE_FIELDS:
        request[field] = _declared_posture(field)

    for basis_field, prefix in BASIS_SHORTCUT_PREFIXES.items():
        basis_value = request.get(basis_field)
        if isinstance(basis_value, Mapping):
            if "path" in basis_value:
                request[f"selected_{prefix}_result_path"] = basis_value["path"]
            if "outcome" in basis_value:
                request[f"selected_{prefix}_result_outcome"] = basis_value["outcome"]
            if "result_version" in basis_value:
                request[f"selected_{prefix}_result_version"] = basis_value["result_version"]
            if "failed_check_count" in basis_value:
                request[f"selected_{prefix}_failed_check_count"] = basis_value["failed_check_count"]

    false_defaults = _canonical_false_non_claims()
    false_defaults.update(
        {
            "self_recursive_growth_boundary_created_before_review": False,
            "selected_self_continuation_already_created_self_recursive_growth": False,
            "selected_self_continuation_already_created_runtime_daemon": False,
            "selected_self_continuation_already_created_runtime_loop": False,
            "selected_self_continuation_already_created_public_api": False,
            "selected_self_continuation_already_created_participant_facing_interface": False,
            "selected_self_continuation_already_created_distributed_network_behavior": False,
            "selected_self_continuation_treated_as_self_recursive_growth": False,
            "selected_self_continuation_treated_as_runtime_daemon": False,
            "selected_self_continuation_treated_as_runtime_loop": False,
            "selected_self_continuation_treated_as_public_api": False,
            "selected_self_continuation_treated_as_participant_facing_interface": False,
            "selected_self_continuation_treated_as_distributed_network_behavior": False,
            "selected_self_continuation_authorized_future_work": False,
            "selected_bounded_self_continuation_envelope_treated_as_self_recursive_growth": False,
            "selected_bounded_self_continuation_envelope_authorized_self_recursive_growth": False,
            "selected_bounded_self_continuation_envelope_authorized_runtime_daemon": False,
            "selected_bounded_self_continuation_envelope_authorized_runtime_loop": False,
            "selected_bounded_self_continuation_envelope_authorized_arbitrary_runtime_activity": False,
            "selected_runtime_hosting_boundary_v1_failure_repaired": False,
            "selected_runtime_hosting_boundary_v1_failure_hidden": False,
            "selected_runtime_hosting_boundary_v1_failure_claimed_passed": False,
            "raw_full_prior_artifact_body_returned": False,
        }
    )
    request.update(false_defaults)

    for key, value in overrides.items():
        if value == "__DELETE__":
            request.pop(key, None)
        else:
            request[key] = value
    return request

