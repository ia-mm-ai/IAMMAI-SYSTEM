"""Bounded portable source-body verification second-carrier execution resolver.

This module is downstream of a recorded second-carrier execution boundary. It
may record one bounded second-carrier execution posture only. Execution remains
execution posture; it is not execution output, second-carrier output capture,
second-carrier result, second-carrier success, external result capture,
cross-carrier evidence review, source transfer, source receipt, reception
authorization, source, authority, currentness, runtime, final completion,
continuation, reusable permission, derivative reception, vessel relation,
another reception request, or follow-on work.

The v1 packet-emission-boundary resolver remains visible predecessor
conformance-failure evidence. This resolver does not repair it, hide it, erase
it, or claim it passed. It imports no repo-local modules, runs no commands,
mutates no upstream artifact, keeps selected basis sections reference-shaped,
contains raw or hidden-state payload values, and never returns a raw full prior
artifact body outside bounded execution posture.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class PortableSourceBodyVerificationSecondCarrierExecutionError(Exception):
    """Raised for hard second-carrier-execution input/output failures."""


RESOLVER_MODULE = "resolve_portable_source_body_verification_second_carrier_execution"
RESULT_TYPE = "portable_source_body_verification_second_carrier_execution_result"
RESULT_VERSION = "0.1.0"
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_portable_source_body_verification_"
    "second_carrier_execution"
)

CORE_QUESTION = (
    "Can the second-carrier-execution-boundary basis be used to record one "
    "bounded second-carrier execution without creating execution output, "
    "second-carrier output capture, second-carrier result, second-carrier "
    "success, external result, cross-carrier evidence, source transfer, source "
    "receipt, reception authorization, source, authority, currentness, runtime, "
    "final completion, continuation, reusable permission, derivative reception, "
    "vessel relation, another reception request, or follow-on work?"
)

OUTCOME_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_RECORDED"
OUTCOME_NOT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION"
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION"
)
INTENT_BLOCK = "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

SECOND_CARRIER_EXECUTION_BOUNDARY_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_BOUNDARY_RECORDED"
)
SECOND_CARRIER_EXECUTION_BOUNDARY_RESULT_VERSION = "0.1.0"
SECOND_CARRIER_RECEIPT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RECEIPT_RECORDED"
)

SUPPORTED_SECOND_CARRIER_EXECUTION_SCOPE = (
    "SECOND_CARRIER_EXECUTION_SPEC_ONLY",
    "ONE_BOUNDED_SECOND_CARRIER_EXECUTION_RECORDED",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_BASIS_PRESERVED",
    "SECOND_CARRIER_RECEIPT_BASIS_PRESERVED",
    "RECEIPT_ARTIFACT_BASIS_PRESERVED",
    "EXECUTION_RECORDED_BOUNDED",
    "EXECUTION_ARTIFACT_RECORDED_OR_BOUNDED",
    "EXECUTION_OUTPUT_NOT_CREATED",
    "EXECUTION_NOT_OUTPUT_CAPTURE",
    "EXECUTION_NOT_RESULT",
    "EXECUTION_NOT_SUCCESS",
    "EXECUTION_NOT_EXTERNAL_RESULT",
    "EXECUTION_NOT_CROSS_CARRIER_EVIDENCE",
    "EXECUTION_NOT_SOURCE_TRANSFER",
    "EXECUTION_NOT_SOURCE_RECEIPT",
    "EXECUTION_NOT_RECEPTION_AUTHORIZATION",
    "SECOND_CARRIER_OUTPUT_CAPTURE_NOT_CREATED",
    "SECOND_CARRIER_RESULT_NOT_CREATED",
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
    "NO_OUTPUT_INFERENCE",
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
    "HIDDEN_REPO_STATE_NOT_USED_AS_EXECUTION_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_NOT_EXECUTION_AUTHORITY",
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
    "selected_second_carrier_execution_boundary_basis",
    "selected_second_carrier_execution_boundary_terminal_summary_basis",
    "selected_second_carrier_receipt_basis",
    "selected_second_carrier_receipt_terminal_summary_basis",
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
    "second_carrier_execution_spec_only_posture",
    "one_bounded_second_carrier_execution_posture",
    "second_carrier_execution_boundary_basis_preserved_posture",
    "second_carrier_receipt_basis_preserved_posture",
    "receipt_artifact_basis_preserved_posture",
    "execution_recorded_bounded_posture",
    "execution_artifact_recorded_or_bounded_posture",
    "execution_output_not_created_posture",
    "execution_not_output_capture_posture",
    "execution_not_result_posture",
    "execution_not_success_posture",
    "execution_not_external_result_posture",
    "execution_not_cross_carrier_evidence_posture",
    "execution_not_source_transfer_posture",
    "execution_not_source_receipt_posture",
    "execution_not_reception_authorization_posture",
    "second_carrier_output_capture_not_created_posture",
    "second_carrier_result_not_created_posture",
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
    "repo_local_availability_not_execution_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "second_carrier_execution_recorded",
    "bounded_second_carrier_execution_recorded",
    "execution_artifact_recorded_or_bounded",
    "second_carrier_execution_boundary_basis_preserved",
    "second_carrier_receipt_basis_preserved",
    "receipt_artifact_basis_preserved",
    "execution_recorded_bounded",
    "execution_output_not_created",
    "execution_not_output_capture",
    "execution_not_result",
    "execution_not_success",
    "execution_not_external_result",
    "execution_not_cross_carrier_evidence",
    "execution_not_source_transfer",
    "execution_not_source_receipt",
    "execution_not_reception_authorization",
    "second_carrier_output_capture_not_created",
    "second_carrier_result_not_created",
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
    "hidden_repo_state_not_used_as_execution_authority",
    "repo_local_availability_not_execution_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
)

REQUIRED_FALSE_NON_CLAIMS = (
    "execution_output_created",
    "second_carrier_output_capture_created",
    "second_carrier_result_created",
    "second_carrier_success_created",
    "external_result_created",
    "cross_carrier_evidence_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "second_carrier_execution_treated_as_output",
    "second_carrier_execution_treated_as_output_capture",
    "second_carrier_execution_treated_as_result",
    "second_carrier_execution_treated_as_success",
    "second_carrier_execution_treated_as_external_result",
    "second_carrier_execution_treated_as_cross_carrier_evidence",
    "second_carrier_execution_treated_as_source_transfer",
    "second_carrier_execution_treated_as_source_receipt",
    "second_carrier_execution_treated_as_reception_authorization",
    "second_carrier_execution_treated_as_source",
    "second_carrier_execution_treated_as_authority",
    "second_carrier_execution_treated_as_currentness",
    "second_carrier_execution_treated_as_final_completion",
    "second_carrier_execution_treated_as_runtime",
    "second_carrier_execution_treated_as_continuation",
    "second_carrier_execution_treated_as_reusable_permission",
    "second_carrier_execution_treated_as_follow_on_work",
    "receiving_carrier_treated_as_authority",
    "artifact_existence_treated_as_execution_authority",
    "artifact_path_treated_as_currentness",
    "repo_local_availability_treated_as_execution_authority",
    "hidden_repo_state_used_as_execution_content",
    "hidden_repo_state_used_as_execution_authority",
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

BLOCK_CODES = frozenset(
    {
        "DECLARED_SECOND_CARRIER_EXECUTION_REQUEST_MALFORMED",
        "DECLARED_SECOND_CARRIER_EXECUTION_REQUEST_UNREADABLE",
        "SECOND_CARRIER_EXECUTION_BLOCK_REQUESTED",
        "SECOND_CARRIER_EXECUTION_QUESTION_UNDECLARED",
        "SECOND_CARRIER_EXECUTION_INTENT_UNSUPPORTED",
        "SECOND_CARRIER_EXECUTION_BOUNDARY_BASIS_MISSING",
        "SECOND_CARRIER_EXECUTION_BOUNDARY_TERMINAL_SUMMARY_BASIS_MISSING",
        "SECOND_CARRIER_EXECUTION_BOUNDARY_NOT_RECORDED",
        "SECOND_CARRIER_EXECUTION_BOUNDARY_FAILED_CHECKS_PRESENT",
        "SECOND_CARRIER_EXECUTION_BOUNDARY_VERSION_NOT_0_1_0",
        "SECOND_CARRIER_EXECUTION_BOUNDARY_DID_NOT_DECLARE_FUTURE_EXECUTION_STEP",
        "SECOND_CARRIER_EXECUTION_BOUNDARY_ALREADY_CREATED_EXECUTION",
        "SECOND_CARRIER_EXECUTION_BOUNDARY_ALREADY_CREATED_EXECUTION_ARTIFACT",
        "SECOND_CARRIER_EXECUTION_BOUNDARY_ALREADY_CREATED_EXECUTION_OUTPUT",
        "SECOND_CARRIER_EXECUTION_BOUNDARY_ALREADY_CREATED_SECOND_CARRIER_OUTPUT_CAPTURE",
        "SECOND_CARRIER_EXECUTION_BOUNDARY_ALREADY_CREATED_SECOND_CARRIER_RESULT",
        "SECOND_CARRIER_EXECUTION_BOUNDARY_ALREADY_CREATED_SECOND_CARRIER_SUCCESS",
        "SECOND_CARRIER_EXECUTION_BOUNDARY_CREATED_EXTERNAL_RESULT",
        "SECOND_CARRIER_EXECUTION_BOUNDARY_CREATED_CROSS_CARRIER_EVIDENCE",
        "SECOND_CARRIER_EXECUTION_BOUNDARY_USED_HIDDEN_REPO_STATE_AS_EXECUTION_AUTHORITY",
        "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_REPO_LOCAL_AVAILABILITY_AS_EXECUTION_AUTHORITY",
        "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_RECEIVING_CARRIER_AS_AUTHORITY",
        "SECOND_CARRIER_EXECUTION_BOUNDARY_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY",
        "SECOND_CARRIER_RECEIPT_BASIS_MISSING",
        "SECOND_CARRIER_RECEIPT_TERMINAL_SUMMARY_BASIS_MISSING",
        "SECOND_CARRIER_RECEIPT_BOUNDARY_BASIS_MISSING",
        "SECOND_CARRIER_RECEIPT_NOT_RECORDED",
        "SECOND_CARRIER_RECEIPT_FAILED_CHECKS_PRESENT",
        "SECOND_CARRIER_RECEIPT_DID_NOT_RECORD_BOUNDED_RECEIPT",
        "SECOND_CARRIER_RECEIPT_TREATED_RECEIPT_AS_EXECUTION",
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
        "SECOND_CARRIER_EXECUTION_TREATED_AS_OUTPUT",
        "SECOND_CARRIER_EXECUTION_TREATED_AS_OUTPUT_CAPTURE",
        "SECOND_CARRIER_EXECUTION_TREATED_AS_RESULT",
        "SECOND_CARRIER_EXECUTION_TREATED_AS_SUCCESS",
        "SECOND_CARRIER_EXECUTION_TREATED_AS_EXTERNAL_RESULT",
        "SECOND_CARRIER_EXECUTION_TREATED_AS_CROSS_CARRIER_EVIDENCE",
        "SECOND_CARRIER_EXECUTION_TREATED_AS_SOURCE_TRANSFER",
        "SECOND_CARRIER_EXECUTION_TREATED_AS_SOURCE_RECEIPT",
        "SECOND_CARRIER_EXECUTION_TREATED_AS_RECEPTION_AUTHORIZATION",
        "SECOND_CARRIER_EXECUTION_TREATED_AS_SOURCE",
        "SECOND_CARRIER_EXECUTION_TREATED_AS_AUTHORITY",
        "SECOND_CARRIER_EXECUTION_TREATED_AS_CURRENTNESS",
        "SECOND_CARRIER_EXECUTION_TREATED_AS_FINAL_COMPLETION",
        "SECOND_CARRIER_EXECUTION_TREATED_AS_RUNTIME",
        "SECOND_CARRIER_EXECUTION_TREATED_AS_CONTINUATION",
        "SECOND_CARRIER_EXECUTION_TREATED_AS_REUSABLE_PERMISSION",
        "SECOND_CARRIER_EXECUTION_TREATED_AS_FOLLOW_ON_WORK",
        "EXECUTION_OUTPUT_CREATED",
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
        "ARTIFACT_EXISTENCE_TREATED_AS_EXECUTION_AUTHORITY",
        "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_EXECUTION_AUTHORITY",
        "HIDDEN_REPO_STATE_USED_AS_EXECUTION_CONTENT",
        "HIDDEN_REPO_STATE_USED_AS_EXECUTION_AUTHORITY",
        "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
        "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENT_REPORT_ARTIFACT",
        "COMMAND_REPORT_LINEAGE_TREATED_AS_SOURCE",
        "COMMAND_REPORT_LINEAGE_TREATED_AS_AUTHORITY",
        "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENTNESS",
        "CONSUMED_REQUEST_REOPENED",
        "AUTHORIZATION_TOKEN_REUSED",
        "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_EXECUTION",
        "ARTIFACTS_MUTATED",
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "UNSUPPORTED_SECOND_CARRIER_EXECUTION_SCOPE",
    }
)

NON_CLAIM_BLOCK_CODE_BY_KEY = {
    "execution_output_created": "EXECUTION_OUTPUT_CREATED",
    "second_carrier_output_capture_created": "SECOND_CARRIER_OUTPUT_CAPTURE_CREATED",
    "second_carrier_result_created": "SECOND_CARRIER_RESULT_CREATED",
    "second_carrier_success_created": "SECOND_CARRIER_SUCCESS_CREATED",
    "external_result_created": "EXTERNAL_RESULT_CREATED",
    "cross_carrier_evidence_created": "CROSS_CARRIER_EVIDENCE_CREATED",
    "source_transfer_occurred": "SOURCE_TRANSFER_OCCURRED",
    "source_receipt_occurred": "SOURCE_RECEIPT_OCCURRED",
    "reception_authorization_created": "RECEPTION_AUTHORIZATION_CREATED",
    "second_carrier_execution_treated_as_output": (
        "SECOND_CARRIER_EXECUTION_TREATED_AS_OUTPUT"
    ),
    "second_carrier_execution_treated_as_output_capture": (
        "SECOND_CARRIER_EXECUTION_TREATED_AS_OUTPUT_CAPTURE"
    ),
    "second_carrier_execution_treated_as_result": (
        "SECOND_CARRIER_EXECUTION_TREATED_AS_RESULT"
    ),
    "second_carrier_execution_treated_as_success": (
        "SECOND_CARRIER_EXECUTION_TREATED_AS_SUCCESS"
    ),
    "second_carrier_execution_treated_as_external_result": (
        "SECOND_CARRIER_EXECUTION_TREATED_AS_EXTERNAL_RESULT"
    ),
    "second_carrier_execution_treated_as_cross_carrier_evidence": (
        "SECOND_CARRIER_EXECUTION_TREATED_AS_CROSS_CARRIER_EVIDENCE"
    ),
    "second_carrier_execution_treated_as_source_transfer": (
        "SECOND_CARRIER_EXECUTION_TREATED_AS_SOURCE_TRANSFER"
    ),
    "second_carrier_execution_treated_as_source_receipt": (
        "SECOND_CARRIER_EXECUTION_TREATED_AS_SOURCE_RECEIPT"
    ),
    "second_carrier_execution_treated_as_reception_authorization": (
        "SECOND_CARRIER_EXECUTION_TREATED_AS_RECEPTION_AUTHORIZATION"
    ),
    "second_carrier_execution_treated_as_source": (
        "SECOND_CARRIER_EXECUTION_TREATED_AS_SOURCE"
    ),
    "second_carrier_execution_treated_as_authority": (
        "SECOND_CARRIER_EXECUTION_TREATED_AS_AUTHORITY"
    ),
    "second_carrier_execution_treated_as_currentness": (
        "SECOND_CARRIER_EXECUTION_TREATED_AS_CURRENTNESS"
    ),
    "second_carrier_execution_treated_as_final_completion": (
        "SECOND_CARRIER_EXECUTION_TREATED_AS_FINAL_COMPLETION"
    ),
    "second_carrier_execution_treated_as_runtime": (
        "SECOND_CARRIER_EXECUTION_TREATED_AS_RUNTIME"
    ),
    "second_carrier_execution_treated_as_continuation": (
        "SECOND_CARRIER_EXECUTION_TREATED_AS_CONTINUATION"
    ),
    "second_carrier_execution_treated_as_reusable_permission": (
        "SECOND_CARRIER_EXECUTION_TREATED_AS_REUSABLE_PERMISSION"
    ),
    "second_carrier_execution_treated_as_follow_on_work": (
        "SECOND_CARRIER_EXECUTION_TREATED_AS_FOLLOW_ON_WORK"
    ),
    "receiving_carrier_treated_as_authority": "RECEIVING_CARRIER_TREATED_AS_AUTHORITY",
    "artifact_existence_treated_as_execution_authority": (
        "ARTIFACT_EXISTENCE_TREATED_AS_EXECUTION_AUTHORITY"
    ),
    "artifact_path_treated_as_currentness": "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "repo_local_availability_treated_as_execution_authority": (
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_EXECUTION_AUTHORITY"
    ),
    "hidden_repo_state_used_as_execution_content": (
        "HIDDEN_REPO_STATE_USED_AS_EXECUTION_CONTENT"
    ),
    "hidden_repo_state_used_as_execution_authority": (
        "HIDDEN_REPO_STATE_USED_AS_EXECUTION_AUTHORITY"
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
    "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
    "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
    "v1_repaired": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "v1_hidden": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "v1_claimed_passed": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
}

EXTRA_FORBIDDEN_FLAG_BLOCK_CODE_BY_KEY = {
    "second_carrier_execution_boundary_already_created_execution": (
        "SECOND_CARRIER_EXECUTION_BOUNDARY_ALREADY_CREATED_EXECUTION"
    ),
    "second_carrier_execution_boundary_already_created_execution_artifact": (
        "SECOND_CARRIER_EXECUTION_BOUNDARY_ALREADY_CREATED_EXECUTION_ARTIFACT"
    ),
    "second_carrier_execution_boundary_already_created_execution_output": (
        "SECOND_CARRIER_EXECUTION_BOUNDARY_ALREADY_CREATED_EXECUTION_OUTPUT"
    ),
    "second_carrier_execution_boundary_already_created_second_carrier_output_capture": (
        "SECOND_CARRIER_EXECUTION_BOUNDARY_ALREADY_CREATED_SECOND_CARRIER_OUTPUT_CAPTURE"
    ),
    "second_carrier_execution_boundary_already_created_second_carrier_result": (
        "SECOND_CARRIER_EXECUTION_BOUNDARY_ALREADY_CREATED_SECOND_CARRIER_RESULT"
    ),
    "second_carrier_execution_boundary_already_created_second_carrier_success": (
        "SECOND_CARRIER_EXECUTION_BOUNDARY_ALREADY_CREATED_SECOND_CARRIER_SUCCESS"
    ),
    "second_carrier_execution_boundary_created_external_result": (
        "SECOND_CARRIER_EXECUTION_BOUNDARY_CREATED_EXTERNAL_RESULT"
    ),
    "second_carrier_execution_boundary_created_cross_carrier_evidence": (
        "SECOND_CARRIER_EXECUTION_BOUNDARY_CREATED_CROSS_CARRIER_EVIDENCE"
    ),
    "second_carrier_execution_boundary_used_hidden_repo_state_as_execution_authority": (
        "SECOND_CARRIER_EXECUTION_BOUNDARY_USED_HIDDEN_REPO_STATE_AS_EXECUTION_AUTHORITY"
    ),
    "second_carrier_execution_boundary_treated_repo_local_availability_as_execution_authority": (
        "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_REPO_LOCAL_AVAILABILITY_AS_EXECUTION_AUTHORITY"
    ),
    "second_carrier_execution_boundary_treated_receiving_carrier_as_authority": (
        "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_RECEIVING_CARRIER_AS_AUTHORITY"
    ),
    "second_carrier_execution_boundary_raw_full_prior_artifact_body_returned": (
        "SECOND_CARRIER_EXECUTION_BOUNDARY_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY"
    ),
    "command_report_lineage_treated_as_current_report_artifact": (
        "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENT_REPORT_ARTIFACT"
    ),
    "command_report_lineage_treated_as_source": "COMMAND_REPORT_LINEAGE_TREATED_AS_SOURCE",
    "command_report_lineage_treated_as_authority": (
        "COMMAND_REPORT_LINEAGE_TREATED_AS_AUTHORITY"
    ),
    "command_report_lineage_treated_as_currentness": (
        "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENTNESS"
    ),
    "full_prior_artifact_body_emitted_outside_bounded_execution": (
        "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_EXECUTION"
    ),
}

POSTURE_TO_STATEMENT = {
    "second_carrier_execution_spec_only_posture": "second_carrier_execution_recorded",
    "one_bounded_second_carrier_execution_posture": (
        "bounded_second_carrier_execution_recorded"
    ),
    "second_carrier_execution_boundary_basis_preserved_posture": (
        "second_carrier_execution_boundary_basis_preserved"
    ),
    "second_carrier_receipt_basis_preserved_posture": (
        "second_carrier_receipt_basis_preserved"
    ),
    "receipt_artifact_basis_preserved_posture": "receipt_artifact_basis_preserved",
    "execution_recorded_bounded_posture": "execution_recorded_bounded",
    "execution_artifact_recorded_or_bounded_posture": (
        "execution_artifact_recorded_or_bounded"
    ),
    "execution_output_not_created_posture": "execution_output_not_created",
    "execution_not_output_capture_posture": "execution_not_output_capture",
    "execution_not_result_posture": "execution_not_result",
    "execution_not_success_posture": "execution_not_success",
    "execution_not_external_result_posture": "execution_not_external_result",
    "execution_not_cross_carrier_evidence_posture": (
        "execution_not_cross_carrier_evidence"
    ),
    "execution_not_source_transfer_posture": "execution_not_source_transfer",
    "execution_not_source_receipt_posture": "execution_not_source_receipt",
    "execution_not_reception_authorization_posture": (
        "execution_not_reception_authorization"
    ),
    "second_carrier_output_capture_not_created_posture": (
        "second_carrier_output_capture_not_created"
    ),
    "second_carrier_result_not_created_posture": "second_carrier_result_not_created",
    "second_carrier_success_not_created_posture": "second_carrier_success_not_created",
    "external_result_not_created_posture": "external_result_not_created",
    "cross_carrier_evidence_not_created_posture": "cross_carrier_evidence_not_created",
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
    "repo_local_availability_not_execution_authority_posture": (
        "repo_local_availability_not_execution_authority"
    ),
    "selected_basis_reference_shape_posture": "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned_posture": (
        "raw_full_prior_artifact_body_not_returned"
    ),
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
    "unlisted_file_dependency",
}
REDACTED_REFERENCE_VALUE = "[bounded-reference-omitted-raw-or-hidden-state]"

WHAT_REMAINS_OPEN = (
    "second-carrier execution test",
    "second-carrier execution live artifact",
    "second-carrier execution terminal summary, if needed",
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


def _is_mapping(value: Any) -> bool:
    return hasattr(value, "items") and callable(value.items)


def _is_sequence(value: Any) -> bool:
    return isinstance(value, (list, tuple, set, frozenset))


def _json_safe(value: Any) -> Any:
    if _is_mapping(value):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, (set, frozenset, tuple)):
        return [_json_safe(item) for item in sorted(value, key=lambda item: str(item))]
    if isinstance(value, list):
        return [_json_safe(item) for item in value]
    if value is None or isinstance(value, (str, int, float, bool)):
        return copy.deepcopy(value)
    return str(value)


def _sensitive_string(value: str) -> bool:
    markers = (
        "MUST_NOT_RETURN",
        "HOSTILE_",
        "RAW_SECOND_CARRIER_EXECUTION_BODY",
        "RAW_SECOND_CARRIER_EXECUTION_BOUNDARY_BODY",
        "RAW_SECOND_CARRIER_RECEIPT_BODY",
        "RAW_PACKET_TRANSFER_BODY",
        "HIDDEN_REPO_STATE",
    )
    return any(marker in value for marker in markers)


def _sanitize_reference(value: Any) -> Any:
    if _is_mapping(value):
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
    if isinstance(value, (set, frozenset)):
        return [_sanitize_reference(item) for item in sorted(value, key=lambda item: str(item))]
    if isinstance(value, str) and _sensitive_string(value):
        return REDACTED_REFERENCE_VALUE
    return _json_safe(value)


def _to_bool(value: Any, default: bool | None = None) -> bool | None:
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    if isinstance(value, int) and value in (0, 1):
        return bool(value)
    if isinstance(value, str):
        lowered = value.strip().lower()
        if lowered in {"true", "yes", "1"}:
            return True
        if lowered in {"false", "no", "0"}:
            return False
    if _is_mapping(value):
        for key in ("value", "declared", "preserved", "recorded", "posture"):
            if key in value:
                converted = _to_bool(value[key], None)
                if converted is not None:
                    return converted
    return default


def _to_int(value: Any, default: int | None = None) -> int | None:
    if value is None or isinstance(value, bool):
        return default
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            return default
    return default


def _find_key(value: Any, key_names: set[str], depth: int = 0) -> Any:
    if depth > 7:
        return None
    if _is_mapping(value):
        for key, item in value.items():
            if str(key) in key_names:
                return item
        for item in value.values():
            found = _find_key(item, key_names, depth + 1)
            if found is not None:
                return found
    elif _is_sequence(value):
        for item in value:
            found = _find_key(item, key_names, depth + 1)
            if found is not None:
                return found
    return None


def _extract_value(
    request: Mapping[str, Any],
    top_level_keys: tuple[str, ...],
    basis_keys: tuple[str, ...] = (),
) -> Any:
    for key in top_level_keys:
        if key in request:
            return request[key]
    search_keys = set(top_level_keys)
    for basis_key in basis_keys:
        if basis_key in request:
            found = _find_key(request[basis_key], search_keys)
            if found is not None:
                return found
    return None


def _declared(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    if _is_mapping(value):
        if "declared" in value:
            return _to_bool(value["declared"], False) is True
        return bool(value)
    if _is_sequence(value):
        return len(value) > 0
    if isinstance(value, str):
        return bool(value.strip())
    return True


def _basis_declared(request: Mapping[str, Any], key: str) -> bool:
    return key in request and _declared(request.get(key))


def _posture_declared(request: Mapping[str, Any], key: str) -> bool:
    return key in request and _declared(request.get(key))


def _scope_values(scope_value: Any) -> tuple[str, ...]:
    if isinstance(scope_value, str):
        return (scope_value,)
    if _is_mapping(scope_value):
        if "scope" in scope_value:
            return _scope_values(scope_value["scope"])
        if "values" in scope_value:
            return _scope_values(scope_value["values"])
        return tuple(str(key) for key, value in scope_value.items() if _to_bool(value, False))
    if _is_sequence(scope_value):
        return tuple(str(item) for item in scope_value)
    return ()


def _check_record(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    block_code: str,
) -> dict[str, Any]:
    code = None if passed else block_code
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": _sanitize_reference(expected_posture),
        "actual_posture": _sanitize_reference(actual_posture),
        "block_code": code,
        "failure_code": code,
    }


def _check_count(checks: Sequence[Mapping[str, Any]], passed: bool) -> int:
    return sum(1 for check in checks if _to_bool(check.get("passed"), False) is passed)


def _block_from_checks(checks: Sequence[Mapping[str, Any]]) -> dict[str, Any] | None:
    for check in checks:
        if _to_bool(check.get("passed"), False) is False:
            code = check.get("block_code") or check.get("failure_code")
            return {
                "blocked": True,
                "block_code": code,
                "block_reason": check.get("check_name"),
            }
    return None


def _build_metadata(request: Mapping[str, Any]) -> dict[str, Any]:
    request_id = str(
        request.get(
            "second_carrier_execution_request_id",
            "portable_source_body_verification_second_carrier_execution_reference_review_001",
        )
    )
    return {
        "portable_source_body_verification_second_carrier_execution_result_id": request_id,
        "portable_source_body_verification_second_carrier_execution_request_id": request_id,
        "portable_source_body_verification_second_carrier_execution_result_type": (
            RESULT_TYPE
        ),
        "portable_source_body_verification_second_carrier_execution_result_version": (
            RESULT_VERSION
        ),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "resolver_module": RESOLVER_MODULE,
    }


def _build_declared_question(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "second_carrier_execution_request_id": request.get(
            "second_carrier_execution_request_id"
        ),
        "second_carrier_execution_question": request.get("second_carrier_execution_question"),
        "second_carrier_execution_intent": request.get("second_carrier_execution_intent"),
        "core_question": CORE_QUESTION,
    }


def _build_basis_section(request: Mapping[str, Any], key: str) -> dict[str, Any]:
    basis = request.get(key)
    section: dict[str, Any] = {
        "basis_key": key,
        "basis_declared": _basis_declared(request, key),
        "reference_shape_preserved": True,
        "selected_reference": _sanitize_reference(basis),
        "basis_remains_basis_only": True,
        "raw_full_prior_artifact_body_returned": False,
        "prior_artifacts_mutated": False,
    }
    if key == "selected_second_carrier_execution_boundary_basis":
        section.update(
            {
                "selected_second_carrier_execution_boundary_result_id": request.get(
                    "selected_second_carrier_execution_boundary_result_id"
                ),
                "selected_second_carrier_execution_boundary_result_path": request.get(
                    "selected_second_carrier_execution_boundary_result_path"
                ),
                "selected_second_carrier_execution_boundary_result_outcome": (
                    _extract_value(
                        request,
                        (
                            "selected_second_carrier_execution_boundary_result_outcome",
                            "outcome",
                            "result_outcome",
                        ),
                        (key,),
                    )
                ),
                "selected_second_carrier_execution_boundary_result_version": (
                    _extract_value(
                        request,
                        (
                            "selected_second_carrier_execution_boundary_result_version",
                            "result_version",
                            "portable_source_body_verification_second_carrier_execution_boundary_result_version",
                        ),
                        (key,),
                    )
                ),
                "selected_second_carrier_execution_boundary_failed_check_count": (
                    _extract_value(
                        request,
                        (
                            "selected_second_carrier_execution_boundary_failed_check_count",
                            "failed_check_count",
                        ),
                        (key,),
                    )
                ),
                "selected_second_carrier_execution_boundary_declared_future_execution_step": (
                    _extract_value(
                        request,
                        (
                            "selected_second_carrier_execution_boundary_declared_future_execution_step",
                            "one_future_second_carrier_execution_step_declared",
                        ),
                        (key,),
                    )
                ),
            }
        )
    if key == "selected_second_carrier_receipt_basis":
        section.update(
            {
                "selected_second_carrier_receipt_result_id": request.get(
                    "selected_second_carrier_receipt_result_id"
                ),
                "selected_second_carrier_receipt_result_path": request.get(
                    "selected_second_carrier_receipt_result_path"
                ),
                "selected_second_carrier_receipt_result_outcome": _extract_value(
                    request,
                    (
                        "selected_second_carrier_receipt_result_outcome",
                        "outcome",
                        "result_outcome",
                    ),
                    (key,),
                ),
                "selected_second_carrier_receipt_failed_check_count": _extract_value(
                    request,
                    (
                        "selected_second_carrier_receipt_failed_check_count",
                        "failed_check_count",
                    ),
                    (key,),
                ),
                "selected_second_carrier_receipt_bounded_receipt_recorded": (
                    _extract_value(
                        request,
                        (
                            "selected_second_carrier_receipt_bounded_receipt_recorded",
                            "bounded_second_carrier_receipt_recorded",
                            "bounded_receipt_recorded",
                            "receipt_recorded_bounded",
                        ),
                        (key,),
                    )
                ),
                "selected_second_carrier_receipt_receipt_not_execution": _extract_value(
                    request,
                    (
                        "selected_second_carrier_receipt_receipt_not_execution",
                        "receipt_not_execution",
                    ),
                    (key,),
                ),
            }
        )
    return _json_safe(section)


def _build_statement(outcome: str) -> dict[str, bool]:
    statement = {key: False for key in ALLOWED_TRUE_RECORDED_FIELDS}
    if outcome == OUTCOME_RECORDED:
        statement.update({key: True for key in ALLOWED_TRUE_RECORDED_FIELDS})
    return statement


def _build_posture_section(
    request: Mapping[str, Any],
    key: str,
    statement: Mapping[str, bool],
) -> dict[str, Any]:
    statement_key = POSTURE_TO_STATEMENT.get(key)
    return {
        "posture_key": key,
        "declared": _posture_declared(request, key),
        "preserved": bool(statement.get(statement_key, False)) if statement_key else False,
        "statement_key": statement_key,
        "source_value": _sanitize_reference(request.get(key)),
    }


def _build_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _build_non_meaning() -> dict[str, bool]:
    return {
        "execution_output_exists": False,
        "second_carrier_output_capture_exists": False,
        "second_carrier_result_exists": False,
        "second_carrier_success_exists": False,
        "external_result_exists": False,
        "cross_carrier_evidence_exists": False,
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
        "execution_became_output": False,
        "execution_became_result": False,
        "execution_became_success": False,
        "execution_became_external_result": False,
        "execution_became_cross_carrier_proof": False,
        "execution_became_source_transfer": False,
        "execution_became_source_receipt": False,
        "execution_became_reception_authorization": False,
        "execution_became_source": False,
        "execution_became_authority": False,
        "execution_became_currentness": False,
        "receiving_carrier_became_authority": False,
        "transferred_packet_became_source": False,
        "transferred_packet_became_authority": False,
        "transferred_packet_became_currentness": False,
        "artifact_existence_became_execution_authority": False,
        "artifact_path_became_currentness": False,
        "repo_local_availability_became_execution_authority": False,
        "hidden_repo_state_became_execution_authority": False,
        "v1_packet_emission_boundary_repaired": False,
        "v1_packet_emission_boundary_hidden": False,
        "v1_packet_emission_boundary_erased": False,
        "v1_packet_emission_boundary_claimed_passed": False,
    }


def _build_additional_basis(outcome: str, request: Mapping[str, Any]) -> dict[str, Any]:
    if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        return {
            "additional_basis_required": True,
            "missing_or_unclear_basis": _sanitize_reference(
                request.get("additional_basis_context")
            ),
            "missing_basis_scheduled": False,
            "missing_basis_authorized": False,
            "missing_basis_executed": False,
        }
    return {
        "additional_basis_required": False,
        "missing_or_unclear_basis": [],
        "missing_basis_scheduled": False,
        "missing_basis_authorized": False,
        "missing_basis_executed": False,
    }


def _build_not_recorded_basis(outcome: str, request: Mapping[str, Any]) -> dict[str, Any]:
    if outcome == OUTCOME_NOT_RECORDED:
        return {
            "not_recorded": True,
            "reason": _sanitize_reference(
                request.get(
                    "not_recorded_basis",
                    "second-carrier execution not recorded by declared intent",
                )
            ),
            "mutation_performed": False,
            "next_work_authorized": False,
        }
    return {
        "not_recorded": False,
        "reason": None,
        "mutation_performed": False,
        "next_work_authorized": False,
    }


def _build_what_remains_open() -> dict[str, Any]:
    return {
        "open_items": list(WHAT_REMAINS_OPEN),
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }


def _request_non_claim_value(request: Mapping[str, Any], key: str) -> tuple[bool, Any]:
    declared_non_claims = request.get("declared_non_claims")
    if _is_mapping(declared_non_claims) and key in declared_non_claims:
        return True, declared_non_claims[key]
    if key in request:
        return True, request[key]
    return False, None


def _forbidden_request_flag(request: Mapping[str, Any], key: str) -> bool:
    return _to_bool(_extract_value(request, (key,), SELECTED_BASIS_KEYS), False) is True


def _false_or_safe_inverse(
    request: Mapping[str, Any],
    false_keys: tuple[str, ...],
    inverse_true_keys: tuple[str, ...],
    basis_keys: tuple[str, ...],
) -> bool:
    actual_false = _to_bool(_extract_value(request, false_keys, basis_keys), None)
    if actual_false is not None:
        return actual_false is False
    actual_inverse = _to_bool(_extract_value(request, inverse_true_keys, basis_keys), None)
    return actual_inverse is True


def _truthy_basis_value(
    request: Mapping[str, Any],
    keys: tuple[str, ...],
    basis_keys: tuple[str, ...],
) -> bool:
    return _to_bool(_extract_value(request, keys, basis_keys), None) is True


def _add_basis_presence_checks(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    basis_presence_checks = (
        (
            "second-carrier execution boundary terminal summary basis declared",
            "selected_second_carrier_execution_boundary_terminal_summary_basis",
            "SECOND_CARRIER_EXECUTION_BOUNDARY_TERMINAL_SUMMARY_BASIS_MISSING",
        ),
        (
            "second-carrier receipt terminal summary basis declared",
            "selected_second_carrier_receipt_terminal_summary_basis",
            "SECOND_CARRIER_RECEIPT_TERMINAL_SUMMARY_BASIS_MISSING",
        ),
        (
            "second-carrier receipt boundary basis declared",
            "selected_second_carrier_receipt_boundary_basis",
            "SECOND_CARRIER_RECEIPT_BOUNDARY_BASIS_MISSING",
        ),
        ("packet transfer basis declared", "selected_packet_transfer_basis", "PACKET_TRANSFER_BASIS_MISSING"),
        (
            "packet-transfer-boundary basis declared",
            "selected_packet_transfer_boundary_basis",
            "PACKET_TRANSFER_BOUNDARY_BASIS_MISSING",
        ),
        ("packet emission basis declared", "selected_packet_emission_basis", "PACKET_EMISSION_BASIS_MISSING"),
        (
            "packet-emission-boundary-v2 basis declared",
            "selected_packet_emission_boundary_v2_basis",
            "PACKET_EMISSION_BOUNDARY_V2_BASIS_MISSING",
        ),
        (
            "packet-emission-boundary-v1 predecessor failure basis declared",
            "selected_packet_emission_boundary_v1_predecessor_failure_basis",
            "PACKET_EMISSION_BOUNDARY_V1_PREDECESSOR_FAILURE_BASIS_MISSING",
        ),
        ("packet artifact basis declared", "selected_packet_artifact_basis", "PACKET_ARTIFACT_BASIS_MISSING"),
        ("packet boundary basis declared", "selected_packet_boundary_basis", "PACKET_BOUNDARY_BASIS_MISSING"),
        ("command success basis declared", "selected_command_success_basis", "COMMAND_SUCCESS_BASIS_MISSING"),
        ("command result v2 basis declared", "selected_command_result_v2_basis", "COMMAND_RESULT_V2_BASIS_MISSING"),
        ("output capture v2 basis declared", "selected_output_capture_v2_basis", "OUTPUT_CAPTURE_V2_BASIS_MISSING"),
        (
            "command output/report artifact basis declared",
            "selected_command_output_report_artifact_basis",
            "COMMAND_OUTPUT_REPORT_ARTIFACT_BASIS_MISSING",
        ),
        ("original-carrier execution trace audit-only basis declared", "selected_command_execution_basis", "COMMAND_EXECUTION_BASIS_MISSING"),
        ("command report lineage basis declared", "selected_command_report_lineage_basis", "COMMAND_REPORT_LINEAGE_BASIS_MISSING"),
        ("predecessor failure evidence basis declared", "selected_predecessor_failure_basis", "PREDECESSOR_FAILURE_BASIS_MISSING"),
        ("evidence manifest basis declared", "selected_evidence_manifest_basis", "EVIDENCE_MANIFEST_BASIS_MISSING"),
        ("artifact containment basis declared", "selected_artifact_containment_basis", "ARTIFACT_CONTAINMENT_BASIS_MISSING"),
        ("portable verification basis declared", "selected_portable_verification_basis", "PORTABLE_VERIFICATION_BASIS_MISSING"),
    )
    for name, key, code in basis_presence_checks:
        checks.append(
            _check_record(name, _basis_declared(request, key), "basis declared", request.get(key), code)
        )


def _build_checks(
    request: Mapping[str, Any],
    malformed_code: str | None = None,
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    def add(name: str, passed: bool, expected: Any, actual: Any, code: str) -> None:
        checks.append(_check_record(name, passed, expected, actual, code))

    if malformed_code is not None:
        add(
            "declared second-carrier execution request is a mapping",
            False,
            "mapping request",
            "malformed or missing request",
            malformed_code,
        )
        return checks

    question = request.get("second_carrier_execution_question")
    intent = request.get("second_carrier_execution_intent")
    scope = _scope_values(request.get("second_carrier_execution_scope"))

    add(
        "second-carrier execution question declared",
        question == CORE_QUESTION,
        CORE_QUESTION,
        question,
        "SECOND_CARRIER_EXECUTION_QUESTION_UNDECLARED",
    )
    add(
        "second-carrier execution intent supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "SECOND_CARRIER_EXECUTION_INTENT_UNSUPPORTED",
    )
    if intent == INTENT_BLOCK:
        add(
            "explicit second-carrier execution block requested",
            False,
            "non-blocking second-carrier execution intent",
            intent,
            "SECOND_CARRIER_EXECUTION_BLOCK_REQUESTED",
        )

    unsupported_scope = sorted(set(scope) - set(SUPPORTED_SECOND_CARRIER_EXECUTION_SCOPE))
    add(
        "second-carrier execution scope supported",
        bool(scope) and not unsupported_scope,
        sorted(SUPPORTED_SECOND_CARRIER_EXECUTION_SCOPE),
        scope,
        "UNSUPPORTED_SECOND_CARRIER_EXECUTION_SCOPE",
    )

    boundary_basis_key = "selected_second_carrier_execution_boundary_basis"
    add(
        "second-carrier execution boundary basis declared",
        _basis_declared(request, boundary_basis_key),
        "selected second-carrier execution boundary basis declared",
        request.get(boundary_basis_key),
        "SECOND_CARRIER_EXECUTION_BOUNDARY_BASIS_MISSING",
    )
    boundary_outcome = _extract_value(
        request,
        (
            "selected_second_carrier_execution_boundary_result_outcome",
            "outcome",
            "result_outcome",
        ),
        (boundary_basis_key,),
    )
    add(
        "second-carrier execution boundary outcome recorded",
        boundary_outcome == SECOND_CARRIER_EXECUTION_BOUNDARY_RECORDED,
        SECOND_CARRIER_EXECUTION_BOUNDARY_RECORDED,
        boundary_outcome,
        "SECOND_CARRIER_EXECUTION_BOUNDARY_NOT_RECORDED",
    )
    boundary_version = _extract_value(
        request,
        (
            "selected_second_carrier_execution_boundary_result_version",
            "result_version",
            "portable_source_body_verification_second_carrier_execution_boundary_result_version",
        ),
        (boundary_basis_key,),
    )
    add(
        "second-carrier execution boundary version 0.1.0",
        boundary_version == SECOND_CARRIER_EXECUTION_BOUNDARY_RESULT_VERSION,
        SECOND_CARRIER_EXECUTION_BOUNDARY_RESULT_VERSION,
        boundary_version,
        "SECOND_CARRIER_EXECUTION_BOUNDARY_VERSION_NOT_0_1_0",
    )
    boundary_failed_count = _to_int(
        _extract_value(
            request,
            (
                "selected_second_carrier_execution_boundary_failed_check_count",
                "failed_check_count",
            ),
            (boundary_basis_key,),
        )
    )
    add(
        "second-carrier execution boundary failed checks zero",
        boundary_failed_count == 0,
        0,
        boundary_failed_count,
        "SECOND_CARRIER_EXECUTION_BOUNDARY_FAILED_CHECKS_PRESENT",
    )
    add(
        "second-carrier execution boundary declared future execution step",
        _truthy_basis_value(
            request,
            (
                "selected_second_carrier_execution_boundary_declared_future_execution_step",
                "one_future_second_carrier_execution_step_declared",
            ),
            (boundary_basis_key,),
        ),
        True,
        _extract_value(
            request,
            (
                "selected_second_carrier_execution_boundary_declared_future_execution_step",
                "one_future_second_carrier_execution_step_declared",
            ),
            (boundary_basis_key,),
        ),
        "SECOND_CARRIER_EXECUTION_BOUNDARY_DID_NOT_DECLARE_FUTURE_EXECUTION_STEP",
    )

    boundary_false_expectations = (
        (
            "second-carrier execution boundary did not already create execution",
            (
                "selected_second_carrier_execution_boundary_already_created_execution",
                "second_carrier_execution_created",
            ),
            ("execution_not_created",),
            "SECOND_CARRIER_EXECUTION_BOUNDARY_ALREADY_CREATED_EXECUTION",
        ),
        (
            "second-carrier execution boundary did not already create execution artifact",
            (
                "selected_second_carrier_execution_boundary_already_created_execution_artifact",
                "execution_artifact_created",
            ),
            ("execution_artifact_not_created",),
            "SECOND_CARRIER_EXECUTION_BOUNDARY_ALREADY_CREATED_EXECUTION_ARTIFACT",
        ),
        (
            "second-carrier execution boundary did not already create execution output",
            (
                "selected_second_carrier_execution_boundary_already_created_execution_output",
                "execution_output_created",
            ),
            ("execution_output_not_created",),
            "SECOND_CARRIER_EXECUTION_BOUNDARY_ALREADY_CREATED_EXECUTION_OUTPUT",
        ),
        (
            "second-carrier execution boundary did not already create second-carrier output capture",
            (
                "selected_second_carrier_execution_boundary_already_created_second_carrier_output_capture",
                "second_carrier_output_capture_created",
            ),
            ("second_carrier_output_capture_not_created",),
            "SECOND_CARRIER_EXECUTION_BOUNDARY_ALREADY_CREATED_SECOND_CARRIER_OUTPUT_CAPTURE",
        ),
        (
            "second-carrier execution boundary did not already create second-carrier result",
            (
                "selected_second_carrier_execution_boundary_already_created_second_carrier_result",
                "second_carrier_result_created",
            ),
            ("second_carrier_result_not_created",),
            "SECOND_CARRIER_EXECUTION_BOUNDARY_ALREADY_CREATED_SECOND_CARRIER_RESULT",
        ),
        (
            "second-carrier execution boundary did not already create second-carrier success",
            (
                "selected_second_carrier_execution_boundary_already_created_second_carrier_success",
                "second_carrier_success_created",
            ),
            ("second_carrier_success_not_created",),
            "SECOND_CARRIER_EXECUTION_BOUNDARY_ALREADY_CREATED_SECOND_CARRIER_SUCCESS",
        ),
        (
            "second-carrier execution boundary did not create external result",
            (
                "selected_second_carrier_execution_boundary_created_external_result",
                "external_result_created",
            ),
            ("external_result_not_created",),
            "SECOND_CARRIER_EXECUTION_BOUNDARY_CREATED_EXTERNAL_RESULT",
        ),
        (
            "second-carrier execution boundary did not create cross-carrier evidence",
            (
                "selected_second_carrier_execution_boundary_created_cross_carrier_evidence",
                "cross_carrier_evidence_created",
            ),
            ("cross_carrier_evidence_not_created",),
            "SECOND_CARRIER_EXECUTION_BOUNDARY_CREATED_CROSS_CARRIER_EVIDENCE",
        ),
        (
            "second-carrier execution boundary did not use hidden repo state as execution authority",
            (
                "selected_second_carrier_execution_boundary_used_hidden_repo_state_as_execution_authority",
                "hidden_repo_state_used_as_execution_authority",
            ),
            ("hidden_repo_state_not_used_as_execution_authority",),
            "SECOND_CARRIER_EXECUTION_BOUNDARY_USED_HIDDEN_REPO_STATE_AS_EXECUTION_AUTHORITY",
        ),
        (
            "second-carrier execution boundary did not treat repo-local availability as execution authority",
            (
                "selected_second_carrier_execution_boundary_treated_repo_local_availability_as_execution_authority",
                "repo_local_availability_treated_as_execution_authority",
            ),
            ("repo_local_availability_not_execution_authority",),
            "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_REPO_LOCAL_AVAILABILITY_AS_EXECUTION_AUTHORITY",
        ),
        (
            "second-carrier execution boundary did not treat receiving carrier as authority",
            (
                "selected_second_carrier_execution_boundary_treated_receiving_carrier_as_authority",
                "receiving_carrier_treated_as_authority",
            ),
            ("receiving_carrier_not_authority",),
            "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_RECEIVING_CARRIER_AS_AUTHORITY",
        ),
        (
            "second-carrier execution boundary did not return raw full prior artifact body",
            (
                "selected_second_carrier_execution_boundary_raw_full_prior_artifact_body_returned",
                "raw_full_prior_artifact_body_returned",
            ),
            ("raw_full_prior_artifact_body_not_returned",),
            "SECOND_CARRIER_EXECUTION_BOUNDARY_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY",
        ),
    )
    for name, false_keys, inverse_true_keys, code in boundary_false_expectations:
        add(
            name,
            _false_or_safe_inverse(request, false_keys, inverse_true_keys, (boundary_basis_key,)),
            "false posture or explicit safe inverse",
            {
                "forbidden": _extract_value(request, false_keys, (boundary_basis_key,)),
                "safe_inverse": _extract_value(
                    request, inverse_true_keys, (boundary_basis_key,)
                ),
            },
            code,
        )

    receipt_basis_key = "selected_second_carrier_receipt_basis"
    add(
        "second-carrier receipt basis declared",
        _basis_declared(request, receipt_basis_key),
        "selected second-carrier receipt basis declared",
        request.get(receipt_basis_key),
        "SECOND_CARRIER_RECEIPT_BASIS_MISSING",
    )
    receipt_outcome = _extract_value(
        request,
        ("selected_second_carrier_receipt_result_outcome", "outcome", "result_outcome"),
        (receipt_basis_key,),
    )
    add(
        "second-carrier receipt outcome recorded",
        receipt_outcome == SECOND_CARRIER_RECEIPT_RECORDED,
        SECOND_CARRIER_RECEIPT_RECORDED,
        receipt_outcome,
        "SECOND_CARRIER_RECEIPT_NOT_RECORDED",
    )
    receipt_failed_count = _to_int(
        _extract_value(
            request,
            ("selected_second_carrier_receipt_failed_check_count", "failed_check_count"),
            (receipt_basis_key,),
        )
    )
    add(
        "second-carrier receipt failed checks zero",
        receipt_failed_count == 0,
        0,
        receipt_failed_count,
        "SECOND_CARRIER_RECEIPT_FAILED_CHECKS_PRESENT",
    )
    add(
        "second-carrier receipt recorded bounded receipt",
        _truthy_basis_value(
            request,
            (
                "selected_second_carrier_receipt_bounded_receipt_recorded",
                "bounded_second_carrier_receipt_recorded",
                "bounded_receipt_recorded",
                "receipt_recorded_bounded",
            ),
            (receipt_basis_key,),
        ),
        True,
        _extract_value(
            request,
            (
                "selected_second_carrier_receipt_bounded_receipt_recorded",
                "bounded_second_carrier_receipt_recorded",
                "bounded_receipt_recorded",
                "receipt_recorded_bounded",
            ),
            (receipt_basis_key,),
        ),
        "SECOND_CARRIER_RECEIPT_DID_NOT_RECORD_BOUNDED_RECEIPT",
    )
    add(
        "second-carrier receipt records receipt not execution",
        _truthy_basis_value(
            request,
            (
                "selected_second_carrier_receipt_receipt_not_execution",
                "receipt_not_execution",
            ),
            (receipt_basis_key,),
        ),
        True,
        _extract_value(
            request,
            (
                "selected_second_carrier_receipt_receipt_not_execution",
                "receipt_not_execution",
            ),
            (receipt_basis_key,),
        ),
        "SECOND_CARRIER_RECEIPT_TREATED_RECEIPT_AS_EXECUTION",
    )

    _add_basis_presence_checks(request, checks)

    audit_only = _to_bool(
        _extract_value(
            request,
            ("original_carrier_execution_trace_audit_only", "execution_trace_audit_only"),
            ("selected_command_execution_basis",),
        ),
        True,
    )
    add(
        "original-carrier execution trace remains audit-only",
        audit_only is True,
        True,
        audit_only,
        "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    )

    lineage_false_expectations = (
        (
            "predecessor failure evidence visible and unrepaired",
            "v1_repaired",
            "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        ),
        (
            "predecessor failure evidence not hidden",
            "v1_hidden",
            "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        ),
        (
            "predecessor failure evidence not claimed passed",
            "v1_claimed_passed",
            "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        ),
        (
            "command report lineage not current report artifact",
            "command_report_lineage_treated_as_current_report_artifact",
            "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENT_REPORT_ARTIFACT",
        ),
        (
            "command report lineage not source",
            "command_report_lineage_treated_as_source",
            "COMMAND_REPORT_LINEAGE_TREATED_AS_SOURCE",
        ),
        (
            "command report lineage not authority",
            "command_report_lineage_treated_as_authority",
            "COMMAND_REPORT_LINEAGE_TREATED_AS_AUTHORITY",
        ),
        (
            "command report lineage not currentness",
            "command_report_lineage_treated_as_currentness",
            "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENTNESS",
        ),
    )
    for name, key, code in lineage_false_expectations:
        actual = _to_bool(
            _extract_value(
                request,
                (key,),
                (
                    "selected_command_report_lineage_basis",
                    "selected_predecessor_failure_basis",
                    "selected_packet_emission_boundary_v1_predecessor_failure_basis",
                ),
            ),
            False,
        )
        add(name, actual is False, False, actual, code)

    for posture_key in POSTURE_KEYS:
        add(
            f"{posture_key} declared",
            _posture_declared(request, posture_key),
            "posture declared",
            request.get(posture_key),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )

    hidden_authority_blocked = _to_bool(
        request.get("hidden_repo_state_not_used_as_execution_authority"), True
    )
    add(
        "hidden repo state not used as execution authority",
        hidden_authority_blocked is True,
        True,
        hidden_authority_blocked,
        "HIDDEN_REPO_STATE_USED_AS_EXECUTION_AUTHORITY",
    )
    reference_shape = _to_bool(request.get("reference_shaped_input_posture"), True)
    add(
        "selected basis reference-shaped",
        reference_shape is True,
        True,
        reference_shape,
        "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    )
    raw_full_body_emitted = _to_bool(
        request.get("full_prior_artifact_body_emitted_outside_bounded_execution"),
        False,
    )
    add(
        "full prior artifact body not emitted outside bounded execution posture",
        raw_full_body_emitted is False,
        False,
        raw_full_body_emitted,
        "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_EXECUTION",
    )
    authorization_reuse_blocked = _to_bool(
        request.get("authorization_token_reuse_blocked"), True
    )
    add(
        "authorization token reuse remains blocked",
        authorization_reuse_blocked is True,
        True,
        authorization_reuse_blocked,
        "AUTHORIZATION_TOKEN_REUSED",
    )
    consumed_token_closed = _to_bool(
        request.get("consumed_request_token_remains_closed"), True
    )
    add(
        "consumed request token remains closed",
        consumed_token_closed is True,
        True,
        consumed_token_closed,
        "CONSUMED_REQUEST_REOPENED",
    )

    for key, code in NON_CLAIM_BLOCK_CODE_BY_KEY.items():
        actual = _forbidden_request_flag(request, key)
        add(f"forbidden flag not true: {key}", actual is False, False, actual, code)

    for key, code in EXTRA_FORBIDDEN_FLAG_BLOCK_CODE_BY_KEY.items():
        actual = _forbidden_request_flag(request, key)
        add(f"extra forbidden flag not true: {key}", actual is False, False, actual, code)

    declared_non_claims = request.get("declared_non_claims")
    for key in REQUIRED_FALSE_NON_CLAIMS:
        declared, actual = _request_non_claim_value(request, key)
        converted = _to_bool(actual, None)
        code = NON_CLAIM_BLOCK_CODE_BY_KEY.get(key, "NON_CLAIM_MISSING_OR_FLIPPED")
        add(
            f"required non-claim false: {key}",
            declared and converted is False,
            {key: False},
            {key: actual, "declared_non_claims_present": _is_mapping(declared_non_claims)},
            code if declared else "NON_CLAIM_MISSING_OR_FLIPPED",
        )

    return checks


def _resolve_outcome(request: Mapping[str, Any], checks: Sequence[Mapping[str, Any]]) -> str:
    if any(_to_bool(check.get("passed"), False) is False for check in checks):
        return OUTCOME_BLOCKED
    requested = request.get("requested_second_carrier_execution_outcome")
    if requested == OUTCOME_REQUIRES_ADDITIONAL_BASIS or request.get("additional_basis_context"):
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS
    if requested == OUTCOME_NOT_RECORDED or request.get("not_recorded_basis"):
        return OUTCOME_NOT_RECORDED
    if request.get("second_carrier_execution_intent") == INTENT_DO_NOT_RECORD:
        return OUTCOME_NOT_RECORDED
    return OUTCOME_RECORDED


def _build_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    outcome: str,
) -> dict[str, Any]:
    statement = _build_statement(outcome)
    result: dict[str, Any] = {
        "portable_source_body_verification_second_carrier_execution_metadata": (
            _build_metadata(request)
        ),
        "declared_second_carrier_execution_question": _build_declared_question(request),
    }
    for key in SELECTED_BASIS_KEYS:
        result[key] = _build_basis_section(request, key)
    for key in POSTURE_KEYS:
        result[key] = _build_posture_section(request, key, statement)

    scope = _scope_values(request.get("second_carrier_execution_scope"))
    result.update(
        {
            "second_carrier_execution_scope": {
                "supported_scope": sorted(SUPPORTED_SECOND_CARRIER_EXECUTION_SCOPE),
                "declared_scope": list(scope),
                "unsupported_scope": sorted(
                    set(scope) - set(SUPPORTED_SECOND_CARRIER_EXECUTION_SCOPE)
                ),
            },
            "second_carrier_execution_checks": checks,
            "second_carrier_execution_statement": statement,
            "second_carrier_execution_non_meaning": _build_non_meaning(),
            "additional_basis_required": _build_additional_basis(outcome, request),
            "not_recorded_basis": _build_not_recorded_basis(outcome, request),
            "what_remains_open": _build_what_remains_open(),
            "non_claims": _build_non_claims(),
            "outcome": outcome,
            "block": _block_from_checks(checks) if outcome == OUTCOME_BLOCKED else None,
        }
    )
    result["portable_source_body_verification_second_carrier_execution_summary"] = (
        build_portable_source_body_verification_second_carrier_execution_summary(result)
    )
    return _json_safe(result)


def resolve_portable_source_body_verification_second_carrier_execution(
    declared_second_carrier_execution_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded second-carrier execution posture only."""

    malformed_code = None
    if declared_second_carrier_execution_request is None or not _is_mapping(
        declared_second_carrier_execution_request
    ):
        request: dict[str, Any] = {}
        malformed_code = "DECLARED_SECOND_CARRIER_EXECUTION_REQUEST_MALFORMED"
    else:
        request = copy.deepcopy(dict(declared_second_carrier_execution_request))
        forced_block = request.get("_forced_block_code")
        if forced_block in BLOCK_CODES:
            malformed_code = str(forced_block)

    checks = _build_checks(request, malformed_code)
    outcome = _resolve_outcome(request, checks)
    return _build_result(request, checks, outcome)


