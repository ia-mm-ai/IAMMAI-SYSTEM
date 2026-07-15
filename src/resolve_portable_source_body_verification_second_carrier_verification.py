"""Bounded portable source-body verification second-carrier verification resolver.

This module records one bounded second-carrier verification posture from clean
second-carrier-verification-boundary basis. It does not create external result,
cross-carrier evidence, portable verification closure, source transfer, source
receipt, reception authorization, source, authority, currentness, runtime, final
completion, continuation, reusable permission, or follow-on work.
"""

from pathlib import Path
import json
import datetime
import copy
from typing import Any, Iterable, Mapping


class PortableSourceBodyVerificationSecondCarrierVerificationError(Exception):
    """Bounded resolver error for unreadable paths or impossible result shape."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_portable_source_body_verification_second_carrier_verification"

OUTCOME_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_VERIFICATION_RECORDED"
OUTCOME_NOT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_VERIFICATION_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_VERIFICATION_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_VERIFICATION_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_verification"
)

RECORD_INTENT = "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_VERIFICATION"
DO_NOT_RECORD_INTENT = "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_VERIFICATION"
BLOCK_INTENT = "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_VERIFICATION"
SUPPORTED_INTENTS = (RECORD_INTENT, DO_NOT_RECORD_INTENT, BLOCK_INTENT)

REQUIRED_QUESTION = (
    "Can the clean second-carrier-verification-boundary basis be used to record "
    "one bounded second-carrier verification posture without creating external "
    "result, cross-carrier evidence, portable verification closure, source "
    "transfer, source receipt, reception authorization, source, authority, "
    "currentness, runtime, final completion, continuation, reusable permission, "
    "derivative reception, vessel relation, another reception request, or "
    "follow-on work?"
)

BOUNDARY_OUTCOME_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_VERIFICATION_BOUNDARY_RECORDED"
)
SUCCESS_OUTCOME_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_SUCCESS_RECORDED"
SUCCESS_BOUNDARY_OUTCOME_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_SUCCESS_BOUNDARY_RECORDED"
)
RESULT_OUTCOME_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RESULT_RECORDED"
OUTPUT_CAPTURE_OUTCOME_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_OUTPUT_CAPTURE_RECORDED"
)

SUPPORTED_SCOPE_VALUES = (
    "SECOND_CARRIER_VERIFICATION_SPEC_ONLY",
    "ONE_BOUNDED_SECOND_CARRIER_VERIFICATION_RECORDED",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_BASIS_PRESERVED",
    "SECOND_CARRIER_SUCCESS_BASIS_PRESERVED",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_BASIS_PRESERVED",
    "SECOND_CARRIER_RESULT_BASIS_PRESERVED",
    "RETURNED_SECOND_CARRIER_CAPTURE_BASIS_PRESERVED",
    "CAPTURE_INTAKE_BASIS_PRESERVED",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_PRESERVED",
    "VERIFICATION_RECORDED_BOUNDED",
    "VERIFICATION_ARTIFACT_RECORDED_OR_BOUNDED",
    "VERIFICATION_NOT_EXTERNAL_RESULT",
    "VERIFICATION_NOT_CROSS_CARRIER_EVIDENCE",
    "VERIFICATION_NOT_PORTABLE_VERIFICATION_CLOSURE",
    "VERIFICATION_NOT_SOURCE_TRANSFER",
    "VERIFICATION_NOT_SOURCE_RECEIPT",
    "VERIFICATION_NOT_RECEPTION_AUTHORIZATION",
    "ZERO_EXIT_CODE_NOT_VERIFICATION_AS_STANDALONE_INFERENCE",
    "OK_OUTPUT_NOT_VERIFICATION_AS_STANDALONE_INFERENCE",
    "RAN_7_TESTS_NOT_CROSS_CARRIER_PROOF",
    "RETURNED_CAPTURE_NOT_CROSS_CARRIER_PROOF",
    "EXTERNAL_RESULT_NOT_CREATED",
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
SUPPORTED_SECOND_CARRIER_VERIFICATION_SCOPE = SUPPORTED_SCOPE_VALUES

REQUIRED_FALSE_NON_CLAIMS = (
    "external_result_created",
    "cross_carrier_evidence_created",
    "portable_verification_closure_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "second_carrier_verification_treated_as_external_result",
    "second_carrier_verification_treated_as_cross_carrier_evidence",
    "second_carrier_verification_treated_as_portable_verification_closure",
    "second_carrier_verification_treated_as_source_transfer",
    "second_carrier_verification_treated_as_source_receipt",
    "second_carrier_verification_treated_as_reception_authorization",
    "second_carrier_verification_treated_as_source",
    "second_carrier_verification_treated_as_authority",
    "second_carrier_verification_treated_as_currentness",
    "second_carrier_verification_treated_as_final_completion",
    "second_carrier_verification_treated_as_runtime",
    "second_carrier_verification_treated_as_continuation",
    "second_carrier_verification_treated_as_reusable_permission",
    "second_carrier_verification_treated_as_follow_on_work",
    "zero_exit_code_treated_as_verification_standalone",
    "ok_output_treated_as_verification_standalone",
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

ALLOWED_TRUE_RECORDED_FIELDS = (
    "second_carrier_verification_recorded",
    "bounded_second_carrier_verification_recorded",
    "verification_artifact_recorded_or_bounded",
    "second_carrier_verification_boundary_basis_preserved",
    "second_carrier_success_basis_preserved",
    "returned_second_carrier_capture_basis_preserved",
    "capture_intake_basis_preserved",
    "second_carrier_output_capture_basis_preserved",
    "verification_recorded_bounded",
    "verification_not_external_result",
    "verification_not_cross_carrier_evidence",
    "verification_not_portable_verification_closure",
    "verification_not_source_transfer",
    "verification_not_source_receipt",
    "verification_not_reception_authorization",
    "zero_exit_code_not_verification_as_standalone_inference",
    "ok_output_not_verification_as_standalone_inference",
    "ran_7_tests_not_cross_carrier_proof",
    "returned_capture_not_cross_carrier_proof",
    "external_result_not_created",
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

BLOCK_CODES = (
    "DECLARED_SECOND_CARRIER_VERIFICATION_REQUEST_MALFORMED",
    "DECLARED_SECOND_CARRIER_VERIFICATION_REQUEST_UNREADABLE",
    "DECLARED_SECOND_CARRIER_VERIFICATION_REQUEST_BLOCKED",
    "SECOND_CARRIER_VERIFICATION_QUESTION_UNDECLARED",
    "SECOND_CARRIER_VERIFICATION_INTENT_UNSUPPORTED",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_BASIS_MISSING",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_NOT_RECORDED",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_VERSION_NOT_0_1_0",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_DID_NOT_DECLARE_FUTURE_VERIFICATION_STEP",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_ALREADY_CREATED_VERIFICATION",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_ALREADY_CREATED_EXTERNAL_RESULT",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_ALREADY_CREATED_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_ALREADY_CREATED_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_VERIFICATION_BOUNDARY_AS_VERIFICATION",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_VERIFICATION_BOUNDARY_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_VERIFICATION_BOUNDARY_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_VERIFICATION_BOUNDARY_AS_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_ZERO_EXIT_CODE_AS_VERIFICATION",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_OK_AS_VERIFICATION",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_RAN_7_TESTS_AS_CROSS_CARRIER_PROOF",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
    "SECOND_CARRIER_SUCCESS_BASIS_MISSING",
    "SECOND_CARRIER_SUCCESS_NOT_RECORDED",
    "SECOND_CARRIER_SUCCESS_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_SUCCESS_ALREADY_CREATED_VERIFICATION",
    "SECOND_CARRIER_SUCCESS_ALREADY_CREATED_EXTERNAL_RESULT",
    "SECOND_CARRIER_SUCCESS_ALREADY_CREATED_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_SUCCESS_ALREADY_CREATED_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_SUCCESS_TREATED_SUCCESS_AS_VERIFICATION",
    "SECOND_CARRIER_SUCCESS_TREATED_SUCCESS_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_SUCCESS_TREATED_ZERO_EXIT_CODE_AS_VERIFICATION",
    "SECOND_CARRIER_SUCCESS_TREATED_OK_AS_VERIFICATION",
    "SECOND_CARRIER_SUCCESS_TREATED_RAN_7_TESTS_AS_CROSS_CARRIER_PROOF",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_BASIS_MISSING",
    "SECOND_CARRIER_RESULT_BASIS_MISSING",
    "SECOND_CARRIER_RESULT_NOT_RECORDED",
    "SECOND_CARRIER_RESULT_FAILED_CHECKS_PRESENT",
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
    "SECOND_CARRIER_VERIFICATION_TREATED_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_VERIFICATION_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_VERIFICATION_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_VERIFICATION_TREATED_AS_SOURCE_TRANSFER",
    "SECOND_CARRIER_VERIFICATION_TREATED_AS_SOURCE_RECEIPT",
    "SECOND_CARRIER_VERIFICATION_TREATED_AS_RECEPTION_AUTHORIZATION",
    "SECOND_CARRIER_VERIFICATION_TREATED_AS_SOURCE",
    "SECOND_CARRIER_VERIFICATION_TREATED_AS_AUTHORITY",
    "SECOND_CARRIER_VERIFICATION_TREATED_AS_CURRENTNESS",
    "SECOND_CARRIER_VERIFICATION_TREATED_AS_FINAL_COMPLETION",
    "SECOND_CARRIER_VERIFICATION_TREATED_AS_RUNTIME",
    "SECOND_CARRIER_VERIFICATION_TREATED_AS_CONTINUATION",
    "SECOND_CARRIER_VERIFICATION_TREATED_AS_REUSABLE_PERMISSION",
    "SECOND_CARRIER_VERIFICATION_TREATED_AS_FOLLOW_ON_WORK",
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
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_VERIFICATION",
    "ARTIFACTS_MUTATED",
    "RETURNED_CAPTURE_MATERIAL_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_SECOND_CARRIER_VERIFICATION_SCOPE",
)

SELECTED_BASIS_FIELDS = (
    "selected_second_carrier_verification_boundary_basis",
    "selected_second_carrier_verification_boundary_terminal_summary_basis",
    "selected_second_carrier_success_basis",
    "selected_second_carrier_success_terminal_summary_basis",
    "selected_second_carrier_success_boundary_basis",
    "selected_second_carrier_result_basis",
    "selected_second_carrier_result_terminal_summary_basis",
    "selected_second_carrier_result_boundary_v2_basis",
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

POSTURE_FIELDS = (
    "second_carrier_verification_spec_only_posture",
    "one_bounded_second_carrier_verification_posture",
    "second_carrier_verification_boundary_basis_preserved_posture",
    "second_carrier_success_basis_preserved_posture",
    "second_carrier_success_boundary_basis_preserved_posture",
    "second_carrier_result_basis_preserved_posture",
    "returned_second_carrier_capture_basis_preserved_posture",
    "capture_intake_basis_preserved_posture",
    "second_carrier_output_capture_basis_preserved_posture",
    "verification_recorded_bounded_posture",
    "verification_artifact_recorded_or_bounded_posture",
    "verification_not_external_result_posture",
    "verification_not_cross_carrier_evidence_posture",
    "verification_not_portable_verification_closure_posture",
    "verification_not_source_transfer_posture",
    "verification_not_source_receipt_posture",
    "verification_not_reception_authorization_posture",
    "zero_exit_code_not_verification_as_standalone_inference_posture",
    "ok_output_not_verification_as_standalone_inference_posture",
    "ran_7_tests_not_cross_carrier_proof_posture",
    "returned_capture_not_cross_carrier_proof_posture",
    "external_result_not_created_posture",
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
    "hidden_repo_state_not_used_as_verification_authority_posture",
    "repo_local_availability_not_verification_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "first_success_boundary_test_failure_preserved_posture",
    "first_result_boundary_resolver_failure_preserved_posture",
    "authorization_token_reuse_blocked_posture",
    "consumed_request_token_remains_closed_posture",
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
HOSTILE_SENTINELS = (
    "RAW_SECOND_CARRIER_VERIFICATION_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)
REDACTED_CONTENT = "[bounded-redacted-raw-or-hidden-state]"


def _official_strings() -> set[str]:
    return set(SUPPORTED_SCOPE_VALUES) | set(BLOCK_CODES) | set(OUTCOME_FAMILY) | {
        BOUNDARY_OUTCOME_RECORDED,
        SUCCESS_OUTCOME_RECORDED,
        SUCCESS_BOUNDARY_OUTCOME_RECORDED,
        RESULT_OUTCOME_RECORDED,
        OUTPUT_CAPTURE_OUTCOME_RECORDED,
        RESULT_VERSION,
    } | set(REQUIRED_FALSE_NON_CLAIMS) | set(ALLOWED_TRUE_RECORDED_FIELDS) | set(POSTURE_FIELDS)


def _is_sensitive_key(key: str | None) -> bool:
    if key is None:
        return False
    lowered = str(key).lower()
    return lowered in SENSITIVE_CONTENT_KEYS or lowered.endswith("_body")


def _sanitize_json_value(value: Any, key: str | None = None) -> Any:
    official = _official_strings()
    if isinstance(value, str):
        if value in official:
            return value
        if any(sentinel in value for sentinel in HOSTILE_SENTINELS):
            return REDACTED_CONTENT
        if _is_sensitive_key(key):
            return REDACTED_CONTENT
        return value
    if _is_sensitive_key(key):
        return REDACTED_CONTENT
    if isinstance(value, Mapping):
        return {
            str(inner_key): _sanitize_json_value(inner_value, str(inner_key))
            for inner_key, inner_value in value.items()
        }
    if isinstance(value, (list, tuple, set)):
        return [_sanitize_json_value(item, key) for item in value]
    return copy.deepcopy(value)


def _utc_timestamp() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z")


def _as_bool(value: Any, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return default
    if isinstance(value, (int, float)):
        return bool(value)
    if isinstance(value, str):
        normalized = value.strip().lower()
        if normalized in {"true", "1", "yes", "y", "recorded", "preserved", "ok"}:
            return True
        if normalized in {"false", "0", "no", "n", "none", "null", ""}:
            return False
    return bool(value)


def _as_int(value: Any, default: int | None = None) -> int | None:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value.strip())
        except ValueError:
            return default
    return default


def _find_first(mapping: Any, keys: Iterable[str]) -> Any:
    if not isinstance(mapping, Mapping):
        return None
    wanted = set(keys)
    for key, value in mapping.items():
        key_string = str(key)
        if key_string in wanted:
            return value
        if _is_sensitive_key(key_string):
            continue
        if isinstance(value, Mapping):
            found = _find_first(value, wanted)
            if found is not None:
                return found
    return None


def _request_value(
    request: Mapping[str, Any],
    top_level_key: str,
    basis_fields: Iterable[str] = (),
    nested_keys: Iterable[str] = (),
    default: Any = None,
) -> Any:
    if top_level_key in request:
        return request[top_level_key]
    for basis_field in basis_fields:
        found = _find_first(request.get(basis_field), nested_keys)
        if found is not None:
            return found
    return default


def _declared(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, Mapping):
        if "declared" in value:
            return _as_bool(value["declared"])
        if "basis_declared" in value:
            return _as_bool(value["basis_declared"])
        return bool(value)
    if isinstance(value, (list, tuple, set)):
        return bool(value)
    return bool(value)


def _request_declares(request: Mapping[str, Any], field: str) -> bool:
    return field in request and _declared(request.get(field))


def _make_check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str,
) -> dict[str, Any]:
    if code not in BLOCK_CODES:
        raise PortableSourceBodyVerificationSecondCarrierVerificationError(
            f"Unsupported internal block code: {code}"
        )
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": _sanitize_json_value(expected_posture),
        "actual_posture": _sanitize_json_value(actual_posture),
        "block_code": None if passed else code,
        "failure_code": None if passed else code,
    }


def _scope_values(request: Mapping[str, Any]) -> list[Any]:
    values = request.get("second_carrier_verification_scope", list(SUPPORTED_SCOPE_VALUES))
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


def _expected_false_non_claim_code(key: str) -> str:
    direct = {
        "external_result_created": "EXTERNAL_RESULT_CREATED",
        "cross_carrier_evidence_created": "CROSS_CARRIER_EVIDENCE_CREATED",
        "portable_verification_closure_created": "PORTABLE_VERIFICATION_CLOSURE_CREATED",
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
        "artifact_existence_treated_as_verification_authority": "ARTIFACT_EXISTENCE_TREATED_AS_VERIFICATION_AUTHORITY",
        "artifact_path_treated_as_currentness": "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
        "repo_local_availability_treated_as_verification_authority": "REPO_LOCAL_AVAILABILITY_TREATED_AS_VERIFICATION_AUTHORITY",
        "hidden_repo_state_used_as_verification_content": "HIDDEN_REPO_STATE_USED_AS_VERIFICATION_CONTENT",
        "hidden_repo_state_used_as_verification_authority": "HIDDEN_REPO_STATE_USED_AS_VERIFICATION_AUTHORITY",
        "raw_full_prior_artifact_body_returned": "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
        "prior_artifacts_mutated": "ARTIFACTS_MUTATED",
        "returned_capture_material_mutated": "RETURNED_CAPTURE_MATERIAL_MUTATED",
        "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
        "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
        "zero_exit_code_treated_as_verification_standalone": "ZERO_EXIT_CODE_TREATED_AS_VERIFICATION",
        "ok_output_treated_as_verification_standalone": "OK_OUTPUT_TREATED_AS_VERIFICATION",
        "ran_7_tests_treated_as_cross_carrier_proof": "RAN_7_TESTS_TREATED_AS_CROSS_CARRIER_PROOF",
        "returned_capture_treated_as_cross_carrier_evidence": "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_PROOF",
    }
    if key.startswith("second_carrier_verification_treated_as_"):
        suffix = key.removeprefix("second_carrier_verification_treated_as_").upper()
        return f"SECOND_CARRIER_VERIFICATION_TREATED_AS_{suffix}"
    if key.startswith("first_success_boundary_test_"):
        return "FIRST_SUCCESS_BOUNDARY_TEST_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED"
    if key.startswith("first_result_boundary_resolver_"):
        return "FIRST_RESULT_BOUNDARY_RESOLVER_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED"
    if key.startswith("v1_"):
        return "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"
    return direct.get(key, "NON_CLAIM_MISSING_OR_FLIPPED")


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
    }


def _reference_basis_section(field_name: str, request: Mapping[str, Any]) -> dict[str, Any]:
    selected = request.get(field_name)
    shortcut_prefixes = {
        "selected_second_carrier_verification_boundary_basis": (
            "selected_second_carrier_verification_boundary_",
        ),
        "selected_second_carrier_success_basis": ("selected_second_carrier_success_",),
        "selected_second_carrier_success_boundary_basis": (
            "selected_second_carrier_success_boundary_",
        ),
        "selected_second_carrier_result_basis": ("selected_second_carrier_result_",),
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
    }.get(field_name, ())
    shortcuts = {
        key: _sanitize_json_value(value, key)
        for key, value in request.items()
        if any(str(key).startswith(prefix) for prefix in shortcut_prefixes)
    }
    return {
        "basis_name": field_name,
        "basis_declared": _declared(selected),
        "reference_shape": True,
        "selected_reference": _sanitize_json_value(selected, field_name),
        "selected_shortcut_values": shortcuts,
        "raw_full_prior_artifact_body_returned": False,
        "hidden_repo_state_used_as_verification_authority": False,
    }


def _posture_section(field_name: str, request: Mapping[str, Any], recorded: bool) -> dict[str, Any]:
    return {
        "posture_name": field_name,
        "declared": bool(recorded),
        "request_declared": _request_declares(request, field_name),
        "bounded_second_carrier_verification_posture_only": True,
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
        "verification_became_external_result": False,
        "verification_became_cross_carrier_proof": False,
        "verification_became_portable_verification_closure": False,
        "verification_became_source_transfer_source_receipt_or_reception_authorization": False,
        "verification_became_source_authority_or_currentness": False,
        "verification_artifact_became_external_result_cross_carrier_evidence_or_portable_closure": False,
        "returned_capture_became_cross_carrier_proof": False,
        "zero_exit_code_became_verification_automatically": False,
        "ok_became_verification_automatically": False,
        "ran_7_tests_became_cross_carrier_proof": False,
        "macbook_pro_became_authority": False,
        "macbook_air_became_source": False,
        "artifact_existence_became_verification_authority": False,
        "artifact_path_became_currentness": False,
        "repo_local_availability_became_verification_authority": False,
        "hidden_repo_state_became_verification_authority": False,
        "first_success_boundary_test_repaired_hidden_erased_or_claimed_passed": False,
        "first_result_boundary_resolver_repaired_hidden_erased_or_claimed_passed": False,
        "v1_packet_emission_boundary_resolver_repaired_hidden_erased_or_claimed_passed": False,
    }


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "second-carrier verification test",
            "second-carrier verification live artifact",
            "second-carrier verification terminal summary, if needed",
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


def _validate_request(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    question = request.get("second_carrier_verification_question")
    checks.append(
        _make_check(
            "second_carrier_verification_question_declared",
            question == REQUIRED_QUESTION,
            REQUIRED_QUESTION,
            question,
            "SECOND_CARRIER_VERIFICATION_QUESTION_UNDECLARED",
        )
    )

    intent = request.get("second_carrier_verification_intent")
    checks.append(
        _make_check(
            "second_carrier_verification_intent_supported",
            intent in SUPPORTED_INTENTS,
            list(SUPPORTED_INTENTS),
            intent,
            "SECOND_CARRIER_VERIFICATION_INTENT_UNSUPPORTED",
        )
    )

    scope_values = _scope_values(request)
    unsupported_scope = [value for value in scope_values if value not in SUPPORTED_SCOPE_VALUES]
    checks.append(
        _make_check(
            "second_carrier_verification_scope_supported",
            not unsupported_scope,
            list(SUPPORTED_SCOPE_VALUES),
            scope_values,
            "UNSUPPORTED_SECOND_CARRIER_VERIFICATION_SCOPE",
        )
    )

    basis_required = (
        ("selected_second_carrier_verification_boundary_basis", "SECOND_CARRIER_VERIFICATION_BOUNDARY_BASIS_MISSING"),
        ("selected_second_carrier_verification_boundary_terminal_summary_basis", "SECOND_CARRIER_VERIFICATION_BOUNDARY_BASIS_MISSING"),
        ("selected_second_carrier_success_basis", "SECOND_CARRIER_SUCCESS_BASIS_MISSING"),
        ("selected_second_carrier_success_terminal_summary_basis", "SECOND_CARRIER_SUCCESS_BASIS_MISSING"),
        ("selected_second_carrier_success_boundary_basis", "SECOND_CARRIER_SUCCESS_BOUNDARY_BASIS_MISSING"),
        ("selected_second_carrier_result_basis", "SECOND_CARRIER_RESULT_BASIS_MISSING"),
        ("selected_second_carrier_result_terminal_summary_basis", "SECOND_CARRIER_RESULT_BASIS_MISSING"),
        ("selected_second_carrier_result_boundary_v2_basis", "SECOND_CARRIER_RESULT_BASIS_MISSING"),
        ("selected_returned_second_carrier_live_capture_intake_basis", "RETURNED_CAPTURE_INTAKE_BASIS_MISSING"),
        ("selected_returned_capture_material_basis", "RETURNED_CAPTURE_MATERIAL_MISSING"),
        ("selected_second_carrier_output_capture_basis", "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_MISSING"),
        ("selected_packet_transfer_basis", "SECOND_CARRIER_VERIFICATION_BOUNDARY_BASIS_MISSING"),
        ("selected_packet_emission_basis", "SECOND_CARRIER_VERIFICATION_BOUNDARY_BASIS_MISSING"),
        ("selected_packet_emission_boundary_v2_basis", "SECOND_CARRIER_VERIFICATION_BOUNDARY_BASIS_MISSING"),
        ("selected_packet_emission_boundary_v1_predecessor_failure_basis", "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
        ("selected_packet_artifact_basis", "SECOND_CARRIER_VERIFICATION_BOUNDARY_BASIS_MISSING"),
        ("selected_command_success_basis", "SECOND_CARRIER_VERIFICATION_BOUNDARY_BASIS_MISSING"),
        ("selected_command_result_v2_basis", "SECOND_CARRIER_VERIFICATION_BOUNDARY_BASIS_MISSING"),
        ("selected_output_capture_v2_basis", "SECOND_CARRIER_VERIFICATION_BOUNDARY_BASIS_MISSING"),
        ("selected_command_output_report_artifact_basis", "SECOND_CARRIER_VERIFICATION_BOUNDARY_BASIS_MISSING"),
        ("selected_command_execution_basis", "SECOND_CARRIER_VERIFICATION_BOUNDARY_BASIS_MISSING"),
        ("selected_command_report_lineage_basis", "SECOND_CARRIER_VERIFICATION_BOUNDARY_BASIS_MISSING"),
        ("selected_predecessor_failure_basis", "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
        ("selected_evidence_manifest_basis", "SECOND_CARRIER_VERIFICATION_BOUNDARY_BASIS_MISSING"),
        ("selected_artifact_containment_basis", "SECOND_CARRIER_VERIFICATION_BOUNDARY_BASIS_MISSING"),
        ("selected_portable_verification_basis", "SECOND_CARRIER_VERIFICATION_BOUNDARY_BASIS_MISSING"),
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
    boundary_fields = (
        "selected_second_carrier_verification_boundary_basis",
        "selected_second_carrier_verification_boundary_terminal_summary_basis",
    )
    success_fields = (
        "selected_second_carrier_success_basis",
        "selected_second_carrier_success_terminal_summary_basis",
    )
    success_boundary_fields = ("selected_second_carrier_success_boundary_basis",)
    result_fields = (
        "selected_second_carrier_result_basis",
        "selected_second_carrier_result_terminal_summary_basis",
    )
    output_capture_fields = ("selected_second_carrier_output_capture_basis",)

    checks.append(
        _make_check(
            "second_carrier_verification_boundary_outcome_recorded",
            _request_value(
                request,
                "selected_second_carrier_verification_boundary_result_outcome",
                boundary_fields,
                ("outcome", "result_outcome"),
            )
            == BOUNDARY_OUTCOME_RECORDED,
            BOUNDARY_OUTCOME_RECORDED,
            _request_value(
                request,
                "selected_second_carrier_verification_boundary_result_outcome",
                boundary_fields,
                ("outcome", "result_outcome"),
            ),
            "SECOND_CARRIER_VERIFICATION_BOUNDARY_NOT_RECORDED",
        )
    )
    checks.append(
        _make_check(
            "second_carrier_verification_boundary_version_0_1_0",
            _request_value(
                request,
                "selected_second_carrier_verification_boundary_result_version",
                boundary_fields,
                ("result_version", "version"),
            )
            == RESULT_VERSION,
            RESULT_VERSION,
            _request_value(
                request,
                "selected_second_carrier_verification_boundary_result_version",
                boundary_fields,
                ("result_version", "version"),
            ),
            "SECOND_CARRIER_VERIFICATION_BOUNDARY_VERSION_NOT_0_1_0",
        )
    )
    checks.append(
        _make_check(
            "second_carrier_verification_boundary_failed_checks_zero",
            _as_int(
                _request_value(
                    request,
                    "selected_second_carrier_verification_boundary_failed_check_count",
                    boundary_fields,
                    ("failed_check_count",),
                )
            )
            == 0,
            0,
            _request_value(
                request,
                "selected_second_carrier_verification_boundary_failed_check_count",
                boundary_fields,
                ("failed_check_count",),
            ),
            "SECOND_CARRIER_VERIFICATION_BOUNDARY_FAILED_CHECKS_PRESENT",
        )
    )
    boundary_bool_checks = (
        (
            "selected_second_carrier_verification_boundary_declared_future_verification_step",
            ("one_future_second_carrier_verification_step_declared", "declared_future_verification_step"),
            True,
            "SECOND_CARRIER_VERIFICATION_BOUNDARY_DID_NOT_DECLARE_FUTURE_VERIFICATION_STEP",
            "second_carrier_verification_boundary_declared_future_verification_step",
        ),
        (
            "selected_second_carrier_verification_boundary_already_created_verification",
            ("verification_created", "already_created_verification"),
            False,
            "SECOND_CARRIER_VERIFICATION_BOUNDARY_ALREADY_CREATED_VERIFICATION",
            "second_carrier_verification_boundary_did_not_already_create_verification",
        ),
        (
            "selected_second_carrier_verification_boundary_already_created_external_result",
            ("external_result_created", "already_created_external_result"),
            False,
            "SECOND_CARRIER_VERIFICATION_BOUNDARY_ALREADY_CREATED_EXTERNAL_RESULT",
            "second_carrier_verification_boundary_did_not_already_create_external_result",
        ),
        (
            "selected_second_carrier_verification_boundary_already_created_cross_carrier_evidence",
            ("cross_carrier_evidence_created", "already_created_cross_carrier_evidence"),
            False,
            "SECOND_CARRIER_VERIFICATION_BOUNDARY_ALREADY_CREATED_CROSS_CARRIER_EVIDENCE",
            "second_carrier_verification_boundary_did_not_already_create_cross_carrier_evidence",
        ),
        (
            "selected_second_carrier_verification_boundary_already_created_portable_verification_closure",
            ("portable_verification_closure_created", "already_created_portable_verification_closure"),
            False,
            "SECOND_CARRIER_VERIFICATION_BOUNDARY_ALREADY_CREATED_PORTABLE_VERIFICATION_CLOSURE",
            "second_carrier_verification_boundary_did_not_already_create_portable_verification_closure",
        ),
        (
            "selected_second_carrier_verification_boundary_treated_verification_boundary_as_verification",
            ("verification_boundary_treated_as_verification",),
            False,
            "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_VERIFICATION_BOUNDARY_AS_VERIFICATION",
            "second_carrier_verification_boundary_not_treated_as_verification",
        ),
        (
            "selected_second_carrier_verification_boundary_treated_verification_boundary_as_external_result",
            ("verification_boundary_treated_as_external_result",),
            False,
            "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_VERIFICATION_BOUNDARY_AS_EXTERNAL_RESULT",
            "second_carrier_verification_boundary_not_treated_as_external_result",
        ),
        (
            "selected_second_carrier_verification_boundary_treated_verification_boundary_as_cross_carrier_evidence",
            ("verification_boundary_treated_as_cross_carrier_evidence",),
            False,
            "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_VERIFICATION_BOUNDARY_AS_CROSS_CARRIER_EVIDENCE",
            "second_carrier_verification_boundary_not_treated_as_cross_carrier_evidence",
        ),
        (
            "selected_second_carrier_verification_boundary_treated_verification_boundary_as_portable_verification_closure",
            ("verification_boundary_treated_as_portable_verification_closure",),
            False,
            "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_VERIFICATION_BOUNDARY_AS_PORTABLE_VERIFICATION_CLOSURE",
            "second_carrier_verification_boundary_not_treated_as_portable_verification_closure",
        ),
        (
            "selected_second_carrier_verification_boundary_zero_exit_code_not_verification",
            ("zero_exit_code_not_verification",),
            True,
            "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_ZERO_EXIT_CODE_AS_VERIFICATION",
            "second_carrier_verification_boundary_kept_zero_exit_code_not_verification",
        ),
        (
            "selected_second_carrier_verification_boundary_ok_not_verification",
            ("ok_output_not_verification",),
            True,
            "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_OK_AS_VERIFICATION",
            "second_carrier_verification_boundary_kept_ok_not_verification",
        ),
        (
            "selected_second_carrier_verification_boundary_ran_7_tests_not_cross_carrier_proof",
            ("ran_7_tests_not_cross_carrier_proof",),
            True,
            "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_RAN_7_TESTS_AS_CROSS_CARRIER_PROOF",
            "second_carrier_verification_boundary_kept_ran_7_tests_not_cross_carrier_proof",
        ),
        (
            "selected_second_carrier_verification_boundary_returned_capture_not_cross_carrier_proof",
            ("returned_capture_not_cross_carrier_proof",),
            True,
            "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_PROOF",
            "second_carrier_verification_boundary_kept_returned_capture_not_cross_carrier_proof",
        ),
        (
            "selected_second_carrier_verification_boundary_official_enum_scope_strings_redacted",
            ("official_enum_scope_strings_redacted",),
            False,
            "SECOND_CARRIER_VERIFICATION_BOUNDARY_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
            "second_carrier_verification_boundary_kept_official_enum_scope_strings_unredacted",
        ),
        (
            "selected_second_carrier_verification_boundary_first_success_boundary_test_failure_preserved",
            ("first_success_boundary_test_failure_preserved",),
            True,
            "FIRST_SUCCESS_BOUNDARY_TEST_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
            "second_carrier_verification_boundary_preserved_first_success_boundary_test_failure",
        ),
    )
    for top_key, nested_keys, expected, code, check_name in boundary_bool_checks:
        actual = _request_value(request, top_key, boundary_fields, nested_keys, expected)
        checks.append(
            _make_check(
                check_name,
                _as_bool(actual) is expected,
                expected,
                actual,
                code,
            )
        )

    checks.append(
        _make_check(
            "second_carrier_success_outcome_recorded",
            _request_value(
                request,
                "selected_second_carrier_success_result_outcome",
                success_fields,
                ("outcome", "result_outcome"),
            )
            == SUCCESS_OUTCOME_RECORDED,
            SUCCESS_OUTCOME_RECORDED,
            _request_value(
                request,
                "selected_second_carrier_success_result_outcome",
                success_fields,
                ("outcome", "result_outcome"),
            ),
            "SECOND_CARRIER_SUCCESS_NOT_RECORDED",
        )
    )
    checks.append(
        _make_check(
            "second_carrier_success_version_0_1_0",
            _request_value(
                request,
                "selected_second_carrier_success_result_version",
                success_fields,
                ("result_version", "version"),
            )
            == RESULT_VERSION,
            RESULT_VERSION,
            _request_value(
                request,
                "selected_second_carrier_success_result_version",
                success_fields,
                ("result_version", "version"),
            ),
            "SECOND_CARRIER_SUCCESS_FAILED_CHECKS_PRESENT",
        )
    )
    checks.append(
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
        )
    )
    success_bool_checks = (
        (
            "selected_second_carrier_success_bounded_success_recorded",
            ("bounded_success_recorded", "second_carrier_success_recorded"),
            True,
            "SECOND_CARRIER_SUCCESS_NOT_RECORDED",
            "second_carrier_success_recorded_bounded_success",
        ),
        (
            "selected_second_carrier_success_treated_success_as_verification",
            ("success_treated_as_verification",),
            False,
            "SECOND_CARRIER_SUCCESS_TREATED_SUCCESS_AS_VERIFICATION",
            "second_carrier_success_did_not_treat_success_as_verification",
        ),
        (
            "selected_second_carrier_success_treated_success_as_external_result",
            ("success_treated_as_external_result",),
            False,
            "SECOND_CARRIER_SUCCESS_TREATED_SUCCESS_AS_EXTERNAL_RESULT",
            "second_carrier_success_did_not_treat_success_as_external_result",
        ),
        (
            "selected_second_carrier_success_zero_exit_code_not_verification",
            ("zero_exit_code_not_verification",),
            True,
            "SECOND_CARRIER_SUCCESS_TREATED_ZERO_EXIT_CODE_AS_VERIFICATION",
            "second_carrier_success_kept_zero_exit_code_not_verification",
        ),
        (
            "selected_second_carrier_success_ok_not_verification",
            ("ok_output_not_verification",),
            True,
            "SECOND_CARRIER_SUCCESS_TREATED_OK_AS_VERIFICATION",
            "second_carrier_success_kept_ok_not_verification",
        ),
        (
            "selected_second_carrier_success_ran_7_tests_not_cross_carrier_proof",
            ("ran_7_tests_not_cross_carrier_proof",),
            True,
            "SECOND_CARRIER_SUCCESS_TREATED_RAN_7_TESTS_AS_CROSS_CARRIER_PROOF",
            "second_carrier_success_kept_ran_7_tests_not_cross_carrier_proof",
        ),
    )
    for top_key, nested_keys, expected, code, check_name in success_bool_checks:
        actual = _request_value(request, top_key, success_fields, nested_keys, expected)
        checks.append(_make_check(check_name, _as_bool(actual) is expected, expected, actual, code))

    checks.append(
        _make_check(
            "second_carrier_success_boundary_outcome_recorded",
            _request_value(
                request,
                "selected_second_carrier_success_boundary_result_outcome",
                success_boundary_fields,
                ("outcome", "result_outcome"),
                SUCCESS_BOUNDARY_OUTCOME_RECORDED,
            )
            == SUCCESS_BOUNDARY_OUTCOME_RECORDED,
            SUCCESS_BOUNDARY_OUTCOME_RECORDED,
            _request_value(
                request,
                "selected_second_carrier_success_boundary_result_outcome",
                success_boundary_fields,
                ("outcome", "result_outcome"),
            ),
            "SECOND_CARRIER_SUCCESS_BOUNDARY_BASIS_MISSING",
        )
    )
    checks.append(
        _make_check(
            "second_carrier_success_boundary_failed_checks_zero",
            _as_int(
                _request_value(
                    request,
                    "selected_second_carrier_success_boundary_failed_check_count",
                    success_boundary_fields,
                    ("failed_check_count",),
                    0,
                )
            )
            == 0,
            0,
            _request_value(
                request,
                "selected_second_carrier_success_boundary_failed_check_count",
                success_boundary_fields,
                ("failed_check_count",),
            ),
            "SECOND_CARRIER_SUCCESS_BOUNDARY_BASIS_MISSING",
        )
    )

    checks.append(
        _make_check(
            "second_carrier_result_outcome_recorded",
            _request_value(
                request,
                "selected_second_carrier_result_result_outcome",
                result_fields,
                ("outcome", "result_outcome"),
            )
            == RESULT_OUTCOME_RECORDED,
            RESULT_OUTCOME_RECORDED,
            _request_value(
                request,
                "selected_second_carrier_result_result_outcome",
                result_fields,
                ("outcome", "result_outcome"),
            ),
            "SECOND_CARRIER_RESULT_NOT_RECORDED",
        )
    )
    checks.append(
        _make_check(
            "second_carrier_result_version_0_1_0",
            _request_value(
                request,
                "selected_second_carrier_result_result_version",
                result_fields,
                ("result_version", "version"),
            )
            == RESULT_VERSION,
            RESULT_VERSION,
            _request_value(
                request,
                "selected_second_carrier_result_result_version",
                result_fields,
                ("result_version", "version"),
            ),
            "SECOND_CARRIER_RESULT_FAILED_CHECKS_PRESENT",
        )
    )
    checks.append(
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
        )
    )

    capture_checks = (
        ("selected_returned_capture_intake_preserved", True, "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED", "returned_capture_intake_preserved"),
        ("selected_returned_capture_intake_capture_only", True, "RETURNED_CAPTURE_TREATED_AS_VERIFICATION", "returned_capture_intake_capture_only"),
        ("selected_returned_capture_from_macbook_pro_to_macbook_air", True, "RECEIVING_CARRIER_TREATED_AS_AUTHORITY", "macbook_pro_to_macbook_air_return_preserved"),
        ("selected_returned_capture_placeholder_fields_unrepaired", True, "PLACEHOLDER_CARRIER_FIELDS_REPAIRED", "raw_placeholder_carrier_fields_unrepaired"),
    )
    for top_key, expected, code, check_name in capture_checks:
        actual = request.get(top_key, expected)
        checks.append(_make_check(check_name, _as_bool(actual) is expected, expected, actual, code))

    returned_required = (
        ("selected_returned_capture_zip_path", "RETURNED_ZIP_PATH_MISSING"),
        ("selected_returned_capture_hash_path", "RETURNED_HASH_PATH_MISSING"),
        ("selected_returned_capture_extracted_directory_path", "RETURNED_EXTRACTED_DIRECTORY_MISSING"),
        ("selected_returned_capture_combined_terminal_log_path", "RETURNED_COMBINED_TERMINAL_LOG_MISSING"),
        ("selected_returned_capture_exit_code", "RETURNED_EXIT_CODE_MISSING"),
        ("selected_returned_capture_command_text", "RETURNED_COMMAND_TEXT_MISSING"),
        ("selected_returned_capture_started_at", "RETURNED_TIMESTAMPS_MISSING"),
        ("selected_returned_capture_completed_at", "RETURNED_TIMESTAMPS_MISSING"),
    )
    for field_name, code in returned_required:
        checks.append(
            _make_check(
                f"{field_name}_declared",
                _declared(request.get(field_name)),
                "declared returned capture basis",
                request.get(field_name),
                code,
            )
        )
    checks.append(
        _make_check(
            "returned_capture_exit_code_zero_preserved",
            str(request.get("selected_returned_capture_exit_code")) == "0",
            "0",
            request.get("selected_returned_capture_exit_code"),
            "ZERO_EXIT_CODE_TREATED_AS_VERIFICATION",
        )
    )
    checks.append(
        _make_check(
            "returned_capture_ran_7_tests_line_preserved",
            _declared(request.get("selected_returned_capture_ran_7_tests_line")),
            "Ran 7 tests line declared",
            request.get("selected_returned_capture_ran_7_tests_line"),
            "RAN_7_TESTS_TREATED_AS_CROSS_CARRIER_PROOF",
        )
    )
    checks.append(
        _make_check(
            "returned_capture_ok_line_preserved",
            _declared(request.get("selected_returned_capture_ok_line")),
            "OK line declared",
            request.get("selected_returned_capture_ok_line"),
            "OK_OUTPUT_TREATED_AS_VERIFICATION",
        )
    )

    checks.append(
        _make_check(
            "second_carrier_output_capture_outcome_recorded",
            _request_value(
                request,
                "selected_second_carrier_output_capture_result_outcome",
                output_capture_fields,
                ("outcome", "result_outcome"),
            )
            == OUTPUT_CAPTURE_OUTCOME_RECORDED,
            OUTPUT_CAPTURE_OUTCOME_RECORDED,
            _request_value(
                request,
                "selected_second_carrier_output_capture_result_outcome",
                output_capture_fields,
                ("outcome", "result_outcome"),
            ),
            "SECOND_CARRIER_OUTPUT_CAPTURE_NOT_RECORDED",
        )
    )
    checks.append(
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
        )
    )
    return checks


def _posture_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    posture_code = {
        "verification_not_external_result_posture": "SECOND_CARRIER_VERIFICATION_TREATED_AS_EXTERNAL_RESULT",
        "verification_not_cross_carrier_evidence_posture": "SECOND_CARRIER_VERIFICATION_TREATED_AS_CROSS_CARRIER_EVIDENCE",
        "verification_not_portable_verification_closure_posture": "SECOND_CARRIER_VERIFICATION_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
        "verification_not_source_transfer_posture": "SECOND_CARRIER_VERIFICATION_TREATED_AS_SOURCE_TRANSFER",
        "verification_not_source_receipt_posture": "SECOND_CARRIER_VERIFICATION_TREATED_AS_SOURCE_RECEIPT",
        "verification_not_reception_authorization_posture": "SECOND_CARRIER_VERIFICATION_TREATED_AS_RECEPTION_AUTHORIZATION",
        "zero_exit_code_not_verification_as_standalone_inference_posture": "ZERO_EXIT_CODE_TREATED_AS_VERIFICATION",
        "ok_output_not_verification_as_standalone_inference_posture": "OK_OUTPUT_TREATED_AS_VERIFICATION",
        "ran_7_tests_not_cross_carrier_proof_posture": "RAN_7_TESTS_TREATED_AS_CROSS_CARRIER_PROOF",
        "returned_capture_not_cross_carrier_proof_posture": "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_PROOF",
        "external_result_not_created_posture": "EXTERNAL_RESULT_CREATED",
        "cross_carrier_evidence_not_created_posture": "CROSS_CARRIER_EVIDENCE_CREATED",
        "portable_verification_closure_not_created_posture": "PORTABLE_VERIFICATION_CLOSURE_CREATED",
        "receiving_carrier_not_authority_posture": "RECEIVING_CARRIER_TREATED_AS_AUTHORITY",
        "hidden_repo_state_excluded_posture": "HIDDEN_REPO_STATE_USED_AS_VERIFICATION_CONTENT",
        "hidden_repo_state_not_used_as_verification_authority_posture": "HIDDEN_REPO_STATE_USED_AS_VERIFICATION_AUTHORITY",
        "repo_local_availability_not_verification_authority_posture": "REPO_LOCAL_AVAILABILITY_TREATED_AS_VERIFICATION_AUTHORITY",
        "raw_full_prior_artifact_body_not_returned_posture": "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
        "official_enum_scope_strings_not_redacted_posture": "SECOND_CARRIER_VERIFICATION_BOUNDARY_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
        "first_success_boundary_test_failure_preserved_posture": "FIRST_SUCCESS_BOUNDARY_TEST_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
        "first_result_boundary_resolver_failure_preserved_posture": "FIRST_RESULT_BOUNDARY_RESOLVER_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
        "authorization_token_reuse_blocked_posture": "AUTHORIZATION_TOKEN_REUSED",
        "consumed_request_token_remains_closed_posture": "CONSUMED_REQUEST_REOPENED",
    }
    for field_name in POSTURE_FIELDS:
        code = posture_code.get(field_name, "NON_CLAIM_MISSING_OR_FLIPPED")
        checks.append(
            _make_check(
                f"{field_name}_declared",
                _request_declares(request, field_name),
                "declared bounded posture",
                request.get(field_name),
                code,
            )
        )
    return checks


def _non_claim_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    declared_non_claims = request.get("declared_non_claims")
    for key in REQUIRED_FALSE_NON_CLAIMS:
        actual = _non_claim_value(request, key)
        missing = not isinstance(declared_non_claims, Mapping) or key not in declared_non_claims
        passed = not missing and actual is False
        code = "NON_CLAIM_MISSING_OR_FLIPPED" if missing else _expected_false_non_claim_code(key)
        checks.append(
            _make_check(
                f"non_claim_{key}_false",
                passed,
                False,
                actual,
                code,
            )
        )
    return checks


def _first_failed_code(checks: list[dict[str, Any]]) -> str | None:
    for check in checks:
        if not check.get("passed"):
            code = check.get("block_code") or check.get("failure_code")
            if code:
                return str(code)
    return None


def _build_additional_basis(request: Mapping[str, Any], outcome: str) -> dict[str, Any]:
    if outcome != OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        return {
            "additional_basis_required": False,
            "basis": [],
            "missing_basis_not_scheduled": True,
            "missing_basis_not_authorized": True,
            "missing_basis_not_executed": True,
        }
    context = request.get("additional_basis_context", [])
    return {
        "additional_basis_required": True,
        "basis": _sanitize_json_value(context, "additional_basis_context"),
        "missing_basis_not_scheduled": True,
        "missing_basis_not_authorized": True,
        "missing_basis_not_executed": True,
    }


def _build_not_recorded_basis(request: Mapping[str, Any], outcome: str) -> dict[str, Any]:
    if outcome != OUTCOME_NOT_RECORDED:
        return {
            "not_recorded": False,
            "basis": [],
            "no_mutation": True,
            "no_next_work_authorized": True,
        }
    basis = request.get("not_recorded_basis", request.get("block_reason", "not recorded by request"))
    return {
        "not_recorded": True,
        "basis": _sanitize_json_value(basis, "not_recorded_basis"),
        "no_external_result_created": True,
        "no_cross_carrier_evidence_created": True,
        "no_portable_verification_closure_created": True,
        "no_source_authority_currentness_runtime_or_follow_on_created": True,
        "no_mutation": True,
        "no_next_work_authorized": True,
    }


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: list[dict[str, Any]],
    block_code: str | None = None,
    block_reason: str | None = None,
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    request_id = str(
        request.get(
            "second_carrier_verification_request_id",
            "portable_source_body_verification_second_carrier_verification_unidentified_request",
        )
    )
    if block_code is not None and block_code not in BLOCK_CODES:
        raise PortableSourceBodyVerificationSecondCarrierVerificationError(
            f"Unsupported block code: {block_code}"
        )

    result: dict[str, Any] = {
        "portable_source_body_verification_second_carrier_verification_metadata": {
            "portable_source_body_verification_second_carrier_verification_id": (
                f"{request_id}__portable_source_body_verification_second_carrier_verification_result"
            ),
            "portable_source_body_verification_second_carrier_verification_type": (
                "portable_source_body_verification_second_carrier_verification_result"
            ),
            "portable_source_body_verification_second_carrier_verification_version": RESULT_VERSION,
            "generated_at": _utc_timestamp(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_second_carrier_verification_question": {
            "second_carrier_verification_request_id": request_id,
            "question": request.get("second_carrier_verification_question"),
            "intent": request.get("second_carrier_verification_intent"),
        },
    }

    for field_name in SELECTED_BASIS_FIELDS:
        result[field_name] = _reference_basis_section(field_name, request)
    for field_name in POSTURE_FIELDS:
        result[field_name] = _posture_section(field_name, request, recorded)

    result.update(
        {
            "second_carrier_verification_scope": _sanitize_json_value(_scope_values(request)),
            "second_carrier_verification_checks": checks,
            "second_carrier_verification_statement": _recorded_statement(recorded),
            "second_carrier_verification_non_meaning": _non_meaning(),
            "additional_basis_required": _build_additional_basis(request, outcome),
            "not_recorded_basis": _build_not_recorded_basis(request, outcome),
            "what_remains_open": _what_remains_open(),
            "non_claims": _false_non_claims(),
            "outcome": outcome,
            "block": None
            if block_code is None
            else {
                "blocked": True,
                "block_code": block_code,
                "block_reason": _sanitize_json_value(block_reason or block_code, "block_reason"),
            },
        }
    )
    result["portable_source_body_verification_second_carrier_verification_summary"] = (
        build_portable_source_body_verification_second_carrier_verification_summary(result)
    )
    return result


def resolve_portable_source_body_verification_second_carrier_verification(
    declared_second_carrier_verification_request: Mapping[str, Any] | None = None,
) -> dict:
    if declared_second_carrier_verification_request is None or not isinstance(
        declared_second_carrier_verification_request, Mapping
    ):
        checks = [
            _make_check(
                "declared_second_carrier_verification_request_mapping",
                False,
                "mapping",
                type(declared_second_carrier_verification_request).__name__,
                "DECLARED_SECOND_CARRIER_VERIFICATION_REQUEST_MALFORMED",
            )
        ]
        return _build_result(
            {},
            OUTCOME_BLOCKED,
            checks,
            "DECLARED_SECOND_CARRIER_VERIFICATION_REQUEST_MALFORMED",
            "Declared second-carrier verification request must be a mapping.",
        )

    request = copy.deepcopy(dict(declared_second_carrier_verification_request))
    checks = _validate_request(request)
    failed_code = _first_failed_code(checks)
    intent = request.get("second_carrier_verification_intent")

    if intent == BLOCK_INTENT:
        return _build_result(
            request,
            OUTCOME_BLOCKED,
            checks,
            "DECLARED_SECOND_CARRIER_VERIFICATION_REQUEST_BLOCKED",
            str(request.get("block_reason", "declared block intent")),
        )
    if failed_code is not None:
        return _build_result(
            request,
            OUTCOME_BLOCKED,
            checks,
            failed_code,
            str(request.get("block_reason", failed_code)),
        )
    if intent == DO_NOT_RECORD_INTENT or request.get("requested_second_carrier_verification_outcome") == OUTCOME_NOT_RECORDED:
        return _build_result(request, OUTCOME_NOT_RECORDED, checks)
    if request.get("requested_second_carrier_verification_outcome") == OUTCOME_REQUIRES_ADDITIONAL_BASIS or request.get(
        "additional_basis_context"
    ):
        return _build_result(request, OUTCOME_REQUIRES_ADDITIONAL_BASIS, checks)
    return _build_result(request, OUTCOME_RECORDED, checks)


def resolve_portable_source_body_verification_second_carrier_verification_from_path(
    declared_second_carrier_verification_request_path: Path | str,
) -> dict:
    path = Path(declared_second_carrier_verification_request_path)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise PortableSourceBodyVerificationSecondCarrierVerificationError(
            f"Declared second-carrier verification request is unreadable: {path}"
        ) from exc
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError as exc:
        raise PortableSourceBodyVerificationSecondCarrierVerificationError(
            f"Declared second-carrier verification request is malformed JSON: {path}"
        ) from exc
    if not isinstance(parsed, Mapping):
        checks = [
            _make_check(
                "declared_second_carrier_verification_request_json_object",
                False,
                "JSON object",
                type(parsed).__name__,
                "DECLARED_SECOND_CARRIER_VERIFICATION_REQUEST_MALFORMED",
            )
        ]
        return _build_result(
            {},
            OUTCOME_BLOCKED,
            checks,
            "DECLARED_SECOND_CARRIER_VERIFICATION_REQUEST_MALFORMED",
            "Declared second-carrier verification request JSON must be an object.",
        )
    return resolve_portable_source_body_verification_second_carrier_verification(parsed)


def build_portable_source_body_verification_second_carrier_verification_summary(
    result: Mapping[str, Any],
) -> dict:
    metadata = result.get("portable_source_body_verification_second_carrier_verification_metadata", {})
    declared = result.get("declared_second_carrier_verification_question", {})
    checks = result.get("second_carrier_verification_checks", [])
    statement = result.get("second_carrier_verification_statement", {})
    non_claims = result.get("non_claims", {})
    block = result.get("block")

    passed_count = sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed") is True)
    failed_count = sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed") is not True)

    boundary_basis = result.get("selected_second_carrier_verification_boundary_basis", {})
    success_basis = result.get("selected_second_carrier_success_basis", {})
    returned_capture_basis = result.get("selected_returned_capture_material_basis", {})

    return {
        "outcome": result.get("outcome"),
        "block_code": None if block is None else block.get("block_code"),
        "block_reason": None if block is None else block.get("block_reason"),
        "request_id": declared.get("second_carrier_verification_request_id"),
        "question": declared.get("question"),
        "intent": declared.get("intent"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": metadata.get(
            "portable_source_body_verification_second_carrier_verification_version"
        ),
        "resolver_module": metadata.get("resolver_module"),
        "second_carrier_verification_recorded": bool(
            statement.get("second_carrier_verification_recorded")
        ),
        "bounded_second_carrier_verification_recorded": bool(
            statement.get("bounded_second_carrier_verification_recorded")
        ),
        "verification_artifact_recorded_or_bounded": bool(
            statement.get("verification_artifact_recorded_or_bounded")
        ),
        "second_carrier_verification_boundary_basis_preserved": bool(
            statement.get("second_carrier_verification_boundary_basis_preserved")
        ),
        "second_carrier_success_basis_preserved": bool(
            statement.get("second_carrier_success_basis_preserved")
        ),
        "returned_second_carrier_capture_basis_preserved": bool(
            statement.get("returned_second_carrier_capture_basis_preserved")
        ),
        "capture_intake_basis_preserved": bool(statement.get("capture_intake_basis_preserved")),
        "second_carrier_output_capture_basis_preserved": bool(
            statement.get("second_carrier_output_capture_basis_preserved")
        ),
        "verification_recorded_bounded": bool(statement.get("verification_recorded_bounded")),
        "verification_not_external_result": bool(statement.get("verification_not_external_result")),
        "verification_not_cross_carrier_evidence": bool(
            statement.get("verification_not_cross_carrier_evidence")
        ),
        "verification_not_portable_verification_closure": bool(
            statement.get("verification_not_portable_verification_closure")
        ),
        "verification_not_source_transfer": bool(statement.get("verification_not_source_transfer")),
        "verification_not_source_receipt": bool(statement.get("verification_not_source_receipt")),
        "verification_not_reception_authorization": bool(
            statement.get("verification_not_reception_authorization")
        ),
        "zero_exit_code_not_verification_as_standalone_inference": bool(
            statement.get("zero_exit_code_not_verification_as_standalone_inference")
        ),
        "ok_output_not_verification_as_standalone_inference": bool(
            statement.get("ok_output_not_verification_as_standalone_inference")
        ),
        "ran_7_tests_not_cross_carrier_proof": bool(
            statement.get("ran_7_tests_not_cross_carrier_proof")
        ),
        "returned_capture_not_cross_carrier_proof": bool(
            statement.get("returned_capture_not_cross_carrier_proof")
        ),
        "external_result_not_created": bool(statement.get("external_result_not_created")),
        "cross_carrier_evidence_not_created": bool(
            statement.get("cross_carrier_evidence_not_created")
        ),
        "portable_verification_closure_not_created": bool(
            statement.get("portable_verification_closure_not_created")
        ),
        "receiving_carrier_not_authority": bool(statement.get("receiving_carrier_not_authority")),
        "source_not_created": bool(statement.get("source_not_created")),
        "authority_not_created": bool(statement.get("authority_not_created")),
        "currentness_not_created": bool(statement.get("currentness_not_created")),
        "final_completion_not_created": bool(statement.get("final_completion_not_created")),
        "runtime_not_created": bool(statement.get("runtime_not_created")),
        "follow_on_work_not_authorized": bool(statement.get("follow_on_work_not_authorized")),
        "hidden_repo_state_excluded": bool(statement.get("hidden_repo_state_excluded")),
        "hidden_repo_state_not_used_as_verification_authority": bool(
            statement.get("hidden_repo_state_not_used_as_verification_authority")
        ),
        "repo_local_availability_not_verification_authority": bool(
            statement.get("repo_local_availability_not_verification_authority")
        ),
        "selected_basis_reference_shape_preserved": bool(
            statement.get("selected_basis_reference_shape_preserved")
        ),
        "raw_full_prior_artifact_body_not_returned": bool(
            statement.get("raw_full_prior_artifact_body_not_returned")
        ),
        "official_enum_scope_strings_not_redacted": bool(
            statement.get("official_enum_scope_strings_not_redacted")
        ),
        "hostile_raw_body_content_contained": bool(
            statement.get("hostile_raw_body_content_contained")
        ),
        "selected_verification_boundary_shortcuts": boundary_basis.get("selected_shortcut_values", {}),
        "selected_second_carrier_success_shortcuts": success_basis.get("selected_shortcut_values", {}),
        "selected_returned_capture_shortcuts": returned_capture_basis.get("selected_shortcut_values", {}),
        "no_external_result_cross_carrier_evidence_or_portable_closure": (
            non_claims.get("external_result_created") is False
            and non_claims.get("cross_carrier_evidence_created") is False
            and non_claims.get("portable_verification_closure_created") is False
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
                "external_result_created",
                "cross_carrier_evidence_created",
                "portable_verification_closure_created",
                "source_created",
                "authority_created",
                "currentness_created",
                "follow_on_work_authorized",
                "consumed_request_reopened",
                "authorization_token_reused",
            )
        },
        "first_success_boundary_test_preserved_as_failed_predecessor": bool(
            statement.get("first_success_boundary_test_failure_preserved")
        ),
        "v1_predecessor_failure_preserved": (
            non_claims.get("v1_repaired") is False
            and non_claims.get("v1_hidden") is False
            and non_claims.get("v1_claimed_passed") is False
        ),
        "v1_not_repaired": non_claims.get("v1_repaired") is False,
        "v1_not_hidden": non_claims.get("v1_hidden") is False,
        "v1_not_claimed_passed": non_claims.get("v1_claimed_passed") is False,
        "first_result_boundary_resolver_preserved_as_failed_predecessor": bool(
            statement.get("first_result_boundary_resolver_failure_preserved")
        ),
    }


def _result_filename(result: Mapping[str, Any]) -> str:
    declared = result.get("declared_second_carrier_verification_question", {})
    request_id = str(
        declared.get(
            "second_carrier_verification_request_id",
            "portable_source_body_verification_second_carrier_verification_unidentified_request",
        )
    )
    safe_request_id = "".join(
        character if character.isalnum() or character in {"-", "_", "."} else "_"
        for character in request_id
    ).strip("_")
    return f"{safe_request_id}__portable_source_body_verification_second_carrier_verification_result.json"


def _without_overwrite(path: Path) -> Path:
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


def write_portable_source_body_verification_second_carrier_verification_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    filename = _result_filename(result)
    if output_path is None:
        path = OUTPUT_ROOT / filename
    else:
        supplied = Path(output_path)
        path = supplied if supplied.suffix == ".json" else supplied / filename
    path = _without_overwrite(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(_sanitize_json_value(dict(result)), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return path


def build_declared_portable_source_body_verification_second_carrier_verification_request(
    **overrides: Any,
) -> dict:
    request_id = overrides.pop(
        "second_carrier_verification_request_id",
        "portable_source_body_verification_second_carrier_verification_reference_review_001",
    )
    request: dict[str, Any] = {
        "second_carrier_verification_request_id": request_id,
        "second_carrier_verification_question": REQUIRED_QUESTION,
        "second_carrier_verification_intent": RECORD_INTENT,
        "selected_second_carrier_verification_boundary_basis": _basis(
            "second_carrier_verification_boundary_live_artifact",
            BOUNDARY_OUTCOME_RECORDED,
            RESULT_VERSION,
            0,
            one_future_second_carrier_verification_step_declared=True,
            verification_created=False,
            external_result_created=False,
            cross_carrier_evidence_created=False,
            portable_verification_closure_created=False,
            verification_boundary_treated_as_verification=False,
            verification_boundary_treated_as_external_result=False,
            verification_boundary_treated_as_cross_carrier_evidence=False,
            verification_boundary_treated_as_portable_verification_closure=False,
            zero_exit_code_not_verification=True,
            ok_output_not_verification=True,
            ran_7_tests_not_cross_carrier_proof=True,
            returned_capture_not_cross_carrier_proof=True,
            official_enum_scope_strings_redacted=False,
            first_success_boundary_test_failure_preserved=True,
            first_result_boundary_resolver_failure_preserved=True,
        ),
        "selected_second_carrier_verification_boundary_terminal_summary_basis": _basis(
            "second_carrier_verification_boundary_terminal_summary"
        ),
        "selected_second_carrier_success_basis": _basis(
            "second_carrier_success_live_artifact",
            SUCCESS_OUTCOME_RECORDED,
            RESULT_VERSION,
            0,
            bounded_success_recorded=True,
            success_treated_as_verification=False,
            success_treated_as_external_result=False,
            zero_exit_code_not_verification=True,
            ok_output_not_verification=True,
            ran_7_tests_not_cross_carrier_proof=True,
        ),
        "selected_second_carrier_success_terminal_summary_basis": _basis(
            "second_carrier_success_terminal_summary"
        ),
        "selected_second_carrier_success_boundary_basis": _basis(
            "second_carrier_success_boundary_basis",
            SUCCESS_BOUNDARY_OUTCOME_RECORDED,
            RESULT_VERSION,
            0,
        ),
        "selected_second_carrier_result_basis": _basis(
            "second_carrier_result_live_artifact",
            RESULT_OUTCOME_RECORDED,
            RESULT_VERSION,
            0,
            bounded_result_recorded=True,
        ),
        "selected_second_carrier_result_terminal_summary_basis": _basis(
            "second_carrier_result_terminal_summary"
        ),
        "selected_second_carrier_result_boundary_v2_basis": _basis(
            "second_carrier_result_boundary_v2_basis"
        ),
        "selected_returned_second_carrier_live_capture_intake_basis": _basis(
            "returned_second_carrier_live_capture_intake",
            intake_preserved=True,
            capture_only=True,
        ),
        "selected_returned_capture_material_basis": _basis(
            "returned_second_carrier_capture_material",
            returned_from_macbook_pro_to_macbook_air=True,
            placeholder_fields_unrepaired=True,
        ),
        "selected_second_carrier_output_capture_basis": _basis(
            "second_carrier_output_capture_live_artifact",
            OUTPUT_CAPTURE_OUTCOME_RECORDED,
            RESULT_VERSION,
            0,
        ),
        "selected_packet_transfer_basis": _basis("packet_transfer_basis"),
        "selected_packet_emission_basis": _basis("packet_emission_basis"),
        "selected_packet_emission_boundary_v2_basis": _basis("packet_emission_boundary_v2_basis"),
        "selected_packet_emission_boundary_v1_predecessor_failure_basis": _basis(
            "packet_emission_boundary_v1_predecessor_failure_basis"
        ),
        "selected_packet_artifact_basis": _basis("packet_artifact_basis"),
        "selected_command_success_basis": _basis("command_success_basis"),
        "selected_command_result_v2_basis": _basis("command_result_v2_basis"),
        "selected_output_capture_v2_basis": _basis("output_capture_v2_basis"),
        "selected_command_output_report_artifact_basis": _basis(
            "command_output_report_artifact_basis"
        ),
        "selected_command_execution_basis": _basis("command_execution_basis"),
        "selected_command_report_lineage_basis": _basis(
            "command_report_lineage_basis",
            command_report_lineage_not_current_report_artifact=True,
            command_report_lineage_not_source=True,
            command_report_lineage_not_authority=True,
            command_report_lineage_not_currentness=True,
        ),
        "selected_predecessor_failure_basis": _basis(
            "predecessor_failure_basis",
            first_success_boundary_test_failure_preserved=True,
            first_result_boundary_resolver_failure_preserved=True,
            v1_packet_emission_boundary_failure_preserved=True,
        ),
        "selected_evidence_manifest_basis": _basis("evidence_manifest_basis"),
        "selected_artifact_containment_basis": _basis("artifact_containment_basis"),
        "selected_portable_verification_basis": _basis("portable_verification_basis"),
        "second_carrier_verification_scope": list(SUPPORTED_SCOPE_VALUES),
        "declared_non_claims": _false_non_claims(),
        "selected_second_carrier_verification_boundary_result_outcome": BOUNDARY_OUTCOME_RECORDED,
        "selected_second_carrier_verification_boundary_result_version": RESULT_VERSION,
        "selected_second_carrier_verification_boundary_failed_check_count": 0,
        "selected_second_carrier_verification_boundary_declared_future_verification_step": True,
        "selected_second_carrier_verification_boundary_already_created_verification": False,
        "selected_second_carrier_verification_boundary_already_created_external_result": False,
        "selected_second_carrier_verification_boundary_already_created_cross_carrier_evidence": False,
        "selected_second_carrier_verification_boundary_already_created_portable_verification_closure": False,
        "selected_second_carrier_verification_boundary_treated_verification_boundary_as_verification": False,
        "selected_second_carrier_verification_boundary_treated_verification_boundary_as_external_result": False,
        "selected_second_carrier_verification_boundary_treated_verification_boundary_as_cross_carrier_evidence": False,
        "selected_second_carrier_verification_boundary_treated_verification_boundary_as_portable_verification_closure": False,
        "selected_second_carrier_verification_boundary_zero_exit_code_not_verification": True,
        "selected_second_carrier_verification_boundary_ok_not_verification": True,
        "selected_second_carrier_verification_boundary_ran_7_tests_not_cross_carrier_proof": True,
        "selected_second_carrier_verification_boundary_returned_capture_not_cross_carrier_proof": True,
        "selected_second_carrier_verification_boundary_official_enum_scope_strings_redacted": False,
        "selected_second_carrier_verification_boundary_first_success_boundary_test_failure_preserved": True,
        "selected_second_carrier_success_result_outcome": SUCCESS_OUTCOME_RECORDED,
        "selected_second_carrier_success_result_version": RESULT_VERSION,
        "selected_second_carrier_success_failed_check_count": 0,
        "selected_second_carrier_success_bounded_success_recorded": True,
        "selected_second_carrier_success_treated_success_as_verification": False,
        "selected_second_carrier_success_treated_success_as_external_result": False,
        "selected_second_carrier_success_zero_exit_code_not_verification": True,
        "selected_second_carrier_success_ok_not_verification": True,
        "selected_second_carrier_success_ran_7_tests_not_cross_carrier_proof": True,
        "selected_second_carrier_success_boundary_result_outcome": SUCCESS_BOUNDARY_OUTCOME_RECORDED,
        "selected_second_carrier_success_boundary_failed_check_count": 0,
        "selected_second_carrier_result_result_outcome": RESULT_OUTCOME_RECORDED,
        "selected_second_carrier_result_result_version": RESULT_VERSION,
        "selected_second_carrier_result_failed_check_count": 0,
        "selected_second_carrier_result_bounded_result_recorded": True,
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
            "python -m unittest "
            "tests/test_resolve_portable_source_body_verification_second_carrier_success.py"
        ),
        "selected_returned_capture_working_directory": "/Users/markomarkota/IAMMAI-SYSTEM",
        "selected_returned_capture_started_at": "captured-run-started-at-reference",
        "selected_returned_capture_completed_at": "captured-run-completed-at-reference",
        "selected_returned_capture_exit_code": "0",
        "selected_returned_capture_ran_7_tests_line": "Ran 7 tests in 0.451s",
        "selected_returned_capture_ok_line": "OK",
        "selected_returned_capture_raw_placeholder_carrier_label": "raw-placeholder-carrier-label",
        "selected_returned_capture_raw_placeholder_carrier_type": "raw-placeholder-carrier-type",
        "selected_returned_capture_placeholder_fields_unrepaired": True,
        "selected_second_carrier_output_capture_result_outcome": OUTPUT_CAPTURE_OUTCOME_RECORDED,
        "selected_second_carrier_output_capture_failed_check_count": 0,
        "reference_shaped_input_posture": True,
        "requested_second_carrier_verification_outcome": OUTCOME_RECORDED,
    }
    for posture_field in POSTURE_FIELDS:
        request[posture_field] = _posture(posture_field)
    request.update(overrides)
    return request
