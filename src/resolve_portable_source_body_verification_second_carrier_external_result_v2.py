"""Bounded portable source-body verification second-carrier external-result resolver v2.

This resolver is downstream of second-carrier-external-result-boundary. It
records one bounded second-carrier external-result posture only. It does not
create cross-carrier evidence, portable verification closure, source transfer,
source receipt, reception authorization, source, authority, currentness,
runtime, final completion, continuation, reusable permission, or follow-on
work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping, Sequence
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class PortableSourceBodyVerificationSecondCarrierExternalResultError(Exception):
    """Raised for hard resolver input and output failures."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_portable_source_body_verification_second_carrier_external_result_v2"
RESULT_TYPE = "portable_source_body_verification_second_carrier_external_result"
DEFAULT_REQUEST_ID = "portable_source_body_verification_second_carrier_external_result_reference_review_001"
OUTPUT_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_external_result"
)

OUTCOME_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT_RECORDED"
OUTCOME_NOT_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT"
INTENT_BLOCK = "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

CORE_QUESTION = (
    "Can the clean second-carrier-external-result-boundary basis be used to record one bounded "
    "second-carrier external-result posture without creating cross-carrier evidence, portable "
    "verification closure, source transfer, source receipt, reception authorization, source, "
    "authority, currentness, runtime, final completion, continuation, reusable permission, "
    "derivative reception, vessel relation, another reception request, or follow-on work?"
)

EXPECTED_BOUNDARY_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_RECORDED"
)
EXPECTED_VERIFICATION_OUTCOME = "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_VERIFICATION_RECORDED"
EXPECTED_VERIFICATION_BOUNDARY_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_VERIFICATION_BOUNDARY_RECORDED"
)
EXPECTED_SUCCESS_OUTCOME = "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_SUCCESS_RECORDED"
EXPECTED_RESULT_OUTCOME = "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RESULT_RECORDED"
EXPECTED_OUTPUT_CAPTURE_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_OUTPUT_CAPTURE_RECORDED"
)

