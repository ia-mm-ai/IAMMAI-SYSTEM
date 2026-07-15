"""Post-minimal-runtime successor-runtime-step-boundary resolver.

This module records one bounded successor-runtime-step-boundary posture from a
clean minimal-runtime basis. It declares one future successor-runtime-step review
only. It does not create successor runtime step, runtime hosting, ongoing
runtime, reusable runtime permission, continuation, source transfer, source
receipt, reception authorization, source, authority, currentness, deployment,
public release, operation permission, reusable permission, adoption,
receiving-context governance, publication flow, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class PostMinimalRuntimeSuccessorRuntimeStepBoundaryError(Exception):
    """Bounded resolver error for successor-runtime-step-boundary inputs."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_post_minimal_runtime_successor_runtime_step_boundary"

OUTCOME_RECORDED = "POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_BOUNDARY_RECORDED"
OUTCOME_NOT_RECORDED = "POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_BOUNDARY_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_BOUNDARY_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = "RECORD_POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_BOUNDARY"
INTENT_BLOCK = "BLOCK_POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

EXPECTED_MINIMAL_RUNTIME_OUTCOME = "POST_PORTABLE_VERIFICATION_MINIMAL_RUNTIME_RECORDED"
EXPECTED_RUNTIME_BOUNDARY_OUTCOME = "POST_PORTABLE_VERIFICATION_RUNTIME_BOUNDARY_RECORDED"
EXPECTED_RUNTIME_READINESS_OUTCOME = "POST_PORTABLE_VERIFICATION_RUNTIME_READINESS_RECORDED"
EXPECTED_FINAL_COMPLETION_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_RECORDED"
)

CORE_QUESTION = (
    "Can the clean post-portable-verification minimal-runtime basis be bounded "
    "for one future successor-runtime-step review without creating successor "
    "runtime step, runtime hosting, ongoing runtime, reusable runtime permission, "
    "continuation beyond the previously recorded single bounded minimal-runtime "
    "step posture, source transfer, source receipt, reception authorization, "
    "source, authority, currentness, deployment, public release, operation "
    "permission, reusable permission, derivative reception, vessel relation, "
    "another reception request, adoption, receiving-context governance, "
    "publication flow, or follow-on work?"
)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_post_minimal_runtime_successor_runtime_step_boundary"
)

SUPPORTED_SCOPE_VALUES = (
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_SPEC_ONLY",
    "ONE_FUTURE_SUCCESSOR_RUNTIME_STEP_REVIEW_DECLARED",
    "MINIMAL_RUNTIME_BASIS_PRESERVED",
    "MINIMAL_RUNTIME_NOT_SUCCESSOR_RUNTIME_STEP",
    "BOUNDED_RUNTIME_RESULT_OR_REFUSAL_NOT_SUCCESSOR_AUTHORIZATION",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_NOT_SUCCESSOR_RUNTIME_STEP",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_NOT_RUNTIME_HOSTING",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_NOT_ONGOING_RUNTIME",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_NOT_CONTINUATION",
    "SUCCESSOR_RUNTIME_STEP_NOT_CREATED",
    "RUNTIME_HOSTING_NOT_CREATED",
    "ONGOING_RUNTIME_NOT_CREATED",
    "REUSABLE_RUNTIME_PERMISSION_NOT_CREATED",
    "NO_CONTINUATION_AUTHORIZED",
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
    "NO_SUCCESSOR_STEP_INFERENCE",
    "NO_RUNTIME_HOSTING_INFERENCE",
    "NO_ONGOING_RUNTIME_INFERENCE",
    "NO_CONTINUATION_INFERENCE",
    "NO_SOURCE_INFERENCE",
    "NO_AUTHORITY_INFERENCE",
    "NO_CURRENTNESS_INFERENCE",
    "NO_DEPLOYMENT_INFERENCE",
    "NO_PUBLIC_RELEASE_INFERENCE",
    "NO_OPERATION_PERMISSION_INFERENCE",
    "NO_FOLLOW_ON_WORK_INFERENCE",
    "NO_UNBOUNDED_PASS_FAIL_INFERENCE",
    "HIDDEN_REPO_STATE_EXCLUDED",
    "HIDDEN_REPO_STATE_NOT_USED_AS_SUCCESSOR_RUNTIME_STEP_BOUNDARY_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_NOT_SUCCESSOR_RUNTIME_STEP_BOUNDARY_AUTHORITY",
    "ARTIFACT_EXISTENCE_NOT_SUCCESSOR_RUNTIME_STEP_BOUNDARY_AUTHORITY",
    "LATEST_FILE_POSTURE_NOT_SUCCESSOR_RUNTIME_STEP_BOUNDARY_AUTHORITY",
    "SELECTED_BASIS_REFERENCE_SHAPE_PRESERVED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "PREDECESSOR_FAILURE_EVIDENCE_PRESERVED",
    "AUTHORIZATION_TOKEN_REUSE_BLOCKED",
    "CONSUMED_REQUEST_TOKEN_REMAINS_CLOSED",
    "CONSUMED_REQUEST_NOT_REOPENED",
)
SUPPORTED_SUCCESSOR_RUNTIME_STEP_BOUNDARY_SCOPE = SUPPORTED_SCOPE_VALUES

REQUIRED_FALSE_NON_CLAIMS = (
    "successor_runtime_step_created",
    "runtime_hosting_created",
    "ongoing_runtime_created",
    "reusable_runtime_permission_created",
    "continuation_authorized",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "successor_runtime_step_boundary_treated_as_successor_runtime_step",
    "successor_runtime_step_boundary_treated_as_runtime_hosting",
    "successor_runtime_step_boundary_treated_as_ongoing_runtime",
    "successor_runtime_step_boundary_treated_as_continuation",
    "successor_runtime_step_boundary_treated_as_source_transfer",
    "successor_runtime_step_boundary_treated_as_source_receipt",
    "successor_runtime_step_boundary_treated_as_reception_authorization",
    "successor_runtime_step_boundary_treated_as_source",
    "successor_runtime_step_boundary_treated_as_authority",
    "successor_runtime_step_boundary_treated_as_currentness",
    "successor_runtime_step_boundary_treated_as_deployment",
    "successor_runtime_step_boundary_treated_as_public_release",
    "successor_runtime_step_boundary_treated_as_operation_permission",
    "successor_runtime_step_boundary_treated_as_reusable_permission",
    "successor_runtime_step_boundary_treated_as_follow_on_work",
    "minimal_runtime_treated_as_successor_runtime_step",
    "minimal_runtime_treated_as_runtime_hosting",
    "minimal_runtime_treated_as_ongoing_runtime",
    "minimal_runtime_treated_as_continuation",
    "bounded_runtime_result_or_refusal_authorized_successor",
    "artifact_existence_treated_as_successor_runtime_step_boundary_authority",
    "artifact_path_treated_as_currentness",
    "latest_file_posture_treated_as_successor_runtime_step_boundary_authority",
    "repo_local_availability_treated_as_successor_runtime_step_boundary_authority",
    "hidden_repo_state_used_as_successor_runtime_step_boundary_content",
    "hidden_repo_state_used_as_successor_runtime_step_boundary_authority",
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
    "successor_runtime_step_boundary_recorded",
    "one_future_successor_runtime_step_review_declared",
    "minimal_runtime_basis_preserved",
    "minimal_runtime_not_successor_runtime_step",
    "bounded_runtime_result_or_refusal_not_successor_authorization",
    "successor_runtime_step_boundary_not_successor_runtime_step",
    "successor_runtime_step_boundary_not_runtime_hosting",
    "successor_runtime_step_boundary_not_ongoing_runtime",
    "successor_runtime_step_boundary_not_continuation",
    "successor_runtime_step_not_created",
    "runtime_hosting_not_created",
    "ongoing_runtime_not_created",
    "reusable_runtime_permission_not_created",
    "continuation_not_authorized",
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
    "hidden_repo_state_not_used_as_successor_runtime_step_boundary_authority",
    "repo_local_availability_not_successor_runtime_step_boundary_authority",
    "artifact_existence_not_successor_runtime_step_boundary_authority",
    "latest_file_posture_not_successor_runtime_step_boundary_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "official_enum_scope_strings_not_redacted",
    "hostile_raw_body_content_contained",
    "predecessor_failure_evidence_preserved",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
)

