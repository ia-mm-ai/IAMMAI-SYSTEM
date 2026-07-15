"""Resolve portable source-body verification second-carrier success boundary.

This module records one bounded second-carrier success-boundary posture only. It
is downstream of the clean second-carrier result line. It may preserve that one
future second-carrier success step can be declared, but it does not create
second-carrier success, verification, external result, cross-carrier evidence,
portable verification closure, source transfer, source receipt, reception
authorization, source, authority, currentness, final completion, runtime,
continuation, reusable permission, derivative reception, vessel relation,
another reception request, or follow-on work.
"""

from __future__ import annotations

import copy
import datetime
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any


class PortableSourceBodyVerificationSecondCarrierSuccessBoundaryError(Exception):
    """Bounded resolver error for explicit unreadable or malformed inputs."""


RESOLVER_MODULE = (
    "resolve_portable_source_body_verification_second_carrier_success_boundary"
)
RESULT_TYPE = (
    "portable_source_body_verification_second_carrier_success_boundary_result"
)
RESULT_VERSION = "0.1.0"
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_portable_source_body_verification_"
    "second_carrier_success_boundary"
)

CORE_QUESTION = (
    "Can the clean second-carrier result basis be bounded for one future "
    "second-carrier success step without creating success yet, verification, "
    "external result, cross-carrier evidence, portable verification closure, "
    "source transfer, source receipt, reception authorization, source, "
    "authority, currentness, runtime, final completion, continuation, reusable "
    "permission, derivative reception, vessel relation, another reception "
    "request, or follow-on work?"
)

OUTCOME_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_SUCCESS_BOUNDARY_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_SUCCESS_BOUNDARY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_SUCCESS_BOUNDARY_"
    "REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_SUCCESS_BOUNDARY_BLOCKED"
)
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = (
    "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_SUCCESS_BOUNDARY"
)
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_SUCCESS_BOUNDARY"
)
INTENT_BLOCK = (
    "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_SUCCESS_BOUNDARY"
)
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

EXPECTED_SECOND_CARRIER_RESULT_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RESULT_RECORDED"
)
EXPECTED_SECOND_CARRIER_RESULT_VERSION = "0.1.0"
EXPECTED_SECOND_CARRIER_RESULT_BOUNDARY_V2_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RESULT_BOUNDARY_RECORDED"
)
EXPECTED_SECOND_CARRIER_OUTPUT_CAPTURE_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_OUTPUT_CAPTURE_RECORDED"
)