SUPPORTED_SCOPE_VALUES = (
    "SECOND_CARRIER_EXTERNAL_RESULT_SPEC_ONLY",
    "ONE_BOUNDED_SECOND_CARRIER_EXTERNAL_RESULT_RECORDED",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_BASIS_PRESERVED",
    "SECOND_CARRIER_VERIFICATION_BASIS_PRESERVED",
    "SECOND_CARRIER_SUCCESS_BASIS_PRESERVED",
    "SECOND_CARRIER_RESULT_BASIS_PRESERVED",
    "RETURNED_SECOND_CARRIER_CAPTURE_BASIS_PRESERVED",
    "CAPTURE_INTAKE_BASIS_PRESERVED",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_PRESERVED",
    "EXTERNAL_RESULT_RECORDED_BOUNDED",
    "EXTERNAL_RESULT_ARTIFACT_RECORDED_OR_BOUNDED",
    "EXTERNAL_RESULT_NOT_CROSS_CARRIER_EVIDENCE",
    "EXTERNAL_RESULT_NOT_PORTABLE_VERIFICATION_CLOSURE",
    "EXTERNAL_RESULT_NOT_SOURCE_TRANSFER",
    "EXTERNAL_RESULT_NOT_SOURCE_RECEIPT",
    "EXTERNAL_RESULT_NOT_RECEPTION_AUTHORIZATION",
    "ZERO_EXIT_CODE_NOT_EXTERNAL_RESULT_AS_STANDALONE_INFERENCE",
    "STRING_ZERO_NOT_EXTERNAL_RESULT_AS_STANDALONE_INFERENCE",
    "OK_OUTPUT_NOT_EXTERNAL_RESULT_AS_STANDALONE_INFERENCE",
    "RAN_7_TESTS_NOT_CROSS_CARRIER_PROOF",
    "RETURNED_CAPTURE_NOT_CROSS_CARRIER_PROOF",
    "CROSS_CARRIER_EVIDENCE_NOT_CREATED",
    "PORTABLE_VERIFICATION_CLOSURE_NOT_CREATED",
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
SUPPORTED_SECOND_CARRIER_EXTERNAL_RESULT_SCOPE = SUPPORTED_SCOPE_VALUES

REQUIRED_FALSE_NON_CLAIMS = (
    "cross_carrier_evidence_created",
    "portable_verification_closure_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "second_carrier_external_result_treated_as_cross_carrier_evidence",
    "second_carrier_external_result_treated_as_portable_verification_closure",
    "second_carrier_external_result_treated_as_source_transfer",
    "second_carrier_external_result_treated_as_source_receipt",
    "second_carrier_external_result_treated_as_reception_authorization",
    "second_carrier_external_result_treated_as_source",
    "second_carrier_external_result_treated_as_authority",
    "second_carrier_external_result_treated_as_currentness",
    "second_carrier_external_result_treated_as_final_completion",
    "second_carrier_external_result_treated_as_runtime",
    "second_carrier_external_result_treated_as_continuation",
    "second_carrier_external_result_treated_as_reusable_permission",
    "second_carrier_external_result_treated_as_follow_on_work",
    "zero_exit_code_treated_as_external_result_standalone",
    "string_zero_treated_as_external_result_standalone",
    "string_zero_representation_turned_into_doctrine",
    "ok_output_treated_as_external_result_standalone",
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

ALLOWED_TRUE_RECORDED_FIELDS = (
    "second_carrier_external_result_recorded",
    "bounded_second_carrier_external_result_recorded",
    "external_result_artifact_recorded_or_bounded",
    "second_carrier_external_result_boundary_basis_preserved",
    "second_carrier_verification_basis_preserved",
    "returned_second_carrier_capture_basis_preserved",
    "capture_intake_basis_preserved",
    "second_carrier_output_capture_basis_preserved",
    "external_result_recorded_bounded",
    "external_result_not_cross_carrier_evidence",
    "external_result_not_portable_verification_closure",
    "external_result_not_source_transfer",
    "external_result_not_source_receipt",
    "external_result_not_reception_authorization",
    "zero_exit_code_not_external_result_as_standalone_inference",
    "string_zero_not_external_result_as_standalone_inference",
    "ok_output_not_external_result_as_standalone_inference",
    "ran_7_tests_not_cross_carrier_proof",
    "returned_capture_not_cross_carrier_proof",
    "cross_carrier_evidence_not_created",
    "portable_verification_closure_not_created",
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

BLOCK_CODES = (
    "DECLARED_SECOND_CARRIER_EXTERNAL_RESULT_REQUEST_MALFORMED",
    "DECLARED_SECOND_CARRIER_EXTERNAL_RESULT_REQUEST_UNREADABLE",
    "SECOND_CARRIER_EXTERNAL_RESULT_QUESTION_UNDECLARED",
    "SECOND_CARRIER_EXTERNAL_RESULT_INTENT_UNSUPPORTED",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_BASIS_MISSING",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_NOT_RECORDED",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_VERSION_NOT_0_1_0",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_DID_NOT_DECLARE_FUTURE_EXTERNAL_RESULT_STEP",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_ALREADY_CREATED_EXTERNAL_RESULT",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_ALREADY_CREATED_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_ALREADY_CREATED_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_EXTERNAL_RESULT_BOUNDARY_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_EXTERNAL_RESULT_BOUNDARY_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_EXTERNAL_RESULT_BOUNDARY_AS_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_ZERO_EXIT_CODE_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_STRING_ZERO_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_OK_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_RAN_7_TESTS_AS_CROSS_CARRIER_PROOF",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
    "SECOND_CARRIER_VERIFICATION_BASIS_MISSING",
    "SECOND_CARRIER_VERIFICATION_NOT_RECORDED",
    "SECOND_CARRIER_VERIFICATION_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_VERIFICATION_ALREADY_CREATED_EXTERNAL_RESULT",
    "SECOND_CARRIER_VERIFICATION_ALREADY_CREATED_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_VERIFICATION_ALREADY_CREATED_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_VERIFICATION_TREATED_VERIFICATION_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_VERIFICATION_TREATED_VERIFICATION_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_VERIFICATION_TREATED_ZERO_EXIT_CODE_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_VERIFICATION_TREATED_STRING_ZERO_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_VERIFICATION_TREATED_OK_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_VERIFICATION_TREATED_RAN_7_TESTS_AS_CROSS_CARRIER_PROOF",
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
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_SOURCE_TRANSFER",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_SOURCE_RECEIPT",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_RECEPTION_AUTHORIZATION",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_SOURCE",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_AUTHORITY",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_CURRENTNESS",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_FINAL_COMPLETION",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_RUNTIME",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_CONTINUATION",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_REUSABLE_PERMISSION",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_FOLLOW_ON_WORK",
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
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_EXTERNAL_RESULT",
    "STRING_ZERO_REPRESENTATION_TURNED_INTO_DOCTRINE",
    "ARTIFACTS_MUTATED",
    "RETURNED_CAPTURE_MATERIAL_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_SECOND_CARRIER_EXTERNAL_RESULT_SCOPE",
)

SELECTED_BASIS_KEYS = (
    "selected_second_carrier_external_result_boundary_basis",
    "selected_second_carrier_external_result_boundary_terminal_summary_basis",
    "selected_second_carrier_verification_basis",
    "selected_second_carrier_verification_terminal_summary_basis",
    "selected_second_carrier_verification_boundary_basis",
    "selected_second_carrier_success_basis",
    "selected_second_carrier_result_basis",
    "selected_second_carrier_result_terminal_summary_basis",
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
    "second_carrier_external_result_spec_only_posture",
    "one_bounded_second_carrier_external_result_posture",
    "second_carrier_external_result_boundary_basis_preserved_posture",
    "second_carrier_verification_basis_preserved_posture",
    "returned_second_carrier_capture_basis_preserved_posture",
    "capture_intake_basis_preserved_posture",
    "second_carrier_output_capture_basis_preserved_posture",
    "external_result_recorded_bounded_posture",
    "external_result_artifact_recorded_or_bounded_posture",
    "external_result_not_cross_carrier_evidence_posture",
    "external_result_not_portable_verification_closure_posture",
    "external_result_not_source_transfer_posture",
    "external_result_not_source_receipt_posture",
    "external_result_not_reception_authorization_posture",
    "zero_exit_code_not_external_result_as_standalone_inference_posture",
    "string_zero_not_external_result_as_standalone_inference_posture",
    "ok_output_not_external_result_as_standalone_inference_posture",
    "ran_7_tests_not_cross_carrier_proof_posture",
    "returned_capture_not_cross_carrier_proof_posture",
    "cross_carrier_evidence_not_created_posture",
    "portable_verification_closure_not_created_posture",
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
HOSTILE_SENTINELS = (
    "RAW_SECOND_CARRIER_EXTERNAL_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)
REDACTED_RAW_VALUE = "[bounded-redacted-raw-or-hidden-state]"


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _as_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"true", "1", "yes", "y", "recorded", "created"}
    return bool(value)


def _has_value(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, Mapping):
        return bool(value)
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return bool(value)
    return True


def _safe_int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _sanitize(value: Any, key: str | None = None) -> Any:
    if key is not None and (key in SENSITIVE_CONTENT_KEYS or key.endswith("_body")):
        return REDACTED_RAW_VALUE
    if isinstance(value, Mapping):
        return {str(k): _sanitize(v, str(k)) for k, v in value.items()}
    if isinstance(value, list):
        return [_sanitize(item, key) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item, key) for item in value]
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, str) and any(sentinel in value for sentinel in HOSTILE_SENTINELS):
        return REDACTED_RAW_VALUE
    return value


def _deepcopy_request(request: Mapping[str, Any]) -> dict[str, Any]:
    return copy.deepcopy(dict(request))


def _nested_truthy(value: Any, names: set[str]) -> bool:
    if isinstance(value, Mapping):
        for key, item in value.items():
            if str(key) in names and _as_bool(item):
                return True
            if _nested_truthy(item, names):
                return True
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return any(_nested_truthy(item, names) for item in value)
    return False


def _any_truthy(
    request: Mapping[str, Any],
    top_level_keys: Sequence[str],
    nested_basis_key: str | None = None,
    nested_names: Sequence[str] = (),
) -> bool:
    for key in top_level_keys:
        if _as_bool(request.get(key)):
            return True
    if nested_basis_key is not None:
        names = set(nested_names) | set(top_level_keys)
        if _nested_truthy(request.get(nested_basis_key), names):
            return True
    return False


def _any_selected_basis_truthy(request: Mapping[str, Any], names: Sequence[str]) -> bool:
    nested_names = set(names)
    return any(_nested_truthy(request.get(key), nested_names) for key in SELECTED_BASIS_KEYS)


def _scope_values(request: Mapping[str, Any]) -> list[str]:
    raw = request.get("second_carrier_external_result_scope", SUPPORTED_SCOPE_VALUES)
    if isinstance(raw, Mapping):
        values = raw.get("scope_values", raw.get("values", ()))
    else:
        values = raw
    if isinstance(values, str):
        return [values]
    if isinstance(values, Sequence):
        return [str(value) for value in values]
    return []


def _unsupported_scope_values(request: Mapping[str, Any]) -> list[str]:
    supported = set(SUPPORTED_SCOPE_VALUES)
    return [value for value in _scope_values(request) if value not in supported]


def _declared_non_claims(request: Mapping[str, Any]) -> Mapping[str, Any]:
    value = request.get("declared_non_claims")
    return value if isinstance(value, Mapping) else {}


def _claim_value(request: Mapping[str, Any], name: str) -> Any:
    if name in request:
        return request.get(name)
    return _declared_non_claims(request).get(name)


def _basis_declared(request: Mapping[str, Any], key: str) -> bool:
    return _has_value(request.get(key))


def _posture_declared(request: Mapping[str, Any], key: str) -> bool:
    return _as_bool(request.get(key))


def _check(
    check_name: str,
    passed: bool,
    expected_posture: str,
    actual_posture: str,
    code: str,
) -> dict[str, Any]:
    record: dict[str, Any] = {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": expected_posture,
        "actual_posture": actual_posture,
    }
    if passed:
        record["failure_code"] = None
        record["block_code"] = None
    else:
        record["failure_code"] = code
        record["block_code"] = code
    return record


def _failed_checks(checks: Sequence[Mapping[str, Any]]) -> list[Mapping[str, Any]]:
    return [check for check in checks if not bool(check.get("passed"))]


def _first_failed_code(checks: Sequence[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if not bool(check.get("passed")):
            return str(check.get("block_code") or check.get("failure_code"))
    return None


def _evaluate_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    add = checks.append

    question = request.get("second_carrier_external_result_question")
    intent = request.get("second_carrier_external_result_intent")

    add(_check(
        "second_carrier_external_result_question_declared",
        _has_value(question),
        "question is declared",
        "question declared" if _has_value(question) else "question undeclared",
        "SECOND_CARRIER_EXTERNAL_RESULT_QUESTION_UNDECLARED",
    ))
    add(_check(
        "second_carrier_external_result_intent_supported",
        intent in SUPPORTED_INTENTS,
        "intent is supported",
        str(intent),
        "SECOND_CARRIER_EXTERNAL_RESULT_INTENT_UNSUPPORTED",
    ))
    add(_check(
        "second_carrier_external_result_scope_supported",
        not _unsupported_scope_values(request),
        "scope values are supported",
        ", ".join(_unsupported_scope_values(request)) if _unsupported_scope_values(request) else "supported",
        "UNSUPPORTED_SECOND_CARRIER_EXTERNAL_RESULT_SCOPE",
    ))

    boundary_basis_declared = _basis_declared(request, "selected_second_carrier_external_result_boundary_basis")
    add(_check(
        "second_carrier_external_result_boundary_basis_declared",
        boundary_basis_declared,
        "boundary basis declared",
        "declared" if boundary_basis_declared else "missing",
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_BASIS_MISSING",
    ))
    add(_check(
        "second_carrier_external_result_boundary_outcome_recorded",
        request.get("selected_second_carrier_external_result_boundary_result_outcome") == EXPECTED_BOUNDARY_OUTCOME,
        EXPECTED_BOUNDARY_OUTCOME,
        str(request.get("selected_second_carrier_external_result_boundary_result_outcome")),
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_NOT_RECORDED",
    ))
    add(_check(
        "second_carrier_external_result_boundary_version_0_1_0",
        request.get("selected_second_carrier_external_result_boundary_result_version") == RESULT_VERSION,
        RESULT_VERSION,
        str(request.get("selected_second_carrier_external_result_boundary_result_version")),
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_VERSION_NOT_0_1_0",
    ))
    add(_check(
        "second_carrier_external_result_boundary_failed_checks_zero",
        _safe_int(request.get("selected_second_carrier_external_result_boundary_failed_check_count")) == 0,
        "failed check count zero",
        str(request.get("selected_second_carrier_external_result_boundary_failed_check_count")),
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_FAILED_CHECKS_PRESENT",
    ))
    add(_check(
        "second_carrier_external_result_boundary_declared_future_external_result_step",
        _as_bool(request.get("selected_second_carrier_external_result_boundary_declared_future_external_result_step")),
        "future external-result step declared",
        str(request.get("selected_second_carrier_external_result_boundary_declared_future_external_result_step")),
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_DID_NOT_DECLARE_FUTURE_EXTERNAL_RESULT_STEP",
    ))
    add(_check(
        "second_carrier_external_result_boundary_did_not_create_external_result",
        not _as_bool(request.get("selected_second_carrier_external_result_boundary_already_created_external_result")),
        "external result not already created",
        str(request.get("selected_second_carrier_external_result_boundary_already_created_external_result")),
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_ALREADY_CREATED_EXTERNAL_RESULT",
    ))
    add(_check(
        "second_carrier_external_result_boundary_did_not_create_cross_carrier_evidence",
        not _as_bool(request.get("selected_second_carrier_external_result_boundary_already_created_cross_carrier_evidence")),
        "cross-carrier evidence not created",
        str(request.get("selected_second_carrier_external_result_boundary_already_created_cross_carrier_evidence")),
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_ALREADY_CREATED_CROSS_CARRIER_EVIDENCE",
    ))
    add(_check(
        "second_carrier_external_result_boundary_did_not_create_portable_verification_closure",
        not _as_bool(request.get("selected_second_carrier_external_result_boundary_already_created_portable_verification_closure")),
        "portable verification closure not created",
        str(request.get("selected_second_carrier_external_result_boundary_already_created_portable_verification_closure")),
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_ALREADY_CREATED_PORTABLE_VERIFICATION_CLOSURE",
    ))
    add(_check(
        "second_carrier_external_result_boundary_not_treated_as_external_result",
        not _as_bool(request.get("selected_second_carrier_external_result_boundary_treated_external_result_boundary_as_external_result")),
        "boundary not treated as external result",
        str(request.get("selected_second_carrier_external_result_boundary_treated_external_result_boundary_as_external_result")),
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_EXTERNAL_RESULT_BOUNDARY_AS_EXTERNAL_RESULT",
    ))
    add(_check(
        "second_carrier_external_result_boundary_not_treated_as_cross_carrier_evidence",
        not _as_bool(request.get("selected_second_carrier_external_result_boundary_treated_external_result_boundary_as_cross_carrier_evidence")),
        "boundary not treated as cross-carrier evidence",
        str(request.get("selected_second_carrier_external_result_boundary_treated_external_result_boundary_as_cross_carrier_evidence")),
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_EXTERNAL_RESULT_BOUNDARY_AS_CROSS_CARRIER_EVIDENCE",
    ))
    add(_check(
        "second_carrier_external_result_boundary_not_treated_as_portable_verification_closure",
        not _as_bool(request.get("selected_second_carrier_external_result_boundary_treated_external_result_boundary_as_portable_verification_closure")),
        "boundary not treated as portable verification closure",
        str(request.get("selected_second_carrier_external_result_boundary_treated_external_result_boundary_as_portable_verification_closure")),
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_EXTERNAL_RESULT_BOUNDARY_AS_PORTABLE_VERIFICATION_CLOSURE",
    ))
    add(_check(
        "second_carrier_external_result_boundary_kept_zero_exit_code_not_external_result",
        _as_bool(request.get("selected_second_carrier_external_result_boundary_zero_exit_code_not_external_result")),
        "zero exit code not external result",
        str(request.get("selected_second_carrier_external_result_boundary_zero_exit_code_not_external_result")),
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_ZERO_EXIT_CODE_AS_EXTERNAL_RESULT",
    ))
    add(_check(
        "second_carrier_external_result_boundary_kept_string_zero_not_external_result",
        _as_bool(request.get("selected_second_carrier_external_result_boundary_string_zero_not_external_result")),
        'string "0" not external result',
        str(request.get("selected_second_carrier_external_result_boundary_string_zero_not_external_result")),
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_STRING_ZERO_AS_EXTERNAL_RESULT",
    ))
    add(_check(
        "second_carrier_external_result_boundary_kept_ok_not_external_result",
        _as_bool(request.get("selected_second_carrier_external_result_boundary_ok_not_external_result")),
        "OK not external result",
        str(request.get("selected_second_carrier_external_result_boundary_ok_not_external_result")),
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_OK_AS_EXTERNAL_RESULT",
    ))
    add(_check(
        "second_carrier_external_result_boundary_kept_ran_7_tests_not_cross_carrier_proof",
        _as_bool(request.get("selected_second_carrier_external_result_boundary_ran_7_tests_not_cross_carrier_proof")),
        "Ran 7 tests not cross-carrier proof",
        str(request.get("selected_second_carrier_external_result_boundary_ran_7_tests_not_cross_carrier_proof")),
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_TREATED_RAN_7_TESTS_AS_CROSS_CARRIER_PROOF",
    ))
    add(_check(
        "second_carrier_external_result_boundary_official_enum_scope_strings_unredacted",
        not _as_bool(request.get("selected_second_carrier_external_result_boundary_official_enum_scope_strings_redacted")),
        "official enum and scope strings not redacted",
        str(request.get("selected_second_carrier_external_result_boundary_official_enum_scope_strings_redacted")),
        "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
    ))
    add(_check(
        "second_carrier_external_result_boundary_preserved_first_success_boundary_test_failure",
        _as_bool(request.get("selected_second_carrier_external_result_boundary_first_success_boundary_test_failure_preserved")),
        "first success-boundary test failure preserved",
        str(request.get("selected_second_carrier_external_result_boundary_first_success_boundary_test_failure_preserved")),
        "FIRST_SUCCESS_BOUNDARY_TEST_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    ))

    verification_basis_declared = _basis_declared(request, "selected_second_carrier_verification_basis")
    add(_check(
        "second_carrier_verification_basis_declared",
        verification_basis_declared,
        "verification basis declared",
        "declared" if verification_basis_declared else "missing",
        "SECOND_CARRIER_VERIFICATION_BASIS_MISSING",
    ))
    add(_check(
        "second_carrier_verification_outcome_recorded",
        request.get("selected_second_carrier_verification_result_outcome") == EXPECTED_VERIFICATION_OUTCOME,
        EXPECTED_VERIFICATION_OUTCOME,
        str(request.get("selected_second_carrier_verification_result_outcome")),
        "SECOND_CARRIER_VERIFICATION_NOT_RECORDED",
    ))
    add(_check(
        "second_carrier_verification_failed_checks_zero",
        _safe_int(request.get("selected_second_carrier_verification_failed_check_count")) == 0,
        "failed check count zero",
        str(request.get("selected_second_carrier_verification_failed_check_count")),
        "SECOND_CARRIER_VERIFICATION_FAILED_CHECKS_PRESENT",
    ))
    add(_check(
        "second_carrier_verification_did_not_already_create_external_result",
        not _any_truthy(
            request,
            (
                "selected_second_carrier_verification_already_created_external_result",
                "second_carrier_verification_already_created_external_result",
                "selected_second_carrier_verification_external_result_created",
            ),
            "selected_second_carrier_verification_basis",
            (
                "already_created_external_result",
                "created_external_result",
                "external_result_created",
                "selected_second_carrier_verification_already_created_external_result",
            ),
        ),
        "verification did not already create external result",
        "not created",
        "SECOND_CARRIER_VERIFICATION_ALREADY_CREATED_EXTERNAL_RESULT",
    ))
    add(_check(
        "second_carrier_verification_did_not_already_create_cross_carrier_evidence",
        not _any_truthy(
            request,
            (
                "selected_second_carrier_verification_already_created_cross_carrier_evidence",
                "second_carrier_verification_already_created_cross_carrier_evidence",
            ),
            "selected_second_carrier_verification_basis",
            (
                "already_created_cross_carrier_evidence",
                "created_cross_carrier_evidence",
                "cross_carrier_evidence_created",
                "selected_second_carrier_verification_already_created_cross_carrier_evidence",
            ),
        ),
        "verification did not already create cross-carrier evidence",
        "not created",
        "SECOND_CARRIER_VERIFICATION_ALREADY_CREATED_CROSS_CARRIER_EVIDENCE",
    ))
    add(_check(
        "second_carrier_verification_did_not_already_create_portable_verification_closure",
        not _any_truthy(
            request,
            (
                "selected_second_carrier_verification_already_created_portable_verification_closure",
                "second_carrier_verification_already_created_portable_verification_closure",
            ),
            "selected_second_carrier_verification_basis",
            (
                "already_created_portable_verification_closure",
                "created_portable_verification_closure",
                "portable_verification_closure_created",
                "selected_second_carrier_verification_already_created_portable_verification_closure",
            ),
        ),
        "verification did not already create portable verification closure",
        "not created",
        "SECOND_CARRIER_VERIFICATION_ALREADY_CREATED_PORTABLE_VERIFICATION_CLOSURE",
    ))
    add(_check(
        "second_carrier_verification_recorded_bounded_verification",
        _as_bool(request.get("selected_second_carrier_verification_bounded_verification_recorded")),
        "bounded verification recorded",
        str(request.get("selected_second_carrier_verification_bounded_verification_recorded")),
        "SECOND_CARRIER_VERIFICATION_NOT_RECORDED",
    ))
    add(_check(
        "second_carrier_verification_not_treated_as_external_result",
        not _as_bool(request.get("selected_second_carrier_verification_treated_verification_as_external_result")),
        "verification not treated as external result",
        str(request.get("selected_second_carrier_verification_treated_verification_as_external_result")),
        "SECOND_CARRIER_VERIFICATION_TREATED_VERIFICATION_AS_EXTERNAL_RESULT",
    ))
    add(_check(
        "second_carrier_verification_not_treated_as_cross_carrier_evidence",
        not _as_bool(request.get("selected_second_carrier_verification_treated_verification_as_cross_carrier_evidence")),
        "verification not treated as cross-carrier evidence",
        str(request.get("selected_second_carrier_verification_treated_verification_as_cross_carrier_evidence")),
        "SECOND_CARRIER_VERIFICATION_TREATED_VERIFICATION_AS_CROSS_CARRIER_EVIDENCE",
    ))
    add(_check(
        "second_carrier_verification_kept_zero_exit_code_not_external_result",
        _as_bool(request.get("selected_second_carrier_verification_zero_exit_code_not_external_result")),
        "zero exit code not external result",
        str(request.get("selected_second_carrier_verification_zero_exit_code_not_external_result")),
        "SECOND_CARRIER_VERIFICATION_TREATED_ZERO_EXIT_CODE_AS_EXTERNAL_RESULT",
    ))
    add(_check(
        "second_carrier_verification_kept_string_zero_not_external_result",
        _as_bool(request.get("selected_second_carrier_verification_string_zero_not_external_result")),
        'string "0" not external result',
        str(request.get("selected_second_carrier_verification_string_zero_not_external_result")),
        "SECOND_CARRIER_VERIFICATION_TREATED_STRING_ZERO_AS_EXTERNAL_RESULT",
    ))
    add(_check(
        "second_carrier_verification_kept_ok_not_external_result",
        _as_bool(request.get("selected_second_carrier_verification_ok_not_external_result")),
        "OK not external result",
        str(request.get("selected_second_carrier_verification_ok_not_external_result")),
        "SECOND_CARRIER_VERIFICATION_TREATED_OK_AS_EXTERNAL_RESULT",
    ))
    add(_check(
        "second_carrier_verification_kept_ran_7_tests_not_cross_carrier_proof",
        _as_bool(request.get("selected_second_carrier_verification_ran_7_tests_not_cross_carrier_proof")),
        "Ran 7 tests not cross-carrier proof",
        str(request.get("selected_second_carrier_verification_ran_7_tests_not_cross_carrier_proof")),
        "SECOND_CARRIER_VERIFICATION_TREATED_RAN_7_TESTS_AS_CROSS_CARRIER_PROOF",
    ))

    add(_check(
        "second_carrier_verification_boundary_basis_declared",
        _basis_declared(request, "selected_second_carrier_verification_boundary_basis"),
        "verification boundary basis declared",
        "declared" if _basis_declared(request, "selected_second_carrier_verification_boundary_basis") else "missing",
        "SECOND_CARRIER_VERIFICATION_BOUNDARY_BASIS_MISSING",
    ))
    add(_check(
        "second_carrier_verification_boundary_outcome_recorded",
        request.get("selected_second_carrier_verification_boundary_result_outcome") == EXPECTED_VERIFICATION_BOUNDARY_OUTCOME,
        EXPECTED_VERIFICATION_BOUNDARY_OUTCOME,
        str(request.get("selected_second_carrier_verification_boundary_result_outcome")),
        "SECOND_CARRIER_VERIFICATION_BOUNDARY_BASIS_MISSING",
    ))
    add(_check(
        "second_carrier_verification_boundary_failed_checks_zero",
        _safe_int(request.get("selected_second_carrier_verification_boundary_failed_check_count")) == 0,
        "failed check count zero",
        str(request.get("selected_second_carrier_verification_boundary_failed_check_count")),
        "SECOND_CARRIER_VERIFICATION_FAILED_CHECKS_PRESENT",
    ))
    add(_check(
        "second_carrier_success_basis_declared",
        _basis_declared(request, "selected_second_carrier_success_basis"),
        "success basis declared",
        "declared" if _basis_declared(request, "selected_second_carrier_success_basis") else "missing",
        "SECOND_CARRIER_SUCCESS_BASIS_MISSING",
    ))
    add(_check(
        "second_carrier_success_recorded",
        request.get("selected_second_carrier_success_result_outcome") == EXPECTED_SUCCESS_OUTCOME,
        EXPECTED_SUCCESS_OUTCOME,
        str(request.get("selected_second_carrier_success_result_outcome")),
        "SECOND_CARRIER_SUCCESS_NOT_RECORDED",
    ))
    add(_check(
        "second_carrier_success_failed_checks_zero",
        _safe_int(request.get("selected_second_carrier_success_failed_check_count")) == 0,
        "failed check count zero",
        str(request.get("selected_second_carrier_success_failed_check_count")),
        "SECOND_CARRIER_SUCCESS_FAILED_CHECKS_PRESENT",
    ))
    add(_check(
        "second_carrier_result_basis_declared",
        _basis_declared(request, "selected_second_carrier_result_basis"),
        "result basis declared",
        "declared" if _basis_declared(request, "selected_second_carrier_result_basis") else "missing",
        "SECOND_CARRIER_RESULT_BASIS_MISSING",
    ))
    add(_check(
        "second_carrier_result_recorded",
        request.get("selected_second_carrier_result_result_outcome") == EXPECTED_RESULT_OUTCOME,
        EXPECTED_RESULT_OUTCOME,
        str(request.get("selected_second_carrier_result_result_outcome")),
        "SECOND_CARRIER_RESULT_NOT_RECORDED",
    ))
    add(_check(
        "second_carrier_result_failed_checks_zero",
        _safe_int(request.get("selected_second_carrier_result_failed_check_count")) == 0,
        "failed check count zero",
        str(request.get("selected_second_carrier_result_failed_check_count")),
        "SECOND_CARRIER_RESULT_FAILED_CHECKS_PRESENT",
    ))

    add(_check(
        "returned_capture_intake_basis_declared",
        _basis_declared(request, "selected_returned_second_carrier_live_capture_intake_basis"),
        "returned capture intake basis declared",
        "declared" if _basis_declared(request, "selected_returned_second_carrier_live_capture_intake_basis") else "missing",
        "RETURNED_CAPTURE_INTAKE_BASIS_MISSING",
    ))
    add(_check(
        "returned_capture_intake_preserved",
        _as_bool(request.get("selected_returned_capture_intake_preserved")),
        "returned capture intake preserved",
        str(request.get("selected_returned_capture_intake_preserved")),
        "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
    ))
    add(_check(
        "returned_capture_intake_capture_only",
        _as_bool(request.get("selected_returned_capture_intake_capture_only")),
        "returned capture intake remains capture-only",
        str(request.get("selected_returned_capture_intake_capture_only")),
        "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
    ))
    add(_check(
        "returned_capture_macbook_pro_to_macbook_air_preserved",
        _as_bool(request.get("selected_returned_capture_from_macbook_pro_to_macbook_air")),
        "MacBook Pro to MacBook Air return preserved as non-authority context",
        str(request.get("selected_returned_capture_from_macbook_pro_to_macbook_air")),
        "RECEIVING_CARRIER_TREATED_AS_AUTHORITY",
    ))
    add(_check(
        "returned_capture_not_treated_as_external_result",
        not _as_bool(request.get("returned_capture_treated_as_external_result")),
        "returned capture not external result",
        str(request.get("returned_capture_treated_as_external_result")),
        "RETURNED_CAPTURE_TREATED_AS_EXTERNAL_RESULT",
    ))
    add(_check(
        "returned_capture_not_treated_as_cross_carrier_proof",
        not _as_bool(request.get("returned_capture_treated_as_cross_carrier_proof")),
        "returned capture not cross-carrier proof",
        str(request.get("returned_capture_treated_as_cross_carrier_proof")),
        "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_PROOF",
    ))
    add(_check(
        "zero_exit_code_not_treated_as_external_result",
        not _as_bool(request.get("zero_exit_code_treated_as_external_result")),
        "zero exit code not external result",
        str(request.get("zero_exit_code_treated_as_external_result")),
        "ZERO_EXIT_CODE_TREATED_AS_EXTERNAL_RESULT",
    ))
    add(_check(
        "string_zero_not_treated_as_external_result",
        not _as_bool(request.get("string_zero_treated_as_external_result")),
        'string "0" not external result',
        str(request.get("string_zero_treated_as_external_result")),
        "STRING_ZERO_TREATED_AS_EXTERNAL_RESULT",
    ))
    add(_check(
        "ok_output_not_treated_as_external_result",
        not _as_bool(request.get("ok_output_treated_as_external_result")),
        "OK not external result",
        str(request.get("ok_output_treated_as_external_result")),
        "OK_OUTPUT_TREATED_AS_EXTERNAL_RESULT",
    ))
    add(_check(
        "ran_7_tests_not_treated_as_cross_carrier_proof",
        not _as_bool(request.get("ran_7_tests_treated_as_cross_carrier_proof")),
        "Ran 7 tests not cross-carrier proof",
        str(request.get("ran_7_tests_treated_as_cross_carrier_proof")),
        "RAN_7_TESTS_TREATED_AS_CROSS_CARRIER_PROOF",
    ))
    add(_check(
        "placeholder_carrier_fields_unrepaired",
        _as_bool(request.get("selected_returned_capture_placeholder_fields_unrepaired")),
        "placeholder carrier fields unrepaired",
        str(request.get("selected_returned_capture_placeholder_fields_unrepaired")),
        "PLACEHOLDER_CARRIER_FIELDS_REPAIRED",
    ))
    for key, code in (
        ("selected_returned_capture_zip_path", "RETURNED_ZIP_PATH_MISSING"),
        ("selected_returned_capture_hash_path", "RETURNED_HASH_PATH_MISSING"),
        ("selected_returned_capture_extracted_directory_path", "RETURNED_EXTRACTED_DIRECTORY_MISSING"),
        ("selected_returned_capture_combined_terminal_log_path", "RETURNED_COMBINED_TERMINAL_LOG_MISSING"),
        ("selected_returned_capture_exit_code", "RETURNED_EXIT_CODE_MISSING"),
        ("selected_returned_capture_command_text", "RETURNED_COMMAND_TEXT_MISSING"),
        ("selected_returned_capture_started_at", "RETURNED_TIMESTAMPS_MISSING"),
        ("selected_returned_capture_completed_at", "RETURNED_TIMESTAMPS_MISSING"),
    ):
        add(_check(
            f"{key}_declared",
            _has_value(request.get(key)),
            f"{key} declared",
            "declared" if _has_value(request.get(key)) else "missing",
            code,
        ))
    add(_check(
        "returned_capture_material_basis_declared",
        _basis_declared(request, "selected_returned_capture_material_basis"),
        "returned capture material basis declared",
        "declared" if _basis_declared(request, "selected_returned_capture_material_basis") else "missing",
        "RETURNED_CAPTURE_MATERIAL_MISSING",
    ))
    add(_check(
        "second_carrier_output_capture_basis_declared",
        _basis_declared(request, "selected_second_carrier_output_capture_basis"),
        "second-carrier output capture basis declared",
        "declared" if _basis_declared(request, "selected_second_carrier_output_capture_basis") else "missing",
        "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_MISSING",
    ))
    add(_check(
        "second_carrier_output_capture_recorded",
        request.get("selected_second_carrier_output_capture_result_outcome") == EXPECTED_OUTPUT_CAPTURE_OUTCOME,
        EXPECTED_OUTPUT_CAPTURE_OUTCOME,
        str(request.get("selected_second_carrier_output_capture_result_outcome")),
        "SECOND_CARRIER_OUTPUT_CAPTURE_NOT_RECORDED",
    ))
    add(_check(
        "second_carrier_output_capture_failed_checks_zero",
        _safe_int(request.get("selected_second_carrier_output_capture_failed_check_count")) == 0,
        "failed check count zero",
        str(request.get("selected_second_carrier_output_capture_failed_check_count")),
        "SECOND_CARRIER_OUTPUT_CAPTURE_FAILED_CHECKS_PRESENT",
    ))

    for key in (
        "selected_packet_transfer_basis",
        "selected_packet_emission_basis",
        "selected_command_success_basis",
        "selected_command_result_v2_basis",
        "selected_output_capture_v2_basis",
        "selected_command_output_report_artifact_basis",
        "selected_evidence_manifest_basis",
        "selected_artifact_containment_basis",
        "selected_portable_verification_basis",
        "selected_predecessor_failure_basis",
    ):
        add(_check(
            f"{key}_declared",
            _basis_declared(request, key),
            f"{key} declared",
            "declared" if _basis_declared(request, key) else "missing",
            "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_BASIS_MISSING",
        ))

    lineage_checks = (
        (
            "command_report_lineage_not_current_report_artifact",
            ("command_report_lineage_treated_as_current_report_artifact", "selected_command_report_lineage_treated_as_current_report_artifact"),
            ("treated_as_current_report_artifact", "current_report_artifact", "command_report_lineage_treated_as_current_report_artifact"),
            "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENT_REPORT_ARTIFACT",
        ),
        (
            "command_report_lineage_not_source",
            ("command_report_lineage_treated_as_source", "selected_command_report_lineage_treated_as_source"),
            ("treated_as_source", "command_report_lineage_treated_as_source"),
            "COMMAND_REPORT_LINEAGE_TREATED_AS_SOURCE",
        ),
        (
            "command_report_lineage_not_authority",
            ("command_report_lineage_treated_as_authority", "selected_command_report_lineage_treated_as_authority"),
            ("treated_as_authority", "command_report_lineage_treated_as_authority"),
            "COMMAND_REPORT_LINEAGE_TREATED_AS_AUTHORITY",
        ),
        (
            "command_report_lineage_not_currentness",
            ("command_report_lineage_treated_as_currentness", "selected_command_report_lineage_treated_as_currentness"),
            ("treated_as_currentness", "command_report_lineage_treated_as_currentness"),
            "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENTNESS",
        ),
    )
    for check_name, top_keys, nested_names, code in lineage_checks:
        overread = _any_truthy(request, top_keys, "selected_command_report_lineage_basis", nested_names)
        add(_check(check_name, not overread, "command report lineage is not authority material", "preserved", code))

    full_prior_body_emitted = _any_truthy(
        request,
        ("full_prior_artifact_body_emitted_outside_bounded_external_result", "raw_full_prior_artifact_body_returned"),
    ) or _any_selected_basis_truthy(
        request,
        (
            "full_prior_artifact_body_emitted_outside_bounded_external_result",
            "raw_full_prior_artifact_body_returned",
            "full_prior_artifact_body_emitted",
            "raw_full_prior_artifact_body_emitted",
        ),
    )
    add(_check(
        "full_prior_artifact_body_not_emitted_outside_bounded_external_result",
        not full_prior_body_emitted,
        "full prior artifact body not emitted outside bounded external-result posture",
        "not emitted" if not full_prior_body_emitted else "emitted",
        "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_EXTERNAL_RESULT",
    ))
    add(_check(
        "selected_basis_reference_shape_preserved",
        _as_bool(request.get("reference_shaped_input_posture", True)) and not _as_bool(request.get("selected_basis_not_reference_shaped")),
        "selected basis remains reference-shaped",
        str(request.get("reference_shaped_input_posture", True)),
        "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    ))

    direct_overreach = (
        ("second_carrier_external_result_treated_as_cross_carrier_evidence", "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_CROSS_CARRIER_EVIDENCE"),
        ("second_carrier_external_result_treated_as_portable_verification_closure", "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE"),
        ("second_carrier_external_result_treated_as_source_transfer", "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_SOURCE_TRANSFER"),
        ("second_carrier_external_result_treated_as_source_receipt", "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_SOURCE_RECEIPT"),
        ("second_carrier_external_result_treated_as_reception_authorization", "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_RECEPTION_AUTHORIZATION"),
        ("second_carrier_external_result_treated_as_source", "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_SOURCE"),
        ("second_carrier_external_result_treated_as_authority", "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_AUTHORITY"),
        ("second_carrier_external_result_treated_as_currentness", "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_CURRENTNESS"),
        ("second_carrier_external_result_treated_as_final_completion", "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_FINAL_COMPLETION"),
        ("second_carrier_external_result_treated_as_runtime", "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_RUNTIME"),
        ("second_carrier_external_result_treated_as_continuation", "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_CONTINUATION"),
        ("second_carrier_external_result_treated_as_reusable_permission", "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_REUSABLE_PERMISSION"),
        ("second_carrier_external_result_treated_as_follow_on_work", "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_AS_FOLLOW_ON_WORK"),
        ("cross_carrier_evidence_created", "CROSS_CARRIER_EVIDENCE_CREATED"),
        ("portable_verification_closure_created", "PORTABLE_VERIFICATION_CLOSURE_CREATED"),
        ("source_transfer_occurred", "SOURCE_TRANSFER_OCCURRED"),
        ("source_receipt_occurred", "SOURCE_RECEIPT_OCCURRED"),
        ("reception_authorization_created", "RECEPTION_AUTHORIZATION_CREATED"),
        ("source_created", "SOURCE_CREATED"),
        ("authority_created", "AUTHORITY_CREATED"),
        ("currentness_created", "CURRENTNESS_CREATED"),
        ("final_completion_claimed", "FINAL_COMPLETION_CLAIMED"),
        ("runtime_hosting_created", "RUNTIME_HOSTING_CREATED"),
        ("deployment_created", "DEPLOYMENT_CREATED"),
        ("public_release_created", "PUBLIC_RELEASE_CREATED"),
        ("operation_permission_created", "OPERATION_PERMISSION_CREATED"),
        ("continuation_authorized", "CONTINUATION_AUTHORIZED"),
        ("reusable_permission_created", "REUSABLE_PERMISSION_CREATED"),
        ("derivative_reception_authorized", "DERIVATIVE_RECEPTION_AUTHORIZED"),
        ("vessel_relation_authorized", "VESSEL_RELATION_AUTHORIZED"),
        ("another_reception_request_authorized", "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"),
        ("follow_on_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
        ("receiving_carrier_treated_as_authority", "RECEIVING_CARRIER_TREATED_AS_AUTHORITY"),
        ("artifact_existence_treated_as_external_result_authority", "ARTIFACT_EXISTENCE_TREATED_AS_EXTERNAL_RESULT_AUTHORITY"),
        ("artifact_path_treated_as_currentness", "ARTIFACT_PATH_TREATED_AS_CURRENTNESS"),
        ("repo_local_availability_treated_as_external_result_authority", "REPO_LOCAL_AVAILABILITY_TREATED_AS_EXTERNAL_RESULT_AUTHORITY"),
        ("hidden_repo_state_used_as_external_result_content", "HIDDEN_REPO_STATE_USED_AS_EXTERNAL_RESULT_CONTENT"),
        ("hidden_repo_state_used_as_external_result_authority", "HIDDEN_REPO_STATE_USED_AS_EXTERNAL_RESULT_AUTHORITY"),
        ("selected_basis_not_reference_shaped", "SELECTED_BASIS_NOT_REFERENCE_SHAPED"),
        ("raw_full_prior_artifact_body_returned", "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED"),
        ("predecessor_failure_evidence_hidden_or_repaired", "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
        ("first_success_boundary_test_hidden_or_repaired_or_claimed_passed", "FIRST_SUCCESS_BOUNDARY_TEST_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED"),
        ("first_result_boundary_resolver_hidden_or_repaired_or_claimed_passed", "FIRST_RESULT_BOUNDARY_RESOLVER_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED"),
        ("consumed_request_reopened", "CONSUMED_REQUEST_REOPENED"),
        ("authorization_token_reused", "AUTHORIZATION_TOKEN_REUSED"),
        ("string_zero_representation_turned_into_doctrine", "STRING_ZERO_REPRESENTATION_TURNED_INTO_DOCTRINE"),
        ("artifacts_mutated", "ARTIFACTS_MUTATED"),
        ("returned_capture_material_mutated", "RETURNED_CAPTURE_MATERIAL_MUTATED"),
    )
    for field, code in direct_overreach:
        value = _claim_value(request, field)
        add(_check(
            f"{field}_false",
            not _as_bool(value),
            f"{field} is false",
            str(value),
            code,
        ))

    for key in POSTURE_KEYS:
        add(_check(
            f"{key}_declared",
            _posture_declared(request, key),
            f"{key} declared",
            str(request.get(key)),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ))

    declared_non_claims = _declared_non_claims(request)
    non_claims_ok = all(key in declared_non_claims and declared_non_claims[key] is False for key in REQUIRED_FALSE_NON_CLAIMS)
    add(_check(
        "required_false_non_claims_explicit",
        non_claims_ok,
        "required non-claims false",
        "complete" if non_claims_ok else "missing or flipped",
        "NON_CLAIM_MISSING_OR_FLIPPED",
    ))

    return checks


def _metadata(request: Mapping[str, Any]) -> dict[str, Any]:
    request_id = str(request.get("second_carrier_external_result_request_id") or DEFAULT_REQUEST_ID)
    return {
        "portable_source_body_verification_second_carrier_external_result_id": request_id,
        "portable_source_body_verification_second_carrier_external_result_type": RESULT_TYPE,
        "portable_source_body_verification_second_carrier_external_result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
    }


def _declared_question_section(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "second_carrier_external_result_request_id": request.get("second_carrier_external_result_request_id"),
        "second_carrier_external_result_question": request.get("second_carrier_external_result_question"),
        "second_carrier_external_result_intent": request.get("second_carrier_external_result_intent"),
        "core_question": CORE_QUESTION,
        "second_carrier_external_result_spec_only": True,
    }


def _reference_section(request: Mapping[str, Any], key: str) -> dict[str, Any]:
    raw = request.get(key)
    if isinstance(raw, Mapping):
        section = _sanitize(raw)
    else:
        section = {"basis_value": _sanitize(raw)}
    if not isinstance(section, dict):
        section = {"basis_value": section}
    section.setdefault("selected_basis_key", key)
    section.setdefault("basis_only", True)
    section.setdefault("selected_basis_reference_shape_preserved", True)
    section.setdefault("repo_local_availability_not_external_result_authority", True)
    section.setdefault("hidden_repo_state_excluded", True)
    section.setdefault("raw_full_prior_artifact_body_not_returned", True)
    return section


def _posture_section(request: Mapping[str, Any], key: str) -> dict[str, Any]:
    return {
        "posture_key": key,
        "declared": _posture_declared(request, key),
        "basis_only": True,
        "does_not_create_cross_carrier_evidence": True,
        "does_not_create_portable_verification_closure": True,
        "does_not_create_source_authority_currentness_runtime_or_follow_on": True,
    }


def _scope_section(request: Mapping[str, Any]) -> dict[str, Any]:
    values = _scope_values(request)
    return {
        "scope_values": values,
        "supported_scope_values": list(SUPPORTED_SCOPE_VALUES),
        "unsupported_scope_values": _unsupported_scope_values(request),
        "official_enum_scope_strings_not_redacted": True,
    }


def _statement(outcome: str) -> dict[str, bool]:
    recorded = outcome == OUTCOME_RECORDED
    return {key: bool(recorded) for key in ALLOWED_TRUE_RECORDED_FIELDS}


def _non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _non_meaning() -> dict[str, bool]:
    return {
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
        "external_result_became_cross_carrier_proof": False,
        "external_result_became_portable_verification_closure": False,
        "external_result_became_source_transfer_source_receipt_or_reception_authorization": False,
        "external_result_became_source_authority_or_currentness": False,
        "external_result_artifact_became_cross_carrier_evidence_or_portable_verification_closure": False,
        "returned_capture_became_cross_carrier_proof": False,
        "zero_exit_code_became_external_result_automatically": False,
        "string_zero_became_external_result_automatically": False,
        "string_zero_became_doctrine": False,
        "ok_became_external_result_automatically": False,
        "ran_7_tests_became_cross_carrier_proof": False,
        "macbook_pro_became_authority": False,
        "macbook_air_became_source": False,
        "artifact_existence_became_external_result_authority": False,
        "artifact_path_became_currentness": False,
        "repo_local_availability_became_external_result_authority": False,
        "hidden_repo_state_became_external_result_authority": False,
        "first_success_boundary_test_was_repaired_hidden_erased_or_claimed_passed": False,
        "first_result_boundary_resolver_was_repaired_hidden_erased_or_claimed_passed": False,
        "v1_packet_emission_boundary_resolver_was_repaired_hidden_erased_or_claimed_passed": False,
    }


def _additional_basis_required(outcome: str, checks: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    required = outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    return {
        "additional_basis_required": required,
        "missing_or_unclear_basis": [check.get("check_name") for check in _failed_checks(checks)] if required else [],
        "missing_basis_scheduled": False,
        "missing_basis_authorized": False,
        "missing_basis_executed": False,
    }


def _not_recorded_basis(outcome: str, checks: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    not_recorded = outcome == OUTCOME_NOT_RECORDED
    return {
        "not_recorded": not_recorded,
        "failed_review_basis": [check.get("check_name") for check in _failed_checks(checks)] if not_recorded else [],
        "prior_artifacts_mutated": False,
        "prior_artifacts_repaired": False,
        "next_work_authorized": False,
    }


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "second-carrier external-result test",
            "second-carrier external-result live artifact",
            "second-carrier external-result terminal summary, if needed",
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


def _block(outcome: str, checks: Sequence[Mapping[str, Any]], explicit_reason: str | None = None) -> dict[str, Any] | None:
    if outcome != OUTCOME_BLOCKED:
        return None
    code = _first_failed_code(checks) or "DECLARED_SECOND_CARRIER_EXTERNAL_RESULT_REQUEST_MALFORMED"
    return {
        "blocked": True,
        "block_code": code,
        "block_reason": explicit_reason or code,
        "cross_carrier_evidence_created": False,
        "portable_verification_closure_created": False,
        "source_authority_currentness_runtime_final_completion_or_follow_on_created": False,
    }


def _summary_from_parts(
    request: Mapping[str, Any],
    outcome: str,
    checks: Sequence[Mapping[str, Any]],
    statement: Mapping[str, Any],
    non_claims: Mapping[str, Any],
    block: Mapping[str, Any] | None,
) -> dict[str, Any]:
    failed_count = len(_failed_checks(checks))
    summary: dict[str, Any] = {
        "outcome": outcome,
        "block_code": None if block is None else block.get("block_code"),
        "block_reason": None if block is None else block.get("block_reason"),
        "request_id": request.get("second_carrier_external_result_request_id"),
        "question": request.get("second_carrier_external_result_question"),
        "intent": request.get("second_carrier_external_result_intent"),
        "passed_check_count": len(checks) - failed_count,
        "failed_check_count": failed_count,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "selected_second_carrier_external_result_boundary_outcome": request.get("selected_second_carrier_external_result_boundary_result_outcome"),
        "selected_second_carrier_external_result_boundary_result_version": request.get("selected_second_carrier_external_result_boundary_result_version"),
        "selected_second_carrier_external_result_boundary_failed_check_count": request.get("selected_second_carrier_external_result_boundary_failed_check_count"),
        "selected_second_carrier_verification_outcome": request.get("selected_second_carrier_verification_result_outcome"),
        "selected_second_carrier_verification_result_version": request.get("selected_second_carrier_verification_result_version"),
        "selected_second_carrier_verification_failed_check_count": request.get("selected_second_carrier_verification_failed_check_count"),
        "selected_returned_capture_intake_path": request.get("selected_returned_capture_intake_path"),
        "selected_returned_capture_zip_path": request.get("selected_returned_capture_zip_path"),
        "selected_returned_capture_hash_path": request.get("selected_returned_capture_hash_path"),
        "selected_returned_capture_extracted_directory_path": request.get("selected_returned_capture_extracted_directory_path"),
        "selected_returned_capture_exit_code": request.get("selected_returned_capture_exit_code"),
        "selected_returned_capture_declared_exit_code": request.get("selected_returned_capture_declared_exit_code"),
        "selected_returned_capture_ok_line": request.get("selected_returned_capture_ok_line"),
        "no_cross_carrier_evidence_or_portable_closure": True,
        "no_source_authority_currentness_final_completion_or_runtime": True,
        "no_deployment_public_release_or_follow_on": True,
        "first_success_boundary_test_failure_preserved": True,
        "v1_predecessor_failure_preserved": True,
        "v1_not_repaired_hidden_or_claimed_passed": True,
        "first_result_boundary_resolver_failure_preserved": True,
    }
    summary.update({key: bool(statement.get(key)) for key in ALLOWED_TRUE_RECORDED_FIELDS})
    summary.update({key: bool(non_claims.get(key)) for key in REQUIRED_FALSE_NON_CLAIMS})
    return summary


def build_portable_source_body_verification_second_carrier_external_result_summary(
    result: Mapping[str, Any]
) -> dict[str, Any]:
    summary = result.get("portable_source_body_verification_second_carrier_external_result_summary")
    if isinstance(summary, Mapping):
        return dict(summary)
    checks = result.get("second_carrier_external_result_checks", [])
    if not isinstance(checks, Sequence) or isinstance(checks, (str, bytes, bytearray)):
        checks = []
    request = result.get("declared_second_carrier_external_result_question", {})
    if not isinstance(request, Mapping):
        request = {}
    statement = result.get("second_carrier_external_result_statement", {})
    if not isinstance(statement, Mapping):
        statement = {}
    non_claims = result.get("non_claims", {})
    if not isinstance(non_claims, Mapping):
        non_claims = {}
    block = result.get("block")
    return _summary_from_parts(
        request,
        str(result.get("outcome")),
        checks,  # type: ignore[arg-type]
        statement,
        non_claims,
        block if isinstance(block, Mapping) else None,
    )


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: Sequence[Mapping[str, Any]],
    explicit_block_reason: str | None = None,
) -> dict[str, Any]:
    statement = _statement(outcome)
    non_claims = _non_claims()
    block = _block(outcome, checks, explicit_block_reason)
    result: dict[str, Any] = {
        "portable_source_body_verification_second_carrier_external_result_metadata": _metadata(request),
        "declared_second_carrier_external_result_question": _declared_question_section(request),
        "second_carrier_external_result_scope": _scope_section(request),
        "second_carrier_external_result_checks": [dict(check) for check in checks],
        "second_carrier_external_result_statement": statement,
        "second_carrier_external_result_non_meaning": _non_meaning(),
        "additional_basis_required": _additional_basis_required(outcome, checks),
        "not_recorded_basis": _not_recorded_basis(outcome, checks),
        "what_remains_open": _what_remains_open(),
        "non_claims": non_claims,
        "outcome": outcome,
        "block": block,
    }
    for key in SELECTED_BASIS_KEYS:
        result[key] = _reference_section(request, key)
    for key in POSTURE_KEYS:
        result[key] = _posture_section(request, key)

    summary = _summary_from_parts(request, outcome, checks, statement, non_claims, block)
    result["portable_source_body_verification_second_carrier_external_result_summary"] = summary
    ordered_keys = (
        "portable_source_body_verification_second_carrier_external_result_metadata",
        "declared_second_carrier_external_result_question",
        *SELECTED_BASIS_KEYS,
        *POSTURE_KEYS,
        "second_carrier_external_result_scope",
        "second_carrier_external_result_checks",
        "second_carrier_external_result_statement",
        "second_carrier_external_result_non_meaning",
        "additional_basis_required",
        "not_recorded_basis",
        "what_remains_open",
        "non_claims",
        "outcome",
        "block",
        "portable_source_body_verification_second_carrier_external_result_summary",
    )
    return {key: result[key] for key in ordered_keys}


def _malformed_result(reason: str, code: str = "DECLARED_SECOND_CARRIER_EXTERNAL_RESULT_REQUEST_MALFORMED") -> dict[str, Any]:
    request = build_declared_portable_source_body_verification_second_carrier_external_result_request()
    checks = [_check("declared_second_carrier_external_result_request_mapping", False, "JSON object mapping", reason, code)]
    return _build_result(request, OUTCOME_BLOCKED, checks, reason)


def resolve_portable_source_body_verification_second_carrier_external_result(
    declared_second_carrier_external_result_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    if declared_second_carrier_external_result_request is None:
        return _malformed_result("request missing")
    if not isinstance(declared_second_carrier_external_result_request, Mapping):
        return _malformed_result("request is not a mapping")

    request = _deepcopy_request(declared_second_carrier_external_result_request)
    if request.get("second_carrier_external_result_intent") == INTENT_BLOCK:
        checks = [_check(
            "second_carrier_external_result_intent_explicit_block",
            False,
            "intent is not explicit block",
            INTENT_BLOCK,
            "SECOND_CARRIER_EXTERNAL_RESULT_INTENT_UNSUPPORTED",
        )]
        return _build_result(request, OUTCOME_BLOCKED, checks, "explicit block intent")
    if request.get("second_carrier_external_result_intent") == INTENT_DO_NOT_RECORD:
        checks = _evaluate_checks(request)
        return _build_result(request, OUTCOME_NOT_RECORDED, checks, "do-not-record intent")

    checks = _evaluate_checks(request)
    outcome = OUTCOME_RECORDED if not _failed_checks(checks) else OUTCOME_BLOCKED
    return _build_result(request, outcome, checks)


def resolve_portable_source_body_verification_second_carrier_external_result_from_path(
    declared_second_carrier_external_result_request_path: Path | str,
) -> dict[str, Any]:
    path = Path(declared_second_carrier_external_result_request_path)
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise PortableSourceBodyVerificationSecondCarrierExternalResultError(
            f"Declared second-carrier external-result request path is unreadable: {path}"
        ) from exc
    except json.JSONDecodeError as exc:
        raise PortableSourceBodyVerificationSecondCarrierExternalResultError(
            f"Declared second-carrier external-result request JSON is malformed: {path}"
        ) from exc
    if not isinstance(payload, Mapping):
        return _malformed_result("request JSON must be an object")
    return resolve_portable_source_body_verification_second_carrier_external_result(payload)


def write_portable_source_body_verification_second_carrier_external_result_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    metadata = result.get("portable_source_body_verification_second_carrier_external_result_metadata", {})
    if isinstance(metadata, Mapping):
        request_id = str(
            metadata.get("portable_source_body_verification_second_carrier_external_result_id")
            or DEFAULT_REQUEST_ID
        )
    else:
        request_id = DEFAULT_REQUEST_ID
    if output_path is None:
        target = OUTPUT_ROOT / f"{request_id}__portable_source_body_verification_second_carrier_external_result_result.json"
    else:
        target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    final_target = target
    if final_target.exists():
        stem = target.stem
        suffix = target.suffix
        counter = 1
        while final_target.exists():
            final_target = target.with_name(f"{stem}_{counter:03d}{suffix}")
            counter += 1
    final_target.write_text(json.dumps(_sanitize(dict(result)), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return final_target


def build_declared_portable_source_body_verification_second_carrier_external_result_request(
    **overrides: Any,
) -> dict[str, Any]:
    request: dict[str, Any] = {
        "second_carrier_external_result_request_id": DEFAULT_REQUEST_ID,
        "second_carrier_external_result_question": CORE_QUESTION,
        "second_carrier_external_result_intent": INTENT_RECORD,
        "second_carrier_external_result_scope": list(SUPPORTED_SCOPE_VALUES),
        "declared_non_claims": {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
        "reference_shaped_input_posture": True,
        "selected_second_carrier_external_result_boundary_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_external_result_boundary/"
            "portable_source_body_verification_second_carrier_external_result_boundary_reference_review_001__"
            "portable_source_body_verification_second_carrier_external_result_boundary_result.json"
        ),
        "selected_second_carrier_external_result_boundary_result_outcome": EXPECTED_BOUNDARY_OUTCOME,
        "selected_second_carrier_external_result_boundary_result_version": RESULT_VERSION,
        "selected_second_carrier_external_result_boundary_failed_check_count": 0,
        "selected_second_carrier_external_result_boundary_declared_future_external_result_step": True,
        "selected_second_carrier_external_result_boundary_already_created_external_result": False,
        "selected_second_carrier_external_result_boundary_already_created_cross_carrier_evidence": False,
        "selected_second_carrier_external_result_boundary_already_created_portable_verification_closure": False,
        "selected_second_carrier_external_result_boundary_treated_external_result_boundary_as_external_result": False,
        "selected_second_carrier_external_result_boundary_treated_external_result_boundary_as_cross_carrier_evidence": False,
        "selected_second_carrier_external_result_boundary_treated_external_result_boundary_as_portable_verification_closure": False,
        "selected_second_carrier_external_result_boundary_zero_exit_code_not_external_result": True,
        "selected_second_carrier_external_result_boundary_string_zero_not_external_result": True,
        "selected_second_carrier_external_result_boundary_ok_not_external_result": True,
        "selected_second_carrier_external_result_boundary_ran_7_tests_not_cross_carrier_proof": True,
        "selected_second_carrier_external_result_boundary_official_enum_scope_strings_redacted": False,
        "selected_second_carrier_external_result_boundary_first_success_boundary_test_failure_preserved": True,
        "selected_second_carrier_verification_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_verification/"
            "portable_source_body_verification_second_carrier_verification_reference_review_001__"
            "portable_source_body_verification_second_carrier_verification_result.json"
        ),
        "selected_second_carrier_verification_result_outcome": EXPECTED_VERIFICATION_OUTCOME,
        "selected_second_carrier_verification_result_version": RESULT_VERSION,
        "selected_second_carrier_verification_failed_check_count": 0,
        "selected_second_carrier_verification_bounded_verification_recorded": True,
        "selected_second_carrier_verification_already_created_external_result": False,
        "selected_second_carrier_verification_already_created_cross_carrier_evidence": False,
        "selected_second_carrier_verification_already_created_portable_verification_closure": False,
        "selected_second_carrier_verification_treated_verification_as_external_result": False,
        "selected_second_carrier_verification_treated_verification_as_cross_carrier_evidence": False,
        "selected_second_carrier_verification_zero_exit_code_not_external_result": True,
        "selected_second_carrier_verification_string_zero_not_external_result": True,
        "selected_second_carrier_verification_ok_not_external_result": True,
        "selected_second_carrier_verification_ran_7_tests_not_cross_carrier_proof": True,
        "selected_second_carrier_verification_boundary_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_verification_boundary/"
            "portable_source_body_verification_second_carrier_verification_boundary_reference_review_001__"
            "portable_source_body_verification_second_carrier_verification_boundary_result.json"
        ),
        "selected_second_carrier_verification_boundary_result_outcome": EXPECTED_VERIFICATION_BOUNDARY_OUTCOME,
        "selected_second_carrier_verification_boundary_failed_check_count": 0,
        "selected_second_carrier_success_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_success/"
            "portable_source_body_verification_second_carrier_success_reference_review_001__"
            "portable_source_body_verification_second_carrier_success_result.json"
        ),
        "selected_second_carrier_success_result_outcome": EXPECTED_SUCCESS_OUTCOME,
        "selected_second_carrier_success_failed_check_count": 0,
        "selected_second_carrier_result_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_result/"
            "portable_source_body_verification_second_carrier_result_reference_review_001__"
            "portable_source_body_verification_second_carrier_result_result.json"
        ),
        "selected_second_carrier_result_result_outcome": EXPECTED_RESULT_OUTCOME,
        "selected_second_carrier_result_failed_check_count": 0,
        "selected_returned_capture_intake_path": (
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_RETURNED_SECOND_CARRIER_LIVE_CAPTURE_INTAKE_V0.md"
        ),
        "selected_returned_capture_intake_preserved": True,
        "selected_returned_capture_intake_capture_only": True,
        "selected_returned_capture_from_macbook_pro_to_macbook_air": True,
        "selected_returned_capture_zip_path": (
            "artifacts/actual_second_carrier_live_capture/portable_source_body_verification_actual_second_carrier_capture_001/"
            "original_zip/iammai_second_carrier_capture_001.zip"
        ),
        "selected_returned_capture_hash_path": (
            "artifacts/actual_second_carrier_live_capture/portable_source_body_verification_actual_second_carrier_capture_001/"
            "hashes/iammai_second_carrier_capture_001.sha256"
        ),
        "selected_returned_capture_extracted_directory_path": (
            "artifacts/actual_second_carrier_live_capture/portable_source_body_verification_actual_second_carrier_capture_001/"
            "extracted/iammai_second_carrier_capture_001"
        ),
        "selected_returned_capture_combined_terminal_log_path": (
            "artifacts/actual_second_carrier_live_capture/portable_source_body_verification_actual_second_carrier_capture_001/"
            "extracted/iammai_second_carrier_capture_001/combined_terminal_log.txt"
        ),
        "selected_returned_capture_stdout_path": (
            "artifacts/actual_second_carrier_live_capture/portable_source_body_verification_actual_second_carrier_capture_001/"
            "extracted/iammai_second_carrier_capture_001/stdout.txt"
        ),
        "selected_returned_capture_stderr_path": (
            "artifacts/actual_second_carrier_live_capture/portable_source_body_verification_actual_second_carrier_capture_001/"
            "extracted/iammai_second_carrier_capture_001/stderr.txt"
        ),
        "selected_returned_capture_command_text": (
            "python -m unittest tests.test_resolve_portable_source_body_verification_second_carrier_verification"
        ),
        "selected_returned_capture_working_directory": "/Users/markomarkota/IAMMAI-SYSTEM",
        "selected_returned_capture_started_at": "2026-05-10T00:00:00Z",
        "selected_returned_capture_completed_at": "2026-05-10T00:00:01Z",
        "selected_returned_capture_exit_code": 0,
        "selected_returned_capture_declared_exit_code": "0",
        "selected_returned_capture_ran_7_tests_line": "Ran 7 tests in 0.451s",
        "selected_returned_capture_ok_line": "OK",
        "selected_returned_capture_raw_placeholder_carrier_label": "CARRIER_LABEL_PLACEHOLDER",
        "selected_returned_capture_raw_placeholder_carrier_type": "CARRIER_TYPE_PLACEHOLDER",
        "selected_returned_capture_placeholder_fields_unrepaired": True,
        "selected_second_carrier_output_capture_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_output_capture/"
            "portable_source_body_verification_second_carrier_output_capture_reference_review_001__"
            "portable_source_body_verification_second_carrier_output_capture_result.json"
        ),
        "selected_second_carrier_output_capture_result_outcome": EXPECTED_OUTPUT_CAPTURE_OUTCOME,
        "selected_second_carrier_output_capture_failed_check_count": 0,
        "returned_capture_treated_as_external_result": False,
        "returned_capture_treated_as_cross_carrier_proof": False,
        "zero_exit_code_treated_as_external_result": False,
        "string_zero_treated_as_external_result": False,
        "ok_output_treated_as_external_result": False,
        "ran_7_tests_treated_as_cross_carrier_proof": False,
        "command_report_lineage_treated_as_current_report_artifact": False,
        "command_report_lineage_treated_as_source": False,
        "command_report_lineage_treated_as_authority": False,
        "command_report_lineage_treated_as_currentness": False,
        "selected_command_report_lineage_treated_as_current_report_artifact": False,
        "selected_command_report_lineage_treated_as_source": False,
        "selected_command_report_lineage_treated_as_authority": False,
        "selected_command_report_lineage_treated_as_currentness": False,
        "full_prior_artifact_body_emitted_outside_bounded_external_result": False,
        "raw_full_prior_artifact_body_returned": False,
        "selected_second_carrier_external_result_boundary_basis": {
            "basis_id": "second_carrier_external_result_boundary_basis",
            "outcome": EXPECTED_BOUNDARY_OUTCOME,
            "result_version": RESULT_VERSION,
        },
        "selected_second_carrier_external_result_boundary_terminal_summary_basis": {
            "basis_id": "second_carrier_external_result_boundary_terminal_summary",
            "external_result_not_created_before_this_step": True,
        },
        "selected_second_carrier_verification_basis": {
            "basis_id": "second_carrier_verification_basis",
            "outcome": EXPECTED_VERIFICATION_OUTCOME,
            "already_created_external_result": False,
            "already_created_cross_carrier_evidence": False,
            "already_created_portable_verification_closure": False,
        },
        "selected_second_carrier_verification_terminal_summary_basis": {
            "basis_id": "second_carrier_verification_terminal_summary",
            "bounded_verification_posture": True,
        },
        "selected_second_carrier_verification_boundary_basis": {
            "basis_id": "second_carrier_verification_boundary_basis",
            "outcome": EXPECTED_VERIFICATION_BOUNDARY_OUTCOME,
        },
        "selected_second_carrier_success_basis": {
            "basis_id": "second_carrier_success_basis",
            "outcome": EXPECTED_SUCCESS_OUTCOME,
        },
        "selected_second_carrier_result_basis": {
            "basis_id": "second_carrier_result_basis",
            "outcome": EXPECTED_RESULT_OUTCOME,
        },
        "selected_second_carrier_result_terminal_summary_basis": {
            "basis_id": "second_carrier_result_terminal_summary",
            "bounded_result_posture": True,
        },
        "selected_returned_second_carrier_live_capture_intake_basis": {
            "basis_id": "returned_second_carrier_live_capture_intake",
            "capture_only": True,
        },
        "selected_returned_capture_material_basis": {
            "basis_id": "returned_capture_material",
            "exit_code": 0,
            "declared_exit_code": "0",
            "ok_line": "OK",
        },
        "selected_second_carrier_output_capture_basis": {
            "basis_id": "second_carrier_output_capture_basis",
            "outcome": EXPECTED_OUTPUT_CAPTURE_OUTCOME,
        },
        "selected_packet_transfer_basis": {"basis_id": "packet_transfer_basis"},
        "selected_packet_emission_basis": {"basis_id": "packet_emission_basis"},
        "selected_packet_emission_boundary_v2_basis": {"basis_id": "packet_emission_boundary_v2_basis"},
        "selected_packet_emission_boundary_v1_predecessor_failure_basis": {
            "basis_id": "packet_emission_boundary_v1_predecessor_failure_basis",
            "predecessor_failure_preserved": True,
        },
        "selected_packet_artifact_basis": {"basis_id": "packet_artifact_basis"},
        "selected_command_success_basis": {"basis_id": "command_success_basis"},
        "selected_command_result_v2_basis": {"basis_id": "command_result_v2_basis"},
        "selected_output_capture_v2_basis": {"basis_id": "output_capture_v2_basis"},
        "selected_command_output_report_artifact_basis": {"basis_id": "command_output_report_artifact_basis"},
        "selected_command_execution_basis": {"basis_id": "command_execution_basis"},
        "selected_command_report_lineage_basis": {
            "basis_id": "command_report_lineage_basis",
            "treated_as_current_report_artifact": False,
            "treated_as_source": False,
            "treated_as_authority": False,
            "treated_as_currentness": False,
        },
        "selected_predecessor_failure_basis": {
            "first_success_boundary_test_failure_preserved": True,
            "first_result_boundary_resolver_failure_preserved": True,
            "v1_packet_emission_boundary_failure_preserved": True,
        },
        "selected_evidence_manifest_basis": {"basis_id": "evidence_manifest_basis"},
        "selected_artifact_containment_basis": {
            "basis_id": "artifact_containment_basis",
            "raw_full_prior_artifact_body_not_returned": True,
        },
        "selected_portable_verification_basis": {"basis_id": "portable_verification_basis"},
    }
    for key in POSTURE_KEYS:
        request[key] = True
    request.update(overrides)
    return request
