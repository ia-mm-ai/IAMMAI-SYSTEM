"""Bounded portable source-body verification second-carrier receipt resolver.

This module records at most one bounded second-carrier receipt posture
downstream of the clean second-carrier-receipt-boundary basis. Second-carrier
receipt remains receipt posture only. It is not second-carrier execution,
external result capture, cross-carrier evidence review, source transfer, source
receipt, reception authorization, source, authority, currentness, final
completion, runtime, continuation, reusable permission, derivative reception,
vessel relation, another reception request, or follow-on work.

The resolver is self-contained, uses only the Python standard library, imports
no repo-local modules, runs no commands, mutates no upstream artifact, and
never returns a raw full prior artifact body outside bounded receipt posture.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class PortableSourceBodyVerificationSecondCarrierReceiptError(Exception):
    """Raised for explicit unreadable path or malformed JSON path inputs."""


RESOLVER_MODULE = "resolve_portable_source_body_verification_second_carrier_receipt"
RESULT_TYPE = "portable_source_body_verification_second_carrier_receipt_result"
RESULT_VERSION = "0.1.0"
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_portable_source_body_verification_"
    "second_carrier_receipt"
)

CORE_QUESTION = (
    "Can the second-carrier-receipt-boundary basis be used to record one "
    "bounded second-carrier receipt without creating second-carrier execution, "
    "external result, cross-carrier evidence, source transfer, source receipt, "
    "reception authorization, source, authority, currentness, runtime, final "
    "completion, continuation, reusable permission, derivative reception, "
    "vessel relation, another reception request, or follow-on work?"
)

OUTCOME_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RECEIPT_RECORDED"
OUTCOME_NOT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RECEIPT_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RECEIPT_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RECEIPT_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RECEIPT"
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RECEIPT"
)
INTENT_BLOCK = "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RECEIPT"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

SECOND_CARRIER_RECEIPT_BOUNDARY_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RECEIPT_BOUNDARY_RECORDED"
)
SECOND_CARRIER_RECEIPT_BOUNDARY_RESULT_VERSION = "0.1.0"
PACKET_TRANSFER_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_TRANSFER_RECORDED"
PACKET_TRANSFER_RESULT_VERSION = "0.1.0"
PACKET_TRANSFER_BOUNDARY_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_TRANSFER_BOUNDARY_RECORDED"
)
PACKET_EMISSION_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_RECORDED"
PACKET_EMISSION_BOUNDARY_V2_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_BOUNDARY_RECORDED"
)
PACKET_ARTIFACT_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_ARTIFACT_RECORDED"
PACKET_BOUNDARY_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_BOUNDARY_RECORDED"
COMMAND_SUCCESS_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_RECORDED"
COMMAND_RESULT_V2_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_RECORDED"
OUTPUT_CAPTURE_V2_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_RECORDED"
COMMAND_OUTPUT_REPORT_ARTIFACT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_REPORT_ARTIFACT_RECORDED"
)
POST_INVOCATION_COMMAND_EXECUTION_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_RECORDED"
)

SUPPORTED_SECOND_CARRIER_RECEIPT_SCOPE = (
    "SECOND_CARRIER_RECEIPT_SPEC_ONLY",
    "ONE_BOUNDED_SECOND_CARRIER_RECEIPT_RECORDED",
    "SECOND_CARRIER_RECEIPT_BOUNDARY_BASIS_PRESERVED",
    "PACKET_TRANSFER_BASIS_PRESERVED",
    "TRANSFERRED_PACKET_BASIS_PRESERVED",
    "RECEIPT_RECORDED_BOUNDED",
    "RECEIPT_ARTIFACT_RECORDED_OR_BOUNDED",
    "RECEIPT_NOT_EXECUTION",
    "RECEIPT_NOT_EXTERNAL_RESULT",
    "RECEIPT_NOT_CROSS_CARRIER_EVIDENCE",
    "RECEIVING_CARRIER_NOT_AUTHORITY",
    "CARRIER_POSSESSION_NOT_AUTHORITY",
    "COPY_PRESENCE_NOT_AUTHORITY",
    "SECOND_CARRIER_EXECUTION_NOT_AUTHORIZED",
    "EXTERNAL_RESULT_NOT_CREATED",
    "CROSS_CARRIER_EVIDENCE_NOT_CREATED",
    "SOURCE_TRANSFER_NOT_AUTHORIZED",
    "SOURCE_RECEIPT_NOT_CREATED",
    "RECEPTION_AUTHORIZATION_NOT_CREATED",
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
    "NO_EXECUTION_INFERENCE",
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
    "HIDDEN_REPO_STATE_NOT_USED_AS_RECEIPT_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_NOT_RECEIPT_AUTHORITY",
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
    "selected_second_carrier_receipt_boundary_basis",
    "selected_second_carrier_receipt_boundary_terminal_summary_basis",
    "selected_packet_transfer_basis",
    "selected_packet_transfer_terminal_summary_basis",
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
    "second_carrier_receipt_spec_only_posture",
    "one_bounded_second_carrier_receipt_posture",
    "second_carrier_receipt_boundary_basis_preserved_posture",
    "packet_transfer_basis_preserved_posture",
    "transferred_packet_basis_preserved_posture",
    "receipt_recorded_bounded_posture",
    "receipt_artifact_recorded_or_bounded_posture",
    "receipt_not_execution_posture",
    "receipt_not_external_result_posture",
    "receipt_not_cross_carrier_evidence_posture",
    "receiving_carrier_not_authority_posture",
    "carrier_possession_not_authority_posture",
    "copy_presence_not_authority_posture",
    "second_carrier_execution_not_authorized_posture",
    "external_result_not_created_posture",
    "cross_carrier_evidence_not_created_posture",
    "source_transfer_not_authorized_posture",
    "source_receipt_not_created_posture",
    "reception_authorization_not_created_posture",
    "source_not_created_posture",
    "authority_not_created_posture",
    "currentness_not_created_posture",
    "final_completion_not_created_posture",
    "runtime_not_created_posture",
    "continuation_not_authorized_posture",
    "reusable_permission_not_created_posture",
    "follow_on_work_not_authorized_posture",
    "hidden_repo_state_excluded_posture",
    "repo_local_availability_not_receipt_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
)

REQUIRED_FALSE_NON_CLAIMS = (
    "second_carrier_execution_created",
    "external_result_created",
    "cross_carrier_evidence_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "second_carrier_receipt_treated_as_execution",
    "second_carrier_receipt_treated_as_external_result",
    "second_carrier_receipt_treated_as_cross_carrier_evidence",
    "second_carrier_receipt_treated_as_source_transfer",
    "second_carrier_receipt_treated_as_source_receipt",
    "second_carrier_receipt_treated_as_reception_authorization",
    "second_carrier_receipt_treated_as_source",
    "second_carrier_receipt_treated_as_authority",
    "second_carrier_receipt_treated_as_currentness",
    "second_carrier_receipt_treated_as_final_completion",
    "second_carrier_receipt_treated_as_runtime",
    "second_carrier_receipt_treated_as_continuation",
    "second_carrier_receipt_treated_as_reusable_permission",
    "second_carrier_receipt_treated_as_follow_on_work",
    "receiving_carrier_treated_as_authority",
    "carrier_possession_treated_as_authority",
    "copy_presence_treated_as_authority",
    "artifact_existence_treated_as_receipt_authority",
    "artifact_path_treated_as_currentness",
    "repo_local_availability_treated_as_receipt_authority",
    "hidden_repo_state_used_as_receipt_content",
    "hidden_repo_state_used_as_receipt_authority",
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
    "second_carrier_receipt_recorded",
    "bounded_second_carrier_receipt_recorded",
    "receipt_artifact_recorded_or_bounded",
    "second_carrier_receipt_boundary_basis_preserved",
    "packet_transfer_basis_preserved",
    "transferred_packet_basis_preserved",
    "receipt_recorded_bounded",
    "receipt_not_execution",
    "receipt_not_external_result",
    "receipt_not_cross_carrier_evidence",
    "receiving_carrier_not_authority",
    "carrier_possession_not_authority",
    "copy_presence_not_authority",
    "second_carrier_execution_not_authorized",
    "external_result_not_created",
    "cross_carrier_evidence_not_created",
    "source_transfer_not_authorized",
    "source_receipt_not_created",
    "reception_authorization_not_created",
    "source_not_created",
    "authority_not_created",
    "currentness_not_created",
    "final_completion_not_created",
    "runtime_not_created",
    "continuation_not_authorized",
    "reusable_permission_not_created",
    "follow_on_work_not_authorized",
    "hidden_repo_state_excluded",
    "hidden_repo_state_not_used_as_receipt_authority",
    "repo_local_availability_not_receipt_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
)

BLOCK_CODES = frozenset(
    {
        "DECLARED_SECOND_CARRIER_RECEIPT_REQUEST_MALFORMED",
        "DECLARED_SECOND_CARRIER_RECEIPT_REQUEST_UNREADABLE",
        "SECOND_CARRIER_RECEIPT_BLOCK_REQUESTED",
        "SECOND_CARRIER_RECEIPT_NOT_RECORD_REQUESTED",
        "SECOND_CARRIER_RECEIPT_QUESTION_UNDECLARED",
        "SECOND_CARRIER_RECEIPT_INTENT_UNSUPPORTED",
        "SECOND_CARRIER_RECEIPT_BOUNDARY_BASIS_MISSING",
        "SECOND_CARRIER_RECEIPT_BOUNDARY_TERMINAL_SUMMARY_BASIS_MISSING",
        "SECOND_CARRIER_RECEIPT_BOUNDARY_NOT_RECORDED",
        "SECOND_CARRIER_RECEIPT_BOUNDARY_FAILED_CHECKS_PRESENT",
        "SECOND_CARRIER_RECEIPT_BOUNDARY_VERSION_NOT_0_1_0",
        "SECOND_CARRIER_RECEIPT_BOUNDARY_DID_NOT_DECLARE_FUTURE_RECEIPT_STEP",
        "SECOND_CARRIER_RECEIPT_BOUNDARY_ALREADY_CREATED_RECEIPT",
        "SECOND_CARRIER_RECEIPT_BOUNDARY_ALREADY_CREATED_RECEIPT_ARTIFACT",
        "SECOND_CARRIER_RECEIPT_BOUNDARY_AUTHORIZED_SECOND_CARRIER_EXECUTION",
        "SECOND_CARRIER_RECEIPT_BOUNDARY_CREATED_EXTERNAL_RESULT",
        "SECOND_CARRIER_RECEIPT_BOUNDARY_CREATED_CROSS_CARRIER_EVIDENCE",
        "SECOND_CARRIER_RECEIPT_BOUNDARY_USED_HIDDEN_REPO_STATE_AS_RECEIPT_AUTHORITY",
        "SECOND_CARRIER_RECEIPT_BOUNDARY_TREATED_REPO_LOCAL_AVAILABILITY_AS_RECEIPT_AUTHORITY",
        "SECOND_CARRIER_RECEIPT_BOUNDARY_TREATED_CARRIER_POSSESSION_AS_RECEIPT_AUTHORITY",
        "SECOND_CARRIER_RECEIPT_BOUNDARY_TREATED_COPY_PRESENCE_AS_RECEIPT_AUTHORITY",
        "SECOND_CARRIER_RECEIPT_BOUNDARY_TREATED_RECEIVING_CARRIER_AS_AUTHORITY",
        "SECOND_CARRIER_RECEIPT_BOUNDARY_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY",
        "PACKET_TRANSFER_BASIS_MISSING",
        "PACKET_TRANSFER_TERMINAL_SUMMARY_BASIS_MISSING",
        "PACKET_TRANSFER_BOUNDARY_BASIS_MISSING",
        "PACKET_TRANSFER_NOT_RECORDED",
        "PACKET_TRANSFER_FAILED_CHECKS_PRESENT",
        "PACKET_TRANSFER_VERSION_NOT_0_1_0",
        "PACKET_TRANSFER_DID_NOT_RECORD_BOUNDED_PACKET_TRANSFER",
        "PACKET_TRANSFER_TREATED_TRANSFER_AS_RECEIPT",
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
        "SECOND_CARRIER_RECEIPT_TREATED_AS_EXECUTION",
        "SECOND_CARRIER_RECEIPT_TREATED_AS_EXTERNAL_RESULT",
        "SECOND_CARRIER_RECEIPT_TREATED_AS_CROSS_CARRIER_EVIDENCE",
        "SECOND_CARRIER_RECEIPT_TREATED_AS_SOURCE_TRANSFER",
        "SECOND_CARRIER_RECEIPT_TREATED_AS_SOURCE_RECEIPT",
        "SECOND_CARRIER_RECEIPT_TREATED_AS_RECEPTION_AUTHORIZATION",
        "SECOND_CARRIER_RECEIPT_TREATED_AS_SOURCE",
        "SECOND_CARRIER_RECEIPT_TREATED_AS_AUTHORITY",
        "SECOND_CARRIER_RECEIPT_TREATED_AS_CURRENTNESS",
        "SECOND_CARRIER_RECEIPT_TREATED_AS_FINAL_COMPLETION",
        "SECOND_CARRIER_RECEIPT_TREATED_AS_RUNTIME",
        "SECOND_CARRIER_RECEIPT_TREATED_AS_CONTINUATION",
        "SECOND_CARRIER_RECEIPT_TREATED_AS_REUSABLE_PERMISSION",
        "SECOND_CARRIER_RECEIPT_TREATED_AS_FOLLOW_ON_WORK",
        "SECOND_CARRIER_EXECUTION_CREATED",
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
        "CARRIER_POSSESSION_TREATED_AS_AUTHORITY",
        "COPY_PRESENCE_TREATED_AS_AUTHORITY",
        "ARTIFACT_EXISTENCE_TREATED_AS_RECEIPT_AUTHORITY",
        "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_RECEIPT_AUTHORITY",
        "HIDDEN_REPO_STATE_USED_AS_RECEIPT_CONTENT",
        "HIDDEN_REPO_STATE_USED_AS_RECEIPT_AUTHORITY",
        "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
        "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENT_REPORT_ARTIFACT",
        "COMMAND_REPORT_LINEAGE_TREATED_AS_SOURCE",
        "COMMAND_REPORT_LINEAGE_TREATED_AS_AUTHORITY",
        "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENTNESS",
        "CONSUMED_REQUEST_REOPENED",
        "AUTHORIZATION_TOKEN_REUSED",
        "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_RECEIPT",
        "ARTIFACTS_MUTATED",
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "UNSUPPORTED_SECOND_CARRIER_RECEIPT_SCOPE",
    }
)

NON_CLAIM_BLOCK_CODE_BY_KEY = {
    "second_carrier_execution_created": "SECOND_CARRIER_EXECUTION_CREATED",
    "external_result_created": "EXTERNAL_RESULT_CREATED",
    "cross_carrier_evidence_created": "CROSS_CARRIER_EVIDENCE_CREATED",
    "source_transfer_occurred": "SOURCE_TRANSFER_OCCURRED",
    "source_receipt_occurred": "SOURCE_RECEIPT_OCCURRED",
    "reception_authorization_created": "RECEPTION_AUTHORIZATION_CREATED",
    "second_carrier_receipt_treated_as_execution": (
        "SECOND_CARRIER_RECEIPT_TREATED_AS_EXECUTION"
    ),
    "second_carrier_receipt_treated_as_external_result": (
        "SECOND_CARRIER_RECEIPT_TREATED_AS_EXTERNAL_RESULT"
    ),
    "second_carrier_receipt_treated_as_cross_carrier_evidence": (
        "SECOND_CARRIER_RECEIPT_TREATED_AS_CROSS_CARRIER_EVIDENCE"
    ),
    "second_carrier_receipt_treated_as_source_transfer": (
        "SECOND_CARRIER_RECEIPT_TREATED_AS_SOURCE_TRANSFER"
    ),
    "second_carrier_receipt_treated_as_source_receipt": (
        "SECOND_CARRIER_RECEIPT_TREATED_AS_SOURCE_RECEIPT"
    ),
    "second_carrier_receipt_treated_as_reception_authorization": (
        "SECOND_CARRIER_RECEIPT_TREATED_AS_RECEPTION_AUTHORIZATION"
    ),
    "second_carrier_receipt_treated_as_source": "SECOND_CARRIER_RECEIPT_TREATED_AS_SOURCE",
    "second_carrier_receipt_treated_as_authority": (
        "SECOND_CARRIER_RECEIPT_TREATED_AS_AUTHORITY"
    ),
    "second_carrier_receipt_treated_as_currentness": (
        "SECOND_CARRIER_RECEIPT_TREATED_AS_CURRENTNESS"
    ),
    "second_carrier_receipt_treated_as_final_completion": (
        "SECOND_CARRIER_RECEIPT_TREATED_AS_FINAL_COMPLETION"
    ),
    "second_carrier_receipt_treated_as_runtime": (
        "SECOND_CARRIER_RECEIPT_TREATED_AS_RUNTIME"
    ),
    "second_carrier_receipt_treated_as_continuation": (
        "SECOND_CARRIER_RECEIPT_TREATED_AS_CONTINUATION"
    ),
    "second_carrier_receipt_treated_as_reusable_permission": (
        "SECOND_CARRIER_RECEIPT_TREATED_AS_REUSABLE_PERMISSION"
    ),
    "second_carrier_receipt_treated_as_follow_on_work": (
        "SECOND_CARRIER_RECEIPT_TREATED_AS_FOLLOW_ON_WORK"
    ),
    "receiving_carrier_treated_as_authority": "RECEIVING_CARRIER_TREATED_AS_AUTHORITY",
    "carrier_possession_treated_as_authority": "CARRIER_POSSESSION_TREATED_AS_AUTHORITY",
    "copy_presence_treated_as_authority": "COPY_PRESENCE_TREATED_AS_AUTHORITY",
    "artifact_existence_treated_as_receipt_authority": (
        "ARTIFACT_EXISTENCE_TREATED_AS_RECEIPT_AUTHORITY"
    ),
    "artifact_path_treated_as_currentness": "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "repo_local_availability_treated_as_receipt_authority": (
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_RECEIPT_AUTHORITY"
    ),
    "hidden_repo_state_used_as_receipt_content": "HIDDEN_REPO_STATE_USED_AS_RECEIPT_CONTENT",
    "hidden_repo_state_used_as_receipt_authority": (
        "HIDDEN_REPO_STATE_USED_AS_RECEIPT_AUTHORITY"
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

POSTURE_TO_STATEMENT = {
    "second_carrier_receipt_spec_only_posture": "second_carrier_receipt_recorded",
    "one_bounded_second_carrier_receipt_posture": (
        "bounded_second_carrier_receipt_recorded"
    ),
    "second_carrier_receipt_boundary_basis_preserved_posture": (
        "second_carrier_receipt_boundary_basis_preserved"
    ),
    "packet_transfer_basis_preserved_posture": "packet_transfer_basis_preserved",
    "transferred_packet_basis_preserved_posture": "transferred_packet_basis_preserved",
    "receipt_recorded_bounded_posture": "receipt_recorded_bounded",
    "receipt_artifact_recorded_or_bounded_posture": (
        "receipt_artifact_recorded_or_bounded"
    ),
    "receipt_not_execution_posture": "receipt_not_execution",
    "receipt_not_external_result_posture": "receipt_not_external_result",
    "receipt_not_cross_carrier_evidence_posture": "receipt_not_cross_carrier_evidence",
    "receiving_carrier_not_authority_posture": "receiving_carrier_not_authority",
    "carrier_possession_not_authority_posture": "carrier_possession_not_authority",
    "copy_presence_not_authority_posture": "copy_presence_not_authority",
    "second_carrier_execution_not_authorized_posture": (
        "second_carrier_execution_not_authorized"
    ),
    "external_result_not_created_posture": "external_result_not_created",
    "cross_carrier_evidence_not_created_posture": "cross_carrier_evidence_not_created",
    "source_transfer_not_authorized_posture": "source_transfer_not_authorized",
    "source_receipt_not_created_posture": "source_receipt_not_created",
    "reception_authorization_not_created_posture": "reception_authorization_not_created",
    "source_not_created_posture": "source_not_created",
    "authority_not_created_posture": "authority_not_created",
    "currentness_not_created_posture": "currentness_not_created",
    "final_completion_not_created_posture": "final_completion_not_created",
    "runtime_not_created_posture": "runtime_not_created",
    "continuation_not_authorized_posture": "continuation_not_authorized",
    "reusable_permission_not_created_posture": "reusable_permission_not_created",
    "follow_on_work_not_authorized_posture": "follow_on_work_not_authorized",
    "hidden_repo_state_excluded_posture": "hidden_repo_state_excluded",
    "repo_local_availability_not_receipt_authority_posture": (
        "repo_local_availability_not_receipt_authority"
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
    "receipt_body",
    "receipt_artifact_body",
    "execution_body",
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
    "unlisted_file_dependency",
}
REDACTED_REFERENCE_VALUE = "[bounded-reference-omitted-raw-or-hidden-state]"

WHAT_REMAINS_OPEN = (
    "second-carrier receipt test",
    "second-carrier receipt live artifact",
    "second-carrier receipt terminal summary, if needed",
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
        "RAW_SECOND_CARRIER_RECEIPT_BODY",
        "RAW_SECOND_CARRIER_RECEIPT_BOUNDARY_BODY",
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
            "second_carrier_receipt_request_id",
            "portable_source_body_verification_second_carrier_receipt_reference_review_001",
        )
    )
    return {
        "portable_source_body_verification_second_carrier_receipt_result_id": request_id,
        "portable_source_body_verification_second_carrier_receipt_request_id": request_id,
        "portable_source_body_verification_second_carrier_receipt_result_type": RESULT_TYPE,
        "portable_source_body_verification_second_carrier_receipt_result_version": (
            RESULT_VERSION
        ),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "resolver_module": RESOLVER_MODULE,
    }


def _build_declared_question(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "second_carrier_receipt_request_id": request.get("second_carrier_receipt_request_id"),
        "second_carrier_receipt_question": request.get("second_carrier_receipt_question"),
        "second_carrier_receipt_intent": request.get("second_carrier_receipt_intent"),
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
    if key == "selected_second_carrier_receipt_boundary_basis":
        section.update(
            {
                "selected_second_carrier_receipt_boundary_result_id": request.get(
                    "selected_second_carrier_receipt_boundary_result_id"
                ),
                "selected_second_carrier_receipt_boundary_result_path": request.get(
                    "selected_second_carrier_receipt_boundary_result_path"
                ),
                "selected_second_carrier_receipt_boundary_result_outcome": (
                    _extract_value(
                        request,
                        (
                            "selected_second_carrier_receipt_boundary_result_outcome",
                            "outcome",
                            "result_outcome",
                        ),
                        (key,),
                    )
                ),
                "selected_second_carrier_receipt_boundary_result_version": (
                    _extract_value(
                        request,
                        (
                            "selected_second_carrier_receipt_boundary_result_version",
                            "result_version",
                            "portable_source_body_verification_second_carrier_receipt_boundary_result_version",
                        ),
                        (key,),
                    )
                ),
                "selected_second_carrier_receipt_boundary_failed_check_count": (
                    _extract_value(
                        request,
                        (
                            "selected_second_carrier_receipt_boundary_failed_check_count",
                            "failed_check_count",
                        ),
                        (key,),
                    )
                ),
                "selected_second_carrier_receipt_boundary_declared_future_receipt_step": (
                    _extract_value(
                        request,
                        (
                            "selected_second_carrier_receipt_boundary_declared_future_receipt_step",
                            "one_future_second_carrier_receipt_step_declared",
                        ),
                        (key,),
                    )
                ),
            }
        )
    if key == "selected_packet_transfer_basis":
        section.update(
            {
                "selected_packet_transfer_result_id": request.get(
                    "selected_packet_transfer_result_id"
                ),
                "selected_packet_transfer_result_path": request.get(
                    "selected_packet_transfer_result_path"
                ),
                "selected_packet_transfer_result_outcome": _extract_value(
                    request,
                    ("selected_packet_transfer_result_outcome", "outcome", "result_outcome"),
                    (key,),
                ),
                "selected_packet_transfer_result_version": _extract_value(
                    request,
                    (
                        "selected_packet_transfer_result_version",
                        "result_version",
                        "portable_source_body_verification_packet_transfer_result_version",
                    ),
                    (key,),
                ),
                "selected_packet_transfer_failed_check_count": _extract_value(
                    request,
                    ("selected_packet_transfer_failed_check_count", "failed_check_count"),
                    (key,),
                ),
                "selected_packet_transfer_bounded_packet_transfer_recorded": (
                    _extract_value(
                        request,
                        (
                            "selected_packet_transfer_bounded_packet_transfer_recorded",
                            "bounded_packet_transfer_recorded",
                        ),
                        (key,),
                    )
                ),
                "selected_packet_transfer_transfer_not_receipt": _extract_value(
                    request,
                    ("selected_packet_transfer_transfer_not_receipt", "transfer_not_receipt"),
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
        "second_carrier_executed_anything": False,
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
        "receipt_became_execution": False,
        "receipt_became_external_result": False,
        "receipt_became_cross_carrier_proof": False,
        "receipt_became_source_transfer": False,
        "receipt_became_source_receipt": False,
        "receipt_became_reception_authorization": False,
        "receipt_became_source": False,
        "receipt_became_authority": False,
        "receipt_became_currentness": False,
        "receiving_carrier_became_authority": False,
        "transferred_packet_became_source": False,
        "transferred_packet_became_authority": False,
        "transferred_packet_became_currentness": False,
        "artifact_existence_became_receipt_authority": False,
        "artifact_path_became_currentness": False,
        "repo_local_availability_became_receipt_authority": False,
        "hidden_repo_state_became_receipt_authority": False,
        "v1_packet_emission_boundary_repaired": False,
        "v1_packet_emission_boundary_hidden": False,
        "v1_packet_emission_boundary_erased": False,
        "v1_packet_emission_boundary_claimed_passed": False,
    }


def _build_additional_basis(outcome: str, request: Mapping[str, Any]) -> dict[str, Any]:
    context = request.get("additional_basis_context")
    if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        return {
            "additional_basis_required": True,
            "missing_or_unclear_basis": _sanitize_reference(context),
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
                    "second-carrier receipt not recorded by declared intent",
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


def _forbidden_request_flag(
    request: Mapping[str, Any],
    key: str,
    basis_keys: tuple[str, ...] = SELECTED_BASIS_KEYS,
) -> bool:
    return _to_bool(_extract_value(request, (key,), basis_keys), False) is True


def _boundary_false_check(
    request: Mapping[str, Any],
    false_keys: tuple[str, ...],
    inverse_true_keys: tuple[str, ...],
) -> bool:
    actual_false = _to_bool(
        _extract_value(request, false_keys, ("selected_second_carrier_receipt_boundary_basis",)),
        None,
    )
    if actual_false is not None:
        return actual_false is False
    actual_inverse = _to_bool(
        _extract_value(
            request,
            inverse_true_keys,
            ("selected_second_carrier_receipt_boundary_basis",),
        ),
        None,
    )
    return actual_inverse is True


def _add_basis_presence_checks(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    basis_presence_checks = (
        (
            "second-carrier receipt boundary terminal summary basis declared",
            "selected_second_carrier_receipt_boundary_terminal_summary_basis",
            "SECOND_CARRIER_RECEIPT_BOUNDARY_TERMINAL_SUMMARY_BASIS_MISSING",
        ),
        (
            "packet transfer terminal summary basis declared",
            "selected_packet_transfer_terminal_summary_basis",
            "PACKET_TRANSFER_TERMINAL_SUMMARY_BASIS_MISSING",
        ),
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
        ("execution trace audit-only basis declared", "selected_command_execution_basis", "COMMAND_EXECUTION_BASIS_MISSING"),
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
            "declared second-carrier receipt request is a mapping",
            False,
            "mapping request",
            "malformed or missing request",
            malformed_code,
        )
        return checks

    question = request.get("second_carrier_receipt_question")
    intent = request.get("second_carrier_receipt_intent")
    scope = _scope_values(request.get("second_carrier_receipt_scope"))

    add(
        "second-carrier receipt question declared",
        question == CORE_QUESTION,
        CORE_QUESTION,
        question,
        "SECOND_CARRIER_RECEIPT_QUESTION_UNDECLARED",
    )
    add(
        "second-carrier receipt intent supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "SECOND_CARRIER_RECEIPT_INTENT_UNSUPPORTED",
    )
    if intent == INTENT_BLOCK:
        add(
            "explicit second-carrier receipt block requested",
            False,
            "non-blocking second-carrier receipt intent",
            intent,
            "SECOND_CARRIER_RECEIPT_BLOCK_REQUESTED",
        )

    unsupported_scope = sorted(set(scope) - set(SUPPORTED_SECOND_CARRIER_RECEIPT_SCOPE))
    add(
        "second-carrier receipt scope supported",
        bool(scope) and not unsupported_scope,
        sorted(SUPPORTED_SECOND_CARRIER_RECEIPT_SCOPE),
        scope,
        "UNSUPPORTED_SECOND_CARRIER_RECEIPT_SCOPE",
    )

    add(
        "second-carrier receipt boundary basis declared",
        _basis_declared(request, "selected_second_carrier_receipt_boundary_basis"),
        "selected second-carrier receipt boundary basis declared",
        request.get("selected_second_carrier_receipt_boundary_basis"),
        "SECOND_CARRIER_RECEIPT_BOUNDARY_BASIS_MISSING",
    )
    boundary_outcome = _extract_value(
        request,
        (
            "selected_second_carrier_receipt_boundary_result_outcome",
            "outcome",
            "result_outcome",
        ),
        ("selected_second_carrier_receipt_boundary_basis",),
    )
    add(
        "second-carrier receipt boundary outcome recorded",
        boundary_outcome == SECOND_CARRIER_RECEIPT_BOUNDARY_RECORDED,
        SECOND_CARRIER_RECEIPT_BOUNDARY_RECORDED,
        boundary_outcome,
        "SECOND_CARRIER_RECEIPT_BOUNDARY_NOT_RECORDED",
    )
    boundary_version = _extract_value(
        request,
        (
            "selected_second_carrier_receipt_boundary_result_version",
            "result_version",
            "portable_source_body_verification_second_carrier_receipt_boundary_result_version",
        ),
        ("selected_second_carrier_receipt_boundary_basis",),
    )
    add(
        "second-carrier receipt boundary version 0.1.0",
        boundary_version == SECOND_CARRIER_RECEIPT_BOUNDARY_RESULT_VERSION,
        SECOND_CARRIER_RECEIPT_BOUNDARY_RESULT_VERSION,
        boundary_version,
        "SECOND_CARRIER_RECEIPT_BOUNDARY_VERSION_NOT_0_1_0",
    )
    boundary_failed_count = _to_int(
        _extract_value(
            request,
            (
                "selected_second_carrier_receipt_boundary_failed_check_count",
                "failed_check_count",
            ),
            ("selected_second_carrier_receipt_boundary_basis",),
        )
    )
    add(
        "second-carrier receipt boundary failed checks zero",
        boundary_failed_count == 0,
        0,
        boundary_failed_count,
        "SECOND_CARRIER_RECEIPT_BOUNDARY_FAILED_CHECKS_PRESENT",
    )
    future_receipt_step = _to_bool(
        _extract_value(
            request,
            (
                "selected_second_carrier_receipt_boundary_declared_future_receipt_step",
                "one_future_second_carrier_receipt_step_declared",
            ),
            ("selected_second_carrier_receipt_boundary_basis",),
        ),
        None,
    )
    add(
        "second-carrier receipt boundary declared future receipt step",
        future_receipt_step is True,
        True,
        future_receipt_step,
        "SECOND_CARRIER_RECEIPT_BOUNDARY_DID_NOT_DECLARE_FUTURE_RECEIPT_STEP",
    )

    boundary_false_expectations = (
        (
            "second-carrier receipt boundary did not already create receipt",
            (
                "selected_second_carrier_receipt_boundary_already_created_receipt",
                "second_carrier_receipt_created",
            ),
            ("receipt_not_created",),
            "SECOND_CARRIER_RECEIPT_BOUNDARY_ALREADY_CREATED_RECEIPT",
        ),
        (
            "second-carrier receipt boundary did not already create receipt artifact",
            (
                "selected_second_carrier_receipt_boundary_already_created_receipt_artifact",
                "receipt_artifact_created",
            ),
            ("receipt_artifact_not_created",),
            "SECOND_CARRIER_RECEIPT_BOUNDARY_ALREADY_CREATED_RECEIPT_ARTIFACT",
        ),
        (
            "second-carrier receipt boundary did not authorize second-carrier execution",
            (
                "selected_second_carrier_receipt_boundary_authorized_second_carrier_execution",
                "second_carrier_execution_authorized",
                "second_carrier_execution_created",
            ),
            ("second_carrier_execution_not_authorized",),
            "SECOND_CARRIER_RECEIPT_BOUNDARY_AUTHORIZED_SECOND_CARRIER_EXECUTION",
        ),
        (
            "second-carrier receipt boundary did not create external result",
            (
                "selected_second_carrier_receipt_boundary_created_external_result",
                "external_result_created",
            ),
            ("external_result_not_created",),
            "SECOND_CARRIER_RECEIPT_BOUNDARY_CREATED_EXTERNAL_RESULT",
        ),
        (
            "second-carrier receipt boundary did not create cross-carrier evidence",
            (
                "selected_second_carrier_receipt_boundary_created_cross_carrier_evidence",
                "cross_carrier_evidence_created",
            ),
            ("cross_carrier_evidence_not_created",),
            "SECOND_CARRIER_RECEIPT_BOUNDARY_CREATED_CROSS_CARRIER_EVIDENCE",
        ),
        (
            "second-carrier receipt boundary did not use hidden repo state as receipt authority",
            (
                "selected_second_carrier_receipt_boundary_used_hidden_repo_state_as_receipt_authority",
                "hidden_repo_state_used_as_receipt_authority",
            ),
            ("hidden_repo_state_not_used_as_receipt_authority", "hidden_repo_state_excluded"),
            "SECOND_CARRIER_RECEIPT_BOUNDARY_USED_HIDDEN_REPO_STATE_AS_RECEIPT_AUTHORITY",
        ),
        (
            "second-carrier receipt boundary did not treat repo-local availability as receipt authority",
            (
                "selected_second_carrier_receipt_boundary_treated_repo_local_availability_as_receipt_authority",
                "repo_local_availability_treated_as_receipt_authority",
            ),
            ("repo_local_availability_not_receipt_authority",),
            "SECOND_CARRIER_RECEIPT_BOUNDARY_TREATED_REPO_LOCAL_AVAILABILITY_AS_RECEIPT_AUTHORITY",
        ),
        (
            "second-carrier receipt boundary did not treat carrier possession as receipt authority",
            (
                "selected_second_carrier_receipt_boundary_treated_carrier_possession_as_receipt_authority",
                "carrier_possession_treated_as_receipt_authority",
            ),
            ("carrier_possession_not_receipt_authority",),
            "SECOND_CARRIER_RECEIPT_BOUNDARY_TREATED_CARRIER_POSSESSION_AS_RECEIPT_AUTHORITY",
        ),
        (
            "second-carrier receipt boundary did not treat copy presence as receipt authority",
            (
                "selected_second_carrier_receipt_boundary_treated_copy_presence_as_receipt_authority",
                "copy_presence_treated_as_receipt_authority",
            ),
            ("copy_presence_not_receipt_authority",),
            "SECOND_CARRIER_RECEIPT_BOUNDARY_TREATED_COPY_PRESENCE_AS_RECEIPT_AUTHORITY",
        ),
        (
            "second-carrier receipt boundary did not treat receiving carrier as authority",
            (
                "selected_second_carrier_receipt_boundary_treated_receiving_carrier_as_authority",
                "receiving_carrier_treated_as_authority",
            ),
            ("receiving_carrier_not_authority",),
            "SECOND_CARRIER_RECEIPT_BOUNDARY_TREATED_RECEIVING_CARRIER_AS_AUTHORITY",
        ),
        (
            "second-carrier receipt boundary did not return raw full prior artifact body",
            (
                "selected_second_carrier_receipt_boundary_raw_full_prior_artifact_body_returned",
                "raw_full_prior_artifact_body_returned",
            ),
            ("raw_full_prior_artifact_body_not_returned",),
            "SECOND_CARRIER_RECEIPT_BOUNDARY_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY",
        ),
    )
    for name, false_keys, inverse_true_keys, code in boundary_false_expectations:
        add(
            name,
            _boundary_false_check(request, false_keys, inverse_true_keys),
            "false posture or explicit safe inverse",
            {
                "forbidden": _extract_value(
                    request, false_keys, ("selected_second_carrier_receipt_boundary_basis",)
                ),
                "safe_inverse": _extract_value(
                    request,
                    inverse_true_keys,
                    ("selected_second_carrier_receipt_boundary_basis",),
                ),
            },
            code,
        )

    add(
        "packet transfer basis declared",
        _basis_declared(request, "selected_packet_transfer_basis"),
        "selected packet transfer basis declared",
        request.get("selected_packet_transfer_basis"),
        "PACKET_TRANSFER_BASIS_MISSING",
    )
    packet_transfer_outcome = _extract_value(
        request,
        ("selected_packet_transfer_result_outcome", "outcome", "result_outcome"),
        ("selected_packet_transfer_basis",),
    )
    add(
        "packet transfer outcome recorded",
        packet_transfer_outcome == PACKET_TRANSFER_RECORDED,
        PACKET_TRANSFER_RECORDED,
        packet_transfer_outcome,
        "PACKET_TRANSFER_NOT_RECORDED",
    )
    packet_transfer_version = _extract_value(
        request,
        (
            "selected_packet_transfer_result_version",
            "result_version",
            "portable_source_body_verification_packet_transfer_result_version",
        ),
        ("selected_packet_transfer_basis",),
    )
    add(
        "packet transfer version 0.1.0",
        packet_transfer_version == PACKET_TRANSFER_RESULT_VERSION,
        PACKET_TRANSFER_RESULT_VERSION,
        packet_transfer_version,
        "PACKET_TRANSFER_VERSION_NOT_0_1_0",
    )
    packet_transfer_failed_count = _to_int(
        _extract_value(
            request,
            ("selected_packet_transfer_failed_check_count", "failed_check_count"),
            ("selected_packet_transfer_basis",),
        )
    )
    add(
        "packet transfer failed checks zero",
        packet_transfer_failed_count == 0,
        0,
        packet_transfer_failed_count,
        "PACKET_TRANSFER_FAILED_CHECKS_PRESENT",
    )
    bounded_packet_transfer = _to_bool(
        _extract_value(
            request,
            (
                "selected_packet_transfer_bounded_packet_transfer_recorded",
                "bounded_packet_transfer_recorded",
            ),
            ("selected_packet_transfer_basis",),
        )
    )
    add(
        "packet transfer recorded bounded packet transfer",
        bounded_packet_transfer is True,
        True,
        bounded_packet_transfer,
        "PACKET_TRANSFER_DID_NOT_RECORD_BOUNDED_PACKET_TRANSFER",
    )
    transfer_not_receipt = _to_bool(
        _extract_value(
            request,
            ("selected_packet_transfer_transfer_not_receipt", "transfer_not_receipt"),
            ("selected_packet_transfer_basis",),
        )
    )
    add(
        "packet transfer records transfer not receipt",
        transfer_not_receipt is True,
        True,
        transfer_not_receipt,
        "PACKET_TRANSFER_TREATED_TRANSFER_AS_RECEIPT",
    )

    _add_basis_presence_checks(request, checks)

    audit_only = _to_bool(
        _extract_value(
            request,
            ("execution_trace_audit_only",),
            ("selected_command_execution_basis",),
        ),
        True,
    )
    add(
        "execution trace remains audit-only",
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

    reference_shape = _to_bool(request.get("reference_shaped_input_posture"), True)
    add(
        "selected basis reference-shaped",
        reference_shape is True,
        True,
        reference_shape,
        "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    )
    raw_full_body_emitted = _to_bool(
        request.get("full_prior_artifact_body_emitted_outside_bounded_receipt"), False
    )
    add(
        "full prior artifact body not emitted outside bounded receipt posture",
        raw_full_body_emitted is False,
        False,
        raw_full_body_emitted,
        "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_RECEIPT",
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
    requested = request.get("requested_second_carrier_receipt_outcome")
    if requested == OUTCOME_REQUIRES_ADDITIONAL_BASIS or request.get("additional_basis_context"):
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS
    if requested == OUTCOME_NOT_RECORDED or request.get("not_recorded_basis"):
        return OUTCOME_NOT_RECORDED
    if request.get("second_carrier_receipt_intent") == INTENT_DO_NOT_RECORD:
        return OUTCOME_NOT_RECORDED
    return OUTCOME_RECORDED


def _build_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    outcome: str,
) -> dict[str, Any]:
    statement = _build_statement(outcome)
    result: dict[str, Any] = {
        "portable_source_body_verification_second_carrier_receipt_metadata": (
            _build_metadata(request)
        ),
        "declared_second_carrier_receipt_question": _build_declared_question(request),
    }
    for key in SELECTED_BASIS_KEYS:
        result[key] = _build_basis_section(request, key)
    for key in POSTURE_KEYS:
        result[key] = _build_posture_section(request, key, statement)

    result.update(
        {
            "second_carrier_receipt_scope": {
                "supported_scope": sorted(SUPPORTED_SECOND_CARRIER_RECEIPT_SCOPE),
                "declared_scope": list(_scope_values(request.get("second_carrier_receipt_scope"))),
                "unsupported_scope": sorted(
                    set(_scope_values(request.get("second_carrier_receipt_scope")))
                    - set(SUPPORTED_SECOND_CARRIER_RECEIPT_SCOPE)
                ),
            },
            "second_carrier_receipt_checks": checks,
            "second_carrier_receipt_statement": statement,
            "second_carrier_receipt_non_meaning": _build_non_meaning(),
            "additional_basis_required": _build_additional_basis(outcome, request),
            "not_recorded_basis": _build_not_recorded_basis(outcome, request),
            "what_remains_open": _build_what_remains_open(),
            "non_claims": _build_non_claims(),
            "outcome": outcome,
            "block": _block_from_checks(checks) if outcome == OUTCOME_BLOCKED else None,
        }
    )
    result["portable_source_body_verification_second_carrier_receipt_summary"] = (
        build_portable_source_body_verification_second_carrier_receipt_summary(result)
    )
    return _json_safe(result)


def resolve_portable_source_body_verification_second_carrier_receipt(
    declared_second_carrier_receipt_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded receipt posture without creating later authority."""

    malformed_code = None
    if declared_second_carrier_receipt_request is None or not _is_mapping(
        declared_second_carrier_receipt_request
    ):
        request: dict[str, Any] = {}
        malformed_code = "DECLARED_SECOND_CARRIER_RECEIPT_REQUEST_MALFORMED"
    else:
        request = copy.deepcopy(dict(declared_second_carrier_receipt_request))
        forced_block = request.get("_forced_block_code")
        if forced_block in BLOCK_CODES:
            malformed_code = str(forced_block)

    checks = _build_checks(request, malformed_code)
    outcome = _resolve_outcome(request, checks)
    return _build_result(request, checks, outcome)


