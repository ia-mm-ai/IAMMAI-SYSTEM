"""Bounded post-portable-verification runtime-readiness resolver.

This resolver is downstream of the runtime-readiness-boundary line. It records
one bounded runtime-readiness posture only. Runtime-readiness here is not
runtime, runtime boundary, runtime step, continuation, source transfer, source
receipt, reception authorization, source, authority, currentness, deployment,
public release, operation permission, reusable permission, adoption,
receiving-context governance, publication flow, or follow-on work.

The resolver is self-contained, imports no repo-local modules, runs no
subprocesses, performs no network access, and mutates no upstream artifact. It
keeps official enum, scope, outcome, block-code, posture, non-claim, and
boolean field strings unredacted while containing hostile raw body payloads.
"""

from __future__ import annotations

import copy
import datetime
import json
from pathlib import Path
from typing import Any, Iterable, Mapping


class PostPortableVerificationRuntimeReadinessError(Exception):
    """Raised for bounded runtime-readiness path/write failures."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_post_portable_verification_runtime_readiness"
RESULT_TYPE = "post_portable_verification_runtime_readiness"
DEFAULT_REQUEST_ID = "post_portable_verification_runtime_readiness_reference_review_001"
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_post_portable_verification_"
    "runtime_readiness"
)

CORE_QUESTION = (
    "Can the clean post-portable-verification runtime-readiness-boundary "
    "basis be used to record one bounded runtime-readiness posture without "
    "creating runtime, runtime boundary, runtime step, continuation, source "
    "transfer, source receipt, reception authorization, source, authority, "
    "currentness, deployment, public release, operation permission, reusable "
    "permission, derivative reception, vessel relation, another reception "
    "request, adoption, receiving-context governance, publication flow, or "
    "follow-on work?"
)

OUTCOME_RECORDED = "POST_PORTABLE_VERIFICATION_RUNTIME_READINESS_RECORDED"
OUTCOME_NOT_RECORDED = "POST_PORTABLE_VERIFICATION_RUNTIME_READINESS_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "POST_PORTABLE_VERIFICATION_RUNTIME_READINESS_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "POST_PORTABLE_VERIFICATION_RUNTIME_READINESS_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = "RECORD_POST_PORTABLE_VERIFICATION_RUNTIME_READINESS"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_POST_PORTABLE_VERIFICATION_RUNTIME_READINESS"
INTENT_BLOCK = "BLOCK_POST_PORTABLE_VERIFICATION_RUNTIME_READINESS"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

EXPECTED_RUNTIME_READINESS_BOUNDARY_OUTCOME = (
    "POST_PORTABLE_VERIFICATION_RUNTIME_READINESS_BOUNDARY_RECORDED"
)
EXPECTED_FINAL_COMPLETION_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_RECORDED"
)

SUPPORTED_SCOPE_VALUES = (
    "RUNTIME_READINESS_SPEC_ONLY",
    "ONE_BOUNDED_RUNTIME_READINESS_RECORDED",
    "RUNTIME_READINESS_BOUNDARY_BASIS_PRESERVED",
    "PORTABLE_VERIFICATION_FINAL_COMPLETION_BASIS_PRESERVED",
    "POST_PORTABLE_VERIFICATION_CURRENTNESS_BASIS_PRESERVED",
    "CHECKABILITY_NOT_CONTINUATION_PRESERVED",
    "RUNTIME_READINESS_NOT_RUNTIME",
    "RUNTIME_READINESS_NOT_RUNTIME_BOUNDARY",
    "RUNTIME_READINESS_NOT_RUNTIME_STEP",
    "RUNTIME_READINESS_NOT_CONTINUATION",
    "RUNTIME_READINESS_NOT_SOURCE_TRANSFER",
    "RUNTIME_READINESS_NOT_SOURCE_RECEIPT",
    "RUNTIME_READINESS_NOT_RECEPTION_AUTHORIZATION",
    "RUNTIME_READINESS_NOT_SOURCE",
    "RUNTIME_READINESS_NOT_AUTHORITY",
    "RUNTIME_READINESS_NOT_CURRENTNESS",
    "RUNTIME_BOUNDARY_NOT_CREATED",
    "RUNTIME_NOT_CREATED",
    "RUNTIME_STEP_NOT_CREATED",
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
    "NO_RUNTIME_INFERENCE",
    "NO_RUNTIME_BOUNDARY_INFERENCE",
    "NO_RUNTIME_STEP_INFERENCE",
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
    "HIDDEN_REPO_STATE_NOT_USED_AS_RUNTIME_READINESS_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_NOT_RUNTIME_READINESS_AUTHORITY",
    "ARTIFACT_EXISTENCE_NOT_RUNTIME_READINESS_AUTHORITY",
    "LATEST_FILE_POSTURE_NOT_RUNTIME_READINESS_AUTHORITY",
    "SELECTED_BASIS_REFERENCE_SHAPE_PRESERVED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "PREDECESSOR_FAILURE_EVIDENCE_PRESERVED",
    "AUTHORIZATION_TOKEN_REUSE_BLOCKED",
    "CONSUMED_REQUEST_TOKEN_REMAINS_CLOSED",
    "CONSUMED_REQUEST_NOT_REOPENED",
)
SUPPORTED_RUNTIME_READINESS_SCOPE = SUPPORTED_SCOPE_VALUES

REQUIRED_FALSE_NON_CLAIMS = (
    "runtime_created",
    "runtime_boundary_created",
    "runtime_step_created",
    "continuation_authorized",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "runtime_readiness_treated_as_runtime",
    "runtime_readiness_treated_as_runtime_boundary",
    "runtime_readiness_treated_as_runtime_step",
    "runtime_readiness_treated_as_continuation",
    "runtime_readiness_treated_as_source_transfer",
    "runtime_readiness_treated_as_source_receipt",
    "runtime_readiness_treated_as_reception_authorization",
    "runtime_readiness_treated_as_source",
    "runtime_readiness_treated_as_authority",
    "runtime_readiness_treated_as_currentness",
    "runtime_readiness_treated_as_deployment",
    "runtime_readiness_treated_as_public_release",
    "runtime_readiness_treated_as_operation_permission",
    "runtime_readiness_treated_as_reusable_permission",
    "runtime_readiness_treated_as_follow_on_work",
    "runtime_readiness_boundary_treated_as_runtime_readiness_without_review",
    "portable_verification_final_completion_treated_as_runtime",
    "portable_verification_final_completion_treated_as_continuation",
    "post_portable_verification_currentness_surface_treated_as_runtime_permission",
    "post_portable_verification_currentness_surface_treated_as_operation_permission",
    "checkability_treated_as_continuation",
    "artifact_existence_treated_as_runtime_readiness_authority",
    "artifact_path_treated_as_currentness",
    "latest_file_posture_treated_as_runtime_readiness_authority",
    "repo_local_availability_treated_as_runtime_readiness_authority",
    "hidden_repo_state_used_as_runtime_readiness_content",
    "hidden_repo_state_used_as_runtime_readiness_authority",
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
    "runtime_readiness_recorded",
    "bounded_runtime_readiness_recorded",
    "runtime_readiness_boundary_basis_preserved",
    "portable_verification_final_completion_basis_preserved",
    "post_portable_verification_currentness_basis_preserved",
    "checkability_not_continuation_preserved",
    "runtime_readiness_not_runtime",
    "runtime_readiness_not_runtime_boundary",
    "runtime_readiness_not_runtime_step",
    "runtime_readiness_not_continuation",
    "runtime_boundary_not_created",
    "runtime_not_created",
    "runtime_step_not_created",
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
    "hidden_repo_state_not_used_as_runtime_readiness_authority",
    "repo_local_availability_not_runtime_readiness_authority",
    "artifact_existence_not_runtime_readiness_authority",
    "latest_file_posture_not_runtime_readiness_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "official_enum_scope_strings_not_redacted",
    "hostile_raw_body_content_contained",
    "predecessor_failure_evidence_preserved",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
)

RECORDING_STATEMENT_FIELDS = (
    "runtime_readiness_recorded",
    "bounded_runtime_readiness_recorded",
)

BLOCK_CODES = (
    "DECLARED_RUNTIME_READINESS_REQUEST_MALFORMED",
    "DECLARED_RUNTIME_READINESS_REQUEST_UNREADABLE",
    "RUNTIME_READINESS_REQUEST_DECLARED_BLOCK",
    "RUNTIME_READINESS_QUESTION_UNDECLARED",
    "RUNTIME_READINESS_INTENT_UNSUPPORTED",
    "RUNTIME_READINESS_BOUNDARY_BASIS_MISSING",
    "RUNTIME_READINESS_BOUNDARY_NOT_RECORDED",
    "RUNTIME_READINESS_BOUNDARY_FAILED_CHECKS_PRESENT",
    "RUNTIME_READINESS_BOUNDARY_VERSION_NOT_0_1_0",
    "RUNTIME_READINESS_BOUNDARY_DID_NOT_DECLARE_FUTURE_RUNTIME_READINESS_REVIEW_STEP",
    "RUNTIME_READINESS_BOUNDARY_ALREADY_CREATED_RUNTIME_READINESS",
    "RUNTIME_READINESS_BOUNDARY_ALREADY_CREATED_RUNTIME",
    "RUNTIME_READINESS_BOUNDARY_ALREADY_AUTHORIZED_CONTINUATION",
    "RUNTIME_READINESS_BOUNDARY_TREATED_BOUNDARY_AS_RUNTIME_READINESS",
    "RUNTIME_READINESS_BOUNDARY_TREATED_BOUNDARY_AS_RUNTIME",
    "RUNTIME_READINESS_BOUNDARY_TREATED_CHECKABILITY_AS_CONTINUATION",
    "RUNTIME_READINESS_BOUNDARY_TREATED_FINAL_COMPLETION_AS_RUNTIME",
    "RUNTIME_READINESS_BOUNDARY_TREATED_FINAL_COMPLETION_AS_CONTINUATION",
    "RUNTIME_READINESS_BOUNDARY_TREATED_CURRENTNESS_SURFACE_AS_RUNTIME_PERMISSION",
    "RUNTIME_READINESS_BOUNDARY_TREATED_CURRENTNESS_SURFACE_AS_OPERATION_PERMISSION",
    "RUNTIME_READINESS_BOUNDARY_AUTHORIZED_FUTURE_WORK",
    "RUNTIME_READINESS_CREATED_BEFORE_REVIEW",
    "RUNTIME_CREATED",
    "RUNTIME_BOUNDARY_CREATED",
    "RUNTIME_STEP_CREATED",
    "CONTINUATION_AUTHORIZED",
    "RUNTIME_READINESS_TREATED_AS_RUNTIME",
    "RUNTIME_READINESS_TREATED_AS_RUNTIME_BOUNDARY",
    "RUNTIME_READINESS_TREATED_AS_RUNTIME_STEP",
    "RUNTIME_READINESS_TREATED_AS_CONTINUATION",
    "RUNTIME_READINESS_TREATED_AS_SOURCE_TRANSFER",
    "RUNTIME_READINESS_TREATED_AS_SOURCE_RECEIPT",
    "RUNTIME_READINESS_TREATED_AS_RECEPTION_AUTHORIZATION",
    "RUNTIME_READINESS_TREATED_AS_SOURCE",
    "RUNTIME_READINESS_TREATED_AS_AUTHORITY",
    "RUNTIME_READINESS_TREATED_AS_CURRENTNESS",
    "RUNTIME_READINESS_TREATED_AS_DEPLOYMENT",
    "RUNTIME_READINESS_TREATED_AS_PUBLIC_RELEASE",
    "RUNTIME_READINESS_TREATED_AS_OPERATION_PERMISSION",
    "RUNTIME_READINESS_TREATED_AS_REUSABLE_PERMISSION",
    "RUNTIME_READINESS_TREATED_AS_FOLLOW_ON_WORK",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_READINESS_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_READINESS_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_READINESS_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_RUNTIME_READINESS_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_RUNTIME_READINESS_AUTHORITY",
    "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_RUNTIME_READINESS_SCOPE",
    "POST_PORTABLE_VERIFICATION_CURRENTNESS_BASIS_MISSING",
    "POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_AUTHORIZED_NEXT_WORK",
    "FINAL_COMPLETION_BASIS_MISSING",
    "FINAL_COMPLETION_NOT_RECORDED",
    "FINAL_COMPLETION_FAILED_CHECKS_PRESENT",
    "FINAL_COMPLETION_VERSION_NOT_0_1_0",
    "ARTIFACTS_MUTATED",
)

SELECTED_BASIS_FIELDS = (
    "selected_runtime_readiness_boundary_basis",
    "selected_runtime_readiness_boundary_terminal_summary_basis",
    "selected_portable_verification_final_completion_basis",
    "selected_post_portable_verification_currentness_basis",
    "selected_final_completion_artifact_basis",
    "selected_returned_second_carrier_capture_lineage_basis",
)

POSTURE_FIELDS = (
    "runtime_readiness_spec_only_posture",
    "one_bounded_runtime_readiness_posture",
    "runtime_readiness_boundary_basis_preserved_posture",
    "portable_verification_final_completion_basis_preserved_posture",
    "post_portable_verification_currentness_basis_preserved_posture",
    "checkability_not_continuation_preserved_posture",
    "runtime_readiness_not_runtime_posture",
    "runtime_readiness_not_runtime_boundary_posture",
    "runtime_readiness_not_runtime_step_posture",
    "runtime_readiness_not_continuation_posture",
    "runtime_boundary_not_created_posture",
    "runtime_not_created_posture",
    "runtime_step_not_created_posture",
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
    "repo_local_availability_not_runtime_readiness_authority_posture",
    "artifact_existence_not_runtime_readiness_authority_posture",
    "latest_file_posture_not_runtime_readiness_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
)

SENSITIVE_CONTENT_KEYS = {
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
    "raw_runtime_body",
    "capture_body",
    "runtime_readiness_body",
    "runtime_boundary_body",
    "runtime_body",
    "source_body",
    "authority_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
}
HOSTILE_SENTINELS = (
    "RAW_RUNTIME_READINESS_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)
REDACTED_RAW_VALUE = "[bounded-redacted-raw-or-hidden-state]"
REFERENCE_SHAPED_REDACTION = "[bounded-reference-redacted-raw-or-hidden-state]"

OFFICIAL_STRINGS = (
    set(SUPPORTED_SCOPE_VALUES)
    | set(BLOCK_CODES)
    | set(OUTCOME_FAMILY)
    | set(REQUIRED_FALSE_NON_CLAIMS)
    | set(ALLOWED_TRUE_RECORDED_FIELDS)
    | set(SELECTED_BASIS_FIELDS)
    | set(POSTURE_FIELDS)
    | {
        RESULT_VERSION,
        RESOLVER_MODULE,
        RESULT_TYPE,
        CORE_QUESTION,
        INTENT_RECORD,
        INTENT_DO_NOT_RECORD,
        INTENT_BLOCK,
        EXPECTED_RUNTIME_READINESS_BOUNDARY_OUTCOME,
        EXPECTED_FINAL_COMPLETION_OUTCOME,
        "RUNTIME_READINESS_NOT_RUNTIME",
        "RUNTIME_READINESS_NOT_RUNTIME_BOUNDARY",
        "RUNTIME_READINESS_NOT_RUNTIME_STEP",
        "RUNTIME_READINESS_NOT_CONTINUATION",
        "RUNTIME_BOUNDARY_NOT_CREATED",
        "RUNTIME_NOT_CREATED",
        "RUNTIME_STEP_NOT_CREATED",
        "CHECKABILITY_NOT_CONTINUATION_PRESERVED",
        "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
        "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
        "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
        "PREDECESSOR_FAILURE_EVIDENCE_PRESERVED",
        "REPO_LOCAL_AVAILABILITY_NOT_RUNTIME_READINESS_AUTHORITY",
        "ARTIFACT_EXISTENCE_NOT_RUNTIME_READINESS_AUTHORITY",
        "LATEST_FILE_POSTURE_NOT_RUNTIME_READINESS_AUTHORITY",
    }
)

NON_CLAIM_BLOCK_CODE = {
    "runtime_created": "RUNTIME_CREATED",
    "runtime_boundary_created": "RUNTIME_BOUNDARY_CREATED",
    "runtime_step_created": "RUNTIME_STEP_CREATED",
    "continuation_authorized": "CONTINUATION_AUTHORIZED",
    "source_transfer_occurred": "SOURCE_TRANSFER_OCCURRED",
    "source_receipt_occurred": "SOURCE_RECEIPT_OCCURRED",
    "reception_authorization_created": "RECEPTION_AUTHORIZATION_CREATED",
    "runtime_readiness_treated_as_runtime": "RUNTIME_READINESS_TREATED_AS_RUNTIME",
    "runtime_readiness_treated_as_runtime_boundary": "RUNTIME_READINESS_TREATED_AS_RUNTIME_BOUNDARY",
    "runtime_readiness_treated_as_runtime_step": "RUNTIME_READINESS_TREATED_AS_RUNTIME_STEP",
    "runtime_readiness_treated_as_continuation": "RUNTIME_READINESS_TREATED_AS_CONTINUATION",
    "runtime_readiness_treated_as_source_transfer": "RUNTIME_READINESS_TREATED_AS_SOURCE_TRANSFER",
    "runtime_readiness_treated_as_source_receipt": "RUNTIME_READINESS_TREATED_AS_SOURCE_RECEIPT",
    "runtime_readiness_treated_as_reception_authorization": "RUNTIME_READINESS_TREATED_AS_RECEPTION_AUTHORIZATION",
    "runtime_readiness_treated_as_source": "RUNTIME_READINESS_TREATED_AS_SOURCE",
    "runtime_readiness_treated_as_authority": "RUNTIME_READINESS_TREATED_AS_AUTHORITY",
    "runtime_readiness_treated_as_currentness": "RUNTIME_READINESS_TREATED_AS_CURRENTNESS",
    "runtime_readiness_treated_as_deployment": "RUNTIME_READINESS_TREATED_AS_DEPLOYMENT",
    "runtime_readiness_treated_as_public_release": "RUNTIME_READINESS_TREATED_AS_PUBLIC_RELEASE",
    "runtime_readiness_treated_as_operation_permission": "RUNTIME_READINESS_TREATED_AS_OPERATION_PERMISSION",
    "runtime_readiness_treated_as_reusable_permission": "RUNTIME_READINESS_TREATED_AS_REUSABLE_PERMISSION",
    "runtime_readiness_treated_as_follow_on_work": "RUNTIME_READINESS_TREATED_AS_FOLLOW_ON_WORK",
    "runtime_readiness_boundary_treated_as_runtime_readiness_without_review": "RUNTIME_READINESS_BOUNDARY_TREATED_BOUNDARY_AS_RUNTIME_READINESS",
    "portable_verification_final_completion_treated_as_runtime": "RUNTIME_READINESS_BOUNDARY_TREATED_FINAL_COMPLETION_AS_RUNTIME",
    "portable_verification_final_completion_treated_as_continuation": "RUNTIME_READINESS_BOUNDARY_TREATED_FINAL_COMPLETION_AS_CONTINUATION",
    "post_portable_verification_currentness_surface_treated_as_runtime_permission": "RUNTIME_READINESS_BOUNDARY_TREATED_CURRENTNESS_SURFACE_AS_RUNTIME_PERMISSION",
    "post_portable_verification_currentness_surface_treated_as_operation_permission": "RUNTIME_READINESS_BOUNDARY_TREATED_CURRENTNESS_SURFACE_AS_OPERATION_PERMISSION",
    "checkability_treated_as_continuation": "RUNTIME_READINESS_BOUNDARY_TREATED_CHECKABILITY_AS_CONTINUATION",
    "artifact_existence_treated_as_runtime_readiness_authority": "ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_READINESS_AUTHORITY",
    "artifact_path_treated_as_currentness": "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "latest_file_posture_treated_as_runtime_readiness_authority": "LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_READINESS_AUTHORITY",
    "repo_local_availability_treated_as_runtime_readiness_authority": "REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_READINESS_AUTHORITY",
    "hidden_repo_state_used_as_runtime_readiness_content": "HIDDEN_REPO_STATE_USED_AS_RUNTIME_READINESS_CONTENT",
    "hidden_repo_state_used_as_runtime_readiness_authority": "HIDDEN_REPO_STATE_USED_AS_RUNTIME_READINESS_AUTHORITY",
    "source_created": "SOURCE_CREATED",
    "authority_created": "AUTHORITY_CREATED",
    "currentness_created": "CURRENTNESS_CREATED",
    "deployment_created": "DEPLOYMENT_CREATED",
    "public_release_created": "PUBLIC_RELEASE_CREATED",
    "operation_permission_created": "OPERATION_PERMISSION_CREATED",
    "reusable_permission_created": "REUSABLE_PERMISSION_CREATED",
    "derivative_reception_authorized": "DERIVATIVE_RECEPTION_AUTHORIZED",
    "vessel_relation_authorized": "VESSEL_RELATION_AUTHORIZED",
    "another_reception_request_authorized": "ANOTHER_RECEPTION_REQUEST_AUTHORIZED",
    "adoption_created": "ADOPTION_CREATED",
    "receiving_context_governance_created": "RECEIVING_CONTEXT_GOVERNANCE_CREATED",
    "publication_flow_created": "PUBLICATION_FLOW_CREATED",
    "follow_on_work_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
    "raw_full_prior_artifact_body_returned": "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "prior_artifacts_mutated": "ARTIFACTS_MUTATED",
    "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
    "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
    "predecessor_failure_repaired": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_hidden": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_claimed_passed": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
}

FORBIDDEN_OUTPUT_ROOT_FRAGMENTS = (
    "integrity_host_v0_min_coexistence_post_portable_verification_runtime_readiness_boundary",
    "integrity_host_v0_min_coexistence_portable_source_body_verification_final_completion",
    "integrity_host_v0_min_coexistence_portable_source_body_verification_final_completion_boundary",
    "integrity_host_v0_min_coexistence_portable_source_body_verification_portable_verification_closure",
    "integrity_host_v0_min_coexistence_portable_source_body_verification_portable_verification_closure_boundary",
    "integrity_host_v0_min_coexistence_portable_source_body_verification_cross_carrier_evidence",
    "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_external_result",
    "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_verification",
    "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_success",
    "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_result",
    "actual_second_carrier_live_capture",
    "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_output_capture",
    "integrity_host_v0_min_coexistence_portable_source_body_verification_packet_transfer",
    "integrity_host_v0_min_coexistence_portable_source_body_verification_packet_emission",
    "integrity_host_v0_min_coexistence_portable_source_body_verification_command_success",
    "integrity_host_v0_min_coexistence_portable_source_body_verification_command_result",
    "source_transfer",
    "source-transfer",
    "source_receipt",
    "source-receipt",
    "reception",
    "/runtime/",
    "runtime_boundary",
    "runtime-boundary",
    "deployment",
    "public_release",
    "public-release",
)


def _is_mapping(value: Any) -> bool:
    return hasattr(value, "items")


def _utc_now() -> str:
    return (
        datetime.datetime.now(datetime.timezone.utc)
        .isoformat(timespec="seconds")
        .replace("+00:00", "Z")
    )


def _present(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return value != ""
    if _is_mapping(value):
        return bool(dict(value))
    if isinstance(value, (list, tuple, set, frozenset)):
        return bool(value)
    return True


def _as_int(value: Any, default: int | None = None) -> int | None:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value.strip())
        except ValueError:
            return default
    return default


def _truth(value: Any) -> bool:
    if value is True:
        return True
    if _is_mapping(value):
        mapping = dict(value)
        if mapping.get("declared") is False:
            return False
        for key in ("value", "preserved", "recorded", "declared"):
            if key in mapping:
                return mapping.get(key) is True
    return False


def _request_field(
    request: Mapping[str, Any],
    key: str,
    sections: Iterable[str] = SELECTED_BASIS_FIELDS,
    default: Any = None,
) -> Any:
    if key in request:
        return request.get(key)
    for section_name in sections:
        section = request.get(section_name)
        if _is_mapping(section) and key in section:
            return dict(section).get(key)
    return default


def _sensitive_key(key: str | None) -> bool:
    if key is None:
        return False
    lowered = key.lower()
    return lowered in SENSITIVE_CONTENT_KEYS or lowered.endswith("_body")


def _sanitize(value: Any, parent_key: str | None = None) -> Any:
    if _sensitive_key(parent_key):
        if isinstance(value, str) and value in OFFICIAL_STRINGS:
            return value
        return REDACTED_RAW_VALUE
    if _is_mapping(value):
        return {str(key): _sanitize(val, str(key)) for key, val in dict(value).items()}
    if isinstance(value, (list, tuple)):
        return [_sanitize(item, parent_key) for item in value]
    if isinstance(value, (set, frozenset)):
        return sorted((_sanitize(item, parent_key) for item in value), key=str)
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, (datetime.datetime, datetime.date)):
        return value.isoformat()
    if isinstance(value, str):
        if value in OFFICIAL_STRINGS:
            return value
        if any(sentinel in value for sentinel in HOSTILE_SENTINELS):
            return REDACTED_RAW_VALUE
        return value
    if isinstance(value, (int, float, bool)) or value is None:
        return value
    return str(value)


def _sanitize_mapping(value: Any) -> dict[str, Any]:
    sanitized = _sanitize(value)
    if isinstance(sanitized, dict):
        return sanitized
    if sanitized in (None, ""):
        return {}
    return {"selected_basis_reference": sanitized}


def _check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    block_code: str,
) -> None:
    public_code = (
        block_code
        if block_code in BLOCK_CODES
        else "DECLARED_RUNTIME_READINESS_REQUEST_MALFORMED"
    )
    checks.append(
        {
            "check_name": check_name,
            "passed": bool(passed),
            "expected_posture": _sanitize(expected_posture),
            "actual_posture": _sanitize(actual_posture),
            "block_code": None if passed else public_code,
            "failure_code": None if passed else public_code,
        }
    )


def _first_failed_check(checks: Iterable[Mapping[str, Any]]) -> Mapping[str, Any] | None:
    for check in checks:
        if check.get("passed") is not True:
            return check
    return None


def _request_id(request: Mapping[str, Any]) -> str:
    value = request.get("runtime_readiness_request_id")
    if isinstance(value, str) and value:
        return value
    return DEFAULT_REQUEST_ID


def _declared_non_claims(request: Mapping[str, Any]) -> Mapping[str, Any]:
    value = request.get("declared_non_claims")
    if _is_mapping(value):
        return dict(value)
    return {}


def _scope_values(request: Mapping[str, Any]) -> list[Any]:
    value = request.get("runtime_readiness_scope")
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if _is_mapping(value):
        return list(dict(value).values())
    if isinstance(value, (list, tuple, set, frozenset)):
        return list(value)
    return [value]


def _reference_basis(
    basis_name: str,
    path: str,
    outcome: str | None = None,
    version: str = RESULT_VERSION,
    failed_check_count: int = 0,
    **extra: Any,
) -> dict[str, Any]:
    basis: dict[str, Any] = {
        "basis_name": basis_name,
        "selected_reference_path": path,
        "reference_shape_preserved": True,
        "raw_full_prior_artifact_body_returned": False,
        "hostile_raw_body_content_contained": True,
    }
    if outcome is not None:
        basis["outcome"] = outcome
        basis["result_version"] = version
        basis["failed_check_count"] = failed_check_count
    basis.update(extra)
    return basis


def _posture(posture_name: str) -> dict[str, Any]:
    return {"posture_name": posture_name, "declared": True, "value": True}


def _runtime_readiness_statement(recorded: bool) -> dict[str, bool]:
    statement: dict[str, bool] = {}
    for field_name in ALLOWED_TRUE_RECORDED_FIELDS:
        if field_name in RECORDING_STATEMENT_FIELDS:
            statement[field_name] = bool(recorded)
        else:
            statement[field_name] = True
    return statement


def _safe_non_claims() -> dict[str, bool]:
    return {field_name: False for field_name in REQUIRED_FALSE_NON_CLAIMS}


def _runtime_readiness_non_meaning() -> dict[str, bool]:
    return {
        "runtime_readiness_is_runtime": False,
        "runtime_readiness_is_runtime_boundary": False,
        "runtime_readiness_is_runtime_step": False,
        "runtime_readiness_is_continuation": False,
        "runtime_readiness_is_source_transfer": False,
        "runtime_readiness_is_source_receipt": False,
        "runtime_readiness_is_reception_authorization": False,
        "runtime_readiness_is_source": False,
        "runtime_readiness_is_authority": False,
        "runtime_readiness_is_currentness": False,
        "runtime_readiness_is_deployment": False,
        "runtime_readiness_is_public_release": False,
        "runtime_readiness_is_operation_permission": False,
        "runtime_readiness_is_follow_on_work": False,
        "runtime_boundary_exists_here": False,
        "runtime_exists_here": False,
        "runtime_step_exists_here": False,
        "continuation_is_authorized_here": False,
        "checkability_beyond_original_carrier_is_continuation": False,
        "artifact_existence_is_runtime_readiness_authority": False,
        "repo_local_availability_is_runtime_readiness_authority": False,
        "latest_file_posture_is_runtime_readiness_authority": False,
        "hidden_repo_state_is_runtime_readiness_authority": False,
    }


def _what_remains_open() -> list[str]:
    return [
        "runtime-readiness resolver",
        "runtime-readiness test",
        "runtime-readiness live artifact",
        "runtime-readiness terminal summary, if needed",
        "runtime boundary",
        "minimal runtime specification",
        "minimal runtime resolver/test/live artifact",
        "runtime result/refusal artifact",
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
        "runtime hosting",
        "deployment",
        "public release",
        "continuation",
        "publication flow",
        "reusable permission",
        "successor reception request",
        "follow-on work",
    ]


def _posture_block_code(posture_field: str) -> str:
    mapping = {
        "runtime_readiness_spec_only_posture": "RUNTIME_READINESS_TREATED_AS_RUNTIME",
        "one_bounded_runtime_readiness_posture": "RUNTIME_READINESS_TREATED_AS_RUNTIME",
        "runtime_readiness_boundary_basis_preserved_posture": "RUNTIME_READINESS_BOUNDARY_BASIS_MISSING",
        "portable_verification_final_completion_basis_preserved_posture": "FINAL_COMPLETION_BASIS_MISSING",
        "post_portable_verification_currentness_basis_preserved_posture": "POST_PORTABLE_VERIFICATION_CURRENTNESS_BASIS_MISSING",
        "checkability_not_continuation_preserved_posture": "RUNTIME_READINESS_BOUNDARY_TREATED_CHECKABILITY_AS_CONTINUATION",
        "runtime_readiness_not_runtime_posture": "RUNTIME_READINESS_TREATED_AS_RUNTIME",
        "runtime_readiness_not_runtime_boundary_posture": "RUNTIME_READINESS_TREATED_AS_RUNTIME_BOUNDARY",
        "runtime_readiness_not_runtime_step_posture": "RUNTIME_READINESS_TREATED_AS_RUNTIME_STEP",
        "runtime_readiness_not_continuation_posture": "RUNTIME_READINESS_TREATED_AS_CONTINUATION",
        "runtime_boundary_not_created_posture": "RUNTIME_BOUNDARY_CREATED",
        "runtime_not_created_posture": "RUNTIME_CREATED",
        "runtime_step_not_created_posture": "RUNTIME_STEP_CREATED",
        "continuation_not_authorized_posture": "CONTINUATION_AUTHORIZED",
        "source_transfer_not_created_posture": "SOURCE_TRANSFER_OCCURRED",
        "source_receipt_not_created_posture": "SOURCE_RECEIPT_OCCURRED",
        "reception_authorization_not_created_posture": "RECEPTION_AUTHORIZATION_CREATED",
        "source_not_created_posture": "SOURCE_CREATED",
        "authority_not_created_posture": "AUTHORITY_CREATED",
        "currentness_not_created_posture": "CURRENTNESS_CREATED",
        "deployment_not_created_posture": "DEPLOYMENT_CREATED",
        "public_release_not_created_posture": "PUBLIC_RELEASE_CREATED",
        "operation_permission_not_created_posture": "OPERATION_PERMISSION_CREATED",
        "reusable_permission_not_created_posture": "REUSABLE_PERMISSION_CREATED",
        "follow_on_work_not_authorized_posture": "FOLLOW_ON_WORK_AUTHORIZED",
        "hidden_repo_state_excluded_posture": "HIDDEN_REPO_STATE_USED_AS_RUNTIME_READINESS_CONTENT",
        "repo_local_availability_not_runtime_readiness_authority_posture": "REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_READINESS_AUTHORITY",
        "artifact_existence_not_runtime_readiness_authority_posture": "ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_READINESS_AUTHORITY",
        "latest_file_posture_not_runtime_readiness_authority_posture": "LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_READINESS_AUTHORITY",
        "selected_basis_reference_shape_posture": "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
        "raw_full_prior_artifact_body_not_returned_posture": "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
        "official_enum_scope_strings_not_redacted_posture": "UNSUPPORTED_RUNTIME_READINESS_SCOPE",
        "hostile_raw_body_content_contained_posture": "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
        "predecessor_failure_evidence_preserved_posture": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    }
    return mapping.get(posture_field, "RUNTIME_READINESS_QUESTION_UNDECLARED")


def _add_core_checks(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    forced_block_code: str | None = None,
    forced_block_reason: str | None = None,
) -> None:
    if forced_block_code is not None:
        _check(
            checks,
            "declared runtime-readiness request readable and mapping-shaped",
            False,
            "readable mapping declared runtime-readiness request",
            forced_block_reason or forced_block_code,
            forced_block_code,
        )

    question = request.get("runtime_readiness_question")
    intent = request.get("runtime_readiness_intent")
    scope = _scope_values(request)
    unsupported_scope = [value for value in scope if value not in SUPPORTED_SCOPE_VALUES]
    non_claims = _declared_non_claims(request)

    _check(
        checks,
        "runtime-readiness question declared",
        question == CORE_QUESTION,
        CORE_QUESTION,
        question,
        "RUNTIME_READINESS_QUESTION_UNDECLARED",
    )
    _check(
        checks,
        "intent supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "RUNTIME_READINESS_INTENT_UNSUPPORTED",
    )
    _check(
        checks,
        "explicit block intent absent",
        intent != INTENT_BLOCK,
        "record or do-not-record runtime-readiness intent",
        intent,
        "RUNTIME_READINESS_REQUEST_DECLARED_BLOCK",
    )
    _check(
        checks,
        "runtime-readiness scope supported",
        bool(scope) and not unsupported_scope,
        SUPPORTED_SCOPE_VALUES,
        unsupported_scope or scope,
        "UNSUPPORTED_RUNTIME_READINESS_SCOPE",
    )

    for basis_field, code in (
        ("selected_runtime_readiness_boundary_basis", "RUNTIME_READINESS_BOUNDARY_BASIS_MISSING"),
        (
            "selected_runtime_readiness_boundary_terminal_summary_basis",
            "RUNTIME_READINESS_BOUNDARY_BASIS_MISSING",
        ),
    ):
        _check(
            checks,
            f"{basis_field} declared",
            _present(request.get(basis_field)),
            f"{basis_field} present",
            request.get(basis_field),
            code,
        )

    _check(
        checks,
        "runtime-readiness-boundary outcome recorded",
        _request_field(request, "selected_runtime_readiness_boundary_result_outcome")
        == EXPECTED_RUNTIME_READINESS_BOUNDARY_OUTCOME,
        EXPECTED_RUNTIME_READINESS_BOUNDARY_OUTCOME,
        _request_field(request, "selected_runtime_readiness_boundary_result_outcome"),
        "RUNTIME_READINESS_BOUNDARY_NOT_RECORDED",
    )
    _check(
        checks,
        "runtime-readiness-boundary version 0.1.0",
        _request_field(request, "selected_runtime_readiness_boundary_result_version")
        == RESULT_VERSION,
        RESULT_VERSION,
        _request_field(request, "selected_runtime_readiness_boundary_result_version"),
        "RUNTIME_READINESS_BOUNDARY_VERSION_NOT_0_1_0",
    )
    _check(
        checks,
        "runtime-readiness-boundary failed checks zero",
        _as_int(
            _request_field(request, "selected_runtime_readiness_boundary_failed_check_count")
        )
        == 0,
        0,
        _request_field(request, "selected_runtime_readiness_boundary_failed_check_count"),
        "RUNTIME_READINESS_BOUNDARY_FAILED_CHECKS_PRESENT",
    )
    _check(
        checks,
        "runtime-readiness-boundary declared future runtime-readiness review step",
        _request_field(
            request,
            "selected_runtime_readiness_boundary_declared_future_runtime_readiness_review_step",
        )
        is True,
        True,
        _request_field(
            request,
            "selected_runtime_readiness_boundary_declared_future_runtime_readiness_review_step",
        ),
        "RUNTIME_READINESS_BOUNDARY_DID_NOT_DECLARE_FUTURE_RUNTIME_READINESS_REVIEW_STEP",
    )

    for field_name, code in (
        (
            "selected_runtime_readiness_boundary_already_created_runtime_readiness",
            "RUNTIME_READINESS_BOUNDARY_ALREADY_CREATED_RUNTIME_READINESS",
        ),
        (
            "selected_runtime_readiness_boundary_already_created_runtime",
            "RUNTIME_READINESS_BOUNDARY_ALREADY_CREATED_RUNTIME",
        ),
        (
            "selected_runtime_readiness_boundary_already_authorized_continuation",
            "RUNTIME_READINESS_BOUNDARY_ALREADY_AUTHORIZED_CONTINUATION",
        ),
        (
            "selected_runtime_readiness_boundary_treated_boundary_as_runtime_readiness",
            "RUNTIME_READINESS_BOUNDARY_TREATED_BOUNDARY_AS_RUNTIME_READINESS",
        ),
        (
            "selected_runtime_readiness_boundary_treated_boundary_as_runtime",
            "RUNTIME_READINESS_BOUNDARY_TREATED_BOUNDARY_AS_RUNTIME",
        ),
        (
            "selected_runtime_readiness_boundary_treated_checkability_as_continuation",
            "RUNTIME_READINESS_BOUNDARY_TREATED_CHECKABILITY_AS_CONTINUATION",
        ),
        (
            "selected_runtime_readiness_boundary_treated_final_completion_as_runtime",
            "RUNTIME_READINESS_BOUNDARY_TREATED_FINAL_COMPLETION_AS_RUNTIME",
        ),
        (
            "selected_runtime_readiness_boundary_treated_final_completion_as_continuation",
            "RUNTIME_READINESS_BOUNDARY_TREATED_FINAL_COMPLETION_AS_CONTINUATION",
        ),
        (
            "selected_runtime_readiness_boundary_treated_currentness_surface_as_runtime_permission",
            "RUNTIME_READINESS_BOUNDARY_TREATED_CURRENTNESS_SURFACE_AS_RUNTIME_PERMISSION",
        ),
        (
            "selected_runtime_readiness_boundary_treated_currentness_surface_as_operation_permission",
            "RUNTIME_READINESS_BOUNDARY_TREATED_CURRENTNESS_SURFACE_AS_OPERATION_PERMISSION",
        ),
        (
            "selected_runtime_readiness_boundary_authorized_future_work",
            "RUNTIME_READINESS_BOUNDARY_AUTHORIZED_FUTURE_WORK",
        ),
    ):
        _check(
            checks,
            field_name.replace("_", " "),
            _request_field(request, field_name) is not True,
            False,
            _request_field(request, field_name),
            code,
        )

    for field_name, code in (
        ("runtime_readiness_created_before_review", "RUNTIME_READINESS_CREATED_BEFORE_REVIEW"),
        ("runtime_created", "RUNTIME_CREATED"),
        ("runtime_boundary_created", "RUNTIME_BOUNDARY_CREATED"),
        ("runtime_step_created", "RUNTIME_STEP_CREATED"),
        ("continuation_authorized", "CONTINUATION_AUTHORIZED"),
    ):
        _check(
            checks,
            field_name.replace("_", " "),
            request.get(field_name) is not True,
            False,
            request.get(field_name),
            code,
        )

    for basis_field in (
        "selected_portable_verification_final_completion_basis",
        "selected_final_completion_artifact_basis",
    ):
        _check(
            checks,
            f"{basis_field} declared",
            _present(request.get(basis_field)),
            f"{basis_field} present",
            request.get(basis_field),
            "FINAL_COMPLETION_BASIS_MISSING",
        )
    _check(
        checks,
        "portable verification final-completion outcome recorded",
        _request_field(request, "selected_portable_verification_final_completion_result_outcome")
        == EXPECTED_FINAL_COMPLETION_OUTCOME,
        EXPECTED_FINAL_COMPLETION_OUTCOME,
        _request_field(request, "selected_portable_verification_final_completion_result_outcome"),
        "FINAL_COMPLETION_NOT_RECORDED",
    )
    _check(
        checks,
        "portable verification final-completion version 0.1.0",
        _request_field(request, "selected_portable_verification_final_completion_result_version")
        == RESULT_VERSION,
        RESULT_VERSION,
        _request_field(request, "selected_portable_verification_final_completion_result_version"),
        "FINAL_COMPLETION_VERSION_NOT_0_1_0",
    )
    _check(
        checks,
        "portable verification final-completion failed checks zero",
        _as_int(
            _request_field(
                request,
                "selected_portable_verification_final_completion_failed_check_count",
            )
        )
        == 0,
        0,
        _request_field(
            request,
            "selected_portable_verification_final_completion_failed_check_count",
        ),
        "FINAL_COMPLETION_FAILED_CHECKS_PRESENT",
    )

    _check(
        checks,
        "post-portable currentness surface basis declared",
        _present(request.get("selected_post_portable_verification_currentness_basis")),
        "selected post-portable-verification currentness surface basis",
        request.get("selected_post_portable_verification_currentness_basis"),
        "POST_PORTABLE_VERIFICATION_CURRENTNESS_BASIS_MISSING",
    )
    _check(
        checks,
        "post-portable currentness surface states checkability not continuation",
        _request_field(
            request,
            "selected_post_portable_currentness_surface_states_checkability_not_continuation",
        )
        is True,
        True,
        _request_field(
            request,
            "selected_post_portable_currentness_surface_states_checkability_not_continuation",
        ),
        "RUNTIME_READINESS_BOUNDARY_TREATED_CHECKABILITY_AS_CONTINUATION",
    )
    _check(
        checks,
        "post-portable currentness surface does not authorize next work",
        _request_field(request, "selected_post_portable_currentness_surface_authorized_next_work")
        is not True,
        False,
        _request_field(request, "selected_post_portable_currentness_surface_authorized_next_work"),
        "POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_AUTHORIZED_NEXT_WORK",
    )

    _check(
        checks,
        "predecessor failure evidence visible and unrepaired",
        request.get("predecessor_failure_evidence_preserved") is True
        and request.get("predecessor_failure_repaired") is False
        and request.get("predecessor_failure_hidden") is False
        and request.get("predecessor_failure_claimed_passed") is False,
        "predecessor failure evidence visible and unrepaired",
        {
            "preserved": request.get("predecessor_failure_evidence_preserved"),
            "repaired": request.get("predecessor_failure_repaired"),
            "hidden": request.get("predecessor_failure_hidden"),
            "claimed_passed": request.get("predecessor_failure_claimed_passed"),
        },
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    )
    _check(
        checks,
        "selected basis reference-shaped",
        request.get("reference_shaped_input_posture") is not False,
        "selected basis reference-shaped",
        request.get("reference_shaped_input_posture"),
        "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    )

    for posture_field in POSTURE_FIELDS:
        _check(
            checks,
            f"{posture_field} declared",
            _truth(request.get(posture_field)),
            "posture declared true",
            request.get(posture_field),
            _posture_block_code(posture_field),
        )

    for field_name in REQUIRED_FALSE_NON_CLAIMS:
        _check(
            checks,
            f"required non-claim false: {field_name}",
            non_claims.get(field_name) is False,
            False,
            non_claims.get(field_name),
            NON_CLAIM_BLOCK_CODE.get(field_name, "NON_CLAIM_MISSING_OR_FLIPPED"),
        )

    _check(
        checks,
        "official enum scope strings not redacted",
        not any(value in {REFERENCE_SHAPED_REDACTION, REDACTED_RAW_VALUE} for value in scope),
        "official scope values preserved",
        scope,
        "UNSUPPORTED_RUNTIME_READINESS_SCOPE",
    )
    _check(
        checks,
        "hostile raw body content contained",
        _truth(request.get("hostile_raw_body_content_contained_posture")),
        "hostile raw body content contained",
        request.get("hostile_raw_body_content_contained_posture"),
        "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    )


def _resolve_mapping(
    request: Mapping[str, Any],
    forced_block_code: str | None = None,
    forced_block_reason: str | None = None,
) -> dict[str, Any]:
    request_copy = copy.deepcopy(dict(request))
    checks: list[dict[str, Any]] = []
    _add_core_checks(request_copy, checks, forced_block_code, forced_block_reason)

    failed_check = _first_failed_check(checks)
    requested_outcome = request_copy.get("requested_runtime_readiness_outcome")
    intent = request_copy.get("runtime_readiness_intent")
    if failed_check is not None:
        outcome = OUTCOME_BLOCKED
        block_code = str(
            failed_check.get("block_code")
            or failed_check.get("failure_code")
            or "DECLARED_RUNTIME_READINESS_REQUEST_MALFORMED"
        )
        block_reason = str(failed_check.get("actual_posture"))
    elif intent == INTENT_DO_NOT_RECORD or requested_outcome == OUTCOME_NOT_RECORDED:
        outcome = OUTCOME_NOT_RECORDED
        block_code = None
        block_reason = None
    elif requested_outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
        block_code = None
        block_reason = None
    else:
        outcome = OUTCOME_RECORDED
        block_code = None
        block_reason = None

    recorded = outcome == OUTCOME_RECORDED
    metadata = {
        "post_portable_verification_runtime_readiness_id": _request_id(request_copy),
        "post_portable_verification_runtime_readiness_type": RESULT_TYPE,
        "post_portable_verification_runtime_readiness_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
    }
    result: dict[str, Any] = {
        "post_portable_verification_runtime_readiness_metadata": metadata,
        "declared_runtime_readiness_question": {
            "runtime_readiness_request_id": _request_id(request_copy),
            "runtime_readiness_question": request_copy.get("runtime_readiness_question"),
            "runtime_readiness_intent": request_copy.get("runtime_readiness_intent"),
        },
    }

    for field_name in SELECTED_BASIS_FIELDS:
        result[field_name] = _sanitize_mapping(request_copy.get(field_name))
    for posture_field in POSTURE_FIELDS:
        result[posture_field] = _sanitize_mapping(request_copy.get(posture_field))

    result.update(
        {
            "runtime_readiness_scope": _sanitize(_scope_values(request_copy)),
            "runtime_readiness_checks": checks,
            "runtime_readiness_statement": _runtime_readiness_statement(recorded),
            "runtime_readiness_non_meaning": _runtime_readiness_non_meaning(),
            "additional_basis_required": _sanitize(
                request_copy.get("additional_basis_context", [])
                if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
                else []
            ),
            "not_recorded_basis": _sanitize(
                request_copy.get("not_recorded_basis", [])
                if outcome == OUTCOME_NOT_RECORDED
                else []
            ),
            "what_remains_open": _what_remains_open(),
            "non_claims": _safe_non_claims(),
            "outcome": outcome,
            "block": None
            if block_code is None
            else {"block_code": block_code, "block_reason": block_reason},
        }
    )
    result["post_portable_verification_runtime_readiness_summary"] = (
        build_post_portable_verification_runtime_readiness_summary(result)
    )
    return result


def resolve_post_portable_verification_runtime_readiness(
    declared_runtime_readiness_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded runtime-readiness posture."""

    if declared_runtime_readiness_request is None:
        return _resolve_mapping(
            {},
            "DECLARED_RUNTIME_READINESS_REQUEST_MALFORMED",
            "declared runtime-readiness request is missing",
        )
    if not _is_mapping(declared_runtime_readiness_request):
        return _resolve_mapping(
            {"malformed_request_type": type(declared_runtime_readiness_request).__name__},
            "DECLARED_RUNTIME_READINESS_REQUEST_MALFORMED",
            "declared runtime-readiness request is not a mapping",
        )
    return _resolve_mapping(declared_runtime_readiness_request)


