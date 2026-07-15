"""Resolve portable source-body verification cross-carrier evidence boundary.

This module records one bounded future cross-carrier evidence review-step
boundary only. It is downstream of the second-carrier external-result line.
It does not create cross-carrier evidence, portable verification closure,
source transfer, source receipt, reception authorization, source, authority,
currentness, final completion, runtime, continuation, reusable permission,
derivative reception, vessel relation, another reception request, or follow-on
work.
"""

from __future__ import annotations

import copy
import datetime
import json
from pathlib import Path
from typing import Any, Mapping


class PortableSourceBodyVerificationCrossCarrierEvidenceBoundaryError(Exception):
    """Raised for unreadable declared paths or impossible resolver shape."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_portable_source_body_verification_cross_carrier_evidence_boundary"
)
RESULT_TYPE = "portable_source_body_verification_cross_carrier_evidence_boundary_result"
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_portable_source_body_verification_"
    "cross_carrier_evidence_boundary"
)

CORE_QUESTION = (
    "Can the clean second-carrier-external-result basis be bounded for one "
    "future cross-carrier evidence review step without creating cross-carrier "
    "evidence yet, portable verification closure, source transfer, source "
    "receipt, reception authorization, source, authority, currentness, "
    "runtime, final completion, continuation, reusable permission, derivative "
    "reception, vessel relation, another reception request, or follow-on work?"
)

OUTCOME_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_CROSS_CARRIER_EVIDENCE_BOUNDARY_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_CROSS_CARRIER_EVIDENCE_BOUNDARY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_CROSS_CARRIER_EVIDENCE_BOUNDARY_"
    "REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_CROSS_CARRIER_EVIDENCE_BOUNDARY_BLOCKED"
)
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_CROSS_CARRIER_EVIDENCE_BOUNDARY"
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_CROSS_CARRIER_EVIDENCE_BOUNDARY"
)
INTENT_BLOCK = "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_CROSS_CARRIER_EVIDENCE_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

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
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_ONLY",
    "ONE_FUTURE_CROSS_CARRIER_EVIDENCE_REVIEW_STEP_ONLY",
    "SECOND_CARRIER_EXTERNAL_RESULT_BASIS_PRESERVED",
    "EXTERNAL_RESULT_ARTIFACT_BASIS_PRESERVED",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_BASIS_PRESERVED",
    "SECOND_CARRIER_VERIFICATION_BASIS_PRESERVED",
    "RETURNED_SECOND_CARRIER_CAPTURE_BASIS_PRESERVED",
    "CAPTURE_INTAKE_BASIS_PRESERVED",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_PRESERVED",
    "CROSS_CARRIER_EVIDENCE_NOT_CREATED",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_NOT_CROSS_CARRIER_EVIDENCE",
    "EXTERNAL_RESULT_NOT_CROSS_CARRIER_EVIDENCE",
    "ZERO_EXIT_CODE_NOT_CROSS_CARRIER_EVIDENCE",
    "STRING_ZERO_NOT_CROSS_CARRIER_EVIDENCE",
    "OK_OUTPUT_NOT_CROSS_CARRIER_EVIDENCE",
    "RAN_7_TESTS_NOT_CROSS_CARRIER_EVIDENCE",
    "RETURNED_CAPTURE_NOT_CROSS_CARRIER_EVIDENCE",
    "PORTABLE_VERIFICATION_CLOSURE_NOT_CREATED",
    "CROSS_CARRIER_EVIDENCE_NOT_SOURCE_TRANSFER",
    "CROSS_CARRIER_EVIDENCE_NOT_SOURCE_RECEIPT",
    "CROSS_CARRIER_EVIDENCE_NOT_RECEPTION_AUTHORIZATION",
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
    "HIDDEN_REPO_STATE_NOT_USED_AS_CROSS_CARRIER_EVIDENCE_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_NOT_CROSS_CARRIER_EVIDENCE_AUTHORITY",
    "SELECTED_BASIS_REFERENCE_SHAPE_PRESERVED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
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
SUPPORTED_CROSS_CARRIER_EVIDENCE_BOUNDARY_SCOPE = SUPPORTED_SCOPE_VALUES

ALLOWED_TRUE_RECORDED_FIELDS = (
    "cross_carrier_evidence_boundary_recorded",
    "one_future_cross_carrier_evidence_review_step_declared",
    "second_carrier_external_result_basis_preserved",
    "external_result_artifact_basis_preserved",
    "second_carrier_external_result_boundary_basis_preserved",
    "second_carrier_verification_basis_preserved",
    "returned_second_carrier_capture_basis_preserved",
    "capture_intake_basis_preserved",
    "second_carrier_output_capture_basis_preserved",
    "cross_carrier_evidence_not_created",
    "cross_carrier_evidence_boundary_not_cross_carrier_evidence",
    "external_result_not_cross_carrier_evidence",
    "zero_exit_code_not_cross_carrier_evidence",
    "string_zero_not_cross_carrier_evidence",
    "ok_output_not_cross_carrier_evidence",
    "ran_7_tests_not_cross_carrier_evidence",
    "returned_capture_not_cross_carrier_evidence",
    "portable_verification_closure_not_created",
    "cross_carrier_evidence_not_source_transfer",
    "cross_carrier_evidence_not_source_receipt",
    "cross_carrier_evidence_not_reception_authorization",
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
    "hidden_repo_state_not_used_as_cross_carrier_evidence_authority",
    "repo_local_availability_not_cross_carrier_evidence_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "official_enum_scope_strings_not_redacted",
    "hostile_raw_body_content_contained",
    "predecessor_external_result_v1_failure_preserved",
    "first_success_boundary_test_failure_preserved",
    "first_result_boundary_resolver_failure_preserved",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
)

REQUIRED_FALSE_NON_CLAIMS = (
    "cross_carrier_evidence_created",
    "portable_verification_closure_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "cross_carrier_evidence_boundary_treated_as_cross_carrier_evidence",
    "cross_carrier_evidence_boundary_treated_as_portable_verification_closure",
    "cross_carrier_evidence_boundary_treated_as_source_transfer",
    "cross_carrier_evidence_boundary_treated_as_source_receipt",
    "cross_carrier_evidence_boundary_treated_as_reception_authorization",
    "cross_carrier_evidence_boundary_treated_as_source",
    "cross_carrier_evidence_boundary_treated_as_authority",
    "cross_carrier_evidence_boundary_treated_as_currentness",
    "cross_carrier_evidence_boundary_treated_as_final_completion",
    "cross_carrier_evidence_boundary_treated_as_runtime",
    "cross_carrier_evidence_boundary_treated_as_continuation",
    "cross_carrier_evidence_boundary_treated_as_reusable_permission",
    "cross_carrier_evidence_boundary_treated_as_follow_on_work",
    "second_carrier_external_result_treated_as_cross_carrier_evidence",
    "zero_exit_code_treated_as_cross_carrier_evidence",
    "string_zero_treated_as_cross_carrier_evidence",
    "string_zero_representation_turned_into_doctrine",
    "ok_output_treated_as_cross_carrier_evidence",
    "ran_7_tests_treated_as_cross_carrier_proof",
    "returned_capture_treated_as_cross_carrier_evidence",
    "receiving_carrier_treated_as_authority",
    "artifact_existence_treated_as_cross_carrier_evidence_authority",
    "artifact_path_treated_as_currentness",
    "repo_local_availability_treated_as_cross_carrier_evidence_authority",
    "hidden_repo_state_used_as_cross_carrier_evidence_content",
    "hidden_repo_state_used_as_cross_carrier_evidence_authority",
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
    "DECLARED_CROSS_CARRIER_EVIDENCE_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_CROSS_CARRIER_EVIDENCE_BOUNDARY_REQUEST_UNREADABLE",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_QUESTION_UNDECLARED",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_INTENT_UNSUPPORTED",
    "SECOND_CARRIER_EXTERNAL_RESULT_BASIS_MISSING",
    "SECOND_CARRIER_EXTERNAL_RESULT_NOT_RECORDED",
    "SECOND_CARRIER_EXTERNAL_RESULT_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_EXTERNAL_RESULT_VERSION_NOT_0_1_0",
    "SECOND_CARRIER_EXTERNAL_RESULT_DID_NOT_RECORD_BOUNDED_EXTERNAL_RESULT",
    "SECOND_CARRIER_EXTERNAL_RESULT_ALREADY_CREATED_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXTERNAL_RESULT_ALREADY_CREATED_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_EXTERNAL_RESULT_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_EXTERNAL_RESULT_AS_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_ZERO_EXIT_CODE_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_STRING_ZERO_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_STRING_ZERO_AS_DOCTRINE",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_OK_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_RAN_7_TESTS_AS_CROSS_CARRIER_PROOF",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_RETURNED_CAPTURE_AS_CROSS_CARRIER_PROOF",
    "SECOND_CARRIER_EXTERNAL_RESULT_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
    "PREDECESSOR_EXTERNAL_RESULT_V1_FAILURE_MISSING_OR_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_BASIS_MISSING",
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
    "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "ZERO_EXIT_CODE_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "STRING_ZERO_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "STRING_ZERO_REPRESENTATION_TURNED_INTO_DOCTRINE",
    "OK_OUTPUT_TREATED_AS_CROSS_CARRIER_EVIDENCE",
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
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_SOURCE",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_AUTHORITY",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_CURRENTNESS",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_FINAL_COMPLETION",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_RUNTIME",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_CONTINUATION",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_CROSS_CARRIER_EVIDENCE_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_CROSS_CARRIER_EVIDENCE_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_CROSS_CARRIER_EVIDENCE_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_CROSS_CARRIER_EVIDENCE_AUTHORITY",
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
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_CROSS_CARRIER_EVIDENCE_BOUNDARY",
    "ARTIFACTS_MUTATED",
    "RETURNED_CAPTURE_MATERIAL_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_CROSS_CARRIER_EVIDENCE_BOUNDARY_SCOPE",
)

SELECTED_BASIS_FIELDS = (
    "selected_second_carrier_external_result_basis",
    "selected_second_carrier_external_result_terminal_summary_basis",
    "selected_second_carrier_external_result_boundary_basis",
    "selected_second_carrier_external_result_boundary_terminal_summary_basis",
    "selected_second_carrier_verification_basis",
    "selected_second_carrier_verification_terminal_summary_basis",
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

POSTURE_SECTIONS = (
    "cross_carrier_evidence_boundary_only_posture",
    "one_future_cross_carrier_evidence_review_step_posture",
    "second_carrier_external_result_basis_preserved_posture",
    "external_result_artifact_basis_preserved_posture",
    "second_carrier_external_result_boundary_basis_preserved_posture",
    "second_carrier_verification_basis_preserved_posture",
    "returned_second_carrier_capture_basis_preserved_posture",
    "capture_intake_basis_preserved_posture",
    "second_carrier_output_capture_basis_preserved_posture",
    "cross_carrier_evidence_not_created_posture",
    "cross_carrier_evidence_boundary_not_cross_carrier_evidence_posture",
    "external_result_not_cross_carrier_evidence_posture",
    "zero_exit_code_not_cross_carrier_evidence_posture",
    "string_zero_not_cross_carrier_evidence_posture",
    "ok_output_not_cross_carrier_evidence_posture",
    "ran_7_tests_not_cross_carrier_evidence_posture",
    "returned_capture_not_cross_carrier_evidence_posture",
    "portable_verification_closure_not_created_posture",
    "cross_carrier_evidence_not_source_transfer_posture",
    "cross_carrier_evidence_not_source_receipt_posture",
    "cross_carrier_evidence_not_reception_authorization_posture",
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
    "repo_local_availability_not_cross_carrier_evidence_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_external_result_v1_failure_preserved_posture",
    "first_success_boundary_test_failure_preserved_posture",
    "first_result_boundary_resolver_failure_preserved_posture",
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
    "capture_body",
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
    "RAW_CROSS_CARRIER_EVIDENCE_BOUNDARY_BODY_MUST_NOT_RETURN",
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
)

NON_MEANING = (
    "cross-carrier evidence exists",
    "portable verification closure exists",
    "source transfer occurred",
    "source receipt occurred",
    "reception authorization exists",
    "source exists",
    "authority exists",
    "currentness exists",
    "final completion exists",
    "runtime exists",
    "deployment exists",
    "public release exists",
    "continuation authorized",
    "reusable permission exists",
    "follow-on work authorized",
    "cross-carrier evidence boundary became cross-carrier evidence",
    "cross-carrier evidence boundary became portable verification closure",
    "cross-carrier evidence boundary became source transfer/source receipt/reception authorization",
    "cross-carrier evidence boundary became source/authority/currentness",
    "external result became cross-carrier evidence",
    "zero exit code became cross-carrier evidence",
    'string "0" became cross-carrier evidence',
    'string "0" became doctrine',
    "OK became cross-carrier evidence",
    "Ran 7 tests became cross-carrier proof",
    "returned capture became cross-carrier proof",
    "MacBook Pro became authority",
    "MacBook Air became source",
    "artifact existence became cross-carrier-evidence authority",
    "artifact path became currentness",
    "repo-local availability became cross-carrier-evidence authority",
    "hidden repo state became cross-carrier-evidence authority",
    "predecessor external-result v1 resolver/test was repaired/hidden/erased/claimed passed",
    "first success-boundary test was repaired/hidden/erased/claimed passed",
    "first result-boundary resolver was repaired/hidden/erased/claimed passed",
    "v1 packet-emission-boundary resolver was repaired/hidden/erased/claimed passed",
)

WHAT_REMAINS_OPEN = (
    "cross-carrier evidence boundary test",
    "cross-carrier evidence boundary live artifact",
    "cross-carrier evidence boundary terminal summary, if needed",
    "cross-carrier evidence review spec/resolver/test/live artifact, if admitted",
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
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()


def _json_safe(value: Any) -> Any:
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, Mapping):
        return {str(k): _json_safe(v) for k, v in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [_json_safe(v) for v in value]
    return value


def _is_sensitive_key(key: str) -> bool:
    lowered = key.lower()
    return lowered in SENSITIVE_CONTENT_KEYS or lowered.endswith("_body")


def _sanitize(value: Any, key: str | None = None) -> Any:
    if key is not None and _is_sensitive_key(key):
        return REDACTED_RAW_VALUE
    if isinstance(value, Mapping):
        return {str(k): _sanitize(v, str(k)) for k, v in value.items()}
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
        "bounded_to": "cross_carrier_evidence_boundary",
        "creates_cross_carrier_evidence": False,
        "creates_portable_verification_closure": False,
        "creates_source_authority_currentness_runtime_final_completion_or_follow_on": False,
    }


def _selected_basis(
    request: Mapping[str, Any],
    field: str,
    shortcut_prefixes: tuple[str, ...] = (),
) -> dict[str, Any]:
    shortcuts: dict[str, Any] = {}
    for key, value in request.items():
        if any(str(key).startswith(prefix) for prefix in shortcut_prefixes):
            shortcuts[str(key)] = value
    return {
        "basis_field": field,
        "basis_declared": _basis_declared(request, field),
        "selected_basis_reference_shape_preserved": True,
        "basis": _sanitize(_json_safe(copy.deepcopy(request.get(field)))),
        "selected_shortcuts": _sanitize(_json_safe(shortcuts)),
        "raw_full_prior_artifact_body_returned": False,
        "hidden_repo_state_used_as_authority": False,
    }


def _missing_or_flipped_non_claim(request: Mapping[str, Any]) -> str | None:
    declared = request.get("declared_non_claims")
    if not isinstance(declared, Mapping):
        return "declared_non_claims"
    for key in REQUIRED_FALSE_NON_CLAIMS:
        if key not in declared or declared.get(key) is not False:
            return key
    return None


OVERREACH_FLAG_CODES: tuple[tuple[set[str], str], ...] = (
    ({"cross_carrier_evidence_created"}, "CROSS_CARRIER_EVIDENCE_CREATED"),
    ({"portable_verification_closure_created"}, "PORTABLE_VERIFICATION_CLOSURE_CREATED"),
    ({"source_transfer_occurred"}, "SOURCE_TRANSFER_OCCURRED"),
    ({"source_receipt_occurred"}, "SOURCE_RECEIPT_OCCURRED"),
    ({"reception_authorization_created"}, "RECEPTION_AUTHORIZATION_CREATED"),
    ({"source_created"}, "SOURCE_CREATED"),
    ({"authority_created"}, "AUTHORITY_CREATED"),
    ({"currentness_created"}, "CURRENTNESS_CREATED"),
    ({"final_completion_claimed", "final_completion_created"}, "FINAL_COMPLETION_CLAIMED"),
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
        {"cross_carrier_evidence_boundary_treated_as_cross_carrier_evidence"},
        "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    ),
    (
        {"cross_carrier_evidence_boundary_treated_as_portable_verification_closure"},
        "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
    ),
    (
        {"cross_carrier_evidence_boundary_treated_as_source_transfer"},
        "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    ),
    (
        {"cross_carrier_evidence_boundary_treated_as_source_receipt"},
        "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    ),
    (
        {"cross_carrier_evidence_boundary_treated_as_reception_authorization"},
        "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    ),
    (
        {"cross_carrier_evidence_boundary_treated_as_source"},
        "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_SOURCE",
    ),
    (
        {"cross_carrier_evidence_boundary_treated_as_authority"},
        "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_AUTHORITY",
    ),
    (
        {"cross_carrier_evidence_boundary_treated_as_currentness"},
        "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_CURRENTNESS",
    ),
    (
        {"cross_carrier_evidence_boundary_treated_as_final_completion"},
        "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_FINAL_COMPLETION",
    ),
    (
        {"cross_carrier_evidence_boundary_treated_as_runtime"},
        "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_RUNTIME",
    ),
    (
        {"cross_carrier_evidence_boundary_treated_as_continuation"},
        "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_CONTINUATION",
    ),
    (
        {"cross_carrier_evidence_boundary_treated_as_reusable_permission"},
        "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION",
    ),
    (
        {"cross_carrier_evidence_boundary_treated_as_follow_on_work"},
        "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
    ),
    (
        {"second_carrier_external_result_treated_as_cross_carrier_evidence"},
        "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_EXTERNAL_RESULT_AS_CROSS_CARRIER_EVIDENCE",
    ),
    ({"zero_exit_code_treated_as_cross_carrier_evidence"}, "ZERO_EXIT_CODE_TREATED_AS_CROSS_CARRIER_EVIDENCE"),
    ({"string_zero_treated_as_cross_carrier_evidence"}, "STRING_ZERO_TREATED_AS_CROSS_CARRIER_EVIDENCE"),
    (
        {"string_zero_representation_turned_into_doctrine"},
        "STRING_ZERO_REPRESENTATION_TURNED_INTO_DOCTRINE",
    ),
    ({"ok_output_treated_as_cross_carrier_evidence"}, "OK_OUTPUT_TREATED_AS_CROSS_CARRIER_EVIDENCE"),
    ({"ran_7_tests_treated_as_cross_carrier_proof"}, "RAN_7_TESTS_TREATED_AS_CROSS_CARRIER_PROOF"),
    ({"returned_capture_treated_as_cross_carrier_evidence"}, "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_EVIDENCE"),
    ({"receiving_carrier_treated_as_authority"}, "RECEIVING_CARRIER_TREATED_AS_AUTHORITY"),
    (
        {"artifact_existence_treated_as_cross_carrier_evidence_authority"},
        "ARTIFACT_EXISTENCE_TREATED_AS_CROSS_CARRIER_EVIDENCE_AUTHORITY",
    ),
    ({"artifact_path_treated_as_currentness"}, "ARTIFACT_PATH_TREATED_AS_CURRENTNESS"),
    (
        {"repo_local_availability_treated_as_cross_carrier_evidence_authority"},
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_CROSS_CARRIER_EVIDENCE_AUTHORITY",
    ),
    (
        {"hidden_repo_state_used_as_cross_carrier_evidence_content"},
        "HIDDEN_REPO_STATE_USED_AS_CROSS_CARRIER_EVIDENCE_CONTENT",
    ),
    (
        {"hidden_repo_state_used_as_cross_carrier_evidence_authority"},
        "HIDDEN_REPO_STATE_USED_AS_CROSS_CARRIER_EVIDENCE_AUTHORITY",
    ),
    ({"selected_basis_not_reference_shaped"}, "SELECTED_BASIS_NOT_REFERENCE_SHAPED"),
    ({"raw_full_prior_artifact_body_returned"}, "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED"),
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
        {"command_report_lineage_treated_as_current_report_artifact", "selected_command_report_lineage_treated_as_current_report_artifact"},
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
        {"full_prior_artifact_body_emitted_outside_bounded_cross_carrier_evidence_boundary"},
        "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_CROSS_CARRIER_EVIDENCE_BOUNDARY",
    ),
    ({"prior_artifacts_mutated", "artifacts_mutated"}, "ARTIFACTS_MUTATED"),
    ({"returned_capture_material_mutated"}, "RETURNED_CAPTURE_MATERIAL_MUTATED"),
)


def _evaluate_request(request: Mapping[str, Any]) -> tuple[list[dict[str, Any]], dict[str, Any] | None]:
    checks: list[dict[str, Any]] = []

    question = request.get("cross_carrier_evidence_boundary_question")
    _check(
        checks,
        "cross-carrier evidence boundary question declared",
        isinstance(question, str) and bool(question.strip()),
        "declared bounded cross-carrier evidence boundary question",
        question,
        "CROSS_CARRIER_EVIDENCE_BOUNDARY_QUESTION_UNDECLARED",
    )

    intent = request.get("cross_carrier_evidence_boundary_intent")
    _check(
        checks,
        "cross-carrier evidence boundary intent supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "CROSS_CARRIER_EVIDENCE_BOUNDARY_INTENT_UNSUPPORTED",
    )
    if intent == INTENT_BLOCK:
        _check(
            checks,
            "cross-carrier evidence boundary explicit block intent absent",
            False,
            "not explicitly blocked",
            intent,
            "CROSS_CARRIER_EVIDENCE_BOUNDARY_INTENT_UNSUPPORTED",
        )

    scope = _scope_values(request.get("cross_carrier_evidence_boundary_scope"))
    unsupported_scope = [value for value in scope if value not in SUPPORTED_SCOPE_VALUES]
    _check(
        checks,
        "cross-carrier evidence boundary scope supported",
        not unsupported_scope,
        "only supported cross-carrier evidence boundary scope values",
        unsupported_scope,
        "UNSUPPORTED_CROSS_CARRIER_EVIDENCE_BOUNDARY_SCOPE",
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
        "second-carrier external-result basis declared",
        _basis_declared(request, "selected_second_carrier_external_result_basis"),
        "selected second-carrier external-result basis declared",
        request.get("selected_second_carrier_external_result_basis"),
        "SECOND_CARRIER_EXTERNAL_RESULT_BASIS_MISSING",
    )

    external_result_outcome = _request_value(
        request,
        {"selected_second_carrier_external_result_result_outcome", "external_result_outcome", "outcome"},
    )
    _check(
        checks,
        "second-carrier external-result outcome recorded",
        external_result_outcome == EXPECTED_SECOND_CARRIER_EXTERNAL_RESULT_OUTCOME,
        EXPECTED_SECOND_CARRIER_EXTERNAL_RESULT_OUTCOME,
        external_result_outcome,
        "SECOND_CARRIER_EXTERNAL_RESULT_NOT_RECORDED",
    )

    external_result_version = _request_value(
        request,
        {"selected_second_carrier_external_result_result_version", "external_result_result_version", "result_version"},
    )
    _check(
        checks,
        "second-carrier external-result version 0.1.0",
        external_result_version == RESULT_VERSION,
        RESULT_VERSION,
        external_result_version,
        "SECOND_CARRIER_EXTERNAL_RESULT_VERSION_NOT_0_1_0",
    )

    external_result_failed = _as_int(
        _request_value(
            request,
            {"selected_second_carrier_external_result_failed_check_count", "failed_check_count"},
            0,
        )
    )
    _check(
        checks,
        "second-carrier external-result failed checks zero",
        external_result_failed == 0,
        0,
        external_result_failed,
        "SECOND_CARRIER_EXTERNAL_RESULT_FAILED_CHECKS_PRESENT",
    )

    bounded_external_result = _request_truthy(
        request,
        {
            "selected_second_carrier_external_result_bounded_external_result_recorded",
            "bounded_second_carrier_external_result_recorded",
            "second_carrier_external_result_recorded",
        },
    )
    _check(
        checks,
        "second-carrier external-result recorded bounded external result",
        bounded_external_result,
        True,
        bounded_external_result,
        "SECOND_CARRIER_EXTERNAL_RESULT_DID_NOT_RECORD_BOUNDED_EXTERNAL_RESULT",
    )

    external_result_guard_checks = (
        (
            "second-carrier external result did not already create cross-carrier evidence",
            {
                "selected_second_carrier_external_result_already_created_cross_carrier_evidence",
                "already_created_cross_carrier_evidence",
                "cross_carrier_evidence_created",
            },
            "SECOND_CARRIER_EXTERNAL_RESULT_ALREADY_CREATED_CROSS_CARRIER_EVIDENCE",
        ),
        (
            "second-carrier external result did not already create portable verification closure",
            {
                "selected_second_carrier_external_result_already_created_portable_verification_closure",
                "already_created_portable_verification_closure",
                "portable_verification_closure_created",
            },
            "SECOND_CARRIER_EXTERNAL_RESULT_ALREADY_CREATED_PORTABLE_VERIFICATION_CLOSURE",
        ),
        (
            "second-carrier external result did not treat external result as cross-carrier evidence",
            {
                "selected_second_carrier_external_result_treated_external_result_as_cross_carrier_evidence",
                "treated_external_result_as_cross_carrier_evidence",
                "second_carrier_external_result_treated_as_cross_carrier_evidence",
            },
            "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_EXTERNAL_RESULT_AS_CROSS_CARRIER_EVIDENCE",
        ),
        (
            "second-carrier external result did not treat external result as portable verification closure",
            {
                "selected_second_carrier_external_result_treated_external_result_as_portable_verification_closure",
                "treated_external_result_as_portable_verification_closure",
            },
            "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_EXTERNAL_RESULT_AS_PORTABLE_VERIFICATION_CLOSURE",
        ),
        (
            "second-carrier external result kept zero exit code not cross-carrier evidence",
            {"zero_exit_code_treated_as_cross_carrier_evidence"},
            "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_ZERO_EXIT_CODE_AS_CROSS_CARRIER_EVIDENCE",
        ),
        (
            "second-carrier external result kept string zero not cross-carrier evidence",
            {"string_zero_treated_as_cross_carrier_evidence"},
            "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_STRING_ZERO_AS_CROSS_CARRIER_EVIDENCE",
        ),
        (
            "second-carrier external result kept string zero not doctrine",
            {"string_zero_representation_turned_into_doctrine"},
            "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_STRING_ZERO_AS_DOCTRINE",
        ),
        (
            "second-carrier external result kept OK not cross-carrier evidence",
            {"ok_output_treated_as_cross_carrier_evidence"},
            "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_OK_AS_CROSS_CARRIER_EVIDENCE",
        ),
        (
            "second-carrier external result kept Ran 7 tests not cross-carrier proof",
            {"ran_7_tests_treated_as_cross_carrier_proof"},
            "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_RAN_7_TESTS_AS_CROSS_CARRIER_PROOF",
        ),
        (
            "second-carrier external result kept returned capture not cross-carrier proof",
            {"returned_capture_treated_as_cross_carrier_evidence"},
            "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_RETURNED_CAPTURE_AS_CROSS_CARRIER_PROOF",
        ),
        (
            "second-carrier external result kept official enum scope strings unredacted",
            {"selected_second_carrier_external_result_official_enum_scope_strings_redacted"},
            "SECOND_CARRIER_EXTERNAL_RESULT_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
        ),
    )
    for check_name, keys, code in external_result_guard_checks:
        actual = _request_truthy(request, keys)
        _check(checks, check_name, not actual, False, actual, code)

    external_result_preservation_checks = (
        (
            "second-carrier external result preserved zero exit code as not cross-carrier evidence",
            {"selected_second_carrier_external_result_zero_exit_code_not_cross_carrier_evidence"},
            "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_ZERO_EXIT_CODE_AS_CROSS_CARRIER_EVIDENCE",
        ),
        (
            "second-carrier external result preserved string zero as not cross-carrier evidence",
            {"selected_second_carrier_external_result_string_zero_not_cross_carrier_evidence"},
            "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_STRING_ZERO_AS_CROSS_CARRIER_EVIDENCE",
        ),
        (
            "second-carrier external result preserved OK as not cross-carrier evidence",
            {"selected_second_carrier_external_result_ok_not_cross_carrier_evidence"},
            "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_OK_AS_CROSS_CARRIER_EVIDENCE",
        ),
        (
            "second-carrier external result preserved Ran 7 tests as not cross-carrier evidence",
            {"selected_second_carrier_external_result_ran_7_tests_not_cross_carrier_evidence"},
            "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_RAN_7_TESTS_AS_CROSS_CARRIER_PROOF",
        ),
        (
            "second-carrier external result preserved returned capture as not cross-carrier evidence",
            {"selected_second_carrier_external_result_returned_capture_not_cross_carrier_evidence"},
            "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_RETURNED_CAPTURE_AS_CROSS_CARRIER_PROOF",
        ),
        (
            "selected basis reference shape preserved",
            {"reference_shaped_input_posture"},
            "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
        ),
    )
    for check_name, keys, code in external_result_preservation_checks:
        actual = _request_truthy(request, keys)
        _check(checks, check_name, actual, True, actual, code)

    predecessor_preserved = _request_truthy(
        request,
        {
            "selected_second_carrier_external_result_predecessor_v1_failure_preserved",
            "predecessor_external_result_v1_failure_preserved",
        },
    )
    _check(
        checks,
        "predecessor external-result v1 failure preserved",
        predecessor_preserved,
        True,
        predecessor_preserved,
        "PREDECESSOR_EXTERNAL_RESULT_V1_FAILURE_MISSING_OR_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
    )

    basis_checks = (
        (
            "selected_second_carrier_external_result_boundary_basis",
            "second-carrier external-result boundary basis declared",
            "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_BASIS_MISSING",
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
    for field, check_name, code in basis_checks:
        _check(checks, check_name, _basis_declared(request, field), "declared", request.get(field), code)

    outcome_checks = (
        (
            "second-carrier external-result boundary outcome recorded",
            {"selected_second_carrier_external_result_boundary_result_outcome"},
            EXPECTED_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_OUTCOME,
            "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_BASIS_MISSING",
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
            "second-carrier external-result boundary failed checks zero",
            {"selected_second_carrier_external_result_boundary_failed_check_count"},
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
        "declared string zero representation not turned into doctrine",
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

    posture_checks = (
        "cross_carrier_evidence_boundary_only_posture",
        "one_future_cross_carrier_evidence_review_step_posture",
        "second_carrier_external_result_basis_preserved_posture",
        "external_result_artifact_basis_preserved_posture",
        "cross_carrier_evidence_not_created_posture",
        "cross_carrier_evidence_boundary_not_cross_carrier_evidence_posture",
        "external_result_not_cross_carrier_evidence_posture",
        "zero_exit_code_not_cross_carrier_evidence_posture",
        "string_zero_not_cross_carrier_evidence_posture",
        "ok_output_not_cross_carrier_evidence_posture",
        "ran_7_tests_not_cross_carrier_evidence_posture",
        "returned_capture_not_cross_carrier_evidence_posture",
        "portable_verification_closure_not_created_posture",
        "cross_carrier_evidence_not_source_transfer_posture",
        "cross_carrier_evidence_not_source_receipt_posture",
        "cross_carrier_evidence_not_reception_authorization_posture",
        "source_not_created_posture",
        "authority_not_created_posture",
        "currentness_not_created_posture",
        "final_completion_not_created_posture",
        "runtime_not_created_posture",
        "follow_on_work_not_authorized_posture",
        "hidden_repo_state_excluded_posture",
        "repo_local_availability_not_cross_carrier_evidence_authority_posture",
        "selected_basis_reference_shape_posture",
        "raw_full_prior_artifact_body_not_returned_posture",
        "official_enum_scope_strings_not_redacted_posture",
        "hostile_raw_body_content_contained_posture",
    )
    for field in posture_checks:
        _check(checks, f"{field} declared", _posture_declared(request, field), "declared", request.get(field), "NON_CLAIM_MISSING_OR_FLIPPED")

    for keys, code in OVERREACH_FLAG_CODES:
        actual = _request_truthy(request, keys)
        _check(checks, f"{code} not present", not actual, False, actual, code)

    return checks, _first_failure(checks)


def _result_id(request: Mapping[str, Any]) -> str:
    value = request.get("cross_carrier_evidence_boundary_request_id")
    if isinstance(value, str) and value.strip():
        return value.strip()
    return "portable_source_body_verification_cross_carrier_evidence_boundary_request_001"


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

    result: dict[str, Any] = {
        "portable_source_body_verification_cross_carrier_evidence_boundary_metadata": {
            "portable_source_body_verification_cross_carrier_evidence_boundary_result_id": request_id,
            "portable_source_body_verification_cross_carrier_evidence_boundary_result_type": RESULT_TYPE,
            "portable_source_body_verification_cross_carrier_evidence_boundary_result_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_cross_carrier_evidence_boundary_question": {
            "request_id": request_id,
            "question": request.get("cross_carrier_evidence_boundary_question"),
            "intent": request.get("cross_carrier_evidence_boundary_intent"),
            "core_question": CORE_QUESTION,
        },
    }

    for field in SELECTED_BASIS_FIELDS:
        result[field] = _selected_basis(request, field, (field.replace("_basis", ""),))

    for field in POSTURE_SECTIONS:
        result[field] = _posture(field, recorded)

    result["cross_carrier_evidence_boundary_scope"] = _scope_values(
        request.get("cross_carrier_evidence_boundary_scope")
    )
    result["cross_carrier_evidence_boundary_checks"] = checks
    result["cross_carrier_evidence_boundary_statement"] = statement
    result["cross_carrier_evidence_boundary_non_meaning"] = {
        "preserved_non_meanings": list(NON_MEANING),
        "does_not_create_cross_carrier_evidence": True,
        "does_not_create_portable_verification_closure": True,
        "does_not_authorize_follow_on_work": True,
    }
    result["additional_basis_required"] = {
        "required": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "missing_or_unclear_basis": _sanitize(_json_safe(request.get("additional_basis_context", []))),
        "missing_basis_scheduled": False,
        "missing_basis_authorized": False,
        "missing_basis_executed": False,
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
    result["portable_source_body_verification_cross_carrier_evidence_boundary_summary"] = (
        build_portable_source_body_verification_cross_carrier_evidence_boundary_summary(result)
    )
    return result


def _malformed_result(reason: str, code: str) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    _check(checks, reason, False, "mapping request", reason, code)
    block = _first_failure(checks)
    return _build_result({}, OUTCOME_BLOCKED, checks, block)


def resolve_portable_source_body_verification_cross_carrier_evidence_boundary(
    declared_cross_carrier_evidence_boundary_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one bounded cross-carrier evidence boundary posture."""

    if declared_cross_carrier_evidence_boundary_request is None:
        return _malformed_result(
            "declared cross-carrier evidence boundary request missing",
            "DECLARED_CROSS_CARRIER_EVIDENCE_BOUNDARY_REQUEST_MALFORMED",
        )
    if not isinstance(declared_cross_carrier_evidence_boundary_request, Mapping):
        return _malformed_result(
            "declared cross-carrier evidence boundary request malformed",
            "DECLARED_CROSS_CARRIER_EVIDENCE_BOUNDARY_REQUEST_MALFORMED",
        )

    request = copy.deepcopy(dict(declared_cross_carrier_evidence_boundary_request))
    checks, block = _evaluate_request(request)
    requested_outcome = request.get("requested_cross_carrier_evidence_boundary_outcome")

    if block is not None:
        outcome = OUTCOME_BLOCKED
    elif request.get("cross_carrier_evidence_boundary_intent") == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_RECORDED
    elif requested_outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
    elif requested_outcome == OUTCOME_NOT_RECORDED:
        outcome = OUTCOME_NOT_RECORDED
    else:
        outcome = OUTCOME_RECORDED

    return _build_result(request, outcome, checks, block)