BLOCK_CODES = (
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_QUESTION_UNDECLARED",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_INTENT_UNSUPPORTED",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_REQUEST_DECLARED_BLOCK",
    "MINIMAL_RUNTIME_BASIS_MISSING",
    "MINIMAL_RUNTIME_NOT_RECORDED",
    "MINIMAL_RUNTIME_FAILED_CHECKS_PRESENT",
    "MINIMAL_RUNTIME_VERSION_NOT_0_1_0",
    "MINIMAL_RUNTIME_DID_NOT_RECORD_BOUNDED_MINIMAL_RUNTIME_STEP",
    "MINIMAL_RUNTIME_DID_NOT_RECORD_BOUNDED_RESULT_OR_REFUSAL",
    "MINIMAL_RUNTIME_ALREADY_CREATED_RUNTIME_HOSTING",
    "MINIMAL_RUNTIME_ALREADY_CREATED_ONGOING_RUNTIME",
    "MINIMAL_RUNTIME_ALREADY_CREATED_SUCCESSOR_RUNTIME_STEP",
    "MINIMAL_RUNTIME_ALREADY_AUTHORIZED_CONTINUATION_BEYOND_SINGLE_STEP",
    "MINIMAL_RUNTIME_TREATED_AS_RUNTIME_HOSTING",
    "MINIMAL_RUNTIME_TREATED_AS_ONGOING_RUNTIME",
    "MINIMAL_RUNTIME_TREATED_AS_SUCCESSOR_RUNTIME_STEP",
    "MINIMAL_RUNTIME_TREATED_AS_CONTINUATION",
    "MINIMAL_RUNTIME_AUTHORIZED_FUTURE_WORK",
    "BOUNDED_RUNTIME_RESULT_OR_REFUSAL_AUTHORIZED_SUCCESSOR",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_CREATED_BEFORE_REVIEW",
    "SUCCESSOR_RUNTIME_STEP_CREATED",
    "RUNTIME_HOSTING_CREATED",
    "ONGOING_RUNTIME_CREATED",
    "REUSABLE_RUNTIME_PERMISSION_CREATED",
    "CONTINUATION_AUTHORIZED",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_SUCCESSOR_RUNTIME_STEP",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_RUNTIME_HOSTING",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_ONGOING_RUNTIME",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_CONTINUATION",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_SOURCE",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_AUTHORITY",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_CURRENTNESS",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_DEPLOYMENT",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_PUBLIC_RELEASE",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_OPERATION_PERMISSION",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_SUCCESSOR_RUNTIME_STEP_BOUNDARY_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "LATEST_FILE_POSTURE_TREATED_AS_SUCCESSOR_RUNTIME_STEP_BOUNDARY_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_SUCCESSOR_RUNTIME_STEP_BOUNDARY_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_SUCCESSOR_RUNTIME_STEP_BOUNDARY_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_SUCCESSOR_RUNTIME_STEP_BOUNDARY_AUTHORITY",
    "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "PRIOR_ARTIFACTS_MUTATED",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_SUCCESSOR_RUNTIME_STEP_BOUNDARY_SCOPE",
    "DECLARED_SUCCESSOR_RUNTIME_STEP_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_SUCCESSOR_RUNTIME_STEP_BOUNDARY_REQUEST_UNREADABLE",
)

SELECTED_BASIS_FIELDS = (
    "selected_minimal_runtime_basis",
    "selected_minimal_runtime_terminal_summary_basis",
    "selected_runtime_boundary_basis",
    "selected_runtime_readiness_basis",
    "selected_portable_verification_final_completion_basis",
    "selected_post_portable_verification_currentness_basis",
    "selected_returned_second_carrier_capture_lineage_basis",
)

POSTURE_FIELDS = (
    "successor_runtime_step_boundary_spec_only_posture",
    "one_future_successor_runtime_step_review_posture",
    "minimal_runtime_basis_preserved_posture",
    "minimal_runtime_not_successor_runtime_step_posture",
    "bounded_runtime_result_or_refusal_not_successor_authorization_posture",
    "successor_runtime_step_boundary_not_successor_runtime_step_posture",
    "successor_runtime_step_boundary_not_runtime_hosting_posture",
    "successor_runtime_step_boundary_not_ongoing_runtime_posture",
    "successor_runtime_step_boundary_not_continuation_posture",
    "successor_runtime_step_not_created_posture",
    "runtime_hosting_not_created_posture",
    "ongoing_runtime_not_created_posture",
    "reusable_runtime_permission_not_created_posture",
    "continuation_not_authorized_posture",
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
    "repo_local_availability_not_successor_runtime_step_boundary_authority_posture",
    "artifact_existence_not_successor_runtime_step_boundary_authority_posture",
    "latest_file_posture_not_successor_runtime_step_boundary_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
)

SECTION_NAMES = (
    "post_minimal_runtime_successor_runtime_step_boundary_metadata",
    "declared_successor_runtime_step_boundary_question",
    "successor_runtime_step_boundary_scope",
    "successor_runtime_step_boundary_checks",
    "successor_runtime_step_boundary_statement",
    "successor_runtime_step_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "post_minimal_runtime_successor_runtime_step_boundary_summary",
) + SELECTED_BASIS_FIELDS + POSTURE_FIELDS

SENSITIVE_CONTENT_KEYS = frozenset(
    {
        "raw_body",
        "raw_full_body",
        "full_body",
        "artifact_body",
        "raw_result_body",
        "raw_output_body",
        "raw_capture_body",
        "raw_success_body",
        "raw_verification_body",
        "raw_external_result_body",
        "raw_cross_carrier_evidence_body",
        "raw_portable_verification_closure_body",
        "raw_final_completion_body",
        "raw_runtime_readiness_boundary_body",
        "raw_runtime_readiness_body",
        "raw_runtime_boundary_body",
        "raw_minimal_runtime_body",
        "raw_successor_runtime_step_boundary_body",
        "raw_successor_runtime_step_body",
        "raw_runtime_hosting_body",
        "raw_ongoing_runtime_body",
        "raw_runtime_body",
        "capture_body",
        "runtime_readiness_body",
        "runtime_boundary_body",
        "minimal_runtime_body",
        "successor_runtime_step_boundary_body",
        "successor_runtime_step_body",
        "runtime_hosting_body",
        "ongoing_runtime_body",
        "runtime_body",
        "source_body",
        "authority_body",
        "hidden_repo_state",
        "current_working_tree",
        "local_cache",
        "repo_local_only_dependency",
    }
)

