"""Resolve portable source-body verification portable-verification-closure boundary.

This resolver is downstream of the recorded cross-carrier evidence line. It may
record one future line-level portable verification closure review step only. It
does not create portable verification closure, final completion, source
transfer, source receipt, reception authorization, source, authority,
currentness, runtime, deployment, public release, operation permission,
continuation, reusable permission, derivative reception, vessel relation,
another reception request, or follow-on work.

The resolver is self-contained, imports no repo-local modules, runs no
subprocesses, performs no network access, mutates no upstream artifact, and
keeps official enum, scope, outcome, block-code, posture, non-claim, section,
and boolean field strings unredacted while containing hostile raw body payloads.
"""

from __future__ import annotations

import copy
import datetime
import json
from pathlib import Path
from typing import Any, Mapping


class PortableSourceBodyVerificationPortableVerificationClosureBoundaryError(Exception):
    """Raised for unreadable paths, malformed JSON, or impossible result shape."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_portable_source_body_verification_portable_verification_closure_boundary"
)
RESULT_TYPE = "portable_source_body_verification_portable_verification_closure_boundary"
DEFAULT_REQUEST_ID = (
    "portable_source_body_verification_portable_verification_closure_boundary_"
    "reference_review_001"
)
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_portable_source_body_verification_"
    "portable_verification_closure_boundary"
)

CORE_QUESTION = (
    "Can the clean cross-carrier-evidence basis be bounded for one future "
    "line-level portable verification closure review step without creating "
    "portable verification closure yet, final completion, source transfer, "
    "source receipt, reception authorization, source, authority, currentness, "
    "runtime, deployment, public release, operation permission, continuation, "
    "reusable permission, derivative reception, vessel relation, another "
    "reception request, or follow-on work?"
)

OUTCOME_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_"
    "REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_BLOCKED"
)
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = (
    "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_PORTABLE_VERIFICATION_CLOSURE_BOUNDARY"
)
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_PORTABLE_VERIFICATION_CLOSURE_BOUNDARY"
)
INTENT_BLOCK = (
    "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_PORTABLE_VERIFICATION_CLOSURE_BOUNDARY"
)
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

EXPECTED_CROSS_CARRIER_EVIDENCE_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_CROSS_CARRIER_EVIDENCE_RECORDED"
)
EXPECTED_CROSS_CARRIER_EVIDENCE_BOUNDARY_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_CROSS_CARRIER_EVIDENCE_BOUNDARY_RECORDED"
)
EXPECTED_SECOND_CARRIER_EXTERNAL_RESULT_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT_RECORDED"
)
EXPECTED_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_RECORDED"
)
EXPECTED_SECOND_CARRIER_VERIFICATION_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_VERIFICATION_RECORDED"
)
EXPECTED_SECOND_CARRIER_SUCCESS_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_SUCCESS_RECORDED"
)
EXPECTED_SECOND_CARRIER_RESULT_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RESULT_RECORDED"
)
EXPECTED_SECOND_CARRIER_OUTPUT_CAPTURE_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_OUTPUT_CAPTURE_RECORDED"
)

SUPPORTED_SCOPE_VALUES = (
    "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_ONLY",
    "ONE_FUTURE_PORTABLE_VERIFICATION_CLOSURE_REVIEW_STEP_ONLY",
    "CROSS_CARRIER_EVIDENCE_BASIS_PRESERVED",
    "CROSS_CARRIER_EVIDENCE_ARTIFACT_BASIS_PRESERVED",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_BASIS_PRESERVED",
    "SECOND_CARRIER_EXTERNAL_RESULT_BASIS_PRESERVED",
    "RETURNED_SECOND_CARRIER_CAPTURE_BASIS_PRESERVED",
    "CAPTURE_INTAKE_BASIS_PRESERVED",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_PRESERVED",
    "PORTABLE_VERIFICATION_CLOSURE_NOT_CREATED",
    "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_NOT_PORTABLE_VERIFICATION_CLOSURE",
    "CROSS_CARRIER_EVIDENCE_NOT_PORTABLE_VERIFICATION_CLOSURE",
    "ZERO_EXIT_CODE_NOT_PORTABLE_VERIFICATION_CLOSURE",
    "STRING_ZERO_NOT_PORTABLE_VERIFICATION_CLOSURE",
    "OK_OUTPUT_NOT_PORTABLE_VERIFICATION_CLOSURE",
    "RAN_7_TESTS_NOT_PORTABLE_VERIFICATION_CLOSURE",
    "RETURNED_CAPTURE_NOT_PORTABLE_VERIFICATION_CLOSURE",
    "FINAL_COMPLETION_NOT_CREATED",
    "PORTABLE_VERIFICATION_CLOSURE_NOT_SOURCE_TRANSFER",
    "PORTABLE_VERIFICATION_CLOSURE_NOT_SOURCE_RECEIPT",
    "PORTABLE_VERIFICATION_CLOSURE_NOT_RECEPTION_AUTHORIZATION",
    "RECEIVING_CARRIER_NOT_AUTHORITY",
    "NO_SOURCE_CREATED",
    "NO_AUTHORITY_CREATED",
    "NO_CURRENTNESS_CREATED",
    "NO_RUNTIME_CREATED",
    "NO_DEPLOYMENT_CREATED",
    "NO_PUBLIC_RELEASE_CREATED",
    "NO_OPERATION_PERMISSION_CREATED",
    "NO_CONTINUATION_AUTHORIZED",
    "NO_REUSABLE_PERMISSION",
    "NO_DERIVATIVE_RECEPTION",
    "NO_VESSEL_RELATION",
    "NO_ANOTHER_RECEPTION_REQUEST",
    "NO_FOLLOW_ON_WORK_AUTHORIZED",
    "NO_PORTABLE_VERIFICATION_CLOSURE_INFERENCE",
    "NO_FINAL_COMPLETION_INFERENCE",
    "NO_SOURCE_INFERENCE",
    "NO_AUTHORITY_INFERENCE",
    "NO_CURRENTNESS_INFERENCE",
    "NO_RUNTIME_INFERENCE",
    "NO_FOLLOW_ON_WORK_INFERENCE",
    "NO_UNBOUNDED_PASS_FAIL_INFERENCE",
    "HIDDEN_REPO_STATE_EXCLUDED",
    "HIDDEN_REPO_STATE_NOT_USED_AS_PORTABLE_VERIFICATION_CLOSURE_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_NOT_PORTABLE_VERIFICATION_CLOSURE_AUTHORITY",
    "SELECTED_BASIS_REFERENCE_SHAPE_PRESERVED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "PREDECESSOR_CROSS_CARRIER_EVIDENCE_FAILURE_PRESERVED",
    "PREDECESSOR_EXTERNAL_RESULT_V1_FAILURE_PRESERVED",
    "FIRST_SUCCESS_BOUNDARY_TEST_FAILURE_PRESERVED",
    "FIRST_RESULT_BOUNDARY_RESOLVER_FAILURE_PRESERVED",
    "AUTHORIZATION_TOKEN_REUSE_BLOCKED",
    "CONSUMED_REQUEST_TOKEN_REMAINS_CLOSED",
    "CONSUMED_REQUEST_NOT_REOPENED",
    "COMMAND_REPORT_LINEAGE_NOT_CURRENT_REPORT_ARTIFACT",
    "COMMAND_REPORT_LINEAGE_NOT_SOURCE",
    "COMMAND_REPORT_LINEAGE_NOT_AUTHORITY",
    "COMMAND_REPORT_LINEAGE_NOT_CURRENTNESS",
    "RETURNED_RESULT_CONTAINMENT_PRESERVED",
)
SUPPORTED_PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_SCOPE = SUPPORTED_SCOPE_VALUES

ALLOWED_TRUE_RECORDED_FIELDS = (
    "portable_verification_closure_boundary_recorded",
    "one_future_portable_verification_closure_review_step_declared",
    "cross_carrier_evidence_basis_preserved",
    "cross_carrier_evidence_artifact_basis_preserved",
    "cross_carrier_evidence_boundary_basis_preserved",
    "second_carrier_external_result_basis_preserved",
    "returned_second_carrier_capture_basis_preserved",
    "capture_intake_basis_preserved",
    "second_carrier_output_capture_basis_preserved",
    "portable_verification_closure_not_created",
    "portable_verification_closure_boundary_not_portable_verification_closure",
    "cross_carrier_evidence_not_portable_verification_closure",
    "zero_exit_code_not_portable_verification_closure",
    "string_zero_not_portable_verification_closure",
    "ok_output_not_portable_verification_closure",
    "ran_7_tests_not_portable_verification_closure",
    "returned_capture_not_portable_verification_closure",
    "final_completion_not_created",
    "portable_verification_closure_not_source_transfer",
    "portable_verification_closure_not_source_receipt",
    "portable_verification_closure_not_reception_authorization",
    "receiving_carrier_not_authority",
    "source_not_created",
    "authority_not_created",
    "currentness_not_created",
    "runtime_not_created",
    "continuation_not_authorized",
    "reusable_permission_not_created",
    "follow_on_work_not_authorized",
    "hidden_repo_state_excluded",
    "hidden_repo_state_not_used_as_portable_verification_closure_authority",
    "repo_local_availability_not_portable_verification_closure_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "official_enum_scope_strings_not_redacted",
    "hostile_raw_body_content_contained",
    "predecessor_cross_carrier_evidence_failure_preserved",
    "predecessor_external_result_v1_failure_preserved",
    "first_success_boundary_test_failure_preserved",
    "first_result_boundary_resolver_failure_preserved",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
)

REQUIRED_FALSE_NON_CLAIMS = (
    "portable_verification_closure_created",
    "final_completion_claimed",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "portable_verification_closure_boundary_treated_as_portable_verification_closure",
    "portable_verification_closure_boundary_treated_as_final_completion",
    "portable_verification_closure_boundary_treated_as_source_transfer",
    "portable_verification_closure_boundary_treated_as_source_receipt",
    "portable_verification_closure_boundary_treated_as_reception_authorization",
    "portable_verification_closure_boundary_treated_as_source",
    "portable_verification_closure_boundary_treated_as_authority",
    "portable_verification_closure_boundary_treated_as_currentness",
    "portable_verification_closure_boundary_treated_as_runtime",
    "portable_verification_closure_boundary_treated_as_continuation",
    "portable_verification_closure_boundary_treated_as_reusable_permission",
    "portable_verification_closure_boundary_treated_as_follow_on_work",
    "cross_carrier_evidence_treated_as_portable_verification_closure",
    "zero_exit_code_treated_as_portable_verification_closure",
    "string_zero_treated_as_portable_verification_closure",
    "string_zero_representation_turned_into_doctrine",
    "ok_output_treated_as_portable_verification_closure",
    "ran_7_tests_treated_as_portable_verification_closure",
    "returned_capture_treated_as_portable_verification_closure",
    "receiving_carrier_treated_as_authority",
    "artifact_existence_treated_as_portable_verification_closure_authority",
    "artifact_path_treated_as_currentness",
    "repo_local_availability_treated_as_portable_verification_closure_authority",
    "hidden_repo_state_used_as_portable_verification_closure_content",
    "hidden_repo_state_used_as_portable_verification_closure_authority",
    "source_created",
    "authority_created",
    "currentness_created",
    "runtime_hosting_created",
    "deployment_created",
    "public_release_created",
    "operation_permission_created",
    "continuation_authorized",
    "reusable_permission_created",
    "derivative_reception_authorized",
    "vessel_relation_authorized",
    "another_reception_request_authorized",
    "follow_on_work_authorized",
    "raw_full_prior_artifact_body_returned",
    "prior_artifacts_mutated",
    "returned_capture_material_mutated",
    "consumed_request_reopened",
    "authorization_token_reused",
    "predecessor_cross_carrier_evidence_repaired",
    "predecessor_cross_carrier_evidence_hidden",
    "predecessor_cross_carrier_evidence_claimed_passed",
    "predecessor_external_result_v1_repaired",
    "predecessor_external_result_v1_hidden",
    "predecessor_external_result_v1_claimed_passed",
    "v1_packet_emission_repaired",
    "v1_packet_emission_hidden",
    "v1_packet_emission_claimed_passed",
    "first_success_boundary_test_repaired",
    "first_success_boundary_test_hidden",
    "first_success_boundary_test_claimed_passed",
    "first_result_boundary_resolver_repaired",
    "first_result_boundary_resolver_hidden",
    "first_result_boundary_resolver_claimed_passed",
)

BLOCK_CODES = (
    "DECLARED_PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_REQUEST_UNREADABLE",
    "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_QUESTION_UNDECLARED",
    "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_INTENT_UNSUPPORTED",
    "CROSS_CARRIER_EVIDENCE_BASIS_MISSING",
    "CROSS_CARRIER_EVIDENCE_NOT_RECORDED",
    "CROSS_CARRIER_EVIDENCE_FAILED_CHECKS_PRESENT",
    "CROSS_CARRIER_EVIDENCE_VERSION_NOT_0_1_0",
    "CROSS_CARRIER_EVIDENCE_DID_NOT_RECORD_BOUNDED_EVIDENCE",
    "CROSS_CARRIER_EVIDENCE_ALREADY_CREATED_PORTABLE_VERIFICATION_CLOSURE",
    "CROSS_CARRIER_EVIDENCE_ALREADY_CREATED_FINAL_COMPLETION",
    "CROSS_CARRIER_EVIDENCE_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
    "CROSS_CARRIER_EVIDENCE_TREATED_AS_SOURCE_TRANSFER",
    "CROSS_CARRIER_EVIDENCE_TREATED_AS_SOURCE_RECEIPT",
    "CROSS_CARRIER_EVIDENCE_TREATED_AS_RECEPTION_AUTHORIZATION",
    "CROSS_CARRIER_EVIDENCE_TREATED_AS_SOURCE",
    "CROSS_CARRIER_EVIDENCE_TREATED_AS_AUTHORITY",
    "CROSS_CARRIER_EVIDENCE_TREATED_AS_CURRENTNESS",
    "CROSS_CARRIER_EVIDENCE_TREATED_AS_FINAL_COMPLETION",
    "CROSS_CARRIER_EVIDENCE_TREATED_AS_RUNTIME",
    "CROSS_CARRIER_EVIDENCE_TREATED_AS_FOLLOW_ON_WORK",
    "CROSS_CARRIER_EVIDENCE_TREATED_ZERO_EXIT_CODE_AS_PORTABLE_VERIFICATION_CLOSURE",
    "CROSS_CARRIER_EVIDENCE_TREATED_STRING_ZERO_AS_PORTABLE_VERIFICATION_CLOSURE",
    "CROSS_CARRIER_EVIDENCE_TREATED_STRING_ZERO_AS_DOCTRINE",
    "CROSS_CARRIER_EVIDENCE_TREATED_OK_AS_PORTABLE_VERIFICATION_CLOSURE",
    "CROSS_CARRIER_EVIDENCE_TREATED_RAN_7_TESTS_AS_PORTABLE_VERIFICATION_CLOSURE",
    "CROSS_CARRIER_EVIDENCE_TREATED_RETURNED_CAPTURE_AS_PORTABLE_VERIFICATION_CLOSURE",
    "CROSS_CARRIER_EVIDENCE_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
    "PREDECESSOR_CROSS_CARRIER_EVIDENCE_FAILURE_MISSING_OR_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
    "PREDECESSOR_EXTERNAL_RESULT_V1_FAILURE_MISSING_OR_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_BASIS_MISSING",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_NOT_RECORDED",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_EXTERNAL_RESULT_BASIS_MISSING",
    "SECOND_CARRIER_EXTERNAL_RESULT_NOT_RECORDED",
    "SECOND_CARRIER_EXTERNAL_RESULT_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_EXTERNAL_RESULT_ALREADY_CREATED_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_EXTERNAL_RESULT_AS_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_STRING_ZERO_AS_DOCTRINE",
    "SECOND_CARRIER_VERIFICATION_BASIS_MISSING",
    "SECOND_CARRIER_VERIFICATION_NOT_RECORDED",
    "SECOND_CARRIER_VERIFICATION_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_SUCCESS_BASIS_MISSING",
    "SECOND_CARRIER_SUCCESS_NOT_RECORDED",
    "SECOND_CARRIER_SUCCESS_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_RESULT_BASIS_MISSING",
    "SECOND_CARRIER_RESULT_NOT_RECORDED",
    "SECOND_CARRIER_RESULT_FAILED_CHECKS_PRESENT",
    "RETURNED_CAPTURE_INTAKE_BASIS_MISSING",
    "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
    "RETURNED_CAPTURE_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
    "ZERO_EXIT_CODE_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
    "STRING_ZERO_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
    "STRING_ZERO_REPRESENTATION_TURNED_INTO_DOCTRINE",
    "OK_OUTPUT_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
    "RAN_7_TESTS_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
    "PLACEHOLDER_CARRIER_FIELDS_REPAIRED",
    "RETURNED_CAPTURE_MATERIAL_MISSING",
    "RETURNED_ZIP_PATH_MISSING",
    "RETURNED_HASH_PATH_MISSING",
    "RETURNED_EXTRACTED_DIRECTORY_MISSING",
    "RETURNED_COMBINED_TERMINAL_LOG_MISSING",
    "RETURNED_EXIT_CODE_MISSING",
    "RETURNED_COMMAND_TEXT_MISSING",
    "RETURNED_TIMESTAMPS_MISSING",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_MISSING",
    "SECOND_CARRIER_OUTPUT_CAPTURE_NOT_RECORDED",
    "SECOND_CARRIER_OUTPUT_CAPTURE_FAILED_CHECKS_PRESENT",
    "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
    "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_FINAL_COMPLETION",
    "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_SOURCE",
    "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_AUTHORITY",
    "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_CURRENTNESS",
    "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_RUNTIME",
    "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_CONTINUATION",
    "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION",
    "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
    "PORTABLE_VERIFICATION_CLOSURE_CREATED",
    "FINAL_COMPLETION_CLAIMED",
    "SOURCE_TRANSFER_OCCURRED",
    "SOURCE_RECEIPT_OCCURRED",
    "RECEPTION_AUTHORIZATION_CREATED",
    "SOURCE_CREATED",
    "AUTHORITY_CREATED",
    "CURRENTNESS_CREATED",
    "RUNTIME_HOSTING_CREATED",
    "DEPLOYMENT_CREATED",
    "PUBLIC_RELEASE_CREATED",
    "OPERATION_PERMISSION_CREATED",
    "CONTINUATION_AUTHORIZED",
    "REUSABLE_PERMISSION_CREATED",
    "DERIVATIVE_RECEPTION_AUTHORIZED",
    "VESSEL_RELATION_AUTHORIZED",
    "ANOTHER_RECEPTION_REQUEST_AUTHORIZED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "RECEIVING_CARRIER_TREATED_AS_AUTHORITY",
    "ARTIFACT_EXISTENCE_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_PORTABLE_VERIFICATION_CLOSURE_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_PORTABLE_VERIFICATION_CLOSURE_AUTHORITY",
    "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "FIRST_SUCCESS_BOUNDARY_TEST_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    "FIRST_RESULT_BOUNDARY_RESOLVER_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENT_REPORT_ARTIFACT",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_SOURCE",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_AUTHORITY",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENTNESS",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_PORTABLE_VERIFICATION_CLOSURE_BOUNDARY",
    "ARTIFACTS_MUTATED",
    "RETURNED_CAPTURE_MATERIAL_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_SCOPE",
)

SELECTED_BASIS_FIELDS = (
    "selected_cross_carrier_evidence_basis",
    "selected_cross_carrier_evidence_terminal_summary_basis",
    "selected_cross_carrier_evidence_boundary_basis",
    "selected_second_carrier_external_result_basis",
    "selected_second_carrier_external_result_terminal_summary_basis",
    "selected_second_carrier_external_result_boundary_basis",
    "selected_second_carrier_verification_basis",
    "selected_second_carrier_success_basis",
    "selected_second_carrier_result_basis",
    "selected_returned_second_carrier_live_capture_intake_basis",
    "selected_returned_capture_material_basis",
    "selected_second_carrier_output_capture_basis",
    "selected_packet_transfer_basis",
    "selected_packet_emission_basis",
    "selected_command_success_basis",
    "selected_command_result_v2_basis",
    "selected_output_capture_v2_basis",
    "selected_command_output_report_artifact_basis",
    "selected_command_execution_basis",
    "selected_command_report_lineage_basis",
    "selected_predecessor_failure_basis",
    "selected_evidence_manifest_basis",
    "selected_artifact_containment_basis",
    "selected_portable_verification_basis",
)
SELECTED_BASIS_KEYS = SELECTED_BASIS_FIELDS

POSTURE_SECTIONS = (
    "portable_verification_closure_boundary_only_posture",
    "one_future_portable_verification_closure_review_step_posture",
    "cross_carrier_evidence_basis_preserved_posture",
    "cross_carrier_evidence_artifact_basis_preserved_posture",
    "cross_carrier_evidence_boundary_basis_preserved_posture",
    "second_carrier_external_result_basis_preserved_posture",
    "returned_second_carrier_capture_basis_preserved_posture",
    "capture_intake_basis_preserved_posture",
    "second_carrier_output_capture_basis_preserved_posture",
    "portable_verification_closure_not_created_posture",
    "portable_verification_closure_boundary_not_portable_verification_closure_posture",
    "cross_carrier_evidence_not_portable_verification_closure_posture",
    "zero_exit_code_not_portable_verification_closure_posture",
    "string_zero_not_portable_verification_closure_posture",
    "ok_output_not_portable_verification_closure_posture",
    "ran_7_tests_not_portable_verification_closure_posture",
    "returned_capture_not_portable_verification_closure_posture",
    "final_completion_not_created_posture",
    "portable_verification_closure_not_source_transfer_posture",
    "portable_verification_closure_not_source_receipt_posture",
    "portable_verification_closure_not_reception_authorization_posture",
    "receiving_carrier_not_authority_posture",
    "source_not_created_posture",
    "authority_not_created_posture",
    "currentness_not_created_posture",
    "runtime_not_created_posture",
    "continuation_not_authorized_posture",
    "reusable_permission_not_created_posture",
    "follow_on_work_not_authorized_posture",
    "hidden_repo_state_excluded_posture",
    "repo_local_availability_not_portable_verification_closure_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_cross_carrier_evidence_failure_preserved_posture",
    "predecessor_external_result_v1_failure_preserved_posture",
    "first_success_boundary_test_failure_preserved_posture",
    "first_result_boundary_resolver_failure_preserved_posture",
)
POSTURE_KEYS = POSTURE_SECTIONS

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
    "raw_portable_verification_closure_boundary_body",
    "capture_body",
    "cross_carrier_evidence_body",
    "portable_verification_closure_body",
    "final_completion_body",
    "source_body",
    "authority_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
}
HOSTILE_SENTINELS = (
    "RAW_PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)
REDACTED_RAW_VALUE = "[bounded-redacted-raw-or-hidden-state]"

OFFICIAL_STRINGS = (
    set(SUPPORTED_SCOPE_VALUES)
    | set(OUTCOME_FAMILY)
    | set(BLOCK_CODES)
    | set(ALLOWED_TRUE_RECORDED_FIELDS)
    | set(REQUIRED_FALSE_NON_CLAIMS)
    | set(SELECTED_BASIS_FIELDS)
    | set(POSTURE_SECTIONS)
)

NON_MEANING_KEYS = (
    "portable_verification_closure_exists",
    "final_completion_exists",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_exists",
    "source_exists",
    "authority_exists",
    "currentness_exists",
    "runtime_exists",
    "deployment_exists",
    "public_release_exists",
    "operation_permission_exists",
    "continuation_authorized",
    "reusable_permission_exists",
    "derivative_reception_authorized",
    "vessel_relation_authorized",
    "another_reception_request_authorized",
    "follow_on_work_authorized",
    "portable_verification_closure_boundary_became_portable_verification_closure",
    "portable_verification_closure_boundary_became_final_completion",
    "portable_verification_closure_boundary_became_source_authority_currentness_runtime",
    "cross_carrier_evidence_became_portable_verification_closure",
    "zero_exit_code_became_portable_verification_closure",
    "string_zero_became_portable_verification_closure",
    "string_zero_became_doctrine",
    "ok_became_portable_verification_closure",
    "ran_7_tests_became_portable_verification_closure",
    "returned_capture_became_portable_verification_closure",
    "macbook_pro_became_authority",
    "macbook_air_became_source",
    "artifact_existence_became_portable_verification_closure_authority",
    "artifact_path_became_currentness",
    "repo_local_availability_became_portable_verification_closure_authority",
    "hidden_repo_state_became_portable_verification_closure_authority",
    "predecessor_cross_carrier_evidence_resolver_repaired_hidden_erased_or_claimed_passed",
    "predecessor_external_result_v1_resolver_test_repaired_hidden_erased_or_claimed_passed",
    "first_success_boundary_test_repaired_hidden_erased_or_claimed_passed",
    "first_result_boundary_resolver_repaired_hidden_erased_or_claimed_passed",
    "v1_packet_emission_boundary_resolver_repaired_hidden_erased_or_claimed_passed",
)

WHAT_REMAINS_OPEN = (
    "portable verification closure boundary test",
    "portable verification closure boundary live artifact",
    "portable verification closure boundary terminal summary, if needed",
    "portable verification closure spec/resolver/test/live artifact, if admitted",
    "line-level portable verification closure review",
    "final completion review",
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
    "optional future numeric-zero declared-input resolver review, if separately selected",
)


def _utc_now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()


def _json_safe(value: Any) -> Any:
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, Mapping):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [_json_safe(item) for item in value]
    return value


def _is_sensitive_key(key: str) -> bool:
    lowered = key.lower()
    return lowered in SENSITIVE_CONTENT_KEYS or lowered.endswith("_body")


def _sanitize(value: Any, key: str | None = None) -> Any:
    if key is not None and _is_sensitive_key(key):
        return REDACTED_RAW_VALUE
    if isinstance(value, Mapping):
        return {str(item_key): _sanitize(item, str(item_key)) for item_key, item in value.items()}
    if isinstance(value, list):
        return [_sanitize(item) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item) for item in value]
    if isinstance(value, set):
        return [_sanitize(item) for item in sorted(value, key=str)]
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, str):
        if value in OFFICIAL_STRINGS:
            return value
        if any(sentinel in value for sentinel in HOSTILE_SENTINELS):
            return REDACTED_RAW_VALUE
        return value
    return value


def _truthy(value: Any) -> bool:
    if value is True:
        return True
    if value is False or value is None:
        return False
    if isinstance(value, str):
        return value.strip().lower() in {"true", "yes", "y", "1", "on"}
    if isinstance(value, (int, float)):
        return value != 0
    return bool(value)


def _as_int(value: Any, default: int = 0) -> int:
    if isinstance(value, bool):
        return int(value)
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _find_key(value: Any, keys: set[str]) -> Any:
    if isinstance(value, Mapping):
        for key, nested in value.items():
            if str(key) in keys:
                return nested
        for nested in value.values():
            found = _find_key(nested, keys)
            if found is not None:
                return found
    elif isinstance(value, (list, tuple)):
        for item in value:
            found = _find_key(item, keys)
            if found is not None:
                return found
    return None


def _request_value(request: Mapping[str, Any], keys: set[str], default: Any = None) -> Any:
    for key in keys:
        if key in request:
            return request[key]
    found = _find_key(request, keys)
    return default if found is None else found


def _request_truthy(request: Mapping[str, Any], keys: set[str]) -> bool:
    return _truthy(_request_value(request, keys, False))


def _basis_declared(request: Mapping[str, Any], field: str) -> bool:
    if field not in request:
        return False
    value = request.get(field)
    if value is None or value is False:
        return False
    if isinstance(value, (str, list, tuple, set, dict)) and len(value) == 0:
        return False
    return True


def _posture_declared(request: Mapping[str, Any], field: str) -> bool:
    if field not in request:
        return False
    value = request.get(field)
    if isinstance(value, Mapping) and "declared" in value:
        return _truthy(value.get("declared"))
    return _basis_declared(request, field)


def _scope_values(raw_scope: Any) -> list[str]:
    if raw_scope is None:
        return list(SUPPORTED_SCOPE_VALUES)
    if isinstance(raw_scope, str):
        return [raw_scope]
    if isinstance(raw_scope, Mapping):
        if "scope_values" in raw_scope:
            return _scope_values(raw_scope.get("scope_values"))
        if "declared_scope_values" in raw_scope:
            return _scope_values(raw_scope.get("declared_scope_values"))
        return [str(key) for key, value in raw_scope.items() if _truthy(value)]
    if isinstance(raw_scope, (list, tuple, set)):
        return [str(value) for value in raw_scope]
    return [str(raw_scope)]


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
        "expected_posture": _sanitize(_json_safe(expected_posture)),
        "actual_posture": _sanitize(_json_safe(actual_posture)),
    }
    if passed:
        record["block_code"] = None
        record["failure_code"] = None
    else:
        record["block_code"] = code
        record["failure_code"] = code
    checks.append(record)


def _first_failure(checks: list[dict[str, Any]]) -> dict[str, Any] | None:
    for check in checks:
        if not check.get("passed", False):
            code = check.get("block_code") or check.get("failure_code")
            return {
                "block_code": code,
                "block_reason": check.get("check_name"),
                "expected_posture": check.get("expected_posture"),
                "actual_posture": check.get("actual_posture"),
            }
    return None


def _non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _statement(recorded: bool) -> dict[str, bool]:
    return {key: bool(recorded) for key in ALLOWED_TRUE_RECORDED_FIELDS}


def _posture(name: str, recorded: bool) -> dict[str, Any]:
    return {
        "posture_name": name,
        "declared": bool(recorded),
        "bounded_to": "portable_verification_closure_boundary",
        "creates_portable_verification_closure": False,
        "creates_final_completion": False,
        "creates_source_transfer": False,
        "creates_source_receipt": False,
        "creates_reception_authorization": False,
        "creates_source_authority_currentness_runtime_or_follow_on": False,
    }


def _shortcut_prefixes_for_field(field: str) -> tuple[str, ...]:
    if field == "selected_cross_carrier_evidence_basis":
        return ("selected_cross_carrier_evidence_",)
    if field == "selected_returned_capture_material_basis":
        return ("selected_returned_capture_",)
    if field == "selected_returned_second_carrier_live_capture_intake_basis":
        return (
            "selected_returned_capture_",
            "selected_returned_second_carrier_live_capture_intake",
        )
    return (field.replace("_basis", ""),)


def _selected_basis(
    request: Mapping[str, Any],
    field: str,
    shortcut_prefixes: tuple[str, ...] = (),
) -> dict[str, Any]:
    shortcuts: dict[str, Any] = {}
    for key, value in request.items():
        if any(str(key).startswith(prefix) for prefix in shortcut_prefixes):
            shortcuts[str(key)] = value
    selected = {
        "basis_field": field,
        "basis_declared": _basis_declared(request, field),
        "selected_basis_reference_shape_preserved": True,
        "basis": _sanitize(_json_safe(copy.deepcopy(request.get(field)))),
        "selected_shortcuts": _sanitize(_json_safe(shortcuts)),
        "raw_full_prior_artifact_body_returned": False,
        "hidden_repo_state_used_as_authority": False,
        "repo_local_availability_used_as_authority": False,
        "basis_only": True,
        "creates_portable_verification_closure": False,
        "creates_final_completion": False,
        "creates_source_authority_currentness_runtime_or_follow_on": False,
    }
    if field == "selected_predecessor_failure_basis":
        selected.update(
            {
                "predecessor_cross_carrier_evidence_failure_preserved": True,
                "predecessor_cross_carrier_evidence_not_repaired": True,
                "predecessor_cross_carrier_evidence_not_hidden": True,
                "predecessor_cross_carrier_evidence_not_claimed_passed": True,
                "predecessor_external_result_v1_failure_preserved": True,
                "predecessor_external_result_v1_not_repaired": True,
                "predecessor_external_result_v1_not_hidden": True,
                "predecessor_external_result_v1_not_claimed_passed": True,
                "first_success_boundary_test_failure_preserved": True,
                "first_result_boundary_resolver_failure_preserved": True,
                "v1_packet_emission_boundary_failure_preserved": True,
            }
        )
    return selected


def _missing_or_flipped_non_claim(request: Mapping[str, Any]) -> str | None:
    declared = request.get("declared_non_claims")
    if not isinstance(declared, Mapping):
        return "declared_non_claims"
    for key in REQUIRED_FALSE_NON_CLAIMS:
        if key not in declared or declared.get(key) is not False:
            return key
    return None


OVERREACH_FLAG_CODES: tuple[tuple[set[str], str], ...] = (
    (
        {"portable_verification_closure_boundary_treated_as_portable_verification_closure"},
        "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
    ),
    (
        {"portable_verification_closure_boundary_treated_as_final_completion"},
        "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_FINAL_COMPLETION",
    ),
    (
        {"portable_verification_closure_boundary_treated_as_source_transfer"},
        "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    ),
    (
        {"portable_verification_closure_boundary_treated_as_source_receipt"},
        "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    ),
    (
        {"portable_verification_closure_boundary_treated_as_reception_authorization"},
        "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    ),
    (
        {"portable_verification_closure_boundary_treated_as_source"},
        "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_SOURCE",
    ),
    (
        {"portable_verification_closure_boundary_treated_as_authority"},
        "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_AUTHORITY",
    ),
    (
        {"portable_verification_closure_boundary_treated_as_currentness"},
        "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_CURRENTNESS",
    ),
    (
        {"portable_verification_closure_boundary_treated_as_runtime"},
        "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_RUNTIME",
    ),
    (
        {"portable_verification_closure_boundary_treated_as_continuation"},
        "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_CONTINUATION",
    ),
    (
        {"portable_verification_closure_boundary_treated_as_reusable_permission"},
        "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION",
    ),
    (
        {"portable_verification_closure_boundary_treated_as_follow_on_work"},
        "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
    ),
    ({"portable_verification_closure_created"}, "PORTABLE_VERIFICATION_CLOSURE_CREATED"),
    ({"final_completion_claimed", "final_completion_created"}, "FINAL_COMPLETION_CLAIMED"),
    ({"source_transfer_occurred"}, "SOURCE_TRANSFER_OCCURRED"),
    ({"source_receipt_occurred"}, "SOURCE_RECEIPT_OCCURRED"),
    ({"reception_authorization_created"}, "RECEPTION_AUTHORIZATION_CREATED"),
    ({"source_created"}, "SOURCE_CREATED"),
    ({"authority_created"}, "AUTHORITY_CREATED"),
    ({"currentness_created"}, "CURRENTNESS_CREATED"),
    ({"runtime_hosting_created", "runtime_created"}, "RUNTIME_HOSTING_CREATED"),
    ({"deployment_created"}, "DEPLOYMENT_CREATED"),
    ({"public_release_created"}, "PUBLIC_RELEASE_CREATED"),
    ({"operation_permission_created"}, "OPERATION_PERMISSION_CREATED"),
    ({"continuation_authorized"}, "CONTINUATION_AUTHORIZED"),
    ({"reusable_permission_created"}, "REUSABLE_PERMISSION_CREATED"),
    ({"derivative_reception_authorized"}, "DERIVATIVE_RECEPTION_AUTHORIZED"),
    ({"vessel_relation_authorized"}, "VESSEL_RELATION_AUTHORIZED"),
    ({"another_reception_request_authorized"}, "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"),
    ({"follow_on_work_authorized"}, "FOLLOW_ON_WORK_AUTHORIZED"),
    (
        {
            "cross_carrier_evidence_treated_as_portable_verification_closure",
            "selected_cross_carrier_evidence_treated_as_portable_verification_closure",
        },
        "CROSS_CARRIER_EVIDENCE_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
    ),
    (
        {
            "cross_carrier_evidence_treated_as_source_transfer",
            "selected_cross_carrier_evidence_treated_as_source_transfer",
        },
        "CROSS_CARRIER_EVIDENCE_TREATED_AS_SOURCE_TRANSFER",
    ),
    (
        {
            "cross_carrier_evidence_treated_as_source_receipt",
            "selected_cross_carrier_evidence_treated_as_source_receipt",
        },
        "CROSS_CARRIER_EVIDENCE_TREATED_AS_SOURCE_RECEIPT",
    ),
    (
        {
            "cross_carrier_evidence_treated_as_reception_authorization",
            "selected_cross_carrier_evidence_treated_as_reception_authorization",
        },
        "CROSS_CARRIER_EVIDENCE_TREATED_AS_RECEPTION_AUTHORIZATION",
    ),
    (
        {
            "cross_carrier_evidence_treated_as_source",
            "selected_cross_carrier_evidence_treated_as_source",
        },
        "CROSS_CARRIER_EVIDENCE_TREATED_AS_SOURCE",
    ),
    (
        {
            "cross_carrier_evidence_treated_as_authority",
            "selected_cross_carrier_evidence_treated_as_authority",
        },
        "CROSS_CARRIER_EVIDENCE_TREATED_AS_AUTHORITY",
    ),
    (
        {
            "cross_carrier_evidence_treated_as_currentness",
            "selected_cross_carrier_evidence_treated_as_currentness",
        },
        "CROSS_CARRIER_EVIDENCE_TREATED_AS_CURRENTNESS",
    ),
    (
        {
            "cross_carrier_evidence_treated_as_final_completion",
            "selected_cross_carrier_evidence_treated_as_final_completion",
        },
        "CROSS_CARRIER_EVIDENCE_TREATED_AS_FINAL_COMPLETION",
    ),
    (
        {
            "cross_carrier_evidence_treated_as_runtime",
            "selected_cross_carrier_evidence_treated_as_runtime",
        },
        "CROSS_CARRIER_EVIDENCE_TREATED_AS_RUNTIME",
    ),
    (
        {
            "cross_carrier_evidence_treated_as_follow_on_work",
            "selected_cross_carrier_evidence_treated_as_follow_on_work",
        },
        "CROSS_CARRIER_EVIDENCE_TREATED_AS_FOLLOW_ON_WORK",
    ),
    (
        {
            "zero_exit_code_treated_as_portable_verification_closure",
            "selected_cross_carrier_evidence_treated_zero_exit_code_as_portable_verification_closure",
        },
        "ZERO_EXIT_CODE_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
    ),
    (
        {
            "string_zero_treated_as_portable_verification_closure",
            "selected_cross_carrier_evidence_treated_string_zero_as_portable_verification_closure",
        },
        "STRING_ZERO_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
    ),
    (
        {
            "string_zero_representation_turned_into_doctrine",
            "selected_cross_carrier_evidence_treated_string_zero_as_doctrine",
        },
        "STRING_ZERO_REPRESENTATION_TURNED_INTO_DOCTRINE",
    ),
    (
        {
            "ok_output_treated_as_portable_verification_closure",
            "selected_cross_carrier_evidence_treated_ok_as_portable_verification_closure",
        },
        "OK_OUTPUT_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
    ),
    (
        {
            "ran_7_tests_treated_as_portable_verification_closure",
            "selected_cross_carrier_evidence_treated_ran_7_tests_as_portable_verification_closure",
        },
        "RAN_7_TESTS_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
    ),
    (
        {
            "returned_capture_treated_as_portable_verification_closure",
            "selected_cross_carrier_evidence_treated_returned_capture_as_portable_verification_closure",
        },
        "RETURNED_CAPTURE_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
    ),
    ({"receiving_carrier_treated_as_authority"}, "RECEIVING_CARRIER_TREATED_AS_AUTHORITY"),
    (
        {"artifact_existence_treated_as_portable_verification_closure_authority"},
        "ARTIFACT_EXISTENCE_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE_AUTHORITY",
    ),
    ({"artifact_path_treated_as_currentness"}, "ARTIFACT_PATH_TREATED_AS_CURRENTNESS"),
    (
        {"repo_local_availability_treated_as_portable_verification_closure_authority"},
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE_AUTHORITY",
    ),
    (
        {"hidden_repo_state_used_as_portable_verification_closure_content"},
        "HIDDEN_REPO_STATE_USED_AS_PORTABLE_VERIFICATION_CLOSURE_CONTENT",
    ),
    (
        {"hidden_repo_state_used_as_portable_verification_closure_authority"},
        "HIDDEN_REPO_STATE_USED_AS_PORTABLE_VERIFICATION_CLOSURE_AUTHORITY",
    ),
    ({"selected_basis_not_reference_shaped"}, "SELECTED_BASIS_NOT_REFERENCE_SHAPED"),
    ({"raw_full_prior_artifact_body_returned"}, "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED"),
    (
        {
            "predecessor_cross_carrier_evidence_repaired",
            "predecessor_cross_carrier_evidence_hidden",
            "predecessor_cross_carrier_evidence_claimed_passed",
        },
        "PREDECESSOR_CROSS_CARRIER_EVIDENCE_FAILURE_MISSING_OR_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
    ),
    (
        {
            "predecessor_external_result_v1_repaired",
            "predecessor_external_result_v1_hidden",
            "predecessor_external_result_v1_claimed_passed",
        },
        "PREDECESSOR_EXTERNAL_RESULT_V1_FAILURE_MISSING_OR_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
    ),
    (
        {"v1_packet_emission_repaired", "v1_packet_emission_hidden", "v1_packet_emission_claimed_passed"},
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    ),
    (
        {
            "first_success_boundary_test_repaired",
            "first_success_boundary_test_hidden",
            "first_success_boundary_test_claimed_passed",
        },
        "FIRST_SUCCESS_BOUNDARY_TEST_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    ),
    (
        {
            "first_result_boundary_resolver_repaired",
            "first_result_boundary_resolver_hidden",
            "first_result_boundary_resolver_claimed_passed",
        },
        "FIRST_RESULT_BOUNDARY_RESOLVER_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    ),
    (
        {
            "command_report_lineage_treated_as_current_report_artifact",
            "selected_command_report_lineage_treated_as_current_report_artifact",
        },
        "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENT_REPORT_ARTIFACT",
    ),
    (
        {"command_report_lineage_treated_as_source", "selected_command_report_lineage_treated_as_source"},
        "COMMAND_REPORT_LINEAGE_TREATED_AS_SOURCE",
    ),
    (
        {"command_report_lineage_treated_as_authority", "selected_command_report_lineage_treated_as_authority"},
        "COMMAND_REPORT_LINEAGE_TREATED_AS_AUTHORITY",
    ),
    (
        {"command_report_lineage_treated_as_currentness", "selected_command_report_lineage_treated_as_currentness"},
        "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENTNESS",
    ),
    ({"consumed_request_reopened"}, "CONSUMED_REQUEST_REOPENED"),
    ({"authorization_token_reused"}, "AUTHORIZATION_TOKEN_REUSED"),
    (
        {"full_prior_artifact_body_emitted_outside_bounded_portable_verification_closure_boundary"},
        "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_PORTABLE_VERIFICATION_CLOSURE_BOUNDARY",
    ),
    ({"prior_artifacts_mutated", "artifacts_mutated"}, "ARTIFACTS_MUTATED"),
    ({"returned_capture_material_mutated"}, "RETURNED_CAPTURE_MATERIAL_MUTATED"),
)


def _evaluate_request(request: Mapping[str, Any]) -> tuple[list[dict[str, Any]], dict[str, Any] | None]:
    checks: list[dict[str, Any]] = []

    question = request.get("portable_verification_closure_boundary_question")
    _check(
        checks,
        "portable verification closure boundary question declared",
        isinstance(question, str) and bool(question.strip()),
        "declared bounded portable verification closure boundary question",
        question,
        "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_QUESTION_UNDECLARED",
    )

    intent = request.get("portable_verification_closure_boundary_intent")
    _check(
        checks,
        "portable verification closure boundary intent supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_INTENT_UNSUPPORTED",
    )
    if intent == INTENT_BLOCK:
        _check(
            checks,
            "portable verification closure boundary explicit block intent absent",
            False,
            "not explicitly blocked",
            intent,
            "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_INTENT_UNSUPPORTED",
        )

    scope = _scope_values(request.get("portable_verification_closure_boundary_scope"))
    unsupported_scope = [value for value in scope if value not in SUPPORTED_SCOPE_VALUES]
    _check(
        checks,
        "portable verification closure boundary scope supported",
        not unsupported_scope,
        "only supported portable verification closure boundary scope values",
        unsupported_scope,
        "UNSUPPORTED_PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_SCOPE",
    )

    missing_non_claim = _missing_or_flipped_non_claim(request)
    _check(
        checks,
        "required non-claims false",
        missing_non_claim is None,
        "all required non-claims present and false",
        missing_non_claim,
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )

    _check(
        checks,
        "selected basis remains reference-shaped",
        _request_truthy(request, {"reference_shaped_input_posture"}),
        True,
        request.get("reference_shaped_input_posture"),
        "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    )

    _check(
        checks,
        "cross-carrier evidence basis declared",
        _basis_declared(request, "selected_cross_carrier_evidence_basis"),
        "selected cross-carrier evidence basis declared",
        request.get("selected_cross_carrier_evidence_basis"),
        "CROSS_CARRIER_EVIDENCE_BASIS_MISSING",
    )
    _check(
        checks,
        "cross-carrier evidence terminal summary basis declared",
        _basis_declared(request, "selected_cross_carrier_evidence_terminal_summary_basis"),
        "selected cross-carrier evidence terminal summary basis declared",
        request.get("selected_cross_carrier_evidence_terminal_summary_basis"),
        "CROSS_CARRIER_EVIDENCE_BASIS_MISSING",
    )

    cross_carrier_evidence_outcome = _request_value(
        request,
        {"selected_cross_carrier_evidence_result_outcome", "cross_carrier_evidence_result_outcome"},
    )
    _check(
        checks,
        "cross-carrier evidence outcome recorded",
        cross_carrier_evidence_outcome == EXPECTED_CROSS_CARRIER_EVIDENCE_OUTCOME,
        EXPECTED_CROSS_CARRIER_EVIDENCE_OUTCOME,
        cross_carrier_evidence_outcome,
        "CROSS_CARRIER_EVIDENCE_NOT_RECORDED",
    )

    cross_carrier_evidence_version = _request_value(
        request,
        {"selected_cross_carrier_evidence_result_version", "cross_carrier_evidence_result_version"},
    )
    _check(
        checks,
        "cross-carrier evidence version 0.1.0",
        cross_carrier_evidence_version == RESULT_VERSION,
        RESULT_VERSION,
        cross_carrier_evidence_version,
        "CROSS_CARRIER_EVIDENCE_VERSION_NOT_0_1_0",
    )

    cross_carrier_evidence_failed = _as_int(
        _request_value(request, {"selected_cross_carrier_evidence_failed_check_count"}, 0)
    )
    _check(
        checks,
        "cross-carrier evidence failed checks zero",
        cross_carrier_evidence_failed == 0,
        0,
        cross_carrier_evidence_failed,
        "CROSS_CARRIER_EVIDENCE_FAILED_CHECKS_PRESENT",
    )

    cross_carrier_evidence_required_true_checks = (
        (
            "cross-carrier evidence recorded bounded evidence",
            {"selected_cross_carrier_evidence_bounded_evidence_recorded"},
            "CROSS_CARRIER_EVIDENCE_DID_NOT_RECORD_BOUNDED_EVIDENCE",
        ),
        (
            "cross-carrier evidence kept evidence not portable verification closure",
            {"selected_cross_carrier_evidence_not_portable_verification_closure"},
            "CROSS_CARRIER_EVIDENCE_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
        ),
        (
            "cross-carrier evidence kept zero exit code not portable verification closure",
            {"selected_cross_carrier_evidence_zero_exit_code_not_portable_verification_closure"},
            "CROSS_CARRIER_EVIDENCE_TREATED_ZERO_EXIT_CODE_AS_PORTABLE_VERIFICATION_CLOSURE",
        ),
        (
            "cross-carrier evidence kept string zero not portable verification closure",
            {"selected_cross_carrier_evidence_string_zero_not_portable_verification_closure"},
            "CROSS_CARRIER_EVIDENCE_TREATED_STRING_ZERO_AS_PORTABLE_VERIFICATION_CLOSURE",
        ),
        (
            "cross-carrier evidence kept OK not portable verification closure",
            {"selected_cross_carrier_evidence_ok_not_portable_verification_closure"},
            "CROSS_CARRIER_EVIDENCE_TREATED_OK_AS_PORTABLE_VERIFICATION_CLOSURE",
        ),
        (
            "cross-carrier evidence kept Ran 7 tests not portable verification closure",
            {"selected_cross_carrier_evidence_ran_7_tests_not_portable_verification_closure"},
            "CROSS_CARRIER_EVIDENCE_TREATED_RAN_7_TESTS_AS_PORTABLE_VERIFICATION_CLOSURE",
        ),
        (
            "cross-carrier evidence kept returned capture not portable verification closure",
            {"selected_cross_carrier_evidence_returned_capture_not_portable_verification_closure"},
            "CROSS_CARRIER_EVIDENCE_TREATED_RETURNED_CAPTURE_AS_PORTABLE_VERIFICATION_CLOSURE",
        ),
        (
            "predecessor cross-carrier evidence failure preserved",
            {
                "selected_cross_carrier_evidence_predecessor_failure_preserved",
                "predecessor_cross_carrier_evidence_failure_preserved",
            },
            "PREDECESSOR_CROSS_CARRIER_EVIDENCE_FAILURE_MISSING_OR_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
        ),
        (
            "predecessor external-result v1 failure preserved",
            {"predecessor_external_result_v1_failure_preserved"},
            "PREDECESSOR_EXTERNAL_RESULT_V1_FAILURE_MISSING_OR_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
        ),
    )
    for check_name, keys, code in cross_carrier_evidence_required_true_checks:
        actual = _request_truthy(request, keys)
        _check(checks, check_name, actual, True, actual, code)

    cross_carrier_evidence_required_false_checks = (
        (
            "cross-carrier evidence did not already create portable verification closure",
            {"selected_cross_carrier_evidence_already_created_portable_verification_closure"},
            "CROSS_CARRIER_EVIDENCE_ALREADY_CREATED_PORTABLE_VERIFICATION_CLOSURE",
        ),
        (
            "cross-carrier evidence did not already create final completion",
            {"selected_cross_carrier_evidence_already_created_final_completion"},
            "CROSS_CARRIER_EVIDENCE_ALREADY_CREATED_FINAL_COMPLETION",
        ),
        (
            "cross-carrier evidence did not treat evidence as portable verification closure",
            {"selected_cross_carrier_evidence_treated_as_portable_verification_closure"},
            "CROSS_CARRIER_EVIDENCE_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
        ),
        (
            "cross-carrier evidence did not treat string zero as doctrine",
            {"selected_cross_carrier_evidence_treated_string_zero_as_doctrine"},
            "CROSS_CARRIER_EVIDENCE_TREATED_STRING_ZERO_AS_DOCTRINE",
        ),
        (
            "cross-carrier evidence did not redact official enum scope strings",
            {"selected_cross_carrier_evidence_official_enum_scope_strings_redacted"},
            "CROSS_CARRIER_EVIDENCE_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
        ),
    )
    for check_name, keys, code in cross_carrier_evidence_required_false_checks:
        actual = _request_truthy(request, keys)
        _check(checks, check_name, not actual, False, actual, code)

    for check_name, keys, code in (
        (
            "cross-carrier evidence did not treat evidence as source transfer",
            {"selected_cross_carrier_evidence_treated_as_source_transfer"},
            "CROSS_CARRIER_EVIDENCE_TREATED_AS_SOURCE_TRANSFER",
        ),
        (
            "cross-carrier evidence did not treat evidence as source receipt",
            {"selected_cross_carrier_evidence_treated_as_source_receipt"},
            "CROSS_CARRIER_EVIDENCE_TREATED_AS_SOURCE_RECEIPT",
        ),
        (
            "cross-carrier evidence did not treat evidence as reception authorization",
            {"selected_cross_carrier_evidence_treated_as_reception_authorization"},
            "CROSS_CARRIER_EVIDENCE_TREATED_AS_RECEPTION_AUTHORIZATION",
        ),
        (
            "cross-carrier evidence did not treat evidence as source",
            {"selected_cross_carrier_evidence_treated_as_source"},
            "CROSS_CARRIER_EVIDENCE_TREATED_AS_SOURCE",
        ),
        (
            "cross-carrier evidence did not treat evidence as authority",
            {"selected_cross_carrier_evidence_treated_as_authority"},
            "CROSS_CARRIER_EVIDENCE_TREATED_AS_AUTHORITY",
        ),
        (
            "cross-carrier evidence did not treat evidence as currentness",
            {"selected_cross_carrier_evidence_treated_as_currentness"},
            "CROSS_CARRIER_EVIDENCE_TREATED_AS_CURRENTNESS",
        ),
        (
            "cross-carrier evidence did not treat evidence as final completion",
            {"selected_cross_carrier_evidence_treated_as_final_completion"},
            "CROSS_CARRIER_EVIDENCE_TREATED_AS_FINAL_COMPLETION",
        ),
        (
            "cross-carrier evidence did not treat evidence as runtime",
            {"selected_cross_carrier_evidence_treated_as_runtime"},
            "CROSS_CARRIER_EVIDENCE_TREATED_AS_RUNTIME",
        ),
        (
            "cross-carrier evidence did not treat evidence as follow-on work",
            {"selected_cross_carrier_evidence_treated_as_follow_on_work"},
            "CROSS_CARRIER_EVIDENCE_TREATED_AS_FOLLOW_ON_WORK",
        ),
    ):
        actual = _request_truthy(request, keys)
        _check(checks, check_name, not actual, False, actual, code)

    boundary_basis_checks = (
        (
            "selected_cross_carrier_evidence_boundary_basis",
            "cross-carrier evidence boundary basis declared",
            "CROSS_CARRIER_EVIDENCE_BOUNDARY_BASIS_MISSING",
        ),
        (
            "selected_second_carrier_external_result_basis",
            "second-carrier external-result basis declared",
            "SECOND_CARRIER_EXTERNAL_RESULT_BASIS_MISSING",
        ),
        (
            "selected_second_carrier_external_result_terminal_summary_basis",
            "second-carrier external-result terminal summary basis declared",
            "SECOND_CARRIER_EXTERNAL_RESULT_BASIS_MISSING",
        ),
        (
            "selected_second_carrier_external_result_boundary_basis",
            "second-carrier external-result boundary basis declared",
            "SECOND_CARRIER_EXTERNAL_RESULT_BASIS_MISSING",
        ),
        (
            "selected_second_carrier_verification_basis",
            "second-carrier verification basis declared",
            "SECOND_CARRIER_VERIFICATION_BASIS_MISSING",
        ),
        (
            "selected_second_carrier_success_basis",
            "second-carrier success basis declared",
            "SECOND_CARRIER_SUCCESS_BASIS_MISSING",
        ),
        (
            "selected_second_carrier_result_basis",
            "second-carrier result basis declared",
            "SECOND_CARRIER_RESULT_BASIS_MISSING",
        ),
        (
            "selected_returned_second_carrier_live_capture_intake_basis",
            "returned capture intake basis declared",
            "RETURNED_CAPTURE_INTAKE_BASIS_MISSING",
        ),
        (
            "selected_returned_capture_material_basis",
            "returned capture material basis declared",
            "RETURNED_CAPTURE_MATERIAL_MISSING",
        ),
        (
            "selected_second_carrier_output_capture_basis",
            "second-carrier output capture basis declared",
            "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_MISSING",
        ),
    )
    for field, check_name, code in boundary_basis_checks:
        _check(checks, check_name, _basis_declared(request, field), "declared", request.get(field), code)

    outcome_checks = (
        (
            "cross-carrier evidence boundary outcome recorded",
            {"selected_cross_carrier_evidence_boundary_result_outcome"},
            EXPECTED_CROSS_CARRIER_EVIDENCE_BOUNDARY_OUTCOME,
            "CROSS_CARRIER_EVIDENCE_BOUNDARY_NOT_RECORDED",
        ),
        (
            "second-carrier external-result outcome recorded",
            {"selected_second_carrier_external_result_result_outcome"},
            EXPECTED_SECOND_CARRIER_EXTERNAL_RESULT_OUTCOME,
            "SECOND_CARRIER_EXTERNAL_RESULT_NOT_RECORDED",
        ),
        (
            "second-carrier verification outcome recorded",
            {"selected_second_carrier_verification_result_outcome"},
            EXPECTED_SECOND_CARRIER_VERIFICATION_OUTCOME,
            "SECOND_CARRIER_VERIFICATION_NOT_RECORDED",
        ),
        (
            "second-carrier success outcome recorded",
            {"selected_second_carrier_success_result_outcome"},
            EXPECTED_SECOND_CARRIER_SUCCESS_OUTCOME,
            "SECOND_CARRIER_SUCCESS_NOT_RECORDED",
        ),
        (
            "second-carrier result outcome recorded",
            {"selected_second_carrier_result_result_outcome"},
            EXPECTED_SECOND_CARRIER_RESULT_OUTCOME,
            "SECOND_CARRIER_RESULT_NOT_RECORDED",
        ),
        (
            "second-carrier output capture outcome recorded",
            {"selected_second_carrier_output_capture_result_outcome"},
            EXPECTED_SECOND_CARRIER_OUTPUT_CAPTURE_OUTCOME,
            "SECOND_CARRIER_OUTPUT_CAPTURE_NOT_RECORDED",
        ),
    )
    for check_name, keys, expected, code in outcome_checks:
        actual = _request_value(request, keys)
        _check(checks, check_name, actual == expected, expected, actual, code)

    failed_count_checks = (
        (
            "cross-carrier evidence boundary failed checks zero",
            {"selected_cross_carrier_evidence_boundary_failed_check_count"},
            "CROSS_CARRIER_EVIDENCE_BOUNDARY_FAILED_CHECKS_PRESENT",
        ),
        (
            "second-carrier external-result failed checks zero",
            {"selected_second_carrier_external_result_failed_check_count"},
            "SECOND_CARRIER_EXTERNAL_RESULT_FAILED_CHECKS_PRESENT",
        ),
        (
            "second-carrier verification failed checks zero",
            {"selected_second_carrier_verification_failed_check_count"},
            "SECOND_CARRIER_VERIFICATION_FAILED_CHECKS_PRESENT",
        ),
        (
            "second-carrier success failed checks zero",
            {"selected_second_carrier_success_failed_check_count"},
            "SECOND_CARRIER_SUCCESS_FAILED_CHECKS_PRESENT",
        ),
        (
            "second-carrier result failed checks zero",
            {"selected_second_carrier_result_failed_check_count"},
            "SECOND_CARRIER_RESULT_FAILED_CHECKS_PRESENT",
        ),
        (
            "second-carrier output capture failed checks zero",
            {"selected_second_carrier_output_capture_failed_check_count"},
            "SECOND_CARRIER_OUTPUT_CAPTURE_FAILED_CHECKS_PRESENT",
        ),
    )
    for check_name, keys, code in failed_count_checks:
        actual = _as_int(_request_value(request, keys, 0))
        _check(checks, check_name, actual == 0, 0, actual, code)

    external_result_guard_checks = (
        (
            "second-carrier external result did not already create portable verification closure",
            {"selected_second_carrier_external_result_already_created_portable_verification_closure"},
            "SECOND_CARRIER_EXTERNAL_RESULT_ALREADY_CREATED_PORTABLE_VERIFICATION_CLOSURE",
        ),
        (
            "second-carrier external result did not treat external result as portable verification closure",
            {"selected_second_carrier_external_result_treated_external_result_as_portable_verification_closure"},
            "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_EXTERNAL_RESULT_AS_PORTABLE_VERIFICATION_CLOSURE",
        ),
        (
            "second-carrier external result did not treat string zero as doctrine",
            {"selected_second_carrier_external_result_treated_string_zero_as_doctrine"},
            "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_STRING_ZERO_AS_DOCTRINE",
        ),
    )
    for check_name, keys, code in external_result_guard_checks:
        actual = _request_truthy(request, keys)
        _check(checks, check_name, not actual, False, actual, code)

    capture_checks = (
        (
            "returned capture intake preserved",
            {"selected_returned_capture_intake_preserved"},
            True,
            "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
        ),
        (
            "returned capture intake says capture-only",
            {"selected_returned_capture_intake_capture_only"},
            True,
            "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
        ),
        (
            "MacBook Pro to MacBook Air return preserved",
            {"selected_returned_capture_from_macbook_pro_to_macbook_air"},
            True,
            "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
        ),
        (
            "raw placeholder carrier fields preserved and unrepaired",
            {"selected_returned_capture_placeholder_fields_unrepaired"},
            True,
            "PLACEHOLDER_CARRIER_FIELDS_REPAIRED",
        ),
    )
    for check_name, keys, expected, code in capture_checks:
        actual = _request_truthy(request, keys)
        _check(checks, check_name, actual == expected, expected, actual, code)

    capture_path_checks = (
        ("selected_returned_capture_zip_path", "returned zip path declared", "RETURNED_ZIP_PATH_MISSING"),
        ("selected_returned_capture_hash_path", "returned hash path declared", "RETURNED_HASH_PATH_MISSING"),
        (
            "selected_returned_capture_extracted_directory_path",
            "returned extracted directory declared",
            "RETURNED_EXTRACTED_DIRECTORY_MISSING",
        ),
        (
            "selected_returned_capture_combined_terminal_log_path",
            "returned combined terminal log declared",
            "RETURNED_COMBINED_TERMINAL_LOG_MISSING",
        ),
        ("selected_returned_capture_exit_code", "returned exit code declared", "RETURNED_EXIT_CODE_MISSING"),
        ("selected_returned_capture_command_text", "returned command text declared", "RETURNED_COMMAND_TEXT_MISSING"),
        ("selected_returned_capture_started_at", "returned started timestamp declared", "RETURNED_TIMESTAMPS_MISSING"),
        ("selected_returned_capture_completed_at", "returned completed timestamp declared", "RETURNED_TIMESTAMPS_MISSING"),
    )
    for field, check_name, code in capture_path_checks:
        _check(checks, check_name, _basis_declared(request, field), "declared", request.get(field), code)

    declared_zero = request.get("selected_returned_capture_declared_exit_code")
    _check(
        checks,
        'declared string "0" representation not turned into doctrine',
        str(declared_zero) == "0",
        'string "0" declared-input representation only',
        declared_zero,
        "STRING_ZERO_REPRESENTATION_TURNED_INTO_DOCTRINE",
    )

    ancillary_basis_fields = (
        "selected_packet_transfer_basis",
        "selected_packet_emission_basis",
        "selected_command_success_basis",
        "selected_command_result_v2_basis",
        "selected_output_capture_v2_basis",
        "selected_command_output_report_artifact_basis",
        "selected_command_execution_basis",
        "selected_command_report_lineage_basis",
        "selected_predecessor_failure_basis",
        "selected_evidence_manifest_basis",
        "selected_artifact_containment_basis",
        "selected_portable_verification_basis",
    )
    for field in ancillary_basis_fields:
        _check(
            checks,
            f"{field} declared",
            _basis_declared(request, field),
            "declared",
            request.get(field),
            "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_MISSING",
        )

    for field in POSTURE_SECTIONS:
        _check(
            checks,
            f"{field} declared",
            _posture_declared(request, field),
            "declared",
            request.get(field),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )

    for keys, code in OVERREACH_FLAG_CODES:
        actual = _request_truthy(request, keys)
        _check(checks, f"{code} not present", not actual, False, actual, code)

    return checks, _first_failure(checks)


def _result_id(request: Mapping[str, Any]) -> str:
    value = request.get("portable_verification_closure_boundary_request_id")
    if isinstance(value, str) and value.strip():
        return value.strip()
    return DEFAULT_REQUEST_ID


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: list[dict[str, Any]],
    block: dict[str, Any] | None,
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    request_id = _result_id(request)
    statement = _statement(recorded)
    non_claims = _non_claims()
    scope_values = _scope_values(request.get("portable_verification_closure_boundary_scope"))

    result: dict[str, Any] = {
        "portable_source_body_verification_portable_verification_closure_boundary_metadata": {
            "portable_source_body_verification_portable_verification_closure_boundary_result_id": request_id,
            "portable_source_body_verification_portable_verification_closure_boundary_result_type": RESULT_TYPE,
            "portable_source_body_verification_portable_verification_closure_boundary_result_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_portable_verification_closure_boundary_question": {
            "request_id": request_id,
            "question": request.get("portable_verification_closure_boundary_question"),
            "intent": request.get("portable_verification_closure_boundary_intent"),
            "core_question": CORE_QUESTION,
        },
    }

    for field in SELECTED_BASIS_FIELDS:
        result[field] = _selected_basis(request, field, _shortcut_prefixes_for_field(field))

    for field in POSTURE_SECTIONS:
        result[field] = _posture(field, recorded)

    result["portable_verification_closure_boundary_scope"] = {
        "scope_values": list(scope_values),
        "declared_scope_values": list(scope_values),
        "supported_scope_values": list(SUPPORTED_SCOPE_VALUES),
        "unsupported_scope_values": [
            value for value in scope_values if value not in SUPPORTED_SCOPE_VALUES
        ],
        "official_enum_scope_strings_not_redacted": True,
    }
    result["portable_verification_closure_boundary_checks"] = checks
    result["portable_verification_closure_boundary_statement"] = statement
    result["portable_verification_closure_boundary_non_meaning"] = {
        key: False for key in NON_MEANING_KEYS
    }
    result["additional_basis_required"] = {
        "required": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "missing_or_unclear_basis": _sanitize(_json_safe(request.get("additional_basis_context", []))),
        "missing_basis_scheduled": False,
        "missing_basis_authorized": False,
        "missing_basis_executed": False,
        "creates_portable_verification_closure": False,
        "creates_final_completion": False,
    }
    result["not_recorded_basis"] = {
        "not_recorded": outcome == OUTCOME_NOT_RECORDED,
        "basis": _sanitize(_json_safe(request.get("not_recorded_basis", []))),
        "no_mutation": True,
        "no_follow_on_authorization": True,
    }
    result["what_remains_open"] = {
        "items": list(WHAT_REMAINS_OPEN),
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }
    result["non_claims"] = non_claims
    result["outcome"] = outcome
    result["block"] = block
    result["portable_source_body_verification_portable_verification_closure_boundary_summary"] = (
        build_portable_source_body_verification_portable_verification_closure_boundary_summary(result)
    )
    return result


def _malformed_result(reason: str, code: str) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    _check(checks, reason, False, "mapping request", reason, code)
    block = _first_failure(checks)
    return _build_result({}, OUTCOME_BLOCKED, checks, block)


def resolve_portable_source_body_verification_portable_verification_closure_boundary(
    declared_portable_verification_closure_boundary_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one bounded portable-verification-closure-boundary posture."""

    if declared_portable_verification_closure_boundary_request is None:
        return _malformed_result(
            "declared portable verification closure boundary request missing",
            "DECLARED_PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_REQUEST_MALFORMED",
        )
    if not isinstance(declared_portable_verification_closure_boundary_request, Mapping):
        return _malformed_result(
            "declared portable verification closure boundary request malformed",
            "DECLARED_PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_REQUEST_MALFORMED",
        )

    request = copy.deepcopy(dict(declared_portable_verification_closure_boundary_request))
    checks, block = _evaluate_request(request)
    requested_outcome = request.get("requested_portable_verification_closure_boundary_outcome")

    if block is not None:
        outcome = OUTCOME_BLOCKED
    elif request.get("portable_verification_closure_boundary_intent") == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_RECORDED
    elif requested_outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
    elif requested_outcome == OUTCOME_NOT_RECORDED:
        outcome = OUTCOME_NOT_RECORDED
    else:
        outcome = OUTCOME_RECORDED

    return _build_result(request, outcome, checks, block)