SUPPORTED_SCOPE_VALUES = (
    "SECOND_CARRIER_SUCCESS_BOUNDARY_ONLY",
    "ONE_FUTURE_SECOND_CARRIER_SUCCESS_STEP_ONLY",
    "SECOND_CARRIER_RESULT_BASIS_PRESERVED",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_BASIS_PRESERVED",
    "RETURNED_SECOND_CARRIER_CAPTURE_BASIS_PRESERVED",
    "CAPTURE_INTAKE_BASIS_PRESERVED",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_PRESERVED",
    "RESULT_ARTIFACT_BASIS_PRESERVED",
    "SUCCESS_NOT_CREATED",
    "SUCCESS_BOUNDARY_NOT_SUCCESS",
    "RESULT_NOT_SUCCESS",
    "RESULT_NOT_VERIFICATION",
    "ZERO_EXIT_CODE_NOT_SUCCESS",
    "OK_OUTPUT_NOT_VERIFICATION",
    "RAN_7_TESTS_NOT_CROSS_CARRIER_PROOF",
    "RETURNED_CAPTURE_NOT_CROSS_CARRIER_PROOF",
    "VERIFICATION_NOT_CREATED",
    "EXTERNAL_RESULT_NOT_CREATED",
    "CROSS_CARRIER_EVIDENCE_NOT_CREATED",
    "PORTABLE_VERIFICATION_CLOSURE_NOT_CREATED",
    "SUCCESS_NOT_SOURCE_TRANSFER",
    "SUCCESS_NOT_SOURCE_RECEIPT",
    "SUCCESS_NOT_RECEPTION_AUTHORIZATION",
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
    "NO_PORTABLE_VERIFICATION_CLOSURE_INFERENCE",
    "NO_SOURCE_INFERENCE",
    "NO_AUTHORITY_INFERENCE",
    "NO_CURRENTNESS_INFERENCE",
    "NO_FINAL_COMPLETION_INFERENCE",
    "NO_RUNTIME_INFERENCE",
    "NO_FOLLOW_ON_WORK_INFERENCE",
    "NO_UNBOUNDED_PASS_FAIL_INFERENCE",
    "HIDDEN_REPO_STATE_EXCLUDED",
    "HIDDEN_REPO_STATE_NOT_USED_AS_SUCCESS_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_NOT_SUCCESS_AUTHORITY",
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
SUPPORTED_SECOND_CARRIER_SUCCESS_BOUNDARY_SCOPE = SUPPORTED_SCOPE_VALUES

SELECTED_BASIS_KEYS = (
    "selected_second_carrier_result_basis",
    "selected_second_carrier_result_terminal_summary_basis",
    "selected_second_carrier_result_boundary_v2_basis",
    "selected_returned_second_carrier_live_capture_intake_basis",
    "selected_returned_capture_material_basis",
    "selected_second_carrier_output_capture_basis",
    "selected_second_carrier_output_capture_terminal_summary_basis",
    "selected_second_carrier_output_capture_boundary_basis",
    "selected_second_carrier_execution_output_basis",
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
    "second_carrier_success_boundary_only_posture",
    "one_future_second_carrier_success_step_posture",
    "second_carrier_result_basis_preserved_posture",
    "second_carrier_result_boundary_v2_basis_preserved_posture",
    "returned_second_carrier_capture_basis_preserved_posture",
    "capture_intake_basis_preserved_posture",
    "second_carrier_output_capture_basis_preserved_posture",
    "result_artifact_basis_preserved_posture",
    "success_not_created_posture",
    "success_boundary_not_success_posture",
    "result_not_success_posture",
    "result_not_verification_posture",
    "zero_exit_code_not_success_posture",
    "ok_output_not_verification_posture",
    "ran_7_tests_not_cross_carrier_proof_posture",
    "returned_capture_not_cross_carrier_proof_posture",
    "verification_not_created_posture",
    "external_result_not_created_posture",
    "cross_carrier_evidence_not_created_posture",
    "portable_verification_closure_not_created_posture",
    "success_not_source_transfer_posture",
    "success_not_source_receipt_posture",
    "success_not_reception_authorization_posture",
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
    "repo_local_availability_not_success_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "first_result_boundary_resolver_failure_preserved_posture",
)

REQUIRED_FALSE_NON_CLAIMS = (
    "second_carrier_success_created",
    "verification_created",
    "external_result_created",
    "cross_carrier_evidence_created",
    "portable_verification_closure_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "second_carrier_success_boundary_treated_as_success",
    "second_carrier_success_boundary_treated_as_verification",
    "second_carrier_success_boundary_treated_as_external_result",
    "second_carrier_success_boundary_treated_as_cross_carrier_evidence",
    "second_carrier_success_boundary_treated_as_portable_verification_closure",
    "second_carrier_success_boundary_treated_as_source_transfer",
    "second_carrier_success_boundary_treated_as_source_receipt",
    "second_carrier_success_boundary_treated_as_reception_authorization",
    "second_carrier_success_boundary_treated_as_source",
    "second_carrier_success_boundary_treated_as_authority",
    "second_carrier_success_boundary_treated_as_currentness",
    "second_carrier_success_boundary_treated_as_final_completion",
    "second_carrier_success_boundary_treated_as_runtime",
    "second_carrier_success_boundary_treated_as_continuation",
    "second_carrier_success_boundary_treated_as_reusable_permission",
    "second_carrier_success_boundary_treated_as_follow_on_work",
    "second_carrier_result_treated_as_success",
    "second_carrier_result_treated_as_verification",
    "zero_exit_code_treated_as_success",
    "ok_output_treated_as_verification",
    "ran_7_tests_treated_as_cross_carrier_proof",
    "returned_capture_treated_as_cross_carrier_evidence",
    "receiving_carrier_treated_as_authority",
    "artifact_existence_treated_as_success_authority",
    "artifact_path_treated_as_currentness",
    "repo_local_availability_treated_as_success_authority",
    "hidden_repo_state_used_as_success_content",
    "hidden_repo_state_used_as_success_authority",
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
    "first_result_boundary_resolver_repaired",
    "first_result_boundary_resolver_hidden",
    "first_result_boundary_resolver_claimed_passed",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "second_carrier_success_boundary_recorded",
    "one_future_second_carrier_success_step_declared",
    "second_carrier_result_basis_preserved",
    "second_carrier_result_boundary_v2_basis_preserved",
    "returned_second_carrier_capture_basis_preserved",
    "capture_intake_basis_preserved",
    "second_carrier_output_capture_basis_preserved",
    "result_artifact_basis_preserved",
    "success_not_created",
    "success_boundary_not_success",
    "result_not_success",
    "result_not_verification",
    "zero_exit_code_not_success",
    "ok_output_not_verification",
    "ran_7_tests_not_cross_carrier_proof",
    "returned_capture_not_cross_carrier_proof",
    "verification_not_created",
    "external_result_not_created",
    "cross_carrier_evidence_not_created",
    "portable_verification_closure_not_created",
    "success_not_source_transfer",
    "success_not_source_receipt",
    "success_not_reception_authorization",
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
    "hidden_repo_state_not_used_as_success_authority",
    "repo_local_availability_not_success_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "official_enum_scope_strings_not_redacted",
    "hostile_raw_body_content_contained",
    "first_result_boundary_resolver_failure_preserved",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
)

BLOCK_CODES = (
    "DECLARED_SECOND_CARRIER_SUCCESS_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_SECOND_CARRIER_SUCCESS_BOUNDARY_REQUEST_UNREADABLE",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_QUESTION_UNDECLARED",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_INTENT_UNSUPPORTED",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_BLOCK_REQUESTED",
    "SECOND_CARRIER_RESULT_BASIS_MISSING",
    "SECOND_CARRIER_RESULT_NOT_RECORDED",
    "SECOND_CARRIER_RESULT_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_RESULT_VERSION_NOT_0_1_0",
    "SECOND_CARRIER_RESULT_DID_NOT_RECORD_BOUNDED_RESULT",
    "SECOND_CARRIER_RESULT_ALREADY_CREATED_SUCCESS",
    "SECOND_CARRIER_RESULT_ALREADY_CREATED_VERIFICATION",
    "SECOND_CARRIER_RESULT_ALREADY_CREATED_EXTERNAL_RESULT",
    "SECOND_CARRIER_RESULT_ALREADY_CREATED_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_RESULT_TREATED_RESULT_AS_SUCCESS",
    "SECOND_CARRIER_RESULT_TREATED_RESULT_AS_VERIFICATION",
    "SECOND_CARRIER_RESULT_TREATED_RESULT_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_RESULT_TREATED_RESULT_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_RESULT_TREATED_ZERO_EXIT_CODE_AS_SUCCESS",
    "SECOND_CARRIER_RESULT_TREATED_OK_AS_VERIFICATION",
    "SECOND_CARRIER_RESULT_TREATED_RAN_7_TESTS_AS_CROSS_CARRIER_PROOF",
    "SECOND_CARRIER_RESULT_TREATED_RETURNED_CAPTURE_AS_CROSS_CARRIER_PROOF",
    "SECOND_CARRIER_RESULT_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_BASIS_MISSING",
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
    "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_SUCCESS",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_VERIFICATION",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_SOURCE",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_AUTHORITY",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_CURRENTNESS",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_FINAL_COMPLETION",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_RUNTIME",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_CONTINUATION",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
    "SECOND_CARRIER_SUCCESS_CREATED",
    "VERIFICATION_CREATED",
    "EXTERNAL_RESULT_CREATED",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_SUCCESS_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_SUCCESS_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_SUCCESS_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_SUCCESS_AUTHORITY",
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
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_SUCCESS_BOUNDARY",
    "ARTIFACTS_MUTATED",
    "RETURNED_CAPTURE_MATERIAL_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_SECOND_CARRIER_SUCCESS_BOUNDARY_SCOPE",
)

NON_CLAIM_BLOCK_CODE_BY_KEY = {
    "second_carrier_success_created": "SECOND_CARRIER_SUCCESS_CREATED",
    "verification_created": "VERIFICATION_CREATED",
    "external_result_created": "EXTERNAL_RESULT_CREATED",
    "cross_carrier_evidence_created": "CROSS_CARRIER_EVIDENCE_CREATED",
    "portable_verification_closure_created": "PORTABLE_VERIFICATION_CLOSURE_CREATED",
    "source_transfer_occurred": "SOURCE_TRANSFER_OCCURRED",
    "source_receipt_occurred": "SOURCE_RECEIPT_OCCURRED",
    "reception_authorization_created": "RECEPTION_AUTHORIZATION_CREATED",
    "second_carrier_success_boundary_treated_as_success": (
        "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_SUCCESS"
    ),
    "second_carrier_success_boundary_treated_as_verification": (
        "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_VERIFICATION"
    ),
    "second_carrier_success_boundary_treated_as_external_result": (
        "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_EXTERNAL_RESULT"
    ),
    "second_carrier_success_boundary_treated_as_cross_carrier_evidence": (
        "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_CROSS_CARRIER_EVIDENCE"
    ),
    "second_carrier_success_boundary_treated_as_portable_verification_closure": (
        "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE"
    ),
    "second_carrier_success_boundary_treated_as_source_transfer": (
        "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_SOURCE_TRANSFER"
    ),
    "second_carrier_success_boundary_treated_as_source_receipt": (
        "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_SOURCE_RECEIPT"
    ),
    "second_carrier_success_boundary_treated_as_reception_authorization": (
        "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION"
    ),
    "second_carrier_success_boundary_treated_as_source": (
        "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_SOURCE"
    ),
    "second_carrier_success_boundary_treated_as_authority": (
        "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_AUTHORITY"
    ),
    "second_carrier_success_boundary_treated_as_currentness": (
        "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_CURRENTNESS"
    ),
    "second_carrier_success_boundary_treated_as_final_completion": (
        "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_FINAL_COMPLETION"
    ),
    "second_carrier_success_boundary_treated_as_runtime": (
        "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_RUNTIME"
    ),
    "second_carrier_success_boundary_treated_as_continuation": (
        "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_CONTINUATION"
    ),
    "second_carrier_success_boundary_treated_as_reusable_permission": (
        "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION"
    ),
    "second_carrier_success_boundary_treated_as_follow_on_work": (
        "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK"
    ),
    "second_carrier_result_treated_as_success": (
        "SECOND_CARRIER_RESULT_TREATED_RESULT_AS_SUCCESS"
    ),
    "second_carrier_result_treated_as_verification": (
        "SECOND_CARRIER_RESULT_TREATED_RESULT_AS_VERIFICATION"
    ),
    "zero_exit_code_treated_as_success": "ZERO_EXIT_CODE_TREATED_AS_SUCCESS",
    "ok_output_treated_as_verification": "OK_OUTPUT_TREATED_AS_VERIFICATION",
    "ran_7_tests_treated_as_cross_carrier_proof": (
        "RAN_7_TESTS_TREATED_AS_CROSS_CARRIER_PROOF"
    ),
    "returned_capture_treated_as_cross_carrier_evidence": (
        "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_PROOF"
    ),
    "receiving_carrier_treated_as_authority": (
        "RECEIVING_CARRIER_TREATED_AS_AUTHORITY"
    ),
    "artifact_existence_treated_as_success_authority": (
        "ARTIFACT_EXISTENCE_TREATED_AS_SUCCESS_AUTHORITY"
    ),
    "artifact_path_treated_as_currentness": "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "repo_local_availability_treated_as_success_authority": (
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_SUCCESS_AUTHORITY"
    ),
    "hidden_repo_state_used_as_success_content": (
        "HIDDEN_REPO_STATE_USED_AS_SUCCESS_CONTENT"
    ),
    "hidden_repo_state_used_as_success_authority": (
        "HIDDEN_REPO_STATE_USED_AS_SUCCESS_AUTHORITY"
    ),
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
    "returned_capture_material_mutated": "RETURNED_CAPTURE_MATERIAL_MUTATED",
    "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
    "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
    "v1_repaired": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "v1_hidden": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "v1_claimed_passed": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "first_result_boundary_resolver_repaired": (
        "FIRST_RESULT_BOUNDARY_RESOLVER_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED"
    ),
    "first_result_boundary_resolver_hidden": (
        "FIRST_RESULT_BOUNDARY_RESOLVER_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED"
    ),
    "first_result_boundary_resolver_claimed_passed": (
        "FIRST_RESULT_BOUNDARY_RESOLVER_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED"
    ),
}

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
        "capture_body",
        "second_carrier_success_body",
        "verification_body",
        "external_result_body",
        "cross_carrier_evidence_body",
        "source_body",
        "authority_body",
        "hidden_repo_state",
        "current_working_tree",
        "local_cache",
        "repo_local_only_dependency",
    }
)
HOSTILE_SENTINELS = (
    "RAW_SECOND_CARRIER_SUCCESS_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
    "HOSTILE_SECOND_CARRIER_SUCCESS_BOUNDARY_FULL_BODY_VALUE_MUST_NOT_RETURN",
)
REDACTION_TEXT = "[bounded-second-carrier-success-boundary-redacted-raw-body]"

