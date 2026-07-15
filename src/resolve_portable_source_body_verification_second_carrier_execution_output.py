"""Resolve one bounded second-carrier execution output posture.

This resolver is downstream of the second-carrier execution output boundary. It
records one bounded execution-output / second-carrier-output posture only; it
does not create output capture, result, success, external result,
cross-carrier evidence, source transfer, source receipt, reception
authorization, authority, currentness, runtime, final completion, continuation,
reusable permission, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class PortableSourceBodyVerificationSecondCarrierExecutionOutputError(Exception):
    """Raised for unreadable paths, malformed JSON files, or write failures."""


RESOLVER_MODULE = (
    "resolve_portable_source_body_verification_second_carrier_execution_output"
)
RESULT_TYPE = "portable_source_body_verification_second_carrier_execution_output_result"
RESULT_VERSION = "0.1.0"
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_portable_source_body_verification_"
    "second_carrier_execution_output"
)

QUESTION = (
    "Can the second-carrier-execution-output-boundary basis be used to record "
    "one bounded execution output / second-carrier output without creating "
    "second-carrier output capture, second-carrier result, second-carrier "
    "success, external result, cross-carrier evidence, source transfer, source "
    "receipt, reception authorization, source, authority, currentness, runtime, "
    "final completion, continuation, reusable permission, derivative reception, "
    "vessel relation, another reception request, or follow-on work?"
)

INTENT_RECORD = (
    "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_OUTPUT"
)
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_OUTPUT"
)
INTENT_BLOCK = (
    "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_OUTPUT"
)
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

OUTCOME_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_OUTPUT_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_OUTPUT_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_OUTPUT_"
    "REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_OUTPUT_BLOCKED"
)

OUTPUT_BOUNDARY_OUTCOME_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_"
    "RECORDED"
)
SECOND_CARRIER_EXECUTION_OUTCOME_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_RECORDED"
)

SUPPORTED_SECOND_CARRIER_EXECUTION_OUTPUT_SCOPE = (
    "SECOND_CARRIER_EXECUTION_OUTPUT_SPEC_ONLY",
    "ONE_BOUNDED_SECOND_CARRIER_EXECUTION_OUTPUT_RECORDED",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_BASIS_PRESERVED",
    "SECOND_CARRIER_EXECUTION_BASIS_PRESERVED",
    "EXECUTION_ARTIFACT_BASIS_PRESERVED",
    "OUTPUT_RECORDED_BOUNDED",
    "OUTPUT_ARTIFACT_RECORDED_OR_BOUNDED",
    "OUTPUT_NOT_CAPTURE",
    "OUTPUT_NOT_RESULT",
    "OUTPUT_NOT_SUCCESS",
    "OUTPUT_NOT_EXTERNAL_RESULT",
    "OUTPUT_NOT_CROSS_CARRIER_EVIDENCE",
    "OUTPUT_NOT_SOURCE_TRANSFER",
    "OUTPUT_NOT_SOURCE_RECEIPT",
    "OUTPUT_NOT_RECEPTION_AUTHORIZATION",
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
    "selected_second_carrier_execution_output_boundary_basis",
    "selected_second_carrier_execution_output_boundary_terminal_summary_basis",
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
    "second_carrier_execution_output_spec_only_posture",
    "one_bounded_second_carrier_execution_output_posture",
    "second_carrier_execution_output_boundary_basis_preserved_posture",
    "second_carrier_execution_basis_preserved_posture",
    "execution_artifact_basis_preserved_posture",
    "output_recorded_bounded_posture",
    "output_artifact_recorded_or_bounded_posture",
    "output_not_capture_posture",
    "output_not_result_posture",
    "output_not_success_posture",
    "output_not_external_result_posture",
    "output_not_cross_carrier_evidence_posture",
    "output_not_source_transfer_posture",
    "output_not_source_receipt_posture",
    "output_not_reception_authorization_posture",
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
    "repo_local_availability_not_output_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
)

REQUIRED_FALSE_NON_CLAIMS = (
    "second_carrier_output_capture_created",
    "second_carrier_result_created",
    "second_carrier_success_created",
    "external_result_created",
    "cross_carrier_evidence_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "second_carrier_execution_output_treated_as_capture",
    "second_carrier_execution_output_treated_as_result",
    "second_carrier_execution_output_treated_as_success",
    "second_carrier_execution_output_treated_as_external_result",
    "second_carrier_execution_output_treated_as_cross_carrier_evidence",
    "second_carrier_execution_output_treated_as_source_transfer",
    "second_carrier_execution_output_treated_as_source_receipt",
    "second_carrier_execution_output_treated_as_reception_authorization",
    "second_carrier_execution_output_treated_as_source",
    "second_carrier_execution_output_treated_as_authority",
    "second_carrier_execution_output_treated_as_currentness",
    "second_carrier_execution_output_treated_as_final_completion",
    "second_carrier_execution_output_treated_as_runtime",
    "second_carrier_execution_output_treated_as_continuation",
    "second_carrier_execution_output_treated_as_reusable_permission",
    "second_carrier_execution_output_treated_as_follow_on_work",
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

ALLOWED_TRUE_RECORDED_FIELDS = (
    "second_carrier_execution_output_recorded",
    "bounded_second_carrier_execution_output_recorded",
    "output_artifact_recorded_or_bounded",
    "second_carrier_execution_output_boundary_basis_preserved",
    "second_carrier_execution_basis_preserved",
    "execution_artifact_basis_preserved",
    "output_recorded_bounded",
    "output_not_capture",
    "output_not_result",
    "output_not_success",
    "output_not_external_result",
    "output_not_cross_carrier_evidence",
    "output_not_source_transfer",
    "output_not_source_receipt",
    "output_not_reception_authorization",
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
    "hidden_repo_state_not_used_as_output_authority",
    "repo_local_availability_not_output_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
)

BLOCK_CODES = (
    "DECLARED_SECOND_CARRIER_EXECUTION_OUTPUT_REQUEST_MALFORMED",
    "DECLARED_SECOND_CARRIER_EXECUTION_OUTPUT_REQUEST_UNREADABLE",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BLOCK_REQUESTED",
    "SECOND_CARRIER_EXECUTION_OUTPUT_QUESTION_UNDECLARED",
    "SECOND_CARRIER_EXECUTION_OUTPUT_INTENT_UNSUPPORTED",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_BASIS_MISSING",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TERMINAL_SUMMARY_BASIS_MISSING",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_NOT_RECORDED",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_VERSION_NOT_0_1_0",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_DID_NOT_DECLARE_FUTURE_OUTPUT_STEP",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_ALREADY_CREATED_OUTPUT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_ALREADY_CREATED_OUTPUT_ARTIFACT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_ALREADY_CREATED_OUTPUT_CAPTURE",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_ALREADY_CREATED_SECOND_CARRIER_RESULT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_ALREADY_CREATED_SECOND_CARRIER_SUCCESS",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_CREATED_EXTERNAL_RESULT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_CREATED_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_USED_HIDDEN_REPO_STATE_AS_OUTPUT_AUTHORITY",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_REPO_LOCAL_AVAILABILITY_AS_OUTPUT_AUTHORITY",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_RECEIVING_CARRIER_AS_AUTHORITY",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY",
    "SECOND_CARRIER_EXECUTION_BASIS_MISSING",
    "SECOND_CARRIER_EXECUTION_TERMINAL_SUMMARY_BASIS_MISSING",
    "SECOND_CARRIER_EXECUTION_NOT_RECORDED",
    "SECOND_CARRIER_EXECUTION_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_EXECUTION_DID_NOT_RECORD_BOUNDED_EXECUTION",
    "SECOND_CARRIER_EXECUTION_TREATED_EXECUTION_AS_OUTPUT",
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
    "SECOND_CARRIER_EXECUTION_OUTPUT_SPEC_ONLY_POSTURE_MISSING",
    "ONE_BOUNDED_SECOND_CARRIER_EXECUTION_OUTPUT_POSTURE_MISSING",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_BASIS_PRESERVED_POSTURE_MISSING",
    "SECOND_CARRIER_EXECUTION_BASIS_PRESERVED_POSTURE_MISSING",
    "EXECUTION_ARTIFACT_BASIS_PRESERVED_POSTURE_MISSING",
    "OUTPUT_RECORDED_BOUNDED_POSTURE_MISSING",
    "OUTPUT_ARTIFACT_RECORDED_OR_BOUNDED_POSTURE_MISSING",
    "OUTPUT_NOT_CAPTURE_POSTURE_MISSING",
    "OUTPUT_NOT_RESULT_POSTURE_MISSING",
    "OUTPUT_NOT_SUCCESS_POSTURE_MISSING",
    "OUTPUT_NOT_EXTERNAL_RESULT_POSTURE_MISSING",
    "OUTPUT_NOT_CROSS_CARRIER_EVIDENCE_POSTURE_MISSING",
    "OUTPUT_NOT_SOURCE_TRANSFER_POSTURE_MISSING",
    "OUTPUT_NOT_SOURCE_RECEIPT_POSTURE_MISSING",
    "OUTPUT_NOT_RECEPTION_AUTHORIZATION_POSTURE_MISSING",
    "SECOND_CARRIER_OUTPUT_CAPTURE_NOT_CREATED_POSTURE_MISSING",
    "SECOND_CARRIER_RESULT_NOT_CREATED_POSTURE_MISSING",
    "SECOND_CARRIER_SUCCESS_NOT_CREATED_POSTURE_MISSING",
    "EXTERNAL_RESULT_NOT_CREATED_POSTURE_MISSING",
    "CROSS_CARRIER_EVIDENCE_NOT_CREATED_POSTURE_MISSING",
    "RECEIVING_CARRIER_NOT_AUTHORITY_POSTURE_MISSING",
    "SOURCE_NOT_CREATED_POSTURE_MISSING",
    "AUTHORITY_NOT_CREATED_POSTURE_MISSING",
    "CURRENTNESS_NOT_CREATED_POSTURE_MISSING",
    "FINAL_COMPLETION_NOT_CREATED_POSTURE_MISSING",
    "RUNTIME_NOT_CREATED_POSTURE_MISSING",
    "CONTINUATION_NOT_AUTHORIZED_POSTURE_MISSING",
    "REUSABLE_PERMISSION_NOT_CREATED_POSTURE_MISSING",
    "FOLLOW_ON_WORK_NOT_AUTHORIZED_POSTURE_MISSING",
    "HIDDEN_REPO_STATE_EXCLUDED_POSTURE_MISSING",
    "REPO_LOCAL_AVAILABILITY_NOT_OUTPUT_AUTHORITY_POSTURE_MISSING",
    "SELECTED_BASIS_REFERENCE_SHAPE_POSTURE_MISSING",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED_POSTURE_MISSING",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_CAPTURE",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_RESULT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_SUCCESS",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_SOURCE_TRANSFER",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_SOURCE_RECEIPT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_RECEPTION_AUTHORIZATION",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_SOURCE",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_AUTHORITY",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_CURRENTNESS",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_FINAL_COMPLETION",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_RUNTIME",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_CONTINUATION",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_REUSABLE_PERMISSION",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_FOLLOW_ON_WORK",
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
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_OUTPUT",
    "ARTIFACTS_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_SECOND_CARRIER_EXECUTION_OUTPUT_SCOPE",
)

_BASIS_MISSING_CODES = {
    "selected_second_carrier_execution_output_boundary_basis": (
        "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_BASIS_MISSING"
    ),
    "selected_second_carrier_execution_output_boundary_terminal_summary_basis": (
        "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TERMINAL_SUMMARY_BASIS_MISSING"
    ),
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
    "selected_packet_transfer_boundary_basis": (
        "PACKET_TRANSFER_BOUNDARY_BASIS_MISSING"
    ),
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

_POSTURE_MISSING_CODES = {
    key: key.removesuffix("_posture").upper() + "_POSTURE_MISSING"
    for key in POSTURE_KEYS
}

_SENSITIVE_KEYS = frozenset(
    {
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
        "second_carrier_output_body",
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
        "output_artifact_presence",
        "output_path_existence",
        "output_path_possibility",
        "unlisted_file_dependency",
    }
)
_REDACTION = "[bounded-reference-redacted-raw-or-hidden-state]"


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _is_declared(value: Any) -> bool:
    if value is None:
        return False
    if value is False:
        return False
    if isinstance(value, str) and not value.strip():
        return False
    if isinstance(value, (list, tuple, dict, set)) and len(value) == 0:
        return False
    return True


def _sanitize(value: Any) -> Any:
    if isinstance(value, Mapping):
        sanitized: dict[str, Any] = {}
        for key, item in value.items():
            key_text = str(key)
            if key_text in _SENSITIVE_KEYS:
                sanitized[key_text] = _REDACTION
            else:
                sanitized[key_text] = _sanitize(item)
        return sanitized
    if isinstance(value, list):
        return [_sanitize(item) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item) for item in value]
    if isinstance(value, Path):
        return str(value)
    return copy.deepcopy(value)


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
    section.setdefault("basis_declared", _is_declared(supplied))
    section.setdefault("basis_role", "selected_reference_basis_only")
    section.setdefault("does_not_create_capture_result_success_or_authority", True)
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
    section.setdefault("preserves_output_membrane", True)
    return section


def _nested_get(mapping: Mapping[str, Any], path: tuple[str, ...]) -> Any:
    current: Any = mapping
    for key in path:
        if not isinstance(current, Mapping) or key not in current:
            return None
        current = current[key]
    return current


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
        if lowered in {"true", "yes", "1"}:
            return True
        if lowered in {"false", "no", "0"}:
            return False
    if value is None:
        return default
    return bool(value)


def _as_int(value: Any, default: int | None = None) -> int | None:
    if isinstance(value, bool):
        return default
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            return default
    return default


def _output_boundary_value(request: Mapping[str, Any], field: str) -> Any:
    basis = request.get("selected_second_carrier_execution_output_boundary_basis")
    return _first_declared(
        request.get(f"selected_second_carrier_execution_output_boundary_{field}"),
        request.get(f"selected_second_carrier_execution_output_boundary_result_{field}"),
        _nested_get(basis, (field,)) if isinstance(basis, Mapping) else None,
        _nested_get(basis, ("metadata", field)) if isinstance(basis, Mapping) else None,
        _nested_get(basis, ("statement", field)) if isinstance(basis, Mapping) else None,
        _nested_get(basis, ("non_claims", field)) if isinstance(basis, Mapping) else None,
        _nested_get(basis, ("summary", field)) if isinstance(basis, Mapping) else None,
    )


def _execution_value(request: Mapping[str, Any], field: str) -> Any:
    basis = request.get("selected_second_carrier_execution_basis")
    return _first_declared(
        request.get(f"selected_second_carrier_execution_{field}"),
        request.get(f"selected_second_carrier_execution_result_{field}"),
        _nested_get(basis, (field,)) if isinstance(basis, Mapping) else None,
        _nested_get(basis, ("metadata", field)) if isinstance(basis, Mapping) else None,
        _nested_get(basis, ("statement", field)) if isinstance(basis, Mapping) else None,
        _nested_get(basis, ("summary", field)) if isinstance(basis, Mapping) else None,
        _nested_get(basis, ("non_claims", field)) if isinstance(basis, Mapping) else None,
    )


def _output_boundary_bool(
    request: Mapping[str, Any],
    field: str,
    default: bool = False,
) -> bool:
    return _as_bool(_output_boundary_value(request, field), default=default)


def _execution_bool(
    request: Mapping[str, Any],
    field: str,
    default: bool = False,
) -> bool:
    return _as_bool(_execution_value(request, field), default=default)


def _check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: str,
    actual_posture: Any,
    code: str | None = None,
) -> None:
    record: dict[str, Any] = {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": expected_posture,
        "actual_posture": _sanitize(actual_posture),
    }
    if not passed and code:
        record["block_code"] = code
        record["failure_code"] = code
    checks.append(record)


def _block(code: str, reason: str) -> dict[str, Any]:
    return {
        "blocked": True,
        "block_code": code,
        "reason": reason,
        "does_not_create_output_capture_result_success_or_authority": True,
    }


def _empty_block() -> dict[str, Any]:
    return {
        "blocked": False,
        "block_code": None,
        "reason": None,
        "does_not_create_output_capture_result_success_or_authority": True,
    }


def _statement(recorded: bool) -> dict[str, bool]:
    statement = {key: False for key in ALLOWED_TRUE_RECORDED_FIELDS}
    if recorded:
        statement.update({key: True for key in ALLOWED_TRUE_RECORDED_FIELDS})
    return statement


def _non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _non_meaning() -> dict[str, bool]:
    return {
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
        "output_became_capture": False,
        "output_became_result": False,
        "output_became_success": False,
        "output_became_external_result": False,
        "output_became_cross_carrier_proof": False,
        "output_became_source_transfer_source_receipt_or_reception_authorization": False,
        "output_became_source_authority_or_currentness": False,
        "output_artifact_became_capture_result_success_external_result_or_cross_carrier_evidence": False,
        "receiving_carrier_became_authority": False,
        "transferred_packet_became_source_authority_or_currentness": False,
        "artifact_existence_became_output_authority": False,
        "artifact_path_became_currentness": False,
        "repo_local_availability_became_output_authority": False,
        "hidden_repo_state_became_output_authority": False,
        "v1_packet_emission_boundary_resolver_repaired_hidden_erased_or_claimed_passed": False,
    }


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "second-carrier execution output test",
            "second-carrier execution output live artifact",
            "second-carrier execution output terminal summary, if needed",
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


def _scope_from_request(request: Mapping[str, Any]) -> list[str]:
    supplied = request.get("second_carrier_execution_output_scope")
    if supplied is None:
        return list(SUPPORTED_SECOND_CARRIER_EXECUTION_OUTPUT_SCOPE)
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


def _build_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    question = request.get("second_carrier_execution_output_question")
    intent = request.get("second_carrier_execution_output_intent")
    scopes = _scope_from_request(request)
    unsupported_scopes = [
        scope
        for scope in scopes
        if scope not in SUPPORTED_SECOND_CARRIER_EXECUTION_OUTPUT_SCOPE
    ]

    _check(
        checks,
        "second_carrier_execution_output_question_declared",
        question == QUESTION,
        QUESTION,
        question,
        "SECOND_CARRIER_EXECUTION_OUTPUT_QUESTION_UNDECLARED",
    )
    _check(
        checks,
        "second_carrier_execution_output_intent_supported",
        intent in SUPPORTED_INTENTS and intent != INTENT_BLOCK,
        f"one of {SUPPORTED_INTENTS[:-1]}",
        intent,
        "SECOND_CARRIER_EXECUTION_OUTPUT_INTENT_UNSUPPORTED"
        if intent != INTENT_BLOCK
        else "SECOND_CARRIER_EXECUTION_OUTPUT_BLOCK_REQUESTED",
    )
    _check(
        checks,
        "second_carrier_execution_output_scope_supported",
        not unsupported_scopes,
        list(SUPPORTED_SECOND_CARRIER_EXECUTION_OUTPUT_SCOPE),
        scopes,
        "UNSUPPORTED_SECOND_CARRIER_EXECUTION_OUTPUT_SCOPE",
    )

    for key in SELECTED_BASIS_KEYS:
        _check(
            checks,
            f"{key}_declared",
            _is_declared(request.get(key)),
            "basis declared as reference-shaped selected basis",
            request.get(key),
            _BASIS_MISSING_CODES[key],
        )

    output_boundary_outcome = _output_boundary_value(request, "outcome")
    output_boundary_version = _first_declared(
        _output_boundary_value(request, "version"),
        _output_boundary_value(request, "result_version"),
        _output_boundary_value(
            request,
            "portable_source_body_verification_second_carrier_execution_output_boundary_result_version",
        ),
    )
    output_boundary_failed_count = _as_int(
        _first_declared(
            _output_boundary_value(request, "failed_check_count"),
            _output_boundary_value(request, "failed_checks"),
        ),
        default=None,
    )

    _check(
        checks,
        "second_carrier_execution_output_boundary_outcome_recorded",
        output_boundary_outcome == OUTPUT_BOUNDARY_OUTCOME_RECORDED,
        OUTPUT_BOUNDARY_OUTCOME_RECORDED,
        output_boundary_outcome,
        "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_NOT_RECORDED",
    )
    _check(
        checks,
        "second_carrier_execution_output_boundary_version_0_1_0",
        output_boundary_version == RESULT_VERSION,
        RESULT_VERSION,
        output_boundary_version,
        "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_VERSION_NOT_0_1_0",
    )
    _check(
        checks,
        "second_carrier_execution_output_boundary_failed_checks_zero",
        output_boundary_failed_count == 0,
        0,
        output_boundary_failed_count,
        "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_FAILED_CHECKS_PRESENT",
    )
    _check(
        checks,
        "second_carrier_execution_output_boundary_declared_future_output_step",
        _output_boundary_bool(
            request,
            "declared_future_output_step",
            default=False,
        )
        or _output_boundary_bool(
            request,
            "one_future_second_carrier_execution_output_step_declared",
            default=False,
        ),
        "one future execution-output / second-carrier-output step declared",
        _output_boundary_value(request, "declared_future_output_step"),
        "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_DID_NOT_DECLARE_FUTURE_OUTPUT_STEP",
    )

    boundary_negative_checks = (
        (
            "second_carrier_execution_output_boundary_did_not_already_create_output",
            "already_created_output",
            "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_ALREADY_CREATED_OUTPUT",
        ),
        (
            "second_carrier_execution_output_boundary_did_not_already_create_output_artifact",
            "already_created_output_artifact",
            "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_ALREADY_CREATED_OUTPUT_ARTIFACT",
        ),
        (
            "second_carrier_execution_output_boundary_did_not_already_create_output_capture",
            "already_created_output_capture",
            "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_ALREADY_CREATED_OUTPUT_CAPTURE",
        ),
        (
            "second_carrier_execution_output_boundary_did_not_already_create_second_carrier_result",
            "already_created_second_carrier_result",
            "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_ALREADY_CREATED_SECOND_CARRIER_RESULT",
        ),
        (
            "second_carrier_execution_output_boundary_did_not_already_create_second_carrier_success",
            "already_created_second_carrier_success",
            "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_ALREADY_CREATED_SECOND_CARRIER_SUCCESS",
        ),
        (
            "second_carrier_execution_output_boundary_did_not_create_external_result",
            "created_external_result",
            "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_CREATED_EXTERNAL_RESULT",
        ),
        (
            "second_carrier_execution_output_boundary_did_not_create_cross_carrier_evidence",
            "created_cross_carrier_evidence",
            "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_CREATED_CROSS_CARRIER_EVIDENCE",
        ),
        (
            "second_carrier_execution_output_boundary_did_not_use_hidden_repo_state_as_output_authority",
            "used_hidden_repo_state_as_output_authority",
            "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_USED_HIDDEN_REPO_STATE_AS_OUTPUT_AUTHORITY",
        ),
        (
            "second_carrier_execution_output_boundary_did_not_treat_repo_local_availability_as_output_authority",
            "treated_repo_local_availability_as_output_authority",
            "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_REPO_LOCAL_AVAILABILITY_AS_OUTPUT_AUTHORITY",
        ),
        (
            "second_carrier_execution_output_boundary_did_not_treat_receiving_carrier_as_authority",
            "treated_receiving_carrier_as_authority",
            "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_RECEIVING_CARRIER_AS_AUTHORITY",
        ),
        (
            "second_carrier_execution_output_boundary_did_not_return_raw_full_prior_artifact_body",
            "raw_full_prior_artifact_body_returned",
            "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY",
        ),
    )
    for check_name, field, code in boundary_negative_checks:
        value = _output_boundary_value(request, field)
        _check(
            checks,
            check_name,
            not _as_bool(value, default=False),
            False,
            value,
            code,
        )

    execution_outcome = _execution_value(request, "outcome")
    execution_failed_count = _as_int(
        _first_declared(
            _execution_value(request, "failed_check_count"),
            _execution_value(request, "failed_checks"),
        ),
        default=None,
    )
    _check(
        checks,
        "second_carrier_execution_outcome_recorded",
        execution_outcome == SECOND_CARRIER_EXECUTION_OUTCOME_RECORDED,
        SECOND_CARRIER_EXECUTION_OUTCOME_RECORDED,
        execution_outcome,
        "SECOND_CARRIER_EXECUTION_NOT_RECORDED",
    )
    _check(
        checks,
        "second_carrier_execution_failed_checks_zero",
        execution_failed_count == 0,
        0,
        execution_failed_count,
        "SECOND_CARRIER_EXECUTION_FAILED_CHECKS_PRESENT",
    )
    _check(
        checks,
        "second_carrier_execution_recorded_bounded_execution",
        _execution_bool(request, "bounded_execution_recorded", default=False)
        or _execution_bool(request, "recorded_bounded_execution", default=False),
        "bounded second-carrier execution recorded",
        _first_declared(
            _execution_value(request, "bounded_execution_recorded"),
            _execution_value(request, "recorded_bounded_execution"),
        ),
        "SECOND_CARRIER_EXECUTION_DID_NOT_RECORD_BOUNDED_EXECUTION",
    )
    _check(
        checks,
        "second_carrier_execution_did_not_treat_execution_as_output",
        not _execution_bool(request, "treated_execution_as_output", default=False)
        and (
            _execution_bool(request, "execution_not_output", default=True)
            or _execution_value(request, "execution_not_output") is None
        ),
        "execution remains bounded execution posture and is not output",
        {
            "treated_execution_as_output": _execution_value(
                request,
                "treated_execution_as_output",
            ),
            "execution_not_output": _execution_value(request, "execution_not_output"),
        },
        "SECOND_CARRIER_EXECUTION_TREATED_EXECUTION_AS_OUTPUT",
    )

    for key in POSTURE_KEYS:
        _check(
            checks,
            f"{key}_declared",
            _is_declared(request.get(key)),
            "posture declared and bounded",
            request.get(key),
            _POSTURE_MISSING_CODES[key],
        )

    lineage_basis = request.get("selected_command_report_lineage_basis")
    lineage_only = True
    if isinstance(lineage_basis, Mapping):
        lineage_only = (
            not _as_bool(lineage_basis.get("treated_as_current_report_artifact"))
            and not _as_bool(lineage_basis.get("treated_as_source"))
            and not _as_bool(lineage_basis.get("treated_as_authority"))
            and not _as_bool(lineage_basis.get("treated_as_currentness"))
        )
    _check(
        checks,
        "command_report_lineage_remains_lineage_only",
        lineage_only,
        "command report lineage remains lineage only",
        lineage_basis,
        "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENTNESS",
    )

    predecessor_basis = request.get(
        "selected_packet_emission_boundary_v1_predecessor_failure_basis"
    )
    predecessor_visible = True
    if isinstance(predecessor_basis, Mapping):
        predecessor_visible = (
            not _as_bool(predecessor_basis.get("repaired"))
            and not _as_bool(predecessor_basis.get("hidden"))
            and not _as_bool(predecessor_basis.get("claimed_passed"))
        )
    _check(
        checks,
        "predecessor_failure_evidence_visible_and_unrepaired",
        predecessor_visible,
        "v1 predecessor failure remains visible and unrepaired",
        predecessor_basis,
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    )

    _check(
        checks,
        "selected_basis_reference_shape_preserved",
        _as_bool(request.get("reference_shaped_input_posture"), default=True),
        "selected basis remains reference-shaped unless bounded output material is explicitly recorded",
        request.get("reference_shaped_input_posture", True),
        "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    )

    non_claims = _declared_non_claims_from_request(request)
    missing_or_flipped = [
        key for key in REQUIRED_FALSE_NON_CLAIMS if non_claims.get(key) is not False
    ]
    _check(
        checks,
        "required_non_claims_explicit_and_false",
        not missing_or_flipped,
        {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
        {"missing_or_flipped": missing_or_flipped},
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )

    shortcut_block_checks = (
        (
            "second_carrier_execution_output_not_treated_as_capture",
            "second_carrier_execution_output_treated_as_capture",
            "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_CAPTURE",
        ),
        (
            "second_carrier_execution_output_not_treated_as_result",
            "second_carrier_execution_output_treated_as_result",
            "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_RESULT",
        ),
        (
            "second_carrier_execution_output_not_treated_as_success",
            "second_carrier_execution_output_treated_as_success",
            "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_SUCCESS",
        ),
        (
            "second_carrier_execution_output_not_treated_as_external_result",
            "second_carrier_execution_output_treated_as_external_result",
            "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_EXTERNAL_RESULT",
        ),
        (
            "second_carrier_execution_output_not_treated_as_cross_carrier_evidence",
            "second_carrier_execution_output_treated_as_cross_carrier_evidence",
            "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_CROSS_CARRIER_EVIDENCE",
        ),
        (
            "second_carrier_execution_output_not_treated_as_source_transfer",
            "second_carrier_execution_output_treated_as_source_transfer",
            "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_SOURCE_TRANSFER",
        ),
        (
            "second_carrier_execution_output_not_treated_as_source_receipt",
            "second_carrier_execution_output_treated_as_source_receipt",
            "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_SOURCE_RECEIPT",
        ),
        (
            "second_carrier_execution_output_not_treated_as_reception_authorization",
            "second_carrier_execution_output_treated_as_reception_authorization",
            "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_RECEPTION_AUTHORIZATION",
        ),
        (
            "second_carrier_execution_output_not_treated_as_source",
            "second_carrier_execution_output_treated_as_source",
            "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_SOURCE",
        ),
        (
            "second_carrier_execution_output_not_treated_as_authority",
            "second_carrier_execution_output_treated_as_authority",
            "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_AUTHORITY",
        ),
        (
            "second_carrier_execution_output_not_treated_as_currentness",
            "second_carrier_execution_output_treated_as_currentness",
            "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_CURRENTNESS",
        ),
        (
            "second_carrier_execution_output_not_treated_as_final_completion",
            "second_carrier_execution_output_treated_as_final_completion",
            "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_FINAL_COMPLETION",
        ),
        (
            "second_carrier_execution_output_not_treated_as_runtime",
            "second_carrier_execution_output_treated_as_runtime",
            "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_RUNTIME",
        ),
        (
            "second_carrier_execution_output_not_treated_as_continuation",
            "second_carrier_execution_output_treated_as_continuation",
            "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_CONTINUATION",
        ),
        (
            "second_carrier_execution_output_not_treated_as_reusable_permission",
            "second_carrier_execution_output_treated_as_reusable_permission",
            "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_REUSABLE_PERMISSION",
        ),
        (
            "second_carrier_execution_output_not_treated_as_follow_on_work",
            "second_carrier_execution_output_treated_as_follow_on_work",
            "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_FOLLOW_ON_WORK",
        ),
        (
            "second_carrier_output_capture_not_created",
            "second_carrier_output_capture_created",
            "SECOND_CARRIER_OUTPUT_CAPTURE_CREATED",
        ),
        (
            "second_carrier_result_not_created",
            "second_carrier_result_created",
            "SECOND_CARRIER_RESULT_CREATED",
        ),
        (
            "second_carrier_success_not_created",
            "second_carrier_success_created",
            "SECOND_CARRIER_SUCCESS_CREATED",
        ),
        ("external_result_not_created", "external_result_created", "EXTERNAL_RESULT_CREATED"),
        (
            "cross_carrier_evidence_not_created",
            "cross_carrier_evidence_created",
            "CROSS_CARRIER_EVIDENCE_CREATED",
        ),
        ("source_transfer_not_occurred", "source_transfer_occurred", "SOURCE_TRANSFER_OCCURRED"),
        ("source_receipt_not_occurred", "source_receipt_occurred", "SOURCE_RECEIPT_OCCURRED"),
        (
            "reception_authorization_not_created",
            "reception_authorization_created",
            "RECEPTION_AUTHORIZATION_CREATED",
        ),
        ("source_not_created", "source_created", "SOURCE_CREATED"),
        ("authority_not_created", "authority_created", "AUTHORITY_CREATED"),
        ("currentness_not_created", "currentness_created", "CURRENTNESS_CREATED"),
        (
            "final_completion_not_claimed",
            "final_completion_claimed",
            "FINAL_COMPLETION_CLAIMED",
        ),
        ("runtime_hosting_not_created", "runtime_hosting_created", "RUNTIME_HOSTING_CREATED"),
        ("deployment_not_created", "deployment_created", "DEPLOYMENT_CREATED"),
        ("public_release_not_created", "public_release_created", "PUBLIC_RELEASE_CREATED"),
        (
            "operation_permission_not_created",
            "operation_permission_created",
            "OPERATION_PERMISSION_CREATED",
        ),
        ("continuation_not_authorized", "continuation_authorized", "CONTINUATION_AUTHORIZED"),
        ("reusable_permission_not_created", "reusable_permission_created", "REUSABLE_PERMISSION_CREATED"),
        (
            "derivative_reception_not_authorized",
            "derivative_reception_authorized",
            "DERIVATIVE_RECEPTION_AUTHORIZED",
        ),
        ("vessel_relation_not_authorized", "vessel_relation_authorized", "VESSEL_RELATION_AUTHORIZED"),
        (
            "another_reception_request_not_authorized",
            "another_reception_request_authorized",
            "ANOTHER_RECEPTION_REQUEST_AUTHORIZED",
        ),
        ("follow_on_work_not_authorized", "follow_on_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
        (
            "receiving_carrier_not_treated_as_authority",
            "receiving_carrier_treated_as_authority",
            "RECEIVING_CARRIER_TREATED_AS_AUTHORITY",
        ),
        (
            "artifact_existence_not_treated_as_output_authority",
            "artifact_existence_treated_as_output_authority",
            "ARTIFACT_EXISTENCE_TREATED_AS_OUTPUT_AUTHORITY",
        ),
        (
            "artifact_path_not_treated_as_currentness",
            "artifact_path_treated_as_currentness",
            "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
        ),
        (
            "repo_local_availability_not_treated_as_output_authority",
            "repo_local_availability_treated_as_output_authority",
            "REPO_LOCAL_AVAILABILITY_TREATED_AS_OUTPUT_AUTHORITY",
        ),
        (
            "hidden_repo_state_not_used_as_output_content",
            "hidden_repo_state_used_as_output_content",
            "HIDDEN_REPO_STATE_USED_AS_OUTPUT_CONTENT",
        ),
        (
            "hidden_repo_state_not_used_as_output_authority",
            "hidden_repo_state_used_as_output_authority",
            "HIDDEN_REPO_STATE_USED_AS_OUTPUT_AUTHORITY",
        ),
        (
            "raw_full_prior_artifact_body_not_returned",
            "raw_full_prior_artifact_body_returned",
            "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
        ),
        (
            "consumed_request_not_reopened",
            "consumed_request_reopened",
            "CONSUMED_REQUEST_REOPENED",
        ),
        (
            "authorization_token_not_reused",
            "authorization_token_reused",
            "AUTHORIZATION_TOKEN_REUSED",
        ),
        (
            "full_prior_artifact_body_not_emitted_outside_bounded_output",
            "full_prior_artifact_body_emitted_outside_bounded_output",
            "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_OUTPUT",
        ),
        ("artifacts_not_mutated", "artifacts_mutated", "ARTIFACTS_MUTATED"),
    )
    for check_name, field, code in shortcut_block_checks:
        value = _first_declared(request.get(field), non_claims.get(field))
        _check(checks, check_name, not _as_bool(value), False, value, code)

    return checks


def _first_failure(checks: list[dict[str, Any]]) -> tuple[str, str] | None:
    for check in checks:
        if not check.get("passed"):
            code = str(check.get("block_code") or check.get("failure_code"))
            return code, str(check.get("check_name"))
    return None


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: list[dict[str, Any]],
    block: dict[str, Any],
) -> dict[str, Any]:
    request_id = str(
        request.get("second_carrier_execution_output_request_id")
        or "portable_source_body_verification_second_carrier_execution_output_request"
    )
    statement = _statement(outcome == OUTCOME_RECORDED)
    failed_count = sum(1 for check in checks if not check.get("passed"))
    passed_count = sum(1 for check in checks if check.get("passed"))

    result: dict[str, Any] = {
        "portable_source_body_verification_second_carrier_execution_output_metadata": {
            "portable_source_body_verification_second_carrier_execution_output_result_id": (
                request_id
            ),
            "portable_source_body_verification_second_carrier_execution_output_result_type": (
                RESULT_TYPE
            ),
            "portable_source_body_verification_second_carrier_execution_output_result_version": (
                RESULT_VERSION
            ),
            "result_version": RESULT_VERSION,
            "generated_at": _now(),
            "resolver_module": RESOLVER_MODULE,
            "second_carrier_execution_output_request_id": request_id,
        },
        "declared_second_carrier_execution_output_question": {
            "second_carrier_execution_output_request_id": request_id,
            "question": request.get("second_carrier_execution_output_question"),
            "intent": request.get("second_carrier_execution_output_intent"),
        },
        "second_carrier_execution_output_scope": {
            "declared_scope": _scope_from_request(request),
            "supported_scope": list(SUPPORTED_SECOND_CARRIER_EXECUTION_OUTPUT_SCOPE),
            "unsupported_scope_values": [
                scope
                for scope in _scope_from_request(request)
                if scope not in SUPPORTED_SECOND_CARRIER_EXECUTION_OUTPUT_SCOPE
            ],
        },
        "second_carrier_execution_output_checks": checks,
        "second_carrier_execution_output_statement": statement,
        "second_carrier_execution_output_non_meaning": _non_meaning(),
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

    result[
        "selected_second_carrier_execution_output_boundary_basis"
    ].setdefault("outcome", _output_boundary_value(request, "outcome"))
    result[
        "selected_second_carrier_execution_output_boundary_basis"
    ].setdefault("result_version", _first_declared(
        _output_boundary_value(request, "version"),
        _output_boundary_value(request, "result_version"),
    ))
    result[
        "selected_second_carrier_execution_output_boundary_basis"
    ].setdefault("failed_check_count", _as_int(
        _output_boundary_value(request, "failed_check_count"),
        default=None,
    ))
    result[
        "selected_second_carrier_execution_output_boundary_basis"
    ].setdefault(
        "declared_future_output_step",
        _output_boundary_bool(request, "declared_future_output_step")
        or _output_boundary_bool(
            request,
            "one_future_second_carrier_execution_output_step_declared",
        ),
    )
    result["selected_second_carrier_execution_basis"].setdefault(
        "outcome",
        _execution_value(request, "outcome"),
    )
    result["selected_second_carrier_execution_basis"].setdefault(
        "failed_check_count",
        _as_int(_execution_value(request, "failed_check_count"), default=None),
    )
    result["selected_second_carrier_execution_basis"].setdefault(
        "bounded_execution_recorded",
        _execution_bool(request, "bounded_execution_recorded")
        or _execution_bool(request, "recorded_bounded_execution"),
    )
    result["selected_second_carrier_execution_basis"].setdefault(
        "execution_not_output",
        not _execution_bool(request, "treated_execution_as_output"),
    )

    summary = build_portable_source_body_verification_second_carrier_execution_output_summary(
        result
    )
    summary["passed_check_count"] = passed_count
    summary["failed_check_count"] = failed_count
    result[
        "portable_source_body_verification_second_carrier_execution_output_summary"
    ] = summary
    return result


def _malformed_result(reason: str) -> dict[str, Any]:
    request = {
        "second_carrier_execution_output_request_id": (
            "malformed_second_carrier_execution_output_request"
        ),
        "second_carrier_execution_output_question": None,
        "second_carrier_execution_output_intent": None,
    }
    checks: list[dict[str, Any]] = []
    _check(
        checks,
        "declared_second_carrier_execution_output_request_mapping",
        False,
        "mapping request",
        reason,
        "DECLARED_SECOND_CARRIER_EXECUTION_OUTPUT_REQUEST_MALFORMED",
    )
    return _build_result(
        request,
        OUTCOME_BLOCKED,
        checks,
        _block("DECLARED_SECOND_CARRIER_EXECUTION_OUTPUT_REQUEST_MALFORMED", reason),
    )


def resolve_portable_source_body_verification_second_carrier_execution_output(
    declared_second_carrier_execution_output_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve bounded second-carrier execution output posture."""

    if declared_second_carrier_execution_output_request is None:
        return _malformed_result("declared request is missing")
    if not isinstance(declared_second_carrier_execution_output_request, Mapping):
        return _malformed_result("declared request must be a mapping")

    request = copy.deepcopy(dict(declared_second_carrier_execution_output_request))
    checks = _build_checks(request)
    failure = _first_failure(checks)

    requested_outcome = request.get("requested_second_carrier_execution_output_outcome")
    if failure:
        code, name = failure
        return _build_result(
            request,
            OUTCOME_BLOCKED,
            checks,
            _block(code, f"blocked by {name}"),
        )
    if requested_outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        return _build_result(request, OUTCOME_REQUIRES_ADDITIONAL_BASIS, checks, _empty_block())
    if requested_outcome == OUTCOME_NOT_RECORDED or request.get(
        "second_carrier_execution_output_intent"
    ) == INTENT_DO_NOT_RECORD:
        return _build_result(request, OUTCOME_NOT_RECORDED, checks, _empty_block())
    return _build_result(request, OUTCOME_RECORDED, checks, _empty_block())


