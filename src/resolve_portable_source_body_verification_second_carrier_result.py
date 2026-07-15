"""Resolve portable source-body verification second-carrier result.

This resolver is downstream of the clean second-carrier-result-boundary-v2
line. It records one bounded second-carrier result posture only. It does not
create second-carrier success, external result, cross-carrier evidence, source
transfer, source receipt, reception authorization, source, authority,
currentness, final completion, runtime, continuation, reusable permission,
derivative reception, vessel relation, another reception request, or follow-on
work.

The resolver preserves the first result-boundary resolver and v1
packet-emission-boundary resolver as predecessor failure evidence. It also
keeps official enum, scope, outcome, block-code, posture, section, and boolean
field strings unredacted while containing hostile raw body payload values.
"""

from __future__ import annotations

import copy
import datetime
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any


class PortableSourceBodyVerificationSecondCarrierResultError(Exception):
    """Bounded resolver error for explicit unreadable or malformed inputs."""


RESOLVER_MODULE = "resolve_portable_source_body_verification_second_carrier_result"
RESULT_TYPE = "portable_source_body_verification_second_carrier_result"
RESULT_VERSION = "0.1.0"
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_portable_source_body_verification_"
    "second_carrier_result"
)

CORE_QUESTION = (
    "Can the clean second-carrier-result-boundary-v2 basis be used to record "
    "one bounded second-carrier result from the preserved returned "
    "second-carrier capture without creating second-carrier success, external "
    "result, cross-carrier evidence, source transfer, source receipt, "
    "reception authorization, source, authority, currentness, runtime, final "
    "completion, continuation, reusable permission, derivative reception, "
    "vessel relation, another reception request, or follow-on work?"
)

OUTCOME_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RESULT_RECORDED"
OUTCOME_NOT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RESULT_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RESULT_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RESULT_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RESULT"
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RESULT"
)
INTENT_BLOCK = "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RESULT"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

EXPECTED_BOUNDARY_V2_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RESULT_BOUNDARY_RECORDED"
)
EXPECTED_BOUNDARY_V2_VERSION = "0.2.0"
EXPECTED_OUTPUT_CAPTURE_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_OUTPUT_CAPTURE_RECORDED"
)

SUPPORTED_SCOPE_VALUES = (
    "SECOND_CARRIER_RESULT_SPEC_ONLY",
    "ONE_BOUNDED_SECOND_CARRIER_RESULT_RECORDED",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_BASIS_PRESERVED",
    "RETURNED_SECOND_CARRIER_CAPTURE_BASIS_PRESERVED",
    "CAPTURE_INTAKE_BASIS_PRESERVED",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_PRESERVED",
    "CAPTURE_ARTIFACT_BASIS_PRESERVED",
    "RESULT_RECORDED_BOUNDED",
    "RESULT_ARTIFACT_RECORDED_OR_BOUNDED",
    "RESULT_NOT_SUCCESS",
    "RESULT_NOT_VERIFICATION",
    "RESULT_NOT_EXTERNAL_RESULT",
    "RESULT_NOT_CROSS_CARRIER_EVIDENCE",
    "RESULT_NOT_SOURCE_TRANSFER",
    "RESULT_NOT_SOURCE_RECEIPT",
    "RESULT_NOT_RECEPTION_AUTHORIZATION",
    "ZERO_EXIT_CODE_NOT_SUCCESS",
    "OK_OUTPUT_NOT_VERIFICATION",
    "RAN_7_TESTS_NOT_CROSS_CARRIER_PROOF",
    "RETURNED_CAPTURE_NOT_CROSS_CARRIER_PROOF",
    "SECOND_CARRIER_SUCCESS_NOT_CREATED",
    "EXTERNAL_RESULT_NOT_CREATED",
    "CROSS_CARRIER_EVIDENCE_NOT_CREATED",
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
    "NO_SUCCESS_INFERENCE",
    "NO_VERIFICATION_INFERENCE",
    "NO_EXTERNAL_RESULT_INFERENCE",
    "NO_CROSS_CARRIER_EVIDENCE_INFERENCE",
    "NO_SOURCE_INFERENCE",
    "NO_AUTHORITY_INFERENCE",
    "NO_CURRENTNESS_INFERENCE",
    "NO_FINAL_COMPLETION_INFERENCE",
    "NO_RUNTIME_INFERENCE",
    "NO_FOLLOW_ON_WORK_INFERENCE",
    "NO_UNBOUNDED_PASS_FAIL_INFERENCE",
    "HIDDEN_REPO_STATE_EXCLUDED",
    "HIDDEN_REPO_STATE_NOT_USED_AS_RESULT_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_NOT_RESULT_AUTHORITY",
    "SELECTED_BASIS_REFERENCE_SHAPE_PRESERVED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
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
SUPPORTED_SECOND_CARRIER_RESULT_SCOPE = SUPPORTED_SCOPE_VALUES

SELECTED_BASIS_KEYS = (
    "selected_second_carrier_result_boundary_v2_basis",
    "selected_second_carrier_result_boundary_v2_terminal_summary_basis",
    "selected_returned_second_carrier_live_capture_intake_basis",
    "selected_returned_capture_material_basis",
    "selected_returned_zip_basis",
    "selected_returned_hash_basis",
    "selected_returned_extracted_files_basis",
    "selected_returned_combined_terminal_log_basis",
    "selected_returned_exit_code_basis",
    "selected_returned_command_text_basis",
    "selected_returned_timestamps_basis",
    "selected_second_carrier_output_capture_basis",
    "selected_second_carrier_output_capture_terminal_summary_basis",
    "selected_second_carrier_output_capture_boundary_basis",
    "selected_second_carrier_execution_output_basis",
    "selected_second_carrier_execution_basis",
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
    "second_carrier_result_spec_only_posture",
    "one_bounded_second_carrier_result_posture",
    "second_carrier_result_boundary_v2_basis_preserved_posture",
    "returned_second_carrier_capture_basis_preserved_posture",
    "capture_intake_basis_preserved_posture",
    "second_carrier_output_capture_basis_preserved_posture",
    "capture_artifact_basis_preserved_posture",
    "result_recorded_bounded_posture",
    "result_artifact_recorded_or_bounded_posture",
    "result_not_success_posture",
    "result_not_verification_posture",
    "result_not_external_result_posture",
    "result_not_cross_carrier_evidence_posture",
    "result_not_source_transfer_posture",
    "result_not_source_receipt_posture",
    "result_not_reception_authorization_posture",
    "zero_exit_code_not_success_posture",
    "ok_output_not_verification_posture",
    "ran_7_tests_not_cross_carrier_proof_posture",
    "returned_capture_not_cross_carrier_proof_posture",
    "second_carrier_success_not_created_posture",
    "external_result_not_created_posture",
    "cross_carrier_evidence_not_created_posture",
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
    "repo_local_availability_not_result_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "first_result_boundary_resolver_failure_preserved_posture",
)

REQUIRED_FALSE_NON_CLAIMS = (
    "second_carrier_success_created",
    "external_result_created",
    "cross_carrier_evidence_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "second_carrier_result_treated_as_success",
    "second_carrier_result_treated_as_verification",
    "second_carrier_result_treated_as_external_result",
    "second_carrier_result_treated_as_cross_carrier_evidence",
    "second_carrier_result_treated_as_source_transfer",
    "second_carrier_result_treated_as_source_receipt",
    "second_carrier_result_treated_as_reception_authorization",
    "second_carrier_result_treated_as_source",
    "second_carrier_result_treated_as_authority",
    "second_carrier_result_treated_as_currentness",
    "second_carrier_result_treated_as_final_completion",
    "second_carrier_result_treated_as_runtime",
    "second_carrier_result_treated_as_continuation",
    "second_carrier_result_treated_as_reusable_permission",
    "second_carrier_result_treated_as_follow_on_work",
    "zero_exit_code_treated_as_success",
    "ok_output_treated_as_verification",
    "ran_7_tests_treated_as_cross_carrier_proof",
    "returned_capture_treated_as_cross_carrier_evidence",
    "receiving_carrier_treated_as_authority",
    "artifact_existence_treated_as_result_authority",
    "artifact_path_treated_as_currentness",
    "repo_local_availability_treated_as_result_authority",
    "hidden_repo_state_used_as_result_content",
    "hidden_repo_state_used_as_result_authority",
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
    "consumed_request_reopened",
    "authorization_token_reused",
    "v1_repaired",
    "v1_hidden",
    "v1_claimed_passed",
    "first_result_boundary_resolver_repaired",
    "first_result_boundary_resolver_hidden",
    "first_result_boundary_resolver_claimed_passed",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "second_carrier_result_recorded",
    "bounded_second_carrier_result_recorded",
    "result_artifact_recorded_or_bounded",
    "second_carrier_result_boundary_v2_basis_preserved",
    "returned_second_carrier_capture_basis_preserved",
    "capture_intake_basis_preserved",
    "second_carrier_output_capture_basis_preserved",
    "capture_artifact_basis_preserved",
    "result_recorded_bounded",
    "result_not_success",
    "result_not_verification",
    "result_not_external_result",
    "result_not_cross_carrier_evidence",
    "result_not_source_transfer",
    "result_not_source_receipt",
    "result_not_reception_authorization",
    "zero_exit_code_not_success",
    "ok_output_not_verification",
    "ran_7_tests_not_cross_carrier_proof",
    "returned_capture_not_cross_carrier_proof",
    "second_carrier_success_not_created",
    "external_result_not_created",
    "cross_carrier_evidence_not_created",
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
    "hidden_repo_state_not_used_as_result_authority",
    "repo_local_availability_not_result_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "official_enum_scope_strings_not_redacted",
    "hostile_raw_body_content_contained",
    "first_result_boundary_resolver_failure_preserved",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
)

BLOCK_CODES = (
    "DECLARED_SECOND_CARRIER_RESULT_REQUEST_MALFORMED",
    "DECLARED_SECOND_CARRIER_RESULT_REQUEST_UNREADABLE",
    "SECOND_CARRIER_RESULT_QUESTION_UNDECLARED",
    "SECOND_CARRIER_RESULT_INTENT_UNSUPPORTED",
    "SECOND_CARRIER_RESULT_BLOCK_REQUESTED",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_BASIS_MISSING",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_NOT_RECORDED",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_VERSION_NOT_0_2_0",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_DID_NOT_DECLARE_FUTURE_RESULT_STEP",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_ALREADY_CREATED_RESULT",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_ALREADY_CREATED_SUCCESS",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_ALREADY_CREATED_EXTERNAL_RESULT",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_ALREADY_CREATED_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_TREATED_ZERO_EXIT_CODE_AS_SUCCESS",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_TREATED_OK_AS_VERIFICATION",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_TREATED_RETURNED_CAPTURE_AS_CROSS_CARRIER_PROOF",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
    "RETURNED_CAPTURE_INTAKE_BASIS_MISSING",
    "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
    "RETURNED_CAPTURE_TREATED_AS_RESULT",
    "RETURNED_CAPTURE_TREATED_AS_SUCCESS",
    "RETURNED_CAPTURE_TREATED_AS_VERIFICATION",
    "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_PROOF",
    "ZERO_EXIT_CODE_TREATED_AS_SUCCESS",
    "OK_OUTPUT_TREATED_AS_VERIFICATION",
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
    "SECOND_CARRIER_OUTPUT_CAPTURE_DID_NOT_RECORD_BOUNDED_CAPTURE",
    "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_RESULT",
    "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_SUCCESS",
    "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_RESULT_TREATED_AS_SUCCESS",
    "SECOND_CARRIER_RESULT_TREATED_AS_VERIFICATION",
    "SECOND_CARRIER_RESULT_TREATED_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_RESULT_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_RESULT_TREATED_AS_SOURCE_TRANSFER",
    "SECOND_CARRIER_RESULT_TREATED_AS_SOURCE_RECEIPT",
    "SECOND_CARRIER_RESULT_TREATED_AS_RECEPTION_AUTHORIZATION",
    "SECOND_CARRIER_RESULT_TREATED_AS_SOURCE",
    "SECOND_CARRIER_RESULT_TREATED_AS_AUTHORITY",
    "SECOND_CARRIER_RESULT_TREATED_AS_CURRENTNESS",
    "SECOND_CARRIER_RESULT_TREATED_AS_FINAL_COMPLETION",
    "SECOND_CARRIER_RESULT_TREATED_AS_RUNTIME",
    "SECOND_CARRIER_RESULT_TREATED_AS_CONTINUATION",
    "SECOND_CARRIER_RESULT_TREATED_AS_REUSABLE_PERMISSION",
    "SECOND_CARRIER_RESULT_TREATED_AS_FOLLOW_ON_WORK",
    "SECOND_CARRIER_SUCCESS_CREATED",
    "EXTERNAL_RESULT_CREATED",
    "CROSS_CARRIER_EVIDENCE_CREATED",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_RESULT_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_RESULT_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_RESULT_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_RESULT_AUTHORITY",
    "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "FIRST_RESULT_BOUNDARY_RESOLVER_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENT_REPORT_ARTIFACT",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_SOURCE",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_AUTHORITY",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENTNESS",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_RESULT",
    "ARTIFACTS_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_SECOND_CARRIER_RESULT_SCOPE",
)

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_result_body",
    "raw_output_body",
    "raw_capture_body",
    "capture_body",
    "second_carrier_result_body",
    "external_result_body",
    "cross_carrier_evidence_body",
    "source_body",
    "authority_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
}

