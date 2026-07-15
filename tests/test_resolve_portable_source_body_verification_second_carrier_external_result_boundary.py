"""Executable checks for second-carrier external-result boundary posture only.

This suite is downstream of the bounded second-carrier verification line. It
verifies that the resolver records one future second-carrier external-result
step only while preserving that external result, cross-carrier evidence,
portable verification closure, source transfer, source receipt, reception
authorization, source, authority, currentness, runtime, final completion,
continuation, reusable permission, and follow-on work are not created.

The tests use only synthetic bounded basis objects and temporary paths. They do
not mutate returned capture material, standing artifacts, predecessor failure
surfaces, or any file outside this new test surface.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Callable
from unittest.mock import patch


sys.dont_write_bytecode = True

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_portable_source_body_verification_second_carrier_external_result_boundary as resolver


RECORDED = resolver.OUTCOME_RECORDED
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = set(resolver.OUTCOME_FAMILY)
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
TRUE_RECORDED_FIELDS = tuple(resolver.ALLOWED_TRUE_RECORDED_FIELDS)
SELECTED_BASIS_KEYS = tuple(resolver.SELECTED_BASIS_KEYS)
POSTURE_KEYS = tuple(resolver.POSTURE_KEYS)

RAW_SENTINELS = (
    "RAW_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)
HOSTILE_VALUES = (
    "hostile-raw-body-value",
    "hostile-raw-full-body-value",
    "hostile-full-body-value",
    "hostile-artifact-body-value",
    "hostile-raw-result-body-value",
    "hostile-raw-output-body-value",
    "hostile-raw-capture-body-value",
    "hostile-raw-success-body-value",
    "hostile-raw-verification-body-value",
    "hostile-raw-external-result-body-value",
    "hostile-capture-body-value",
    "hostile-second-carrier-external-result-body-value",
    "hostile-cross-carrier-evidence-body-value",
    "hostile-portable-verification-closure-body-value",
    "hostile-source-body-value",
    "hostile-authority-body-value",
    "hostile-current-working-tree-value",
    "hostile-local-cache-value",
    "hostile-repo-local-only-dependency-value",
)
REDACTION_PLACEHOLDERS = {
    "[bounded-external-result-boundary-redacted]",
    "[bounded-redacted-raw-or-hidden-state]",
}
OFFICIAL_SCOPE_VALUES = (
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "RETURNED_RESULT_CONTAINMENT_PRESERVED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "FIRST_SUCCESS_BOUNDARY_TEST_FAILURE_PRESERVED",
    "FIRST_RESULT_BOUNDARY_RESOLVER_FAILURE_PRESERVED",
    "STRING_ZERO_NOT_EXTERNAL_RESULT",
    "EXTERNAL_RESULT_NOT_CREATED",
    "EXTERNAL_RESULT_BOUNDARY_NOT_EXTERNAL_RESULT",
)

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_second_carrier_external_result_boundary_metadata",
    "declared_second_carrier_external_result_boundary_question",
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
    "second_carrier_external_result_boundary_scope",
    "second_carrier_external_result_boundary_checks",
    "second_carrier_external_result_boundary_statement",
    "second_carrier_external_result_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_second_carrier_external_result_boundary_summary",
)

REPRESENTATIVE_BLOCK_CODES = (
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_QUESTION_UNDECLARED",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_INTENT_UNSUPPORTED",
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
    "SECOND_CARRIER_RESULT_BASIS_MISSING",
    "SECOND_CARRIER_RESULT_NOT_RECORDED",
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
    "PUBLIC_RELEASE_CREATED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "RECEIVING_CARRIER_TREATED_AS_AUTHORITY",
    "ARTIFACT_EXISTENCE_TREATED_AS_EXTERNAL_RESULT_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_EXTERNAL_RESULT_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_EXTERNAL_RESULT_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_EXTERNAL_RESULT_AUTHORITY",
    "FIRST_SUCCESS_BOUNDARY_TEST_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    "FIRST_RESULT_BOUNDARY_RESOLVER_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_EXTERNAL_RESULT_BOUNDARY",
    "STRING_ZERO_REPRESENTATION_TURNED_INTO_DOCTRINE",
    "ARTIFACTS_MUTATED",
    "RETURNED_CAPTURE_MATERIAL_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_SCOPE",
)

CRITICAL_FALSE_NON_CLAIMS = (
    "external_result_created",
    "cross_carrier_evidence_created",
    "portable_verification_closure_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "second_carrier_external_result_boundary_treated_as_external_result",
    "second_carrier_external_result_boundary_treated_as_cross_carrier_evidence",
    "second_carrier_external_result_boundary_treated_as_portable_verification_closure",
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


def build_request() -> dict[str, Any]:
    return (
        resolver.build_declared_portable_source_body_verification_second_carrier_external_result_boundary_request()
    )


def mutate_request(mutator: Callable[[dict[str, Any]], None]) -> dict[str, Any]:
    request = build_request()
    mutator(request)
    return request


def serialized(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=False)


def flip_non_claim(request: dict[str, Any], key: str) -> None:
    request["declared_non_claims"][key] = True


def drop_non_claim(request: dict[str, Any], key: str) -> None:
    request["declared_non_claims"].pop(key, None)


def set_field(request: dict[str, Any], key: str, value: Any) -> None:
    request[key] = value


def pop_field(request: dict[str, Any], key: str) -> None:
    request.pop(key, None)


class PortableSourceBodyVerificationSecondCarrierExternalResultBoundaryTests(
    unittest.TestCase
):
    def assert_public_codes(self, result: dict[str, Any]) -> None:
        codes = set(resolver.BLOCK_CODES)
        block = result.get("block")
        if isinstance(block, dict) and block.get("block_code") is not None:
            self.assertIn(block["block_code"], codes)
        for check in result.get("second_carrier_external_result_boundary_checks", []):
            if not isinstance(check, dict):
                continue
            for code_key in ("block_code", "failure_code"):
                code = check.get(code_key)
                if code is not None:
                    self.assertIn(code, codes)

    def assert_generated_booleans_are_bool(self, result: dict[str, Any]) -> None:
        for section_name in (
            "second_carrier_external_result_boundary_statement",
            "second_carrier_external_result_boundary_non_meaning",
            "non_claims",
        ):
            section = result[section_name]
            self.assertIsInstance(section, dict)
            for key, value in section.items():
                self.assertIs(type(value), bool, f"{section_name}.{key}")
        for check in result["second_carrier_external_result_boundary_checks"]:
            self.assertIs(type(check["passed"]), bool, check["check_name"])

    def assert_no_raw_or_hidden_sentinels(self, result: dict[str, Any]) -> None:
        body = serialized(result)
        for sentinel in RAW_SENTINELS:
            self.assertNotIn(sentinel, body)
        for hostile_value in HOSTILE_VALUES:
            self.assertNotIn(hostile_value, body)

    def assert_official_scope_preserved(self, result: dict[str, Any]) -> None:
        scope = result["second_carrier_external_result_boundary_scope"]
        self.assertIsInstance(scope, list)
        for value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(value, scope)
        for value in SUPPORTED_SCOPE:
            self.assertIn(value, scope)
        for placeholder in REDACTION_PLACEHOLDERS:
            self.assertNotIn(placeholder, scope)
        for value in scope:
            self.assertNotEqual(value, "[bounded-external-result-boundary-redacted]")
            self.assertNotEqual(value, "[bounded-redacted-raw-or-hidden-state]")
        for check in result["second_carrier_external_result_boundary_checks"]:
            self.assertNotIn(check.get("block_code"), REDACTION_PLACEHOLDERS)
            self.assertNotIn(check.get("failure_code"), REDACTION_PLACEHOLDERS)
        self.assert_public_codes(result)

    def assert_no_later_work_created(self, result: dict[str, Any]) -> None:
        non_claims = result["non_claims"]
        for key in CRITICAL_FALSE_NON_CLAIMS:
            self.assertIs(non_claims[key], False, key)
        statement = result["second_carrier_external_result_boundary_statement"]
        if result["outcome"] == RECORDED:
            self.assertIs(statement["external_result_not_created"], True)
            self.assertIs(statement["cross_carrier_evidence_not_created"], True)
            self.assertIs(statement["portable_verification_closure_not_created"], True)
            self.assertIs(statement["source_not_created"], True)
            self.assertIs(statement["authority_not_created"], True)
            self.assertIs(statement["currentness_not_created"], True)
            self.assertIs(statement["final_completion_not_created"], True)
            self.assertIs(statement["runtime_not_created"], True)
            self.assertIs(statement["follow_on_work_not_authorized"], True)

    def assert_blocked_result(self, result: dict[str, Any]) -> None:
        self.assertEqual(BLOCKED, result["outcome"])
        self.assertIsInstance(result.get("block"), dict)
        self.assertIn(result["block"].get("block_code"), resolver.BLOCK_CODES)
        self.assert_public_codes(result)
        self.assert_no_later_work_created(result)
        self.assert_generated_booleans_are_bool(result)

    def assert_path_failure_is_bounded(self, path: Path) -> None:
        try:
            result = (
                resolver.resolve_portable_source_body_verification_second_carrier_external_result_boundary_from_path(
                    path
                )
            )
        except resolver.PortableSourceBodyVerificationSecondCarrierExternalResultBoundaryError:
            return
        self.assert_blocked_result(result)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_portable_source_body_verification_second_carrier_external_result_boundary",
            "resolve_portable_source_body_verification_second_carrier_external_result_boundary_from_path",
            "write_portable_source_body_verification_second_carrier_external_result_boundary_result",
            "build_portable_source_body_verification_second_carrier_external_result_boundary_summary",
            "build_declared_portable_source_body_verification_second_carrier_external_result_boundary_request",
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
            "SUPPORTED_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)
        self.assertEqual("0.1.0", resolver.RESULT_VERSION)
        self.assertEqual(
            "resolve_portable_source_body_verification_second_carrier_external_result_boundary",
            resolver.RESOLVER_MODULE,
        )
        self.assertEqual(
            resolver.SUPPORTED_SCOPE_VALUES,
            resolver.SUPPORTED_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_SCOPE,
        )
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_portable_source_body_"
                "verification_second_carrier_external_result_boundary"
            )
        )
        for value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(value, SUPPORTED_SCOPE)
        for value in (
            "EXTERNAL_RESULT_NOT_CREATED",
            "EXTERNAL_RESULT_BOUNDARY_NOT_EXTERNAL_RESULT",
        ):
            self.assertIn(value, SUPPORTED_SCOPE)
        for code in REPRESENTATIVE_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES, code)

    def test_successful_recorded_result_from_no_argument_builder(self) -> None:
        request = build_request()
        result = (
            resolver.resolve_portable_source_body_verification_second_carrier_external_result_boundary(
                request
            )
        )
        summary = (
            resolver.build_portable_source_body_verification_second_carrier_external_result_boundary_summary(
                result
            )
        )

        self.assertIsInstance(result, dict)
        self.assertEqual(RECORDED, result["outcome"])
        self.assertIsNone(result["block"])
        self.assertEqual(0, summary["failed_check_count"])
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual("0.1.0", summary["result_version"])
        self.assertEqual(resolver.RESOLVER_MODULE, summary["resolver_module"])
        self.assertEqual(
            request["second_carrier_external_result_boundary_request_id"],
            summary["request_id"],
        )
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result, section)

        statement = result["second_carrier_external_result_boundary_statement"]
        for field in TRUE_RECORDED_FIELDS:
            self.assertIn(field, statement)
            self.assertIs(statement[field], True, field)

        non_claims = result["non_claims"]
        for field in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(field, non_claims)
            self.assertIs(non_claims[field], False, field)

        self.assertEqual(
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_VERIFICATION_RECORDED",
            summary["selected_second_carrier_verification_outcome"],
        )
        self.assertEqual("0.1.0", summary["selected_second_carrier_verification_result_version"])
        self.assertEqual(0, summary["selected_second_carrier_verification_failed_check_count"])
        self.assertEqual(
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_VERIFICATION_BOUNDARY_RECORDED",
            summary["selected_second_carrier_verification_boundary_outcome"],
        )
        self.assertEqual(
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_SUCCESS_RECORDED",
            summary["selected_second_carrier_success_outcome"],
        )
        self.assertEqual("0", str(summary["selected_returned_capture_exit_code"]))
        self.assertEqual("OK", summary["selected_returned_capture_ok_line"])
        self.assert_no_later_work_created(result)
        self.assert_generated_booleans_are_bool(result)
        self.assert_public_codes(result)
        self.assert_official_scope_preserved(result)
        self.assert_no_raw_or_hidden_sentinels(result)

    def test_official_enum_strings_are_preserved_without_redaction_placeholders(self) -> None:
        request = build_request()
        result = (
            resolver.resolve_portable_source_body_verification_second_carrier_external_result_boundary(
                request
            )
        )
        self.assert_official_scope_preserved(result)

        all_scope_request = build_request()
        all_scope_request["second_carrier_external_result_boundary_scope"] = list(
            resolver.SUPPORTED_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_SCOPE
        )
        all_scope_result = (
            resolver.resolve_portable_source_body_verification_second_carrier_external_result_boundary(
                all_scope_request
            )
        )
        self.assertEqual(RECORDED, all_scope_result["outcome"])
        self.assertEqual(
            list(resolver.SUPPORTED_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_SCOPE),
            all_scope_result["second_carrier_external_result_boundary_scope"],
        )
        self.assert_official_scope_preserved(all_scope_result)

    def test_raw_hidden_hostile_content_is_contained_without_mutating_request(self) -> None:
        request = build_request()
        hostile_payload = {
            "raw_body": HOSTILE_VALUES[0],
            "raw_full_body": HOSTILE_VALUES[1],
            "full_body": HOSTILE_VALUES[2],
            "artifact_body": HOSTILE_VALUES[3],
            "raw_result_body": HOSTILE_VALUES[4],
            "raw_output_body": HOSTILE_VALUES[5],
            "raw_capture_body": HOSTILE_VALUES[6],
            "raw_success_body": HOSTILE_VALUES[7],
            "raw_verification_body": HOSTILE_VALUES[8],
            "raw_external_result_body": HOSTILE_VALUES[9],
            "capture_body": HOSTILE_VALUES[10],
            "second_carrier_external_result_body": HOSTILE_VALUES[11],
            "cross_carrier_evidence_body": HOSTILE_VALUES[12],
            "portable_verification_closure_body": HOSTILE_VALUES[13],
            "source_body": HOSTILE_VALUES[14],
            "authority_body": HOSTILE_VALUES[15],
            "hidden_repo_state": RAW_SENTINELS[2],
            "current_working_tree": HOSTILE_VALUES[16],
            "local_cache": HOSTILE_VALUES[17],
            "repo_local_only_dependency": HOSTILE_VALUES[18],
            "nested": [
                {"raw_body": RAW_SENTINELS[0]},
                {"full_body": RAW_SENTINELS[1]},
                {"value": RAW_SENTINELS[2]},
            ],
        }
        for field_name in (
            "selected_second_carrier_verification_basis",
            "selected_second_carrier_verification_terminal_summary_basis",
            "selected_second_carrier_verification_boundary_basis",
            "selected_second_carrier_verification_boundary_terminal_summary_basis",
            "selected_second_carrier_success_basis",
            "selected_second_carrier_result_basis",
            "selected_returned_second_carrier_live_capture_intake_basis",
            "selected_returned_capture_material_basis",
            "selected_second_carrier_output_capture_basis",
            "selected_command_report_lineage_basis",
            "selected_artifact_containment_basis",
        ):
            request[field_name]["hostile_payload"] = copy.deepcopy(hostile_payload)
        before = copy.deepcopy(request)

        result = (
            resolver.resolve_portable_source_body_verification_second_carrier_external_result_boundary(
                request
            )
        )

        self.assertEqual(before, request)
        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assert_no_raw_or_hidden_sentinels(result)
        self.assert_official_scope_preserved(result)
        self.assert_public_codes(result)
        self.assert_no_later_work_created(result)
        self.assert_generated_booleans_are_bool(result)
        non_claims = result["non_claims"]
        self.assertIs(non_claims["hidden_repo_state_used_as_external_result_content"], False)
        self.assertIs(non_claims["hidden_repo_state_used_as_external_result_authority"], False)
        self.assertIs(
            non_claims["repo_local_availability_treated_as_external_result_authority"],
            False,
        )
        self.assertIs(non_claims["receiving_carrier_treated_as_authority"], False)
        self.assertIs(
            non_claims["artifact_existence_treated_as_external_result_authority"],
            False,
        )
        self.assertIs(non_claims["artifact_path_treated_as_currentness"], False)
        self.assertIs(non_claims["string_zero_treated_as_external_result"], False)

    def test_representative_blocking_behavior(self) -> None:
        block_cases: tuple[tuple[str, Callable[[], Any]], ...] = (
            ("missing request mapping", lambda: {}),
            ("non-mapping request", lambda: ["not", "a", "mapping"]),
            (
                "explicit block intent",
                lambda: mutate_request(
                    lambda r: set_field(
                        r,
                        "second_carrier_external_result_boundary_intent",
                        "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY",
                    )
                ),
            ),
            (
                "unsupported intent",
                lambda: mutate_request(
                    lambda r: set_field(
                        r,
                        "second_carrier_external_result_boundary_intent",
                        "UNSUPPORTED_INTENT",
                    )
                ),
            ),
            (
                "unsupported scope",
                lambda: mutate_request(
                    lambda r: set_field(
                        r, "second_carrier_external_result_boundary_scope", ["UNSUPPORTED_SCOPE"]
                    )
                ),
            ),
            (
                "missing second-carrier verification basis",
                lambda: mutate_request(lambda r: pop_field(r, "selected_second_carrier_verification_basis")),
            ),
            (
                "second-carrier verification not recorded",
                lambda: mutate_request(
                    lambda r: set_field(
                        r, "selected_second_carrier_verification_result_outcome", "NOT_RECORDED"
                    )
                ),
            ),
            (
                "second-carrier verification failed checks",
                lambda: mutate_request(
                    lambda r: set_field(r, "selected_second_carrier_verification_failed_check_count", 1)
                ),
            ),
            (
                "second-carrier verification version wrong",
                lambda: mutate_request(
                    lambda r: set_field(r, "selected_second_carrier_verification_result_version", "9.9.9")
                ),
            ),
            (
                "second-carrier verification did not record bounded verification",
                lambda: mutate_request(
                    lambda r: set_field(
                        r, "selected_second_carrier_verification_bounded_verification_recorded", False
                    )
                ),
            ),
            (
                "second-carrier verification created external result",
                lambda: mutate_request(
                    lambda r: set_field(
                        r, "selected_second_carrier_verification_already_created_external_result", True
                    )
                ),
            ),
            (
                "second-carrier verification created cross-carrier evidence",
                lambda: mutate_request(
                    lambda r: set_field(
                        r,
                        "selected_second_carrier_verification_already_created_cross_carrier_evidence",
                        True,
                    )
                ),
            ),
            (
                "second-carrier verification created portable verification closure",
                lambda: mutate_request(
                    lambda r: set_field(
                        r,
                        "selected_second_carrier_verification_already_created_portable_verification_closure",
                        True,
                    )
                ),
            ),
            (
                "verification treated as external result",
                lambda: mutate_request(
                    lambda r: set_field(
                        r, "selected_second_carrier_verification_treated_verification_as_external_result", True
                    )
                ),
            ),
            (
                "verification treated as cross-carrier evidence",
                lambda: mutate_request(
                    lambda r: set_field(
                        r,
                        "selected_second_carrier_verification_treated_verification_as_cross_carrier_evidence",
                        True,
                    )
                ),
            ),
            (
                "verification treated as portable verification closure",
                lambda: mutate_request(
                    lambda r: set_field(
                        r,
                        "selected_second_carrier_verification_treated_verification_as_portable_verification_closure",
                        True,
                    )
                ),
            ),
            (
                "verification treated zero exit code as external result",
                lambda: mutate_request(
                    lambda r: set_field(
                        r, "selected_second_carrier_verification_zero_exit_code_not_external_result", False
                    )
                ),
            ),
            (
                "verification treated string zero as external result",
                lambda: mutate_request(
                    lambda r: set_field(
                        r, "selected_second_carrier_verification_string_zero_not_external_result", False
                    )
                ),
            ),
            (
                "verification treated OK as external result",
                lambda: mutate_request(
                    lambda r: set_field(r, "selected_second_carrier_verification_ok_not_external_result", False)
                ),
            ),
            (
                "verification treated Ran 7 tests as cross-carrier proof",
                lambda: mutate_request(
                    lambda r: set_field(
                        r,
                        "selected_second_carrier_verification_ran_7_tests_not_cross_carrier_proof",
                        False,
                    )
                ),
            ),
            (
                "verification treated returned capture as cross-carrier proof",
                lambda: mutate_request(
                    lambda r: set_field(
                        r,
                        "selected_second_carrier_verification_returned_capture_not_cross_carrier_proof",
                        False,
                    )
                ),
            ),
            (
                "verification redacted official enum strings",
                lambda: mutate_request(
                    lambda r: set_field(
                        r, "selected_second_carrier_verification_official_enum_scope_strings_redacted", True
                    )
                ),
            ),
            (
                "verification boundary basis missing",
                lambda: mutate_request(
                    lambda r: pop_field(r, "selected_second_carrier_verification_boundary_basis")
                ),
            ),
            (
                "success basis missing",
                lambda: mutate_request(lambda r: pop_field(r, "selected_second_carrier_success_basis")),
            ),
            (
                "success not recorded",
                lambda: mutate_request(
                    lambda r: set_field(r, "selected_second_carrier_success_result_outcome", "NOT_RECORDED")
                ),
            ),
            (
                "success failed checks",
                lambda: mutate_request(
                    lambda r: set_field(r, "selected_second_carrier_success_failed_check_count", 2)
                ),
            ),
            (
                "result basis missing",
                lambda: mutate_request(lambda r: pop_field(r, "selected_second_carrier_result_basis")),
            ),
            (
                "result not recorded",
                lambda: mutate_request(
                    lambda r: set_field(r, "selected_second_carrier_result_result_outcome", "NOT_RECORDED")
                ),
            ),
            (
                "result failed checks",
                lambda: mutate_request(
                    lambda r: set_field(r, "selected_second_carrier_result_failed_check_count", 1)
                ),
            ),
            (
                "returned capture intake basis missing",
                lambda: mutate_request(
                    lambda r: pop_field(r, "selected_returned_second_carrier_live_capture_intake_basis")
                ),
            ),
            (
                "returned capture intake not preserved",
                lambda: mutate_request(
                    lambda r: set_field(r, "selected_returned_capture_intake_preserved", False)
                ),
            ),
            (
                "returned capture treated as external result",
                lambda: mutate_request(
                    lambda r: set_field(r, "selected_returned_capture_intake_capture_only", False)
                ),
            ),
            (
                "returned capture treated as cross-carrier proof",
                lambda: mutate_request(lambda r: flip_non_claim(r, "returned_capture_treated_as_cross_carrier_evidence")),
            ),
            (
                "zero exit code treated as external result",
                lambda: mutate_request(lambda r: flip_non_claim(r, "zero_exit_code_treated_as_external_result")),
            ),
            (
                "string zero treated as external result",
                lambda: mutate_request(lambda r: flip_non_claim(r, "string_zero_treated_as_external_result")),
            ),
            (
                "OK output treated as external result",
                lambda: mutate_request(lambda r: flip_non_claim(r, "ok_output_treated_as_external_result")),
            ),
            (
                "Ran 7 tests treated as cross-carrier proof",
                lambda: mutate_request(lambda r: flip_non_claim(r, "ran_7_tests_treated_as_cross_carrier_proof")),
            ),
            (
                "placeholder carrier fields repaired",
                lambda: mutate_request(
                    lambda r: set_field(r, "selected_returned_capture_placeholder_fields_unrepaired", False)
                ),
            ),
            (
                "returned capture material missing",
                lambda: mutate_request(lambda r: pop_field(r, "selected_returned_capture_material_basis")),
            ),
            (
                "returned zip path missing",
                lambda: mutate_request(lambda r: set_field(r, "selected_returned_capture_zip_path", "")),
            ),
            (
                "returned hash path missing",
                lambda: mutate_request(lambda r: set_field(r, "selected_returned_capture_hash_path", "")),
            ),
            (
                "returned extracted directory missing",
                lambda: mutate_request(
                    lambda r: set_field(r, "selected_returned_capture_extracted_directory_path", "")
                ),
            ),
            (
                "returned combined terminal log missing",
                lambda: mutate_request(
                    lambda r: set_field(r, "selected_returned_capture_combined_terminal_log_path", "")
                ),
            ),
            (
                "returned exit code missing",
                lambda: mutate_request(lambda r: set_field(r, "selected_returned_capture_exit_code", "")),
            ),
            (
                "returned command text missing",
                lambda: mutate_request(lambda r: set_field(r, "selected_returned_capture_command_text", "")),
            ),
            (
                "returned timestamps missing",
                lambda: mutate_request(lambda r: set_field(r, "selected_returned_capture_started_at", "")),
            ),
            (
                "output capture basis missing",
                lambda: mutate_request(lambda r: pop_field(r, "selected_second_carrier_output_capture_basis")),
            ),
            (
                "output capture not recorded",
                lambda: mutate_request(
                    lambda r: set_field(
                        r, "selected_second_carrier_output_capture_result_outcome", "NOT_RECORDED"
                    )
                ),
            ),
            (
                "output capture failed checks",
                lambda: mutate_request(
                    lambda r: set_field(r, "selected_second_carrier_output_capture_failed_check_count", 1)
                ),
            ),
            (
                "external-result boundary treated as external result",
                lambda: mutate_request(
                    lambda r: flip_non_claim(
                        r, "second_carrier_external_result_boundary_treated_as_external_result"
                    )
                ),
            ),
            (
                "external-result boundary treated as cross-carrier evidence",
                lambda: mutate_request(
                    lambda r: flip_non_claim(
                        r, "second_carrier_external_result_boundary_treated_as_cross_carrier_evidence"
                    )
                ),
            ),
            (
                "external-result boundary treated as portable verification closure",
                lambda: mutate_request(
                    lambda r: flip_non_claim(
                        r,
                        "second_carrier_external_result_boundary_treated_as_portable_verification_closure",
                    )
                ),
            ),
            (
                "external-result boundary treated as source transfer",
                lambda: mutate_request(
                    lambda r: flip_non_claim(
                        r, "second_carrier_external_result_boundary_treated_as_source_transfer"
                    )
                ),
            ),
            (
                "external-result boundary treated as source receipt",
                lambda: mutate_request(
                    lambda r: flip_non_claim(
                        r, "second_carrier_external_result_boundary_treated_as_source_receipt"
                    )
                ),
            ),
            (
                "external-result boundary treated as reception authorization",
                lambda: mutate_request(
                    lambda r: flip_non_claim(
                        r, "second_carrier_external_result_boundary_treated_as_reception_authorization"
                    )
                ),
            ),
            (
                "external-result boundary treated as source",
                lambda: mutate_request(
                    lambda r: flip_non_claim(r, "second_carrier_external_result_boundary_treated_as_source")
                ),
            ),
            (
                "external-result boundary treated as authority",
                lambda: mutate_request(
                    lambda r: flip_non_claim(r, "second_carrier_external_result_boundary_treated_as_authority")
                ),
            ),
            (
                "external-result boundary treated as currentness",
                lambda: mutate_request(
                    lambda r: flip_non_claim(
                        r, "second_carrier_external_result_boundary_treated_as_currentness"
                    )
                ),
            ),
            (
                "external-result boundary treated as final completion",
                lambda: mutate_request(
                    lambda r: flip_non_claim(
                        r, "second_carrier_external_result_boundary_treated_as_final_completion"
                    )
                ),
            ),
            (
                "external-result boundary treated as runtime",
                lambda: mutate_request(
                    lambda r: flip_non_claim(r, "second_carrier_external_result_boundary_treated_as_runtime")
                ),
            ),
            (
                "external-result boundary treated as continuation",
                lambda: mutate_request(
                    lambda r: flip_non_claim(
                        r, "second_carrier_external_result_boundary_treated_as_continuation"
                    )
                ),
            ),
            (
                "external-result boundary treated as reusable permission",
                lambda: mutate_request(
                    lambda r: flip_non_claim(
                        r, "second_carrier_external_result_boundary_treated_as_reusable_permission"
                    )
                ),
            ),
            (
                "external-result boundary treated as follow-on work",
                lambda: mutate_request(
                    lambda r: flip_non_claim(
                        r, "second_carrier_external_result_boundary_treated_as_follow_on_work"
                    )
                ),
            ),
            ("external result created", lambda: mutate_request(lambda r: flip_non_claim(r, "external_result_created"))),
            (
                "cross-carrier evidence created",
                lambda: mutate_request(lambda r: flip_non_claim(r, "cross_carrier_evidence_created")),
            ),
            (
                "portable verification closure created",
                lambda: mutate_request(lambda r: flip_non_claim(r, "portable_verification_closure_created")),
            ),
            ("source transfer occurred", lambda: mutate_request(lambda r: flip_non_claim(r, "source_transfer_occurred"))),
            ("source receipt occurred", lambda: mutate_request(lambda r: flip_non_claim(r, "source_receipt_occurred"))),
            (
                "reception authorization created",
                lambda: mutate_request(lambda r: flip_non_claim(r, "reception_authorization_created")),
            ),
            ("source created", lambda: mutate_request(lambda r: flip_non_claim(r, "source_created"))),
            ("authority created", lambda: mutate_request(lambda r: flip_non_claim(r, "authority_created"))),
            ("currentness created", lambda: mutate_request(lambda r: flip_non_claim(r, "currentness_created"))),
            (
                "final completion claimed",
                lambda: mutate_request(lambda r: flip_non_claim(r, "final_completion_claimed")),
            ),
            (
                "runtime hosting created",
                lambda: mutate_request(lambda r: flip_non_claim(r, "runtime_hosting_created")),
            ),
            ("deployment created", lambda: mutate_request(lambda r: flip_non_claim(r, "deployment_created"))),
            ("public release created", lambda: mutate_request(lambda r: flip_non_claim(r, "public_release_created"))),
            (
                "operation permission created",
                lambda: mutate_request(lambda r: flip_non_claim(r, "operation_permission_created")),
            ),
            ("continuation authorized", lambda: mutate_request(lambda r: flip_non_claim(r, "continuation_authorized"))),
            (
                "reusable permission created",
                lambda: mutate_request(lambda r: flip_non_claim(r, "reusable_permission_created")),
            ),
            ("follow-on authorized", lambda: mutate_request(lambda r: flip_non_claim(r, "follow_on_work_authorized"))),
            (
                "receiving carrier treated as authority",
                lambda: mutate_request(lambda r: flip_non_claim(r, "receiving_carrier_treated_as_authority")),
            ),
            (
                "artifact existence treated as external-result authority",
                lambda: mutate_request(
                    lambda r: flip_non_claim(r, "artifact_existence_treated_as_external_result_authority")
                ),
            ),
            (
                "artifact path treated as currentness",
                lambda: mutate_request(lambda r: flip_non_claim(r, "artifact_path_treated_as_currentness")),
            ),
            (
                "repo-local availability treated as authority",
                lambda: mutate_request(
                    lambda r: flip_non_claim(r, "repo_local_availability_treated_as_external_result_authority")
                ),
            ),
            (
                "hidden repo state used as content",
                lambda: mutate_request(lambda r: flip_non_claim(r, "hidden_repo_state_used_as_external_result_content")),
            ),
            (
                "hidden repo state used as authority",
                lambda: mutate_request(lambda r: flip_non_claim(r, "hidden_repo_state_used_as_external_result_authority")),
            ),
            (
                "selected basis not reference shaped",
                lambda: mutate_request(lambda r: set_field(r, "selected_basis_reference_shape_posture", False)),
            ),
            (
                "raw full prior artifact body returned",
                lambda: mutate_request(lambda r: flip_non_claim(r, "raw_full_prior_artifact_body_returned")),
            ),
            (
                "predecessor failure evidence repaired",
                lambda: mutate_request(lambda r: flip_non_claim(r, "v1_repaired")),
            ),
            (
                "first success-boundary test hidden",
                lambda: mutate_request(lambda r: flip_non_claim(r, "first_success_boundary_test_hidden")),
            ),
            (
                "first result-boundary resolver claimed passed",
                lambda: mutate_request(lambda r: flip_non_claim(r, "first_result_boundary_resolver_claimed_passed")),
            ),
            (
                "command report lineage treated as current report artifact",
                lambda: mutate_request(
                    lambda r: set_field(r, "raw_full_prior_artifact_body_not_returned_posture", False)
                ),
            ),
            (
                "consumed request reopened",
                lambda: mutate_request(lambda r: flip_non_claim(r, "consumed_request_reopened")),
            ),
            (
                "authorization token reused",
                lambda: mutate_request(lambda r: flip_non_claim(r, "authorization_token_reused")),
            ),
            (
                "full prior artifact body emitted outside boundary",
                lambda: mutate_request(lambda r: set_field(r, "hostile_raw_body_content_contained_posture", False)),
            ),
            (
                "string zero representation became doctrine",
                lambda: mutate_request(
                    lambda r: set_field(r, "string_zero_representation_turned_into_doctrine", True)
                ),
            ),
            ("artifacts mutated", lambda: mutate_request(lambda r: flip_non_claim(r, "prior_artifacts_mutated"))),
            (
                "returned capture material mutated",
                lambda: mutate_request(lambda r: flip_non_claim(r, "returned_capture_material_mutated")),
            ),
            (
                "required non-claim missing",
                lambda: mutate_request(lambda r: drop_non_claim(r, "external_result_created")),
            ),
        )

        for name, build_case in block_cases:
            with self.subTest(name=name):
                result = (
                    resolver.resolve_portable_source_body_verification_second_carrier_external_result_boundary(
                        build_case()
                    )
                )
                self.assert_blocked_result(result)
                non_claims = result["non_claims"]
                self.assertIs(non_claims["zero_exit_code_treated_as_external_result"], False)
                self.assertIs(non_claims["string_zero_treated_as_external_result"], False)
                self.assertIs(non_claims["ok_output_treated_as_external_result"], False)
                self.assertIs(non_claims["ran_7_tests_treated_as_cross_carrier_proof"], False)
                self.assertIs(non_claims["returned_capture_treated_as_cross_carrier_evidence"], False)
                self.assertIs(non_claims["consumed_request_reopened"], False)
                self.assertIs(non_claims["authorization_token_reused"], False)
                self.assertIs(non_claims["first_success_boundary_test_repaired"], False)
                self.assertIs(non_claims["first_success_boundary_test_hidden"], False)
                self.assertIs(non_claims["first_success_boundary_test_claimed_passed"], False)
                self.assertIs(non_claims["v1_repaired"], False)
                self.assertIs(non_claims["v1_hidden"], False)
                self.assertIs(non_claims["v1_claimed_passed"], False)
                self.assertIs(non_claims["first_result_boundary_resolver_repaired"], False)
                self.assertIs(non_claims["first_result_boundary_resolver_hidden"], False)
                self.assertIs(non_claims["first_result_boundary_resolver_claimed_passed"], False)

    def test_path_and_write_behavior(self) -> None:
        request = build_request()
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp = Path(tmp_dir)
            request_path = tmp / "request.json"
            request_path.write_text(json.dumps(request, indent=2, sort_keys=True), encoding="utf-8")
            result = (
                resolver.resolve_portable_source_body_verification_second_carrier_external_result_boundary_from_path(
                    request_path
                )
            )
            self.assertEqual(RECORDED, result["outcome"])
            summary = (
                resolver.build_portable_source_body_verification_second_carrier_external_result_boundary_summary(
                    result
                )
            )
            self.assertEqual("0.1.0", summary["result_version"])
            self.assertEqual(resolver.RESOLVER_MODULE, summary["resolver_module"])

            malformed_path = tmp / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            self.assert_path_failure_is_bounded(malformed_path)

            array_path = tmp / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            self.assert_path_failure_is_bounded(array_path)

            missing_path = tmp / "missing.json"
            self.assert_path_failure_is_bounded(missing_path)

            patched_root = tmp / resolver.OUTPUT_ROOT
            with patch.object(resolver, "OUTPUT_ROOT", patched_root):
                first = (
                    resolver.write_portable_source_body_verification_second_carrier_external_result_boundary_result(
                        result
                    )
                )
                second = (
                    resolver.write_portable_source_body_verification_second_carrier_external_result_boundary_result(
                        result
                    )
                )
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertEqual(patched_root, first.parent)
            self.assertEqual(patched_root, second.parent)
            self.assertEqual(RECORDED, json.loads(first.read_text(encoding="utf-8"))["outcome"])
            self.assertEqual(RECORDED, json.loads(second.read_text(encoding="utf-8"))["outcome"])
            self.assertIn(
                "artifacts/"
                "integrity_host_v0_min_coexistence_portable_source_body_"
                "verification_second_carrier_external_result_boundary",
                first.as_posix(),
            )
            forbidden_fragments = (
                "actual_second_carrier_live_capture",
                "portable_source_body_verification_second_carrier_verification/",
                "portable_source_body_verification_second_carrier_success/",
                "portable_source_body_verification_second_carrier_result/",
                "cross_carrier",
                "portable_verification_closure",
                "runtime",
                "deployment",
                "public_release",
            )
            for fragment in forbidden_fragments:
                self.assertNotIn(fragment, first.as_posix())
                self.assertNotIn(fragment, second.as_posix())

    def test_non_mutation_of_declared_request_and_selected_basis(self) -> None:
        request = build_request()
        selected_before = {key: copy.deepcopy(request[key]) for key in SELECTED_BASIS_KEYS}
        posture_before = {key: copy.deepcopy(request[key]) for key in POSTURE_KEYS}
        scope_before = copy.deepcopy(request["second_carrier_external_result_boundary_scope"])
        non_claims_before = copy.deepcopy(request["declared_non_claims"])
        before = copy.deepcopy(request)

        result = (
            resolver.resolve_portable_source_body_verification_second_carrier_external_result_boundary(
                request
            )
        )

        self.assertEqual(RECORDED, result["outcome"])
        self.assertEqual(before, request)
        for key, value in selected_before.items():
            self.assertEqual(value, request[key], key)
        for key, value in posture_before.items():
            self.assertEqual(value, request[key], key)
        self.assertEqual(scope_before, request["second_carrier_external_result_boundary_scope"])
        self.assertEqual(non_claims_before, request["declared_non_claims"])

    def test_predecessor_failure_preservation(self) -> None:
        request = build_request()
        result = (
            resolver.resolve_portable_source_body_verification_second_carrier_external_result_boundary(
                request
            )
        )
        summary = (
            resolver.build_portable_source_body_verification_second_carrier_external_result_boundary_summary(
                result
            )
        )
        statement = result["second_carrier_external_result_boundary_statement"]
        non_claims = result["non_claims"]

        self.assertIs(statement["first_success_boundary_test_failure_preserved"], True)
        self.assertIs(statement["first_result_boundary_resolver_failure_preserved"], True)
        self.assertIs(
            summary["first_success_boundary_test_preserved_as_failed_predecessor"],
            True,
        )
        self.assertIs(summary["v1_predecessor_failure_preserved"], True)
        self.assertIs(summary["v1_not_repaired"], True)
        self.assertIs(summary["v1_not_hidden"], True)
        self.assertIs(summary["v1_not_claimed_passed"], True)
        self.assertIs(
            summary["first_result_boundary_resolver_preserved_as_failed_predecessor"],
            True,
        )
        self.assertIs(non_claims["first_success_boundary_test_repaired"], False)
        self.assertIs(non_claims["first_success_boundary_test_hidden"], False)
        self.assertIs(non_claims["first_success_boundary_test_claimed_passed"], False)
        self.assertIs(non_claims["v1_repaired"], False)
        self.assertIs(non_claims["v1_hidden"], False)
        self.assertIs(non_claims["v1_claimed_passed"], False)
        self.assertIs(non_claims["first_result_boundary_resolver_repaired"], False)
        self.assertIs(non_claims["first_result_boundary_resolver_hidden"], False)
        self.assertIs(non_claims["first_result_boundary_resolver_claimed_passed"], False)


if __name__ == "__main__":
    unittest.main()