def resolve_post_portable_verification_runtime_readiness_from_path(
    declared_runtime_readiness_request_path: Path | str,
) -> dict[str, Any]:
    """Load a declared runtime-readiness request JSON file and resolve it."""

    try:
        path = Path(declared_runtime_readiness_request_path)
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        return _resolve_mapping(
            {"runtime_readiness_request_id": DEFAULT_REQUEST_ID},
            "DECLARED_RUNTIME_READINESS_REQUEST_UNREADABLE",
            str(exc),
        )
    try:
        loaded = json.loads(raw)
    except json.JSONDecodeError as exc:
        return _resolve_mapping(
            {"runtime_readiness_request_id": DEFAULT_REQUEST_ID},
            "DECLARED_RUNTIME_READINESS_REQUEST_MALFORMED",
            str(exc),
        )
    if not _is_mapping(loaded):
        return _resolve_mapping(
            {"runtime_readiness_request_id": DEFAULT_REQUEST_ID},
            "DECLARED_RUNTIME_READINESS_REQUEST_MALFORMED",
            "declared runtime-readiness request JSON root is not an object",
        )
    return resolve_post_portable_verification_runtime_readiness(loaded)


def build_post_portable_verification_runtime_readiness_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact JSON-safe summary for a runtime-readiness result."""

    checks = result.get("runtime_readiness_checks", [])
    if not isinstance(checks, list):
        checks = []
    passed_count = sum(
        1 for check in checks if _is_mapping(check) and check.get("passed") is True
    )
    failed_count = sum(
        1 for check in checks if _is_mapping(check) and check.get("passed") is not True
    )
    metadata = result.get("post_portable_verification_runtime_readiness_metadata", {})
    question = result.get("declared_runtime_readiness_question", {})
    statement = result.get("runtime_readiness_statement", {})
    non_claims = result.get("non_claims", {})
    block = result.get("block")
    if not _is_mapping(metadata):
        metadata = {}
    if not _is_mapping(question):
        question = {}
    if not _is_mapping(statement):
        statement = {}
    if not _is_mapping(non_claims):
        non_claims = {}
    if not _is_mapping(block):
        block = {}

    summary = {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "request_id": question.get("runtime_readiness_request_id")
        or metadata.get("post_portable_verification_runtime_readiness_id"),
        "question": question.get("runtime_readiness_question"),
        "intent": question.get("runtime_readiness_intent"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": metadata.get(
            "post_portable_verification_runtime_readiness_version"
        ),
        "resolver_module": metadata.get("resolver_module"),
        "runtime_readiness_recorded": statement.get("runtime_readiness_recorded"),
        "bounded_runtime_readiness_recorded": statement.get(
            "bounded_runtime_readiness_recorded"
        ),
        "runtime_readiness_boundary_basis_preserved": statement.get(
            "runtime_readiness_boundary_basis_preserved"
        ),
        "portable_verification_final_completion_basis_preserved": statement.get(
            "portable_verification_final_completion_basis_preserved"
        ),
        "post_portable_verification_currentness_basis_preserved": statement.get(
            "post_portable_verification_currentness_basis_preserved"
        ),
        "checkability_not_continuation_preserved": statement.get(
            "checkability_not_continuation_preserved"
        ),
        "runtime_readiness_not_runtime": statement.get(
            "runtime_readiness_not_runtime"
        ),
        "runtime_readiness_not_runtime_boundary": statement.get(
            "runtime_readiness_not_runtime_boundary"
        ),
        "runtime_readiness_not_runtime_step": statement.get(
            "runtime_readiness_not_runtime_step"
        ),
        "runtime_readiness_not_continuation": statement.get(
            "runtime_readiness_not_continuation"
        ),
        "runtime_boundary_not_created": statement.get("runtime_boundary_not_created"),
        "runtime_not_created": statement.get("runtime_not_created"),
        "runtime_step_not_created": statement.get("runtime_step_not_created"),
        "continuation_not_authorized": statement.get("continuation_not_authorized"),
        "source_transfer_not_created": statement.get("source_transfer_not_created"),
        "source_receipt_not_created": statement.get("source_receipt_not_created"),
        "reception_authorization_not_created": statement.get(
            "reception_authorization_not_created"
        ),
        "source_not_created": statement.get("source_not_created"),
        "authority_not_created": statement.get("authority_not_created"),
        "currentness_not_created": statement.get("currentness_not_created"),
        "deployment_not_created": statement.get("deployment_not_created"),
        "public_release_not_created": statement.get("public_release_not_created"),
        "operation_permission_not_created": statement.get(
            "operation_permission_not_created"
        ),
        "follow_on_work_not_authorized": statement.get(
            "follow_on_work_not_authorized"
        ),
        "hidden_repo_state_excluded": statement.get("hidden_repo_state_excluded"),
        "hidden_repo_state_not_used_as_runtime_readiness_authority": statement.get(
            "hidden_repo_state_not_used_as_runtime_readiness_authority"
        ),
        "repo_local_availability_not_runtime_readiness_authority": statement.get(
            "repo_local_availability_not_runtime_readiness_authority"
        ),
        "artifact_existence_not_runtime_readiness_authority": statement.get(
            "artifact_existence_not_runtime_readiness_authority"
        ),
        "latest_file_posture_not_runtime_readiness_authority": statement.get(
            "latest_file_posture_not_runtime_readiness_authority"
        ),
        "selected_basis_reference_shape_preserved": statement.get(
            "selected_basis_reference_shape_preserved"
        ),
        "raw_full_prior_artifact_body_not_returned": statement.get(
            "raw_full_prior_artifact_body_not_returned"
        ),
        "official_enum_scope_strings_not_redacted": statement.get(
            "official_enum_scope_strings_not_redacted"
        ),
        "hostile_raw_body_content_contained": statement.get(
            "hostile_raw_body_content_contained"
        ),
        "selected_runtime_readiness_boundary_outcome": _summary_request_value(
            result, "selected_runtime_readiness_boundary_result_outcome"
        ),
        "selected_runtime_readiness_boundary_version": _summary_request_value(
            result, "selected_runtime_readiness_boundary_result_version"
        ),
        "selected_runtime_readiness_boundary_failed_check_count": _summary_request_value(
            result, "selected_runtime_readiness_boundary_failed_check_count"
        ),
        "selected_final_completion_outcome": _summary_request_value(
            result, "selected_portable_verification_final_completion_result_outcome"
        ),
        "selected_final_completion_version": _summary_request_value(
            result, "selected_portable_verification_final_completion_result_version"
        ),
        "selected_final_completion_failed_check_count": _summary_request_value(
            result, "selected_portable_verification_final_completion_failed_check_count"
        ),
        "selected_post_portable_currentness_surface_path": _summary_request_value(
            result, "selected_post_portable_currentness_surface_path"
        ),
        "no_runtime_runtime_boundary_runtime_step_continuation_source_authority_currentness_deployment_public_release_follow_on": (
            non_claims.get("runtime_created") is False
            and non_claims.get("runtime_boundary_created") is False
            and non_claims.get("runtime_step_created") is False
            and non_claims.get("continuation_authorized") is False
            and non_claims.get("source_created") is False
            and non_claims.get("authority_created") is False
            and non_claims.get("currentness_created") is False
            and non_claims.get("deployment_created") is False
            and non_claims.get("public_release_created") is False
            and non_claims.get("follow_on_work_authorized") is False
        ),
        "key_non_claims": {
            "runtime_created": non_claims.get("runtime_created"),
            "runtime_boundary_created": non_claims.get("runtime_boundary_created"),
            "runtime_step_created": non_claims.get("runtime_step_created"),
            "continuation_authorized": non_claims.get("continuation_authorized"),
            "runtime_readiness_treated_as_runtime": non_claims.get(
                "runtime_readiness_treated_as_runtime"
            ),
            "runtime_readiness_treated_as_runtime_boundary": non_claims.get(
                "runtime_readiness_treated_as_runtime_boundary"
            ),
            "runtime_readiness_treated_as_runtime_step": non_claims.get(
                "runtime_readiness_treated_as_runtime_step"
            ),
            "authorization_token_reused": non_claims.get("authorization_token_reused"),
            "consumed_request_reopened": non_claims.get("consumed_request_reopened"),
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
    return _sanitize_mapping(summary)


def _summary_request_value(result: Mapping[str, Any], key: str) -> Any:
    for section_name in SELECTED_BASIS_FIELDS:
        section = result.get(section_name)
        if _is_mapping(section) and key in section:
            return section.get(key)
    return None


def write_post_portable_verification_runtime_readiness_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write a runtime-readiness result JSON file without overwrite."""

    if not _is_mapping(result):
        raise PostPortableVerificationRuntimeReadinessError(
            "runtime-readiness result must be a mapping"
        )
    metadata = result.get("post_portable_verification_runtime_readiness_metadata", {})
    request_id = DEFAULT_REQUEST_ID
    if _is_mapping(metadata):
        value = metadata.get("post_portable_verification_runtime_readiness_id")
        if isinstance(value, str) and value:
            request_id = value
    filename = f"{request_id}__post_portable_verification_runtime_readiness_result.json"
    if output_path is None:
        candidate = OUTPUT_ROOT / filename
    else:
        candidate = Path(output_path)
        if candidate.suffix != ".json":
            candidate = candidate / filename
    candidate = _ensure_allowed_output_path(candidate)
    candidate.parent.mkdir(parents=True, exist_ok=True)
    final_path = _with_numeric_suffix_if_exists(candidate)
    final_path.write_text(
        json.dumps(_sanitize(result), indent=2, sort_keys=True, ensure_ascii=False)
        + "\n",
        encoding="utf-8",
    )
    return final_path