def resolve_portable_source_body_verification_second_carrier_execution_output_from_path(
    declared_second_carrier_execution_output_request_path: Path | str,
) -> dict[str, Any]:
    """Read a JSON request object from a path and resolve it."""

    path = Path(declared_second_carrier_execution_output_request_path)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise PortableSourceBodyVerificationSecondCarrierExecutionOutputError(
            f"declared request path is missing: {path}"
        ) from exc
    except OSError as exc:
        raise PortableSourceBodyVerificationSecondCarrierExecutionOutputError(
            f"declared request path is unreadable: {path}"
        ) from exc
    except json.JSONDecodeError as exc:
        raise PortableSourceBodyVerificationSecondCarrierExecutionOutputError(
            f"declared request JSON is malformed: {path}"
        ) from exc
    if not isinstance(data, Mapping):
        return _malformed_result("declared request JSON must be an object")
    return resolve_portable_source_body_verification_second_carrier_execution_output(data)


def _safe_filename_part(value: Any) -> str:
    text = str(value or "second_carrier_execution_output_request").strip()
    safe = []
    for character in text:
        if character.isalnum() or character in {"-", "_", "."}:
            safe.append(character)
        else:
            safe.append("_")
    return "".join(safe).strip("._") or "second_carrier_execution_output_request"


