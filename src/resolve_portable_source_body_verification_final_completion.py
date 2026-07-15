"""Bounded portable source-body verification final-completion resolver.

This resolver is downstream of the final-completion-boundary line. It records
one bounded line-level final-completion posture only. Final completion here is
not source transfer, source receipt, reception authorization, source,
authority, currentness, runtime, deployment, public release, operation
permission, continuation, reusable permission, adoption, receiving-context
governance, publication flow, or follow-on work.

The resolver is self-contained, imports no repo-local modules, runs no
subprocesses, performs no network access, and mutates no upstream artifact. It
keeps official enum, scope, outcome, block-code, posture, non-claim, and
boolean field strings unredacted while containing hostile raw body payloads.
"""

from __future__ import annotations

import copy
import datetime
import json
from collections.abc import Iterable as IterableABC
from collections.abc import Mapping as MappingABC
from pathlib import Path
from typing import Any, Iterable, Mapping


class PortableSourceBodyVerificationFinalCompletionError(Exception):
    """Raised for bounded final-completion path and serialization failures."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_portable_source_body_verification_final_completion"
RESULT_TYPE = "portable_source_body_verification_final_completion"
DEFAULT_REQUEST_ID = (
    "portable_source_body_verification_final_completion_reference_review_001"
)
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_portable_source_body_verification_"
    "final_completion"
)

CORE_QUESTION = (
    "Can the clean final-completion-boundary basis be used to record one "
    "bounded final-completion posture for this portable source-body "
    "verification line without creating source transfer, source receipt, "
    "reception authorization, source, authority, currentness, runtime, "
    "deployment, public release, operation permission, continuation, reusable "
    "permission, derivative reception, vessel relation, another reception "
    "request, adoption, receiving-context governance, publication flow, or "
    "follow-on work?"
)

OUTCOME_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_RECORDED"
OUTCOME_NOT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION"
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION"
)
INTENT_BLOCK = "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

EXPECTED_FINAL_COMPLETION_BOUNDARY_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_BOUNDARY_RECORDED"
)
EXPECTED_PORTABLE_VERIFICATION_CLOSURE_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_PORTABLE_VERIFICATION_CLOSURE_RECORDED"
)
EXPECTED_CROSS_CARRIER_EVIDENCE_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_CROSS_CARRIER_EVIDENCE_RECORDED"
)
EXPECTED_SECOND_CARRIER_EXTERNAL_RESULT_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT_RECORDED"
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
    "FINAL_COMPLETION_SPEC_ONLY",
    "ONE_BOUNDED_FINAL_COMPLETION_RECORDED",
    "FINAL_COMPLETION_BOUNDARY_BASIS_PRESERVED",
    "PORTABLE_VERIFICATION_CLOSURE_BASIS_PRESERVED",
    "PORTABLE_VERIFICATION_CLOSURE_ARTIFACT_BASIS_PRESERVED",
    "CROSS_CARRIER_EVIDENCE_BASIS_PRESERVED",
    "RETURNED_SECOND_CARRIER_CAPTURE_BASIS_PRESERVED",
    "CAPTURE_INTAKE_BASIS_PRESERVED",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_PRESERVED",
    "FINAL_COMPLETION_RECORDED_BOUNDED",
    "FINAL_COMPLETION_ARTIFACT_RECORDED_OR_BOUNDED",
    "FINAL_COMPLETION_NOT_SOURCE_TRANSFER",
    "FINAL_COMPLETION_NOT_SOURCE_RECEIPT",
    "FINAL_COMPLETION_NOT_RECEPTION_AUTHORIZATION",
    "FINAL_COMPLETION_NOT_SOURCE",
    "FINAL_COMPLETION_NOT_AUTHORITY",
    "FINAL_COMPLETION_NOT_CURRENTNESS",
    "FINAL_COMPLETION_NOT_RUNTIME",
    "FINAL_COMPLETION_NOT_DEPLOYMENT",
    "FINAL_COMPLETION_NOT_PUBLIC_RELEASE",
    "FINAL_COMPLETION_NOT_OPERATION_PERMISSION",
    "ZERO_EXIT_CODE_NOT_FINAL_COMPLETION_AS_STANDALONE_INFERENCE",
    "STRING_ZERO_NOT_FINAL_COMPLETION_AS_STANDALONE_INFERENCE",
    "OK_OUTPUT_NOT_FINAL_COMPLETION_AS_STANDALONE_INFERENCE",
    "RAN_7_TESTS_NOT_FINAL_COMPLETION_AS_STANDALONE_INFERENCE",
    "RETURNED_CAPTURE_NOT_FINAL_COMPLETION_AS_STANDALONE_INFERENCE",
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
    "NO_SOURCE_INFERENCE",
    "NO_AUTHORITY_INFERENCE",
    "NO_CURRENTNESS_INFERENCE",
    "NO_RUNTIME_INFERENCE",
    "NO_DEPLOYMENT_INFERENCE",
    "NO_PUBLIC_RELEASE_INFERENCE",
    "NO_OPERATION_PERMISSION_INFERENCE",
    "NO_FOLLOW_ON_WORK_INFERENCE",
    "NO_UNBOUNDED_PASS_FAIL_INFERENCE",
    "HIDDEN_REPO_STATE_EXCLUDED",
    "HIDDEN_REPO_STATE_NOT_USED_AS_FINAL_COMPLETION_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_NOT_FINAL_COMPLETION_AUTHORITY",
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
SUPPORTED_FINAL_COMPLETION_SCOPE = SUPPORTED_SCOPE_VALUES

REQUIRED_FALSE_NON_CLAIMS = (
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "final_completion_treated_as_source_transfer",
    "final_completion_treated_as_source_receipt",
    "final_completion_treated_as_reception_authorization",
    "final_completion_treated_as_source",
    "final_completion_treated_as_authority",
    "final_completion_treated_as_currentness",
    "final_completion_treated_as_runtime",
    "final_completion_treated_as_deployment",
    "final_completion_treated_as_public_release",
    "final_completion_treated_as_operation_permission",
    "final_completion_treated_as_continuation",
    "final_completion_treated_as_reusable_permission",
    "final_completion_treated_as_follow_on_work",
    "zero_exit_code_treated_as_final_completion_standalone",
    "string_zero_treated_as_final_completion_standalone",
    "string_zero_representation_turned_into_doctrine",
    "ok_output_treated_as_final_completion_standalone",
    "ran_7_tests_treated_as_final_completion_standalone",
    "returned_capture_treated_as_final_completion_standalone",
    "receiving_carrier_treated_as_authority",
    "artifact_existence_treated_as_final_completion_authority",
    "artifact_path_treated_as_currentness",
    "repo_local_availability_treated_as_final_completion_authority",
    "hidden_repo_state_used_as_final_completion_content",
    "hidden_repo_state_used_as_final_completion_authority",
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

ALLOWED_TRUE_RECORDED_FIELDS = (
    "final_completion_recorded",
    "bounded_final_completion_recorded",
    "final_completion_artifact_recorded_or_bounded",
    "final_completion_boundary_basis_preserved",
    "portable_verification_closure_basis_preserved",
    "portable_verification_closure_artifact_basis_preserved",
    "cross_carrier_evidence_basis_preserved",
    "returned_second_carrier_capture_basis_preserved",
    "capture_intake_basis_preserved",
    "second_carrier_output_capture_basis_preserved",
    "final_completion_recorded_bounded",
    "final_completion_not_source_transfer",
    "final_completion_not_source_receipt",
    "final_completion_not_reception_authorization",
    "final_completion_not_source",
    "final_completion_not_authority",
    "final_completion_not_currentness",
    "final_completion_not_runtime",
    "final_completion_not_deployment",
    "final_completion_not_public_release",
    "final_completion_not_operation_permission",
    "zero_exit_code_not_final_completion_as_standalone_inference",
    "string_zero_not_final_completion_as_standalone_inference",
    "ok_output_not_final_completion_as_standalone_inference",
    "ran_7_tests_not_final_completion_as_standalone_inference",
    "returned_capture_not_final_completion_as_standalone_inference",
    "receiving_carrier_not_authority",
    "source_not_created",
    "authority_not_created",
    "currentness_not_created",
    "runtime_not_created",
    "deployment_not_created",
    "public_release_not_created",
    "operation_permission_not_created",
    "continuation_not_authorized",
    "reusable_permission_not_created",
    "follow_on_work_not_authorized",
    "hidden_repo_state_excluded",
    "hidden_repo_state_not_used_as_final_completion_authority",
    "repo_local_availability_not_final_completion_authority",
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

BLOCK_CODES = (
    "DECLARED_FINAL_COMPLETION_REQUEST_MALFORMED",
    "DECLARED_FINAL_COMPLETION_REQUEST_UNREADABLE",
    "FINAL_COMPLETION_REQUEST_DECLARED_BLOCK",
    "FINAL_COMPLETION_QUESTION_UNDECLARED",
    "FINAL_COMPLETION_INTENT_UNSUPPORTED",
    "FINAL_COMPLETION_BOUNDARY_BASIS_MISSING",
    "FINAL_COMPLETION_BOUNDARY_NOT_RECORDED",
    "FINAL_COMPLETION_BOUNDARY_FAILED_CHECKS_PRESENT",
    "FINAL_COMPLETION_BOUNDARY_VERSION_NOT_0_1_0",
    "FINAL_COMPLETION_BOUNDARY_DID_NOT_DECLARE_FUTURE_FINAL_COMPLETION_REVIEW_STEP",
    "FINAL_COMPLETION_BOUNDARY_ALREADY_CREATED_FINAL_COMPLETION",
    "FINAL_COMPLETION_BOUNDARY_TREATED_BOUNDARY_AS_FINAL_COMPLETION",
    "FINAL_COMPLETION_BOUNDARY_TREATED_ZERO_EXIT_CODE_AS_FINAL_COMPLETION",
    "FINAL_COMPLETION_BOUNDARY_TREATED_STRING_ZERO_AS_FINAL_COMPLETION",
    "FINAL_COMPLETION_BOUNDARY_TREATED_STRING_ZERO_AS_DOCTRINE",
    "FINAL_COMPLETION_BOUNDARY_TREATED_OK_AS_FINAL_COMPLETION",
    "FINAL_COMPLETION_BOUNDARY_TREATED_RAN_7_TESTS_AS_FINAL_COMPLETION",
    "FINAL_COMPLETION_BOUNDARY_TREATED_RETURNED_CAPTURE_AS_FINAL_COMPLETION",
    "FINAL_COMPLETION_BOUNDARY_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
    "PREDECESSOR_CROSS_CARRIER_EVIDENCE_FAILURE_MISSING_OR_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
    "PREDECESSOR_EXTERNAL_RESULT_V1_FAILURE_MISSING_OR_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
    "PORTABLE_VERIFICATION_CLOSURE_BASIS_MISSING",
    "PORTABLE_VERIFICATION_CLOSURE_NOT_RECORDED",
    "PORTABLE_VERIFICATION_CLOSURE_FAILED_CHECKS_PRESENT",
    "PORTABLE_VERIFICATION_CLOSURE_ALREADY_CREATED_FINAL_COMPLETION",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_FINAL_COMPLETION",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_SOURCE",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_AUTHORITY",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_CURRENTNESS",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_RUNTIME",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_DEPLOYMENT",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_PUBLIC_RELEASE",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_OPERATION_PERMISSION",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_FOLLOW_ON_WORK",
    "CROSS_CARRIER_EVIDENCE_BASIS_MISSING",
    "CROSS_CARRIER_EVIDENCE_NOT_RECORDED",
    "CROSS_CARRIER_EVIDENCE_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_EXTERNAL_RESULT_BASIS_MISSING",
    "SECOND_CARRIER_EXTERNAL_RESULT_NOT_RECORDED",
    "SECOND_CARRIER_EXTERNAL_RESULT_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_VERIFICATION_BASIS_MISSING",
    "SECOND_CARRIER_VERIFICATION_NOT_RECORDED",
    "SECOND_CARRIER_SUCCESS_BASIS_MISSING",
    "SECOND_CARRIER_SUCCESS_NOT_RECORDED",
    "SECOND_CARRIER_RESULT_BASIS_MISSING",
    "SECOND_CARRIER_RESULT_NOT_RECORDED",
    "RETURNED_CAPTURE_INTAKE_BASIS_MISSING",
    "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
    "RETURNED_CAPTURE_TREATED_AS_FINAL_COMPLETION",
    "ZERO_EXIT_CODE_TREATED_AS_FINAL_COMPLETION",
    "STRING_ZERO_TREATED_AS_FINAL_COMPLETION",
    "STRING_ZERO_REPRESENTATION_TURNED_INTO_DOCTRINE",
    "OK_OUTPUT_TREATED_AS_FINAL_COMPLETION",
    "RAN_7_TESTS_TREATED_AS_FINAL_COMPLETION",
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
    "FINAL_COMPLETION_TREATED_AS_SOURCE_TRANSFER",
    "FINAL_COMPLETION_TREATED_AS_SOURCE_RECEIPT",
    "FINAL_COMPLETION_TREATED_AS_RECEPTION_AUTHORIZATION",
    "FINAL_COMPLETION_TREATED_AS_SOURCE",
    "FINAL_COMPLETION_TREATED_AS_AUTHORITY",
    "FINAL_COMPLETION_TREATED_AS_CURRENTNESS",
    "FINAL_COMPLETION_TREATED_AS_RUNTIME",
    "FINAL_COMPLETION_TREATED_AS_DEPLOYMENT",
    "FINAL_COMPLETION_TREATED_AS_PUBLIC_RELEASE",
    "FINAL_COMPLETION_TREATED_AS_OPERATION_PERMISSION",
    "FINAL_COMPLETION_TREATED_AS_CONTINUATION",
    "FINAL_COMPLETION_TREATED_AS_REUSABLE_PERMISSION",
    "FINAL_COMPLETION_TREATED_AS_FOLLOW_ON_WORK",
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
    "ADOPTION_CREATED",
    "RECEIVING_CONTEXT_GOVERNANCE_CREATED",
    "PUBLICATION_FLOW_CREATED",
    "RECEIVING_CARRIER_TREATED_AS_AUTHORITY",
    "ARTIFACT_EXISTENCE_TREATED_AS_FINAL_COMPLETION_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_FINAL_COMPLETION_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_FINAL_COMPLETION_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_FINAL_COMPLETION_AUTHORITY",
    "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "FIRST_SUCCESS_BOUNDARY_TEST_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    "FIRST_RESULT_BOUNDARY_RESOLVER_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    "V1_PACKET_EMISSION_BOUNDARY_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENT_REPORT_ARTIFACT",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_SOURCE",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_AUTHORITY",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENTNESS",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_FINAL_COMPLETION",
    "ARTIFACTS_MUTATED",
    "RETURNED_CAPTURE_MATERIAL_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_FINAL_COMPLETION_SCOPE",
)

SELECTED_BASIS_FIELDS = (
    "selected_final_completion_boundary_basis",
    "selected_final_completion_boundary_terminal_summary_basis",
    "selected_portable_verification_closure_basis",
    "selected_portable_verification_closure_terminal_summary_basis",
    "selected_portable_verification_closure_boundary_basis",
    "selected_cross_carrier_evidence_basis",
    "selected_cross_carrier_evidence_terminal_summary_basis",
    "selected_second_carrier_external_result_basis",
    "selected_second_carrier_external_result_terminal_summary_basis",
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

POSTURE_FIELDS = (
    "final_completion_spec_only_posture",
    "one_bounded_final_completion_posture",
    "final_completion_boundary_basis_preserved_posture",
    "portable_verification_closure_basis_preserved_posture",
    "portable_verification_closure_artifact_basis_preserved_posture",
    "cross_carrier_evidence_basis_preserved_posture",
    "returned_second_carrier_capture_basis_preserved_posture",
    "capture_intake_basis_preserved_posture",
    "second_carrier_output_capture_basis_preserved_posture",
    "final_completion_recorded_bounded_posture",
    "final_completion_artifact_recorded_or_bounded_posture",
    "final_completion_not_source_transfer_posture",
    "final_completion_not_source_receipt_posture",
    "final_completion_not_reception_authorization_posture",
    "final_completion_not_source_posture",
    "final_completion_not_authority_posture",
    "final_completion_not_currentness_posture",
    "final_completion_not_runtime_posture",
    "final_completion_not_deployment_posture",
    "final_completion_not_public_release_posture",
    "final_completion_not_operation_permission_posture",
    "zero_exit_code_not_final_completion_as_standalone_inference_posture",
    "string_zero_not_final_completion_as_standalone_inference_posture",
    "ok_output_not_final_completion_as_standalone_inference_posture",
    "ran_7_tests_not_final_completion_as_standalone_inference_posture",
    "returned_capture_not_final_completion_as_standalone_inference_posture",
    "receiving_carrier_not_authority_posture",
    "source_not_created_posture",
    "authority_not_created_posture",
    "currentness_not_created_posture",
    "runtime_not_created_posture",
    "deployment_not_created_posture",
    "public_release_not_created_posture",
    "operation_permission_not_created_posture",
    "continuation_not_authorized_posture",
    "reusable_permission_not_created_posture",
    "follow_on_work_not_authorized_posture",
    "hidden_repo_state_excluded_posture",
    "repo_local_availability_not_final_completion_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_cross_carrier_evidence_failure_preserved_posture",
    "predecessor_external_result_v1_failure_preserved_posture",
    "first_success_boundary_test_failure_preserved_posture",
    "first_result_boundary_resolver_failure_preserved_posture",
)

RECORDING_STATEMENT_FIELDS = (
    "final_completion_recorded",
    "bounded_final_completion_recorded",
    "final_completion_artifact_recorded_or_bounded",
    "final_completion_recorded_bounded",
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
    "RAW_FINAL_COMPLETION_BODY_MUST_NOT_RETURN",
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
        EXPECTED_FINAL_COMPLETION_BOUNDARY_OUTCOME,
        EXPECTED_PORTABLE_VERIFICATION_CLOSURE_OUTCOME,
        EXPECTED_CROSS_CARRIER_EVIDENCE_OUTCOME,
        EXPECTED_SECOND_CARRIER_EXTERNAL_RESULT_OUTCOME,
        EXPECTED_SECOND_CARRIER_VERIFICATION_OUTCOME,
        EXPECTED_SECOND_CARRIER_SUCCESS_OUTCOME,
        EXPECTED_SECOND_CARRIER_RESULT_OUTCOME,
        EXPECTED_SECOND_CARRIER_OUTPUT_CAPTURE_OUTCOME,
        "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
        "RETURNED_RESULT_CONTAINMENT_PRESERVED",
        "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
        "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
        "PREDECESSOR_CROSS_CARRIER_EVIDENCE_FAILURE_PRESERVED",
        "PREDECESSOR_EXTERNAL_RESULT_V1_FAILURE_PRESERVED",
        "FIRST_SUCCESS_BOUNDARY_TEST_FAILURE_PRESERVED",
        "FIRST_RESULT_BOUNDARY_RESOLVER_FAILURE_PRESERVED",
        "STRING_ZERO_NOT_FINAL_COMPLETION_AS_STANDALONE_INFERENCE",
    }
)

NON_CLAIM_BLOCK_CODE = {
    "source_transfer_occurred": "SOURCE_TRANSFER_OCCURRED",
    "source_receipt_occurred": "SOURCE_RECEIPT_OCCURRED",
    "reception_authorization_created": "RECEPTION_AUTHORIZATION_CREATED",
    "final_completion_treated_as_source_transfer": "FINAL_COMPLETION_TREATED_AS_SOURCE_TRANSFER",
    "final_completion_treated_as_source_receipt": "FINAL_COMPLETION_TREATED_AS_SOURCE_RECEIPT",
    "final_completion_treated_as_reception_authorization": "FINAL_COMPLETION_TREATED_AS_RECEPTION_AUTHORIZATION",
    "final_completion_treated_as_source": "FINAL_COMPLETION_TREATED_AS_SOURCE",
    "final_completion_treated_as_authority": "FINAL_COMPLETION_TREATED_AS_AUTHORITY",
    "final_completion_treated_as_currentness": "FINAL_COMPLETION_TREATED_AS_CURRENTNESS",
    "final_completion_treated_as_runtime": "FINAL_COMPLETION_TREATED_AS_RUNTIME",
    "final_completion_treated_as_deployment": "FINAL_COMPLETION_TREATED_AS_DEPLOYMENT",
    "final_completion_treated_as_public_release": "FINAL_COMPLETION_TREATED_AS_PUBLIC_RELEASE",
    "final_completion_treated_as_operation_permission": "FINAL_COMPLETION_TREATED_AS_OPERATION_PERMISSION",
    "final_completion_treated_as_continuation": "FINAL_COMPLETION_TREATED_AS_CONTINUATION",
    "final_completion_treated_as_reusable_permission": "FINAL_COMPLETION_TREATED_AS_REUSABLE_PERMISSION",
    "final_completion_treated_as_follow_on_work": "FINAL_COMPLETION_TREATED_AS_FOLLOW_ON_WORK",
    "zero_exit_code_treated_as_final_completion_standalone": "ZERO_EXIT_CODE_TREATED_AS_FINAL_COMPLETION",
    "string_zero_treated_as_final_completion_standalone": "STRING_ZERO_TREATED_AS_FINAL_COMPLETION",
    "string_zero_representation_turned_into_doctrine": "STRING_ZERO_REPRESENTATION_TURNED_INTO_DOCTRINE",
    "ok_output_treated_as_final_completion_standalone": "OK_OUTPUT_TREATED_AS_FINAL_COMPLETION",
    "ran_7_tests_treated_as_final_completion_standalone": "RAN_7_TESTS_TREATED_AS_FINAL_COMPLETION",
    "returned_capture_treated_as_final_completion_standalone": "RETURNED_CAPTURE_TREATED_AS_FINAL_COMPLETION",
    "receiving_carrier_treated_as_authority": "RECEIVING_CARRIER_TREATED_AS_AUTHORITY",
    "artifact_existence_treated_as_final_completion_authority": "ARTIFACT_EXISTENCE_TREATED_AS_FINAL_COMPLETION_AUTHORITY",
    "artifact_path_treated_as_currentness": "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "repo_local_availability_treated_as_final_completion_authority": "REPO_LOCAL_AVAILABILITY_TREATED_AS_FINAL_COMPLETION_AUTHORITY",
    "hidden_repo_state_used_as_final_completion_content": "HIDDEN_REPO_STATE_USED_AS_FINAL_COMPLETION_CONTENT",
    "hidden_repo_state_used_as_final_completion_authority": "HIDDEN_REPO_STATE_USED_AS_FINAL_COMPLETION_AUTHORITY",
    "source_created": "SOURCE_CREATED",
    "authority_created": "AUTHORITY_CREATED",
    "currentness_created": "CURRENTNESS_CREATED",
    "runtime_hosting_created": "RUNTIME_HOSTING_CREATED",
    "deployment_created": "DEPLOYMENT_CREATED",
    "public_release_created": "PUBLIC_RELEASE_CREATED",
    "operation_permission_created": "OPERATION_PERMISSION_CREATED",
    "continuation_authorized": "CONTINUATION_AUTHORIZED",
    "reusable_permission_created": "REUSABLE_PERMISSION_CREATED",
    "derivative_reception_authorized": "DERIVATIVE_RECEPTION_AUTHORIZED",
    "vessel_relation_authorized": "VESSEL_RELATION_AUTHORIZED",
    "another_reception_request_authorized": "ANOTHER_RECEPTION_REQUEST_AUTHORIZED",
    "follow_on_work_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
    "raw_full_prior_artifact_body_returned": "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "prior_artifacts_mutated": "ARTIFACTS_MUTATED",
    "returned_capture_material_mutated": "RETURNED_CAPTURE_MATERIAL_MUTATED",
    "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
    "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
    "predecessor_cross_carrier_evidence_repaired": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_cross_carrier_evidence_hidden": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_cross_carrier_evidence_claimed_passed": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_external_result_v1_repaired": "PREDECESSOR_EXTERNAL_RESULT_V1_FAILURE_MISSING_OR_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
    "predecessor_external_result_v1_hidden": "PREDECESSOR_EXTERNAL_RESULT_V1_FAILURE_MISSING_OR_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
    "predecessor_external_result_v1_claimed_passed": "PREDECESSOR_EXTERNAL_RESULT_V1_FAILURE_MISSING_OR_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
    "v1_packet_emission_repaired": "V1_PACKET_EMISSION_BOUNDARY_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    "v1_packet_emission_hidden": "V1_PACKET_EMISSION_BOUNDARY_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    "v1_packet_emission_claimed_passed": "V1_PACKET_EMISSION_BOUNDARY_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    "first_success_boundary_test_repaired": "FIRST_SUCCESS_BOUNDARY_TEST_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    "first_success_boundary_test_hidden": "FIRST_SUCCESS_BOUNDARY_TEST_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    "first_success_boundary_test_claimed_passed": "FIRST_SUCCESS_BOUNDARY_TEST_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    "first_result_boundary_resolver_repaired": "FIRST_RESULT_BOUNDARY_RESOLVER_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    "first_result_boundary_resolver_hidden": "FIRST_RESULT_BOUNDARY_RESOLVER_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    "first_result_boundary_resolver_claimed_passed": "FIRST_RESULT_BOUNDARY_RESOLVER_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
}

FORBIDDEN_OUTPUT_ROOT_FRAGMENTS = (
    "integrity_host_v0_min_coexistence_portable_source_body_verification_final_completion_boundary",
    "integrity_host_v0_min_coexistence_portable_source_body_verification_portable_verification_closure",
    "integrity_host_v0_min_coexistence_portable_source_body_verification_portable_verification_closure_boundary",
    "integrity_host_v0_min_coexistence_portable_source_body_verification_cross_carrier_evidence",
    "integrity_host_v0_min_coexistence_portable_source_body_verification_cross_carrier_evidence_boundary",
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
    "runtime",
    "deployment",
    "public_release",
    "public-release",
    "source_transfer",
    "source-transfer",
    "source_receipt",
    "source-receipt",
    "reception",
)


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
    if isinstance(value, (list, tuple, set, frozenset, dict)):
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
    if isinstance(value, MappingABC):
        if value.get("declared") is False:
            return False
        if "value" in value:
            return value.get("value") is True
        if "preserved" in value:
            return value.get("preserved") is True
        if "recorded" in value:
            return value.get("recorded") is True
        if "blocked" in value:
            return value.get("blocked") is True
        if "declared" in value:
            return value.get("declared") is True
    return False


def _false(value: Any) -> bool:
    return value is False


def _basis_declared(request: Mapping[str, Any], field_name: str) -> bool:
    return _present(request.get(field_name))


def _sensitive_key(key: str | None) -> bool:
    if key is None:
        return False
    lowered = key.lower()
    return lowered in SENSITIVE_CONTENT_KEYS or lowered.endswith("_body")


def _sanitize(value: Any, parent_key: str | None = None) -> Any:
    if isinstance(value, MappingABC):
        return {str(key): _sanitize(val, str(key)) for key, val in value.items()}
    if isinstance(value, (list, tuple)):
        return [_sanitize(item, parent_key) for item in value]
    if isinstance(value, (set, frozenset)):
        return sorted(_sanitize(item, parent_key) for item in value)
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, (datetime.datetime, datetime.date)):
        return value.isoformat()
    if isinstance(value, (str, int, float, bool)) or value is None:
        if isinstance(value, str):
            if value in OFFICIAL_STRINGS:
                return value
            if any(sentinel in value for sentinel in HOSTILE_SENTINELS):
                return REDACTED_RAW_VALUE
            if _sensitive_key(parent_key):
                return REDACTED_RAW_VALUE
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
    public_code = block_code if block_code in BLOCK_CODES else "DECLARED_FINAL_COMPLETION_REQUEST_MALFORMED"
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
    value = request.get("final_completion_request_id")
    if isinstance(value, str) and value:
        return value
    return DEFAULT_REQUEST_ID


def _declared_non_claims(request: Mapping[str, Any]) -> Mapping[str, Any]:
    value = request.get("declared_non_claims")
    if isinstance(value, MappingABC):
        return value
    return {}


def _scope_values(request: Mapping[str, Any]) -> list[Any]:
    value = request.get("final_completion_scope")
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, MappingABC):
        return list(value.values())
    if isinstance(value, IterableABC):
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


def _final_completion_statement(recorded: bool) -> dict[str, bool]:
    statement: dict[str, bool] = {}
    for field_name in ALLOWED_TRUE_RECORDED_FIELDS:
        if field_name in RECORDING_STATEMENT_FIELDS:
            statement[field_name] = bool(recorded)
        else:
            statement[field_name] = True
    return statement


def _safe_non_claims() -> dict[str, bool]:
    return {field_name: False for field_name in REQUIRED_FALSE_NON_CLAIMS}


def _final_completion_non_meaning() -> dict[str, bool]:
    return {
        "final_completion_is_source_transfer": False,
        "final_completion_is_source_receipt": False,
        "final_completion_is_reception_authorization": False,
        "final_completion_is_source": False,
        "final_completion_is_authority": False,
        "final_completion_is_currentness": False,
        "final_completion_is_runtime": False,
        "final_completion_is_deployment": False,
        "final_completion_is_public_release": False,
        "final_completion_is_operation_permission": False,
        "final_completion_is_continuation": False,
        "final_completion_is_reusable_permission": False,
        "final_completion_is_derivative_reception": False,
        "final_completion_is_vessel_relation": False,
        "final_completion_is_another_reception_request": False,
        "final_completion_is_adoption": False,
        "final_completion_is_receiving_context_governance": False,
        "final_completion_is_publication_flow": False,
        "final_completion_is_follow_on_work": False,
        "zero_exit_code_is_final_completion_by_standalone_inference": False,
        "string_zero_is_final_completion_by_standalone_inference": False,
        "string_zero_is_doctrine": False,
        "ok_output_is_final_completion_by_standalone_inference": False,
        "ran_7_tests_is_final_completion_by_standalone_inference": False,
        "returned_capture_is_final_completion_by_standalone_inference": False,
        "macbook_pro_is_authority": False,
        "macbook_air_is_source_or_authority": False,
    }


def _what_remains_open() -> list[str]:
    return [
        "final-completion terminal summary, if needed",
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
    ]


def _add_core_checks(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    forced_block_code: str | None = None,
    forced_block_reason: str | None = None,
) -> None:
    if forced_block_code is not None:
        _check(
            checks,
            "declared final-completion request readable and mapping-shaped",
            False,
            "readable mapping declared final-completion request",
            forced_block_reason or forced_block_code,
            forced_block_code,
        )

    question = request.get("final_completion_question")
    intent = request.get("final_completion_intent")
    scope = _scope_values(request)
    unsupported_scope = [value for value in scope if value not in SUPPORTED_SCOPE_VALUES]
    non_claims = _declared_non_claims(request)

    _check(
        checks,
        "final-completion question declared",
        question == CORE_QUESTION,
        CORE_QUESTION,
        question,
        "FINAL_COMPLETION_QUESTION_UNDECLARED",
    )
    _check(
        checks,
        "intent supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "FINAL_COMPLETION_INTENT_UNSUPPORTED",
    )
    _check(
        checks,
        "explicit block intent absent",
        intent != INTENT_BLOCK,
        "record or do-not-record final-completion intent",
        intent,
        "FINAL_COMPLETION_REQUEST_DECLARED_BLOCK",
    )
    _check(
        checks,
        "final-completion scope supported",
        bool(scope) and not unsupported_scope,
        SUPPORTED_SCOPE_VALUES,
        unsupported_scope or scope,
        "UNSUPPORTED_FINAL_COMPLETION_SCOPE",
    )

    _check(
        checks,
        "final-completion-boundary basis declared",
        _basis_declared(request, "selected_final_completion_boundary_basis"),
        "selected final-completion-boundary basis",
        request.get("selected_final_completion_boundary_basis"),
        "FINAL_COMPLETION_BOUNDARY_BASIS_MISSING",
    )
    _check(
        checks,
        "final-completion-boundary outcome recorded",
        request.get("selected_final_completion_boundary_result_outcome")
        == EXPECTED_FINAL_COMPLETION_BOUNDARY_OUTCOME,
        EXPECTED_FINAL_COMPLETION_BOUNDARY_OUTCOME,
        request.get("selected_final_completion_boundary_result_outcome"),
        "FINAL_COMPLETION_BOUNDARY_NOT_RECORDED",
    )
    _check(
        checks,
        "final-completion-boundary version 0.1.0",
        request.get("selected_final_completion_boundary_result_version") == RESULT_VERSION,
        RESULT_VERSION,
        request.get("selected_final_completion_boundary_result_version"),
        "FINAL_COMPLETION_BOUNDARY_VERSION_NOT_0_1_0",
    )
    _check(
        checks,
        "final-completion-boundary failed checks zero",
        _as_int(request.get("selected_final_completion_boundary_failed_check_count")) == 0,
        0,
        request.get("selected_final_completion_boundary_failed_check_count"),
        "FINAL_COMPLETION_BOUNDARY_FAILED_CHECKS_PRESENT",
    )
    _check(
        checks,
        "final-completion-boundary declared future final-completion review step",
        request.get("selected_final_completion_boundary_declared_future_final_completion_review_step")
        is True,
        True,
        request.get("selected_final_completion_boundary_declared_future_final_completion_review_step"),
        "FINAL_COMPLETION_BOUNDARY_DID_NOT_DECLARE_FUTURE_FINAL_COMPLETION_REVIEW_STEP",
    )
    _check(
        checks,
        "final-completion-boundary did not already create final completion",
        request.get("selected_final_completion_boundary_already_created_final_completion")
        is False,
        False,
        request.get("selected_final_completion_boundary_already_created_final_completion"),
        "FINAL_COMPLETION_BOUNDARY_ALREADY_CREATED_FINAL_COMPLETION",
    )
    _check(
        checks,
        "final-completion-boundary did not treat boundary as final completion",
        request.get("selected_final_completion_boundary_treated_boundary_as_final_completion")
        is False,
        False,
        request.get("selected_final_completion_boundary_treated_boundary_as_final_completion"),
        "FINAL_COMPLETION_BOUNDARY_TREATED_BOUNDARY_AS_FINAL_COMPLETION",
    )
    _check(
        checks,
        "final-completion-boundary kept zero exit code not final completion",
        request.get("selected_final_completion_boundary_zero_exit_code_not_final_completion")
        is True,
        True,
        request.get("selected_final_completion_boundary_zero_exit_code_not_final_completion"),
        "FINAL_COMPLETION_BOUNDARY_TREATED_ZERO_EXIT_CODE_AS_FINAL_COMPLETION",
    )
    _check(
        checks,
        "final-completion-boundary kept string zero not final completion",
        request.get("selected_final_completion_boundary_string_zero_not_final_completion")
        is True,
        True,
        request.get("selected_final_completion_boundary_string_zero_not_final_completion"),
        "FINAL_COMPLETION_BOUNDARY_TREATED_STRING_ZERO_AS_FINAL_COMPLETION",
    )
    _check(
        checks,
        "final-completion-boundary kept string zero not doctrine",
        request.get("selected_final_completion_boundary_string_zero_turned_into_doctrine")
        is False,
        False,
        request.get("selected_final_completion_boundary_string_zero_turned_into_doctrine"),
        "FINAL_COMPLETION_BOUNDARY_TREATED_STRING_ZERO_AS_DOCTRINE",
    )
    _check(
        checks,
        "final-completion-boundary kept OK not final completion",
        request.get("selected_final_completion_boundary_ok_not_final_completion") is True,
        True,
        request.get("selected_final_completion_boundary_ok_not_final_completion"),
        "FINAL_COMPLETION_BOUNDARY_TREATED_OK_AS_FINAL_COMPLETION",
    )
    _check(
        checks,
        "final-completion-boundary kept Ran 7 tests not final completion",
        request.get("selected_final_completion_boundary_ran_7_tests_not_final_completion")
        is True,
        True,
        request.get("selected_final_completion_boundary_ran_7_tests_not_final_completion"),
        "FINAL_COMPLETION_BOUNDARY_TREATED_RAN_7_TESTS_AS_FINAL_COMPLETION",
    )
    _check(
        checks,
        "final-completion-boundary kept returned capture not final completion",
        request.get("selected_final_completion_boundary_returned_capture_not_final_completion")
        is True,
        True,
        request.get("selected_final_completion_boundary_returned_capture_not_final_completion"),
        "FINAL_COMPLETION_BOUNDARY_TREATED_RETURNED_CAPTURE_AS_FINAL_COMPLETION",
    )
    _check(
        checks,
        "final-completion-boundary kept official enum scope strings not redacted",
        request.get("selected_final_completion_boundary_official_enum_scope_strings_redacted")
        is False
        and "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED" in scope,
        "official enum scope strings unredacted",
        {
            "redacted": request.get(
                "selected_final_completion_boundary_official_enum_scope_strings_redacted"
            ),
            "scope": scope,
        },
        "FINAL_COMPLETION_BOUNDARY_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
    )
    _check(
        checks,
        "predecessor cross-carrier evidence failure preserved",
        request.get("selected_final_completion_boundary_predecessor_cross_carrier_evidence_failure_preserved")
        is True
        and request.get("predecessor_cross_carrier_evidence_failure_preserved") is True,
        True,
        {
            "boundary_basis": request.get(
                "selected_final_completion_boundary_predecessor_cross_carrier_evidence_failure_preserved"
            ),
            "request": request.get("predecessor_cross_carrier_evidence_failure_preserved"),
        },
        "PREDECESSOR_CROSS_CARRIER_EVIDENCE_FAILURE_MISSING_OR_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
    )
    _check(
        checks,
        "predecessor external-result v1 failure preserved",
        request.get("predecessor_external_result_v1_failure_preserved") is True,
        True,
        request.get("predecessor_external_result_v1_failure_preserved"),
        "PREDECESSOR_EXTERNAL_RESULT_V1_FAILURE_MISSING_OR_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
    )

    _check(
        checks,
        "portable-verification-closure basis declared",
        _basis_declared(request, "selected_portable_verification_closure_basis"),
        "selected portable-verification-closure basis",
        request.get("selected_portable_verification_closure_basis"),
        "PORTABLE_VERIFICATION_CLOSURE_BASIS_MISSING",
    )
    _check(
        checks,
        "portable-verification-closure outcome recorded",
        request.get("selected_portable_verification_closure_result_outcome")
        == EXPECTED_PORTABLE_VERIFICATION_CLOSURE_OUTCOME,
        EXPECTED_PORTABLE_VERIFICATION_CLOSURE_OUTCOME,
        request.get("selected_portable_verification_closure_result_outcome"),
        "PORTABLE_VERIFICATION_CLOSURE_NOT_RECORDED",
    )
    _check(
        checks,
        "portable-verification-closure version 0.1.0",
        request.get("selected_portable_verification_closure_result_version")
        == RESULT_VERSION,
        RESULT_VERSION,
        request.get("selected_portable_verification_closure_result_version"),
        "PORTABLE_VERIFICATION_CLOSURE_NOT_RECORDED",
    )
    _check(
        checks,
        "portable-verification-closure failed checks zero",
        _as_int(request.get("selected_portable_verification_closure_failed_check_count"))
        == 0,
        0,
        request.get("selected_portable_verification_closure_failed_check_count"),
        "PORTABLE_VERIFICATION_CLOSURE_FAILED_CHECKS_PRESENT",
    )
    _check(
        checks,
        "portable-verification-closure recorded bounded line-level closure",
        request.get("selected_portable_verification_closure_bounded_closure_recorded")
        is True,
        True,
        request.get("selected_portable_verification_closure_bounded_closure_recorded"),
        "PORTABLE_VERIFICATION_CLOSURE_NOT_RECORDED",
    )
    _check(
        checks,
        "portable-verification-closure did not already create final completion",
        request.get("selected_portable_verification_closure_already_created_final_completion")
        is False,
        False,
        request.get("selected_portable_verification_closure_already_created_final_completion"),
        "PORTABLE_VERIFICATION_CLOSURE_ALREADY_CREATED_FINAL_COMPLETION",
    )
    for field_name, code in (
        ("selected_portable_verification_closure_treated_as_final_completion", "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_FINAL_COMPLETION"),
        ("selected_portable_verification_closure_treated_as_source", "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_SOURCE"),
        ("selected_portable_verification_closure_treated_as_authority", "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_AUTHORITY"),
        ("selected_portable_verification_closure_treated_as_currentness", "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_CURRENTNESS"),
        ("selected_portable_verification_closure_treated_as_runtime", "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_RUNTIME"),
        ("selected_portable_verification_closure_treated_as_deployment", "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_DEPLOYMENT"),
        ("selected_portable_verification_closure_treated_as_public_release", "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_PUBLIC_RELEASE"),
        ("selected_portable_verification_closure_treated_as_operation_permission", "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_OPERATION_PERMISSION"),
        ("selected_portable_verification_closure_treated_as_follow_on_work", "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_FOLLOW_ON_WORK"),
    ):
        _check(
            checks,
            field_name.replace("_", " "),
            request.get(field_name) is False,
            False,
            request.get(field_name),
            code,
        )

    _check(
        checks,
        "cross-carrier evidence basis declared",
        _basis_declared(request, "selected_cross_carrier_evidence_basis"),
        "selected cross-carrier evidence basis",
        request.get("selected_cross_carrier_evidence_basis"),
        "CROSS_CARRIER_EVIDENCE_BASIS_MISSING",
    )
    _check(
        checks,
        "cross-carrier evidence recorded",
        request.get("selected_cross_carrier_evidence_result_outcome")
        == EXPECTED_CROSS_CARRIER_EVIDENCE_OUTCOME,
        EXPECTED_CROSS_CARRIER_EVIDENCE_OUTCOME,
        request.get("selected_cross_carrier_evidence_result_outcome"),
        "CROSS_CARRIER_EVIDENCE_NOT_RECORDED",
    )
    _check(
        checks,
        "cross-carrier evidence failed checks zero",
        _as_int(request.get("selected_cross_carrier_evidence_failed_check_count")) == 0,
        0,
        request.get("selected_cross_carrier_evidence_failed_check_count"),
        "CROSS_CARRIER_EVIDENCE_FAILED_CHECKS_PRESENT",
    )

    _check(
        checks,
        "second-carrier external-result basis declared",
        _basis_declared(request, "selected_second_carrier_external_result_basis"),
        "selected second-carrier external-result basis",
        request.get("selected_second_carrier_external_result_basis"),
        "SECOND_CARRIER_EXTERNAL_RESULT_BASIS_MISSING",
    )
    _check(
        checks,
        "second-carrier external-result recorded",
        request.get("selected_second_carrier_external_result_result_outcome")
        == EXPECTED_SECOND_CARRIER_EXTERNAL_RESULT_OUTCOME,
        EXPECTED_SECOND_CARRIER_EXTERNAL_RESULT_OUTCOME,
        request.get("selected_second_carrier_external_result_result_outcome"),
        "SECOND_CARRIER_EXTERNAL_RESULT_NOT_RECORDED",
    )
    _check(
        checks,
        "second-carrier external-result failed checks zero",
        _as_int(request.get("selected_second_carrier_external_result_failed_check_count"))
        == 0,
        0,
        request.get("selected_second_carrier_external_result_failed_check_count"),
        "SECOND_CARRIER_EXTERNAL_RESULT_FAILED_CHECKS_PRESENT",
    )

    for basis_field, outcome_field, expected, missing_code, not_recorded_code in (
        (
            "selected_second_carrier_verification_basis",
            "selected_second_carrier_verification_result_outcome",
            EXPECTED_SECOND_CARRIER_VERIFICATION_OUTCOME,
            "SECOND_CARRIER_VERIFICATION_BASIS_MISSING",
            "SECOND_CARRIER_VERIFICATION_NOT_RECORDED",
        ),
        (
            "selected_second_carrier_success_basis",
            "selected_second_carrier_success_result_outcome",
            EXPECTED_SECOND_CARRIER_SUCCESS_OUTCOME,
            "SECOND_CARRIER_SUCCESS_BASIS_MISSING",
            "SECOND_CARRIER_SUCCESS_NOT_RECORDED",
        ),
        (
            "selected_second_carrier_result_basis",
            "selected_second_carrier_result_result_outcome",
            EXPECTED_SECOND_CARRIER_RESULT_OUTCOME,
            "SECOND_CARRIER_RESULT_BASIS_MISSING",
            "SECOND_CARRIER_RESULT_NOT_RECORDED",
        ),
    ):
        _check(
            checks,
            f"{basis_field} declared",
            _basis_declared(request, basis_field),
            f"{basis_field} present",
            request.get(basis_field),
            missing_code,
        )
        _check(
            checks,
            f"{outcome_field} recorded",
            request.get(outcome_field) == expected,
            expected,
            request.get(outcome_field),
            not_recorded_code,
        )

    _check(
        checks,
        "returned capture intake basis declared",
        _basis_declared(request, "selected_returned_second_carrier_live_capture_intake_basis"),
        "selected returned capture intake basis",
        request.get("selected_returned_second_carrier_live_capture_intake_basis"),
        "RETURNED_CAPTURE_INTAKE_BASIS_MISSING",
    )
    _check(
        checks,
        "returned capture intake preserved",
        request.get("selected_returned_capture_intake_preserved") is True
        and request.get("selected_returned_capture_intake_capture_only") is True,
        "capture intake preserved as capture-only basis",
        {
            "preserved": request.get("selected_returned_capture_intake_preserved"),
            "capture_only": request.get("selected_returned_capture_intake_capture_only"),
        },
        "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
    )
    _check(
        checks,
        "returned capture material basis declared",
        _basis_declared(request, "selected_returned_capture_material_basis"),
        "selected returned capture material basis",
        request.get("selected_returned_capture_material_basis"),
        "RETURNED_CAPTURE_MATERIAL_MISSING",
    )
    for field_name, code in (
        ("selected_returned_capture_zip_path", "RETURNED_ZIP_PATH_MISSING"),
        ("selected_returned_capture_hash_path", "RETURNED_HASH_PATH_MISSING"),
        ("selected_returned_capture_extracted_directory_path", "RETURNED_EXTRACTED_DIRECTORY_MISSING"),
        ("selected_returned_capture_combined_terminal_log_path", "RETURNED_COMBINED_TERMINAL_LOG_MISSING"),
        ("selected_returned_capture_exit_code", "RETURNED_EXIT_CODE_MISSING"),
        ("selected_returned_capture_command_text", "RETURNED_COMMAND_TEXT_MISSING"),
    ):
        _check(
            checks,
            f"{field_name} basis declared",
            _present(request.get(field_name)),
            f"{field_name} present",
            request.get(field_name),
            code,
        )
    _check(
        checks,
        "returned capture timestamps basis declared",
        _present(request.get("selected_returned_capture_started_at"))
        and _present(request.get("selected_returned_capture_completed_at")),
        "run_started_at and run_completed_at present",
        {
            "started_at": request.get("selected_returned_capture_started_at"),
            "completed_at": request.get("selected_returned_capture_completed_at"),
        },
        "RETURNED_TIMESTAMPS_MISSING",
    )
    _check(
        checks,
        "declared string zero representation not turned into doctrine",
        request.get("selected_returned_capture_declared_exit_code") == "0"
        and non_claims.get("string_zero_representation_turned_into_doctrine") is False,
        'declared exit code string "0" with doctrine non-claim false',
        {
            "declared_exit_code": request.get("selected_returned_capture_declared_exit_code"),
            "doctrine_non_claim": non_claims.get(
                "string_zero_representation_turned_into_doctrine"
            ),
        },
        "STRING_ZERO_REPRESENTATION_TURNED_INTO_DOCTRINE",
    )
    _check(
        checks,
        "raw placeholder carrier fields preserved and unrepaired",
        request.get("selected_returned_capture_placeholder_fields_unrepaired") is True,
        "placeholder carrier fields unrepaired",
        request.get("selected_returned_capture_placeholder_fields_unrepaired"),
        "PLACEHOLDER_CARRIER_FIELDS_REPAIRED",
    )

    _check(
        checks,
        "second-carrier output capture basis declared",
        _basis_declared(request, "selected_second_carrier_output_capture_basis"),
        "selected second-carrier output capture basis",
        request.get("selected_second_carrier_output_capture_basis"),
        "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_MISSING",
    )
    _check(
        checks,
        "second-carrier output capture recorded",
        request.get("selected_second_carrier_output_capture_result_outcome")
        == EXPECTED_SECOND_CARRIER_OUTPUT_CAPTURE_OUTCOME,
        EXPECTED_SECOND_CARRIER_OUTPUT_CAPTURE_OUTCOME,
        request.get("selected_second_carrier_output_capture_result_outcome"),
        "SECOND_CARRIER_OUTPUT_CAPTURE_NOT_RECORDED",
    )
    _check(
        checks,
        "second-carrier output capture failed checks zero",
        _as_int(request.get("selected_second_carrier_output_capture_failed_check_count"))
        == 0,
        0,
        request.get("selected_second_carrier_output_capture_failed_check_count"),
        "SECOND_CARRIER_OUTPUT_CAPTURE_FAILED_CHECKS_PRESENT",
    )

    predecessor_basis = request.get("selected_predecessor_failure_basis")
    predecessor_visible = isinstance(predecessor_basis, MappingABC) and all(
        predecessor_basis.get(field) is True
        for field in (
            "predecessor_cross_carrier_evidence_failure_preserved",
            "predecessor_external_result_v1_failure_preserved",
            "first_success_boundary_test_failure_preserved",
            "first_result_boundary_resolver_failure_preserved",
            "v1_packet_emission_boundary_failure_preserved",
        )
    )
    predecessor_unrepaired = isinstance(predecessor_basis, MappingABC) and not any(
        predecessor_basis.get(field) is True
        for field in (
            "predecessor_cross_carrier_evidence_repaired",
            "predecessor_cross_carrier_evidence_hidden",
            "predecessor_cross_carrier_evidence_claimed_passed",
            "predecessor_external_result_v1_repaired",
            "predecessor_external_result_v1_hidden",
            "predecessor_external_result_v1_claimed_passed",
            "first_success_boundary_test_repaired",
            "first_success_boundary_test_hidden",
            "first_success_boundary_test_claimed_passed",
            "first_result_boundary_resolver_repaired",
            "first_result_boundary_resolver_hidden",
            "first_result_boundary_resolver_claimed_passed",
            "v1_packet_emission_repaired",
            "v1_packet_emission_hidden",
            "v1_packet_emission_claimed_passed",
        )
    )
    _check(
        checks,
        "predecessor failure visible and unrepaired",
        predecessor_visible and predecessor_unrepaired,
        "predecessor failure evidence visible and unrepaired",
        predecessor_basis,
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    )

    for posture_field in POSTURE_FIELDS:
        code = "FINAL_COMPLETION_QUESTION_UNDECLARED"
        if posture_field == "final_completion_spec_only_posture":
            code = "FINAL_COMPLETION_QUESTION_UNDECLARED"
        elif posture_field in {
            "final_completion_not_source_transfer_posture",
            "final_completion_not_source_receipt_posture",
            "final_completion_not_reception_authorization_posture",
        }:
            code = "FINAL_COMPLETION_TREATED_AS_SOURCE_TRANSFER"
        elif posture_field in {
            "final_completion_not_source_posture",
            "final_completion_not_authority_posture",
            "final_completion_not_currentness_posture",
            "final_completion_not_runtime_posture",
            "final_completion_not_deployment_posture",
            "final_completion_not_public_release_posture",
            "final_completion_not_operation_permission_posture",
        }:
            code = "FINAL_COMPLETION_TREATED_AS_SOURCE"
        elif posture_field.startswith("zero_exit_code"):
            code = "ZERO_EXIT_CODE_TREATED_AS_FINAL_COMPLETION"
        elif posture_field.startswith("string_zero"):
            code = "STRING_ZERO_TREATED_AS_FINAL_COMPLETION"
        elif posture_field.startswith("ok_output"):
            code = "OK_OUTPUT_TREATED_AS_FINAL_COMPLETION"
        elif posture_field.startswith("ran_7_tests"):
            code = "RAN_7_TESTS_TREATED_AS_FINAL_COMPLETION"
        elif posture_field.startswith("returned_capture"):
            code = "RETURNED_CAPTURE_TREATED_AS_FINAL_COMPLETION"
        elif posture_field == "hidden_repo_state_excluded_posture":
            code = "HIDDEN_REPO_STATE_USED_AS_FINAL_COMPLETION_CONTENT"
        elif posture_field == "repo_local_availability_not_final_completion_authority_posture":
            code = "REPO_LOCAL_AVAILABILITY_TREATED_AS_FINAL_COMPLETION_AUTHORITY"
        elif posture_field == "selected_basis_reference_shape_posture":
            code = "SELECTED_BASIS_NOT_REFERENCE_SHAPED"
        elif posture_field == "raw_full_prior_artifact_body_not_returned_posture":
            code = "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED"
        elif posture_field == "official_enum_scope_strings_not_redacted_posture":
            code = "FINAL_COMPLETION_BOUNDARY_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS"
        _check(
            checks,
            f"{posture_field} declared",
            _truth(request.get(posture_field)),
            "posture declared true",
            request.get(posture_field),
            code,
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
        "FINAL_COMPLETION_BOUNDARY_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
    )
    _check(
        checks,
        "hostile raw body content contained",
        _truth(request.get("hostile_raw_body_content_contained_posture")),
        "hostile raw body content contained",
        request.get("hostile_raw_body_content_contained_posture"),
        "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_FINAL_COMPLETION",
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
    requested_outcome = request_copy.get("requested_final_completion_outcome")
    intent = request_copy.get("final_completion_intent")
    if failed_check is not None:
        outcome = OUTCOME_BLOCKED
        block_code = str(
            failed_check.get("block_code")
            or failed_check.get("failure_code")
            or "DECLARED_FINAL_COMPLETION_REQUEST_MALFORMED"
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
        "portable_source_body_verification_final_completion_id": _request_id(request_copy),
        "portable_source_body_verification_final_completion_type": RESULT_TYPE,
        "portable_source_body_verification_final_completion_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
    }
    result: dict[str, Any] = {
        "portable_source_body_verification_final_completion_metadata": metadata,
        "declared_final_completion_question": {
            "final_completion_request_id": _request_id(request_copy),
            "final_completion_question": request_copy.get("final_completion_question"),
            "final_completion_intent": request_copy.get("final_completion_intent"),
        },
    }

    for field_name in SELECTED_BASIS_FIELDS:
        result[field_name] = _sanitize_mapping(request_copy.get(field_name))
    for posture_field in POSTURE_FIELDS:
        result[posture_field] = _sanitize_mapping(request_copy.get(posture_field))

    result.update(
        {
            "final_completion_scope": _sanitize(_scope_values(request_copy)),
            "final_completion_checks": checks,
            "final_completion_statement": _final_completion_statement(recorded),
            "final_completion_non_meaning": _final_completion_non_meaning(),
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
    result["portable_source_body_verification_final_completion_summary"] = (
        build_portable_source_body_verification_final_completion_summary(result)
    )
    return result


def resolve_portable_source_body_verification_final_completion(
    declared_final_completion_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded final-completion posture from a declared request."""

    if declared_final_completion_request is None:
        return _resolve_mapping(
            {},
            "DECLARED_FINAL_COMPLETION_REQUEST_MALFORMED",
            "declared final-completion request is missing",
        )
    if not isinstance(declared_final_completion_request, MappingABC):
        return _resolve_mapping(
            {"malformed_request_type": type(declared_final_completion_request).__name__},
            "DECLARED_FINAL_COMPLETION_REQUEST_MALFORMED",
            "declared final-completion request is not a mapping",
        )
    return _resolve_mapping(declared_final_completion_request)