def _ensure_allowed_output_path(path: Path) -> Path:
    normalized = path.as_posix()
    default_root = OUTPUT_ROOT.as_posix()
    if default_root in normalized:
        return path
    for fragment in FORBIDDEN_OUTPUT_ROOT_FRAGMENTS:
        if fragment in normalized:
            raise PostPortableVerificationRuntimeReadinessError(
                "refusing to write runtime-readiness result into "
                f"prohibited root: {fragment}"
            )
    return path


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


def build_declared_post_portable_verification_runtime_readiness_request(
    runtime_readiness_request_id: str = DEFAULT_REQUEST_ID,
    runtime_readiness_question: str = CORE_QUESTION,
    runtime_readiness_intent: str = INTENT_RECORD,
    runtime_readiness_scope: Iterable[str] | None = None,
    declared_non_claims: Mapping[str, bool] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build a clean declared request for one bounded runtime-readiness review."""

    non_claims = _safe_non_claims()
    if declared_non_claims is not None:
        non_claims.update(dict(declared_non_claims))
    scope = list(runtime_readiness_scope or SUPPORTED_SCOPE_VALUES)
    boundary_artifact_path = (
        "artifacts/integrity_host_v0_min_coexistence_post_portable_verification_"
        "runtime_readiness_boundary/"
        "post_portable_verification_runtime_readiness_boundary_reference_review_001"
        "__post_portable_verification_runtime_readiness_boundary_result.json"
    )
    final_completion_artifact_path = (
        "artifacts/integrity_host_v0_min_coexistence_portable_source_body_"
        "verification_final_completion/"
        "portable_source_body_verification_final_completion_reference_review_001"
        "__portable_source_body_verification_final_completion_result.json"
    )
    request: dict[str, Any] = {
        "runtime_readiness_request_id": runtime_readiness_request_id,
        "runtime_readiness_question": runtime_readiness_question,
        "runtime_readiness_intent": runtime_readiness_intent,
        "runtime_readiness_scope": scope,
        "declared_non_claims": non_claims,
        "requested_runtime_readiness_outcome": OUTCOME_RECORDED,
        "selected_runtime_readiness_boundary_basis": _reference_basis(
            "post_portable_verification_runtime_readiness_boundary_artifact",
            boundary_artifact_path,
            EXPECTED_RUNTIME_READINESS_BOUNDARY_OUTCOME,
            selected_runtime_readiness_boundary_result_path=boundary_artifact_path,
            selected_runtime_readiness_boundary_result_outcome=EXPECTED_RUNTIME_READINESS_BOUNDARY_OUTCOME,
            selected_runtime_readiness_boundary_result_version=RESULT_VERSION,
            selected_runtime_readiness_boundary_failed_check_count=0,
            selected_runtime_readiness_boundary_declared_future_runtime_readiness_review_step=True,
            selected_runtime_readiness_boundary_already_created_runtime_readiness=False,
            selected_runtime_readiness_boundary_already_created_runtime=False,
            selected_runtime_readiness_boundary_already_authorized_continuation=False,
            selected_runtime_readiness_boundary_treated_boundary_as_runtime_readiness=False,
            selected_runtime_readiness_boundary_treated_boundary_as_runtime=False,
            selected_runtime_readiness_boundary_treated_checkability_as_continuation=False,
            selected_runtime_readiness_boundary_treated_final_completion_as_runtime=False,
            selected_runtime_readiness_boundary_treated_final_completion_as_continuation=False,
            selected_runtime_readiness_boundary_treated_currentness_surface_as_runtime_permission=False,
            selected_runtime_readiness_boundary_treated_currentness_surface_as_operation_permission=False,
            selected_runtime_readiness_boundary_authorized_future_work=False,
        ),
        "selected_runtime_readiness_boundary_terminal_summary_basis": _reference_basis(
            "post_portable_verification_runtime_readiness_boundary_terminal_summary",
            "spec/POST_PORTABLE_VERIFICATION_RUNTIME_READINESS_BOUNDARY_TERMINAL_SUMMARY_V0.md",
            terminal_summary_states_runtime_readiness_not_created=True,
            terminal_summary_states_runtime_not_created=True,
            terminal_summary_states_continuation_not_authorized=True,
            terminal_summary_selected_runtime_readiness_review=False,
            terminal_summary_requires_separate_bounded_specification=True,
        ),
        "selected_portable_verification_final_completion_basis": _reference_basis(
            "portable_verification_final_completion_terminal_summary",
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_TERMINAL_SUMMARY_V0.md",
        ),
        "selected_post_portable_verification_currentness_basis": _reference_basis(
            "post_portable_verification_currentness_surface",
            "spec/POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_V0.md",
            selected_post_portable_currentness_surface_path="spec/POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_V0.md",
            selected_post_portable_currentness_surface_states_checkability_not_continuation=True,
            selected_post_portable_currentness_surface_authorized_next_work=False,
        ),
        "selected_final_completion_artifact_basis": _reference_basis(
            "portable_verification_final_completion_artifact",
            final_completion_artifact_path,
            EXPECTED_FINAL_COMPLETION_OUTCOME,
            selected_portable_verification_final_completion_result_path=final_completion_artifact_path,
            selected_portable_verification_final_completion_result_outcome=EXPECTED_FINAL_COMPLETION_OUTCOME,
            selected_portable_verification_final_completion_result_version=RESULT_VERSION,
            selected_portable_verification_final_completion_failed_check_count=0,
        ),
        "selected_returned_second_carrier_capture_lineage_basis": _reference_basis(
            "returned_second_carrier_capture_lineage",
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_RETURNED_SECOND_CARRIER_LIVE_CAPTURE_INTAKE_V0.md",
            lineage_only=True,
            runtime_basis=False,
        ),
        "selected_runtime_readiness_boundary_result_path": boundary_artifact_path,
        "selected_runtime_readiness_boundary_result_outcome": EXPECTED_RUNTIME_READINESS_BOUNDARY_OUTCOME,
        "selected_runtime_readiness_boundary_result_version": RESULT_VERSION,
        "selected_runtime_readiness_boundary_failed_check_count": 0,
        "selected_runtime_readiness_boundary_declared_future_runtime_readiness_review_step": True,
        "selected_runtime_readiness_boundary_already_created_runtime_readiness": False,
        "selected_runtime_readiness_boundary_already_created_runtime": False,
        "selected_runtime_readiness_boundary_already_authorized_continuation": False,
        "selected_runtime_readiness_boundary_treated_boundary_as_runtime_readiness": False,
        "selected_runtime_readiness_boundary_treated_boundary_as_runtime": False,
        "selected_runtime_readiness_boundary_treated_checkability_as_continuation": False,
        "selected_runtime_readiness_boundary_treated_final_completion_as_runtime": False,
        "selected_runtime_readiness_boundary_treated_final_completion_as_continuation": False,
        "selected_runtime_readiness_boundary_treated_currentness_surface_as_runtime_permission": False,
        "selected_runtime_readiness_boundary_treated_currentness_surface_as_operation_permission": False,
        "selected_runtime_readiness_boundary_authorized_future_work": False,
        "selected_portable_verification_final_completion_result_path": final_completion_artifact_path,
        "selected_portable_verification_final_completion_result_outcome": EXPECTED_FINAL_COMPLETION_OUTCOME,
        "selected_portable_verification_final_completion_result_version": RESULT_VERSION,
        "selected_portable_verification_final_completion_failed_check_count": 0,
        "selected_post_portable_currentness_surface_path": "spec/POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_V0.md",
        "selected_post_portable_currentness_surface_states_checkability_not_continuation": True,
        "selected_post_portable_currentness_surface_authorized_next_work": False,
        "runtime_readiness_created_before_review": False,
        "runtime_created": False,
        "runtime_boundary_created": False,
        "runtime_step_created": False,
        "continuation_authorized": False,
        "reference_shaped_input_posture": True,
        "predecessor_failure_evidence_preserved": True,
        "predecessor_failure_repaired": False,
        "predecessor_failure_hidden": False,
        "predecessor_failure_claimed_passed": False,
        "additional_basis_context": [],
        "not_recorded_basis": [],
        "block_reason": None,
    }
    for posture_field in POSTURE_FIELDS:
        request[posture_field] = _posture(posture_field)
    request.update(overrides)
    return copy.deepcopy(request)