HOSTILE_SENTINELS = (
    "RAW_SECOND_CARRIER_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
    "HOSTILE_SECOND_CARRIER_RESULT_FULL_BODY_VALUE_MUST_NOT_RETURN",
)

NON_CLAIM_BLOCK_CODE_BY_KEY = {
    "second_carrier_success_created": "SECOND_CARRIER_SUCCESS_CREATED",
    "external_result_created": "EXTERNAL_RESULT_CREATED",
    "cross_carrier_evidence_created": "CROSS_CARRIER_EVIDENCE_CREATED",
    "source_transfer_occurred": "SOURCE_TRANSFER_OCCURRED",
    "source_receipt_occurred": "SOURCE_RECEIPT_OCCURRED",
    "reception_authorization_created": "RECEPTION_AUTHORIZATION_CREATED",
    "second_carrier_result_treated_as_success": "SECOND_CARRIER_RESULT_TREATED_AS_SUCCESS",
    "second_carrier_result_treated_as_verification": "SECOND_CARRIER_RESULT_TREATED_AS_VERIFICATION",
    "second_carrier_result_treated_as_external_result": "SECOND_CARRIER_RESULT_TREATED_AS_EXTERNAL_RESULT",
    "second_carrier_result_treated_as_cross_carrier_evidence": "SECOND_CARRIER_RESULT_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "second_carrier_result_treated_as_source_transfer": "SECOND_CARRIER_RESULT_TREATED_AS_SOURCE_TRANSFER",
    "second_carrier_result_treated_as_source_receipt": "SECOND_CARRIER_RESULT_TREATED_AS_SOURCE_RECEIPT",
    "second_carrier_result_treated_as_reception_authorization": "SECOND_CARRIER_RESULT_TREATED_AS_RECEPTION_AUTHORIZATION",
    "second_carrier_result_treated_as_source": "SECOND_CARRIER_RESULT_TREATED_AS_SOURCE",
    "second_carrier_result_treated_as_authority": "SECOND_CARRIER_RESULT_TREATED_AS_AUTHORITY",
    "second_carrier_result_treated_as_currentness": "SECOND_CARRIER_RESULT_TREATED_AS_CURRENTNESS",
    "second_carrier_result_treated_as_final_completion": "SECOND_CARRIER_RESULT_TREATED_AS_FINAL_COMPLETION",
    "second_carrier_result_treated_as_runtime": "SECOND_CARRIER_RESULT_TREATED_AS_RUNTIME",
    "second_carrier_result_treated_as_continuation": "SECOND_CARRIER_RESULT_TREATED_AS_CONTINUATION",
    "second_carrier_result_treated_as_reusable_permission": "SECOND_CARRIER_RESULT_TREATED_AS_REUSABLE_PERMISSION",
    "second_carrier_result_treated_as_follow_on_work": "SECOND_CARRIER_RESULT_TREATED_AS_FOLLOW_ON_WORK",
    "zero_exit_code_treated_as_success": "ZERO_EXIT_CODE_TREATED_AS_SUCCESS",
    "ok_output_treated_as_verification": "OK_OUTPUT_TREATED_AS_VERIFICATION",
    "ran_7_tests_treated_as_cross_carrier_proof": "RAN_7_TESTS_TREATED_AS_CROSS_CARRIER_PROOF",
    "returned_capture_treated_as_cross_carrier_evidence": "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_PROOF",
    "receiving_carrier_treated_as_authority": "RECEIVING_CARRIER_TREATED_AS_AUTHORITY",
    "artifact_existence_treated_as_result_authority": "ARTIFACT_EXISTENCE_TREATED_AS_RESULT_AUTHORITY",
    "artifact_path_treated_as_currentness": "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "repo_local_availability_treated_as_result_authority": "REPO_LOCAL_AVAILABILITY_TREATED_AS_RESULT_AUTHORITY",
    "hidden_repo_state_used_as_result_content": "HIDDEN_REPO_STATE_USED_AS_RESULT_CONTENT",
    "hidden_repo_state_used_as_result_authority": "HIDDEN_REPO_STATE_USED_AS_RESULT_AUTHORITY",
    "source_created": "SOURCE_CREATED",
    "authority_created": "AUTHORITY_CREATED",
    "currentness_created": "CURRENTNESS_CREATED",
    "final_completion_claimed": "FINAL_COMPLETION_CLAIMED",
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
    "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
    "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
    "v1_repaired": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "v1_hidden": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "v1_claimed_passed": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "first_result_boundary_resolver_repaired": "FIRST_RESULT_BOUNDARY_RESOLVER_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    "first_result_boundary_resolver_hidden": "FIRST_RESULT_BOUNDARY_RESOLVER_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    "first_result_boundary_resolver_claimed_passed": "FIRST_RESULT_BOUNDARY_RESOLVER_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
}

OFFICIAL_STRINGS = set(SUPPORTED_SCOPE_VALUES) | set(OUTCOME_FAMILY) | set(BLOCK_CODES)
OFFICIAL_STRINGS.update(REQUIRED_FALSE_NON_CLAIMS)
OFFICIAL_STRINGS.update(ALLOWED_TRUE_RECORDED_FIELDS)
OFFICIAL_STRINGS.update(SELECTED_BASIS_KEYS)
OFFICIAL_STRINGS.update(POSTURE_KEYS)
OFFICIAL_STRINGS.update(SUPPORTED_INTENTS)
OFFICIAL_STRINGS.update(
    {
        RESOLVER_MODULE,
        RESULT_VERSION,
        CORE_QUESTION,
        EXPECTED_BOUNDARY_V2_OUTCOME,
        EXPECTED_OUTPUT_CAPTURE_OUTCOME,
    }
)