def resolve_portable_source_body_verification_portable_verification_closure_boundary_from_path(
    declared_portable_verification_closure_boundary_request_path: Path | str,
) -> dict:
    """Load a JSON object request from path and resolve it."""

    path = Path(declared_portable_verification_closure_boundary_request_path)
    try:
        raw_text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise PortableSourceBodyVerificationPortableVerificationClosureBoundaryError(
            f"declared portable verification closure boundary request unreadable: {path}"
        ) from exc
    try:
        loaded = json.loads(raw_text)
    except json.JSONDecodeError as exc:
        raise PortableSourceBodyVerificationPortableVerificationClosureBoundaryError(
            f"declared portable verification closure boundary request malformed JSON: {path}"
        ) from exc
    if not isinstance(loaded, Mapping):
        return _malformed_result(
            "declared portable verification closure boundary request path did not contain JSON object",
            "DECLARED_PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_REQUEST_MALFORMED",
        )
    return resolve_portable_source_body_verification_portable_verification_closure_boundary(loaded)


def _selected_summary_value(result: Mapping[str, Any], section: str, shortcut: str) -> Any:
    selected = result.get(section, {})
    if not isinstance(selected, Mapping):
        return None
    shortcuts = selected.get("selected_shortcuts", {})
    if isinstance(shortcuts, Mapping) and shortcut in shortcuts:
        return shortcuts.get(shortcut)
    basis = selected.get("basis", {})
    if isinstance(basis, Mapping):
        return _find_key(basis, {shortcut})
    return None


