"""Resolve portable source-body verification second-carrier verification boundary.

This module is downstream of the bounded second-carrier success line. It may
record one future second-carrier verification step boundary only. It does not
create verification, external result, cross-carrier evidence, portable
verification closure, source transfer, source receipt, reception authorization,
source, authority, currentness, final completion, runtime, continuation,
reusable permission, derivative reception, vessel relation, another reception
request, or follow-on work.

The resolver is self-contained, imports no repo-local modules, runs no
subprocesses, mutates no upstream artifact, preserves predecessor failure
evidence, and keeps official enum, scope, outcome, block-code, posture,
section, non-claim, and boolean-field strings unredacted while containing
hostile raw body payload values.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping, Sequence
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class PortableSourceBodyVerificationSecondCarrierVerificationBoundaryError(Exception):
    """Bounded resolver error for explicit unreadable or malformed inputs."""


RESOLVER_MODULE = (
    "resolve_portable_source_body_verification_second_carrier_verification_boundary"
)
RESULT_TYPE = (
    "portable_source_body_verification_second_carrier_verification_boundary_result"
)
RESULT_VERSION = "0.1.0"
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_portable_source_body_verification_"
    "second_carrier_verification_boundary"
)

CORE_QUESTION = (
    "Can the clean second-carrier-success basis be bounded for one future "
    "second-carrier verification step without creating verification yet, "
    "external result, cross-carrier evidence, portable verification closure, "
    "source transfer, source receipt, reception authorization, source, "
    "authority, currentness, runtime, final completion, continuation, reusable "
    "permission, derivative reception, vessel relation, another reception "
    "request, or follow-on work?"
)

OUTCOME_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_VERIFICATION_BOUNDARY_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_VERIFICATION_BOUNDARY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_VERIFICATION_BOUNDARY_"
    "REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_VERIFICATION_BOUNDARY_BLOCKED"
)
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = (
    "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_VERIFICATION_BOUNDARY"
)
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_VERIFICATION_BOUNDARY"
)
INTENT_BLOCK = (
    "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_VERIFICATION_BOUNDARY"
)
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

EXPECTED_SECOND_CARRIER_SUCCESS_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_SUCCESS_RECORDED"
)
EXPECTED_SECOND_CARRIER_SUCCESS_VERSION = "0.1.0"
EXPECTED_SECOND_CARRIER_SUCCESS_BOUNDARY_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_SUCCESS_BOUNDARY_RECORDED"
)
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
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_ONLY",
    "ONE_FUTURE_SECOND_CARRIER_VERIFICATION_STEP_ONLY",
    "SECOND_CARRIER_SUCCESS_BASIS_PRESERVED",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_BASIS_PRESERVED",
    "SECOND_CARRIER_RESULT_BASIS_PRESERVED",
    "RETURNED_SECOND_CARRIER_CAPTURE_BASIS_PRESERVED",
    "CAPTURE_INTAKE_BASIS_PRESERVED",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_PRESERVED",
    "SUCCESS_ARTIFACT_BASIS_PRESERVED",
    "VERIFICATION_NOT_CREATED",
    "VERIFICATION_BOUNDARY_NOT_VERIFICATION",
    "SUCCESS_NOT_VERIFICATION",
    "SUCCESS_NOT_EXTERNAL_RESULT",
    "ZERO_EXIT_CODE_NOT_VERIFICATION",
    "OK_OUTPUT_NOT_VERIFICATION",
    "RAN_7_TESTS_NOT_CROSS_CARRIER_PROOF",
    "RETURNED_CAPTURE_NOT_CROSS_CARRIER_PROOF",
    "EXTERNAL_RESULT_NOT_CREATED",
    "CROSS_CARRIER_EVIDENCE_NOT_CREATED",
    "PORTABLE_VERIFICATION_CLOSURE_NOT_CREATED",
    "VERIFICATION_NOT_SOURCE_TRANSFER",
    "VERIFICATION_NOT_SOURCE_RECEIPT",
    "VERIFICATION_NOT_RECEPTION_AUTHORIZATION",
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
    "HIDDEN_REPO_STATE_NOT_USED_AS_VERIFICATION_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_NOT_VERIFICATION_AUTHORITY",
    "SELECTED_BASIS_REFERENCE_SHAPE_PRESERVED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
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
SUPPORTED_SECOND_CARRIER_VERIFICATION_BOUNDARY_SCOPE = SUPPORTED_SCOPE_VALUES

SELECTED_BASIS_KEYS = (
    "selected_second_carrier_success_basis",
    "selected_second_carrier_success_terminal_summary_basis",
    "selected_second_carrier_success_boundary_basis",
    "selected_second_carrier_success_boundary_terminal_summary_basis",
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
    "second_carrier_verification_boundary_only_posture",
    "one_future_second_carrier_verification_step_posture",
    "second_carrier_success_basis_preserved_posture",
    "second_carrier_success_boundary_basis_preserved_posture",
    "second_carrier_result_basis_preserved_posture",
    "returned_second_carrier_capture_basis_preserved_posture",
    "capture_intake_basis_preserved_posture",
    "second_carrier_output_capture_basis_preserved_posture",
    "success_artifact_basis_preserved_posture",
    "verification_not_created_posture",
    "verification_boundary_not_verification_posture",
    "success_not_verification_posture",
    "success_not_external_result_posture",
    "zero_exit_code_not_verification_posture",
    "ok_output_not_verification_posture",
    "ran_7_tests_not_cross_carrier_proof_posture",
    "returned_capture_not_cross_carrier_proof_posture",
    "external_result_not_created_posture",
    "cross_carrier_evidence_not_created_posture",
    "portable_verification_closure_not_created_posture",
    "verification_not_source_transfer_posture",
    "verification_not_source_receipt_posture",
    "verification_not_reception_authorization_posture",
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
    "repo_local_availability_not_verification_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "first_success_boundary_test_failure_preserved_posture",
    "first_result_boundary_resolver_failure_preserved_posture",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "second_carrier_verification_boundary_recorded",
    "one_future_second_carrier_verification_step_declared",
    "second_carrier_success_basis_preserved",
    "second_carrier_success_boundary_basis_preserved",
    "second_carrier_result_basis_preserved",
    "returned_second_carrier_capture_basis_preserved",
    "capture_intake_basis_preserved",
    "second_carrier_output_capture_basis_preserved",
    "success_artifact_basis_preserved",
    "verification_not_created",
    "verification_boundary_not_verification",
    "success_not_verification",
    "success_not_external_result",
    "zero_exit_code_not_verification",
    "ok_output_not_verification",
    "ran_7_tests_not_cross_carrier_proof",
    "returned_capture_not_cross_carrier_proof",
    "external_result_not_created",
    "cross_carrier_evidence_not_created",
    "portable_verification_closure_not_created",
    "verification_not_source_transfer",
    "verification_not_source_receipt",
    "verification_not_reception_authorization",
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
    "hidden_repo_state_not_used_as_verification_authority",
    "repo_local_availability_not_verification_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "official_enum_scope_strings_not_redacted",
    "hostile_raw_body_content_contained",
    "first_success_boundary_test_failure_preserved",
    "first_result_boundary_resolver_failure_preserved",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
)

REQUIRED_FALSE_NON_CLAIMS = (
    "verification_created",
    "external_result_created",
    "cross_carrier_evidence_created",
    "portable_verification_closure_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "second_carrier_verification_boundary_treated_as_verification",
    "second_carrier_verification_boundary_treated_as_external_result",
    "second_carrier_verification_boundary_treated_as_cross_carrier_evidence",
    "second_carrier_verification_boundary_treated_as_portable_verification_closure",
    "second_carrier_verification_boundary_treated_as_source_transfer",
    "second_carrier_verification_boundary_treated_as_source_receipt",
    "second_carrier_verification_boundary_treated_as_reception_authorization",
    "second_carrier_verification_boundary_treated_as_source",
    "second_carrier_verification_boundary_treated_as_authority",
    "second_carrier_verification_boundary_treated_as_currentness",
    "second_carrier_verification_boundary_treated_as_final_completion",
    "second_carrier_verification_boundary_treated_as_runtime",
    "second_carrier_verification_boundary_treated_as_continuation",
    "second_carrier_verification_boundary_treated_as_reusable_permission",
    "second_carrier_verification_boundary_treated_as_follow_on_work",
    "second_carrier_success_treated_as_verification",
    "second_carrier_success_treated_as_external_result",
    "zero_exit_code_treated_as_verification",
    "ok_output_treated_as_verification",
    "ran_7_tests_treated_as_cross_carrier_proof",
    "returned_capture_treated_as_cross_carrier_evidence",
    "receiving_carrier_treated_as_authority",
    "artifact_existence_treated_as_verification_authority",
    "artifact_path_treated_as_currentness",
    "repo_local_availability_treated_as_verification_authority",
    "hidden_repo_state_used_as_verification_content",
    "hidden_repo_state_used_as_verification_authority",
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
    "first_success_boundary_test_repaired",
    "first_success_boundary_test_hidden",
    "first_success_boundary_test_claimed_passed",
    "first_result_boundary_resolver_repaired",
    "first_result_boundary_resolver_hidden",
    "first_result_boundary_resolver_claimed_passed",
)

BLOCK_CODES = (
    "DECLARED_SECOND_CARRIER_VERIFICATION_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_SECOND_CARRIER_VERIFICATION_BOUNDARY_REQUEST_UNREADABLE",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_QUESTION_UNDECLARED",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_INTENT_UNSUPPORTED",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_BLOCK_REQUESTED",
    "SECOND_CARRIER_SUCCESS_BASIS_MISSING",
    "SECOND_CARRIER_SUCCESS_NOT_RECORDED",
    "SECOND_CARRIER_SUCCESS_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_SUCCESS_VERSION_NOT_0_1_0",
    "SECOND_CARRIER_SUCCESS_DID_NOT_RECORD_BOUNDED_SUCCESS",
    "SECOND_CARRIER_SUCCESS_ALREADY_CREATED_VERIFICATION",
    "SECOND_CARRIER_SUCCESS_ALREADY_CREATED_EXTERNAL_RESULT",
    "SECOND_CARRIER_SUCCESS_ALREADY_CREATED_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_SUCCESS_ALREADY_CREATED_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_SUCCESS_TREATED_SUCCESS_AS_VERIFICATION",
    "SECOND_CARRIER_SUCCESS_TREATED_SUCCESS_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_SUCCESS_TREATED_SUCCESS_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_SUCCESS_TREATED_SUCCESS_AS_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_SUCCESS_TREATED_ZERO_EXIT_CODE_AS_VERIFICATION",
    "SECOND_CARRIER_SUCCESS_TREATED_OK_AS_VERIFICATION",
    "SECOND_CARRIER_SUCCESS_TREATED_RAN_7_TESTS_AS_CROSS_CARRIER_PROOF",
    "SECOND_CARRIER_SUCCESS_TREATED_RETURNED_CAPTURE_AS_CROSS_CARRIER_PROOF",
    "SECOND_CARRIER_SUCCESS_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_BASIS_MISSING",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_NOT_RECORDED",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_RESULT_BASIS_MISSING",
    "SECOND_CARRIER_RESULT_NOT_RECORDED",
    "SECOND_CARRIER_RESULT_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_RESULT_VERSION_NOT_0_1_0",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_BASIS_MISSING",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_NOT_RECORDED",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_FAILED_CHECKS_PRESENT",
    "RETURNED_CAPTURE_INTAKE_BASIS_MISSING",
    "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
    "RETURNED_CAPTURE_TREATED_AS_VERIFICATION",
    "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_PROOF",
    "ZERO_EXIT_CODE_TREATED_AS_VERIFICATION",
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
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_VERIFICATION",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_SOURCE",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_AUTHORITY",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_CURRENTNESS",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_FINAL_COMPLETION",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_RUNTIME",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_CONTINUATION",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_VERIFICATION_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_VERIFICATION_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_VERIFICATION_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_VERIFICATION_AUTHORITY",
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
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_VERIFICATION_BOUNDARY",
    "ARTIFACTS_MUTATED",
    "RETURNED_CAPTURE_MATERIAL_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_SECOND_CARRIER_VERIFICATION_BOUNDARY_SCOPE",
)

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
        "raw_verification_body",
        "capture_body",
        "second_carrier_verification_body",
        "external_result_body",
        "cross_carrier_evidence_body",
        "portable_verification_closure_body",
        "source_body",
        "authority_body",
        "hidden_repo_state",
        "current_working_tree",
        "local_cache",
        "repo_local_only_dependency",
    }
)
RAW_SENTINELS = (
    "RAW_SECOND_CARRIER_VERIFICATION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)
REDACTED_RAW_VALUE = "[bounded-redacted-raw-or-hidden-state]"

OFFICIAL_STRINGS = frozenset(
    set(SUPPORTED_SCOPE_VALUES)
    | set(OUTCOME_FAMILY)
    | set(BLOCK_CODES)
    | set(SELECTED_BASIS_KEYS)
    | set(POSTURE_KEYS)
    | set(REQUIRED_FALSE_NON_CLAIMS)
    | set(ALLOWED_TRUE_RECORDED_FIELDS)
    | set(SUPPORTED_INTENTS)
    | {
        RESOLVER_MODULE,
        RESULT_VERSION,
        RESULT_TYPE,
        CORE_QUESTION,
        EXPECTED_SECOND_CARRIER_SUCCESS_OUTCOME,
        EXPECTED_SECOND_CARRIER_SUCCESS_BOUNDARY_OUTCOME,
        EXPECTED_SECOND_CARRIER_RESULT_OUTCOME,
        EXPECTED_SECOND_CARRIER_RESULT_BOUNDARY_V2_OUTCOME,
        EXPECTED_SECOND_CARRIER_OUTPUT_CAPTURE_OUTCOME,
        "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
        "RETURNED_RESULT_CONTAINMENT_PRESERVED",
        "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
        "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
        "FIRST_SUCCESS_BOUNDARY_TEST_FAILURE_PRESERVED",
        "FIRST_RESULT_BOUNDARY_RESOLVER_FAILURE_PRESERVED",
    }
)


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _is_sensitive_key(key: Any) -> bool:
    key_text = str(key)
    return key_text in SENSITIVE_CONTENT_KEYS or key_text.endswith("_body")


def _contains_raw_sentinel(value: str) -> bool:
    return any(sentinel in value for sentinel in RAW_SENTINELS)


def _sanitize(value: Any, *, key: str | None = None) -> Any:
    if isinstance(value, str):
        if value in OFFICIAL_STRINGS:
            return value
        if key is not None and _is_sensitive_key(key):
            return REDACTED_RAW_VALUE
        if _contains_raw_sentinel(value):
            return REDACTED_RAW_VALUE
        return value
    if isinstance(value, Mapping):
        sanitized: dict[str, Any] = {}
        for item_key, item_value in value.items():
            key_text = str(item_key)
            if _is_sensitive_key(key_text):
                if isinstance(item_value, str) and item_value in OFFICIAL_STRINGS:
                    sanitized[key_text] = item_value
                else:
                    sanitized[key_text] = REDACTED_RAW_VALUE
            else:
                sanitized[key_text] = _sanitize(item_value, key=key_text)
        return sanitized
    if isinstance(value, (list, tuple)):
        return [_sanitize(item, key=key) for item in value]
    if isinstance(value, set):
        return [_sanitize(item, key=key) for item in sorted(value, key=str)]
    if isinstance(value, Path):
        return str(value)
    return copy.deepcopy(value)


def _json_safe(value: Any) -> Any:
    return _sanitize(value)


def _as_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, Mapping):
        for key in (
            "declared",
            "preserved",
            "recorded",
            "basis_preserved",
            "posture_declared",
            "expected_posture_preserved",
        ):
            if value.get(key) is True:
                return True
    return False


def _as_false(value: Any) -> bool:
    return value is False


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


def _request_id(request: Mapping[str, Any]) -> str:
    value = request.get("second_carrier_verification_boundary_request_id")
    if isinstance(value, str) and value.strip():
        return value.strip()
    return "portable_source_body_verification_second_carrier_verification_boundary_request_001"


def _basis_declared(request: Mapping[str, Any], key: str) -> bool:
    if key not in request:
        return False
    value = request.get(key)
    if value is None:
        return False
    if value == {} or value == [] or value == "":
        return False
    return True


def _lookup(
    request: Mapping[str, Any],
    direct_keys: Sequence[str],
    basis_keys: Sequence[str] = (),
    nested_keys: Sequence[str] = (),
) -> Any:
    for key in direct_keys:
        if key in request:
            return request[key]
    for basis_key in basis_keys:
        value = request.get(basis_key)
        if isinstance(value, Mapping):
            found = _lookup_nested(value, nested_keys or direct_keys)
            if found is not None:
                return found
    return None


def _lookup_nested(value: Mapping[str, Any], keys: Sequence[str]) -> Any:
    for key in keys:
        if key in value:
            return value[key]
    for item in value.values():
        if isinstance(item, Mapping):
            found = _lookup_nested(item, keys)
            if found is not None:
                return found
    return None


def _check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    block_code: str,
) -> dict[str, Any]:
    if block_code not in BLOCK_CODES:
        raise PortableSourceBodyVerificationSecondCarrierVerificationBoundaryError(
            f"internal check used unknown block code: {block_code}"
        )
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": _json_safe(expected_posture),
        "actual_posture": _json_safe(actual_posture),
        "block_code": None if passed else block_code,
        "failure_code": None if passed else block_code,
    }


def _scope_values(request: Mapping[str, Any]) -> list[str]:
    value = request.get("second_carrier_verification_boundary_scope")
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, Sequence) and not isinstance(value, (bytes, bytearray)):
        return [str(item) for item in value]
    return [str(value)]


def _selected_shortcuts_for_basis(request: Mapping[str, Any], basis_key: str) -> dict[str, Any]:
    prefixes_by_basis = {
        "selected_second_carrier_success_basis": (
            "selected_second_carrier_success_",
        ),
        "selected_second_carrier_success_boundary_basis": (
            "selected_second_carrier_success_boundary_",
        ),
        "selected_second_carrier_result_basis": (
            "selected_second_carrier_result_",
        ),
        "selected_second_carrier_result_boundary_v2_basis": (
            "selected_second_carrier_result_boundary_v2_",
        ),
        "selected_returned_second_carrier_live_capture_intake_basis": (
            "selected_returned_capture_",
        ),
        "selected_returned_capture_material_basis": ("selected_returned_capture_",),
        "selected_second_carrier_output_capture_basis": (
            "selected_second_carrier_output_capture_",
        ),
    }
    prefixes = prefixes_by_basis.get(basis_key, ())
    shortcuts: dict[str, Any] = {}
    for key, value in request.items():
        if any(str(key).startswith(prefix) for prefix in prefixes):
            shortcuts[str(key)] = _sanitize(value, key=str(key))
    return shortcuts


def _reference_basis_section(request: Mapping[str, Any], basis_key: str) -> dict[str, Any]:
    supplied = request.get(basis_key)
    return {
        "selected_basis_key": basis_key,
        "basis_declared": _basis_declared(request, basis_key),
        "basis_reference_shape_preserved": True,
        "basis_only": True,
        "not_verification": True,
        "not_external_result": True,
        "not_cross_carrier_evidence": True,
        "not_portable_verification_closure": True,
        "not_source_or_authority_or_currentness": True,
        "selected_basis": _sanitize(supplied, key=basis_key) if supplied is not None else None,
        "selected_shortcut_fields": _selected_shortcuts_for_basis(request, basis_key),
    }


def _posture_section(request: Mapping[str, Any], posture_key: str) -> dict[str, Any]:
    supplied = request.get(posture_key)
    return {
        "posture_key": posture_key,
        "declared": _as_bool(supplied),
        "basis_only": True,
        "created_verification": False,
        "created_external_result": False,
        "created_cross_carrier_evidence": False,
        "created_portable_verification_closure": False,
        "created_source_authority_currentness_runtime_or_completion": False,
        "authorized_follow_on_work": False,
        "declared_posture": _sanitize(supplied, key=posture_key) if supplied is not None else None,
    }


def _false_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


NON_CLAIM_BLOCK_CODE = {
    "verification_created": "VERIFICATION_CREATED",
    "external_result_created": "EXTERNAL_RESULT_CREATED",
    "cross_carrier_evidence_created": "CROSS_CARRIER_EVIDENCE_CREATED",
    "portable_verification_closure_created": "PORTABLE_VERIFICATION_CLOSURE_CREATED",
    "source_transfer_occurred": "SOURCE_TRANSFER_OCCURRED",
    "source_receipt_occurred": "SOURCE_RECEIPT_OCCURRED",
    "reception_authorization_created": "RECEPTION_AUTHORIZATION_CREATED",
    "second_carrier_verification_boundary_treated_as_verification": (
        "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_VERIFICATION"
    ),
    "second_carrier_verification_boundary_treated_as_external_result": (
        "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_EXTERNAL_RESULT"
    ),
    "second_carrier_verification_boundary_treated_as_cross_carrier_evidence": (
        "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_CROSS_CARRIER_EVIDENCE"
    ),
    "second_carrier_verification_boundary_treated_as_portable_verification_closure": (
        "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE"
    ),
    "second_carrier_verification_boundary_treated_as_source_transfer": (
        "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_SOURCE_TRANSFER"
    ),
    "second_carrier_verification_boundary_treated_as_source_receipt": (
        "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_SOURCE_RECEIPT"
    ),
    "second_carrier_verification_boundary_treated_as_reception_authorization": (
        "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION"
    ),
    "second_carrier_verification_boundary_treated_as_source": (
        "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_SOURCE"
    ),
    "second_carrier_verification_boundary_treated_as_authority": (
        "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_AUTHORITY"
    ),
    "second_carrier_verification_boundary_treated_as_currentness": (
        "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_CURRENTNESS"
    ),
    "second_carrier_verification_boundary_treated_as_final_completion": (
        "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_FINAL_COMPLETION"
    ),
    "second_carrier_verification_boundary_treated_as_runtime": (
        "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_RUNTIME"
    ),
    "second_carrier_verification_boundary_treated_as_continuation": (
        "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_CONTINUATION"
    ),
    "second_carrier_verification_boundary_treated_as_reusable_permission": (
        "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION"
    ),
    "second_carrier_verification_boundary_treated_as_follow_on_work": (
        "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK"
    ),
    "second_carrier_success_treated_as_verification": (
        "SECOND_CARRIER_SUCCESS_TREATED_SUCCESS_AS_VERIFICATION"
    ),
    "second_carrier_success_treated_as_external_result": (
        "SECOND_CARRIER_SUCCESS_TREATED_SUCCESS_AS_EXTERNAL_RESULT"
    ),
    "zero_exit_code_treated_as_verification": "ZERO_EXIT_CODE_TREATED_AS_VERIFICATION",
    "ok_output_treated_as_verification": "OK_OUTPUT_TREATED_AS_VERIFICATION",
    "ran_7_tests_treated_as_cross_carrier_proof": (
        "RAN_7_TESTS_TREATED_AS_CROSS_CARRIER_PROOF"
    ),
    "returned_capture_treated_as_cross_carrier_evidence": (
        "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_PROOF"
    ),
    "receiving_carrier_treated_as_authority": "RECEIVING_CARRIER_TREATED_AS_AUTHORITY",
    "artifact_existence_treated_as_verification_authority": (
        "ARTIFACT_EXISTENCE_TREATED_AS_VERIFICATION_AUTHORITY"
    ),
    "artifact_path_treated_as_currentness": "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "repo_local_availability_treated_as_verification_authority": (
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_VERIFICATION_AUTHORITY"
    ),
    "hidden_repo_state_used_as_verification_content": (
        "HIDDEN_REPO_STATE_USED_AS_VERIFICATION_CONTENT"
    ),
    "hidden_repo_state_used_as_verification_authority": (
        "HIDDEN_REPO_STATE_USED_AS_VERIFICATION_AUTHORITY"
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
    "first_success_boundary_test_repaired": (
        "FIRST_SUCCESS_BOUNDARY_TEST_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED"
    ),
    "first_success_boundary_test_hidden": (
        "FIRST_SUCCESS_BOUNDARY_TEST_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED"
    ),
    "first_success_boundary_test_claimed_passed": (
        "FIRST_SUCCESS_BOUNDARY_TEST_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED"
    ),
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


def _build_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    scope_values = _scope_values(request)

    checks.append(
        _check(
            "second_carrier_verification_boundary_question_declared",
            request.get("second_carrier_verification_boundary_question") == CORE_QUESTION,
            CORE_QUESTION,
            request.get("second_carrier_verification_boundary_question"),
            "SECOND_CARRIER_VERIFICATION_BOUNDARY_QUESTION_UNDECLARED",
        )
    )
    checks.append(
        _check(
            "second_carrier_verification_boundary_intent_supported",
            request.get("second_carrier_verification_boundary_intent") in SUPPORTED_INTENTS,
            SUPPORTED_INTENTS,
            request.get("second_carrier_verification_boundary_intent"),
            "SECOND_CARRIER_VERIFICATION_BOUNDARY_INTENT_UNSUPPORTED",
        )
    )
    checks.append(
        _check(
            "second_carrier_verification_boundary_scope_supported",
            bool(scope_values)
            and all(value in SUPPORTED_SCOPE_VALUES for value in scope_values),
            SUPPORTED_SCOPE_VALUES,
            scope_values,
            "UNSUPPORTED_SECOND_CARRIER_VERIFICATION_BOUNDARY_SCOPE",
        )
    )

    checks.extend(_success_basis_checks(request))
    checks.extend(_returned_capture_checks(request))
    checks.extend(_selected_basis_presence_checks(request))
    checks.extend(_posture_checks(request))
    checks.extend(_non_claim_checks(request))
    return checks


def _success_basis_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    success_outcome = _lookup(
        request,
        ("selected_second_carrier_success_result_outcome",),
        ("selected_second_carrier_success_basis",),
        ("outcome", "result_outcome"),
    )
    success_version = _lookup(
        request,
        ("selected_second_carrier_success_result_version",),
        ("selected_second_carrier_success_basis",),
        ("result_version", "version"),
    )
    success_failed_count = _as_int(
        _lookup(
            request,
            ("selected_second_carrier_success_failed_check_count",),
            ("selected_second_carrier_success_basis",),
            ("failed_check_count",),
        )
    )
    success_boundary_outcome = _lookup(
        request,
        ("selected_second_carrier_success_boundary_result_outcome",),
        ("selected_second_carrier_success_boundary_basis",),
        ("outcome", "result_outcome"),
    )
    success_boundary_failed = _as_int(
        _lookup(
            request,
            ("selected_second_carrier_success_boundary_failed_check_count",),
            ("selected_second_carrier_success_boundary_basis",),
            ("failed_check_count",),
        )
    )
    result_outcome = _lookup(
        request,
        ("selected_second_carrier_result_result_outcome",),
        ("selected_second_carrier_result_basis",),
        ("outcome", "result_outcome"),
    )
    result_version = _lookup(
        request,
        ("selected_second_carrier_result_result_version",),
        ("selected_second_carrier_result_basis",),
        ("result_version", "version"),
    )
    result_failed = _as_int(
        _lookup(
            request,
            ("selected_second_carrier_result_failed_check_count",),
            ("selected_second_carrier_result_basis",),
            ("failed_check_count",),
        )
    )
    result_boundary_v2_outcome = _lookup(
        request,
        ("selected_second_carrier_result_boundary_v2_result_outcome",),
        ("selected_second_carrier_result_boundary_v2_basis",),
        ("outcome", "result_outcome"),
    )
    result_boundary_v2_failed = _as_int(
        _lookup(
            request,
            ("selected_second_carrier_result_boundary_v2_failed_check_count",),
            ("selected_second_carrier_result_boundary_v2_basis",),
            ("failed_check_count",),
        )
    )

    return [
        _check(
            "second_carrier_success_basis_declared",
            _basis_declared(request, "selected_second_carrier_success_basis"),
            "declared selected second-carrier success basis",
            request.get("selected_second_carrier_success_basis"),
            "SECOND_CARRIER_SUCCESS_BASIS_MISSING",
        ),
        _check(
            "second_carrier_success_outcome_recorded",
            success_outcome == EXPECTED_SECOND_CARRIER_SUCCESS_OUTCOME,
            EXPECTED_SECOND_CARRIER_SUCCESS_OUTCOME,
            success_outcome,
            "SECOND_CARRIER_SUCCESS_NOT_RECORDED",
        ),
        _check(
            "second_carrier_success_version_0_1_0",
            success_version == EXPECTED_SECOND_CARRIER_SUCCESS_VERSION,
            EXPECTED_SECOND_CARRIER_SUCCESS_VERSION,
            success_version,
            "SECOND_CARRIER_SUCCESS_VERSION_NOT_0_1_0",
        ),
        _check(
            "second_carrier_success_failed_checks_zero",
            success_failed_count == 0,
            0,
            success_failed_count,
            "SECOND_CARRIER_SUCCESS_FAILED_CHECKS_PRESENT",
        ),
        _check(
            "second_carrier_success_recorded_bounded_success",
            _as_bool(
                _lookup(
                    request,
                    ("selected_second_carrier_success_bounded_success_recorded",),
                    ("selected_second_carrier_success_basis",),
                    (
                        "bounded_second_carrier_success_recorded",
                        "second_carrier_success_recorded",
                    ),
                )
            ),
            True,
            _lookup(
                request,
                ("selected_second_carrier_success_bounded_success_recorded",),
                ("selected_second_carrier_success_basis",),
                ("bounded_second_carrier_success_recorded",),
            ),
            "SECOND_CARRIER_SUCCESS_DID_NOT_RECORD_BOUNDED_SUCCESS",
        ),
        _check_false_shortcut(
            request,
            "second_carrier_success_did_not_already_create_verification",
            "selected_second_carrier_success_already_created_verification",
            "SECOND_CARRIER_SUCCESS_ALREADY_CREATED_VERIFICATION",
        ),
        _check_false_shortcut(
            request,
            "second_carrier_success_did_not_already_create_external_result",
            "selected_second_carrier_success_already_created_external_result",
            "SECOND_CARRIER_SUCCESS_ALREADY_CREATED_EXTERNAL_RESULT",
        ),
        _check_false_shortcut(
            request,
            "second_carrier_success_did_not_already_create_cross_carrier_evidence",
            "selected_second_carrier_success_already_created_cross_carrier_evidence",
            "SECOND_CARRIER_SUCCESS_ALREADY_CREATED_CROSS_CARRIER_EVIDENCE",
        ),
        _check_false_shortcut(
            request,
            "second_carrier_success_did_not_already_create_portable_verification_closure",
            "selected_second_carrier_success_already_created_portable_verification_closure",
            "SECOND_CARRIER_SUCCESS_ALREADY_CREATED_PORTABLE_VERIFICATION_CLOSURE",
        ),
        _check_false_shortcut(
            request,
            "second_carrier_success_did_not_treat_success_as_verification",
            "selected_second_carrier_success_treated_success_as_verification",
            "SECOND_CARRIER_SUCCESS_TREATED_SUCCESS_AS_VERIFICATION",
        ),
        _check_false_shortcut(
            request,
            "second_carrier_success_did_not_treat_success_as_external_result",
            "selected_second_carrier_success_treated_success_as_external_result",
            "SECOND_CARRIER_SUCCESS_TREATED_SUCCESS_AS_EXTERNAL_RESULT",
        ),
        _check_false_shortcut(
            request,
            "second_carrier_success_did_not_treat_success_as_cross_carrier_evidence",
            "selected_second_carrier_success_treated_success_as_cross_carrier_evidence",
            "SECOND_CARRIER_SUCCESS_TREATED_SUCCESS_AS_CROSS_CARRIER_EVIDENCE",
        ),
        _check_false_shortcut(
            request,
            "second_carrier_success_did_not_treat_success_as_portable_verification_closure",
            "selected_second_carrier_success_treated_success_as_portable_verification_closure",
            "SECOND_CARRIER_SUCCESS_TREATED_SUCCESS_AS_PORTABLE_VERIFICATION_CLOSURE",
        ),
        _check_true_shortcut(
            request,
            "second_carrier_success_kept_zero_exit_code_not_verification",
            "selected_second_carrier_success_zero_exit_code_not_verification",
            "SECOND_CARRIER_SUCCESS_TREATED_ZERO_EXIT_CODE_AS_VERIFICATION",
        ),
        _check_true_shortcut(
            request,
            "second_carrier_success_kept_ok_not_verification",
            "selected_second_carrier_success_ok_not_verification",
            "SECOND_CARRIER_SUCCESS_TREATED_OK_AS_VERIFICATION",
        ),
        _check_true_shortcut(
            request,
            "second_carrier_success_kept_ran_7_tests_not_cross_carrier_proof",
            "selected_second_carrier_success_ran_7_tests_not_cross_carrier_proof",
            "SECOND_CARRIER_SUCCESS_TREATED_RAN_7_TESTS_AS_CROSS_CARRIER_PROOF",
        ),
        _check_true_shortcut(
            request,
            "second_carrier_success_kept_returned_capture_not_cross_carrier_proof",
            "selected_second_carrier_success_returned_capture_not_cross_carrier_proof",
            "SECOND_CARRIER_SUCCESS_TREATED_RETURNED_CAPTURE_AS_CROSS_CARRIER_PROOF",
        ),
        _check(
            "second_carrier_success_kept_official_enum_scope_strings_unredacted",
            request.get("selected_second_carrier_success_official_enum_scope_strings_redacted")
            is False,
            False,
            request.get("selected_second_carrier_success_official_enum_scope_strings_redacted"),
            "SECOND_CARRIER_SUCCESS_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
        ),
        _check_true_shortcut(
            request,
            "second_carrier_success_preserved_first_success_boundary_test_failure",
            "selected_second_carrier_success_first_success_boundary_test_failure_preserved",
            "FIRST_SUCCESS_BOUNDARY_TEST_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
        ),
        _check(
            "second_carrier_success_boundary_basis_declared",
            _basis_declared(request, "selected_second_carrier_success_boundary_basis"),
            "declared selected second-carrier success boundary basis",
            request.get("selected_second_carrier_success_boundary_basis"),
            "SECOND_CARRIER_SUCCESS_BOUNDARY_BASIS_MISSING",
        ),
        _check(
            "second_carrier_success_boundary_outcome_recorded",
            success_boundary_outcome == EXPECTED_SECOND_CARRIER_SUCCESS_BOUNDARY_OUTCOME,
            EXPECTED_SECOND_CARRIER_SUCCESS_BOUNDARY_OUTCOME,
            success_boundary_outcome,
            "SECOND_CARRIER_SUCCESS_BOUNDARY_NOT_RECORDED",
        ),
        _check(
            "second_carrier_success_boundary_failed_checks_zero",
            success_boundary_failed == 0,
            0,
            success_boundary_failed,
            "SECOND_CARRIER_SUCCESS_BOUNDARY_FAILED_CHECKS_PRESENT",
        ),
        _check(
            "second_carrier_result_basis_declared",
            _basis_declared(request, "selected_second_carrier_result_basis"),
            "declared selected second-carrier result basis",
            request.get("selected_second_carrier_result_basis"),
            "SECOND_CARRIER_RESULT_BASIS_MISSING",
        ),
        _check(
            "second_carrier_result_outcome_recorded",
            result_outcome == EXPECTED_SECOND_CARRIER_RESULT_OUTCOME,
            EXPECTED_SECOND_CARRIER_RESULT_OUTCOME,
            result_outcome,
            "SECOND_CARRIER_RESULT_NOT_RECORDED",
        ),
        _check(
            "second_carrier_result_version_0_1_0",
            result_version == EXPECTED_SECOND_CARRIER_RESULT_VERSION,
            EXPECTED_SECOND_CARRIER_RESULT_VERSION,
            result_version,
            "SECOND_CARRIER_RESULT_VERSION_NOT_0_1_0",
        ),
        _check(
            "second_carrier_result_failed_checks_zero",
            result_failed == 0,
            0,
            result_failed,
            "SECOND_CARRIER_RESULT_FAILED_CHECKS_PRESENT",
        ),
        _check_true_shortcut(
            request,
            "second_carrier_result_recorded_bounded_result",
            "selected_second_carrier_result_bounded_result_recorded",
            "SECOND_CARRIER_RESULT_NOT_RECORDED",
        ),
        _check(
            "second_carrier_result_boundary_v2_basis_declared",
            _basis_declared(request, "selected_second_carrier_result_boundary_v2_basis"),
            "declared selected second-carrier result boundary v2 basis",
            request.get("selected_second_carrier_result_boundary_v2_basis"),
            "SECOND_CARRIER_RESULT_BOUNDARY_V2_BASIS_MISSING",
        ),
        _check(
            "second_carrier_result_boundary_v2_outcome_recorded",
            result_boundary_v2_outcome == EXPECTED_SECOND_CARRIER_RESULT_BOUNDARY_V2_OUTCOME,
            EXPECTED_SECOND_CARRIER_RESULT_BOUNDARY_V2_OUTCOME,
            result_boundary_v2_outcome,
            "SECOND_CARRIER_RESULT_BOUNDARY_V2_NOT_RECORDED",
        ),
        _check(
            "second_carrier_result_boundary_v2_failed_checks_zero",
            result_boundary_v2_failed == 0,
            0,
            result_boundary_v2_failed,
            "SECOND_CARRIER_RESULT_BOUNDARY_V2_FAILED_CHECKS_PRESENT",
        ),
    ]


def _check_false_shortcut(
    request: Mapping[str, Any], name: str, field: str, code: str
) -> dict[str, Any]:
    value = request.get(field)
    return _check(name, value is False, False, value, code)


def _check_true_shortcut(
    request: Mapping[str, Any], name: str, field: str, code: str
) -> dict[str, Any]:
    value = request.get(field)
    return _check(name, _as_bool(value), True, value, code)


def _returned_capture_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    output_capture_outcome = _lookup(
        request,
        ("selected_second_carrier_output_capture_result_outcome",),
        ("selected_second_carrier_output_capture_basis",),
        ("outcome", "result_outcome"),
    )
    output_capture_failed = _as_int(
        _lookup(
            request,
            ("selected_second_carrier_output_capture_failed_check_count",),
            ("selected_second_carrier_output_capture_basis",),
            ("failed_check_count",),
        )
    )
    return [
        _check(
            "returned_capture_intake_basis_declared",
            _basis_declared(request, "selected_returned_second_carrier_live_capture_intake_basis"),
            "declared returned second-carrier live capture intake basis",
            request.get("selected_returned_second_carrier_live_capture_intake_basis"),
            "RETURNED_CAPTURE_INTAKE_BASIS_MISSING",
        ),
        _check_true_shortcut(
            request,
            "returned_capture_intake_preserved",
            "selected_returned_capture_intake_preserved",
            "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
        ),
        _check_true_shortcut(
            request,
            "returned_capture_intake_capture_only",
            "selected_returned_capture_intake_capture_only",
            "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
        ),
        _check_true_shortcut(
            request,
            "returned_capture_from_macbook_pro_to_macbook_air_preserved",
            "selected_returned_capture_from_macbook_pro_to_macbook_air",
            "RECEIVING_CARRIER_TREATED_AS_AUTHORITY",
        ),
        _check_present(
            request,
            "returned_capture_material_basis_declared",
            "selected_returned_capture_material_basis",
            "RETURNED_CAPTURE_MATERIAL_MISSING",
        ),
        _check_present(
            request,
            "returned_zip_path_declared",
            "selected_returned_capture_zip_path",
            "RETURNED_ZIP_PATH_MISSING",
        ),
        _check_present(
            request,
            "returned_hash_path_declared",
            "selected_returned_capture_hash_path",
            "RETURNED_HASH_PATH_MISSING",
        ),
        _check_present(
            request,
            "returned_extracted_directory_declared",
            "selected_returned_capture_extracted_directory_path",
            "RETURNED_EXTRACTED_DIRECTORY_MISSING",
        ),
        _check_present(
            request,
            "returned_combined_terminal_log_declared",
            "selected_returned_capture_combined_terminal_log_path",
            "RETURNED_COMBINED_TERMINAL_LOG_MISSING",
        ),
        _check_present(
            request,
            "returned_exit_code_declared",
            "selected_returned_capture_exit_code",
            "RETURNED_EXIT_CODE_MISSING",
        ),
        _check_present(
            request,
            "returned_command_text_declared",
            "selected_returned_capture_command_text",
            "RETURNED_COMMAND_TEXT_MISSING",
        ),
        _check(
            "returned_timestamps_declared",
            bool(request.get("selected_returned_capture_started_at"))
            and bool(request.get("selected_returned_capture_completed_at")),
            "started and completed timestamps declared",
            {
                "started_at": request.get("selected_returned_capture_started_at"),
                "completed_at": request.get("selected_returned_capture_completed_at"),
            },
            "RETURNED_TIMESTAMPS_MISSING",
        ),
        _check_true_shortcut(
            request,
            "placeholder_carrier_fields_unrepaired",
            "selected_returned_capture_placeholder_fields_unrepaired",
            "PLACEHOLDER_CARRIER_FIELDS_REPAIRED",
        ),
        _check(
            "second_carrier_output_capture_basis_declared",
            _basis_declared(request, "selected_second_carrier_output_capture_basis"),
            "declared selected second-carrier output capture basis",
            request.get("selected_second_carrier_output_capture_basis"),
            "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_MISSING",
        ),
        _check(
            "second_carrier_output_capture_outcome_recorded",
            output_capture_outcome == EXPECTED_SECOND_CARRIER_OUTPUT_CAPTURE_OUTCOME,
            EXPECTED_SECOND_CARRIER_OUTPUT_CAPTURE_OUTCOME,
            output_capture_outcome,
            "SECOND_CARRIER_OUTPUT_CAPTURE_NOT_RECORDED",
        ),
        _check(
            "second_carrier_output_capture_failed_checks_zero",
            output_capture_failed == 0,
            0,
            output_capture_failed,
            "SECOND_CARRIER_OUTPUT_CAPTURE_FAILED_CHECKS_PRESENT",
        ),
    ]


def _check_present(
    request: Mapping[str, Any], name: str, field: str, code: str
) -> dict[str, Any]:
    value = request.get(field)
    return _check(name, value not in (None, "", {}, []), "present", value, code)


def _selected_basis_presence_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    for basis_key in (
        "selected_second_carrier_success_terminal_summary_basis",
        "selected_second_carrier_success_boundary_terminal_summary_basis",
        "selected_second_carrier_result_terminal_summary_basis",
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
    ):
        checks.append(
            _check(
                f"{basis_key}_declared",
                _basis_declared(request, basis_key),
                "declared reference-shaped selected basis",
                request.get(basis_key),
                "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
            )
        )
    return checks


def _posture_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    code_by_posture = {
        "verification_not_created_posture": "VERIFICATION_CREATED",
        "verification_boundary_not_verification_posture": (
            "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_VERIFICATION"
        ),
        "success_not_verification_posture": "SECOND_CARRIER_SUCCESS_TREATED_SUCCESS_AS_VERIFICATION",
        "success_not_external_result_posture": (
            "SECOND_CARRIER_SUCCESS_TREATED_SUCCESS_AS_EXTERNAL_RESULT"
        ),
        "zero_exit_code_not_verification_posture": "ZERO_EXIT_CODE_TREATED_AS_VERIFICATION",
        "ok_output_not_verification_posture": "OK_OUTPUT_TREATED_AS_VERIFICATION",
        "ran_7_tests_not_cross_carrier_proof_posture": (
            "RAN_7_TESTS_TREATED_AS_CROSS_CARRIER_PROOF"
        ),
        "returned_capture_not_cross_carrier_proof_posture": (
            "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_PROOF"
        ),
        "external_result_not_created_posture": "EXTERNAL_RESULT_CREATED",
        "cross_carrier_evidence_not_created_posture": "CROSS_CARRIER_EVIDENCE_CREATED",
        "portable_verification_closure_not_created_posture": (
            "PORTABLE_VERIFICATION_CLOSURE_CREATED"
        ),
        "verification_not_source_transfer_posture": (
            "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_SOURCE_TRANSFER"
        ),
        "verification_not_source_receipt_posture": (
            "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_SOURCE_RECEIPT"
        ),
        "verification_not_reception_authorization_posture": (
            "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION"
        ),
        "receiving_carrier_not_authority_posture": "RECEIVING_CARRIER_TREATED_AS_AUTHORITY",
        "source_not_created_posture": "SOURCE_CREATED",
        "authority_not_created_posture": "AUTHORITY_CREATED",
        "currentness_not_created_posture": "CURRENTNESS_CREATED",
        "final_completion_not_created_posture": "FINAL_COMPLETION_CLAIMED",
        "runtime_not_created_posture": "RUNTIME_HOSTING_CREATED",
        "continuation_not_authorized_posture": "CONTINUATION_AUTHORIZED",
        "reusable_permission_not_created_posture": "REUSABLE_PERMISSION_CREATED",
        "follow_on_work_not_authorized_posture": "FOLLOW_ON_WORK_AUTHORIZED",
        "repo_local_availability_not_verification_authority_posture": (
            "REPO_LOCAL_AVAILABILITY_TREATED_AS_VERIFICATION_AUTHORITY"
        ),
        "raw_full_prior_artifact_body_not_returned_posture": (
            "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED"
        ),
        "first_success_boundary_test_failure_preserved_posture": (
            "FIRST_SUCCESS_BOUNDARY_TEST_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED"
        ),
        "first_result_boundary_resolver_failure_preserved_posture": (
            "FIRST_RESULT_BOUNDARY_RESOLVER_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED"
        ),
    }
    checks: list[dict[str, Any]] = []
    for posture_key in POSTURE_KEYS:
        checks.append(
            _check(
                f"{posture_key}_declared",
                _as_bool(request.get(posture_key)),
                "declared posture",
                request.get(posture_key),
                code_by_posture.get(posture_key, "SELECTED_BASIS_NOT_REFERENCE_SHAPED"),
            )
        )
    return checks


def _non_claim_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    declared = request.get("declared_non_claims")
    if not isinstance(declared, Mapping):
        declared = {}
    checks: list[dict[str, Any]] = []
    for non_claim in REQUIRED_FALSE_NON_CLAIMS:
        actual = declared.get(non_claim)
        checks.append(
            _check(
                f"non_claim_{non_claim}_false",
                actual is False,
                False,
                actual,
                NON_CLAIM_BLOCK_CODE.get(non_claim, "NON_CLAIM_MISSING_OR_FLIPPED"),
            )
        )
    return checks


def _first_failed_code(checks: Sequence[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is not True:
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str):
                return code
    return None


def _statement_for_outcome(outcome: str) -> dict[str, bool]:
    recorded = outcome == OUTCOME_RECORDED
    return {key: recorded for key in ALLOWED_TRUE_RECORDED_FIELDS}


def _non_meaning() -> dict[str, bool]:
    return {
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
        "verification_boundary_became_verification": False,
        "verification_boundary_became_external_result": False,
        "verification_boundary_became_cross_carrier_proof": False,
        "verification_boundary_became_portable_verification_closure": False,
        "verification_boundary_became_source_transfer_source_receipt_or_reception": False,
        "verification_boundary_became_source_authority_or_currentness": False,
        "success_became_verification": False,
        "success_became_external_result": False,
        "zero_exit_code_became_verification": False,
        "ok_became_verification_by_itself": False,
        "ran_7_tests_became_cross_carrier_proof": False,
        "returned_capture_became_proof": False,
        "macbook_pro_became_authority": False,
        "macbook_air_became_source": False,
        "artifact_existence_became_verification_authority": False,
        "artifact_path_became_currentness": False,
        "repo_local_availability_became_verification_authority": False,
        "hidden_repo_state_became_verification_authority": False,
        "first_success_boundary_test_repaired_hidden_erased_or_claimed_passed": False,
        "first_result_boundary_resolver_repaired_hidden_erased_or_claimed_passed": False,
        "v1_packet_emission_boundary_repaired_hidden_erased_or_claimed_passed": False,
    }


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "second-carrier verification boundary test",
            "second-carrier verification boundary live artifact",
            "second-carrier verification boundary terminal summary, if needed",
            "second-carrier verification spec/resolver/test/live artifact, if admitted",
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


def _additional_basis(outcome: str, request: Mapping[str, Any]) -> dict[str, Any]:
    required = outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    return {
        "additional_basis_required": required,
        "missing_or_unclear_basis": _sanitize(
            request.get("additional_basis_context", []), key="additional_basis_context"
        )
        if required
        else [],
        "missing_basis_scheduled": False,
        "missing_basis_authorized": False,
        "missing_basis_executed": False,
    }


def _not_recorded(outcome: str, request: Mapping[str, Any]) -> dict[str, Any]:
    not_recorded = outcome == OUTCOME_NOT_RECORDED
    return {
        "not_recorded": not_recorded,
        "not_recorded_basis": _sanitize(
            request.get("not_recorded_basis", []), key="not_recorded_basis"
        )
        if not_recorded
        else [],
        "verification_created": False,
        "external_result_created": False,
        "cross_carrier_evidence_created": False,
        "portable_verification_closure_created": False,
        "source_authority_currentness_final_completion_runtime_or_follow_on_created": False,
        "mutation_performed": False,
    }


def resolve_portable_source_body_verification_second_carrier_verification_boundary(
    declared_second_carrier_verification_boundary_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded second-carrier verification-boundary posture."""

    if declared_second_carrier_verification_boundary_request is None:
        return _blocked_malformed_result(
            {},
            "DECLARED_SECOND_CARRIER_VERIFICATION_BOUNDARY_REQUEST_MALFORMED",
            "declared second-carrier verification-boundary request is missing",
        )
    if not isinstance(declared_second_carrier_verification_boundary_request, Mapping):
        return _blocked_malformed_result(
            {},
            "DECLARED_SECOND_CARRIER_VERIFICATION_BOUNDARY_REQUEST_MALFORMED",
            "declared second-carrier verification-boundary request must be a mapping",
        )

    request = copy.deepcopy(dict(declared_second_carrier_verification_boundary_request))
    checks = _build_checks(request)

    intent = request.get("second_carrier_verification_boundary_intent")
    requested_outcome = request.get("requested_second_carrier_verification_boundary_outcome")
    failed_code = _first_failed_code(checks)
    block_code: str | None = None
    block_reason: str | None = None

    if intent == INTENT_BLOCK:
        outcome = OUTCOME_BLOCKED
        block_code = _declared_block_code(request, "SECOND_CARRIER_VERIFICATION_BOUNDARY_BLOCK_REQUESTED")
        block_reason = str(request.get("block_reason") or "declared request asked to block")
    elif failed_code is not None:
        outcome = OUTCOME_BLOCKED
        block_code = failed_code
        block_reason = str(request.get("block_reason") or f"check failed: {failed_code}")
    elif intent == INTENT_DO_NOT_RECORD or requested_outcome == OUTCOME_NOT_RECORDED:
        outcome = OUTCOME_NOT_RECORDED
    elif requested_outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS or request.get(
        "additional_basis_context"
    ):
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
    else:
        outcome = OUTCOME_RECORDED

    return _build_result(request, checks, outcome, block_code, block_reason)