def _utc_now() -> str:
    return (
        datetime.datetime.now(datetime.timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def _is_present(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (Mapping, Sequence)) and not isinstance(
        value, (str, bytes, bytearray)
    ):
        return bool(value)
    return True


def _as_bool(value: Any, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return default
    if isinstance(value, str):
        lowered = value.strip().lower()
        if lowered in {"true", "yes", "1", "recorded", "preserved", "declared"}:
            return True
        if lowered in {"false", "no", "0", "missing", "blocked"}:
            return False
    return bool(value)


def _as_int(value: Any) -> int | None:
    if isinstance(value, bool) or value is None:
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value.strip())
        except ValueError:
            return None
    return None


def _is_sensitive_key(key: str) -> bool:
    lowered = key.lower()
    return lowered in SENSITIVE_CONTENT_KEYS or lowered.endswith("_body")


def _sanitize(value: Any, parent_key: str | None = None) -> Any:
    if isinstance(value, Mapping):
        sanitized: dict[str, Any] = {}
        for key, item in value.items():
            key_text = str(key)
            if _is_sensitive_key(key_text):
                sanitized[key_text] = "[bounded-second-carrier-result-redacted-raw-body]"
            else:
                sanitized[key_text] = _sanitize(item, key_text)
        return sanitized
    if isinstance(value, list):
        return [_sanitize(item, parent_key) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item, parent_key) for item in value]
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, str):
        if value in OFFICIAL_STRINGS:
            return value
        if any(sentinel in value for sentinel in HOSTILE_SENTINELS):
            return "[bounded-second-carrier-result-redacted-raw-body]"
    return value


def _json_safe(value: Any) -> Any:
    return json.loads(json.dumps(_sanitize(value), sort_keys=True, default=str))


def _false_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _request_non_claims(request: Mapping[str, Any]) -> dict[str, Any]:
    supplied = request.get("declared_non_claims")
    if not isinstance(supplied, Mapping):
        return {}
    return {str(key): supplied[key] for key in supplied}


def _declared_non_claims_false(request: Mapping[str, Any]) -> dict[str, bool]:
    supplied = _request_non_claims(request)
    result = _false_non_claims()
    for key in REQUIRED_FALSE_NON_CLAIMS:
        if key in supplied:
            result[key] = _as_bool(supplied[key])
    return result


def _negative_flag(request: Mapping[str, Any], key: str) -> bool:
    supplied = _request_non_claims(request)
    if key in supplied:
        return _as_bool(supplied.get(key))
    return _as_bool(request.get(key))


def _basis_supplied(request: Mapping[str, Any], key: str) -> bool:
    return _is_present(request.get(key))


def _scope_values(request: Mapping[str, Any]) -> list[str]:
    supplied = request.get("second_carrier_result_scope")
    if supplied is None:
        return []
    if isinstance(supplied, str):
        return [supplied]
    if isinstance(supplied, Sequence) and not isinstance(
        supplied, (str, bytes, bytearray)
    ):
        return [str(item) for item in supplied]
    return [str(supplied)]


def _unsupported_scope_values(request: Mapping[str, Any]) -> list[str]:
    supported = set(SUPPORTED_SCOPE_VALUES)
    return [value for value in _scope_values(request) if value not in supported]


def _serialized_contains_hostile_sentinel(value: Any) -> bool:
    serialized = json.dumps(_sanitize(value), sort_keys=True, default=str)
    return any(sentinel in serialized for sentinel in HOSTILE_SENTINELS)


def _check(
    check_name: str,
    passed: bool,
    expected_posture: str,
    actual_posture: Any,
    code: str,
) -> dict[str, Any]:
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": expected_posture,
        "actual_posture": _sanitize(actual_posture),
        "block_code": None if passed else code,
        "failure_code": None if passed else code,
    }


