"""Resolve portable source-body verification second-carrier external-result boundary.

This resolver is downstream of the clean second-carrier verification line. It
may record that clean second-carrier verification basis is available for one
future second-carrier external-result step only. It does not create external
result, cross-carrier evidence, portable verification closure, source transfer,
source receipt, reception authorization, source, authority, currentness, final
completion, runtime, deployment, public release, continuation, reusable
permission, derivative reception, vessel relation, another reception request,
or follow-on work.

The module is self-contained, imports no repo-local modules, runs no
subprocesses, performs no network access, mutates no upstream artifact, and
keeps official enum, scope, outcome, block-code, posture, non-claim, and
boolean field strings unredacted while containing hostile raw body payloads.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class PortableSourceBodyVerificationSecondCarrierExternalResultBoundaryError(Exception):
    """Bounded resolver error for explicit unreadable or malformed inputs."""


RESOLVER_MODULE = (
    "resolve_portable_source_body_verification_second_carrier_external_result_boundary"
)
RESULT_TYPE = (
    "portable_source_body_verification_second_carrier_external_result_boundary_result"
)
RESULT_VERSION = "0.1.0"
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_portable_source_body_verification_"
    "second_carrier_external_result_boundary"
)

CORE_QUESTION = (
    "Can the clean second-carrier-verification basis be bounded for one future "
    "second-carrier external-result step without creating external result yet, "
    "cross-carrier evidence, portable verification closure, source transfer, "
    "source receipt, reception authorization, source, authority, currentness, "
    "runtime, final completion, continuation, reusable permission, derivative "
    "reception, vessel relation, another reception request, or follow-on work?"
)

OUTCOME_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_"
    "REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_BLOCKED"
)
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = (
    "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY"
)
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY"
)
INTENT_BLOCK = (
    "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY"
)
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

EXPECTED_SECOND_CARRIER_VERIFICATION_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_VERIFICATION_RECORDED"
)
EXPECTED_SECOND_CARRIER_VERIFICATION_BOUNDARY_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_VERIFICATION_BOUNDARY_RECORDED"
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
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_ONLY",
    "ONE_FUTURE_SECOND_CARRIER_EXTERNAL_RESULT_STEP_ONLY",
    "SECOND_CARRIER_VERIFICATION_BASIS_PRESERVED",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_BASIS_PRESERVED",
    "SECOND_CARRIER_SUCCESS_BASIS_PRESERVED",
    "SECOND_CARRIER_RESULT_BASIS_PRESERVED",
    "RETURNED_SECOND_CARRIER_CAPTURE_BASIS_PRESERVED",
    "CAPTURE_INTAKE_BASIS_PRESERVED",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_PRESERVED",
    "VERIFICATION_ARTIFACT_BASIS_PRESERVED",
    "EXTERNAL_RESULT_NOT_CREATED",
    "EXTERNAL_RESULT_BOUNDARY_NOT_EXTERNAL_RESULT",
    "VERIFICATION_NOT_EXTERNAL_RESULT",
    "VERIFICATION_NOT_CROSS_CARRIER_EVIDENCE",
    "ZERO_EXIT_CODE_NOT_EXTERNAL_RESULT",
    "STRING_ZERO_NOT_EXTERNAL_RESULT",
    "OK_OUTPUT_NOT_EXTERNAL_RESULT",
    "RAN_7_TESTS_NOT_CROSS_CARRIER_PROOF",
    "RETURNED_CAPTURE_NOT_CROSS_CARRIER_PROOF",
    "CROSS_CARRIER_EVIDENCE_NOT_CREATED",
    "PORTABLE_VERIFICATION_CLOSURE_NOT_CREATED",
    "EXTERNAL_RESULT_NOT_SOURCE_TRANSFER",
    "EXTERNAL_RESULT_NOT_SOURCE_RECEIPT",
    "EXTERNAL_RESULT_NOT_RECEPTION_AUTHORIZATION",
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
    "HIDDEN_REPO_STATE_NOT_USED_AS_EXTERNAL_RESULT_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_NOT_EXTERNAL_RESULT_AUTHORITY",
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
SUPPORTED_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_SCOPE = SUPPORTED_SCOPE_VALUES

SELECTED_BASIS_KEYS = (
    "selected_second_carrier_verification_basis",
    "selected_second_carrier_verification_terminal_summary_basis",
    "selected_second_carrier_verification_boundary_basis",
    "selected_second_carrier_verification_boundary_terminal_summary_basis",
    "selected_second_carrier_success_basis",
    "selected_second_carrier_success_terminal_summary_basis",
    "selected_second_carrier_result_basis",
    "selected_returned_second_carrier_live_capture_intake_basis",
    "selected_returned_capture_material_basis",
    "selected_second_carrier_output_capture_basis",
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
    "second_carrier_external_result_boundary_only_posture",
    "one_future_second_carrier_external_result_step_posture",
    "second_carrier_verification_basis_preserved_posture",
    "second_carrier_verification_boundary_basis_preserved_posture",
    "second_carrier_success_basis_preserved_posture",
    "second_carrier_result_basis_preserved_posture",
    "returned_second_carrier_capture_basis_preserved_posture",
    "capture_intake_basis_preserved_posture",
    "second_carrier_output_capture_basis_preserved_posture",
    "verification_artifact_basis_preserved_posture",
    "external_result_not_created_posture",
    "external_result_boundary_not_external_result_posture",
    "verification_not_external_result_posture",
    "verification_not_cross_carrier_evidence_posture",
    "zero_exit_code_not_external_result_posture",
    "string_zero_not_external_result_posture",
    "ok_output_not_external_result_posture",
    "ran_7_tests_not_cross_carrier_proof_posture",
    "returned_capture_not_cross_carrier_proof_posture",
    "cross_carrier_evidence_not_created_posture",
    "portable_verification_closure_not_created_posture",
    "external_result_not_source_transfer_posture",
    "external_result_not_source_receipt_posture",
    "external_result_not_reception_authorization_posture",
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
    "repo_local_availability_not_external_result_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "first_success_boundary_test_failure_preserved_posture",
    "first_result_boundary_resolver_failure_preserved_posture",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "second_carrier_external_result_boundary_recorded",
    "one_future_second_carrier_external_result_step_declared",
    "second_carrier_verification_basis_preserved",
    "second_carrier_verification_boundary_basis_preserved",
    "second_carrier_success_basis_preserved",
    "second_carrier_result_basis_preserved",
    "returned_second_carrier_capture_basis_preserved",
    "capture_intake_basis_preserved",
    "second_carrier_output_capture_basis_preserved",
    "verification_artifact_basis_preserved",
    "external_result_not_created",
    "external_result_boundary_not_external_result",
    "verification_not_external_result",
    "verification_not_cross_carrier_evidence",
    "zero_exit_code_not_external_result",
    "string_zero_not_external_result",
    "ok_output_not_external_result",
    "ran_7_tests_not_cross_carrier_proof",
    "returned_capture_not_cross_carrier_proof",
    "cross_carrier_evidence_not_created",
    "portable_verification_closure_not_created",
    "external_result_not_source_transfer",
    "external_result_not_source_receipt",
    "external_result_not_reception_authorization",
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
    "hidden_repo_state_not_used_as_external_result_authority",
    "repo_local_availability_not_external_result_authority",
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
    "external_result_created",
    "cross_carrier_evidence_created",
    "portable_verification_closure_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "second_carrier_external_result_boundary_treated_as_external_result",
    "second_carrier_external_result_boundary_treated_as_cross_carrier_evidence",
    "second_carrier_external_result_boundary_treated_as_portable_verification_closure",
    "second_carrier_external_result_boundary_treated_as_source_transfer",
    "second_carrier_external_result_boundary_treated_as_source_receipt",
    "second_carrier_external_result_boundary_treated_as_reception_authorization",
    "second_carrier_external_result_boundary_treated_as_source",
    "second_carrier_external_result_boundary_treated_as_authority",
    "second_carrier_external_result_boundary_treated_as_currentness",
    "second_carrier_external_result_boundary_treated_as_final_completion",
    "second_carrier_external_result_boundary_treated_as_runtime",
    "second_carrier_external_result_boundary_treated_as_continuation",
    "second_carrier_external_result_boundary_treated_as_reusable_permission",
    "second_carrier_external_result_boundary_treated_as_follow_on_work",
    "second_carrier_verification_treated_as_external_result",
    "second_carrier_verification_treated_as_cross_carrier_evidence",
    "zero_exit_code_treated_as_external_result",
    "string_zero_treated_as_external_result",
    "ok_output_treated_as_external_result",
    "ran_7_tests_treated_as_cross_carrier_proof",
    "returned_capture_treated_as_cross_carrier_evidence",
    "receiving_carrier_treated_as_authority",
    "artifact_existence_treated_as_external_result_authority",
    "artifact_path_treated_as_currentness",
    "repo_local_availability_treated_as_external_result_authority",
    "hidden_repo_state_used_as_external_result_content",
    "hidden_repo_state_used_as_external_result_authority",
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
    "DECLARED_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_REQUEST_UNREADABLE",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_QUESTION_UNDECLARED",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_INTENT_UNSUPPORTED",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_BLOCK_REQUESTED",
    "SECOND_CARRIER_VERIFICATION_BASIS_MISSING",
    "SECOND_CARRIER_VERIFICATION_NOT_RECORDED",
    "SECOND_CARRIER_VERIFICATION_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_VERIFICATION_VERSION_NOT_0_1_0",
    "SECOND_CARRIER_VERIFICATION_DID_NOT_RECORD_BOUNDED_VERIFICATION",
    "SECOND_CARRIER_VERIFICATION_ALREADY_CREATED_EXTERNAL_RESULT",
    "SECOND_CARRIER_VERIFICATION_ALREADY_CREATED_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_VERIFICATION_ALREADY_CREATED_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_VERIFICATION_TREATED_VERIFICATION_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_VERIFICATION_TREATED_VERIFICATION_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_VERIFICATION_TREATED_VERIFICATION_AS_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_VERIFICATION_TREATED_ZERO_EXIT_CODE_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_VERIFICATION_TREATED_STRING_ZERO_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_VERIFICATION_TREATED_OK_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_VERIFICATION_TREATED_RAN_7_TESTS_AS_CROSS_CARRIER_PROOF",
    "SECOND_CARRIER_VERIFICATION_TREATED_RETURNED_CAPTURE_AS_CROSS_CARRIER_PROOF",
    "SECOND_CARRIER_VERIFICATION_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_BASIS_MISSING",
    "SECOND_CARRIER_SUCCESS_BASIS_MISSING",
    "SECOND_CARRIER_SUCCESS_NOT_RECORDED",
    "SECOND_CARRIER_SUCCESS_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_RESULT_BASIS_MISSING",
    "SECOND_CARRIER_RESULT_NOT_RECORDED",
    "SECOND_CARRIER_RESULT_FAILED_CHECKS_PRESENT",
    "RETURNED_CAPTURE_INTAKE_BASIS_MISSING",
    "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
    "RETURNED_CAPTURE_TREATED_AS_EXTERNAL_RESULT",
    "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_PROOF",
    "ZERO_EXIT_CODE_TREATED_AS_EXTERNAL_RESULT",
    "STRING_ZERO_TREATED_AS_EXTERNAL_RESULT",
    "OK_OUTPUT_TREATED_AS_EXTERNAL_RESULT",
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
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_AS_SOURCE",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_AS_AUTHORITY",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_AS_CURRENTNESS",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_AS_FINAL_COMPLETION",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_AS_RUNTIME",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_AS_CONTINUATION",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_EXTERNAL_RESULT_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_EXTERNAL_RESULT_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_EXTERNAL_RESULT_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_EXTERNAL_RESULT_AUTHORITY",
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
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_EXTERNAL_RESULT_BOUNDARY",
    "STRING_ZERO_REPRESENTATION_TURNED_INTO_DOCTRINE",
    "ARTIFACTS_MUTATED",
    "RETURNED_CAPTURE_MATERIAL_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_SCOPE",
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
        "raw_external_result_body",
        "capture_body",
        "second_carrier_external_result_body",
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
    "RAW_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_BODY_MUST_NOT_RETURN",
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
        RESULT_TYPE,
        RESULT_VERSION,
        CORE_QUESTION,
        EXPECTED_SECOND_CARRIER_VERIFICATION_OUTCOME,
        EXPECTED_SECOND_CARRIER_VERIFICATION_BOUNDARY_OUTCOME,
        EXPECTED_SECOND_CARRIER_SUCCESS_OUTCOME,
        EXPECTED_SECOND_CARRIER_RESULT_OUTCOME,
        EXPECTED_SECOND_CARRIER_OUTPUT_CAPTURE_OUTCOME,
        "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
        "RETURNED_RESULT_CONTAINMENT_PRESERVED",
        "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
        "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
        "FIRST_SUCCESS_BOUNDARY_TEST_FAILURE_PRESERVED",
        "FIRST_RESULT_BOUNDARY_RESOLVER_FAILURE_PRESERVED",
        "STRING_ZERO_NOT_EXTERNAL_RESULT",
    }
)


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _is_sensitive_key(key: Any) -> bool:
    key_text = str(key)
    return key_text in SENSITIVE_CONTENT_KEYS or key_text.endswith("_body")


def _contains_raw_sentinel(value: str) -> bool:
    return any(sentinel in value for sentinel in RAW_SENTINELS)


def _sanitize(value: Any, key: str | None = None) -> Any:
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
                sanitized[key_text] = _sanitize(item_value, key_text)
        return sanitized
    if isinstance(value, (list, tuple)):
        return [_sanitize(item, key) for item in value]
    if isinstance(value, set):
        return [_sanitize(item, key) for item in sorted(value, key=str)]
    if isinstance(value, Path):
        return str(value)
    return copy.deepcopy(value)


def _declared(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, Mapping):
        return bool(value)
    if isinstance(value, (list, tuple, set)):
        return bool(value)
    return True


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


def _as_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        lowered = value.strip().lower()
        if lowered in {"true", "yes", "1"}:
            return True
        if lowered in {"false", "no", "0"}:
            return False
    if isinstance(value, Mapping):
        for key in (
            "declared",
            "preserved",
            "recorded",
            "basis_preserved",
            "posture_declared",
            "expected_posture_preserved",
            "closed",
            "blocked",
        ):
            if key in value:
                return _as_bool(value[key])
    return False


def _request_id(request: Mapping[str, Any]) -> str:
    value = request.get("second_carrier_external_result_boundary_request_id")
    if isinstance(value, str) and value.strip():
        return value.strip()
    return (
        "portable_source_body_verification_second_carrier_external_result_"
        "boundary_request_001"
    )


def _request_declares(request: Mapping[str, Any], key: str) -> bool:
    return key in request and _declared(request.get(key))


def _nested_value(value: Any, nested_keys: tuple[str, ...]) -> Any:
    if not isinstance(value, Mapping):
        return None
    for key in nested_keys:
        if key in value:
            return value[key]
    for container_key in (
        "statement",
        "summary",
        "non_claims",
        "selected_shortcut_values",
        "metadata",
        "selected_reference",
    ):
        nested = value.get(container_key)
        if isinstance(nested, Mapping):
            found = _nested_value(nested, nested_keys)
            if found is not None:
                return found
    return None


def _request_value(
    request: Mapping[str, Any],
    top_key: str,
    basis_fields: tuple[str, ...] = (),
    nested_keys: tuple[str, ...] = (),
    default: Any = None,
) -> Any:
    if top_key in request:
        return request[top_key]
    for field_name in basis_fields:
        found = _nested_value(request.get(field_name), nested_keys)
        if found is not None:
            return found
    return default


def _scope_values(request: Mapping[str, Any]) -> list[Any]:
    values = request.get("second_carrier_external_result_boundary_scope", SUPPORTED_SCOPE_VALUES)
    if isinstance(values, str):
        return [values]
    if isinstance(values, Mapping):
        return list(values.values())
    if isinstance(values, (list, tuple, set)):
        return list(values)
    return [values]


def _non_claim_value(request: Mapping[str, Any], key: str) -> Any:
    non_claims = request.get("declared_non_claims")
    if isinstance(non_claims, Mapping) and key in non_claims:
        return non_claims[key]
    if key in request:
        return request[key]
    return None


def _non_claim_code(key: str) -> str:
    direct = {
        "external_result_created": "EXTERNAL_RESULT_CREATED",
        "cross_carrier_evidence_created": "CROSS_CARRIER_EVIDENCE_CREATED",
        "portable_verification_closure_created": "PORTABLE_VERIFICATION_CLOSURE_CREATED",
        "source_transfer_occurred": "SOURCE_TRANSFER_OCCURRED",
        "source_receipt_occurred": "SOURCE_RECEIPT_OCCURRED",
        "reception_authorization_created": "RECEPTION_AUTHORIZATION_CREATED",
        "zero_exit_code_treated_as_external_result": "ZERO_EXIT_CODE_TREATED_AS_EXTERNAL_RESULT",
        "string_zero_treated_as_external_result": "STRING_ZERO_TREATED_AS_EXTERNAL_RESULT",
        "ok_output_treated_as_external_result": "OK_OUTPUT_TREATED_AS_EXTERNAL_RESULT",
        "ran_7_tests_treated_as_cross_carrier_proof": "RAN_7_TESTS_TREATED_AS_CROSS_CARRIER_PROOF",
        "returned_capture_treated_as_cross_carrier_evidence": "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_PROOF",
        "receiving_carrier_treated_as_authority": "RECEIVING_CARRIER_TREATED_AS_AUTHORITY",
        "artifact_existence_treated_as_external_result_authority": "ARTIFACT_EXISTENCE_TREATED_AS_EXTERNAL_RESULT_AUTHORITY",
        "artifact_path_treated_as_currentness": "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
        "repo_local_availability_treated_as_external_result_authority": "REPO_LOCAL_AVAILABILITY_TREATED_AS_EXTERNAL_RESULT_AUTHORITY",
        "hidden_repo_state_used_as_external_result_content": "HIDDEN_REPO_STATE_USED_AS_EXTERNAL_RESULT_CONTENT",
        "hidden_repo_state_used_as_external_result_authority": "HIDDEN_REPO_STATE_USED_AS_EXTERNAL_RESULT_AUTHORITY",
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
    }
    if key.startswith("second_carrier_external_result_boundary_treated_as_"):
        suffix = key.removeprefix(
            "second_carrier_external_result_boundary_treated_as_"
        ).upper()
        return f"SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_AS_{suffix}"
    if key == "second_carrier_verification_treated_as_external_result":
        return "SECOND_CARRIER_VERIFICATION_TREATED_VERIFICATION_AS_EXTERNAL_RESULT"
    if key == "second_carrier_verification_treated_as_cross_carrier_evidence":
        return "SECOND_CARRIER_VERIFICATION_TREATED_VERIFICATION_AS_CROSS_CARRIER_EVIDENCE"
    if key.startswith("first_success_boundary_test_"):
        return "FIRST_SUCCESS_BOUNDARY_TEST_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED"
    if key.startswith("first_result_boundary_resolver_"):
        return "FIRST_RESULT_BOUNDARY_RESOLVER_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED"
    if key.startswith("v1_"):
        return "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"
    return direct.get(key, "NON_CLAIM_MISSING_OR_FLIPPED")


def _make_check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    block_code: str,
) -> dict[str, Any]:
    check = {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": _sanitize(expected_posture),
        "actual_posture": _sanitize(actual_posture),
        "block_code": None,
        "failure_code": None,
    }
    if not passed:
        check["block_code"] = block_code
        check["failure_code"] = block_code
    return check


def _basis(
    basis_name: str,
    outcome: str | None = None,
    version: str | None = None,
    failed_check_count: int | None = None,
    **extra: Any,
) -> dict[str, Any]:
    result = {
        "basis_name": basis_name,
        "basis_declared": True,
        "reference_shape": True,
        "basis_only": True,
        "external_result_created": False,
        "cross_carrier_evidence_created": False,
        "portable_verification_closure_created": False,
    }
    if outcome is not None:
        result["outcome"] = outcome
    if version is not None:
        result["result_version"] = version
    if failed_check_count is not None:
        result["failed_check_count"] = failed_check_count
    result.update(extra)
    return result


def _posture(posture_name: str) -> dict[str, Any]:
    return {
        "posture_name": posture_name,
        "declared": True,
        "bounded": True,
        "second_carrier_external_result_boundary_only": True,
    }


def _reference_basis_section(field_name: str, request: Mapping[str, Any]) -> dict[str, Any]:
    selected = request.get(field_name)
    shortcut_prefixes = {
        "selected_second_carrier_verification_basis": (
            "selected_second_carrier_verification_",
        ),
        "selected_second_carrier_verification_boundary_basis": (
            "selected_second_carrier_verification_boundary_",
        ),
        "selected_second_carrier_success_basis": ("selected_second_carrier_success_",),
        "selected_second_carrier_result_basis": ("selected_second_carrier_result_",),
        "selected_returned_second_carrier_live_capture_intake_basis": (
            "selected_returned_capture_",
        ),
        "selected_returned_capture_material_basis": ("selected_returned_capture_",),
        "selected_second_carrier_output_capture_basis": (
            "selected_second_carrier_output_capture_",
        ),
    }.get(field_name, ())
    shortcuts = {
        str(key): _sanitize(value, str(key))
        for key, value in request.items()
        if any(str(key).startswith(prefix) for prefix in shortcut_prefixes)
    }
    return {
        "basis_name": field_name,
        "basis_declared": _request_declares(request, field_name),
        "reference_shape": True,
        "basis_only": True,
        "selected_reference": _sanitize(selected, field_name),
        "selected_shortcut_values": shortcuts,
        "external_result_created": False,
        "cross_carrier_evidence_created": False,
        "portable_verification_closure_created": False,
        "source_created": False,
        "authority_created": False,
        "currentness_created": False,
        "runtime_created": False,
        "follow_on_work_authorized": False,
        "raw_full_prior_artifact_body_returned": False,
        "hidden_repo_state_used_as_external_result_authority": False,
        "repo_local_availability_treated_as_external_result_authority": False,
    }


def _posture_section(field_name: str, request: Mapping[str, Any], recorded: bool) -> dict[str, Any]:
    return {
        "posture_name": field_name,
        "declared": bool(recorded),
        "request_declared": _as_bool(request.get(field_name)),
        "bounded_second_carrier_external_result_boundary_posture_only": True,
        "external_result_created": False,
        "cross_carrier_evidence_created": False,
        "portable_verification_closure_created": False,
        "follow_on_work_authorized": False,
    }


def _recorded_statement(recorded: bool) -> dict[str, bool]:
    return {field: bool(recorded) for field in ALLOWED_TRUE_RECORDED_FIELDS}


def _false_non_claims() -> dict[str, bool]:
    return {field: False for field in REQUIRED_FALSE_NON_CLAIMS}


def _non_meaning() -> dict[str, bool]:
    return {
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
        "external_result_boundary_became_external_result": False,
        "external_result_boundary_became_cross_carrier_proof": False,
        "external_result_boundary_became_portable_verification_closure": False,
        "external_result_boundary_became_source_transfer_source_receipt_or_reception_authorization": False,
        "external_result_boundary_became_source_authority_or_currentness": False,
        "verification_became_external_result": False,
        "verification_became_cross_carrier_evidence": False,
        "zero_exit_code_became_external_result": False,
        "string_zero_became_external_result": False,
        "string_zero_became_doctrine": False,
        "ok_became_external_result": False,
        "ran_7_tests_became_cross_carrier_proof": False,
        "returned_capture_became_proof": False,
        "macbook_pro_became_authority": False,
        "macbook_air_became_source": False,
        "artifact_existence_became_external_result_authority": False,
        "artifact_path_became_currentness": False,
        "repo_local_availability_became_external_result_authority": False,
        "hidden_repo_state_became_external_result_authority": False,
        "first_success_boundary_test_repaired_hidden_erased_or_claimed_passed": False,
        "first_result_boundary_resolver_repaired_hidden_erased_or_claimed_passed": False,
        "v1_packet_emission_boundary_resolver_repaired_hidden_erased_or_claimed_passed": False,
    }


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "second-carrier external-result boundary test",
            "second-carrier external-result boundary live artifact",
            "second-carrier external-result boundary terminal summary, if needed",
            "second-carrier external result spec/resolver/test/live artifact, if admitted",
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
            "optional future numeric-zero declared-input resolver review, if separately selected",
        ],
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }


def _validate_request(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    question = request.get("second_carrier_external_result_boundary_question")
    checks.append(
        _make_check(
            "second_carrier_external_result_boundary_question_declared",
            question == CORE_QUESTION,
            CORE_QUESTION,
            question,
            "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_QUESTION_UNDECLARED",
        )
    )

    intent = request.get("second_carrier_external_result_boundary_intent")
    checks.append(
        _make_check(
            "second_carrier_external_result_boundary_intent_supported",
            intent in SUPPORTED_INTENTS,
            list(SUPPORTED_INTENTS),
            intent,
            "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_INTENT_UNSUPPORTED",
        )
    )

    scope_values = _scope_values(request)
    unsupported_scope = [value for value in scope_values if value not in SUPPORTED_SCOPE_VALUES]
    checks.append(
        _make_check(
            "second_carrier_external_result_boundary_scope_supported",
            not unsupported_scope,
            list(SUPPORTED_SCOPE_VALUES),
            scope_values,
            "UNSUPPORTED_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_SCOPE",
        )
    )

    basis_required = (
        ("selected_second_carrier_verification_basis", "SECOND_CARRIER_VERIFICATION_BASIS_MISSING"),
        ("selected_second_carrier_verification_terminal_summary_basis", "SECOND_CARRIER_VERIFICATION_BASIS_MISSING"),
        ("selected_second_carrier_verification_boundary_basis", "SECOND_CARRIER_VERIFICATION_BOUNDARY_BASIS_MISSING"),
        ("selected_second_carrier_verification_boundary_terminal_summary_basis", "SECOND_CARRIER_VERIFICATION_BOUNDARY_BASIS_MISSING"),
        ("selected_second_carrier_success_basis", "SECOND_CARRIER_SUCCESS_BASIS_MISSING"),
        ("selected_second_carrier_success_terminal_summary_basis", "SECOND_CARRIER_SUCCESS_BASIS_MISSING"),
        ("selected_second_carrier_result_basis", "SECOND_CARRIER_RESULT_BASIS_MISSING"),
        ("selected_returned_second_carrier_live_capture_intake_basis", "RETURNED_CAPTURE_INTAKE_BASIS_MISSING"),
        ("selected_returned_capture_material_basis", "RETURNED_CAPTURE_MATERIAL_MISSING"),
        ("selected_second_carrier_output_capture_basis", "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_MISSING"),
        ("selected_packet_transfer_basis", "SECOND_CARRIER_VERIFICATION_BASIS_MISSING"),
        ("selected_packet_emission_basis", "SECOND_CARRIER_VERIFICATION_BASIS_MISSING"),
        ("selected_packet_emission_boundary_v2_basis", "SECOND_CARRIER_VERIFICATION_BASIS_MISSING"),
        ("selected_packet_emission_boundary_v1_predecessor_failure_basis", "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
        ("selected_packet_artifact_basis", "SECOND_CARRIER_VERIFICATION_BASIS_MISSING"),
        ("selected_command_success_basis", "SECOND_CARRIER_VERIFICATION_BASIS_MISSING"),
        ("selected_command_result_v2_basis", "SECOND_CARRIER_VERIFICATION_BASIS_MISSING"),
        ("selected_output_capture_v2_basis", "SECOND_CARRIER_VERIFICATION_BASIS_MISSING"),
        ("selected_command_output_report_artifact_basis", "SECOND_CARRIER_VERIFICATION_BASIS_MISSING"),
        ("selected_command_execution_basis", "SECOND_CARRIER_VERIFICATION_BASIS_MISSING"),
        ("selected_command_report_lineage_basis", "SECOND_CARRIER_VERIFICATION_BASIS_MISSING"),
        ("selected_predecessor_failure_basis", "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
        ("selected_evidence_manifest_basis", "SECOND_CARRIER_VERIFICATION_BASIS_MISSING"),
        ("selected_artifact_containment_basis", "SECOND_CARRIER_VERIFICATION_BASIS_MISSING"),
        ("selected_portable_verification_basis", "SECOND_CARRIER_VERIFICATION_BASIS_MISSING"),
    )
    for field_name, code in basis_required:
        checks.append(
            _make_check(
                f"{field_name}_declared",
                _request_declares(request, field_name),
                "declared reference-shaped basis",
                request.get(field_name),
                code,
            )
        )

    checks.extend(_basis_integrity_checks(request))
    checks.extend(_posture_checks(request))
    checks.extend(_non_claim_checks(request))
    return checks


def _basis_integrity_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    verification_fields = (
        "selected_second_carrier_verification_basis",
        "selected_second_carrier_verification_terminal_summary_basis",
    )
    verification_boundary_fields = (
        "selected_second_carrier_verification_boundary_basis",
        "selected_second_carrier_verification_boundary_terminal_summary_basis",
    )
    success_fields = (
        "selected_second_carrier_success_basis",
        "selected_second_carrier_success_terminal_summary_basis",
    )
    result_fields = ("selected_second_carrier_result_basis",)
    intake_fields = ("selected_returned_second_carrier_live_capture_intake_basis",)
    capture_fields = ("selected_returned_capture_material_basis",)
    output_capture_fields = ("selected_second_carrier_output_capture_basis",)

    checks.append(
        _make_check(
            "second_carrier_verification_outcome_recorded",
            _request_value(
                request,
                "selected_second_carrier_verification_result_outcome",
                verification_fields,
                ("outcome", "result_outcome"),
            )
            == EXPECTED_SECOND_CARRIER_VERIFICATION_OUTCOME,
            EXPECTED_SECOND_CARRIER_VERIFICATION_OUTCOME,
            _request_value(
                request,
                "selected_second_carrier_verification_result_outcome",
                verification_fields,
                ("outcome", "result_outcome"),
            ),
            "SECOND_CARRIER_VERIFICATION_NOT_RECORDED",
        )
    )
    checks.append(
        _make_check(
            "second_carrier_verification_version_0_1_0",
            _request_value(
                request,
                "selected_second_carrier_verification_result_version",
                verification_fields,
                ("result_version", "version"),
            )
            == RESULT_VERSION,
            RESULT_VERSION,
            _request_value(
                request,
                "selected_second_carrier_verification_result_version",
                verification_fields,
                ("result_version", "version"),
            ),
            "SECOND_CARRIER_VERIFICATION_VERSION_NOT_0_1_0",
        )
    )
    checks.append(
        _make_check(
            "second_carrier_verification_failed_checks_zero",
            _as_int(
                _request_value(
                    request,
                    "selected_second_carrier_verification_failed_check_count",
                    verification_fields,
                    ("failed_check_count",),
                )
            )
            == 0,
            0,
            _request_value(
                request,
                "selected_second_carrier_verification_failed_check_count",
                verification_fields,
                ("failed_check_count",),
            ),
            "SECOND_CARRIER_VERIFICATION_FAILED_CHECKS_PRESENT",
        )
    )

    verification_bool_checks = (
        (
            "selected_second_carrier_verification_bounded_verification_recorded",
            ("bounded_second_carrier_verification_recorded", "verification_recorded_bounded"),
            True,
            "SECOND_CARRIER_VERIFICATION_DID_NOT_RECORD_BOUNDED_VERIFICATION",
            "second_carrier_verification_recorded_bounded_verification",
        ),
        (
            "selected_second_carrier_verification_already_created_external_result",
            ("external_result_created", "already_created_external_result"),
            False,
            "SECOND_CARRIER_VERIFICATION_ALREADY_CREATED_EXTERNAL_RESULT",
            "second_carrier_verification_did_not_already_create_external_result",
        ),
        (
            "selected_second_carrier_verification_already_created_cross_carrier_evidence",
            ("cross_carrier_evidence_created", "already_created_cross_carrier_evidence"),
            False,
            "SECOND_CARRIER_VERIFICATION_ALREADY_CREATED_CROSS_CARRIER_EVIDENCE",
            "second_carrier_verification_did_not_already_create_cross_carrier_evidence",
        ),
        (
            "selected_second_carrier_verification_already_created_portable_verification_closure",
            ("portable_verification_closure_created", "already_created_portable_verification_closure"),
            False,
            "SECOND_CARRIER_VERIFICATION_ALREADY_CREATED_PORTABLE_VERIFICATION_CLOSURE",
            "second_carrier_verification_did_not_already_create_portable_verification_closure",
        ),
        (
            "selected_second_carrier_verification_treated_verification_as_external_result",
            ("verification_treated_as_external_result",),
            False,
            "SECOND_CARRIER_VERIFICATION_TREATED_VERIFICATION_AS_EXTERNAL_RESULT",
            "second_carrier_verification_did_not_treat_verification_as_external_result",
        ),
        (
            "selected_second_carrier_verification_treated_verification_as_cross_carrier_evidence",
            ("verification_treated_as_cross_carrier_evidence",),
            False,
            "SECOND_CARRIER_VERIFICATION_TREATED_VERIFICATION_AS_CROSS_CARRIER_EVIDENCE",
            "second_carrier_verification_did_not_treat_verification_as_cross_carrier_evidence",
        ),
        (
            "selected_second_carrier_verification_treated_verification_as_portable_verification_closure",
            ("verification_treated_as_portable_verification_closure",),
            False,
            "SECOND_CARRIER_VERIFICATION_TREATED_VERIFICATION_AS_PORTABLE_VERIFICATION_CLOSURE",
            "second_carrier_verification_did_not_treat_verification_as_portable_closure",
        ),
        (
            "selected_second_carrier_verification_zero_exit_code_not_external_result",
            ("zero_exit_code_not_external_result", "zero_exit_code_not_verification_as_standalone_inference"),
            True,
            "SECOND_CARRIER_VERIFICATION_TREATED_ZERO_EXIT_CODE_AS_EXTERNAL_RESULT",
            "second_carrier_verification_kept_zero_exit_code_not_external_result",
        ),
        (
            "selected_second_carrier_verification_string_zero_not_external_result",
            ("string_zero_not_external_result",),
            True,
            "SECOND_CARRIER_VERIFICATION_TREATED_STRING_ZERO_AS_EXTERNAL_RESULT",
            "second_carrier_verification_kept_string_zero_not_external_result",
        ),
        (
            "selected_second_carrier_verification_ok_not_external_result",
            ("ok_output_not_external_result", "ok_output_not_verification_as_standalone_inference"),
            True,
            "SECOND_CARRIER_VERIFICATION_TREATED_OK_AS_EXTERNAL_RESULT",
            "second_carrier_verification_kept_ok_not_external_result",
        ),
        (
            "selected_second_carrier_verification_ran_7_tests_not_cross_carrier_proof",
            ("ran_7_tests_not_cross_carrier_proof",),
            True,
            "SECOND_CARRIER_VERIFICATION_TREATED_RAN_7_TESTS_AS_CROSS_CARRIER_PROOF",
            "second_carrier_verification_kept_ran_7_tests_not_cross_carrier_proof",
        ),
        (
            "selected_second_carrier_verification_returned_capture_not_cross_carrier_proof",
            ("returned_capture_not_cross_carrier_proof",),
            True,
            "SECOND_CARRIER_VERIFICATION_TREATED_RETURNED_CAPTURE_AS_CROSS_CARRIER_PROOF",
            "second_carrier_verification_kept_returned_capture_not_cross_carrier_proof",
        ),
        (
            "selected_second_carrier_verification_official_enum_scope_strings_redacted",
            ("official_enum_scope_strings_redacted",),
            False,
            "SECOND_CARRIER_VERIFICATION_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
            "second_carrier_verification_kept_official_enums_unredacted",
        ),
        (
            "selected_second_carrier_verification_first_success_boundary_test_failure_preserved",
            ("first_success_boundary_test_failure_preserved",),
            True,
            "FIRST_SUCCESS_BOUNDARY_TEST_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
            "second_carrier_verification_preserved_first_success_boundary_failure",
        ),
    )
    for top_key, nested_keys, expected, code, check_name in verification_bool_checks:
        actual = _request_value(request, top_key, verification_fields, nested_keys, expected)
        checks.append(
            _make_check(
                check_name,
                _as_bool(actual) is expected,
                expected,
                actual,
                code,
            )
        )

    checks.extend(
        [
            _make_check(
                "second_carrier_verification_boundary_outcome_recorded",
                _request_value(
                    request,
                    "selected_second_carrier_verification_boundary_result_outcome",
                    verification_boundary_fields,
                    ("outcome", "result_outcome"),
                )
                == EXPECTED_SECOND_CARRIER_VERIFICATION_BOUNDARY_OUTCOME,
                EXPECTED_SECOND_CARRIER_VERIFICATION_BOUNDARY_OUTCOME,
                _request_value(
                    request,
                    "selected_second_carrier_verification_boundary_result_outcome",
                    verification_boundary_fields,
                    ("outcome", "result_outcome"),
                ),
                "SECOND_CARRIER_VERIFICATION_BOUNDARY_BASIS_MISSING",
            ),
            _make_check(
                "second_carrier_verification_boundary_failed_checks_zero",
                _as_int(
                    _request_value(
                        request,
                        "selected_second_carrier_verification_boundary_failed_check_count",
                        verification_boundary_fields,
                        ("failed_check_count",),
                    )
                )
                == 0,
                0,
                _request_value(
                    request,
                    "selected_second_carrier_verification_boundary_failed_check_count",
                    verification_boundary_fields,
                    ("failed_check_count",),
                ),
                "SECOND_CARRIER_VERIFICATION_BOUNDARY_BASIS_MISSING",
            ),
            _make_check(
                "second_carrier_success_outcome_recorded",
                _request_value(
                    request,
                    "selected_second_carrier_success_result_outcome",
                    success_fields,
                    ("outcome", "result_outcome"),
                )
                == EXPECTED_SECOND_CARRIER_SUCCESS_OUTCOME,
                EXPECTED_SECOND_CARRIER_SUCCESS_OUTCOME,
                _request_value(
                    request,
                    "selected_second_carrier_success_result_outcome",
                    success_fields,
                    ("outcome", "result_outcome"),
                ),
                "SECOND_CARRIER_SUCCESS_NOT_RECORDED",
            ),
            _make_check(
                "second_carrier_success_failed_checks_zero",
                _as_int(
                    _request_value(
                        request,
                        "selected_second_carrier_success_failed_check_count",
                        success_fields,
                        ("failed_check_count",),
                    )
                )
                == 0,
                0,
                _request_value(
                    request,
                    "selected_second_carrier_success_failed_check_count",
                    success_fields,
                    ("failed_check_count",),
                ),
                "SECOND_CARRIER_SUCCESS_FAILED_CHECKS_PRESENT",
            ),
            _make_check(
                "second_carrier_result_outcome_recorded",
                _request_value(
                    request,
                    "selected_second_carrier_result_result_outcome",
                    result_fields,
                    ("outcome", "result_outcome"),
                )
                == EXPECTED_SECOND_CARRIER_RESULT_OUTCOME,
                EXPECTED_SECOND_CARRIER_RESULT_OUTCOME,
                _request_value(
                    request,
                    "selected_second_carrier_result_result_outcome",
                    result_fields,
                    ("outcome", "result_outcome"),
                ),
                "SECOND_CARRIER_RESULT_NOT_RECORDED",
            ),
            _make_check(
                "second_carrier_result_failed_checks_zero",
                _as_int(
                    _request_value(
                        request,
                        "selected_second_carrier_result_failed_check_count",
                        result_fields,
                        ("failed_check_count",),
                    )
                )
                == 0,
                0,
                _request_value(
                    request,
                    "selected_second_carrier_result_failed_check_count",
                    result_fields,
                    ("failed_check_count",),
                ),
                "SECOND_CARRIER_RESULT_FAILED_CHECKS_PRESENT",
            ),
            _make_check(
                "returned_capture_intake_preserved",
                _as_bool(
                    _request_value(
                        request,
                        "selected_returned_capture_intake_preserved",
                        intake_fields,
                        ("intake_preserved", "preserved"),
                        True,
                    )
                )
                is True,
                True,
                _request_value(
                    request,
                    "selected_returned_capture_intake_preserved",
                    intake_fields,
                    ("intake_preserved", "preserved"),
                ),
                "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
            ),
            _make_check(
                "returned_capture_intake_capture_only",
                _as_bool(
                    _request_value(
                        request,
                        "selected_returned_capture_intake_capture_only",
                        intake_fields,
                        ("capture_only", "returned_capture_capture_only"),
                        True,
                    )
                )
                is True,
                True,
                _request_value(
                    request,
                    "selected_returned_capture_intake_capture_only",
                    intake_fields,
                    ("capture_only", "returned_capture_capture_only"),
                ),
                "RETURNED_CAPTURE_TREATED_AS_EXTERNAL_RESULT",
            ),
            _make_check(
                "returned_capture_macbook_pro_to_macbook_air_preserved",
                _as_bool(
                    _request_value(
                        request,
                        "selected_returned_capture_from_macbook_pro_to_macbook_air",
                        capture_fields,
                        ("macbook_pro_to_macbook_air",),
                        True,
                    )
                )
                is True,
                True,
                _request_value(
                    request,
                    "selected_returned_capture_from_macbook_pro_to_macbook_air",
                    capture_fields,
                    ("macbook_pro_to_macbook_air",),
                ),
                "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
            ),
            _make_check(
                "returned_capture_placeholder_fields_unrepaired",
                _as_bool(
                    _request_value(
                        request,
                        "selected_returned_capture_placeholder_fields_unrepaired",
                        capture_fields,
                        ("placeholder_fields_unrepaired",),
                        True,
                    )
                )
                is True,
                True,
                _request_value(
                    request,
                    "selected_returned_capture_placeholder_fields_unrepaired",
                    capture_fields,
                    ("placeholder_fields_unrepaired",),
                ),
                "PLACEHOLDER_CARRIER_FIELDS_REPAIRED",
            ),
            _make_check(
                "second_carrier_output_capture_outcome_recorded",
                _request_value(
                    request,
                    "selected_second_carrier_output_capture_result_outcome",
                    output_capture_fields,
                    ("outcome", "result_outcome"),
                )
                == EXPECTED_SECOND_CARRIER_OUTPUT_CAPTURE_OUTCOME,
                EXPECTED_SECOND_CARRIER_OUTPUT_CAPTURE_OUTCOME,
                _request_value(
                    request,
                    "selected_second_carrier_output_capture_result_outcome",
                    output_capture_fields,
                    ("outcome", "result_outcome"),
                ),
                "SECOND_CARRIER_OUTPUT_CAPTURE_NOT_RECORDED",
            ),
            _make_check(
                "second_carrier_output_capture_failed_checks_zero",
                _as_int(
                    _request_value(
                        request,
                        "selected_second_carrier_output_capture_failed_check_count",
                        output_capture_fields,
                        ("failed_check_count",),
                    )
                )
                == 0,
                0,
                _request_value(
                    request,
                    "selected_second_carrier_output_capture_failed_check_count",
                    output_capture_fields,
                    ("failed_check_count",),
                ),
                "SECOND_CARRIER_OUTPUT_CAPTURE_FAILED_CHECKS_PRESENT",
            ),
        ]
    )

    capture_required = (
        ("selected_returned_capture_zip_path", capture_fields, ("zip_path", "original_zip_path"), "RETURNED_ZIP_PATH_MISSING"),
        ("selected_returned_capture_hash_path", capture_fields, ("hash_path",), "RETURNED_HASH_PATH_MISSING"),
        ("selected_returned_capture_extracted_directory_path", capture_fields, ("extracted_directory_path",), "RETURNED_EXTRACTED_DIRECTORY_MISSING"),
        ("selected_returned_capture_combined_terminal_log_path", capture_fields, ("combined_terminal_log_path",), "RETURNED_COMBINED_TERMINAL_LOG_MISSING"),
        ("selected_returned_capture_exit_code", capture_fields, ("exit_code",), "RETURNED_EXIT_CODE_MISSING"),
        ("selected_returned_capture_command_text", capture_fields, ("command_text",), "RETURNED_COMMAND_TEXT_MISSING"),
        ("selected_returned_capture_started_at", capture_fields, ("run_started_at", "started_at"), "RETURNED_TIMESTAMPS_MISSING"),
        ("selected_returned_capture_completed_at", capture_fields, ("run_completed_at", "completed_at"), "RETURNED_TIMESTAMPS_MISSING"),
    )
    for top_key, fields, nested_keys, code in capture_required:
        actual = _request_value(request, top_key, fields, nested_keys)
        checks.append(
            _make_check(
                f"{top_key}_declared",
                _declared(actual),
                "declared returned capture basis",
                actual,
                code,
            )
        )

    exit_code = _request_value(
        request,
        "selected_returned_capture_exit_code",
        capture_fields,
        ("exit_code",),
    )
    checks.append(
        _make_check(
            "string_zero_representation_not_doctrine",
            request.get("string_zero_representation_turned_into_doctrine") is not True,
            "string zero is a declared-input representation only",
            request.get("string_zero_representation_turned_into_doctrine", False),
            "STRING_ZERO_REPRESENTATION_TURNED_INTO_DOCTRINE",
        )
    )
    checks.append(
        _make_check(
            "returned_capture_exit_code_preserved_as_basis_only",
            str(exit_code) == "0",
            'returned capture exit code "0" or 0 as basis only',
            exit_code,
            "RETURNED_EXIT_CODE_MISSING",
        )
    )

    predecessor_visible = _request_declares(request, "selected_predecessor_failure_basis")
    checks.append(
        _make_check(
            "predecessor_failure_visible_and_unrepaired",
            predecessor_visible
            and _non_claim_value(request, "v1_repaired") is False
            and _non_claim_value(request, "first_success_boundary_test_repaired") is False
            and _non_claim_value(request, "first_result_boundary_resolver_repaired") is False,
            "predecessor failures visible and unrepaired",
            request.get("selected_predecessor_failure_basis"),
            "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        )
    )
    return checks


def _posture_code(posture_key: str) -> str:
    direct = {
        "external_result_not_created_posture": "EXTERNAL_RESULT_CREATED",
        "external_result_boundary_not_external_result_posture": "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_AS_EXTERNAL_RESULT",
        "verification_not_external_result_posture": "SECOND_CARRIER_VERIFICATION_TREATED_VERIFICATION_AS_EXTERNAL_RESULT",
        "verification_not_cross_carrier_evidence_posture": "SECOND_CARRIER_VERIFICATION_TREATED_VERIFICATION_AS_CROSS_CARRIER_EVIDENCE",
        "zero_exit_code_not_external_result_posture": "ZERO_EXIT_CODE_TREATED_AS_EXTERNAL_RESULT",
        "string_zero_not_external_result_posture": "STRING_ZERO_TREATED_AS_EXTERNAL_RESULT",
        "ok_output_not_external_result_posture": "OK_OUTPUT_TREATED_AS_EXTERNAL_RESULT",
        "ran_7_tests_not_cross_carrier_proof_posture": "RAN_7_TESTS_TREATED_AS_CROSS_CARRIER_PROOF",
        "returned_capture_not_cross_carrier_proof_posture": "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_PROOF",
        "cross_carrier_evidence_not_created_posture": "CROSS_CARRIER_EVIDENCE_CREATED",
        "portable_verification_closure_not_created_posture": "PORTABLE_VERIFICATION_CLOSURE_CREATED",
        "external_result_not_source_transfer_posture": "SOURCE_TRANSFER_OCCURRED",
        "external_result_not_source_receipt_posture": "SOURCE_RECEIPT_OCCURRED",
        "external_result_not_reception_authorization_posture": "RECEPTION_AUTHORIZATION_CREATED",
        "receiving_carrier_not_authority_posture": "RECEIVING_CARRIER_TREATED_AS_AUTHORITY",
        "source_not_created_posture": "SOURCE_CREATED",
        "authority_not_created_posture": "AUTHORITY_CREATED",
        "currentness_not_created_posture": "CURRENTNESS_CREATED",
        "final_completion_not_created_posture": "FINAL_COMPLETION_CLAIMED",
        "runtime_not_created_posture": "RUNTIME_HOSTING_CREATED",
        "continuation_not_authorized_posture": "CONTINUATION_AUTHORIZED",
        "reusable_permission_not_created_posture": "REUSABLE_PERMISSION_CREATED",
        "follow_on_work_not_authorized_posture": "FOLLOW_ON_WORK_AUTHORIZED",
        "hidden_repo_state_excluded_posture": "HIDDEN_REPO_STATE_USED_AS_EXTERNAL_RESULT_CONTENT",
        "repo_local_availability_not_external_result_authority_posture": "REPO_LOCAL_AVAILABILITY_TREATED_AS_EXTERNAL_RESULT_AUTHORITY",
        "selected_basis_reference_shape_posture": "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
        "raw_full_prior_artifact_body_not_returned_posture": "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
        "official_enum_scope_strings_not_redacted_posture": "SECOND_CARRIER_VERIFICATION_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
        "hostile_raw_body_content_contained_posture": "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_EXTERNAL_RESULT_BOUNDARY",
        "first_success_boundary_test_failure_preserved_posture": "FIRST_SUCCESS_BOUNDARY_TEST_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
        "first_result_boundary_resolver_failure_preserved_posture": "FIRST_RESULT_BOUNDARY_RESOLVER_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    }
    return direct.get(posture_key, "NON_CLAIM_MISSING_OR_FLIPPED")


def _posture_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    for posture_key in POSTURE_KEYS:
        actual = request.get(posture_key)
        checks.append(
            _make_check(
                f"{posture_key}_declared",
                _as_bool(actual) is True,
                "declared posture",
                actual,
                _posture_code(posture_key),
            )
        )
    return checks


def _non_claim_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    for key in REQUIRED_FALSE_NON_CLAIMS:
        actual = _non_claim_value(request, key)
        checks.append(
            _make_check(
                f"{key}_false",
                actual is False,
                False,
                actual,
                _non_claim_code(key),
            )
        )
    return checks


def _first_failed_check(checks: list[dict[str, Any]]) -> dict[str, Any] | None:
    for check in checks:
        if not check["passed"]:
            return check
    return None


def _additional_basis_required(outcome: str, request: Mapping[str, Any]) -> dict[str, Any]:
    context = request.get("additional_basis_context")
    required = outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    return {
        "required": required,
        "basis": _sanitize(context) if required else [],
        "missing_or_unclear_basis": _sanitize(context) if required else [],
        "missing_basis_scheduled": False,
        "missing_basis_authorized": False,
        "missing_basis_executed": False,
        "external_result_created": False,
        "cross_carrier_evidence_created": False,
        "portable_verification_closure_created": False,
        "follow_on_work_authorized": False,
    }


def _not_recorded_basis(outcome: str, request: Mapping[str, Any]) -> dict[str, Any]:
    basis = request.get("not_recorded_basis")
    not_recorded = outcome == OUTCOME_NOT_RECORDED
    return {
        "not_recorded": not_recorded,
        "basis": _sanitize(basis) if not_recorded else [],
        "failed_review_reason": _sanitize(basis) if not_recorded else None,
        "prior_artifacts_mutated": False,
        "returned_capture_material_mutated": False,
        "next_work_authorized": False,
    }


def _determine_outcome(
    request: Mapping[str, Any], checks: list[dict[str, Any]]
) -> tuple[str, dict[str, Any] | None]:
    intent = request.get("second_carrier_external_result_boundary_intent")
    if intent == INTENT_BLOCK:
        block = {
            "blocked": True,
            "block_code": "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_BLOCK_REQUESTED",
            "block_reason": _sanitize(request.get("block_reason", "explicit block intent")),
        }
        return OUTCOME_BLOCKED, block
    failed = _first_failed_check(checks)
    if failed is not None:
        block = {
            "blocked": True,
            "block_code": failed["block_code"],
            "block_reason": failed["check_name"],
        }
        return OUTCOME_BLOCKED, block
    requested = request.get("requested_second_carrier_external_result_boundary_outcome")
    if requested == OUTCOME_REQUIRES_ADDITIONAL_BASIS or _declared(
        request.get("additional_basis_context")
    ):
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS, None
    if requested == OUTCOME_NOT_RECORDED or intent == INTENT_DO_NOT_RECORD:
        return OUTCOME_NOT_RECORDED, None
    return OUTCOME_RECORDED, None


def _metadata(request: Mapping[str, Any]) -> dict[str, Any]:
    request_id = _request_id(request)
    result_id = f"{request_id}__{RESULT_TYPE}"
    return {
        "portable_source_body_verification_second_carrier_external_result_boundary_result_id": result_id,
        "portable_source_body_verification_second_carrier_external_result_boundary_result_type": RESULT_TYPE,
        "portable_source_body_verification_second_carrier_external_result_boundary_result_version": RESULT_VERSION,
        "generated_at": _now(),
        "resolver_module": RESOLVER_MODULE,
        "second_carrier_external_result_boundary_request_id": request_id,
    }


def _declared_question(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "second_carrier_external_result_boundary_request_id": _request_id(request),
        "question": _sanitize(request.get("second_carrier_external_result_boundary_question")),
        "expected_question": CORE_QUESTION,
        "intent": _sanitize(request.get("second_carrier_external_result_boundary_intent")),
    }


def _result_from_request(request: Mapping[str, Any]) -> dict[str, Any]:
    checks = _validate_request(request)
    outcome, block = _determine_outcome(request, checks)
    recorded = outcome == OUTCOME_RECORDED
    metadata = _metadata(request)
    non_claims = _false_non_claims()

    result: dict[str, Any] = {
        "portable_source_body_verification_second_carrier_external_result_boundary_metadata": metadata,
        "declared_second_carrier_external_result_boundary_question": _declared_question(request),
    }
    for field_name in SELECTED_BASIS_KEYS:
        result[field_name] = _reference_basis_section(field_name, request)
    for posture_key in POSTURE_KEYS:
        result[posture_key] = _posture_section(posture_key, request, recorded)

    result.update(
        {
            "second_carrier_external_result_boundary_scope": _sanitize(_scope_values(request)),
            "second_carrier_external_result_boundary_checks": checks,
            "second_carrier_external_result_boundary_statement": _recorded_statement(recorded),
            "second_carrier_external_result_boundary_non_meaning": _non_meaning(),
            "additional_basis_required": _additional_basis_required(outcome, request),
            "not_recorded_basis": _not_recorded_basis(outcome, request),
            "what_remains_open": _what_remains_open(),
            "non_claims": non_claims,
            "outcome": outcome,
            "block": block,
        }
    )
    result[
        "portable_source_body_verification_second_carrier_external_result_boundary_summary"
    ] = build_portable_source_body_verification_second_carrier_external_result_boundary_summary(
        result
    )
    return result


def resolve_portable_source_body_verification_second_carrier_external_result_boundary(
    declared_second_carrier_external_result_boundary_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded second-carrier external-result-boundary request."""

    if declared_second_carrier_external_result_boundary_request is None:
        declared_second_carrier_external_result_boundary_request = (
            build_declared_portable_source_body_verification_second_carrier_external_result_boundary_request()
        )
    if not isinstance(declared_second_carrier_external_result_boundary_request, Mapping):
        request = {
            "second_carrier_external_result_boundary_request_id": (
                "malformed_second_carrier_external_result_boundary_request"
            ),
            "second_carrier_external_result_boundary_question": None,
            "second_carrier_external_result_boundary_intent": None,
            "declared_non_claims": _false_non_claims(),
        }
        result = _result_from_request(request)
        result["outcome"] = OUTCOME_BLOCKED
        result["block"] = {
            "blocked": True,
            "block_code": "DECLARED_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_REQUEST_MALFORMED",
            "block_reason": "request must be a mapping",
        }
        result[
            "portable_source_body_verification_second_carrier_external_result_boundary_summary"
        ] = build_portable_source_body_verification_second_carrier_external_result_boundary_summary(
            result
        )
        return result
    request = copy.deepcopy(dict(declared_second_carrier_external_result_boundary_request))
    return _result_from_request(request)


