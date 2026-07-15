"""Resolve portable source-body verification second-carrier execution output boundary.

This resolver records one bounded membrane only: whether recorded second-carrier
execution basis may be preserved for one future execution-output /
second-carrier-output step.  It does not create output, an output artifact,
output capture, result, success, external result, cross-carrier evidence,
source transfer, source receipt, reception authorization, source, authority,
currentness, runtime, final completion, continuation, reusable permission, or
follow-on work.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class PortableSourceBodyVerificationSecondCarrierExecutionOutputBoundaryError(Exception):
    """Bounded resolver error for unreadable paths and impossible shapes."""


RESOLVER_MODULE = (
    "resolve_portable_source_body_verification_second_carrier_execution_output_boundary"
)
RESULT_TYPE = (
    "portable_source_body_verification_second_carrier_execution_output_boundary_result"
)
RESULT_VERSION = "0.1.0"
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_portable_source_body_verification_"
    "second_carrier_execution_output_boundary"
)

CORE_QUESTION = (
    "Can the recorded second-carrier execution basis be bounded for one future "
    "execution-output / second-carrier-output step without creating output yet, "
    "creating second-carrier output capture, creating second-carrier result, "
    "creating second-carrier success, creating external result, creating "
    "cross-carrier evidence, creating source transfer, creating source receipt, "
    "creating reception authorization, creating source, authority, currentness, "
    "runtime, final completion, continuation, reusable permission, derivative "
    "reception, vessel relation, another reception request, or follow-on work?"
)

OUTCOME_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_"
    "NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_"
    "REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_BLOCKED"
)
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = (
    "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY"
)
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_"
    "OUTPUT_BOUNDARY"
)
INTENT_BLOCK = (
    "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY"
)
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

SUPPORTED_SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_SCOPE = (
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_ONLY",
    "ONE_FUTURE_SECOND_CARRIER_EXECUTION_OUTPUT_STEP_ONLY",
    "SECOND_CARRIER_EXECUTION_BASIS_PRESERVED",
    "EXECUTION_ARTIFACT_BASIS_PRESERVED",
    "EXECUTION_NOT_OUTPUT",
    "OUTPUT_NOT_CREATED",
    "OUTPUT_ARTIFACT_NOT_CREATED",
    "OUTPUT_CAPTURE_NOT_CREATED",
    "SECOND_CARRIER_RESULT_NOT_CREATED",
    "SECOND_CARRIER_SUCCESS_NOT_CREATED",
    "EXTERNAL_RESULT_NOT_CREATED",
    "CROSS_CARRIER_EVIDENCE_NOT_CREATED",
    "OUTPUT_NOT_SOURCE_TRANSFER",
    "OUTPUT_NOT_SOURCE_RECEIPT",
    "OUTPUT_NOT_RECEPTION_AUTHORIZATION",
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
    "NO_OUTPUT_INFERENCE",
    "NO_CAPTURE_INFERENCE",
    "NO_RESULT_INFERENCE",
    "NO_SUCCESS_INFERENCE",
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
    "HIDDEN_REPO_STATE_NOT_USED_AS_OUTPUT_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_NOT_OUTPUT_AUTHORITY",
    "SELECTED_BASIS_REFERENCE_SHAPE_PRESERVED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "AUTHORIZATION_TOKEN_REUSE_BLOCKED",
    "CONSUMED_REQUEST_TOKEN_REMAINS_CLOSED",
    "CONSUMED_REQUEST_NOT_REOPENED",
    "COMMAND_REPORT_LINEAGE_NOT_CURRENT_REPORT_ARTIFACT",
    "COMMAND_REPORT_LINEAGE_NOT_SOURCE",
    "COMMAND_REPORT_LINEAGE_NOT_AUTHORITY",
    "COMMAND_REPORT_LINEAGE_NOT_CURRENTNESS",
    "RETURNED_RESULT_CONTAINMENT_PRESERVED",
)

SELECTED_BASIS_KEYS = (
    "selected_second_carrier_execution_basis",
    "selected_second_carrier_execution_terminal_summary_basis",
    "selected_second_carrier_execution_boundary_basis",
    "selected_second_carrier_receipt_basis",
    "selected_second_carrier_receipt_boundary_basis",
    "selected_packet_transfer_basis",
    "selected_packet_transfer_boundary_basis",
    "selected_packet_emission_basis",
    "selected_packet_emission_boundary_v2_basis",
    "selected_packet_emission_boundary_v1_predecessor_failure_basis",
    "selected_packet_artifact_basis",
    "selected_packet_boundary_basis",
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
    "second_carrier_execution_output_boundary_only_posture",
    "one_future_second_carrier_execution_output_step_posture",
    "second_carrier_execution_basis_preserved_posture",
    "execution_artifact_basis_preserved_posture",
    "execution_not_output_posture",
    "output_not_created_posture",
    "output_artifact_not_created_posture",
    "output_capture_not_created_posture",
    "second_carrier_result_not_created_posture",
    "second_carrier_success_not_created_posture",
    "external_result_not_created_posture",
    "cross_carrier_evidence_not_created_posture",
    "output_not_source_transfer_posture",
    "output_not_source_receipt_posture",
    "output_not_reception_authorization_posture",
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
    "repo_local_availability_not_output_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
)

POSTURE_TO_STATEMENT = {
    "second_carrier_execution_output_boundary_only_posture": (
        "second_carrier_execution_output_boundary_recorded"
    ),
    "one_future_second_carrier_execution_output_step_posture": (
        "one_future_second_carrier_execution_output_step_declared"
    ),
    "second_carrier_execution_basis_preserved_posture": (
        "second_carrier_execution_basis_preserved"
    ),
    "execution_artifact_basis_preserved_posture": (
        "execution_artifact_basis_preserved"
    ),
    "execution_not_output_posture": "execution_not_output",
    "output_not_created_posture": "output_not_created",
    "output_artifact_not_created_posture": "output_artifact_not_created",
    "output_capture_not_created_posture": "output_capture_not_created",
    "second_carrier_result_not_created_posture": (
        "second_carrier_result_not_created"
    ),
    "second_carrier_success_not_created_posture": (
        "second_carrier_success_not_created"
    ),
    "external_result_not_created_posture": "external_result_not_created",
    "cross_carrier_evidence_not_created_posture": (
        "cross_carrier_evidence_not_created"
    ),
    "output_not_source_transfer_posture": "output_not_source_transfer",
    "output_not_source_receipt_posture": "output_not_source_receipt",
    "output_not_reception_authorization_posture": (
        "output_not_reception_authorization"
    ),
    "receiving_carrier_not_authority_posture": "receiving_carrier_not_authority",
    "source_not_created_posture": "source_not_created",
    "authority_not_created_posture": "authority_not_created",
    "currentness_not_created_posture": "currentness_not_created",
    "final_completion_not_created_posture": "final_completion_not_created",
    "runtime_not_created_posture": "runtime_not_created",
    "continuation_not_authorized_posture": "continuation_not_authorized",
    "reusable_permission_not_created_posture": "reusable_permission_not_created",
    "follow_on_work_not_authorized_posture": "follow_on_work_not_authorized",
    "hidden_repo_state_excluded_posture": "hidden_repo_state_excluded",
    "repo_local_availability_not_output_authority_posture": (
        "repo_local_availability_not_output_authority"
    ),
    "selected_basis_reference_shape_posture": (
        "selected_basis_reference_shape_preserved"
    ),
    "raw_full_prior_artifact_body_not_returned_posture": (
        "raw_full_prior_artifact_body_not_returned"
    ),
}

ALLOWED_TRUE_RECORDED_FIELDS = (
    "second_carrier_execution_output_boundary_recorded",
    "one_future_second_carrier_execution_output_step_declared",
    "second_carrier_execution_basis_preserved",
    "execution_artifact_basis_preserved",
    "execution_not_output",
    "output_not_created",
    "output_artifact_not_created",
    "output_capture_not_created",
    "second_carrier_result_not_created",
    "second_carrier_success_not_created",
    "external_result_not_created",
    "cross_carrier_evidence_not_created",
    "output_not_source_transfer",
    "output_not_source_receipt",
    "output_not_reception_authorization",
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
    "hidden_repo_state_not_used_as_output_authority",
    "repo_local_availability_not_output_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
)

REQUIRED_FALSE_NON_CLAIMS = (
    "execution_output_created",
    "output_artifact_created",
    "second_carrier_output_capture_created",
    "second_carrier_result_created",
    "second_carrier_success_created",
    "external_result_created",
    "cross_carrier_evidence_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "second_carrier_execution_output_boundary_treated_as_output",
    "second_carrier_execution_output_boundary_treated_as_output_artifact",
    "second_carrier_execution_output_boundary_treated_as_output_capture",
    "second_carrier_execution_output_boundary_treated_as_result",
    "second_carrier_execution_output_boundary_treated_as_success",
    "second_carrier_execution_output_boundary_treated_as_external_result",
    "second_carrier_execution_output_boundary_treated_as_cross_carrier_evidence",
    "second_carrier_execution_output_boundary_treated_as_source_transfer",
    "second_carrier_execution_output_boundary_treated_as_source_receipt",
    "second_carrier_execution_output_boundary_treated_as_reception_authorization",
    "second_carrier_execution_output_boundary_treated_as_source",
    "second_carrier_execution_output_boundary_treated_as_authority",
    "second_carrier_execution_output_boundary_treated_as_currentness",
    "second_carrier_execution_output_boundary_treated_as_final_completion",
    "second_carrier_execution_output_boundary_treated_as_runtime",
    "second_carrier_execution_output_boundary_treated_as_continuation",
    "second_carrier_execution_output_boundary_treated_as_reusable_permission",
    "second_carrier_execution_output_boundary_treated_as_follow_on_work",
    "receiving_carrier_treated_as_authority",
    "artifact_existence_treated_as_output_authority",
    "artifact_path_treated_as_currentness",
    "repo_local_availability_treated_as_output_authority",
    "hidden_repo_state_used_as_output_content",
    "hidden_repo_state_used_as_output_authority",
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
)

BLOCK_CODES = (
    "DECLARED_SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_REQUEST_UNREADABLE",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_BLOCK_REQUESTED",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_QUESTION_UNDECLARED",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_INTENT_UNSUPPORTED",
    "SECOND_CARRIER_EXECUTION_BASIS_MISSING",
    "SECOND_CARRIER_EXECUTION_TERMINAL_SUMMARY_BASIS_MISSING",
    "SECOND_CARRIER_EXECUTION_NOT_RECORDED",
    "SECOND_CARRIER_EXECUTION_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_EXECUTION_VERSION_NOT_0_1_0",
    "SECOND_CARRIER_EXECUTION_DID_NOT_RECORD_BOUNDED_EXECUTION",
    "SECOND_CARRIER_EXECUTION_ALREADY_CREATED_EXECUTION_OUTPUT",
    "SECOND_CARRIER_EXECUTION_ALREADY_CREATED_SECOND_CARRIER_OUTPUT_CAPTURE",
    "SECOND_CARRIER_EXECUTION_ALREADY_CREATED_SECOND_CARRIER_RESULT",
    "SECOND_CARRIER_EXECUTION_ALREADY_CREATED_SECOND_CARRIER_SUCCESS",
    "SECOND_CARRIER_EXECUTION_CREATED_EXTERNAL_RESULT",
    "SECOND_CARRIER_EXECUTION_CREATED_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXECUTION_TREATED_EXECUTION_AS_OUTPUT",
    "SECOND_CARRIER_EXECUTION_TREATED_EXECUTION_AS_OUTPUT_CAPTURE",
    "SECOND_CARRIER_EXECUTION_TREATED_EXECUTION_AS_RESULT",
    "SECOND_CARRIER_EXECUTION_TREATED_EXECUTION_AS_SUCCESS",
    "SECOND_CARRIER_EXECUTION_TREATED_EXECUTION_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_EXECUTION_TREATED_EXECUTION_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXECUTION_USED_HIDDEN_REPO_STATE_AS_OUTPUT_AUTHORITY",
    "SECOND_CARRIER_EXECUTION_TREATED_REPO_LOCAL_AVAILABILITY_AS_OUTPUT_AUTHORITY",
    "SECOND_CARRIER_EXECUTION_TREATED_RECEIVING_CARRIER_AS_AUTHORITY",
    "SECOND_CARRIER_EXECUTION_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY_OUTSIDE_BOUNDED_EXECUTION",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_BASIS_MISSING",
    "SECOND_CARRIER_RECEIPT_BASIS_MISSING",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_BASIS_MISSING",
    "PACKET_TRANSFER_BASIS_MISSING",
    "PACKET_TRANSFER_BOUNDARY_BASIS_MISSING",
    "PACKET_EMISSION_BASIS_MISSING",
    "PACKET_EMISSION_BOUNDARY_V2_BASIS_MISSING",
    "PACKET_EMISSION_BOUNDARY_V1_PREDECESSOR_FAILURE_BASIS_MISSING",
    "PACKET_ARTIFACT_BASIS_MISSING",
    "PACKET_BOUNDARY_BASIS_MISSING",
    "COMMAND_SUCCESS_BASIS_MISSING",
    "COMMAND_RESULT_V2_BASIS_MISSING",
    "OUTPUT_CAPTURE_V2_BASIS_MISSING",
    "COMMAND_OUTPUT_REPORT_ARTIFACT_BASIS_MISSING",
    "COMMAND_EXECUTION_BASIS_MISSING",
    "COMMAND_REPORT_LINEAGE_BASIS_MISSING",
    "PREDECESSOR_FAILURE_BASIS_MISSING",
    "EVIDENCE_MANIFEST_BASIS_MISSING",
    "ARTIFACT_CONTAINMENT_BASIS_MISSING",
    "PORTABLE_VERIFICATION_BASIS_MISSING",
    "COMMAND_REPORT_LINEAGE_NOT_LINEAGE_ONLY",
    "PREDECESSOR_FAILURE_EVIDENCE_NOT_VISIBLE",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_POSTURE_MISSING",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_OUTPUT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_OUTPUT_ARTIFACT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_OUTPUT_CAPTURE",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_RESULT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_SUCCESS",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_SOURCE",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_AUTHORITY",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_CURRENTNESS",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_FINAL_COMPLETION",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_RUNTIME",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_CONTINUATION",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
    "EXECUTION_OUTPUT_CREATED",
    "OUTPUT_ARTIFACT_CREATED",
    "SECOND_CARRIER_OUTPUT_CAPTURE_CREATED",
    "SECOND_CARRIER_RESULT_CREATED",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_OUTPUT_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_OUTPUT_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_OUTPUT_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_OUTPUT_AUTHORITY",
    "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENT_REPORT_ARTIFACT",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_SOURCE",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_AUTHORITY",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENTNESS",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_OUTPUT_BOUNDARY",
    "ARTIFACTS_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_SCOPE",
)

NON_CLAIM_BLOCK_CODE_BY_KEY = {
    "execution_output_created": "EXECUTION_OUTPUT_CREATED",
    "output_artifact_created": "OUTPUT_ARTIFACT_CREATED",
    "second_carrier_output_capture_created": "SECOND_CARRIER_OUTPUT_CAPTURE_CREATED",
    "second_carrier_result_created": "SECOND_CARRIER_RESULT_CREATED",
    "second_carrier_success_created": "SECOND_CARRIER_SUCCESS_CREATED",
    "external_result_created": "EXTERNAL_RESULT_CREATED",
    "cross_carrier_evidence_created": "CROSS_CARRIER_EVIDENCE_CREATED",
    "source_transfer_occurred": "SOURCE_TRANSFER_OCCURRED",
    "source_receipt_occurred": "SOURCE_RECEIPT_OCCURRED",
    "reception_authorization_created": "RECEPTION_AUTHORIZATION_CREATED",
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
    "receiving_carrier_treated_as_authority": "RECEIVING_CARRIER_TREATED_AS_AUTHORITY",
    "artifact_existence_treated_as_output_authority": (
        "ARTIFACT_EXISTENCE_TREATED_AS_OUTPUT_AUTHORITY"
    ),
    "artifact_path_treated_as_currentness": "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "repo_local_availability_treated_as_output_authority": (
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_OUTPUT_AUTHORITY"
    ),
    "hidden_repo_state_used_as_output_content": (
        "HIDDEN_REPO_STATE_USED_AS_OUTPUT_CONTENT"
    ),
    "hidden_repo_state_used_as_output_authority": (
        "HIDDEN_REPO_STATE_USED_AS_OUTPUT_AUTHORITY"
    ),
    "raw_full_prior_artifact_body_returned": (
        "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED"
    ),
    "prior_artifacts_mutated": "ARTIFACTS_MUTATED",
    "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
    "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
    "v1_repaired": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "v1_hidden": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "v1_claimed_passed": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
}

for _name in (
    "output",
    "output_artifact",
    "output_capture",
    "result",
    "success",
    "external_result",
    "cross_carrier_evidence",
    "source_transfer",
    "source_receipt",
    "reception_authorization",
    "source",
    "authority",
    "currentness",
    "final_completion",
    "runtime",
    "continuation",
    "reusable_permission",
    "follow_on_work",
):
    NON_CLAIM_BLOCK_CODE_BY_KEY[
        f"second_carrier_execution_output_boundary_treated_as_{_name}"
    ] = f"SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_{_name.upper()}"

EXTRA_FORBIDDEN_FLAG_BLOCK_CODE_BY_KEY = {
    "selected_second_carrier_execution_execution_output_created": (
        "SECOND_CARRIER_EXECUTION_ALREADY_CREATED_EXECUTION_OUTPUT"
    ),
    "selected_second_carrier_execution_created_second_carrier_output_capture": (
        "SECOND_CARRIER_EXECUTION_ALREADY_CREATED_SECOND_CARRIER_OUTPUT_CAPTURE"
    ),
    "selected_second_carrier_execution_created_second_carrier_result": (
        "SECOND_CARRIER_EXECUTION_ALREADY_CREATED_SECOND_CARRIER_RESULT"
    ),
    "selected_second_carrier_execution_created_second_carrier_success": (
        "SECOND_CARRIER_EXECUTION_ALREADY_CREATED_SECOND_CARRIER_SUCCESS"
    ),
    "selected_second_carrier_execution_created_external_result": (
        "SECOND_CARRIER_EXECUTION_CREATED_EXTERNAL_RESULT"
    ),
    "selected_second_carrier_execution_created_cross_carrier_evidence": (
        "SECOND_CARRIER_EXECUTION_CREATED_CROSS_CARRIER_EVIDENCE"
    ),
    "selected_second_carrier_execution_treated_execution_as_output": (
        "SECOND_CARRIER_EXECUTION_TREATED_EXECUTION_AS_OUTPUT"
    ),
    "selected_second_carrier_execution_treated_execution_as_output_capture": (
        "SECOND_CARRIER_EXECUTION_TREATED_EXECUTION_AS_OUTPUT_CAPTURE"
    ),
    "selected_second_carrier_execution_treated_execution_as_result": (
        "SECOND_CARRIER_EXECUTION_TREATED_EXECUTION_AS_RESULT"
    ),
    "selected_second_carrier_execution_treated_execution_as_success": (
        "SECOND_CARRIER_EXECUTION_TREATED_EXECUTION_AS_SUCCESS"
    ),
    "selected_second_carrier_execution_treated_execution_as_external_result": (
        "SECOND_CARRIER_EXECUTION_TREATED_EXECUTION_AS_EXTERNAL_RESULT"
    ),
    "selected_second_carrier_execution_treated_execution_as_cross_carrier_evidence": (
        "SECOND_CARRIER_EXECUTION_TREATED_EXECUTION_AS_CROSS_CARRIER_EVIDENCE"
    ),
    "selected_second_carrier_execution_used_hidden_repo_state_as_output_authority": (
        "SECOND_CARRIER_EXECUTION_USED_HIDDEN_REPO_STATE_AS_OUTPUT_AUTHORITY"
    ),
    "selected_second_carrier_execution_treated_repo_local_availability_as_output_authority": (
        "SECOND_CARRIER_EXECUTION_TREATED_REPO_LOCAL_AVAILABILITY_AS_OUTPUT_AUTHORITY"
    ),
    "selected_second_carrier_execution_treated_receiving_carrier_as_authority": (
        "SECOND_CARRIER_EXECUTION_TREATED_RECEIVING_CARRIER_AS_AUTHORITY"
    ),
    "selected_second_carrier_execution_raw_full_prior_artifact_body_returned_outside_bounded_execution": (
        "SECOND_CARRIER_EXECUTION_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY_OUTSIDE_BOUNDED_EXECUTION"
    ),
    "command_report_lineage_treated_as_current_report_artifact": (
        "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENT_REPORT_ARTIFACT"
    ),
    "command_report_lineage_treated_as_source": (
        "COMMAND_REPORT_LINEAGE_TREATED_AS_SOURCE"
    ),
    "command_report_lineage_treated_as_authority": (
        "COMMAND_REPORT_LINEAGE_TREATED_AS_AUTHORITY"
    ),
    "command_report_lineage_treated_as_currentness": (
        "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENTNESS"
    ),
    "full_prior_artifact_body_emitted_outside_bounded_output_boundary": (
        "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_OUTPUT_BOUNDARY"
    ),
}

BASIS_MISSING_BLOCK_CODE_BY_KEY = {
    "selected_second_carrier_execution_basis": "SECOND_CARRIER_EXECUTION_BASIS_MISSING",
    "selected_second_carrier_execution_terminal_summary_basis": (
        "SECOND_CARRIER_EXECUTION_TERMINAL_SUMMARY_BASIS_MISSING"
    ),
    "selected_second_carrier_execution_boundary_basis": (
        "SECOND_CARRIER_EXECUTION_BOUNDARY_BASIS_MISSING"
    ),
    "selected_second_carrier_receipt_basis": "SECOND_CARRIER_RECEIPT_BASIS_MISSING",
    "selected_second_carrier_receipt_boundary_basis": (
        "SECOND_CARRIER_RECEIPT_BOUNDARY_BASIS_MISSING"
    ),
    "selected_packet_transfer_basis": "PACKET_TRANSFER_BASIS_MISSING",
    "selected_packet_transfer_boundary_basis": "PACKET_TRANSFER_BOUNDARY_BASIS_MISSING",
    "selected_packet_emission_basis": "PACKET_EMISSION_BASIS_MISSING",
    "selected_packet_emission_boundary_v2_basis": (
        "PACKET_EMISSION_BOUNDARY_V2_BASIS_MISSING"
    ),
    "selected_packet_emission_boundary_v1_predecessor_failure_basis": (
        "PACKET_EMISSION_BOUNDARY_V1_PREDECESSOR_FAILURE_BASIS_MISSING"
    ),
    "selected_packet_artifact_basis": "PACKET_ARTIFACT_BASIS_MISSING",
    "selected_packet_boundary_basis": "PACKET_BOUNDARY_BASIS_MISSING",
    "selected_command_success_basis": "COMMAND_SUCCESS_BASIS_MISSING",
    "selected_command_result_v2_basis": "COMMAND_RESULT_V2_BASIS_MISSING",
    "selected_output_capture_v2_basis": "OUTPUT_CAPTURE_V2_BASIS_MISSING",
    "selected_command_output_report_artifact_basis": (
        "COMMAND_OUTPUT_REPORT_ARTIFACT_BASIS_MISSING"
    ),
    "selected_command_execution_basis": "COMMAND_EXECUTION_BASIS_MISSING",
    "selected_command_report_lineage_basis": "COMMAND_REPORT_LINEAGE_BASIS_MISSING",
    "selected_predecessor_failure_basis": "PREDECESSOR_FAILURE_BASIS_MISSING",
    "selected_evidence_manifest_basis": "EVIDENCE_MANIFEST_BASIS_MISSING",
    "selected_artifact_containment_basis": "ARTIFACT_CONTAINMENT_BASIS_MISSING",
    "selected_portable_verification_basis": "PORTABLE_VERIFICATION_BASIS_MISSING",
}

SENSITIVE_BASIS_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_result_body",
    "raw_output_body",
    "execution_body",
    "execution_artifact_body",
    "execution_output_body",
    "output_body",
    "output_artifact_body",
    "second_carrier_output_capture_body",
    "second_carrier_result_body",
    "second_carrier_success_body",
    "external_result_body",
    "cross_carrier_evidence_body",
    "packet_body",
    "source_body",
    "authority_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
    "carrier_possession",
    "copy_presence",
    "receiving_carrier",
    "receipt_artifact_presence",
    "execution_artifact_presence",
    "execution_presence",
    "unlisted_file_dependency",
}
REDACTED_REFERENCE_VALUE = "[bounded-reference-redacted-raw-or-hidden-state]"

WHAT_REMAINS_OPEN_ITEMS = (
    "second-carrier execution output boundary test",
    "second-carrier execution output boundary live artifact",
    "second-carrier execution output boundary terminal summary, if needed",
    "execution output / second-carrier output spec/resolver/test/live artifact",
    "second-carrier output capture",
    "second-carrier result",
    "second-carrier success",
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


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _is_mapping(value: Any) -> bool:
    return isinstance(value, Mapping)


def _is_sequence(value: Any) -> bool:
    return isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray))


def _json_safe(value: Any) -> Any:
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, Mapping):
        return {str(k): _json_safe(v) for k, v in value.items()}
    if isinstance(value, tuple):
        return [_json_safe(v) for v in value]
    if isinstance(value, list):
        return [_json_safe(v) for v in value]
    if isinstance(value, set):
        return sorted(_json_safe(v) for v in value)
    return value


def _sensitive_string(value: str) -> bool:
    upper = value.upper()
    return any(
        marker in upper
        for marker in (
            "MUST_NOT_RETURN",
            "RAW_SECOND_CARRIER_EXECUTION_BODY",
            "RAW_SECOND_CARRIER_OUTPUT_BOUNDARY_BODY",
            "RAW_FULL_PRIOR_ARTIFACT_BODY",
            "HIDDEN_REPO_STATE",
            "CURRENT_WORKING_TREE",
            "LOCAL_CACHE",
            "UNLISTED_FILE_DEPENDENCY",
            "HOSTILE_FULL_BODY",
        )
    )


def _sanitize_reference(value: Any) -> Any:
    if isinstance(value, Mapping):
        sanitized: dict[str, Any] = {}
        for key, item in value.items():
            key_text = str(key)
            if key_text in SENSITIVE_BASIS_KEYS:
                sanitized[key_text] = REDACTED_REFERENCE_VALUE
            else:
                sanitized[key_text] = _sanitize_reference(item)
        return sanitized
    if isinstance(value, list):
        return [_sanitize_reference(item) for item in value]
    if isinstance(value, tuple):
        return [_sanitize_reference(item) for item in value]
    if isinstance(value, str) and _sensitive_string(value):
        return REDACTED_REFERENCE_VALUE
    return _json_safe(value)


def _to_bool(value: Any, default: bool | None = None) -> bool | None:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        lowered = value.strip().lower()
        if lowered == "true":
            return True
        if lowered == "false":
            return False
    return default


def _to_int(value: Any, default: int | None = None) -> int | None:
    if isinstance(value, bool):
        return default
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value.strip())
        except ValueError:
            return default
    return default


def _find_key(value: Any, key_names: set[str], max_depth: int = 8) -> Any:
    if max_depth < 0:
        return None
    if isinstance(value, Mapping):
        for key, item in value.items():
            if str(key) in key_names:
                return item
        for item in value.values():
            found = _find_key(item, key_names, max_depth - 1)
            if found is not None:
                return found
    elif isinstance(value, list):
        for item in value:
            found = _find_key(item, key_names, max_depth - 1)
            if found is not None:
                return found
    return None


def _request_basis(request: Mapping[str, Any], key: str) -> Any:
    return request.get(key)


def _declared(value: Any) -> bool:
    if value is None:
        return False
    if value is False:
        return False
    if value == "":
        return False
    if isinstance(value, Mapping):
        if value.get("declared") is False:
            return False
        if value.get("basis_declared") is False:
            return False
        if value.get("posture_declared") is False:
            return False
        return True
    if _is_sequence(value):
        return len(value) > 0
    return True


def _basis_declared(request: Mapping[str, Any], key: str) -> bool:
    return _declared(_request_basis(request, key))


def _posture_declared(request: Mapping[str, Any], key: str) -> bool:
    value = request.get(key)
    if _to_bool(value, None) is not None:
        return bool(value)
    return _declared(value)


def _extract_value(
    request: Mapping[str, Any],
    top_level_keys: Sequence[str],
    basis_keys: Sequence[str] = (),
) -> Any:
    for key in top_level_keys:
        if key in request:
            return request[key]
    for basis_key in basis_keys:
        basis = _request_basis(request, basis_key)
        if basis is not None:
            found = _find_key(basis, set(top_level_keys))
            if found is not None:
                return found
    return None


def _scope_values(value: Any) -> tuple[str, ...]:
    if value is None:
        return ()
    if isinstance(value, str):
        return (value,)
    if _is_sequence(value):
        return tuple(str(item) for item in value)
    if isinstance(value, Mapping):
        if isinstance(value.get("scope"), str):
            return (value["scope"],)
        if _is_sequence(value.get("scope")):
            return tuple(str(item) for item in value["scope"])
        if _is_sequence(value.get("values")):
            return tuple(str(item) for item in value["values"])
    return (str(value),)


def _check_record(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    block_code: str | None,
) -> dict[str, Any]:
    record: dict[str, Any] = {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": _json_safe(expected_posture),
        "actual_posture": _sanitize_reference(actual_posture),
    }
    if passed:
        record["block_code"] = None
        record["failure_code"] = None
    else:
        record["block_code"] = block_code
        record["failure_code"] = block_code
    return record


def _add_check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    block_code: str,
) -> None:
    checks.append(
        _check_record(
            check_name=check_name,
            passed=passed,
            expected_posture=expected_posture,
            actual_posture=actual_posture,
            block_code=block_code,
        )
    )


def _check_counts(checks: Sequence[Mapping[str, Any]]) -> tuple[int, int]:
    passed = sum(1 for check in checks if check.get("passed") is True)
    failed = sum(1 for check in checks if check.get("passed") is not True)
    return passed, failed


def _block_from_checks(
    checks: Sequence[Mapping[str, Any]], explicit_reason: Any = None
) -> dict[str, Any] | None:
    for check in checks:
        if check.get("passed") is not True:
            code = check.get("block_code") or check.get("failure_code")
            return {
                "blocked": True,
                "block_code": code,
                "reason": str(explicit_reason or check.get("check_name")),
            }
    return None


def _selected_execution_basis(request: Mapping[str, Any]) -> Any:
    return request.get("selected_second_carrier_execution_basis")


def _execution_basis_value(
    request: Mapping[str, Any],
    keys: Sequence[str],
) -> Any:
    return _extract_value(
        request,
        keys,
        basis_keys=("selected_second_carrier_execution_basis",),
    )


def _execution_basis_bool(
    request: Mapping[str, Any],
    false_keys: Sequence[str],
    true_inverse_keys: Sequence[str] = (),
) -> bool | None:
    false_value = _execution_basis_value(request, false_keys)
    false_bool = _to_bool(false_value, None)
    if false_bool is not None:
        return false_bool is False
    true_value = _execution_basis_value(request, true_inverse_keys)
    true_bool = _to_bool(true_value, None)
    if true_bool is not None:
        return true_bool is True
    return None


def _non_claims_from_request(request: Mapping[str, Any]) -> dict[str, bool]:
    declared = request.get("declared_non_claims", {})
    if not isinstance(declared, Mapping):
        declared = {}
    non_claims: dict[str, bool] = {}
    for key in REQUIRED_FALSE_NON_CLAIMS:
        non_claims[key] = bool(_to_bool(declared.get(key), False))
    return non_claims


def _block_code_for_non_claim(key: str) -> str:
    return NON_CLAIM_BLOCK_CODE_BY_KEY.get(key, "NON_CLAIM_MISSING_OR_FLIPPED")


def _build_checks(
    request: Mapping[str, Any],
    malformed_code: str | None = None,
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    if malformed_code is not None:
        _add_check(
            checks,
            "declared second-carrier execution output boundary request is mapping",
            False,
            "mapping JSON object",
            type(request).__name__,
            malformed_code,
        )
        return checks

    question = request.get("second_carrier_execution_output_boundary_question")
    _add_check(
        checks,
        "second-carrier execution output boundary question declared",
        question == CORE_QUESTION,
        CORE_QUESTION,
        question,
        "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_QUESTION_UNDECLARED",
    )

    intent = request.get("second_carrier_execution_output_boundary_intent")
    _add_check(
        checks,
        "second-carrier execution output boundary intent supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_INTENT_UNSUPPORTED",
    )
    if intent == INTENT_BLOCK:
        _add_check(
            checks,
            "second-carrier execution output boundary explicit block not requested",
            False,
            "no explicit block request",
            intent,
            "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_BLOCK_REQUESTED",
        )

    scope_values = _scope_values(request.get("second_carrier_execution_output_boundary_scope"))
    unsupported_scope = [
        scope
        for scope in scope_values
        if scope not in SUPPORTED_SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_SCOPE
    ]
    _add_check(
        checks,
        "second-carrier execution output boundary scope supported",
        bool(scope_values) and not unsupported_scope,
        SUPPORTED_SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_SCOPE,
        scope_values,
        "UNSUPPORTED_SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_SCOPE",
    )

    for basis_key in SELECTED_BASIS_KEYS:
        _add_check(
            checks,
            f"{basis_key} declared",
            _basis_declared(request, basis_key),
            "declared reference-shaped basis",
            _request_basis(request, basis_key),
            BASIS_MISSING_BLOCK_CODE_BY_KEY[basis_key],
        )

    execution_outcome = _execution_basis_value(
        request,
        (
            "selected_second_carrier_execution_result_outcome",
            "outcome",
        ),
    )
    _add_check(
        checks,
        "second-carrier execution outcome recorded",
        execution_outcome
        == "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_RECORDED",
        "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_RECORDED",
        execution_outcome,
        "SECOND_CARRIER_EXECUTION_NOT_RECORDED",
    )

    execution_version = _execution_basis_value(
        request,
        (
            "selected_second_carrier_execution_result_version",
            "result_version",
            "portable_source_body_verification_second_carrier_execution_result_version",
        ),
    )
    _add_check(
        checks,
        "second-carrier execution result version is 0.1.0",
        execution_version == RESULT_VERSION,
        RESULT_VERSION,
        execution_version,
        "SECOND_CARRIER_EXECUTION_VERSION_NOT_0_1_0",
    )

    failed_check_count = _to_int(
        _execution_basis_value(
            request,
            (
                "selected_second_carrier_execution_failed_check_count",
                "failed_check_count",
            ),
        ),
        None,
    )
    _add_check(
        checks,
        "second-carrier execution failed checks zero",
        failed_check_count == 0,
        0,
        failed_check_count,
        "SECOND_CARRIER_EXECUTION_FAILED_CHECKS_PRESENT",
    )

    bounded_recorded = _to_bool(
        _execution_basis_value(
            request,
            (
                "selected_second_carrier_execution_bounded_execution_recorded",
                "bounded_second_carrier_execution_recorded",
                "second_carrier_execution_recorded",
            ),
        ),
        None,
    )
    _add_check(
        checks,
        "second-carrier execution recorded bounded execution",
        bounded_recorded is True,
        True,
        bounded_recorded,
        "SECOND_CARRIER_EXECUTION_DID_NOT_RECORD_BOUNDED_EXECUTION",
    )

    execution_false_expectations = (
        (
            "second-carrier execution did not create execution output",
            (
                "selected_second_carrier_execution_execution_output_created",
                "execution_output_created",
            ),
            ("execution_output_not_created",),
            "SECOND_CARRIER_EXECUTION_ALREADY_CREATED_EXECUTION_OUTPUT",
        ),
        (
            "second-carrier execution did not create second-carrier output capture",
            (
                "selected_second_carrier_execution_created_second_carrier_output_capture",
                "second_carrier_output_capture_created",
            ),
            ("second_carrier_output_capture_not_created",),
            "SECOND_CARRIER_EXECUTION_ALREADY_CREATED_SECOND_CARRIER_OUTPUT_CAPTURE",
        ),
        (
            "second-carrier execution did not create second-carrier result",
            (
                "selected_second_carrier_execution_created_second_carrier_result",
                "second_carrier_result_created",
            ),
            ("second_carrier_result_not_created",),
            "SECOND_CARRIER_EXECUTION_ALREADY_CREATED_SECOND_CARRIER_RESULT",
        ),
        (
            "second-carrier execution did not create second-carrier success",
            (
                "selected_second_carrier_execution_created_second_carrier_success",
                "second_carrier_success_created",
            ),
            ("second_carrier_success_not_created",),
            "SECOND_CARRIER_EXECUTION_ALREADY_CREATED_SECOND_CARRIER_SUCCESS",
        ),
        (
            "second-carrier execution did not create external result",
            (
                "selected_second_carrier_execution_created_external_result",
                "external_result_created",
            ),
            ("external_result_not_created",),
            "SECOND_CARRIER_EXECUTION_CREATED_EXTERNAL_RESULT",
        ),
        (
            "second-carrier execution did not create cross-carrier evidence",
            (
                "selected_second_carrier_execution_created_cross_carrier_evidence",
                "cross_carrier_evidence_created",
            ),
            ("cross_carrier_evidence_not_created",),
            "SECOND_CARRIER_EXECUTION_CREATED_CROSS_CARRIER_EVIDENCE",
        ),
        (
            "second-carrier execution did not treat execution as output",
            (
                "selected_second_carrier_execution_treated_execution_as_output",
                "second_carrier_execution_treated_as_output",
            ),
            ("execution_not_output",),
            "SECOND_CARRIER_EXECUTION_TREATED_EXECUTION_AS_OUTPUT",
        ),
        (
            "second-carrier execution did not treat execution as output capture",
            (
                "selected_second_carrier_execution_treated_execution_as_output_capture",
                "second_carrier_execution_treated_as_output_capture",
            ),
            ("execution_not_output_capture",),
            "SECOND_CARRIER_EXECUTION_TREATED_EXECUTION_AS_OUTPUT_CAPTURE",
        ),
        (
            "second-carrier execution did not treat execution as result",
            (
                "selected_second_carrier_execution_treated_execution_as_result",
                "second_carrier_execution_treated_as_result",
            ),
            ("execution_not_result",),
            "SECOND_CARRIER_EXECUTION_TREATED_EXECUTION_AS_RESULT",
        ),
        (
            "second-carrier execution did not treat execution as success",
            (
                "selected_second_carrier_execution_treated_execution_as_success",
                "second_carrier_execution_treated_as_success",
            ),
            ("execution_not_success",),
            "SECOND_CARRIER_EXECUTION_TREATED_EXECUTION_AS_SUCCESS",
        ),
        (
            "second-carrier execution did not treat execution as external result",
            (
                "selected_second_carrier_execution_treated_execution_as_external_result",
                "second_carrier_execution_treated_as_external_result",
            ),
            ("execution_not_external_result",),
            "SECOND_CARRIER_EXECUTION_TREATED_EXECUTION_AS_EXTERNAL_RESULT",
        ),
        (
            "second-carrier execution did not treat execution as cross-carrier evidence",
            (
                "selected_second_carrier_execution_treated_execution_as_cross_carrier_evidence",
                "second_carrier_execution_treated_as_cross_carrier_evidence",
            ),
            ("execution_not_cross_carrier_evidence",),
            "SECOND_CARRIER_EXECUTION_TREATED_EXECUTION_AS_CROSS_CARRIER_EVIDENCE",
        ),
        (
            "second-carrier execution did not use hidden repo state as output authority",
            (
                "selected_second_carrier_execution_used_hidden_repo_state_as_output_authority",
                "hidden_repo_state_used_as_output_authority",
            ),
            (
                "hidden_repo_state_not_used_as_output_authority",
                "hidden_repo_state_not_used_as_execution_authority",
            ),
            "SECOND_CARRIER_EXECUTION_USED_HIDDEN_REPO_STATE_AS_OUTPUT_AUTHORITY",
        ),
        (
            "second-carrier execution did not treat repo-local availability as output authority",
            (
                "selected_second_carrier_execution_treated_repo_local_availability_as_output_authority",
                "repo_local_availability_treated_as_output_authority",
            ),
            (
                "repo_local_availability_not_output_authority",
                "repo_local_availability_not_execution_authority",
            ),
            "SECOND_CARRIER_EXECUTION_TREATED_REPO_LOCAL_AVAILABILITY_AS_OUTPUT_AUTHORITY",
        ),
        (
            "second-carrier execution did not treat receiving carrier as authority",
            (
                "selected_second_carrier_execution_treated_receiving_carrier_as_authority",
                "receiving_carrier_treated_as_authority",
            ),
            ("receiving_carrier_not_authority",),
            "SECOND_CARRIER_EXECUTION_TREATED_RECEIVING_CARRIER_AS_AUTHORITY",
        ),
        (
            "second-carrier execution did not return raw full prior artifact body",
            (
                "selected_second_carrier_execution_raw_full_prior_artifact_body_returned_outside_bounded_execution",
                "raw_full_prior_artifact_body_returned",
            ),
            ("raw_full_prior_artifact_body_not_returned",),
            "SECOND_CARRIER_EXECUTION_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY_OUTSIDE_BOUNDED_EXECUTION",
        ),
    )
    for check_name, false_keys, true_keys, code in execution_false_expectations:
        actual = _execution_basis_bool(request, false_keys, true_keys)
        _add_check(checks, check_name, actual is True, "false or inverse true", actual, code)

    for posture_key in POSTURE_KEYS:
        _add_check(
            checks,
            f"{posture_key} declared",
            _posture_declared(request, posture_key),
            "declared second-carrier execution output boundary posture",
            request.get(posture_key),
            "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_POSTURE_MISSING",
        )

    lineage_basis = request.get("selected_command_report_lineage_basis")
    lineage_only = _to_bool(
        _find_key(lineage_basis, {"lineage_only", "command_report_lineage_remains_lineage_only"}),
        True,
    )
    _add_check(
        checks,
        "command report lineage remains lineage only",
        lineage_only is True,
        True,
        lineage_only,
        "COMMAND_REPORT_LINEAGE_NOT_LINEAGE_ONLY",
    )

    predecessor_basis = request.get("selected_predecessor_failure_basis")
    v1_basis = request.get("selected_packet_emission_boundary_v1_predecessor_failure_basis")
    predecessor_visible = _to_bool(
        _find_key(
            {"predecessor": predecessor_basis, "v1": v1_basis},
            {
                "predecessor_failure_visible",
                "predecessor_failure_evidence_visible",
                "v1_predecessor_failure_preserved",
            },
        ),
        True,
    )
    _add_check(
        checks,
        "predecessor failure evidence visible and unrepaired",
        predecessor_visible is True,
        True,
        predecessor_visible,
        "PREDECESSOR_FAILURE_EVIDENCE_NOT_VISIBLE",
    )

    reference_shaped = _to_bool(request.get("reference_shaped_input_posture"), True)
    _add_check(
        checks,
        "selected basis remains reference-shaped",
        reference_shaped is True,
        True,
        reference_shaped,
        "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    )

    non_claims = request.get("declared_non_claims")
    for key in REQUIRED_FALSE_NON_CLAIMS:
        if not isinstance(non_claims, Mapping) or key not in non_claims:
            passed = False
            actual = None
        else:
            actual_bool = _to_bool(non_claims.get(key), None)
            passed = actual_bool is False
            actual = actual_bool
        _add_check(
            checks,
            f"declared non-claim {key} is false",
            passed,
            False,
            actual,
            _block_code_for_non_claim(key),
        )

    for key, code in EXTRA_FORBIDDEN_FLAG_BLOCK_CODE_BY_KEY.items():
        actual = _to_bool(_extract_value(request, (key,), SELECTED_BASIS_KEYS), False)
        _add_check(
            checks,
            f"forbidden flag {key} remains false",
            actual is False,
            False,
            actual,
            code,
        )

    return checks


def _build_metadata(
    request: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    passed_count, failed_count = _check_counts(checks)
    request_id = str(
        request.get("second_carrier_execution_output_boundary_request_id")
        or "portable_source_body_verification_second_carrier_execution_output_boundary_reference_review_001"
    )
    return {
        "portable_source_body_verification_second_carrier_execution_output_boundary_result_id": (
            f"{request_id}__portable_source_body_verification_second_carrier_execution_output_boundary_result"
        ),
        "portable_source_body_verification_second_carrier_execution_output_boundary_result_type": RESULT_TYPE,
        "portable_source_body_verification_second_carrier_execution_output_boundary_result_version": RESULT_VERSION,
        "second_carrier_execution_output_boundary_request_id": request_id,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
    }


def _build_declared_question(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "second_carrier_execution_output_boundary_request_id": request.get(
            "second_carrier_execution_output_boundary_request_id"
        ),
        "question": request.get("second_carrier_execution_output_boundary_question"),
        "governing_question": CORE_QUESTION,
        "intent": request.get("second_carrier_execution_output_boundary_intent"),
    }


def _build_basis_section(request: Mapping[str, Any], key: str) -> dict[str, Any]:
    basis = _request_basis(request, key)
    section: dict[str, Any] = {
        "basis_key": key,
        "basis_declared": _basis_declared(request, key),
        "basis_remains_basis_only": True,
        "reference_shape_preserved": True,
        "selected_reference": _sanitize_reference(basis),
        "raw_full_prior_artifact_body_returned": False,
        "prior_artifacts_mutated": False,
    }
    if key == "selected_second_carrier_execution_basis":
        section.update(
            {
                "selected_second_carrier_execution_result_path": request.get(
                    "selected_second_carrier_execution_result_path"
                )
                or _find_key(basis, {"result_path", "path", "artifact_path"}),
                "selected_second_carrier_execution_result_id": request.get(
                    "selected_second_carrier_execution_result_id"
                )
                or _find_key(
                    basis,
                    {
                        "portable_source_body_verification_second_carrier_execution_result_id",
                        "result_id",
                        "artifact_id",
                    },
                ),
                "selected_second_carrier_execution_result_outcome": _execution_basis_value(
                    request,
                    (
                        "selected_second_carrier_execution_result_outcome",
                        "outcome",
                    ),
                ),
                "selected_second_carrier_execution_result_version": _execution_basis_value(
                    request,
                    (
                        "selected_second_carrier_execution_result_version",
                        "result_version",
                        "portable_source_body_verification_second_carrier_execution_result_version",
                    ),
                ),
                "selected_second_carrier_execution_failed_check_count": _to_int(
                    _execution_basis_value(
                        request,
                        (
                            "selected_second_carrier_execution_failed_check_count",
                            "failed_check_count",
                        ),
                    ),
                    None,
                ),
                "selected_second_carrier_execution_bounded_execution_recorded": _to_bool(
                    _execution_basis_value(
                        request,
                        (
                            "selected_second_carrier_execution_bounded_execution_recorded",
                            "bounded_second_carrier_execution_recorded",
                            "second_carrier_execution_recorded",
                        ),
                    ),
                    None,
                ),
                "execution_output_not_created": _execution_basis_bool(
                    request,
                    (
                        "selected_second_carrier_execution_execution_output_created",
                        "execution_output_created",
                    ),
                    ("execution_output_not_created",),
                ),
                "second_carrier_output_capture_not_created": _execution_basis_bool(
                    request,
                    (
                        "selected_second_carrier_execution_created_second_carrier_output_capture",
                        "second_carrier_output_capture_created",
                    ),
                    ("second_carrier_output_capture_not_created",),
                ),
                "second_carrier_result_not_created": _execution_basis_bool(
                    request,
                    (
                        "selected_second_carrier_execution_created_second_carrier_result",
                        "second_carrier_result_created",
                    ),
                    ("second_carrier_result_not_created",),
                ),
                "second_carrier_success_not_created": _execution_basis_bool(
                    request,
                    (
                        "selected_second_carrier_execution_created_second_carrier_success",
                        "second_carrier_success_created",
                    ),
                    ("second_carrier_success_not_created",),
                ),
                "external_result_not_created": _execution_basis_bool(
                    request,
                    (
                        "selected_second_carrier_execution_created_external_result",
                        "external_result_created",
                    ),
                    ("external_result_not_created",),
                ),
                "cross_carrier_evidence_not_created": _execution_basis_bool(
                    request,
                    (
                        "selected_second_carrier_execution_created_cross_carrier_evidence",
                        "cross_carrier_evidence_created",
                    ),
                    ("cross_carrier_evidence_not_created",),
                ),
            }
        )
    if key == "selected_command_report_lineage_basis":
        section.update(
            {
                "command_report_lineage_remains_lineage_only": True,
                "command_report_lineage_not_current_report_artifact": True,
                "command_report_lineage_not_source": True,
                "command_report_lineage_not_authority": True,
                "command_report_lineage_not_currentness": True,
            }
        )
    if key in (
        "selected_predecessor_failure_basis",
        "selected_packet_emission_boundary_v1_predecessor_failure_basis",
    ):
        section.update(
            {
                "predecessor_failure_evidence_visible": True,
                "predecessor_failure_evidence_unrepaired": True,
                "v1_repaired": False,
                "v1_hidden": False,
                "v1_claimed_passed": False,
            }
        )
    return section


def _build_posture_section(
    request: Mapping[str, Any], key: str, recorded: bool
) -> dict[str, Any]:
    statement_key = POSTURE_TO_STATEMENT[key]
    return {
        "posture_key": key,
        "posture_declared": _posture_declared(request, key),
        statement_key: bool(recorded),
        "posture_scope": "second-carrier-execution-output-boundary only",
        "creates_output": False,
        "creates_output_artifact": False,
        "creates_output_capture": False,
        "creates_result": False,
        "creates_success": False,
        "creates_external_result": False,
        "creates_cross_carrier_evidence": False,
        "creates_source_authority_currentness_runtime_final_completion": False,
        "authorizes_follow_on_work": False,
    }


def _build_statement(outcome: str) -> dict[str, bool]:
    recorded = outcome == OUTCOME_RECORDED
    statement = {key: bool(recorded) for key in ALLOWED_TRUE_RECORDED_FIELDS}
    for key in REQUIRED_FALSE_NON_CLAIMS:
        statement[key] = False
    statement["full_prior_artifact_body_emitted_outside_bounded_output_boundary"] = False
    statement["artifacts_mutated"] = False
    return statement


def _build_non_meaning() -> dict[str, bool]:
    false_keys = (
        "execution_output_exists",
        "output_artifact_exists",
        "second_carrier_output_capture_exists",
        "second_carrier_result_exists",
        "second_carrier_success_exists",
        "external_result_exists",
        "cross_carrier_evidence_exists",
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
        "output_boundary_became_output",
        "output_boundary_became_capture",
        "output_boundary_became_result",
        "output_boundary_became_success",
        "output_boundary_became_external_result",
        "output_boundary_became_cross_carrier_proof",
        "output_boundary_became_source_transfer",
        "output_boundary_became_source_receipt",
        "output_boundary_became_reception_authorization",
        "output_boundary_became_source",
        "output_boundary_became_authority",
        "output_boundary_became_currentness",
        "execution_became_output",
        "execution_artifact_became_output",
        "receiving_carrier_became_authority",
        "transferred_packet_became_source",
        "transferred_packet_became_authority",
        "transferred_packet_became_currentness",
        "artifact_existence_became_output_authority",
        "artifact_path_became_currentness",
        "repo_local_availability_became_output_authority",
        "hidden_repo_state_became_output_authority",
        "v1_packet_emission_boundary_repaired",
        "v1_packet_emission_boundary_hidden",
        "v1_packet_emission_boundary_erased",
        "v1_packet_emission_boundary_claimed_passed",
    )
    return {key: False for key in false_keys}


def _build_additional_basis_required(
    outcome: str, request: Mapping[str, Any]
) -> dict[str, Any]:
    context = request.get("additional_basis_context")
    required = outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    return {
        "additional_basis_required": required,
        "additional_basis_context": _sanitize_reference(context) if required else [],
        "missing_basis_scheduled": False,
        "missing_basis_authorized": False,
        "missing_basis_executed": False,
    }


def _build_not_recorded_basis(outcome: str, request: Mapping[str, Any]) -> dict[str, Any]:
    provided = request.get("not_recorded_basis")
    not_recorded = outcome == OUTCOME_NOT_RECORDED
    return {
        "not_recorded": not_recorded,
        "not_recorded_basis": _sanitize_reference(provided) if not_recorded else [],
        "prior_artifacts_mutated": False,
        "prior_artifacts_repaired": False,
        "next_work_authorized": False,
    }


def _build_what_remains_open() -> dict[str, Any]:
    return {
        "open_items": list(WHAT_REMAINS_OPEN_ITEMS),
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }


def _determine_outcome(
    request: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
) -> str:
    if _block_from_checks(checks, request.get("block_reason")) is not None:
        return OUTCOME_BLOCKED
    requested = request.get("requested_second_carrier_execution_output_boundary_outcome")
    if requested == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS
    if requested == OUTCOME_NOT_RECORDED:
        return OUTCOME_NOT_RECORDED
    if request.get("second_carrier_execution_output_boundary_intent") == INTENT_DO_NOT_RECORD:
        return OUTCOME_NOT_RECORDED
    return OUTCOME_RECORDED


def resolve_portable_source_body_verification_second_carrier_execution_output_boundary(
    declared_second_carrier_execution_output_boundary_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded second-carrier execution output boundary posture."""

    malformed_code: str | None = None
    if declared_second_carrier_execution_output_boundary_request is None:
        request: dict[str, Any] = {}
        malformed_code = (
            "DECLARED_SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_REQUEST_MALFORMED"
        )
    elif not isinstance(
        declared_second_carrier_execution_output_boundary_request, Mapping
    ):
        request = {}
        malformed_code = (
            "DECLARED_SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_REQUEST_MALFORMED"
        )
    else:
        request = copy.deepcopy(
            dict(declared_second_carrier_execution_output_boundary_request)
        )

    checks = _build_checks(request, malformed_code=malformed_code)
    outcome = _determine_outcome(request, checks)
    block = (
        _block_from_checks(checks, request.get("block_reason"))
        if outcome == OUTCOME_BLOCKED
        else None
    )
    recorded = outcome == OUTCOME_RECORDED

    result: dict[str, Any] = {
        "portable_source_body_verification_second_carrier_execution_output_boundary_metadata": _build_metadata(
            request, checks
        ),
        "declared_second_carrier_execution_output_boundary_question": _build_declared_question(
            request
        ),
    }

    for basis_key in SELECTED_BASIS_KEYS:
        result[basis_key] = _build_basis_section(request, basis_key)

    for posture_key in POSTURE_KEYS:
        result[posture_key] = _build_posture_section(request, posture_key, recorded)

    result.update(
        {
            "second_carrier_execution_output_boundary_scope": {
                "scope_values": list(
                    _scope_values(
                        request.get("second_carrier_execution_output_boundary_scope")
                    )
                ),
                "supported_scope_values": list(
                    SUPPORTED_SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_SCOPE
                ),
                "unsupported_scope_values": [
                    scope
                    for scope in _scope_values(
                        request.get("second_carrier_execution_output_boundary_scope")
                    )
                    if scope
                    not in SUPPORTED_SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_SCOPE
                ],
            },
            "second_carrier_execution_output_boundary_checks": checks,
            "second_carrier_execution_output_boundary_statement": _build_statement(
                outcome
            ),
            "second_carrier_execution_output_boundary_non_meaning": _build_non_meaning(),
            "additional_basis_required": _build_additional_basis_required(
                outcome, request
            ),
            "not_recorded_basis": _build_not_recorded_basis(outcome, request),
            "what_remains_open": _build_what_remains_open(),
            "non_claims": _non_claims_from_request(request),
            "outcome": outcome,
            "block": block,
        }
    )
    result[
        "portable_source_body_verification_second_carrier_execution_output_boundary_summary"
    ] = build_portable_source_body_verification_second_carrier_execution_output_boundary_summary(
        result
    )
    return _json_safe(result)