def resolve_portable_source_body_verification_second_carrier_verification_boundary_from_path(
    declared_second_carrier_verification_boundary_request_path: Path | str,
) -> dict[str, Any]:
    """Load a declared request JSON object and resolve it."""

    path = Path(declared_second_carrier_verification_boundary_request_path)
    try:
        raw_text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise PortableSourceBodyVerificationSecondCarrierVerificationBoundaryError(
            f"declared request path is unreadable: {path}"
        ) from exc
    try:
        data = json.loads(raw_text)
    except json.JSONDecodeError as exc:
        raise PortableSourceBodyVerificationSecondCarrierVerificationBoundaryError(
            f"declared request path does not contain valid JSON: {path}"
        ) from exc
    if not isinstance(data, Mapping):
        raise PortableSourceBodyVerificationSecondCarrierVerificationBoundaryError(
            f"declared request path must contain a JSON object: {path}"
        )
    return resolve_portable_source_body_verification_second_carrier_verification_boundary(data)


def _declared_block_code(request: Mapping[str, Any], fallback: str) -> str:
    value = request.get("block_reason")
    if isinstance(value, str) and value in BLOCK_CODES:
        return value
    value = request.get("block_code")
    if isinstance(value, str) and value in BLOCK_CODES:
        return value
    return fallback


