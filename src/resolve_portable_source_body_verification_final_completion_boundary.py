"""Bounded portable source-body verification final-completion-boundary resolver.

This module records one future final-completion review step boundary only. It is
downstream of portable verification closure, preserves that final completion has
not been created, and does not create source transfer, source receipt, reception
authorization, source, authority, currentness, runtime, deployment, public
release, operation permission, continuation, reusable permission, derivative
reception, vessel relation, another reception request, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Iterable, Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class PortableSourceBodyVerificationFinalCompletionBoundaryError(Exception):
    """Raised for bounded final-completion-boundary request read failures."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_portable_source_body_verification_final_completion_boundary"
RESULT_TYPE = "portable_source_body_verification_final_completion_boundary_result"
DEFAULT_REQUEST_ID = "portable_source_body_verification_final_completion_boundary_reference_review_001"
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_portable_source_body_verification_final_completion_boundary"
)

CORE_QUESTION = (
    "Can the clean portable-verification-closure basis be bounded for one future "
    "final-completion review step without creating final completion yet, source "
    "transfer, source receipt, reception authorization, source, authority, "
    "currentness, runtime, deployment, public release, operation permission, "
    "continuation, reusable permission, derivative reception, vessel relation, "
    "another reception request, or follow-on work?"
)

INTENT_RECORD = "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_BOUNDARY"
INTENT_BLOCK = "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

OUTCOME_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_BOUNDARY_RECORDED"
OUTCOME_NOT_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_BOUNDARY_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_BOUNDARY_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

PORTABLE_VERIFICATION_CLOSURE_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_PORTABLE_VERIFICATION_CLOSURE_RECORDED"
)
CROSS_CARRIER_EVIDENCE_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_CROSS_CARRIER_EVIDENCE_RECORDED"
)
SECOND_CARRIER_EXTERNAL_RESULT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT_RECORDED"
)
SECOND_CARRIER_VERIFICATION_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_VERIFICATION_RECORDED"
)
SECOND_CARRIER_SUCCESS_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_SUCCESS_RECORDED"
)
SECOND_CARRIER_RESULT_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RESULT_RECORDED"
SECOND_CARRIER_OUTPUT_CAPTURE_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_OUTPUT_CAPTURE_RECORDED"
)