def resolve_portable_source_body_verification_second_carrier_execution_output_boundary_from_path(
    declared_second_carrier_execution_output_boundary_request_path: Path | str,
) -> dict[str, Any]:
    """Resolve from a JSON object request path."""

    path = Path(declared_second_carrier_execution_output_boundary_request_path)
    try:
        raw = path.read_text(encoding="utf-8")
        parsed = json.loads(raw)
    except OSError as exc:
        raise PortableSourceBodyVerificationSecondCarrierExecutionOutputBoundaryError(
            f"declared request path is unreadable: {path}"
        ) from exc
    except json.JSONDecodeError as exc:
        raise PortableSourceBodyVerificationSecondCarrierExecutionOutputBoundaryError(
            f"declared request path does not contain valid JSON: {path}"
        ) from exc
    if not isinstance(parsed, Mapping):
        return resolve_portable_source_body_verification_second_carrier_execution_output_boundary(
            None
        )
    return resolve_portable_source_body_verification_second_carrier_execution_output_boundary(
        declared_second_carrier_execution_output_boundary_request=parsed
    )


def _summary_bool(statement: Mapping[str, Any], key: str) -> bool:
    return bool(_to_bool(statement.get(key), False))


def build_portable_source_body_verification_second_carrier_execution_output_boundary_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact summary that preserves boundary and non-claim posture."""

    metadata = result.get(
        "portable_source_body_verification_second_carrier_execution_output_boundary_metadata",
        {},
    )
    question = result.get("declared_second_carrier_execution_output_boundary_question", {})
    statement = result.get("second_carrier_execution_output_boundary_statement", {})
    non_claims = result.get("non_claims", {})
    block = result.get("block") or {}
    checks = result.get("second_carrier_execution_output_boundary_checks", [])
    selected_execution = result.get("selected_second_carrier_execution_basis", {})
    passed_count, failed_count = _check_counts(checks if isinstance(checks, list) else [])

    key_non_claims = {
        key: bool(_to_bool(non_claims.get(key), False))
        for key in (
            "execution_output_created",
            "output_artifact_created",
            "second_carrier_output_capture_created",
            "second_carrier_result_created",
            "second_carrier_success_created",
            "external_result_created",
            "cross_carrier_evidence_created",
            "source_transfer_occurred",
            "source_receipt_occurred",
            "reception_authorization_created",
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
            "v1_repaired",
            "v1_hidden",
            "v1_claimed_passed",
        )
    }

    summary: dict[str, Any] = {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("reason"),
        "second_carrier_execution_output_boundary_request_id": metadata.get(
            "second_carrier_execution_output_boundary_request_id"
        ),
        "question": question.get("question"),
        "intent": question.get("intent"),
        "passed_check_count": metadata.get("passed_check_count", passed_count),
        "failed_check_count": metadata.get("failed_check_count", failed_count),
        "selected_second_carrier_execution_outcome": selected_execution.get(
            "selected_second_carrier_execution_result_outcome"
        ),
        "selected_second_carrier_execution_version": selected_execution.get(
            "selected_second_carrier_execution_result_version"
        ),
        "selected_second_carrier_execution_failed_check_count": selected_execution.get(
            "selected_second_carrier_execution_failed_check_count"
        ),
        "key_non_claims": key_non_claims,
        "no_output_output_capture_result_success_external_result_cross_carrier_evidence": (
            key_non_claims["execution_output_created"] is False
            and key_non_claims["output_artifact_created"] is False
            and key_non_claims["second_carrier_output_capture_created"] is False
            and key_non_claims["second_carrier_result_created"] is False
            and key_non_claims["second_carrier_success_created"] is False
            and key_non_claims["external_result_created"] is False
            and key_non_claims["cross_carrier_evidence_created"] is False
        ),
        "no_source_authority_currentness_final_completion_runtime": (
            key_non_claims["source_created"] is False
            and key_non_claims["authority_created"] is False
            and key_non_claims["currentness_created"] is False
            and key_non_claims["final_completion_claimed"] is False
            and key_non_claims["runtime_hosting_created"] is False
        ),
        "no_deployment_public_release_follow_on": (
            key_non_claims["deployment_created"] is False
            and key_non_claims["public_release_created"] is False
            and key_non_claims["follow_on_work_authorized"] is False
        ),
        "v1_predecessor_failure_preserved": True,
        "v1_not_repaired_hidden_claimed_passed": (
            key_non_claims["v1_repaired"] is False
            and key_non_claims["v1_hidden"] is False
            and key_non_claims["v1_claimed_passed"] is False
        ),
    }

    for key in ALLOWED_TRUE_RECORDED_FIELDS:
        summary[key] = _summary_bool(statement, key)
    return _json_safe(summary)


def _safe_filename_part(value: Any) -> str:
    text = str(value or "").strip()
    if not text:
        text = (
            "portable_source_body_verification_second_carrier_execution_"
            "output_boundary_reference_review_001"
        )
    safe = []
    for char in text:
        if char.isalnum() or char in ("-", "_", "."):
            safe.append(char)
        else:
            safe.append("_")
    return "".join(safe)


def _request_id_from_result(result: Mapping[str, Any]) -> str:
    metadata = result.get(
        "portable_source_body_verification_second_carrier_execution_output_boundary_metadata",
        {},
    )
    if isinstance(metadata, Mapping):
        request_id = metadata.get("second_carrier_execution_output_boundary_request_id")
        if request_id:
            return str(request_id)
    question = result.get("declared_second_carrier_execution_output_boundary_question", {})
    if isinstance(question, Mapping) and question.get(
        "second_carrier_execution_output_boundary_request_id"
    ):
        return str(question["second_carrier_execution_output_boundary_request_id"])
    return (
        "portable_source_body_verification_second_carrier_execution_"
        "output_boundary_reference_review_001"
    )


def _unique_output_path(path: Path) -> Path:
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


def write_portable_source_body_verification_second_carrier_execution_output_boundary_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a bounded result JSON without silently overwriting existing files."""

    if not isinstance(result, Mapping):
        raise PortableSourceBodyVerificationSecondCarrierExecutionOutputBoundaryError(
            "result must be a mapping"
        )
    request_id = _safe_filename_part(_request_id_from_result(result))
    filename = (
        f"{request_id}__portable_source_body_verification_second_carrier_execution_"
        "output_boundary_result.json"
    )
    if output_path is None:
        path = OUTPUT_ROOT / filename
    else:
        path = Path(output_path)
        if path.exists() and path.is_dir():
            path = path / filename
        elif path.suffix == "":
            path = path / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    path = _unique_output_path(path)
    path.write_text(
        json.dumps(_json_safe(result), ensure_ascii=True, indent=2, sort_keys=True)
        + "\n",
        encoding="utf-8",
    )
    return path