OFFICIAL_STRINGS = frozenset(
    tuple(SUPPORTED_SCOPE_VALUES)
    + tuple(OUTCOME_FAMILY)
    + tuple(BLOCK_CODES)
    + tuple(REQUIRED_FALSE_NON_CLAIMS)
    + tuple(ALLOWED_TRUE_RECORDED_FIELDS)
    + tuple(POSTURE_KEYS)
    + tuple(SELECTED_BASIS_KEYS)
    + (
        RESOLVER_MODULE,
        RESULT_VERSION,
        RESULT_TYPE,
        CORE_QUESTION,
        EXPECTED_SECOND_CARRIER_RESULT_OUTCOME,
        EXPECTED_SECOND_CARRIER_RESULT_VERSION,
        EXPECTED_SECOND_CARRIER_RESULT_BOUNDARY_V2_OUTCOME,
        EXPECTED_SECOND_CARRIER_OUTPUT_CAPTURE_OUTCOME,
        "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
        "RETURNED_RESULT_CONTAINMENT_PRESERVED",
        "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
        "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    )
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
    if isinstance(value, Mapping):
        return bool(value)
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return bool(value)
    return True


def _as_bool(value: Any) -> bool:
    return bool(value) if isinstance(value, bool) else False


def _as_int(value: Any) -> int | None:
    if isinstance(value, bool):
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


def _sanitize(value: Any, *, parent_key: str | None = None) -> Any:
    if parent_key is not None and _is_sensitive_key(parent_key):
        return REDACTION_TEXT
    if isinstance(value, str):
        if value in OFFICIAL_STRINGS:
            return value
        if any(sentinel in value for sentinel in HOSTILE_SENTINELS):
            return REDACTION_TEXT
        return value
    if isinstance(value, Mapping):
        sanitized: dict[str, Any] = {}
        for key, item in value.items():
            string_key = str(key)
            sanitized[string_key] = _sanitize(item, parent_key=string_key)
        return sanitized
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return [_sanitize(item) for item in value]
    return value


def _json_safe(value: Any) -> Any:
    sanitized = _sanitize(value)
    return json.loads(json.dumps(sanitized, sort_keys=True, default=str))


def _false_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _request_non_claims(request: Mapping[str, Any]) -> dict[str, Any]:
    declared = request.get("declared_non_claims", {})
    if not isinstance(declared, Mapping):
        declared = {}
    merged = _false_non_claims()
    merged.update({str(key): value for key, value in declared.items()})
    for key in REQUIRED_FALSE_NON_CLAIMS:
        if key in request:
            merged[key] = request[key]
    return merged


def _declared_non_claims_false(request: Mapping[str, Any]) -> tuple[bool, list[str]]:
    non_claims = _request_non_claims(request)
    bad = [
        key
        for key in REQUIRED_FALSE_NON_CLAIMS
        if key not in non_claims or non_claims.get(key) is not False
    ]
    return not bad, bad


def _negative_flag(request: Mapping[str, Any], key: str) -> bool:
    non_claims = _request_non_claims(request)
    if key in non_claims:
        return non_claims.get(key) is False
    if key in request:
        return request.get(key) is False
    return True


def _basis_supplied(request: Mapping[str, Any], key: str) -> bool:
    return _is_present(request.get(key))


def _scope_values(request: Mapping[str, Any]) -> tuple[str, ...]:
    raw = request.get(
        "second_carrier_success_boundary_scope",
        request.get("supported_second_carrier_success_boundary_scope", ()),
    )
    if isinstance(raw, str):
        return (raw,)
    if isinstance(raw, Mapping):
        values = raw.get("values", raw.get("scope_values", ()))
        if isinstance(values, str):
            return (values,)
        if isinstance(values, Sequence) and not isinstance(
            values, (str, bytes, bytearray)
        ):
            return tuple(str(value) for value in values)
        return tuple(str(value) for value in raw.values())
    if isinstance(raw, Sequence) and not isinstance(raw, (str, bytes, bytearray)):
        return tuple(str(value) for value in raw)
    return ()


def _unsupported_scope_values(request: Mapping[str, Any]) -> list[str]:
    supported = set(SUPPORTED_SCOPE_VALUES)
    return [value for value in _scope_values(request) if value not in supported]


def _serialized_contains_hostile_sentinel(value: Any) -> bool:
    serialized = json.dumps(_json_safe(value), sort_keys=True, default=str)
    return any(sentinel in serialized for sentinel in HOSTILE_SENTINELS)


def _check(
    check_name: str,
    passed: bool,
    expected_posture: str,
    actual_posture: Any,
    block_code: str,
) -> dict[str, Any]:
    record: dict[str, Any] = {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": expected_posture,
        "actual_posture": _json_safe(actual_posture),
    }
    if passed:
        record["block_code"] = None
        record["failure_code"] = None
    else:
        record["block_code"] = block_code
        record["failure_code"] = block_code
    return record


def _basis_extra(request: Mapping[str, Any], key: str) -> dict[str, Any]:
    if key == "selected_second_carrier_result_basis":
        return {
            "selected_second_carrier_result_result_path": _json_safe(
                request.get("selected_second_carrier_result_result_path")
            ),
            "selected_second_carrier_result_result_outcome": request.get(
                "selected_second_carrier_result_result_outcome"
            ),
            "selected_second_carrier_result_result_version": request.get(
                "selected_second_carrier_result_result_version"
            ),
            "selected_second_carrier_result_failed_check_count": request.get(
                "selected_second_carrier_result_failed_check_count"
            ),
            "selected_second_carrier_result_bounded_result_recorded": _as_bool(
                request.get("selected_second_carrier_result_bounded_result_recorded")
            ),
            "selected_second_carrier_result_zero_exit_code_not_success": _as_bool(
                request.get("selected_second_carrier_result_zero_exit_code_not_success")
            ),
            "selected_second_carrier_result_ok_not_verification": _as_bool(
                request.get("selected_second_carrier_result_ok_not_verification")
            ),
            "selected_second_carrier_result_ran_7_tests_not_cross_carrier_proof": (
                _as_bool(
                    request.get(
                        "selected_second_carrier_result_"
                        "ran_7_tests_not_cross_carrier_proof"
                    )
                )
            ),
            "selected_second_carrier_result_returned_capture_not_cross_carrier_proof": (
                _as_bool(
                    request.get(
                        "selected_second_carrier_result_"
                        "returned_capture_not_cross_carrier_proof"
                    )
                )
            ),
            "selected_second_carrier_result_first_result_boundary_resolver_preserved": (
                _as_bool(
                    request.get(
                        "selected_second_carrier_result_"
                        "first_result_boundary_resolver_preserved"
                    )
                )
            ),
        }
    if key == "selected_second_carrier_result_boundary_v2_basis":
        return {
            "selected_second_carrier_result_boundary_v2_result_path": _json_safe(
                request.get("selected_second_carrier_result_boundary_v2_result_path")
            ),
            "selected_second_carrier_result_boundary_v2_result_outcome": request.get(
                "selected_second_carrier_result_boundary_v2_result_outcome"
            ),
            "selected_second_carrier_result_boundary_v2_failed_check_count": request.get(
                "selected_second_carrier_result_boundary_v2_failed_check_count"
            ),
        }
    if key == "selected_returned_second_carrier_live_capture_intake_basis":
        return {
            "selected_returned_capture_intake_path": _json_safe(
                request.get("selected_returned_capture_intake_path")
            ),
            "selected_returned_capture_intake_preserved": _as_bool(
                request.get("selected_returned_capture_intake_preserved")
            ),
            "selected_returned_capture_intake_capture_only": _as_bool(
                request.get("selected_returned_capture_intake_capture_only")
            ),
            "selected_returned_capture_from_macbook_pro_to_macbook_air": _as_bool(
                request.get("selected_returned_capture_from_macbook_pro_to_macbook_air")
            ),
        }
    if key == "selected_returned_capture_material_basis":
        return {
            "selected_returned_capture_zip_path": _json_safe(
                request.get("selected_returned_capture_zip_path")
            ),
            "selected_returned_capture_hash_path": _json_safe(
                request.get("selected_returned_capture_hash_path")
            ),
            "selected_returned_capture_extracted_directory_path": _json_safe(
                request.get("selected_returned_capture_extracted_directory_path")
            ),
            "selected_returned_capture_combined_terminal_log_path": _json_safe(
                request.get("selected_returned_capture_combined_terminal_log_path")
            ),
            "selected_returned_capture_stdout_path": _json_safe(
                request.get("selected_returned_capture_stdout_path")
            ),
            "selected_returned_capture_stderr_path": _json_safe(
                request.get("selected_returned_capture_stderr_path")
            ),
            "selected_returned_capture_command_text": _json_safe(
                request.get("selected_returned_capture_command_text")
            ),
            "selected_returned_capture_working_directory": _json_safe(
                request.get("selected_returned_capture_working_directory")
            ),
            "selected_returned_capture_started_at": _json_safe(
                request.get("selected_returned_capture_started_at")
            ),
            "selected_returned_capture_completed_at": _json_safe(
                request.get("selected_returned_capture_completed_at")
            ),
            "selected_returned_capture_exit_code": request.get(
                "selected_returned_capture_exit_code"
            ),
            "selected_returned_capture_ran_7_tests_line": _json_safe(
                request.get("selected_returned_capture_ran_7_tests_line")
            ),
            "selected_returned_capture_ok_line": _json_safe(
                request.get("selected_returned_capture_ok_line")
            ),
            "selected_returned_capture_raw_placeholder_carrier_label": _json_safe(
                request.get("selected_returned_capture_raw_placeholder_carrier_label")
            ),
            "selected_returned_capture_raw_placeholder_carrier_type": _json_safe(
                request.get("selected_returned_capture_raw_placeholder_carrier_type")
            ),
            "selected_returned_capture_placeholder_fields_unrepaired": _as_bool(
                request.get("selected_returned_capture_placeholder_fields_unrepaired")
            ),
        }
    if key == "selected_second_carrier_output_capture_basis":
        return {
            "selected_second_carrier_output_capture_result_path": _json_safe(
                request.get("selected_second_carrier_output_capture_result_path")
            ),
            "selected_second_carrier_output_capture_result_outcome": request.get(
                "selected_second_carrier_output_capture_result_outcome"
            ),
            "selected_second_carrier_output_capture_failed_check_count": request.get(
                "selected_second_carrier_output_capture_failed_check_count"
            ),
        }
    if key == "selected_packet_emission_boundary_v1_predecessor_failure_basis":
        return {
            "v1_predecessor_failure_preserved": True,
            "v1_not_repaired": not _as_bool(request.get("v1_repaired")),
            "v1_not_hidden": not _as_bool(request.get("v1_hidden")),
            "v1_not_claimed_passed": not _as_bool(request.get("v1_claimed_passed")),
        }
    if key == "selected_predecessor_failure_basis":
        return {
            "first_result_boundary_resolver_failure_preserved": True,
            "first_result_boundary_resolver_not_repaired": not _as_bool(
                request.get("first_result_boundary_resolver_repaired")
            ),
            "first_result_boundary_resolver_not_hidden": not _as_bool(
                request.get("first_result_boundary_resolver_hidden")
            ),
            "first_result_boundary_resolver_not_claimed_passed": not _as_bool(
                request.get("first_result_boundary_resolver_claimed_passed")
            ),
        }
    return {}


def _selected_basis(request: Mapping[str, Any], key: str) -> dict[str, Any]:
    supplied = _basis_supplied(request, key)
    basis = {
        "basis_key": key,
        "basis_declared": supplied,
        "basis_role": (
            "reference-shaped second-carrier-success-boundary basis only"
        ),
        "selected_basis_reference_shape_preserved": _as_bool(
            request.get("reference_shaped_input_posture", True)
        ),
        "does_not_create_success": True,
        "does_not_create_verification": True,
        "does_not_create_external_result": True,
        "does_not_create_cross_carrier_evidence": True,
        "does_not_create_portable_verification_closure": True,
        "does_not_create_source_transfer": True,
        "does_not_create_source_receipt": True,
        "does_not_create_reception_authorization": True,
        "does_not_create_source_authority_currentness_runtime_or_final_completion": True,
        "does_not_authorize_follow_on_work": True,
    }
    if supplied:
        basis["selected_basis"] = _json_safe(request.get(key))
    basis.update(_basis_extra(request, key))
    return basis


def _posture(request: Mapping[str, Any], key: str) -> dict[str, Any]:
    declared = _as_bool(request.get(key))
    return {
        "posture_key": key,
        "declared": declared,
        "preserved_as_second_carrier_success_boundary_only": declared,
        "does_not_create_success": True,
        "does_not_create_verification": True,
        "does_not_create_external_result": True,
        "does_not_create_cross_carrier_evidence": True,
        "does_not_create_portable_verification_closure": True,
        "does_not_create_source_transfer_source_receipt_or_reception_authorization": True,
        "does_not_create_source_authority_currentness_runtime_or_final_completion": True,
        "does_not_authorize_follow_on_work": True,
    }


def _basis_missing_code(key: str) -> str:
    if key == "selected_second_carrier_result_basis":
        return "SECOND_CARRIER_RESULT_BASIS_MISSING"
    if key == "selected_second_carrier_result_boundary_v2_basis":
        return "SECOND_CARRIER_RESULT_BOUNDARY_V2_BASIS_MISSING"
    if key == "selected_returned_second_carrier_live_capture_intake_basis":
        return "RETURNED_CAPTURE_INTAKE_BASIS_MISSING"
    if key == "selected_returned_capture_material_basis":
        return "RETURNED_CAPTURE_MATERIAL_MISSING"
    if key == "selected_second_carrier_output_capture_basis":
        return "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_MISSING"
    return "SECOND_CARRIER_RESULT_BASIS_MISSING"


def _build_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    question = request.get("second_carrier_success_boundary_question")
    intent = request.get("second_carrier_success_boundary_intent")
    checks.append(
        _check(
            "second_carrier_success_boundary_question_declared",
            question == CORE_QUESTION,
            CORE_QUESTION,
            question,
            "SECOND_CARRIER_SUCCESS_BOUNDARY_QUESTION_UNDECLARED",
        )
    )
    checks.append(
        _check(
            "second_carrier_success_boundary_intent_supported",
            intent in SUPPORTED_INTENTS,
            list(SUPPORTED_INTENTS),
            intent,
            "SECOND_CARRIER_SUCCESS_BOUNDARY_INTENT_UNSUPPORTED",
        )
    )

    scope = _scope_values(request)
    unsupported_scope = _unsupported_scope_values(request)
    checks.append(
        _check(
            "second_carrier_success_boundary_scope_declared",
            bool(scope),
            "declared supported second-carrier-success-boundary scope",
            scope,
            "UNSUPPORTED_SECOND_CARRIER_SUCCESS_BOUNDARY_SCOPE",
        )
    )
    checks.append(
        _check(
            "second_carrier_success_boundary_scope_supported",
            not unsupported_scope,
            list(SUPPORTED_SCOPE_VALUES),
            unsupported_scope,
            "UNSUPPORTED_SECOND_CARRIER_SUCCESS_BOUNDARY_SCOPE",
        )
    )

    for official_scope in (
        "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
        "RETURNED_RESULT_CONTAINMENT_PRESERVED",
        "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
        "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    ):
        checks.append(
            _check(
                f"{official_scope.lower()}_scope_preserved",
                official_scope in scope,
                "official scope enum string is present and unredacted",
                scope,
                "UNSUPPORTED_SECOND_CARRIER_SUCCESS_BOUNDARY_SCOPE",
            )
        )

    for key in SELECTED_BASIS_KEYS:
        checks.append(
            _check(
                f"{key}_declared",
                _basis_supplied(request, key),
                "selected basis is declared and reference-shaped",
                request.get(key),
                _basis_missing_code(key),
            )
        )

    result_failed_count = _as_int(
        request.get("selected_second_carrier_result_failed_check_count")
    )
    checks.extend(
        [
            _check(
                "second_carrier_result_outcome_recorded",
                request.get("selected_second_carrier_result_result_outcome")
                == EXPECTED_SECOND_CARRIER_RESULT_OUTCOME,
                EXPECTED_SECOND_CARRIER_RESULT_OUTCOME,
                request.get("selected_second_carrier_result_result_outcome"),
                "SECOND_CARRIER_RESULT_NOT_RECORDED",
            ),
            _check(
                "second_carrier_result_version_0_1_0",
                request.get("selected_second_carrier_result_result_version")
                == EXPECTED_SECOND_CARRIER_RESULT_VERSION,
                EXPECTED_SECOND_CARRIER_RESULT_VERSION,
                request.get("selected_second_carrier_result_result_version"),
                "SECOND_CARRIER_RESULT_VERSION_NOT_0_1_0",
            ),
            _check(
                "second_carrier_result_failed_checks_zero",
                result_failed_count == 0,
                0,
                request.get("selected_second_carrier_result_failed_check_count"),
                "SECOND_CARRIER_RESULT_FAILED_CHECKS_PRESENT",
            ),
            _check(
                "second_carrier_result_recorded_bounded_result",
                _as_bool(
                    request.get("selected_second_carrier_result_bounded_result_recorded")
                ),
                True,
                request.get("selected_second_carrier_result_bounded_result_recorded"),
                "SECOND_CARRIER_RESULT_DID_NOT_RECORD_BOUNDED_RESULT",
            ),
            _check(
                "second_carrier_result_did_not_already_create_success",
                not _as_bool(
                    request.get("selected_second_carrier_result_already_created_success")
                ),
                False,
                request.get("selected_second_carrier_result_already_created_success"),
                "SECOND_CARRIER_RESULT_ALREADY_CREATED_SUCCESS",
            ),
            _check(
                "second_carrier_result_did_not_already_create_verification",
                not _as_bool(
                    request.get(
                        "selected_second_carrier_result_already_created_verification"
                    )
                ),
                False,
                request.get(
                    "selected_second_carrier_result_already_created_verification"
                ),
                "SECOND_CARRIER_RESULT_ALREADY_CREATED_VERIFICATION",
            ),
            _check(
                "second_carrier_result_did_not_already_create_external_result",
                not _as_bool(
                    request.get(
                        "selected_second_carrier_result_already_created_external_result"
                    )
                ),
                False,
                request.get(
                    "selected_second_carrier_result_already_created_external_result"
                ),
                "SECOND_CARRIER_RESULT_ALREADY_CREATED_EXTERNAL_RESULT",
            ),
            _check(
                "second_carrier_result_did_not_already_create_cross_carrier_evidence",
                not _as_bool(
                    request.get(
                        "selected_second_carrier_result_"
                        "already_created_cross_carrier_evidence"
                    )
                ),
                False,
                request.get(
                    "selected_second_carrier_result_"
                    "already_created_cross_carrier_evidence"
                ),
                "SECOND_CARRIER_RESULT_ALREADY_CREATED_CROSS_CARRIER_EVIDENCE",
            ),
            _check(
                "second_carrier_result_did_not_treat_result_as_success",
                not _as_bool(
                    request.get("selected_second_carrier_result_treated_result_as_success")
                )
                and _negative_flag(request, "second_carrier_result_treated_as_success"),
                False,
                {
                    "shortcut": request.get(
                        "selected_second_carrier_result_treated_result_as_success"
                    ),
                    "non_claim": _request_non_claims(request).get(
                        "second_carrier_result_treated_as_success"
                    ),
                },
                "SECOND_CARRIER_RESULT_TREATED_RESULT_AS_SUCCESS",
            ),
            _check(
                "second_carrier_result_did_not_treat_result_as_verification",
                not _as_bool(
                    request.get(
                        "selected_second_carrier_result_treated_result_as_verification"
                    )
                )
                and _negative_flag(
                    request, "second_carrier_result_treated_as_verification"
                ),
                False,
                {
                    "shortcut": request.get(
                        "selected_second_carrier_result_treated_result_as_verification"
                    ),
                    "non_claim": _request_non_claims(request).get(
                        "second_carrier_result_treated_as_verification"
                    ),
                },
                "SECOND_CARRIER_RESULT_TREATED_RESULT_AS_VERIFICATION",
            ),
            _check(
                "second_carrier_result_did_not_treat_result_as_external_result",
                not _as_bool(
                    request.get(
                        "selected_second_carrier_result_treated_result_as_external_result"
                    )
                ),
                False,
                request.get(
                    "selected_second_carrier_result_treated_result_as_external_result"
                ),
                "SECOND_CARRIER_RESULT_TREATED_RESULT_AS_EXTERNAL_RESULT",
            ),
            _check(
                "second_carrier_result_did_not_treat_result_as_cross_carrier_evidence",
                not _as_bool(
                    request.get(
                        "selected_second_carrier_result_"
                        "treated_result_as_cross_carrier_evidence"
                    )
                ),
                False,
                request.get(
                    "selected_second_carrier_result_"
                    "treated_result_as_cross_carrier_evidence"
                ),
                "SECOND_CARRIER_RESULT_TREATED_RESULT_AS_CROSS_CARRIER_EVIDENCE",
            ),
            _check(
                "second_carrier_result_kept_zero_exit_code_not_success",
                _as_bool(
                    request.get("selected_second_carrier_result_zero_exit_code_not_success")
                )
                and _negative_flag(request, "zero_exit_code_treated_as_success"),
                True,
                request.get("selected_second_carrier_result_zero_exit_code_not_success"),
                "SECOND_CARRIER_RESULT_TREATED_ZERO_EXIT_CODE_AS_SUCCESS",
            ),
            _check(
                "second_carrier_result_kept_ok_not_verification",
                _as_bool(
                    request.get("selected_second_carrier_result_ok_not_verification")
                )
                and _negative_flag(request, "ok_output_treated_as_verification"),
                True,
                request.get("selected_second_carrier_result_ok_not_verification"),
                "SECOND_CARRIER_RESULT_TREATED_OK_AS_VERIFICATION",
            ),
            _check(
                "second_carrier_result_kept_ran_7_tests_not_cross_carrier_proof",
                _as_bool(
                    request.get(
                        "selected_second_carrier_result_"
                        "ran_7_tests_not_cross_carrier_proof"
                    )
                )
                and _negative_flag(
                    request, "ran_7_tests_treated_as_cross_carrier_proof"
                ),
                True,
                request.get(
                    "selected_second_carrier_result_"
                    "ran_7_tests_not_cross_carrier_proof"
                ),
                "SECOND_CARRIER_RESULT_TREATED_RAN_7_TESTS_AS_CROSS_CARRIER_PROOF",
            ),
            _check(
                "second_carrier_result_kept_returned_capture_not_cross_carrier_proof",
                _as_bool(
                    request.get(
                        "selected_second_carrier_result_"
                        "returned_capture_not_cross_carrier_proof"
                    )
                )
                and _negative_flag(
                    request, "returned_capture_treated_as_cross_carrier_evidence"
                ),
                True,
                request.get(
                    "selected_second_carrier_result_"
                    "returned_capture_not_cross_carrier_proof"
                ),
                "SECOND_CARRIER_RESULT_TREATED_RETURNED_CAPTURE_AS_CROSS_CARRIER_PROOF",
            ),
            _check(
                "second_carrier_result_kept_official_enum_scope_strings_unredacted",
                not _as_bool(
                    request.get(
                        "selected_second_carrier_result_"
                        "official_enum_scope_strings_redacted"
                    )
                ),
                False,
                request.get(
                    "selected_second_carrier_result_official_enum_scope_strings_redacted"
                ),
                "SECOND_CARRIER_RESULT_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
            ),
            _check(
                "second_carrier_result_preserved_first_result_boundary_failure",
                _as_bool(
                    request.get(
                        "selected_second_carrier_result_"
                        "first_result_boundary_resolver_preserved"
                    )
                ),
                True,
                request.get(
                    "selected_second_carrier_result_"
                    "first_result_boundary_resolver_preserved"
                ),
                "FIRST_RESULT_BOUNDARY_RESOLVER_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
            ),
        ]
    )

    boundary_v2_failed_count = _as_int(
        request.get("selected_second_carrier_result_boundary_v2_failed_check_count")
    )
    if _is_present(request.get("selected_second_carrier_result_boundary_v2_result_outcome")):
        checks.append(
            _check(
                "second_carrier_result_boundary_v2_outcome_recorded",
                request.get("selected_second_carrier_result_boundary_v2_result_outcome")
                == EXPECTED_SECOND_CARRIER_RESULT_BOUNDARY_V2_OUTCOME,
                EXPECTED_SECOND_CARRIER_RESULT_BOUNDARY_V2_OUTCOME,
                request.get("selected_second_carrier_result_boundary_v2_result_outcome"),
                "SECOND_CARRIER_RESULT_BOUNDARY_V2_BASIS_MISSING",
            )
        )
    if boundary_v2_failed_count is not None:
        checks.append(
            _check(
                "second_carrier_result_boundary_v2_failed_checks_zero",
                boundary_v2_failed_count == 0,
                0,
                request.get("selected_second_carrier_result_boundary_v2_failed_check_count"),
                "SECOND_CARRIER_RESULT_BOUNDARY_V2_BASIS_MISSING",
            )
        )

    checks.extend(
        [
            _check(
                "returned_capture_intake_preserved",
                _as_bool(request.get("selected_returned_capture_intake_preserved")),
                True,
                request.get("selected_returned_capture_intake_preserved"),
                "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
            ),
            _check(
                "returned_capture_intake_capture_only",
                _as_bool(request.get("selected_returned_capture_intake_capture_only")),
                True,
                request.get("selected_returned_capture_intake_capture_only"),
                "RETURNED_CAPTURE_TREATED_AS_RESULT",
            ),
            _check(
                "returned_capture_from_macbook_pro_to_macbook_air_preserved",
                _as_bool(
                    request.get("selected_returned_capture_from_macbook_pro_to_macbook_air")
                ),
                True,
                request.get("selected_returned_capture_from_macbook_pro_to_macbook_air"),
                "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
            ),
        ]
    )

    for key, code in (
        ("selected_returned_capture_zip_path", "RETURNED_ZIP_PATH_MISSING"),
        ("selected_returned_capture_hash_path", "RETURNED_HASH_PATH_MISSING"),
        (
            "selected_returned_capture_extracted_directory_path",
            "RETURNED_EXTRACTED_DIRECTORY_MISSING",
        ),
        (
            "selected_returned_capture_combined_terminal_log_path",
            "RETURNED_COMBINED_TERMINAL_LOG_MISSING",
        ),
        ("selected_returned_capture_exit_code", "RETURNED_EXIT_CODE_MISSING"),
        ("selected_returned_capture_command_text", "RETURNED_COMMAND_TEXT_MISSING"),
        ("selected_returned_capture_started_at", "RETURNED_TIMESTAMPS_MISSING"),
        ("selected_returned_capture_completed_at", "RETURNED_TIMESTAMPS_MISSING"),
    ):
        checks.append(
            _check(
                f"{key}_declared",
                _is_present(request.get(key)),
                "returned capture material reference declared",
                request.get(key),
                code,
            )
        )

    checks.extend(
        [
            _check(
                "returned_capture_did_not_treat_capture_as_result",
                not _as_bool(request.get("returned_capture_treated_as_result")),
                False,
                request.get("returned_capture_treated_as_result"),
                "RETURNED_CAPTURE_TREATED_AS_RESULT",
            ),
            _check(
                "returned_capture_did_not_treat_capture_as_success",
                not _as_bool(request.get("returned_capture_treated_as_success")),
                False,
                request.get("returned_capture_treated_as_success"),
                "RETURNED_CAPTURE_TREATED_AS_SUCCESS",
            ),
            _check(
                "returned_capture_did_not_treat_capture_as_verification",
                not _as_bool(request.get("returned_capture_treated_as_verification")),
                False,
                request.get("returned_capture_treated_as_verification"),
                "RETURNED_CAPTURE_TREATED_AS_VERIFICATION",
            ),
            _check(
                "returned_capture_did_not_treat_capture_as_cross_carrier_proof",
                _negative_flag(
                    request, "returned_capture_treated_as_cross_carrier_evidence"
                )
                and not _as_bool(
                    request.get("returned_capture_treated_as_cross_carrier_proof")
                ),
                False,
                {
                    "non_claim": _request_non_claims(request).get(
                        "returned_capture_treated_as_cross_carrier_evidence"
                    ),
                    "direct": request.get(
                        "returned_capture_treated_as_cross_carrier_proof"
                    ),
                },
                "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_PROOF",
            ),
            _check(
                "raw_placeholder_carrier_fields_unrepaired",
                _as_bool(
                    request.get("selected_returned_capture_placeholder_fields_unrepaired")
                ),
                True,
                request.get("selected_returned_capture_placeholder_fields_unrepaired"),
                "PLACEHOLDER_CARRIER_FIELDS_REPAIRED",
            ),
        ]
    )

    output_capture_failed_count = _as_int(
        request.get("selected_second_carrier_output_capture_failed_check_count")
    )
    checks.extend(
        [
            _check(
                "second_carrier_output_capture_outcome_recorded",
                request.get("selected_second_carrier_output_capture_result_outcome")
                == EXPECTED_SECOND_CARRIER_OUTPUT_CAPTURE_OUTCOME,
                EXPECTED_SECOND_CARRIER_OUTPUT_CAPTURE_OUTCOME,
                request.get("selected_second_carrier_output_capture_result_outcome"),
                "SECOND_CARRIER_OUTPUT_CAPTURE_NOT_RECORDED",
            ),
            _check(
                "second_carrier_output_capture_failed_checks_zero",
                output_capture_failed_count == 0,
                0,
                request.get("selected_second_carrier_output_capture_failed_check_count"),
                "SECOND_CARRIER_OUTPUT_CAPTURE_FAILED_CHECKS_PRESENT",
            ),
        ]
    )

    for key in POSTURE_KEYS:
        checks.append(
            _check(
                f"{key}_declared",
                _as_bool(request.get(key)),
                "required second-carrier-success-boundary posture declared",
                request.get(key),
                "NON_CLAIM_MISSING_OR_FLIPPED",
            )
        )

    checks.extend(
        [
            _check(
                "selected_basis_reference_shape_preserved",
                _as_bool(request.get("reference_shaped_input_posture", True)),
                True,
                request.get("reference_shaped_input_posture", True),
                "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
            ),
            _check(
                "hostile_raw_body_content_contained",
                not _serialized_contains_hostile_sentinel(request),
                "hostile raw body sentinel absent after bounded sanitization",
                "contained",
                "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_SUCCESS_BOUNDARY",
            ),
            _check(
                "raw_full_prior_artifact_body_not_returned",
                _negative_flag(request, "raw_full_prior_artifact_body_returned"),
                False,
                _request_non_claims(request).get("raw_full_prior_artifact_body_returned"),
                "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
            ),
            _check(
                "consumed_request_token_remains_closed",
                _negative_flag(request, "consumed_request_reopened"),
                False,
                _request_non_claims(request).get("consumed_request_reopened"),
                "CONSUMED_REQUEST_REOPENED",
            ),
            _check(
                "authorization_token_reuse_blocked",
                _negative_flag(request, "authorization_token_reused"),
                False,
                _request_non_claims(request).get("authorization_token_reused"),
                "AUTHORIZATION_TOKEN_REUSED",
            ),
            _check(
                "returned_capture_material_not_mutated",
                _negative_flag(request, "returned_capture_material_mutated"),
                False,
                _request_non_claims(request).get("returned_capture_material_mutated"),
                "RETURNED_CAPTURE_MATERIAL_MUTATED",
            ),
        ]
    )

    for key, code in (
        (
            "command_report_lineage_treated_as_current_report_artifact",
            "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENT_REPORT_ARTIFACT",
        ),
        ("command_report_lineage_treated_as_source", "COMMAND_REPORT_LINEAGE_TREATED_AS_SOURCE"),
        (
            "command_report_lineage_treated_as_authority",
            "COMMAND_REPORT_LINEAGE_TREATED_AS_AUTHORITY",
        ),
        (
            "command_report_lineage_treated_as_currentness",
            "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENTNESS",
        ),
        (
            "full_prior_artifact_body_emitted_outside_bounded_success_boundary",
            "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_SUCCESS_BOUNDARY",
        ),
        ("artifacts_mutated", "ARTIFACTS_MUTATED"),
    ):
        checks.append(
            _check(
                f"{key}_false",
                not _as_bool(request.get(key)),
                False,
                request.get(key),
                code,
            )
        )

    non_claims_false, bad_non_claims = _declared_non_claims_false(request)
    checks.append(
        _check(
            "required_non_claims_false",
            non_claims_false,
            "all required non-claims explicit false",
            bad_non_claims,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    for key in REQUIRED_FALSE_NON_CLAIMS:
        checks.append(
            _check(
                f"non_claim_{key}_false",
                _request_non_claims(request).get(key) is False,
                False,
                _request_non_claims(request).get(key),
                NON_CLAIM_BLOCK_CODE_BY_KEY.get(key, "NON_CLAIM_MISSING_OR_FLIPPED"),
            )
        )

    return checks


def _first_failed_check(checks: Sequence[Mapping[str, Any]]) -> Mapping[str, Any] | None:
    for check in checks:
        if not check.get("passed"):
            return check
    return None


def _statement(outcome: str) -> dict[str, bool]:
    recorded = outcome == OUTCOME_RECORDED
    return {
        "second_carrier_success_boundary_recorded": recorded,
        "one_future_second_carrier_success_step_declared": recorded,
        "second_carrier_result_basis_preserved": recorded,
        "second_carrier_result_boundary_v2_basis_preserved": recorded,
        "returned_second_carrier_capture_basis_preserved": recorded,
        "capture_intake_basis_preserved": recorded,
        "second_carrier_output_capture_basis_preserved": recorded,
        "result_artifact_basis_preserved": recorded,
        "success_not_created": True,
        "success_boundary_not_success": True,
        "result_not_success": True,
        "result_not_verification": True,
        "zero_exit_code_not_success": True,
        "ok_output_not_verification": True,
        "ran_7_tests_not_cross_carrier_proof": True,
        "returned_capture_not_cross_carrier_proof": True,
        "verification_not_created": True,
        "external_result_not_created": True,
        "cross_carrier_evidence_not_created": True,
        "portable_verification_closure_not_created": True,
        "success_not_source_transfer": True,
        "success_not_source_receipt": True,
        "success_not_reception_authorization": True,
        "receiving_carrier_not_authority": True,
        "source_not_created": True,
        "authority_not_created": True,
        "currentness_not_created": True,
        "final_completion_not_created": True,
        "runtime_not_created": True,
        "continuation_not_authorized": True,
        "reusable_permission_not_created": True,
        "follow_on_work_not_authorized": True,
        "hidden_repo_state_excluded": True,
        "hidden_repo_state_not_used_as_success_authority": True,
        "repo_local_availability_not_success_authority": True,
        "selected_basis_reference_shape_preserved": True,
        "raw_full_prior_artifact_body_not_returned": True,
        "official_enum_scope_strings_not_redacted": True,
        "hostile_raw_body_content_contained": True,
        "first_result_boundary_resolver_failure_preserved": True,
        "authorization_token_reuse_blocked": True,
        "consumed_request_token_remains_closed": True,
        "v1_predecessor_failure_preserved": True,
        "v1_not_repaired": True,
        "v1_not_hidden": True,
        "v1_not_claimed_passed": True,
    }


def _non_meaning() -> dict[str, bool]:
    return {
        "second_carrier_success_exists": False,
        "verification_has_occurred": False,
        "external_result_exists": False,
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
        "success_boundary_became_success": False,
        "success_boundary_became_verification": False,
        "success_boundary_became_external_result": False,
        "success_boundary_became_cross_carrier_proof": False,
        "success_boundary_became_portable_verification_closure": False,
        "success_boundary_became_source_transfer_source_receipt_or_reception_authorization": False,
        "success_boundary_became_source_authority_or_currentness": False,
        "result_became_success": False,
        "result_became_verification": False,
        "zero_exit_code_became_success": False,
        "ok_became_verification": False,
        "ran_7_tests_became_cross_carrier_proof": False,
        "returned_capture_became_proof": False,
        "macbook_pro_became_authority": False,
        "macbook_air_became_source": False,
        "artifact_existence_became_success_authority": False,
        "artifact_path_became_currentness": False,
        "repo_local_availability_became_success_authority": False,
        "hidden_repo_state_became_success_authority": False,
        "first_result_boundary_resolver_was_repaired_hidden_erased_or_claimed_passed": False,
        "v1_packet_emission_boundary_resolver_was_repaired_hidden_erased_or_claimed_passed": False,
    }


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "second-carrier success boundary test",
            "second-carrier success boundary live artifact",
            "second-carrier success boundary terminal summary, if needed",
            "second-carrier success spec/resolver/test/live artifact",
            "verification boundary/spec/resolver/test/live artifact, if ever admitted",
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
        ],
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }


def _additional_basis_required(
    outcome: str, checks: Sequence[Mapping[str, Any]], request: Mapping[str, Any]
) -> dict[str, Any]:
    if outcome != OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        return {
            "additional_basis_required": False,
            "missing_or_unclear_basis": [],
            "missing_basis_scheduled": False,
            "missing_basis_authorized": False,
            "missing_basis_executed": False,
        }
    failed = [check for check in checks if not check.get("passed")]
    declared_context = request.get("additional_basis_context", failed)
    return {
        "additional_basis_required": True,
        "missing_or_unclear_basis": _json_safe(declared_context),
        "missing_basis_scheduled": False,
        "missing_basis_authorized": False,
        "missing_basis_executed": False,
    }


def _not_recorded_basis(
    outcome: str, checks: Sequence[Mapping[str, Any]], request: Mapping[str, Any]
) -> dict[str, Any]:
    if outcome != OUTCOME_NOT_RECORDED:
        return {
            "not_recorded": False,
            "not_recorded_basis": [],
            "prior_artifacts_mutated": False,
            "next_work_authorized": False,
        }
    declared = request.get("not_recorded_basis")
    if not _is_present(declared):
        declared = [check for check in checks if not check.get("passed")]
    return {
        "not_recorded": True,
        "not_recorded_basis": _json_safe(declared),
        "prior_artifacts_mutated": False,
        "next_work_authorized": False,
    }


def _block(block_code: str | None, reason: Any = None) -> dict[str, Any] | None:
    if block_code is None:
        return None
    return {
        "blocked": True,
        "block_code": block_code,
        "block_reason": _json_safe(reason),
    }


def _result_id(request: Mapping[str, Any]) -> str:
    request_id = request.get("second_carrier_success_boundary_request_id")
    if isinstance(request_id, str) and request_id.strip():
        return f"{request_id.strip()}__portable_source_body_verification_second_carrier_success_boundary_result"
    return "portable_source_body_verification_second_carrier_success_boundary_result"


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: Sequence[Mapping[str, Any]],
    block_code: str | None = None,
    block_reason: Any = None,
) -> dict[str, Any]:
    result: dict[str, Any] = {}
    result_id = _result_id(request)
    non_claims = _false_non_claims()
    non_claims.update(
        {
            key: False
            for key, value in _request_non_claims(request).items()
            if key in REQUIRED_FALSE_NON_CLAIMS and value is False
        }
    )
    statement = _statement(outcome)

    result["portable_source_body_verification_second_carrier_success_boundary_metadata"] = {
        "portable_source_body_verification_second_carrier_success_boundary_result_id": result_id,
        "portable_source_body_verification_second_carrier_success_boundary_result_type": RESULT_TYPE,
        "portable_source_body_verification_second_carrier_success_boundary_result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
        "source_material_mutated": False,
        "returned_capture_material_mutated": False,
        "second_carrier_result_material_mutated": False,
    }
    result["declared_second_carrier_success_boundary_question"] = {
        "second_carrier_success_boundary_request_id": request.get(
            "second_carrier_success_boundary_request_id"
        ),
        "question": request.get("second_carrier_success_boundary_question"),
        "intent": request.get("second_carrier_success_boundary_intent"),
        "core_question": CORE_QUESTION,
    }
    for key in SELECTED_BASIS_KEYS:
        result[key] = _selected_basis(request, key)
    for key in POSTURE_KEYS:
        result[key] = _posture(request, key)

    result["second_carrier_success_boundary_scope"] = list(_scope_values(request))
    result["second_carrier_success_boundary_checks"] = list(checks)
    result["second_carrier_success_boundary_statement"] = statement
    result["second_carrier_success_boundary_non_meaning"] = _non_meaning()
    result["additional_basis_required"] = _additional_basis_required(
        outcome, checks, request
    )
    result["not_recorded_basis"] = _not_recorded_basis(outcome, checks, request)
    result["what_remains_open"] = _what_remains_open()
    result["non_claims"] = non_claims
    result["outcome"] = outcome
    result["block"] = _block(block_code, block_reason)
    result[
        "portable_source_body_verification_second_carrier_success_boundary_summary"
    ] = build_portable_source_body_verification_second_carrier_success_boundary_summary(
        result
    )
    return _json_safe(result)


def _blocked_result(block_code: str, reason: Any = None) -> dict[str, Any]:
    request = {
        "second_carrier_success_boundary_request_id": (
            "portable_source_body_verification_second_carrier_success_boundary_blocked"
        ),
        "second_carrier_success_boundary_question": None,
        "second_carrier_success_boundary_intent": None,
        "second_carrier_success_boundary_scope": (),
        "declared_non_claims": _false_non_claims(),
    }
    checks = [
        _check(
            "declared_second_carrier_success_boundary_request_malformed",
            False,
            "mapping request with declared second-carrier-success-boundary question",
            reason,
            block_code,
        )
    ]
    return _build_result(request, OUTCOME_BLOCKED, checks, block_code, reason)


def resolve_portable_source_body_verification_second_carrier_success_boundary(
    declared_second_carrier_success_boundary_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded second-carrier success-boundary request."""

    if declared_second_carrier_success_boundary_request is None:
        return _blocked_result(
            "DECLARED_SECOND_CARRIER_SUCCESS_BOUNDARY_REQUEST_MALFORMED",
            "declared request missing",
        )
    if not isinstance(declared_second_carrier_success_boundary_request, Mapping):
        return _blocked_result(
            "DECLARED_SECOND_CARRIER_SUCCESS_BOUNDARY_REQUEST_MALFORMED",
            "declared request must be a mapping",
        )

    request = copy.deepcopy(dict(declared_second_carrier_success_boundary_request))
    request = _json_safe(request)
    checks = _build_checks(request)

    intent = request.get("second_carrier_success_boundary_intent")
    if intent == INTENT_BLOCK:
        return _build_result(
            request,
            OUTCOME_BLOCKED,
            checks,
            "SECOND_CARRIER_SUCCESS_BOUNDARY_BLOCK_REQUESTED",
            request.get("block_reason", "declared block intent"),
        )

    failed = _first_failed_check(checks)
    if failed is not None:
        code = str(failed.get("block_code") or "NON_CLAIM_MISSING_OR_FLIPPED")
        return _build_result(request, OUTCOME_BLOCKED, checks, code, failed)

    requested_outcome = request.get("requested_second_carrier_success_boundary_outcome")
    if intent == INTENT_DO_NOT_RECORD or requested_outcome == OUTCOME_NOT_RECORDED:
        return _build_result(
            request,
            OUTCOME_NOT_RECORDED,
            checks,
            None,
            request.get("not_recorded_basis", "declared not-recorded posture"),
        )
    if requested_outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        return _build_result(
            request,
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            checks,
            None,
            request.get("additional_basis_context", "declared additional basis posture"),
        )
    if requested_outcome == OUTCOME_BLOCKED:
        return _build_result(
            request,
            OUTCOME_BLOCKED,
            checks,
            "SECOND_CARRIER_SUCCESS_BOUNDARY_BLOCK_REQUESTED",
            request.get("block_reason", "declared blocked posture"),
        )
    return _build_result(request, OUTCOME_RECORDED, checks)


def resolve_portable_source_body_verification_second_carrier_success_boundary_from_path(
    declared_second_carrier_success_boundary_request_path: Path | str,
) -> dict[str, Any]:
    """Load and resolve a declared second-carrier success-boundary JSON object."""

    path = Path(declared_second_carrier_success_boundary_request_path)
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise PortableSourceBodyVerificationSecondCarrierSuccessBoundaryError(
            f"declared second-carrier success-boundary request unreadable: {path}"
        ) from exc
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise PortableSourceBodyVerificationSecondCarrierSuccessBoundaryError(
            f"declared second-carrier success-boundary request malformed JSON: {path}"
        ) from exc
    if not isinstance(parsed, Mapping):
        return _blocked_result(
            "DECLARED_SECOND_CARRIER_SUCCESS_BOUNDARY_REQUEST_MALFORMED",
            "declared request JSON must be an object",
        )
    return resolve_portable_source_body_verification_second_carrier_success_boundary(
        parsed
    )


def build_portable_source_body_verification_second_carrier_success_boundary_summary(
    result: Mapping[str, Any]
) -> dict[str, Any]:
    """Build a bounded summary for a second-carrier success-boundary result."""

    checks = result.get("second_carrier_success_boundary_checks", [])
    if not isinstance(checks, Sequence) or isinstance(checks, (str, bytes, bytearray)):
        checks = []
    passed_count = sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed"))
    failed_count = sum(
        1 for check in checks if isinstance(check, Mapping) and not check.get("passed")
    )
    metadata = result.get(
        "portable_source_body_verification_second_carrier_success_boundary_metadata", {}
    )
    if not isinstance(metadata, Mapping):
        metadata = {}
    question = result.get("declared_second_carrier_success_boundary_question", {})
    if not isinstance(question, Mapping):
        question = {}
    statement = result.get("second_carrier_success_boundary_statement", {})
    if not isinstance(statement, Mapping):
        statement = {}
    non_claims = result.get("non_claims", {})
    if not isinstance(non_claims, Mapping):
        non_claims = {}
    block = result.get("block")
    block_code = None
    block_reason = None
    if isinstance(block, Mapping):
        block_code = block.get("block_code")
        block_reason = block.get("block_reason")
    selected_result = result.get("selected_second_carrier_result_basis", {})
    if not isinstance(selected_result, Mapping):
        selected_result = {}
    selected_capture = result.get("selected_returned_capture_material_basis", {})
    if not isinstance(selected_capture, Mapping):
        selected_capture = {}
    selected_intake = result.get(
        "selected_returned_second_carrier_live_capture_intake_basis", {}
    )
    if not isinstance(selected_intake, Mapping):
        selected_intake = {}

    summary = {
        "outcome": result.get("outcome"),
        "block_code": block_code,
        "block_reason": block_reason,
        "request_id": question.get("second_carrier_success_boundary_request_id"),
        "question": question.get("question"),
        "intent": question.get("intent"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": metadata.get(
            "portable_source_body_verification_second_carrier_success_boundary_result_version"
        ),
        "resolver_module": metadata.get("resolver_module"),
        "selected_second_carrier_result_outcome": selected_result.get(
            "selected_second_carrier_result_result_outcome"
        ),
        "selected_second_carrier_result_version": selected_result.get(
            "selected_second_carrier_result_result_version"
        ),
        "selected_second_carrier_result_failed_check_count": selected_result.get(
            "selected_second_carrier_result_failed_check_count"
        ),
        "selected_returned_capture_intake_path": selected_intake.get(
            "selected_returned_capture_intake_path"
        ),
        "selected_returned_capture_zip_path": selected_capture.get(
            "selected_returned_capture_zip_path"
        ),
        "selected_returned_capture_hash_path": selected_capture.get(
            "selected_returned_capture_hash_path"
        ),
        "selected_returned_capture_extracted_directory_path": selected_capture.get(
            "selected_returned_capture_extracted_directory_path"
        ),
        "selected_returned_capture_exit_code": selected_capture.get(
            "selected_returned_capture_exit_code"
        ),
        "selected_returned_capture_ok_line": selected_capture.get(
            "selected_returned_capture_ok_line"
        ),
        "no_success_verification_external_result_cross_carrier_evidence_or_portable_closure": (
            bool(statement.get("success_not_created"))
            and bool(statement.get("verification_not_created"))
            and bool(statement.get("external_result_not_created"))
            and bool(statement.get("cross_carrier_evidence_not_created"))
            and bool(statement.get("portable_verification_closure_not_created"))
        ),
        "no_source_authority_currentness_final_completion_or_runtime": (
            bool(statement.get("source_not_created"))
            and bool(statement.get("authority_not_created"))
            and bool(statement.get("currentness_not_created"))
            and bool(statement.get("final_completion_not_created"))
            and bool(statement.get("runtime_not_created"))
        ),
        "no_deployment_public_release_or_follow_on": (
            non_claims.get("deployment_created") is False
            and non_claims.get("public_release_created") is False
            and non_claims.get("follow_on_work_authorized") is False
        ),
        "key_non_claims": {
            key: non_claims.get(key)
            for key in (
                "second_carrier_success_created",
                "verification_created",
                "external_result_created",
                "cross_carrier_evidence_created",
                "portable_verification_closure_created",
                "source_created",
                "authority_created",
                "currentness_created",
                "final_completion_claimed",
                "runtime_hosting_created",
                "deployment_created",
                "public_release_created",
                "follow_on_work_authorized",
                "consumed_request_reopened",
                "authorization_token_reused",
            )
        },
        "v1_predecessor_failure_preserved": statement.get(
            "v1_predecessor_failure_preserved"
        ),
        "v1_not_repaired": statement.get("v1_not_repaired"),
        "v1_not_hidden": statement.get("v1_not_hidden"),
        "v1_not_claimed_passed": statement.get("v1_not_claimed_passed"),
        "first_result_boundary_resolver_preserved_as_failed_predecessor": statement.get(
            "first_result_boundary_resolver_failure_preserved"
        ),
    }
    for key in ALLOWED_TRUE_RECORDED_FIELDS:
        summary[key] = bool(statement.get(key))
    return _json_safe(summary)


def write_portable_source_body_verification_second_carrier_success_boundary_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write a bounded second-carrier success-boundary result JSON artifact."""

    if not isinstance(result, Mapping):
        raise PortableSourceBodyVerificationSecondCarrierSuccessBoundaryError(
            "second-carrier success-boundary result must be a mapping"
        )
    metadata = result.get(
        "portable_source_body_verification_second_carrier_success_boundary_metadata", {}
    )
    if not isinstance(metadata, Mapping):
        metadata = {}
    result_id = metadata.get(
        "portable_source_body_verification_second_carrier_success_boundary_result_id",
        "portable_source_body_verification_second_carrier_success_boundary_result",
    )
    filename = f"{result_id}.json"
    if output_path is None:
        destination = Path(OUTPUT_ROOT) / filename
    else:
        supplied = Path(output_path)
        destination = supplied / filename if supplied.suffix == "" else supplied
    destination.parent.mkdir(parents=True, exist_ok=True)
    candidate = destination
    if candidate.exists():
        stem = candidate.stem
        suffix = candidate.suffix
        counter = 1
        while candidate.exists():
            candidate = candidate.with_name(f"{stem}_{counter:03d}{suffix}")
            counter += 1
    candidate.write_text(
        json.dumps(_json_safe(result), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return candidate


def build_declared_portable_source_body_verification_second_carrier_success_boundary_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Build a clean declared second-carrier success-boundary request."""

    request_id = overrides.pop(
        "second_carrier_success_boundary_request_id",
        "portable_source_body_verification_second_carrier_success_boundary_reference_review_001",
    )
    request: dict[str, Any] = {
        "second_carrier_success_boundary_request_id": request_id,
        "second_carrier_success_boundary_question": CORE_QUESTION,
        "second_carrier_success_boundary_intent": INTENT_RECORD,
        "second_carrier_success_boundary_scope": list(SUPPORTED_SCOPE_VALUES),
        "declared_non_claims": _false_non_claims(),
        "reference_shaped_input_posture": True,
        "selected_second_carrier_result_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_"
            "verification_second_carrier_result/"
            "portable_source_body_verification_second_carrier_result_reference_review_"
            "001__portable_source_body_verification_second_carrier_result_result.json"
        ),
        "selected_second_carrier_result_result_outcome": (
            EXPECTED_SECOND_CARRIER_RESULT_OUTCOME
        ),
        "selected_second_carrier_result_result_version": (
            EXPECTED_SECOND_CARRIER_RESULT_VERSION
        ),
        "selected_second_carrier_result_failed_check_count": 0,
        "selected_second_carrier_result_bounded_result_recorded": True,
        "selected_second_carrier_result_already_created_success": False,
        "selected_second_carrier_result_already_created_verification": False,
        "selected_second_carrier_result_already_created_external_result": False,
        "selected_second_carrier_result_already_created_cross_carrier_evidence": False,
        "selected_second_carrier_result_treated_result_as_success": False,
        "selected_second_carrier_result_treated_result_as_verification": False,
        "selected_second_carrier_result_treated_result_as_external_result": False,
        "selected_second_carrier_result_treated_result_as_cross_carrier_evidence": False,
        "selected_second_carrier_result_zero_exit_code_not_success": True,
        "selected_second_carrier_result_ok_not_verification": True,
        "selected_second_carrier_result_ran_7_tests_not_cross_carrier_proof": True,
        "selected_second_carrier_result_returned_capture_not_cross_carrier_proof": True,
        "selected_second_carrier_result_official_enum_scope_strings_redacted": False,
        "selected_second_carrier_result_official_enum_scope_strings_not_redacted": True,
        "selected_second_carrier_result_first_result_boundary_resolver_preserved": True,
        "selected_second_carrier_result_boundary_v2_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_"
            "verification_second_carrier_result_boundary_v2/"
            "portable_source_body_verification_second_carrier_result_boundary_"
            "reference_review_001_v2__portable_source_body_verification_second_"
            "carrier_result_boundary_v2_result.json"
        ),
        "selected_second_carrier_result_boundary_v2_result_outcome": (
            EXPECTED_SECOND_CARRIER_RESULT_BOUNDARY_V2_OUTCOME
        ),
        "selected_second_carrier_result_boundary_v2_failed_check_count": 0,
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
            "python -m unittest tests/test_resolve_portable_source_body_"
            "verification_second_carrier_result.py"
        ),
        "selected_returned_capture_working_directory": (
            "/Users/markomarkota/IAMMAI-SYSTEM"
        ),
        "selected_returned_capture_started_at": "2026-05-09T00:00:00Z",
        "selected_returned_capture_completed_at": "2026-05-09T00:00:01Z",
        "selected_returned_capture_exit_code": 0,
        "selected_returned_capture_ran_7_tests_line": "Ran 7 tests in 0.451s",
        "selected_returned_capture_ok_line": "OK",
        "selected_returned_capture_raw_placeholder_carrier_label": (
            "raw placeholder carrier label preserved"
        ),
        "selected_returned_capture_raw_placeholder_carrier_type": (
            "raw placeholder carrier type preserved"
        ),
        "selected_returned_capture_placeholder_fields_unrepaired": True,
        "selected_second_carrier_output_capture_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_"
            "verification_second_carrier_output_capture/"
            "portable_source_body_verification_second_carrier_output_capture_result.json"
        ),
        "selected_second_carrier_output_capture_result_outcome": (
            EXPECTED_SECOND_CARRIER_OUTPUT_CAPTURE_OUTCOME
        ),
        "selected_second_carrier_output_capture_failed_check_count": 0,
    }

    for key in SELECTED_BASIS_KEYS:
        request[key] = {
            "basis_id": key,
            "basis_role": "reference-shaped success-boundary basis only",
            "basis_reference_shape_preserved": True,
            "does_not_create_success": True,
            "does_not_create_verification": True,
            "does_not_create_external_result": True,
            "does_not_create_cross_carrier_evidence": True,
            "does_not_create_portable_verification_closure": True,
            "does_not_authorize_follow_on_work": True,
        }
    for key in POSTURE_KEYS:
        request[key] = True

    request.update(overrides)
    if "declared_non_claims" not in overrides:
        request["declared_non_claims"] = _false_non_claims()
    else:
        merged_non_claims = _false_non_claims()
        declared = overrides.get("declared_non_claims")
        if isinstance(declared, Mapping):
            merged_non_claims.update({str(key): value for key, value in declared.items()})
        request["declared_non_claims"] = merged_non_claims
    return _json_safe(request)