SUPPORTED_SCOPE_VALUES = (
    "FINAL_COMPLETION_BOUNDARY_ONLY",
    "ONE_FUTURE_FINAL_COMPLETION_REVIEW_STEP_ONLY",
    "PORTABLE_VERIFICATION_CLOSURE_BASIS_PRESERVED",
    "PORTABLE_VERIFICATION_CLOSURE_ARTIFACT_BASIS_PRESERVED",
    "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_BASIS_PRESERVED",
    "CROSS_CARRIER_EVIDENCE_BASIS_PRESERVED",
    "RETURNED_SECOND_CARRIER_CAPTURE_BASIS_PRESERVED",
    "CAPTURE_INTAKE_BASIS_PRESERVED",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_PRESERVED",
    "FINAL_COMPLETION_NOT_CREATED",
    "FINAL_COMPLETION_BOUNDARY_NOT_FINAL_COMPLETION",
    "PORTABLE_VERIFICATION_CLOSURE_NOT_FINAL_COMPLETION",
    "ZERO_EXIT_CODE_NOT_FINAL_COMPLETION",
    "STRING_ZERO_NOT_FINAL_COMPLETION",
    "OK_OUTPUT_NOT_FINAL_COMPLETION",
    "RAN_7_TESTS_NOT_FINAL_COMPLETION",
    "RETURNED_CAPTURE_NOT_FINAL_COMPLETION",
    "FINAL_COMPLETION_NOT_SOURCE_TRANSFER",
    "FINAL_COMPLETION_NOT_SOURCE_RECEIPT",
    "FINAL_COMPLETION_NOT_RECEPTION_AUTHORIZATION",
    "RECEIVING_CARRIER_NOT_AUTHORITY",
    "NO_SOURCE_CREATED",
    "NO_AUTHORITY_CREATED",
    "NO_CURRENTNESS_CREATED",
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
    "NO_FINAL_COMPLETION_INFERENCE",
    "NO_SOURCE_INFERENCE",
    "NO_AUTHORITY_INFERENCE",
    "NO_CURRENTNESS_INFERENCE",
    "NO_RUNTIME_INFERENCE",
    "NO_DEPLOYMENT_INFERENCE",
    "NO_PUBLIC_RELEASE_INFERENCE",
    "NO_OPERATION_PERMISSION_INFERENCE",
    "NO_FOLLOW_ON_WORK_INFERENCE",
    "NO_UNBOUNDED_PASS_FAIL_INFERENCE",
    "HIDDEN_REPO_STATE_EXCLUDED",
    "HIDDEN_REPO_STATE_NOT_USED_AS_FINAL_COMPLETION_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_NOT_FINAL_COMPLETION_AUTHORITY",
    "SELECTED_BASIS_REFERENCE_SHAPE_PRESERVED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "PREDECESSOR_CROSS_CARRIER_EVIDENCE_FAILURE_PRESERVED",
    "PREDECESSOR_EXTERNAL_RESULT_V1_FAILURE_PRESERVED",
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
SUPPORTED_FINAL_COMPLETION_BOUNDARY_SCOPE = SUPPORTED_SCOPE_VALUES

ALLOWED_TRUE_RECORDED_FIELDS = (
    "final_completion_boundary_recorded",
    "one_future_final_completion_review_step_declared",
    "portable_verification_closure_basis_preserved",
    "portable_verification_closure_artifact_basis_preserved",
    "portable_verification_closure_boundary_basis_preserved",
    "cross_carrier_evidence_basis_preserved",
    "returned_second_carrier_capture_basis_preserved",
    "capture_intake_basis_preserved",
    "second_carrier_output_capture_basis_preserved",
    "final_completion_not_created",
    "final_completion_boundary_not_final_completion",
    "portable_verification_closure_not_final_completion",
    "zero_exit_code_not_final_completion",
    "string_zero_not_final_completion",
    "ok_output_not_final_completion",
    "ran_7_tests_not_final_completion",
    "returned_capture_not_final_completion",
    "final_completion_not_source_transfer",
    "final_completion_not_source_receipt",
    "final_completion_not_reception_authorization",
    "receiving_carrier_not_authority",
    "source_not_created",
    "authority_not_created",
    "currentness_not_created",
    "runtime_not_created",
    "deployment_not_created",
    "public_release_not_created",
    "operation_permission_not_created",
    "continuation_not_authorized",
    "reusable_permission_not_created",
    "follow_on_work_not_authorized",
    "hidden_repo_state_excluded",
    "hidden_repo_state_not_used_as_final_completion_authority",
    "repo_local_availability_not_final_completion_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "official_enum_scope_strings_not_redacted",
    "hostile_raw_body_content_contained",
    "predecessor_cross_carrier_evidence_failure_preserved",
    "predecessor_external_result_v1_failure_preserved",
    "first_success_boundary_test_failure_preserved",
    "first_result_boundary_resolver_failure_preserved",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
)

REQUIRED_FALSE_NON_CLAIMS = (
    "final_completion_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "final_completion_boundary_treated_as_final_completion",
    "final_completion_boundary_treated_as_source_transfer",
    "final_completion_boundary_treated_as_source_receipt",
    "final_completion_boundary_treated_as_reception_authorization",
    "final_completion_boundary_treated_as_source",
    "final_completion_boundary_treated_as_authority",
    "final_completion_boundary_treated_as_currentness",
    "final_completion_boundary_treated_as_runtime",
    "final_completion_boundary_treated_as_deployment",
    "final_completion_boundary_treated_as_public_release",
    "final_completion_boundary_treated_as_operation_permission",
    "final_completion_boundary_treated_as_continuation",
    "final_completion_boundary_treated_as_reusable_permission",
    "final_completion_boundary_treated_as_follow_on_work",
    "portable_verification_closure_treated_as_final_completion",
    "zero_exit_code_treated_as_final_completion",
    "string_zero_treated_as_final_completion",
    "string_zero_representation_turned_into_doctrine",
    "ok_output_treated_as_final_completion",
    "ran_7_tests_treated_as_final_completion",
    "returned_capture_treated_as_final_completion",
    "receiving_carrier_treated_as_authority",
    "artifact_existence_treated_as_final_completion_authority",
    "artifact_path_treated_as_currentness",
    "repo_local_availability_treated_as_final_completion_authority",
    "hidden_repo_state_used_as_final_completion_content",
    "hidden_repo_state_used_as_final_completion_authority",
    "source_created",
    "authority_created",
    "currentness_created",
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
    "predecessor_cross_carrier_evidence_repaired",
    "predecessor_cross_carrier_evidence_hidden",
    "predecessor_cross_carrier_evidence_claimed_passed",
    "predecessor_external_result_v1_repaired",
    "predecessor_external_result_v1_hidden",
    "predecessor_external_result_v1_claimed_passed",
    "v1_packet_emission_repaired",
    "v1_packet_emission_hidden",
    "v1_packet_emission_claimed_passed",
    "first_success_boundary_test_repaired",
    "first_success_boundary_test_hidden",
    "first_success_boundary_test_claimed_passed",
    "first_result_boundary_resolver_repaired",
    "first_result_boundary_resolver_hidden",
    "first_result_boundary_resolver_claimed_passed",
)

BLOCK_CODES = (
    "FINAL_COMPLETION_BOUNDARY_QUESTION_UNDECLARED",
    "FINAL_COMPLETION_BOUNDARY_INTENT_UNSUPPORTED",
    "PORTABLE_VERIFICATION_CLOSURE_BASIS_MISSING",
    "PORTABLE_VERIFICATION_CLOSURE_NOT_RECORDED",
    "PORTABLE_VERIFICATION_CLOSURE_FAILED_CHECKS_PRESENT",
    "PORTABLE_VERIFICATION_CLOSURE_VERSION_NOT_0_1_0",
    "PORTABLE_VERIFICATION_CLOSURE_DID_NOT_RECORD_BOUNDED_CLOSURE",
    "PORTABLE_VERIFICATION_CLOSURE_ALREADY_CREATED_FINAL_COMPLETION",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_FINAL_COMPLETION",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_SOURCE_TRANSFER",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_SOURCE_RECEIPT",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_RECEPTION_AUTHORIZATION",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_SOURCE",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_AUTHORITY",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_CURRENTNESS",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_RUNTIME",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_DEPLOYMENT",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_PUBLIC_RELEASE",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_OPERATION_PERMISSION",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_FOLLOW_ON_WORK",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_ZERO_EXIT_CODE_AS_FINAL_COMPLETION",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_STRING_ZERO_AS_FINAL_COMPLETION",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_STRING_ZERO_AS_DOCTRINE",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_OK_AS_FINAL_COMPLETION",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_RAN_7_TESTS_AS_FINAL_COMPLETION",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_RETURNED_CAPTURE_AS_FINAL_COMPLETION",
    "PORTABLE_VERIFICATION_CLOSURE_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
    "PREDECESSOR_CROSS_CARRIER_EVIDENCE_FAILURE_MISSING_OR_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
    "PREDECESSOR_EXTERNAL_RESULT_V1_FAILURE_MISSING_OR_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
    "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_BASIS_MISSING",
    "CROSS_CARRIER_EVIDENCE_BASIS_MISSING",
    "CROSS_CARRIER_EVIDENCE_NOT_RECORDED",
    "CROSS_CARRIER_EVIDENCE_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_EXTERNAL_RESULT_BASIS_MISSING",
    "SECOND_CARRIER_EXTERNAL_RESULT_NOT_RECORDED",
    "SECOND_CARRIER_EXTERNAL_RESULT_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_VERIFICATION_BASIS_MISSING",
    "SECOND_CARRIER_VERIFICATION_NOT_RECORDED",
    "SECOND_CARRIER_SUCCESS_BASIS_MISSING",
    "SECOND_CARRIER_SUCCESS_NOT_RECORDED",
    "SECOND_CARRIER_RESULT_BASIS_MISSING",
    "SECOND_CARRIER_RESULT_NOT_RECORDED",
    "RETURNED_CAPTURE_INTAKE_BASIS_MISSING",
    "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
    "RETURNED_CAPTURE_TREATED_AS_FINAL_COMPLETION",
    "ZERO_EXIT_CODE_TREATED_AS_FINAL_COMPLETION",
    "STRING_ZERO_TREATED_AS_FINAL_COMPLETION",
    "STRING_ZERO_REPRESENTATION_TURNED_INTO_DOCTRINE",
    "OK_OUTPUT_TREATED_AS_FINAL_COMPLETION",
    "RAN_7_TESTS_TREATED_AS_FINAL_COMPLETION",
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
    "FINAL_COMPLETION_BOUNDARY_TREATED_AS_FINAL_COMPLETION",
    "FINAL_COMPLETION_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "FINAL_COMPLETION_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "FINAL_COMPLETION_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "FINAL_COMPLETION_BOUNDARY_TREATED_AS_SOURCE",
    "FINAL_COMPLETION_BOUNDARY_TREATED_AS_AUTHORITY",
    "FINAL_COMPLETION_BOUNDARY_TREATED_AS_CURRENTNESS",
    "FINAL_COMPLETION_BOUNDARY_TREATED_AS_RUNTIME",
    "FINAL_COMPLETION_BOUNDARY_TREATED_AS_DEPLOYMENT",
    "FINAL_COMPLETION_BOUNDARY_TREATED_AS_PUBLIC_RELEASE",
    "FINAL_COMPLETION_BOUNDARY_TREATED_AS_OPERATION_PERMISSION",
    "FINAL_COMPLETION_BOUNDARY_TREATED_AS_CONTINUATION",
    "FINAL_COMPLETION_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION",
    "FINAL_COMPLETION_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
    "FINAL_COMPLETION_CREATED",
    "SOURCE_TRANSFER_OCCURRED",
    "SOURCE_RECEIPT_OCCURRED",
    "RECEPTION_AUTHORIZATION_CREATED",
    "SOURCE_CREATED",
    "AUTHORITY_CREATED",
    "CURRENTNESS_CREATED",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_FINAL_COMPLETION_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_FINAL_COMPLETION_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_FINAL_COMPLETION_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_FINAL_COMPLETION_AUTHORITY",
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
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_FINAL_COMPLETION_BOUNDARY",
    "ARTIFACTS_MUTATED",
    "RETURNED_CAPTURE_MATERIAL_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_FINAL_COMPLETION_BOUNDARY_SCOPE",
    "DECLARED_FINAL_COMPLETION_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_FINAL_COMPLETION_BOUNDARY_REQUEST_UNREADABLE",
    "FINAL_COMPLETION_BOUNDARY_EXPLICIT_BLOCK_INTENT",
)

SELECTED_BASIS_KEYS = (
    "selected_portable_verification_closure_basis",
    "selected_portable_verification_closure_terminal_summary_basis",
    "selected_portable_verification_closure_boundary_basis",
    "selected_cross_carrier_evidence_basis",
    "selected_cross_carrier_evidence_terminal_summary_basis",
    "selected_second_carrier_external_result_basis",
    "selected_second_carrier_external_result_terminal_summary_basis",
    "selected_second_carrier_verification_basis",
    "selected_second_carrier_success_basis",
    "selected_second_carrier_result_basis",
    "selected_returned_second_carrier_live_capture_intake_basis",
    "selected_returned_capture_material_basis",
    "selected_second_carrier_output_capture_basis",
    "selected_packet_transfer_basis",
    "selected_packet_emission_basis",
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
    "final_completion_boundary_only_posture",
    "one_future_final_completion_review_step_posture",
    "portable_verification_closure_basis_preserved_posture",
    "portable_verification_closure_artifact_basis_preserved_posture",
    "portable_verification_closure_boundary_basis_preserved_posture",
    "cross_carrier_evidence_basis_preserved_posture",
    "returned_second_carrier_capture_basis_preserved_posture",
    "capture_intake_basis_preserved_posture",
    "second_carrier_output_capture_basis_preserved_posture",
    "final_completion_not_created_posture",
    "final_completion_boundary_not_final_completion_posture",
    "portable_verification_closure_not_final_completion_posture",
    "zero_exit_code_not_final_completion_posture",
    "string_zero_not_final_completion_posture",
    "ok_output_not_final_completion_posture",
    "ran_7_tests_not_final_completion_posture",
    "returned_capture_not_final_completion_posture",
    "final_completion_not_source_transfer_posture",
    "final_completion_not_source_receipt_posture",
    "final_completion_not_reception_authorization_posture",
    "receiving_carrier_not_authority_posture",
    "source_not_created_posture",
    "authority_not_created_posture",
    "currentness_not_created_posture",
    "runtime_not_created_posture",
    "deployment_not_created_posture",
    "public_release_not_created_posture",
    "operation_permission_not_created_posture",
    "continuation_not_authorized_posture",
    "reusable_permission_not_created_posture",
    "follow_on_work_not_authorized_posture",
    "hidden_repo_state_excluded_posture",
    "repo_local_availability_not_final_completion_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_cross_carrier_evidence_failure_preserved_posture",
    "predecessor_external_result_v1_failure_preserved_posture",
    "first_success_boundary_test_failure_preserved_posture",
    "first_result_boundary_resolver_failure_preserved_posture",
)

SENSITIVE_KEY_NAMES = {
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
    "raw_cross_carrier_evidence_body",
    "raw_portable_verification_closure_body",
    "raw_final_completion_body",
    "capture_body",
    "cross_carrier_evidence_body",
    "portable_verification_closure_body",
    "final_completion_body",
    "source_body",
    "authority_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
}
HOSTILE_SENTINELS = (
    "RAW_FINAL_COMPLETION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)
REDACTED_RAW_VALUE = "[bounded-redacted-raw-or-hidden-state]"

OPEN_ITEMS = (
    "final-completion boundary resolver, if separately requested after this resolver",
    "final-completion boundary test",
    "final-completion boundary live artifact",
    "final-completion boundary terminal summary, if needed",
    "final-completion spec/resolver/test/live artifact, if admitted",
    "final-completion review",
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
    "runtime hosting",
    "deployment",
    "public release",
    "continuation",
    "publication flow",
    "reusable permission",
    "successor reception request",
    "follow-on work",
    "optional future numeric-zero declared-input resolver review, if separately selected",
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _is_sensitive_key(key: str) -> bool:
    lowered = key.lower()
    return lowered in SENSITIVE_KEY_NAMES or lowered.endswith("_body")


def _json_safe(value: Any, key: str | None = None) -> Any:
    if key is not None and _is_sensitive_key(key):
        return REDACTED_RAW_VALUE
    if isinstance(value, Mapping):
        return {str(k): _json_safe(v, str(k)) for k, v in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [_json_safe(item, key) for item in value]
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, str):
        if any(sentinel in value for sentinel in HOSTILE_SENTINELS):
            return REDACTED_RAW_VALUE
        return value
    if value is None or isinstance(value, (bool, int, float)):
        return value
    return str(value)


def _copy_json_safe(value: Any) -> Any:
    return _json_safe(copy.deepcopy(value))


def _basis_declared(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, Mapping):
        return bool(value) and value.get("basis_declared") is not False
    if isinstance(value, (list, tuple, set)):
        return bool(value)
    if isinstance(value, str):
        return bool(value.strip())
    return bool(value)


def _is_true(value: Any) -> bool:
    if value is True:
        return True
    if isinstance(value, str):
        return value.strip().lower() in {"true", "yes", "1", "recorded", "preserved"}
    return False


def _is_false(value: Any) -> bool:
    if value is False:
        return True
    if isinstance(value, str):
        return value.strip().lower() in {"false", "no", "0", "not_recorded", "blocked"}
    return False


def _as_int(value: Any, default: int | None = None) -> int | None:
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


def _deep_find(value: Any, names: Iterable[str]) -> Any:
    name_set = set(names)
    if isinstance(value, Mapping):
        for name in name_set:
            if name in value:
                return value[name]
        for child in value.values():
            found = _deep_find(child, name_set)
            if found is not None:
                return found
    if isinstance(value, (list, tuple)):
        for child in value:
            found = _deep_find(child, name_set)
            if found is not None:
                return found
    return None


def _pick(
    request: Mapping[str, Any],
    basis_key: str | None,
    direct_names: Iterable[str],
    nested_names: Iterable[str] = (),
    default: Any = None,
) -> Any:
    direct_value = default
    direct_found = False
    for name in direct_names:
        if name in request:
            direct_value = request[name]
            direct_found = True
            break
    if basis_key is not None:
        basis = request.get(basis_key)
        found = _deep_find(basis, nested_names or direct_names)
        if found is not None:
            return found
    if direct_found:
        return direct_value
    return default


def _section(request: Mapping[str, Any], key: str) -> Any:
    if key in request:
        return _copy_json_safe(request[key])
    return {"basis_declared": False, "basis_key": key}


def _posture_declared(value: Any) -> bool:
    if isinstance(value, Mapping):
        if value.get("declared") is False:
            return False
        if value.get("posture_declared") is False:
            return False
        return bool(value)
    return _basis_declared(value)


def _check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    block_code: str,
) -> dict[str, Any]:
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": _json_safe(expected_posture),
        "actual_posture": _json_safe(actual_posture),
        "block_code": block_code,
    }


def _failed_checks(checks: Iterable[Mapping[str, Any]]) -> list[Mapping[str, Any]]:
    return [check for check in checks if not check.get("passed")]


def _first_failed_code(checks: Iterable[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if not check.get("passed"):
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str):
                return code
    return None


def _scope_values(request: Mapping[str, Any]) -> list[str]:
    raw_scope = request.get("final_completion_boundary_scope", SUPPORTED_SCOPE_VALUES)
    if isinstance(raw_scope, str):
        return [raw_scope]
    if isinstance(raw_scope, Mapping):
        return [str(value) for value in raw_scope.values()]
    if isinstance(raw_scope, Iterable):
        return [str(value) for value in raw_scope]
    return [str(raw_scope)]


def _recorded_statement(outcome: str, checks: list[Mapping[str, Any]]) -> dict[str, bool]:
    recorded = outcome == OUTCOME_RECORDED and not _failed_checks(checks)
    statement = {name: False for name in ALLOWED_TRUE_RECORDED_FIELDS}
    if recorded:
        for name in ALLOWED_TRUE_RECORDED_FIELDS:
            statement[name] = True
        return statement

    # Protective non-inflationary statements remain true even when recording is blocked.
    protective_true = {
        "final_completion_not_created",
        "final_completion_boundary_not_final_completion",
        "portable_verification_closure_not_final_completion",
        "zero_exit_code_not_final_completion",
        "string_zero_not_final_completion",
        "ok_output_not_final_completion",
        "ran_7_tests_not_final_completion",
        "returned_capture_not_final_completion",
        "final_completion_not_source_transfer",
        "final_completion_not_source_receipt",
        "final_completion_not_reception_authorization",
        "receiving_carrier_not_authority",
        "source_not_created",
        "authority_not_created",
        "currentness_not_created",
        "runtime_not_created",
        "deployment_not_created",
        "public_release_not_created",
        "operation_permission_not_created",
        "continuation_not_authorized",
        "reusable_permission_not_created",
        "follow_on_work_not_authorized",
        "hidden_repo_state_excluded",
        "hidden_repo_state_not_used_as_final_completion_authority",
        "repo_local_availability_not_final_completion_authority",
        "raw_full_prior_artifact_body_not_returned",
        "official_enum_scope_strings_not_redacted",
        "hostile_raw_body_content_contained",
        "authorization_token_reuse_blocked",
        "consumed_request_token_remains_closed",
    }
    for name in protective_true:
        statement[name] = True
    return statement


def _non_meaning() -> dict[str, bool]:
    return {
        "final_completion_exists": False,
        "source_transfer_occurred": False,
        "source_receipt_occurred": False,
        "reception_authorization_exists": False,
        "source_exists": False,
        "authority_exists": False,
        "currentness_exists": False,
        "runtime_exists": False,
        "deployment_exists": False,
        "public_release_exists": False,
        "operation_permission_exists": False,
        "continuation_authorized": False,
        "reusable_permission_exists": False,
        "follow_on_work_authorized": False,
        "final_completion_boundary_became_final_completion": False,
        "portable_verification_closure_became_final_completion": False,
        "zero_exit_code_became_final_completion": False,
        "string_zero_became_final_completion": False,
        "string_zero_became_doctrine": False,
        "ok_became_final_completion": False,
        "ran_7_tests_became_final_completion": False,
        "returned_capture_became_final_completion": False,
        "macbook_pro_became_authority": False,
        "repo_local_availability_became_final_completion_authority": False,
        "hidden_repo_state_became_final_completion_authority": False,
    }


def _default_non_claims() -> dict[str, bool]:
    return {name: False for name in REQUIRED_FALSE_NON_CLAIMS}


def _posture_value(name: str) -> dict[str, Any]:
    return {
        "posture_name": name,
        "declared": True,
        "bounded": True,
        "posture": name.replace("_posture", ""),
    }


def _reference_basis(name: str, **values: Any) -> dict[str, Any]:
    basis = {
        "basis_name": name,
        "basis_declared": True,
        "basis_shape": "reference",
    }
    basis.update(values)
    return basis


def _build_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    question = request.get("final_completion_boundary_question")
    checks.append(
        _check(
            "final_completion_boundary_question_declared",
            bool(isinstance(question, str) and question.strip()),
            "declared final-completion-boundary question",
            question,
            "FINAL_COMPLETION_BOUNDARY_QUESTION_UNDECLARED",
        )
    )

    intent = request.get("final_completion_boundary_intent")
    checks.append(
        _check(
            "final_completion_boundary_intent_supported",
            intent in SUPPORTED_INTENTS,
            SUPPORTED_INTENTS,
            intent,
            "FINAL_COMPLETION_BOUNDARY_INTENT_UNSUPPORTED",
        )
    )
    if intent == INTENT_BLOCK:
        checks.append(
            _check(
                "final_completion_boundary_explicit_block_intent",
                False,
                "recording not explicitly blocked",
                intent,
                "FINAL_COMPLETION_BOUNDARY_EXPLICIT_BLOCK_INTENT",
            )
        )

    scope = _scope_values(request)
    unsupported_scope = [value for value in scope if value not in SUPPORTED_SCOPE_VALUES]
    checks.append(
        _check(
            "final_completion_boundary_scope_supported",
            not unsupported_scope,
            "only supported final-completion-boundary scope values",
            unsupported_scope or scope,
            "UNSUPPORTED_FINAL_COMPLETION_BOUNDARY_SCOPE",
        )
    )

    portable_closure_basis = request.get("selected_portable_verification_closure_basis")
    checks.append(
        _check(
            "portable_verification_closure_basis_declared",
            _basis_declared(portable_closure_basis),
            "selected portable-verification-closure basis declared",
            portable_closure_basis,
            "PORTABLE_VERIFICATION_CLOSURE_BASIS_MISSING",
        )
    )

    portable_closure_outcome = _pick(
        request,
        "selected_portable_verification_closure_basis",
        ("selected_portable_verification_closure_result_outcome",),
        ("outcome", "result_outcome"),
    )
    checks.append(
        _check(
            "portable_verification_closure_outcome_recorded",
            portable_closure_outcome == PORTABLE_VERIFICATION_CLOSURE_RECORDED,
            PORTABLE_VERIFICATION_CLOSURE_RECORDED,
            portable_closure_outcome,
            "PORTABLE_VERIFICATION_CLOSURE_NOT_RECORDED",
        )
    )

    portable_closure_version = _pick(
        request,
        "selected_portable_verification_closure_basis",
        ("selected_portable_verification_closure_result_version",),
        (
            "result_version",
            "portable_source_body_verification_portable_verification_closure_result_version",
        ),
    )
    checks.append(
        _check(
            "portable_verification_closure_version_0_1_0",
            portable_closure_version == RESULT_VERSION,
            RESULT_VERSION,
            portable_closure_version,
            "PORTABLE_VERIFICATION_CLOSURE_VERSION_NOT_0_1_0",
        )
    )

    portable_closure_failed_count = _as_int(
        _pick(
            request,
            "selected_portable_verification_closure_basis",
            ("selected_portable_verification_closure_failed_check_count",),
            ("failed_check_count",),
        )
    )
    checks.append(
        _check(
            "portable_verification_closure_failed_checks_zero",
            portable_closure_failed_count == 0,
            0,
            portable_closure_failed_count,
            "PORTABLE_VERIFICATION_CLOSURE_FAILED_CHECKS_PRESENT",
        )
    )

    bounded_closure_recorded = _pick(
        request,
        "selected_portable_verification_closure_basis",
        ("selected_portable_verification_closure_bounded_closure_recorded",),
        (
            "bounded_portable_verification_closure_recorded",
            "portable_verification_closure_recorded_bounded",
            "portable_verification_closure_recorded",
        ),
    )
    checks.append(
        _check(
            "portable_verification_closure_recorded_bounded_line_level_closure",
            _is_true(bounded_closure_recorded),
            True,
            bounded_closure_recorded,
            "PORTABLE_VERIFICATION_CLOSURE_DID_NOT_RECORD_BOUNDED_CLOSURE",
        )
    )

    negative_shortcuts = (
        (
            "portable_verification_closure_did_not_already_create_final_completion",
            "selected_portable_verification_closure_already_created_final_completion",
            "PORTABLE_VERIFICATION_CLOSURE_ALREADY_CREATED_FINAL_COMPLETION",
        ),
        (
            "portable_verification_closure_not_treated_as_final_completion",
            "selected_portable_verification_closure_treated_as_final_completion",
            "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_FINAL_COMPLETION",
        ),
        (
            "portable_verification_closure_not_treated_as_source_transfer",
            "selected_portable_verification_closure_treated_as_source_transfer",
            "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_SOURCE_TRANSFER",
        ),
        (
            "portable_verification_closure_not_treated_as_source_receipt",
            "selected_portable_verification_closure_treated_as_source_receipt",
            "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_SOURCE_RECEIPT",
        ),
        (
            "portable_verification_closure_not_treated_as_reception_authorization",
            "selected_portable_verification_closure_treated_as_reception_authorization",
            "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_RECEPTION_AUTHORIZATION",
        ),
        (
            "portable_verification_closure_not_treated_as_source",
            "selected_portable_verification_closure_treated_as_source",
            "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_SOURCE",
        ),
        (
            "portable_verification_closure_not_treated_as_authority",
            "selected_portable_verification_closure_treated_as_authority",
            "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_AUTHORITY",
        ),
        (
            "portable_verification_closure_not_treated_as_currentness",
            "selected_portable_verification_closure_treated_as_currentness",
            "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_CURRENTNESS",
        ),
        (
            "portable_verification_closure_not_treated_as_runtime",
            "selected_portable_verification_closure_treated_as_runtime",
            "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_RUNTIME",
        ),
        (
            "portable_verification_closure_not_treated_as_deployment",
            "selected_portable_verification_closure_treated_as_deployment",
            "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_DEPLOYMENT",
        ),
        (
            "portable_verification_closure_not_treated_as_public_release",
            "selected_portable_verification_closure_treated_as_public_release",
            "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_PUBLIC_RELEASE",
        ),
        (
            "portable_verification_closure_not_treated_as_operation_permission",
            "selected_portable_verification_closure_treated_as_operation_permission",
            "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_OPERATION_PERMISSION",
        ),
        (
            "portable_verification_closure_not_treated_as_follow_on_work",
            "selected_portable_verification_closure_treated_as_follow_on_work",
            "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_FOLLOW_ON_WORK",
        ),
        (
            "portable_verification_closure_not_treated_zero_exit_code_as_final_completion",
            "selected_portable_verification_closure_treated_zero_exit_code_as_final_completion",
            "PORTABLE_VERIFICATION_CLOSURE_TREATED_ZERO_EXIT_CODE_AS_FINAL_COMPLETION",
        ),
        (
            "portable_verification_closure_not_treated_string_zero_as_final_completion",
            "selected_portable_verification_closure_treated_string_zero_as_final_completion",
            "PORTABLE_VERIFICATION_CLOSURE_TREATED_STRING_ZERO_AS_FINAL_COMPLETION",
        ),
        (
            "portable_verification_closure_not_treated_string_zero_as_doctrine",
            "selected_portable_verification_closure_treated_string_zero_as_doctrine",
            "PORTABLE_VERIFICATION_CLOSURE_TREATED_STRING_ZERO_AS_DOCTRINE",
        ),
        (
            "portable_verification_closure_not_treated_ok_as_final_completion",
            "selected_portable_verification_closure_treated_ok_as_final_completion",
            "PORTABLE_VERIFICATION_CLOSURE_TREATED_OK_AS_FINAL_COMPLETION",
        ),
        (
            "portable_verification_closure_not_treated_ran_7_tests_as_final_completion",
            "selected_portable_verification_closure_treated_ran_7_tests_as_final_completion",
            "PORTABLE_VERIFICATION_CLOSURE_TREATED_RAN_7_TESTS_AS_FINAL_COMPLETION",
        ),
        (
            "portable_verification_closure_not_treated_returned_capture_as_final_completion",
            "selected_portable_verification_closure_treated_returned_capture_as_final_completion",
            "PORTABLE_VERIFICATION_CLOSURE_TREATED_RETURNED_CAPTURE_AS_FINAL_COMPLETION",
        ),
        (
            "portable_verification_closure_did_not_redact_official_enum_scope_strings",
            "selected_portable_verification_closure_official_enum_scope_strings_redacted",
            "PORTABLE_VERIFICATION_CLOSURE_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
        ),
    )
    for check_name, field_name, code in negative_shortcuts:
        alternate_name = field_name.removeprefix("selected_")
        actual = request.get(field_name, request.get(alternate_name, False))
        checks.append(_check(check_name, not _is_true(actual), False, actual, code))

    positive_shortcuts = (
        (
            "portable_verification_closure_kept_zero_exit_code_not_final_completion",
            "selected_portable_verification_closure_zero_exit_code_not_final_completion",
            "PORTABLE_VERIFICATION_CLOSURE_TREATED_ZERO_EXIT_CODE_AS_FINAL_COMPLETION",
        ),
        (
            "portable_verification_closure_kept_string_zero_not_final_completion",
            "selected_portable_verification_closure_string_zero_not_final_completion",
            "PORTABLE_VERIFICATION_CLOSURE_TREATED_STRING_ZERO_AS_FINAL_COMPLETION",
        ),
        (
            "portable_verification_closure_kept_ok_not_final_completion",
            "selected_portable_verification_closure_ok_not_final_completion",
            "PORTABLE_VERIFICATION_CLOSURE_TREATED_OK_AS_FINAL_COMPLETION",
        ),
        (
            "portable_verification_closure_kept_ran_7_tests_not_final_completion",
            "selected_portable_verification_closure_ran_7_tests_not_final_completion",
            "PORTABLE_VERIFICATION_CLOSURE_TREATED_RAN_7_TESTS_AS_FINAL_COMPLETION",
        ),
        (
            "portable_verification_closure_kept_returned_capture_not_final_completion",
            "selected_portable_verification_closure_returned_capture_not_final_completion",
            "PORTABLE_VERIFICATION_CLOSURE_TREATED_RETURNED_CAPTURE_AS_FINAL_COMPLETION",
        ),
        (
            "predecessor_cross_carrier_evidence_failure_preserved",
            "predecessor_cross_carrier_evidence_failure_preserved",
            "PREDECESSOR_CROSS_CARRIER_EVIDENCE_FAILURE_MISSING_OR_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
        ),
        (
            "predecessor_external_result_v1_failure_preserved",
            "predecessor_external_result_v1_failure_preserved",
            "PREDECESSOR_EXTERNAL_RESULT_V1_FAILURE_MISSING_OR_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
        ),
    )
    for check_name, field_name, code in positive_shortcuts:
        if field_name == "predecessor_cross_carrier_evidence_failure_preserved":
            actual = request.get(
                "selected_portable_verification_closure_predecessor_cross_carrier_evidence_failure_preserved",
                request.get(field_name),
            )
        else:
            actual = request.get(field_name)
        checks.append(_check(check_name, _is_true(actual), True, actual, code))

    string_zero_doctrine = request.get("string_zero_representation_turned_into_doctrine", False)
    declared_non_claims = request.get("declared_non_claims", {})
    if isinstance(declared_non_claims, Mapping):
        string_zero_doctrine = declared_non_claims.get(
            "string_zero_representation_turned_into_doctrine", string_zero_doctrine
        )
    checks.append(
        _check(
            "declared_string_zero_representation_not_doctrine",
            _is_false(string_zero_doctrine),
            False,
            string_zero_doctrine,
            "PORTABLE_VERIFICATION_CLOSURE_TREATED_STRING_ZERO_AS_DOCTRINE",
        )
    )

    checks.append(
        _check(
            "portable_verification_closure_boundary_basis_declared",
            _basis_declared(request.get("selected_portable_verification_closure_boundary_basis")),
            "selected portable-verification-closure-boundary basis declared",
            request.get("selected_portable_verification_closure_boundary_basis"),
            "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_BASIS_MISSING",
        )
    )

    cross_basis = request.get("selected_cross_carrier_evidence_basis")
    checks.append(
        _check(
            "cross_carrier_evidence_basis_declared",
            _basis_declared(cross_basis),
            "selected cross-carrier evidence basis declared",
            cross_basis,
            "CROSS_CARRIER_EVIDENCE_BASIS_MISSING",
        )
    )
    cross_outcome = _pick(
        request,
        "selected_cross_carrier_evidence_basis",
        ("selected_cross_carrier_evidence_result_outcome",),
        ("outcome", "result_outcome"),
    )
    checks.append(
        _check(
            "cross_carrier_evidence_recorded",
            cross_outcome == CROSS_CARRIER_EVIDENCE_RECORDED,
            CROSS_CARRIER_EVIDENCE_RECORDED,
            cross_outcome,
            "CROSS_CARRIER_EVIDENCE_NOT_RECORDED",
        )
    )
    cross_failed = _as_int(request.get("selected_cross_carrier_evidence_failed_check_count", 0))
    checks.append(
        _check(
            "cross_carrier_evidence_failed_checks_zero",
            cross_failed == 0,
            0,
            cross_failed,
            "CROSS_CARRIER_EVIDENCE_FAILED_CHECKS_PRESENT",
        )
    )

    external_basis = request.get("selected_second_carrier_external_result_basis")
    checks.append(
        _check(
            "second_carrier_external_result_basis_declared",
            _basis_declared(external_basis),
            "selected second-carrier external-result basis declared",
            external_basis,
            "SECOND_CARRIER_EXTERNAL_RESULT_BASIS_MISSING",
        )
    )
    external_outcome = _pick(
        request,
        "selected_second_carrier_external_result_basis",
        ("selected_second_carrier_external_result_result_outcome",),
        ("outcome", "result_outcome"),
    )
    checks.append(
        _check(
            "second_carrier_external_result_recorded",
            external_outcome == SECOND_CARRIER_EXTERNAL_RESULT_RECORDED,
            SECOND_CARRIER_EXTERNAL_RESULT_RECORDED,
            external_outcome,
            "SECOND_CARRIER_EXTERNAL_RESULT_NOT_RECORDED",
        )
    )
    external_failed = _as_int(
        request.get("selected_second_carrier_external_result_failed_check_count", 0)
    )
    checks.append(
        _check(
            "second_carrier_external_result_failed_checks_zero",
            external_failed == 0,
            0,
            external_failed,
            "SECOND_CARRIER_EXTERNAL_RESULT_FAILED_CHECKS_PRESENT",
        )
    )

    for basis_key, shortcut, expected, missing_code, not_recorded_code, check_label in (
        (
            "selected_second_carrier_verification_basis",
            "selected_second_carrier_verification_result_outcome",
            SECOND_CARRIER_VERIFICATION_RECORDED,
            "SECOND_CARRIER_VERIFICATION_BASIS_MISSING",
            "SECOND_CARRIER_VERIFICATION_NOT_RECORDED",
            "second_carrier_verification",
        ),
        (
            "selected_second_carrier_success_basis",
            "selected_second_carrier_success_result_outcome",
            SECOND_CARRIER_SUCCESS_RECORDED,
            "SECOND_CARRIER_SUCCESS_BASIS_MISSING",
            "SECOND_CARRIER_SUCCESS_NOT_RECORDED",
            "second_carrier_success",
        ),
        (
            "selected_second_carrier_result_basis",
            "selected_second_carrier_result_result_outcome",
            SECOND_CARRIER_RESULT_RECORDED,
            "SECOND_CARRIER_RESULT_BASIS_MISSING",
            "SECOND_CARRIER_RESULT_NOT_RECORDED",
            "second_carrier_result",
        ),
    ):
        basis = request.get(basis_key)
        checks.append(
            _check(
                f"{check_label}_basis_declared",
                _basis_declared(basis),
                f"selected {check_label.replace('_', '-')} basis declared",
                basis,
                missing_code,
            )
        )
        outcome = _pick(request, basis_key, (shortcut,), ("outcome", "result_outcome"))
        checks.append(
            _check(
                f"{check_label}_recorded",
                outcome == expected,
                expected,
                outcome,
                not_recorded_code,
            )
        )

    capture_intake_basis = request.get("selected_returned_second_carrier_live_capture_intake_basis")
    checks.append(
        _check(
            "returned_capture_intake_basis_declared",
            _basis_declared(capture_intake_basis),
            "selected returned second-carrier live capture intake basis declared",
            capture_intake_basis,
            "RETURNED_CAPTURE_INTAKE_BASIS_MISSING",
        )
    )
    capture_intake_preserved = request.get("selected_returned_capture_intake_preserved")
    checks.append(
        _check(
            "returned_capture_intake_preserved",
            _is_true(capture_intake_preserved),
            True,
            capture_intake_preserved,
            "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
        )
    )
    capture_only = request.get("selected_returned_capture_intake_capture_only", True)
    checks.append(
        _check(
            "returned_capture_intake_not_final_completion",
            _is_true(capture_only),
            True,
            capture_only,
            "RETURNED_CAPTURE_TREATED_AS_FINAL_COMPLETION",
        )
    )

    checks.append(
        _check(
            "returned_capture_material_basis_declared",
            _basis_declared(request.get("selected_returned_capture_material_basis")),
            "selected returned capture material basis declared",
            request.get("selected_returned_capture_material_basis"),
            "RETURNED_CAPTURE_MATERIAL_MISSING",
        )
    )
    for field_name, code, label in (
        ("selected_returned_capture_zip_path", "RETURNED_ZIP_PATH_MISSING", "returned zip path"),
        ("selected_returned_capture_hash_path", "RETURNED_HASH_PATH_MISSING", "returned hash path"),
        (
            "selected_returned_capture_extracted_directory_path",
            "RETURNED_EXTRACTED_DIRECTORY_MISSING",
            "returned extracted directory path",
        ),
        (
            "selected_returned_capture_combined_terminal_log_path",
            "RETURNED_COMBINED_TERMINAL_LOG_MISSING",
            "returned combined terminal log path",
        ),
        ("selected_returned_capture_exit_code", "RETURNED_EXIT_CODE_MISSING", "returned exit code"),
        ("selected_returned_capture_command_text", "RETURNED_COMMAND_TEXT_MISSING", "returned command text"),
        ("selected_returned_capture_started_at", "RETURNED_TIMESTAMPS_MISSING", "returned start timestamp"),
        ("selected_returned_capture_completed_at", "RETURNED_TIMESTAMPS_MISSING", "returned completion timestamp"),
    ):
        actual = request.get(field_name)
        checks.append(
            _check(
                f"{field_name}_declared",
                _basis_declared(actual) or actual == 0,
                f"{label} declared as basis only",
                actual,
                code,
            )
        )

    placeholder_unrepaired = request.get("selected_returned_capture_placeholder_fields_unrepaired")
    checks.append(
        _check(
            "raw_placeholder_carrier_fields_preserved_unrepaired",
            _is_true(placeholder_unrepaired),
            True,
            placeholder_unrepaired,
            "PLACEHOLDER_CARRIER_FIELDS_REPAIRED",
        )
    )

    output_capture_basis = request.get("selected_second_carrier_output_capture_basis")
    checks.append(
        _check(
            "second_carrier_output_capture_basis_declared",
            _basis_declared(output_capture_basis),
            "selected second-carrier output capture basis declared",
            output_capture_basis,
            "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_MISSING",
        )
    )
    output_capture_outcome = _pick(
        request,
        "selected_second_carrier_output_capture_basis",
        ("selected_second_carrier_output_capture_result_outcome",),
        ("outcome", "result_outcome"),
    )
    checks.append(
        _check(
            "second_carrier_output_capture_recorded",
            output_capture_outcome == SECOND_CARRIER_OUTPUT_CAPTURE_RECORDED,
            SECOND_CARRIER_OUTPUT_CAPTURE_RECORDED,
            output_capture_outcome,
            "SECOND_CARRIER_OUTPUT_CAPTURE_NOT_RECORDED",
        )
    )
    output_capture_failed = _as_int(request.get("selected_second_carrier_output_capture_failed_check_count", 0))
    checks.append(
        _check(
            "second_carrier_output_capture_failed_checks_zero",
            output_capture_failed == 0,
            0,
            output_capture_failed,
            "SECOND_CARRIER_OUTPUT_CAPTURE_FAILED_CHECKS_PRESENT",
        )
    )

    predecessor_failure_basis = request.get("selected_predecessor_failure_basis")
    checks.append(
        _check(
            "predecessor_failure_basis_declared",
            _basis_declared(predecessor_failure_basis),
            "selected predecessor failure basis remains visible",
            predecessor_failure_basis,
            "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        )
    )
    for check_name, field_name, code in (
        (
            "first_success_boundary_test_failure_preserved",
            "first_success_boundary_test_failure_preserved",
            "FIRST_SUCCESS_BOUNDARY_TEST_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
        ),
        (
            "first_result_boundary_resolver_failure_preserved",
            "first_result_boundary_resolver_failure_preserved",
            "FIRST_RESULT_BOUNDARY_RESOLVER_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
        ),
        (
            "v1_packet_emission_predecessor_failure_preserved",
            "v1_packet_emission_predecessor_failure_preserved",
            "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        ),
    ):
        actual = request.get(field_name, _deep_find(predecessor_failure_basis, (field_name,)))
        checks.append(_check(check_name, _is_true(actual), True, actual, code))
    for check_name, field_name in (
        ("predecessor_failure_not_repaired", "repaired"),
        ("predecessor_failure_not_hidden", "hidden"),
        ("predecessor_failure_not_claimed_passed", "claimed_passed"),
    ):
        actual = request.get(field_name, _deep_find(predecessor_failure_basis, (field_name,)))
        checks.append(
            _check(
                check_name,
                not _is_true(actual),
                False,
                actual,
                "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
            )
        )

    reference_shaped = request.get("reference_shaped_input_posture", True)
    checks.append(
        _check(
            "selected_basis_reference_shaped",
            _is_true(reference_shaped),
            True,
            reference_shaped,
            "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
        )
    )
    for check_name, field_name, code in (
        (
            "artifacts_not_mutated",
            "artifacts_mutated",
            "ARTIFACTS_MUTATED",
        ),
        (
            "full_prior_artifact_body_not_emitted_outside_boundary",
            "full_prior_artifact_body_emitted_outside_bounded_final_completion_boundary",
            "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_FINAL_COMPLETION_BOUNDARY",
        ),
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
    ):
        actual = request.get(field_name, False)
        checks.append(_check(check_name, not _is_true(actual), False, actual, code))

    posture_codes = {
        "final_completion_boundary_only_posture": "FINAL_COMPLETION_BOUNDARY_TREATED_AS_FINAL_COMPLETION",
        "one_future_final_completion_review_step_posture": "FINAL_COMPLETION_BOUNDARY_QUESTION_UNDECLARED",
        "portable_verification_closure_basis_preserved_posture": "PORTABLE_VERIFICATION_CLOSURE_BASIS_MISSING",
        "portable_verification_closure_artifact_basis_preserved_posture": "PORTABLE_VERIFICATION_CLOSURE_BASIS_MISSING",
        "portable_verification_closure_boundary_basis_preserved_posture": "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_BASIS_MISSING",
        "cross_carrier_evidence_basis_preserved_posture": "CROSS_CARRIER_EVIDENCE_BASIS_MISSING",
        "returned_second_carrier_capture_basis_preserved_posture": "RETURNED_CAPTURE_MATERIAL_MISSING",
        "capture_intake_basis_preserved_posture": "RETURNED_CAPTURE_INTAKE_BASIS_MISSING",
        "second_carrier_output_capture_basis_preserved_posture": "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_MISSING",
        "final_completion_not_created_posture": "FINAL_COMPLETION_CREATED",
        "final_completion_boundary_not_final_completion_posture": "FINAL_COMPLETION_BOUNDARY_TREATED_AS_FINAL_COMPLETION",
        "portable_verification_closure_not_final_completion_posture": "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_FINAL_COMPLETION",
        "zero_exit_code_not_final_completion_posture": "ZERO_EXIT_CODE_TREATED_AS_FINAL_COMPLETION",
        "string_zero_not_final_completion_posture": "STRING_ZERO_TREATED_AS_FINAL_COMPLETION",
        "ok_output_not_final_completion_posture": "OK_OUTPUT_TREATED_AS_FINAL_COMPLETION",
        "ran_7_tests_not_final_completion_posture": "RAN_7_TESTS_TREATED_AS_FINAL_COMPLETION",
        "returned_capture_not_final_completion_posture": "RETURNED_CAPTURE_TREATED_AS_FINAL_COMPLETION",
        "final_completion_not_source_transfer_posture": "SOURCE_TRANSFER_OCCURRED",
        "final_completion_not_source_receipt_posture": "SOURCE_RECEIPT_OCCURRED",
        "final_completion_not_reception_authorization_posture": "RECEPTION_AUTHORIZATION_CREATED",
        "receiving_carrier_not_authority_posture": "RECEIVING_CARRIER_TREATED_AS_AUTHORITY",
        "source_not_created_posture": "SOURCE_CREATED",
        "authority_not_created_posture": "AUTHORITY_CREATED",
        "currentness_not_created_posture": "CURRENTNESS_CREATED",
        "runtime_not_created_posture": "RUNTIME_HOSTING_CREATED",
        "deployment_not_created_posture": "DEPLOYMENT_CREATED",
        "public_release_not_created_posture": "PUBLIC_RELEASE_CREATED",
        "operation_permission_not_created_posture": "OPERATION_PERMISSION_CREATED",
        "continuation_not_authorized_posture": "CONTINUATION_AUTHORIZED",
        "reusable_permission_not_created_posture": "REUSABLE_PERMISSION_CREATED",
        "follow_on_work_not_authorized_posture": "FOLLOW_ON_WORK_AUTHORIZED",
        "hidden_repo_state_excluded_posture": "HIDDEN_REPO_STATE_USED_AS_FINAL_COMPLETION_CONTENT",
        "repo_local_availability_not_final_completion_authority_posture": "REPO_LOCAL_AVAILABILITY_TREATED_AS_FINAL_COMPLETION_AUTHORITY",
        "selected_basis_reference_shape_posture": "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
        "raw_full_prior_artifact_body_not_returned_posture": "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
        "official_enum_scope_strings_not_redacted_posture": "PORTABLE_VERIFICATION_CLOSURE_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
        "hostile_raw_body_content_contained_posture": "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_FINAL_COMPLETION_BOUNDARY",
        "predecessor_cross_carrier_evidence_failure_preserved_posture": "PREDECESSOR_CROSS_CARRIER_EVIDENCE_FAILURE_MISSING_OR_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
        "predecessor_external_result_v1_failure_preserved_posture": "PREDECESSOR_EXTERNAL_RESULT_V1_FAILURE_MISSING_OR_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
        "first_success_boundary_test_failure_preserved_posture": "FIRST_SUCCESS_BOUNDARY_TEST_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
        "first_result_boundary_resolver_failure_preserved_posture": "FIRST_RESULT_BOUNDARY_RESOLVER_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    }
    for key in POSTURE_KEYS:
        actual = request.get(key)
        checks.append(
            _check(
                f"{key}_declared",
                _posture_declared(actual),
                f"{key} declared",
                actual,
                posture_codes[key],
            )
        )

    if isinstance(declared_non_claims, Mapping):
        for claim in REQUIRED_FALSE_NON_CLAIMS:
            actual = request.get(claim, declared_non_claims.get(claim))
            checks.append(
                _check(
                    f"non_claim_{claim}_false",
                    _is_false(actual),
                    False,
                    actual,
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                )
            )
    else:
        checks.append(
            _check(
                "declared_non_claims_mapping",
                False,
                "declared non-claims mapping with explicit false values",
                declared_non_claims,
                "NON_CLAIM_MISSING_OR_FLIPPED",
            )
        )

    return checks


def _determine_outcome(request: Mapping[str, Any], checks: list[Mapping[str, Any]]) -> str:
    if _failed_checks(checks):
        return OUTCOME_BLOCKED
    requested = request.get("requested_final_completion_boundary_outcome")
    if requested in {OUTCOME_NOT_RECORDED, OUTCOME_REQUIRES_ADDITIONAL_BASIS}:
        return str(requested)
    if request.get("final_completion_boundary_intent") == INTENT_DO_NOT_RECORD:
        return OUTCOME_NOT_RECORDED
    return OUTCOME_RECORDED


def _build_result(
    request: Mapping[str, Any],
    checks: list[Mapping[str, Any]],
    outcome: str,
    block_reason: str | None = None,
) -> dict[str, Any]:
    request_id = str(request.get("final_completion_boundary_request_id") or DEFAULT_REQUEST_ID)
    failed = _failed_checks(checks)
    block_code = _first_failed_code(checks)
    statement = _recorded_statement(outcome, checks)
    metadata = {
        "portable_source_body_verification_final_completion_boundary_result_id": (
            f"{request_id}__portable_source_body_verification_final_completion_boundary_result"
        ),
        "portable_source_body_verification_final_completion_boundary_result_type": RESULT_TYPE,
        "portable_source_body_verification_final_completion_boundary_result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
        "final_completion_boundary_request_id": request_id,
        "passed_check_count": len(checks) - len(failed),
        "failed_check_count": len(failed),
    }
    block = None
    if outcome == OUTCOME_BLOCKED:
        block = {
            "blocked": True,
            "block_code": block_code or "DECLARED_FINAL_COMPLETION_BOUNDARY_REQUEST_MALFORMED",
            "block_reason": block_reason or "Final-completion-boundary review blocked.",
        }

    result: dict[str, Any] = {
        "portable_source_body_verification_final_completion_boundary_metadata": metadata,
        "declared_final_completion_boundary_question": {
            "final_completion_boundary_request_id": request_id,
            "final_completion_boundary_question": request.get("final_completion_boundary_question"),
            "final_completion_boundary_intent": request.get("final_completion_boundary_intent"),
        },
    }
    for key in SELECTED_BASIS_KEYS:
        result[key] = _section(request, key)
    for key in POSTURE_KEYS:
        result[key] = _section(request, key)
    result.update(
        {
            "final_completion_boundary_scope": _json_safe(_scope_values(request)),
            "final_completion_boundary_checks": _json_safe(checks),
            "final_completion_boundary_statement": statement,
            "final_completion_boundary_non_meaning": _non_meaning(),
            "additional_basis_required": {
                "required": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                "basis": _json_safe(request.get("additional_basis_context", [])),
                "scheduled": False,
                "authorized": False,
                "executed": False,
            },
            "not_recorded_basis": {
                "not_recorded": outcome == OUTCOME_NOT_RECORDED,
                "basis": _json_safe(request.get("not_recorded_basis", [])),
                "prior_artifacts_mutated": False,
                "next_work_authorized": False,
            },
            "what_remains_open": list(OPEN_ITEMS),
            "non_claims": _json_safe(request.get("declared_non_claims", _default_non_claims())),
            "outcome": outcome,
            "block": block,
        }
    )
    result["portable_source_body_verification_final_completion_boundary_summary"] = (
        build_portable_source_body_verification_final_completion_boundary_summary(result)
    )
    return result


def _malformed_result(code: str, reason: str) -> dict[str, Any]:
    request = build_declared_portable_source_body_verification_final_completion_boundary_request(
        final_completion_boundary_request_id="malformed_final_completion_boundary_request",
        final_completion_boundary_question="",
        final_completion_boundary_intent=INTENT_BLOCK,
    )
    checks = [
        _check(
            "declared_final_completion_boundary_request_readable_mapping",
            False,
            "readable declared final-completion-boundary request mapping",
            reason,
            code,
        )
    ]
    return _build_result(request, checks, OUTCOME_BLOCKED, reason)


def resolve_portable_source_body_verification_final_completion_boundary(
    declared_final_completion_boundary_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded final-completion-boundary request mapping."""

    if declared_final_completion_boundary_request is None:
        return _malformed_result(
            "DECLARED_FINAL_COMPLETION_BOUNDARY_REQUEST_MALFORMED",
            "Declared final-completion-boundary request is missing.",
        )
    if not isinstance(declared_final_completion_boundary_request, Mapping):
        return _malformed_result(
            "DECLARED_FINAL_COMPLETION_BOUNDARY_REQUEST_MALFORMED",
            "Declared final-completion-boundary request is not a mapping.",
        )

    request = copy.deepcopy(dict(declared_final_completion_boundary_request))
    checks = _build_checks(request)
    outcome = _determine_outcome(request, checks)
    return _build_result(request, checks, outcome)


def resolve_portable_source_body_verification_final_completion_boundary_from_path(
    declared_final_completion_boundary_request_path: Path | str,
) -> dict[str, Any]:
    """Read a JSON request path and resolve final-completion-boundary posture."""

    path = Path(declared_final_completion_boundary_request_path)
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise PortableSourceBodyVerificationFinalCompletionBoundaryError(
            f"Declared final-completion-boundary request is unreadable: {path}"
        ) from exc
    try:
        request = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise PortableSourceBodyVerificationFinalCompletionBoundaryError(
            f"Declared final-completion-boundary request is malformed JSON: {path}"
        ) from exc
    if not isinstance(request, Mapping):
        raise PortableSourceBodyVerificationFinalCompletionBoundaryError(
            f"Declared final-completion-boundary request must be a JSON object: {path}"
        )
    return resolve_portable_source_body_verification_final_completion_boundary(request)


def _summary_field(result: Mapping[str, Any], field_name: str) -> bool:
    statement = result.get("final_completion_boundary_statement", {})
    if isinstance(statement, Mapping):
        return bool(statement.get(field_name))
    return False


def build_portable_source_body_verification_final_completion_boundary_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a bounded summary for a final-completion-boundary result."""

    metadata = result.get("portable_source_body_verification_final_completion_boundary_metadata", {})
    question = result.get("declared_final_completion_boundary_question", {})
    checks = result.get("final_completion_boundary_checks", [])
    if not isinstance(metadata, Mapping):
        metadata = {}
    if not isinstance(question, Mapping):
        question = {}
    if not isinstance(checks, list):
        checks = []
    failed_count = len([check for check in checks if isinstance(check, Mapping) and not check.get("passed")])
    passed_count = len([check for check in checks if isinstance(check, Mapping) and check.get("passed")])
    block = result.get("block") if isinstance(result.get("block"), Mapping) else {}
    portable_closure_basis = result.get("selected_portable_verification_closure_basis", {})
    returned_capture_basis = result.get("selected_returned_capture_material_basis", {})
    capture_intake_basis = result.get("selected_returned_second_carrier_live_capture_intake_basis", {})

    summary = {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") if isinstance(block, Mapping) else None,
        "block_reason": block.get("block_reason") if isinstance(block, Mapping) else None,
        "request_id": question.get("final_completion_boundary_request_id")
        or metadata.get("final_completion_boundary_request_id"),
        "question": question.get("final_completion_boundary_question"),
        "intent": question.get("final_completion_boundary_intent"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": metadata.get(
            "portable_source_body_verification_final_completion_boundary_result_version",
            RESULT_VERSION,
        ),
        "resolver_module": metadata.get("resolver_module", RESOLVER_MODULE),
    }
    for field in ALLOWED_TRUE_RECORDED_FIELDS:
        summary[field] = _summary_field(result, field)

    summary.update(
        {
            "selected_portable_verification_closure_outcome": _deep_find(
                portable_closure_basis, ("outcome", "result_outcome")
            ),
            "selected_portable_verification_closure_version": _deep_find(
                portable_closure_basis,
                (
                    "result_version",
                    "portable_source_body_verification_portable_verification_closure_result_version",
                ),
            ),
            "selected_portable_verification_closure_failed_check_count": _deep_find(
                portable_closure_basis, ("failed_check_count",)
            ),
            "selected_returned_capture_intake_path": _deep_find(
                capture_intake_basis, ("path", "intake_path", "selected_returned_capture_intake_path")
            ),
            "selected_returned_capture_zip_path": _deep_find(
                returned_capture_basis, ("zip_path", "selected_returned_capture_zip_path")
            ),
            "selected_returned_capture_hash_path": _deep_find(
                returned_capture_basis, ("hash_path", "selected_returned_capture_hash_path")
            ),
            "selected_returned_capture_extracted_directory_path": _deep_find(
                returned_capture_basis,
                ("extracted_directory_path", "selected_returned_capture_extracted_directory_path"),
            ),
            "selected_returned_capture_exit_code": _deep_find(
                returned_capture_basis, ("exit_code", "selected_returned_capture_exit_code")
            ),
            "selected_returned_capture_declared_exit_code": _deep_find(
                returned_capture_basis, ("declared_exit_code", "selected_returned_capture_declared_exit_code")
            ),
            "selected_returned_capture_ok_line": _deep_find(
                returned_capture_basis, ("ok_line", "selected_returned_capture_ok_line")
            ),
            "no_final_completion": not bool(result.get("non_claims", {}).get("final_completion_created"))
            if isinstance(result.get("non_claims"), Mapping)
            else True,
            "no_source_authority_currentness_runtime_deployment_public_release_follow_on": all(
                not bool(result.get("non_claims", {}).get(name))
                for name in (
                    "source_created",
                    "authority_created",
                    "currentness_created",
                    "runtime_hosting_created",
                    "deployment_created",
                    "public_release_created",
                    "follow_on_work_authorized",
                )
            )
            if isinstance(result.get("non_claims"), Mapping)
            else True,
            "predecessor_cross_carrier_evidence_failure_preserved": _summary_field(
                result, "predecessor_cross_carrier_evidence_failure_preserved"
            ),
            "predecessor_external_result_v1_failure_preserved": _summary_field(
                result, "predecessor_external_result_v1_failure_preserved"
            ),
            "first_success_boundary_test_preserved_as_failed_predecessor": _summary_field(
                result, "first_success_boundary_test_failure_preserved"
            ),
            "v1_packet_emission_predecessor_failure_preserved": True,
            "first_result_boundary_resolver_preserved_as_failed_predecessor": _summary_field(
                result, "first_result_boundary_resolver_failure_preserved"
            ),
            "final_completion_created": False,
            "source_transfer_occurred": False,
            "source_receipt_occurred": False,
            "reception_authorization_created": False,
            "string_zero_representation_turned_into_doctrine": False,
            "authorization_token_reused": False,
            "consumed_request_reopened": False,
        }
    )
    return _json_safe(summary)


def _deduplicated_output_path(path: Path) -> Path:
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


def write_portable_source_body_verification_final_completion_boundary_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a bounded final-completion-boundary result JSON without overwriting."""

    metadata = result.get("portable_source_body_verification_final_completion_boundary_metadata", {})
    request_id = DEFAULT_REQUEST_ID
    if isinstance(metadata, Mapping):
        request_id = str(metadata.get("final_completion_boundary_request_id") or request_id)
    filename = f"{request_id}__portable_source_body_verification_final_completion_boundary_result.json"
    if output_path is None:
        path = OUTPUT_ROOT / filename
    else:
        candidate = Path(output_path)
        path = candidate / filename if candidate.suffix == "" else candidate
    path = _deduplicated_output_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(_json_safe(result), indent=2, sort_keys=True, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    return path


def build_declared_portable_source_body_verification_final_completion_boundary_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Build a valid declared final-completion-boundary request."""

    non_claims = _default_non_claims()
    request: dict[str, Any] = {
        "final_completion_boundary_request_id": DEFAULT_REQUEST_ID,
        "final_completion_boundary_question": CORE_QUESTION,
        "final_completion_boundary_intent": INTENT_RECORD,
        "final_completion_boundary_scope": list(SUPPORTED_SCOPE_VALUES),
        "selected_portable_verification_closure_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_"
            "portable_verification_closure/portable_source_body_verification_portable_"
            "verification_closure_reference_review_001__portable_source_body_verification_"
            "portable_verification_closure_result.json"
        ),
        "selected_portable_verification_closure_result_outcome": PORTABLE_VERIFICATION_CLOSURE_RECORDED,
        "selected_portable_verification_closure_result_version": RESULT_VERSION,
        "selected_portable_verification_closure_failed_check_count": 0,
        "selected_portable_verification_closure_bounded_closure_recorded": True,
        "selected_portable_verification_closure_already_created_final_completion": False,
        "selected_portable_verification_closure_treated_as_final_completion": False,
        "selected_portable_verification_closure_treated_as_source_transfer": False,
        "selected_portable_verification_closure_treated_as_source_receipt": False,
        "selected_portable_verification_closure_treated_as_reception_authorization": False,
        "selected_portable_verification_closure_treated_as_source": False,
        "selected_portable_verification_closure_treated_as_authority": False,
        "selected_portable_verification_closure_treated_as_currentness": False,
        "selected_portable_verification_closure_treated_as_runtime": False,
        "selected_portable_verification_closure_treated_as_deployment": False,
        "selected_portable_verification_closure_treated_as_public_release": False,
        "selected_portable_verification_closure_treated_as_operation_permission": False,
        "selected_portable_verification_closure_treated_as_follow_on_work": False,
        "selected_portable_verification_closure_zero_exit_code_not_final_completion": True,
        "selected_portable_verification_closure_string_zero_not_final_completion": True,
        "selected_portable_verification_closure_ok_not_final_completion": True,
        "selected_portable_verification_closure_ran_7_tests_not_final_completion": True,
        "selected_portable_verification_closure_returned_capture_not_final_completion": True,
        "selected_portable_verification_closure_official_enum_scope_strings_redacted": False,
        "selected_portable_verification_closure_predecessor_cross_carrier_evidence_failure_preserved": True,
        "selected_portable_verification_closure_boundary_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_"
            "portable_verification_closure_boundary/portable_source_body_verification_"
            "portable_verification_closure_boundary_reference_review_001__portable_source_body_"
            "verification_portable_verification_closure_boundary_result.json"
        ),
        "selected_cross_carrier_evidence_result_outcome": CROSS_CARRIER_EVIDENCE_RECORDED,
        "selected_cross_carrier_evidence_failed_check_count": 0,
        "selected_second_carrier_external_result_result_outcome": SECOND_CARRIER_EXTERNAL_RESULT_RECORDED,
        "selected_second_carrier_external_result_failed_check_count": 0,
        "selected_second_carrier_verification_result_outcome": SECOND_CARRIER_VERIFICATION_RECORDED,
        "selected_second_carrier_success_result_outcome": SECOND_CARRIER_SUCCESS_RECORDED,
        "selected_second_carrier_result_result_outcome": SECOND_CARRIER_RESULT_RECORDED,
        "selected_returned_capture_intake_path": (
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_RETURNED_SECOND_CARRIER_LIVE_CAPTURE_INTAKE_V0.md"
        ),
        "selected_returned_capture_intake_preserved": True,
        "selected_returned_capture_intake_capture_only": True,
        "selected_returned_capture_from_macbook_pro_to_macbook_air": True,
        "selected_returned_capture_zip_path": (
            "artifacts/actual_second_carrier_live_capture/"
            "portable_source_body_verification_actual_second_carrier_capture_001/original_zip/"
            "iammai_second_carrier_capture_001.zip"
        ),
        "selected_returned_capture_hash_path": (
            "artifacts/actual_second_carrier_live_capture/"
            "portable_source_body_verification_actual_second_carrier_capture_001/hashes/"
            "iammai_second_carrier_capture_001.sha256"
        ),
        "selected_returned_capture_extracted_directory_path": (
            "artifacts/actual_second_carrier_live_capture/"
            "portable_source_body_verification_actual_second_carrier_capture_001/extracted/"
            "iammai_second_carrier_capture_001"
        ),
        "selected_returned_capture_combined_terminal_log_path": (
            "artifacts/actual_second_carrier_live_capture/"
            "portable_source_body_verification_actual_second_carrier_capture_001/extracted/"
            "iammai_second_carrier_capture_001/combined_terminal_log.txt"
        ),
        "selected_returned_capture_stdout_path": (
            "artifacts/actual_second_carrier_live_capture/"
            "portable_source_body_verification_actual_second_carrier_capture_001/extracted/"
            "iammai_second_carrier_capture_001/stdout.txt"
        ),
        "selected_returned_capture_stderr_path": (
            "artifacts/actual_second_carrier_live_capture/"
            "portable_source_body_verification_actual_second_carrier_capture_001/extracted/"
            "iammai_second_carrier_capture_001/stderr.txt"
        ),
        "selected_returned_capture_command_text": "python -m unittest",
        "selected_returned_capture_working_directory": "/Users/markomarkota/IAMMAI-SYSTEM",
        "selected_returned_capture_started_at": "2026-05-12T00:00:00Z",
        "selected_returned_capture_completed_at": "2026-05-12T00:00:01Z",
        "selected_returned_capture_exit_code": 0,
        "selected_returned_capture_declared_exit_code": "0",
        "selected_returned_capture_ran_7_tests_line": "Ran 7 tests in 0.451s",
        "selected_returned_capture_ok_line": "OK",
        "selected_returned_capture_raw_placeholder_carrier_label": "raw placeholder carrier field",
        "selected_returned_capture_raw_placeholder_carrier_type": "raw placeholder carrier field",
        "selected_returned_capture_placeholder_fields_unrepaired": True,
        "selected_second_carrier_output_capture_result_outcome": SECOND_CARRIER_OUTPUT_CAPTURE_RECORDED,
        "selected_second_carrier_output_capture_failed_check_count": 0,
        "predecessor_cross_carrier_evidence_failure_preserved": True,
        "predecessor_external_result_v1_failure_preserved": True,
        "first_success_boundary_test_failure_preserved": True,
        "first_result_boundary_resolver_failure_preserved": True,
        "v1_packet_emission_predecessor_failure_preserved": True,
        "reference_shaped_input_posture": True,
        "declared_non_claims": non_claims,
    }

    request["selected_portable_verification_closure_basis"] = _reference_basis(
        "portable_verification_closure",
        outcome=PORTABLE_VERIFICATION_CLOSURE_RECORDED,
        result_version=RESULT_VERSION,
        failed_check_count=0,
        bounded_portable_verification_closure_recorded=True,
        portable_verification_closure_not_final_completion=True,
        final_completion_not_created=True,
    )
    request["selected_portable_verification_closure_terminal_summary_basis"] = _reference_basis(
        "portable_verification_closure_terminal_summary",
        path="spec/PORTABLE_SOURCE_BODY_VERIFICATION_PORTABLE_VERIFICATION_CLOSURE_TERMINAL_SUMMARY_V0.md",
    )
    request["selected_portable_verification_closure_boundary_basis"] = _reference_basis(
        "portable_verification_closure_boundary",
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_RECORDED",
        result_version=RESULT_VERSION,
        failed_check_count=0,
    )
    request["selected_cross_carrier_evidence_basis"] = _reference_basis(
        "cross_carrier_evidence",
        outcome=CROSS_CARRIER_EVIDENCE_RECORDED,
        failed_check_count=0,
    )
    request["selected_cross_carrier_evidence_terminal_summary_basis"] = _reference_basis(
        "cross_carrier_evidence_terminal_summary",
        path="spec/PORTABLE_SOURCE_BODY_VERIFICATION_CROSS_CARRIER_EVIDENCE_TERMINAL_SUMMARY_V0.md",
    )
    request["selected_second_carrier_external_result_basis"] = _reference_basis(
        "second_carrier_external_result",
        outcome=SECOND_CARRIER_EXTERNAL_RESULT_RECORDED,
        failed_check_count=0,
    )
    request["selected_second_carrier_external_result_terminal_summary_basis"] = _reference_basis(
        "second_carrier_external_result_terminal_summary",
        path="spec/PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT_TERMINAL_SUMMARY_V0.md",
    )
    request["selected_second_carrier_verification_basis"] = _reference_basis(
        "second_carrier_verification",
        outcome=SECOND_CARRIER_VERIFICATION_RECORDED,
    )
    request["selected_second_carrier_success_basis"] = _reference_basis(
        "second_carrier_success",
        outcome=SECOND_CARRIER_SUCCESS_RECORDED,
    )
    request["selected_second_carrier_result_basis"] = _reference_basis(
        "second_carrier_result",
        outcome=SECOND_CARRIER_RESULT_RECORDED,
    )
    request["selected_returned_second_carrier_live_capture_intake_basis"] = _reference_basis(
        "returned_second_carrier_live_capture_intake",
        path=request["selected_returned_capture_intake_path"],
        preserved=True,
    )
    request["selected_returned_capture_material_basis"] = _reference_basis(
        "returned_capture_material",
        zip_path=request["selected_returned_capture_zip_path"],
        hash_path=request["selected_returned_capture_hash_path"],
        extracted_directory_path=request["selected_returned_capture_extracted_directory_path"],
        combined_terminal_log_path=request["selected_returned_capture_combined_terminal_log_path"],
        stdout_path=request["selected_returned_capture_stdout_path"],
        stderr_path=request["selected_returned_capture_stderr_path"],
        command_text=request["selected_returned_capture_command_text"],
        working_directory=request["selected_returned_capture_working_directory"],
        started_at=request["selected_returned_capture_started_at"],
        completed_at=request["selected_returned_capture_completed_at"],
        exit_code=request["selected_returned_capture_exit_code"],
        declared_exit_code=request["selected_returned_capture_declared_exit_code"],
        ran_7_tests_line=request["selected_returned_capture_ran_7_tests_line"],
        ok_line=request["selected_returned_capture_ok_line"],
        placeholder_fields_unrepaired=True,
    )
    request["selected_second_carrier_output_capture_basis"] = _reference_basis(
        "second_carrier_output_capture",
        outcome=SECOND_CARRIER_OUTPUT_CAPTURE_RECORDED,
        failed_check_count=0,
    )
    for key in (
        "selected_packet_transfer_basis",
        "selected_packet_emission_basis",
        "selected_command_success_basis",
        "selected_command_result_v2_basis",
        "selected_output_capture_v2_basis",
        "selected_command_output_report_artifact_basis",
        "selected_command_execution_basis",
        "selected_command_report_lineage_basis",
        "selected_evidence_manifest_basis",
        "selected_artifact_containment_basis",
        "selected_portable_verification_basis",
    ):
        request[key] = _reference_basis(key.replace("selected_", "").replace("_basis", ""))
    request["selected_predecessor_failure_basis"] = _reference_basis(
        "predecessor_failure",
        predecessor_cross_carrier_evidence_failure_preserved=True,
        predecessor_external_result_v1_failure_preserved=True,
        first_success_boundary_test_failure_preserved=True,
        first_result_boundary_resolver_failure_preserved=True,
        v1_packet_emission_predecessor_failure_preserved=True,
        repaired=False,
        hidden=False,
        claimed_passed=False,
    )
    for key in POSTURE_KEYS:
        request[key] = _posture_value(key)

    if overrides:
        request.update(copy.deepcopy(overrides))
    return request
