"""Executable checks for second-carrier external-result v2 posture only.

This suite is downstream of the second-carrier-external-result-boundary line.
It verifies that the v2 resolver records one bounded second-carrier external
result posture only, while blocking the predecessor v1 overreach cases:
verification already external result, verification already cross-carrier
evidence, verification already portable verification closure, command report
lineage overreads, and full prior artifact body emission.

The predecessor v1 external-result resolver and test remain preserved
conformance-failure evidence. This suite does not repair, hide, rename, delete,
or claim passed those predecessor surfaces. The tests use synthetic bounded
basis objects and temporary paths only.
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

import resolve_portable_source_body_verification_second_carrier_external_result_v2 as resolver


RECORDED = resolver.OUTCOME_RECORDED
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = set(resolver.OUTCOME_FAMILY)
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_SECOND_CARRIER_EXTERNAL_RESULT_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
TRUE_RECORDED_FIELDS = tuple(resolver.ALLOWED_TRUE_RECORDED_FIELDS)
SELECTED_BASIS_KEYS = tuple(resolver.SELECTED_BASIS_KEYS)
POSTURE_KEYS = tuple(resolver.POSTURE_KEYS)

RAW_SENTINELS = (
    "RAW_SECOND_CARRIER_EXTERNAL_RESULT_BODY_MUST_NOT_RETURN",
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
    "[bounded-external-result-redacted]",
    "[bounded-redacted-raw-or-hidden-state]",
}
OFFICIAL_SCOPE_VALUES = (
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "RETURNED_RESULT_CONTAINMENT_PRESERVED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "FIRST_SUCCESS_BOUNDARY_TEST_FAILURE_PRESERVED",
    "FIRST_RESULT_BOUNDARY_RESOLVER_FAILURE_PRESERVED",
    "STRING_ZERO_NOT_EXTERNAL_RESULT_AS_STANDALONE_INFERENCE",
    "EXTERNAL_RESULT_NOT_CROSS_CARRIER_EVIDENCE",
    "EXTERNAL_RESULT_NOT_PORTABLE_VERIFICATION_CLOSURE",
)

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_second_carrier_external_result_metadata",
    "declared_second_carrier_external_result_question",
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

REPRESENTATIVE_BLOCK_CODES = (
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


def default_request() -> dict[str, Any]:
    return resolver.build_declared_portable_source_body_verification_second_carrier_external_result_request()


def resolve_request(request: dict[str, Any]) -> dict[str, Any]:
    return resolver.resolve_portable_source_body_verification_second_carrier_external_result(request)


def serialized(result: dict[str, Any]) -> str:
    return json.dumps(result, sort_keys=True)


def checks(result: dict[str, Any]) -> list[dict[str, Any]]:
    return list(result.get("second_carrier_external_result_checks", []))


def statement(result: dict[str, Any]) -> dict[str, Any]:
    return dict(result.get("second_carrier_external_result_statement", {}))


def non_claims(result: dict[str, Any]) -> dict[str, Any]:
    return dict(result.get("non_claims", {}))


def scope_values(result: dict[str, Any]) -> list[str]:
    scope = result.get("second_carrier_external_result_scope", {})
    values = scope.get("scope_values", scope.get("declared_scope_values", []))
    return list(values)


def mutate_key(key: str, value: Any) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request[key] = value

    return mutate


def clear_key(key: str) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request[key] = None

    return mutate


def flip_non_claim(key: str) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request["declared_non_claims"][key] = True

    return mutate


def remove_non_claim(key: str) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request["declared_non_claims"].pop(key, None)

    return mutate


def set_basis_flag(
    basis_key: str, flag_key: str, value: Any
) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        basis = request.setdefault(basis_key, {})
        if not isinstance(basis, dict):
            basis = {}
            request[basis_key] = basis
        basis[flag_key] = value

    return mutate


class PortableSourceBodyVerificationSecondCarrierExternalResultV2Test(unittest.TestCase):
    def assert_public_codes(self, result: dict[str, Any]) -> None:
        block = result.get("block")
        if isinstance(block, dict) and block.get("block_code") is not None:
            self.assertIn(block["block_code"], resolver.BLOCK_CODES)
        for check in checks(result):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)
                    self.assertNotIn(code, REDACTION_PLACEHOLDERS)

    def assert_boolean_fields_are_bool(self, result: dict[str, Any]) -> None:
        for key, value in statement(result).items():
            self.assertIs(type(value), bool, key)
        for key, value in non_claims(result).items():
            self.assertIs(type(value), bool, key)

    def assert_no_raw_or_hidden_sentinels(self, result: dict[str, Any]) -> None:
        body = serialized(result)
        for sentinel in RAW_SENTINELS:
            self.assertNotIn(sentinel, body)
        for hostile_value in HOSTILE_VALUES:
            self.assertNotIn(hostile_value, body)

    def assert_official_scope_strings_preserved(self, result: dict[str, Any]) -> None:
        values = scope_values(result)
        for official_value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(official_value, values)
        for value in values:
            self.assertNotIn(value, REDACTION_PLACEHOLDERS)
        self.assertTrue(set(SUPPORTED_SCOPE).issuperset(values))

    def assert_no_forbidden_creation(self, result: dict[str, Any]) -> None:
        claims = non_claims(result)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(claims.get(key), False, key)
        non_meaning = result.get("second_carrier_external_result_non_meaning", {})
        for key, value in non_meaning.items():
            self.assertIs(value, False, key)

    def assert_blocked_result(self, result: dict[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), BLOCKED)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIsNotNone(block.get("block_code"))
        self.assertIn(block.get("block_code"), resolver.BLOCK_CODES)
        self.assert_public_codes(result)
        self.assert_no_forbidden_creation(result)
        self.assert_boolean_fields_are_bool(result)

    def assert_block_code(self, result: dict[str, Any], expected_code: str) -> None:
        self.assert_blocked_result(result)
        self.assertEqual(result["block"]["block_code"], expected_code)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_portable_source_body_verification_second_carrier_external_result",
            "resolve_portable_source_body_verification_second_carrier_external_result_from_path",
            "write_portable_source_body_verification_second_carrier_external_result_result",
            "build_portable_source_body_verification_second_carrier_external_result_summary",
            "build_declared_portable_source_body_verification_second_carrier_external_result_request",
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
            "SUPPORTED_SECOND_CARRIER_EXTERNAL_RESULT_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_portable_source_body_verification_second_carrier_external_result_v2",
        )
        self.assertEqual(
            resolver.SUPPORTED_SECOND_CARRIER_EXTERNAL_RESULT_SCOPE,
            resolver.SUPPORTED_SCOPE_VALUES,
        )
        self.assertTrue(
            resolver.OUTPUT_ROOT.as_posix().endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_portable_source_body_verification_"
                "second_carrier_external_result"
            )
        )

        for official_value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(
                official_value,
                resolver.SUPPORTED_SECOND_CARRIER_EXTERNAL_RESULT_SCOPE,
            )
        for code in REPRESENTATIVE_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES, code)

    def test_successful_recorded_result_from_no_argument_builder(self) -> None:
        request = default_request()
        snapshot = copy.deepcopy(request)
        result = resolve_request(request)
        summary = resolver.build_portable_source_body_verification_second_carrier_external_result_summary(
            result
        )

        self.assertEqual(request, snapshot)
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertIsNone(result["block"])
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertEqual(summary["request_id"], request["second_carrier_external_result_request_id"])

        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result, section)

        recorded_statement = statement(result)
        for key in TRUE_RECORDED_FIELDS:
            self.assertIs(recorded_statement.get(key), True, key)

        claims = non_claims(result)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(claims.get(key), False, key)

        self.assert_public_codes(result)
        self.assert_boolean_fields_are_bool(result)
        self.assert_no_raw_or_hidden_sentinels(result)
        self.assert_official_scope_strings_preserved(result)
        self.assert_no_forbidden_creation(result)

    def test_official_enum_strings_are_preserved_without_redaction_placeholders(self) -> None:
        request = default_request()
        result = resolve_request(request)
        self.assertEqual(result["outcome"], RECORDED)
        self.assert_official_scope_strings_preserved(result)
        self.assert_public_codes(result)

        custom_request = default_request()
        custom_request["second_carrier_external_result_scope"] = list(
            resolver.SUPPORTED_SECOND_CARRIER_EXTERNAL_RESULT_SCOPE
        )
        custom_result = resolve_request(custom_request)
        self.assertEqual(custom_result["outcome"], RECORDED)
        self.assert_official_scope_strings_preserved(custom_result)

    def test_raw_and_hidden_hostile_content_is_contained(self) -> None:
        request = default_request()
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
            "nested": {
                "raw": RAW_SENTINELS[0],
                "items": [RAW_SENTINELS[1], RAW_SENTINELS[2]],
            },
        }
        for basis_key in (
            "selected_second_carrier_external_result_boundary_basis",
            "selected_second_carrier_external_result_boundary_terminal_summary_basis",
            "selected_second_carrier_verification_basis",
            "selected_second_carrier_verification_terminal_summary_basis",
            "selected_second_carrier_success_basis",
            "selected_second_carrier_result_basis",
            "selected_returned_second_carrier_live_capture_intake_basis",
            "selected_returned_capture_material_basis",
            "selected_second_carrier_output_capture_basis",
            "selected_command_report_lineage_basis",
            "selected_artifact_containment_basis",
        ):
            request[basis_key].update(copy.deepcopy(hostile_payload))

        snapshot = copy.deepcopy(request)
        result = resolve_request(request)
        self.assertEqual(request, snapshot)
        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assert_no_raw_or_hidden_sentinels(result)
        self.assert_official_scope_strings_preserved(result)
        self.assert_public_codes(result)
        self.assert_no_forbidden_creation(result)
        self.assert_boolean_fields_are_bool(result)

    def test_v1_missed_overreach_cases_block_with_specific_v2_codes(self) -> None:
        cases: tuple[tuple[str, Callable[[dict[str, Any]], None], str], ...] = (
            (
                "verification already external result",
                mutate_key("selected_second_carrier_verification_already_created_external_result", True),
                "SECOND_CARRIER_VERIFICATION_ALREADY_CREATED_EXTERNAL_RESULT",
            ),
            (
                "verification already cross carrier",
                mutate_key("selected_second_carrier_verification_already_created_cross_carrier_evidence", True),
                "SECOND_CARRIER_VERIFICATION_ALREADY_CREATED_CROSS_CARRIER_EVIDENCE",
            ),
            (
                "verification already closure",
                mutate_key("selected_second_carrier_verification_already_created_portable_verification_closure", True),
                "SECOND_CARRIER_VERIFICATION_ALREADY_CREATED_PORTABLE_VERIFICATION_CLOSURE",
            ),
            (
                "command lineage current report",
                mutate_key("selected_command_report_lineage_treated_as_current_report_artifact", True),
                "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENT_REPORT_ARTIFACT",
            ),
            (
                "command lineage source",
                mutate_key("selected_command_report_lineage_treated_as_source", True),
                "COMMAND_REPORT_LINEAGE_TREATED_AS_SOURCE",
            ),
            (
                "command lineage authority",
                mutate_key("selected_command_report_lineage_treated_as_authority", True),
                "COMMAND_REPORT_LINEAGE_TREATED_AS_AUTHORITY",
            ),
            (
                "command lineage currentness",
                mutate_key("selected_command_report_lineage_treated_as_currentness", True),
                "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENTNESS",
            ),
            (
                "full prior body emitted",
                mutate_key("full_prior_artifact_body_emitted_outside_bounded_external_result", True),
                "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_EXTERNAL_RESULT",
            ),
            (
                "nested verification already external result",
                set_basis_flag("selected_second_carrier_verification_basis", "already_created_external_result", True),
                "SECOND_CARRIER_VERIFICATION_ALREADY_CREATED_EXTERNAL_RESULT",
            ),
            (
                "nested command lineage authority",
                set_basis_flag("selected_command_report_lineage_basis", "treated_as_authority", True),
                "COMMAND_REPORT_LINEAGE_TREATED_AS_AUTHORITY",
            ),
            (
                "nested full prior body emitted",
                set_basis_flag(
                    "selected_artifact_containment_basis",
                    "full_prior_artifact_body_emitted_outside_bounded_external_result",
                    True,
                ),
                "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_EXTERNAL_RESULT",
            ),
        )
        for name, mutator, expected_code in cases:
            with self.subTest(name=name):
                request = default_request()
                mutator(request)
                result = resolve_request(request)
                self.assert_block_code(result, expected_code)

    def test_representative_blocking_behavior(self) -> None:
        block_cases: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
            ("missing question", mutate_key("second_carrier_external_result_question", "")),
            ("explicit block intent", mutate_key("second_carrier_external_result_intent", "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT")),
            ("unsupported intent", mutate_key("second_carrier_external_result_intent", "UNSUPPORTED_INTENT")),
            ("unsupported scope", lambda request: request["second_carrier_external_result_scope"].append("UNSUPPORTED_SCOPE")),
            ("missing boundary basis", clear_key("selected_second_carrier_external_result_boundary_basis")),
            ("boundary not recorded", mutate_key("selected_second_carrier_external_result_boundary_result_outcome", "NOT_RECORDED")),
            ("boundary failed checks", mutate_key("selected_second_carrier_external_result_boundary_failed_check_count", 1)),
            ("boundary version wrong", mutate_key("selected_second_carrier_external_result_boundary_result_version", "9.9.9")),
            ("boundary no future step", mutate_key("selected_second_carrier_external_result_boundary_declared_future_external_result_step", False)),
            ("boundary already external result", mutate_key("selected_second_carrier_external_result_boundary_already_created_external_result", True)),
            ("boundary already cross carrier", mutate_key("selected_second_carrier_external_result_boundary_already_created_cross_carrier_evidence", True)),
            ("boundary already closure", mutate_key("selected_second_carrier_external_result_boundary_already_created_portable_verification_closure", True)),
            ("boundary treated as external result", mutate_key("selected_second_carrier_external_result_boundary_treated_external_result_boundary_as_external_result", True)),
            ("boundary treated as cross carrier", mutate_key("selected_second_carrier_external_result_boundary_treated_external_result_boundary_as_cross_carrier_evidence", True)),
            ("boundary treated as closure", mutate_key("selected_second_carrier_external_result_boundary_treated_external_result_boundary_as_portable_verification_closure", True)),
            ("boundary treated zero exit as external", mutate_key("selected_second_carrier_external_result_boundary_zero_exit_code_not_external_result", False)),
            ("boundary treated string zero as external", mutate_key("selected_second_carrier_external_result_boundary_string_zero_not_external_result", False)),
            ("boundary treated ok as external", mutate_key("selected_second_carrier_external_result_boundary_ok_not_external_result", False)),
            ("boundary treated ran seven as proof", mutate_key("selected_second_carrier_external_result_boundary_ran_7_tests_not_cross_carrier_proof", False)),
            ("boundary redacted official strings", mutate_key("selected_second_carrier_external_result_boundary_official_enum_scope_strings_redacted", True)),
            ("verification basis missing", clear_key("selected_second_carrier_verification_basis")),
            ("verification not recorded", mutate_key("selected_second_carrier_verification_result_outcome", "NOT_RECORDED")),
            ("verification failed checks", mutate_key("selected_second_carrier_verification_failed_check_count", 1)),
            ("verification already external result", mutate_key("selected_second_carrier_verification_already_created_external_result", True)),
            ("verification already cross carrier", mutate_key("selected_second_carrier_verification_already_created_cross_carrier_evidence", True)),
            ("verification already closure", mutate_key("selected_second_carrier_verification_already_created_portable_verification_closure", True)),
            ("verification treated verification as external", mutate_key("selected_second_carrier_verification_treated_verification_as_external_result", True)),
            ("verification treated verification as cross carrier", mutate_key("selected_second_carrier_verification_treated_verification_as_cross_carrier_evidence", True)),
            ("verification treated zero as external", mutate_key("selected_second_carrier_verification_zero_exit_code_not_external_result", False)),
            ("verification treated string zero as external", mutate_key("selected_second_carrier_verification_string_zero_not_external_result", False)),
            ("verification treated ok as external", mutate_key("selected_second_carrier_verification_ok_not_external_result", False)),
            ("verification treated ran seven as proof", mutate_key("selected_second_carrier_verification_ran_7_tests_not_cross_carrier_proof", False)),
            ("success basis missing", clear_key("selected_second_carrier_success_basis")),
            ("success not recorded", mutate_key("selected_second_carrier_success_result_outcome", "NOT_RECORDED")),
            ("success failed checks", mutate_key("selected_second_carrier_success_failed_check_count", 1)),
            ("result basis missing", clear_key("selected_second_carrier_result_basis")),
            ("result not recorded", mutate_key("selected_second_carrier_result_result_outcome", "NOT_RECORDED")),
            ("result failed checks", mutate_key("selected_second_carrier_result_failed_check_count", 1)),
            ("returned capture intake missing", clear_key("selected_returned_second_carrier_live_capture_intake_basis")),
            ("returned capture intake not preserved", mutate_key("selected_returned_capture_intake_preserved", False)),
            ("returned capture treated as external result", mutate_key("returned_capture_treated_as_external_result", True)),
            ("returned capture treated as proof", mutate_key("returned_capture_treated_as_cross_carrier_proof", True)),
            ("zero exit treated as external", mutate_key("zero_exit_code_treated_as_external_result", True)),
            ("string zero treated as external", mutate_key("string_zero_treated_as_external_result", True)),
            ("ok treated as external", mutate_key("ok_output_treated_as_external_result", True)),
            ("ran seven treated as proof", mutate_key("ran_7_tests_treated_as_cross_carrier_proof", True)),
            ("placeholder fields repaired", mutate_key("selected_returned_capture_placeholder_fields_unrepaired", False)),
            ("returned capture material missing", clear_key("selected_returned_capture_material_basis")),
            ("returned zip missing", mutate_key("selected_returned_capture_zip_path", "")),
            ("returned hash missing", mutate_key("selected_returned_capture_hash_path", "")),
            ("returned extracted missing", mutate_key("selected_returned_capture_extracted_directory_path", "")),
            ("returned combined log missing", mutate_key("selected_returned_capture_combined_terminal_log_path", "")),
            ("returned exit code missing", mutate_key("selected_returned_capture_exit_code", None)),
            ("returned command text missing", mutate_key("selected_returned_capture_command_text", "")),
            ("returned timestamps missing", mutate_key("selected_returned_capture_started_at", "")),
            ("output capture basis missing", clear_key("selected_second_carrier_output_capture_basis")),
            ("output capture not recorded", mutate_key("selected_second_carrier_output_capture_result_outcome", "NOT_RECORDED")),
            ("output capture failed checks", mutate_key("selected_second_carrier_output_capture_failed_check_count", 1)),
            ("external result treated as cross carrier", flip_non_claim("second_carrier_external_result_treated_as_cross_carrier_evidence")),
            ("external result treated as closure", flip_non_claim("second_carrier_external_result_treated_as_portable_verification_closure")),
            ("external result treated as transfer", flip_non_claim("second_carrier_external_result_treated_as_source_transfer")),
            ("external result treated as receipt", flip_non_claim("second_carrier_external_result_treated_as_source_receipt")),
            ("external result treated as reception", flip_non_claim("second_carrier_external_result_treated_as_reception_authorization")),
            ("external result treated as source", flip_non_claim("second_carrier_external_result_treated_as_source")),
            ("external result treated as authority", flip_non_claim("second_carrier_external_result_treated_as_authority")),
            ("external result treated as currentness", flip_non_claim("second_carrier_external_result_treated_as_currentness")),
            ("external result treated as final completion", flip_non_claim("second_carrier_external_result_treated_as_final_completion")),
            ("external result treated as runtime", flip_non_claim("second_carrier_external_result_treated_as_runtime")),
            ("external result treated as continuation", flip_non_claim("second_carrier_external_result_treated_as_continuation")),
            ("external result treated as reusable", flip_non_claim("second_carrier_external_result_treated_as_reusable_permission")),
            ("external result treated as follow-on", flip_non_claim("second_carrier_external_result_treated_as_follow_on_work")),
            ("cross carrier evidence created", flip_non_claim("cross_carrier_evidence_created")),
            ("portable closure created", flip_non_claim("portable_verification_closure_created")),
            ("source transfer occurred", flip_non_claim("source_transfer_occurred")),
            ("source receipt occurred", flip_non_claim("source_receipt_occurred")),
            ("reception authorization created", flip_non_claim("reception_authorization_created")),
            ("source created", flip_non_claim("source_created")),
            ("authority created", flip_non_claim("authority_created")),
            ("currentness created", flip_non_claim("currentness_created")),
            ("final completion claimed", flip_non_claim("final_completion_claimed")),
            ("runtime created", flip_non_claim("runtime_hosting_created")),
            ("deployment created", flip_non_claim("deployment_created")),
            ("public release created", flip_non_claim("public_release_created")),
            ("operation permission created", flip_non_claim("operation_permission_created")),
            ("continuation authorized", flip_non_claim("continuation_authorized")),
            ("reusable permission created", flip_non_claim("reusable_permission_created")),
            ("derivative reception authorized", flip_non_claim("derivative_reception_authorized")),
            ("vessel relation authorized", flip_non_claim("vessel_relation_authorized")),
            ("another reception request authorized", flip_non_claim("another_reception_request_authorized")),
            ("follow-on authorized", flip_non_claim("follow_on_work_authorized")),
            ("receiving carrier authority", flip_non_claim("receiving_carrier_treated_as_authority")),
            ("artifact existence authority", flip_non_claim("artifact_existence_treated_as_external_result_authority")),
            ("artifact path currentness", flip_non_claim("artifact_path_treated_as_currentness")),
            ("repo local authority", flip_non_claim("repo_local_availability_treated_as_external_result_authority")),
            ("hidden repo content", flip_non_claim("hidden_repo_state_used_as_external_result_content")),
            ("hidden repo authority", flip_non_claim("hidden_repo_state_used_as_external_result_authority")),
            ("selected basis not reference-shaped", mutate_key("reference_shaped_input_posture", False)),
            ("raw full prior artifact body returned", flip_non_claim("raw_full_prior_artifact_body_returned")),
            ("predecessor failure hidden", mutate_key("predecessor_failure_evidence_hidden_or_repaired", True)),
            ("first success boundary repaired", flip_non_claim("first_success_boundary_test_repaired")),
            ("first success boundary hidden", flip_non_claim("first_success_boundary_test_hidden")),
            ("first success boundary claimed passed", flip_non_claim("first_success_boundary_test_claimed_passed")),
            ("first result boundary repaired", flip_non_claim("first_result_boundary_resolver_repaired")),
            ("first result boundary hidden", flip_non_claim("first_result_boundary_resolver_hidden")),
            ("first result boundary claimed passed", flip_non_claim("first_result_boundary_resolver_claimed_passed")),
            ("v1 repaired", flip_non_claim("v1_repaired")),
            ("v1 hidden", flip_non_claim("v1_hidden")),
            ("v1 claimed passed", flip_non_claim("v1_claimed_passed")),
            ("command lineage current report", mutate_key("selected_command_report_lineage_treated_as_current_report_artifact", True)),
            ("command lineage source", mutate_key("selected_command_report_lineage_treated_as_source", True)),
            ("command lineage authority", mutate_key("selected_command_report_lineage_treated_as_authority", True)),
            ("command lineage currentness", mutate_key("selected_command_report_lineage_treated_as_currentness", True)),
            ("consumed request reopened", flip_non_claim("consumed_request_reopened")),
            ("authorization reused", flip_non_claim("authorization_token_reused")),
            ("full prior body emitted", mutate_key("full_prior_artifact_body_emitted_outside_bounded_external_result", True)),
            ("string zero doctrine", flip_non_claim("string_zero_representation_turned_into_doctrine")),
            ("artifacts mutated", mutate_key("artifacts_mutated", True)),
            ("returned capture material mutated", mutate_key("returned_capture_material_mutated", True)),
            ("required non-claim missing", remove_non_claim("cross_carrier_evidence_created")),
        )

        missing_result = resolver.resolve_portable_source_body_verification_second_carrier_external_result()
        self.assert_blocked_result(missing_result)
        non_mapping_result = resolver.resolve_portable_source_body_verification_second_carrier_external_result(
            ["not", "a", "mapping"]  # type: ignore[arg-type]
        )
        self.assert_blocked_result(non_mapping_result)

        for name, mutator in block_cases:
            with self.subTest(name=name):
                request = default_request()
                mutator(request)
                result = resolve_request(request)
                self.assert_blocked_result(result)

    def test_path_and_write_behavior(self) -> None:
        request = default_request()
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            request_path = temp_root / "request.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")

            result = resolver.resolve_portable_source_body_verification_second_carrier_external_result_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], RECORDED)
            summary = result["portable_source_body_verification_second_carrier_external_result_summary"]
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)

            malformed_path = temp_root / "malformed.json"
            malformed_path.write_text("{not valid json", encoding="utf-8")
            with self.assertRaises(
                resolver.PortableSourceBodyVerificationSecondCarrierExternalResultError
            ):
                resolver.resolve_portable_source_body_verification_second_carrier_external_result_from_path(
                    malformed_path
                )

            array_path = temp_root / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolver.resolve_portable_source_body_verification_second_carrier_external_result_from_path(
                array_path
            )
            self.assert_blocked_result(array_result)

            with self.assertRaises(
                resolver.PortableSourceBodyVerificationSecondCarrierExternalResultError
            ):
                resolver.resolve_portable_source_body_verification_second_carrier_external_result_from_path(
                    temp_root / "missing.json"
                )

            output_root = (
                temp_root
                / "artifacts"
                / "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_external_result"
            )
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_portable_source_body_verification_second_carrier_external_result_result(
                    result
                )
                second_path = resolver.write_portable_source_body_verification_second_carrier_external_result_result(
                    result
                )

            self.assertTrue(first_path.parent.exists())
            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertEqual(first_path.parent, output_root)
            self.assertEqual(second_path.parent, output_root)
            self.assertEqual(json.loads(first_path.read_text(encoding="utf-8"))["outcome"], RECORDED)
            self.assertIn(
                "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_external_result",
                first_path.as_posix(),
            )
            for forbidden in (
                "actual_second_carrier_live_capture",
                "second_carrier_external_result_boundary",
                "second_carrier_verification/",
                "second_carrier_success/",
                "second_carrier_result/",
                "cross_carrier",
                "portable_verification_closure",
                "runtime",
                "deployment",
                "public_release",
            ):
                self.assertNotIn(forbidden, first_path.as_posix())
                self.assertNotIn(forbidden, second_path.as_posix())

    def test_non_mutation_of_request_and_selected_inputs(self) -> None:
        request = default_request()
        request["second_carrier_external_result_scope"] = {
            "scope_values": list(resolver.SUPPORTED_SECOND_CARRIER_EXTERNAL_RESULT_SCOPE)
        }
        for key in SELECTED_BASIS_KEYS:
            request[key]["non_mutation_marker"] = {"nested": [key, "preserve"]}
        for key in POSTURE_KEYS:
            request[key] = {"declared": True, "non_mutation_marker": [key, "preserve"]}
        request["declared_non_claims"]["non_mutation_marker"] = False
        snapshot = copy.deepcopy(request)

        result = resolve_request(request)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(request, snapshot)

    def test_predecessor_failure_preservation(self) -> None:
        request = default_request()
        result = resolve_request(request)
        summary = resolver.build_portable_source_body_verification_second_carrier_external_result_summary(
            result
        )
        recorded_statement = statement(result)
        claims = non_claims(result)

        self.assertIs(recorded_statement["first_success_boundary_test_failure_preserved"], True)
        self.assertIs(recorded_statement["first_result_boundary_resolver_failure_preserved"], True)
        self.assertIs(claims["first_success_boundary_test_repaired"], False)
        self.assertIs(claims["first_success_boundary_test_hidden"], False)
        self.assertIs(claims["first_success_boundary_test_claimed_passed"], False)
        self.assertIs(claims["v1_repaired"], False)
        self.assertIs(claims["v1_hidden"], False)
        self.assertIs(claims["v1_claimed_passed"], False)
        self.assertIs(claims["first_result_boundary_resolver_repaired"], False)
        self.assertIs(claims["first_result_boundary_resolver_hidden"], False)
        self.assertIs(claims["first_result_boundary_resolver_claimed_passed"], False)

        predecessor_basis = result["selected_predecessor_failure_basis"]
        self.assertIs(predecessor_basis["first_success_boundary_test_failure_preserved"], True)
        self.assertIs(predecessor_basis["first_result_boundary_resolver_failure_preserved"], True)
        self.assertIs(predecessor_basis["v1_packet_emission_boundary_failure_preserved"], True)

        self.assertIs(summary["first_success_boundary_test_failure_preserved"], True)
        self.assertIs(summary["v1_predecessor_failure_preserved"], True)
        self.assertIs(summary["v1_not_repaired_hidden_or_claimed_passed"], True)
        self.assertIs(summary["first_result_boundary_resolver_failure_preserved"], True)
        self.assertIs(summary["v1_repaired"], False)
        self.assertIs(summary["v1_hidden"], False)
        self.assertIs(summary["v1_claimed_passed"], False)


if __name__ == "__main__":
    unittest.main()
