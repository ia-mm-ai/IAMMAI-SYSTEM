"""Bounded portable source-body verification packet transfer-boundary resolver.

This module is downstream of recorded packet emission. It may record one future
packet-transfer / copy-to-another-device step boundary only. The boundary is not
transfer, copying, source transfer, source receipt, reception authorization,
second-carrier receipt, second-carrier execution, external result capture,
cross-carrier evidence review, source, authority, currentness, runtime, final
completion, continuation, reusable permission, or follow-on work.

The v1 packet-emission-boundary resolver remains visible predecessor
conformance-failure evidence. This resolver does not repair it, hide it, or
claim it passed. It keeps selected basis sections reference-shaped, contains raw
or hidden-state payload values, imports no repo-local modules, runs no commands,
mutates no upstream artifact, and never returns a raw full prior artifact body.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class PortableSourceBodyVerificationPacketTransferBoundaryError(Exception):
    """Raised for hard packet-transfer-boundary input, output, or shape failures."""


RESOLVER_MODULE = "resolve_portable_source_body_verification_packet_transfer_boundary"
RESULT_TYPE = "portable_source_body_verification_packet_transfer_boundary_result"
RESULT_VERSION = "0.1.0"
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_portable_source_body_verification_packet_transfer_boundary"
)

CORE_QUESTION = (
    "Can the recorded packet-emission basis be bounded for one future "
    "packet-transfer / copy-to-another-device step without transferring it yet, "
    "copying it yet, creating source transfer, creating source receipt, creating "
    "reception authorization, creating second-carrier receipt or execution, "
    "creating external result, creating cross-carrier evidence, or creating "
    "source, authority, currentness, runtime, final completion, continuation, "
    "reusable permission, derivative reception, vessel relation, another "
    "reception request, or follow-on work?"
)

OUTCOME_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_TRANSFER_BOUNDARY_RECORDED"
OUTCOME_NOT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_TRANSFER_BOUNDARY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_TRANSFER_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_TRANSFER_BOUNDARY_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_TRANSFER_BOUNDARY"
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_TRANSFER_BOUNDARY"
)
INTENT_BLOCK = "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_TRANSFER_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

PACKET_EMISSION_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_RECORDED"
PACKET_EMISSION_RESULT_VERSION = "0.1.0"
PACKET_EMISSION_BOUNDARY_V2_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_BOUNDARY_RECORDED"
)
PACKET_EMISSION_BOUNDARY_V2_RESULT_VERSION = "0.2.0"
PACKET_ARTIFACT_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_ARTIFACT_RECORDED"
PACKET_BOUNDARY_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_BOUNDARY_RECORDED"
COMMAND_SUCCESS_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_RECORDED"
COMMAND_RESULT_V2_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_RECORDED"
OUTPUT_CAPTURE_V2_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_RECORDED"
COMMAND_OUTPUT_REPORT_ARTIFACT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_REPORT_ARTIFACT_RECORDED"
)

SUPPORTED_PACKET_TRANSFER_BOUNDARY_SCOPE = frozenset(
    {
        "PACKET_TRANSFER_BOUNDARY_ONLY",
        "ONE_FUTURE_TRANSFER_STEP_ONLY",
        "PACKET_EMISSION_BASIS_PRESERVED",
        "EMITTED_PACKET_BASIS_PRESERVED",
        "PACKET_EMISSION_NOT_TRANSFER",
        "TRANSFER_NOT_PERFORMED",
        "COPY_TO_ANOTHER_DEVICE_NOT_PERFORMED",
        "SECOND_CARRIER_RECEIPT_NOT_CREATED",
        "SECOND_CARRIER_EXECUTION_NOT_AUTHORIZED",
        "SOURCE_TRANSFER_NOT_AUTHORIZED",
        "SOURCE_RECEIPT_NOT_CREATED",
        "RECEPTION_AUTHORIZATION_NOT_CREATED",
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
        "NO_EXECUTION_INFERENCE",
        "NO_CROSS_CARRIER_EVIDENCE_INFERENCE",
        "NO_SOURCE_INFERENCE",
        "NO_AUTHORITY_INFERENCE",
        "NO_CURRENTNESS_INFERENCE",
        "NO_FINAL_COMPLETION_INFERENCE",
        "NO_RUNTIME_INFERENCE",
        "NO_FOLLOW_ON_WORK_INFERENCE",
        "NO_UNBOUNDED_PASS_FAIL_INFERENCE",
        "HIDDEN_REPO_STATE_EXCLUDED",
        "HIDDEN_REPO_STATE_NOT_USED_AS_TRANSFER_AUTHORITY",
        "REPO_LOCAL_AVAILABILITY_NOT_TRANSFER_AUTHORITY",
        "CARRIER_POSSESSION_NOT_RECEIPT_AUTHORITY",
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
    "selected_packet_emission_basis",
    "selected_packet_emission_terminal_summary_basis",
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
    "packet_transfer_boundary_only_posture",
    "one_future_transfer_step_posture",
    "packet_emission_basis_preserved_posture",
    "emitted_packet_basis_preserved_posture",
    "packet_emission_not_transfer_posture",
    "transfer_not_performed_posture",
    "copy_to_another_device_not_performed_posture",
    "second_carrier_receipt_not_created_posture",
    "second_carrier_execution_not_authorized_posture",
    "source_transfer_not_authorized_posture",
    "source_receipt_not_created_posture",
    "reception_authorization_not_created_posture",
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
    "repo_local_availability_not_transfer_authority_posture",
    "carrier_possession_not_receipt_authority_posture",
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
    "packet_transfer_boundary_treated_as_transfer",
    "packet_transfer_boundary_treated_as_copy_authorization",
    "packet_transfer_boundary_treated_as_source_transfer",
    "packet_transfer_boundary_treated_as_source_receipt",
    "packet_transfer_boundary_treated_as_reception_authorization",
    "packet_transfer_boundary_treated_as_second_carrier_receipt",
    "packet_transfer_boundary_treated_as_second_carrier_execution",
    "packet_transfer_boundary_treated_as_cross_carrier_evidence",
    "packet_transfer_boundary_treated_as_source",
    "packet_transfer_boundary_treated_as_authority",
    "packet_transfer_boundary_treated_as_currentness",
    "packet_transfer_boundary_treated_as_final_completion",
    "packet_transfer_boundary_treated_as_runtime",
    "packet_transfer_boundary_treated_as_continuation",
    "packet_transfer_boundary_treated_as_reusable_permission",
    "packet_transfer_boundary_treated_as_follow_on_work",
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
    "artifact_existence_treated_as_transfer_authority",
    "artifact_path_treated_as_currentness",
    "repo_local_availability_treated_as_transfer_authority",
    "carrier_possession_treated_as_receipt_authority",
    "hidden_repo_state_used_as_transfer_content",
    "hidden_repo_state_used_as_transfer_authority",
    "raw_full_prior_artifact_body_returned",
    "prior_artifacts_mutated",
    "consumed_request_reopened",
    "authorization_token_reused",
    "v1_repaired",
    "v1_hidden",
    "v1_claimed_passed",
)

EXTRA_FALSE_NON_CLAIMS = (
    "artifacts_mutated",
    "full_prior_artifact_body_emitted_outside_bounded_transfer",
    "selected_basis_not_reference_shaped",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "packet_transfer_boundary_recorded",
    "one_future_transfer_step_declared",
    "packet_emission_basis_preserved",
    "emitted_packet_basis_preserved",
    "packet_emission_not_transfer",
    "transfer_not_performed",
    "copy_to_another_device_not_performed",
    "second_carrier_receipt_not_created",
    "second_carrier_execution_not_authorized",
    "source_transfer_not_authorized",
    "source_receipt_not_created",
    "reception_authorization_not_created",
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
    "hidden_repo_state_not_used_as_transfer_authority",
    "repo_local_availability_not_transfer_authority",
    "carrier_possession_not_receipt_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
)

PUBLIC_BLOCK_CODES = (
    "DECLARED_PACKET_TRANSFER_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_PACKET_TRANSFER_BOUNDARY_REQUEST_UNREADABLE",
    "PACKET_TRANSFER_BOUNDARY_QUESTION_UNDECLARED",
    "PACKET_TRANSFER_BOUNDARY_INTENT_UNSUPPORTED",
    "PACKET_TRANSFER_BOUNDARY_EXPLICIT_BLOCK_INTENT",
    "PACKET_EMISSION_BASIS_MISSING",
    "PACKET_EMISSION_TERMINAL_SUMMARY_BASIS_MISSING",
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
    "PREDECESSOR_FAILURE_EVIDENCE_NOT_VISIBLE",
    "EVIDENCE_MANIFEST_BASIS_MISSING",
    "ARTIFACT_CONTAINMENT_BASIS_MISSING",
    "PORTABLE_VERIFICATION_BASIS_MISSING",
    "PACKET_EMISSION_NOT_RECORDED",
    "PACKET_EMISSION_FAILED_CHECKS_PRESENT",
    "PACKET_EMISSION_VERSION_NOT_0_1_0",
    "PACKET_EMISSION_DID_NOT_RECORD_BOUNDED_PACKET_EMISSION",
    "PACKET_EMISSION_DID_NOT_PRESERVE_V1_FAILURE",
    "PACKET_EMISSION_AUTHORIZED_TRANSFER",
    "PACKET_EMISSION_AUTHORIZED_COPY_TO_ANOTHER_DEVICE",
    "PACKET_EMISSION_AUTHORIZED_SOURCE_TRANSFER",
    "PACKET_EMISSION_CREATED_SOURCE_RECEIPT",
    "PACKET_EMISSION_CREATED_RECEPTION_AUTHORIZATION",
    "PACKET_EMISSION_CREATED_SECOND_CARRIER_RECEIPT",
    "PACKET_EMISSION_AUTHORIZED_SECOND_CARRIER_EXECUTION",
    "PACKET_EMISSION_CREATED_EXTERNAL_RESULT",
    "PACKET_EMISSION_CREATED_CROSS_CARRIER_EVIDENCE",
    "PACKET_EMISSION_USED_HIDDEN_REPO_STATE_AS_TRANSFER_AUTHORITY",
    "PACKET_EMISSION_TREATED_REPO_LOCAL_AVAILABILITY_AS_TRANSFER_AUTHORITY",
    "PACKET_EMISSION_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY_OUTSIDE_BOUNDED_EMISSION",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_TRANSFER",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_COPY_AUTHORIZATION",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_SECOND_CARRIER_RECEIPT",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_SECOND_CARRIER_EXECUTION",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_SOURCE",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_AUTHORITY",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_CURRENTNESS",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_FINAL_COMPLETION",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_RUNTIME",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_CONTINUATION",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION",
    "PACKET_TRANSFER_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_TRANSFER_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_TRANSFER_AUTHORITY",
    "CARRIER_POSSESSION_TREATED_AS_RECEIPT_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_TRANSFER_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_TRANSFER_AUTHORITY",
    "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENT_REPORT_ARTIFACT",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_SOURCE",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_AUTHORITY",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENTNESS",
    "COMMAND_REPORT_LINEAGE_NOT_LINEAGE_ONLY",
    "EXECUTION_TRACE_NOT_AUDIT_ONLY",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_TRANSFER",
    "ARTIFACTS_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_PACKET_TRANSFER_BOUNDARY_SCOPE",
    "PACKET_TRANSFER_BOUNDARY_ONLY_POSTURE_MISSING",
    "ONE_FUTURE_TRANSFER_STEP_POSTURE_MISSING",
    "PACKET_EMISSION_BASIS_PRESERVED_POSTURE_MISSING",
    "EMITTED_PACKET_BASIS_PRESERVED_POSTURE_MISSING",
    "PACKET_EMISSION_NOT_TRANSFER_POSTURE_MISSING",
    "TRANSFER_NOT_PERFORMED_POSTURE_MISSING",
    "COPY_TO_ANOTHER_DEVICE_NOT_PERFORMED_POSTURE_MISSING",
    "SECOND_CARRIER_RECEIPT_NOT_CREATED_POSTURE_MISSING",
    "SECOND_CARRIER_EXECUTION_NOT_AUTHORIZED_POSTURE_MISSING",
    "SOURCE_TRANSFER_NOT_AUTHORIZED_POSTURE_MISSING",
    "SOURCE_RECEIPT_NOT_CREATED_POSTURE_MISSING",
    "RECEPTION_AUTHORIZATION_NOT_CREATED_POSTURE_MISSING",
    "EXTERNAL_RESULT_NOT_CREATED_POSTURE_MISSING",
    "CROSS_CARRIER_EVIDENCE_NOT_CREATED_POSTURE_MISSING",
    "NO_SOURCE_AUTHORITY_CURRENTNESS_FINAL_COMPLETION_RUNTIME_FOLLOW_ON_POSTURE_MISSING",
    "HIDDEN_REPO_STATE_EXCLUDED_POSTURE_MISSING",
    "REPO_LOCAL_AVAILABILITY_NOT_TRANSFER_AUTHORITY_POSTURE_MISSING",
    "CARRIER_POSSESSION_NOT_RECEIPT_AUTHORITY_POSTURE_MISSING",
    "SELECTED_BASIS_REFERENCE_SHAPE_POSTURE_MISSING",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED_POSTURE_MISSING",
)
BLOCK_CODES = frozenset(PUBLIC_BLOCK_CODES)

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
    "packet_transfer_boundary_treated_as_transfer": "PACKET_TRANSFER_BOUNDARY_TREATED_AS_TRANSFER",
    "packet_transfer_boundary_treated_as_copy_authorization": "PACKET_TRANSFER_BOUNDARY_TREATED_AS_COPY_AUTHORIZATION",
    "packet_transfer_boundary_treated_as_source_transfer": "PACKET_TRANSFER_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "packet_transfer_boundary_treated_as_source_receipt": "PACKET_TRANSFER_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "packet_transfer_boundary_treated_as_reception_authorization": "PACKET_TRANSFER_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "packet_transfer_boundary_treated_as_second_carrier_receipt": "PACKET_TRANSFER_BOUNDARY_TREATED_AS_SECOND_CARRIER_RECEIPT",
    "packet_transfer_boundary_treated_as_second_carrier_execution": "PACKET_TRANSFER_BOUNDARY_TREATED_AS_SECOND_CARRIER_EXECUTION",
    "packet_transfer_boundary_treated_as_cross_carrier_evidence": "PACKET_TRANSFER_BOUNDARY_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "packet_transfer_boundary_treated_as_source": "PACKET_TRANSFER_BOUNDARY_TREATED_AS_SOURCE",
    "packet_transfer_boundary_treated_as_authority": "PACKET_TRANSFER_BOUNDARY_TREATED_AS_AUTHORITY",
    "packet_transfer_boundary_treated_as_currentness": "PACKET_TRANSFER_BOUNDARY_TREATED_AS_CURRENTNESS",
    "packet_transfer_boundary_treated_as_final_completion": "PACKET_TRANSFER_BOUNDARY_TREATED_AS_FINAL_COMPLETION",
    "packet_transfer_boundary_treated_as_runtime": "PACKET_TRANSFER_BOUNDARY_TREATED_AS_RUNTIME",
    "packet_transfer_boundary_treated_as_continuation": "PACKET_TRANSFER_BOUNDARY_TREATED_AS_CONTINUATION",
    "packet_transfer_boundary_treated_as_reusable_permission": "PACKET_TRANSFER_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION",
    "packet_transfer_boundary_treated_as_follow_on_work": "PACKET_TRANSFER_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
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
    "artifact_existence_treated_as_transfer_authority": "ARTIFACT_EXISTENCE_TREATED_AS_TRANSFER_AUTHORITY",
    "artifact_path_treated_as_currentness": "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "repo_local_availability_treated_as_transfer_authority": "REPO_LOCAL_AVAILABILITY_TREATED_AS_TRANSFER_AUTHORITY",
    "carrier_possession_treated_as_receipt_authority": "CARRIER_POSSESSION_TREATED_AS_RECEIPT_AUTHORITY",
    "hidden_repo_state_used_as_transfer_content": "HIDDEN_REPO_STATE_USED_AS_TRANSFER_CONTENT",
    "hidden_repo_state_used_as_transfer_authority": "HIDDEN_REPO_STATE_USED_AS_TRANSFER_AUTHORITY",
    "raw_full_prior_artifact_body_returned": "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "prior_artifacts_mutated": "ARTIFACTS_MUTATED",
    "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
    "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
    "v1_repaired": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "v1_hidden": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "v1_claimed_passed": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "artifacts_mutated": "ARTIFACTS_MUTATED",
    "full_prior_artifact_body_emitted_outside_bounded_transfer": (
        "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_TRANSFER"
    ),
    "selected_basis_not_reference_shaped": "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
}

SENSITIVE_EXACT_KEYS = frozenset(
    {
        "raw_body",
        "raw_full_body",
        "raw_full_prior_body",
        "raw_full_prior_artifact_body",
        "full_body",
        "full_prior_body",
        "full_prior_artifact_body",
        "artifact_body",
        "prior_artifact_body",
        "raw_prior_artifact_body",
        "prior_artifact_raw_body",
        "raw_result_body",
        "raw_output_body",
        "emitted_packet_body",
        "packet_body",
        "packet_transfer_body",
        "transfer_body",
        "transfer_artifact_body",
        "copy_body",
        "copy_artifact_body",
        "copy_to_another_device_body",
        "source_body",
        "authority_body",
        "hidden_repo_state",
        "current_working_tree",
        "local_cache",
        "repo_local_only_dependency",
        "unlisted_file_dependency",
    }
)
REDACTION = "[bounded-reference-omitted-raw-or-hidden-state]"
HOSTILE_SENTINELS = (
    "RAW_PACKET_TRANSFER_BODY_MUST_NOT_RETURN",
    "RAW_PACKET_EMISSION_BODY_MUST_NOT_RETURN",
    "RAW_PORTABLE_SOURCE_BODY_MUST_NOT_RETURN",
)


def _is_mapping(value: Any) -> bool:
    return isinstance(value, Mapping)


def _copy(value: Any) -> Any:
    return copy.deepcopy(value)


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _json_safe(value: Any, key_hint: str | None = None) -> Any:
    if key_hint in SENSITIVE_EXACT_KEYS:
        return REDACTION
    if _is_mapping(value):
        result: dict[str, Any] = {}
        for key, item in value.items():
            key_text = str(key)
            result[key_text] = _json_safe(item, key_text)
        return result
    if isinstance(value, list):
        return [_json_safe(item) for item in value]
    if isinstance(value, tuple):
        return [_json_safe(item) for item in value]
    if isinstance(value, set) or isinstance(value, frozenset):
        return sorted(_json_safe(item) for item in value)
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, str):
        if any(sentinel in value for sentinel in HOSTILE_SENTINELS):
            return REDACTION
        return value
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    return str(value)


def _declared(value: Any) -> bool:
    if value is None:
        return False
    if value is False:
        return False
    if value == "":
        return False
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes)) and len(value) == 0:
        return False
    if _is_mapping(value) and value.get("declared") is False:
        return False
    return True


def _deep_find(mapping: Any, names: Sequence[str], default: Any = None) -> Any:
    if not _is_mapping(mapping):
        return default
    for name in names:
        if name in mapping:
            return mapping[name]
    for value in mapping.values():
        if _is_mapping(value):
            found = _deep_find(value, names, default=None)
            if found is not None:
                return found
        elif isinstance(value, list):
            for item in value:
                found = _deep_find(item, names, default=None)
                if found is not None:
                    return found
    return default


def _value(
    request: Mapping[str, Any],
    shortcut_names: Sequence[str],
    section_key: str,
    default: Any = None,
) -> Any:
    for name in shortcut_names:
        if name in request:
            return request[name]
    section = request.get(section_key)
    found = _deep_find(section, shortcut_names, default=None)
    if found is not None:
        return found
    return default


def _values(
    request: Mapping[str, Any],
    shortcut_names: Sequence[str],
    section_key: str,
) -> list[Any]:
    found: list[Any] = []
    for name in shortcut_names:
        if name in request:
            found.append(request[name])
    section = request.get(section_key)
    for name in shortcut_names:
        section_value = _deep_find(section, (name,), default=None)
        if section_value is not None:
            found.append(section_value)
    return found


def _as_int(value: Any, default: int | None = None) -> int | None:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            return default
    return default


def _scope_values(request: Mapping[str, Any]) -> list[str]:
    value = request.get("packet_transfer_boundary_scope", [])
    if _is_mapping(value):
        value = value.get("scope_values", [])
    if isinstance(value, str):
        return [value]
    if isinstance(value, Sequence):
        return [str(item) for item in value]
    return []


def _non_claims_from_request(request: Mapping[str, Any]) -> dict[str, Any]:
    declared = request.get("declared_non_claims", {})
    result: dict[str, Any] = {}
    for key in REQUIRED_FALSE_NON_CLAIMS + EXTRA_FALSE_NON_CLAIMS:
        if _is_mapping(declared) and key in declared:
            result[key] = declared[key]
        elif key in request:
            result[key] = request[key]
        else:
            result[key] = None
    return result


def _any_true(
    request: Mapping[str, Any],
    names: Sequence[str],
    section_key: str | None = None,
) -> bool:
    for name in names:
        if request.get(name) is True:
            return True
    declared = request.get("declared_non_claims", {})
    if _is_mapping(declared):
        for name in names:
            if declared.get(name) is True:
                return True
    if section_key is not None:
        section = request.get(section_key)
        for name in names:
            if _deep_find(section, (name,), default=None) is True:
                return True
    return False


def _check(
    checks: list[dict[str, Any]],
    name: str,
    passed: bool,
    expected: Any,
    actual: Any,
    code: str,
) -> None:
    if code not in BLOCK_CODES:
        raise PortableSourceBodyVerificationPacketTransferBoundaryError(
            f"undeclared packet-transfer-boundary block code: {code}"
        )
    check = {
        "check_name": name,
        "passed": bool(passed),
        "expected_posture": _json_safe(expected),
        "actual_posture": _json_safe(actual),
        "block_code": None,
        "failure_code": None,
    }
    if not passed:
        check["block_code"] = code
        check["failure_code"] = code
    checks.append(check)


def _failed_code(checks: Sequence[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if not check.get("passed"):
            code = check.get("block_code") or check.get("failure_code")
            return str(code or "NON_CLAIM_MISSING_OR_FLIPPED")
    return None


def _safe_basis_section(
    key: str,
    section: Any,
    request: Mapping[str, Any],
) -> dict[str, Any]:
    result: dict[str, Any] = {
        "basis_key": key,
        "declared": _declared(section),
        "basis_only": True,
        "reference_shaped": True,
        "selected_basis_reference_shape_preserved": True,
        "raw_full_prior_artifact_body_returned": False,
        "raw_full_prior_artifact_body_not_returned": True,
        "hidden_repo_state_excluded": True,
        "hidden_repo_state_not_used_as_transfer_authority": True,
        "repo_local_availability_not_transfer_authority": True,
        "carrier_possession_not_receipt_authority": True,
    }
    if _is_mapping(section):
        for item_key, item_value in section.items():
            item_key_text = str(item_key)
            if item_key_text in SENSITIVE_EXACT_KEYS:
                result[item_key_text] = REDACTION
            else:
                result[item_key_text] = _json_safe(item_value, item_key_text)

    if key == "selected_packet_emission_basis":
        result.setdefault(
            "result_path",
            _json_safe(request.get("selected_packet_emission_result_path")),
        )
        result.setdefault("result_id", request.get("selected_packet_emission_result_id"))
        result.setdefault(
            "outcome",
            request.get("selected_packet_emission_result_outcome", result.get("outcome")),
        )
        result.setdefault(
            "result_version",
            request.get("selected_packet_emission_result_version", result.get("result_version")),
        )
        result.setdefault(
            "failed_check_count",
            request.get(
                "selected_packet_emission_failed_check_count",
                result.get("failed_check_count"),
            ),
        )
        result.setdefault(
            "bounded_packet_emission_recorded",
            request.get(
                "selected_packet_emission_bounded_packet_emission_recorded",
                result.get("bounded_packet_emission_recorded"),
            ),
        )
        result.setdefault(
            "packet_emission_boundary_v1_failure_preserved",
            request.get(
                "selected_packet_emission_v1_failure_preserved",
                result.get("packet_emission_boundary_v1_failure_preserved"),
            ),
        )
    elif key == "selected_packet_emission_boundary_v2_basis":
        result.setdefault(
            "result_path",
            _json_safe(request.get("selected_packet_emission_boundary_v2_result_path")),
        )
    elif key == "selected_packet_artifact_basis":
        result.setdefault(
            "result_path",
            _json_safe(request.get("selected_packet_artifact_result_path")),
        )
    return _json_safe(result)


def _posture_section(key: str, request: Mapping[str, Any], recorded: bool) -> dict[str, Any]:
    source = request.get(key)
    result: dict[str, Any] = {
        "posture_key": key,
        "declared": _declared(source),
        "packet_transfer_boundary_posture_only": True,
        "packet_transfer_boundary_recorded": recorded,
        "one_future_transfer_step_declared": recorded,
        "packet_emission_basis_preserved": recorded,
        "emitted_packet_basis_preserved": recorded,
        "packet_emission_not_transfer": recorded,
        "transfer_not_performed": recorded,
        "copy_to_another_device_not_performed": recorded,
        "second_carrier_receipt_not_created": recorded,
        "second_carrier_execution_not_authorized": recorded,
        "source_transfer_not_authorized": recorded,
        "source_receipt_not_created": recorded,
        "reception_authorization_not_created": recorded,
        "external_result_not_created": recorded,
        "cross_carrier_evidence_not_created": recorded,
        "source_not_created": recorded,
        "authority_not_created": recorded,
        "currentness_not_created": recorded,
        "final_completion_not_created": recorded,
        "runtime_not_created": recorded,
        "continuation_not_authorized": recorded,
        "reusable_permission_not_created": recorded,
        "follow_on_work_not_authorized": recorded,
        "hidden_repo_state_excluded": recorded,
        "hidden_repo_state_not_used_as_transfer_authority": recorded,
        "repo_local_availability_not_transfer_authority": recorded,
        "carrier_possession_not_receipt_authority": recorded,
        "selected_basis_reference_shape_preserved": recorded,
        "raw_full_prior_artifact_body_not_returned": recorded,
        "authorization_token_reuse_blocked": recorded,
        "consumed_request_token_remains_closed": recorded,
    }
    if _is_mapping(source):
        result["source_posture_reference"] = _json_safe(source)
    return result


def _statement(recorded: bool) -> dict[str, Any]:
    statement = {key: False for key in REQUIRED_FALSE_NON_CLAIMS}
    statement.update({key: False for key in EXTRA_FALSE_NON_CLAIMS})
    statement.update({key: recorded for key in ALLOWED_TRUE_RECORDED_FIELDS})
    statement.update(
        {
            "packet_transfer_boundary_is_not_packet_transfer": True,
            "packet_transfer_boundary_is_not_copy_to_another_device": True,
            "packet_transfer_boundary_is_not_source_transfer": True,
            "packet_transfer_boundary_is_not_source_receipt": True,
            "packet_transfer_boundary_is_not_reception_authorization": True,
            "packet_transfer_boundary_is_not_second_carrier_receipt": True,
            "packet_transfer_boundary_is_not_second_carrier_execution": True,
            "packet_transfer_boundary_is_not_external_result": True,
            "packet_transfer_boundary_is_not_cross_carrier_evidence": True,
            "packet_transfer_boundary_is_not_source_authority_currentness_runtime_final_completion": True,
            "packet_emission_remains_bounded_local_emission_posture": True,
            "emitted_packet_remains_bounded_local_emission_posture": True,
            "actual_transfer_requires_separate_bounded_step": True,
            "copy_to_another_device_requires_separate_bounded_step": True,
            "second_carrier_receipt_or_execution_requires_separate_bounded_step": True,
            "cross_carrier_evidence_review_requires_separate_bounded_step": True,
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
        "transfer_boundary_became_transfer": False,
        "transfer_boundary_became_copy_authorization": False,
        "transfer_boundary_became_second_carrier_receipt": False,
        "transfer_boundary_became_second_carrier_execution": False,
        "transfer_boundary_became_cross_carrier_proof": False,
        "transfer_boundary_became_source_authority_currentness": False,
        "carrier_possession_became_receipt": False,
        "artifact_existence_became_transfer_authority": False,
        "artifact_path_became_currentness": False,
        "repo_local_availability_became_transfer_authority": False,
        "hidden_repo_state_became_transfer_authority": False,
        "v1_packet_emission_boundary_resolver_was_repaired_hidden_erased_or_claimed_passed": False,
    }


def _additional_basis_required(request: Mapping[str, Any], outcome: str) -> dict[str, Any]:
    return {
        "additional_basis_required": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "missing_or_unclear_basis": _json_safe(request.get("additional_basis_context", []))
        if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
        else [],
        "missing_basis_not_scheduled": True,
        "missing_basis_not_authorized": True,
        "missing_basis_not_executed": True,
        "packet_transferred": False,
        "packet_copied_to_another_device": False,
        "source_created": False,
        "authority_created": False,
        "currentness_created": False,
        "final_completion_claimed": False,
        "runtime_hosting_created": False,
        "follow_on_work_authorized": False,
    }


def _not_recorded_basis(
    request: Mapping[str, Any],
    outcome: str,
    failed_code: str | None,
) -> dict[str, Any]:
    return {
        "not_recorded": outcome == OUTCOME_NOT_RECORDED,
        "not_recorded_reason": _json_safe(request.get("not_recorded_basis"))
        if outcome == OUTCOME_NOT_RECORDED
        else None,
        "failed_review_code": failed_code if outcome == OUTCOME_NOT_RECORDED else None,
        "packet_transferred": False,
        "packet_copied_to_another_device": False,
        "source_created": False,
        "authority_created": False,
        "currentness_created": False,
        "final_completion_claimed": False,
        "runtime_hosting_created": False,
        "cross_carrier_evidence_created": False,
        "follow_on_work_authorized": False,
        "artifacts_mutated": False,
    }


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "packet transfer boundary test",
            "packet transfer boundary live artifact",
            "packet transfer boundary terminal summary, if needed",
            "packet transfer spec/resolver/test/live artifact",
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


def _all_selected_basis_reference_shaped(request: Mapping[str, Any]) -> bool:
    if request.get("reference_shaped_input_posture") is False:
        return False
    if request.get("selected_basis_not_reference_shaped") is True:
        return False
    for key in SELECTED_BASIS_KEYS:
        section = request.get(key)
        if not _is_mapping(section):
            continue
        if section.get("reference_shaped") is False:
            return False
        if section.get("selected_basis_reference_shape_preserved") is False:
            return False
        if section.get("selected_basis_not_reference_shaped") is True:
            return False
    return True


def _all_raw_full_prior_body_not_returned(request: Mapping[str, Any]) -> bool:
    if request.get("raw_full_prior_artifact_body_returned") is True:
        return False
    if request.get("full_prior_artifact_body_emitted_outside_bounded_transfer") is True:
        return False
    for key in SELECTED_BASIS_KEYS:
        section = request.get(key)
        if not _is_mapping(section):
            continue
        if section.get("raw_full_prior_artifact_body_returned") is True:
            return False
        if section.get("raw_full_prior_artifact_body_not_returned") is False:
            return False
        if section.get("full_prior_artifact_body_emitted_outside_bounded_transfer") is True:
            return False
    return True


def _hidden_repo_state_excluded(request: Mapping[str, Any]) -> bool:
    if request.get("hidden_repo_state_excluded") is False:
        return False
    if request.get("hidden_repo_state_used_as_transfer_content") is True:
        return False
    if request.get("hidden_repo_state_used_as_transfer_authority") is True:
        return False
    for key in SELECTED_BASIS_KEYS:
        section = request.get(key)
        if not _is_mapping(section):
            continue
        if section.get("hidden_repo_state_excluded") is False:
            return False
        if section.get("hidden_repo_state_used_as_transfer_content") is True:
            return False
        if section.get("hidden_repo_state_used_as_transfer_authority") is True:
            return False
    return True


def _build_checks(request: Mapping[str, Any] | None) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    if not _is_mapping(request):
        _check(
            checks,
            "declared packet transfer boundary request is mapping",
            False,
            "mapping request",
            type(request).__name__,
            "DECLARED_PACKET_TRANSFER_BOUNDARY_REQUEST_MALFORMED",
        )
        return checks

    question = request.get("packet_transfer_boundary_question")
    intent = request.get("packet_transfer_boundary_intent")
    scope_values = _scope_values(request)
    unsupported_scope = sorted(
        value for value in scope_values if value not in SUPPORTED_PACKET_TRANSFER_BOUNDARY_SCOPE
    )

    _check(
        checks,
        "packet transfer boundary question declared",
        question == CORE_QUESTION,
        CORE_QUESTION,
        question,
        "PACKET_TRANSFER_BOUNDARY_QUESTION_UNDECLARED",
    )
    _check(
        checks,
        "packet transfer boundary intent supported",
        intent in SUPPORTED_INTENTS,
        sorted(SUPPORTED_INTENTS),
        intent,
        "PACKET_TRANSFER_BOUNDARY_INTENT_UNSUPPORTED",
    )
    _check(
        checks,
        "packet transfer boundary explicit block intent absent",
        intent != INTENT_BLOCK,
        "not explicit block intent",
        intent,
        "PACKET_TRANSFER_BOUNDARY_EXPLICIT_BLOCK_INTENT",
    )
    _check(
        checks,
        "packet transfer boundary scope supported",
        bool(scope_values) and not unsupported_scope,
        sorted(SUPPORTED_PACKET_TRANSFER_BOUNDARY_SCOPE),
        scope_values,
        "UNSUPPORTED_PACKET_TRANSFER_BOUNDARY_SCOPE",
    )

    missing_codes = {
        "selected_packet_emission_basis": "PACKET_EMISSION_BASIS_MISSING",
        "selected_packet_emission_terminal_summary_basis": (
            "PACKET_EMISSION_TERMINAL_SUMMARY_BASIS_MISSING"
        ),
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

    emission_outcome_values = _values(
        request,
        ("selected_packet_emission_result_outcome", "outcome", "result_outcome"),
        "selected_packet_emission_basis",
    )
    emission_outcome = emission_outcome_values[0] if emission_outcome_values else None
    emission_version_values = _values(
        request,
        (
            "selected_packet_emission_result_version",
            "result_version",
            "portable_source_body_verification_packet_emission_result_version",
        ),
        "selected_packet_emission_basis",
    )
    emission_version = emission_version_values[0] if emission_version_values else None
    emission_failed_check_values = [
        _as_int(value, default=None)
        for value in _values(
            request,
            ("selected_packet_emission_failed_check_count", "failed_check_count"),
            "selected_packet_emission_basis",
        )
    ]
    emission_failed_checks = (
        emission_failed_check_values[0] if emission_failed_check_values else None
    )
    bounded_emission_values = _values(
        request,
        (
            "selected_packet_emission_bounded_packet_emission_recorded",
            "bounded_packet_emission_recorded",
            "packet_emission_recorded",
        ),
        "selected_packet_emission_basis",
    )
    bounded_emission = bounded_emission_values[0] if bounded_emission_values else None
    v1_failure_preserved_values = _values(
        request,
        (
            "selected_packet_emission_v1_failure_preserved",
            "packet_emission_boundary_v1_failure_preserved",
            "v1_predecessor_failure_preserved",
        ),
        "selected_packet_emission_basis",
    )
    v1_failure_preserved = (
        v1_failure_preserved_values[0] if v1_failure_preserved_values else None
    )

    _check(
        checks,
        "packet emission outcome recorded",
        bool(emission_outcome_values)
        and all(value == PACKET_EMISSION_RECORDED for value in emission_outcome_values),
        PACKET_EMISSION_RECORDED,
        emission_outcome_values or emission_outcome,
        "PACKET_EMISSION_NOT_RECORDED",
    )
    _check(
        checks,
        "packet emission version 0.1.0",
        bool(emission_version_values)
        and all(value == PACKET_EMISSION_RESULT_VERSION for value in emission_version_values),
        PACKET_EMISSION_RESULT_VERSION,
        emission_version_values or emission_version,
        "PACKET_EMISSION_VERSION_NOT_0_1_0",
    )
    _check(
        checks,
        "packet emission failed checks zero",
        bool(emission_failed_check_values)
        and all(value == 0 for value in emission_failed_check_values),
        0,
        emission_failed_check_values or emission_failed_checks,
        "PACKET_EMISSION_FAILED_CHECKS_PRESENT",
    )
    _check(
        checks,
        "packet emission recorded bounded packet emission",
        bool(bounded_emission_values) and all(value is True for value in bounded_emission_values),
        True,
        bounded_emission_values or bounded_emission,
        "PACKET_EMISSION_DID_NOT_RECORD_BOUNDED_PACKET_EMISSION",
    )
    _check(
        checks,
        "packet emission preserved v1 packet-emission-boundary failure",
        bool(v1_failure_preserved_values)
        and all(value is True for value in v1_failure_preserved_values),
        True,
        v1_failure_preserved_values or v1_failure_preserved,
        "PACKET_EMISSION_DID_NOT_PRESERVE_V1_FAILURE",
    )

    for name, names, code in (
        (
            "packet emission did not authorize transfer",
            (
                "selected_packet_emission_authorized_transfer",
                "packet_transfer_authorized",
                "packet_transferred",
            ),
            "PACKET_EMISSION_AUTHORIZED_TRANSFER",
        ),
        (
            "packet emission did not authorize copy to another device",
            (
                "selected_packet_emission_authorized_copy_to_another_device",
                "copy_to_another_device_authorized",
                "packet_copied_to_another_device",
            ),
            "PACKET_EMISSION_AUTHORIZED_COPY_TO_ANOTHER_DEVICE",
        ),
        (
            "packet emission did not authorize source transfer",
            (
                "selected_packet_emission_authorized_source_transfer",
                "source_transfer_authorized",
                "source_transfer_occurred",
            ),
            "PACKET_EMISSION_AUTHORIZED_SOURCE_TRANSFER",
        ),
        (
            "packet emission did not create source receipt",
            (
                "selected_packet_emission_created_source_receipt",
                "source_receipt_created",
                "source_receipt_occurred",
            ),
            "PACKET_EMISSION_CREATED_SOURCE_RECEIPT",
        ),
        (
            "packet emission did not create reception authorization",
            (
                "selected_packet_emission_created_reception_authorization",
                "reception_authorization_created",
            ),
            "PACKET_EMISSION_CREATED_RECEPTION_AUTHORIZATION",
        ),
        (
            "packet emission did not create second-carrier receipt",
            (
                "selected_packet_emission_created_second_carrier_receipt",
                "second_carrier_receipt_created",
            ),
            "PACKET_EMISSION_CREATED_SECOND_CARRIER_RECEIPT",
        ),
        (
            "packet emission did not authorize second-carrier execution",
            (
                "selected_packet_emission_authorized_second_carrier_execution",
                "second_carrier_execution_authorized",
                "second_carrier_execution_created",
            ),
            "PACKET_EMISSION_AUTHORIZED_SECOND_CARRIER_EXECUTION",
        ),
        (
            "packet emission did not create external result",
            ("selected_packet_emission_created_external_result", "external_result_created"),
            "PACKET_EMISSION_CREATED_EXTERNAL_RESULT",
        ),
        (
            "packet emission did not create cross-carrier evidence",
            (
                "selected_packet_emission_created_cross_carrier_evidence",
                "cross_carrier_evidence_created",
            ),
            "PACKET_EMISSION_CREATED_CROSS_CARRIER_EVIDENCE",
        ),
        (
            "packet emission did not use hidden repo state as transfer authority",
            (
                "selected_packet_emission_used_hidden_repo_state_as_transfer_authority",
                "hidden_repo_state_used_as_transfer_content",
                "hidden_repo_state_used_as_transfer_authority",
                "hidden_repo_state_used_as_emission_content",
                "hidden_repo_state_used_as_emission_authority",
            ),
            "PACKET_EMISSION_USED_HIDDEN_REPO_STATE_AS_TRANSFER_AUTHORITY",
        ),
        (
            "packet emission did not treat repo-local availability as transfer authority",
            (
                "selected_packet_emission_treated_repo_local_availability_as_transfer_authority",
                "repo_local_availability_treated_as_transfer_authority",
                "repo_local_availability_treated_as_emission_authority",
            ),
            "PACKET_EMISSION_TREATED_REPO_LOCAL_AVAILABILITY_AS_TRANSFER_AUTHORITY",
        ),
        (
            "packet emission did not return raw full prior artifact body outside bounded emission",
            (
                "selected_packet_emission_raw_full_prior_artifact_body_returned_outside_bounded_emission",
                "raw_full_prior_artifact_body_returned",
                "full_prior_artifact_body_emitted_outside_bounded_emission",
            ),
            "PACKET_EMISSION_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY_OUTSIDE_BOUNDED_EMISSION",
        ),
    ):
        actual = _any_true(request, names, "selected_packet_emission_basis")
        _check(checks, name, actual is False, False, actual, code)

    for name, names, code in (
        (
            "packet emission recorded transfer not authorized",
            ("packet_transfer_not_authorized",),
            "PACKET_EMISSION_AUTHORIZED_TRANSFER",
        ),
        (
            "packet emission recorded copy to another device not authorized",
            ("copy_to_another_device_not_authorized",),
            "PACKET_EMISSION_AUTHORIZED_COPY_TO_ANOTHER_DEVICE",
        ),
        (
            "packet emission recorded source transfer not authorized",
            ("source_transfer_not_authorized",),
            "PACKET_EMISSION_AUTHORIZED_SOURCE_TRANSFER",
        ),
        (
            "packet emission recorded source receipt not created",
            ("source_receipt_not_created",),
            "PACKET_EMISSION_CREATED_SOURCE_RECEIPT",
        ),
        (
            "packet emission recorded reception authorization not created",
            ("reception_authorization_not_created",),
            "PACKET_EMISSION_CREATED_RECEPTION_AUTHORIZATION",
        ),
        (
            "packet emission recorded second-carrier receipt not created",
            ("second_carrier_receipt_not_created",),
            "PACKET_EMISSION_CREATED_SECOND_CARRIER_RECEIPT",
        ),
        (
            "packet emission recorded second-carrier execution not authorized",
            ("second_carrier_execution_not_authorized",),
            "PACKET_EMISSION_AUTHORIZED_SECOND_CARRIER_EXECUTION",
        ),
        (
            "packet emission recorded external result not created",
            ("external_result_not_created",),
            "PACKET_EMISSION_CREATED_EXTERNAL_RESULT",
        ),
        (
            "packet emission recorded cross-carrier evidence not created",
            ("cross_carrier_evidence_not_created",),
            "PACKET_EMISSION_CREATED_CROSS_CARRIER_EVIDENCE",
        ),
        (
            "packet emission recorded hidden repo state excluded",
            ("hidden_repo_state_excluded",),
            "PACKET_EMISSION_USED_HIDDEN_REPO_STATE_AS_TRANSFER_AUTHORITY",
        ),
        (
            "packet emission recorded hidden repo state not used as authority",
            (
                "hidden_repo_state_not_used_as_transfer_authority",
                "hidden_repo_state_not_used_as_emission_authority",
            ),
            "PACKET_EMISSION_USED_HIDDEN_REPO_STATE_AS_TRANSFER_AUTHORITY",
        ),
        (
            "packet emission recorded repo-local availability not authority",
            (
                "repo_local_availability_not_transfer_authority",
                "repo_local_availability_not_emission_authority",
            ),
            "PACKET_EMISSION_TREATED_REPO_LOCAL_AVAILABILITY_AS_TRANSFER_AUTHORITY",
        ),
        (
            "packet emission recorded raw full prior artifact body not returned",
            ("raw_full_prior_artifact_body_not_returned",),
            "PACKET_EMISSION_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY_OUTSIDE_BOUNDED_EMISSION",
        ),
    ):
        actual_values = _values(request, names, "selected_packet_emission_basis")
        _check(
            checks,
            name,
            bool(actual_values) and all(value is True for value in actual_values),
            True,
            actual_values,
            code,
        )

    execution_audit_only = _value(
        request,
        ("execution_trace_audit_only", "audit_only", "execution_audit_only"),
        "selected_command_execution_basis",
        default=True,
    )
    _check(
        checks,
        "execution trace audit-only",
        execution_audit_only is True,
        True,
        execution_audit_only,
        "EXECUTION_TRACE_NOT_AUDIT_ONLY",
    )

    lineage_only = _value(
        request,
        ("command_report_lineage_only", "lineage_only"),
        "selected_command_report_lineage_basis",
        default=True,
    )
    _check(
        checks,
        "command report lineage lineage-only",
        lineage_only is True,
        True,
        lineage_only,
        "COMMAND_REPORT_LINEAGE_NOT_LINEAGE_ONLY",
    )
    for name, field, code in (
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
            "v1_repaired",
            "v1_hidden",
            "v1_claimed_passed",
        ),
        "selected_predecessor_failure_basis",
    )
    _check(
        checks,
        "predecessor failure evidence visible",
        predecessor_visible is True,
        True,
        predecessor_visible,
        "PREDECESSOR_FAILURE_EVIDENCE_NOT_VISIBLE",
    )
    _check(
        checks,
        "predecessor failure evidence visible and unrepaired",
        predecessor_repaired is False,
        False,
        predecessor_repaired,
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    )

    posture_missing_codes = {
        "packet_transfer_boundary_only_posture": "PACKET_TRANSFER_BOUNDARY_ONLY_POSTURE_MISSING",
        "one_future_transfer_step_posture": "ONE_FUTURE_TRANSFER_STEP_POSTURE_MISSING",
        "packet_emission_basis_preserved_posture": "PACKET_EMISSION_BASIS_PRESERVED_POSTURE_MISSING",
        "emitted_packet_basis_preserved_posture": "EMITTED_PACKET_BASIS_PRESERVED_POSTURE_MISSING",
        "packet_emission_not_transfer_posture": "PACKET_EMISSION_NOT_TRANSFER_POSTURE_MISSING",
        "transfer_not_performed_posture": "TRANSFER_NOT_PERFORMED_POSTURE_MISSING",
        "copy_to_another_device_not_performed_posture": "COPY_TO_ANOTHER_DEVICE_NOT_PERFORMED_POSTURE_MISSING",
        "second_carrier_receipt_not_created_posture": "SECOND_CARRIER_RECEIPT_NOT_CREATED_POSTURE_MISSING",
        "second_carrier_execution_not_authorized_posture": "SECOND_CARRIER_EXECUTION_NOT_AUTHORIZED_POSTURE_MISSING",
        "source_transfer_not_authorized_posture": "SOURCE_TRANSFER_NOT_AUTHORIZED_POSTURE_MISSING",
        "source_receipt_not_created_posture": "SOURCE_RECEIPT_NOT_CREATED_POSTURE_MISSING",
        "reception_authorization_not_created_posture": "RECEPTION_AUTHORIZATION_NOT_CREATED_POSTURE_MISSING",
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
        "repo_local_availability_not_transfer_authority_posture": "REPO_LOCAL_AVAILABILITY_NOT_TRANSFER_AUTHORITY_POSTURE_MISSING",
        "carrier_possession_not_receipt_authority_posture": "CARRIER_POSSESSION_NOT_RECEIPT_AUTHORITY_POSTURE_MISSING",
        "selected_basis_reference_shape_posture": "SELECTED_BASIS_REFERENCE_SHAPE_POSTURE_MISSING",
        "raw_full_prior_artifact_body_not_returned_posture": "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED_POSTURE_MISSING",
    }
    for key in POSTURE_KEYS:
        _check(
            checks,
            f"{key} declared",
            _declared(request.get(key)),
            "declared posture",
            request.get(key),
            posture_missing_codes[key],
        )

    for name, names, code in (
        (
            "packet transfer boundary not treated as transfer",
            ("packet_transfer_boundary_treated_as_transfer",),
            "PACKET_TRANSFER_BOUNDARY_TREATED_AS_TRANSFER",
        ),
        (
            "packet transfer boundary not treated as copy authorization",
            ("packet_transfer_boundary_treated_as_copy_authorization",),
            "PACKET_TRANSFER_BOUNDARY_TREATED_AS_COPY_AUTHORIZATION",
        ),
        (
            "packet transfer boundary not treated as source transfer",
            ("packet_transfer_boundary_treated_as_source_transfer",),
            "PACKET_TRANSFER_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
        ),
        (
            "packet transfer boundary not treated as source receipt",
            ("packet_transfer_boundary_treated_as_source_receipt",),
            "PACKET_TRANSFER_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
        ),
        (
            "packet transfer boundary not treated as reception authorization",
            ("packet_transfer_boundary_treated_as_reception_authorization",),
            "PACKET_TRANSFER_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
        ),
        (
            "packet transfer boundary not treated as second-carrier receipt",
            ("packet_transfer_boundary_treated_as_second_carrier_receipt",),
            "PACKET_TRANSFER_BOUNDARY_TREATED_AS_SECOND_CARRIER_RECEIPT",
        ),
        (
            "packet transfer boundary not treated as second-carrier execution",
            ("packet_transfer_boundary_treated_as_second_carrier_execution",),
            "PACKET_TRANSFER_BOUNDARY_TREATED_AS_SECOND_CARRIER_EXECUTION",
        ),
        (
            "packet transfer boundary not treated as cross-carrier evidence",
            ("packet_transfer_boundary_treated_as_cross_carrier_evidence",),
            "PACKET_TRANSFER_BOUNDARY_TREATED_AS_CROSS_CARRIER_EVIDENCE",
        ),
        (
            "packet transfer boundary not treated as source",
            ("packet_transfer_boundary_treated_as_source",),
            "PACKET_TRANSFER_BOUNDARY_TREATED_AS_SOURCE",
        ),
        (
            "packet transfer boundary not treated as authority",
            ("packet_transfer_boundary_treated_as_authority",),
            "PACKET_TRANSFER_BOUNDARY_TREATED_AS_AUTHORITY",
        ),
        (
            "packet transfer boundary not treated as currentness",
            ("packet_transfer_boundary_treated_as_currentness",),
            "PACKET_TRANSFER_BOUNDARY_TREATED_AS_CURRENTNESS",
        ),
        (
            "packet transfer boundary not treated as final completion",
            ("packet_transfer_boundary_treated_as_final_completion",),
            "PACKET_TRANSFER_BOUNDARY_TREATED_AS_FINAL_COMPLETION",
        ),
        (
            "packet transfer boundary not treated as runtime",
            ("packet_transfer_boundary_treated_as_runtime",),
            "PACKET_TRANSFER_BOUNDARY_TREATED_AS_RUNTIME",
        ),
        (
            "packet transfer boundary not treated as continuation",
            ("packet_transfer_boundary_treated_as_continuation",),
            "PACKET_TRANSFER_BOUNDARY_TREATED_AS_CONTINUATION",
        ),
        (
            "packet transfer boundary not treated as reusable permission",
            ("packet_transfer_boundary_treated_as_reusable_permission",),
            "PACKET_TRANSFER_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION",
        ),
        (
            "packet transfer boundary not treated as follow-on work",
            ("packet_transfer_boundary_treated_as_follow_on_work",),
            "PACKET_TRANSFER_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
        ),
        ("packet not transferred", ("packet_transferred",), "PACKET_TRANSFERRED"),
        (
            "packet not copied to another device",
            ("packet_copied_to_another_device",),
            "PACKET_COPIED_TO_ANOTHER_DEVICE",
        ),
        ("source transfer did not occur", ("source_transfer_occurred",), "SOURCE_TRANSFER_OCCURRED"),
        ("source receipt did not occur", ("source_receipt_occurred",), "SOURCE_RECEIPT_OCCURRED"),
        (
            "reception authorization not created",
            ("reception_authorization_created",),
            "RECEPTION_AUTHORIZATION_CREATED",
        ),
        (
            "second-carrier receipt not created",
            ("second_carrier_receipt_created",),
            "SECOND_CARRIER_RECEIPT_CREATED",
        ),
        (
            "second-carrier execution not created",
            ("second_carrier_execution_created",),
            "SECOND_CARRIER_EXECUTION_CREATED",
        ),
        ("external result not created", ("external_result_created",), "EXTERNAL_RESULT_CREATED"),
        (
            "cross-carrier evidence not created",
            ("cross_carrier_evidence_created",),
            "CROSS_CARRIER_EVIDENCE_CREATED",
        ),
        ("source not created", ("source_created",), "SOURCE_CREATED"),
        ("authority not created", ("authority_created",), "AUTHORITY_CREATED"),
        ("currentness not created", ("currentness_created",), "CURRENTNESS_CREATED"),
        ("final completion not claimed", ("final_completion_claimed",), "FINAL_COMPLETION_CLAIMED"),
        ("runtime hosting not created", ("runtime_hosting_created",), "RUNTIME_HOSTING_CREATED"),
        ("deployment not created", ("deployment_created",), "DEPLOYMENT_CREATED"),
        ("public release not created", ("public_release_created",), "PUBLIC_RELEASE_CREATED"),
        (
            "operation permission not created",
            ("operation_permission_created",),
            "OPERATION_PERMISSION_CREATED",
        ),
        ("continuation not authorized", ("continuation_authorized",), "CONTINUATION_AUTHORIZED"),
        ("reusable permission not created", ("reusable_permission_created",), "REUSABLE_PERMISSION_CREATED"),
        (
            "derivative reception not authorized",
            ("derivative_reception_authorized",),
            "DERIVATIVE_RECEPTION_AUTHORIZED",
        ),
        ("vessel relation not authorized", ("vessel_relation_authorized",), "VESSEL_RELATION_AUTHORIZED"),
        (
            "another reception request not authorized",
            ("another_reception_request_authorized",),
            "ANOTHER_RECEPTION_REQUEST_AUTHORIZED",
        ),
        ("follow-on work not authorized", ("follow_on_work_authorized",), "FOLLOW_ON_WORK_AUTHORIZED"),
        (
            "artifact existence not treated as transfer authority",
            ("artifact_existence_treated_as_transfer_authority",),
            "ARTIFACT_EXISTENCE_TREATED_AS_TRANSFER_AUTHORITY",
        ),
        ("artifact path not treated as currentness", ("artifact_path_treated_as_currentness",), "ARTIFACT_PATH_TREATED_AS_CURRENTNESS"),
        (
            "repo-local availability not treated as transfer authority",
            ("repo_local_availability_treated_as_transfer_authority",),
            "REPO_LOCAL_AVAILABILITY_TREATED_AS_TRANSFER_AUTHORITY",
        ),
        (
            "carrier possession not treated as receipt authority",
            ("carrier_possession_treated_as_receipt_authority",),
            "CARRIER_POSSESSION_TREATED_AS_RECEIPT_AUTHORITY",
        ),
        (
            "hidden repo state not used as transfer content",
            ("hidden_repo_state_used_as_transfer_content",),
            "HIDDEN_REPO_STATE_USED_AS_TRANSFER_CONTENT",
        ),
        (
            "hidden repo state not used as transfer authority",
            ("hidden_repo_state_used_as_transfer_authority",),
            "HIDDEN_REPO_STATE_USED_AS_TRANSFER_AUTHORITY",
        ),
        ("consumed request not reopened", ("consumed_request_reopened",), "CONSUMED_REQUEST_REOPENED"),
        ("authorization token not reused", ("authorization_token_reused",), "AUTHORIZATION_TOKEN_REUSED"),
        (
            "full prior artifact body not emitted outside bounded transfer",
            ("full_prior_artifact_body_emitted_outside_bounded_transfer",),
            "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_TRANSFER",
        ),
        ("artifacts not mutated", ("artifacts_mutated", "prior_artifacts_mutated"), "ARTIFACTS_MUTATED"),
    ):
        actual = _any_true(request, names)
        _check(checks, name, actual is False, False, actual, code)

    _check(
        checks,
        "selected basis reference-shaped",
        _all_selected_basis_reference_shaped(request),
        True,
        "selected basis reference-shaped",
        "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    )
    _check(
        checks,
        "raw full prior artifact body not returned",
        _all_raw_full_prior_body_not_returned(request),
        True,
        "raw full prior artifact body not returned",
        "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    )
    _check(
        checks,
        "hidden repo state excluded",
        _hidden_repo_state_excluded(request),
        True,
        "hidden repo state excluded",
        "HIDDEN_REPO_STATE_USED_AS_TRANSFER_AUTHORITY",
    )

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
    requested = request.get("requested_packet_transfer_boundary_outcome")
    if requested in OUTCOME_FAMILY:
        return str(requested)
    intent = request.get("packet_transfer_boundary_intent")
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
        "block_code": failed_code or "DECLARED_PACKET_TRANSFER_BOUNDARY_REQUEST_MALFORMED",
        "block_reason": reason
        or "Packet-transfer-boundary request is blocked by bounded membrane checks.",
        "packet_transfer_boundary_recorded": False,
        "one_future_transfer_step_declared": False,
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
    request_id = "portable_source_body_verification_packet_transfer_boundary_request"
    if _is_mapping(request):
        request_id = str(request.get("packet_transfer_boundary_request_id") or request_id)
    return {
        "portable_source_body_verification_packet_transfer_boundary_result_id": (
            f"{request_id}__portable_source_body_verification_packet_transfer_boundary_result"
        ),
        "packet_transfer_boundary_request_id": request_id,
        "portable_source_body_verification_packet_transfer_boundary_result_type": RESULT_TYPE,
        "portable_source_body_verification_packet_transfer_boundary_result_version": RESULT_VERSION,
        "generated_at": _now(),
        "resolver_module": RESOLVER_MODULE,
        "packet_emission_basis_resolver_module": (
            "resolve_portable_source_body_verification_packet_emission"
        ),
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
        "packet_transfer_boundary_does_not_repair_hide_or_claim_v1_passed": True,
        "passed_check_count": sum(1 for check in checks if check.get("passed")),
        "failed_check_count": sum(1 for check in checks if not check.get("passed")),
    }


def _base_result(request: Mapping[str, Any] | None, outcome: str, checks: list[dict[str, Any]]) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    failed_code = _failed_code(checks)
    request_map = request if _is_mapping(request) else {}
    result: dict[str, Any] = {
        "portable_source_body_verification_packet_transfer_boundary_metadata": _metadata(
            request, checks
        ),
        "declared_packet_transfer_boundary_question": {
            "request_id": request_map.get("packet_transfer_boundary_request_id"),
            "question": request_map.get("packet_transfer_boundary_question"),
            "expected_question": CORE_QUESTION,
            "intent": request_map.get("packet_transfer_boundary_intent"),
            "question_declared": request_map.get("packet_transfer_boundary_question")
            == CORE_QUESTION,
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
            "packet_transfer_boundary_scope": {
                "scope_values": _scope_values(request_map),
                "supported_scope_values": sorted(SUPPORTED_PACKET_TRANSFER_BOUNDARY_SCOPE),
                "unsupported_scope_values": sorted(
                    value
                    for value in _scope_values(request_map)
                    if value not in SUPPORTED_PACKET_TRANSFER_BOUNDARY_SCOPE
                ),
            },
            "packet_transfer_boundary_checks": checks,
            "packet_transfer_boundary_statement": _statement(recorded),
            "packet_transfer_boundary_non_meaning": _non_meaning(),
            "additional_basis_required": _additional_basis_required(request_map, outcome),
            "not_recorded_basis": _not_recorded_basis(request_map, outcome, failed_code),
            "what_remains_open": _what_remains_open(),
            "non_claims": non_claims,
            "outcome": outcome,
            "block": _block(outcome, failed_code, request),
        }
    )
    result["portable_source_body_verification_packet_transfer_boundary_summary"] = (
        build_portable_source_body_verification_packet_transfer_boundary_summary(result)
    )
    return _json_safe(result)


def resolve_portable_source_body_verification_packet_transfer_boundary(
    declared_packet_transfer_boundary_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one bounded portable source-body verification packet-transfer boundary."""

    request = _copy(declared_packet_transfer_boundary_request)
    if request is not None and not _is_mapping(request):
        checks = _build_checks(None)
        return _base_result(None, OUTCOME_BLOCKED, checks)
    checks = _build_checks(request)
    outcome = _determine_outcome(request, checks)
    return _base_result(request, outcome, checks)