def _default_basis(
    basis_key: str,
    outcome: str | None = None,
    extra: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    basis = {
        "basis_key": basis_key,
        "basis_declared": True,
        "reference_shape_preserved": True,
        "basis_remains_basis_only": True,
        "failed_check_count": 0,
    }
    if outcome is not None:
        basis["outcome"] = outcome
    if extra:
        basis.update(dict(extra))
    return basis


def _default_posture(posture_key: str) -> dict[str, Any]:
    return {
        "posture_key": posture_key,
        "posture_declared": True,
        "declared": True,
        "posture": True,
    }


def build_declared_portable_source_body_verification_second_carrier_execution_output_boundary_request(
    second_carrier_execution_output_boundary_request_id: str = (
        "portable_source_body_verification_second_carrier_execution_"
        "output_boundary_reference_review_001"
    ),
    **overrides: Any,
) -> dict[str, Any]:
    """Build a bounded request that records output-boundary posture only."""

    non_claims = {key: False for key in REQUIRED_FALSE_NON_CLAIMS}
    execution_basis = _default_basis(
        "selected_second_carrier_execution_basis",
        "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_RECORDED",
        {
            "result_version": RESULT_VERSION,
            "bounded_second_carrier_execution_recorded": True,
            "second_carrier_execution_recorded": True,
            "execution_output_not_created": True,
            "execution_not_output": True,
            "execution_not_output_capture": True,
            "execution_not_result": True,
            "execution_not_success": True,
            "execution_not_external_result": True,
            "execution_not_cross_carrier_evidence": True,
            "second_carrier_output_capture_not_created": True,
            "second_carrier_result_not_created": True,
            "second_carrier_success_not_created": True,
            "external_result_not_created": True,
            "cross_carrier_evidence_not_created": True,
            "receiving_carrier_not_authority": True,
            "hidden_repo_state_excluded": True,
            "hidden_repo_state_not_used_as_output_authority": True,
            "hidden_repo_state_not_used_as_execution_authority": True,
            "repo_local_availability_not_output_authority": True,
            "repo_local_availability_not_execution_authority": True,
            "raw_full_prior_artifact_body_not_returned": True,
            **non_claims,
        },
    )

    request: dict[str, Any] = {
        "second_carrier_execution_output_boundary_request_id": (
            second_carrier_execution_output_boundary_request_id
        ),
        "second_carrier_execution_output_boundary_question": CORE_QUESTION,
        "second_carrier_execution_output_boundary_intent": INTENT_RECORD,
        "second_carrier_execution_output_boundary_scope": list(
            SUPPORTED_SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_SCOPE
        ),
        "declared_non_claims": non_claims,
        "reference_shaped_input_posture": True,
        "selected_second_carrier_execution_basis": execution_basis,
        "selected_second_carrier_execution_terminal_summary_basis": _default_basis(
            "selected_second_carrier_execution_terminal_summary_basis",
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_RECORDED",
        ),
        "selected_second_carrier_execution_boundary_basis": _default_basis(
            "selected_second_carrier_execution_boundary_basis",
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_BOUNDARY_RECORDED",
        ),
        "selected_second_carrier_receipt_basis": _default_basis(
            "selected_second_carrier_receipt_basis",
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RECEIPT_RECORDED",
        ),
        "selected_second_carrier_receipt_boundary_basis": _default_basis(
            "selected_second_carrier_receipt_boundary_basis",
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RECEIPT_BOUNDARY_RECORDED",
        ),
        "selected_packet_transfer_basis": _default_basis(
            "selected_packet_transfer_basis",
            "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_TRANSFER_RECORDED",
        ),
        "selected_packet_transfer_boundary_basis": _default_basis(
            "selected_packet_transfer_boundary_basis",
            "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_TRANSFER_BOUNDARY_RECORDED",
        ),
        "selected_packet_emission_basis": _default_basis(
            "selected_packet_emission_basis",
            "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_RECORDED",
        ),
        "selected_packet_emission_boundary_v2_basis": _default_basis(
            "selected_packet_emission_boundary_v2_basis",
            "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_BOUNDARY_RECORDED",
        ),
        "selected_packet_emission_boundary_v1_predecessor_failure_basis": _default_basis(
            "selected_packet_emission_boundary_v1_predecessor_failure_basis",
            None,
            {
                "predecessor_failure_evidence_visible": True,
                "predecessor_failure_evidence_unrepaired": True,
                "v1_repaired": False,
                "v1_hidden": False,
                "v1_claimed_passed": False,
            },
        ),
        "selected_packet_artifact_basis": _default_basis(
            "selected_packet_artifact_basis",
            "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_ARTIFACT_RECORDED",
        ),
        "selected_packet_boundary_basis": _default_basis(
            "selected_packet_boundary_basis",
            "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_BOUNDARY_RECORDED",
        ),
        "selected_command_success_basis": _default_basis(
            "selected_command_success_basis",
            "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_RECORDED",
        ),
        "selected_command_result_v2_basis": _default_basis(
            "selected_command_result_v2_basis",
            "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_RECORDED",
        ),
        "selected_output_capture_v2_basis": _default_basis(
            "selected_output_capture_v2_basis",
            "PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_RECORDED",
        ),
        "selected_command_output_report_artifact_basis": _default_basis(
            "selected_command_output_report_artifact_basis",
            "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_REPORT_ARTIFACT_RECORDED",
        ),
        "selected_command_execution_basis": _default_basis(
            "selected_command_execution_basis",
            "PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_RECORDED",
            {"original_carrier_execution_trace_audit_only": True},
        ),
        "selected_command_report_lineage_basis": _default_basis(
            "selected_command_report_lineage_basis",
            None,
            {
                "lineage_only": True,
                "command_report_lineage_remains_lineage_only": True,
                "command_report_lineage_treated_as_current_report_artifact": False,
                "command_report_lineage_treated_as_source": False,
                "command_report_lineage_treated_as_authority": False,
                "command_report_lineage_treated_as_currentness": False,
            },
        ),
        "selected_predecessor_failure_basis": _default_basis(
            "selected_predecessor_failure_basis",
            None,
            {
                "predecessor_failure_visible": True,
                "predecessor_failure_evidence_visible": True,
                "predecessor_failure_evidence_unrepaired": True,
            },
        ),
        "selected_evidence_manifest_basis": _default_basis(
            "selected_evidence_manifest_basis", None
        ),
        "selected_artifact_containment_basis": _default_basis(
            "selected_artifact_containment_basis", None
        ),
        "selected_portable_verification_basis": _default_basis(
            "selected_portable_verification_basis", None
        ),
    }
    for posture_key in POSTURE_KEYS:
        request[posture_key] = _default_posture(posture_key)
    request.update(overrides)
    return _json_safe(request)