HOSTILE_SENTINELS = (
    "RAW_SUCCESSOR_RUNTIME_STEP_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_SUCCESSOR_RUNTIME_STEP_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HOSTING_BODY_MUST_NOT_RETURN",
    "RAW_ONGOING_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)

OFFICIAL_STRINGS = frozenset(
    SUPPORTED_SCOPE_VALUES
    + OUTCOME_FAMILY
    + BLOCK_CODES
    + SUPPORTED_INTENTS
    + tuple(REQUIRED_FALSE_NON_CLAIMS)
    + tuple(ALLOWED_TRUE_RECORDED_FIELDS)
    + SECTION_NAMES
    + (
        RESOLVER_MODULE,
        RESULT_VERSION,
        CORE_QUESTION,
        EXPECTED_MINIMAL_RUNTIME_OUTCOME,
        EXPECTED_RUNTIME_BOUNDARY_OUTCOME,
        EXPECTED_RUNTIME_READINESS_OUTCOME,
        EXPECTED_FINAL_COMPLETION_OUTCOME,
    )
)

FALSE_CHECK_FIELD_CODES = (
    (
        "successor_runtime_step_boundary_created_before_review",
        "SUCCESSOR_RUNTIME_STEP_BOUNDARY_CREATED_BEFORE_REVIEW",
    ),
    ("successor_runtime_step_created", "SUCCESSOR_RUNTIME_STEP_CREATED"),
    ("runtime_hosting_created", "RUNTIME_HOSTING_CREATED"),
    ("ongoing_runtime_created", "ONGOING_RUNTIME_CREATED"),
    ("reusable_runtime_permission_created", "REUSABLE_RUNTIME_PERMISSION_CREATED"),
    ("continuation_authorized", "CONTINUATION_AUTHORIZED"),
    ("source_transfer_occurred", "SOURCE_TRANSFER_OCCURRED"),
    ("source_receipt_occurred", "SOURCE_RECEIPT_OCCURRED"),
    ("reception_authorization_created", "RECEPTION_AUTHORIZATION_CREATED"),
    (
        "successor_runtime_step_boundary_treated_as_successor_runtime_step",
        "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_SUCCESSOR_RUNTIME_STEP",
    ),
    (
        "successor_runtime_step_boundary_treated_as_runtime_hosting",
        "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_RUNTIME_HOSTING",
    ),
    (
        "successor_runtime_step_boundary_treated_as_ongoing_runtime",
        "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_ONGOING_RUNTIME",
    ),
    (
        "successor_runtime_step_boundary_treated_as_continuation",
        "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_CONTINUATION",
    ),
    (
        "successor_runtime_step_boundary_treated_as_source_transfer",
        "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    ),
    (
        "successor_runtime_step_boundary_treated_as_source_receipt",
        "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    ),
    (
        "successor_runtime_step_boundary_treated_as_reception_authorization",
        "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    ),
    (
        "successor_runtime_step_boundary_treated_as_source",
        "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_SOURCE",
    ),
    (
        "successor_runtime_step_boundary_treated_as_authority",
        "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_AUTHORITY",
    ),
    (
        "successor_runtime_step_boundary_treated_as_currentness",
        "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_CURRENTNESS",
    ),
    (
        "successor_runtime_step_boundary_treated_as_deployment",
        "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_DEPLOYMENT",
    ),
    (
        "successor_runtime_step_boundary_treated_as_public_release",
        "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_PUBLIC_RELEASE",
    ),
    (
        "successor_runtime_step_boundary_treated_as_operation_permission",
        "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_OPERATION_PERMISSION",
    ),
    (
        "successor_runtime_step_boundary_treated_as_reusable_permission",
        "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION",
    ),
    (
        "successor_runtime_step_boundary_treated_as_follow_on_work",
        "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
    ),
    (
        "minimal_runtime_treated_as_successor_runtime_step",
        "MINIMAL_RUNTIME_TREATED_AS_SUCCESSOR_RUNTIME_STEP",
    ),
    (
        "minimal_runtime_treated_as_repeatability",
        "MINIMAL_RUNTIME_TREATED_AS_SUCCESSOR_RUNTIME_STEP",
    ),
    (
        "minimal_runtime_treated_as_runtime_hosting",
        "MINIMAL_RUNTIME_TREATED_AS_RUNTIME_HOSTING",
    ),
    (
        "minimal_runtime_treated_as_ongoing_runtime",
        "MINIMAL_RUNTIME_TREATED_AS_ONGOING_RUNTIME",
    ),
    ("minimal_runtime_treated_as_continuation", "MINIMAL_RUNTIME_TREATED_AS_CONTINUATION"),
    (
        "bounded_runtime_result_or_refusal_authorized_successor",
        "BOUNDED_RUNTIME_RESULT_OR_REFUSAL_AUTHORIZED_SUCCESSOR",
    ),
    (
        "artifact_existence_treated_as_successor_runtime_step_boundary_authority",
        "ARTIFACT_EXISTENCE_TREATED_AS_SUCCESSOR_RUNTIME_STEP_BOUNDARY_AUTHORITY",
    ),
    ("artifact_path_treated_as_currentness", "ARTIFACT_PATH_TREATED_AS_CURRENTNESS"),
    (
        "latest_file_posture_treated_as_successor_runtime_step_boundary_authority",
        "LATEST_FILE_POSTURE_TREATED_AS_SUCCESSOR_RUNTIME_STEP_BOUNDARY_AUTHORITY",
    ),
    (
        "repo_local_availability_treated_as_successor_runtime_step_boundary_authority",
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_SUCCESSOR_RUNTIME_STEP_BOUNDARY_AUTHORITY",
    ),
    (
        "hidden_repo_state_used_as_successor_runtime_step_boundary_content",
        "HIDDEN_REPO_STATE_USED_AS_SUCCESSOR_RUNTIME_STEP_BOUNDARY_CONTENT",
    ),
    (
        "hidden_repo_state_used_as_successor_runtime_step_boundary_authority",
        "HIDDEN_REPO_STATE_USED_AS_SUCCESSOR_RUNTIME_STEP_BOUNDARY_AUTHORITY",
    ),
    ("selected_basis_not_reference_shaped", "SELECTED_BASIS_NOT_REFERENCE_SHAPED"),
    ("source_created", "SOURCE_CREATED"),
    ("authority_created", "AUTHORITY_CREATED"),
    ("currentness_created", "CURRENTNESS_CREATED"),
    ("deployment_created", "DEPLOYMENT_CREATED"),
    ("public_release_created", "PUBLIC_RELEASE_CREATED"),
    ("operation_permission_created", "OPERATION_PERMISSION_CREATED"),
    ("reusable_permission_created", "REUSABLE_PERMISSION_CREATED"),
    ("derivative_reception_authorized", "DERIVATIVE_RECEPTION_AUTHORIZED"),
    ("vessel_relation_authorized", "VESSEL_RELATION_AUTHORIZED"),
    ("another_reception_request_authorized", "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"),
    ("adoption_created", "ADOPTION_CREATED"),
    ("receiving_context_governance_created", "RECEIVING_CONTEXT_GOVERNANCE_CREATED"),
    ("publication_flow_created", "PUBLICATION_FLOW_CREATED"),
    ("follow_on_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
    ("raw_full_prior_artifact_body_returned", "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED"),
    ("prior_artifacts_mutated", "PRIOR_ARTIFACTS_MUTATED"),
    ("consumed_request_reopened", "CONSUMED_REQUEST_REOPENED"),
    ("authorization_token_reused", "AUTHORIZATION_TOKEN_REUSED"),
    ("predecessor_failure_repaired", "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
    ("predecessor_failure_hidden", "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
    (
        "predecessor_failure_claimed_passed",
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    ),
)

PROHIBITED_OUTPUT_PATH_MARKERS = (
    "integrity_host_v0_min_coexistence_post_portable_verification_minimal_runtime/",
    "integrity_host_v0_min_coexistence_post_portable_verification_runtime_boundary/",
    "integrity_host_v0_min_coexistence_post_portable_verification_runtime_readiness/",
    "integrity_host_v0_min_coexistence_post_portable_verification_runtime_readiness_boundary/",
    "integrity_host_v0_min_coexistence_portable_source_body_verification_final_completion/",
    "integrity_host_v0_min_coexistence_portable_source_body_verification_final_completion_boundary/",
    "integrity_host_v0_min_coexistence_portable_source_body_verification_portable_verification_closure/",
    "integrity_host_v0_min_coexistence_portable_verification_closure_boundary/",
    "integrity_host_v0_min_coexistence_portable_source_body_verification_cross_carrier_evidence/",
    "second_carrier_external_result",
    "second_carrier_verification",
    "second_carrier_success",
    "second_carrier_result",
    "actual_second_carrier_live_capture",
    "second_carrier_output_capture",
    "packet_transfer",
    "packet-transfer",
    "packet_emission",
    "packet-emission",
    "command_success",
    "command-success",
    "command_result",
    "command-result",
    "source_transfer",
    "source-transfer",
    "source_receipt",
    "source-receipt",
    "reception",
    "runtime_hosting",
    "runtime-hosting",
    "ongoing_runtime",
    "ongoing-runtime",
    "deployment",
    "public_release",
    "public-release",
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _is_mapping(value: Any) -> bool:
    return hasattr(value, "items") and hasattr(value, "get")


def _deepcopy_mapping(value: Mapping[str, Any]) -> dict[str, Any]:
    return copy.deepcopy(dict(value))


def _safe_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _is_sensitive_key(key: Any) -> bool:
    if not isinstance(key, str):
        return False
    return key in SENSITIVE_CONTENT_KEYS or key.endswith("_body")


def _sanitize(value: Any, key: str | None = None) -> Any:
    if isinstance(value, str):
        if value in OFFICIAL_STRINGS:
            return value
        if key is not None and _is_sensitive_key(key):
            return "[bounded-redacted-raw-or-hidden-state]"
        if any(sentinel in value for sentinel in HOSTILE_SENTINELS):
            return "[bounded-redacted-raw-or-hidden-state]"
        return value
    if isinstance(value, bool) or value is None or isinstance(value, (int, float)):
        return value
    if _is_mapping(value):
        sanitized: dict[str, Any] = {}
        for raw_key, raw_value in value.items():
            safe_key = str(raw_key)
            if _is_sensitive_key(safe_key):
                if isinstance(raw_value, str) and raw_value in OFFICIAL_STRINGS:
                    sanitized[safe_key] = raw_value
                else:
                    sanitized[safe_key] = "[bounded-redacted-raw-or-hidden-state]"
            else:
                sanitized[safe_key] = _sanitize(raw_value, safe_key)
        return sanitized
    if isinstance(value, (list, tuple)):
        return [_sanitize(item, key) for item in value]
    return str(value)


def _as_int(value: Any, default: int | None = None) -> int | None:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            return default
    return default


def _present(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, tuple, dict)):
        return bool(value)
    return True


def _find_key(value: Any, key: str, depth: int = 5) -> Any:
    if depth < 0:
        return None
    if _is_mapping(value):
        if key in value:
            return value.get(key)
        for nested in value.values():
            found = _find_key(nested, key, depth - 1)
            if found is not None:
                return found
    elif isinstance(value, (list, tuple)):
        for nested in value:
            found = _find_key(nested, key, depth - 1)
            if found is not None:
                return found
    return None


def _value_from_request_or_basis(
    request: Mapping[str, Any],
    request_key: str,
    basis_key: str,
    basis_section: str,
    default: Any = None,
) -> Any:
    if request_key in request:
        return request.get(request_key)
    basis = request.get(basis_section)
    found = _find_key(basis, basis_key)
    if found is not None:
        return found
    return default


def _check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    block_code: str,
) -> dict[str, Any]:
    record: dict[str, Any] = {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": _sanitize(expected_posture),
        "actual_posture": _sanitize(actual_posture),
    }
    if passed:
        record["failure_code"] = None
        record["block_code"] = None
    else:
        record["failure_code"] = block_code
        record["block_code"] = block_code
    return record


def _add_check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    block_code: str,
) -> None:
    checks.append(_check(check_name, passed, expected_posture, actual_posture, block_code))


def _scope_values(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if _is_mapping(value):
        return [str(item) for item, included in value.items() if included is True]
    if isinstance(value, (list, tuple, set)):
        return [str(item) for item in value]
    return []


def _posture(name: str, declared: bool = True) -> dict[str, Any]:
    return {
        "posture_name": name,
        "declared": bool(declared),
        "preserved": bool(declared),
        "bounded_successor_runtime_step_boundary_only": True,
        "creates_successor_runtime_step": False,
        "creates_runtime_hosting": False,
        "creates_ongoing_runtime": False,
        "authorizes_continuation": False,
    }


def _default_basis(name: str, path: str, **extra: Any) -> dict[str, Any]:
    basis = {
        "basis_name": name,
        "basis_path": path,
        "basis_posture": "reference-shaped selected basis only",
        "selected_basis_reference_shape_preserved": True,
        "raw_full_prior_artifact_body_not_returned": True,
        "hidden_repo_state_excluded": True,
    }
    basis.update(extra)
    return basis


def _statement(recorded: bool) -> dict[str, bool]:
    statement = {key: True for key in ALLOWED_TRUE_RECORDED_FIELDS}
    statement["successor_runtime_step_boundary_recorded"] = bool(recorded)
    statement["one_future_successor_runtime_step_review_declared"] = bool(recorded)
    return statement


def _non_meaning() -> dict[str, bool]:
    return {
        "successor_runtime_step_boundary_is_successor_runtime_step": False,
        "successor_runtime_step_boundary_is_runtime_hosting": False,
        "successor_runtime_step_boundary_is_ongoing_runtime": False,
        "successor_runtime_step_boundary_is_continuation": False,
        "successor_runtime_step_boundary_is_source_transfer": False,
        "successor_runtime_step_boundary_is_source_receipt": False,
        "successor_runtime_step_boundary_is_reception_authorization": False,
        "successor_runtime_step_boundary_is_source": False,
        "successor_runtime_step_boundary_is_authority": False,
        "successor_runtime_step_boundary_is_currentness": False,
        "successor_runtime_step_boundary_is_deployment": False,
        "successor_runtime_step_boundary_is_public_release": False,
        "successor_runtime_step_boundary_is_operation_permission": False,
        "successor_runtime_step_boundary_is_reusable_permission": False,
        "successor_runtime_step_boundary_is_follow_on_work": False,
        "minimal_runtime_is_successor_runtime_step": False,
        "minimal_runtime_is_runtime_hosting": False,
        "minimal_runtime_is_ongoing_runtime": False,
        "minimal_runtime_is_continuation": False,
        "bounded_runtime_result_or_refusal_is_successor_authorization": False,
        "successor_runtime_step_exists_here": False,
        "runtime_hosting_exists_here": False,
        "ongoing_runtime_exists_here": False,
        "reusable_runtime_permission_exists_here": False,
        "continuation_authorized_here": False,
        "artifact_existence_is_successor_runtime_step_boundary_authority": False,
        "repo_local_availability_is_successor_runtime_step_boundary_authority": False,
        "latest_file_posture_is_successor_runtime_step_boundary_authority": False,
        "hidden_repo_state_is_successor_runtime_step_boundary_authority": False,
    }


def _what_remains_open() -> list[str]:
    return [
        "successor-runtime-step-boundary test",
        "successor-runtime-step-boundary live artifact",
        "successor-runtime-step-boundary terminal summary, if needed",
        "successor-runtime-step specification",
        "successor-runtime-step resolver/test/live artifact",
        "runtime hosting",
        "ongoing runtime",
        "continuation beyond bounded steps",
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


def _block_from_checks(
    checks: list[dict[str, Any]], requested_reason: Any = None
) -> dict[str, Any] | None:
    for check_record in checks:
        if check_record.get("passed") is False:
            return {
                "blocked": True,
                "block_code": check_record.get("block_code"),
                "block_reason": _sanitize(
                    requested_reason
                    if _present(requested_reason)
                    else check_record.get("actual_posture")
                ),
            }
    return None


def _basis_present(request: Mapping[str, Any], field: str, shortcut_path: str | None) -> bool:
    return _present(request.get(field)) or _present(request.get(shortcut_path or ""))


def _add_false_basis_check(
    checks: list[dict[str, Any]],
    request: Mapping[str, Any],
    check_name: str,
    request_key: str,
    basis_key: str,
    basis_section: str,
    block_code: str,
) -> None:
    actual = _value_from_request_or_basis(request, request_key, basis_key, basis_section, False)
    _add_check(checks, check_name, actual is False, False, actual, block_code)


def _add_boundary_checks(
    request: Mapping[str, Any],
    forced_block_code: str | None = None,
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    if forced_block_code is not None:
        _add_check(
            checks,
            "declared successor-runtime-step-boundary request shape",
            False,
            "well-formed mapping request",
            forced_block_code,
            forced_block_code,
        )
        return checks

    question = request.get("successor_runtime_step_boundary_question")
    intent = request.get("successor_runtime_step_boundary_intent")
    scope = _scope_values(request.get("successor_runtime_step_boundary_scope"))
    unsupported_scope = [value for value in scope if value not in SUPPORTED_SCOPE_VALUES]

    _add_check(
        checks,
        "successor-runtime-step-boundary question declared",
        question == CORE_QUESTION,
        CORE_QUESTION,
        question,
        "SUCCESSOR_RUNTIME_STEP_BOUNDARY_QUESTION_UNDECLARED",
    )
    _add_check(
        checks,
        "intent supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "SUCCESSOR_RUNTIME_STEP_BOUNDARY_INTENT_UNSUPPORTED",
    )
    _add_check(
        checks,
        "explicit block intent not selected",
        intent != INTENT_BLOCK,
        "successor-runtime-step-boundary request is not declared blocked",
        intent,
        "SUCCESSOR_RUNTIME_STEP_BOUNDARY_REQUEST_DECLARED_BLOCK",
    )
    _add_check(
        checks,
        "successor-runtime-step-boundary scope supported",
        bool(scope) and not unsupported_scope,
        SUPPORTED_SCOPE_VALUES,
        unsupported_scope or scope,
        "UNSUPPORTED_SUCCESSOR_RUNTIME_STEP_BOUNDARY_SCOPE",
    )

    minimal_basis_declared = _basis_present(
        request, "selected_minimal_runtime_basis", "selected_minimal_runtime_result_path"
    )
    minimal_terminal_declared = _basis_present(
        request, "selected_minimal_runtime_terminal_summary_basis", None
    )
    _add_check(
        checks,
        "minimal-runtime basis declared",
        minimal_basis_declared and minimal_terminal_declared,
        "minimal-runtime basis and terminal summary declared",
        {
            "selected_minimal_runtime_basis": minimal_basis_declared,
            "selected_minimal_runtime_terminal_summary_basis": minimal_terminal_declared,
        },
        "MINIMAL_RUNTIME_BASIS_MISSING",
    )
    minimal_outcome = _value_from_request_or_basis(
        request,
        "selected_minimal_runtime_result_outcome",
        "outcome",
        "selected_minimal_runtime_basis",
    )
    _add_check(
        checks,
        "minimal-runtime outcome recorded",
        minimal_outcome == EXPECTED_MINIMAL_RUNTIME_OUTCOME,
        EXPECTED_MINIMAL_RUNTIME_OUTCOME,
        minimal_outcome,
        "MINIMAL_RUNTIME_NOT_RECORDED",
    )
    minimal_version = _value_from_request_or_basis(
        request,
        "selected_minimal_runtime_result_version",
        "result_version",
        "selected_minimal_runtime_basis",
    )
    _add_check(
        checks,
        "minimal-runtime version 0.1.0",
        minimal_version == RESULT_VERSION,
        RESULT_VERSION,
        minimal_version,
        "MINIMAL_RUNTIME_VERSION_NOT_0_1_0",
    )
    minimal_failed_count = _as_int(
        _value_from_request_or_basis(
            request,
            "selected_minimal_runtime_failed_check_count",
            "failed_check_count",
            "selected_minimal_runtime_basis",
        )
    )
    _add_check(
        checks,
        "minimal-runtime failed checks zero",
        minimal_failed_count == 0,
        0,
        minimal_failed_count,
        "MINIMAL_RUNTIME_FAILED_CHECKS_PRESENT",
    )
    bounded_step_recorded = _value_from_request_or_basis(
        request,
        "selected_minimal_runtime_bounded_minimal_runtime_step_recorded",
        "bounded_minimal_runtime_step_recorded",
        "selected_minimal_runtime_basis",
    )
    _add_check(
        checks,
        "minimal-runtime recorded bounded minimal-runtime step",
        bounded_step_recorded is True,
        True,
        bounded_step_recorded,
        "MINIMAL_RUNTIME_DID_NOT_RECORD_BOUNDED_MINIMAL_RUNTIME_STEP",
    )
    bounded_result_recorded = _value_from_request_or_basis(
        request,
        "selected_minimal_runtime_bounded_runtime_result_or_refusal_recorded",
        "bounded_minimal_runtime_result_or_refusal",
        "selected_minimal_runtime_basis",
    )
    _add_check(
        checks,
        "minimal-runtime recorded bounded runtime result/refusal posture",
        bounded_result_recorded is True,
        True,
        bounded_result_recorded,
        "MINIMAL_RUNTIME_DID_NOT_RECORD_BOUNDED_RESULT_OR_REFUSAL",
    )
    no_successor_authorized = _value_from_request_or_basis(
        request,
        "selected_minimal_runtime_no_successor_action_authorized",
        "no_successor_action_authorized",
        "selected_minimal_runtime_basis",
    )
    _add_check(
        checks,
        "minimal-runtime did not authorize successor action",
        no_successor_authorized is True,
        True,
        no_successor_authorized,
        "BOUNDED_RUNTIME_RESULT_OR_REFUSAL_AUTHORIZED_SUCCESSOR",
    )

    minimal_false_checks = (
        (
            "minimal-runtime did not create runtime hosting",
            "selected_minimal_runtime_already_created_runtime_hosting",
            "runtime_hosting_created",
            "MINIMAL_RUNTIME_ALREADY_CREATED_RUNTIME_HOSTING",
        ),
        (
            "minimal-runtime did not create ongoing runtime",
            "selected_minimal_runtime_already_created_ongoing_runtime",
            "ongoing_runtime_created",
            "MINIMAL_RUNTIME_ALREADY_CREATED_ONGOING_RUNTIME",
        ),
        (
            "minimal-runtime did not create successor runtime step",
            "selected_minimal_runtime_already_created_successor_runtime_step",
            "successor_runtime_step_created",
            "MINIMAL_RUNTIME_ALREADY_CREATED_SUCCESSOR_RUNTIME_STEP",
        ),
        (
            "minimal-runtime did not authorize continuation beyond single step",
            "selected_minimal_runtime_already_authorized_continuation_beyond_single_step",
            "continuation_beyond_single_step_authorized",
            "MINIMAL_RUNTIME_ALREADY_AUTHORIZED_CONTINUATION_BEYOND_SINGLE_STEP",
        ),
        (
            "minimal-runtime did not treat minimal runtime as runtime hosting",
            "selected_minimal_runtime_treated_as_runtime_hosting",
            "minimal_runtime_treated_as_runtime_hosting",
            "MINIMAL_RUNTIME_TREATED_AS_RUNTIME_HOSTING",
        ),
        (
            "minimal-runtime did not treat minimal runtime as ongoing runtime",
            "selected_minimal_runtime_treated_as_ongoing_runtime",
            "minimal_runtime_treated_as_ongoing_runtime",
            "MINIMAL_RUNTIME_TREATED_AS_ONGOING_RUNTIME",
        ),
        (
            "minimal-runtime did not treat minimal runtime as successor runtime step",
            "selected_minimal_runtime_treated_as_successor_runtime_step",
            "minimal_runtime_treated_as_successor_runtime_step",
            "MINIMAL_RUNTIME_TREATED_AS_SUCCESSOR_RUNTIME_STEP",
        ),
        (
            "minimal-runtime did not treat minimal runtime as continuation",
            "selected_minimal_runtime_treated_as_continuation",
            "minimal_runtime_treated_as_continuation",
            "MINIMAL_RUNTIME_TREATED_AS_CONTINUATION",
        ),
        (
            "minimal-runtime did not authorize future work",
            "selected_minimal_runtime_authorized_future_work",
            "follow_on_work_authorized",
            "MINIMAL_RUNTIME_AUTHORIZED_FUTURE_WORK",
        ),
        (
            "bounded runtime result/refusal did not authorize successor",
            "selected_bounded_runtime_result_or_refusal_authorized_successor",
            "bounded_runtime_result_or_refusal_authorized_successor",
            "BOUNDED_RUNTIME_RESULT_OR_REFUSAL_AUTHORIZED_SUCCESSOR",
        ),
    )
    for name, request_key, basis_key, code in minimal_false_checks:
        _add_false_basis_check(
            checks, request, name, request_key, basis_key, "selected_minimal_runtime_basis", code
        )

    runtime_boundary_declared = _basis_present(
        request, "selected_runtime_boundary_basis", "selected_runtime_boundary_result_path"
    )
    _add_check(
        checks,
        "runtime-boundary basis declared",
        runtime_boundary_declared,
        "runtime-boundary basis declared",
        runtime_boundary_declared,
        "MINIMAL_RUNTIME_BASIS_MISSING",
    )
    runtime_boundary_outcome = _value_from_request_or_basis(
        request,
        "selected_runtime_boundary_result_outcome",
        "outcome",
        "selected_runtime_boundary_basis",
    )
    _add_check(
        checks,
        "runtime-boundary outcome recorded",
        runtime_boundary_outcome == EXPECTED_RUNTIME_BOUNDARY_OUTCOME,
        EXPECTED_RUNTIME_BOUNDARY_OUTCOME,
        runtime_boundary_outcome,
        "MINIMAL_RUNTIME_BASIS_MISSING",
    )
    runtime_boundary_version = _value_from_request_or_basis(
        request,
        "selected_runtime_boundary_result_version",
        "result_version",
        "selected_runtime_boundary_basis",
    )
    _add_check(
        checks,
        "runtime-boundary version 0.1.0",
        runtime_boundary_version == RESULT_VERSION,
        RESULT_VERSION,
        runtime_boundary_version,
        "MINIMAL_RUNTIME_BASIS_MISSING",
    )
    runtime_boundary_failed_count = _as_int(
        _value_from_request_or_basis(
            request,
            "selected_runtime_boundary_failed_check_count",
            "failed_check_count",
            "selected_runtime_boundary_basis",
        )
    )
    _add_check(
        checks,
        "runtime-boundary failed checks zero",
        runtime_boundary_failed_count == 0,
        0,
        runtime_boundary_failed_count,
        "MINIMAL_RUNTIME_BASIS_MISSING",
    )

    runtime_readiness_declared = _basis_present(
        request, "selected_runtime_readiness_basis", "selected_runtime_readiness_result_path"
    )
    _add_check(
        checks,
        "runtime-readiness basis declared",
        runtime_readiness_declared,
        "runtime-readiness basis declared",
        runtime_readiness_declared,
        "MINIMAL_RUNTIME_BASIS_MISSING",
    )
    runtime_readiness_outcome = _value_from_request_or_basis(
        request,
        "selected_runtime_readiness_result_outcome",
        "outcome",
        "selected_runtime_readiness_basis",
    )
    _add_check(
        checks,
        "runtime-readiness outcome recorded",
        runtime_readiness_outcome == EXPECTED_RUNTIME_READINESS_OUTCOME,
        EXPECTED_RUNTIME_READINESS_OUTCOME,
        runtime_readiness_outcome,
        "MINIMAL_RUNTIME_BASIS_MISSING",
    )
    runtime_readiness_version = _value_from_request_or_basis(
        request,
        "selected_runtime_readiness_result_version",
        "result_version",
        "selected_runtime_readiness_basis",
    )
    _add_check(
        checks,
        "runtime-readiness version 0.1.0",
        runtime_readiness_version == RESULT_VERSION,
        RESULT_VERSION,
        runtime_readiness_version,
        "MINIMAL_RUNTIME_BASIS_MISSING",
    )
    runtime_readiness_failed_count = _as_int(
        _value_from_request_or_basis(
            request,
            "selected_runtime_readiness_failed_check_count",
            "failed_check_count",
            "selected_runtime_readiness_basis",
        )
    )
    _add_check(
        checks,
        "runtime-readiness failed checks zero",
        runtime_readiness_failed_count == 0,
        0,
        runtime_readiness_failed_count,
        "MINIMAL_RUNTIME_BASIS_MISSING",
    )

    final_completion_declared = _basis_present(
        request,
        "selected_portable_verification_final_completion_basis",
        "selected_portable_verification_final_completion_result_path",
    )
    _add_check(
        checks,
        "portable verification final-completion basis declared",
        final_completion_declared,
        "portable verification final-completion basis declared",
        final_completion_declared,
        "MINIMAL_RUNTIME_BASIS_MISSING",
    )
    final_completion_outcome = _value_from_request_or_basis(
        request,
        "selected_portable_verification_final_completion_result_outcome",
        "outcome",
        "selected_portable_verification_final_completion_basis",
    )
    _add_check(
        checks,
        "portable verification final-completion outcome recorded",
        final_completion_outcome == EXPECTED_FINAL_COMPLETION_OUTCOME,
        EXPECTED_FINAL_COMPLETION_OUTCOME,
        final_completion_outcome,
        "MINIMAL_RUNTIME_BASIS_MISSING",
    )
    final_completion_version = _value_from_request_or_basis(
        request,
        "selected_portable_verification_final_completion_result_version",
        "result_version",
        "selected_portable_verification_final_completion_basis",
    )
    _add_check(
        checks,
        "portable verification final-completion version 0.1.0",
        final_completion_version == RESULT_VERSION,
        RESULT_VERSION,
        final_completion_version,
        "MINIMAL_RUNTIME_BASIS_MISSING",
    )
    final_completion_failed_count = _as_int(
        _value_from_request_or_basis(
            request,
            "selected_portable_verification_final_completion_failed_check_count",
            "failed_check_count",
            "selected_portable_verification_final_completion_basis",
        )
    )
    _add_check(
        checks,
        "portable verification final-completion failed checks zero",
        final_completion_failed_count == 0,
        0,
        final_completion_failed_count,
        "MINIMAL_RUNTIME_BASIS_MISSING",
    )

    currentness_declared = _basis_present(
        request,
        "selected_post_portable_verification_currentness_basis",
        "selected_post_portable_currentness_surface_path",
    )
    _add_check(
        checks,
        "post-portable currentness surface basis declared",
        currentness_declared,
        "post-portable currentness surface basis declared",
        currentness_declared,
        "MINIMAL_RUNTIME_BASIS_MISSING",
    )
    currentness_checkability = _value_from_request_or_basis(
        request,
        "selected_post_portable_currentness_surface_states_checkability_not_continuation",
        "states_checkability_not_continuation",
        "selected_post_portable_verification_currentness_basis",
    )
    _add_check(
        checks,
        "post-portable currentness surface states checkability not continuation",
        currentness_checkability is True,
        True,
        currentness_checkability,
        "MINIMAL_RUNTIME_BASIS_MISSING",
    )
    currentness_authorized_next_work = _value_from_request_or_basis(
        request,
        "selected_post_portable_currentness_surface_authorized_next_work",
        "authorized_next_work",
        "selected_post_portable_verification_currentness_basis",
        False,
    )
    _add_check(
        checks,
        "post-portable currentness surface does not authorize next work",
        currentness_authorized_next_work is False,
        False,
        currentness_authorized_next_work,
        "FOLLOW_ON_WORK_AUTHORIZED",
    )

    predecessor_hidden = bool(request.get("predecessor_failure_hidden", False))
    predecessor_repaired = bool(request.get("predecessor_failure_repaired", False))
    predecessor_claimed = bool(request.get("predecessor_failure_claimed_passed", False))
    predecessor_preserved = request.get(
        "predecessor_failure_evidence_preserved_posture",
        request.get("predecessor_failure_evidence_preserved", True),
    )
    _add_check(
        checks,
        "predecessor failure evidence visible and unrepaired",
        predecessor_preserved is not False
        and not predecessor_hidden
        and not predecessor_repaired
        and not predecessor_claimed,
        "predecessor failure evidence preserved, unrepaired, unhidden, not claimed passed",
        {
            "predecessor_failure_evidence_preserved": predecessor_preserved,
            "predecessor_failure_hidden": predecessor_hidden,
            "predecessor_failure_repaired": predecessor_repaired,
            "predecessor_failure_claimed_passed": predecessor_claimed,
        },
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    )

    for field in POSTURE_FIELDS:
        actual = request.get(field)
        declared = _present(actual)
        _add_check(
            checks,
            field.replace("_", " ") + " declared",
            declared,
            "declared bounded posture",
            actual,
            {
                "selected_basis_reference_shape_posture": "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
                "raw_full_prior_artifact_body_not_returned_posture": (
                    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED"
                ),
                "predecessor_failure_evidence_preserved_posture": (
                    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"
                ),
            }.get(field, "NON_CLAIM_MISSING_OR_FLIPPED"),
        )

    source_authority_postures = (
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
    )
    _add_check(
        checks,
        "source/authority/currentness/deployment/public-release/operation-permission/follow-on not-created posture declared",
        all(_present(request.get(field)) for field in source_authority_postures),
        "all source/authority/currentness/deployment/public-release/operation-permission/follow-on non-creation postures declared",
        {field: _present(request.get(field)) for field in source_authority_postures},
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )

    explicit_guard_checks = (
        (
            "hidden repo state excluded",
            "hidden_repo_state_excluded",
            True,
            "HIDDEN_REPO_STATE_USED_AS_SUCCESSOR_RUNTIME_STEP_BOUNDARY_CONTENT",
        ),
        (
            "hidden repo state not used as successor-runtime-step-boundary authority",
            "hidden_repo_state_used_as_successor_runtime_step_boundary_authority",
            False,
            "HIDDEN_REPO_STATE_USED_AS_SUCCESSOR_RUNTIME_STEP_BOUNDARY_AUTHORITY",
        ),
        (
            "repo-local availability not successor-runtime-step-boundary authority",
            "repo_local_availability_treated_as_successor_runtime_step_boundary_authority",
            False,
            "REPO_LOCAL_AVAILABILITY_TREATED_AS_SUCCESSOR_RUNTIME_STEP_BOUNDARY_AUTHORITY",
        ),
        (
            "artifact existence not successor-runtime-step-boundary authority",
            "artifact_existence_treated_as_successor_runtime_step_boundary_authority",
            False,
            "ARTIFACT_EXISTENCE_TREATED_AS_SUCCESSOR_RUNTIME_STEP_BOUNDARY_AUTHORITY",
        ),
        (
            "latest file posture not successor-runtime-step-boundary authority",
            "latest_file_posture_treated_as_successor_runtime_step_boundary_authority",
            False,
            "LATEST_FILE_POSTURE_TREATED_AS_SUCCESSOR_RUNTIME_STEP_BOUNDARY_AUTHORITY",
        ),
        (
            "selected basis reference-shaped",
            "reference_shaped_input_posture",
            True,
            "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
        ),
        (
            "raw full prior artifact body not returned",
            "raw_full_prior_artifact_body_returned",
            False,
            "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
        ),
        (
            "official enum scope strings not redacted",
            "official_enum_scope_strings_not_redacted",
            True,
            "UNSUPPORTED_SUCCESSOR_RUNTIME_STEP_BOUNDARY_SCOPE",
        ),
        (
            "hostile raw body content contained",
            "hostile_raw_body_content_contained",
            True,
            "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
        ),
        (
            "consumed token remains closed",
            "consumed_request_reopened",
            False,
            "CONSUMED_REQUEST_REOPENED",
        ),
        (
            "authorization token reuse blocked",
            "authorization_token_reused",
            False,
            "AUTHORIZATION_TOKEN_REUSED",
        ),
    )
    for name, field, expected, code in explicit_guard_checks:
        actual = request.get(field)
        if expected is True:
            passed = actual is not False
        else:
            passed = actual is not True
        _add_check(checks, name, passed, expected, actual, code)

    for field, code in FALSE_CHECK_FIELD_CODES:
        actual = request.get(field, False)
        _add_check(checks, f"{field} remains false", actual is False, False, actual, code)

    declared_non_claims = request.get("declared_non_claims")
    non_claims_mapping = declared_non_claims if _is_mapping(declared_non_claims) else {}
    for field in REQUIRED_FALSE_NON_CLAIMS:
        actual = non_claims_mapping.get(field, request.get(field, None))
        _add_check(
            checks,
            f"required non-claim false: {field}",
            actual is False,
            False,
            actual,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )

    return checks


def _resolve_outcome(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> str:
    if any(check_record.get("passed") is False for check_record in checks):
        return OUTCOME_BLOCKED
    requested = request.get("requested_successor_runtime_step_boundary_outcome")
    intent = request.get("successor_runtime_step_boundary_intent")
    if requested == OUTCOME_NOT_RECORDED or intent == INTENT_DO_NOT_RECORD:
        return OUTCOME_NOT_RECORDED
    if requested == OUTCOME_REQUIRES_ADDITIONAL_BASIS or _present(
        request.get("additional_basis_context")
    ):
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS
    return OUTCOME_RECORDED


def _metadata(request: Mapping[str, Any]) -> dict[str, Any]:
    request_id = request.get(
        "successor_runtime_step_boundary_request_id",
        "post_minimal_runtime_successor_runtime_step_boundary_reference_review_001",
    )
    return {
        "post_minimal_runtime_successor_runtime_step_boundary_id": _sanitize(request_id),
        "post_minimal_runtime_successor_runtime_step_boundary_type": (
            "post_minimal_runtime_successor_runtime_step_boundary"
        ),
        "post_minimal_runtime_successor_runtime_step_boundary_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
    }


def _extract_selected_summary_value(
    result: Mapping[str, Any], section_name: str, key: str
) -> Any:
    section = result.get(section_name)
    if not _is_mapping(section):
        return None
    if key in section:
        return section.get(key)
    found = _find_key(section, key, depth=4)
    return found


def build_post_minimal_runtime_successor_runtime_step_boundary_summary(
    result: Mapping[str, Any]
) -> dict[str, Any]:
    """Build a bounded summary from a successor-runtime-step-boundary result."""

    checks = result.get("successor_runtime_step_boundary_checks", [])
    if not isinstance(checks, list):
        checks = []
    passed_count = sum(
        1 for item in checks if _is_mapping(item) and item.get("passed") is True
    )
    failed_count = sum(
        1 for item in checks if _is_mapping(item) and item.get("passed") is False
    )
    metadata = result.get(
        "post_minimal_runtime_successor_runtime_step_boundary_metadata", {}
    )
    if not _is_mapping(metadata):
        metadata = {}
    block = result.get("block")
    if not _is_mapping(block):
        block = {}
    statement = result.get("successor_runtime_step_boundary_statement", {})
    if not _is_mapping(statement):
        statement = {}
    non_claims = result.get("non_claims", {})
    if not _is_mapping(non_claims):
        non_claims = {}
    declared_question = result.get("declared_successor_runtime_step_boundary_question", {})
    if not _is_mapping(declared_question):
        declared_question = {}

    summary = {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "request_id": metadata.get(
            "post_minimal_runtime_successor_runtime_step_boundary_id"
        ),
        "question": declared_question.get("successor_runtime_step_boundary_question"),
        "intent": declared_question.get("successor_runtime_step_boundary_intent"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": metadata.get(
            "post_minimal_runtime_successor_runtime_step_boundary_version",
            RESULT_VERSION,
        ),
        "resolver_module": metadata.get("resolver_module", RESOLVER_MODULE),
        "selected_minimal_runtime_outcome": _extract_selected_summary_value(
            result, "selected_minimal_runtime_basis", "outcome"
        ),
        "selected_minimal_runtime_version": _extract_selected_summary_value(
            result, "selected_minimal_runtime_basis", "result_version"
        ),
        "selected_minimal_runtime_failed_check_count": _extract_selected_summary_value(
            result, "selected_minimal_runtime_basis", "failed_check_count"
        ),
        "selected_runtime_boundary_outcome": _extract_selected_summary_value(
            result, "selected_runtime_boundary_basis", "outcome"
        ),
        "selected_runtime_boundary_version": _extract_selected_summary_value(
            result, "selected_runtime_boundary_basis", "result_version"
        ),
        "selected_runtime_boundary_failed_check_count": _extract_selected_summary_value(
            result, "selected_runtime_boundary_basis", "failed_check_count"
        ),
        "selected_runtime_readiness_outcome": _extract_selected_summary_value(
            result, "selected_runtime_readiness_basis", "outcome"
        ),
        "selected_runtime_readiness_version": _extract_selected_summary_value(
            result, "selected_runtime_readiness_basis", "result_version"
        ),
        "selected_runtime_readiness_failed_check_count": _extract_selected_summary_value(
            result, "selected_runtime_readiness_basis", "failed_check_count"
        ),
        "selected_final_completion_outcome": _extract_selected_summary_value(
            result, "selected_portable_verification_final_completion_basis", "outcome"
        ),
        "selected_final_completion_version": _extract_selected_summary_value(
            result,
            "selected_portable_verification_final_completion_basis",
            "result_version",
        ),
        "selected_final_completion_failed_check_count": _extract_selected_summary_value(
            result,
            "selected_portable_verification_final_completion_basis",
            "failed_check_count",
        ),
        "selected_post_portable_currentness_surface_path": _extract_selected_summary_value(
            result,
            "selected_post_portable_verification_currentness_basis",
            "basis_path",
        ),
        "no_successor_runtime_step_runtime_hosting_ongoing_runtime_continuation_source_authority_currentness_deployment_public_release_follow_on": True,
        "key_non_claims": {
            key: non_claims.get(key)
            for key in (
                "successor_runtime_step_created",
                "runtime_hosting_created",
                "ongoing_runtime_created",
                "reusable_runtime_permission_created",
                "continuation_authorized",
                "source_created",
                "authority_created",
                "currentness_created",
                "deployment_created",
                "public_release_created",
                "follow_on_work_authorized",
                "consumed_request_reopened",
                "authorization_token_reused",
                "predecessor_failure_repaired",
                "predecessor_failure_hidden",
                "predecessor_failure_claimed_passed",
            )
        },
        "predecessor_failure_evidence_preserved": statement.get(
            "predecessor_failure_evidence_preserved"
        ),
        "consumed_request_token_remains_closed": statement.get(
            "consumed_request_token_remains_closed"
        ),
        "authorization_token_reuse_blocked": statement.get(
            "authorization_token_reuse_blocked"
        ),
    }
    for field in ALLOWED_TRUE_RECORDED_FIELDS:
        summary[field] = statement.get(field)
    return _sanitize(summary)


def resolve_post_minimal_runtime_successor_runtime_step_boundary(
    declared_successor_runtime_step_boundary_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one bounded post-minimal-runtime successor-step-boundary request."""

    if declared_successor_runtime_step_boundary_request is None:
        request = build_declared_post_minimal_runtime_successor_runtime_step_boundary_request()
        forced_block_code = None
    elif not _is_mapping(declared_successor_runtime_step_boundary_request):
        request = {
            "successor_runtime_step_boundary_request_id": (
                "malformed_successor_runtime_step_boundary_request"
            ),
            "successor_runtime_step_boundary_question": None,
            "successor_runtime_step_boundary_intent": None,
            "declared_non_claims": _safe_non_claims(),
        }
        forced_block_code = "DECLARED_SUCCESSOR_RUNTIME_STEP_BOUNDARY_REQUEST_MALFORMED"
    else:
        request = _deepcopy_mapping(declared_successor_runtime_step_boundary_request)
        forced_block_code = None

    checks = _add_boundary_checks(request, forced_block_code=forced_block_code)
    outcome = _resolve_outcome(request, checks)
    recorded = outcome == OUTCOME_RECORDED
    block = _block_from_checks(checks, request.get("block_reason"))
    metadata = _metadata(request)
    non_claims = _safe_non_claims()

    result: dict[str, Any] = {
        "post_minimal_runtime_successor_runtime_step_boundary_metadata": metadata,
        "declared_successor_runtime_step_boundary_question": {
            "successor_runtime_step_boundary_request_id": metadata[
                "post_minimal_runtime_successor_runtime_step_boundary_id"
            ],
            "successor_runtime_step_boundary_question": _sanitize(
                request.get("successor_runtime_step_boundary_question")
            ),
            "successor_runtime_step_boundary_intent": _sanitize(
                request.get("successor_runtime_step_boundary_intent")
            ),
        },
        "successor_runtime_step_boundary_scope": _sanitize(
            _scope_values(request.get("successor_runtime_step_boundary_scope"))
        ),
        "successor_runtime_step_boundary_checks": checks,
        "successor_runtime_step_boundary_statement": _statement(recorded),
        "successor_runtime_step_boundary_non_meaning": _non_meaning(),
        "additional_basis_required": _sanitize(request.get("additional_basis_context")),
        "not_recorded_basis": _sanitize(request.get("not_recorded_basis")),
        "what_remains_open": _what_remains_open(),
        "non_claims": non_claims,
        "outcome": outcome,
        "block": block,
    }

    for field in SELECTED_BASIS_FIELDS:
        result[field] = _sanitize(request.get(field, {}))
    for field in POSTURE_FIELDS:
        result[field] = _sanitize(request.get(field, _posture(field)))

    result["post_minimal_runtime_successor_runtime_step_boundary_summary"] = (
        build_post_minimal_runtime_successor_runtime_step_boundary_summary(result)
    )
    return result


def resolve_post_minimal_runtime_successor_runtime_step_boundary_from_path(
    declared_successor_runtime_step_boundary_request_path: Path | str,
) -> dict:
    """Read a declared successor-runtime-step-boundary request JSON and resolve it."""

    path = Path(declared_successor_runtime_step_boundary_request_path)
    try:
        raw = path.read_text(encoding="utf-8")
        loaded = json.loads(raw)
    except OSError as exc:
        request = {
            "successor_runtime_step_boundary_request_id": (
                "unreadable_successor_runtime_step_boundary_request"
            ),
            "successor_runtime_step_boundary_question": None,
            "successor_runtime_step_boundary_intent": None,
            "block_reason": str(exc),
            "declared_non_claims": _safe_non_claims(),
        }
        checks = _add_boundary_checks(
            request,
            forced_block_code="DECLARED_SUCCESSOR_RUNTIME_STEP_BOUNDARY_REQUEST_UNREADABLE",
        )
        return _result_from_forced_request(request, checks)
    except json.JSONDecodeError as exc:
        request = {
            "successor_runtime_step_boundary_request_id": (
                "malformed_successor_runtime_step_boundary_request"
            ),
            "successor_runtime_step_boundary_question": None,
            "successor_runtime_step_boundary_intent": None,
            "block_reason": str(exc),
            "declared_non_claims": _safe_non_claims(),
        }
        checks = _add_boundary_checks(
            request,
            forced_block_code="DECLARED_SUCCESSOR_RUNTIME_STEP_BOUNDARY_REQUEST_MALFORMED",
        )
        return _result_from_forced_request(request, checks)
    if not _is_mapping(loaded):
        request = {
            "successor_runtime_step_boundary_request_id": (
                "malformed_successor_runtime_step_boundary_request"
            ),
            "successor_runtime_step_boundary_question": None,
            "successor_runtime_step_boundary_intent": None,
            "block_reason": "declared request JSON must be an object",
            "declared_non_claims": _safe_non_claims(),
        }
        checks = _add_boundary_checks(
            request,
            forced_block_code="DECLARED_SUCCESSOR_RUNTIME_STEP_BOUNDARY_REQUEST_MALFORMED",
        )
        return _result_from_forced_request(request, checks)
    return resolve_post_minimal_runtime_successor_runtime_step_boundary(loaded)


def _result_from_forced_request(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> dict:
    metadata = _metadata(request)
    result: dict[str, Any] = {
        "post_minimal_runtime_successor_runtime_step_boundary_metadata": metadata,
        "declared_successor_runtime_step_boundary_question": {
            "successor_runtime_step_boundary_request_id": metadata[
                "post_minimal_runtime_successor_runtime_step_boundary_id"
            ],
            "successor_runtime_step_boundary_question": _sanitize(
                request.get("successor_runtime_step_boundary_question")
            ),
            "successor_runtime_step_boundary_intent": _sanitize(
                request.get("successor_runtime_step_boundary_intent")
            ),
        },
        "successor_runtime_step_boundary_scope": [],
        "successor_runtime_step_boundary_checks": checks,
        "successor_runtime_step_boundary_statement": _statement(False),
        "successor_runtime_step_boundary_non_meaning": _non_meaning(),
        "additional_basis_required": None,
        "not_recorded_basis": None,
        "what_remains_open": _what_remains_open(),
        "non_claims": _safe_non_claims(),
        "outcome": OUTCOME_BLOCKED,
        "block": _block_from_checks(checks, request.get("block_reason")),
    }
    for field in SELECTED_BASIS_FIELDS:
        result[field] = {}
    for field in POSTURE_FIELDS:
        result[field] = _posture(field, declared=False)
    result["post_minimal_runtime_successor_runtime_step_boundary_summary"] = (
        build_post_minimal_runtime_successor_runtime_step_boundary_summary(result)
    )
    return result


def write_post_minimal_runtime_successor_runtime_step_boundary_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write a bounded successor-runtime-step-boundary result JSON."""

    if not _is_mapping(result):
        raise PostMinimalRuntimeSuccessorRuntimeStepBoundaryError(
            "result must be a mapping"
        )
    if output_path is None:
        metadata = result.get(
            "post_minimal_runtime_successor_runtime_step_boundary_metadata", {}
        )
        if not _is_mapping(metadata):
            metadata = {}
        request_id = str(
            metadata.get(
                "post_minimal_runtime_successor_runtime_step_boundary_id",
                "post_minimal_runtime_successor_runtime_step_boundary_reference_review_001",
            )
        )
        output_path = (
            OUTPUT_ROOT
            / f"{request_id}__post_minimal_runtime_successor_runtime_step_boundary_result.json"
        )
    path = Path(output_path)
    _ensure_allowed_output_path(path)
    path = _with_numeric_suffix_if_exists(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(_sanitize(result), indent=2, sort_keys=True, ensure_ascii=True)
        + "\n",
        encoding="utf-8",
    )
    return path


def _ensure_allowed_output_path(path: Path) -> None:
    path_text = path.as_posix()
    if OUTPUT_ROOT.as_posix() in path_text:
        return
    for marker in PROHIBITED_OUTPUT_PATH_MARKERS:
        if marker in path_text:
            raise PostMinimalRuntimeSuccessorRuntimeStepBoundaryError(
                f"output path targets a prohibited root: {marker}"
            )


def _with_numeric_suffix_if_exists(path: Path) -> Path:
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


def build_declared_post_minimal_runtime_successor_runtime_step_boundary_request(
    *,
    successor_runtime_step_boundary_request_id: str = (
        "post_minimal_runtime_successor_runtime_step_boundary_reference_review_001"
    ),
    successor_runtime_step_boundary_question: str = CORE_QUESTION,
    successor_runtime_step_boundary_intent: str = INTENT_RECORD,
    successor_runtime_step_boundary_scope: Any = None,
    overrides: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a clean declared successor-runtime-step-boundary request."""

    minimal_runtime_result_path = (
        "artifacts/"
        "integrity_host_v0_min_coexistence_post_portable_verification_minimal_runtime/"
        "post_portable_verification_minimal_runtime_reference_review_001"
        "__post_portable_verification_minimal_runtime_result.json"
    )
    runtime_boundary_result_path = (
        "artifacts/"
        "integrity_host_v0_min_coexistence_post_portable_verification_runtime_boundary/"
        "post_portable_verification_runtime_boundary_reference_review_001"
        "__post_portable_verification_runtime_boundary_result.json"
    )
    runtime_readiness_result_path = (
        "artifacts/"
        "integrity_host_v0_min_coexistence_post_portable_verification_runtime_readiness/"
        "post_portable_verification_runtime_readiness_reference_review_001"
        "__post_portable_verification_runtime_readiness_result.json"
    )
    final_completion_result_path = (
        "artifacts/"
        "integrity_host_v0_min_coexistence_portable_source_body_verification_final_completion/"
        "portable_source_body_verification_final_completion_reference_review_001"
        "__portable_source_body_verification_final_completion_result.json"
    )
    scope = (
        list(SUPPORTED_SCOPE_VALUES)
        if successor_runtime_step_boundary_scope is None
        else copy.deepcopy(successor_runtime_step_boundary_scope)
    )

    request: dict[str, Any] = {
        "successor_runtime_step_boundary_request_id": (
            successor_runtime_step_boundary_request_id
        ),
        "successor_runtime_step_boundary_question": (
            successor_runtime_step_boundary_question
        ),
        "successor_runtime_step_boundary_intent": (
            successor_runtime_step_boundary_intent
        ),
        "selected_minimal_runtime_basis": _default_basis(
            "post-portable-verification minimal-runtime live artifact",
            minimal_runtime_result_path,
            outcome=EXPECTED_MINIMAL_RUNTIME_OUTCOME,
            result_version=RESULT_VERSION,
            failed_check_count=0,
            bounded_minimal_runtime_step_recorded=True,
            bounded_minimal_runtime_result_or_refusal=True,
            no_successor_action_authorized=True,
            runtime_hosting_created=False,
            ongoing_runtime_created=False,
            successor_runtime_step_created=False,
            continuation_beyond_single_step_authorized=False,
            minimal_runtime_treated_as_runtime_hosting=False,
            minimal_runtime_treated_as_ongoing_runtime=False,
            minimal_runtime_treated_as_successor_runtime_step=False,
            minimal_runtime_treated_as_continuation=False,
            bounded_runtime_result_or_refusal_authorized_successor=False,
            follow_on_work_authorized=False,
            minimal_runtime_statement={
                "minimal_runtime_recorded": True,
                "bounded_minimal_runtime_step_recorded": True,
                "minimal_runtime_not_successor_runtime_step": True,
                "runtime_hosting_not_created": True,
                "ongoing_runtime_not_created": True,
                "successor_runtime_step_not_created": True,
                "continuation_beyond_single_step_not_authorized": True,
            },
            minimal_runtime_runtime_result_or_refusal={
                "bounded_minimal_runtime_result_or_refusal": True,
                "recorded": True,
                "result_or_refusal": (
                    "one bounded minimal-runtime posture recorded from selected "
                    "standing basis; no successor action authorized"
                ),
                "selects_successor": False,
                "creates_successor_runtime_step": False,
                "creates_runtime_hosting": False,
                "creates_ongoing_runtime": False,
                "authorizes_continuation_beyond_single_step": False,
            },
        ),
        "selected_minimal_runtime_terminal_summary_basis": _default_basis(
            "post-portable-verification minimal-runtime terminal summary",
            "spec/POST_PORTABLE_VERIFICATION_MINIMAL_RUNTIME_TERMINAL_SUMMARY_V0.md",
            runtime_hosting_not_created=True,
            ongoing_runtime_not_created=True,
            successor_runtime_step_not_created=True,
            continuation_beyond_single_step_not_authorized=True,
            no_successor_runtime_step_selected=True,
            future_work_requires_separate_step_back_review=True,
            future_work_requires_separately_bounded_specification=True,
        ),
        "selected_runtime_boundary_basis": _default_basis(
            "post-portable-verification runtime-boundary live artifact",
            runtime_boundary_result_path,
            outcome=EXPECTED_RUNTIME_BOUNDARY_OUTCOME,
            result_version=RESULT_VERSION,
            failed_check_count=0,
        ),
        "selected_runtime_readiness_basis": _default_basis(
            "post-portable-verification runtime-readiness live artifact",
            runtime_readiness_result_path,
            outcome=EXPECTED_RUNTIME_READINESS_OUTCOME,
            result_version=RESULT_VERSION,
            failed_check_count=0,
        ),
        "selected_portable_verification_final_completion_basis": _default_basis(
            "portable source-body verification final-completion live artifact",
            final_completion_result_path,
            outcome=EXPECTED_FINAL_COMPLETION_OUTCOME,
            result_version=RESULT_VERSION,
            failed_check_count=0,
        ),
        "selected_post_portable_verification_currentness_basis": _default_basis(
            "post-portable-verification currentness surface",
            "spec/POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_V0.md",
            states_checkability_not_continuation=True,
            authorized_next_work=False,
        ),
        "selected_returned_second_carrier_capture_lineage_basis": _default_basis(
            "returned second-carrier live capture intake lineage basis",
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_RETURNED_SECOND_CARRIER_LIVE_CAPTURE_INTAKE_V0.md",
            lineage_only=True,
            runtime_basis=False,
        ),
        "successor_runtime_step_boundary_scope": scope,
        "declared_non_claims": _safe_non_claims(),
        "selected_minimal_runtime_result_path": minimal_runtime_result_path,
        "selected_minimal_runtime_result_outcome": EXPECTED_MINIMAL_RUNTIME_OUTCOME,
        "selected_minimal_runtime_result_version": RESULT_VERSION,
        "selected_minimal_runtime_failed_check_count": 0,
        "selected_minimal_runtime_bounded_minimal_runtime_step_recorded": True,
        "selected_minimal_runtime_bounded_runtime_result_or_refusal_recorded": True,
        "selected_minimal_runtime_no_successor_action_authorized": True,
        "selected_minimal_runtime_already_created_runtime_hosting": False,
        "selected_minimal_runtime_already_created_ongoing_runtime": False,
        "selected_minimal_runtime_already_created_successor_runtime_step": False,
        "selected_minimal_runtime_already_authorized_continuation_beyond_single_step": False,
        "selected_minimal_runtime_treated_as_runtime_hosting": False,
        "selected_minimal_runtime_treated_as_ongoing_runtime": False,
        "selected_minimal_runtime_treated_as_successor_runtime_step": False,
        "selected_minimal_runtime_treated_as_continuation": False,
        "selected_minimal_runtime_authorized_future_work": False,
        "selected_bounded_runtime_result_or_refusal_authorized_successor": False,
        "selected_runtime_boundary_result_path": runtime_boundary_result_path,
        "selected_runtime_boundary_result_outcome": EXPECTED_RUNTIME_BOUNDARY_OUTCOME,
        "selected_runtime_boundary_result_version": RESULT_VERSION,
        "selected_runtime_boundary_failed_check_count": 0,
        "selected_runtime_readiness_result_path": runtime_readiness_result_path,
        "selected_runtime_readiness_result_outcome": EXPECTED_RUNTIME_READINESS_OUTCOME,
        "selected_runtime_readiness_result_version": RESULT_VERSION,
        "selected_runtime_readiness_failed_check_count": 0,
        "selected_portable_verification_final_completion_result_path": (
            final_completion_result_path
        ),
        "selected_portable_verification_final_completion_result_outcome": (
            EXPECTED_FINAL_COMPLETION_OUTCOME
        ),
        "selected_portable_verification_final_completion_result_version": RESULT_VERSION,
        "selected_portable_verification_final_completion_failed_check_count": 0,
        "selected_post_portable_currentness_surface_path": (
            "spec/POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_V0.md"
        ),
        "selected_post_portable_currentness_surface_states_checkability_not_continuation": True,
        "selected_post_portable_currentness_surface_authorized_next_work": False,
        "successor_runtime_step_boundary_created_before_review": False,
        "successor_runtime_step_created": False,
        "runtime_hosting_created": False,
        "ongoing_runtime_created": False,
        "reusable_runtime_permission_created": False,
        "continuation_authorized": False,
        "reference_shaped_input_posture": True,
        "additional_basis_context": None,
        "not_recorded_basis": None,
        "block_reason": None,
        "requested_successor_runtime_step_boundary_outcome": OUTCOME_RECORDED,
        "hidden_repo_state_excluded": True,
        "official_enum_scope_strings_not_redacted": True,
        "hostile_raw_body_content_contained": True,
        "predecessor_failure_evidence_preserved": True,
    }

    for field in POSTURE_FIELDS:
        request[field] = _posture(field)
    for field in REQUIRED_FALSE_NON_CLAIMS:
        request[field] = False

    if overrides:
        for key, value in overrides.items():
            request[key] = copy.deepcopy(value)
    return request