def resolve_portable_source_body_verification_packet_transfer_boundary_from_path(
    declared_packet_transfer_boundary_request_path: Path | str,
) -> dict:
    """Load a JSON object request from path and resolve bounded packet-transfer boundary."""

    path = Path(declared_packet_transfer_boundary_request_path)
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise PortableSourceBodyVerificationPacketTransferBoundaryError(
            "DECLARED_PACKET_TRANSFER_BOUNDARY_REQUEST_UNREADABLE: "
            f"declared packet-transfer-boundary request is unreadable: {path}"
        ) from exc
    try:
        request = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise PortableSourceBodyVerificationPacketTransferBoundaryError(
            "DECLARED_PACKET_TRANSFER_BOUNDARY_REQUEST_MALFORMED: "
            f"declared packet-transfer-boundary request is malformed JSON: {path}"
        ) from exc
    if not _is_mapping(request):
        raise PortableSourceBodyVerificationPacketTransferBoundaryError(
            "DECLARED_PACKET_TRANSFER_BOUNDARY_REQUEST_MALFORMED: "
            "declared packet-transfer-boundary request JSON must be an object"
        )
    return resolve_portable_source_body_verification_packet_transfer_boundary(request)


def build_portable_source_body_verification_packet_transfer_boundary_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a compact transfer-boundary summary without promoting it into transfer."""

    metadata = result.get("portable_source_body_verification_packet_transfer_boundary_metadata", {})
    question = result.get("declared_packet_transfer_boundary_question", {})
    checks = result.get("packet_transfer_boundary_checks", [])
    statement = result.get("packet_transfer_boundary_statement", {})
    non_claims = result.get("non_claims", {})
    emission_basis = result.get("selected_packet_emission_basis", {})
    block = result.get("block")
    summary: dict[str, Any] = {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") if _is_mapping(block) else None,
        "block_reason": block.get("block_reason") if _is_mapping(block) else None,
        "request_id": metadata.get("packet_transfer_boundary_request_id")
        if _is_mapping(metadata)
        else None,
        "question": question.get("question") if _is_mapping(question) else None,
        "intent": question.get("intent") if _is_mapping(question) else None,
        "passed_check_count": sum(
            1 for check in checks if _is_mapping(check) and check.get("passed")
        ),
        "failed_check_count": sum(
            1 for check in checks if _is_mapping(check) and not check.get("passed")
        ),
        "selected_packet_emission_outcome": emission_basis.get("outcome")
        if _is_mapping(emission_basis)
        else None,
        "selected_packet_emission_version": emission_basis.get("result_version")
        if _is_mapping(emission_basis)
        else None,
        "selected_packet_emission_failed_check_count": emission_basis.get("failed_check_count")
        if _is_mapping(emission_basis)
        else None,
        "v1_predecessor_failure_preserved": (
            statement.get("packet_emission_basis_preserved") is True
            and _is_mapping(non_claims)
            and non_claims.get("v1_repaired") is False
            and non_claims.get("v1_hidden") is False
            and non_claims.get("v1_claimed_passed") is False
        ),
        "v1_repaired": non_claims.get("v1_repaired") is True if _is_mapping(non_claims) else False,
        "v1_hidden": non_claims.get("v1_hidden") is True if _is_mapping(non_claims) else False,
        "v1_claimed_passed": (
            non_claims.get("v1_claimed_passed") is True if _is_mapping(non_claims) else False
        ),
        "no_transfer_copy_receipt_execution_cross_carrier_evidence": (
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
                "hidden_repo_state_used_as_transfer_content",
                "hidden_repo_state_used_as_transfer_authority",
                "repo_local_availability_treated_as_transfer_authority",
                "carrier_possession_treated_as_receipt_authority",
                "artifact_existence_treated_as_transfer_authority",
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
    metadata = result.get("portable_source_body_verification_packet_transfer_boundary_metadata")
    if _is_mapping(metadata) and metadata.get("packet_transfer_boundary_request_id"):
        return str(metadata["packet_transfer_boundary_request_id"])
    question = result.get("declared_packet_transfer_boundary_question")
    if _is_mapping(question) and question.get("request_id"):
        return str(question["request_id"])
    return "portable_source_body_verification_packet_transfer_boundary_request"


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


def write_portable_source_body_verification_packet_transfer_boundary_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a bounded packet-transfer-boundary JSON result without overwriting files."""

    safe_result = _json_safe(_copy(result))
    request_id = _request_id_from_result(safe_result)
    if output_path is None:
        destination = OUTPUT_ROOT / (
            f"{request_id}__portable_source_body_verification_packet_transfer_boundary_result.json"
        )
    else:
        destination = Path(output_path)
        if destination.exists() and destination.is_dir():
            destination = destination / (
                f"{request_id}__portable_source_body_verification_packet_transfer_boundary_result.json"
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
        "raw_full_prior_artifact_body_not_returned": True,
        "hidden_repo_state_excluded": True,
        "hidden_repo_state_used_as_transfer_content": False,
        "hidden_repo_state_used_as_transfer_authority": False,
        "hidden_repo_state_not_used_as_transfer_authority": True,
        "repo_local_availability_not_transfer_authority": True,
        "repo_local_availability_treated_as_transfer_authority": False,
        "carrier_possession_not_receipt_authority": True,
        "carrier_possession_treated_as_receipt_authority": False,
        "artifact_existence_treated_as_transfer_authority": False,
        "artifact_path_treated_as_currentness": False,
    }
    if outcome is not None:
        basis["outcome"] = outcome
    return basis


