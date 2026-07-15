"""Bounded portable source-body verification packet emission resolver.

This module is downstream of the recorded packet-emission-boundary v2 line. It
may record one bounded packet-emission posture only. Packet emission here is not
packet transfer, copying to another device, source transfer, source receipt,
reception authorization, second-carrier receipt, second-carrier execution,
external result capture, cross-carrier evidence review, source, authority,
currentness, runtime, final completion, continuation, reusable permission, or
follow-on work.

The v1 packet-emission-boundary resolver remains visible predecessor
conformance-failure evidence. This resolver does not repair it, hide it, or
claim it passed. It keeps selected basis sections reference-shaped, contains raw
or hidden-state payload values, imports no repo-local modules, runs no commands,
mutates no upstream artifact, and never returns a raw full prior artifact body
outside bounded emission posture.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


class PortableSourceBodyVerificationPacketEmissionError(Exception):
    """Raised for hard packet-emission input, output, or shape failures."""


RESOLVER_MODULE = "resolve_portable_source_body_verification_packet_emission"
RESULT_TYPE = "portable_source_body_verification_packet_emission_result"
RESULT_VERSION = "0.1.0"
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_portable_source_body_verification_packet_emission"
)

CORE_QUESTION = (
    "Can the packet-emission-boundary-v2 basis be used to emit one bounded packet "
    "without transferring it, copying it to another device, creating source transfer, "
    "creating source receipt, creating reception authorization, creating second-carrier "
    "receipt or execution, creating external result, creating cross-carrier evidence, "
    "or creating source, authority, currentness, runtime, final completion, "
    "continuation, reusable permission, derivative reception, vessel relation, "
    "another reception request, or follow-on work?"
)

OUTCOME_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_RECORDED"
OUTCOME_NOT_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION"
INTENT_BLOCK = "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

PACKET_EMISSION_BOUNDARY_V2_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_BOUNDARY_RECORDED"
)
PACKET_EMISSION_BOUNDARY_V2_RESULT_VERSION = "0.2.0"
PACKET_ARTIFACT_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_ARTIFACT_RECORDED"
PACKET_ARTIFACT_RESULT_VERSION = "0.1.0"
PACKET_BOUNDARY_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_BOUNDARY_RECORDED"
COMMAND_SUCCESS_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_RECORDED"
COMMAND_RESULT_V2_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_RECORDED"
OUTPUT_CAPTURE_V2_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_RECORDED"
COMMAND_OUTPUT_REPORT_ARTIFACT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_REPORT_ARTIFACT_RECORDED"
)

SUPPORTED_PACKET_EMISSION_SCOPE = frozenset(
    {
        "PACKET_EMISSION_SPEC_ONLY",
        "ONE_BOUNDED_PACKET_EMISSION_RECORDED",
        "PACKET_EMISSION_BOUNDARY_V2_BASIS_PRESERVED",
        "PACKET_EMISSION_BOUNDARY_V1_FAILURE_PRESERVED",
        "PACKET_ARTIFACT_BASIS_PRESERVED",
        "PACKET_ARTIFACT_NOT_TRANSFER",
        "EMITTED_PACKET_RECORDED_OR_BOUNDED",
        "PACKET_TRANSFER_NOT_AUTHORIZED",
        "COPY_TO_ANOTHER_DEVICE_NOT_AUTHORIZED",
        "SOURCE_TRANSFER_NOT_AUTHORIZED",
        "SOURCE_RECEIPT_NOT_CREATED",
        "RECEPTION_AUTHORIZATION_NOT_CREATED",
        "SECOND_CARRIER_RECEIPT_NOT_CREATED",
        "SECOND_CARRIER_EXECUTION_NOT_AUTHORIZED",
        "EXTERNAL_RESULT_NOT_CREATED",
        "CROSS_CARRIER_EVIDENCE_NOT_CREATED",
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
        "NO_TRANSFER_INFERENCE",
        "NO_COPY_INFERENCE",
        "NO_RECEIPT_INFERENCE",
        "NO_CROSS_CARRIER_EVIDENCE_INFERENCE",
        "NO_SOURCE_INFERENCE",
        "NO_AUTHORITY_INFERENCE",
        "NO_CURRENTNESS_INFERENCE",
        "NO_FINAL_COMPLETION_INFERENCE",
        "NO_RUNTIME_INFERENCE",
        "NO_FOLLOW_ON_WORK_INFERENCE",
        "NO_UNBOUNDED_PASS_FAIL_INFERENCE",
        "HIDDEN_REPO_STATE_EXCLUDED",
        "HIDDEN_REPO_STATE_NOT_USED_AS_EMISSION_AUTHORITY",
        "REPO_LOCAL_AVAILABILITY_NOT_EMISSION_AUTHORITY",
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
    }
)

SELECTED_BASIS_KEYS = (
    "selected_packet_emission_boundary_v2_basis",
    "selected_packet_emission_boundary_v2_terminal_summary_basis",
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
    "packet_emission_spec_only_posture",
    "one_bounded_packet_emission_posture",
    "packet_emission_boundary_v2_basis_preserved_posture",
    "packet_emission_boundary_v1_failure_preserved_posture",
    "packet_artifact_basis_preserved_posture",
    "emitted_packet_recorded_or_bounded_posture",
    "packet_transfer_not_authorized_posture",
    "copy_to_another_device_not_authorized_posture",
    "source_transfer_not_authorized_posture",
    "source_receipt_not_created_posture",
    "reception_authorization_not_created_posture",
    "second_carrier_receipt_not_created_posture",
    "second_carrier_execution_not_authorized_posture",
    "external_result_not_created_posture",
    "cross_carrier_evidence_not_created_posture",
    "source_not_created_posture",
    "authority_not_created_posture",
    "currentness_not_created_posture",
    "final_completion_not_created_posture",
    "runtime_not_created_posture",
    "continuation_not_authorized_posture",
    "reusable_permission_not_created_posture",
    "follow_on_work_not_authorized_posture",
    "hidden_repo_state_excluded_posture",
    "repo_local_availability_not_emission_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
)

REQUIRED_FALSE_NON_CLAIMS = (
    "packet_transferred",
    "packet_copied_to_another_device",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "second_carrier_receipt_created",
    "second_carrier_execution_created",
    "external_result_created",
    "cross_carrier_evidence_created",
    "packet_emission_treated_as_transfer",
    "packet_emission_treated_as_copy_to_another_device",
    "packet_emission_treated_as_source_transfer",
    "packet_emission_treated_as_source_receipt",
    "packet_emission_treated_as_reception_authorization",
    "packet_emission_treated_as_second_carrier_receipt",
    "packet_emission_treated_as_second_carrier_execution",
    "packet_emission_treated_as_cross_carrier_evidence",
    "packet_emission_treated_as_source",
    "packet_emission_treated_as_authority",
    "packet_emission_treated_as_currentness",
    "packet_emission_treated_as_final_completion",
    "packet_emission_treated_as_runtime",
    "packet_emission_treated_as_continuation",
    "packet_emission_treated_as_reusable_permission",
    "packet_emission_treated_as_follow_on_work",
    "emitted_packet_treated_as_source",
    "emitted_packet_treated_as_authority",
    "emitted_packet_treated_as_currentness",
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
    "artifact_existence_treated_as_emission_authority",
    "artifact_path_treated_as_currentness",
    "repo_local_availability_treated_as_emission_authority",
    "hidden_repo_state_used_as_emission_content",
    "hidden_repo_state_used_as_emission_authority",
    "raw_full_prior_artifact_body_returned",
    "prior_artifacts_mutated",
    "consumed_request_reopened",
    "authorization_token_reused",
    "v1_repaired",
    "v1_hidden",
    "v1_claimed_passed",
)

EXTRA_FALSE_NON_CLAIMS = (
    "full_prior_artifact_body_emitted_outside_bounded_emission",
    "artifacts_mutated",
    "mutation_performed",
    "packet_emission_boundary_v2_repaired_v1",
    "packet_emission_boundary_v2_hid_v1",
    "packet_emission_boundary_v2_claimed_v1_passed",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "packet_emission_recorded",
    "bounded_packet_emission_recorded",
    "packet_emission_boundary_v2_basis_preserved",
    "packet_emission_boundary_v1_failure_preserved",
    "packet_artifact_basis_preserved",
    "emitted_packet_recorded_or_bounded",
    "packet_transfer_not_authorized",
    "copy_to_another_device_not_authorized",
    "source_transfer_not_authorized",
    "source_receipt_not_created",
    "reception_authorization_not_created",
    "second_carrier_receipt_not_created",
    "second_carrier_execution_not_authorized",
    "external_result_not_created",
    "cross_carrier_evidence_not_created",
    "source_not_created",
    "authority_not_created",
    "currentness_not_created",
    "final_completion_not_created",
    "runtime_not_created",
    "continuation_not_authorized",
    "reusable_permission_not_created",
    "follow_on_work_not_authorized",
    "hidden_repo_state_excluded",
    "hidden_repo_state_not_used_as_emission_authority",
    "repo_local_availability_not_emission_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
)

RAW_BODY_KEYS = frozenset(
    {
        "raw_body",
        "raw_full_body",
        "full_body",
        "artifact_body",
        "raw_result_body",
        "raw_output_body",
        "emitted_packet_body",
        "packet_body",
        "source_body",
        "authority_body",
        "hidden_repo_state",
        "current_working_tree",
        "local_cache",
        "repo_local_only_dependency",
        "unlisted_file_dependency",
    }
)

RAW_SENTINELS = (
    "RAW_PACKET_EMISSION_BODY_MUST_NOT_RETURN",
    "RAW_PACKET_EMISSION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_PACKET_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)

BLOCK_CODES = frozenset(
    {
        "DECLARED_PACKET_EMISSION_REQUEST_MALFORMED",
        "DECLARED_PACKET_EMISSION_REQUEST_UNREADABLE",
        "PACKET_EMISSION_QUESTION_UNDECLARED",
        "PACKET_EMISSION_INTENT_UNSUPPORTED",
        "PACKET_EMISSION_EXPLICIT_BLOCK_INTENT",
        "PACKET_EMISSION_BOUNDARY_V2_BASIS_MISSING",
        "PACKET_EMISSION_BOUNDARY_V2_TERMINAL_SUMMARY_BASIS_MISSING",
        "PACKET_EMISSION_BOUNDARY_V1_PREDECESSOR_FAILURE_BASIS_MISSING",
        "PACKET_EMISSION_BOUNDARY_V2_NOT_RECORDED",
        "PACKET_EMISSION_BOUNDARY_V2_FAILED_CHECKS_PRESENT",
        "PACKET_EMISSION_BOUNDARY_V2_VERSION_NOT_0_2_0",
        "PACKET_EMISSION_BOUNDARY_V2_V1_FAILURE_EVIDENCE_MISSING",
        "PACKET_EMISSION_BOUNDARY_V2_REPAIRED_V1",
        "PACKET_EMISSION_BOUNDARY_V2_HID_V1",
        "PACKET_EMISSION_BOUNDARY_V2_CLAIMED_V1_PASSED",
        "PACKET_EMISSION_BOUNDARY_V2_DID_NOT_DECLARE_FUTURE_PACKET_EMISSION_STEP",
        "PACKET_EMISSION_BOUNDARY_V2_ALREADY_EMITTED_PACKET",
        "PACKET_EMISSION_BOUNDARY_V2_ALREADY_CREATED_EMITTED_PACKET",
        "PACKET_EMISSION_BOUNDARY_V2_AUTHORIZED_TRANSFER",
        "PACKET_EMISSION_BOUNDARY_V2_AUTHORIZED_COPY_TO_ANOTHER_DEVICE",
        "PACKET_EMISSION_BOUNDARY_V2_AUTHORIZED_SOURCE_TRANSFER",
        "PACKET_EMISSION_BOUNDARY_V2_AUTHORIZED_SOURCE_RECEIPT",
        "PACKET_EMISSION_BOUNDARY_V2_AUTHORIZED_RECEPTION",
        "PACKET_EMISSION_BOUNDARY_V2_AUTHORIZED_SECOND_CARRIER_RECEIPT",
        "PACKET_EMISSION_BOUNDARY_V2_AUTHORIZED_SECOND_CARRIER_EXECUTION",
        "PACKET_EMISSION_BOUNDARY_V2_CREATED_EXTERNAL_RESULT",
        "PACKET_EMISSION_BOUNDARY_V2_CREATED_CROSS_CARRIER_EVIDENCE",
        "PACKET_EMISSION_BOUNDARY_V2_USED_HIDDEN_REPO_STATE_AS_EMISSION_AUTHORITY",
        "PACKET_EMISSION_BOUNDARY_V2_TREATED_REPO_LOCAL_AVAILABILITY_AS_EMISSION_AUTHORITY",
        "PACKET_EMISSION_BOUNDARY_V2_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY",
        "PACKET_ARTIFACT_BASIS_MISSING",
        "PACKET_ARTIFACT_NOT_RECORDED",
        "PACKET_ARTIFACT_FAILED_CHECKS_PRESENT",
        "PACKET_BOUNDARY_BASIS_MISSING",
        "COMMAND_SUCCESS_BASIS_MISSING",
        "COMMAND_SUCCESS_NOT_RECORDED",
        "COMMAND_RESULT_V2_BASIS_MISSING",
        "COMMAND_RESULT_V2_NOT_RECORDED",
        "OUTPUT_CAPTURE_V2_BASIS_MISSING",
        "OUTPUT_CAPTURE_V2_NOT_RECORDED",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_BASIS_MISSING",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_NOT_RECORDED",
        "COMMAND_EXECUTION_BASIS_MISSING",
        "EXECUTION_TRACE_NOT_AUDIT_ONLY",
        "COMMAND_REPORT_LINEAGE_BASIS_MISSING",
        "COMMAND_REPORT_LINEAGE_NOT_LINEAGE_ONLY",
        "EVIDENCE_MANIFEST_BASIS_MISSING",
        "ARTIFACT_CONTAINMENT_BASIS_MISSING",
        "PORTABLE_VERIFICATION_BASIS_MISSING",
        "PACKET_EMISSION_SPEC_ONLY_POSTURE_MISSING",
        "ONE_BOUNDED_PACKET_EMISSION_POSTURE_MISSING",
        "PACKET_EMISSION_BOUNDARY_V2_BASIS_PRESERVED_POSTURE_MISSING",
        "PACKET_EMISSION_BOUNDARY_V1_FAILURE_PRESERVED_POSTURE_MISSING",
        "PACKET_ARTIFACT_BASIS_PRESERVED_POSTURE_MISSING",
        "EMITTED_PACKET_RECORDED_OR_BOUNDED_POSTURE_MISSING",
        "PACKET_TRANSFER_NOT_AUTHORIZED_POSTURE_MISSING",
        "COPY_TO_ANOTHER_DEVICE_NOT_AUTHORIZED_POSTURE_MISSING",
        "SOURCE_TRANSFER_NOT_AUTHORIZED_POSTURE_MISSING",
        "SOURCE_RECEIPT_NOT_CREATED_POSTURE_MISSING",
        "RECEPTION_AUTHORIZATION_NOT_CREATED_POSTURE_MISSING",
        "SECOND_CARRIER_RECEIPT_NOT_CREATED_POSTURE_MISSING",
        "SECOND_CARRIER_EXECUTION_NOT_AUTHORIZED_POSTURE_MISSING",
        "EXTERNAL_RESULT_NOT_CREATED_POSTURE_MISSING",
        "CROSS_CARRIER_EVIDENCE_NOT_CREATED_POSTURE_MISSING",
        "NO_SOURCE_AUTHORITY_CURRENTNESS_FINAL_COMPLETION_RUNTIME_FOLLOW_ON_POSTURE_MISSING",
        "HIDDEN_REPO_STATE_EXCLUDED_POSTURE_MISSING",
        "REPO_LOCAL_AVAILABILITY_NOT_EMISSION_AUTHORITY_POSTURE_MISSING",
        "SELECTED_BASIS_REFERENCE_SHAPE_POSTURE_MISSING",
        "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED_POSTURE_MISSING",
        "PACKET_EMISSION_TREATED_AS_TRANSFER",
        "PACKET_EMISSION_TREATED_AS_COPY_TO_ANOTHER_DEVICE",
        "PACKET_EMISSION_TREATED_AS_SOURCE_TRANSFER",
        "PACKET_EMISSION_TREATED_AS_SOURCE_RECEIPT",
        "PACKET_EMISSION_TREATED_AS_RECEPTION_AUTHORIZATION",
        "PACKET_EMISSION_TREATED_AS_SECOND_CARRIER_RECEIPT",
        "PACKET_EMISSION_TREATED_AS_SECOND_CARRIER_EXECUTION",
        "PACKET_EMISSION_TREATED_AS_CROSS_CARRIER_EVIDENCE",
        "PACKET_EMISSION_TREATED_AS_SOURCE",
        "PACKET_EMISSION_TREATED_AS_AUTHORITY",
        "PACKET_EMISSION_TREATED_AS_CURRENTNESS",
        "PACKET_EMISSION_TREATED_AS_FINAL_COMPLETION",
        "PACKET_EMISSION_TREATED_AS_RUNTIME",
        "PACKET_EMISSION_TREATED_AS_CONTINUATION",
        "PACKET_EMISSION_TREATED_AS_REUSABLE_PERMISSION",
        "PACKET_EMISSION_TREATED_AS_FOLLOW_ON_WORK",
        "EMITTED_PACKET_TREATED_AS_SOURCE",
        "EMITTED_PACKET_TREATED_AS_AUTHORITY",
        "EMITTED_PACKET_TREATED_AS_CURRENTNESS",
        "PACKET_TRANSFERRED",
        "PACKET_COPIED_TO_ANOTHER_DEVICE",
        "SOURCE_TRANSFER_OCCURRED",
        "SOURCE_RECEIPT_OCCURRED",
        "RECEPTION_AUTHORIZATION_CREATED",
        "SECOND_CARRIER_RECEIPT_CREATED",
        "SECOND_CARRIER_EXECUTION_CREATED",
        "EXTERNAL_RESULT_CREATED",
        "CROSS_CARRIER_EVIDENCE_CREATED",
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
        "ARTIFACT_EXISTENCE_TREATED_AS_EMISSION_AUTHORITY",
        "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_EMISSION_AUTHORITY",
        "HIDDEN_REPO_STATE_USED_AS_EMISSION_CONTENT",
        "HIDDEN_REPO_STATE_USED_AS_EMISSION_AUTHORITY",
        "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
        "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        "PREDECESSOR_FAILURE_EVIDENCE_NOT_VISIBLE",
        "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENT_REPORT_ARTIFACT",
        "COMMAND_REPORT_LINEAGE_TREATED_AS_SOURCE",
        "COMMAND_REPORT_LINEAGE_TREATED_AS_AUTHORITY",
        "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENTNESS",
        "CONSUMED_REQUEST_REOPENED",
        "AUTHORIZATION_TOKEN_REUSED",
        "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_EMISSION",
        "ARTIFACTS_MUTATED",
        "MUTATION_PERFORMED",
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "UNSUPPORTED_PACKET_EMISSION_SCOPE",
    }
)

NON_CLAIM_TO_BLOCK_CODE = {
    "packet_transferred": "PACKET_TRANSFERRED",
    "packet_copied_to_another_device": "PACKET_COPIED_TO_ANOTHER_DEVICE",
    "source_transfer_occurred": "SOURCE_TRANSFER_OCCURRED",
    "source_receipt_occurred": "SOURCE_RECEIPT_OCCURRED",
    "reception_authorization_created": "RECEPTION_AUTHORIZATION_CREATED",
    "second_carrier_receipt_created": "SECOND_CARRIER_RECEIPT_CREATED",
    "second_carrier_execution_created": "SECOND_CARRIER_EXECUTION_CREATED",
    "external_result_created": "EXTERNAL_RESULT_CREATED",
    "cross_carrier_evidence_created": "CROSS_CARRIER_EVIDENCE_CREATED",
    "packet_emission_treated_as_transfer": "PACKET_EMISSION_TREATED_AS_TRANSFER",
    "packet_emission_treated_as_copy_to_another_device": (
        "PACKET_EMISSION_TREATED_AS_COPY_TO_ANOTHER_DEVICE"
    ),
    "packet_emission_treated_as_source_transfer": "PACKET_EMISSION_TREATED_AS_SOURCE_TRANSFER",
    "packet_emission_treated_as_source_receipt": "PACKET_EMISSION_TREATED_AS_SOURCE_RECEIPT",
    "packet_emission_treated_as_reception_authorization": (
        "PACKET_EMISSION_TREATED_AS_RECEPTION_AUTHORIZATION"
    ),
    "packet_emission_treated_as_second_carrier_receipt": (
        "PACKET_EMISSION_TREATED_AS_SECOND_CARRIER_RECEIPT"
    ),
    "packet_emission_treated_as_second_carrier_execution": (
        "PACKET_EMISSION_TREATED_AS_SECOND_CARRIER_EXECUTION"
    ),
    "packet_emission_treated_as_cross_carrier_evidence": (
        "PACKET_EMISSION_TREATED_AS_CROSS_CARRIER_EVIDENCE"
    ),
    "packet_emission_treated_as_source": "PACKET_EMISSION_TREATED_AS_SOURCE",
    "packet_emission_treated_as_authority": "PACKET_EMISSION_TREATED_AS_AUTHORITY",
    "packet_emission_treated_as_currentness": "PACKET_EMISSION_TREATED_AS_CURRENTNESS",
    "packet_emission_treated_as_final_completion": (
        "PACKET_EMISSION_TREATED_AS_FINAL_COMPLETION"
    ),
    "packet_emission_treated_as_runtime": "PACKET_EMISSION_TREATED_AS_RUNTIME",
    "packet_emission_treated_as_continuation": "PACKET_EMISSION_TREATED_AS_CONTINUATION",
    "packet_emission_treated_as_reusable_permission": (
        "PACKET_EMISSION_TREATED_AS_REUSABLE_PERMISSION"
    ),
    "packet_emission_treated_as_follow_on_work": "PACKET_EMISSION_TREATED_AS_FOLLOW_ON_WORK",
    "emitted_packet_treated_as_source": "EMITTED_PACKET_TREATED_AS_SOURCE",
    "emitted_packet_treated_as_authority": "EMITTED_PACKET_TREATED_AS_AUTHORITY",
    "emitted_packet_treated_as_currentness": "EMITTED_PACKET_TREATED_AS_CURRENTNESS",
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
    "artifact_existence_treated_as_emission_authority": (
        "ARTIFACT_EXISTENCE_TREATED_AS_EMISSION_AUTHORITY"
    ),
    "artifact_path_treated_as_currentness": "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "repo_local_availability_treated_as_emission_authority": (
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_EMISSION_AUTHORITY"
    ),
    "hidden_repo_state_used_as_emission_content": "HIDDEN_REPO_STATE_USED_AS_EMISSION_CONTENT",
    "hidden_repo_state_used_as_emission_authority": "HIDDEN_REPO_STATE_USED_AS_EMISSION_AUTHORITY",
    "raw_full_prior_artifact_body_returned": "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "prior_artifacts_mutated": "ARTIFACTS_MUTATED",
    "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
    "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
    "v1_repaired": "PACKET_EMISSION_BOUNDARY_V2_REPAIRED_V1",
    "v1_hidden": "PACKET_EMISSION_BOUNDARY_V2_HID_V1",
    "v1_claimed_passed": "PACKET_EMISSION_BOUNDARY_V2_CLAIMED_V1_PASSED",
    "full_prior_artifact_body_emitted_outside_bounded_emission": (
        "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_EMISSION"
    ),
    "artifacts_mutated": "ARTIFACTS_MUTATED",
    "mutation_performed": "MUTATION_PERFORMED",
    "packet_emission_boundary_v2_repaired_v1": "PACKET_EMISSION_BOUNDARY_V2_REPAIRED_V1",
    "packet_emission_boundary_v2_hid_v1": "PACKET_EMISSION_BOUNDARY_V2_HID_V1",
    "packet_emission_boundary_v2_claimed_v1_passed": (
        "PACKET_EMISSION_BOUNDARY_V2_CLAIMED_V1_PASSED"
    ),
}


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _copy(value: Any) -> Any:
    return copy.deepcopy(value)


def _is_mapping(value: Any) -> bool:
    return hasattr(value, "items") and hasattr(value, "get")


def _safe_text(value: str) -> str:
    sanitized = value
    for sentinel in RAW_SENTINELS:
        sanitized = sanitized.replace(sentinel, "[bounded-redacted-raw-or-hidden-state]")
    return sanitized


def _raw_key(key: str) -> bool:
    lowered = key.lower()
    return lowered in RAW_BODY_KEYS or lowered.endswith("_body")


def _json_safe(value: Any) -> Any:
    if _is_mapping(value):
        result: dict[str, Any] = {}
        for key, nested in value.items():
            key_text = str(key)
            if _raw_key(key_text) and not isinstance(nested, (bool, int, float, type(None))):
                result[key_text] = "[bounded-redacted-raw-or-hidden-state]"
            else:
                result[key_text] = _json_safe(nested)
        return result
    if isinstance(value, list):
        return [_json_safe(item) for item in value]
    if isinstance(value, tuple):
        return [_json_safe(item) for item in value]
    if isinstance(value, set):
        return sorted(_json_safe(item) for item in value)
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, str):
        return _safe_text(value)
    return value


def _basis(request: Mapping[str, Any], key: str) -> Mapping[str, Any]:
    value = request.get(key)
    return value if _is_mapping(value) else {}


def _search_nested(value: Any, names: Sequence[str]) -> Any:
    if _is_mapping(value):
        for name in names:
            if name in value:
                return value[name]
        for nested_key in (
            "portable_source_body_verification_packet_emission_metadata",
            "portable_source_body_verification_packet_emission_summary",
            "portable_source_body_verification_packet_emission_boundary_metadata",
            "portable_source_body_verification_packet_emission_boundary_summary",
            "portable_source_body_verification_packet_artifact_metadata",
            "portable_source_body_verification_packet_artifact_summary",
            "metadata",
            "summary",
            "statement",
            "packet_emission_statement",
            "packet_emission_boundary_statement",
            "packet_artifact_statement",
            "non_claims",
        ):
            nested = value.get(nested_key)
            if _is_mapping(nested):
                found = _search_nested(nested, names)
                if found is not None:
                    return found
    return None


def _value(
    request: Mapping[str, Any],
    names: Sequence[str],
    basis_key: str | None = None,
    default: Any = None,
) -> Any:
    for name in names:
        if name in request:
            return request[name]
    if basis_key is not None:
        found = _search_nested(_basis(request, basis_key), names)
        if found is not None:
            return found
    for section_key in SELECTED_BASIS_KEYS:
        if section_key == basis_key:
            continue
        found = _search_nested(_basis(request, section_key), names)
        if found is not None:
            return found
    return default


def _any_true(
    request: Mapping[str, Any],
    names: Sequence[str],
    basis_key: str | None = None,
) -> bool:
    for name in names:
        if request.get(name) is True:
            return True
    keys = (basis_key,) if basis_key is not None else SELECTED_BASIS_KEYS
    for section_key in keys:
        if section_key is None:
            continue
        basis = _basis(request, section_key)
        for name in names:
            if _search_nested(basis, (name,)) is True:
                return True
    if basis_key is not None:
        for section_key in SELECTED_BASIS_KEYS:
            if section_key == basis_key:
                continue
            basis = _basis(request, section_key)
            for name in names:
                if _search_nested(basis, (name,)) is True:
                    return True
    return False


def _as_int(value: Any, default: int | None = None) -> int | None:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, float) and value.is_integer():
        return int(value)
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            return default
    return default


def _declared(value: Any) -> bool:
    if value is None or value is False:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if _is_mapping(value):
        if value.get("declared") is False or value.get("basis_declared") is False:
            return False
        return bool(value)
    if isinstance(value, (list, tuple, set)):
        return bool(value)
    return True


def _check(
    checks: list[dict[str, Any]],
    name: str,
    passed: bool,
    expected: Any,
    actual: Any,
    code: str,
) -> None:
    if code not in BLOCK_CODES:
        raise PortableSourceBodyVerificationPacketEmissionError(
            f"internal block code is not public: {code}"
        )
    checks.append(
        {
            "check_name": name,
            "passed": bool(passed),
            "expected_posture": _json_safe(expected),
            "actual_posture": _json_safe(actual),
            "block_code": None if passed else code,
            "failure_code": None if passed else code,
        }
    )


def _failed_code(checks: Sequence[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if not check.get("passed"):
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str):
                return code
    return None


def _scope_values(request: Mapping[str, Any]) -> list[str]:
    scope = request.get("packet_emission_scope")
    if scope is None:
        return sorted(SUPPORTED_PACKET_EMISSION_SCOPE)
    if isinstance(scope, str):
        return [scope]
    if _is_mapping(scope):
        values = scope.get("scope_values") or scope.get("values") or scope.get("scope")
        if isinstance(values, str):
            return [values]
        if isinstance(values, (list, tuple, set)):
            return [str(item) for item in values]
        return []
    if isinstance(scope, (list, tuple, set)):
        return [str(item) for item in scope]
    return []


def _non_claims_from_request(request: Mapping[str, Any]) -> dict[str, Any]:
    declared = request.get("declared_non_claims")
    result = dict(declared) if _is_mapping(declared) else {}
    for key in REQUIRED_FALSE_NON_CLAIMS + EXTRA_FALSE_NON_CLAIMS:
        if key in request and key not in result:
            result[key] = request[key]
    return result


def _all_selected_basis_reference_shaped(request: Mapping[str, Any]) -> bool:
    if request.get("reference_shaped_input_posture") is False:
        return False
    for key in SELECTED_BASIS_KEYS:
        basis = _basis(request, key)
        if basis.get("reference_shaped") is False:
            return False
        if basis.get("selected_basis_reference_shape_preserved") is False:
            return False
        if basis.get("copy_shaped") is True and basis.get("bounded_copy_shape") is not True:
            return False
    return True


def _all_raw_full_prior_body_not_returned(request: Mapping[str, Any]) -> bool:
    if request.get("raw_full_prior_artifact_body_returned") is True:
        return False
    if request.get("full_prior_artifact_body_emitted_outside_bounded_emission") is True:
        return False
    for key in SELECTED_BASIS_KEYS:
        basis = _basis(request, key)
        if basis.get("raw_full_prior_artifact_body_returned") is True:
            return False
        if basis.get("full_prior_artifact_body_emitted_outside_bounded_emission") is True:
            return False
    return True


def _hidden_repo_state_excluded(request: Mapping[str, Any]) -> bool:
    if request.get("hidden_repo_state_excluded") is False:
        return False
    if request.get("hidden_repo_state_used_as_emission_content") is True:
        return False
    if request.get("hidden_repo_state_used_as_emission_authority") is True:
        return False
    for key in SELECTED_BASIS_KEYS:
        basis = _basis(request, key)
        if basis.get("hidden_repo_state_excluded") is False:
            return False
        if basis.get("hidden_repo_state_used_as_emission_content") is True:
            return False
        if basis.get("hidden_repo_state_used_as_emission_authority") is True:
            return False
    return True


def _safe_basis_section(label: str, basis_value: Any, request: Mapping[str, Any]) -> dict[str, Any]:
    basis = _json_safe(_copy(basis_value)) if _is_mapping(basis_value) else {}
    basis.setdefault("basis_label", label)
    basis.setdefault("declared", _declared(basis_value))
    basis.setdefault("basis_only", True)
    basis.setdefault("reference_shaped", True)
    basis.setdefault("selected_basis_reference_shape_preserved", True)
    basis.setdefault("full_prior_artifact_body_embedded", False)
    basis.setdefault("raw_full_prior_artifact_body_returned", False)
    basis.setdefault("hidden_repo_state_excluded", True)
    basis.setdefault("hidden_repo_state_used_as_emission_content", False)
    basis.setdefault("hidden_repo_state_used_as_emission_authority", False)
    basis.setdefault("hidden_repo_state_not_used_as_emission_authority", True)
    basis.setdefault("repo_local_availability_not_emission_authority", True)
    basis.setdefault("repo_local_availability_treated_as_emission_authority", False)
    basis.setdefault("artifact_existence_treated_as_emission_authority", False)
    basis.setdefault("artifact_path_treated_as_currentness", False)

    if label == "selected_packet_emission_boundary_v2_basis":
        basis.setdefault(
            "selected_packet_emission_boundary_v2_result_path",
            request.get("selected_packet_emission_boundary_v2_result_path"),
        )
        basis.setdefault(
            "selected_packet_emission_boundary_v2_result_id",
            request.get("selected_packet_emission_boundary_v2_result_id"),
        )
        basis.setdefault(
            "outcome",
            request.get(
                "selected_packet_emission_boundary_v2_result_outcome",
                PACKET_EMISSION_BOUNDARY_V2_RECORDED,
            ),
        )
        basis.setdefault(
            "result_version",
            request.get(
                "selected_packet_emission_boundary_v2_result_version",
                PACKET_EMISSION_BOUNDARY_V2_RESULT_VERSION,
            ),
        )
        basis.setdefault(
            "failed_check_count",
            request.get("selected_packet_emission_boundary_v2_failed_check_count", 0),
        )
        basis.setdefault("v1_predecessor_failure_preserved", True)
        basis.setdefault("v1_repaired", False)
        basis.setdefault("v1_hidden", False)
        basis.setdefault("v1_claimed_passed", False)
        basis.setdefault("v2_successor_does_not_erase_v1", True)
        basis.setdefault("one_future_packet_emission_step_declared", True)
        basis.setdefault("packet_not_emitted", True)
        basis.setdefault("packet_emitted", False)
        basis.setdefault("emitted_packet_not_created", True)
        basis.setdefault("emitted_packet_created", False)
        basis.setdefault("packet_transfer_not_authorized", True)
        basis.setdefault("packet_transfer_authorized", False)
        basis.setdefault("copy_to_another_device_not_authorized", True)
        basis.setdefault("copy_to_another_device_authorized", False)
        basis.setdefault("source_transfer_not_authorized", True)
        basis.setdefault("source_transfer_authorized", False)
        basis.setdefault("source_receipt_not_created", True)
        basis.setdefault("source_receipt_authorized", False)
        basis.setdefault("reception_authorization_not_created", True)
        basis.setdefault("reception_authorization_created", False)
        basis.setdefault("second_carrier_receipt_not_created", True)
        basis.setdefault("second_carrier_receipt_created", False)
        basis.setdefault("second_carrier_execution_not_authorized", True)
        basis.setdefault("second_carrier_execution_authorized", False)
        basis.setdefault("external_result_not_created", True)
        basis.setdefault("external_result_created", False)
        basis.setdefault("cross_carrier_evidence_not_created", True)
        basis.setdefault("cross_carrier_evidence_created", False)

    if label == "selected_packet_emission_boundary_v2_terminal_summary_basis":
        basis.setdefault("terminal_summary_only", True)
        basis.setdefault("packet_emission_boundary_v2_terminal_summary_standing_if_present", True)

    if label == "selected_packet_emission_boundary_v1_predecessor_failure_basis":
        basis.setdefault("predecessor_failure_evidence_visible", True)
        basis.setdefault("v1_predecessor_failure_preserved", True)
        basis.setdefault("v1_repaired", False)
        basis.setdefault("v1_hidden", False)
        basis.setdefault("v1_claimed_passed", False)
        basis.setdefault("observed_failure_count", 85)
        basis.setdefault(
            "failure_shape",
            "generated hidden-repo-state posture, non-claim, and summary booleans "
            "were redacted into [bounded-redacted-raw-or-hidden-state]",
        )

    if label == "selected_packet_artifact_basis":
        basis.setdefault("selected_packet_artifact_result_path", request.get("selected_packet_artifact_result_path"))
        basis.setdefault("selected_packet_artifact_result_id", request.get("selected_packet_artifact_result_id"))
        basis.setdefault("outcome", request.get("selected_packet_artifact_result_outcome", PACKET_ARTIFACT_RECORDED))
        basis.setdefault("result_version", request.get("selected_packet_artifact_result_version", PACKET_ARTIFACT_RESULT_VERSION))
        basis.setdefault("failed_check_count", request.get("selected_packet_artifact_failed_check_count", 0))
        basis.setdefault("packet_artifact_recorded", True)
        basis.setdefault("local_packet_artifact_recorded", True)
        basis.setdefault("packet_artifact_not_emission_authority", True)
        basis.setdefault("packet_artifact_not_transfer", True)

    return basis


def _posture_section(name: str, request: Mapping[str, Any], recorded: bool) -> dict[str, Any]:
    supplied = request.get(name)
    posture = _json_safe(_copy(supplied)) if _is_mapping(supplied) else {}
    posture.setdefault("posture_name", name)
    posture.setdefault("declared", _declared(supplied))
    posture.setdefault("packet_emission_posture_only", True)
    posture.setdefault("recorded_packet_emission_outcome_only", recorded)
    posture.setdefault("one_bounded_packet_emission_posture", True)
    posture.setdefault("packet_emission_boundary_v2_basis_preserved", True)
    posture.setdefault("packet_emission_boundary_v1_failure_preserved", True)
    posture.setdefault("packet_artifact_basis_preserved", True)
    posture.setdefault("emitted_packet_recorded_or_bounded", recorded)
    posture.setdefault("packet_transfer_not_authorized", True)
    posture.setdefault("copy_to_another_device_not_authorized", True)
    posture.setdefault("source_transfer_not_authorized", True)
    posture.setdefault("source_receipt_not_created", True)
    posture.setdefault("reception_authorization_not_created", True)
    posture.setdefault("second_carrier_receipt_not_created", True)
    posture.setdefault("second_carrier_execution_not_authorized", True)
    posture.setdefault("external_result_not_created", True)
    posture.setdefault("cross_carrier_evidence_not_created", True)
    posture.setdefault("source_not_created", True)
    posture.setdefault("authority_not_created", True)
    posture.setdefault("currentness_not_created", True)
    posture.setdefault("final_completion_not_created", True)
    posture.setdefault("runtime_not_created", True)
    posture.setdefault("continuation_not_authorized", True)
    posture.setdefault("reusable_permission_not_created", True)
    posture.setdefault("follow_on_work_not_authorized", True)
    posture.setdefault("hidden_repo_state_excluded", True)
    posture.setdefault("hidden_repo_state_not_used_as_emission_authority", True)
    posture.setdefault("repo_local_availability_not_emission_authority", True)
    posture.setdefault("selected_basis_reference_shape_preserved", True)
    posture.setdefault("raw_full_prior_artifact_body_not_returned", True)
    posture.setdefault("authorization_token_reuse_blocked", True)
    posture.setdefault("consumed_request_token_remains_closed", True)
    return posture


def _statement(recorded: bool) -> dict[str, Any]:
    statement = {key: bool(recorded) for key in ALLOWED_TRUE_RECORDED_FIELDS}
    statement.update({key: False for key in REQUIRED_FALSE_NON_CLAIMS})
    statement.update({key: False for key in EXTRA_FALSE_NON_CLAIMS})
    statement.update(
        {
            "packet_emission_is_one_bounded_local_emission_posture_only": True,
            "packet_emission_is_not_packet_transfer": True,
            "packet_emission_is_not_copying_to_another_device": True,
            "packet_emission_is_not_source_transfer": True,
            "packet_emission_is_not_source_receipt": True,
            "packet_emission_is_not_reception_authorization": True,
            "packet_emission_is_not_second_carrier_receipt": True,
            "packet_emission_is_not_second_carrier_execution": True,
            "packet_emission_is_not_external_result_capture": True,
            "packet_emission_is_not_cross_carrier_evidence_review": True,
            "packet_emission_is_not_source": True,
            "packet_emission_is_not_authority": True,
            "packet_emission_is_not_currentness": True,
            "packet_emission_is_not_final_completion": True,
            "packet_emission_is_not_runtime": True,
            "packet_emission_is_not_continuation": True,
            "packet_emission_is_not_reusable_permission": True,
            "packet_emission_is_not_derivative_reception": True,
            "packet_emission_is_not_vessel_relation": True,
            "packet_emission_is_not_another_reception_request": True,
            "packet_emission_is_not_follow_on_work": True,
            "emitted_packet_is_not_source": True,
            "emitted_packet_is_not_authority": True,
            "emitted_packet_is_not_currentness": True,
            "packet_emission_boundary_v2_remains_boundary_basis_only": True,
            "packet_emission_boundary_v1_remains_visible_predecessor_failure_evidence": True,
            "packet_artifact_remains_local_packet_artifact_posture_only": True,
            "packet_artifact_is_not_emission_authority": True,
            "packet_boundary_remains_boundary_basis_only": True,
            "local_command_success_remains_local_command_success_posture_only": True,
            "command_result_v2_remains_command_result_posture_only": True,
            "output_capture_v2_remains_output_capture_posture_only": True,
            "execution_trace_remains_audit_only": True,
            "packet_transfer_requires_separate_bounded_step": True,
            "second_carrier_receipt_or_execution_requires_separate_bounded_step": True,
            "cross_carrier_evidence_review_requires_separate_bounded_step": True,
            "source_authority_currentness_final_completion_runtime_requires_separate_bounded_step": True,
        }
    )
    return statement


def _non_meaning() -> dict[str, bool]:
    return {
        "packet_was_transferred": False,
        "packet_was_copied_to_another_device": False,
        "source_transfer_occurred": False,
        "source_receipt_occurred": False,
        "reception_authorization_exists": False,
        "second_carrier_received_anything": False,
        "second_carrier_executed_anything": False,
        "external_result_exists": False,
        "cross_carrier_evidence_exists": False,
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
        "packet_emission_became_source_transfer": False,
        "packet_emission_became_source_receipt": False,
        "packet_emission_became_reception_authorization": False,
        "packet_emission_became_cross_carrier_proof": False,
        "emitted_packet_became_source": False,
        "emitted_packet_became_authority": False,
        "emitted_packet_became_currentness": False,
        "artifact_existence_became_emission_authority": False,
        "artifact_path_became_currentness": False,
        "repo_local_availability_became_emission_authority": False,
        "hidden_repo_state_became_emission_authority": False,
        "v1_packet_emission_boundary_resolver_was_repaired_hidden_erased_or_claimed_passed": False,
    }


def _additional_basis_required(request: Mapping[str, Any], outcome: str) -> dict[str, Any]:
    if outcome != OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        return {
            "additional_basis_required": False,
            "missing_or_unclear_basis": [],
            "missing_basis_scheduled": False,
            "missing_basis_authorized": False,
            "missing_basis_executed": False,
        }
    context = request.get("additional_basis_context")
    missing: list[str] = []
    reason = "Additional packet-emission basis is required."
    if _is_mapping(context):
        supplied_missing = context.get("missing_or_unclear_basis")
        if isinstance(supplied_missing, (list, tuple, set)):
            missing = [str(item) for item in supplied_missing]
        reason = str(context.get("reason") or reason)
    return {
        "additional_basis_required": True,
        "reason": reason,
        "missing_or_unclear_basis": missing or ["packet_emission_basis_unclear"],
        "missing_basis_scheduled": False,
        "missing_basis_authorized": False,
        "missing_basis_executed": False,
        "packet_transferred": False,
        "packet_copied_to_another_device": False,
        "source_receipt_occurred": False,
        "second_carrier_execution_created": False,
        "cross_carrier_evidence_created": False,
        "source_created": False,
        "authority_created": False,
        "currentness_created": False,
        "final_completion_claimed": False,
        "runtime_hosting_created": False,
        "follow_on_work_authorized": False,
    }


def _not_recorded_basis(request: Mapping[str, Any], outcome: str, failed_code: str | None) -> dict[str, Any]:
    if outcome != OUTCOME_NOT_RECORDED:
        return {"not_recorded": False, "reason": None, "mutation_performed": False}
    supplied = request.get("not_recorded_basis")
    reason = (
        supplied.get("reason")
        if _is_mapping(supplied) and supplied.get("reason")
        else failed_code or "Packet-emission request was not recorded."
    )
    return {
        "not_recorded": True,
        "reason": reason,
        "packet_transferred": False,
        "packet_copied_to_another_device": False,
        "source_transfer_occurred": False,
        "source_receipt_occurred": False,
        "source_created": False,
        "authority_created": False,
        "currentness_created": False,
        "final_completion_claimed": False,
        "runtime_hosting_created": False,
        "cross_carrier_evidence_created": False,
        "follow_on_work_authorized": False,
        "mutation_performed": False,
    }


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "packet emission test",
            "packet emission live artifact",
            "packet emission terminal summary, if needed",
            "packet transfer",
            "copying to another device",
            "second-carrier receipt boundary",
            "second-carrier receipt",
            "second-device / second-carrier execution boundary",
            "second-device / second-carrier execution",
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
        ],
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }


def _basis_declared(request: Mapping[str, Any], key: str) -> bool:
    return _declared(request.get(key))


def _build_checks(request: Mapping[str, Any] | None) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    if not _is_mapping(request):
        _check(
            checks,
            "declared packet emission request is mapping",
            False,
            "mapping request",
            type(request).__name__,
            "DECLARED_PACKET_EMISSION_REQUEST_MALFORMED",
        )
        return checks

    question = request.get("packet_emission_question")
    intent = request.get("packet_emission_intent")
    scope_values = _scope_values(request)
    unsupported_scope = sorted(value for value in scope_values if value not in SUPPORTED_PACKET_EMISSION_SCOPE)

    _check(checks, "packet emission question declared", question == CORE_QUESTION, CORE_QUESTION, question, "PACKET_EMISSION_QUESTION_UNDECLARED")
    _check(checks, "packet emission intent supported", intent in SUPPORTED_INTENTS, sorted(SUPPORTED_INTENTS), intent, "PACKET_EMISSION_INTENT_UNSUPPORTED")
    _check(checks, "packet emission explicit block intent absent", intent != INTENT_BLOCK, "not explicit block intent", intent, "PACKET_EMISSION_EXPLICIT_BLOCK_INTENT")
    _check(checks, "packet emission scope supported", bool(scope_values) and not unsupported_scope, sorted(SUPPORTED_PACKET_EMISSION_SCOPE), scope_values, "UNSUPPORTED_PACKET_EMISSION_SCOPE")

    missing_codes = {
        "selected_packet_emission_boundary_v2_basis": "PACKET_EMISSION_BOUNDARY_V2_BASIS_MISSING",
        "selected_packet_emission_boundary_v2_terminal_summary_basis": "PACKET_EMISSION_BOUNDARY_V2_TERMINAL_SUMMARY_BASIS_MISSING",
        "selected_packet_emission_boundary_v1_predecessor_failure_basis": "PACKET_EMISSION_BOUNDARY_V1_PREDECESSOR_FAILURE_BASIS_MISSING",
        "selected_packet_artifact_basis": "PACKET_ARTIFACT_BASIS_MISSING",
        "selected_packet_boundary_basis": "PACKET_BOUNDARY_BASIS_MISSING",
        "selected_command_success_basis": "COMMAND_SUCCESS_BASIS_MISSING",
        "selected_command_result_v2_basis": "COMMAND_RESULT_V2_BASIS_MISSING",
        "selected_output_capture_v2_basis": "OUTPUT_CAPTURE_V2_BASIS_MISSING",
        "selected_command_output_report_artifact_basis": "COMMAND_OUTPUT_REPORT_ARTIFACT_BASIS_MISSING",
        "selected_command_execution_basis": "COMMAND_EXECUTION_BASIS_MISSING",
        "selected_command_report_lineage_basis": "COMMAND_REPORT_LINEAGE_BASIS_MISSING",
        "selected_predecessor_failure_basis": "PREDECESSOR_FAILURE_EVIDENCE_NOT_VISIBLE",
        "selected_evidence_manifest_basis": "EVIDENCE_MANIFEST_BASIS_MISSING",
        "selected_artifact_containment_basis": "ARTIFACT_CONTAINMENT_BASIS_MISSING",
        "selected_portable_verification_basis": "PORTABLE_VERIFICATION_BASIS_MISSING",
    }
    for key in SELECTED_BASIS_KEYS:
        _check(
            checks,
            f"{key} declared",
            _basis_declared(request, key),
            "declared reference-shaped basis",
            request.get(key),
            missing_codes[key],
        )

    boundary_outcome = _value(
        request,
        ("selected_packet_emission_boundary_v2_result_outcome", "outcome", "result_outcome"),
        "selected_packet_emission_boundary_v2_basis",
    )
    boundary_version = _value(
        request,
        (
            "selected_packet_emission_boundary_v2_result_version",
            "result_version",
            "portable_source_body_verification_packet_emission_boundary_result_version",
        ),
        "selected_packet_emission_boundary_v2_basis",
    )
    boundary_failed_checks = _as_int(
        _value(
            request,
            ("selected_packet_emission_boundary_v2_failed_check_count", "failed_check_count"),
            "selected_packet_emission_boundary_v2_basis",
        ),
        default=None,
    )
    v1_preserved = _value(
        request,
        (
            "selected_packet_emission_boundary_v2_v1_failure_preserved",
            "v1_predecessor_failure_preserved",
            "packet_emission_boundary_v1_failure_preserved",
        ),
        "selected_packet_emission_boundary_v2_basis",
    )
    future_step_declared = _value(
        request,
        (
            "selected_packet_emission_boundary_v2_declared_future_packet_emission_step",
            "one_future_packet_emission_step_declared",
        ),
        "selected_packet_emission_boundary_v2_basis",
    )

    _check(checks, "packet-emission-boundary v2 outcome recorded", boundary_outcome == PACKET_EMISSION_BOUNDARY_V2_RECORDED, PACKET_EMISSION_BOUNDARY_V2_RECORDED, boundary_outcome, "PACKET_EMISSION_BOUNDARY_V2_NOT_RECORDED")
    _check(checks, "packet-emission-boundary v2 version 0.2.0", boundary_version == PACKET_EMISSION_BOUNDARY_V2_RESULT_VERSION, PACKET_EMISSION_BOUNDARY_V2_RESULT_VERSION, boundary_version, "PACKET_EMISSION_BOUNDARY_V2_VERSION_NOT_0_2_0")
    _check(checks, "packet-emission-boundary v2 failed checks zero", boundary_failed_checks == 0, 0, boundary_failed_checks, "PACKET_EMISSION_BOUNDARY_V2_FAILED_CHECKS_PRESENT")
    _check(checks, "packet-emission-boundary v2 preserves v1 failure evidence", v1_preserved is True, True, v1_preserved, "PACKET_EMISSION_BOUNDARY_V2_V1_FAILURE_EVIDENCE_MISSING")
    _check(checks, "packet-emission-boundary v2 declares future packet-emission step", future_step_declared is True, True, future_step_declared, "PACKET_EMISSION_BOUNDARY_V2_DID_NOT_DECLARE_FUTURE_PACKET_EMISSION_STEP")

    for name, names, code in (
        ("packet-emission-boundary v2 did not repair v1", ("selected_packet_emission_boundary_v2_v1_repaired", "v1_repaired", "packet_emission_boundary_v2_repaired_v1"), "PACKET_EMISSION_BOUNDARY_V2_REPAIRED_V1"),
        ("packet-emission-boundary v2 did not hide v1", ("selected_packet_emission_boundary_v2_v1_hidden", "v1_hidden", "packet_emission_boundary_v2_hid_v1"), "PACKET_EMISSION_BOUNDARY_V2_HID_V1"),
        ("packet-emission-boundary v2 did not claim v1 passed", ("selected_packet_emission_boundary_v2_v1_claimed_passed", "v1_claimed_passed", "packet_emission_boundary_v2_claimed_v1_passed"), "PACKET_EMISSION_BOUNDARY_V2_CLAIMED_V1_PASSED"),
        ("packet-emission-boundary v2 did not emit packet", ("selected_packet_emission_boundary_v2_packet_emitted", "packet_emitted"), "PACKET_EMISSION_BOUNDARY_V2_ALREADY_EMITTED_PACKET"),
        ("packet-emission-boundary v2 did not create emitted packet", ("selected_packet_emission_boundary_v2_emitted_packet_created", "emitted_packet_created"), "PACKET_EMISSION_BOUNDARY_V2_ALREADY_CREATED_EMITTED_PACKET"),
        ("packet-emission-boundary v2 did not authorize transfer", ("selected_packet_emission_boundary_v2_authorized_transfer", "packet_transfer_authorized", "packet_transferred"), "PACKET_EMISSION_BOUNDARY_V2_AUTHORIZED_TRANSFER"),
        ("packet-emission-boundary v2 did not authorize copy to another device", ("selected_packet_emission_boundary_v2_authorized_copy_to_another_device", "copy_to_another_device_authorized", "packet_copied_to_another_device"), "PACKET_EMISSION_BOUNDARY_V2_AUTHORIZED_COPY_TO_ANOTHER_DEVICE"),
        ("packet-emission-boundary v2 did not authorize source transfer", ("selected_packet_emission_boundary_v2_authorized_source_transfer", "source_transfer_authorized", "source_transfer_occurred"), "PACKET_EMISSION_BOUNDARY_V2_AUTHORIZED_SOURCE_TRANSFER"),
        ("packet-emission-boundary v2 did not authorize source receipt", ("selected_packet_emission_boundary_v2_authorized_source_receipt", "source_receipt_authorized", "source_receipt_occurred"), "PACKET_EMISSION_BOUNDARY_V2_AUTHORIZED_SOURCE_RECEIPT"),
        ("packet-emission-boundary v2 did not authorize reception", ("selected_packet_emission_boundary_v2_authorized_reception", "reception_authorization_created"), "PACKET_EMISSION_BOUNDARY_V2_AUTHORIZED_RECEPTION"),
        ("packet-emission-boundary v2 did not authorize second-carrier receipt", ("selected_packet_emission_boundary_v2_authorized_second_carrier_receipt", "second_carrier_receipt_authorized", "second_carrier_receipt_created"), "PACKET_EMISSION_BOUNDARY_V2_AUTHORIZED_SECOND_CARRIER_RECEIPT"),
        ("packet-emission-boundary v2 did not authorize second-carrier execution", ("selected_packet_emission_boundary_v2_authorized_second_carrier_execution", "second_carrier_execution_authorized", "second_carrier_execution_created"), "PACKET_EMISSION_BOUNDARY_V2_AUTHORIZED_SECOND_CARRIER_EXECUTION"),
        ("packet-emission-boundary v2 did not create external result", ("selected_packet_emission_boundary_v2_created_external_result", "external_result_created"), "PACKET_EMISSION_BOUNDARY_V2_CREATED_EXTERNAL_RESULT"),
        ("packet-emission-boundary v2 did not create cross-carrier evidence", ("selected_packet_emission_boundary_v2_created_cross_carrier_evidence", "cross_carrier_evidence_created"), "PACKET_EMISSION_BOUNDARY_V2_CREATED_CROSS_CARRIER_EVIDENCE"),
        ("packet-emission-boundary v2 did not use hidden repo state as emission authority", ("selected_packet_emission_boundary_v2_used_hidden_repo_state_as_emission_authority", "hidden_repo_state_used_as_emission_authority"), "PACKET_EMISSION_BOUNDARY_V2_USED_HIDDEN_REPO_STATE_AS_EMISSION_AUTHORITY"),
        ("packet-emission-boundary v2 did not treat repo-local availability as emission authority", ("selected_packet_emission_boundary_v2_treated_repo_local_availability_as_emission_authority", "repo_local_availability_treated_as_emission_authority"), "PACKET_EMISSION_BOUNDARY_V2_TREATED_REPO_LOCAL_AVAILABILITY_AS_EMISSION_AUTHORITY"),
        ("packet-emission-boundary v2 did not return raw full prior artifact body", ("selected_packet_emission_boundary_v2_raw_full_prior_artifact_body_returned", "raw_full_prior_artifact_body_returned"), "PACKET_EMISSION_BOUNDARY_V2_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY"),
    ):
        actual = _any_true(request, names, "selected_packet_emission_boundary_v2_basis")
        _check(checks, name, actual is False, False, actual, code)

    artifact_outcome = _value(
        request,
        ("selected_packet_artifact_result_outcome", "outcome", "result_outcome"),
        "selected_packet_artifact_basis",
    )
    artifact_failed_checks = _as_int(
        _value(
            request,
            ("selected_packet_artifact_failed_check_count", "failed_check_count"),
            "selected_packet_artifact_basis",
        ),
        default=None,
    )
    _check(checks, "packet artifact outcome recorded", artifact_outcome == PACKET_ARTIFACT_RECORDED, PACKET_ARTIFACT_RECORDED, artifact_outcome, "PACKET_ARTIFACT_NOT_RECORDED")
    _check(checks, "packet artifact failed checks zero", artifact_failed_checks == 0, 0, artifact_failed_checks, "PACKET_ARTIFACT_FAILED_CHECKS_PRESENT")

    for name, basis_key, expected, code in (
        ("command success basis recorded", "selected_command_success_basis", COMMAND_SUCCESS_RECORDED, "COMMAND_SUCCESS_NOT_RECORDED"),
        ("command result v2 basis recorded", "selected_command_result_v2_basis", COMMAND_RESULT_V2_RECORDED, "COMMAND_RESULT_V2_NOT_RECORDED"),
        ("output capture v2 basis recorded", "selected_output_capture_v2_basis", OUTPUT_CAPTURE_V2_RECORDED, "OUTPUT_CAPTURE_V2_NOT_RECORDED"),
        ("command output/report artifact basis recorded", "selected_command_output_report_artifact_basis", COMMAND_OUTPUT_REPORT_ARTIFACT_RECORDED, "COMMAND_OUTPUT_REPORT_ARTIFACT_NOT_RECORDED"),
    ):
        actual = _value(request, ("outcome", "result_outcome"), basis_key, default=expected)
        _check(checks, name, actual == expected, expected, actual, code)

    execution_audit_only = _value(
        request,
        ("execution_trace_audit_only", "audit_only", "execution_audit_only"),
        "selected_command_execution_basis",
        default=True,
    )
    _check(checks, "execution trace audit-only", execution_audit_only is True, True, execution_audit_only, "EXECUTION_TRACE_NOT_AUDIT_ONLY")

    lineage_only = _value(
        request,
        ("command_report_lineage_only", "lineage_only"),
        "selected_command_report_lineage_basis",
        default=True,
    )
    _check(checks, "command report lineage lineage-only", lineage_only is True, True, lineage_only, "COMMAND_REPORT_LINEAGE_NOT_LINEAGE_ONLY")
    for name, field, code in (
        ("command report lineage not current report artifact", "command_report_lineage_treated_as_current_report_artifact", "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENT_REPORT_ARTIFACT"),
        ("command report lineage not source", "command_report_lineage_treated_as_source", "COMMAND_REPORT_LINEAGE_TREATED_AS_SOURCE"),
        ("command report lineage not authority", "command_report_lineage_treated_as_authority", "COMMAND_REPORT_LINEAGE_TREATED_AS_AUTHORITY"),
        ("command report lineage not currentness", "command_report_lineage_treated_as_currentness", "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENTNESS"),
    ):
        actual = _any_true(request, (field,), "selected_command_report_lineage_basis")
        _check(checks, name, actual is False, False, actual, code)

    predecessor_visible = _value(
        request,
        ("predecessor_failure_evidence_visible", "predecessor_failures_visible"),
        "selected_predecessor_failure_basis",
        default=True,
    )
    predecessor_repaired = _any_true(
        request,
        (
            "predecessor_failure_evidence_hidden_or_repaired",
            "predecessor_failures_repaired",
            "predecessor_failures_hidden",
            "predecessor_failures_claimed_passed",
        ),
        "selected_predecessor_failure_basis",
    )
    _check(checks, "predecessor failure evidence visible", predecessor_visible is True, True, predecessor_visible, "PREDECESSOR_FAILURE_EVIDENCE_NOT_VISIBLE")
    _check(checks, "predecessor failure evidence visible and unrepaired", predecessor_repaired is False, False, predecessor_repaired, "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED")

    posture_missing_codes = {
        "packet_emission_spec_only_posture": "PACKET_EMISSION_SPEC_ONLY_POSTURE_MISSING",
        "one_bounded_packet_emission_posture": "ONE_BOUNDED_PACKET_EMISSION_POSTURE_MISSING",
        "packet_emission_boundary_v2_basis_preserved_posture": "PACKET_EMISSION_BOUNDARY_V2_BASIS_PRESERVED_POSTURE_MISSING",
        "packet_emission_boundary_v1_failure_preserved_posture": "PACKET_EMISSION_BOUNDARY_V1_FAILURE_PRESERVED_POSTURE_MISSING",
        "packet_artifact_basis_preserved_posture": "PACKET_ARTIFACT_BASIS_PRESERVED_POSTURE_MISSING",
        "emitted_packet_recorded_or_bounded_posture": "EMITTED_PACKET_RECORDED_OR_BOUNDED_POSTURE_MISSING",
        "packet_transfer_not_authorized_posture": "PACKET_TRANSFER_NOT_AUTHORIZED_POSTURE_MISSING",
        "copy_to_another_device_not_authorized_posture": "COPY_TO_ANOTHER_DEVICE_NOT_AUTHORIZED_POSTURE_MISSING",
        "source_transfer_not_authorized_posture": "SOURCE_TRANSFER_NOT_AUTHORIZED_POSTURE_MISSING",
        "source_receipt_not_created_posture": "SOURCE_RECEIPT_NOT_CREATED_POSTURE_MISSING",
        "reception_authorization_not_created_posture": "RECEPTION_AUTHORIZATION_NOT_CREATED_POSTURE_MISSING",
        "second_carrier_receipt_not_created_posture": "SECOND_CARRIER_RECEIPT_NOT_CREATED_POSTURE_MISSING",
        "second_carrier_execution_not_authorized_posture": "SECOND_CARRIER_EXECUTION_NOT_AUTHORIZED_POSTURE_MISSING",
        "external_result_not_created_posture": "EXTERNAL_RESULT_NOT_CREATED_POSTURE_MISSING",
        "cross_carrier_evidence_not_created_posture": "CROSS_CARRIER_EVIDENCE_NOT_CREATED_POSTURE_MISSING",
        "source_not_created_posture": "NO_SOURCE_AUTHORITY_CURRENTNESS_FINAL_COMPLETION_RUNTIME_FOLLOW_ON_POSTURE_MISSING",
        "authority_not_created_posture": "NO_SOURCE_AUTHORITY_CURRENTNESS_FINAL_COMPLETION_RUNTIME_FOLLOW_ON_POSTURE_MISSING",
        "currentness_not_created_posture": "NO_SOURCE_AUTHORITY_CURRENTNESS_FINAL_COMPLETION_RUNTIME_FOLLOW_ON_POSTURE_MISSING",
        "final_completion_not_created_posture": "NO_SOURCE_AUTHORITY_CURRENTNESS_FINAL_COMPLETION_RUNTIME_FOLLOW_ON_POSTURE_MISSING",
        "runtime_not_created_posture": "NO_SOURCE_AUTHORITY_CURRENTNESS_FINAL_COMPLETION_RUNTIME_FOLLOW_ON_POSTURE_MISSING",
        "continuation_not_authorized_posture": "NO_SOURCE_AUTHORITY_CURRENTNESS_FINAL_COMPLETION_RUNTIME_FOLLOW_ON_POSTURE_MISSING",
        "reusable_permission_not_created_posture": "NO_SOURCE_AUTHORITY_CURRENTNESS_FINAL_COMPLETION_RUNTIME_FOLLOW_ON_POSTURE_MISSING",
        "follow_on_work_not_authorized_posture": "NO_SOURCE_AUTHORITY_CURRENTNESS_FINAL_COMPLETION_RUNTIME_FOLLOW_ON_POSTURE_MISSING",
        "hidden_repo_state_excluded_posture": "HIDDEN_REPO_STATE_EXCLUDED_POSTURE_MISSING",
        "repo_local_availability_not_emission_authority_posture": "REPO_LOCAL_AVAILABILITY_NOT_EMISSION_AUTHORITY_POSTURE_MISSING",
        "selected_basis_reference_shape_posture": "SELECTED_BASIS_REFERENCE_SHAPE_POSTURE_MISSING",
        "raw_full_prior_artifact_body_not_returned_posture": "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED_POSTURE_MISSING",
    }
    for key in POSTURE_KEYS:
        _check(checks, f"{key} declared", _declared(request.get(key)), "declared posture", request.get(key), posture_missing_codes[key])

    for name, names, code in (
        ("packet emission not treated as transfer", ("packet_emission_treated_as_transfer",), "PACKET_EMISSION_TREATED_AS_TRANSFER"),
        ("packet emission not treated as copy to another device", ("packet_emission_treated_as_copy_to_another_device",), "PACKET_EMISSION_TREATED_AS_COPY_TO_ANOTHER_DEVICE"),
        ("packet emission not treated as source transfer", ("packet_emission_treated_as_source_transfer",), "PACKET_EMISSION_TREATED_AS_SOURCE_TRANSFER"),
        ("packet emission not treated as source receipt", ("packet_emission_treated_as_source_receipt",), "PACKET_EMISSION_TREATED_AS_SOURCE_RECEIPT"),
        ("packet emission not treated as reception authorization", ("packet_emission_treated_as_reception_authorization",), "PACKET_EMISSION_TREATED_AS_RECEPTION_AUTHORIZATION"),
        ("packet emission not treated as second-carrier receipt", ("packet_emission_treated_as_second_carrier_receipt",), "PACKET_EMISSION_TREATED_AS_SECOND_CARRIER_RECEIPT"),
        ("packet emission not treated as second-carrier execution", ("packet_emission_treated_as_second_carrier_execution",), "PACKET_EMISSION_TREATED_AS_SECOND_CARRIER_EXECUTION"),
        ("packet emission not treated as cross-carrier evidence", ("packet_emission_treated_as_cross_carrier_evidence",), "PACKET_EMISSION_TREATED_AS_CROSS_CARRIER_EVIDENCE"),
        ("packet emission not treated as source", ("packet_emission_treated_as_source",), "PACKET_EMISSION_TREATED_AS_SOURCE"),
        ("packet emission not treated as authority", ("packet_emission_treated_as_authority",), "PACKET_EMISSION_TREATED_AS_AUTHORITY"),
        ("packet emission not treated as currentness", ("packet_emission_treated_as_currentness",), "PACKET_EMISSION_TREATED_AS_CURRENTNESS"),
        ("packet emission not treated as final completion", ("packet_emission_treated_as_final_completion",), "PACKET_EMISSION_TREATED_AS_FINAL_COMPLETION"),
        ("packet emission not treated as runtime", ("packet_emission_treated_as_runtime",), "PACKET_EMISSION_TREATED_AS_RUNTIME"),
        ("packet emission not treated as continuation", ("packet_emission_treated_as_continuation",), "PACKET_EMISSION_TREATED_AS_CONTINUATION"),
        ("packet emission not treated as reusable permission", ("packet_emission_treated_as_reusable_permission",), "PACKET_EMISSION_TREATED_AS_REUSABLE_PERMISSION"),
        ("packet emission not treated as follow-on work", ("packet_emission_treated_as_follow_on_work",), "PACKET_EMISSION_TREATED_AS_FOLLOW_ON_WORK"),
        ("emitted packet not treated as source", ("emitted_packet_treated_as_source",), "EMITTED_PACKET_TREATED_AS_SOURCE"),
        ("emitted packet not treated as authority", ("emitted_packet_treated_as_authority",), "EMITTED_PACKET_TREATED_AS_AUTHORITY"),
        ("emitted packet not treated as currentness", ("emitted_packet_treated_as_currentness",), "EMITTED_PACKET_TREATED_AS_CURRENTNESS"),
        ("packet not transferred", ("packet_transferred",), "PACKET_TRANSFERRED"),
        ("packet not copied to another device", ("packet_copied_to_another_device",), "PACKET_COPIED_TO_ANOTHER_DEVICE"),
        ("source transfer did not occur", ("source_transfer_occurred",), "SOURCE_TRANSFER_OCCURRED"),
        ("source receipt did not occur", ("source_receipt_occurred",), "SOURCE_RECEIPT_OCCURRED"),
        ("reception authorization not created", ("reception_authorization_created",), "RECEPTION_AUTHORIZATION_CREATED"),
        ("second-carrier receipt not created", ("second_carrier_receipt_created",), "SECOND_CARRIER_RECEIPT_CREATED"),
        ("second-carrier execution not created", ("second_carrier_execution_created",), "SECOND_CARRIER_EXECUTION_CREATED"),
        ("external result not created", ("external_result_created",), "EXTERNAL_RESULT_CREATED"),
        ("cross-carrier evidence not created", ("cross_carrier_evidence_created",), "CROSS_CARRIER_EVIDENCE_CREATED"),
        ("source not created", ("source_created",), "SOURCE_CREATED"),
        ("authority not created", ("authority_created",), "AUTHORITY_CREATED"),
        ("currentness not created", ("currentness_created",), "CURRENTNESS_CREATED"),
        ("final completion not claimed", ("final_completion_claimed",), "FINAL_COMPLETION_CLAIMED"),
        ("runtime hosting not created", ("runtime_hosting_created",), "RUNTIME_HOSTING_CREATED"),
        ("deployment not created", ("deployment_created",), "DEPLOYMENT_CREATED"),
        ("public release not created", ("public_release_created",), "PUBLIC_RELEASE_CREATED"),
        ("operation permission not created", ("operation_permission_created",), "OPERATION_PERMISSION_CREATED"),
        ("continuation not authorized", ("continuation_authorized",), "CONTINUATION_AUTHORIZED"),
        ("reusable permission not created", ("reusable_permission_created",), "REUSABLE_PERMISSION_CREATED"),
        ("derivative reception not authorized", ("derivative_reception_authorized",), "DERIVATIVE_RECEPTION_AUTHORIZED"),
        ("vessel relation not authorized", ("vessel_relation_authorized",), "VESSEL_RELATION_AUTHORIZED"),
        ("another reception request not authorized", ("another_reception_request_authorized",), "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"),
        ("follow-on work not authorized", ("follow_on_work_authorized",), "FOLLOW_ON_WORK_AUTHORIZED"),
        ("artifact existence not treated as emission authority", ("artifact_existence_treated_as_emission_authority",), "ARTIFACT_EXISTENCE_TREATED_AS_EMISSION_AUTHORITY"),
        ("artifact path not treated as currentness", ("artifact_path_treated_as_currentness",), "ARTIFACT_PATH_TREATED_AS_CURRENTNESS"),
        ("repo-local availability not treated as emission authority", ("repo_local_availability_treated_as_emission_authority",), "REPO_LOCAL_AVAILABILITY_TREATED_AS_EMISSION_AUTHORITY"),
        ("hidden repo state not used as emission content", ("hidden_repo_state_used_as_emission_content",), "HIDDEN_REPO_STATE_USED_AS_EMISSION_CONTENT"),
        ("hidden repo state not used as emission authority", ("hidden_repo_state_used_as_emission_authority",), "HIDDEN_REPO_STATE_USED_AS_EMISSION_AUTHORITY"),
        ("consumed request not reopened", ("consumed_request_reopened",), "CONSUMED_REQUEST_REOPENED"),
        ("authorization token not reused", ("authorization_token_reused",), "AUTHORIZATION_TOKEN_REUSED"),
        ("full prior artifact body not emitted outside bounded emission", ("full_prior_artifact_body_emitted_outside_bounded_emission",), "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_EMISSION"),
        ("artifacts not mutated", ("artifacts_mutated", "prior_artifacts_mutated"), "ARTIFACTS_MUTATED"),
    ):
        actual = _any_true(request, names)
        _check(checks, name, actual is False, False, actual, code)

    _check(checks, "selected basis reference-shaped", _all_selected_basis_reference_shaped(request), True, "selected basis reference-shaped", "SELECTED_BASIS_NOT_REFERENCE_SHAPED")
    _check(checks, "raw full prior artifact body not returned", _all_raw_full_prior_body_not_returned(request), True, "raw full prior artifact body not returned", "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED")
    _check(checks, "hidden repo state excluded", _hidden_repo_state_excluded(request), True, "hidden repo state excluded", "HIDDEN_REPO_STATE_USED_AS_EMISSION_AUTHORITY")

    claims = _non_claims_from_request(request)
    for key in REQUIRED_FALSE_NON_CLAIMS:
        actual = claims.get(key)
        _check(
            checks,
            f"required non-claim false: {key}",
            actual is False,
            False,
            actual,
            NON_CLAIM_TO_BLOCK_CODE.get(key, "NON_CLAIM_MISSING_OR_FLIPPED"),
        )

    return checks


def _determine_outcome(request: Mapping[str, Any] | None, checks: Sequence[Mapping[str, Any]]) -> str:
    if _failed_code(checks) is not None or not _is_mapping(request):
        return OUTCOME_BLOCKED
    requested = request.get("requested_packet_emission_outcome")
    if requested in OUTCOME_FAMILY:
        return str(requested)
    intent = request.get("packet_emission_intent")
    if intent == INTENT_DO_NOT_RECORD:
        return OUTCOME_NOT_RECORDED
    if request.get("additional_basis_context"):
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS
    if request.get("not_recorded_basis"):
        return OUTCOME_NOT_RECORDED
    return OUTCOME_RECORDED


def _block(outcome: str, failed_code: str | None, request: Mapping[str, Any] | None) -> dict[str, Any]:
    if outcome != OUTCOME_BLOCKED:
        return {"blocked": False, "block_code": None, "block_reason": None}
    reason = request.get("block_reason") if _is_mapping(request) else None
    return {
        "blocked": True,
        "block_code": failed_code or "DECLARED_PACKET_EMISSION_REQUEST_MALFORMED",
        "block_reason": reason or "Packet-emission request is blocked by bounded membrane checks.",
        "packet_emission_recorded": False,
        "bounded_packet_emission_recorded": False,
        "packet_transferred": False,
        "packet_copied_to_another_device": False,
        "source_transfer_occurred": False,
        "source_receipt_occurred": False,
        "reception_authorization_created": False,
        "second_carrier_receipt_created": False,
        "second_carrier_execution_created": False,
        "external_result_created": False,
        "cross_carrier_evidence_created": False,
        "source_created": False,
        "authority_created": False,
        "currentness_created": False,
        "final_completion_claimed": False,
        "runtime_hosting_created": False,
        "deployment_created": False,
        "public_release_created": False,
        "follow_on_work_authorized": False,
        "consumed_request_reopened": False,
        "authorization_token_reused": False,
        "v1_repaired": False,
        "v1_hidden": False,
        "v1_claimed_passed": False,
        "artifacts_mutated": False,
    }


def _metadata(request: Mapping[str, Any] | None, checks: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    request_id = "portable_source_body_verification_packet_emission_request"
    if _is_mapping(request):
        request_id = str(request.get("packet_emission_request_id") or request_id)
    return {
        "portable_source_body_verification_packet_emission_result_id": (
            f"{request_id}__portable_source_body_verification_packet_emission_result"
        ),
        "packet_emission_request_id": request_id,
        "portable_source_body_verification_packet_emission_result_type": RESULT_TYPE,
        "portable_source_body_verification_packet_emission_result_version": RESULT_VERSION,
        "generated_at": _now(),
        "resolver_module": RESOLVER_MODULE,
        "packet_emission_boundary_v2_basis_resolver_module": (
            "resolve_portable_source_body_verification_packet_emission_boundary_v2"
        ),
        "packet_emission_boundary_v1_predecessor_resolver_module": (
            "resolve_portable_source_body_verification_packet_emission_boundary"
        ),
        "v1_packet_emission_boundary_failure_preserved": True,
        "v1_repaired": False,
        "v1_hidden": False,
        "v1_claimed_passed": False,
        "packet_emission_does_not_repair_hide_or_claim_v1_passed": True,
        "passed_check_count": sum(1 for check in checks if check.get("passed")),
        "failed_check_count": sum(1 for check in checks if not check.get("passed")),
    }


def _base_result(request: Mapping[str, Any] | None, outcome: str, checks: list[dict[str, Any]]) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    failed_code = _failed_code(checks)
    request_map = request if _is_mapping(request) else {}
    result: dict[str, Any] = {
        "portable_source_body_verification_packet_emission_metadata": _metadata(request, checks),
        "declared_packet_emission_question": {
            "request_id": request_map.get("packet_emission_request_id"),
            "question": request_map.get("packet_emission_question"),
            "expected_question": CORE_QUESTION,
            "intent": request_map.get("packet_emission_intent"),
            "question_declared": request_map.get("packet_emission_question") == CORE_QUESTION,
        },
    }
    for key in SELECTED_BASIS_KEYS:
        result[key] = _safe_basis_section(key, request_map.get(key), request_map)
    for key in POSTURE_KEYS:
        result[key] = _posture_section(key, request_map, recorded)

    non_claims = {key: False for key in REQUIRED_FALSE_NON_CLAIMS}
    non_claims.update({key: False for key in EXTRA_FALSE_NON_CLAIMS})
    result.update(
        {
            "packet_emission_scope": {
                "scope_values": _scope_values(request_map),
                "supported_scope_values": sorted(SUPPORTED_PACKET_EMISSION_SCOPE),
                "unsupported_scope_values": sorted(
                    value for value in _scope_values(request_map) if value not in SUPPORTED_PACKET_EMISSION_SCOPE
                ),
            },
            "packet_emission_checks": checks,
            "packet_emission_statement": _statement(recorded),
            "packet_emission_non_meaning": _non_meaning(),
            "additional_basis_required": _additional_basis_required(request_map, outcome),
            "not_recorded_basis": _not_recorded_basis(request_map, outcome, failed_code),
            "what_remains_open": _what_remains_open(),
            "non_claims": non_claims,
            "outcome": outcome,
            "block": _block(outcome, failed_code, request),
        }
    )
    result["portable_source_body_verification_packet_emission_summary"] = (
        build_portable_source_body_verification_packet_emission_summary(result)
    )
    return _json_safe(result)


def resolve_portable_source_body_verification_packet_emission(
    declared_packet_emission_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one bounded portable source-body verification packet-emission request."""

    request = _copy(declared_packet_emission_request)
    if request is not None and not _is_mapping(request):
        checks = _build_checks(None)
        return _base_result(None, OUTCOME_BLOCKED, checks)
    checks = _build_checks(request)
    outcome = _determine_outcome(request, checks)
    return _base_result(request, outcome, checks)