def resolve_portable_source_body_verification_cross_carrier_evidence_boundary_from_path(
    declared_cross_carrier_evidence_boundary_request_path: Path | str,
) -> dict:
    """Load a JSON object request from path and resolve it."""

    path = Path(declared_cross_carrier_evidence_boundary_request_path)
    try:
        raw_text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise PortableSourceBodyVerificationCrossCarrierEvidenceBoundaryError(
            f"declared cross-carrier evidence boundary request unreadable: {path}"
        ) from exc
    try:
        loaded = json.loads(raw_text)
    except json.JSONDecodeError as exc:
        raise PortableSourceBodyVerificationCrossCarrierEvidenceBoundaryError(
            f"declared cross-carrier evidence boundary request malformed JSON: {path}"
        ) from exc
    if not isinstance(loaded, Mapping):
        raise PortableSourceBodyVerificationCrossCarrierEvidenceBoundaryError(
            "declared cross-carrier evidence boundary request path must contain a JSON object"
        )
    return resolve_portable_source_body_verification_cross_carrier_evidence_boundary(loaded)


def build_portable_source_body_verification_cross_carrier_evidence_boundary_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a compact JSON-safe summary from a boundary result."""

    metadata = result.get("portable_source_body_verification_cross_carrier_evidence_boundary_metadata", {})
    declared = result.get("declared_cross_carrier_evidence_boundary_question", {})
    checks = result.get("cross_carrier_evidence_boundary_checks", [])
    statement = result.get("cross_carrier_evidence_boundary_statement", {})
    non_claims = result.get("non_claims", {})
    block = result.get("block")

    failed_count = sum(1 for check in checks if not check.get("passed", False))
    passed_count = sum(1 for check in checks if check.get("passed", False))

    summary = {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") if isinstance(block, Mapping) else None,
        "block_reason": block.get("block_reason") if isinstance(block, Mapping) else None,
        "request_id": metadata.get("portable_source_body_verification_cross_carrier_evidence_boundary_result_id"),
        "question": declared.get("question"),
        "intent": declared.get("intent"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": metadata.get(
            "portable_source_body_verification_cross_carrier_evidence_boundary_result_version",
            RESULT_VERSION,
        ),
        "resolver_module": metadata.get("resolver_module", RESOLVER_MODULE),
        "selected_second_carrier_external_result_outcome": _selected_summary_value(
            result, "selected_second_carrier_external_result_basis", "selected_second_carrier_external_result_result_outcome"
        ),
        "selected_second_carrier_external_result_version": _selected_summary_value(
            result, "selected_second_carrier_external_result_basis", "selected_second_carrier_external_result_result_version"
        ),
        "selected_second_carrier_external_result_failed_check_count": _selected_summary_value(
            result, "selected_second_carrier_external_result_basis", "selected_second_carrier_external_result_failed_check_count"
        ),
        "selected_returned_capture_intake_path": _selected_summary_value(
            result, "selected_returned_second_carrier_live_capture_intake_basis", "selected_returned_capture_intake_path"
        ),
        "selected_returned_capture_zip_path": _selected_summary_value(
            result, "selected_returned_capture_material_basis", "selected_returned_capture_zip_path"
        ),
        "selected_returned_capture_hash_path": _selected_summary_value(
            result, "selected_returned_capture_material_basis", "selected_returned_capture_hash_path"
        ),
        "selected_returned_capture_extracted_directory_path": _selected_summary_value(
            result, "selected_returned_capture_material_basis", "selected_returned_capture_extracted_directory_path"
        ),
        "selected_returned_capture_exit_code": _selected_summary_value(
            result, "selected_returned_capture_material_basis", "selected_returned_capture_exit_code"
        ),
        "selected_returned_capture_declared_exit_code": _selected_summary_value(
            result, "selected_returned_capture_material_basis", "selected_returned_capture_declared_exit_code"
        ),
        "selected_returned_capture_ok_line": _selected_summary_value(
            result, "selected_returned_capture_material_basis", "selected_returned_capture_ok_line"
        ),
        "no_cross_carrier_evidence": non_claims.get("cross_carrier_evidence_created") is False,
        "no_portable_verification_closure": non_claims.get("portable_verification_closure_created") is False,
        "no_source_authority_currentness_final_completion_runtime": (
            non_claims.get("source_created") is False
            and non_claims.get("authority_created") is False
            and non_claims.get("currentness_created") is False
            and non_claims.get("final_completion_claimed") is False
            and non_claims.get("runtime_hosting_created") is False
        ),
        "no_deployment_public_release_follow_on": (
            non_claims.get("deployment_created") is False
            and non_claims.get("public_release_created") is False
            and non_claims.get("follow_on_work_authorized") is False
        ),
        "key_non_claims": {
            key: non_claims.get(key)
            for key in (
                "cross_carrier_evidence_created",
                "portable_verification_closure_created",
                "string_zero_representation_turned_into_doctrine",
                "returned_capture_treated_as_cross_carrier_evidence",
                "authorization_token_reused",
                "consumed_request_reopened",
            )
        },
        "predecessor_external_result_v1_failure_preserved": statement.get(
            "predecessor_external_result_v1_failure_preserved", False
        ),
        "first_success_boundary_test_preserved_as_failed_predecessor": statement.get(
            "first_success_boundary_test_failure_preserved", False
        ),
        "v1_packet_emission_predecessor_failure_preserved": (
            non_claims.get("v1_packet_emission_repaired") is False
            and non_claims.get("v1_packet_emission_hidden") is False
            and non_claims.get("v1_packet_emission_claimed_passed") is False
        ),
        "first_result_boundary_resolver_preserved_as_failed_predecessor": statement.get(
            "first_result_boundary_resolver_failure_preserved", False
        ),
    }
    for key in ALLOWED_TRUE_RECORDED_FIELDS:
        summary[key] = bool(statement.get(key, False))
    return _sanitize(_json_safe(summary))


def _selected_summary_value(result: Mapping[str, Any], section: str, key: str) -> Any:
    selected = result.get(section)
    if not isinstance(selected, Mapping):
        return None
    shortcuts = selected.get("selected_shortcuts")
    if isinstance(shortcuts, Mapping) and key in shortcuts:
        return shortcuts[key]
    basis = selected.get("basis")
    if isinstance(basis, Mapping):
        found = _find_key(basis, {key})
        if found is not None:
            return found
    return None


def write_portable_source_body_verification_cross_carrier_evidence_boundary_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a result JSON without silently overwriting an existing file."""

    metadata = result.get("portable_source_body_verification_cross_carrier_evidence_boundary_metadata", {})
    request_id = metadata.get(
        "portable_source_body_verification_cross_carrier_evidence_boundary_result_id",
        "portable_source_body_verification_cross_carrier_evidence_boundary_request_001",
    )
    filename = f"{request_id}__portable_source_body_verification_cross_carrier_evidence_boundary_result.json"
    path = Path(output_path) if output_path is not None else OUTPUT_ROOT / filename
    path.parent.mkdir(parents=True, exist_ok=True)

    candidate = path
    if candidate.exists():
        stem = path.stem
        suffix = path.suffix
        counter = 1
        while candidate.exists():
            candidate = path.with_name(f"{stem}_{counter:03d}{suffix}")
            counter += 1

    candidate.write_text(
        json.dumps(_sanitize(_json_safe(result)), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return candidate


def build_declared_portable_source_body_verification_cross_carrier_evidence_boundary_request(
    **overrides: Any,
) -> dict:
    """Build a valid declared request that records cleanly by default."""

    request: dict[str, Any] = {
        "cross_carrier_evidence_boundary_request_id": (
            "portable_source_body_verification_cross_carrier_evidence_boundary_reference_review_001"
        ),
        "cross_carrier_evidence_boundary_question": CORE_QUESTION,
        "cross_carrier_evidence_boundary_intent": INTENT_RECORD,
        "selected_second_carrier_external_result_basis": {
            "basis_id": "second_carrier_external_result_v2_result",
            "outcome": EXPECTED_SECOND_CARRIER_EXTERNAL_RESULT_OUTCOME,
            "result_version": RESULT_VERSION,
            "failed_check_count": 0,
            "bounded_second_carrier_external_result_recorded": True,
            "external_result_not_cross_carrier_evidence": True,
            "portable_verification_closure_not_created": True,
            "predecessor_external_result_v1_failure_preserved": True,
        },
        "selected_second_carrier_external_result_terminal_summary_basis": {
            "path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT_TERMINAL_SUMMARY_V0.md",
            "terminal_summary_preserved": True,
        },
        "selected_second_carrier_external_result_boundary_basis": {
            "outcome": EXPECTED_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_OUTCOME,
            "failed_check_count": 0,
        },
        "selected_second_carrier_external_result_boundary_terminal_summary_basis": {
            "path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TERMINAL_SUMMARY_V0.md",
        },
        "selected_second_carrier_verification_basis": {
            "outcome": EXPECTED_SECOND_CARRIER_VERIFICATION_OUTCOME,
            "failed_check_count": 0,
        },
        "selected_second_carrier_verification_terminal_summary_basis": {
            "path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_VERIFICATION_TERMINAL_SUMMARY_V0.md",
        },
        "selected_second_carrier_success_basis": {
            "outcome": EXPECTED_SECOND_CARRIER_SUCCESS_OUTCOME,
            "failed_check_count": 0,
        },
        "selected_second_carrier_result_basis": {
            "outcome": EXPECTED_SECOND_CARRIER_RESULT_OUTCOME,
            "failed_check_count": 0,
        },
        "selected_returned_second_carrier_live_capture_intake_basis": {
            "path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_RETURNED_SECOND_CARRIER_LIVE_CAPTURE_INTAKE_V0.md",
            "preserved": True,
            "capture_only": True,
        },
        "selected_returned_capture_material_basis": {
            "from": "MacBook Pro",
            "to": "MacBook Air",
            "exit_code": "0",
            "declared_exit_code": "0",
            "ran_7_tests_line": "Ran 7 tests in 0.451s",
            "ok_line": "OK",
            "placeholder_fields_unrepaired": True,
        },
        "selected_second_carrier_output_capture_basis": {
            "outcome": EXPECTED_SECOND_CARRIER_OUTPUT_CAPTURE_OUTCOME,
            "failed_check_count": 0,
        },
        "selected_packet_transfer_basis": {"basis_declared": True},
        "selected_packet_emission_basis": {"basis_declared": True},
        "selected_command_success_basis": {"basis_declared": True},
        "selected_command_result_v2_basis": {"basis_declared": True},
        "selected_output_capture_v2_basis": {"basis_declared": True},
        "selected_command_output_report_artifact_basis": {"basis_declared": True},
        "selected_command_execution_basis": {"basis_declared": True},
        "selected_command_report_lineage_basis": {
            "lineage_basis_declared": True,
            "command_report_lineage_not_current_report_artifact": True,
            "command_report_lineage_not_source": True,
            "command_report_lineage_not_authority": True,
            "command_report_lineage_not_currentness": True,
        },
        "selected_predecessor_failure_basis": {
            "predecessor_external_result_v1_failure_preserved": True,
            "first_success_boundary_test_failure_preserved": True,
            "first_result_boundary_resolver_failure_preserved": True,
            "v1_packet_emission_failure_preserved": True,
        },
        "selected_evidence_manifest_basis": {"basis_declared": True},
        "selected_artifact_containment_basis": {"basis_declared": True},
        "selected_portable_verification_basis": {"basis_declared": True},
        "selected_second_carrier_external_result_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_"
            "second_carrier_external_result/portable_source_body_verification_second_carrier_"
            "external_result_reference_review_001__portable_source_body_verification_second_"
            "carrier_external_result_result.json"
        ),
        "selected_second_carrier_external_result_result_outcome": EXPECTED_SECOND_CARRIER_EXTERNAL_RESULT_OUTCOME,
        "selected_second_carrier_external_result_result_version": RESULT_VERSION,
        "selected_second_carrier_external_result_failed_check_count": 0,
        "selected_second_carrier_external_result_bounded_external_result_recorded": True,
        "selected_second_carrier_external_result_already_created_cross_carrier_evidence": False,
        "selected_second_carrier_external_result_already_created_portable_verification_closure": False,
        "selected_second_carrier_external_result_treated_external_result_as_cross_carrier_evidence": False,
        "selected_second_carrier_external_result_treated_external_result_as_portable_verification_closure": False,
        "selected_second_carrier_external_result_zero_exit_code_not_cross_carrier_evidence": True,
        "selected_second_carrier_external_result_string_zero_not_cross_carrier_evidence": True,
        "selected_second_carrier_external_result_ok_not_cross_carrier_evidence": True,
        "selected_second_carrier_external_result_ran_7_tests_not_cross_carrier_evidence": True,
        "selected_second_carrier_external_result_returned_capture_not_cross_carrier_evidence": True,
        "selected_second_carrier_external_result_official_enum_scope_strings_redacted": False,
        "selected_second_carrier_external_result_predecessor_v1_failure_preserved": True,
        "selected_second_carrier_external_result_boundary_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_"
            "second_carrier_external_result_boundary/portable_source_body_verification_second_"
            "carrier_external_result_boundary_reference_review_001__portable_source_body_"
            "verification_second_carrier_external_result_boundary_result.json"
        ),
        "selected_second_carrier_external_result_boundary_result_outcome": (
            EXPECTED_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_OUTCOME
        ),
        "selected_second_carrier_external_result_boundary_failed_check_count": 0,
        "selected_second_carrier_verification_result_path": "artifacts/.../second_carrier_verification_result.json",
        "selected_second_carrier_verification_result_outcome": EXPECTED_SECOND_CARRIER_VERIFICATION_OUTCOME,
        "selected_second_carrier_verification_failed_check_count": 0,
        "selected_second_carrier_success_result_path": "artifacts/.../second_carrier_success_result.json",
        "selected_second_carrier_success_result_outcome": EXPECTED_SECOND_CARRIER_SUCCESS_OUTCOME,
        "selected_second_carrier_success_failed_check_count": 0,
        "selected_second_carrier_result_result_path": "artifacts/.../second_carrier_result_result.json",
        "selected_second_carrier_result_result_outcome": EXPECTED_SECOND_CARRIER_RESULT_OUTCOME,
        "selected_second_carrier_result_failed_check_count": 0,
        "selected_returned_capture_intake_path": (
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_RETURNED_SECOND_CARRIER_LIVE_CAPTURE_INTAKE_V0.md"
        ),
        "selected_returned_capture_intake_preserved": True,
        "selected_returned_capture_intake_capture_only": True,
        "selected_returned_capture_from_macbook_pro_to_macbook_air": True,
        "selected_returned_capture_zip_path": (
            "artifacts/actual_second_carrier_live_capture/portable_source_body_verification_"
            "actual_second_carrier_capture_001/original_zip/iammai_second_carrier_capture_001.zip"
        ),
        "selected_returned_capture_hash_path": (
            "artifacts/actual_second_carrier_live_capture/portable_source_body_verification_"
            "actual_second_carrier_capture_001/hashes/iammai_second_carrier_capture_001.sha256"
        ),
        "selected_returned_capture_extracted_directory_path": (
            "artifacts/actual_second_carrier_live_capture/portable_source_body_verification_"
            "actual_second_carrier_capture_001/extracted/iammai_second_carrier_capture_001"
        ),
        "selected_returned_capture_combined_terminal_log_path": "combined_terminal_log.txt",
        "selected_returned_capture_stdout_path": "stdout.txt",
        "selected_returned_capture_stderr_path": "stderr.txt",
        "selected_returned_capture_command_text": "python -m unittest ...",
        "selected_returned_capture_working_directory": "/Users/markomarkota/IAMMAI-SYSTEM",
        "selected_returned_capture_started_at": "preserved-run-started-at",
        "selected_returned_capture_completed_at": "preserved-run-completed-at",
        "selected_returned_capture_exit_code": "0",
        "selected_returned_capture_declared_exit_code": "0",
        "selected_returned_capture_ran_7_tests_line": "Ran 7 tests in 0.451s",
        "selected_returned_capture_ok_line": "OK",
        "selected_returned_capture_raw_placeholder_carrier_label": "raw-placeholder-carrier-label",
        "selected_returned_capture_raw_placeholder_carrier_type": "raw-placeholder-carrier-type",
        "selected_returned_capture_placeholder_fields_unrepaired": True,
        "selected_second_carrier_output_capture_result_path": "artifacts/.../second_carrier_output_capture_result.json",
        "selected_second_carrier_output_capture_result_outcome": EXPECTED_SECOND_CARRIER_OUTPUT_CAPTURE_OUTCOME,
        "selected_second_carrier_output_capture_failed_check_count": 0,
        "predecessor_external_result_v1_failure_preserved": True,
        "reference_shaped_input_posture": True,
        "additional_basis_context": [],
        "not_recorded_basis": [],
        "block_reason": None,
        "requested_cross_carrier_evidence_boundary_outcome": OUTCOME_RECORDED,
        "cross_carrier_evidence_boundary_scope": list(SUPPORTED_SCOPE_VALUES),
        "declared_non_claims": _non_claims(),
    }

    for posture in POSTURE_SECTIONS:
        request[posture] = {"declared": True, "posture": posture}

    request.update(overrides)
    if "declared_non_claims" not in overrides:
        request["declared_non_claims"] = _non_claims()
    return request
