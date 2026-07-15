"""Bounded second-carrier output-capture-boundary resolver.

This module records at most one portable source-body verification
second-carrier output capture boundary posture. It is downstream of recorded
second-carrier execution output. It may preserve one future second-carrier
output-capture step, but it does not create second-carrier output capture,
capture artifact, second-carrier result, second-carrier success, external
result, cross-carrier evidence, source transfer, source receipt, reception
authorization, source, authority, currentness, final completion, runtime,
continuation, reusable permission, derivative reception, vessel relation,
another reception request, or follow-on work.

The resolver is self-contained, imports no repo-local modules, performs no
network calls, runs no subprocesses, mutates no prior artifact, and never
returns a raw full prior artifact body outside bounded capture-boundary
posture.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class PortableSourceBodyVerificationSecondCarrierOutputCaptureBoundaryError(Exception):
    """Raised for explicit unreadable path or malformed JSON path inputs."""


RESOLVER_MODULE = (
    "resolve_portable_source_body_verification_second_carrier_output_capture_boundary"
)
RESULT_TYPE = (
    "portable_source_body_verification_second_carrier_output_capture_boundary_result"
)
RESULT_VERSION = "0.1.0"
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_portable_source_body_verification_"
    "second_carrier_output_capture_boundary"
)

CORE_QUESTION = (
    "Can the recorded second-carrier execution output basis be bounded for one "
    "future second-carrier output capture step without creating capture yet, "
    "creating second-carrier result, creating second-carrier success, creating "
    "external result, creating cross-carrier evidence, creating source transfer, "
    "creating source receipt, creating reception authorization, creating source, "
    "authority, currentness, runtime, final completion, continuation, reusable "
    "permission, derivative reception, vessel relation, another reception "
    "request, or follow-on work?"
)
EXPECTED_QUESTION = CORE_QUESTION

OUTCOME_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_"
    "REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_BLOCKED"
)
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = (
    "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY"
)
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY"
)
INTENT_BLOCK = (
    "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY"
)
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

SECOND_CARRIER_EXECUTION_OUTPUT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_OUTPUT_RECORDED"
)
SECOND_CARRIER_EXECUTION_OUTPUT_RESULT_VERSION = "0.1.0"

SUPPORTED_SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_SCOPE = (
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_ONLY",
    "ONE_FUTURE_SECOND_CARRIER_OUTPUT_CAPTURE_STEP_ONLY",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BASIS_PRESERVED",
    "OUTPUT_ARTIFACT_BASIS_PRESERVED",
    "OUTPUT_NOT_CAPTURE",
    "CAPTURE_NOT_CREATED",
    "CAPTURE_ARTIFACT_NOT_CREATED",
    "SECOND_CARRIER_RESULT_NOT_CREATED",
    "SECOND_CARRIER_SUCCESS_NOT_CREATED",
    "EXTERNAL_RESULT_NOT_CREATED",
    "CROSS_CARRIER_EVIDENCE_NOT_CREATED",
    "CAPTURE_NOT_SOURCE_TRANSFER",
    "CAPTURE_NOT_SOURCE_RECEIPT",
    "CAPTURE_NOT_RECEPTION_AUTHORIZATION",
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
    "HIDDEN_REPO_STATE_NOT_USED_AS_CAPTURE_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_NOT_CAPTURE_AUTHORITY",
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
    "selected_second_carrier_execution_output_basis",
    "selected_second_carrier_execution_output_terminal_summary_basis",
    "selected_second_carrier_execution_output_boundary_basis",
    "selected_second_carrier_execution_basis",
    "selected_second_carrier_execution_boundary_basis",
    "selected_second_carrier_receipt_basis",
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
    "second_carrier_output_capture_boundary_only_posture",
    "one_future_second_carrier_output_capture_step_posture",
    "second_carrier_execution_output_basis_preserved_posture",
    "output_artifact_basis_preserved_posture",
    "output_not_capture_posture",
    "capture_not_created_posture",
    "capture_artifact_not_created_posture",
    "second_carrier_result_not_created_posture",
    "second_carrier_success_not_created_posture",
    "external_result_not_created_posture",
    "cross_carrier_evidence_not_created_posture",
    "capture_not_source_transfer_posture",
    "capture_not_source_receipt_posture",
    "capture_not_reception_authorization_posture",
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
    "repo_local_availability_not_capture_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
)

REQUIRED_FALSE_NON_CLAIMS = (
    "second_carrier_output_capture_created",
    "capture_artifact_created",
    "second_carrier_result_created",
    "second_carrier_success_created",
    "external_result_created",
    "cross_carrier_evidence_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "second_carrier_output_capture_boundary_treated_as_capture",
    "second_carrier_output_capture_boundary_treated_as_capture_artifact",
    "second_carrier_output_capture_boundary_treated_as_result",
    "second_carrier_output_capture_boundary_treated_as_success",
    "second_carrier_output_capture_boundary_treated_as_external_result",
    "second_carrier_output_capture_boundary_treated_as_cross_carrier_evidence",
    "second_carrier_output_capture_boundary_treated_as_source_transfer",
    "second_carrier_output_capture_boundary_treated_as_source_receipt",
    "second_carrier_output_capture_boundary_treated_as_reception_authorization",
    "second_carrier_output_capture_boundary_treated_as_source",
    "second_carrier_output_capture_boundary_treated_as_authority",
    "second_carrier_output_capture_boundary_treated_as_currentness",
    "second_carrier_output_capture_boundary_treated_as_final_completion",
    "second_carrier_output_capture_boundary_treated_as_runtime",
    "second_carrier_output_capture_boundary_treated_as_continuation",
    "second_carrier_output_capture_boundary_treated_as_reusable_permission",
    "second_carrier_output_capture_boundary_treated_as_follow_on_work",
    "receiving_carrier_treated_as_authority",
    "artifact_existence_treated_as_capture_authority",
    "artifact_path_treated_as_currentness",
    "repo_local_availability_treated_as_capture_authority",
    "hidden_repo_state_used_as_capture_content",
    "hidden_repo_state_used_as_capture_authority",
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

ALLOWED_TRUE_RECORDED_FIELDS = (
    "second_carrier_output_capture_boundary_recorded",
    "one_future_second_carrier_output_capture_step_declared",
    "second_carrier_execution_output_basis_preserved",
    "output_artifact_basis_preserved",
    "output_not_capture",
    "capture_not_created",
    "capture_artifact_not_created",
    "second_carrier_result_not_created",
    "second_carrier_success_not_created",
    "external_result_not_created",
    "cross_carrier_evidence_not_created",
    "capture_not_source_transfer",
    "capture_not_source_receipt",
    "capture_not_reception_authorization",
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
    "hidden_repo_state_not_used_as_capture_authority",
    "repo_local_availability_not_capture_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
)

ALLOWED_FALSE_RECORDED_FIELDS = REQUIRED_FALSE_NON_CLAIMS

_BASIS_MISSING_CODES = {
    "selected_second_carrier_execution_output_basis": (
        "SECOND_CARRIER_EXECUTION_OUTPUT_BASIS_MISSING"
    ),
    "selected_second_carrier_execution_output_terminal_summary_basis": (
        "SECOND_CARRIER_EXECUTION_OUTPUT_TERMINAL_SUMMARY_BASIS_MISSING"
    ),
    "selected_second_carrier_execution_output_boundary_basis": (
        "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_BASIS_MISSING"
    ),
    "selected_second_carrier_execution_basis": "SECOND_CARRIER_EXECUTION_BASIS_MISSING",
    "selected_second_carrier_execution_boundary_basis": (
        "SECOND_CARRIER_EXECUTION_BOUNDARY_BASIS_MISSING"
    ),
    "selected_second_carrier_receipt_basis": "SECOND_CARRIER_RECEIPT_BASIS_MISSING",
    "selected_packet_transfer_basis": "PACKET_TRANSFER_BASIS_MISSING",
    "selected_packet_emission_basis": "PACKET_EMISSION_BASIS_MISSING",
    "selected_packet_emission_boundary_v2_basis": (
        "PACKET_EMISSION_BOUNDARY_V2_BASIS_MISSING"
    ),
    "selected_packet_emission_boundary_v1_predecessor_failure_basis": (
        "PACKET_EMISSION_BOUNDARY_V1_PREDECESSOR_FAILURE_BASIS_MISSING"
    ),
    "selected_packet_artifact_basis": "PACKET_ARTIFACT_BASIS_MISSING",
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

_POSTURE_MISSING_CODES = {
    key: f"{key.removesuffix('_posture').upper()}_POSTURE_MISSING"
    for key in POSTURE_KEYS
}

_NON_CLAIM_BLOCK_CODES = {
    "second_carrier_output_capture_created": "SECOND_CARRIER_OUTPUT_CAPTURE_CREATED",
    "capture_artifact_created": "CAPTURE_ARTIFACT_CREATED",
    "second_carrier_result_created": "SECOND_CARRIER_RESULT_CREATED",
    "second_carrier_success_created": "SECOND_CARRIER_SUCCESS_CREATED",
    "external_result_created": "EXTERNAL_RESULT_CREATED",
    "cross_carrier_evidence_created": "CROSS_CARRIER_EVIDENCE_CREATED",
    "source_transfer_occurred": "SOURCE_TRANSFER_OCCURRED",
    "source_receipt_occurred": "SOURCE_RECEIPT_OCCURRED",
    "reception_authorization_created": "RECEPTION_AUTHORIZATION_CREATED",
    "second_carrier_output_capture_boundary_treated_as_capture": (
        "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_CAPTURE"
    ),
    "second_carrier_output_capture_boundary_treated_as_capture_artifact": (
        "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_CAPTURE_ARTIFACT"
    ),
    "second_carrier_output_capture_boundary_treated_as_result": (
        "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_RESULT"
    ),
    "second_carrier_output_capture_boundary_treated_as_success": (
        "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_SUCCESS"
    ),
    "second_carrier_output_capture_boundary_treated_as_external_result": (
        "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_EXTERNAL_RESULT"
    ),
    "second_carrier_output_capture_boundary_treated_as_cross_carrier_evidence": (
        "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_CROSS_CARRIER_EVIDENCE"
    ),
    "second_carrier_output_capture_boundary_treated_as_source_transfer": (
        "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_SOURCE_TRANSFER"
    ),
    "second_carrier_output_capture_boundary_treated_as_source_receipt": (
        "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_SOURCE_RECEIPT"
    ),
    "second_carrier_output_capture_boundary_treated_as_reception_authorization": (
        "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION"
    ),
    "second_carrier_output_capture_boundary_treated_as_source": (
        "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_SOURCE"
    ),
    "second_carrier_output_capture_boundary_treated_as_authority": (
        "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_AUTHORITY"
    ),
    "second_carrier_output_capture_boundary_treated_as_currentness": (
        "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_CURRENTNESS"
    ),
    "second_carrier_output_capture_boundary_treated_as_final_completion": (
        "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_FINAL_COMPLETION"
    ),
    "second_carrier_output_capture_boundary_treated_as_runtime": (
        "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_RUNTIME"
    ),
    "second_carrier_output_capture_boundary_treated_as_continuation": (
        "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_CONTINUATION"
    ),
    "second_carrier_output_capture_boundary_treated_as_reusable_permission": (
        "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION"
    ),
    "second_carrier_output_capture_boundary_treated_as_follow_on_work": (
        "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK"
    ),
    "receiving_carrier_treated_as_authority": "RECEIVING_CARRIER_TREATED_AS_AUTHORITY",
    "artifact_existence_treated_as_capture_authority": (
        "ARTIFACT_EXISTENCE_TREATED_AS_CAPTURE_AUTHORITY"
    ),
    "artifact_path_treated_as_currentness": "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "repo_local_availability_treated_as_capture_authority": (
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_CAPTURE_AUTHORITY"
    ),
    "hidden_repo_state_used_as_capture_content": (
        "HIDDEN_REPO_STATE_USED_AS_CAPTURE_CONTENT"
    ),
    "hidden_repo_state_used_as_capture_authority": (
        "HIDDEN_REPO_STATE_USED_AS_CAPTURE_AUTHORITY"
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

_STATIC_BLOCK_CODES = (
    "DECLARED_SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_REQUEST_UNREADABLE",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_QUESTION_UNDECLARED",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_INTENT_UNSUPPORTED",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_BLOCK_REQUESTED",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BASIS_MISSING",
    "SECOND_CARRIER_EXECUTION_OUTPUT_NOT_RECORDED",
    "SECOND_CARRIER_EXECUTION_OUTPUT_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_VERSION_NOT_0_1_0",
    "SECOND_CARRIER_EXECUTION_OUTPUT_DID_NOT_RECORD_BOUNDED_OUTPUT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_ALREADY_CREATED_OUTPUT_CAPTURE",
    "SECOND_CARRIER_EXECUTION_OUTPUT_ALREADY_CREATED_SECOND_CARRIER_RESULT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_ALREADY_CREATED_SECOND_CARRIER_SUCCESS",
    "SECOND_CARRIER_EXECUTION_OUTPUT_CREATED_EXTERNAL_RESULT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_CREATED_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_OUTPUT_AS_CAPTURE",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_OUTPUT_AS_RESULT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_OUTPUT_AS_SUCCESS",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_OUTPUT_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_OUTPUT_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXECUTION_OUTPUT_USED_HIDDEN_REPO_STATE_AS_CAPTURE_AUTHORITY",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_REPO_LOCAL_AVAILABILITY_AS_CAPTURE_AUTHORITY",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_RECEIVING_CARRIER_AS_AUTHORITY",
    "SECOND_CARRIER_EXECUTION_OUTPUT_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY_OUTSIDE_BOUNDED_OUTPUT",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_CAPTURE",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_CAPTURE_ARTIFACT",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_RESULT",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_SUCCESS",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_SOURCE",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_AUTHORITY",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_CURRENTNESS",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_FINAL_COMPLETION",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_RUNTIME",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_CONTINUATION",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
    "SECOND_CARRIER_OUTPUT_CAPTURE_CREATED",
    "CAPTURE_ARTIFACT_CREATED",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_CAPTURE_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_CAPTURE_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_CAPTURE_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_CAPTURE_AUTHORITY",
    "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENT_REPORT_ARTIFACT",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_SOURCE",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_AUTHORITY",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENTNESS",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_CAPTURE_BOUNDARY",
    "ARTIFACTS_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_SCOPE",
)

BLOCK_CODES = frozenset(
    _STATIC_BLOCK_CODES
    + tuple(_BASIS_MISSING_CODES.values())
    + tuple(_POSTURE_MISSING_CODES.values())
    + tuple(_NON_CLAIM_BLOCK_CODES.values())
)

_REDACTION = "[bounded-reference-redacted-raw-or-hidden-state]"
_SENSITIVE_TEXT_MARKERS = ("MUST_NOT_RETURN", "HOSTILE_")
_SENSITIVE_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_result_body",
    "raw_output_body",
    "execution_body",
    "execution_artifact_body",
    "output_body",
    "output_artifact_body",
    "second_carrier_output_body",
    "second_carrier_output_capture_body",
    "second_carrier_result_body",
    "second_carrier_success_body",
    "capture_body",
    "capture_artifact_body",
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
    "output_artifact_presence",
    "capture_artifact_presence",
    "output_path_existence",
    "capture_path_existence",
    "unlisted_file_dependency",
}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _contains_sensitive_marker(value: str) -> bool:
    return any(marker in value for marker in _SENSITIVE_TEXT_MARKERS)


def _is_declared(value: Any) -> bool:
    if value is None:
        return False
    if value == "":
        return False
    if value == [] or value == {}:
        return False
    return True


def _sanitize(value: Any) -> Any:
    if isinstance(value, Mapping):
        sanitized: dict[str, Any] = {}
        for key, item in value.items():
            key_text = str(key)
            if key_text in _SENSITIVE_KEYS or _contains_sensitive_marker(key_text):
                sanitized[_REDACTION] = _REDACTION
            elif key_text.endswith("_body") or key_text.endswith("_full_body"):
                sanitized[key_text] = _REDACTION
            else:
                sanitized[key_text] = _sanitize(item)
        return sanitized
    if isinstance(value, list):
        return [_sanitize(item) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item) for item in value]
    if isinstance(value, set):
        return [_sanitize(item) for item in sorted(value, key=str)]
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, str) and _contains_sensitive_marker(value):
        return _REDACTION
    return copy.deepcopy(value)


def _json_safe(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_json_safe(item) for item in value]
    if isinstance(value, tuple):
        return [_json_safe(item) for item in value]
    if isinstance(value, set):
        return [_json_safe(item) for item in sorted(value, key=str)]
    if isinstance(value, Path):
        return str(value)
    if value is None or isinstance(value, (str, int, float, bool)):
        return copy.deepcopy(value)
    return str(value)


def _first_declared(*values: Any) -> Any:
    for value in values:
        if _is_declared(value):
            return value
    return None


def _as_bool(value: Any, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        lowered = value.strip().lower()
        if lowered in {"true", "yes", "1", "recorded", "declared"}:
            return True
        if lowered in {"false", "no", "0", "none", "null", ""}:
            return False
    if isinstance(value, (int, float)):
        return bool(value)
    return default


def _as_int(value: Any, default: int | None = 0) -> int | None:
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


def _nested_lookup(value: Any, names: Sequence[str]) -> Any:
    if not isinstance(value, Mapping):
        return None
    for name in names:
        if name in value and _is_declared(value[name]):
            return value[name]
    nested_keys = (
        "portable_source_body_verification_second_carrier_execution_output_metadata",
        "second_carrier_execution_output_metadata",
        "portable_source_body_verification_second_carrier_execution_output_summary",
        "second_carrier_execution_output_summary",
        "second_carrier_execution_output_statement",
        "statement",
        "summary",
        "metadata",
        "non_claims",
        "selected_values",
    )
    for nested_key in nested_keys:
        nested = value.get(nested_key)
        found = _nested_lookup(nested, names)
        if _is_declared(found):
            return found
    return None


def _execution_output_names(*names: str) -> tuple[str, ...]:
    expanded: list[str] = []
    for name in names:
        expanded.extend(
            (
                f"selected_second_carrier_execution_output_{name}",
                f"selected_second_carrier_execution_output_result_{name}",
                name,
            )
        )
    return tuple(dict.fromkeys(expanded))


def _execution_output_value(request: Mapping[str, Any], *names: str) -> Any:
    expanded = _execution_output_names(*names)
    for name in expanded:
        if name in request and _is_declared(request[name]):
            return request[name]
    basis = request.get("selected_second_carrier_execution_output_basis")
    return _nested_lookup(basis, expanded)


def _execution_output_bool(
    request: Mapping[str, Any],
    *names: str,
    default: bool = False,
) -> bool:
    value = _execution_output_value(request, *names)
    if _is_declared(value):
        return _as_bool(value, default=default)
    return default


def _execution_output_negative_flag(
    request: Mapping[str, Any],
    bad_names: Sequence[str],
    good_names: Sequence[str],
) -> bool:
    bad_value = _execution_output_value(request, *bad_names)
    if _is_declared(bad_value):
        return _as_bool(bad_value)
    good_value = _execution_output_value(request, *good_names)
    if _is_declared(good_value):
        return not _as_bool(good_value)
    return False


def _scope_from_request(request: Mapping[str, Any]) -> list[str]:
    supplied = request.get("second_carrier_output_capture_boundary_scope")
    if supplied is None:
        return list(SUPPORTED_SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_SCOPE)
    if isinstance(supplied, str):
        return [supplied]
    if isinstance(supplied, Mapping):
        values = supplied.get("scope_values", supplied.get("values"))
        if isinstance(values, str):
            return [values]
        if isinstance(values, list):
            return [str(value) for value in values]
        return [str(key) for key, value in supplied.items() if _as_bool(value)]
    if isinstance(supplied, (list, tuple, set)):
        return [str(value) for value in supplied]
    return [str(supplied)]


def _declared_non_claims_from_request(request: Mapping[str, Any]) -> Mapping[str, Any]:
    supplied = request.get("declared_non_claims")
    if isinstance(supplied, Mapping):
        return supplied
    supplied = request.get("non_claims")
    if isinstance(supplied, Mapping):
        return supplied
    return {}


def _claim_value(request: Mapping[str, Any], key: str) -> Any:
    if key in request:
        return request[key]
    non_claims = _declared_non_claims_from_request(request)
    if key in non_claims:
        return non_claims[key]
    return None


def _basis_supplied(request: Mapping[str, Any], key: str) -> bool:
    if _is_declared(request.get(key)):
        return True
    if key == "selected_second_carrier_execution_output_basis":
        return any(
            _is_declared(request.get(shortcut))
            for shortcut in (
                "selected_second_carrier_execution_output_result_path",
                "selected_second_carrier_execution_output_result_id",
                "selected_second_carrier_execution_output_result_outcome",
                "selected_second_carrier_execution_output_result_version",
            )
        )
    return False


def _check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    block_code: str,
) -> None:
    checks.append(
        {
            "check_name": check_name,
            "passed": bool(passed),
            "expected_posture": _json_safe(expected_posture),
            "actual_posture": _sanitize(_json_safe(actual_posture)),
            "block_code": None if passed else block_code,
            "failure_code": None if passed else block_code,
        }
    )


def _first_failure(checks: Sequence[Mapping[str, Any]]) -> tuple[str, str] | None:
    for check in checks:
        if not check.get("passed"):
            code = str(check.get("block_code") or check.get("failure_code"))
            return code, str(check.get("check_name"))
    return None


def _block(block_code: str, reason: str) -> dict[str, Any]:
    return {
        "blocked": True,
        "block_code": block_code,
        "reason": reason,
        "block_code_is_public": block_code in BLOCK_CODES,
    }


def _empty_block() -> dict[str, Any]:
    return {
        "blocked": False,
        "block_code": None,
        "reason": None,
        "block_code_is_public": True,
    }


def _basis_section(request: Mapping[str, Any], key: str) -> dict[str, Any]:
    supplied = request.get(key)
    section: dict[str, Any]
    if isinstance(supplied, Mapping):
        section = _sanitize(supplied)
    elif _is_declared(supplied):
        section = {"basis_reference": _sanitize(supplied)}
    else:
        section = {}
    section.setdefault("basis_key", key)
    section.setdefault("basis_declared", _basis_supplied(request, key))
    section.setdefault("basis_role", "selected_reference_basis_only")
    section.setdefault("basis_reference_shape_preserved", True)
    section.setdefault("selected_basis_reference_shape_preserved", True)
    section.setdefault("basis_does_not_create_capture_result_success_or_authority", True)
    section.setdefault("raw_full_prior_artifact_body_not_returned", True)
    return section


def _posture_section(
    request: Mapping[str, Any],
    key: str,
    expected_posture: str,
) -> dict[str, Any]:
    supplied = request.get(key)
    declared = _is_declared(supplied)
    if isinstance(supplied, Mapping):
        section = _sanitize(supplied)
    elif declared:
        section = {"declared_posture": _sanitize(supplied)}
    else:
        section = {}
    section.setdefault("posture_key", key)
    section.setdefault("posture_declared", declared)
    section.setdefault("expected_posture", expected_posture)
    section.setdefault("preserves_capture_boundary_membrane", True)
    return section


def _statement(recorded: bool) -> dict[str, bool]:
    statement = {field: bool(recorded) for field in ALLOWED_TRUE_RECORDED_FIELDS}
    statement.update({field: False for field in REQUIRED_FALSE_NON_CLAIMS})
    statement.setdefault("second_carrier_output_capture_created", False)
    statement.setdefault("capture_artifact_created", False)
    statement.setdefault("second_carrier_result_created", False)
    statement.setdefault("second_carrier_success_created", False)
    statement.setdefault("external_result_created", False)
    statement.setdefault("cross_carrier_evidence_created", False)
    statement.setdefault("source_transfer_occurred", False)
    statement.setdefault("source_receipt_occurred", False)
    statement.setdefault("reception_authorization_created", False)
    statement["full_prior_artifact_body_emitted_outside_bounded_capture_boundary"] = False
    statement["artifacts_mutated"] = False
    return statement


def _non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _non_meaning() -> dict[str, bool]:
    return {
        "second_carrier_output_capture_exists": False,
        "capture_artifact_exists": False,
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
        "capture_boundary_became_capture": False,
        "capture_boundary_became_result": False,
        "capture_boundary_became_success": False,
        "capture_boundary_became_external_result": False,
        "capture_boundary_became_cross_carrier_proof": False,
        "capture_boundary_became_source_transfer_source_receipt_or_reception_authorization": (
            False
        ),
        "capture_boundary_became_source_authority_or_currentness": False,
        "output_became_capture": False,
        "output_artifact_became_capture": False,
        "receiving_carrier_became_authority": False,
        "transferred_packet_became_source_authority_or_currentness": False,
        "artifact_existence_became_capture_authority": False,
        "artifact_path_became_currentness": False,
        "repo_local_availability_became_capture_authority": False,
        "hidden_repo_state_became_capture_authority": False,
        "v1_packet_emission_boundary_resolver_repaired_hidden_erased_or_claimed_passed": (
            False
        ),
    }


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "second-carrier output capture boundary test",
            "second-carrier output capture boundary live artifact",
            "second-carrier output capture boundary terminal summary, if needed",
            "second-carrier output capture spec/resolver/test/live artifact",
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
        ],
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }


def _build_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    question = request.get("second_carrier_output_capture_boundary_question")
    intent = request.get("second_carrier_output_capture_boundary_intent")
    scopes = _scope_from_request(request)
    unsupported_scopes = [
        scope
        for scope in scopes
        if scope not in SUPPORTED_SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_SCOPE
    ]

    _check(
        checks,
        "second_carrier_output_capture_boundary_question_declared",
        question == CORE_QUESTION,
        CORE_QUESTION,
        question,
        "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_QUESTION_UNDECLARED",
    )
    _check(
        checks,
        "second_carrier_output_capture_boundary_intent_supported",
        intent in SUPPORTED_INTENTS and intent != INTENT_BLOCK,
        f"one of {SUPPORTED_INTENTS[:-1]}",
        intent,
        "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_INTENT_UNSUPPORTED"
        if intent != INTENT_BLOCK
        else "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_BLOCK_REQUESTED",
    )
    _check(
        checks,
        "second_carrier_output_capture_boundary_scope_supported",
        not unsupported_scopes,
        list(SUPPORTED_SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_SCOPE),
        scopes,
        "UNSUPPORTED_SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_SCOPE",
    )

    for key in SELECTED_BASIS_KEYS:
        _check(
            checks,
            f"{key}_declared",
            _basis_supplied(request, key),
            "selected reference-shaped basis declared",
            request.get(key),
            _BASIS_MISSING_CODES[key],
        )

    execution_output_outcome = _execution_output_value(request, "outcome")
    execution_output_version = _first_declared(
        _execution_output_value(request, "result_version"),
        _execution_output_value(request, "version"),
        _execution_output_value(
            request,
            "portable_source_body_verification_second_carrier_execution_output_result_version",
        ),
    )
    execution_output_failed_count = _as_int(
        _first_declared(
            _execution_output_value(request, "failed_check_count"),
            _execution_output_value(request, "failed_checks"),
        ),
        default=None,
    )

    _check(
        checks,
        "second_carrier_execution_output_outcome_recorded",
        execution_output_outcome == SECOND_CARRIER_EXECUTION_OUTPUT_RECORDED,
        SECOND_CARRIER_EXECUTION_OUTPUT_RECORDED,
        execution_output_outcome,
        "SECOND_CARRIER_EXECUTION_OUTPUT_NOT_RECORDED",
    )
    _check(
        checks,
        "second_carrier_execution_output_version_0_1_0",
        execution_output_version == SECOND_CARRIER_EXECUTION_OUTPUT_RESULT_VERSION,
        SECOND_CARRIER_EXECUTION_OUTPUT_RESULT_VERSION,
        execution_output_version,
        "SECOND_CARRIER_EXECUTION_OUTPUT_VERSION_NOT_0_1_0",
    )
    _check(
        checks,
        "second_carrier_execution_output_failed_checks_zero",
        execution_output_failed_count == 0,
        0,
        execution_output_failed_count,
        "SECOND_CARRIER_EXECUTION_OUTPUT_FAILED_CHECKS_PRESENT",
    )
    _check(
        checks,
        "second_carrier_execution_output_recorded_bounded_output",
        _execution_output_bool(
            request,
            "bounded_output_recorded",
            "bounded_second_carrier_execution_output_recorded",
            "second_carrier_execution_output_recorded",
            "output_recorded_bounded",
        ),
        "bounded second-carrier execution output recorded",
        _execution_output_value(
            request,
            "bounded_second_carrier_execution_output_recorded",
            "output_recorded_bounded",
        ),
        "SECOND_CARRIER_EXECUTION_OUTPUT_DID_NOT_RECORD_BOUNDED_OUTPUT",
    )

    execution_output_bad_checks = (
        (
            "second_carrier_execution_output_did_not_create_output_capture",
            ("already_created_output_capture", "output_capture_created"),
            ("second_carrier_output_capture_not_created", "capture_not_created"),
            "SECOND_CARRIER_EXECUTION_OUTPUT_ALREADY_CREATED_OUTPUT_CAPTURE",
        ),
        (
            "second_carrier_execution_output_did_not_create_second_carrier_result",
            ("already_created_second_carrier_result", "second_carrier_result_created"),
            ("second_carrier_result_not_created",),
            "SECOND_CARRIER_EXECUTION_OUTPUT_ALREADY_CREATED_SECOND_CARRIER_RESULT",
        ),
        (
            "second_carrier_execution_output_did_not_create_second_carrier_success",
            ("already_created_second_carrier_success", "second_carrier_success_created"),
            ("second_carrier_success_not_created",),
            "SECOND_CARRIER_EXECUTION_OUTPUT_ALREADY_CREATED_SECOND_CARRIER_SUCCESS",
        ),
        (
            "second_carrier_execution_output_did_not_create_external_result",
            ("created_external_result", "external_result_created"),
            ("external_result_not_created",),
            "SECOND_CARRIER_EXECUTION_OUTPUT_CREATED_EXTERNAL_RESULT",
        ),
        (
            "second_carrier_execution_output_did_not_create_cross_carrier_evidence",
            ("created_cross_carrier_evidence", "cross_carrier_evidence_created"),
            ("cross_carrier_evidence_not_created",),
            "SECOND_CARRIER_EXECUTION_OUTPUT_CREATED_CROSS_CARRIER_EVIDENCE",
        ),
        (
            "second_carrier_execution_output_did_not_treat_output_as_capture",
            ("treated_output_as_capture", "output_treated_as_capture"),
            ("output_not_capture",),
            "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_OUTPUT_AS_CAPTURE",
        ),
        (
            "second_carrier_execution_output_did_not_treat_output_as_result",
            ("treated_output_as_result", "output_treated_as_result"),
            ("output_not_result",),
            "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_OUTPUT_AS_RESULT",
        ),
        (
            "second_carrier_execution_output_did_not_treat_output_as_success",
            ("treated_output_as_success", "output_treated_as_success"),
            ("output_not_success",),
            "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_OUTPUT_AS_SUCCESS",
        ),
        (
            "second_carrier_execution_output_did_not_treat_output_as_external_result",
            ("treated_output_as_external_result", "output_treated_as_external_result"),
            ("output_not_external_result",),
            "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_OUTPUT_AS_EXTERNAL_RESULT",
        ),
        (
            "second_carrier_execution_output_did_not_treat_output_as_cross_carrier_evidence",
            (
                "treated_output_as_cross_carrier_evidence",
                "output_treated_as_cross_carrier_evidence",
            ),
            ("output_not_cross_carrier_evidence",),
            "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_OUTPUT_AS_CROSS_CARRIER_EVIDENCE",
        ),
        (
            "second_carrier_execution_output_did_not_use_hidden_repo_state_as_capture_authority",
            (
                "used_hidden_repo_state_as_capture_authority",
                "hidden_repo_state_used_as_capture_authority",
                "hidden_repo_state_used_as_output_authority",
            ),
            (
                "hidden_repo_state_not_used_as_capture_authority",
                "hidden_repo_state_not_used_as_output_authority",
            ),
            "SECOND_CARRIER_EXECUTION_OUTPUT_USED_HIDDEN_REPO_STATE_AS_CAPTURE_AUTHORITY",
        ),
        (
            "second_carrier_execution_output_did_not_treat_repo_local_availability_as_capture_authority",
            (
                "treated_repo_local_availability_as_capture_authority",
                "repo_local_availability_treated_as_capture_authority",
                "repo_local_availability_treated_as_output_authority",
            ),
            (
                "repo_local_availability_not_capture_authority",
                "repo_local_availability_not_output_authority",
            ),
            "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_REPO_LOCAL_AVAILABILITY_AS_CAPTURE_AUTHORITY",
        ),
        (
            "second_carrier_execution_output_did_not_treat_receiving_carrier_as_authority",
            ("treated_receiving_carrier_as_authority", "receiving_carrier_treated_as_authority"),
            ("receiving_carrier_not_authority",),
            "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_RECEIVING_CARRIER_AS_AUTHORITY",
        ),
        (
            "second_carrier_execution_output_did_not_return_raw_full_prior_artifact_body",
            (
                "raw_full_prior_artifact_body_returned_outside_bounded_output",
                "raw_full_prior_artifact_body_returned",
            ),
            ("raw_full_prior_artifact_body_not_returned",),
            "SECOND_CARRIER_EXECUTION_OUTPUT_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY_OUTSIDE_BOUNDED_OUTPUT",
        ),
    )
    for check_name, bad_names, good_names, code in execution_output_bad_checks:
        bad_flag = _execution_output_negative_flag(request, bad_names, good_names)
        _check(
            checks,
            check_name,
            not bad_flag,
            "false",
            bad_flag,
            code,
        )

    for key in POSTURE_KEYS:
        _check(
            checks,
            f"{key}_declared",
            _is_declared(request.get(key)),
            "capture-boundary posture declared",
            request.get(key),
            _POSTURE_MISSING_CODES[key],
        )

    _check(
        checks,
        "selected_basis_reference_shape_preserved",
        not _as_bool(request.get("selected_basis_not_reference_shaped")),
        "selected basis remains reference-shaped",
        request.get("selected_basis_not_reference_shaped"),
        "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    )
    command_report_lineage_checks = (
        (
            "command_report_lineage_not_current_report_artifact",
            "command_report_lineage_treated_as_current_report_artifact",
            "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENT_REPORT_ARTIFACT",
        ),
        (
            "command_report_lineage_not_source",
            "command_report_lineage_treated_as_source",
            "COMMAND_REPORT_LINEAGE_TREATED_AS_SOURCE",
        ),
        (
            "command_report_lineage_not_authority",
            "command_report_lineage_treated_as_authority",
            "COMMAND_REPORT_LINEAGE_TREATED_AS_AUTHORITY",
        ),
        (
            "command_report_lineage_not_currentness",
            "command_report_lineage_treated_as_currentness",
            "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENTNESS",
        ),
    )
    for check_name, request_key, code in command_report_lineage_checks:
        _check(
            checks,
            check_name,
            not _as_bool(request.get(request_key)),
            "command report lineage remains lineage only",
            request.get(request_key),
            code,
        )

    declared_non_claims = _declared_non_claims_from_request(request)
    for key in REQUIRED_FALSE_NON_CLAIMS:
        _check(
            checks,
            f"{key}_declared_false",
            key in declared_non_claims and declared_non_claims.get(key) is False,
            False,
            declared_non_claims.get(key),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
        claim_value = _claim_value(request, key)
        if _is_declared(claim_value):
            _check(
                checks,
                f"{key}_not_true",
                not _as_bool(claim_value),
                False,
                claim_value,
                _NON_CLAIM_BLOCK_CODES[key],
            )

    _check(
        checks,
        "full_prior_artifact_body_not_emitted_outside_bounded_capture_boundary",
        not _as_bool(
            request.get("full_prior_artifact_body_emitted_outside_bounded_capture_boundary")
        ),
        False,
        request.get("full_prior_artifact_body_emitted_outside_bounded_capture_boundary"),
        "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_CAPTURE_BOUNDARY",
    )
    return checks


def build_portable_source_body_verification_second_carrier_output_capture_boundary_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a bounded summary without promoting capture-boundary posture."""

    metadata = result.get(
        "portable_source_body_verification_second_carrier_output_capture_boundary_metadata",
        {},
    )
    if not isinstance(metadata, Mapping):
        metadata = {}
    declared = result.get("declared_second_carrier_output_capture_boundary_question", {})
    if not isinstance(declared, Mapping):
        declared = {}
    statement = result.get("second_carrier_output_capture_boundary_statement", {})
    if not isinstance(statement, Mapping):
        statement = {}
    non_claims = result.get("non_claims", {})
    if not isinstance(non_claims, Mapping):
        non_claims = {}
    block = result.get("block", {})
    if not isinstance(block, Mapping):
        block = {}
    checks = result.get("second_carrier_output_capture_boundary_checks", [])
    if not isinstance(checks, list):
        checks = []
    selected_output = result.get("selected_second_carrier_execution_output_basis", {})
    if not isinstance(selected_output, Mapping):
        selected_output = {}

    passed_count = sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed"))
    failed_count = sum(
        1 for check in checks if isinstance(check, Mapping) and not check.get("passed")
    )
    summary: dict[str, Any] = {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("reason"),
        "request_id": metadata.get("second_carrier_output_capture_boundary_request_id"),
        "question": declared.get("question"),
        "intent": declared.get("intent"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "selected_second_carrier_execution_output_outcome": selected_output.get("outcome"),
        "selected_second_carrier_execution_output_result_version": selected_output.get(
            "result_version"
        ),
        "selected_second_carrier_execution_output_failed_check_count": selected_output.get(
            "failed_check_count"
        ),
        "key_non_claims": {key: non_claims.get(key) for key in REQUIRED_FALSE_NON_CLAIMS},
        "no_capture_result_success_external_result_or_cross_carrier_evidence": not any(
            _as_bool(non_claims.get(key))
            for key in (
                "second_carrier_output_capture_created",
                "capture_artifact_created",
                "second_carrier_result_created",
                "second_carrier_success_created",
                "external_result_created",
                "cross_carrier_evidence_created",
            )
        ),
        "no_source_authority_currentness_final_completion_runtime": not any(
            _as_bool(non_claims.get(key))
            for key in (
                "source_created",
                "authority_created",
                "currentness_created",
                "final_completion_claimed",
                "runtime_hosting_created",
            )
        ),
        "no_deployment_public_release_or_follow_on": not any(
            _as_bool(non_claims.get(key))
            for key in (
                "deployment_created",
                "public_release_created",
                "follow_on_work_authorized",
            )
        ),
        "v1_predecessor_failure_preserved": not any(
            _as_bool(non_claims.get(key))
            for key in ("v1_repaired", "v1_hidden", "v1_claimed_passed")
        ),
        "v1_not_repaired_hidden_or_claimed_passed": not any(
            _as_bool(non_claims.get(key))
            for key in ("v1_repaired", "v1_hidden", "v1_claimed_passed")
        ),
    }
    for field in ALLOWED_TRUE_RECORDED_FIELDS:
        summary[field] = bool(statement.get(field))
    for field in REQUIRED_FALSE_NON_CLAIMS:
        summary[field] = bool(non_claims.get(field))
    return summary


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: list[dict[str, Any]],
    block: dict[str, Any],
) -> dict[str, Any]:
    request_id = str(
        request.get("second_carrier_output_capture_boundary_request_id")
        or "portable_source_body_verification_second_carrier_output_capture_boundary_request"
    )
    recorded = outcome == OUTCOME_RECORDED
    statement = _statement(recorded)
    failed_count = sum(1 for check in checks if not check.get("passed"))
    passed_count = sum(1 for check in checks if check.get("passed"))

    result: dict[str, Any] = {
        "portable_source_body_verification_second_carrier_output_capture_boundary_metadata": {
            "portable_source_body_verification_second_carrier_output_capture_boundary_result_id": (
                request_id
            ),
            "portable_source_body_verification_second_carrier_output_capture_boundary_result_type": (
                RESULT_TYPE
            ),
            "portable_source_body_verification_second_carrier_output_capture_boundary_result_version": (
                RESULT_VERSION
            ),
            "result_version": RESULT_VERSION,
            "generated_at": _now(),
            "resolver_module": RESOLVER_MODULE,
            "second_carrier_output_capture_boundary_request_id": request_id,
            "passed_check_count": passed_count,
            "failed_check_count": failed_count,
        },
        "declared_second_carrier_output_capture_boundary_question": {
            "second_carrier_output_capture_boundary_request_id": request_id,
            "question": request.get("second_carrier_output_capture_boundary_question"),
            "intent": request.get("second_carrier_output_capture_boundary_intent"),
        },
        "second_carrier_output_capture_boundary_scope": {
            "declared_scope": _scope_from_request(request),
            "supported_scope": list(SUPPORTED_SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_SCOPE),
            "unsupported_scope_values": [
                scope
                for scope in _scope_from_request(request)
                if scope not in SUPPORTED_SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_SCOPE
            ],
        },
        "second_carrier_output_capture_boundary_checks": checks,
        "second_carrier_output_capture_boundary_statement": statement,
        "second_carrier_output_capture_boundary_non_meaning": _non_meaning(),
        "additional_basis_required": {
            "requires_additional_basis": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "basis": _sanitize(request.get("additional_basis_context", {})),
            "missing_basis_not_scheduled": True,
            "missing_basis_not_authorized": True,
            "missing_basis_not_executed": True,
        },
        "not_recorded_basis": {
            "not_recorded": outcome == OUTCOME_NOT_RECORDED,
            "basis": _sanitize(request.get("not_recorded_basis", {})),
            "does_not_mutate_prior_artifacts": True,
            "does_not_repair_prior_artifacts": True,
            "does_not_authorize_next_work": True,
        },
        "what_remains_open": _what_remains_open(),
        "non_claims": _non_claims(),
        "outcome": outcome,
        "block": block,
    }

    for key in SELECTED_BASIS_KEYS:
        result[key] = _basis_section(request, key)
    for key in POSTURE_KEYS:
        result[key] = _posture_section(
            request,
            key,
            key.removesuffix("_posture").replace("_", "-"),
        )

    execution_output_section = result["selected_second_carrier_execution_output_basis"]
    execution_output_section.setdefault(
        "path",
        request.get("selected_second_carrier_execution_output_result_path"),
    )
    execution_output_section.setdefault(
        "result_id",
        request.get("selected_second_carrier_execution_output_result_id"),
    )
    execution_output_section.setdefault(
        "outcome",
        _execution_output_value(request, "outcome"),
    )
    execution_output_section.setdefault(
        "result_version",
        _first_declared(
            _execution_output_value(request, "result_version"),
            _execution_output_value(request, "version"),
        ),
    )
    execution_output_section.setdefault(
        "failed_check_count",
        _as_int(
            _first_declared(
                _execution_output_value(request, "failed_check_count"),
                _execution_output_value(request, "failed_checks"),
            ),
            default=None,
        ),
    )
    execution_output_section.setdefault(
        "bounded_second_carrier_execution_output_recorded",
        _execution_output_bool(
            request,
            "bounded_second_carrier_execution_output_recorded",
            "bounded_output_recorded",
            "second_carrier_execution_output_recorded",
            "output_recorded_bounded",
        ),
    )
    execution_output_section.setdefault(
        "output_not_capture",
        not _execution_output_negative_flag(
            request,
            ("treated_output_as_capture", "output_treated_as_capture"),
            ("output_not_capture",),
        ),
    )
    execution_output_section.setdefault(
        "second_carrier_output_capture_not_created",
        not _execution_output_negative_flag(
            request,
            ("already_created_output_capture", "output_capture_created"),
            ("second_carrier_output_capture_not_created", "capture_not_created"),
        ),
    )
    execution_output_section.setdefault("selected_basis_reference_shape_preserved", True)
    execution_output_section.setdefault("raw_full_prior_artifact_body_not_returned", True)

    summary = build_portable_source_body_verification_second_carrier_output_capture_boundary_summary(
        result
    )
    summary["passed_check_count"] = passed_count
    summary["failed_check_count"] = failed_count
    result[
        "portable_source_body_verification_second_carrier_output_capture_boundary_summary"
    ] = summary
    return _json_safe(result)