def _unique_path(path: Path) -> Path:
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


def write_portable_source_body_verification_second_carrier_execution_output_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a bounded result JSON file without silently overwriting."""

    if not isinstance(result, Mapping):
        raise PortableSourceBodyVerificationSecondCarrierExecutionOutputError(
            "result must be a mapping"
        )
    metadata = result.get(
        "portable_source_body_verification_second_carrier_execution_output_metadata",
        {},
    )
    if not isinstance(metadata, Mapping):
        metadata = {}
    request_id = _first_declared(
        metadata.get("second_carrier_execution_output_request_id"),
        metadata.get(
            "portable_source_body_verification_second_carrier_execution_output_result_id"
        ),
        _nested_get(result, ("declared_second_carrier_execution_output_question", "second_carrier_execution_output_request_id")),
    )
    if output_path is None:
        filename = (
            f"{_safe_filename_part(request_id)}__"
            "portable_source_body_verification_second_carrier_execution_output_result.json"
        )
        path = OUTPUT_ROOT / filename
    else:
        path = Path(output_path)
        if path.exists() and path.is_dir():
            filename = (
                f"{_safe_filename_part(request_id)}__"
                "portable_source_body_verification_second_carrier_execution_output_result.json"
            )
            path = path / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    final_path = _unique_path(path)
    final_path.write_text(
        json.dumps(_sanitize(result), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return final_path


def build_portable_source_body_verification_second_carrier_execution_output_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact summary while preserving key non-claim visibility."""

    metadata = result.get(
        "portable_source_body_verification_second_carrier_execution_output_metadata",
        {},
    )
    if not isinstance(metadata, Mapping):
        metadata = {}
    declared = result.get("declared_second_carrier_execution_output_question", {})
    if not isinstance(declared, Mapping):
        declared = {}
    statement = result.get("second_carrier_execution_output_statement", {})
    if not isinstance(statement, Mapping):
        statement = {}
    checks = result.get("second_carrier_execution_output_checks", [])
    if not isinstance(checks, list):
        checks = []
    block = result.get("block", {})
    if not isinstance(block, Mapping):
        block = {}
    non_claims = result.get("non_claims", {})
    if not isinstance(non_claims, Mapping):
        non_claims = {}
    boundary_basis = result.get(
        "selected_second_carrier_execution_output_boundary_basis",
        {},
    )
    if not isinstance(boundary_basis, Mapping):
        boundary_basis = {}

    summary: dict[str, Any] = {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("reason"),
        "request_id": _first_declared(
            metadata.get("second_carrier_execution_output_request_id"),
            declared.get("second_carrier_execution_output_request_id"),
            metadata.get(
                "portable_source_body_verification_second_carrier_execution_output_result_id"
            ),
        ),
        "question": declared.get("question"),
        "intent": declared.get("intent"),
        "passed_check_count": sum(1 for check in checks if check.get("passed")),
        "failed_check_count": sum(1 for check in checks if not check.get("passed")),
        "result_version": _first_declared(
            metadata.get(
                "portable_source_body_verification_second_carrier_execution_output_result_version"
            ),
            metadata.get("result_version"),
        ),
        "resolver_module": metadata.get("resolver_module"),
        "selected_second_carrier_execution_output_boundary_outcome": boundary_basis.get(
            "outcome"
        ),
        "selected_second_carrier_execution_output_boundary_version": boundary_basis.get(
            "result_version"
        ),
        "selected_second_carrier_execution_output_boundary_failed_check_count": (
            boundary_basis.get("failed_check_count")
        ),
        "key_non_claims": {
            key: non_claims.get(key, False) for key in REQUIRED_FALSE_NON_CLAIMS
        },
        "no_output_capture_result_success_external_result_or_cross_carrier_evidence": (
            non_claims.get("second_carrier_output_capture_created", False) is False
            and non_claims.get("second_carrier_result_created", False) is False
            and non_claims.get("second_carrier_success_created", False) is False
            and non_claims.get("external_result_created", False) is False
            and non_claims.get("cross_carrier_evidence_created", False) is False
        ),
        "no_source_authority_currentness_final_completion_or_runtime": (
            non_claims.get("source_created", False) is False
            and non_claims.get("authority_created", False) is False
            and non_claims.get("currentness_created", False) is False
            and non_claims.get("final_completion_claimed", False) is False
            and non_claims.get("runtime_hosting_created", False) is False
        ),
        "no_deployment_public_release_or_follow_on": (
            non_claims.get("deployment_created", False) is False
            and non_claims.get("public_release_created", False) is False
            and non_claims.get("follow_on_work_authorized", False) is False
        ),
        "v1_predecessor_failure_preserved": (
            non_claims.get("v1_repaired", False) is False
            and non_claims.get("v1_hidden", False) is False
            and non_claims.get("v1_claimed_passed", False) is False
        ),
    }
    for key in ALLOWED_TRUE_RECORDED_FIELDS:
        summary[key] = bool(statement.get(key, False))
    return summary