def resolve_portable_source_body_verification_final_completion_from_path(
    declared_final_completion_request_path: Path | str,
) -> dict[str, Any]:
    """Load a declared final-completion request JSON file and resolve it."""

    try:
        path = Path(declared_final_completion_request_path)
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        return _resolve_mapping(
            {"final_completion_request_id": DEFAULT_REQUEST_ID},
            "DECLARED_FINAL_COMPLETION_REQUEST_UNREADABLE",
            str(exc),
        )
    try:
        loaded = json.loads(raw)
    except json.JSONDecodeError as exc:
        return _resolve_mapping(
            {"final_completion_request_id": DEFAULT_REQUEST_ID},
            "DECLARED_FINAL_COMPLETION_REQUEST_MALFORMED",
            str(exc),
        )
    if not isinstance(loaded, MappingABC):
        return _resolve_mapping(
            {"final_completion_request_id": DEFAULT_REQUEST_ID},
            "DECLARED_FINAL_COMPLETION_REQUEST_MALFORMED",
            "declared final-completion request JSON root is not an object",
        )
    return resolve_portable_source_body_verification_final_completion(loaded)


def build_portable_source_body_verification_final_completion_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact JSON-safe summary for a final-completion result."""

    checks = result.get("final_completion_checks", [])
    if not isinstance(checks, list):
        checks = []
    passed_count = sum(1 for check in checks if isinstance(check, MappingABC) and check.get("passed") is True)
    failed_count = sum(1 for check in checks if isinstance(check, MappingABC) and check.get("passed") is not True)
    metadata = result.get("portable_source_body_verification_final_completion_metadata", {})
    question = result.get("declared_final_completion_question", {})
    statement = result.get("final_completion_statement", {})
    non_claims = result.get("non_claims", {})
    block = result.get("block")
    if not isinstance(metadata, MappingABC):
        metadata = {}
    if not isinstance(question, MappingABC):
        question = {}
    if not isinstance(statement, MappingABC):
        statement = {}
    if not isinstance(non_claims, MappingABC):
        non_claims = {}
    if not isinstance(block, MappingABC):
        block = {}

    summary = {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "request_id": question.get("final_completion_request_id")
        or metadata.get("portable_source_body_verification_final_completion_id"),
        "question": question.get("final_completion_question"),
        "intent": question.get("final_completion_intent"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": metadata.get(
            "portable_source_body_verification_final_completion_version"
        ),
        "resolver_module": metadata.get("resolver_module"),
        "final_completion_recorded": statement.get("final_completion_recorded"),
        "bounded_final_completion_recorded": statement.get(
            "bounded_final_completion_recorded"
        ),
        "final_completion_artifact_recorded_or_bounded": statement.get(
            "final_completion_artifact_recorded_or_bounded"
        ),
        "final_completion_boundary_basis_preserved": statement.get(
            "final_completion_boundary_basis_preserved"
        ),
        "portable_verification_closure_basis_preserved": statement.get(
            "portable_verification_closure_basis_preserved"
        ),
        "portable_verification_closure_artifact_basis_preserved": statement.get(
            "portable_verification_closure_artifact_basis_preserved"
        ),
        "cross_carrier_evidence_basis_preserved": statement.get(
            "cross_carrier_evidence_basis_preserved"
        ),
        "returned_second_carrier_capture_basis_preserved": statement.get(
            "returned_second_carrier_capture_basis_preserved"
        ),
        "capture_intake_basis_preserved": statement.get(
            "capture_intake_basis_preserved"
        ),
        "second_carrier_output_capture_basis_preserved": statement.get(
            "second_carrier_output_capture_basis_preserved"
        ),
        "final_completion_recorded_bounded": statement.get(
            "final_completion_recorded_bounded"
        ),
        "final_completion_not_source_transfer": statement.get(
            "final_completion_not_source_transfer"
        ),
        "final_completion_not_source_receipt": statement.get(
            "final_completion_not_source_receipt"
        ),
        "final_completion_not_reception_authorization": statement.get(
            "final_completion_not_reception_authorization"
        ),
        "final_completion_not_source": statement.get("final_completion_not_source"),
        "final_completion_not_authority": statement.get(
            "final_completion_not_authority"
        ),
        "final_completion_not_currentness": statement.get(
            "final_completion_not_currentness"
        ),
        "final_completion_not_runtime": statement.get("final_completion_not_runtime"),
        "final_completion_not_deployment": statement.get(
            "final_completion_not_deployment"
        ),
        "final_completion_not_public_release": statement.get(
            "final_completion_not_public_release"
        ),
        "final_completion_not_operation_permission": statement.get(
            "final_completion_not_operation_permission"
        ),
        "zero_exit_code_not_final_completion_as_standalone_inference": statement.get(
            "zero_exit_code_not_final_completion_as_standalone_inference"
        ),
        "string_zero_not_final_completion_as_standalone_inference": statement.get(
            "string_zero_not_final_completion_as_standalone_inference"
        ),
        "ok_output_not_final_completion_as_standalone_inference": statement.get(
            "ok_output_not_final_completion_as_standalone_inference"
        ),
        "ran_7_tests_not_final_completion_as_standalone_inference": statement.get(
            "ran_7_tests_not_final_completion_as_standalone_inference"
        ),
        "returned_capture_not_final_completion_as_standalone_inference": statement.get(
            "returned_capture_not_final_completion_as_standalone_inference"
        ),
        "receiving_carrier_not_authority": statement.get(
            "receiving_carrier_not_authority"
        ),
        "source_not_created": statement.get("source_not_created"),
        "authority_not_created": statement.get("authority_not_created"),
        "currentness_not_created": statement.get("currentness_not_created"),
        "runtime_not_created": statement.get("runtime_not_created"),
        "deployment_not_created": statement.get("deployment_not_created"),
        "public_release_not_created": statement.get("public_release_not_created"),
        "operation_permission_not_created": statement.get(
            "operation_permission_not_created"
        ),
        "follow_on_work_not_authorized": statement.get(
            "follow_on_work_not_authorized"
        ),
        "hidden_repo_state_excluded": statement.get("hidden_repo_state_excluded"),
        "hidden_repo_state_not_used_as_final_completion_authority": statement.get(
            "hidden_repo_state_not_used_as_final_completion_authority"
        ),
        "repo_local_availability_not_final_completion_authority": statement.get(
            "repo_local_availability_not_final_completion_authority"
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
        "selected_final_completion_boundary_outcome": _summary_request_value(
            result, "selected_final_completion_boundary_result_outcome"
        ),
        "selected_final_completion_boundary_version": _summary_request_value(
            result, "selected_final_completion_boundary_result_version"
        ),
        "selected_final_completion_boundary_failed_check_count": _summary_request_value(
            result, "selected_final_completion_boundary_failed_check_count"
        ),
        "selected_portable_verification_closure_outcome": _summary_request_value(
            result, "selected_portable_verification_closure_result_outcome"
        ),
        "selected_portable_verification_closure_version": _summary_request_value(
            result, "selected_portable_verification_closure_result_version"
        ),
        "selected_portable_verification_closure_failed_check_count": _summary_request_value(
            result, "selected_portable_verification_closure_failed_check_count"
        ),
        "selected_returned_capture_intake_path": _summary_request_value(
            result, "selected_returned_capture_intake_path"
        ),
        "selected_returned_capture_zip_path": _summary_request_value(
            result, "selected_returned_capture_zip_path"
        ),
        "selected_returned_capture_hash_path": _summary_request_value(
            result, "selected_returned_capture_hash_path"
        ),
        "selected_returned_capture_extracted_directory_path": _summary_request_value(
            result, "selected_returned_capture_extracted_directory_path"
        ),
        "selected_returned_capture_exit_code": _summary_request_value(
            result, "selected_returned_capture_exit_code"
        ),
        "selected_returned_capture_declared_exit_code": _summary_request_value(
            result, "selected_returned_capture_declared_exit_code"
        ),
        "selected_returned_capture_ok_line": _summary_request_value(
            result, "selected_returned_capture_ok_line"
        ),
        "no_source_authority_currentness_runtime_deployment_public_release_follow_on": (
            non_claims.get("source_created") is False
            and non_claims.get("authority_created") is False
            and non_claims.get("currentness_created") is False
            and non_claims.get("runtime_hosting_created") is False
            and non_claims.get("deployment_created") is False
            and non_claims.get("public_release_created") is False
            and non_claims.get("follow_on_work_authorized") is False
        ),
        "key_non_claims": {
            "source_created": non_claims.get("source_created"),
            "authority_created": non_claims.get("authority_created"),
            "currentness_created": non_claims.get("currentness_created"),
            "string_zero_representation_turned_into_doctrine": non_claims.get(
                "string_zero_representation_turned_into_doctrine"
            ),
            "authorization_token_reused": non_claims.get("authorization_token_reused"),
            "consumed_request_reopened": non_claims.get("consumed_request_reopened"),
        },
        "predecessor_cross_carrier_evidence_failure_preserved": statement.get(
            "predecessor_cross_carrier_evidence_failure_preserved"
        ),
        "predecessor_external_result_v1_failure_preserved": statement.get(
            "predecessor_external_result_v1_failure_preserved"
        ),
        "first_success_boundary_test_preserved_as_failed_predecessor": statement.get(
            "first_success_boundary_test_failure_preserved"
        ),
        "v1_packet_emission_predecessor_failure_preserved": (
            non_claims.get("v1_packet_emission_repaired") is False
            and non_claims.get("v1_packet_emission_hidden") is False
            and non_claims.get("v1_packet_emission_claimed_passed") is False
        ),
        "first_result_boundary_resolver_preserved_as_failed_predecessor": statement.get(
            "first_result_boundary_resolver_failure_preserved"
        ),
    }
    return _sanitize_mapping(summary)


def _summary_request_value(result: Mapping[str, Any], key: str) -> Any:
    for section_name in SELECTED_BASIS_FIELDS:
        section = result.get(section_name)
        if isinstance(section, MappingABC) and key in section:
            return section.get(key)
    return None


def write_portable_source_body_verification_final_completion_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write a final-completion result JSON file without silent overwrite."""

    if not isinstance(result, MappingABC):
        raise PortableSourceBodyVerificationFinalCompletionError(
            "final-completion result must be a mapping"
        )
    metadata = result.get("portable_source_body_verification_final_completion_metadata", {})
    request_id = DEFAULT_REQUEST_ID
    if isinstance(metadata, MappingABC):
        value = metadata.get("portable_source_body_verification_final_completion_id")
        if isinstance(value, str) and value:
            request_id = value
    filename = f"{request_id}__portable_source_body_verification_final_completion_result.json"
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
            raise PortableSourceBodyVerificationFinalCompletionError(
                f"refusing to write final-completion result into prohibited root: {fragment}"
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


def build_declared_portable_source_body_verification_final_completion_request(
    final_completion_request_id: str = DEFAULT_REQUEST_ID,
    final_completion_question: str = CORE_QUESTION,
    final_completion_intent: str = INTENT_RECORD,
    final_completion_scope: Iterable[str] | None = None,
    declared_non_claims: Mapping[str, bool] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build a clean declared request for one bounded final-completion review."""

    non_claims = _safe_non_claims()
    if declared_non_claims is not None:
        non_claims.update(dict(declared_non_claims))
    scope = list(final_completion_scope or SUPPORTED_SCOPE_VALUES)
    request: dict[str, Any] = {
        "final_completion_request_id": final_completion_request_id,
        "final_completion_question": final_completion_question,
        "final_completion_intent": final_completion_intent,
        "final_completion_scope": scope,
        "declared_non_claims": non_claims,
        "requested_final_completion_outcome": OUTCOME_RECORDED,
        "selected_final_completion_boundary_basis": _reference_basis(
            "final_completion_boundary",
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_final_completion_boundary/portable_source_body_verification_final_completion_boundary_reference_review_001__portable_source_body_verification_final_completion_boundary_result.json",
            EXPECTED_FINAL_COMPLETION_BOUNDARY_OUTCOME,
            selected_final_completion_boundary_result_outcome=EXPECTED_FINAL_COMPLETION_BOUNDARY_OUTCOME,
            selected_final_completion_boundary_result_version=RESULT_VERSION,
            selected_final_completion_boundary_failed_check_count=0,
        ),
        "selected_final_completion_boundary_terminal_summary_basis": _reference_basis(
            "final_completion_boundary_terminal_summary",
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_BOUNDARY_TERMINAL_SUMMARY_V0.md",
        ),
        "selected_portable_verification_closure_basis": _reference_basis(
            "portable_verification_closure",
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_portable_verification_closure/portable_source_body_verification_portable_verification_closure_reference_review_001__portable_source_body_verification_portable_verification_closure_result.json",
            EXPECTED_PORTABLE_VERIFICATION_CLOSURE_OUTCOME,
            selected_portable_verification_closure_result_outcome=EXPECTED_PORTABLE_VERIFICATION_CLOSURE_OUTCOME,
            selected_portable_verification_closure_result_version=RESULT_VERSION,
            selected_portable_verification_closure_failed_check_count=0,
        ),
        "selected_portable_verification_closure_terminal_summary_basis": _reference_basis(
            "portable_verification_closure_terminal_summary",
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_PORTABLE_VERIFICATION_CLOSURE_TERMINAL_SUMMARY_V0.md",
        ),
        "selected_portable_verification_closure_boundary_basis": _reference_basis(
            "portable_verification_closure_boundary",
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TERMINAL_SUMMARY_V0.md",
        ),
        "selected_cross_carrier_evidence_basis": _reference_basis(
            "cross_carrier_evidence",
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_cross_carrier_evidence/portable_source_body_verification_cross_carrier_evidence_reference_review_001__portable_source_body_verification_cross_carrier_evidence_result.json",
            EXPECTED_CROSS_CARRIER_EVIDENCE_OUTCOME,
            selected_cross_carrier_evidence_result_outcome=EXPECTED_CROSS_CARRIER_EVIDENCE_OUTCOME,
            selected_cross_carrier_evidence_failed_check_count=0,
        ),
        "selected_cross_carrier_evidence_terminal_summary_basis": _reference_basis(
            "cross_carrier_evidence_terminal_summary",
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_CROSS_CARRIER_EVIDENCE_TERMINAL_SUMMARY_V0.md",
        ),
        "selected_second_carrier_external_result_basis": _reference_basis(
            "second_carrier_external_result",
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_external_result/portable_source_body_verification_second_carrier_external_result_reference_review_001__portable_source_body_verification_second_carrier_external_result_result.json",
            EXPECTED_SECOND_CARRIER_EXTERNAL_RESULT_OUTCOME,
            selected_second_carrier_external_result_result_outcome=EXPECTED_SECOND_CARRIER_EXTERNAL_RESULT_OUTCOME,
            selected_second_carrier_external_result_failed_check_count=0,
        ),
        "selected_second_carrier_external_result_terminal_summary_basis": _reference_basis(
            "second_carrier_external_result_terminal_summary",
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT_TERMINAL_SUMMARY_V0.md",
        ),
        "selected_second_carrier_verification_basis": _reference_basis(
            "second_carrier_verification",
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_verification/portable_source_body_verification_second_carrier_verification_reference_review_001__portable_source_body_verification_second_carrier_verification_result.json",
            EXPECTED_SECOND_CARRIER_VERIFICATION_OUTCOME,
        ),
        "selected_second_carrier_success_basis": _reference_basis(
            "second_carrier_success",
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_success/portable_source_body_verification_second_carrier_success_reference_review_001__portable_source_body_verification_second_carrier_success_result.json",
            EXPECTED_SECOND_CARRIER_SUCCESS_OUTCOME,
        ),
        "selected_second_carrier_result_basis": _reference_basis(
            "second_carrier_result",
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_result/portable_source_body_verification_second_carrier_result_reference_review_001__portable_source_body_verification_second_carrier_result_result.json",
            EXPECTED_SECOND_CARRIER_RESULT_OUTCOME,
        ),
        "selected_returned_second_carrier_live_capture_intake_basis": _reference_basis(
            "returned_second_carrier_live_capture_intake",
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_RETURNED_SECOND_CARRIER_LIVE_CAPTURE_INTAKE_V0.md",
            selected_returned_capture_intake_path="spec/PORTABLE_SOURCE_BODY_VERIFICATION_RETURNED_SECOND_CARRIER_LIVE_CAPTURE_INTAKE_V0.md",
            selected_returned_capture_intake_preserved=True,
            selected_returned_capture_intake_capture_only=True,
            selected_returned_capture_from_macbook_pro_to_macbook_air=True,
        ),
        "selected_returned_capture_material_basis": _reference_basis(
            "returned_capture_material",
            "artifacts/actual_second_carrier_live_capture/portable_source_body_verification_actual_second_carrier_capture_001",
            selected_returned_capture_zip_path="artifacts/actual_second_carrier_live_capture/portable_source_body_verification_actual_second_carrier_capture_001/original_zip/iammai_second_carrier_capture_001.zip",
            selected_returned_capture_hash_path="artifacts/actual_second_carrier_live_capture/portable_source_body_verification_actual_second_carrier_capture_001/hashes/iammai_second_carrier_capture_001.sha256",
            selected_returned_capture_extracted_directory_path="artifacts/actual_second_carrier_live_capture/portable_source_body_verification_actual_second_carrier_capture_001/extracted/iammai_second_carrier_capture_001",
            selected_returned_capture_combined_terminal_log_path="artifacts/actual_second_carrier_live_capture/portable_source_body_verification_actual_second_carrier_capture_001/extracted/iammai_second_carrier_capture_001/combined_terminal_log.txt",
            selected_returned_capture_stdout_path="artifacts/actual_second_carrier_live_capture/portable_source_body_verification_actual_second_carrier_capture_001/extracted/iammai_second_carrier_capture_001/stdout.txt",
            selected_returned_capture_stderr_path="artifacts/actual_second_carrier_live_capture/portable_source_body_verification_actual_second_carrier_capture_001/extracted/iammai_second_carrier_capture_001/stderr.txt",
            selected_returned_capture_command_text="python3 -m unittest tests/test_resolve_portable_source_body_verification_second_carrier_output_capture.py",
            selected_returned_capture_working_directory="/Users/markomarkota/Desktop/IAMMAI-SYSTEM",
            selected_returned_capture_started_at="2026-05-09T11:34:26Z",
            selected_returned_capture_completed_at="2026-05-09T11:34:27Z",
            selected_returned_capture_exit_code=0,
            selected_returned_capture_declared_exit_code="0",
            selected_returned_capture_ran_7_tests_line="Ran 7 tests in 0.451s",
            selected_returned_capture_ok_line="OK",
            selected_returned_capture_raw_placeholder_carrier_label="SECOND_DEVICE_LABEL_TO_FILL",
            selected_returned_capture_raw_placeholder_carrier_type="Mac/Linux/etc_TO_FILL",
            selected_returned_capture_placeholder_fields_unrepaired=True,
        ),
        "selected_second_carrier_output_capture_basis": _reference_basis(
            "second_carrier_output_capture",
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_output_capture/portable_source_body_verification_second_carrier_output_capture_reference_review_001__portable_source_body_verification_second_carrier_output_capture_result.json",
            EXPECTED_SECOND_CARRIER_OUTPUT_CAPTURE_OUTCOME,
            selected_second_carrier_output_capture_result_outcome=EXPECTED_SECOND_CARRIER_OUTPUT_CAPTURE_OUTCOME,
            selected_second_carrier_output_capture_failed_check_count=0,
        ),
        "selected_packet_transfer_basis": _reference_basis(
            "packet_transfer",
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_TRANSFER_TERMINAL_SUMMARY_V0.md",
        ),
        "selected_packet_emission_basis": _reference_basis(
            "packet_emission",
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_TERMINAL_SUMMARY_V0.md",
        ),
        "selected_command_success_basis": _reference_basis(
            "command_success",
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_TERMINAL_SUMMARY_V0.md",
        ),
        "selected_command_result_v2_basis": _reference_basis(
            "command_result_v2",
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_V2_TERMINAL_SUMMARY_V0.md",
        ),
        "selected_output_capture_v2_basis": _reference_basis(
            "output_capture_v2",
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_V2_TERMINAL_SUMMARY_V0.md",
        ),
        "selected_command_output_report_artifact_basis": _reference_basis(
            "command_output_report_artifact",
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_REPORT_ARTIFACT_TERMINAL_SUMMARY_V0.md",
        ),
        "selected_command_execution_basis": _reference_basis(
            "command_execution",
            "selected command execution lineage basis",
        ),
        "selected_command_report_lineage_basis": _reference_basis(
            "command_report_lineage",
            "selected command report lineage basis",
            command_report_lineage_not_current_report_artifact=True,
            command_report_lineage_not_source=True,
            command_report_lineage_not_authority=True,
            command_report_lineage_not_currentness=True,
        ),
        "selected_predecessor_failure_basis": {
            "predecessor_cross_carrier_evidence_failure_preserved": True,
            "predecessor_external_result_v1_failure_preserved": True,
            "first_success_boundary_test_failure_preserved": True,
            "first_result_boundary_resolver_failure_preserved": True,
            "v1_packet_emission_boundary_failure_preserved": True,
            "predecessor_cross_carrier_evidence_repaired": False,
            "predecessor_cross_carrier_evidence_hidden": False,
            "predecessor_cross_carrier_evidence_claimed_passed": False,
            "predecessor_external_result_v1_repaired": False,
            "predecessor_external_result_v1_hidden": False,
            "predecessor_external_result_v1_claimed_passed": False,
            "first_success_boundary_test_repaired": False,
            "first_success_boundary_test_hidden": False,
            "first_success_boundary_test_claimed_passed": False,
            "first_result_boundary_resolver_repaired": False,
            "first_result_boundary_resolver_hidden": False,
            "first_result_boundary_resolver_claimed_passed": False,
            "v1_packet_emission_repaired": False,
            "v1_packet_emission_hidden": False,
            "v1_packet_emission_claimed_passed": False,
        },
        "selected_evidence_manifest_basis": _reference_basis(
            "evidence_manifest",
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_EVIDENCE_MANIFEST_BOUNDARY_TERMINAL_SUMMARY_V0.md",
        ),
        "selected_artifact_containment_basis": _reference_basis(
            "artifact_containment",
            "selected artifact containment basis",
            raw_full_prior_artifact_body_not_returned=True,
            returned_result_containment_preserved=True,
        ),
        "selected_portable_verification_basis": _reference_basis(
            "portable_verification",
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_BOUNDARY_TERMINAL_SUMMARY_V0.md",
        ),
        "selected_final_completion_boundary_result_path": "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_final_completion_boundary/portable_source_body_verification_final_completion_boundary_reference_review_001__portable_source_body_verification_final_completion_boundary_result.json",
        "selected_final_completion_boundary_result_outcome": EXPECTED_FINAL_COMPLETION_BOUNDARY_OUTCOME,
        "selected_final_completion_boundary_result_version": RESULT_VERSION,
        "selected_final_completion_boundary_failed_check_count": 0,
        "selected_final_completion_boundary_declared_future_final_completion_review_step": True,
        "selected_final_completion_boundary_already_created_final_completion": False,
        "selected_final_completion_boundary_treated_boundary_as_final_completion": False,
        "selected_final_completion_boundary_zero_exit_code_not_final_completion": True,
        "selected_final_completion_boundary_string_zero_not_final_completion": True,
        "selected_final_completion_boundary_string_zero_turned_into_doctrine": False,
        "selected_final_completion_boundary_ok_not_final_completion": True,
        "selected_final_completion_boundary_ran_7_tests_not_final_completion": True,
        "selected_final_completion_boundary_returned_capture_not_final_completion": True,
        "selected_final_completion_boundary_official_enum_scope_strings_redacted": False,
        "selected_final_completion_boundary_predecessor_cross_carrier_evidence_failure_preserved": True,
        "selected_portable_verification_closure_result_path": "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_portable_verification_closure/portable_source_body_verification_portable_verification_closure_reference_review_001__portable_source_body_verification_portable_verification_closure_result.json",
        "selected_portable_verification_closure_result_outcome": EXPECTED_PORTABLE_VERIFICATION_CLOSURE_OUTCOME,
        "selected_portable_verification_closure_result_version": RESULT_VERSION,
        "selected_portable_verification_closure_failed_check_count": 0,
        "selected_portable_verification_closure_bounded_closure_recorded": True,
        "selected_portable_verification_closure_already_created_final_completion": False,
        "selected_portable_verification_closure_treated_as_final_completion": False,
        "selected_portable_verification_closure_treated_as_source": False,
        "selected_portable_verification_closure_treated_as_authority": False,
        "selected_portable_verification_closure_treated_as_currentness": False,
        "selected_portable_verification_closure_treated_as_runtime": False,
        "selected_portable_verification_closure_treated_as_deployment": False,
        "selected_portable_verification_closure_treated_as_public_release": False,
        "selected_portable_verification_closure_treated_as_operation_permission": False,
        "selected_portable_verification_closure_treated_as_follow_on_work": False,
        "selected_cross_carrier_evidence_result_path": "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_cross_carrier_evidence/portable_source_body_verification_cross_carrier_evidence_reference_review_001__portable_source_body_verification_cross_carrier_evidence_result.json",
        "selected_cross_carrier_evidence_result_outcome": EXPECTED_CROSS_CARRIER_EVIDENCE_OUTCOME,
        "selected_cross_carrier_evidence_failed_check_count": 0,
        "selected_second_carrier_external_result_result_path": "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_external_result/portable_source_body_verification_second_carrier_external_result_reference_review_001__portable_source_body_verification_second_carrier_external_result_result.json",
        "selected_second_carrier_external_result_result_outcome": EXPECTED_SECOND_CARRIER_EXTERNAL_RESULT_OUTCOME,
        "selected_second_carrier_external_result_failed_check_count": 0,
        "selected_second_carrier_verification_result_path": "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_verification/portable_source_body_verification_second_carrier_verification_reference_review_001__portable_source_body_verification_second_carrier_verification_result.json",
        "selected_second_carrier_verification_result_outcome": EXPECTED_SECOND_CARRIER_VERIFICATION_OUTCOME,
        "selected_second_carrier_success_result_path": "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_success/portable_source_body_verification_second_carrier_success_reference_review_001__portable_source_body_verification_second_carrier_success_result.json",
        "selected_second_carrier_success_result_outcome": EXPECTED_SECOND_CARRIER_SUCCESS_OUTCOME,
        "selected_second_carrier_result_result_path": "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_result/portable_source_body_verification_second_carrier_result_reference_review_001__portable_source_body_verification_second_carrier_result_result.json",
        "selected_second_carrier_result_result_outcome": EXPECTED_SECOND_CARRIER_RESULT_OUTCOME,
        "selected_returned_capture_intake_path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_RETURNED_SECOND_CARRIER_LIVE_CAPTURE_INTAKE_V0.md",
        "selected_returned_capture_intake_preserved": True,
        "selected_returned_capture_intake_capture_only": True,
        "selected_returned_capture_from_macbook_pro_to_macbook_air": True,
        "selected_returned_capture_zip_path": "artifacts/actual_second_carrier_live_capture/portable_source_body_verification_actual_second_carrier_capture_001/original_zip/iammai_second_carrier_capture_001.zip",
        "selected_returned_capture_hash_path": "artifacts/actual_second_carrier_live_capture/portable_source_body_verification_actual_second_carrier_capture_001/hashes/iammai_second_carrier_capture_001.sha256",
        "selected_returned_capture_extracted_directory_path": "artifacts/actual_second_carrier_live_capture/portable_source_body_verification_actual_second_carrier_capture_001/extracted/iammai_second_carrier_capture_001",
        "selected_returned_capture_combined_terminal_log_path": "artifacts/actual_second_carrier_live_capture/portable_source_body_verification_actual_second_carrier_capture_001/extracted/iammai_second_carrier_capture_001/combined_terminal_log.txt",
        "selected_returned_capture_stdout_path": "artifacts/actual_second_carrier_live_capture/portable_source_body_verification_actual_second_carrier_capture_001/extracted/iammai_second_carrier_capture_001/stdout.txt",
        "selected_returned_capture_stderr_path": "artifacts/actual_second_carrier_live_capture/portable_source_body_verification_actual_second_carrier_capture_001/extracted/iammai_second_carrier_capture_001/stderr.txt",
        "selected_returned_capture_command_text": "python3 -m unittest tests/test_resolve_portable_source_body_verification_second_carrier_output_capture.py",
        "selected_returned_capture_working_directory": "/Users/markomarkota/Desktop/IAMMAI-SYSTEM",
        "selected_returned_capture_started_at": "2026-05-09T11:34:26Z",
        "selected_returned_capture_completed_at": "2026-05-09T11:34:27Z",
        "selected_returned_capture_exit_code": 0,
        "selected_returned_capture_declared_exit_code": "0",
        "selected_returned_capture_ran_7_tests_line": "Ran 7 tests in 0.451s",
        "selected_returned_capture_ok_line": "OK",
        "selected_returned_capture_raw_placeholder_carrier_label": "SECOND_DEVICE_LABEL_TO_FILL",
        "selected_returned_capture_raw_placeholder_carrier_type": "Mac/Linux/etc_TO_FILL",
        "selected_returned_capture_placeholder_fields_unrepaired": True,
        "selected_second_carrier_output_capture_result_path": "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_output_capture/portable_source_body_verification_second_carrier_output_capture_reference_review_001__portable_source_body_verification_second_carrier_output_capture_result.json",
        "selected_second_carrier_output_capture_result_outcome": EXPECTED_SECOND_CARRIER_OUTPUT_CAPTURE_OUTCOME,
        "selected_second_carrier_output_capture_failed_check_count": 0,
        "predecessor_cross_carrier_evidence_failure_preserved": True,
        "predecessor_external_result_v1_failure_preserved": True,
        "reference_shaped_input_posture": True,
        "additional_basis_context": [],
        "not_recorded_basis": [],
        "block_reason": None,
    }
    for posture_field in POSTURE_FIELDS:
        request[posture_field] = _posture(posture_field)
    request.update(overrides)
    return copy.deepcopy(request)