def _posture_stub(name: str) -> dict[str, Any]:
    return {
        "posture_name": name,
        "declared": True,
        "packet_transfer_boundary_posture_only": True,
        "one_future_transfer_step_declared": True,
        "packet_emission_basis_preserved": True,
        "emitted_packet_basis_preserved": True,
        "packet_emission_not_transfer": True,
        "transfer_not_performed": True,
        "copy_to_another_device_not_performed": True,
        "second_carrier_receipt_not_created": True,
        "second_carrier_execution_not_authorized": True,
        "source_transfer_not_authorized": True,
        "source_receipt_not_created": True,
        "reception_authorization_not_created": True,
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
        "hidden_repo_state_not_used_as_transfer_authority": True,
        "repo_local_availability_not_transfer_authority": True,
        "carrier_possession_not_receipt_authority": True,
        "selected_basis_reference_shape_preserved": True,
        "raw_full_prior_artifact_body_not_returned": True,
        "authorization_token_reuse_blocked": True,
        "consumed_request_token_remains_closed": True,
    }


def build_declared_portable_source_body_verification_packet_transfer_boundary_request(
    packet_transfer_boundary_request_id: str = (
        "portable_source_body_verification_packet_transfer_boundary_reference_review_001"
    ),
    *,
    selected_packet_emission_result_path: Path | str | None = None,
    selected_packet_emission_result_id: str | None = (
        "portable_source_body_verification_packet_emission_reference_review_001"
    ),
    packet_transfer_boundary_intent: str = INTENT_RECORD,
) -> dict[str, Any]:
    """Build a valid declared packet-transfer-boundary request."""

    request: dict[str, Any] = {
        "packet_transfer_boundary_request_id": packet_transfer_boundary_request_id,
        "packet_transfer_boundary_question": CORE_QUESTION,
        "packet_transfer_boundary_intent": packet_transfer_boundary_intent,
        "packet_transfer_boundary_scope": sorted(SUPPORTED_PACKET_TRANSFER_BOUNDARY_SCOPE),
        "declared_non_claims": {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
        "selected_packet_emission_result_path": (
            str(selected_packet_emission_result_path)
            if selected_packet_emission_result_path is not None
            else None
        ),
        "selected_packet_emission_result_id": selected_packet_emission_result_id,
        "selected_packet_emission_result_outcome": PACKET_EMISSION_RECORDED,
        "selected_packet_emission_result_version": PACKET_EMISSION_RESULT_VERSION,
        "selected_packet_emission_failed_check_count": 0,
        "selected_packet_emission_bounded_packet_emission_recorded": True,
        "selected_packet_emission_v1_failure_preserved": True,
        "selected_packet_emission_authorized_transfer": False,
        "selected_packet_emission_authorized_copy_to_another_device": False,
        "selected_packet_emission_authorized_source_transfer": False,
        "selected_packet_emission_created_source_receipt": False,
        "selected_packet_emission_created_reception_authorization": False,
        "selected_packet_emission_created_second_carrier_receipt": False,
        "selected_packet_emission_authorized_second_carrier_execution": False,
        "selected_packet_emission_created_external_result": False,
        "selected_packet_emission_created_cross_carrier_evidence": False,
        "selected_packet_emission_used_hidden_repo_state_as_transfer_authority": False,
        "selected_packet_emission_treated_repo_local_availability_as_transfer_authority": False,
        "selected_packet_emission_raw_full_prior_artifact_body_returned_outside_bounded_emission": False,
        "reference_shaped_input_posture": True,
    }
    request["declared_non_claims"].update({key: False for key in EXTRA_FALSE_NON_CLAIMS})

    packet_emission_basis = _basis_stub("selected_packet_emission_basis", PACKET_EMISSION_RECORDED)
    packet_emission_basis.update(
        {
            "result_id": selected_packet_emission_result_id,
            "result_path": (
                str(selected_packet_emission_result_path)
                if selected_packet_emission_result_path is not None
                else None
            ),
            "result_version": PACKET_EMISSION_RESULT_VERSION,
            "failed_check_count": 0,
            "resolver_module": "resolve_portable_source_body_verification_packet_emission",
            "packet_emission_recorded": True,
            "bounded_packet_emission_recorded": True,
            "packet_emission_boundary_v2_basis_preserved": True,
            "packet_emission_boundary_v1_failure_preserved": True,
            "packet_artifact_basis_preserved": True,
            "emitted_packet_recorded_or_bounded": True,
            "packet_transfer_not_authorized": True,
            "packet_transfer_authorized": False,
            "packet_transferred": False,
            "copy_to_another_device_not_authorized": True,
            "copy_to_another_device_authorized": False,
            "packet_copied_to_another_device": False,
            "source_transfer_not_authorized": True,
            "source_transfer_authorized": False,
            "source_transfer_occurred": False,
            "source_receipt_not_created": True,
            "source_receipt_created": False,
            "source_receipt_occurred": False,
            "reception_authorization_not_created": True,
            "reception_authorization_created": False,
            "second_carrier_receipt_not_created": True,
            "second_carrier_receipt_created": False,
            "second_carrier_execution_not_authorized": True,
            "second_carrier_execution_authorized": False,
            "second_carrier_execution_created": False,
            "external_result_not_created": True,
            "external_result_created": False,
            "cross_carrier_evidence_not_created": True,
            "cross_carrier_evidence_created": False,
            "source_not_created": True,
            "authority_not_created": True,
            "currentness_not_created": True,
            "final_completion_not_created": True,
            "runtime_not_created": True,
            "continuation_not_authorized": True,
            "reusable_permission_not_created": True,
            "follow_on_work_not_authorized": True,
            "hidden_repo_state_excluded": True,
            "hidden_repo_state_not_used_as_transfer_authority": True,
            "hidden_repo_state_not_used_as_emission_authority": True,
            "hidden_repo_state_used_as_transfer_content": False,
            "hidden_repo_state_used_as_transfer_authority": False,
            "hidden_repo_state_used_as_emission_content": False,
            "hidden_repo_state_used_as_emission_authority": False,
            "repo_local_availability_not_transfer_authority": True,
            "repo_local_availability_not_emission_authority": True,
            "repo_local_availability_treated_as_transfer_authority": False,
            "repo_local_availability_treated_as_emission_authority": False,
            "raw_full_prior_artifact_body_not_returned": True,
            "raw_full_prior_artifact_body_returned": False,
            "authorization_token_reuse_blocked": True,
            "authorization_token_reused": False,
            "consumed_request_token_remains_closed": True,
            "consumed_request_reopened": False,
        }
    )
    request["selected_packet_emission_basis"] = packet_emission_basis
    request["selected_packet_emission_terminal_summary_basis"] = _basis_stub(
        "selected_packet_emission_terminal_summary_basis"
    )

    boundary_v2_basis = _basis_stub(
        "selected_packet_emission_boundary_v2_basis",
        PACKET_EMISSION_BOUNDARY_V2_RECORDED,
    )
    boundary_v2_basis.update(
        {
            "result_version": PACKET_EMISSION_BOUNDARY_V2_RESULT_VERSION,
            "failed_check_count": 0,
            "v1_predecessor_failure_preserved": True,
            "v1_repaired": False,
            "v1_hidden": False,
            "v1_claimed_passed": False,
            "one_future_packet_emission_step_declared": True,
            "packet_not_emitted": True,
            "packet_transfer_not_authorized": True,
            "copy_to_another_device_not_authorized": True,
            "source_transfer_not_authorized": True,
            "source_receipt_not_created": True,
            "reception_authorization_not_created": True,
            "second_carrier_receipt_not_created": True,
            "second_carrier_execution_not_authorized": True,
            "external_result_not_created": True,
            "cross_carrier_evidence_not_created": True,
        }
    )
    request["selected_packet_emission_boundary_v2_basis"] = boundary_v2_basis

    v1_failure_basis = _basis_stub(
        "selected_packet_emission_boundary_v1_predecessor_failure_basis"
    )
    v1_failure_basis.update(
        {
            "predecessor_failure_evidence_visible": True,
            "v1_predecessor_failure_preserved": True,
            "v1_failed_packet_emission_boundary_test": True,
            "observed_failure_count": 85,
            "v1_repaired": False,
            "v1_hidden": False,
            "v1_claimed_passed": False,
        }
    )
    request["selected_packet_emission_boundary_v1_predecessor_failure_basis"] = v1_failure_basis

    request["selected_packet_artifact_basis"] = _basis_stub(
        "selected_packet_artifact_basis", PACKET_ARTIFACT_RECORDED
    )
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
            "v1_repaired": False,
            "v1_hidden": False,
            "v1_claimed_passed": False,
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