def _basis_reference(name: str, **values: Any) -> dict[str, Any]:
    section = {
        "basis_name": name,
        "basis_declared": True,
        "basis_role": "selected_reference_basis_only",
        "reference_shape_preserved": True,
    }
    section.update(values)
    return section


def _posture_declared(name: str) -> dict[str, Any]:
    return {
        "posture_declared": True,
        "posture_name": name,
        "preserves_output_membrane": True,
    }


def build_declared_portable_source_body_verification_second_carrier_execution_output_request(
    second_carrier_execution_output_request_id: str = (
        "portable_source_body_verification_second_carrier_execution_output_request_001"
    ),
    second_carrier_execution_output_question: str = QUESTION,
    second_carrier_execution_output_intent: str = INTENT_RECORD,
    **overrides: Any,
) -> dict[str, Any]:
    """Build a small declared request with required false non-claims."""

    request: dict[str, Any] = {
        "second_carrier_execution_output_request_id": (
            second_carrier_execution_output_request_id
        ),
        "second_carrier_execution_output_question": (
            second_carrier_execution_output_question
        ),
        "second_carrier_execution_output_intent": second_carrier_execution_output_intent,
        "second_carrier_execution_output_scope": list(
            SUPPORTED_SECOND_CARRIER_EXECUTION_OUTPUT_SCOPE
        ),
        "declared_non_claims": _non_claims(),
        "reference_shaped_input_posture": True,
        "selected_second_carrier_execution_output_boundary_basis": _basis_reference(
            "second-carrier execution output boundary",
            outcome=OUTPUT_BOUNDARY_OUTCOME_RECORDED,
            result_version=RESULT_VERSION,
            failed_check_count=0,
            declared_future_output_step=True,
            already_created_output=False,
            already_created_output_artifact=False,
            already_created_output_capture=False,
            already_created_second_carrier_result=False,
            already_created_second_carrier_success=False,
            created_external_result=False,
            created_cross_carrier_evidence=False,
            used_hidden_repo_state_as_output_authority=False,
            treated_repo_local_availability_as_output_authority=False,
            treated_receiving_carrier_as_authority=False,
            raw_full_prior_artifact_body_returned=False,
        ),
        "selected_second_carrier_execution_basis": _basis_reference(
            "second-carrier execution",
            outcome=SECOND_CARRIER_EXECUTION_OUTCOME_RECORDED,
            failed_check_count=0,
            bounded_execution_recorded=True,
            recorded_bounded_execution=True,
            execution_not_output=True,
            treated_execution_as_output=False,
        ),
    }

    for key in SELECTED_BASIS_KEYS:
        request.setdefault(key, _basis_reference(key))
    for key in POSTURE_KEYS:
        request[key] = _posture_declared(key.removesuffix("_posture"))
    for key in REQUIRED_FALSE_NON_CLAIMS:
        request.setdefault(key, False)
    request.update(overrides)
    return request