def resolve_portable_source_body_verification_second_carrier_receipt_from_path(
    declared_second_carrier_receipt_request_path: Path | str,
) -> dict[str, Any]:
    """Read a JSON object request from a path and resolve receipt posture."""

    path = Path(declared_second_carrier_receipt_request_path)
    try:
        parsed = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise PortableSourceBodyVerificationSecondCarrierReceiptError(
            f"declared second-carrier receipt request path is unreadable: {path}"
        ) from exc
    except OSError as exc:
        raise PortableSourceBodyVerificationSecondCarrierReceiptError(
            f"declared second-carrier receipt request path is unreadable: {path}"
        ) from exc
    except json.JSONDecodeError as exc:
        raise PortableSourceBodyVerificationSecondCarrierReceiptError(
            f"declared second-carrier receipt request JSON is malformed: {path}"
        ) from exc

    if not _is_mapping(parsed):
        return resolve_portable_source_body_verification_second_carrier_receipt(
            {"_forced_block_code": "DECLARED_SECOND_CARRIER_RECEIPT_REQUEST_MALFORMED"}
        )
    return resolve_portable_source_body_verification_second_carrier_receipt(parsed)


def build_portable_source_body_verification_second_carrier_receipt_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact summary from a second-carrier receipt result."""

    metadata = result.get("portable_source_body_verification_second_carrier_receipt_metadata", {})
    declared = result.get("declared_second_carrier_receipt_question", {})
    statement = result.get("second_carrier_receipt_statement", {})
    checks = result.get("second_carrier_receipt_checks", [])
    block = result.get("block") or {}
    non_claims = result.get("non_claims", {})
    boundary_basis = result.get("selected_second_carrier_receipt_boundary_basis", {})

    if not _is_mapping(metadata):
        metadata = {}
    if not _is_mapping(declared):
        declared = {}
    if not _is_mapping(statement):
        statement = {}
    if not isinstance(checks, list):
        checks = []
    if not _is_mapping(block):
        block = {}
    if not _is_mapping(non_claims):
        non_claims = {}
    if not _is_mapping(boundary_basis):
        boundary_basis = {}

    key_non_claims = {
        key: bool(non_claims.get(key, False))
        for key in (
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
            "receiving_carrier_treated_as_authority",
            "carrier_possession_treated_as_authority",
            "copy_presence_treated_as_authority",
            "hidden_repo_state_used_as_receipt_authority",
            "authorization_token_reused",
            "consumed_request_reopened",
            "v1_repaired",
            "v1_hidden",
            "v1_claimed_passed",
        )
    }
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "request_id": metadata.get(
            "portable_source_body_verification_second_carrier_receipt_request_id"
        ),
        "question": declared.get("second_carrier_receipt_question"),
        "intent": declared.get("second_carrier_receipt_intent"),
        "passed_check_count": _check_count(checks, True),
        "failed_check_count": _check_count(checks, False),
        "second_carrier_receipt_recorded": bool(
            statement.get("second_carrier_receipt_recorded", False)
        ),
        "bounded_second_carrier_receipt_recorded": bool(
            statement.get("bounded_second_carrier_receipt_recorded", False)
        ),
        "receipt_artifact_recorded_or_bounded": bool(
            statement.get("receipt_artifact_recorded_or_bounded", False)
        ),
        "second_carrier_receipt_boundary_basis_preserved": bool(
            statement.get("second_carrier_receipt_boundary_basis_preserved", False)
        ),
        "packet_transfer_basis_preserved": bool(
            statement.get("packet_transfer_basis_preserved", False)
        ),
        "transferred_packet_basis_preserved": bool(
            statement.get("transferred_packet_basis_preserved", False)
        ),
        "receipt_recorded_bounded": bool(statement.get("receipt_recorded_bounded", False)),
        "receipt_not_execution": bool(statement.get("receipt_not_execution", False)),
        "receipt_not_external_result": bool(
            statement.get("receipt_not_external_result", False)
        ),
        "receipt_not_cross_carrier_evidence": bool(
            statement.get("receipt_not_cross_carrier_evidence", False)
        ),
        "receiving_carrier_not_authority": bool(
            statement.get("receiving_carrier_not_authority", False)
        ),
        "carrier_possession_not_authority": bool(
            statement.get("carrier_possession_not_authority", False)
        ),
        "copy_presence_not_authority": bool(statement.get("copy_presence_not_authority", False)),
        "second_carrier_execution_not_authorized": bool(
            statement.get("second_carrier_execution_not_authorized", False)
        ),
        "external_result_not_created": bool(statement.get("external_result_not_created", False)),
        "cross_carrier_evidence_not_created": bool(
            statement.get("cross_carrier_evidence_not_created", False)
        ),
        "source_transfer_not_authorized": bool(
            statement.get("source_transfer_not_authorized", False)
        ),
        "source_receipt_not_created": bool(statement.get("source_receipt_not_created", False)),
        "reception_authorization_not_created": bool(
            statement.get("reception_authorization_not_created", False)
        ),
        "source_not_created": bool(statement.get("source_not_created", False)),
        "authority_not_created": bool(statement.get("authority_not_created", False)),
        "currentness_not_created": bool(statement.get("currentness_not_created", False)),
        "final_completion_not_created": bool(
            statement.get("final_completion_not_created", False)
        ),
        "runtime_not_created": bool(statement.get("runtime_not_created", False)),
        "follow_on_work_not_authorized": bool(
            statement.get("follow_on_work_not_authorized", False)
        ),
        "hidden_repo_state_excluded": bool(statement.get("hidden_repo_state_excluded", False)),
        "hidden_repo_state_not_used_as_receipt_authority": bool(
            statement.get("hidden_repo_state_not_used_as_receipt_authority", False)
        ),
        "repo_local_availability_not_receipt_authority": bool(
            statement.get("repo_local_availability_not_receipt_authority", False)
        ),
        "selected_basis_reference_shape_preserved": bool(
            statement.get("selected_basis_reference_shape_preserved", False)
        ),
        "raw_full_prior_artifact_body_not_returned": bool(
            statement.get("raw_full_prior_artifact_body_not_returned", False)
        ),
        "selected_second_carrier_receipt_boundary_outcome": boundary_basis.get(
            "selected_second_carrier_receipt_boundary_result_outcome"
        ),
        "selected_second_carrier_receipt_boundary_version": boundary_basis.get(
            "selected_second_carrier_receipt_boundary_result_version"
        ),
        "selected_second_carrier_receipt_boundary_failed_check_count": boundary_basis.get(
            "selected_second_carrier_receipt_boundary_failed_check_count"
        ),
        "no_execution_external_result_cross_carrier_evidence": (
            key_non_claims["second_carrier_execution_created"] is False
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
        "key_non_claims": key_non_claims,
        "v1_predecessor_failure_preserved": True,
        "v1_not_repaired_hidden_or_claimed_passed": (
            key_non_claims["v1_repaired"] is False
            and key_non_claims["v1_hidden"] is False
            and key_non_claims["v1_claimed_passed"] is False
        ),
    }


def _safe_filename_part(value: Any) -> str:
    text = str(
        value
        or "portable_source_body_verification_second_carrier_receipt_reference_review_001"
    )
    safe = []
    for char in text:
        if char.isalnum() or char in {"-", "_", "."}:
            safe.append(char)
        else:
            safe.append("_")
    return (
        "".join(safe).strip("_")
        or "portable_source_body_verification_second_carrier_receipt_reference_review_001"
    )


def _next_available_path(path: Path) -> Path:
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


def write_portable_source_body_verification_second_carrier_receipt_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a second-carrier receipt result as stable UTF-8 JSON."""

    if not _is_mapping(result):
        raise PortableSourceBodyVerificationSecondCarrierReceiptError(
            "second-carrier receipt result must be a mapping"
        )
    metadata = result.get("portable_source_body_verification_second_carrier_receipt_metadata", {})
    if not _is_mapping(metadata):
        raise PortableSourceBodyVerificationSecondCarrierReceiptError(
            "second-carrier receipt result metadata must be a mapping"
        )
    request_id = metadata.get(
        "portable_source_body_verification_second_carrier_receipt_request_id",
        metadata.get("portable_source_body_verification_second_carrier_receipt_result_id"),
    )
    filename = (
        f"{_safe_filename_part(request_id)}"
        "__portable_source_body_verification_second_carrier_receipt_result.json"
    )
    if output_path is None:
        path = Path(OUTPUT_ROOT) / filename
    else:
        path = Path(output_path)
        if path.suffix.lower() != ".json":
            path = path / filename
    path = _next_available_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(_json_safe(result), indent=2, sort_keys=True, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    return path


def build_declared_portable_source_body_verification_second_carrier_receipt_request(
    second_carrier_receipt_request_id: str = (
        "portable_source_body_verification_second_carrier_receipt_reference_review_001"
    ),
    **overrides: Any,
) -> dict[str, Any]:
    """Build a valid receipt request with required non-claims false."""

    request: dict[str, Any] = {
        "second_carrier_receipt_request_id": second_carrier_receipt_request_id,
        "second_carrier_receipt_question": CORE_QUESTION,
        "second_carrier_receipt_intent": INTENT_RECORD,
        "selected_second_carrier_receipt_boundary_result_id": (
            "portable_source_body_verification_second_carrier_receipt_boundary_reference_review_001"
        ),
        "selected_second_carrier_receipt_boundary_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_receipt_boundary/"
            "portable_source_body_verification_second_carrier_receipt_boundary_reference_review_001__"
            "portable_source_body_verification_second_carrier_receipt_boundary_result.json"
        ),
        "selected_second_carrier_receipt_boundary_result_outcome": (
            SECOND_CARRIER_RECEIPT_BOUNDARY_RECORDED
        ),
        "selected_second_carrier_receipt_boundary_result_version": (
            SECOND_CARRIER_RECEIPT_BOUNDARY_RESULT_VERSION
        ),
        "selected_second_carrier_receipt_boundary_failed_check_count": 0,
        "selected_second_carrier_receipt_boundary_declared_future_receipt_step": True,
        "selected_second_carrier_receipt_boundary_already_created_receipt": False,
        "selected_second_carrier_receipt_boundary_already_created_receipt_artifact": False,
        "selected_second_carrier_receipt_boundary_authorized_second_carrier_execution": False,
        "selected_second_carrier_receipt_boundary_created_external_result": False,
        "selected_second_carrier_receipt_boundary_created_cross_carrier_evidence": False,
        "selected_second_carrier_receipt_boundary_used_hidden_repo_state_as_receipt_authority": False,
        "selected_second_carrier_receipt_boundary_treated_repo_local_availability_as_receipt_authority": False,
        "selected_second_carrier_receipt_boundary_treated_carrier_possession_as_receipt_authority": False,
        "selected_second_carrier_receipt_boundary_treated_copy_presence_as_receipt_authority": False,
        "selected_second_carrier_receipt_boundary_treated_receiving_carrier_as_authority": False,
        "selected_second_carrier_receipt_boundary_raw_full_prior_artifact_body_returned": False,
        "selected_packet_transfer_result_id": (
            "portable_source_body_verification_packet_transfer_reference_review_001"
        ),
        "selected_packet_transfer_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_packet_transfer/"
            "portable_source_body_verification_packet_transfer_reference_review_001__"
            "portable_source_body_verification_packet_transfer_result.json"
        ),
        "selected_packet_transfer_result_outcome": PACKET_TRANSFER_RECORDED,
        "selected_packet_transfer_result_version": PACKET_TRANSFER_RESULT_VERSION,
        "selected_packet_transfer_failed_check_count": 0,
        "selected_packet_transfer_bounded_packet_transfer_recorded": True,
        "selected_packet_transfer_transfer_not_receipt": True,
        "reference_shaped_input_posture": True,
        "authorization_token_reuse_blocked": True,
        "consumed_request_token_remains_closed": True,
        "second_carrier_receipt_scope": sorted(SUPPORTED_SECOND_CARRIER_RECEIPT_SCOPE),
        "declared_non_claims": _build_non_claims(),
    }

    basis_defaults = {
        "selected_second_carrier_receipt_boundary_basis": {
            "basis_type": "second_carrier_receipt_boundary",
            "outcome": SECOND_CARRIER_RECEIPT_BOUNDARY_RECORDED,
            "result_version": SECOND_CARRIER_RECEIPT_BOUNDARY_RESULT_VERSION,
            "failed_check_count": 0,
            "one_future_second_carrier_receipt_step_declared": True,
            "receipt_not_created": True,
            "receipt_artifact_not_created": True,
            "second_carrier_execution_not_authorized": True,
            "external_result_not_created": True,
            "cross_carrier_evidence_not_created": True,
            "receiving_carrier_not_authority": True,
            "carrier_possession_not_receipt_authority": True,
            "copy_presence_not_receipt_authority": True,
            "hidden_repo_state_excluded": True,
            "hidden_repo_state_not_used_as_receipt_authority": True,
            "repo_local_availability_not_receipt_authority": True,
            "raw_full_prior_artifact_body_not_returned": True,
            "second_carrier_receipt_created": False,
            "receipt_artifact_created": False,
            "second_carrier_execution_created": False,
            "external_result_created": False,
            "cross_carrier_evidence_created": False,
            "hidden_repo_state_used_as_receipt_authority": False,
            "repo_local_availability_treated_as_receipt_authority": False,
            "carrier_possession_treated_as_receipt_authority": False,
            "copy_presence_treated_as_receipt_authority": False,
            "receiving_carrier_treated_as_authority": False,
            "raw_full_prior_artifact_body_returned": False,
        },
        "selected_second_carrier_receipt_boundary_terminal_summary_basis": {
            "basis_type": "second_carrier_receipt_boundary_terminal_summary",
            "terminal_summary_readability_basis_only": True,
            "receipt_not_created": True,
            "receipt_artifact_not_created": True,
            "second_carrier_execution_not_authorized": True,
        },
        "selected_packet_transfer_basis": {
            "basis_type": "packet_transfer",
            "outcome": PACKET_TRANSFER_RECORDED,
            "result_version": PACKET_TRANSFER_RESULT_VERSION,
            "failed_check_count": 0,
            "bounded_packet_transfer_recorded": True,
            "transfer_not_receipt": True,
            "transfer_not_execution": True,
            "packet_transfer_recorded": True,
        },
        "selected_packet_transfer_terminal_summary_basis": {
            "basis_type": "packet_transfer_terminal_summary",
            "packet_transfer_recorded": True,
            "transfer_not_receipt": True,
        },
        "selected_packet_transfer_boundary_basis": {
            "basis_type": "packet_transfer_boundary",
            "outcome": PACKET_TRANSFER_BOUNDARY_RECORDED,
        },
        "selected_packet_emission_basis": {
            "basis_type": "packet_emission",
            "outcome": PACKET_EMISSION_RECORDED,
        },
        "selected_packet_emission_boundary_v2_basis": {
            "basis_type": "packet_emission_boundary_v2",
            "outcome": PACKET_EMISSION_BOUNDARY_V2_RECORDED,
        },
        "selected_packet_emission_boundary_v1_predecessor_failure_basis": {
            "basis_type": "packet_emission_boundary_v1_predecessor_failure",
            "visible": True,
            "v1_repaired": False,
            "v1_hidden": False,
            "v1_claimed_passed": False,
        },
        "selected_packet_artifact_basis": {
            "basis_type": "packet_artifact",
            "outcome": PACKET_ARTIFACT_RECORDED,
        },
        "selected_packet_boundary_basis": {
            "basis_type": "packet_boundary",
            "outcome": PACKET_BOUNDARY_RECORDED,
        },
        "selected_command_success_basis": {
            "basis_type": "command_success",
            "outcome": COMMAND_SUCCESS_RECORDED,
        },
        "selected_command_result_v2_basis": {
            "basis_type": "command_result_v2",
            "outcome": COMMAND_RESULT_V2_RECORDED,
        },
        "selected_output_capture_v2_basis": {
            "basis_type": "output_capture_v2",
            "outcome": OUTPUT_CAPTURE_V2_RECORDED,
        },
        "selected_command_output_report_artifact_basis": {
            "basis_type": "command_output_report_artifact",
            "outcome": COMMAND_OUTPUT_REPORT_ARTIFACT_RECORDED,
        },
        "selected_command_execution_basis": {
            "basis_type": "command_execution",
            "outcome": POST_INVOCATION_COMMAND_EXECUTION_RECORDED,
            "execution_trace_audit_only": True,
        },
        "selected_command_report_lineage_basis": {
            "basis_type": "command_report_lineage",
            "lineage_only": True,
            "command_report_lineage_treated_as_current_report_artifact": False,
            "command_report_lineage_treated_as_source": False,
            "command_report_lineage_treated_as_authority": False,
            "command_report_lineage_treated_as_currentness": False,
        },
        "selected_predecessor_failure_basis": {
            "basis_type": "predecessor_failure",
            "visible": True,
            "v1_repaired": False,
            "v1_hidden": False,
            "v1_claimed_passed": False,
        },
        "selected_evidence_manifest_basis": {
            "basis_type": "evidence_manifest",
            "basis_declared": True,
        },
        "selected_artifact_containment_basis": {
            "basis_type": "artifact_containment",
            "basis_declared": True,
        },
        "selected_portable_verification_basis": {
            "basis_type": "portable_verification",
            "basis_declared": True,
        },
    }
    request.update(basis_defaults)
    for posture_key in POSTURE_KEYS:
        request[posture_key] = {"declared": True, "posture_key": posture_key}
    request.update(copy.deepcopy(overrides))
    return request
