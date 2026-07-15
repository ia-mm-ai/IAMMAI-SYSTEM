"""Bounded resolver for second-carrier external-result posture.

This module records one portable source-body verification second-carrier
external-result posture from clean second-carrier-external-result-boundary
basis. It does not create cross-carrier evidence, portable verification
closure, source transfer, source receipt, reception authorization, source,
authority, currentness, runtime, final completion, continuation, reusable
permission, derivative reception, vessel relation, another reception request,
or follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping, Sequence
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class PortableSourceBodyVerificationSecondCarrierExternalResultError(Exception):
    """Raised for bounded hard failures in path or internal result handling."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_portable_source_body_verification_second_carrier_external_result"
)
RESULT_TYPE = "portable_source_body_verification_second_carrier_external_result"
DEFAULT_REQUEST_ID = (
    "portable_source_body_verification_second_carrier_external_result_reference_review_001"
)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_portable_source_body_verification_"
    "second_carrier_external_result"
)

CORE_QUESTION = (
    "Can the clean second-carrier-external-result-boundary basis be used to "
    "record one bounded second-carrier external-result posture without "
    "creating cross-carrier evidence, portable verification closure, source "
    "transfer, source receipt, reception authorization, source, authority, "
    "currentness, runtime, final completion, continuation, reusable permission, "
    "derivative reception, vessel relation, another reception request, or "
    "follow-on work?"
)

OUTCOME_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT_"
    "REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT_BLOCKED"
)
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = (
    "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT"
)
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT"
)
INTENT_BLOCK = (
    "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT"
)
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

EXPECTED_BOUNDARY_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_RECORDED"
)
EXPECTED_VERIFICATION_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_VERIFICATION_RECORDED"
)
EXPECTED_VERIFICATION_BOUNDARY_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_VERIFICATION_BOUNDARY_RECORDED"
)
EXPECTED_SUCCESS_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_SUCCESS_RECORDED"
)
EXPECTED_RESULT_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RESULT_RECORDED"
)
EXPECTED_OUTPUT_CAPTURE_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_OUTPUT_CAPTURE_RECORDED"
)