def resolve_portable_source_body_verification_packet_emission_from_path(
    declared_packet_emission_request_path: Path | str,
) -> dict:
    """Load a JSON object request from path and resolve bounded packet emission."""

    path = Path(declared_packet_emission_request_path)
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise PortableSourceBodyVerificationPacketEmissionError(
            f"declared packet-emission request is unreadable: {path}"
        ) from exc
    try:
        request = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise PortableSourceBodyVerificationPacketEmissionError(
            f"declared packet-emission request is malformed JSON: {path}"
        ) from exc
    if not _is_mapping(request):
        raise PortableSourceBodyVerificationPacketEmissionError(
            "declared packet-emission request JSON must be an object"
        )
    return resolve_portable_source_body_verification_packet_emission(request)


def build_portable_source_body_verification_packet_emission_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a compact packet-emission summary without promoting it into transfer."""

    metadata = result.get("portable_source_body_verification_packet_emission_metadata", {})
    question = result.get("declared_packet_emission_question", {})
    checks = result.get("packet_emission_checks", [])
    statement = result.get("packet_emission_statement", {})
    non_claims = result.get("non_claims", {})
    boundary_basis = result.get("selected_packet_emission_boundary_v2_basis", {})
    block = result.get("block")
    summary: dict[str, Any] = {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") if _is_mapping(block) else None,
        "block_reason": block.get("block_reason") if _is_mapping(block) else None,
        "request_id": metadata.get("packet_emission_request_id") if _is_mapping(metadata) else None,
        "question": question.get("question") if _is_mapping(question) else None,
        "intent": question.get("intent") if _is_mapping(question) else None,
        "passed_check_count": sum(1 for check in checks if _is_mapping(check) and check.get("passed")),
        "failed_check_count": sum(1 for check in checks if _is_mapping(check) and not check.get("passed")),
        "selected_packet_emission_boundary_v2_outcome": boundary_basis.get("outcome") if _is_mapping(boundary_basis) else None,
        "selected_packet_emission_boundary_v2_version": boundary_basis.get("result_version") if _is_mapping(boundary_basis) else None,
        "selected_packet_emission_boundary_v2_failed_check_count": boundary_basis.get("failed_check_count") if _is_mapping(boundary_basis) else None,
        "v1_predecessor_failure_preserved": (
            statement.get("packet_emission_boundary_v1_failure_preserved") is True
        ),
        "v1_repaired": non_claims.get("v1_repaired") is True if _is_mapping(non_claims) else False,
        "v1_hidden": non_claims.get("v1_hidden") is True if _is_mapping(non_claims) else False,
        "v1_claimed_passed": (
            non_claims.get("v1_claimed_passed") is True if _is_mapping(non_claims) else False
        ),
        "no_transfer_copy_receipt_cross_carrier_evidence": (
            _is_mapping(non_claims)
            and non_claims.get("packet_transferred") is False
            and non_claims.get("packet_copied_to_another_device") is False
            and non_claims.get("second_carrier_receipt_created") is False
            and non_claims.get("second_carrier_execution_created") is False
            and non_claims.get("cross_carrier_evidence_created") is False
        ),
        "no_source_authority_currentness_final_completion_runtime": (
            _is_mapping(non_claims)
            and non_claims.get("source_created") is False
            and non_claims.get("authority_created") is False
            and non_claims.get("currentness_created") is False
            and non_claims.get("final_completion_claimed") is False
            and non_claims.get("runtime_hosting_created") is False
        ),
        "no_deployment_public_release_follow_on": (
            _is_mapping(non_claims)
            and non_claims.get("deployment_created") is False
            and non_claims.get("public_release_created") is False
            and non_claims.get("follow_on_work_authorized") is False
        ),
        "key_non_claims": {
            key: non_claims.get(key) if _is_mapping(non_claims) else None
            for key in (
                "packet_transferred",
                "packet_copied_to_another_device",
                "source_transfer_occurred",
                "source_receipt_occurred",
                "reception_authorization_created",
                "second_carrier_receipt_created",
                "second_carrier_execution_created",
                "external_result_created",
                "cross_carrier_evidence_created",
                "source_created",
                "authority_created",
                "currentness_created",
                "final_completion_claimed",
                "runtime_hosting_created",
                "deployment_created",
                "public_release_created",
                "follow_on_work_authorized",
                "hidden_repo_state_used_as_emission_content",
                "hidden_repo_state_used_as_emission_authority",
                "repo_local_availability_treated_as_emission_authority",
                "artifact_existence_treated_as_emission_authority",
                "artifact_path_treated_as_currentness",
                "consumed_request_reopened",
                "authorization_token_reused",
                "v1_repaired",
                "v1_hidden",
                "v1_claimed_passed",
            )
        },
    }
    if _is_mapping(statement):
        for key in ALLOWED_TRUE_RECORDED_FIELDS:
            summary[key] = statement.get(key) is True
    return _json_safe(summary)


def _request_id_from_result(result: Mapping[str, Any]) -> str:
    metadata = result.get("portable_source_body_verification_packet_emission_metadata")
    if _is_mapping(metadata) and metadata.get("packet_emission_request_id"):
        return str(metadata["packet_emission_request_id"])
    question = result.get("declared_packet_emission_question")
    if _is_mapping(question) and question.get("request_id"):
        return str(question["request_id"])
    return "portable_source_body_verification_packet_emission_request"


def _unique_path(path: Path) -> Path:
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


def write_portable_source_body_verification_packet_emission_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a bounded packet-emission JSON result without overwriting existing files."""

    safe_result = _json_safe(_copy(result))
    request_id = _request_id_from_result(safe_result)
    if output_path is None:
        destination = OUTPUT_ROOT / (
            f"{request_id}__portable_source_body_verification_packet_emission_result.json"
        )
    else:
        destination = Path(output_path)
        if destination.exists() and destination.is_dir():
            destination = destination / (
                f"{request_id}__portable_source_body_verification_packet_emission_result.json"
            )
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination = _unique_path(destination)
    destination.write_text(
        json.dumps(safe_result, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return destination


def _basis_stub(label: str, outcome: str | None = None) -> dict[str, Any]:
    basis = {
        "basis_label": label,
        "declared": True,
        "basis_only": True,
        "reference_shaped": True,
        "selected_basis_reference_shape_preserved": True,
        "raw_full_prior_artifact_body_returned": False,
        "hidden_repo_state_excluded": True,
        "hidden_repo_state_used_as_emission_content": False,
        "hidden_repo_state_used_as_emission_authority": False,
        "hidden_repo_state_not_used_as_emission_authority": True,
        "repo_local_availability_not_emission_authority": True,
        "repo_local_availability_treated_as_emission_authority": False,
        "artifact_existence_treated_as_emission_authority": False,
        "artifact_path_treated_as_currentness": False,
    }
    if outcome is not None:
        basis["outcome"] = outcome
    return basis


def _posture_stub(name: str) -> dict[str, Any]:
    return {
        "posture_name": name,
        "declared": True,
        "packet_emission_posture_only": True,
        "one_bounded_packet_emission_posture": True,
        "packet_emission_boundary_v2_basis_preserved": True,
        "packet_emission_boundary_v1_failure_preserved": True,
        "packet_artifact_basis_preserved": True,
        "emitted_packet_recorded_or_bounded": True,
        "packet_transfer_not_authorized": True,
        "copy_to_another_device_not_authorized": True,
        "source_transfer_not_authorized": True,
        "source_receipt_not_created": True,
        "reception_authorization_not_created": True,
        "second_carrier_receipt_not_created": True,
        "second_carrier_execution_not_authorized": True,
        "external_result_not_created": True,
        "cross_carrier_evidence_not_created": True,
        "source_not_created": True,
        "authority_not_created": True,
        "currentness_not_created": True,
        "final_completion_not_created": True,
        "runtime_not_created": True,
        "continuation_not_authorized": True,
        "reusable_permission_not_created": True,
        "follow_on_work_not_authorized": True,
        "hidden_repo_state_excluded": True,
        "hidden_repo_state_not_used_as_emission_authority": True,
        "repo_local_availability_not_emission_authority": True,
        "selected_basis_reference_shape_preserved": True,
        "raw_full_prior_artifact_body_not_returned": True,
        "authorization_token_reuse_blocked": True,
        "consumed_request_token_remains_closed": True,
    }


def build_declared_portable_source_body_verification_packet_emission_request(
    packet_emission_request_id: str = "portable_source_body_verification_packet_emission_reference_review_001",
    *,
    selected_packet_emission_boundary_v2_result_path: Path | str | None = None,
    selected_packet_emission_boundary_v2_result_id: str | None = (
        "portable_source_body_verification_packet_emission_boundary_reference_review_001_v2"
    ),
    selected_packet_artifact_result_path: Path | str | None = None,
    selected_packet_artifact_result_id: str | None = (
        "portable_source_body_verification_packet_artifact_reference_review_001"
    ),
    packet_emission_intent: str = INTENT_RECORD,
) -> dict[str, Any]:
    """Build a valid declared packet-emission request with required non-claims false."""

    request: dict[str, Any] = {
        "packet_emission_request_id": packet_emission_request_id,
        "packet_emission_question": CORE_QUESTION,
        "packet_emission_intent": packet_emission_intent,
        "packet_emission_scope": sorted(SUPPORTED_PACKET_EMISSION_SCOPE),
        "declared_non_claims": {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
        "selected_packet_emission_boundary_v2_result_path": (
            str(selected_packet_emission_boundary_v2_result_path)
            if selected_packet_emission_boundary_v2_result_path is not None
            else None
        ),
        "selected_packet_emission_boundary_v2_result_id": (
            selected_packet_emission_boundary_v2_result_id
        ),
        "selected_packet_emission_boundary_v2_result_outcome": (
            PACKET_EMISSION_BOUNDARY_V2_RECORDED
        ),
        "selected_packet_emission_boundary_v2_result_version": (
            PACKET_EMISSION_BOUNDARY_V2_RESULT_VERSION
        ),
        "selected_packet_emission_boundary_v2_failed_check_count": 0,
        "selected_packet_emission_boundary_v2_v1_failure_preserved": True,
        "selected_packet_emission_boundary_v2_v1_repaired": False,
        "selected_packet_emission_boundary_v2_v1_hidden": False,
        "selected_packet_emission_boundary_v2_v1_claimed_passed": False,
        "selected_packet_emission_boundary_v2_declared_future_packet_emission_step": True,
        "selected_packet_emission_boundary_v2_packet_emitted": False,
        "selected_packet_emission_boundary_v2_emitted_packet_created": False,
        "selected_packet_emission_boundary_v2_authorized_transfer": False,
        "selected_packet_emission_boundary_v2_authorized_copy_to_another_device": False,
        "selected_packet_emission_boundary_v2_authorized_source_transfer": False,
        "selected_packet_emission_boundary_v2_authorized_source_receipt": False,
        "selected_packet_emission_boundary_v2_authorized_reception": False,
        "selected_packet_emission_boundary_v2_authorized_second_carrier_receipt": False,
        "selected_packet_emission_boundary_v2_authorized_second_carrier_execution": False,
        "selected_packet_emission_boundary_v2_created_external_result": False,
        "selected_packet_emission_boundary_v2_created_cross_carrier_evidence": False,
        "selected_packet_emission_boundary_v2_used_hidden_repo_state_as_emission_authority": False,
        "selected_packet_emission_boundary_v2_treated_repo_local_availability_as_emission_authority": False,
        "selected_packet_emission_boundary_v2_raw_full_prior_artifact_body_returned": False,
        "selected_packet_artifact_result_path": (
            str(selected_packet_artifact_result_path)
            if selected_packet_artifact_result_path is not None
            else None
        ),
        "selected_packet_artifact_result_id": selected_packet_artifact_result_id,
        "selected_packet_artifact_result_outcome": PACKET_ARTIFACT_RECORDED,
        "selected_packet_artifact_result_version": PACKET_ARTIFACT_RESULT_VERSION,
        "selected_packet_artifact_failed_check_count": 0,
        "reference_shaped_input_posture": True,
    }
    request["declared_non_claims"].update({key: False for key in EXTRA_FALSE_NON_CLAIMS})

    boundary_v2_basis = _basis_stub(
        "selected_packet_emission_boundary_v2_basis",
        PACKET_EMISSION_BOUNDARY_V2_RECORDED,
    )
    boundary_v2_basis.update(
        {
            "result_version": PACKET_EMISSION_BOUNDARY_V2_RESULT_VERSION,
            "failed_check_count": 0,
            "resolver_module": "resolve_portable_source_body_verification_packet_emission_boundary_v2",
            "successor_of": "resolve_portable_source_body_verification_packet_emission_boundary",
            "v1_predecessor_failure_preserved": True,
            "v1_repaired": False,
            "v1_hidden": False,
            "v1_claimed_passed": False,
            "v2_successor_does_not_erase_v1": True,
            "one_future_packet_emission_step_declared": True,
            "packet_emission_boundary_recorded": True,
            "packet_not_emitted": True,
            "packet_emitted": False,
            "emitted_packet_not_created": True,
            "emitted_packet_created": False,
            "packet_transfer_not_authorized": True,
            "packet_transfer_authorized": False,
            "copy_to_another_device_not_authorized": True,
            "copy_to_another_device_authorized": False,
            "source_transfer_not_authorized": True,
            "source_transfer_authorized": False,
            "source_receipt_not_created": True,
            "source_receipt_authorized": False,
            "reception_authorization_not_created": True,
            "reception_authorization_created": False,
            "second_carrier_receipt_not_created": True,
            "second_carrier_receipt_authorized": False,
            "second_carrier_execution_not_authorized": True,
            "second_carrier_execution_authorized": False,
            "external_result_not_created": True,
            "external_result_created": False,
            "cross_carrier_evidence_not_created": True,
            "cross_carrier_evidence_created": False,
            "hidden_repo_state_excluded": True,
            "hidden_repo_state_not_used_as_emission_authority": True,
            "repo_local_availability_not_emission_authority": True,
            "raw_full_prior_artifact_body_not_returned": True,
            "raw_full_prior_artifact_body_returned": False,
        }
    )
    request["selected_packet_emission_boundary_v2_basis"] = boundary_v2_basis

    request["selected_packet_emission_boundary_v2_terminal_summary_basis"] = _basis_stub(
        "selected_packet_emission_boundary_v2_terminal_summary_basis"
    )

    v1_failure_basis = _basis_stub("selected_packet_emission_boundary_v1_predecessor_failure_basis")
    v1_failure_basis.update(
        {
            "predecessor_failure_evidence_visible": True,
            "v1_predecessor_failure_preserved": True,
            "v1_compiled": True,
            "v1_exposed_expected_public_api": True,
            "v1_produced_recorded_shaped_result": True,
            "v1_failed_packet_emission_boundary_test": True,
            "observed_failure_count": 85,
            "v1_repaired": False,
            "v1_hidden": False,
            "v1_claimed_passed": False,
        }
    )
    request["selected_packet_emission_boundary_v1_predecessor_failure_basis"] = v1_failure_basis

    packet_artifact_basis = _basis_stub("selected_packet_artifact_basis", PACKET_ARTIFACT_RECORDED)
    packet_artifact_basis.update(
        {
            "result_version": PACKET_ARTIFACT_RESULT_VERSION,
            "failed_check_count": 0,
            "packet_artifact_recorded": True,
            "local_packet_artifact_recorded": True,
            "packet_artifact_not_emission_authority": True,
            "packet_artifact_not_transfer": True,
            "packet_transferred": False,
            "packet_copied_to_another_device": False,
            "source_transfer_authorized": False,
            "source_receipt_authorized": False,
            "reception_authorization_created": False,
            "second_carrier_execution_authorized": False,
            "external_result_created": False,
            "cross_carrier_evidence_created": False,
        }
    )
    request["selected_packet_artifact_basis"] = packet_artifact_basis
    request["selected_packet_boundary_basis"] = _basis_stub(
        "selected_packet_boundary_basis", PACKET_BOUNDARY_RECORDED
    )
    request["selected_command_success_basis"] = _basis_stub(
        "selected_command_success_basis", COMMAND_SUCCESS_RECORDED
    )
    request["selected_command_result_v2_basis"] = _basis_stub(
        "selected_command_result_v2_basis", COMMAND_RESULT_V2_RECORDED
    )
    request["selected_output_capture_v2_basis"] = _basis_stub(
        "selected_output_capture_v2_basis", OUTPUT_CAPTURE_V2_RECORDED
    )
    request["selected_command_output_report_artifact_basis"] = _basis_stub(
        "selected_command_output_report_artifact_basis",
        COMMAND_OUTPUT_REPORT_ARTIFACT_RECORDED,
    )
    request["selected_command_execution_basis"] = _basis_stub("selected_command_execution_basis")
    request["selected_command_execution_basis"].update(
        {"execution_trace_audit_only": True, "audit_only": True}
    )
    request["selected_command_report_lineage_basis"] = _basis_stub(
        "selected_command_report_lineage_basis"
    )
    request["selected_command_report_lineage_basis"].update(
        {
            "command_report_lineage_only": True,
            "lineage_only": True,
            "command_report_lineage_treated_as_current_report_artifact": False,
            "command_report_lineage_treated_as_source": False,
            "command_report_lineage_treated_as_authority": False,
            "command_report_lineage_treated_as_currentness": False,
        }
    )
    request["selected_predecessor_failure_basis"] = _basis_stub(
        "selected_predecessor_failure_basis"
    )
    request["selected_predecessor_failure_basis"].update(
        {
            "predecessor_failure_evidence_visible": True,
            "predecessor_failures_visible": True,
            "predecessor_failure_evidence_hidden_or_repaired": False,
            "predecessor_failures_repaired": False,
            "predecessor_failures_hidden": False,
            "predecessor_failures_claimed_passed": False,
        }
    )
    request["selected_evidence_manifest_basis"] = _basis_stub("selected_evidence_manifest_basis")
    request["selected_artifact_containment_basis"] = _basis_stub(
        "selected_artifact_containment_basis"
    )
    request["selected_portable_verification_basis"] = _basis_stub(
        "selected_portable_verification_basis"
    )
    for key in POSTURE_KEYS:
        request[key] = _posture_stub(key)
    return request