def _malformed_result(reason: str) -> dict[str, Any]:
    request = {
        "second_carrier_output_capture_boundary_request_id": (
            "malformed_second_carrier_output_capture_boundary_request"
        ),
        "second_carrier_output_capture_boundary_question": None,
        "second_carrier_output_capture_boundary_intent": None,
    }
    checks: list[dict[str, Any]] = []
    _check(
        checks,
        "declared_second_carrier_output_capture_boundary_request_mapping",
        False,
        "mapping request",
        reason,
        "DECLARED_SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_REQUEST_MALFORMED",
    )
    return _build_result(
        request,
        OUTCOME_BLOCKED,
        checks,
        _block(
            "DECLARED_SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_REQUEST_MALFORMED",
            reason,
        ),
    )


def resolve_portable_source_body_verification_second_carrier_output_capture_boundary(
    declared_second_carrier_output_capture_boundary_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded second-carrier output-capture-boundary posture."""

    if declared_second_carrier_output_capture_boundary_request is None:
        return _malformed_result("declared request is missing")
    if not isinstance(declared_second_carrier_output_capture_boundary_request, Mapping):
        return _malformed_result("declared request must be a mapping")

    request = copy.deepcopy(dict(declared_second_carrier_output_capture_boundary_request))
    checks = _build_checks(request)
    failure = _first_failure(checks)

    requested_outcome = request.get("requested_second_carrier_output_capture_boundary_outcome")
    if failure:
        code, name = failure
        return _build_result(request, OUTCOME_BLOCKED, checks, _block(code, f"blocked by {name}"))
    if requested_outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        return _build_result(request, OUTCOME_REQUIRES_ADDITIONAL_BASIS, checks, _empty_block())
    if (
        requested_outcome == OUTCOME_NOT_RECORDED
        or request.get("second_carrier_output_capture_boundary_intent") == INTENT_DO_NOT_RECORD
    ):
        return _build_result(request, OUTCOME_NOT_RECORDED, checks, _empty_block())
    return _build_result(request, OUTCOME_RECORDED, checks, _empty_block())


def resolve_portable_source_body_verification_second_carrier_output_capture_boundary_from_path(
    declared_second_carrier_output_capture_boundary_request_path: Path | str,
) -> dict[str, Any]:
    """Read a JSON request object from a path and resolve it."""

    path = Path(declared_second_carrier_output_capture_boundary_request_path)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise PortableSourceBodyVerificationSecondCarrierOutputCaptureBoundaryError(
            f"declared request path is missing: {path}"
        ) from exc
    except OSError as exc:
        raise PortableSourceBodyVerificationSecondCarrierOutputCaptureBoundaryError(
            f"declared request path is unreadable: {path}"
        ) from exc
    except json.JSONDecodeError as exc:
        raise PortableSourceBodyVerificationSecondCarrierOutputCaptureBoundaryError(
            f"declared request JSON is malformed: {path}"
        ) from exc
    if not isinstance(data, Mapping):
        return _malformed_result("declared request JSON must be an object")
    return resolve_portable_source_body_verification_second_carrier_output_capture_boundary(data)


def _safe_filename_part(value: Any) -> str:
    text = str(value or "second_carrier_output_capture_boundary_request").strip()
    safe = []
    for character in text:
        if character.isalnum() or character in {"-", "_", "."}:
            safe.append(character)
        else:
            safe.append("_")
    return "".join(safe).strip("._") or "second_carrier_output_capture_boundary_request"


def _with_suffix_if_exists(path: Path) -> Path:
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


def write_portable_source_body_verification_second_carrier_output_capture_boundary_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a bounded result JSON without silently overwriting existing files."""

    if not isinstance(result, Mapping):
        raise PortableSourceBodyVerificationSecondCarrierOutputCaptureBoundaryError(
            "result must be a mapping"
        )
    safe_result = _json_safe(result)
    metadata = safe_result.get(
        "portable_source_body_verification_second_carrier_output_capture_boundary_metadata",
        {},
    )
    if not isinstance(metadata, Mapping):
        metadata = {}
    request_id = metadata.get("second_carrier_output_capture_boundary_request_id") or metadata.get(
        "portable_source_body_verification_second_carrier_output_capture_boundary_result_id"
    )
    if output_path is None:
        filename = (
            f"{_safe_filename_part(request_id)}__"
            "portable_source_body_verification_second_carrier_output_capture_boundary_result.json"
        )
        path = OUTPUT_ROOT / filename
    else:
        path = Path(output_path)
    path = _with_suffix_if_exists(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(safe_result, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return path


def _reference_basis(label: str, **overrides: Any) -> dict[str, Any]:
    basis: dict[str, Any] = {
        "basis_label": label,
        "declared": True,
        "basis_declared": True,
        "basis_reference": f"synthetic://{label}",
        "path": f"synthetic://{label}.json",
        "result_path": f"synthetic://{label}.json",
        "reference_shaped_basis": True,
        "basis_remains_reference_shaped": True,
        "basis_reference_shape_preserved": True,
        "basis_remains_basis_only": True,
        "basis_is_not_capture": True,
        "basis_is_not_result": True,
        "basis_is_not_success": True,
        "basis_is_not_external_result": True,
        "basis_is_not_cross_carrier_evidence": True,
        "basis_is_not_source": True,
        "basis_is_not_authority": True,
        "basis_is_not_currentness": True,
        "basis_is_not_final_completion": True,
        "basis_is_not_runtime": True,
        "full_upstream_lineage_preserved": True,
        "raw_full_prior_artifact_body_returned": False,
        "prior_artifacts_mutated": False,
        "hidden_repo_state_excluded": True,
        "repo_local_availability_not_capture_authority": True,
        "receiving_carrier_not_authority": True,
        "authorization_token_reuse_blocked": True,
        "authorization_token_reused": False,
        "consumed_request_token_remains_closed": True,
        "consumed_request_reopened": False,
        "v1_repaired": False,
        "v1_hidden": False,
        "v1_claimed_passed": False,
    }
    basis.update(overrides)
    return basis


def build_declared_portable_source_body_verification_second_carrier_output_capture_boundary_request(
    second_carrier_output_capture_boundary_request_id: str = (
        "portable_source_body_verification_second_carrier_output_capture_boundary_reference_review_001"
    ),
    **overrides: Any,
) -> dict[str, Any]:
    """Build a valid bounded second-carrier output-capture-boundary request."""

    execution_output_statement = {
        "second_carrier_execution_output_recorded": True,
        "bounded_second_carrier_execution_output_recorded": True,
        "output_artifact_recorded_or_bounded": True,
        "output_recorded_bounded": True,
        "output_not_capture": True,
        "output_not_result": True,
        "output_not_success": True,
        "output_not_external_result": True,
        "output_not_cross_carrier_evidence": True,
        "second_carrier_output_capture_not_created": True,
        "second_carrier_result_not_created": True,
        "second_carrier_success_not_created": True,
        "external_result_not_created": True,
        "cross_carrier_evidence_not_created": True,
        "receiving_carrier_not_authority": True,
        "hidden_repo_state_excluded": True,
        "hidden_repo_state_not_used_as_output_authority": True,
        "repo_local_availability_not_output_authority": True,
        "selected_basis_reference_shape_preserved": True,
        "raw_full_prior_artifact_body_not_returned": True,
    }
    execution_output_basis = _reference_basis(
        "selected_second_carrier_execution_output_basis",
        outcome=SECOND_CARRIER_EXECUTION_OUTPUT_RECORDED,
        result_version=SECOND_CARRIER_EXECUTION_OUTPUT_RESULT_VERSION,
        failed_check_count=0,
        second_carrier_execution_output_statement=execution_output_statement,
        portable_source_body_verification_second_carrier_execution_output_metadata={
            "portable_source_body_verification_second_carrier_execution_output_result_version": (
                SECOND_CARRIER_EXECUTION_OUTPUT_RESULT_VERSION
            ),
            "result_version": SECOND_CARRIER_EXECUTION_OUTPUT_RESULT_VERSION,
            "failed_check_count": 0,
            "outcome": SECOND_CARRIER_EXECUTION_OUTPUT_RECORDED,
            "resolver_module": "resolve_portable_source_body_verification_second_carrier_execution_output",
        },
    )

    request: dict[str, Any] = {
        "second_carrier_output_capture_boundary_request_id": (
            second_carrier_output_capture_boundary_request_id
        ),
        "second_carrier_output_capture_boundary_question": CORE_QUESTION,
        "second_carrier_output_capture_boundary_intent": INTENT_RECORD,
        "second_carrier_output_capture_boundary_scope": list(
            SUPPORTED_SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_SCOPE
        ),
        "declared_non_claims": {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
        "selected_second_carrier_execution_output_basis": execution_output_basis,
        "selected_second_carrier_execution_output_result_outcome": (
            SECOND_CARRIER_EXECUTION_OUTPUT_RECORDED
        ),
        "selected_second_carrier_execution_output_result_version": (
            SECOND_CARRIER_EXECUTION_OUTPUT_RESULT_VERSION
        ),
        "selected_second_carrier_execution_output_failed_check_count": 0,
        "selected_second_carrier_execution_output_bounded_output_recorded": True,
        "selected_second_carrier_execution_output_already_created_output_capture": False,
        "selected_second_carrier_execution_output_already_created_second_carrier_result": (
            False
        ),
        "selected_second_carrier_execution_output_already_created_second_carrier_success": (
            False
        ),
        "selected_second_carrier_execution_output_created_external_result": False,
        "selected_second_carrier_execution_output_created_cross_carrier_evidence": False,
        "selected_second_carrier_execution_output_treated_output_as_capture": False,
        "selected_second_carrier_execution_output_treated_output_as_result": False,
        "selected_second_carrier_execution_output_treated_output_as_success": False,
        "selected_second_carrier_execution_output_treated_output_as_external_result": False,
        "selected_second_carrier_execution_output_treated_output_as_cross_carrier_evidence": (
            False
        ),
        "selected_second_carrier_execution_output_used_hidden_repo_state_as_capture_authority": (
            False
        ),
        "selected_second_carrier_execution_output_treated_repo_local_availability_as_capture_authority": (
            False
        ),
        "selected_second_carrier_execution_output_treated_receiving_carrier_as_authority": (
            False
        ),
        "selected_second_carrier_execution_output_raw_full_prior_artifact_body_returned_outside_bounded_output": (
            False
        ),
    }
    for key in SELECTED_BASIS_KEYS:
        request.setdefault(key, _reference_basis(key))
    for key in POSTURE_KEYS:
        request[key] = {
            "posture_declared": True,
            "declared": True,
            "posture_key": key,
            "preserves_capture_boundary_membrane": True,
        }
    request.update(overrides)
    return request