def resolve_portable_source_body_verification_second_carrier_execution_from_path(
    declared_second_carrier_execution_request_path: Path | str,
) -> dict[str, Any]:
    """Read a JSON object request from a path and resolve execution posture."""

    path = Path(declared_second_carrier_execution_request_path)
    try:
        parsed = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise PortableSourceBodyVerificationSecondCarrierExecutionError(
            f"declared second-carrier execution request path is unreadable: {path}"
        ) from exc
    except OSError as exc:
        raise PortableSourceBodyVerificationSecondCarrierExecutionError(
            f"declared second-carrier execution request path is unreadable: {path}"
        ) from exc
    except json.JSONDecodeError as exc:
        raise PortableSourceBodyVerificationSecondCarrierExecutionError(
            f"declared second-carrier execution request JSON is malformed: {path}"
        ) from exc

    if not _is_mapping(parsed):
        return resolve_portable_source_body_verification_second_carrier_execution(
            {"_forced_block_code": "DECLARED_SECOND_CARRIER_EXECUTION_REQUEST_MALFORMED"}
        )
    return resolve_portable_source_body_verification_second_carrier_execution(parsed)


def build_portable_source_body_verification_second_carrier_execution_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact summary from a second-carrier execution result."""

    metadata = result.get(
        "portable_source_body_verification_second_carrier_execution_metadata",
        {},
    )
    declared = result.get("declared_second_carrier_execution_question", {})
    statement = result.get("second_carrier_execution_statement", {})
    non_claims = result.get("non_claims", {})
    checks = result.get("second_carrier_execution_checks", [])
    block = result.get("block")
    boundary_basis = result.get("selected_second_carrier_execution_boundary_basis", {})

    summary = {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") if _is_mapping(block) else None,
        "block_reason": block.get("block_reason") if _is_mapping(block) else None,
        "second_carrier_execution_request_id": metadata.get(
            "portable_source_body_verification_second_carrier_execution_request_id"
        ),
        "question": declared.get("second_carrier_execution_question"),
        "intent": declared.get("second_carrier_execution_intent"),
        "passed_check_count": _check_count(checks, True),
        "failed_check_count": _check_count(checks, False),
        "selected_second_carrier_execution_boundary_outcome": boundary_basis.get(
            "selected_second_carrier_execution_boundary_result_outcome"
        ),
        "selected_second_carrier_execution_boundary_result_version": boundary_basis.get(
            "selected_second_carrier_execution_boundary_result_version"
        ),
        "selected_second_carrier_execution_boundary_failed_check_count": (
            boundary_basis.get(
                "selected_second_carrier_execution_boundary_failed_check_count"
            )
        ),
        "no_output_result_success_external_result_or_cross_carrier_evidence": (
            non_claims.get("execution_output_created") is False
            and non_claims.get("second_carrier_output_capture_created") is False
            and non_claims.get("second_carrier_result_created") is False
            and non_claims.get("second_carrier_success_created") is False
            and non_claims.get("external_result_created") is False
            and non_claims.get("cross_carrier_evidence_created") is False
        ),
        "no_source_authority_currentness_final_completion_or_runtime": (
            non_claims.get("source_created") is False
            and non_claims.get("authority_created") is False
            and non_claims.get("currentness_created") is False
            and non_claims.get("final_completion_claimed") is False
            and non_claims.get("runtime_hosting_created") is False
        ),
        "no_deployment_public_release_or_follow_on": (
            non_claims.get("deployment_created") is False
            and non_claims.get("public_release_created") is False
            and non_claims.get("follow_on_work_authorized") is False
        ),
        "key_non_claims": {
            key: non_claims.get(key)
            for key in (
                "execution_output_created",
                "second_carrier_output_capture_created",
                "second_carrier_result_created",
                "second_carrier_success_created",
                "external_result_created",
                "cross_carrier_evidence_created",
                "source_created",
                "authority_created",
                "currentness_created",
                "final_completion_claimed",
                "runtime_hosting_created",
                "follow_on_work_authorized",
                "consumed_request_reopened",
                "authorization_token_reused",
                "v1_repaired",
                "v1_hidden",
                "v1_claimed_passed",
            )
        },
        "v1_predecessor_failure_preserved": True,
        "v1_not_repaired_hidden_or_claimed_passed": (
            non_claims.get("v1_repaired") is False
            and non_claims.get("v1_hidden") is False
            and non_claims.get("v1_claimed_passed") is False
        ),
    }
    for key in ALLOWED_TRUE_RECORDED_FIELDS:
        summary[key] = statement.get(key)
    return _json_safe(summary)


def _deterministic_result_filename(result: Mapping[str, Any]) -> str:
    metadata = result.get(
        "portable_source_body_verification_second_carrier_execution_metadata",
        {},
    )
    request_id = str(
        metadata.get(
            "portable_source_body_verification_second_carrier_execution_request_id",
            "portable_source_body_verification_second_carrier_execution_reference_review_001",
        )
    )
    safe_request_id = "".join(
        character if character.isalnum() or character in {"-", "_"} else "_"
        for character in request_id
    ).strip("_")
    if not safe_request_id:
        safe_request_id = (
            "portable_source_body_verification_second_carrier_execution_reference_review_001"
        )
    return f"{safe_request_id}__portable_source_body_verification_second_carrier_execution_result.json"


def _non_overwriting_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    for index in range(1, 1000):
        candidate = path.with_name(f"{stem}_{index:03d}{suffix}")
        if not candidate.exists():
            return candidate
    raise PortableSourceBodyVerificationSecondCarrierExecutionError(
        f"could not allocate non-overwriting output path under: {path.parent}"
    )


def write_portable_source_body_verification_second_carrier_execution_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a bounded second-carrier execution result without overwriting."""

    if output_path is None:
        target = OUTPUT_ROOT / _deterministic_result_filename(result)
    else:
        target = Path(output_path)
        if target.suffix == "":
            target = target / _deterministic_result_filename(result)
    target = _non_overwriting_path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(_json_safe(result), ensure_ascii=False, indent=2, sort_keys=True)
        + "\n",
        encoding="utf-8",
    )
    return target