SUPPORTED_SCOPE_VALUES = (
    "SECOND_CARRIER_EXTERNAL_RESULT_SPEC_ONLY",
    "ONE_BOUNDED_SECOND_CARRIER_EXTERNAL_RESULT_RECORDED",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_BASIS_PRESERVED",
    "SECOND_CARRIER_VERIFICATION_BASIS_PRESERVED",
    "SECOND_CARRIER_SUCCESS_BASIS_PRESERVED",
    "SECOND_CARRIER_RESULT_BASIS_PRESERVED",
    "RETURNED_SECOND_CARRIER_CAPTURE_BASIS_PRESERVED",
    "CAPTURE_INTAKE_BASIS_PRESERVED",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_PRESERVED",
    "EXTERNAL_RESULT_RECORDED_BOUNDED",
    "EXTERNAL_RESULT_ARTIFACT_RECORDED_OR_BOUNDED",
    "EXTERNAL_RESULT_NOT_CROSS_CARRIER_EVIDENCE",
    "EXTERNAL_RESULT_NOT_PORTABLE_VERIFICATION_CLOSURE",
    "EXTERNAL_RESULT_NOT_SOURCE_TRANSFER",
    "EXTERNAL_RESULT_NOT_SOURCE_RECEIPT",
    "EXTERNAL_RESULT_NOT_RECEPTION_AUTHORIZATION",
    "ZERO_EXIT_CODE_NOT_EXTERNAL_RESULT_AS_STANDALONE_INFERENCE",
    "STRING_ZERO_NOT_EXTERNAL_RESULT_AS_STANDALONE_INFERENCE",
    "OK_OUTPUT_NOT_EXTERNAL_RESULT_AS_STANDALONE_INFERENCE",
    "RAN_7_TESTS_NOT_CROSS_CARRIER_PROOF",
    "RETURNED_CAPTURE_NOT_CROSS_CARRIER_PROOF",
    "CROSS_CARRIER_EVIDENCE_NOT_CREATED",
    "PORTABLE_VERIFICATION_CLOSURE_NOT_CREATED",
    "RECEIVING_CARRIER_NOT_AUTHORITY",
    "NO_SOURCE_CREATED",
    "NO_AUTHORITY_CREATED",
    "NO_CURRENTNESS_CREATED",
    "NO_FINAL_COMPLETION",
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
    "NO_CROSS_CARRIER_EVIDENCE_INFERENCE",
    "NO_PORTABLE_VERIFICATION_CLOSURE_INFERENCE",
    "NO_SOURCE_INFERENCE",
    "NO_AUTHORITY_INFERENCE",
    "NO_CURRENTNESS_INFERENCE",
    "NO_FINAL_COMPLETION_INFERENCE",
    "NO_RUNTIME_INFERENCE",
    "NO_FOLLOW_ON_WORK_INFERENCE",
    "NO_UNBOUNDED_PASS_FAIL_INFERENCE",
    "HIDDEN_REPO_STATE_EXCLUDED",
    "HIDDEN_REPO_STATE_NOT_USED_AS_EXTERNAL_RESULT_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_NOT_EXTERNAL_RESULT_AUTHORITY",
    "SELECTED_BASIS_REFERENCE_SHAPE_PRESERVED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
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
SUPPORTED_SECOND_CARRIER_EXTERNAL_RESULT_SCOPE = SUPPORTED_SCOPE_VALUES

REQUIRED_FALSE_NON_CLAIMS = (
    "cross_carrier_evidence_created",
    "portable_verification_closure_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "second_carrier_external_result_treated_as_cross_carrier_evidence",
    "second_carrier_external_result_treated_as_portable_verification_closure",
    "second_carrier_external_result_treated_as_source_transfer",
    "second_carrier_external_result_treated_as_source_receipt",
    "second_carrier_external_result_treated_as_reception_authorization",
    "second_carrier_external_result_treated_as_source",
    "second_carrier_external_result_treated_as_authority",
    "second_carrier_external_result_treated_as_currentness",
    "second_carrier_external_result_treated_as_final_completion",
    "second_carrier_external_result_treated_as_runtime",
    "second_carrier_external_result_treated_as_continuation",
    "second_carrier_external_result_treated_as_reusable_permission",
    "second_carrier_external_result_treated_as_follow_on_work",
    "zero_exit_code_treated_as_external_result_standalone",
    "string_zero_treated_as_external_result_standalone",
    "string_zero_representation_turned_into_doctrine",
    "ok_output_treated_as_external_result_standalone",
    "ran_7_tests_treated_as_cross_carrier_proof",
    "returned_capture_treated_as_cross_carrier_evidence",
    "receiving_carrier_treated_as_authority",
    "artifact_existence_treated_as_external_result_authority",
    "artifact_path_treated_as_currentness",
    "repo_local_availability_treated_as_external_result_authority",
    "hidden_repo_state_used_as_external_result_content",
    "hidden_repo_state_used_as_external_result_authority",
    "source_created",
    "authority_created",
    "currentness_created",
    "final_completion_claimed",
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
    "v1_repaired",
    "v1_hidden",
    "v1_claimed_passed",
    "first_success_boundary_test_repaired",
    "first_success_boundary_test_hidden",
    "first_success_boundary_test_claimed_passed",
    "first_result_boundary_resolver_repaired",
    "first_result_boundary_resolver_hidden",
    "first_result_boundary_resolver_claimed_passed",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "second_carrier_external_result_recorded",
    "bounded_second_carrier_external_result_recorded",
    "external_result_artifact_recorded_or_bounded",
    "second_carrier_external_result_boundary_basis_preserved",
    "second_carrier_verification_basis_preserved",
    "returned_second_carrier_capture_basis_preserved",
    "capture_intake_basis_preserved",
    "second_carrier_output_capture_basis_preserved",
    "external_result_recorded_bounded",
    "external_result_not_cross_carrier_evidence",
    "external_result_not_portable_verification_closure",
    "external_result_not_source_transfer",
    "external_result_not_source_receipt",
    "external_result_not_reception_authorization",
    "zero_exit_code_not_external_result_as_standalone_inference",
    "string_zero_not_external_result_as_standalone_inference",
    "ok_output_not_external_result_as_standalone_inference",
    "ran_7_tests_not_cross_carrier_proof",
    "returned_capture_not_cross_carrier_proof",
    "cross_carrier_evidence_not_created",
    "portable_verification_closure_not_created",
    "receiving_carrier_not_authority",
    "source_not_created",
    "authority_not_created",
    "currentness_not_created",
    "final_completion_not_created",
    "runtime_not_created",
    "continuation_not_authorized",
    "reusable_permission_not_created",
    "follow_on_work_not_authorized",
    "hidden_repo_state_excluded",
    "hidden_repo_state_not_used_as_external_result_authority",
    "repo_local_availability_not_external_result_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "official_enum_scope_strings_not_redacted",
    "hostile_raw_body_content_contained",
    "first_success_boundary_test_failure_preserved",
    "first_result_boundary_resolver_failure_preserved",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
)

BLOCK_CODES = (
    "DECLARED_SECOND_CARRIER_EXTERNAL_RESULT_REQUEST_MALFORMED",
    "DECLARED_SECOND_CARRIER_EXTERNAL_RESULT_REQUEST_UNREADABLE",
    "SECOND_CARRIER_EXTERNAL_RESULT_QUESTION_UNDECLARED",
    "SECOND_CARRIER_EXTERNAL_RESULT_INTENT_UNSUPPORTED",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_BASIS_MISSING",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_NOT_RECORDED",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_VERSION_NOT_0_1_0",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_DID_NOT_DECLARE_FUTURE_EXTERNAL_RESULT_STEP",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_ALREADY_CREATED_EXTERNAL_RESULT",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_ALREADY_CREATED_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_ALREADY_CREATED_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_EXTERNAL_RESULT_BOUNDARY_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_EXTERNAL_RESULT_BOUNDARY_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_EXTERNAL_RESULT_BOUNDARY_AS_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_ZERO_EXIT_CODE_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_STRING_ZERO_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_OK_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_RAN_7_TESTS_AS_CROSS_CARRIER_PROOF",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
    "SECOND_CARRIER_VERIFICATION_BASIS_MISSING",
    "SECOND_CARRIER_VERIFICATION_NOT_RECORDED",
    "SECOND_CARRIER_VERIFICATION_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_VERIFICATION_ALREADY_CREATED_EXTERNAL_RESULT",
    "SECOND_CARRIER_VERIFICATION_ALREADY_CREATED_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_VERIFICATION_ALREADY_CREATED_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_VERIFICATION_TREATED_VERIFICATION_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_VERIFICATION_TREATED_VERIFICATION_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_VERIFICATION_TREATED_ZERO_EXIT_CODE_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_VERIFICATION_TREATED_STRING_ZERO_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_VERIFICATION_TREATED_OK_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_VERIFICATION_TREATED_RAN_7_TESTS_AS_CROSS_CARRIER_PROOF",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_BASIS_MISSING",
    "SECOND_CARRIER_SUCCESS_BASIS_MISSING",
    "SECOND_CARRIER_SUCCESS_NOT_RECORDED",
    "SECOND_CARRIER_SUCCESS_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_RESULT_BASIS_MISSING",
    "SECOND_CARRIER_RESULT_NOT_RECORDED",
    "SECOND_CARRIER_RESULT_FAILED_CHECKS_PRESENT",
    "RETURNED_CAPTURE_INTAKE_BASIS_MISSING",
    "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
    "RETURNED_CAPTURE_TREATED_AS_EXTERNAL_RESULT",
    "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_PROOF",
    "ZERO_EXIT_CODE_TREATED_AS_EXTERNAL_RESULT",
    "STRING_ZERO_TREATED_AS_EXTERNAL_RESULT",
    "OK_OUTPUT_TREATED_AS_EXTERNAL_RESULT",
    "RAN_7_TESTS_TREATED_AS_CROSS_CARRIER_PROOF",
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
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_SOURCE_TRANSFER",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_SOURCE_RECEIPT",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_RECEPTION_AUTHORIZATION",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_SOURCE",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_AUTHORITY",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_CURRENTNESS",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_FINAL_COMPLETION",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_RUNTIME",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_CONTINUATION",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_REUSABLE_PERMISSION",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_FOLLOW_ON_WORK",
    "CROSS_CARRIER_EVIDENCE_CREATED",
    "PORTABLE_VERIFICATION_CLOSURE_CREATED",
    "SOURCE_TRANSFER_OCCURRED",
    "SOURCE_RECEIPT_OCCURRED",
    "RECEPTION_AUTHORIZATION_CREATED",
    "SOURCE_CREATED",
    "AUTHORITY_CREATED",
    "CURRENTNESS_CREATED",
    "FINAL_COMPLETION_CLAIMED",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_EXTERNAL_RESULT_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_EXTERNAL_RESULT_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_EXTERNAL_RESULT_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_EXTERNAL_RESULT_AUTHORITY",
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
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_EXTERNAL_RESULT",
    "STRING_ZERO_REPRESENTATION_TURNED_INTO_DOCTRINE",
    "ARTIFACTS_MUTATED",
    "RETURNED_CAPTURE_MATERIAL_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_SECOND_CARRIER_EXTERNAL_RESULT_SCOPE",
)

SELECTED_BASIS_KEYS = (
    "selected_second_carrier_external_result_boundary_basis",
    "selected_second_carrier_external_result_boundary_terminal_summary_basis",
    "selected_second_carrier_verification_basis",
    "selected_second_carrier_verification_terminal_summary_basis",
    "selected_second_carrier_verification_boundary_basis",
    "selected_second_carrier_success_basis",
    "selected_second_carrier_result_basis",
    "selected_second_carrier_result_terminal_summary_basis",
    "selected_returned_second_carrier_live_capture_intake_basis",
    "selected_returned_capture_material_basis",
    "selected_second_carrier_output_capture_basis",
    "selected_packet_transfer_basis",
    "selected_packet_emission_basis",
    "selected_packet_emission_boundary_v2_basis",
    "selected_packet_emission_boundary_v1_predecessor_failure_basis",
    "selected_packet_artifact_basis",
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

POSTURE_KEYS = (
    "second_carrier_external_result_spec_only_posture",
    "one_bounded_second_carrier_external_result_posture",
    "second_carrier_external_result_boundary_basis_preserved_posture",
    "second_carrier_verification_basis_preserved_posture",
    "returned_second_carrier_capture_basis_preserved_posture",
    "capture_intake_basis_preserved_posture",
    "second_carrier_output_capture_basis_preserved_posture",
    "external_result_recorded_bounded_posture",
    "external_result_artifact_recorded_or_bounded_posture",
    "external_result_not_cross_carrier_evidence_posture",
    "external_result_not_portable_verification_closure_posture",
    "external_result_not_source_transfer_posture",
    "external_result_not_source_receipt_posture",
    "external_result_not_reception_authorization_posture",
    "zero_exit_code_not_external_result_as_standalone_inference_posture",
    "string_zero_not_external_result_as_standalone_inference_posture",
    "ok_output_not_external_result_as_standalone_inference_posture",
    "ran_7_tests_not_cross_carrier_proof_posture",
    "returned_capture_not_cross_carrier_proof_posture",
    "cross_carrier_evidence_not_created_posture",
    "portable_verification_closure_not_created_posture",
    "receiving_carrier_not_authority_posture",
    "source_not_created_posture",
    "authority_not_created_posture",
    "currentness_not_created_posture",
    "final_completion_not_created_posture",
    "runtime_not_created_posture",
    "continuation_not_authorized_posture",
    "reusable_permission_not_created_posture",
    "follow_on_work_not_authorized_posture",
    "hidden_repo_state_excluded_posture",
    "repo_local_availability_not_external_result_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "first_success_boundary_test_failure_preserved_posture",
    "first_result_boundary_resolver_failure_preserved_posture",
)

BOUNDARY_EXTRA_FIELDS = (
    "selected_second_carrier_external_result_boundary_result_path",
    "selected_second_carrier_external_result_boundary_result_outcome",
    "selected_second_carrier_external_result_boundary_result_version",
    "selected_second_carrier_external_result_boundary_failed_check_count",
    "selected_second_carrier_external_result_boundary_declared_future_external_result_step",
    "selected_second_carrier_external_result_boundary_already_created_external_result",
    "selected_second_carrier_external_result_boundary_already_created_cross_carrier_evidence",
    "selected_second_carrier_external_result_boundary_already_created_portable_verification_closure",
    "selected_second_carrier_external_result_boundary_treated_external_result_boundary_as_external_result",
    "selected_second_carrier_external_result_boundary_treated_external_result_boundary_as_cross_carrier_evidence",
    "selected_second_carrier_external_result_boundary_treated_external_result_boundary_as_portable_verification_closure",
    "selected_second_carrier_external_result_boundary_zero_exit_code_not_external_result",
    "selected_second_carrier_external_result_boundary_string_zero_not_external_result",
    "selected_second_carrier_external_result_boundary_ok_not_external_result",
    "selected_second_carrier_external_result_boundary_ran_7_tests_not_cross_carrier_proof",
    "selected_second_carrier_external_result_boundary_official_enum_scope_strings_redacted",
    "selected_second_carrier_external_result_boundary_first_success_boundary_test_failure_preserved",
)

VERIFICATION_EXTRA_FIELDS = (
    "selected_second_carrier_verification_result_path",
    "selected_second_carrier_verification_result_outcome",
    "selected_second_carrier_verification_result_version",
    "selected_second_carrier_verification_failed_check_count",
    "selected_second_carrier_verification_bounded_verification_recorded",
    "selected_second_carrier_verification_treated_verification_as_external_result",
    "selected_second_carrier_verification_treated_verification_as_cross_carrier_evidence",
    "selected_second_carrier_verification_zero_exit_code_not_external_result",
    "selected_second_carrier_verification_string_zero_not_external_result",
    "selected_second_carrier_verification_ok_not_external_result",
    "selected_second_carrier_verification_ran_7_tests_not_cross_carrier_proof",
)

RETURNED_CAPTURE_EXTRA_FIELDS = (
    "selected_returned_capture_intake_path",
    "selected_returned_capture_intake_preserved",
    "selected_returned_capture_intake_capture_only",
    "selected_returned_capture_from_macbook_pro_to_macbook_air",
    "selected_returned_capture_zip_path",
    "selected_returned_capture_hash_path",
    "selected_returned_capture_extracted_directory_path",
    "selected_returned_capture_combined_terminal_log_path",
    "selected_returned_capture_stdout_path",
    "selected_returned_capture_stderr_path",
    "selected_returned_capture_command_text",
    "selected_returned_capture_working_directory",
    "selected_returned_capture_started_at",
    "selected_returned_capture_completed_at",
    "selected_returned_capture_exit_code",
    "selected_returned_capture_declared_exit_code",
    "selected_returned_capture_ran_7_tests_line",
    "selected_returned_capture_ok_line",
    "selected_returned_capture_raw_placeholder_carrier_label",
    "selected_returned_capture_raw_placeholder_carrier_type",
    "selected_returned_capture_placeholder_fields_unrepaired",
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
    "capture_body",
    "second_carrier_external_result_body",
    "cross_carrier_evidence_body",
    "portable_verification_closure_body",
    "source_body",
    "authority_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
}
HOSTILE_SENTINELS = (
    "RAW_SECOND_CARRIER_EXTERNAL_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)
REDACTED_CONTENT = "[bounded-redacted-raw-or-hidden-state]"

WHAT_REMAINS_OPEN_ITEMS = (
    "second-carrier external-result test",
    "second-carrier external-result live artifact",
    "second-carrier external-result terminal summary, if needed",
    "cross-carrier evidence review",
    "line-level portable verification closure review",
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
    "final completion",
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
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace(
        "+00:00", "Z"
    )


def _has_value(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return value != ""
    if isinstance(value, Mapping):
        return bool(value)
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return bool(value)
    return True


def _as_bool(value: Any, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return default
    if isinstance(value, str):
        lowered = value.strip().lower()
        if lowered in {"true", "yes", "1"}:
            return True
        if lowered in {"false", "no", "0"}:
            return False
    return bool(value)


def _is_zero(value: Any) -> bool:
    return value == 0 or value == "0"


def _safe_int(value: Any, default: int | None = None) -> int | None:
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


def _sanitize(value: Any, key: str = "") -> Any:
    key_lower = key.lower()
    if key_lower in SENSITIVE_CONTENT_KEYS or key_lower.endswith("_body"):
        return REDACTED_CONTENT
    if isinstance(value, str):
        if any(sentinel in value for sentinel in HOSTILE_SENTINELS):
            return REDACTED_CONTENT
        return value
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, Mapping):
        return {str(k): _sanitize(v, str(k)) for k, v in value.items()}
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return [_sanitize(item, key) for item in value]
    return copy.deepcopy(value)


def _request_id(request: Mapping[str, Any]) -> str:
    value = request.get("second_carrier_external_result_request_id")
    if isinstance(value, str) and value:
        return value
    return DEFAULT_REQUEST_ID


def _scope_values(scope: Any) -> list[str]:
    if scope is None:
        return []
    if isinstance(scope, str):
        return [scope]
    if isinstance(scope, Mapping):
        values: list[str] = []
        for key, value in scope.items():
            if _as_bool(value, default=False):
                values.append(str(key))
        return values
    if isinstance(scope, Sequence) and not isinstance(scope, (str, bytes, bytearray)):
        return [str(value) for value in scope]
    return [str(scope)]


def _unsupported_scope_values(request: Mapping[str, Any]) -> list[str]:
    supported = set(SUPPORTED_SCOPE_VALUES)
    return [
        value
        for value in _scope_values(request.get("second_carrier_external_result_scope"))
        if value not in supported
    ]


def _basis_declared(request: Mapping[str, Any], key: str) -> bool:
    return _has_value(request.get(key))


def _posture_declared(request: Mapping[str, Any], key: str) -> bool:
    value = request.get(key)
    if isinstance(value, Mapping):
        for posture_key in (
            "declared",
            "request_declared",
            "preserved",
            "recorded",
            "bounded",
        ):
            if posture_key in value:
                return _as_bool(value.get(posture_key), default=False)
        return bool(value)
    return _as_bool(value, default=False)


def _declared_non_claims(request: Mapping[str, Any]) -> Mapping[str, Any]:
    value = request.get("declared_non_claims")
    if isinstance(value, Mapping):
        return value
    return {}


def _claim_value(request: Mapping[str, Any], key: str) -> Any:
    if key in request:
        return request[key]
    return _declared_non_claims(request).get(key)


def _claim_is_false(request: Mapping[str, Any], key: str) -> bool:
    claims = _declared_non_claims(request)
    return key in claims and claims[key] is False


def _reference_section(
    section_name: str,
    value: Any,
    extras: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    section = {
        "section_name": section_name,
        "basis_declared": _has_value(value),
        "selected_basis_reference_shape_preserved": True,
        "selected_basis": _sanitize(value, section_name),
    }
    if extras:
        section["selected_basis_shortcut_fields"] = _sanitize(extras)
    return section


def _posture_section(section_name: str, request: Mapping[str, Any]) -> dict[str, Any]:
    value = request.get(section_name)
    return {
        "section_name": section_name,
        "posture_declared": _posture_declared(request, section_name),
        "posture": _sanitize(value, section_name),
        "bounded_second_carrier_external_result_posture_only": True,
    }


def _selected_basis_extras(
    section_name: str, request: Mapping[str, Any]
) -> dict[str, Any]:
    fields: tuple[str, ...] = ()
    if section_name == "selected_second_carrier_external_result_boundary_basis":
        fields = BOUNDARY_EXTRA_FIELDS
    elif section_name == "selected_second_carrier_verification_basis":
        fields = VERIFICATION_EXTRA_FIELDS
    elif section_name in {
        "selected_returned_second_carrier_live_capture_intake_basis",
        "selected_returned_capture_material_basis",
    }:
        fields = RETURNED_CAPTURE_EXTRA_FIELDS
    elif section_name == "selected_second_carrier_verification_boundary_basis":
        fields = (
            "selected_second_carrier_verification_boundary_result_path",
            "selected_second_carrier_verification_boundary_result_outcome",
            "selected_second_carrier_verification_boundary_failed_check_count",
        )
    elif section_name == "selected_second_carrier_success_basis":
        fields = (
            "selected_second_carrier_success_result_path",
            "selected_second_carrier_success_result_outcome",
            "selected_second_carrier_success_failed_check_count",
        )
    elif section_name == "selected_second_carrier_result_basis":
        fields = (
            "selected_second_carrier_result_result_path",
            "selected_second_carrier_result_result_outcome",
            "selected_second_carrier_result_failed_check_count",
        )
    elif section_name == "selected_second_carrier_output_capture_basis":
        fields = (
            "selected_second_carrier_output_capture_result_path",
            "selected_second_carrier_output_capture_result_outcome",
            "selected_second_carrier_output_capture_failed_check_count",
        )
    return {field: request.get(field) for field in fields if field in request}


def _check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str,
) -> None:
    public_code = code if code in BLOCK_CODES else "DECLARED_SECOND_CARRIER_EXTERNAL_RESULT_REQUEST_MALFORMED"
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


def _failed_checks(checks: Sequence[Mapping[str, Any]]) -> list[Mapping[str, Any]]:
    return [check for check in checks if not _as_bool(check.get("passed"))]


def _first_failed_code(checks: Sequence[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if not _as_bool(check.get("passed")):
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str):
                return code
    return None


def _evaluate_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    intent = request.get("second_carrier_external_result_intent")
    scope_values = _scope_values(request.get("second_carrier_external_result_scope"))
    unsupported_scope = _unsupported_scope_values(request)

    _check(
        checks,
        "second-carrier external-result question declared",
        _has_value(request.get("second_carrier_external_result_question")),
        CORE_QUESTION,
        request.get("second_carrier_external_result_question"),
        "SECOND_CARRIER_EXTERNAL_RESULT_QUESTION_UNDECLARED",
    )
    _check(
        checks,
        "second-carrier external-result intent supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "SECOND_CARRIER_EXTERNAL_RESULT_INTENT_UNSUPPORTED",
    )
    _check(
        checks,
        "second-carrier external-result scope values supported",
        bool(scope_values) and not unsupported_scope,
        SUPPORTED_SCOPE_VALUES,
        scope_values,
        "UNSUPPORTED_SECOND_CARRIER_EXTERNAL_RESULT_SCOPE",
    )

    _check(
        checks,
        "second-carrier-external-result-boundary basis declared",
        _basis_declared(request, "selected_second_carrier_external_result_boundary_basis"),
        "declared selected second-carrier external-result boundary basis",
        request.get("selected_second_carrier_external_result_boundary_basis"),
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_BASIS_MISSING",
    )
    _check(
        checks,
        "second-carrier-external-result-boundary outcome recorded",
        request.get("selected_second_carrier_external_result_boundary_result_outcome")
        == EXPECTED_BOUNDARY_OUTCOME,
        EXPECTED_BOUNDARY_OUTCOME,
        request.get("selected_second_carrier_external_result_boundary_result_outcome"),
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_NOT_RECORDED",
    )
    _check(
        checks,
        "second-carrier-external-result-boundary version 0.1.0",
        request.get("selected_second_carrier_external_result_boundary_result_version")
        == RESULT_VERSION,
        RESULT_VERSION,
        request.get("selected_second_carrier_external_result_boundary_result_version"),
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_VERSION_NOT_0_1_0",
    )
    _check(
        checks,
        "second-carrier-external-result-boundary failed checks zero",
        _safe_int(
            request.get(
                "selected_second_carrier_external_result_boundary_failed_check_count"
            )
        )
        == 0,
        0,
        request.get("selected_second_carrier_external_result_boundary_failed_check_count"),
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_FAILED_CHECKS_PRESENT",
    )
    _check(
        checks,
        "second-carrier-external-result-boundary declared future external-result step",
        _as_bool(
            request.get(
                "selected_second_carrier_external_result_boundary_declared_future_external_result_step"
            )
        ),
        True,
        request.get(
            "selected_second_carrier_external_result_boundary_declared_future_external_result_step"
        ),
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_DID_NOT_DECLARE_FUTURE_EXTERNAL_RESULT_STEP",
    )
    _check(
        checks,
        "second-carrier-external-result-boundary did not already create external result",
        not _as_bool(
            request.get(
                "selected_second_carrier_external_result_boundary_already_created_external_result"
            )
        ),
        False,
        request.get(
            "selected_second_carrier_external_result_boundary_already_created_external_result"
        ),
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_ALREADY_CREATED_EXTERNAL_RESULT",
    )
    _check(
        checks,
        "second-carrier-external-result-boundary did not already create cross-carrier evidence",
        not _as_bool(
            request.get(
                "selected_second_carrier_external_result_boundary_already_created_cross_carrier_evidence"
            )
        ),
        False,
        request.get(
            "selected_second_carrier_external_result_boundary_already_created_cross_carrier_evidence"
        ),
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_ALREADY_CREATED_CROSS_CARRIER_EVIDENCE",
    )
    _check(
        checks,
        "second-carrier-external-result-boundary did not already create portable verification closure",
        not _as_bool(
            request.get(
                "selected_second_carrier_external_result_boundary_already_created_portable_verification_closure"
            )
        ),
        False,
        request.get(
            "selected_second_carrier_external_result_boundary_already_created_portable_verification_closure"
        ),
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_ALREADY_CREATED_PORTABLE_VERIFICATION_CLOSURE",
    )
    _check(
        checks,
        "second-carrier-external-result-boundary did not treat boundary as external result",
        not _as_bool(
            request.get(
                "selected_second_carrier_external_result_boundary_treated_external_result_boundary_as_external_result"
            )
        ),
        False,
        request.get(
            "selected_second_carrier_external_result_boundary_treated_external_result_boundary_as_external_result"
        ),
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_EXTERNAL_RESULT_BOUNDARY_AS_EXTERNAL_RESULT",
    )
    _check(
        checks,
        "second-carrier-external-result-boundary did not treat boundary as cross-carrier evidence",
        not _as_bool(
            request.get(
                "selected_second_carrier_external_result_boundary_treated_external_result_boundary_as_cross_carrier_evidence"
            )
        ),
        False,
        request.get(
            "selected_second_carrier_external_result_boundary_treated_external_result_boundary_as_cross_carrier_evidence"
        ),
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_EXTERNAL_RESULT_BOUNDARY_AS_CROSS_CARRIER_EVIDENCE",
    )
    _check(
        checks,
        "second-carrier-external-result-boundary did not treat boundary as portable verification closure",
        not _as_bool(
            request.get(
                "selected_second_carrier_external_result_boundary_treated_external_result_boundary_as_portable_verification_closure"
            )
        ),
        False,
        request.get(
            "selected_second_carrier_external_result_boundary_treated_external_result_boundary_as_portable_verification_closure"
        ),
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_EXTERNAL_RESULT_BOUNDARY_AS_PORTABLE_VERIFICATION_CLOSURE",
    )
    _check(
        checks,
        "second-carrier-external-result-boundary kept zero exit code not external result",
        _as_bool(
            request.get(
                "selected_second_carrier_external_result_boundary_zero_exit_code_not_external_result"
            )
        ),
        True,
        request.get(
            "selected_second_carrier_external_result_boundary_zero_exit_code_not_external_result"
        ),
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_ZERO_EXIT_CODE_AS_EXTERNAL_RESULT",
    )
    _check(
        checks,
        'second-carrier-external-result-boundary kept string "0" not external result',
        _as_bool(
            request.get(
                "selected_second_carrier_external_result_boundary_string_zero_not_external_result"
            )
        ),
        True,
        request.get(
            "selected_second_carrier_external_result_boundary_string_zero_not_external_result"
        ),
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_STRING_ZERO_AS_EXTERNAL_RESULT",
    )
    _check(
        checks,
        "second-carrier-external-result-boundary kept OK not external result",
        _as_bool(
            request.get(
                "selected_second_carrier_external_result_boundary_ok_not_external_result"
            )
        ),
        True,
        request.get(
            "selected_second_carrier_external_result_boundary_ok_not_external_result"
        ),
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_OK_AS_EXTERNAL_RESULT",
    )
    _check(
        checks,
        "second-carrier-external-result-boundary kept Ran 7 tests not cross-carrier proof",
        _as_bool(
            request.get(
                "selected_second_carrier_external_result_boundary_ran_7_tests_not_cross_carrier_proof"
            )
        ),
        True,
        request.get(
            "selected_second_carrier_external_result_boundary_ran_7_tests_not_cross_carrier_proof"
        ),
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_RAN_7_TESTS_AS_CROSS_CARRIER_PROOF",
    )
    _check(
        checks,
        "second-carrier-external-result-boundary kept official enum scope strings unredacted",
        not _as_bool(
            request.get(
                "selected_second_carrier_external_result_boundary_official_enum_scope_strings_redacted"
            )
        ),
        False,
        request.get(
            "selected_second_carrier_external_result_boundary_official_enum_scope_strings_redacted"
        ),
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
    )
    _check(
        checks,
        "second-carrier-external-result-boundary preserved first success-boundary test failure",
        _as_bool(
            request.get(
                "selected_second_carrier_external_result_boundary_first_success_boundary_test_failure_preserved"
            )
        ),
        True,
        request.get(
            "selected_second_carrier_external_result_boundary_first_success_boundary_test_failure_preserved"
        ),
        "FIRST_SUCCESS_BOUNDARY_TEST_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    )

    _check(
        checks,
        "second-carrier-verification basis declared",
        _basis_declared(request, "selected_second_carrier_verification_basis"),
        "declared selected second-carrier verification basis",
        request.get("selected_second_carrier_verification_basis"),
        "SECOND_CARRIER_VERIFICATION_BASIS_MISSING",
    )
    _check(
        checks,
        "second-carrier-verification outcome recorded",
        request.get("selected_second_carrier_verification_result_outcome")
        == EXPECTED_VERIFICATION_OUTCOME,
        EXPECTED_VERIFICATION_OUTCOME,
        request.get("selected_second_carrier_verification_result_outcome"),
        "SECOND_CARRIER_VERIFICATION_NOT_RECORDED",
    )
    _check(
        checks,
        "second-carrier-verification version 0.1.0",
        request.get("selected_second_carrier_verification_result_version")
        == RESULT_VERSION,
        RESULT_VERSION,
        request.get("selected_second_carrier_verification_result_version"),
        "SECOND_CARRIER_VERIFICATION_NOT_RECORDED",
    )
    _check(
        checks,
        "second-carrier-verification failed checks zero",
        _safe_int(request.get("selected_second_carrier_verification_failed_check_count"))
        == 0,
        0,
        request.get("selected_second_carrier_verification_failed_check_count"),
        "SECOND_CARRIER_VERIFICATION_FAILED_CHECKS_PRESENT",
    )
    _check(
        checks,
        "second-carrier-verification recorded bounded verification",
        _as_bool(
            request.get("selected_second_carrier_verification_bounded_verification_recorded")
        ),
        True,
        request.get("selected_second_carrier_verification_bounded_verification_recorded"),
        "SECOND_CARRIER_VERIFICATION_NOT_RECORDED",
    )
    _check(
        checks,
        "second-carrier-verification did not treat verification as external result",
        not _as_bool(
            request.get(
                "selected_second_carrier_verification_treated_verification_as_external_result"
            )
        ),
        False,
        request.get(
            "selected_second_carrier_verification_treated_verification_as_external_result"
        ),
        "SECOND_CARRIER_VERIFICATION_TREATED_VERIFICATION_AS_EXTERNAL_RESULT",
    )
    _check(
        checks,
        "second-carrier-verification did not treat verification as cross-carrier evidence",
        not _as_bool(
            request.get(
                "selected_second_carrier_verification_treated_verification_as_cross_carrier_evidence"
            )
        ),
        False,
        request.get(
            "selected_second_carrier_verification_treated_verification_as_cross_carrier_evidence"
        ),
        "SECOND_CARRIER_VERIFICATION_TREATED_VERIFICATION_AS_CROSS_CARRIER_EVIDENCE",
    )
    _check(
        checks,
        "second-carrier-verification kept zero exit code not external result",
        _as_bool(
            request.get(
                "selected_second_carrier_verification_zero_exit_code_not_external_result"
            )
        ),
        True,
        request.get("selected_second_carrier_verification_zero_exit_code_not_external_result"),
        "SECOND_CARRIER_VERIFICATION_TREATED_ZERO_EXIT_CODE_AS_EXTERNAL_RESULT",
    )
    _check(
        checks,
        'second-carrier-verification kept string "0" not external result',
        _as_bool(
            request.get(
                "selected_second_carrier_verification_string_zero_not_external_result"
            )
        ),
        True,
        request.get("selected_second_carrier_verification_string_zero_not_external_result"),
        "SECOND_CARRIER_VERIFICATION_TREATED_STRING_ZERO_AS_EXTERNAL_RESULT",
    )
    _check(
        checks,
        "second-carrier-verification kept OK not external result",
        _as_bool(request.get("selected_second_carrier_verification_ok_not_external_result")),
        True,
        request.get("selected_second_carrier_verification_ok_not_external_result"),
        "SECOND_CARRIER_VERIFICATION_TREATED_OK_AS_EXTERNAL_RESULT",
    )
    _check(
        checks,
        "second-carrier-verification kept Ran 7 tests not cross-carrier proof",
        _as_bool(
            request.get(
                "selected_second_carrier_verification_ran_7_tests_not_cross_carrier_proof"
            )
        ),
        True,
        request.get(
            "selected_second_carrier_verification_ran_7_tests_not_cross_carrier_proof"
        ),
        "SECOND_CARRIER_VERIFICATION_TREATED_RAN_7_TESTS_AS_CROSS_CARRIER_PROOF",
    )

    _check(
        checks,
        "second-carrier-verification-boundary basis declared",
        _basis_declared(request, "selected_second_carrier_verification_boundary_basis"),
        "declared selected second-carrier verification-boundary basis",
        request.get("selected_second_carrier_verification_boundary_basis"),
        "SECOND_CARRIER_VERIFICATION_BOUNDARY_BASIS_MISSING",
    )
    _check(
        checks,
        "second-carrier-verification-boundary outcome recorded",
        request.get("selected_second_carrier_verification_boundary_result_outcome")
        == EXPECTED_VERIFICATION_BOUNDARY_OUTCOME,
        EXPECTED_VERIFICATION_BOUNDARY_OUTCOME,
        request.get("selected_second_carrier_verification_boundary_result_outcome"),
        "SECOND_CARRIER_VERIFICATION_BOUNDARY_BASIS_MISSING",
    )
    _check(
        checks,
        "second-carrier-verification-boundary failed checks zero",
        _safe_int(
            request.get("selected_second_carrier_verification_boundary_failed_check_count")
        )
        == 0,
        0,
        request.get("selected_second_carrier_verification_boundary_failed_check_count"),
        "SECOND_CARRIER_VERIFICATION_BOUNDARY_BASIS_MISSING",
    )

    _check(
        checks,
        "second-carrier-success basis declared",
        _basis_declared(request, "selected_second_carrier_success_basis"),
        "declared selected second-carrier success basis",
        request.get("selected_second_carrier_success_basis"),
        "SECOND_CARRIER_SUCCESS_BASIS_MISSING",
    )
    _check(
        checks,
        "second-carrier-success outcome recorded",
        request.get("selected_second_carrier_success_result_outcome")
        == EXPECTED_SUCCESS_OUTCOME,
        EXPECTED_SUCCESS_OUTCOME,
        request.get("selected_second_carrier_success_result_outcome"),
        "SECOND_CARRIER_SUCCESS_NOT_RECORDED",
    )
    _check(
        checks,
        "second-carrier-success failed checks zero",
        _safe_int(request.get("selected_second_carrier_success_failed_check_count")) == 0,
        0,
        request.get("selected_second_carrier_success_failed_check_count"),
        "SECOND_CARRIER_SUCCESS_FAILED_CHECKS_PRESENT",
    )

    _check(
        checks,
        "second-carrier-result basis declared",
        _basis_declared(request, "selected_second_carrier_result_basis"),
        "declared selected second-carrier result basis",
        request.get("selected_second_carrier_result_basis"),
        "SECOND_CARRIER_RESULT_BASIS_MISSING",
    )
    _check(
        checks,
        "second-carrier-result outcome recorded",
        request.get("selected_second_carrier_result_result_outcome")
        == EXPECTED_RESULT_OUTCOME,
        EXPECTED_RESULT_OUTCOME,
        request.get("selected_second_carrier_result_result_outcome"),
        "SECOND_CARRIER_RESULT_NOT_RECORDED",
    )
    _check(
        checks,
        "second-carrier-result failed checks zero",
        _safe_int(request.get("selected_second_carrier_result_failed_check_count")) == 0,
        0,
        request.get("selected_second_carrier_result_failed_check_count"),
        "SECOND_CARRIER_RESULT_FAILED_CHECKS_PRESENT",
    )

    _check(
        checks,
        "returned capture intake basis declared",
        _basis_declared(request, "selected_returned_second_carrier_live_capture_intake_basis"),
        "declared returned second-carrier live capture intake basis",
        request.get("selected_returned_second_carrier_live_capture_intake_basis"),
        "RETURNED_CAPTURE_INTAKE_BASIS_MISSING",
    )
    _check(
        checks,
        "returned capture intake preserved",
        _as_bool(request.get("selected_returned_capture_intake_preserved")),
        True,
        request.get("selected_returned_capture_intake_preserved"),
        "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
    )
    _check(
        checks,
        "returned capture intake says capture-only",
        _as_bool(request.get("selected_returned_capture_intake_capture_only")),
        True,
        request.get("selected_returned_capture_intake_capture_only"),
        "RETURNED_CAPTURE_TREATED_AS_EXTERNAL_RESULT",
    )
    _check(
        checks,
        "MacBook Pro to MacBook Air return preserved",
        _as_bool(request.get("selected_returned_capture_from_macbook_pro_to_macbook_air")),
        True,
        request.get("selected_returned_capture_from_macbook_pro_to_macbook_air"),
        "RECEIVING_CARRIER_TREATED_AS_AUTHORITY",
    )
    _check(
        checks,
        "returned capture material basis declared",
        _basis_declared(request, "selected_returned_capture_material_basis"),
        "declared selected returned capture material basis",
        request.get("selected_returned_capture_material_basis"),
        "RETURNED_CAPTURE_MATERIAL_MISSING",
    )
    for field, code, label in (
        ("selected_returned_capture_zip_path", "RETURNED_ZIP_PATH_MISSING", "zip"),
        ("selected_returned_capture_hash_path", "RETURNED_HASH_PATH_MISSING", "hash"),
        (
            "selected_returned_capture_extracted_directory_path",
            "RETURNED_EXTRACTED_DIRECTORY_MISSING",
            "extracted directory",
        ),
        (
            "selected_returned_capture_combined_terminal_log_path",
            "RETURNED_COMBINED_TERMINAL_LOG_MISSING",
            "combined terminal log",
        ),
        ("selected_returned_capture_exit_code", "RETURNED_EXIT_CODE_MISSING", "exit code"),
        ("selected_returned_capture_command_text", "RETURNED_COMMAND_TEXT_MISSING", "command"),
    ):
        _check(
            checks,
            f"returned capture {label} basis declared",
            _has_value(request.get(field)),
            f"declared returned capture {label} basis",
            request.get(field),
            code,
        )
    _check(
        checks,
        "returned capture timestamps basis declared",
        _has_value(request.get("selected_returned_capture_started_at"))
        and _has_value(request.get("selected_returned_capture_completed_at")),
        "declared run_started_at and run_completed_at",
        {
            "started_at": request.get("selected_returned_capture_started_at"),
            "completed_at": request.get("selected_returned_capture_completed_at"),
        },
        "RETURNED_TIMESTAMPS_MISSING",
    )
    _check(
        checks,
        'declared string "0" representation not turned into doctrine',
        request.get("selected_returned_capture_declared_exit_code") == "0"
        and not _as_bool(_claim_value(request, "string_zero_representation_turned_into_doctrine")),
        'string "0" preserved as declared-input representation only',
        {
            "declared_exit_code": request.get("selected_returned_capture_declared_exit_code"),
            "string_zero_representation_turned_into_doctrine": _claim_value(
                request, "string_zero_representation_turned_into_doctrine"
            ),
        },
        "STRING_ZERO_REPRESENTATION_TURNED_INTO_DOCTRINE",
    )
    _check(
        checks,
        "returned capture exit code zero preserved as basis only",
        _is_zero(request.get("selected_returned_capture_exit_code")),
        0,
        request.get("selected_returned_capture_exit_code"),
        "RETURNED_EXIT_CODE_MISSING",
    )
    _check(
        checks,
        "returned capture Ran 7 tests line preserved as non-proof",
        "Ran 7 tests" in str(request.get("selected_returned_capture_ran_7_tests_line", "")),
        "Ran 7 tests",
        request.get("selected_returned_capture_ran_7_tests_line"),
        "RAN_7_TESTS_TREATED_AS_CROSS_CARRIER_PROOF",
    )
    _check(
        checks,
        "returned capture OK line preserved as non-external-result",
        str(request.get("selected_returned_capture_ok_line", "")).strip() == "OK",
        "OK",
        request.get("selected_returned_capture_ok_line"),
        "OK_OUTPUT_TREATED_AS_EXTERNAL_RESULT",
    )
    _check(
        checks,
        "raw placeholder carrier fields preserved and unrepaired",
        _as_bool(request.get("selected_returned_capture_placeholder_fields_unrepaired")),
        True,
        request.get("selected_returned_capture_placeholder_fields_unrepaired"),
        "PLACEHOLDER_CARRIER_FIELDS_REPAIRED",
    )

    _check(
        checks,
        "second-carrier output capture basis declared",
        _basis_declared(request, "selected_second_carrier_output_capture_basis"),
        "declared selected second-carrier output capture basis",
        request.get("selected_second_carrier_output_capture_basis"),
        "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_MISSING",
    )
    _check(
        checks,
        "second-carrier output capture outcome recorded",
        request.get("selected_second_carrier_output_capture_result_outcome")
        == EXPECTED_OUTPUT_CAPTURE_OUTCOME,
        EXPECTED_OUTPUT_CAPTURE_OUTCOME,
        request.get("selected_second_carrier_output_capture_result_outcome"),
        "SECOND_CARRIER_OUTPUT_CAPTURE_NOT_RECORDED",
    )
    _check(
        checks,
        "second-carrier output capture failed checks zero",
        _safe_int(
            request.get("selected_second_carrier_output_capture_failed_check_count")
        )
        == 0,
        0,
        request.get("selected_second_carrier_output_capture_failed_check_count"),
        "SECOND_CARRIER_OUTPUT_CAPTURE_FAILED_CHECKS_PRESENT",
    )

    for basis_key in (
        "selected_packet_transfer_basis",
        "selected_packet_emission_basis",
        "selected_packet_emission_boundary_v2_basis",
        "selected_packet_emission_boundary_v1_predecessor_failure_basis",
        "selected_packet_artifact_basis",
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
    ):
        _check(
            checks,
            f"{basis_key} declared",
            _basis_declared(request, basis_key),
            f"declared {basis_key}",
            request.get(basis_key),
            "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_BASIS_MISSING",
        )

    for posture_key in POSTURE_KEYS:
        _check(
            checks,
            f"{posture_key} declared",
            _posture_declared(request, posture_key),
            f"declared {posture_key}",
            request.get(posture_key),
            "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_BASIS_MISSING",
        )

    _check(
        checks,
        "selected basis reference-shaped",
        _as_bool(request.get("reference_shaped_input_posture"), default=True),
        True,
        request.get("reference_shaped_input_posture", True),
        "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    )
    _check(
        checks,
        "hidden repo state excluded",
        _posture_declared(request, "hidden_repo_state_excluded_posture")
        and not _as_bool(_claim_value(request, "hidden_repo_state_used_as_external_result_content"))
        and not _as_bool(_claim_value(request, "hidden_repo_state_used_as_external_result_authority")),
        "hidden repo state excluded and not authority/content",
        {
            "hidden_repo_state_excluded_posture": request.get(
                "hidden_repo_state_excluded_posture"
            ),
            "hidden_repo_state_used_as_external_result_content": _claim_value(
                request, "hidden_repo_state_used_as_external_result_content"
            ),
            "hidden_repo_state_used_as_external_result_authority": _claim_value(
                request, "hidden_repo_state_used_as_external_result_authority"
            ),
        },
        "HIDDEN_REPO_STATE_USED_AS_EXTERNAL_RESULT_CONTENT",
    )
    _check(
        checks,
        "repo-local availability not external-result authority",
        _posture_declared(request, "repo_local_availability_not_external_result_authority_posture")
        and not _as_bool(
            _claim_value(request, "repo_local_availability_treated_as_external_result_authority")
        ),
        "repo-local availability is not external-result authority",
        {
            "posture": request.get(
                "repo_local_availability_not_external_result_authority_posture"
            ),
            "claim": _claim_value(
                request, "repo_local_availability_treated_as_external_result_authority"
            ),
        },
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_EXTERNAL_RESULT_AUTHORITY",
    )
    _check(
        checks,
        "raw full prior artifact body not returned",
        not _as_bool(_claim_value(request, "raw_full_prior_artifact_body_returned")),
        False,
        _claim_value(request, "raw_full_prior_artifact_body_returned"),
        "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    )

    specific_false_checks = (
        ("cross_carrier_evidence_created", "CROSS_CARRIER_EVIDENCE_CREATED"),
        ("portable_verification_closure_created", "PORTABLE_VERIFICATION_CLOSURE_CREATED"),
        ("source_transfer_occurred", "SOURCE_TRANSFER_OCCURRED"),
        ("source_receipt_occurred", "SOURCE_RECEIPT_OCCURRED"),
        ("reception_authorization_created", "RECEPTION_AUTHORIZATION_CREATED"),
        (
            "second_carrier_external_result_treated_as_cross_carrier_evidence",
            "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_CROSS_CARRIER_EVIDENCE",
        ),
        (
            "second_carrier_external_result_treated_as_portable_verification_closure",
            "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
        ),
        (
            "second_carrier_external_result_treated_as_source_transfer",
            "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_SOURCE_TRANSFER",
        ),
        (
            "second_carrier_external_result_treated_as_source_receipt",
            "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_SOURCE_RECEIPT",
        ),
        (
            "second_carrier_external_result_treated_as_reception_authorization",
            "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_RECEPTION_AUTHORIZATION",
        ),
        ("second_carrier_external_result_treated_as_source", "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_SOURCE"),
        (
            "second_carrier_external_result_treated_as_authority",
            "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_AUTHORITY",
        ),
        (
            "second_carrier_external_result_treated_as_currentness",
            "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_CURRENTNESS",
        ),
        (
            "second_carrier_external_result_treated_as_final_completion",
            "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_FINAL_COMPLETION",
        ),
        (
            "second_carrier_external_result_treated_as_runtime",
            "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_RUNTIME",
        ),
        (
            "second_carrier_external_result_treated_as_continuation",
            "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_CONTINUATION",
        ),
        (
            "second_carrier_external_result_treated_as_reusable_permission",
            "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_REUSABLE_PERMISSION",
        ),
        (
            "second_carrier_external_result_treated_as_follow_on_work",
            "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_FOLLOW_ON_WORK",
        ),
        ("zero_exit_code_treated_as_external_result_standalone", "ZERO_EXIT_CODE_TREATED_AS_EXTERNAL_RESULT"),
        ("string_zero_treated_as_external_result_standalone", "STRING_ZERO_TREATED_AS_EXTERNAL_RESULT"),
        ("ok_output_treated_as_external_result_standalone", "OK_OUTPUT_TREATED_AS_EXTERNAL_RESULT"),
        ("ran_7_tests_treated_as_cross_carrier_proof", "RAN_7_TESTS_TREATED_AS_CROSS_CARRIER_PROOF"),
        ("returned_capture_treated_as_cross_carrier_evidence", "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_PROOF"),
        ("receiving_carrier_treated_as_authority", "RECEIVING_CARRIER_TREATED_AS_AUTHORITY"),
        (
            "artifact_existence_treated_as_external_result_authority",
            "ARTIFACT_EXISTENCE_TREATED_AS_EXTERNAL_RESULT_AUTHORITY",
        ),
        ("artifact_path_treated_as_currentness", "ARTIFACT_PATH_TREATED_AS_CURRENTNESS"),
        ("source_created", "SOURCE_CREATED"),
        ("authority_created", "AUTHORITY_CREATED"),
        ("currentness_created", "CURRENTNESS_CREATED"),
        ("final_completion_claimed", "FINAL_COMPLETION_CLAIMED"),
        ("runtime_hosting_created", "RUNTIME_HOSTING_CREATED"),
        ("deployment_created", "DEPLOYMENT_CREATED"),
        ("public_release_created", "PUBLIC_RELEASE_CREATED"),
        ("operation_permission_created", "OPERATION_PERMISSION_CREATED"),
        ("continuation_authorized", "CONTINUATION_AUTHORIZED"),
        ("reusable_permission_created", "REUSABLE_PERMISSION_CREATED"),
        ("derivative_reception_authorized", "DERIVATIVE_RECEPTION_AUTHORIZED"),
        ("vessel_relation_authorized", "VESSEL_RELATION_AUTHORIZED"),
        ("another_reception_request_authorized", "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"),
        ("follow_on_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
        ("consumed_request_reopened", "CONSUMED_REQUEST_REOPENED"),
        ("authorization_token_reused", "AUTHORIZATION_TOKEN_REUSED"),
        ("prior_artifacts_mutated", "ARTIFACTS_MUTATED"),
        ("returned_capture_material_mutated", "RETURNED_CAPTURE_MATERIAL_MUTATED"),
    )
    for key, code in specific_false_checks:
        _check(
            checks,
            f"{key} remains false",
            not _as_bool(_claim_value(request, key)),
            False,
            _claim_value(request, key),
            code,
        )

    _check(
        checks,
        "first success-boundary test failure remains visible and unrepaired",
        not _as_bool(_claim_value(request, "first_success_boundary_test_repaired"))
        and not _as_bool(_claim_value(request, "first_success_boundary_test_hidden"))
        and not _as_bool(_claim_value(request, "first_success_boundary_test_claimed_passed")),
        "not repaired, not hidden, not claimed passed",
        {
            "repaired": _claim_value(request, "first_success_boundary_test_repaired"),
            "hidden": _claim_value(request, "first_success_boundary_test_hidden"),
            "claimed_passed": _claim_value(
                request, "first_success_boundary_test_claimed_passed"
            ),
        },
        "FIRST_SUCCESS_BOUNDARY_TEST_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    )
    _check(
        checks,
        "first result-boundary resolver failure remains visible and unrepaired",
        not _as_bool(_claim_value(request, "first_result_boundary_resolver_repaired"))
        and not _as_bool(_claim_value(request, "first_result_boundary_resolver_hidden"))
        and not _as_bool(_claim_value(request, "first_result_boundary_resolver_claimed_passed")),
        "not repaired, not hidden, not claimed passed",
        {
            "repaired": _claim_value(request, "first_result_boundary_resolver_repaired"),
            "hidden": _claim_value(request, "first_result_boundary_resolver_hidden"),
            "claimed_passed": _claim_value(
                request, "first_result_boundary_resolver_claimed_passed"
            ),
        },
        "FIRST_RESULT_BOUNDARY_RESOLVER_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    )
    _check(
        checks,
        "v1 packet-emission-boundary failure remains visible and unrepaired",
        not _as_bool(_claim_value(request, "v1_repaired"))
        and not _as_bool(_claim_value(request, "v1_hidden"))
        and not _as_bool(_claim_value(request, "v1_claimed_passed")),
        "not repaired, not hidden, not claimed passed",
        {
            "v1_repaired": _claim_value(request, "v1_repaired"),
            "v1_hidden": _claim_value(request, "v1_hidden"),
            "v1_claimed_passed": _claim_value(request, "v1_claimed_passed"),
        },
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    )

    non_claims = _declared_non_claims(request)
    missing_or_flipped = [
        key
        for key in REQUIRED_FALSE_NON_CLAIMS
        if key not in non_claims or non_claims[key] is not False
    ]
    _check(
        checks,
        "required non-claims explicit and false",
        not missing_or_flipped,
        {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
        {key: non_claims.get(key) for key in REQUIRED_FALSE_NON_CLAIMS},
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )

    return checks


def _statement(recorded: bool) -> dict[str, bool]:
    return {key: bool(recorded) for key in ALLOWED_TRUE_RECORDED_FIELDS}


def _non_claims_from_request(request: Mapping[str, Any]) -> dict[str, bool]:
    claims = _declared_non_claims(request)
    result: dict[str, bool] = {}
    for key in REQUIRED_FALSE_NON_CLAIMS:
        result[key] = False if claims.get(key) is False else bool(False)
    return result


def _non_meaning() -> dict[str, bool]:
    return {
        "cross_carrier_evidence_exists": False,
        "portable_verification_closure_exists": False,
        "source_transfer_occurred": False,
        "source_receipt_occurred": False,
        "reception_authorization_exists": False,
        "source_exists": False,
        "authority_exists": False,
        "currentness_exists": False,
        "final_completion_exists": False,
        "runtime_exists": False,
        "deployment_exists": False,
        "public_release_exists": False,
        "continuation_authorized": False,
        "reusable_permission_exists": False,
        "follow_on_work_authorized": False,
        "external_result_became_cross_carrier_proof": False,
        "external_result_became_portable_verification_closure": False,
        "external_result_became_source_transfer_source_receipt_reception_authorization": False,
        "external_result_became_source_authority_currentness": False,
        "external_result_artifact_became_cross_carrier_evidence": False,
        "external_result_artifact_became_portable_verification_closure": False,
        "returned_capture_became_cross_carrier_proof": False,
        "zero_exit_code_became_external_result_automatically": False,
        "string_zero_became_external_result_automatically": False,
        "string_zero_became_doctrine": False,
        "ok_became_external_result_automatically": False,
        "ran_7_tests_became_cross_carrier_proof": False,
        "macbook_pro_became_authority": False,
        "macbook_air_became_source": False,
        "artifact_existence_became_external_result_authority": False,
        "artifact_path_became_currentness": False,
        "repo_local_availability_became_external_result_authority": False,
        "hidden_repo_state_became_external_result_authority": False,
        "first_success_boundary_test_repaired_hidden_erased_or_claimed_passed": False,
        "first_result_boundary_resolver_repaired_hidden_erased_or_claimed_passed": False,
        "v1_packet_emission_boundary_resolver_repaired_hidden_erased_or_claimed_passed": False,
    }


def _additional_basis_required(
    outcome: str, request: Mapping[str, Any]
) -> dict[str, Any]:
    required = outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    return {
        "required": required,
        "missing_or_unclear_basis": _sanitize(
            request.get("additional_basis_context", []) if required else []
        ),
        "missing_basis_scheduled": False,
        "missing_basis_authorized": False,
        "missing_basis_executed": False,
        "cross_carrier_evidence_created": False,
        "portable_verification_closure_created": False,
        "source_authority_currentness_final_completion_runtime_follow_on_created": False,
    }


def _not_recorded_basis(outcome: str, request: Mapping[str, Any]) -> dict[str, Any]:
    not_recorded = outcome == OUTCOME_NOT_RECORDED
    return {
        "not_recorded": not_recorded,
        "basis": _sanitize(request.get("not_recorded_basis", []) if not_recorded else []),
        "reason": _sanitize(request.get("not_recorded_basis")) if not_recorded else None,
        "prior_artifacts_mutated": False,
        "returned_capture_material_mutated": False,
        "next_work_authorized": False,
    }


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": list(WHAT_REMAINS_OPEN_ITEMS),
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }


def _block(code: str | None, reason: str | None = None) -> dict[str, Any] | None:
    if not code:
        return None
    public_code = code if code in BLOCK_CODES else "DECLARED_SECOND_CARRIER_EXTERNAL_RESULT_REQUEST_MALFORMED"
    return {
        "blocked": True,
        "block_code": public_code,
        "block_reason": reason or public_code,
    }


def _basis_sections(request: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
    sections: dict[str, dict[str, Any]] = {}
    for key in SELECTED_BASIS_KEYS:
        sections[key] = _reference_section(
            key,
            request.get(key),
            _selected_basis_extras(key, request),
        )
    return sections


def _posture_sections(request: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
    return {key: _posture_section(key, request) for key in POSTURE_KEYS}


def _scope_section(request: Mapping[str, Any]) -> dict[str, Any]:
    values = _scope_values(request.get("second_carrier_external_result_scope"))
    return {
        "declared_scope_values": values,
        "supported_scope_values": list(SUPPORTED_SCOPE_VALUES),
        "unsupported_scope_values": _unsupported_scope_values(request),
        "unsupported_scope_values_blocked": not _unsupported_scope_values(request),
        "official_enum_scope_strings_not_redacted": True,
    }


def _declared_question_section(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "second_carrier_external_result_request_id": _request_id(request),
        "second_carrier_external_result_question": _sanitize(
            request.get("second_carrier_external_result_question")
        ),
        "expected_second_carrier_external_result_question": CORE_QUESTION,
        "second_carrier_external_result_intent": _sanitize(
            request.get("second_carrier_external_result_intent")
        ),
    }


def _metadata(request: Mapping[str, Any]) -> dict[str, Any]:
    request_id = _request_id(request)
    return {
        "portable_source_body_verification_second_carrier_external_result_id": request_id,
        "portable_source_body_verification_second_carrier_external_result_type": RESULT_TYPE,
        "portable_source_body_verification_second_carrier_external_result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
    }


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: Sequence[Mapping[str, Any]],
    block_code: str | None = None,
    block_reason: str | None = None,
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    result: dict[str, Any] = {
        "portable_source_body_verification_second_carrier_external_result_metadata": _metadata(
            request
        ),
        "declared_second_carrier_external_result_question": _declared_question_section(
            request
        ),
    }
    result.update(_basis_sections(request))
    result.update(_posture_sections(request))
    result["second_carrier_external_result_scope"] = _scope_section(request)
    result["second_carrier_external_result_checks"] = _sanitize(list(checks))
    result["second_carrier_external_result_statement"] = _statement(recorded)
    result["second_carrier_external_result_non_meaning"] = _non_meaning()
    result["additional_basis_required"] = _additional_basis_required(outcome, request)
    result["not_recorded_basis"] = _not_recorded_basis(outcome, request)
    result["what_remains_open"] = _what_remains_open()
    result["non_claims"] = _non_claims_from_request(request)
    result["outcome"] = outcome
    result["block"] = _block(block_code, block_reason)
    result[
        "portable_source_body_verification_second_carrier_external_result_summary"
    ] = build_portable_source_body_verification_second_carrier_external_result_summary(
        result
    )
    return result


def _malformed_result(code: str, reason: str) -> dict[str, Any]:
    request = {
        "second_carrier_external_result_request_id": "malformed_second_carrier_external_result_request",
        "second_carrier_external_result_question": None,
        "second_carrier_external_result_intent": None,
        "second_carrier_external_result_scope": [],
        "declared_non_claims": {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
    }
    checks: list[dict[str, Any]] = []
    _check(
        checks,
        "declared second-carrier external-result request malformed",
        False,
        "JSON object mapping with declared second-carrier external-result request",
        reason,
        code,
    )
    return _build_result(request, OUTCOME_BLOCKED, checks, code, reason)


def resolve_portable_source_body_verification_second_carrier_external_result(
    declared_second_carrier_external_result_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded second-carrier external-result posture."""

    if declared_second_carrier_external_result_request is None:
        return _malformed_result(
            "DECLARED_SECOND_CARRIER_EXTERNAL_RESULT_REQUEST_MALFORMED",
            "declared request is missing",
        )
    if not isinstance(declared_second_carrier_external_result_request, Mapping):
        return _malformed_result(
            "DECLARED_SECOND_CARRIER_EXTERNAL_RESULT_REQUEST_MALFORMED",
            "declared request must be a mapping",
        )

    request = copy.deepcopy(dict(declared_second_carrier_external_result_request))
    checks = _evaluate_checks(request)
    failed = _failed_checks(checks)
    requested_outcome = request.get("requested_second_carrier_external_result_outcome")
    intent = request.get("second_carrier_external_result_intent")

    if failed:
        code = _first_failed_code(checks)
        return _build_result(
            request,
            OUTCOME_BLOCKED,
            checks,
            code,
            f"blocked by failed check: {code}",
        )

    if intent == INTENT_BLOCK or requested_outcome == OUTCOME_BLOCKED:
        requested_code = request.get("block_reason")
        code = requested_code if requested_code in BLOCK_CODES else "SECOND_CARRIER_EXTERNAL_RESULT_INTENT_UNSUPPORTED"
        return _build_result(
            request,
            OUTCOME_BLOCKED,
            checks,
            code,
            "declared request selected blocked posture",
        )

    if intent == INTENT_DO_NOT_RECORD or requested_outcome == OUTCOME_NOT_RECORDED:
        return _build_result(request, OUTCOME_NOT_RECORDED, checks)

    if requested_outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        return _build_result(request, OUTCOME_REQUIRES_ADDITIONAL_BASIS, checks)

    return _build_result(request, OUTCOME_RECORDED, checks)


def resolve_portable_source_body_verification_second_carrier_external_result_from_path(
    declared_second_carrier_external_result_request_path: Path | str,
) -> dict[str, Any]:
    """Load a declared request JSON object from path and resolve it."""

    path = Path(declared_second_carrier_external_result_request_path)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise PortableSourceBodyVerificationSecondCarrierExternalResultError(
            f"declared request path is unreadable: {path}"
        ) from exc
    try:
        loaded = json.loads(text)
    except json.JSONDecodeError as exc:
        raise PortableSourceBodyVerificationSecondCarrierExternalResultError(
            f"declared request path contains malformed JSON: {path}"
        ) from exc
    if not isinstance(loaded, Mapping):
        return _malformed_result(
            "DECLARED_SECOND_CARRIER_EXTERNAL_RESULT_REQUEST_MALFORMED",
            "declared request JSON must be an object",
        )
    return resolve_portable_source_body_verification_second_carrier_external_result(
        loaded
    )


def _safe_filename_part(value: Any) -> str:
    text = str(value or DEFAULT_REQUEST_ID)
    cleaned = []
    for char in text:
        if char.isalnum() or char in {"_", "-", "."}:
            cleaned.append(char)
        else:
            cleaned.append("_")
    return "".join(cleaned).strip("_") or DEFAULT_REQUEST_ID


def _deduplicated_path(path: Path) -> Path:
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


def write_portable_source_body_verification_second_carrier_external_result_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a bounded result artifact without overwriting an existing file."""

    if not isinstance(result, Mapping):
        raise PortableSourceBodyVerificationSecondCarrierExternalResultError(
            "result must be a mapping"
        )
    if output_path is None:
        metadata = result.get(
            "portable_source_body_verification_second_carrier_external_result_metadata",
            {},
        )
        if isinstance(metadata, Mapping):
            request_id = metadata.get(
                "portable_source_body_verification_second_carrier_external_result_id",
                DEFAULT_REQUEST_ID,
            )
        else:
            request_id = DEFAULT_REQUEST_ID
        filename = (
            f"{_safe_filename_part(request_id)}__"
            "portable_source_body_verification_second_carrier_external_result_result.json"
        )
        target = OUTPUT_ROOT / filename
    else:
        target = Path(output_path)

    target = _deduplicated_path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(_sanitize(dict(result)), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return target


def build_portable_source_body_verification_second_carrier_external_result_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact bounded summary from a result artifact."""

    checks = result.get("second_carrier_external_result_checks", [])
    if not isinstance(checks, Sequence) or isinstance(checks, (str, bytes, bytearray)):
        checks = []
    failed_count = len(_failed_checks(checks))  # type: ignore[arg-type]
    passed_count = len(checks) - failed_count
    metadata = result.get(
        "portable_source_body_verification_second_carrier_external_result_metadata",
        {},
    )
    question = result.get("declared_second_carrier_external_result_question", {})
    statement = result.get("second_carrier_external_result_statement", {})
    non_claims = result.get("non_claims", {})
    block = result.get("block") or {}
    boundary_basis = result.get("selected_second_carrier_external_result_boundary_basis", {})
    verification_basis = result.get("selected_second_carrier_verification_basis", {})
    returned_basis = result.get("selected_returned_capture_material_basis", {})
    boundary_shortcuts = (
        boundary_basis.get("selected_basis_shortcut_fields", {})
        if isinstance(boundary_basis, Mapping)
        else {}
    )
    verification_shortcuts = (
        verification_basis.get("selected_basis_shortcut_fields", {})
        if isinstance(verification_basis, Mapping)
        else {}
    )
    returned_shortcuts = (
        returned_basis.get("selected_basis_shortcut_fields", {})
        if isinstance(returned_basis, Mapping)
        else {}
    )

    summary = {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") if isinstance(block, Mapping) else None,
        "block_reason": block.get("block_reason") if isinstance(block, Mapping) else None,
        "request_id": metadata.get(
            "portable_source_body_verification_second_carrier_external_result_id"
        )
        if isinstance(metadata, Mapping)
        else None,
        "question": question.get("second_carrier_external_result_question")
        if isinstance(question, Mapping)
        else None,
        "intent": question.get("second_carrier_external_result_intent")
        if isinstance(question, Mapping)
        else None,
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": metadata.get(
            "portable_source_body_verification_second_carrier_external_result_version"
        )
        if isinstance(metadata, Mapping)
        else RESULT_VERSION,
        "resolver_module": metadata.get("resolver_module")
        if isinstance(metadata, Mapping)
        else RESOLVER_MODULE,
    }
    for key in ALLOWED_TRUE_RECORDED_FIELDS:
        summary[key] = statement.get(key) if isinstance(statement, Mapping) else False

    summary.update(
        {
            "selected_external_result_boundary_outcome": boundary_shortcuts.get(
                "selected_second_carrier_external_result_boundary_result_outcome"
            )
            if isinstance(boundary_shortcuts, Mapping)
            else None,
            "selected_external_result_boundary_version": boundary_shortcuts.get(
                "selected_second_carrier_external_result_boundary_result_version"
            )
            if isinstance(boundary_shortcuts, Mapping)
            else None,
            "selected_external_result_boundary_failed_check_count": boundary_shortcuts.get(
                "selected_second_carrier_external_result_boundary_failed_check_count"
            )
            if isinstance(boundary_shortcuts, Mapping)
            else None,
            "selected_second_carrier_verification_outcome": verification_shortcuts.get(
                "selected_second_carrier_verification_result_outcome"
            )
            if isinstance(verification_shortcuts, Mapping)
            else None,
            "selected_second_carrier_verification_version": verification_shortcuts.get(
                "selected_second_carrier_verification_result_version"
            )
            if isinstance(verification_shortcuts, Mapping)
            else None,
            "selected_second_carrier_verification_failed_check_count": verification_shortcuts.get(
                "selected_second_carrier_verification_failed_check_count"
            )
            if isinstance(verification_shortcuts, Mapping)
            else None,
            "selected_returned_capture_intake_path": returned_shortcuts.get(
                "selected_returned_capture_intake_path"
            )
            if isinstance(returned_shortcuts, Mapping)
            else None,
            "selected_returned_capture_zip_path": returned_shortcuts.get(
                "selected_returned_capture_zip_path"
            )
            if isinstance(returned_shortcuts, Mapping)
            else None,
            "selected_returned_capture_hash_path": returned_shortcuts.get(
                "selected_returned_capture_hash_path"
            )
            if isinstance(returned_shortcuts, Mapping)
            else None,
            "selected_returned_capture_extracted_directory_path": returned_shortcuts.get(
                "selected_returned_capture_extracted_directory_path"
            )
            if isinstance(returned_shortcuts, Mapping)
            else None,
            "selected_returned_capture_exit_code": returned_shortcuts.get(
                "selected_returned_capture_exit_code"
            )
            if isinstance(returned_shortcuts, Mapping)
            else None,
            "selected_returned_capture_declared_exit_code": returned_shortcuts.get(
                "selected_returned_capture_declared_exit_code"
            )
            if isinstance(returned_shortcuts, Mapping)
            else None,
            "selected_returned_capture_ok_line": returned_shortcuts.get(
                "selected_returned_capture_ok_line"
            )
            if isinstance(returned_shortcuts, Mapping)
            else None,
            "no_cross_carrier_evidence": non_claims.get(
                "cross_carrier_evidence_created"
            )
            is False
            if isinstance(non_claims, Mapping)
            else True,
            "no_portable_verification_closure": non_claims.get(
                "portable_verification_closure_created"
            )
            is False
            if isinstance(non_claims, Mapping)
            else True,
            "no_source_authority_currentness_final_completion_runtime": all(
                non_claims.get(key) is False
                for key in (
                    "source_created",
                    "authority_created",
                    "currentness_created",
                    "final_completion_claimed",
                    "runtime_hosting_created",
                )
            )
            if isinstance(non_claims, Mapping)
            else True,
            "no_deployment_public_release_follow_on": all(
                non_claims.get(key) is False
                for key in (
                    "deployment_created",
                    "public_release_created",
                    "follow_on_work_authorized",
                )
            )
            if isinstance(non_claims, Mapping)
            else True,
            "key_non_claims": _sanitize(non_claims),
            "first_success_boundary_test_preserved_as_failed_predecessor": statement.get(
                "first_success_boundary_test_failure_preserved", False
            )
            if isinstance(statement, Mapping)
            else False,
            "v1_predecessor_failure_preserved": non_claims.get("v1_repaired") is False
            if isinstance(non_claims, Mapping)
            else True,
            "v1_not_repaired": non_claims.get("v1_repaired") is False
            if isinstance(non_claims, Mapping)
            else True,
            "v1_not_hidden": non_claims.get("v1_hidden") is False
            if isinstance(non_claims, Mapping)
            else True,
            "v1_not_claimed_passed": non_claims.get("v1_claimed_passed") is False
            if isinstance(non_claims, Mapping)
            else True,
            "first_result_boundary_resolver_preserved_as_failed_predecessor": statement.get(
                "first_result_boundary_resolver_failure_preserved", False
            )
            if isinstance(statement, Mapping)
            else False,
        }
    )
    return _sanitize(summary)


def _default_basis(name: str) -> dict[str, Any]:
    return {
        "basis_id": name,
        "basis_declared": True,
        "reference_shape": True,
        "basis_only": True,
    }


def build_declared_portable_source_body_verification_second_carrier_external_result_request(
    second_carrier_external_result_request_id: str = DEFAULT_REQUEST_ID,
    **overrides: Any,
) -> dict[str, Any]:
    """Build a clean declared request for one bounded external-result posture."""

    request: dict[str, Any] = {
        "second_carrier_external_result_request_id": second_carrier_external_result_request_id,
        "second_carrier_external_result_question": CORE_QUESTION,
        "second_carrier_external_result_intent": INTENT_RECORD,
        "requested_second_carrier_external_result_outcome": OUTCOME_RECORDED,
        "second_carrier_external_result_scope": list(SUPPORTED_SCOPE_VALUES),
        "declared_non_claims": {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
        "reference_shaped_input_posture": True,
        "additional_basis_context": [],
        "not_recorded_basis": [],
        "selected_second_carrier_external_result_boundary_basis": {
            **_default_basis("selected_second_carrier_external_result_boundary_basis"),
            "outcome": EXPECTED_BOUNDARY_OUTCOME,
            "result_version": RESULT_VERSION,
            "failed_check_count": 0,
            "one_future_second_carrier_external_result_step_declared": True,
        },
        "selected_second_carrier_external_result_boundary_terminal_summary_basis": {
            **_default_basis(
                "selected_second_carrier_external_result_boundary_terminal_summary_basis"
            ),
            "path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TERMINAL_SUMMARY_V0.md",
        },
        "selected_second_carrier_verification_basis": {
            **_default_basis("selected_second_carrier_verification_basis"),
            "outcome": EXPECTED_VERIFICATION_OUTCOME,
            "result_version": RESULT_VERSION,
            "failed_check_count": 0,
            "bounded_verification_recorded": True,
        },
        "selected_second_carrier_verification_terminal_summary_basis": {
            **_default_basis("selected_second_carrier_verification_terminal_summary_basis"),
            "path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_VERIFICATION_TERMINAL_SUMMARY_V0.md",
        },
        "selected_second_carrier_verification_boundary_basis": {
            **_default_basis("selected_second_carrier_verification_boundary_basis"),
            "outcome": EXPECTED_VERIFICATION_BOUNDARY_OUTCOME,
            "failed_check_count": 0,
        },
        "selected_second_carrier_success_basis": {
            **_default_basis("selected_second_carrier_success_basis"),
            "outcome": EXPECTED_SUCCESS_OUTCOME,
            "failed_check_count": 0,
        },
        "selected_second_carrier_result_basis": {
            **_default_basis("selected_second_carrier_result_basis"),
            "outcome": EXPECTED_RESULT_OUTCOME,
            "failed_check_count": 0,
        },
        "selected_second_carrier_result_terminal_summary_basis": {
            **_default_basis("selected_second_carrier_result_terminal_summary_basis"),
            "path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RESULT_TERMINAL_SUMMARY_V0.md",
        },
        "selected_returned_second_carrier_live_capture_intake_basis": {
            **_default_basis("selected_returned_second_carrier_live_capture_intake_basis"),
            "path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_RETURNED_SECOND_CARRIER_LIVE_CAPTURE_INTAKE_V0.md",
            "preserved": True,
            "capture_only": True,
        },
        "selected_returned_capture_material_basis": {
            **_default_basis("selected_returned_capture_material_basis"),
            "returned_capture_preserved": True,
            "capture_result_success_verification_external_result_basis_only": True,
        },
        "selected_second_carrier_output_capture_basis": {
            **_default_basis("selected_second_carrier_output_capture_basis"),
            "outcome": EXPECTED_OUTPUT_CAPTURE_OUTCOME,
            "failed_check_count": 0,
        },
    }
    for key in (
        "selected_packet_transfer_basis",
        "selected_packet_emission_basis",
        "selected_packet_emission_boundary_v2_basis",
        "selected_packet_emission_boundary_v1_predecessor_failure_basis",
        "selected_packet_artifact_basis",
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
    ):
        request[key] = _default_basis(key)
    for key in POSTURE_KEYS:
        request[key] = {
            "declared": True,
            "request_declared": True,
            "bounded_second_carrier_external_result_posture_only": True,
        }

    request.update(
        {
            "selected_second_carrier_external_result_boundary_result_path": (
                "artifacts/"
                "integrity_host_v0_min_coexistence_portable_source_body_verification_"
                "second_carrier_external_result_boundary/"
                "portable_source_body_verification_second_carrier_external_result_boundary_"
                "reference_review_001__portable_source_body_verification_"
                "second_carrier_external_result_boundary_result.json"
            ),
            "selected_second_carrier_external_result_boundary_result_outcome": EXPECTED_BOUNDARY_OUTCOME,
            "selected_second_carrier_external_result_boundary_result_version": RESULT_VERSION,
            "selected_second_carrier_external_result_boundary_failed_check_count": 0,
            "selected_second_carrier_external_result_boundary_declared_future_external_result_step": True,
            "selected_second_carrier_external_result_boundary_already_created_external_result": False,
            "selected_second_carrier_external_result_boundary_already_created_cross_carrier_evidence": False,
            "selected_second_carrier_external_result_boundary_already_created_portable_verification_closure": False,
            "selected_second_carrier_external_result_boundary_treated_external_result_boundary_as_external_result": False,
            "selected_second_carrier_external_result_boundary_treated_external_result_boundary_as_cross_carrier_evidence": False,
            "selected_second_carrier_external_result_boundary_treated_external_result_boundary_as_portable_verification_closure": False,
            "selected_second_carrier_external_result_boundary_zero_exit_code_not_external_result": True,
            "selected_second_carrier_external_result_boundary_string_zero_not_external_result": True,
            "selected_second_carrier_external_result_boundary_ok_not_external_result": True,
            "selected_second_carrier_external_result_boundary_ran_7_tests_not_cross_carrier_proof": True,
            "selected_second_carrier_external_result_boundary_official_enum_scope_strings_redacted": False,
            "selected_second_carrier_external_result_boundary_first_success_boundary_test_failure_preserved": True,
            "selected_second_carrier_verification_result_path": (
                "artifacts/"
                "integrity_host_v0_min_coexistence_portable_source_body_verification_"
                "second_carrier_verification/"
                "portable_source_body_verification_second_carrier_verification_"
                "reference_review_001__portable_source_body_verification_"
                "second_carrier_verification_result.json"
            ),
            "selected_second_carrier_verification_result_outcome": EXPECTED_VERIFICATION_OUTCOME,
            "selected_second_carrier_verification_result_version": RESULT_VERSION,
            "selected_second_carrier_verification_failed_check_count": 0,
            "selected_second_carrier_verification_bounded_verification_recorded": True,
            "selected_second_carrier_verification_treated_verification_as_external_result": False,
            "selected_second_carrier_verification_treated_verification_as_cross_carrier_evidence": False,
            "selected_second_carrier_verification_zero_exit_code_not_external_result": True,
            "selected_second_carrier_verification_string_zero_not_external_result": True,
            "selected_second_carrier_verification_ok_not_external_result": True,
            "selected_second_carrier_verification_ran_7_tests_not_cross_carrier_proof": True,
            "selected_second_carrier_verification_boundary_result_path": (
                "artifacts/integrity_host_v0_min_coexistence_portable_source_body_"
                "verification_second_carrier_verification_boundary/"
                "portable_source_body_verification_second_carrier_verification_"
                "boundary_result.json"
            ),
            "selected_second_carrier_verification_boundary_result_outcome": EXPECTED_VERIFICATION_BOUNDARY_OUTCOME,
            "selected_second_carrier_verification_boundary_failed_check_count": 0,
            "selected_second_carrier_success_result_path": (
                "artifacts/integrity_host_v0_min_coexistence_portable_source_body_"
                "verification_second_carrier_success/"
                "portable_source_body_verification_second_carrier_success_result.json"
            ),
            "selected_second_carrier_success_result_outcome": EXPECTED_SUCCESS_OUTCOME,
            "selected_second_carrier_success_failed_check_count": 0,
            "selected_second_carrier_result_result_path": (
                "artifacts/integrity_host_v0_min_coexistence_portable_source_body_"
                "verification_second_carrier_result/"
                "portable_source_body_verification_second_carrier_result_result.json"
            ),
            "selected_second_carrier_result_result_outcome": EXPECTED_RESULT_OUTCOME,
            "selected_second_carrier_result_failed_check_count": 0,
            "selected_returned_capture_intake_path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_RETURNED_SECOND_CARRIER_LIVE_CAPTURE_INTAKE_V0.md",
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
            "selected_returned_capture_working_directory": (
                "/Users/markomarkota/Desktop/IAMMAI-SYSTEM"
            ),
            "selected_returned_capture_started_at": "2026-05-09T11:34:26Z",
            "selected_returned_capture_completed_at": "2026-05-09T11:34:27Z",
            "selected_returned_capture_exit_code": 0,
            "selected_returned_capture_declared_exit_code": "0",
            "selected_returned_capture_ran_7_tests_line": "Ran 7 tests in 0.451s",
            "selected_returned_capture_ok_line": "OK",
            "selected_returned_capture_raw_placeholder_carrier_label": "raw-placeholder-carrier-label",
            "selected_returned_capture_raw_placeholder_carrier_type": "raw-placeholder-carrier-type",
            "selected_returned_capture_placeholder_fields_unrepaired": True,
            "selected_second_carrier_output_capture_result_path": (
                "artifacts/integrity_host_v0_min_coexistence_portable_source_body_"
                "verification_second_carrier_output_capture/"
                "portable_source_body_verification_second_carrier_output_capture_result.json"
            ),
            "selected_second_carrier_output_capture_result_outcome": EXPECTED_OUTPUT_CAPTURE_OUTCOME,
            "selected_second_carrier_output_capture_failed_check_count": 0,
        }
    )

    request.update(copy.deepcopy(overrides))
    return request