def _blocked_malformed_result(
    request: Mapping[str, Any], block_code: str, reason: str
) -> dict[str, Any]:
    checks = [
        _check(
            "declared_second_carrier_verification_boundary_request_malformed",
            False,
            "mapping JSON object",
            reason,
            block_code,
        )
    ]
    return _build_result(request, checks, OUTCOME_BLOCKED, block_code, reason)


def _build_result(
    request: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    outcome: str,
    block_code: str | None,
    block_reason: str | None,
) -> dict[str, Any]:
    request_id = _request_id(request)
    statement = _statement_for_outcome(outcome)
    result: dict[str, Any] = {
        "portable_source_body_verification_second_carrier_verification_boundary_metadata": {
            "portable_source_body_verification_second_carrier_verification_boundary_result_id": request_id,
            "portable_source_body_verification_second_carrier_verification_boundary_result_type": RESULT_TYPE,
            "portable_source_body_verification_second_carrier_verification_boundary_result_version": RESULT_VERSION,
            "generated_at": _now(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_second_carrier_verification_boundary_question": {
            "second_carrier_verification_boundary_request_id": request_id,
            "second_carrier_verification_boundary_question": _sanitize(
                request.get("second_carrier_verification_boundary_question")
            ),
            "second_carrier_verification_boundary_intent": _sanitize(
                request.get("second_carrier_verification_boundary_intent")
            ),
        },
    }

    for basis_key in SELECTED_BASIS_KEYS:
        result[basis_key] = _reference_basis_section(request, basis_key)
    for posture_key in POSTURE_KEYS:
        result[posture_key] = _posture_section(request, posture_key)

    result["second_carrier_verification_boundary_scope"] = _sanitize(_scope_values(request))
    result["second_carrier_verification_boundary_checks"] = _json_safe(checks)
    result["second_carrier_verification_boundary_statement"] = statement
    result["second_carrier_verification_boundary_non_meaning"] = _non_meaning()
    result["additional_basis_required"] = _additional_basis(outcome, request)
    result["not_recorded_basis"] = _not_recorded(outcome, request)
    result["what_remains_open"] = _what_remains_open()
    result["non_claims"] = _false_non_claims()
    result["outcome"] = outcome
    result["block"] = None
    if outcome == OUTCOME_BLOCKED:
        result["block"] = {
            "block_code": block_code,
            "block_reason": _sanitize(block_reason, key="block_reason"),
        }

    result["portable_source_body_verification_second_carrier_verification_boundary_summary"] = (
        build_portable_source_body_verification_second_carrier_verification_boundary_summary(
            result
        )
    )
    return result


def build_portable_source_body_verification_second_carrier_verification_boundary_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact summary for a second-carrier verification-boundary result."""

    metadata = result.get(
        "portable_source_body_verification_second_carrier_verification_boundary_metadata", {}
    )
    declared = result.get("declared_second_carrier_verification_boundary_question", {})
    checks = result.get("second_carrier_verification_boundary_checks", [])
    statement = result.get("second_carrier_verification_boundary_statement", {})
    non_claims = result.get("non_claims", {})
    block = result.get("block")
    passed_count = sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed") is True)
    failed_count = sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed") is not True)
    capture_basis = result.get("selected_returned_capture_material_basis", {})
    success_basis = result.get("selected_second_carrier_success_basis", {})
    success_boundary_basis = result.get("selected_second_carrier_success_boundary_basis", {})
    carrier_result_basis = result.get("selected_second_carrier_result_basis", {})

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") if isinstance(block, Mapping) else None,
        "block_reason": block.get("block_reason") if isinstance(block, Mapping) else None,
        "request_id": declared.get("second_carrier_verification_boundary_request_id"),
        "question": declared.get("second_carrier_verification_boundary_question"),
        "intent": declared.get("second_carrier_verification_boundary_intent"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": metadata.get(
            "portable_source_body_verification_second_carrier_verification_boundary_result_version"
        ),
        "resolver_module": metadata.get("resolver_module"),
        "second_carrier_verification_boundary_recorded": statement.get(
            "second_carrier_verification_boundary_recorded", False
        ),
        "one_future_second_carrier_verification_step_declared": statement.get(
            "one_future_second_carrier_verification_step_declared", False
        ),
        "second_carrier_success_basis_preserved": statement.get(
            "second_carrier_success_basis_preserved", False
        ),
        "second_carrier_success_boundary_basis_preserved": statement.get(
            "second_carrier_success_boundary_basis_preserved", False
        ),
        "second_carrier_result_basis_preserved": statement.get(
            "second_carrier_result_basis_preserved", False
        ),
        "returned_second_carrier_capture_basis_preserved": statement.get(
            "returned_second_carrier_capture_basis_preserved", False
        ),
        "capture_intake_basis_preserved": statement.get("capture_intake_basis_preserved", False),
        "second_carrier_output_capture_basis_preserved": statement.get(
            "second_carrier_output_capture_basis_preserved", False
        ),
        "success_artifact_basis_preserved": statement.get(
            "success_artifact_basis_preserved", False
        ),
        "verification_not_created": statement.get("verification_not_created", False),
        "verification_boundary_not_verification": statement.get(
            "verification_boundary_not_verification", False
        ),
        "success_not_verification": statement.get("success_not_verification", False),
        "success_not_external_result": statement.get("success_not_external_result", False),
        "zero_exit_code_not_verification": statement.get("zero_exit_code_not_verification", False),
        "ok_output_not_verification": statement.get("ok_output_not_verification", False),
        "ran_7_tests_not_cross_carrier_proof": statement.get(
            "ran_7_tests_not_cross_carrier_proof", False
        ),
        "returned_capture_not_cross_carrier_proof": statement.get(
            "returned_capture_not_cross_carrier_proof", False
        ),
        "external_result_not_created": statement.get("external_result_not_created", False),
        "cross_carrier_evidence_not_created": statement.get(
            "cross_carrier_evidence_not_created", False
        ),
        "portable_verification_closure_not_created": statement.get(
            "portable_verification_closure_not_created", False
        ),
        "verification_not_source_transfer": statement.get(
            "verification_not_source_transfer", False
        ),
        "verification_not_source_receipt": statement.get(
            "verification_not_source_receipt", False
        ),
        "verification_not_reception_authorization": statement.get(
            "verification_not_reception_authorization", False
        ),
        "receiving_carrier_not_authority": statement.get(
            "receiving_carrier_not_authority", False
        ),
        "source_not_created": statement.get("source_not_created", False),
        "authority_not_created": statement.get("authority_not_created", False),
        "currentness_not_created": statement.get("currentness_not_created", False),
        "final_completion_not_created": statement.get("final_completion_not_created", False),
        "runtime_not_created": statement.get("runtime_not_created", False),
        "follow_on_work_not_authorized": statement.get("follow_on_work_not_authorized", False),
        "hidden_repo_state_excluded": statement.get("hidden_repo_state_excluded", False),
        "hidden_repo_state_not_used_as_verification_authority": statement.get(
            "hidden_repo_state_not_used_as_verification_authority", False
        ),
        "repo_local_availability_not_verification_authority": statement.get(
            "repo_local_availability_not_verification_authority", False
        ),
        "selected_basis_reference_shape_preserved": statement.get(
            "selected_basis_reference_shape_preserved", False
        ),
        "raw_full_prior_artifact_body_not_returned": statement.get(
            "raw_full_prior_artifact_body_not_returned", False
        ),
        "official_enum_scope_strings_not_redacted": statement.get(
            "official_enum_scope_strings_not_redacted", False
        ),
        "hostile_raw_body_content_contained": statement.get(
            "hostile_raw_body_content_contained", False
        ),
        "selected_second_carrier_success_outcome": _summary_shortcut(
            success_basis, "selected_second_carrier_success_result_outcome"
        ),
        "selected_second_carrier_success_version": _summary_shortcut(
            success_basis, "selected_second_carrier_success_result_version"
        ),
        "selected_second_carrier_success_failed_check_count": _summary_shortcut(
            success_basis, "selected_second_carrier_success_failed_check_count"
        ),
        "selected_second_carrier_success_boundary_outcome": _summary_shortcut(
            success_boundary_basis, "selected_second_carrier_success_boundary_result_outcome"
        ),
        "selected_second_carrier_success_boundary_failed_check_count": _summary_shortcut(
            success_boundary_basis,
            "selected_second_carrier_success_boundary_failed_check_count",
        ),
        "selected_second_carrier_result_outcome": _summary_shortcut(
            carrier_result_basis, "selected_second_carrier_result_result_outcome"
        ),
        "selected_second_carrier_result_version": _summary_shortcut(
            carrier_result_basis, "selected_second_carrier_result_result_version"
        ),
        "selected_second_carrier_result_failed_check_count": _summary_shortcut(
            carrier_result_basis, "selected_second_carrier_result_failed_check_count"
        ),
        "selected_returned_capture_intake_path": _summary_shortcut(
            capture_basis, "selected_returned_capture_intake_path"
        ),
        "selected_returned_capture_zip_path": _summary_shortcut(
            capture_basis, "selected_returned_capture_zip_path"
        ),
        "selected_returned_capture_hash_path": _summary_shortcut(
            capture_basis, "selected_returned_capture_hash_path"
        ),
        "selected_returned_capture_extracted_directory_path": _summary_shortcut(
            capture_basis, "selected_returned_capture_extracted_directory_path"
        ),
        "selected_returned_capture_exit_code": _summary_shortcut(
            capture_basis, "selected_returned_capture_exit_code"
        ),
        "selected_returned_capture_ok_line": _summary_shortcut(
            capture_basis, "selected_returned_capture_ok_line"
        ),
        "no_verification_external_result_cross_carrier_evidence_or_portable_closure": (
            non_claims.get("verification_created") is False
            and non_claims.get("external_result_created") is False
            and non_claims.get("cross_carrier_evidence_created") is False
            and non_claims.get("portable_verification_closure_created") is False
        ),
        "no_source_authority_currentness_final_completion_runtime_or_follow_on": (
            non_claims.get("source_created") is False
            and non_claims.get("authority_created") is False
            and non_claims.get("currentness_created") is False
            and non_claims.get("final_completion_claimed") is False
            and non_claims.get("runtime_hosting_created") is False
            and non_claims.get("follow_on_work_authorized") is False
        ),
        "no_deployment_public_release_or_follow_on": (
            non_claims.get("deployment_created") is False
            and non_claims.get("public_release_created") is False
            and non_claims.get("follow_on_work_authorized") is False
        ),
        "key_non_claims": {
            key: non_claims.get(key)
            for key in (
                "verification_created",
                "external_result_created",
                "cross_carrier_evidence_created",
                "portable_verification_closure_created",
                "source_transfer_occurred",
                "source_receipt_occurred",
                "reception_authorization_created",
                "authorization_token_reused",
                "consumed_request_reopened",
            )
        },
        "first_success_boundary_test_preserved_as_failed_predecessor": statement.get(
            "first_success_boundary_test_failure_preserved", False
        ),
        "v1_predecessor_failure_preserved": (
            non_claims.get("v1_repaired") is False
            and non_claims.get("v1_hidden") is False
            and non_claims.get("v1_claimed_passed") is False
        ),
        "v1_not_repaired": non_claims.get("v1_repaired") is False,
        "v1_not_hidden": non_claims.get("v1_hidden") is False,
        "v1_not_claimed_passed": non_claims.get("v1_claimed_passed") is False,
        "first_result_boundary_resolver_preserved_as_failed_predecessor": statement.get(
            "first_result_boundary_resolver_failure_preserved", False
        ),
    }


def _summary_shortcut(section: Any, key: str) -> Any:
    if not isinstance(section, Mapping):
        return None
    shortcuts = section.get("selected_shortcut_fields")
    if isinstance(shortcuts, Mapping) and key in shortcuts:
        return shortcuts[key]
    selected = section.get("selected_basis")
    if isinstance(selected, Mapping) and key in selected:
        return selected[key]
    return None


def write_portable_source_body_verification_second_carrier_verification_boundary_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write a bounded result JSON artifact without overwriting existing files."""

    result_copy = _json_safe(result)
    metadata = result_copy.get(
        "portable_source_body_verification_second_carrier_verification_boundary_metadata", {}
    )
    if isinstance(metadata, Mapping):
        request_id = metadata.get(
            "portable_source_body_verification_second_carrier_verification_boundary_result_id"
        )
    else:
        request_id = None
    if not isinstance(request_id, str) or not request_id:
        request_id = "portable_source_body_verification_second_carrier_verification_boundary_request_001"

    if output_path is None:
        path = OUTPUT_ROOT / (
            f"{request_id}__portable_source_body_verification_second_carrier_"
            "verification_boundary_result.json"
        )
    else:
        path = Path(output_path)
        if path.exists() and path.is_dir():
            path = path / (
                f"{request_id}__portable_source_body_verification_second_carrier_"
                "verification_boundary_result.json"
            )
    path = _unused_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(result_copy, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return path


def _unused_path(path: Path) -> Path:
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


def build_declared_portable_source_body_verification_second_carrier_verification_boundary_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Build a valid declared request that records cleanly by default."""

    request_id = str(
        overrides.pop(
            "second_carrier_verification_boundary_request_id",
            "portable_source_body_verification_second_carrier_verification_boundary_reference_review_001",
        )
    )
    request: dict[str, Any] = {
        "second_carrier_verification_boundary_request_id": request_id,
        "second_carrier_verification_boundary_question": CORE_QUESTION,
        "second_carrier_verification_boundary_intent": INTENT_RECORD,
        "second_carrier_verification_boundary_scope": list(SUPPORTED_SCOPE_VALUES),
        "declared_non_claims": _false_non_claims(),
        "selected_second_carrier_success_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_"
            "verification_second_carrier_success/"
            "portable_source_body_verification_second_carrier_success_reference_review_001__"
            "portable_source_body_verification_second_carrier_success_result.json"
        ),
        "selected_second_carrier_success_result_outcome": EXPECTED_SECOND_CARRIER_SUCCESS_OUTCOME,
        "selected_second_carrier_success_result_version": EXPECTED_SECOND_CARRIER_SUCCESS_VERSION,
        "selected_second_carrier_success_failed_check_count": 0,
        "selected_second_carrier_success_bounded_success_recorded": True,
        "selected_second_carrier_success_already_created_verification": False,
        "selected_second_carrier_success_already_created_external_result": False,
        "selected_second_carrier_success_already_created_cross_carrier_evidence": False,
        "selected_second_carrier_success_already_created_portable_verification_closure": False,
        "selected_second_carrier_success_treated_success_as_verification": False,
        "selected_second_carrier_success_treated_success_as_external_result": False,
        "selected_second_carrier_success_treated_success_as_cross_carrier_evidence": False,
        "selected_second_carrier_success_treated_success_as_portable_verification_closure": False,
        "selected_second_carrier_success_zero_exit_code_not_verification": True,
        "selected_second_carrier_success_ok_not_verification": True,
        "selected_second_carrier_success_ran_7_tests_not_cross_carrier_proof": True,
        "selected_second_carrier_success_returned_capture_not_cross_carrier_proof": True,
        "selected_second_carrier_success_official_enum_scope_strings_redacted": False,
        "selected_second_carrier_success_first_success_boundary_test_failure_preserved": True,
        "selected_second_carrier_success_boundary_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_"
            "verification_second_carrier_success_boundary/"
            "portable_source_body_verification_second_carrier_success_boundary_reference_review_001__"
            "portable_source_body_verification_second_carrier_success_boundary_result.json"
        ),
        "selected_second_carrier_success_boundary_result_outcome": (
            EXPECTED_SECOND_CARRIER_SUCCESS_BOUNDARY_OUTCOME
        ),
        "selected_second_carrier_success_boundary_failed_check_count": 0,
        "selected_second_carrier_result_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_"
            "verification_second_carrier_result/"
            "portable_source_body_verification_second_carrier_result_reference_review_001__"
            "portable_source_body_verification_second_carrier_result.json"
        ),
        "selected_second_carrier_result_result_outcome": EXPECTED_SECOND_CARRIER_RESULT_OUTCOME,
        "selected_second_carrier_result_result_version": EXPECTED_SECOND_CARRIER_RESULT_VERSION,
        "selected_second_carrier_result_failed_check_count": 0,
        "selected_second_carrier_result_bounded_result_recorded": True,
        "selected_second_carrier_result_boundary_v2_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_"
            "verification_second_carrier_result_boundary_v2/"
            "portable_source_body_verification_second_carrier_result_boundary_reference_review_001_v2__"
            "portable_source_body_verification_second_carrier_result_boundary_v2_result.json"
        ),
        "selected_second_carrier_result_boundary_v2_result_outcome": (
            EXPECTED_SECOND_CARRIER_RESULT_BOUNDARY_V2_OUTCOME
        ),
        "selected_second_carrier_result_boundary_v2_failed_check_count": 0,
        "selected_returned_capture_intake_path": (
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_RETURNED_SECOND_CARRIER_LIVE_CAPTURE_INTAKE_V0.md"
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
            "python3 -m unittest "
            "tests/test_resolve_portable_source_body_verification_second_carrier_output_capture.py"
        ),
        "selected_returned_capture_working_directory": (
            "/Users/markomarkota/Desktop/IAMMAI-SYSTEM"
        ),
        "selected_returned_capture_started_at": "2026-05-09T11:34:26Z",
        "selected_returned_capture_completed_at": "2026-05-09T11:34:27Z",
        "selected_returned_capture_exit_code": 0,
        "selected_returned_capture_ran_7_tests_line": "Ran 7 tests in 0.451s",
        "selected_returned_capture_ok_line": "OK",
        "selected_returned_capture_raw_placeholder_carrier_label": (
            "SECOND_DEVICE_LABEL_TO_FILL"
        ),
        "selected_returned_capture_raw_placeholder_carrier_type": "Mac/Linux/etc_TO_FILL",
        "selected_returned_capture_placeholder_fields_unrepaired": True,
        "selected_second_carrier_output_capture_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_"
            "verification_second_carrier_output_capture/"
            "portable_source_body_verification_second_carrier_output_capture_reference_review_001__"
            "portable_source_body_verification_second_carrier_output_capture_result.json"
        ),
        "selected_second_carrier_output_capture_result_outcome": (
            EXPECTED_SECOND_CARRIER_OUTPUT_CAPTURE_OUTCOME
        ),
        "selected_second_carrier_output_capture_failed_check_count": 0,
        "reference_shaped_input_posture": True,
    }

    for basis_key in SELECTED_BASIS_KEYS:
        request[basis_key] = _builder_basis(basis_key)
    for posture_key in POSTURE_KEYS:
        request[posture_key] = {
            "declared": True,
            "posture_key": posture_key,
            "basis_only": True,
        }

    request.update(overrides)
    return request


def _builder_basis(label: str) -> dict[str, Any]:
    return {
        "basis_label": label,
        "declared": True,
        "basis_declared": True,
        "basis_reference": f"synthetic://{label}",
        "basis_reference_shape_preserved": True,
        "basis_only": True,
        "verification_created": False,
        "external_result_created": False,
        "cross_carrier_evidence_created": False,
        "portable_verification_closure_created": False,
        "source_authority_currentness_runtime_or_completion_created": False,
        "follow_on_work_authorized": False,
    }