def build_declared_portable_source_body_verification_second_carrier_execution_request(
    *,
    second_carrier_execution_request_id: str = (
        "portable_source_body_verification_second_carrier_execution_reference_review_001"
    ),
    selected_second_carrier_execution_boundary_result_path: str | None = None,
    selected_second_carrier_receipt_result_path: str | None = None,
) -> dict[str, Any]:
    """Build a minimal clean request for bounded second-carrier execution."""

    request: dict[str, Any] = {
        "second_carrier_execution_request_id": second_carrier_execution_request_id,
        "second_carrier_execution_question": CORE_QUESTION,
        "second_carrier_execution_intent": INTENT_RECORD,
        "second_carrier_execution_scope": list(SUPPORTED_SECOND_CARRIER_EXECUTION_SCOPE),
        "declared_non_claims": {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
        "reference_shaped_input_posture": True,
        "hidden_repo_state_not_used_as_execution_authority": True,
        "authorization_token_reuse_blocked": True,
        "consumed_request_token_remains_closed": True,
        "original_carrier_execution_trace_audit_only": True,
        "full_prior_artifact_body_emitted_outside_bounded_execution": False,
        "selected_second_carrier_execution_boundary_result_id": (
            "portable_source_body_verification_second_carrier_execution_boundary_reference_review_001"
        ),
        "selected_second_carrier_execution_boundary_result_path": (
            selected_second_carrier_execution_boundary_result_path
        ),
        "selected_second_carrier_execution_boundary_result_outcome": (
            SECOND_CARRIER_EXECUTION_BOUNDARY_RECORDED
        ),
        "selected_second_carrier_execution_boundary_result_version": (
            SECOND_CARRIER_EXECUTION_BOUNDARY_RESULT_VERSION
        ),
        "selected_second_carrier_execution_boundary_failed_check_count": 0,
        "selected_second_carrier_execution_boundary_declared_future_execution_step": True,
        "selected_second_carrier_execution_boundary_already_created_execution": False,
        "selected_second_carrier_execution_boundary_already_created_execution_artifact": False,
        "selected_second_carrier_execution_boundary_already_created_execution_output": False,
        "selected_second_carrier_execution_boundary_already_created_second_carrier_output_capture": False,
        "selected_second_carrier_execution_boundary_already_created_second_carrier_result": False,
        "selected_second_carrier_execution_boundary_already_created_second_carrier_success": False,
        "selected_second_carrier_execution_boundary_created_external_result": False,
        "selected_second_carrier_execution_boundary_created_cross_carrier_evidence": False,
        "selected_second_carrier_execution_boundary_used_hidden_repo_state_as_execution_authority": False,
        "selected_second_carrier_execution_boundary_treated_repo_local_availability_as_execution_authority": False,
        "selected_second_carrier_execution_boundary_treated_receiving_carrier_as_authority": False,
        "selected_second_carrier_execution_boundary_raw_full_prior_artifact_body_returned": False,
        "selected_second_carrier_receipt_result_id": (
            "portable_source_body_verification_second_carrier_receipt_reference_review_001"
        ),
        "selected_second_carrier_receipt_result_path": (
            selected_second_carrier_receipt_result_path
        ),
        "selected_second_carrier_receipt_result_outcome": SECOND_CARRIER_RECEIPT_RECORDED,
        "selected_second_carrier_receipt_failed_check_count": 0,
        "selected_second_carrier_receipt_bounded_receipt_recorded": True,
        "selected_second_carrier_receipt_receipt_not_execution": True,
    }

    request["selected_second_carrier_execution_boundary_basis"] = {
        "basis_id": "selected-second-carrier-execution-boundary",
        "outcome": SECOND_CARRIER_EXECUTION_BOUNDARY_RECORDED,
        "result_version": SECOND_CARRIER_EXECUTION_BOUNDARY_RESULT_VERSION,
        "failed_check_count": 0,
        "one_future_second_carrier_execution_step_declared": True,
        "execution_not_created": True,
        "execution_artifact_not_created": True,
        "execution_output_not_created": True,
        "second_carrier_output_capture_not_created": True,
        "second_carrier_result_not_created": True,
        "second_carrier_success_not_created": True,
        "external_result_not_created": True,
        "cross_carrier_evidence_not_created": True,
        "receiving_carrier_not_authority": True,
        "hidden_repo_state_excluded": True,
        "repo_local_availability_not_execution_authority": True,
        "raw_full_prior_artifact_body_not_returned": True,
        "path": selected_second_carrier_execution_boundary_result_path,
    }
    request["selected_second_carrier_receipt_basis"] = {
        "basis_id": "selected-second-carrier-receipt",
        "outcome": SECOND_CARRIER_RECEIPT_RECORDED,
        "failed_check_count": 0,
        "bounded_second_carrier_receipt_recorded": True,
        "receipt_not_execution": True,
        "path": selected_second_carrier_receipt_result_path,
    }

    for key in SELECTED_BASIS_KEYS:
        request.setdefault(
            key,
            {
                "basis_id": key,
                "basis_declared": True,
                "basis_remains_basis_only": True,
                "reference_shape_preserved": True,
            },
        )
    for key in POSTURE_KEYS:
        request[key] = {
            "declared": True,
            "posture": True,
            "basis_only": key not in {
                "one_bounded_second_carrier_execution_posture",
                "execution_recorded_bounded_posture",
                "execution_artifact_recorded_or_bounded_posture",
            },
        }
    return _json_safe(request)