def _selected_basis(
    request: Mapping[str, Any],
    basis_key: str,
    extra: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    section: dict[str, Any] = {
        "basis_key": basis_key,
        "basis_declared": _basis_supplied(request, basis_key),
        "basis": _sanitize(request.get(basis_key)),
        "basis_role": "reference-shaped second-carrier result basis only",
        "does_not_create_success": True,
        "does_not_create_external_result": True,
        "does_not_create_cross_carrier_evidence": True,
        "does_not_create_source_transfer": True,
        "does_not_create_source_receipt": True,
        "does_not_create_reception_authorization": True,
        "does_not_create_source_authority_currentness_runtime_or_final_completion": True,
        "does_not_authorize_follow_on_work": True,
    }
    if extra:
        section.update(_sanitize(dict(extra)))
    return section


def _posture(request: Mapping[str, Any], key: str, expected: str) -> dict[str, Any]:
    return {
        "posture_key": key,
        "declared": _as_bool(request.get(key)),
        "expected_posture": expected,
        "actual_posture": _sanitize(request.get(key)),
        "posture_role": "bounded second-carrier-result posture only",
    }


def _basis_missing_code(key: str) -> str:
    mapping = {
        "selected_second_carrier_result_boundary_v2_basis": "SECOND_CARRIER_RESULT_BOUNDARY_V2_BASIS_MISSING",
        "selected_second_carrier_result_boundary_v2_terminal_summary_basis": "SECOND_CARRIER_RESULT_BOUNDARY_V2_BASIS_MISSING",
        "selected_returned_second_carrier_live_capture_intake_basis": "RETURNED_CAPTURE_INTAKE_BASIS_MISSING",
        "selected_returned_capture_material_basis": "RETURNED_CAPTURE_MATERIAL_MISSING",
        "selected_returned_zip_basis": "RETURNED_ZIP_PATH_MISSING",
        "selected_returned_hash_basis": "RETURNED_HASH_PATH_MISSING",
        "selected_returned_extracted_files_basis": "RETURNED_EXTRACTED_DIRECTORY_MISSING",
        "selected_returned_combined_terminal_log_basis": "RETURNED_COMBINED_TERMINAL_LOG_MISSING",
        "selected_returned_exit_code_basis": "RETURNED_EXIT_CODE_MISSING",
        "selected_returned_command_text_basis": "RETURNED_COMMAND_TEXT_MISSING",
        "selected_returned_timestamps_basis": "RETURNED_TIMESTAMPS_MISSING",
        "selected_second_carrier_output_capture_basis": "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_MISSING",
        "selected_second_carrier_output_capture_terminal_summary_basis": "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_MISSING",
        "selected_second_carrier_output_capture_boundary_basis": "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_MISSING",
    }
    return mapping.get(key, "SELECTED_BASIS_NOT_REFERENCE_SHAPED")


def _build_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    def add(name: str, passed: bool, expected: str, actual: Any, code: str) -> None:
        checks.append(_check(name, passed, expected, actual, code))

    boundary_failed_count = _as_int(
        request.get("selected_second_carrier_result_boundary_v2_failed_check_count")
    )
    output_capture_failed_count = _as_int(
        request.get("selected_second_carrier_output_capture_failed_check_count")
    )

    add(
        "second_carrier_result_question_declared",
        request.get("second_carrier_result_question") == CORE_QUESTION,
        CORE_QUESTION,
        request.get("second_carrier_result_question"),
        "SECOND_CARRIER_RESULT_QUESTION_UNDECLARED",
    )
    add(
        "second_carrier_result_intent_supported",
        request.get("second_carrier_result_intent") in SUPPORTED_INTENTS,
        "supported second-carrier-result intent",
        request.get("second_carrier_result_intent"),
        "SECOND_CARRIER_RESULT_INTENT_UNSUPPORTED",
    )
    add(
        "second_carrier_result_scope_declared",
        bool(_scope_values(request)),
        "second-carrier result scope declared",
        _scope_values(request),
        "UNSUPPORTED_SECOND_CARRIER_RESULT_SCOPE",
    )
    add(
        "second_carrier_result_scope_supported",
        not _unsupported_scope_values(request),
        "official supported scope enum values preserved and accepted",
        _unsupported_scope_values(request),
        "UNSUPPORTED_SECOND_CARRIER_RESULT_SCOPE",
    )
    add(
        "official_scope_raw_full_prior_artifact_body_not_returned_preserved",
        "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED" in _scope_values(request),
        "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED remains official scope enum",
        _scope_values(request),
        "UNSUPPORTED_SECOND_CARRIER_RESULT_SCOPE",
    )
    add(
        "official_scope_returned_result_containment_preserved",
        "RETURNED_RESULT_CONTAINMENT_PRESERVED" in _scope_values(request),
        "RETURNED_RESULT_CONTAINMENT_PRESERVED remains official scope enum",
        _scope_values(request),
        "UNSUPPORTED_SECOND_CARRIER_RESULT_SCOPE",
    )
    add(
        "official_scope_values_not_redacted",
        "[bounded-second-carrier-result-redacted-raw-body]"
        not in set(_scope_values(request)),
        "official scope enum values are not redacted",
        _scope_values(request),
        "UNSUPPORTED_SECOND_CARRIER_RESULT_SCOPE",
    )

    for key in SELECTED_BASIS_KEYS:
        add(
            f"{key}_declared",
            _basis_supplied(request, key),
            f"{key} declared as reference-shaped basis",
            request.get(key),
            _basis_missing_code(key),
        )

    add(
        "second_carrier_result_boundary_v2_outcome_recorded",
        request.get("selected_second_carrier_result_boundary_v2_result_outcome")
        == EXPECTED_BOUNDARY_V2_OUTCOME,
        EXPECTED_BOUNDARY_V2_OUTCOME,
        request.get("selected_second_carrier_result_boundary_v2_result_outcome"),
        "SECOND_CARRIER_RESULT_BOUNDARY_V2_NOT_RECORDED",
    )
    add(
        "second_carrier_result_boundary_v2_version_0_2_0",
        request.get("selected_second_carrier_result_boundary_v2_result_version")
        == EXPECTED_BOUNDARY_V2_VERSION,
        EXPECTED_BOUNDARY_V2_VERSION,
        request.get("selected_second_carrier_result_boundary_v2_result_version"),
        "SECOND_CARRIER_RESULT_BOUNDARY_V2_VERSION_NOT_0_2_0",
    )
    add(
        "second_carrier_result_boundary_v2_failed_checks_zero",
        boundary_failed_count == 0,
        "second-carrier-result-boundary-v2 failed check count is zero",
        request.get("selected_second_carrier_result_boundary_v2_failed_check_count"),
        "SECOND_CARRIER_RESULT_BOUNDARY_V2_FAILED_CHECKS_PRESENT",
    )
    add(
        "second_carrier_result_boundary_v2_declared_future_result_step",
        _as_bool(
            request.get(
                "selected_second_carrier_result_boundary_v2_declared_future_result_step"
            )
        ),
        "second-carrier-result-boundary-v2 declared one future result step",
        request.get(
            "selected_second_carrier_result_boundary_v2_declared_future_result_step"
        ),
        "SECOND_CARRIER_RESULT_BOUNDARY_V2_DID_NOT_DECLARE_FUTURE_RESULT_STEP",
    )
    add(
        "second_carrier_result_boundary_v2_did_not_already_create_result",
        not _as_bool(
            request.get(
                "selected_second_carrier_result_boundary_v2_already_created_result"
            )
        ),
        "second-carrier-result-boundary-v2 did not already create result",
        request.get("selected_second_carrier_result_boundary_v2_already_created_result"),
        "SECOND_CARRIER_RESULT_BOUNDARY_V2_ALREADY_CREATED_RESULT",
    )
    add(
        "second_carrier_result_boundary_v2_did_not_already_create_success",
        not _as_bool(
            request.get(
                "selected_second_carrier_result_boundary_v2_already_created_success"
            )
        ),
        "second-carrier-result-boundary-v2 did not already create success",
        request.get("selected_second_carrier_result_boundary_v2_already_created_success"),
        "SECOND_CARRIER_RESULT_BOUNDARY_V2_ALREADY_CREATED_SUCCESS",
    )
    add(
        "second_carrier_result_boundary_v2_did_not_already_create_external_result",
        not _as_bool(
            request.get(
                "selected_second_carrier_result_boundary_v2_already_created_external_result"
            )
        ),
        "second-carrier-result-boundary-v2 did not already create external result",
        request.get(
            "selected_second_carrier_result_boundary_v2_already_created_external_result"
        ),
        "SECOND_CARRIER_RESULT_BOUNDARY_V2_ALREADY_CREATED_EXTERNAL_RESULT",
    )
    add(
        "second_carrier_result_boundary_v2_did_not_already_create_cross_carrier_evidence",
        not _as_bool(
            request.get(
                "selected_second_carrier_result_boundary_v2_already_created_cross_carrier_evidence"
            )
        ),
        "second-carrier-result-boundary-v2 did not already create cross-carrier evidence",
        request.get(
            "selected_second_carrier_result_boundary_v2_already_created_cross_carrier_evidence"
        ),
        "SECOND_CARRIER_RESULT_BOUNDARY_V2_ALREADY_CREATED_CROSS_CARRIER_EVIDENCE",
    )
    add(
        "second_carrier_result_boundary_v2_kept_zero_exit_code_not_success",
        _as_bool(
            request.get(
                "selected_second_carrier_result_boundary_v2_zero_exit_code_not_success"
            )
        ),
        "boundary-v2 kept zero exit code not success",
        request.get("selected_second_carrier_result_boundary_v2_zero_exit_code_not_success"),
        "SECOND_CARRIER_RESULT_BOUNDARY_V2_TREATED_ZERO_EXIT_CODE_AS_SUCCESS",
    )
    add(
        "second_carrier_result_boundary_v2_kept_ok_not_verification",
        _as_bool(
            request.get("selected_second_carrier_result_boundary_v2_ok_not_verification")
        ),
        "boundary-v2 kept OK not verification",
        request.get("selected_second_carrier_result_boundary_v2_ok_not_verification"),
        "SECOND_CARRIER_RESULT_BOUNDARY_V2_TREATED_OK_AS_VERIFICATION",
    )
    add(
        "second_carrier_result_boundary_v2_kept_returned_capture_not_cross_carrier_proof",
        _as_bool(
            request.get(
                "selected_second_carrier_result_boundary_v2_returned_capture_not_cross_carrier_proof"
            )
        ),
        "boundary-v2 kept returned capture not cross-carrier proof",
        request.get(
            "selected_second_carrier_result_boundary_v2_returned_capture_not_cross_carrier_proof"
        ),
        "SECOND_CARRIER_RESULT_BOUNDARY_V2_TREATED_RETURNED_CAPTURE_AS_CROSS_CARRIER_PROOF",
    )
    add(
        "second_carrier_result_boundary_v2_official_enum_scope_strings_not_redacted",
        not _as_bool(
            request.get(
                "selected_second_carrier_result_boundary_v2_official_enum_scope_strings_redacted"
            )
        )
        and _as_bool(
            request.get(
                "selected_second_carrier_result_boundary_v2_official_enum_scope_strings_not_redacted",
                True,
            ),
            default=True,
        ),
        "boundary-v2 official enum/scope strings not redacted",
        {
            "redacted": request.get(
                "selected_second_carrier_result_boundary_v2_official_enum_scope_strings_redacted"
            ),
            "not_redacted": request.get(
                "selected_second_carrier_result_boundary_v2_official_enum_scope_strings_not_redacted"
            ),
        },
        "SECOND_CARRIER_RESULT_BOUNDARY_V2_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
    )
    add(
        "second_carrier_result_boundary_v2_first_result_boundary_resolver_preserved",
        _as_bool(
            request.get(
                "selected_second_carrier_result_boundary_v2_first_result_boundary_resolver_preserved"
            )
        ),
        "boundary-v2 preserved first result-boundary resolver failure",
        request.get(
            "selected_second_carrier_result_boundary_v2_first_result_boundary_resolver_preserved"
        ),
        "FIRST_RESULT_BOUNDARY_RESOLVER_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    )

    add(
        "returned_capture_intake_preserved",
        _as_bool(request.get("selected_returned_capture_intake_preserved")),
        "returned capture intake preserved",
        request.get("selected_returned_capture_intake_preserved"),
        "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
    )
    add(
        "returned_capture_intake_capture_only",
        _as_bool(request.get("selected_returned_capture_intake_capture_only")),
        "returned capture intake says capture-only",
        request.get("selected_returned_capture_intake_capture_only"),
        "RETURNED_CAPTURE_TREATED_AS_RESULT",
    )
    add(
        "returned_capture_macbook_pro_to_macbook_air",
        _as_bool(request.get("selected_returned_capture_from_macbook_pro_to_macbook_air")),
        "MacBook Pro to MacBook Air return preserved",
        request.get("selected_returned_capture_from_macbook_pro_to_macbook_air"),
        "RETURNED_CAPTURE_INTAKE_BASIS_MISSING",
    )
    add(
        "returned_zip_path_present",
        _is_present(request.get("selected_returned_capture_zip_path"))
        or _basis_supplied(request, "selected_returned_zip_basis"),
        "returned zip path basis present",
        request.get("selected_returned_capture_zip_path"),
        "RETURNED_ZIP_PATH_MISSING",
    )
    add(
        "returned_hash_path_present",
        _is_present(request.get("selected_returned_capture_hash_path"))
        or _basis_supplied(request, "selected_returned_hash_basis"),
        "returned hash path basis present",
        request.get("selected_returned_capture_hash_path"),
        "RETURNED_HASH_PATH_MISSING",
    )
    add(
        "returned_extracted_directory_path_present",
        _is_present(request.get("selected_returned_capture_extracted_directory_path"))
        or _basis_supplied(request, "selected_returned_extracted_files_basis"),
        "returned extracted directory basis present",
        request.get("selected_returned_capture_extracted_directory_path"),
        "RETURNED_EXTRACTED_DIRECTORY_MISSING",
    )
    add(
        "returned_combined_terminal_log_path_present",
        _is_present(request.get("selected_returned_capture_combined_terminal_log_path"))
        or _basis_supplied(request, "selected_returned_combined_terminal_log_basis"),
        "returned combined terminal log basis present",
        request.get("selected_returned_capture_combined_terminal_log_path"),
        "RETURNED_COMBINED_TERMINAL_LOG_MISSING",
    )
    add(
        "returned_exit_code_present",
        request.get("selected_returned_capture_exit_code") is not None
        or _basis_supplied(request, "selected_returned_exit_code_basis"),
        "returned exit code basis present",
        request.get("selected_returned_capture_exit_code"),
        "RETURNED_EXIT_CODE_MISSING",
    )
    add(
        "returned_command_text_present",
        _is_present(request.get("selected_returned_capture_command_text"))
        or _basis_supplied(request, "selected_returned_command_text_basis"),
        "returned command text basis present",
        request.get("selected_returned_capture_command_text"),
        "RETURNED_COMMAND_TEXT_MISSING",
    )
    add(
        "returned_timestamps_present",
        _is_present(request.get("selected_returned_capture_started_at"))
        and _is_present(request.get("selected_returned_capture_completed_at")),
        "returned started and completed timestamps present",
        {
            "run_started_at": request.get("selected_returned_capture_started_at"),
            "run_completed_at": request.get("selected_returned_capture_completed_at"),
        },
        "RETURNED_TIMESTAMPS_MISSING",
    )
    add(
        "returned_working_directory_captured",
        _is_present(request.get("selected_returned_capture_working_directory")),
        "returned working directory captured",
        request.get("selected_returned_capture_working_directory"),
        "RETURNED_CAPTURE_MATERIAL_MISSING",
    )
    add(
        "returned_exit_code_zero_preserved_as_basis_not_success",
        str(request.get("selected_returned_capture_exit_code")) == "0"
        and _as_bool(request.get("selected_returned_capture_zero_exit_code_not_success"))
        and not _negative_flag(request, "zero_exit_code_treated_as_success"),
        "exit code 0 preserved as basis but not success",
        {
            "exit_code": request.get("selected_returned_capture_exit_code"),
            "not_success": request.get(
                "selected_returned_capture_zero_exit_code_not_success"
            ),
        },
        "ZERO_EXIT_CODE_TREATED_AS_SUCCESS",
    )
    add(
        "returned_ran_7_tests_preserved_as_basis_not_proof",
        "Ran 7 tests" in str(request.get("selected_returned_capture_ran_7_tests_line", ""))
        and not _negative_flag(request, "ran_7_tests_treated_as_cross_carrier_proof"),
        "Ran 7 tests preserved as basis but not cross-carrier proof",
        request.get("selected_returned_capture_ran_7_tests_line"),
        "RAN_7_TESTS_TREATED_AS_CROSS_CARRIER_PROOF",
    )
    add(
        "returned_ok_preserved_as_basis_not_verification",
        str(request.get("selected_returned_capture_ok_line", "")).strip() == "OK"
        and _as_bool(request.get("selected_returned_capture_ok_not_verification"))
        and not _negative_flag(request, "ok_output_treated_as_verification"),
        "OK preserved as basis but not verification",
        request.get("selected_returned_capture_ok_line"),
        "OK_OUTPUT_TREATED_AS_VERIFICATION",
    )
    add(
        "returned_capture_not_cross_carrier_proof",
        _as_bool(request.get("selected_returned_capture_not_cross_carrier_proof"))
        and not _negative_flag(request, "returned_capture_treated_as_cross_carrier_evidence"),
        "returned capture not cross-carrier proof",
        request.get("selected_returned_capture_not_cross_carrier_proof"),
        "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_PROOF",
    )
    add(
        "raw_placeholder_carrier_fields_preserved",
        _is_present(request.get("selected_returned_capture_raw_placeholder_carrier_label"))
        and _is_present(request.get("selected_returned_capture_raw_placeholder_carrier_type")),
        "raw placeholder carrier fields preserved",
        {
            "carrier_label": request.get(
                "selected_returned_capture_raw_placeholder_carrier_label"
            ),
            "carrier_type": request.get(
                "selected_returned_capture_raw_placeholder_carrier_type"
            ),
        },
        "PLACEHOLDER_CARRIER_FIELDS_REPAIRED",
    )
    add(
        "placeholder_fields_unrepaired",
        _as_bool(request.get("selected_returned_capture_placeholder_fields_unrepaired")),
        "placeholder fields unrepaired",
        request.get("selected_returned_capture_placeholder_fields_unrepaired"),
        "PLACEHOLDER_CARRIER_FIELDS_REPAIRED",
    )

    add(
        "second_carrier_output_capture_recorded",
        request.get("selected_second_carrier_output_capture_result_outcome")
        == EXPECTED_OUTPUT_CAPTURE_OUTCOME,
        EXPECTED_OUTPUT_CAPTURE_OUTCOME,
        request.get("selected_second_carrier_output_capture_result_outcome"),
        "SECOND_CARRIER_OUTPUT_CAPTURE_NOT_RECORDED",
    )
    add(
        "second_carrier_output_capture_failed_checks_zero",
        output_capture_failed_count == 0,
        "second-carrier output capture failed check count is zero",
        request.get("selected_second_carrier_output_capture_failed_check_count"),
        "SECOND_CARRIER_OUTPUT_CAPTURE_FAILED_CHECKS_PRESENT",
    )
    add(
        "second_carrier_output_capture_recorded_bounded_capture",
        _as_bool(
            request.get("selected_second_carrier_output_capture_bounded_capture_recorded")
        ),
        "second-carrier output capture recorded bounded capture",
        request.get("selected_second_carrier_output_capture_bounded_capture_recorded"),
        "SECOND_CARRIER_OUTPUT_CAPTURE_DID_NOT_RECORD_BOUNDED_CAPTURE",
    )
    for key, code, expected in (
        (
            "selected_second_carrier_output_capture_treated_capture_as_result",
            "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_RESULT",
            "second-carrier output capture did not treat capture as result",
        ),
        (
            "selected_second_carrier_output_capture_treated_capture_as_success",
            "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_SUCCESS",
            "second-carrier output capture did not treat capture as success",
        ),
        (
            "selected_second_carrier_output_capture_treated_capture_as_external_result",
            "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_EXTERNAL_RESULT",
            "second-carrier output capture did not treat capture as external result",
        ),
        (
            "selected_second_carrier_output_capture_treated_capture_as_cross_carrier_evidence",
            "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_CROSS_CARRIER_EVIDENCE",
            "second-carrier output capture did not treat capture as cross-carrier evidence",
        ),
    ):
        add(key, not _as_bool(request.get(key)), expected, request.get(key), code)

    add(
        "reference_shaped_input_posture",
        _as_bool(request.get("reference_shaped_input_posture"), default=True),
        "selected basis is reference-shaped",
        request.get("reference_shaped_input_posture"),
        "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    )
    add(
        "hostile_raw_body_content_contained",
        not _serialized_contains_hostile_sentinel(request),
        "hostile raw body sentinel content is contained by sanitizer",
        "sanitized request contains no hostile sentinels",
        "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_RESULT",
    )

    for key in POSTURE_KEYS:
        add(
            f"{key}_declared",
            _as_bool(request.get(key)),
            f"{key} declared",
            request.get(key),
            "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
        )

    supplied_non_claims = _request_non_claims(request)
    add(
        "required_non_claims_present",
        all(key in supplied_non_claims for key in REQUIRED_FALSE_NON_CLAIMS),
        "all required non-claims are declared",
        sorted(supplied_non_claims),
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    for key in REQUIRED_FALSE_NON_CLAIMS:
        add(
            f"{key}_false",
            key in supplied_non_claims and not _as_bool(supplied_non_claims.get(key)),
            f"{key} remains false",
            supplied_non_claims.get(key),
            NON_CLAIM_BLOCK_CODE_BY_KEY.get(key, "NON_CLAIM_MISSING_OR_FLIPPED"),
        )

    return checks


def _statement(outcome: str) -> dict[str, bool]:
    return {
        key: bool(outcome == OUTCOME_RECORDED) for key in ALLOWED_TRUE_RECORDED_FIELDS
    }


def _non_meaning() -> dict[str, bool]:
    meanings = (
        "second_carrier_success_exists",
        "external_result_exists",
        "cross_carrier_evidence_exists",
        "verification_has_occurred",
        "source_transfer_occurred",
        "source_receipt_occurred",
        "reception_authorization_exists",
        "source_exists",
        "authority_exists",
        "currentness_exists",
        "final_completion_exists",
        "runtime_exists",
        "deployment_exists",
        "public_release_exists",
        "continuation_authorized",
        "reusable_permission_exists",
        "follow_on_work_authorized",
        "result_became_success",
        "result_became_verification",
        "result_became_external_result",
        "result_became_cross_carrier_proof",
        "result_became_source_transfer_or_receipt_or_reception_authorization",
        "result_became_source_or_authority_or_currentness",
        "result_artifact_became_success_external_result_or_cross_carrier_evidence",
        "returned_capture_became_proof",
        "zero_exit_code_became_success",
        "ok_became_verification",
        "ran_7_tests_became_cross_carrier_proof",
        "macbook_pro_became_authority",
        "macbook_air_became_source",
        "artifact_existence_became_result_authority",
        "artifact_path_became_currentness",
        "repo_local_availability_became_result_authority",
        "hidden_repo_state_became_result_authority",
        "first_result_boundary_resolver_repaired_hidden_erased_or_claimed_passed",
        "v1_packet_emission_boundary_resolver_repaired_hidden_erased_or_claimed_passed",
    )
    return {meaning: False for meaning in meanings}


def _what_remains_open() -> dict[str, Any]:
    open_items = (
        "second-carrier result test",
        "second-carrier result live artifact",
        "second-carrier result terminal summary, if needed",
        "second-carrier success boundary/spec/resolver/test/live artifact",
        "external result artifact",
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
    )
    return {
        "open_items": list(open_items),
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }


def _additional_basis_required(
    outcome: str, request: Mapping[str, Any]
) -> dict[str, Any]:
    if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        context = request.get("additional_basis_context")
        missing = context if isinstance(context, list) else [context] if context else []
        return {
            "required": True,
            "missing_or_unclear_basis": _sanitize(missing),
            "missing_basis_scheduled": False,
            "missing_basis_authorized": False,
            "missing_basis_executed": False,
        }
    return {
        "required": False,
        "missing_or_unclear_basis": [],
        "missing_basis_scheduled": False,
        "missing_basis_authorized": False,
        "missing_basis_executed": False,
    }


def _not_recorded_basis(outcome: str, request: Mapping[str, Any]) -> dict[str, Any]:
    if outcome == OUTCOME_NOT_RECORDED:
        basis = request.get("not_recorded_basis") or request.get("block_reason")
        return {
            "not_recorded": True,
            "reason": _sanitize(basis),
            "no_mutation": True,
            "no_success_created": True,
            "no_external_result_created": True,
            "no_cross_carrier_evidence_created": True,
            "no_source_authority_currentness_final_completion_runtime_or_follow_on": True,
        }
    return {"not_recorded": False, "reason": None, "no_mutation": True}


def _block(code: str | None, reason: Any = None) -> dict[str, Any] | None:
    if code is None:
        return None
    return {
        "blocked": True,
        "block_code": code,
        "block_reason": _sanitize(reason),
    }


def _first_failed_check(checks: Sequence[Mapping[str, Any]]) -> dict[str, Any] | None:
    for check in checks:
        if not _as_bool(check.get("passed")):
            return dict(check)
    return None


def _basis_extra(request: Mapping[str, Any], basis_key: str) -> dict[str, Any]:
    if basis_key == "selected_second_carrier_result_boundary_v2_basis":
        return {
            "selected_result_path": request.get(
                "selected_second_carrier_result_boundary_v2_result_path"
            ),
            "selected_outcome": request.get(
                "selected_second_carrier_result_boundary_v2_result_outcome"
            ),
            "selected_result_version": request.get(
                "selected_second_carrier_result_boundary_v2_result_version"
            ),
            "selected_failed_check_count": request.get(
                "selected_second_carrier_result_boundary_v2_failed_check_count"
            ),
            "declared_future_result_step": request.get(
                "selected_second_carrier_result_boundary_v2_declared_future_result_step"
            ),
            "already_created_result": request.get(
                "selected_second_carrier_result_boundary_v2_already_created_result"
            ),
            "already_created_success": request.get(
                "selected_second_carrier_result_boundary_v2_already_created_success"
            ),
            "already_created_external_result": request.get(
                "selected_second_carrier_result_boundary_v2_already_created_external_result"
            ),
            "already_created_cross_carrier_evidence": request.get(
                "selected_second_carrier_result_boundary_v2_already_created_cross_carrier_evidence"
            ),
            "zero_exit_code_not_success": request.get(
                "selected_second_carrier_result_boundary_v2_zero_exit_code_not_success"
            ),
            "ok_not_verification": request.get(
                "selected_second_carrier_result_boundary_v2_ok_not_verification"
            ),
            "returned_capture_not_cross_carrier_proof": request.get(
                "selected_second_carrier_result_boundary_v2_returned_capture_not_cross_carrier_proof"
            ),
            "official_enum_scope_strings_redacted": request.get(
                "selected_second_carrier_result_boundary_v2_official_enum_scope_strings_redacted"
            ),
            "first_result_boundary_resolver_preserved": request.get(
                "selected_second_carrier_result_boundary_v2_first_result_boundary_resolver_preserved"
            ),
        }
    if basis_key == "selected_returned_second_carrier_live_capture_intake_basis":
        return {
            "selected_intake_path": request.get("selected_returned_capture_intake_path"),
            "intake_preserved": request.get("selected_returned_capture_intake_preserved"),
            "intake_capture_only": request.get(
                "selected_returned_capture_intake_capture_only"
            ),
            "macbook_pro_to_macbook_air": request.get(
                "selected_returned_capture_from_macbook_pro_to_macbook_air"
            ),
        }
    if basis_key == "selected_returned_capture_material_basis":
        return {
            "stdout_path": request.get("selected_returned_capture_stdout_path"),
            "stderr_path": request.get("selected_returned_capture_stderr_path"),
            "working_directory": request.get(
                "selected_returned_capture_working_directory"
            ),
            "ran_7_tests_line": request.get(
                "selected_returned_capture_ran_7_tests_line"
            ),
            "ok_line": request.get("selected_returned_capture_ok_line"),
            "raw_placeholder_carrier_label": request.get(
                "selected_returned_capture_raw_placeholder_carrier_label"
            ),
            "raw_placeholder_carrier_type": request.get(
                "selected_returned_capture_raw_placeholder_carrier_type"
            ),
            "placeholder_fields_unrepaired": request.get(
                "selected_returned_capture_placeholder_fields_unrepaired"
            ),
        }
    if basis_key == "selected_returned_zip_basis":
        return {"selected_zip_path": request.get("selected_returned_capture_zip_path")}
    if basis_key == "selected_returned_hash_basis":
        return {"selected_hash_path": request.get("selected_returned_capture_hash_path")}
    if basis_key == "selected_returned_extracted_files_basis":
        return {
            "selected_extracted_directory_path": request.get(
                "selected_returned_capture_extracted_directory_path"
            )
        }
    if basis_key == "selected_returned_combined_terminal_log_basis":
        return {
            "selected_combined_terminal_log_path": request.get(
                "selected_returned_capture_combined_terminal_log_path"
            )
        }
    if basis_key == "selected_returned_exit_code_basis":
        return {
            "selected_exit_code": request.get("selected_returned_capture_exit_code"),
            "zero_exit_code_not_success": request.get(
                "selected_returned_capture_zero_exit_code_not_success"
            ),
        }
    if basis_key == "selected_returned_command_text_basis":
        return {
            "selected_command_text": request.get("selected_returned_capture_command_text")
        }
    if basis_key == "selected_returned_timestamps_basis":
        return {
            "run_started_at": request.get("selected_returned_capture_started_at"),
            "run_completed_at": request.get("selected_returned_capture_completed_at"),
        }
    if basis_key == "selected_second_carrier_output_capture_basis":
        return {
            "selected_result_path": request.get(
                "selected_second_carrier_output_capture_result_path"
            ),
            "selected_outcome": request.get(
                "selected_second_carrier_output_capture_result_outcome"
            ),
            "selected_failed_check_count": request.get(
                "selected_second_carrier_output_capture_failed_check_count"
            ),
            "bounded_capture_recorded": request.get(
                "selected_second_carrier_output_capture_bounded_capture_recorded"
            ),
            "treated_capture_as_result": request.get(
                "selected_second_carrier_output_capture_treated_capture_as_result"
            ),
            "treated_capture_as_success": request.get(
                "selected_second_carrier_output_capture_treated_capture_as_success"
            ),
            "treated_capture_as_external_result": request.get(
                "selected_second_carrier_output_capture_treated_capture_as_external_result"
            ),
            "treated_capture_as_cross_carrier_evidence": request.get(
                "selected_second_carrier_output_capture_treated_capture_as_cross_carrier_evidence"
            ),
        }
    return {}


def _result_id(request: Mapping[str, Any]) -> str:
    request_id = request.get("second_carrier_result_request_id")
    if _is_present(request_id):
        return str(request_id)
    return "undeclared_second_carrier_result_request"


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: Sequence[Mapping[str, Any]],
    block_code: str | None = None,
    block_reason: Any = None,
) -> dict[str, Any]:
    statement = _statement(outcome)
    non_claims = _false_non_claims()
    if isinstance(request.get("declared_non_claims"), Mapping):
        non_claims.update(_declared_non_claims_false(request))

    result: dict[str, Any] = {
        "portable_source_body_verification_second_carrier_result_metadata": {
            "portable_source_body_verification_second_carrier_result_id": _result_id(
                request
            ),
            "portable_source_body_verification_second_carrier_result_type": RESULT_TYPE,
            "portable_source_body_verification_second_carrier_result_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_second_carrier_result_question": {
            "second_carrier_result_request_id": request.get(
                "second_carrier_result_request_id"
            ),
            "question": request.get("second_carrier_result_question"),
            "intent": request.get("second_carrier_result_intent"),
            "core_question": CORE_QUESTION,
        },
    }

    for key in SELECTED_BASIS_KEYS:
        result[key] = _selected_basis(request, key, _basis_extra(request, key))

    for key in POSTURE_KEYS:
        result[key] = _posture(request, key, f"{key} declared and preserved")

    result.update(
        {
            "second_carrier_result_scope": {
                "scope_values": _scope_values(request),
                "supported_scope_values": list(SUPPORTED_SCOPE_VALUES),
                "unsupported_scope_values": _unsupported_scope_values(request),
                "official_enum_scope_strings_not_redacted": True,
            },
            "second_carrier_result_checks": list(checks),
            "second_carrier_result_statement": statement,
            "second_carrier_result_non_meaning": _non_meaning(),
            "additional_basis_required": _additional_basis_required(outcome, request),
            "not_recorded_basis": _not_recorded_basis(outcome, request),
            "what_remains_open": _what_remains_open(),
            "non_claims": non_claims,
            "outcome": outcome,
            "block": _block(block_code, block_reason),
        }
    )
    result["portable_source_body_verification_second_carrier_result_summary"] = (
        build_portable_source_body_verification_second_carrier_result_summary(result)
    )
    return _json_safe(result)


def _blocked_result(
    request: Mapping[str, Any],
    code: str,
    reason: Any,
    checks: Sequence[Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    block_checks = list(checks or [])
    if not block_checks:
        block_checks.append(
            _check(
                "second_carrier_result_blocked",
                False,
                "bounded second-carrier result request must not be malformed or overreach-shaped",
                reason,
                code,
            )
        )
    return _build_result(request, OUTCOME_BLOCKED, block_checks, code, reason)


def resolve_portable_source_body_verification_second_carrier_result(
    declared_second_carrier_result_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one bounded second-carrier result posture."""

    if declared_second_carrier_result_request is None:
        return _blocked_result(
            {},
            "DECLARED_SECOND_CARRIER_RESULT_REQUEST_MALFORMED",
            "declared second-carrier result request is missing",
        )
    if not isinstance(declared_second_carrier_result_request, Mapping):
        return _blocked_result(
            {},
            "DECLARED_SECOND_CARRIER_RESULT_REQUEST_MALFORMED",
            "declared second-carrier result request must be a JSON object",
        )

    request = copy.deepcopy(dict(declared_second_carrier_result_request))
    intent = request.get("second_carrier_result_intent")

    if intent == INTENT_BLOCK:
        return _blocked_result(
            request,
            "SECOND_CARRIER_RESULT_BLOCK_REQUESTED",
            request.get("block_reason") or "block intent requested",
        )

    checks = _build_checks(request)
    failed = _first_failed_check(checks)
    if failed is not None:
        code = str(failed.get("block_code") or failed.get("failure_code"))
        return _build_result(request, OUTCOME_BLOCKED, checks, code, failed)

    requested_outcome = request.get("requested_second_carrier_result_outcome")
    if intent == INTENT_DO_NOT_RECORD or requested_outcome == OUTCOME_NOT_RECORDED:
        return _build_result(request, OUTCOME_NOT_RECORDED, checks)
    if requested_outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        return _build_result(request, OUTCOME_REQUIRES_ADDITIONAL_BASIS, checks)
    if requested_outcome == OUTCOME_BLOCKED:
        return _blocked_result(
            request,
            "SECOND_CARRIER_RESULT_BLOCK_REQUESTED",
            request.get("block_reason") or "requested blocked outcome",
            checks,
        )

    return _build_result(request, OUTCOME_RECORDED, checks)


def resolve_portable_source_body_verification_second_carrier_result_from_path(
    declared_second_carrier_result_request_path: Path | str,
) -> dict:
    """Load a declared second-carrier result request JSON object and resolve it."""

    path = Path(declared_second_carrier_result_request_path)
    try:
        raw_text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise PortableSourceBodyVerificationSecondCarrierResultError(
            f"declared second-carrier result request path is unreadable: {path}"
        ) from exc
    try:
        loaded = json.loads(raw_text)
    except json.JSONDecodeError as exc:
        raise PortableSourceBodyVerificationSecondCarrierResultError(
            f"declared second-carrier result request JSON is malformed: {path}"
        ) from exc
    if not isinstance(loaded, Mapping):
        return _blocked_result(
            {},
            "DECLARED_SECOND_CARRIER_RESULT_REQUEST_MALFORMED",
            "declared second-carrier result request JSON must be an object",
        )
    return resolve_portable_source_body_verification_second_carrier_result(loaded)


def build_portable_source_body_verification_second_carrier_result_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a bounded summary from a second-carrier result artifact."""

    metadata = result.get("portable_source_body_verification_second_carrier_result_metadata")
    metadata_map = metadata if isinstance(metadata, Mapping) else {}
    question = result.get("declared_second_carrier_result_question")
    question_map = question if isinstance(question, Mapping) else {}
    checks = result.get("second_carrier_result_checks")
    checks_list = list(checks) if isinstance(checks, Sequence) and not isinstance(checks, str) else []
    statement = result.get("second_carrier_result_statement")
    statement_map = statement if isinstance(statement, Mapping) else {}
    non_claims = result.get("non_claims")
    non_claims_map = non_claims if isinstance(non_claims, Mapping) else {}
    block = result.get("block")
    block_map = block if isinstance(block, Mapping) else {}

    passed_count = sum(1 for check in checks_list if _as_bool(check.get("passed")))
    failed_count = sum(1 for check in checks_list if not _as_bool(check.get("passed")))

    boundary_basis = result.get("selected_second_carrier_result_boundary_v2_basis")
    boundary_basis_map = boundary_basis if isinstance(boundary_basis, Mapping) else {}
    intake_basis = result.get("selected_returned_second_carrier_live_capture_intake_basis")
    intake_basis_map = intake_basis if isinstance(intake_basis, Mapping) else {}
    zip_basis = result.get("selected_returned_zip_basis")
    zip_basis_map = zip_basis if isinstance(zip_basis, Mapping) else {}
    hash_basis = result.get("selected_returned_hash_basis")
    hash_basis_map = hash_basis if isinstance(hash_basis, Mapping) else {}
    extracted_basis = result.get("selected_returned_extracted_files_basis")
    extracted_basis_map = extracted_basis if isinstance(extracted_basis, Mapping) else {}
    exit_basis = result.get("selected_returned_exit_code_basis")
    exit_basis_map = exit_basis if isinstance(exit_basis, Mapping) else {}
    material_basis = result.get("selected_returned_capture_material_basis")
    material_basis_map = material_basis if isinstance(material_basis, Mapping) else {}
    output_basis = result.get("selected_second_carrier_output_capture_basis")
    output_basis_map = output_basis if isinstance(output_basis, Mapping) else {}

    summary = {
        "outcome": result.get("outcome"),
        "block_code": block_map.get("block_code"),
        "block_reason": block_map.get("block_reason"),
        "request_id": question_map.get("second_carrier_result_request_id")
        or metadata_map.get("portable_source_body_verification_second_carrier_result_id"),
        "question": question_map.get("question"),
        "intent": question_map.get("intent"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": metadata_map.get(
            "portable_source_body_verification_second_carrier_result_version"
        ),
        "resolver_module": metadata_map.get("resolver_module"),
        "second_carrier_result_recorded": bool(
            statement_map.get("second_carrier_result_recorded", False)
        ),
        "bounded_second_carrier_result_recorded": bool(
            statement_map.get("bounded_second_carrier_result_recorded", False)
        ),
        "result_artifact_recorded_or_bounded": bool(
            statement_map.get("result_artifact_recorded_or_bounded", False)
        ),
        "second_carrier_result_boundary_v2_basis_preserved": bool(
            statement_map.get("second_carrier_result_boundary_v2_basis_preserved", False)
        ),
        "returned_second_carrier_capture_basis_preserved": bool(
            statement_map.get("returned_second_carrier_capture_basis_preserved", False)
        ),
        "capture_intake_basis_preserved": bool(
            statement_map.get("capture_intake_basis_preserved", False)
        ),
        "second_carrier_output_capture_basis_preserved": bool(
            statement_map.get("second_carrier_output_capture_basis_preserved", False)
        ),
        "capture_artifact_basis_preserved": bool(
            statement_map.get("capture_artifact_basis_preserved", False)
        ),
        "result_recorded_bounded": bool(
            statement_map.get("result_recorded_bounded", False)
        ),
        "result_not_success": bool(statement_map.get("result_not_success", False)),
        "result_not_verification": bool(
            statement_map.get("result_not_verification", False)
        ),
        "result_not_external_result": bool(
            statement_map.get("result_not_external_result", False)
        ),
        "result_not_cross_carrier_evidence": bool(
            statement_map.get("result_not_cross_carrier_evidence", False)
        ),
        "result_not_source_transfer": bool(
            statement_map.get("result_not_source_transfer", False)
        ),
        "result_not_source_receipt": bool(
            statement_map.get("result_not_source_receipt", False)
        ),
        "result_not_reception_authorization": bool(
            statement_map.get("result_not_reception_authorization", False)
        ),
        "zero_exit_code_not_success": bool(
            statement_map.get("zero_exit_code_not_success", False)
        ),
        "ok_output_not_verification": bool(
            statement_map.get("ok_output_not_verification", False)
        ),
        "ran_7_tests_not_cross_carrier_proof": bool(
            statement_map.get("ran_7_tests_not_cross_carrier_proof", False)
        ),
        "returned_capture_not_cross_carrier_proof": bool(
            statement_map.get("returned_capture_not_cross_carrier_proof", False)
        ),
        "second_carrier_success_not_created": bool(
            statement_map.get("second_carrier_success_not_created", False)
        ),
        "external_result_not_created": bool(
            statement_map.get("external_result_not_created", False)
        ),
        "cross_carrier_evidence_not_created": bool(
            statement_map.get("cross_carrier_evidence_not_created", False)
        ),
        "receiving_carrier_not_authority": bool(
            statement_map.get("receiving_carrier_not_authority", False)
        ),
        "source_not_created": bool(statement_map.get("source_not_created", False)),
        "authority_not_created": bool(
            statement_map.get("authority_not_created", False)
        ),
        "currentness_not_created": bool(
            statement_map.get("currentness_not_created", False)
        ),
        "final_completion_not_created": bool(
            statement_map.get("final_completion_not_created", False)
        ),
        "runtime_not_created": bool(statement_map.get("runtime_not_created", False)),
        "follow_on_work_not_authorized": bool(
            statement_map.get("follow_on_work_not_authorized", False)
        ),
        "hidden_repo_state_excluded": bool(
            statement_map.get("hidden_repo_state_excluded", False)
        ),
        "hidden_repo_state_not_used_as_result_authority": bool(
            statement_map.get("hidden_repo_state_not_used_as_result_authority", False)
        ),
        "repo_local_availability_not_result_authority": bool(
            statement_map.get("repo_local_availability_not_result_authority", False)
        ),
        "selected_basis_reference_shape_preserved": bool(
            statement_map.get("selected_basis_reference_shape_preserved", False)
        ),
        "raw_full_prior_artifact_body_not_returned": bool(
            statement_map.get("raw_full_prior_artifact_body_not_returned", False)
        ),
        "official_enum_scope_strings_not_redacted": bool(
            statement_map.get("official_enum_scope_strings_not_redacted", False)
        ),
        "hostile_raw_body_content_contained": bool(
            statement_map.get("hostile_raw_body_content_contained", False)
        ),
        "selected_returned_capture_intake_path": intake_basis_map.get(
            "selected_intake_path"
        ),
        "selected_returned_capture_zip_path": zip_basis_map.get("selected_zip_path"),
        "selected_returned_capture_hash_path": hash_basis_map.get("selected_hash_path"),
        "selected_returned_capture_extracted_path": extracted_basis_map.get(
            "selected_extracted_directory_path"
        ),
        "selected_returned_capture_exit_code": exit_basis_map.get(
            "selected_exit_code"
        ),
        "selected_returned_capture_ok_line": material_basis_map.get("ok_line"),
        "selected_second_carrier_result_boundary_v2_outcome": boundary_basis_map.get(
            "selected_outcome"
        ),
        "selected_second_carrier_result_boundary_v2_version": boundary_basis_map.get(
            "selected_result_version"
        ),
        "selected_second_carrier_result_boundary_v2_failed_check_count": boundary_basis_map.get(
            "selected_failed_check_count"
        ),
        "selected_second_carrier_output_capture_outcome": output_basis_map.get(
            "selected_outcome"
        ),
        "selected_second_carrier_output_capture_failed_check_count": output_basis_map.get(
            "selected_failed_check_count"
        ),
        "no_success_external_result_or_cross_carrier_evidence": (
            not _as_bool(non_claims_map.get("second_carrier_success_created"))
            and not _as_bool(non_claims_map.get("external_result_created"))
            and not _as_bool(non_claims_map.get("cross_carrier_evidence_created"))
        ),
        "no_source_authority_currentness_final_completion_or_runtime": (
            not _as_bool(non_claims_map.get("source_created"))
            and not _as_bool(non_claims_map.get("authority_created"))
            and not _as_bool(non_claims_map.get("currentness_created"))
            and not _as_bool(non_claims_map.get("final_completion_claimed"))
            and not _as_bool(non_claims_map.get("runtime_hosting_created"))
        ),
        "no_deployment_public_release_or_follow_on": (
            not _as_bool(non_claims_map.get("deployment_created"))
            and not _as_bool(non_claims_map.get("public_release_created"))
            and not _as_bool(non_claims_map.get("follow_on_work_authorized"))
        ),
        "key_non_claims": {
            key: bool(non_claims_map.get(key, False))
            for key in REQUIRED_FALSE_NON_CLAIMS
        },
        "v1_predecessor_failure_preserved": True,
        "v1_not_repaired": not _as_bool(non_claims_map.get("v1_repaired")),
        "v1_not_hidden": not _as_bool(non_claims_map.get("v1_hidden")),
        "v1_not_claimed_passed": not _as_bool(non_claims_map.get("v1_claimed_passed")),
        "first_result_boundary_resolver_preserved_as_failed_predecessor": bool(
            statement_map.get("first_result_boundary_resolver_failure_preserved", False)
        ),
        "first_result_boundary_resolver_not_repaired": not _as_bool(
            non_claims_map.get("first_result_boundary_resolver_repaired")
        ),
        "first_result_boundary_resolver_not_hidden": not _as_bool(
            non_claims_map.get("first_result_boundary_resolver_hidden")
        ),
        "first_result_boundary_resolver_not_claimed_passed": not _as_bool(
            non_claims_map.get("first_result_boundary_resolver_claimed_passed")
        ),
    }
    return _json_safe(summary)


def write_portable_source_body_verification_second_carrier_result_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write a bounded second-carrier result JSON artifact without overwriting."""

    result_safe = _json_safe(result)
    metadata = result_safe.get("portable_source_body_verification_second_carrier_result_metadata")
    metadata_map = metadata if isinstance(metadata, Mapping) else {}
    request_id = metadata_map.get("portable_source_body_verification_second_carrier_result_id")
    if not _is_present(request_id):
        question = result_safe.get("declared_second_carrier_result_question")
        if isinstance(question, Mapping):
            request_id = question.get("second_carrier_result_request_id")
    if not _is_present(request_id):
        request_id = "undeclared_second_carrier_result_request"

    if output_path is None:
        target = OUTPUT_ROOT / (
            f"{request_id}__portable_source_body_verification_"
            "second_carrier_result_result.json"
        )
    else:
        target = Path(output_path)
        if target.is_dir():
            target = target / (
                f"{request_id}__portable_source_body_verification_"
                "second_carrier_result_result.json"
            )

    target.parent.mkdir(parents=True, exist_ok=True)
    final_target = target
    suffix = 1
    while final_target.exists():
        final_target = target.with_name(f"{target.stem}_{suffix:03d}{target.suffix}")
        suffix += 1

    final_target.write_text(
        json.dumps(result_safe, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return final_target


def build_declared_portable_source_body_verification_second_carrier_result_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Build a clean declared second-carrier result request.

    The helper does not infer success, verification, external result,
    cross-carrier evidence, source, authority, currentness, final completion,
    runtime, continuation, reusable permission, or follow-on work.
    """

    request_id = overrides.pop(
        "second_carrier_result_request_id",
        "portable_source_body_verification_second_carrier_result_reference_review_001",
    )
    basis = {
        "basis_id": "portable_source_body_verification_second_carrier_result_basis",
        "basis_role": "reference-shaped basis only",
    }
    request: dict[str, Any] = {
        "second_carrier_result_request_id": request_id,
        "second_carrier_result_question": CORE_QUESTION,
        "second_carrier_result_intent": INTENT_RECORD,
        "second_carrier_result_scope": list(SUPPORTED_SCOPE_VALUES),
        "declared_non_claims": _false_non_claims(),
        "reference_shaped_input_posture": True,
        "selected_second_carrier_result_boundary_v2_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_"
            "verification_second_carrier_result_boundary_v2/"
            "portable_source_body_verification_second_carrier_result_boundary_"
            "reference_review_001_v2__portable_source_body_verification_second_"
            "carrier_result_boundary_v2_result.json"
        ),
        "selected_second_carrier_result_boundary_v2_result_outcome": EXPECTED_BOUNDARY_V2_OUTCOME,
        "selected_second_carrier_result_boundary_v2_result_version": EXPECTED_BOUNDARY_V2_VERSION,
        "selected_second_carrier_result_boundary_v2_failed_check_count": 0,
        "selected_second_carrier_result_boundary_v2_declared_future_result_step": True,
        "selected_second_carrier_result_boundary_v2_already_created_result": False,
        "selected_second_carrier_result_boundary_v2_already_created_success": False,
        "selected_second_carrier_result_boundary_v2_already_created_external_result": False,
        "selected_second_carrier_result_boundary_v2_already_created_cross_carrier_evidence": False,
        "selected_second_carrier_result_boundary_v2_zero_exit_code_not_success": True,
        "selected_second_carrier_result_boundary_v2_ok_not_verification": True,
        "selected_second_carrier_result_boundary_v2_returned_capture_not_cross_carrier_proof": True,
        "selected_second_carrier_result_boundary_v2_official_enum_scope_strings_redacted": False,
        "selected_second_carrier_result_boundary_v2_official_enum_scope_strings_not_redacted": True,
        "selected_second_carrier_result_boundary_v2_first_result_boundary_resolver_preserved": True,
        "selected_returned_capture_intake_path": (
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_RETURNED_SECOND_CARRIER_"
            "LIVE_CAPTURE_INTAKE_V0.md"
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
            "python -m unittest tests/test_resolve_portable_source_body_verification_"
            "second_carrier_result_boundary_v2.py"
        ),
        "selected_returned_capture_working_directory": "/Users/markomarkota/IAMMAI-SYSTEM",
        "selected_returned_capture_started_at": "2026-05-09T00:00:00Z",
        "selected_returned_capture_completed_at": "2026-05-09T00:00:01Z",
        "selected_returned_capture_exit_code": 0,
        "selected_returned_capture_ran_7_tests_line": "Ran 7 tests in 0.451s",
        "selected_returned_capture_ok_line": "OK",
        "selected_returned_capture_raw_placeholder_carrier_label": "raw_placeholder_carrier_label",
        "selected_returned_capture_raw_placeholder_carrier_type": "raw_placeholder_carrier_type",
        "selected_returned_capture_placeholder_fields_unrepaired": True,
        "selected_returned_capture_zero_exit_code_not_success": True,
        "selected_returned_capture_ok_not_verification": True,
        "selected_returned_capture_not_cross_carrier_proof": True,
        "selected_second_carrier_output_capture_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_"
            "verification_second_carrier_output_capture/"
            "portable_source_body_verification_second_carrier_output_capture_"
            "reference_review_001__portable_source_body_verification_second_"
            "carrier_output_capture_result.json"
        ),
        "selected_second_carrier_output_capture_result_outcome": EXPECTED_OUTPUT_CAPTURE_OUTCOME,
        "selected_second_carrier_output_capture_failed_check_count": 0,
        "selected_second_carrier_output_capture_bounded_capture_recorded": True,
        "selected_second_carrier_output_capture_treated_capture_as_result": False,
        "selected_second_carrier_output_capture_treated_capture_as_success": False,
        "selected_second_carrier_output_capture_treated_capture_as_external_result": False,
        "selected_second_carrier_output_capture_treated_capture_as_cross_carrier_evidence": False,
    }

    for key in SELECTED_BASIS_KEYS:
        request[key] = {
            **basis,
            "basis_key": key,
            "reference_shape_preserved": True,
        }
    request["selected_second_carrier_result_boundary_v2_basis"].update(
        {
            "outcome": EXPECTED_BOUNDARY_V2_OUTCOME,
            "result_version": EXPECTED_BOUNDARY_V2_VERSION,
            "failed_check_count": 0,
            "declared_future_result_step": True,
        }
    )
    request["selected_returned_capture_material_basis"].update(
        {
            "exit_code": 0,
            "ran_7_tests_line": "Ran 7 tests in 0.451s",
            "ok_line": "OK",
            "capture_only": True,
        }
    )
    request["selected_second_carrier_output_capture_basis"].update(
        {
            "outcome": EXPECTED_OUTPUT_CAPTURE_OUTCOME,
            "failed_check_count": 0,
            "bounded_capture_recorded": True,
        }
    )

    for key in POSTURE_KEYS:
        request[key] = True

    request.update(overrides)
    if "declared_non_claims" not in request or not isinstance(
        request["declared_non_claims"], Mapping
    ):
        request["declared_non_claims"] = _false_non_claims()
    else:
        non_claims = _false_non_claims()
        non_claims.update(dict(request["declared_non_claims"]))
        request["declared_non_claims"] = non_claims
    return _json_safe(request)