def resolve_portable_source_body_verification_second_carrier_external_result_boundary_from_path(
    declared_second_carrier_external_result_boundary_request_path: Path | str,
) -> dict[str, Any]:
    """Resolve a JSON object request read from a path."""

    path = Path(declared_second_carrier_external_result_boundary_request_path)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise PortableSourceBodyVerificationSecondCarrierExternalResultBoundaryError(
            f"Unable to read declared request path: {path}"
        ) from exc
    except json.JSONDecodeError as exc:
        raise PortableSourceBodyVerificationSecondCarrierExternalResultBoundaryError(
            f"Malformed declared request JSON: {path}"
        ) from exc
    if not isinstance(data, Mapping):
        raise PortableSourceBodyVerificationSecondCarrierExternalResultBoundaryError(
            "Declared second-carrier external-result-boundary request JSON must be an object"
        )
    return resolve_portable_source_body_verification_second_carrier_external_result_boundary(
        data
    )


def build_portable_source_body_verification_second_carrier_external_result_boundary_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact summary of a bounded external-result-boundary result."""

    checks = result.get("second_carrier_external_result_boundary_checks", [])
    if not isinstance(checks, list):
        checks = []
    passed_check_count = sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed") is True)
    failed_check_count = sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed") is False)
    metadata = result.get(
        "portable_source_body_verification_second_carrier_external_result_boundary_metadata",
        {},
    )
    if not isinstance(metadata, Mapping):
        metadata = {}
    question = result.get("declared_second_carrier_external_result_boundary_question", {})
    if not isinstance(question, Mapping):
        question = {}
    statement = result.get("second_carrier_external_result_boundary_statement", {})
    if not isinstance(statement, Mapping):
        statement = {}
    non_claims = result.get("non_claims", {})
    if not isinstance(non_claims, Mapping):
        non_claims = {}
    verification_basis = result.get("selected_second_carrier_verification_basis", {})
    if not isinstance(verification_basis, Mapping):
        verification_basis = {}
    verification_shortcuts = verification_basis.get("selected_shortcut_values", {})
    if not isinstance(verification_shortcuts, Mapping):
        verification_shortcuts = {}
    verification_boundary_basis = result.get(
        "selected_second_carrier_verification_boundary_basis", {}
    )
    if not isinstance(verification_boundary_basis, Mapping):
        verification_boundary_basis = {}
    verification_boundary_shortcuts = verification_boundary_basis.get(
        "selected_shortcut_values", {}
    )
    if not isinstance(verification_boundary_shortcuts, Mapping):
        verification_boundary_shortcuts = {}
    success_basis = result.get("selected_second_carrier_success_basis", {})
    if not isinstance(success_basis, Mapping):
        success_basis = {}
    success_shortcuts = success_basis.get("selected_shortcut_values", {})
    if not isinstance(success_shortcuts, Mapping):
        success_shortcuts = {}
    capture_basis = result.get("selected_returned_capture_material_basis", {})
    if not isinstance(capture_basis, Mapping):
        capture_basis = {}
    capture_shortcuts = capture_basis.get("selected_shortcut_values", {})
    if not isinstance(capture_shortcuts, Mapping):
        capture_shortcuts = {}

    block = result.get("block")
    block_code = block.get("block_code") if isinstance(block, Mapping) else None
    block_reason = block.get("block_reason") if isinstance(block, Mapping) else None

    summary = {
        "outcome": result.get("outcome"),
        "block_code": block_code,
        "block_reason": block_reason,
        "request_id": metadata.get("second_carrier_external_result_boundary_request_id"),
        "question": question.get("question"),
        "intent": question.get("intent"),
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
        "result_version": metadata.get(
            "portable_source_body_verification_second_carrier_external_result_boundary_result_version"
        ),
        "resolver_module": metadata.get("resolver_module"),
        "selected_second_carrier_verification_outcome": verification_shortcuts.get(
            "selected_second_carrier_verification_result_outcome"
        ),
        "selected_second_carrier_verification_result_version": verification_shortcuts.get(
            "selected_second_carrier_verification_result_version"
        ),
        "selected_second_carrier_verification_failed_check_count": verification_shortcuts.get(
            "selected_second_carrier_verification_failed_check_count"
        ),
        "selected_second_carrier_verification_boundary_outcome": verification_boundary_shortcuts.get(
            "selected_second_carrier_verification_boundary_result_outcome"
        ),
        "selected_second_carrier_verification_boundary_failed_check_count": verification_boundary_shortcuts.get(
            "selected_second_carrier_verification_boundary_failed_check_count"
        ),
        "selected_second_carrier_success_outcome": success_shortcuts.get(
            "selected_second_carrier_success_result_outcome"
        ),
        "selected_second_carrier_success_failed_check_count": success_shortcuts.get(
            "selected_second_carrier_success_failed_check_count"
        ),
        "selected_returned_capture_intake_path": capture_shortcuts.get(
            "selected_returned_capture_intake_path"
        ),
        "selected_returned_capture_zip_path": capture_shortcuts.get(
            "selected_returned_capture_zip_path"
        ),
        "selected_returned_capture_hash_path": capture_shortcuts.get(
            "selected_returned_capture_hash_path"
        ),
        "selected_returned_capture_extracted_directory_path": capture_shortcuts.get(
            "selected_returned_capture_extracted_directory_path"
        ),
        "selected_returned_capture_exit_code": capture_shortcuts.get(
            "selected_returned_capture_exit_code"
        ),
        "selected_returned_capture_ok_line": capture_shortcuts.get(
            "selected_returned_capture_ok_line"
        ),
        "no_external_result_created": non_claims.get("external_result_created") is False,
        "no_cross_carrier_evidence_created": non_claims.get("cross_carrier_evidence_created") is False,
        "no_portable_verification_closure_created": non_claims.get("portable_verification_closure_created") is False,
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
        "first_success_boundary_test_preserved_as_failed_predecessor": non_claims.get(
            "first_success_boundary_test_claimed_passed"
        )
        is False,
        "v1_predecessor_failure_preserved": non_claims.get("v1_claimed_passed") is False,
        "v1_not_repaired": non_claims.get("v1_repaired") is False,
        "v1_not_hidden": non_claims.get("v1_hidden") is False,
        "v1_not_claimed_passed": non_claims.get("v1_claimed_passed") is False,
        "first_result_boundary_resolver_preserved_as_failed_predecessor": non_claims.get(
            "first_result_boundary_resolver_claimed_passed"
        )
        is False,
    }
    for field in ALLOWED_TRUE_RECORDED_FIELDS:
        summary[field] = bool(statement.get(field))
    for key in (
        "external_result_created",
        "cross_carrier_evidence_created",
        "portable_verification_closure_created",
        "string_zero_treated_as_external_result",
        "consumed_request_reopened",
        "authorization_token_reused",
    ):
        summary[key] = non_claims.get(key)
    return _sanitize(summary)


def _safe_filename_component(value: str) -> str:
    safe = []
    for char in value:
        if char.isalnum() or char in {"-", "_", "."}:
            safe.append(char)
        else:
            safe.append("_")
    return "".join(safe).strip("_") or "second_carrier_external_result_boundary_request"


def _non_overwriting_path(path: Path) -> Path:
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


def write_portable_source_body_verification_second_carrier_external_result_boundary_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a bounded result JSON without silently overwriting existing files."""

    metadata = result.get(
        "portable_source_body_verification_second_carrier_external_result_boundary_metadata",
        {},
    )
    request_id = None
    if isinstance(metadata, Mapping):
        request_id = metadata.get("second_carrier_external_result_boundary_request_id")
    if not isinstance(request_id, str) or not request_id.strip():
        request_id = "portable_source_body_verification_second_carrier_external_result_boundary_request_001"
    filename = (
        f"{_safe_filename_component(request_id)}__"
        "portable_source_body_verification_second_carrier_external_result_boundary_result.json"
    )
    path = Path(output_path) if output_path is not None else OUTPUT_ROOT / filename
    if path.exists():
        path = _non_overwriting_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(_sanitize(result), indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return path


def build_declared_portable_source_body_verification_second_carrier_external_result_boundary_request(
    second_carrier_external_result_boundary_request_id: str = (
        "portable_source_body_verification_second_carrier_external_result_"
        "boundary_reference_review_001"
    ),
    **overrides: Any,
) -> dict[str, Any]:
    """Build a clean declared external-result-boundary request."""

    request: dict[str, Any] = {
        "second_carrier_external_result_boundary_request_id": second_carrier_external_result_boundary_request_id,
        "second_carrier_external_result_boundary_question": CORE_QUESTION,
        "second_carrier_external_result_boundary_intent": INTENT_RECORD,
        "second_carrier_external_result_boundary_scope": list(SUPPORTED_SCOPE_VALUES),
        "declared_non_claims": _false_non_claims(),
        "selected_second_carrier_verification_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_"
            "verification_second_carrier_verification/portable_source_body_"
            "verification_second_carrier_verification_reference_review_001__"
            "portable_source_body_verification_second_carrier_verification_result.json"
        ),
        "selected_second_carrier_verification_result_outcome": EXPECTED_SECOND_CARRIER_VERIFICATION_OUTCOME,
        "selected_second_carrier_verification_result_version": RESULT_VERSION,
        "selected_second_carrier_verification_failed_check_count": 0,
        "selected_second_carrier_verification_bounded_verification_recorded": True,
        "selected_second_carrier_verification_already_created_external_result": False,
        "selected_second_carrier_verification_already_created_cross_carrier_evidence": False,
        "selected_second_carrier_verification_already_created_portable_verification_closure": False,
        "selected_second_carrier_verification_treated_verification_as_external_result": False,
        "selected_second_carrier_verification_treated_verification_as_cross_carrier_evidence": False,
        "selected_second_carrier_verification_treated_verification_as_portable_verification_closure": False,
        "selected_second_carrier_verification_zero_exit_code_not_external_result": True,
        "selected_second_carrier_verification_string_zero_not_external_result": True,
        "selected_second_carrier_verification_ok_not_external_result": True,
        "selected_second_carrier_verification_ran_7_tests_not_cross_carrier_proof": True,
        "selected_second_carrier_verification_returned_capture_not_cross_carrier_proof": True,
        "selected_second_carrier_verification_official_enum_scope_strings_redacted": False,
        "selected_second_carrier_verification_first_success_boundary_test_failure_preserved": True,
        "selected_second_carrier_verification_boundary_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_"
            "verification_second_carrier_verification_boundary/"
            "portable_source_body_verification_second_carrier_verification_"
            "boundary_reference_review_001__portable_source_body_verification_"
            "second_carrier_verification_boundary_result.json"
        ),
        "selected_second_carrier_verification_boundary_result_outcome": EXPECTED_SECOND_CARRIER_VERIFICATION_BOUNDARY_OUTCOME,
        "selected_second_carrier_verification_boundary_failed_check_count": 0,
        "selected_second_carrier_success_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_"
            "verification_second_carrier_success/portable_source_body_"
            "verification_second_carrier_success_reference_review_001__"
            "portable_source_body_verification_second_carrier_success_result.json"
        ),
        "selected_second_carrier_success_result_outcome": EXPECTED_SECOND_CARRIER_SUCCESS_OUTCOME,
        "selected_second_carrier_success_failed_check_count": 0,
        "selected_second_carrier_result_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_"
            "verification_second_carrier_result/portable_source_body_"
            "verification_second_carrier_result_reference_review_001__"
            "portable_source_body_verification_second_carrier_result.json"
        ),
        "selected_second_carrier_result_result_outcome": EXPECTED_SECOND_CARRIER_RESULT_OUTCOME,
        "selected_second_carrier_result_failed_check_count": 0,
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
            "python3 -m unittest tests/test_resolve_portable_source_body_"
            "verification_second_carrier_output_capture.py"
        ),
        "selected_returned_capture_working_directory": (
            "/Users/markomarkota/Desktop/IAMMAI-SYSTEM"
        ),
        "selected_returned_capture_started_at": "2026-05-09T11:34:26Z",
        "selected_returned_capture_completed_at": "2026-05-09T11:34:27Z",
        "selected_returned_capture_exit_code": "0",
        "selected_returned_capture_ran_7_tests_line": "Ran 7 tests in 0.451s",
        "selected_returned_capture_ok_line": "OK",
        "selected_returned_capture_raw_placeholder_carrier_label": "placeholder-carrier-label",
        "selected_returned_capture_raw_placeholder_carrier_type": "placeholder-carrier-type",
        "selected_returned_capture_placeholder_fields_unrepaired": True,
        "selected_second_carrier_output_capture_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_"
            "verification_second_carrier_output_capture/portable_source_body_"
            "verification_second_carrier_output_capture_reference_review_001__"
            "portable_source_body_verification_second_carrier_output_capture_result.json"
        ),
        "selected_second_carrier_output_capture_result_outcome": EXPECTED_SECOND_CARRIER_OUTPUT_CAPTURE_OUTCOME,
        "selected_second_carrier_output_capture_failed_check_count": 0,
        "reference_shaped_input_posture": True,
        "string_zero_representation_turned_into_doctrine": False,
    }

    request["selected_second_carrier_verification_basis"] = _basis(
        "selected_second_carrier_verification_basis",
        EXPECTED_SECOND_CARRIER_VERIFICATION_OUTCOME,
        RESULT_VERSION,
        0,
        bounded_second_carrier_verification_recorded=True,
        verification_recorded_bounded=True,
        verification_not_external_result=True,
        verification_not_cross_carrier_evidence=True,
        verification_not_portable_verification_closure=True,
        zero_exit_code_not_external_result=True,
        string_zero_not_external_result=True,
        ok_output_not_external_result=True,
        ran_7_tests_not_cross_carrier_proof=True,
        returned_capture_not_cross_carrier_proof=True,
        external_result_created=False,
        cross_carrier_evidence_created=False,
        portable_verification_closure_created=False,
        official_enum_scope_strings_redacted=False,
        first_success_boundary_test_failure_preserved=True,
    )
    request["selected_second_carrier_verification_terminal_summary_basis"] = _basis(
        "selected_second_carrier_verification_terminal_summary_basis"
    )
    request["selected_second_carrier_verification_boundary_basis"] = _basis(
        "selected_second_carrier_verification_boundary_basis",
        EXPECTED_SECOND_CARRIER_VERIFICATION_BOUNDARY_OUTCOME,
        RESULT_VERSION,
        0,
    )
    request["selected_second_carrier_verification_boundary_terminal_summary_basis"] = _basis(
        "selected_second_carrier_verification_boundary_terminal_summary_basis"
    )
    request["selected_second_carrier_success_basis"] = _basis(
        "selected_second_carrier_success_basis",
        EXPECTED_SECOND_CARRIER_SUCCESS_OUTCOME,
        RESULT_VERSION,
        0,
    )
    request["selected_second_carrier_success_terminal_summary_basis"] = _basis(
        "selected_second_carrier_success_terminal_summary_basis"
    )
    request["selected_second_carrier_result_basis"] = _basis(
        "selected_second_carrier_result_basis",
        EXPECTED_SECOND_CARRIER_RESULT_OUTCOME,
        RESULT_VERSION,
        0,
    )
    request["selected_returned_second_carrier_live_capture_intake_basis"] = _basis(
        "selected_returned_second_carrier_live_capture_intake_basis",
        intake_preserved=True,
        capture_only=True,
    )
    request["selected_returned_capture_material_basis"] = _basis(
        "selected_returned_capture_material_basis",
        macbook_pro_to_macbook_air=True,
        zip_path=request["selected_returned_capture_zip_path"],
        hash_path=request["selected_returned_capture_hash_path"],
        extracted_directory_path=request["selected_returned_capture_extracted_directory_path"],
        combined_terminal_log_path=request["selected_returned_capture_combined_terminal_log_path"],
        stdout_path=request["selected_returned_capture_stdout_path"],
        stderr_path=request["selected_returned_capture_stderr_path"],
        command_text=request["selected_returned_capture_command_text"],
        working_directory=request["selected_returned_capture_working_directory"],
        run_started_at=request["selected_returned_capture_started_at"],
        run_completed_at=request["selected_returned_capture_completed_at"],
        exit_code=request["selected_returned_capture_exit_code"],
        ran_7_tests_line=request["selected_returned_capture_ran_7_tests_line"],
        ok_line=request["selected_returned_capture_ok_line"],
        raw_placeholder_carrier_label=request[
            "selected_returned_capture_raw_placeholder_carrier_label"
        ],
        raw_placeholder_carrier_type=request[
            "selected_returned_capture_raw_placeholder_carrier_type"
        ],
        placeholder_fields_unrepaired=True,
    )
    request["selected_second_carrier_output_capture_basis"] = _basis(
        "selected_second_carrier_output_capture_basis",
        EXPECTED_SECOND_CARRIER_OUTPUT_CAPTURE_OUTCOME,
        RESULT_VERSION,
        0,
    )
    for field_name in SELECTED_BASIS_KEYS:
        request.setdefault(field_name, _basis(field_name))
    for posture_key in POSTURE_KEYS:
        request[posture_key] = _posture(posture_key)

    if overrides:
        request.update(overrides)
    return request
