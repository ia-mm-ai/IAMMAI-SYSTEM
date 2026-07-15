"""Executable checks for second-carrier result posture only.

This suite is downstream of second-carrier-result-boundary-v2. It verifies that
the resolver records one bounded second-carrier result posture only: result is
not success, verification, external result, cross-carrier proof, source
transfer, source receipt, reception authorization, source, authority,
currentness, runtime, final completion, continuation, reusable permission, or
follow-on work. It also verifies that official enum, scope, and block-code
strings are not redacted while hostile raw body payload content remains
contained.
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

import resolve_portable_source_body_verification_second_carrier_result as resolver


RECORDED = resolver.OUTCOME_RECORDED
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = set(resolver.OUTCOME_FAMILY)
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_SECOND_CARRIER_RESULT_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
TRUE_RECORDED_FIELDS = tuple(resolver.ALLOWED_TRUE_RECORDED_FIELDS)
SELECTED_BASIS_KEYS = tuple(resolver.SELECTED_BASIS_KEYS)
POSTURE_KEYS = tuple(resolver.POSTURE_KEYS)

RAW_SENTINELS = (
    "RAW_SECOND_CARRIER_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
    "HOSTILE_SECOND_CARRIER_RESULT_FULL_BODY_VALUE_MUST_NOT_RETURN",
)
HOSTILE_VALUES = (
    "hostile-raw-body-value",
    "hostile-raw-full-body-value",
    "hostile-full-body-value",
    "hostile-artifact-body-value",
    "hostile-raw-result-body-value",
    "hostile-raw-output-body-value",
    "hostile-raw-capture-body-value",
    "hostile-capture-body-value",
    "hostile-second-carrier-result-body-value",
    "hostile-external-result-body-value",
    "hostile-cross-carrier-evidence-body-value",
    "hostile-source-body-value",
    "hostile-authority-body-value",
    "hostile-current-working-tree-value",
    "hostile-local-cache-value",
    "hostile-repo-local-only-dependency-value",
)
REDACTION_STRINGS = {
    "[bounded-result-redacted]",
    "[bounded-second-carrier-result-redacted-raw-body]",
}

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_second_carrier_result_metadata",
    "declared_second_carrier_result_question",
    "selected_second_carrier_result_boundary_v2_basis",
    "selected_second_carrier_result_boundary_v2_terminal_summary_basis",
    "selected_returned_second_carrier_live_capture_intake_basis",
    "selected_returned_capture_material_basis",
    "selected_returned_zip_basis",
    "selected_returned_hash_basis",
    "selected_returned_extracted_files_basis",
    "selected_returned_combined_terminal_log_basis",
    "selected_returned_exit_code_basis",
    "selected_returned_command_text_basis",
    "selected_returned_timestamps_basis",
    "selected_second_carrier_output_capture_basis",
    "selected_second_carrier_output_capture_terminal_summary_basis",
    "selected_second_carrier_output_capture_boundary_basis",
    "selected_second_carrier_execution_output_basis",
    "selected_second_carrier_execution_basis",
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
    "second_carrier_result_spec_only_posture",
    "one_bounded_second_carrier_result_posture",
    "second_carrier_result_boundary_v2_basis_preserved_posture",
    "returned_second_carrier_capture_basis_preserved_posture",
    "capture_intake_basis_preserved_posture",
    "second_carrier_output_capture_basis_preserved_posture",
    "capture_artifact_basis_preserved_posture",
    "result_recorded_bounded_posture",
    "result_artifact_recorded_or_bounded_posture",
    "result_not_success_posture",
    "result_not_verification_posture",
    "result_not_external_result_posture",
    "result_not_cross_carrier_evidence_posture",
    "result_not_source_transfer_posture",
    "result_not_source_receipt_posture",
    "result_not_reception_authorization_posture",
    "zero_exit_code_not_success_posture",
    "ok_output_not_verification_posture",
    "ran_7_tests_not_cross_carrier_proof_posture",
    "returned_capture_not_cross_carrier_proof_posture",
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
    "repo_local_availability_not_result_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "first_result_boundary_resolver_failure_preserved_posture",
    "second_carrier_result_scope",
    "second_carrier_result_checks",
    "second_carrier_result_statement",
    "second_carrier_result_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_second_carrier_result_summary",
)

REPRESENTATIVE_BLOCK_CODES = (
    "SECOND_CARRIER_RESULT_QUESTION_UNDECLARED",
    "SECOND_CARRIER_RESULT_INTENT_UNSUPPORTED",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_BASIS_MISSING",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_NOT_RECORDED",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_VERSION_NOT_0_2_0",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_DID_NOT_DECLARE_FUTURE_RESULT_STEP",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_ALREADY_CREATED_RESULT",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_ALREADY_CREATED_SUCCESS",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_ALREADY_CREATED_EXTERNAL_RESULT",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_ALREADY_CREATED_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_TREATED_ZERO_EXIT_CODE_AS_SUCCESS",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_TREATED_OK_AS_VERIFICATION",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_TREATED_RETURNED_CAPTURE_AS_CROSS_CARRIER_PROOF",
    "SECOND_CARRIER_RESULT_BOUNDARY_V2_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
    "RETURNED_CAPTURE_INTAKE_BASIS_MISSING",
    "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
    "RETURNED_CAPTURE_TREATED_AS_RESULT",
    "RETURNED_CAPTURE_TREATED_AS_SUCCESS",
    "RETURNED_CAPTURE_TREATED_AS_VERIFICATION",
    "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_PROOF",
    "ZERO_EXIT_CODE_TREATED_AS_SUCCESS",
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
    "SECOND_CARRIER_OUTPUT_CAPTURE_DID_NOT_RECORD_BOUNDED_CAPTURE",
    "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_RESULT",
    "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_SUCCESS",
    "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_RESULT_TREATED_AS_SUCCESS",
    "SECOND_CARRIER_RESULT_TREATED_AS_VERIFICATION",
    "SECOND_CARRIER_RESULT_TREATED_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_RESULT_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_RESULT_TREATED_AS_SOURCE_TRANSFER",
    "SECOND_CARRIER_RESULT_TREATED_AS_SOURCE_RECEIPT",
    "SECOND_CARRIER_RESULT_TREATED_AS_RECEPTION_AUTHORIZATION",
    "SECOND_CARRIER_RESULT_TREATED_AS_SOURCE",
    "SECOND_CARRIER_RESULT_TREATED_AS_AUTHORITY",
    "SECOND_CARRIER_RESULT_TREATED_AS_CURRENTNESS",
    "SECOND_CARRIER_RESULT_TREATED_AS_FINAL_COMPLETION",
    "SECOND_CARRIER_RESULT_TREATED_AS_RUNTIME",
    "SECOND_CARRIER_RESULT_TREATED_AS_CONTINUATION",
    "SECOND_CARRIER_RESULT_TREATED_AS_REUSABLE_PERMISSION",
    "SECOND_CARRIER_RESULT_TREATED_AS_FOLLOW_ON_WORK",
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
    "FOLLOW_ON_WORK_AUTHORIZED",
    "RECEIVING_CARRIER_TREATED_AS_AUTHORITY",
    "ARTIFACT_EXISTENCE_TREATED_AS_RESULT_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_RESULT_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_RESULT_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_RESULT_AUTHORITY",
    "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "FIRST_RESULT_BOUNDARY_RESOLVER_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_RESULT",
    "ARTIFACTS_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_SECOND_CARRIER_RESULT_SCOPE",
)


def build_request(**overrides: Any) -> dict[str, Any]:
    return resolver.build_declared_portable_source_body_verification_second_carrier_result_request(
        **overrides
    )


def mutate_non_claim(request: dict[str, Any], key: str, value: bool = True) -> None:
    request.setdefault("declared_non_claims", {})[key] = value


def remove_basis_and_shortcut(
    request: dict[str, Any], basis_key: str, shortcut_key: str | None = None
) -> None:
    request[basis_key] = {}
    if shortcut_key:
        request[shortcut_key] = ""


class SecondCarrierResultTest(unittest.TestCase):
    """Bounded second-carrier-result executable checks."""

    def assert_public_block_codes(self, result: dict[str, Any]) -> None:
        block = result.get("block")
        if block:
            self.assertIn(block.get("block_code"), resolver.BLOCK_CODES)
        for check in result.get("second_carrier_result_checks", []):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_generated_bools_are_bools(self, result: dict[str, Any]) -> None:
        statement = result.get("second_carrier_result_statement", {})
        for key in TRUE_RECORDED_FIELDS:
            self.assertIsInstance(statement.get(key), bool, key)
        non_claims = result.get("non_claims", {})
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIsInstance(non_claims.get(key), bool, key)
        for check in result.get("second_carrier_result_checks", []):
            self.assertIsInstance(check.get("passed"), bool, check.get("check_name"))
        for posture_key in POSTURE_KEYS:
            posture = result.get(posture_key, {})
            if isinstance(posture, dict) and "declared" in posture:
                self.assertIsInstance(posture["declared"], bool, posture_key)

    def assert_no_raw_or_hidden_sentinels(self, result: dict[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in RAW_SENTINELS:
            self.assertNotIn(sentinel, serialized)
        for hostile in HOSTILE_VALUES:
            self.assertNotIn(hostile, serialized)

    def assert_official_enum_strings_not_redacted(self, result: dict[str, Any]) -> None:
        scope_section = result.get("second_carrier_result_scope", {})
        scope_values = scope_section.get("scope_values", [])
        supported_values = scope_section.get("supported_scope_values", [])
        required_official_values = (
            "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
            "RETURNED_RESULT_CONTAINMENT_PRESERVED",
            "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
            "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
        )
        for value in required_official_values:
            self.assertIn(value, scope_values)
            self.assertIn(value, supported_values)
        for value in scope_values:
            self.assertIn(value, resolver.SUPPORTED_SECOND_CARRIER_RESULT_SCOPE)
            self.assertNotIn(value, REDACTION_STRINGS)
        for value in resolver.SUPPORTED_SECOND_CARRIER_RESULT_SCOPE:
            self.assertNotIn(value, REDACTION_STRINGS)

    def assert_no_later_work_created(
        self, result: dict[str, Any], ignored_non_claims: set[str] | None = None
    ) -> None:
        ignored = ignored_non_claims or set()
        non_claims = result.get("non_claims", {})
        for key in REQUIRED_FALSE_NON_CLAIMS:
            if key not in ignored:
                self.assertIs(non_claims.get(key), False, key)
        non_meaning = result.get("second_carrier_result_non_meaning", {})
        for key, value in non_meaning.items():
            self.assertIs(value, False, key)

    def assert_recorded_result_is_clean(self, result: dict[str, Any]) -> None:
        summary = resolver.build_portable_source_body_verification_second_carrier_result_summary(
            result
        )
        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertIsNone(result.get("block"))
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(
            summary["resolver_module"],
            "resolve_portable_source_body_verification_second_carrier_result",
        )
        self.assertGreater(summary["passed_check_count"], 0)
        self.assert_public_block_codes(result)
        self.assert_generated_bools_are_bools(result)
        self.assert_no_raw_or_hidden_sentinels(result)
        self.assert_official_enum_strings_not_redacted(result)
        self.assert_no_later_work_created(result)

    def assert_blocked_result_is_bounded(
        self,
        result: dict[str, Any],
        expected_code: str | None = None,
        ignored_non_claims: set[str] | None = None,
    ) -> None:
        self.assertEqual(result.get("outcome"), BLOCKED)
        self.assertIsInstance(result.get("block"), dict)
        block_code = result["block"].get("block_code")
        self.assertIn(block_code, resolver.BLOCK_CODES)
        if expected_code:
            self.assertEqual(block_code, expected_code)
        self.assert_public_block_codes(result)
        self.assert_generated_bools_are_bools(result)
        self.assert_no_raw_or_hidden_sentinels(result)
        statement = result.get("second_carrier_result_statement", {})
        for key in TRUE_RECORDED_FIELDS:
            self.assertIs(statement.get(key), False, key)
        self.assert_no_later_work_created(result, ignored_non_claims)

    def test_public_api_and_constants(self) -> None:
        public_names = (
            "resolve_portable_source_body_verification_second_carrier_result",
            "resolve_portable_source_body_verification_second_carrier_result_from_path",
            "write_portable_source_body_verification_second_carrier_result_result",
            "build_portable_source_body_verification_second_carrier_result_summary",
            "build_declared_portable_source_body_verification_second_carrier_result_request",
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_SCOPE_VALUES",
            "SUPPORTED_SECOND_CARRIER_RESULT_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        )
        for name in public_names:
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_portable_source_body_verification_second_carrier_result",
        )
        self.assertEqual(
            resolver.SUPPORTED_SECOND_CARRIER_RESULT_SCOPE,
            resolver.SUPPORTED_SCOPE_VALUES,
        )
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_portable_source_body_verification_"
                "second_carrier_result"
            )
        )
        for value in (
            "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
            "RETURNED_RESULT_CONTAINMENT_PRESERVED",
            "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
            "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
        ):
            self.assertIn(value, resolver.SUPPORTED_SECOND_CARRIER_RESULT_SCOPE)
        for code in REPRESENTATIVE_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES, code)

    def test_successful_recorded_result_from_no_argument_builder(self) -> None:
        request = build_request()
        result = resolver.resolve_portable_source_body_verification_second_carrier_result(
            request
        )
        summary = resolver.build_portable_source_body_verification_second_carrier_result_summary(
            result
        )

        self.assertIsInstance(result, dict)
        self.assert_recorded_result_is_clean(result)
        self.assertEqual(summary["request_id"], request["second_carrier_result_request_id"])
        self.assertEqual(
            summary["question"], request["second_carrier_result_question"]
        )
        self.assertEqual(summary["intent"], request["second_carrier_result_intent"])
        self.assertEqual(
            result["portable_source_body_verification_second_carrier_result_summary"],
            summary,
        )
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result, section)

        statement = result["second_carrier_result_statement"]
        for key in TRUE_RECORDED_FIELDS:
            self.assertIs(statement.get(key), True, key)
        non_claims = result["non_claims"]
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(non_claims.get(key), False, key)

        boundary = result["selected_second_carrier_result_boundary_v2_basis"]
        self.assertEqual(
            boundary["selected_outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RESULT_BOUNDARY_RECORDED",
        )
        self.assertEqual(boundary["selected_result_version"], "0.2.0")
        self.assertEqual(boundary["selected_failed_check_count"], 0)
        self.assertIs(boundary["declared_future_result_step"], True)
        self.assertIs(boundary["first_result_boundary_resolver_preserved"], True)

        intake = result["selected_returned_second_carrier_live_capture_intake_basis"]
        capture = result["selected_returned_capture_material_basis"]
        exit_code = result["selected_returned_exit_code_basis"]
        self.assertIs(intake["intake_preserved"], True)
        self.assertIs(intake["intake_capture_only"], True)
        self.assertIs(intake["macbook_pro_to_macbook_air"], True)
        self.assertEqual(capture["working_directory"], "/Users/markomarkota/IAMMAI-SYSTEM")
        self.assertIn("Ran 7 tests", capture["ran_7_tests_line"])
        self.assertEqual(capture["ok_line"], "OK")
        self.assertEqual(capture["raw_placeholder_carrier_label"], "raw_placeholder_carrier_label")
        self.assertEqual(capture["raw_placeholder_carrier_type"], "raw_placeholder_carrier_type")
        self.assertIs(capture["placeholder_fields_unrepaired"], True)
        self.assertEqual(exit_code["selected_exit_code"], 0)
        self.assertIs(exit_code["zero_exit_code_not_success"], True)

    def test_official_enum_strings_are_not_redacted(self) -> None:
        result = resolver.resolve_portable_source_body_verification_second_carrier_result(
            build_request()
        )
        self.assert_recorded_result_is_clean(result)

        checks = result["second_carrier_result_checks"]
        for check in checks:
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code:
                    self.assertIn(code, resolver.BLOCK_CODES)
                    self.assertNotEqual(code, "[bounded-result-redacted]")

        request = build_request(
            second_carrier_result_scope=list(
                resolver.SUPPORTED_SECOND_CARRIER_RESULT_SCOPE
            )
        )
        all_scope_result = (
            resolver.resolve_portable_source_body_verification_second_carrier_result(
                request
            )
        )
        self.assert_recorded_result_is_clean(all_scope_result)

    def test_raw_and_hidden_hostile_content_is_contained_without_mutating_input(
        self,
    ) -> None:
        request = build_request()
        hostile_payload = {
            "raw_body": "hostile-raw-body-value",
            "raw_full_body": "hostile-raw-full-body-value",
            "full_body": "hostile-full-body-value",
            "artifact_body": "hostile-artifact-body-value",
            "raw_result_body": "hostile-raw-result-body-value",
            "raw_output_body": "hostile-raw-output-body-value",
            "raw_capture_body": "hostile-raw-capture-body-value",
            "capture_body": "hostile-capture-body-value",
            "second_carrier_result_body": "hostile-second-carrier-result-body-value",
            "external_result_body": "hostile-external-result-body-value",
            "cross_carrier_evidence_body": (
                "hostile-cross-carrier-evidence-body-value"
            ),
            "source_body": "hostile-source-body-value",
            "authority_body": "hostile-authority-body-value",
            "hidden_repo_state": "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
            "current_working_tree": "hostile-current-working-tree-value",
            "local_cache": "hostile-local-cache-value",
            "repo_local_only_dependency": "hostile-repo-local-only-dependency-value",
            "nested": {
                "official_scope": "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
                "sentinels": [
                    "RAW_SECOND_CARRIER_RESULT_BODY_MUST_NOT_RETURN",
                    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
                    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
                    "HOSTILE_SECOND_CARRIER_RESULT_FULL_BODY_VALUE_MUST_NOT_RETURN",
                ],
            },
        }
        injected_sections = (
            "selected_second_carrier_result_boundary_v2_basis",
            "selected_returned_second_carrier_live_capture_intake_basis",
            "selected_returned_capture_material_basis",
            "selected_returned_combined_terminal_log_basis",
            "selected_second_carrier_output_capture_basis",
            "selected_second_carrier_execution_output_basis",
            "selected_command_report_lineage_basis",
            "selected_artifact_containment_basis",
        )
        for section in injected_sections:
            request[section] = copy.deepcopy(request[section])
            request[section]["hostile_payload"] = copy.deepcopy(hostile_payload)

        original = copy.deepcopy(request)
        result = resolver.resolve_portable_source_body_verification_second_carrier_result(
            request
        )

        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assert_no_raw_or_hidden_sentinels(result)
        self.assert_official_enum_strings_not_redacted(result)
        self.assert_public_block_codes(result)
        self.assert_generated_bools_are_bools(result)
        self.assert_no_later_work_created(result)
        self.assertIs(result["non_claims"]["hidden_repo_state_used_as_result_content"], False)
        self.assertIs(result["non_claims"]["hidden_repo_state_used_as_result_authority"], False)
        self.assertIs(
            result["non_claims"]["repo_local_availability_treated_as_result_authority"],
            False,
        )
        self.assertIs(result["non_claims"]["receiving_carrier_treated_as_authority"], False)
        self.assertIs(
            result["non_claims"]["artifact_existence_treated_as_result_authority"],
            False,
        )
        self.assertIs(result["non_claims"]["artifact_path_treated_as_currentness"], False)
        self.assertEqual(request, original)

    def test_representative_blocking_behavior(self) -> None:
        def with_non_claim(key: str) -> Callable[[dict[str, Any]], None]:
            return lambda request: mutate_non_claim(request, key, True)

        cases: list[tuple[str, Callable[[dict[str, Any]], None], str | None, set[str]]] = [
            (
                "explicit block intent",
                lambda request: request.update(
                    {
                        "second_carrier_result_intent": resolver.INTENT_BLOCK,
                        "block_reason": "operator requested bounded block",
                    }
                ),
                "SECOND_CARRIER_RESULT_BLOCK_REQUESTED",
                set(),
            ),
            (
                "unsupported intent",
                lambda request: request.update(
                    {"second_carrier_result_intent": "UNSUPPORTED_INTENT"}
                ),
                "SECOND_CARRIER_RESULT_INTENT_UNSUPPORTED",
                set(),
            ),
            (
                "unsupported scope",
                lambda request: request.update(
                    {"second_carrier_result_scope": ["UNSUPPORTED_SCOPE"]}
                ),
                "UNSUPPORTED_SECOND_CARRIER_RESULT_SCOPE",
                set(),
            ),
            (
                "missing second-carrier-result-boundary-v2 basis",
                lambda request: remove_basis_and_shortcut(
                    request,
                    "selected_second_carrier_result_boundary_v2_basis",
                    "selected_second_carrier_result_boundary_v2_result_path",
                ),
                "SECOND_CARRIER_RESULT_BOUNDARY_V2_BASIS_MISSING",
                set(),
            ),
            (
                "second-carrier-result-boundary-v2 not recorded",
                lambda request: request.update(
                    {
                        "selected_second_carrier_result_boundary_v2_result_outcome": (
                            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RESULT_BOUNDARY_NOT_RECORDED"
                        )
                    }
                ),
                "SECOND_CARRIER_RESULT_BOUNDARY_V2_NOT_RECORDED",
                set(),
            ),
            (
                "second-carrier-result-boundary-v2 failed checks",
                lambda request: request.update(
                    {"selected_second_carrier_result_boundary_v2_failed_check_count": 1}
                ),
                "SECOND_CARRIER_RESULT_BOUNDARY_V2_FAILED_CHECKS_PRESENT",
                set(),
            ),
            (
                "second-carrier-result-boundary-v2 version not 0.2.0",
                lambda request: request.update(
                    {"selected_second_carrier_result_boundary_v2_result_version": "0.1.0"}
                ),
                "SECOND_CARRIER_RESULT_BOUNDARY_V2_VERSION_NOT_0_2_0",
                set(),
            ),
            (
                "second-carrier-result-boundary-v2 did not declare future result step",
                lambda request: request.update(
                    {
                        "selected_second_carrier_result_boundary_v2_declared_future_result_step": False
                    }
                ),
                "SECOND_CARRIER_RESULT_BOUNDARY_V2_DID_NOT_DECLARE_FUTURE_RESULT_STEP",
                set(),
            ),
            (
                "second-carrier-result-boundary-v2 already created result",
                lambda request: request.update(
                    {
                        "selected_second_carrier_result_boundary_v2_already_created_result": True
                    }
                ),
                "SECOND_CARRIER_RESULT_BOUNDARY_V2_ALREADY_CREATED_RESULT",
                set(),
            ),
            (
                "second-carrier-result-boundary-v2 already created success",
                lambda request: request.update(
                    {
                        "selected_second_carrier_result_boundary_v2_already_created_success": True
                    }
                ),
                "SECOND_CARRIER_RESULT_BOUNDARY_V2_ALREADY_CREATED_SUCCESS",
                set(),
            ),
            (
                "second-carrier-result-boundary-v2 already created external result",
                lambda request: request.update(
                    {
                        "selected_second_carrier_result_boundary_v2_already_created_external_result": True
                    }
                ),
                "SECOND_CARRIER_RESULT_BOUNDARY_V2_ALREADY_CREATED_EXTERNAL_RESULT",
                set(),
            ),
            (
                "second-carrier-result-boundary-v2 already created cross-carrier evidence",
                lambda request: request.update(
                    {
                        "selected_second_carrier_result_boundary_v2_already_created_cross_carrier_evidence": True
                    }
                ),
                "SECOND_CARRIER_RESULT_BOUNDARY_V2_ALREADY_CREATED_CROSS_CARRIER_EVIDENCE",
                set(),
            ),
            (
                "boundary-v2 treated zero exit code as success",
                lambda request: request.update(
                    {
                        "selected_second_carrier_result_boundary_v2_zero_exit_code_not_success": False
                    }
                ),
                "SECOND_CARRIER_RESULT_BOUNDARY_V2_TREATED_ZERO_EXIT_CODE_AS_SUCCESS",
                set(),
            ),
            (
                "boundary-v2 treated OK as verification",
                lambda request: request.update(
                    {
                        "selected_second_carrier_result_boundary_v2_ok_not_verification": False
                    }
                ),
                "SECOND_CARRIER_RESULT_BOUNDARY_V2_TREATED_OK_AS_VERIFICATION",
                set(),
            ),
            (
                "boundary-v2 treated returned capture as cross-carrier proof",
                lambda request: request.update(
                    {
                        "selected_second_carrier_result_boundary_v2_returned_capture_not_cross_carrier_proof": False
                    }
                ),
                "SECOND_CARRIER_RESULT_BOUNDARY_V2_TREATED_RETURNED_CAPTURE_AS_CROSS_CARRIER_PROOF",
                set(),
            ),
            (
                "boundary-v2 redacted official enum scope strings",
                lambda request: request.update(
                    {
                        "selected_second_carrier_result_boundary_v2_official_enum_scope_strings_redacted": True
                    }
                ),
                "SECOND_CARRIER_RESULT_BOUNDARY_V2_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
                set(),
            ),
            (
                "returned capture intake basis missing",
                lambda request: remove_basis_and_shortcut(
                    request,
                    "selected_returned_second_carrier_live_capture_intake_basis",
                    "selected_returned_capture_intake_path",
                ),
                "RETURNED_CAPTURE_INTAKE_BASIS_MISSING",
                set(),
            ),
            (
                "returned capture intake not preserved",
                lambda request: request.update(
                    {"selected_returned_capture_intake_preserved": False}
                ),
                "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
                set(),
            ),
            (
                "returned capture treated as result",
                lambda request: request.update(
                    {"selected_returned_capture_intake_capture_only": False}
                ),
                "RETURNED_CAPTURE_TREATED_AS_RESULT",
                set(),
            ),
            (
                "returned capture treated as success",
                with_non_claim("zero_exit_code_treated_as_success"),
                "ZERO_EXIT_CODE_TREATED_AS_SUCCESS",
                {"zero_exit_code_treated_as_success"},
            ),
            (
                "returned capture treated as verification",
                lambda request: request.update(
                    {"selected_returned_capture_ok_not_verification": False}
                ),
                "OK_OUTPUT_TREATED_AS_VERIFICATION",
                set(),
            ),
            (
                "returned capture treated as cross-carrier proof",
                with_non_claim("returned_capture_treated_as_cross_carrier_evidence"),
                "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_PROOF",
                {"returned_capture_treated_as_cross_carrier_evidence"},
            ),
            (
                "zero exit code treated as success",
                with_non_claim("zero_exit_code_treated_as_success"),
                "ZERO_EXIT_CODE_TREATED_AS_SUCCESS",
                {"zero_exit_code_treated_as_success"},
            ),
            (
                "OK output treated as verification",
                with_non_claim("ok_output_treated_as_verification"),
                "OK_OUTPUT_TREATED_AS_VERIFICATION",
                {"ok_output_treated_as_verification"},
            ),
            (
                "Ran 7 tests treated as cross-carrier proof",
                with_non_claim("ran_7_tests_treated_as_cross_carrier_proof"),
                "RAN_7_TESTS_TREATED_AS_CROSS_CARRIER_PROOF",
                {"ran_7_tests_treated_as_cross_carrier_proof"},
            ),
            (
                "placeholder carrier fields repaired",
                lambda request: request.update(
                    {"selected_returned_capture_placeholder_fields_unrepaired": False}
                ),
                "PLACEHOLDER_CARRIER_FIELDS_REPAIRED",
                set(),
            ),
            (
                "returned capture material missing",
                lambda request: request.update(
                    {"selected_returned_capture_working_directory": ""}
                ),
                "RETURNED_CAPTURE_MATERIAL_MISSING",
                set(),
            ),
            (
                "returned zip path missing",
                lambda request: remove_basis_and_shortcut(
                    request,
                    "selected_returned_zip_basis",
                    "selected_returned_capture_zip_path",
                ),
                "RETURNED_ZIP_PATH_MISSING",
                set(),
            ),
            (
                "returned hash path missing",
                lambda request: remove_basis_and_shortcut(
                    request,
                    "selected_returned_hash_basis",
                    "selected_returned_capture_hash_path",
                ),
                "RETURNED_HASH_PATH_MISSING",
                set(),
            ),
            (
                "returned extracted directory missing",
                lambda request: remove_basis_and_shortcut(
                    request,
                    "selected_returned_extracted_files_basis",
                    "selected_returned_capture_extracted_directory_path",
                ),
                "RETURNED_EXTRACTED_DIRECTORY_MISSING",
                set(),
            ),
            (
                "returned combined terminal log missing",
                lambda request: remove_basis_and_shortcut(
                    request,
                    "selected_returned_combined_terminal_log_basis",
                    "selected_returned_capture_combined_terminal_log_path",
                ),
                "RETURNED_COMBINED_TERMINAL_LOG_MISSING",
                set(),
            ),
            (
                "returned exit code missing",
                lambda request: request.update(
                    {
                        "selected_returned_capture_exit_code": None,
                        "selected_returned_exit_code_basis": {},
                    }
                ),
                "RETURNED_EXIT_CODE_MISSING",
                set(),
            ),
            (
                "returned command text missing",
                lambda request: request.update(
                    {
                        "selected_returned_capture_command_text": "",
                        "selected_returned_command_text_basis": {},
                    }
                ),
                "RETURNED_COMMAND_TEXT_MISSING",
                set(),
            ),
            (
                "returned timestamps missing",
                lambda request: request.update(
                    {
                        "selected_returned_capture_started_at": "",
                        "selected_returned_capture_completed_at": "",
                    }
                ),
                "RETURNED_TIMESTAMPS_MISSING",
                set(),
            ),
            (
                "second-carrier output capture basis missing",
                lambda request: remove_basis_and_shortcut(
                    request,
                    "selected_second_carrier_output_capture_basis",
                    "selected_second_carrier_output_capture_result_path",
                ),
                "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_MISSING",
                set(),
            ),
            (
                "second-carrier output capture not recorded",
                lambda request: request.update(
                    {"selected_second_carrier_output_capture_result_outcome": "NOT_RECORDED"}
                ),
                "SECOND_CARRIER_OUTPUT_CAPTURE_NOT_RECORDED",
                set(),
            ),
            (
                "second-carrier output capture failed checks",
                lambda request: request.update(
                    {"selected_second_carrier_output_capture_failed_check_count": 1}
                ),
                "SECOND_CARRIER_OUTPUT_CAPTURE_FAILED_CHECKS_PRESENT",
                set(),
            ),
            (
                "second-carrier output capture did not record bounded capture",
                lambda request: request.update(
                    {
                        "selected_second_carrier_output_capture_bounded_capture_recorded": False
                    }
                ),
                "SECOND_CARRIER_OUTPUT_CAPTURE_DID_NOT_RECORD_BOUNDED_CAPTURE",
                set(),
            ),
            (
                "second-carrier output capture treated capture as result",
                lambda request: request.update(
                    {"selected_second_carrier_output_capture_treated_capture_as_result": True}
                ),
                "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_RESULT",
                set(),
            ),
            (
                "second-carrier output capture treated capture as success",
                lambda request: request.update(
                    {"selected_second_carrier_output_capture_treated_capture_as_success": True}
                ),
                "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_SUCCESS",
                set(),
            ),
            (
                "second-carrier output capture treated capture as external result",
                lambda request: request.update(
                    {
                        "selected_second_carrier_output_capture_treated_capture_as_external_result": True
                    }
                ),
                "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_EXTERNAL_RESULT",
                set(),
            ),
            (
                "second-carrier output capture treated capture as cross-carrier evidence",
                lambda request: request.update(
                    {
                        "selected_second_carrier_output_capture_treated_capture_as_cross_carrier_evidence": True
                    }
                ),
                "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_CROSS_CARRIER_EVIDENCE",
                set(),
            ),
            (
                "second-carrier result treated as success",
                with_non_claim("second_carrier_result_treated_as_success"),
                "SECOND_CARRIER_RESULT_TREATED_AS_SUCCESS",
                {"second_carrier_result_treated_as_success"},
            ),
            (
                "second-carrier result treated as verification",
                with_non_claim("second_carrier_result_treated_as_verification"),
                "SECOND_CARRIER_RESULT_TREATED_AS_VERIFICATION",
                {"second_carrier_result_treated_as_verification"},
            ),
            (
                "second-carrier result treated as external result",
                with_non_claim("second_carrier_result_treated_as_external_result"),
                "SECOND_CARRIER_RESULT_TREATED_AS_EXTERNAL_RESULT",
                {"second_carrier_result_treated_as_external_result"},
            ),
            (
                "second-carrier result treated as cross-carrier evidence",
                with_non_claim("second_carrier_result_treated_as_cross_carrier_evidence"),
                "SECOND_CARRIER_RESULT_TREATED_AS_CROSS_CARRIER_EVIDENCE",
                {"second_carrier_result_treated_as_cross_carrier_evidence"},
            ),
            (
                "second-carrier result treated as source transfer",
                with_non_claim("second_carrier_result_treated_as_source_transfer"),
                "SECOND_CARRIER_RESULT_TREATED_AS_SOURCE_TRANSFER",
                {"second_carrier_result_treated_as_source_transfer"},
            ),
            (
                "second-carrier result treated as source receipt",
                with_non_claim("second_carrier_result_treated_as_source_receipt"),
                "SECOND_CARRIER_RESULT_TREATED_AS_SOURCE_RECEIPT",
                {"second_carrier_result_treated_as_source_receipt"},
            ),
            (
                "second-carrier result treated as reception authorization",
                with_non_claim(
                    "second_carrier_result_treated_as_reception_authorization"
                ),
                "SECOND_CARRIER_RESULT_TREATED_AS_RECEPTION_AUTHORIZATION",
                {"second_carrier_result_treated_as_reception_authorization"},
            ),
            (
                "second-carrier result treated as source",
                with_non_claim("second_carrier_result_treated_as_source"),
                "SECOND_CARRIER_RESULT_TREATED_AS_SOURCE",
                {"second_carrier_result_treated_as_source"},
            ),
            (
                "second-carrier result treated as authority",
                with_non_claim("second_carrier_result_treated_as_authority"),
                "SECOND_CARRIER_RESULT_TREATED_AS_AUTHORITY",
                {"second_carrier_result_treated_as_authority"},
            ),
            (
                "second-carrier result treated as currentness",
                with_non_claim("second_carrier_result_treated_as_currentness"),
                "SECOND_CARRIER_RESULT_TREATED_AS_CURRENTNESS",
                {"second_carrier_result_treated_as_currentness"},
            ),
            (
                "second-carrier result treated as final completion",
                with_non_claim("second_carrier_result_treated_as_final_completion"),
                "SECOND_CARRIER_RESULT_TREATED_AS_FINAL_COMPLETION",
                {"second_carrier_result_treated_as_final_completion"},
            ),
            (
                "second-carrier result treated as runtime",
                with_non_claim("second_carrier_result_treated_as_runtime"),
                "SECOND_CARRIER_RESULT_TREATED_AS_RUNTIME",
                {"second_carrier_result_treated_as_runtime"},
            ),
            (
                "second-carrier result treated as continuation",
                with_non_claim("second_carrier_result_treated_as_continuation"),
                "SECOND_CARRIER_RESULT_TREATED_AS_CONTINUATION",
                {"second_carrier_result_treated_as_continuation"},
            ),
            (
                "second-carrier result treated as reusable permission",
                with_non_claim("second_carrier_result_treated_as_reusable_permission"),
                "SECOND_CARRIER_RESULT_TREATED_AS_REUSABLE_PERMISSION",
                {"second_carrier_result_treated_as_reusable_permission"},
            ),
            (
                "second-carrier result treated as follow-on work",
                with_non_claim("second_carrier_result_treated_as_follow_on_work"),
                "SECOND_CARRIER_RESULT_TREATED_AS_FOLLOW_ON_WORK",
                {"second_carrier_result_treated_as_follow_on_work"},
            ),
            (
                "second-carrier success created",
                with_non_claim("second_carrier_success_created"),
                "SECOND_CARRIER_SUCCESS_CREATED",
                {"second_carrier_success_created"},
            ),
            (
                "external result created",
                with_non_claim("external_result_created"),
                "EXTERNAL_RESULT_CREATED",
                {"external_result_created"},
            ),
            (
                "cross-carrier evidence created",
                with_non_claim("cross_carrier_evidence_created"),
                "CROSS_CARRIER_EVIDENCE_CREATED",
                {"cross_carrier_evidence_created"},
            ),
            (
                "source transfer occurred",
                with_non_claim("source_transfer_occurred"),
                "SOURCE_TRANSFER_OCCURRED",
                {"source_transfer_occurred"},
            ),
            (
                "source receipt occurred",
                with_non_claim("source_receipt_occurred"),
                "SOURCE_RECEIPT_OCCURRED",
                {"source_receipt_occurred"},
            ),
            (
                "reception authorization created",
                with_non_claim("reception_authorization_created"),
                "RECEPTION_AUTHORIZATION_CREATED",
                {"reception_authorization_created"},
            ),
            ("source created", with_non_claim("source_created"), "SOURCE_CREATED", {"source_created"}),
            (
                "authority created",
                with_non_claim("authority_created"),
                "AUTHORITY_CREATED",
                {"authority_created"},
            ),
            (
                "currentness created",
                with_non_claim("currentness_created"),
                "CURRENTNESS_CREATED",
                {"currentness_created"},
            ),
            (
                "final completion claimed",
                with_non_claim("final_completion_claimed"),
                "FINAL_COMPLETION_CLAIMED",
                {"final_completion_claimed"},
            ),
            (
                "runtime hosting created",
                with_non_claim("runtime_hosting_created"),
                "RUNTIME_HOSTING_CREATED",
                {"runtime_hosting_created"},
            ),
            (
                "deployment created",
                with_non_claim("deployment_created"),
                "DEPLOYMENT_CREATED",
                {"deployment_created"},
            ),
            (
                "public release created",
                with_non_claim("public_release_created"),
                "PUBLIC_RELEASE_CREATED",
                {"public_release_created"},
            ),
            (
                "operation permission created",
                with_non_claim("operation_permission_created"),
                "OPERATION_PERMISSION_CREATED",
                {"operation_permission_created"},
            ),
            (
                "continuation authorized",
                with_non_claim("continuation_authorized"),
                "CONTINUATION_AUTHORIZED",
                {"continuation_authorized"},
            ),
            (
                "reusable permission created",
                with_non_claim("reusable_permission_created"),
                "REUSABLE_PERMISSION_CREATED",
                {"reusable_permission_created"},
            ),
            (
                "follow-on work authorized",
                with_non_claim("follow_on_work_authorized"),
                "FOLLOW_ON_WORK_AUTHORIZED",
                {"follow_on_work_authorized"},
            ),
            (
                "receiving carrier treated as authority",
                with_non_claim("receiving_carrier_treated_as_authority"),
                "RECEIVING_CARRIER_TREATED_AS_AUTHORITY",
                {"receiving_carrier_treated_as_authority"},
            ),
            (
                "artifact existence treated as result authority",
                with_non_claim("artifact_existence_treated_as_result_authority"),
                "ARTIFACT_EXISTENCE_TREATED_AS_RESULT_AUTHORITY",
                {"artifact_existence_treated_as_result_authority"},
            ),
            (
                "artifact path treated as currentness",
                with_non_claim("artifact_path_treated_as_currentness"),
                "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
                {"artifact_path_treated_as_currentness"},
            ),
            (
                "repo-local availability treated as result authority",
                with_non_claim("repo_local_availability_treated_as_result_authority"),
                "REPO_LOCAL_AVAILABILITY_TREATED_AS_RESULT_AUTHORITY",
                {"repo_local_availability_treated_as_result_authority"},
            ),
            (
                "hidden repo state used as result content",
                with_non_claim("hidden_repo_state_used_as_result_content"),
                "HIDDEN_REPO_STATE_USED_AS_RESULT_CONTENT",
                {"hidden_repo_state_used_as_result_content"},
            ),
            (
                "hidden repo state used as result authority",
                with_non_claim("hidden_repo_state_used_as_result_authority"),
                "HIDDEN_REPO_STATE_USED_AS_RESULT_AUTHORITY",
                {"hidden_repo_state_used_as_result_authority"},
            ),
            (
                "selected basis not reference-shaped",
                lambda request: request.update({"reference_shaped_input_posture": False}),
                "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
                set(),
            ),
            (
                "raw full prior artifact body returned",
                with_non_claim("raw_full_prior_artifact_body_returned"),
                "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
                {"raw_full_prior_artifact_body_returned"},
            ),
            (
                "predecessor failure evidence repaired",
                with_non_claim("v1_repaired"),
                "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
                {"v1_repaired"},
            ),
            (
                "first result-boundary resolver hidden",
                with_non_claim("first_result_boundary_resolver_hidden"),
                "FIRST_RESULT_BOUNDARY_RESOLVER_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
                {"first_result_boundary_resolver_hidden"},
            ),
            (
                "consumed request reopened",
                with_non_claim("consumed_request_reopened"),
                "CONSUMED_REQUEST_REOPENED",
                {"consumed_request_reopened"},
            ),
            (
                "authorization token reused",
                with_non_claim("authorization_token_reused"),
                "AUTHORIZATION_TOKEN_REUSED",
                {"authorization_token_reused"},
            ),
            (
                "full prior artifact body emitted outside bounded result posture",
                with_non_claim("raw_full_prior_artifact_body_returned"),
                "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
                {"raw_full_prior_artifact_body_returned"},
            ),
            (
                "artifacts mutated",
                with_non_claim("prior_artifacts_mutated"),
                "ARTIFACTS_MUTATED",
                {"prior_artifacts_mutated"},
            ),
            (
                "required non-claim missing",
                lambda request: request["declared_non_claims"].pop(
                    "second_carrier_success_created"
                ),
                "NON_CLAIM_MISSING_OR_FLIPPED",
                set(),
            ),
        ]

        missing_result = resolver.resolve_portable_source_body_verification_second_carrier_result(
            None
        )
        self.assert_blocked_result_is_bounded(
            missing_result, "DECLARED_SECOND_CARRIER_RESULT_REQUEST_MALFORMED"
        )
        non_mapping_result = (
            resolver.resolve_portable_source_body_verification_second_carrier_result(
                ["not", "a", "mapping"]
            )
        )
        self.assert_blocked_result_is_bounded(
            non_mapping_result, "DECLARED_SECOND_CARRIER_RESULT_REQUEST_MALFORMED"
        )

        for name, mutator, expected_code, ignored in cases:
            with self.subTest(name=name):
                request = build_request()
                mutator(request)
                result = (
                    resolver.resolve_portable_source_body_verification_second_carrier_result(
                        request
                    )
                )
                self.assert_blocked_result_is_bounded(result, expected_code, ignored)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            request_path = root / "valid_request.json"
            request = build_request()
            request_path.write_text(json.dumps(request), encoding="utf-8")

            result = resolver.resolve_portable_source_body_verification_second_carrier_result_from_path(
                request_path
            )
            self.assert_recorded_result_is_clean(result)

            malformed_path = root / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            with self.assertRaises(
                resolver.PortableSourceBodyVerificationSecondCarrierResultError
            ):
                resolver.resolve_portable_source_body_verification_second_carrier_result_from_path(
                    malformed_path
                )

            array_path = root / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolver.resolve_portable_source_body_verification_second_carrier_result_from_path(
                array_path
            )
            self.assert_blocked_result_is_bounded(
                array_result, "DECLARED_SECOND_CARRIER_RESULT_REQUEST_MALFORMED"
            )

            with self.assertRaises(
                resolver.PortableSourceBodyVerificationSecondCarrierResultError
            ):
                resolver.resolve_portable_source_body_verification_second_carrier_result_from_path(
                    root / "missing.json"
                )

            output_root = root / "artifacts" / (
                "integrity_host_v0_min_coexistence_portable_source_body_verification_"
                "second_carrier_result"
            )
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_portable_source_body_verification_second_carrier_result_result(
                    result
                )
                second_path = resolver.write_portable_source_body_verification_second_carrier_result_result(
                    result
                )

            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertEqual(first_path.parent, output_root)
            self.assertIn("second_carrier_result_result", first_path.name)
            parsed = json.loads(first_path.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], RECORDED)
            for path in (first_path, second_path):
                text = str(path)
                self.assertIn(
                    "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_result",
                    text,
                )
                self.assertNotIn("actual_second_carrier_live_capture", text)
                self.assertNotIn("second_carrier_result_boundary_v2", text)
                self.assertNotIn("second_carrier_success", text)
                self.assertNotIn("external_result", text)
                self.assertNotIn("cross_carrier", text)
                self.assertNotIn("runtime", text)
                self.assertNotIn("deployment", text)
                self.assertNotIn("public_release", text)

    def test_non_mutation_of_input_request_and_selected_basis(self) -> None:
        request = build_request()
        request["selected_returned_capture_material_basis"]["nested_reference"] = {
            "scope": "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
            "path": "synthetic/reference/path",
        }
        request["second_carrier_result_scope"] = list(SUPPORTED_SCOPE)
        original = copy.deepcopy(request)

        result = resolver.resolve_portable_source_body_verification_second_carrier_result(
            request
        )

        self.assert_recorded_result_is_clean(result)
        self.assertEqual(request, original)
        for key in SELECTED_BASIS_KEYS:
            self.assertEqual(request[key], original[key], key)
        for key in POSTURE_KEYS:
            self.assertEqual(request[key], original[key], key)
        self.assertEqual(
            request["second_carrier_result_scope"],
            original["second_carrier_result_scope"],
        )
        self.assertEqual(request["declared_non_claims"], original["declared_non_claims"])

    def test_predecessor_failure_preservation(self) -> None:
        result = resolver.resolve_portable_source_body_verification_second_carrier_result(
            build_request()
        )
        summary = result["portable_source_body_verification_second_carrier_result_summary"]
        self.assert_recorded_result_is_clean(result)

        self.assertIs(
            result["selected_second_carrier_result_boundary_v2_basis"][
                "first_result_boundary_resolver_preserved"
            ],
            True,
        )
        self.assertIs(
            result["selected_packet_emission_boundary_v1_predecessor_failure_basis"][
                "basis_declared"
            ],
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
        self.assertIs(summary["first_result_boundary_resolver_not_repaired"], True)
        self.assertIs(summary["first_result_boundary_resolver_not_hidden"], True)
        self.assertIs(
            summary["first_result_boundary_resolver_not_claimed_passed"], True
        )
        non_claims = result["non_claims"]
        self.assertIs(non_claims["v1_repaired"], False)
        self.assertIs(non_claims["v1_hidden"], False)
        self.assertIs(non_claims["v1_claimed_passed"], False)
        self.assertIs(non_claims["first_result_boundary_resolver_repaired"], False)
        self.assertIs(non_claims["first_result_boundary_resolver_hidden"], False)
        self.assertIs(non_claims["first_result_boundary_resolver_claimed_passed"], False)


if __name__ == "__main__":
    unittest.main()
