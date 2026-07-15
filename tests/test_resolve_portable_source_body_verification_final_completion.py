"""Tests for the bounded portable source-body verification final-completion resolver.

This suite exercises final-completion posture only. It preserves the membrane
between final completion and source transfer, source receipt, reception
authorization, source, authority, currentness, runtime, deployment, public
release, operation permission, continuation, reusable permission, adoption,
receiving-context governance, publication flow, and follow-on work.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Callable, Mapping
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_portable_source_body_verification_final_completion as resolver  # noqa: E402


TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_final_completion_metadata",
    "declared_final_completion_question",
    "selected_final_completion_boundary_basis",
    "selected_final_completion_boundary_terminal_summary_basis",
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
    "final_completion_spec_only_posture",
    "one_bounded_final_completion_posture",
    "final_completion_boundary_basis_preserved_posture",
    "portable_verification_closure_basis_preserved_posture",
    "portable_verification_closure_artifact_basis_preserved_posture",
    "cross_carrier_evidence_basis_preserved_posture",
    "returned_second_carrier_capture_basis_preserved_posture",
    "capture_intake_basis_preserved_posture",
    "second_carrier_output_capture_basis_preserved_posture",
    "final_completion_recorded_bounded_posture",
    "final_completion_artifact_recorded_or_bounded_posture",
    "final_completion_not_source_transfer_posture",
    "final_completion_not_source_receipt_posture",
    "final_completion_not_reception_authorization_posture",
    "final_completion_not_source_posture",
    "final_completion_not_authority_posture",
    "final_completion_not_currentness_posture",
    "final_completion_not_runtime_posture",
    "final_completion_not_deployment_posture",
    "final_completion_not_public_release_posture",
    "final_completion_not_operation_permission_posture",
    "zero_exit_code_not_final_completion_as_standalone_inference_posture",
    "string_zero_not_final_completion_as_standalone_inference_posture",
    "ok_output_not_final_completion_as_standalone_inference_posture",
    "ran_7_tests_not_final_completion_as_standalone_inference_posture",
    "returned_capture_not_final_completion_as_standalone_inference_posture",
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
    "final_completion_scope",
    "final_completion_checks",
    "final_completion_statement",
    "final_completion_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_final_completion_summary",
)

SELECTED_BASIS_FIELDS = (
    "selected_final_completion_boundary_basis",
    "selected_final_completion_boundary_terminal_summary_basis",
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

POSTURE_FIELDS = (
    "final_completion_spec_only_posture",
    "one_bounded_final_completion_posture",
    "final_completion_boundary_basis_preserved_posture",
    "portable_verification_closure_basis_preserved_posture",
    "portable_verification_closure_artifact_basis_preserved_posture",
    "cross_carrier_evidence_basis_preserved_posture",
    "returned_second_carrier_capture_basis_preserved_posture",
    "capture_intake_basis_preserved_posture",
    "second_carrier_output_capture_basis_preserved_posture",
    "final_completion_recorded_bounded_posture",
    "final_completion_artifact_recorded_or_bounded_posture",
    "final_completion_not_source_transfer_posture",
    "final_completion_not_source_receipt_posture",
    "final_completion_not_reception_authorization_posture",
    "final_completion_not_source_posture",
    "final_completion_not_authority_posture",
    "final_completion_not_currentness_posture",
    "final_completion_not_runtime_posture",
    "final_completion_not_deployment_posture",
    "final_completion_not_public_release_posture",
    "final_completion_not_operation_permission_posture",
    "zero_exit_code_not_final_completion_as_standalone_inference_posture",
    "string_zero_not_final_completion_as_standalone_inference_posture",
    "ok_output_not_final_completion_as_standalone_inference_posture",
    "ran_7_tests_not_final_completion_as_standalone_inference_posture",
    "returned_capture_not_final_completion_as_standalone_inference_posture",
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

OFFICIAL_SCOPE_VALUES = (
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "RETURNED_RESULT_CONTAINMENT_PRESERVED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "PREDECESSOR_CROSS_CARRIER_EVIDENCE_FAILURE_PRESERVED",
    "PREDECESSOR_EXTERNAL_RESULT_V1_FAILURE_PRESERVED",
    "FIRST_SUCCESS_BOUNDARY_TEST_FAILURE_PRESERVED",
    "FIRST_RESULT_BOUNDARY_RESOLVER_FAILURE_PRESERVED",
    "STRING_ZERO_NOT_FINAL_COMPLETION_AS_STANDALONE_INFERENCE",
    "FINAL_COMPLETION_NOT_SOURCE_TRANSFER",
    "FINAL_COMPLETION_NOT_SOURCE",
    "FINAL_COMPLETION_NOT_AUTHORITY",
    "FINAL_COMPLETION_NOT_CURRENTNESS",
)

REPRESENTATIVE_BLOCK_CODES = (
    "FINAL_COMPLETION_QUESTION_UNDECLARED",
    "FINAL_COMPLETION_INTENT_UNSUPPORTED",
    "FINAL_COMPLETION_BOUNDARY_BASIS_MISSING",
    "FINAL_COMPLETION_BOUNDARY_NOT_RECORDED",
    "FINAL_COMPLETION_BOUNDARY_FAILED_CHECKS_PRESENT",
    "FINAL_COMPLETION_BOUNDARY_VERSION_NOT_0_1_0",
    "FINAL_COMPLETION_BOUNDARY_DID_NOT_DECLARE_FUTURE_FINAL_COMPLETION_REVIEW_STEP",
    "FINAL_COMPLETION_BOUNDARY_ALREADY_CREATED_FINAL_COMPLETION",
    "FINAL_COMPLETION_BOUNDARY_TREATED_BOUNDARY_AS_FINAL_COMPLETION",
    "FINAL_COMPLETION_BOUNDARY_TREATED_ZERO_EXIT_CODE_AS_FINAL_COMPLETION",
    "FINAL_COMPLETION_BOUNDARY_TREATED_STRING_ZERO_AS_FINAL_COMPLETION",
    "FINAL_COMPLETION_BOUNDARY_TREATED_STRING_ZERO_AS_DOCTRINE",
    "FINAL_COMPLETION_BOUNDARY_TREATED_OK_AS_FINAL_COMPLETION",
    "FINAL_COMPLETION_BOUNDARY_TREATED_RAN_7_TESTS_AS_FINAL_COMPLETION",
    "FINAL_COMPLETION_BOUNDARY_TREATED_RETURNED_CAPTURE_AS_FINAL_COMPLETION",
    "FINAL_COMPLETION_BOUNDARY_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
    "PREDECESSOR_CROSS_CARRIER_EVIDENCE_FAILURE_MISSING_OR_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
    "PREDECESSOR_EXTERNAL_RESULT_V1_FAILURE_MISSING_OR_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
    "PORTABLE_VERIFICATION_CLOSURE_BASIS_MISSING",
    "PORTABLE_VERIFICATION_CLOSURE_NOT_RECORDED",
    "PORTABLE_VERIFICATION_CLOSURE_FAILED_CHECKS_PRESENT",
    "PORTABLE_VERIFICATION_CLOSURE_ALREADY_CREATED_FINAL_COMPLETION",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_FINAL_COMPLETION",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_SOURCE",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_AUTHORITY",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_CURRENTNESS",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_RUNTIME",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_DEPLOYMENT",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_PUBLIC_RELEASE",
    "PORTABLE_VERIFICATION_CLOSURE_TREATED_AS_OPERATION_PERMISSION",
    "CROSS_CARRIER_EVIDENCE_BASIS_MISSING",
    "CROSS_CARRIER_EVIDENCE_NOT_RECORDED",
    "SECOND_CARRIER_EXTERNAL_RESULT_BASIS_MISSING",
    "SECOND_CARRIER_EXTERNAL_RESULT_NOT_RECORDED",
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
    "FINAL_COMPLETION_TREATED_AS_SOURCE_TRANSFER",
    "FINAL_COMPLETION_TREATED_AS_SOURCE_RECEIPT",
    "FINAL_COMPLETION_TREATED_AS_RECEPTION_AUTHORIZATION",
    "FINAL_COMPLETION_TREATED_AS_SOURCE",
    "FINAL_COMPLETION_TREATED_AS_AUTHORITY",
    "FINAL_COMPLETION_TREATED_AS_CURRENTNESS",
    "FINAL_COMPLETION_TREATED_AS_RUNTIME",
    "FINAL_COMPLETION_TREATED_AS_DEPLOYMENT",
    "FINAL_COMPLETION_TREATED_AS_PUBLIC_RELEASE",
    "FINAL_COMPLETION_TREATED_AS_OPERATION_PERMISSION",
    "FINAL_COMPLETION_TREATED_AS_CONTINUATION",
    "FINAL_COMPLETION_TREATED_AS_REUSABLE_PERMISSION",
    "FINAL_COMPLETION_TREATED_AS_FOLLOW_ON_WORK",
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
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_FINAL_COMPLETION",
    "ARTIFACTS_MUTATED",
    "RETURNED_CAPTURE_MATERIAL_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_FINAL_COMPLETION_SCOPE",
)

EXPECTED_TRUE_STATEMENT_FIELDS = (
    "final_completion_recorded",
    "bounded_final_completion_recorded",
    "final_completion_artifact_recorded_or_bounded",
    "final_completion_boundary_basis_preserved",
    "portable_verification_closure_basis_preserved",
    "portable_verification_closure_artifact_basis_preserved",
    "cross_carrier_evidence_basis_preserved",
    "returned_second_carrier_capture_basis_preserved",
    "capture_intake_basis_preserved",
    "second_carrier_output_capture_basis_preserved",
    "final_completion_recorded_bounded",
    "final_completion_not_source_transfer",
    "final_completion_not_source_receipt",
    "final_completion_not_reception_authorization",
    "final_completion_not_source",
    "final_completion_not_authority",
    "final_completion_not_currentness",
    "final_completion_not_runtime",
    "final_completion_not_deployment",
    "final_completion_not_public_release",
    "final_completion_not_operation_permission",
    "zero_exit_code_not_final_completion_as_standalone_inference",
    "string_zero_not_final_completion_as_standalone_inference",
    "ok_output_not_final_completion_as_standalone_inference",
    "ran_7_tests_not_final_completion_as_standalone_inference",
    "returned_capture_not_final_completion_as_standalone_inference",
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

EXPECTED_FALSE_NON_CLAIMS = (
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "final_completion_treated_as_source_transfer",
    "final_completion_treated_as_source_receipt",
    "final_completion_treated_as_reception_authorization",
    "final_completion_treated_as_source",
    "final_completion_treated_as_authority",
    "final_completion_treated_as_currentness",
    "final_completion_treated_as_runtime",
    "final_completion_treated_as_deployment",
    "final_completion_treated_as_public_release",
    "final_completion_treated_as_operation_permission",
    "final_completion_treated_as_continuation",
    "final_completion_treated_as_reusable_permission",
    "final_completion_treated_as_follow_on_work",
    "zero_exit_code_treated_as_final_completion_standalone",
    "string_zero_treated_as_final_completion_standalone",
    "string_zero_representation_turned_into_doctrine",
    "ok_output_treated_as_final_completion_standalone",
    "ran_7_tests_treated_as_final_completion_standalone",
    "returned_capture_treated_as_final_completion_standalone",
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

SENSITIVE_KEYS = (
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
)

HOSTILE_SENTINELS = (
    "RAW_FINAL_COMPLETION_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)


def build_request(**overrides: Any) -> dict[str, Any]:
    request = resolver.build_declared_portable_source_body_verification_final_completion_request()
    request.update(overrides)
    return request


def resolve(request: Mapping[str, Any] | None) -> dict[str, Any]:
    return resolver.resolve_portable_source_body_verification_final_completion(request)


def block_from_request(mutator: Callable[[dict[str, Any]], None]) -> dict[str, Any]:
    request = build_request()
    mutator(request)
    return resolve(request)


def set_non_claim(request: dict[str, Any], key: str, value: bool = True) -> None:
    request.setdefault("declared_non_claims", {})[key] = value


def set_posture_value(request: dict[str, Any], key: str, value: bool = False) -> None:
    request[key] = {"declared": value, "value": value}


class PortableSourceBodyVerificationFinalCompletionTests(unittest.TestCase):
    def assert_public_codes(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if isinstance(block, Mapping) and block.get("block_code") is not None:
            self.assertIn(block["block_code"], resolver.BLOCK_CODES)
        for check in result.get("final_completion_checks", ()):
            code = check.get("block_code") or check.get("failure_code")
            if code is not None:
                self.assertIn(code, resolver.BLOCK_CODES)

    def assert_generated_booleans_are_bool(self, result: Mapping[str, Any]) -> None:
        for section_name in ("final_completion_statement", "non_claims", "final_completion_non_meaning"):
            section = result.get(section_name, {})
            self.assertIsInstance(section, Mapping)
            for key, value in section.items():
                self.assertIsInstance(value, bool, f"{section_name}.{key} is not bool")

    def assert_no_raw_or_hidden_sentinels(
        self,
        result: Mapping[str, Any],
        extra_forbidden_values: tuple[str, ...] = (),
    ) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS + extra_forbidden_values:
            self.assertNotIn(sentinel, serialized)

    def assert_official_scope_preserved(self, result: Mapping[str, Any]) -> None:
        scope = result.get("final_completion_scope")
        self.assertIsInstance(scope, list)
        for value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(value, scope)
        self.assertNotIn("[bounded-final-completion-redacted]", scope)
        self.assertNotIn("[bounded-redacted-raw-or-hidden-state]", scope)
        for value in scope:
            self.assertNotEqual(value, "[bounded-final-completion-redacted]")
            self.assertNotEqual(value, "[bounded-redacted-raw-or-hidden-state]")

    def assert_no_escalated_posture_created(self, result: Mapping[str, Any]) -> None:
        non_claims = result["non_claims"]
        statement = result["final_completion_statement"]
        for key in (
            "source_created",
            "authority_created",
            "currentness_created",
            "runtime_hosting_created",
            "deployment_created",
            "public_release_created",
            "operation_permission_created",
            "follow_on_work_authorized",
            "source_transfer_occurred",
            "source_receipt_occurred",
            "reception_authorization_created",
            "consumed_request_reopened",
            "authorization_token_reused",
            "zero_exit_code_treated_as_final_completion_standalone",
            "string_zero_treated_as_final_completion_standalone",
            "string_zero_representation_turned_into_doctrine",
            "ok_output_treated_as_final_completion_standalone",
            "ran_7_tests_treated_as_final_completion_standalone",
            "returned_capture_treated_as_final_completion_standalone",
            "receiving_carrier_treated_as_authority",
            "artifact_existence_treated_as_final_completion_authority",
            "artifact_path_treated_as_currentness",
            "repo_local_availability_treated_as_final_completion_authority",
            "hidden_repo_state_used_as_final_completion_content",
            "hidden_repo_state_used_as_final_completion_authority",
        ):
            self.assertFalse(non_claims[key], key)
        self.assertTrue(statement["source_not_created"])
        self.assertTrue(statement["authority_not_created"])
        self.assertTrue(statement["currentness_not_created"])
        self.assertTrue(statement["runtime_not_created"])
        self.assertTrue(statement["deployment_not_created"])
        self.assertTrue(statement["public_release_not_created"])
        self.assertTrue(statement["operation_permission_not_created"])
        self.assertTrue(statement["follow_on_work_not_authorized"])
        self.assertTrue(statement["authorization_token_reuse_blocked"])
        self.assertTrue(statement["consumed_request_token_remains_closed"])

    def assert_safe_blocked_result(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        self.assertIsInstance(result["block"], Mapping)
        self.assertIn(result["block"]["block_code"], resolver.BLOCK_CODES)
        self.assert_public_codes(result)
        self.assert_generated_booleans_are_bool(result)
        self.assert_no_escalated_posture_created(result)
        non_claims = result["non_claims"]
        for key in (
            "predecessor_cross_carrier_evidence_repaired",
            "predecessor_cross_carrier_evidence_hidden",
            "predecessor_cross_carrier_evidence_claimed_passed",
            "predecessor_external_result_v1_repaired",
            "predecessor_external_result_v1_hidden",
            "predecessor_external_result_v1_claimed_passed",
            "first_success_boundary_test_repaired",
            "first_success_boundary_test_hidden",
            "first_success_boundary_test_claimed_passed",
            "v1_packet_emission_repaired",
            "v1_packet_emission_hidden",
            "v1_packet_emission_claimed_passed",
            "first_result_boundary_resolver_repaired",
            "first_result_boundary_resolver_hidden",
            "first_result_boundary_resolver_claimed_passed",
        ):
            self.assertFalse(non_claims[key], key)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_portable_source_body_verification_final_completion",
            "resolve_portable_source_body_verification_final_completion_from_path",
            "write_portable_source_body_verification_final_completion_result",
            "build_portable_source_body_verification_final_completion_summary",
            "build_declared_portable_source_body_verification_final_completion_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_SCOPE_VALUES",
            "SUPPORTED_FINAL_COMPLETION_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(resolver.RESOLVER_MODULE, "resolve_portable_source_body_verification_final_completion")
        self.assertEqual(resolver.SUPPORTED_FINAL_COMPLETION_SCOPE, resolver.SUPPORTED_SCOPE_VALUES)
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_final_completion"
            )
        )
        for value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(value, resolver.SUPPORTED_FINAL_COMPLETION_SCOPE)
        for code in REPRESENTATIVE_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_successful_recorded_result_from_no_argument_builder(self) -> None:
        request = build_request()
        result = resolve(request)
        summary = resolver.build_portable_source_body_verification_final_completion_summary(result)

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertIsNone(result["block"])
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["request_id"], request["final_completion_request_id"])
        self.assertEqual(
            result["portable_source_body_verification_final_completion_metadata"][
                "portable_source_body_verification_final_completion_version"
            ],
            "0.1.0",
        )

        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        for field in EXPECTED_TRUE_STATEMENT_FIELDS:
            self.assertIs(result["final_completion_statement"][field], True, field)
        for field in EXPECTED_FALSE_NON_CLAIMS:
            self.assertIs(result["non_claims"][field], False, field)

        self.assert_public_codes(result)
        self.assert_generated_booleans_are_bool(result)
        self.assert_official_scope_preserved(result)
        self.assert_no_raw_or_hidden_sentinels(result)
        self.assert_no_escalated_posture_created(result)

    def test_official_enum_strings_are_preserved_without_redaction_placeholders(self) -> None:
        result = resolve(build_request())
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assert_official_scope_preserved(result)
        for check in result["final_completion_checks"]:
            code = check.get("block_code") or check.get("failure_code")
            if code:
                self.assertIn(code, resolver.BLOCK_CODES)
                self.assertNotEqual(code, "[bounded-final-completion-redacted]")
                self.assertNotEqual(code, "[bounded-redacted-raw-or-hidden-state]")

        all_scope_request = build_request(final_completion_scope=list(resolver.SUPPORTED_FINAL_COMPLETION_SCOPE))
        all_scope_result = resolve(all_scope_request)
        self.assertEqual(all_scope_result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(
            set(all_scope_result["final_completion_scope"]),
            set(resolver.SUPPORTED_FINAL_COMPLETION_SCOPE),
        )
        self.assert_official_scope_preserved(all_scope_result)

    def test_raw_hidden_hostile_content_is_contained(self) -> None:
        request = build_request()
        hostile_values = tuple(f"hostile-value-{index}" for index, _ in enumerate(SENSITIVE_KEYS))
        for section in (
            "selected_final_completion_boundary_basis",
            "selected_final_completion_boundary_terminal_summary_basis",
            "selected_portable_verification_closure_basis",
            "selected_portable_verification_closure_terminal_summary_basis",
            "selected_cross_carrier_evidence_basis",
            "selected_cross_carrier_evidence_terminal_summary_basis",
            "selected_second_carrier_external_result_basis",
            "selected_second_carrier_external_result_terminal_summary_basis",
            "selected_second_carrier_success_basis",
            "selected_second_carrier_result_basis",
            "selected_returned_second_carrier_live_capture_intake_basis",
            "selected_returned_capture_material_basis",
            "selected_second_carrier_output_capture_basis",
            "selected_command_report_lineage_basis",
            "selected_artifact_containment_basis",
        ):
            request[section] = copy.deepcopy(request[section])
            for key, value in zip(SENSITIVE_KEYS, hostile_values):
                request[section][key] = value
            request[section]["nested"] = {
                "list": [
                    "safe-reference-shaped-item",
                    "RAW_FINAL_COMPLETION_BODY_MUST_NOT_RETURN",
                    {"inner": "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN"},
                    {"hidden": "HIDDEN_REPO_STATE_MUST_NOT_RETURN"},
                ]
            }

        before = copy.deepcopy(request)
        result = resolve(request)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assertEqual(request, before)
        self.assert_no_raw_or_hidden_sentinels(result, hostile_values)
        self.assert_official_scope_preserved(result)
        self.assert_public_codes(result)
        self.assert_generated_booleans_are_bool(result)
        self.assert_no_escalated_posture_created(result)

    def test_representative_blocking_behavior(self) -> None:
        special_cases: tuple[tuple[str, Callable[[], dict[str, Any]]], ...] = (
            ("missing request", lambda: resolve(None)),
            ("non-mapping request", lambda: resolver.resolve_portable_source_body_verification_final_completion([])),
        )
        for name, case in special_cases:
            with self.subTest(name=name):
                self.assert_safe_blocked_result(case())

        block_cases: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
            ("explicit block intent", lambda r: r.__setitem__("final_completion_intent", "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION")),
            ("unsupported intent", lambda r: r.__setitem__("final_completion_intent", "UNSUPPORTED")),
            ("missing question", lambda r: r.__setitem__("final_completion_question", "")),
            ("unsupported scope", lambda r: r.__setitem__("final_completion_scope", ["UNSUPPORTED_FINAL_COMPLETION_SCOPE_VALUE"])),
            ("missing final-completion boundary basis", lambda r: r.__delitem__("selected_final_completion_boundary_basis")),
            ("boundary not recorded", lambda r: r.__setitem__("selected_final_completion_boundary_result_outcome", "NOT_RECORDED")),
            ("boundary failed checks", lambda r: r.__setitem__("selected_final_completion_boundary_failed_check_count", 1)),
            ("boundary version mismatch", lambda r: r.__setitem__("selected_final_completion_boundary_result_version", "9.9.9")),
            ("boundary missing future step", lambda r: r.__setitem__("selected_final_completion_boundary_declared_future_final_completion_review_step", False)),
            ("boundary already created final completion", lambda r: r.__setitem__("selected_final_completion_boundary_already_created_final_completion", True)),
            ("boundary treated boundary as final completion", lambda r: r.__setitem__("selected_final_completion_boundary_treated_boundary_as_final_completion", True)),
            ("boundary treated zero as final completion", lambda r: r.__setitem__("selected_final_completion_boundary_zero_exit_code_not_final_completion", False)),
            ("boundary treated string zero as final completion", lambda r: r.__setitem__("selected_final_completion_boundary_string_zero_not_final_completion", False)),
            ("boundary string zero doctrine", lambda r: r.__setitem__("selected_final_completion_boundary_string_zero_turned_into_doctrine", True)),
            ("boundary treated OK as final completion", lambda r: r.__setitem__("selected_final_completion_boundary_ok_not_final_completion", False)),
            ("boundary treated Ran 7 as final completion", lambda r: r.__setitem__("selected_final_completion_boundary_ran_7_tests_not_final_completion", False)),
            ("boundary treated returned capture as final completion", lambda r: r.__setitem__("selected_final_completion_boundary_returned_capture_not_final_completion", False)),
            ("boundary redacted official strings", lambda r: r.__setitem__("selected_final_completion_boundary_official_enum_scope_strings_redacted", True)),
            ("cross-carrier predecessor missing", lambda r: r.__setitem__("predecessor_cross_carrier_evidence_failure_preserved", False)),
            ("external-result predecessor missing", lambda r: r.__setitem__("predecessor_external_result_v1_failure_preserved", False)),
            ("closure basis missing", lambda r: r.__delitem__("selected_portable_verification_closure_basis")),
            ("closure not recorded", lambda r: r.__setitem__("selected_portable_verification_closure_result_outcome", "NOT_RECORDED")),
            ("closure failed checks", lambda r: r.__setitem__("selected_portable_verification_closure_failed_check_count", 1)),
            ("closure already created final completion", lambda r: r.__setitem__("selected_portable_verification_closure_already_created_final_completion", True)),
            ("closure treated as final completion", lambda r: r.__setitem__("selected_portable_verification_closure_treated_as_final_completion", True)),
            ("closure treated as source", lambda r: r.__setitem__("selected_portable_verification_closure_treated_as_source", True)),
            ("closure treated as authority", lambda r: r.__setitem__("selected_portable_verification_closure_treated_as_authority", True)),
            ("closure treated as currentness", lambda r: r.__setitem__("selected_portable_verification_closure_treated_as_currentness", True)),
            ("closure treated as runtime", lambda r: r.__setitem__("selected_portable_verification_closure_treated_as_runtime", True)),
            ("closure treated as deployment", lambda r: r.__setitem__("selected_portable_verification_closure_treated_as_deployment", True)),
            ("closure treated as public release", lambda r: r.__setitem__("selected_portable_verification_closure_treated_as_public_release", True)),
            ("closure treated as operation permission", lambda r: r.__setitem__("selected_portable_verification_closure_treated_as_operation_permission", True)),
            ("closure treated as follow-on", lambda r: r.__setitem__("selected_portable_verification_closure_treated_as_follow_on_work", True)),
            ("cross-carrier basis missing", lambda r: r.__delitem__("selected_cross_carrier_evidence_basis")),
            ("cross-carrier not recorded", lambda r: r.__setitem__("selected_cross_carrier_evidence_result_outcome", "NOT_RECORDED")),
            ("external-result basis missing", lambda r: r.__delitem__("selected_second_carrier_external_result_basis")),
            ("external-result not recorded", lambda r: r.__setitem__("selected_second_carrier_external_result_result_outcome", "NOT_RECORDED")),
            ("verification basis missing", lambda r: r.__delitem__("selected_second_carrier_verification_basis")),
            ("verification not recorded", lambda r: r.__setitem__("selected_second_carrier_verification_result_outcome", "NOT_RECORDED")),
            ("success basis missing", lambda r: r.__delitem__("selected_second_carrier_success_basis")),
            ("success not recorded", lambda r: r.__setitem__("selected_second_carrier_success_result_outcome", "NOT_RECORDED")),
            ("result basis missing", lambda r: r.__delitem__("selected_second_carrier_result_basis")),
            ("result not recorded", lambda r: r.__setitem__("selected_second_carrier_result_result_outcome", "NOT_RECORDED")),
            ("capture intake missing", lambda r: r.__delitem__("selected_returned_second_carrier_live_capture_intake_basis")),
            ("capture intake not preserved", lambda r: r.__setitem__("selected_returned_capture_intake_preserved", False)),
            ("returned capture treated final completion", lambda r: set_non_claim(r, "returned_capture_treated_as_final_completion_standalone")),
            ("zero treated final completion", lambda r: set_non_claim(r, "zero_exit_code_treated_as_final_completion_standalone")),
            ("string zero treated final completion", lambda r: set_non_claim(r, "string_zero_treated_as_final_completion_standalone")),
            ("OK treated final completion", lambda r: set_non_claim(r, "ok_output_treated_as_final_completion_standalone")),
            ("Ran 7 treated final completion", lambda r: set_non_claim(r, "ran_7_tests_treated_as_final_completion_standalone")),
            ("placeholder fields repaired", lambda r: r.__setitem__("selected_returned_capture_placeholder_fields_unrepaired", False)),
            ("returned capture material missing", lambda r: r.__delitem__("selected_returned_capture_material_basis")),
            ("returned zip missing", lambda r: r.__setitem__("selected_returned_capture_zip_path", "")),
            ("returned hash missing", lambda r: r.__setitem__("selected_returned_capture_hash_path", "")),
            ("returned extracted missing", lambda r: r.__setitem__("selected_returned_capture_extracted_directory_path", "")),
            ("returned combined log missing", lambda r: r.__setitem__("selected_returned_capture_combined_terminal_log_path", "")),
            ("returned exit code missing", lambda r: r.__setitem__("selected_returned_capture_exit_code", None)),
            ("returned command missing", lambda r: r.__setitem__("selected_returned_capture_command_text", "")),
            ("returned timestamps missing", lambda r: r.__setitem__("selected_returned_capture_started_at", "")),
            ("output capture basis missing", lambda r: r.__delitem__("selected_second_carrier_output_capture_basis")),
            ("output capture not recorded", lambda r: r.__setitem__("selected_second_carrier_output_capture_result_outcome", "NOT_RECORDED")),
            ("output capture failed checks", lambda r: r.__setitem__("selected_second_carrier_output_capture_failed_check_count", 1)),
            ("final completion source transfer", lambda r: set_non_claim(r, "final_completion_treated_as_source_transfer")),
            ("final completion source receipt", lambda r: set_non_claim(r, "final_completion_treated_as_source_receipt")),
            ("final completion reception", lambda r: set_non_claim(r, "final_completion_treated_as_reception_authorization")),
            ("final completion source", lambda r: set_non_claim(r, "final_completion_treated_as_source")),
            ("final completion authority", lambda r: set_non_claim(r, "final_completion_treated_as_authority")),
            ("final completion currentness", lambda r: set_non_claim(r, "final_completion_treated_as_currentness")),
            ("final completion runtime", lambda r: set_non_claim(r, "final_completion_treated_as_runtime")),
            ("final completion deployment", lambda r: set_non_claim(r, "final_completion_treated_as_deployment")),
            ("final completion public release", lambda r: set_non_claim(r, "final_completion_treated_as_public_release")),
            ("final completion operation permission", lambda r: set_non_claim(r, "final_completion_treated_as_operation_permission")),
            ("final completion continuation", lambda r: set_non_claim(r, "final_completion_treated_as_continuation")),
            ("final completion reusable", lambda r: set_non_claim(r, "final_completion_treated_as_reusable_permission")),
            ("final completion follow-on", lambda r: set_non_claim(r, "final_completion_treated_as_follow_on_work")),
            ("source transfer occurred", lambda r: set_non_claim(r, "source_transfer_occurred")),
            ("source receipt occurred", lambda r: set_non_claim(r, "source_receipt_occurred")),
            ("reception authorization created", lambda r: set_non_claim(r, "reception_authorization_created")),
            ("source created", lambda r: set_non_claim(r, "source_created")),
            ("authority created", lambda r: set_non_claim(r, "authority_created")),
            ("currentness created", lambda r: set_non_claim(r, "currentness_created")),
            ("runtime created", lambda r: set_non_claim(r, "runtime_hosting_created")),
            ("deployment created", lambda r: set_non_claim(r, "deployment_created")),
            ("public release created", lambda r: set_non_claim(r, "public_release_created")),
            ("operation permission created", lambda r: set_non_claim(r, "operation_permission_created")),
            ("continuation authorized", lambda r: set_non_claim(r, "continuation_authorized")),
            ("reusable permission created", lambda r: set_non_claim(r, "reusable_permission_created")),
            ("derivative reception authorized", lambda r: set_non_claim(r, "derivative_reception_authorized")),
            ("vessel relation authorized", lambda r: set_non_claim(r, "vessel_relation_authorized")),
            ("another reception request authorized", lambda r: set_non_claim(r, "another_reception_request_authorized")),
            ("follow-on authorized", lambda r: set_non_claim(r, "follow_on_work_authorized")),
            ("receiving carrier authority", lambda r: set_non_claim(r, "receiving_carrier_treated_as_authority")),
            ("artifact existence authority", lambda r: set_non_claim(r, "artifact_existence_treated_as_final_completion_authority")),
            ("artifact path currentness", lambda r: set_non_claim(r, "artifact_path_treated_as_currentness")),
            ("repo local authority", lambda r: set_non_claim(r, "repo_local_availability_treated_as_final_completion_authority")),
            ("hidden state content", lambda r: set_non_claim(r, "hidden_repo_state_used_as_final_completion_content")),
            ("hidden state authority", lambda r: set_non_claim(r, "hidden_repo_state_used_as_final_completion_authority")),
            ("basis not reference shaped", lambda r: set_posture_value(r, "selected_basis_reference_shape_posture")),
            ("raw full prior returned", lambda r: set_non_claim(r, "raw_full_prior_artifact_body_returned")),
            ("predecessor repaired", lambda r: r["selected_predecessor_failure_basis"].__setitem__("predecessor_cross_carrier_evidence_repaired", True)),
            ("first success hidden", lambda r: set_non_claim(r, "first_success_boundary_test_hidden")),
            ("v1 packet emission repaired", lambda r: set_non_claim(r, "v1_packet_emission_repaired")),
            ("first result claimed passed", lambda r: set_non_claim(r, "first_result_boundary_resolver_claimed_passed")),
            ("command lineage current report", lambda r: r.__setitem__("final_completion_scope", ["COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENT_REPORT_ARTIFACT"])),
            ("command lineage source", lambda r: r.__setitem__("final_completion_scope", ["COMMAND_REPORT_LINEAGE_TREATED_AS_SOURCE"])),
            ("command lineage authority", lambda r: r.__setitem__("final_completion_scope", ["COMMAND_REPORT_LINEAGE_TREATED_AS_AUTHORITY"])),
            ("command lineage currentness", lambda r: r.__setitem__("final_completion_scope", ["COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENTNESS"])),
            ("consumed request reopened", lambda r: set_non_claim(r, "consumed_request_reopened")),
            ("authorization token reused", lambda r: set_non_claim(r, "authorization_token_reused")),
            ("full prior body emitted", lambda r: set_posture_value(r, "raw_full_prior_artifact_body_not_returned_posture")),
            ("string zero doctrine", lambda r: set_non_claim(r, "string_zero_representation_turned_into_doctrine")),
            ("artifacts mutated", lambda r: set_non_claim(r, "prior_artifacts_mutated")),
            ("returned capture mutated", lambda r: set_non_claim(r, "returned_capture_material_mutated")),
            ("required non-claim missing", lambda r: r["declared_non_claims"].__delitem__("source_created")),
        )

        for name, mutator in block_cases:
            with self.subTest(name=name):
                self.assert_safe_blocked_result(block_from_request(mutator))

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            request = build_request()
            request_path = root / "request.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")

            result = resolver.resolve_portable_source_body_verification_final_completion_from_path(request_path)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(
                result["portable_source_body_verification_final_completion_metadata"][
                    "portable_source_body_verification_final_completion_version"
                ],
                "0.1.0",
            )
            self.assertEqual(
                result["portable_source_body_verification_final_completion_metadata"]["resolver_module"],
                resolver.RESOLVER_MODULE,
            )

            malformed_path = root / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            self.assert_safe_blocked_result(
                resolver.resolve_portable_source_body_verification_final_completion_from_path(malformed_path)
            )

            array_path = root / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            self.assert_safe_blocked_result(
                resolver.resolve_portable_source_body_verification_final_completion_from_path(array_path)
            )
            self.assert_safe_blocked_result(
                resolver.resolve_portable_source_body_verification_final_completion_from_path(root / "missing.json")
            )

            output_root = (
                root
                / "artifacts"
                / "integrity_host_v0_min_coexistence_portable_source_body_verification_final_completion"
            )
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_portable_source_body_verification_final_completion_result(result)
                second_path = resolver.write_portable_source_body_verification_final_completion_result(result)

            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertEqual(json.loads(first_path.read_text(encoding="utf-8"))["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(json.loads(second_path.read_text(encoding="utf-8"))["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(first_path.parent, output_root)
            self.assertEqual(second_path.parent, output_root)
            for forbidden in (
                "actual_second_carrier_live_capture",
                "final_completion_boundary",
                "portable_verification_closure",
                "cross_carrier_evidence",
                "second_carrier_external_result",
                "runtime",
                "deployment",
                "public_release",
                "source_transfer",
                "source_receipt",
                "reception",
            ):
                self.assertNotIn(forbidden, str(first_path.relative_to(root)))

    def test_resolver_does_not_mutate_declared_request(self) -> None:
        request = build_request()
        for field in SELECTED_BASIS_FIELDS + POSTURE_FIELDS + ("final_completion_scope", "declared_non_claims"):
            self.assertIn(field, request)
        before = copy.deepcopy(request)
        result = resolve(request)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(request, before)
        for field in SELECTED_BASIS_FIELDS + POSTURE_FIELDS:
            self.assertEqual(request[field], before[field], field)
        self.assertEqual(request["final_completion_scope"], before["final_completion_scope"])
        self.assertEqual(request["declared_non_claims"], before["declared_non_claims"])

    def test_predecessor_failure_preservation(self) -> None:
        result = resolve(build_request())
        summary = resolver.build_portable_source_body_verification_final_completion_summary(result)
        statement = result["final_completion_statement"]
        non_claims = result["non_claims"]

        self.assertTrue(statement["predecessor_cross_carrier_evidence_failure_preserved"])
        self.assertTrue(summary["predecessor_cross_carrier_evidence_failure_preserved"])
        self.assertFalse(non_claims["predecessor_cross_carrier_evidence_repaired"])
        self.assertFalse(non_claims["predecessor_cross_carrier_evidence_hidden"])
        self.assertFalse(non_claims["predecessor_cross_carrier_evidence_claimed_passed"])

        self.assertTrue(statement["predecessor_external_result_v1_failure_preserved"])
        self.assertTrue(summary["predecessor_external_result_v1_failure_preserved"])
        self.assertFalse(non_claims["predecessor_external_result_v1_repaired"])
        self.assertFalse(non_claims["predecessor_external_result_v1_hidden"])
        self.assertFalse(non_claims["predecessor_external_result_v1_claimed_passed"])

        self.assertTrue(statement["first_success_boundary_test_failure_preserved"])
        self.assertTrue(summary["first_success_boundary_test_preserved_as_failed_predecessor"])
        self.assertFalse(non_claims["first_success_boundary_test_repaired"])
        self.assertFalse(non_claims["first_success_boundary_test_hidden"])
        self.assertFalse(non_claims["first_success_boundary_test_claimed_passed"])

        self.assertTrue(summary["v1_packet_emission_predecessor_failure_preserved"])
        self.assertFalse(non_claims["v1_packet_emission_repaired"])
        self.assertFalse(non_claims["v1_packet_emission_hidden"])
        self.assertFalse(non_claims["v1_packet_emission_claimed_passed"])

        self.assertTrue(statement["first_result_boundary_resolver_failure_preserved"])
        self.assertTrue(summary["first_result_boundary_resolver_preserved_as_failed_predecessor"])
        self.assertFalse(non_claims["first_result_boundary_resolver_repaired"])
        self.assertFalse(non_claims["first_result_boundary_resolver_hidden"])
        self.assertFalse(non_claims["first_result_boundary_resolver_claimed_passed"])


if __name__ == "__main__":
    unittest.main()