def build_portable_source_body_verification_portable_verification_closure_boundary_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a compact JSON-safe summary from a closure-boundary result."""

    metadata = result.get(
        "portable_source_body_verification_portable_verification_closure_boundary_metadata",
        {},
    )
    declared = result.get("declared_portable_verification_closure_boundary_question", {})
    checks = result.get("portable_verification_closure_boundary_checks", [])
    statement = result.get("portable_verification_closure_boundary_statement", {})
    non_claims = result.get("non_claims", {})
    block = result.get("block")

    failed_count = sum(1 for check in checks if not check.get("passed", False))
    passed_count = sum(1 for check in checks if check.get("passed", False))

    summary = {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") if isinstance(block, Mapping) else None,
        "block_reason": block.get("block_reason") if isinstance(block, Mapping) else None,
        "request_id": metadata.get(
            "portable_source_body_verification_portable_verification_closure_boundary_result_id"
        ),
        "question": declared.get("question"),
        "intent": declared.get("intent"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": metadata.get(
            "portable_source_body_verification_portable_verification_closure_boundary_result_version",
            RESULT_VERSION,
        ),
        "resolver_module": metadata.get("resolver_module", RESOLVER_MODULE),
        "selected_cross_carrier_evidence_outcome": _selected_summary_value(
            result,
            "selected_cross_carrier_evidence_basis",
            "selected_cross_carrier_evidence_result_outcome",
        ),
        "selected_cross_carrier_evidence_version": _selected_summary_value(
            result,
            "selected_cross_carrier_evidence_basis",
            "selected_cross_carrier_evidence_result_version",
        ),
        "selected_cross_carrier_evidence_failed_check_count": _selected_summary_value(
            result,
            "selected_cross_carrier_evidence_basis",
            "selected_cross_carrier_evidence_failed_check_count",
        ),
        "selected_returned_capture_intake_path": _selected_summary_value(
            result,
            "selected_returned_second_carrier_live_capture_intake_basis",
            "selected_returned_capture_intake_path",
        ),
        "selected_returned_capture_zip_path": _selected_summary_value(
            result,
            "selected_returned_capture_material_basis",
            "selected_returned_capture_zip_path",
        ),
        "selected_returned_capture_hash_path": _selected_summary_value(
            result,
            "selected_returned_capture_material_basis",
            "selected_returned_capture_hash_path",
        ),
        "selected_returned_capture_extracted_directory_path": _selected_summary_value(
            result,
            "selected_returned_capture_material_basis",
            "selected_returned_capture_extracted_directory_path",
        ),
        "selected_returned_capture_exit_code": _selected_summary_value(
            result,
            "selected_returned_capture_material_basis",
            "selected_returned_capture_exit_code",
        ),
        "selected_returned_capture_declared_exit_code": _selected_summary_value(
            result,
            "selected_returned_capture_material_basis",
            "selected_returned_capture_declared_exit_code",
        ),
        "selected_returned_capture_ok_line": _selected_summary_value(
            result,
            "selected_returned_capture_material_basis",
            "selected_returned_capture_ok_line",
        ),
        "no_portable_closure": non_claims.get("portable_verification_closure_created") is False,
        "no_final_completion": non_claims.get("final_completion_claimed") is False,
        "no_source_authority_currentness_runtime": (
            non_claims.get("source_created") is False
            and non_claims.get("authority_created") is False
            and non_claims.get("currentness_created") is False
            and non_claims.get("runtime_hosting_created") is False
        ),
        "no_deployment_public_release_follow_on": (
            non_claims.get("deployment_created") is False
            and non_claims.get("public_release_created") is False
            and non_claims.get("follow_on_work_authorized") is False
        ),
        "predecessor_cross_carrier_evidence_failure_preserved": statement.get(
            "predecessor_cross_carrier_evidence_failure_preserved",
            False,
        ),
        "predecessor_external_result_v1_failure_preserved": statement.get(
            "predecessor_external_result_v1_failure_preserved",
            False,
        ),
        "first_success_boundary_test_preserved_as_failed_predecessor": statement.get(
            "first_success_boundary_test_failure_preserved",
            False,
        ),
        "v1_packet_emission_predecessor_failure_preserved": (
            non_claims.get("v1_packet_emission_repaired") is False
            and non_claims.get("v1_packet_emission_hidden") is False
            and non_claims.get("v1_packet_emission_claimed_passed") is False
        ),
        "first_result_boundary_resolver_preserved_as_failed_predecessor": statement.get(
            "first_result_boundary_resolver_failure_preserved",
            False,
        ),
    }
    for key in ALLOWED_TRUE_RECORDED_FIELDS:
        summary[key] = statement.get(key, False)
    for key in REQUIRED_FALSE_NON_CLAIMS:
        summary[key] = non_claims.get(key)
    return _sanitize(_json_safe(summary))


def write_portable_source_body_verification_portable_verification_closure_boundary_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a bounded JSON result without overwriting an existing file."""

    metadata = result.get(
        "portable_source_body_verification_portable_verification_closure_boundary_metadata",
        {},
    )
    request_id = DEFAULT_REQUEST_ID
    if isinstance(metadata, Mapping):
        candidate = metadata.get(
            "portable_source_body_verification_portable_verification_closure_boundary_result_id"
        )
        if isinstance(candidate, str) and candidate.strip():
            request_id = candidate.strip()

    if output_path is None:
        base_path = (
            OUTPUT_ROOT
            / f"{request_id}__portable_source_body_verification_portable_verification_closure_boundary_result.json"
        )
    else:
        base_path = Path(output_path)

    path = base_path
    if path.exists():
        stem = path.stem
        suffix = path.suffix
        parent = path.parent
        counter = 1
        while path.exists():
            path = parent / f"{stem}_{counter:03d}{suffix}"
            counter += 1

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(_sanitize(_json_safe(dict(result))), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return path


def build_declared_portable_source_body_verification_portable_verification_closure_boundary_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Build a valid declared request for one bounded closure-boundary posture."""

    request: dict[str, Any] = {
        "portable_verification_closure_boundary_request_id": DEFAULT_REQUEST_ID,
        "portable_verification_closure_boundary_question": CORE_QUESTION,
        "portable_verification_closure_boundary_intent": INTENT_RECORD,
        "portable_verification_closure_boundary_scope": list(SUPPORTED_SCOPE_VALUES),
        "declared_non_claims": _non_claims(),
        "reference_shaped_input_posture": True,
        "requested_portable_verification_closure_boundary_outcome": OUTCOME_RECORDED,
        "selected_cross_carrier_evidence_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_"
            "cross_carrier_evidence/"
            "portable_source_body_verification_cross_carrier_evidence_reference_review_001__"
            "portable_source_body_verification_cross_carrier_evidence_result.json"
        ),
        "selected_cross_carrier_evidence_result_outcome": EXPECTED_CROSS_CARRIER_EVIDENCE_OUTCOME,
        "selected_cross_carrier_evidence_result_version": RESULT_VERSION,
        "selected_cross_carrier_evidence_failed_check_count": 0,
        "selected_cross_carrier_evidence_bounded_evidence_recorded": True,
        "selected_cross_carrier_evidence_not_portable_verification_closure": True,
        "selected_cross_carrier_evidence_already_created_portable_verification_closure": False,
        "selected_cross_carrier_evidence_already_created_final_completion": False,
        "selected_cross_carrier_evidence_treated_as_portable_verification_closure": False,
        "selected_cross_carrier_evidence_treated_as_source_transfer": False,
        "selected_cross_carrier_evidence_treated_as_source_receipt": False,
        "selected_cross_carrier_evidence_treated_as_reception_authorization": False,
        "selected_cross_carrier_evidence_treated_as_source": False,
        "selected_cross_carrier_evidence_treated_as_authority": False,
        "selected_cross_carrier_evidence_treated_as_currentness": False,
        "selected_cross_carrier_evidence_treated_as_final_completion": False,
        "selected_cross_carrier_evidence_treated_as_runtime": False,
        "selected_cross_carrier_evidence_treated_as_follow_on_work": False,
        "selected_cross_carrier_evidence_zero_exit_code_not_portable_verification_closure": True,
        "selected_cross_carrier_evidence_string_zero_not_portable_verification_closure": True,
        "selected_cross_carrier_evidence_ok_not_portable_verification_closure": True,
        "selected_cross_carrier_evidence_ran_7_tests_not_portable_verification_closure": True,
        "selected_cross_carrier_evidence_returned_capture_not_portable_verification_closure": True,
        "selected_cross_carrier_evidence_treated_string_zero_as_doctrine": False,
        "selected_cross_carrier_evidence_official_enum_scope_strings_redacted": False,
        "selected_cross_carrier_evidence_predecessor_failure_preserved": True,
        "selected_cross_carrier_evidence_boundary_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_"
            "cross_carrier_evidence_boundary/"
            "portable_source_body_verification_cross_carrier_evidence_boundary_reference_review_001__"
            "portable_source_body_verification_cross_carrier_evidence_boundary_result.json"
        ),
        "selected_cross_carrier_evidence_boundary_result_outcome": (
            EXPECTED_CROSS_CARRIER_EVIDENCE_BOUNDARY_OUTCOME
        ),
        "selected_cross_carrier_evidence_boundary_failed_check_count": 0,
        "selected_second_carrier_external_result_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_"
            "second_carrier_external_result/"
            "portable_source_body_verification_second_carrier_external_result_reference_review_001__"
            "portable_source_body_verification_second_carrier_external_result_result.json"
        ),
        "selected_second_carrier_external_result_result_outcome": (
            EXPECTED_SECOND_CARRIER_EXTERNAL_RESULT_OUTCOME
        ),
        "selected_second_carrier_external_result_failed_check_count": 0,
        "selected_second_carrier_external_result_already_created_portable_verification_closure": False,
        "selected_second_carrier_external_result_treated_external_result_as_portable_verification_closure": False,
        "selected_second_carrier_external_result_treated_string_zero_as_doctrine": False,
        "selected_second_carrier_external_result_boundary_result_outcome": (
            EXPECTED_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_OUTCOME
        ),
        "selected_second_carrier_verification_result_outcome": (
            EXPECTED_SECOND_CARRIER_VERIFICATION_OUTCOME
        ),
        "selected_second_carrier_verification_failed_check_count": 0,
        "selected_second_carrier_success_result_outcome": EXPECTED_SECOND_CARRIER_SUCCESS_OUTCOME,
        "selected_second_carrier_success_failed_check_count": 0,
        "selected_second_carrier_result_result_outcome": EXPECTED_SECOND_CARRIER_RESULT_OUTCOME,
        "selected_second_carrier_result_failed_check_count": 0,
        "selected_returned_capture_intake_path": (
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_RETURNED_SECOND_CARRIER_LIVE_CAPTURE_INTAKE_V0.md"
        ),
        "selected_returned_capture_intake_preserved": True,
        "selected_returned_capture_intake_capture_only": True,
        "selected_returned_capture_from_macbook_pro_to_macbook_air": True,
        "selected_returned_capture_zip_path": (
            "artifacts/actual_second_carrier_live_capture/"
            "portable_source_body_verification_actual_second_carrier_capture_001/"
            "original_zip/iammai_second_carrier_capture_001.zip"
        ),
        "selected_returned_capture_hash_path": (
            "artifacts/actual_second_carrier_live_capture/"
            "portable_source_body_verification_actual_second_carrier_capture_001/"
            "hashes/iammai_second_carrier_capture_001.sha256"
        ),
        "selected_returned_capture_extracted_directory_path": (
            "artifacts/actual_second_carrier_live_capture/"
            "portable_source_body_verification_actual_second_carrier_capture_001/"
            "extracted/iammai_second_carrier_capture_001"
        ),
        "selected_returned_capture_combined_terminal_log_path": (
            "artifacts/actual_second_carrier_live_capture/"
            "portable_source_body_verification_actual_second_carrier_capture_001/"
            "extracted/iammai_second_carrier_capture_001/combined_terminal_log.txt"
        ),
        "selected_returned_capture_stdout_path": (
            "artifacts/actual_second_carrier_live_capture/"
            "portable_source_body_verification_actual_second_carrier_capture_001/"
            "extracted/iammai_second_carrier_capture_001/stdout.txt"
        ),
        "selected_returned_capture_stderr_path": (
            "artifacts/actual_second_carrier_live_capture/"
            "portable_source_body_verification_actual_second_carrier_capture_001/"
            "extracted/iammai_second_carrier_capture_001/stderr.txt"
        ),
        "selected_returned_capture_command_text": (
            "python3 -m unittest "
            "tests/test_resolve_portable_source_body_verification_second_carrier_output_capture.py"
        ),
        "selected_returned_capture_working_directory": "/Users/markomarkota/Desktop/IAMMAI-SYSTEM",
        "selected_returned_capture_started_at": "2026-05-09T11:34:26Z",
        "selected_returned_capture_completed_at": "2026-05-09T11:34:27Z",
        "selected_returned_capture_exit_code": 0,
        "selected_returned_capture_declared_exit_code": "0",
        "selected_returned_capture_ran_7_tests_line": "Ran 7 tests in 0.451s",
        "selected_returned_capture_ok_line": "OK",
        "selected_returned_capture_raw_placeholder_carrier_label": "",
        "selected_returned_capture_raw_placeholder_carrier_type": "",
        "selected_returned_capture_placeholder_fields_unrepaired": True,
        "selected_second_carrier_output_capture_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_"
            "second_carrier_output_capture/"
            "portable_source_body_verification_second_carrier_output_capture_result.json"
        ),
        "selected_second_carrier_output_capture_result_outcome": (
            EXPECTED_SECOND_CARRIER_OUTPUT_CAPTURE_OUTCOME
        ),
        "selected_second_carrier_output_capture_failed_check_count": 0,
        "predecessor_cross_carrier_evidence_failure_preserved": True,
        "predecessor_external_result_v1_failure_preserved": True,
    }

    for field in SELECTED_BASIS_FIELDS:
        request[field] = {
            "basis_id": f"{field}_reference",
            "basis_type": "reference_shape",
            "reference_shape": True,
            "basis_only": True,
            "does_not_create_portable_verification_closure": True,
            "does_not_create_final_completion": True,
            "does_not_create_source_authority_currentness_runtime_or_follow_on": True,
        }

    request["selected_cross_carrier_evidence_basis"].update(
        {
            "outcome": EXPECTED_CROSS_CARRIER_EVIDENCE_OUTCOME,
            "result_version": RESULT_VERSION,
            "failed_check_count": 0,
            "bounded_cross_carrier_evidence_recorded": True,
            "cross_carrier_evidence_not_portable_verification_closure": True,
            "portable_verification_closure_not_created": True,
            "final_completion_not_created": True,
        }
    )
    request["selected_cross_carrier_evidence_terminal_summary_basis"].update(
        {
            "cross_carrier_evidence_landed": True,
            "portable_verification_closure_not_created": True,
            "cross_carrier_evidence_not_portable_verification_closure": True,
            "zero_exit_code_not_portable_verification_closure": True,
            "string_zero_not_portable_verification_closure": True,
            "string_zero_not_doctrine": True,
        }
    )
    request["selected_cross_carrier_evidence_boundary_basis"].update(
        {
            "outcome": EXPECTED_CROSS_CARRIER_EVIDENCE_BOUNDARY_OUTCOME,
            "failed_check_count": 0,
            "boundary_basis_only": True,
        }
    )
    request["selected_second_carrier_external_result_basis"].update(
        {
            "outcome": EXPECTED_SECOND_CARRIER_EXTERNAL_RESULT_OUTCOME,
            "failed_check_count": 0,
            "bounded_external_result_recorded": True,
            "external_result_not_portable_verification_closure": True,
        }
    )
    request["selected_returned_capture_material_basis"].update(
        {
            "exit_code": 0,
            "declared_exit_code": "0",
            "ran_7_tests_line": "Ran 7 tests in 0.451s",
            "ok_line": "OK",
            "placeholder_fields_unrepaired": True,
            "capture_only": True,
        }
    )
    request["selected_predecessor_failure_basis"].update(
        {
            "predecessor_cross_carrier_evidence_failure_preserved": True,
            "predecessor_cross_carrier_evidence_not_repaired": True,
            "predecessor_cross_carrier_evidence_not_hidden": True,
            "predecessor_cross_carrier_evidence_not_claimed_passed": True,
            "predecessor_external_result_v1_failure_preserved": True,
            "predecessor_external_result_v1_not_repaired": True,
            "predecessor_external_result_v1_not_hidden": True,
            "predecessor_external_result_v1_not_claimed_passed": True,
            "first_success_boundary_test_failure_preserved": True,
            "first_result_boundary_resolver_failure_preserved": True,
            "v1_packet_emission_failure_preserved": True,
        }
    )

    for field in POSTURE_SECTIONS:
        request[field] = {
            "posture_name": field,
            "declared": True,
            "bounded_to": "portable_verification_closure_boundary",
        }

    request.update(overrides)
    return copy.deepcopy(request)
