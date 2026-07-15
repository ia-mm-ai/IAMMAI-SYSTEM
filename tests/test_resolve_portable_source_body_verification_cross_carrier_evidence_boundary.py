"""Executable checks for cross-carrier-evidence-boundary posture only.

This suite is downstream of the second-carrier external-result line. It
verifies that the cross-carrier evidence boundary resolver records one future
cross-carrier evidence review step only, while preserving that cross-carrier
evidence, portable verification closure, source transfer, source receipt,
reception authorization, source, authority, currentness, runtime, final
completion, continuation, reusable permission, and follow-on work are not
created.

The predecessor external-result v1 resolver/test, first success-boundary test,
first result-boundary resolver, and v1 packet-emission-boundary resolver/test
remain preserved failure evidence. This suite does not repair, hide, rename,
delete, or claim passed those predecessor surfaces.
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

import resolve_portable_source_body_verification_cross_carrier_evidence_boundary as resolver


RECORDED = resolver.OUTCOME_RECORDED
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = set(resolver.OUTCOME_FAMILY)
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_CROSS_CARRIER_EVIDENCE_BOUNDARY_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
TRUE_RECORDED_FIELDS = tuple(resolver.ALLOWED_TRUE_RECORDED_FIELDS)
SELECTED_BASIS_FIELDS = tuple(resolver.SELECTED_BASIS_FIELDS)
POSTURE_SECTIONS = tuple(resolver.POSTURE_SECTIONS)

RAW_SENTINELS = (
    "RAW_CROSS_CARRIER_EVIDENCE_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)
HOSTILE_VALUES = (
    "hostile-cross-carrier-boundary-raw-body-value",
    "hostile-cross-carrier-boundary-raw-full-body-value",
    "hostile-cross-carrier-boundary-full-body-value",
    "hostile-cross-carrier-boundary-artifact-body-value",
    "hostile-cross-carrier-boundary-raw-result-body-value",
    "hostile-cross-carrier-boundary-raw-output-body-value",
    "hostile-cross-carrier-boundary-raw-capture-body-value",
    "hostile-cross-carrier-boundary-raw-success-body-value",
    "hostile-cross-carrier-boundary-raw-verification-body-value",
    "hostile-cross-carrier-boundary-raw-external-result-body-value",
    "hostile-cross-carrier-boundary-raw-cross-carrier-evidence-body-value",
    "hostile-cross-carrier-boundary-capture-body-value",
    "hostile-cross-carrier-boundary-cross-carrier-evidence-body-value",
    "hostile-cross-carrier-boundary-portable-verification-closure-body-value",
    "hostile-cross-carrier-boundary-source-body-value",
    "hostile-cross-carrier-boundary-authority-body-value",
    "hostile-cross-carrier-boundary-current-working-tree-value",
    "hostile-cross-carrier-boundary-local-cache-value",
    "hostile-cross-carrier-boundary-repo-local-only-dependency-value",
)
REDACTION_PLACEHOLDERS = {
    "[bounded-cross-carrier-evidence-boundary-redacted]",
    "[bounded-redacted-raw-or-hidden-state]",
}
OFFICIAL_SCOPE_VALUES = (
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "RETURNED_RESULT_CONTAINMENT_PRESERVED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "PREDECESSOR_EXTERNAL_RESULT_V1_FAILURE_PRESERVED",
    "FIRST_SUCCESS_BOUNDARY_TEST_FAILURE_PRESERVED",
    "FIRST_RESULT_BOUNDARY_RESOLVER_FAILURE_PRESERVED",
    "STRING_ZERO_NOT_CROSS_CARRIER_EVIDENCE",
    "CROSS_CARRIER_EVIDENCE_NOT_CREATED",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_NOT_CROSS_CARRIER_EVIDENCE",
)

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_cross_carrier_evidence_boundary_metadata",
    "declared_cross_carrier_evidence_boundary_question",
    "selected_second_carrier_external_result_basis",
    "selected_second_carrier_external_result_terminal_summary_basis",
    "selected_second_carrier_external_result_boundary_basis",
    "selected_second_carrier_external_result_boundary_terminal_summary_basis",
    "selected_second_carrier_verification_basis",
    "selected_second_carrier_verification_terminal_summary_basis",
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
    "cross_carrier_evidence_boundary_only_posture",
    "one_future_cross_carrier_evidence_review_step_posture",
    "second_carrier_external_result_basis_preserved_posture",
    "external_result_artifact_basis_preserved_posture",
    "second_carrier_external_result_boundary_basis_preserved_posture",
    "second_carrier_verification_basis_preserved_posture",
    "returned_second_carrier_capture_basis_preserved_posture",
    "capture_intake_basis_preserved_posture",
    "second_carrier_output_capture_basis_preserved_posture",
    "cross_carrier_evidence_not_created_posture",
    "cross_carrier_evidence_boundary_not_cross_carrier_evidence_posture",
    "external_result_not_cross_carrier_evidence_posture",
    "zero_exit_code_not_cross_carrier_evidence_posture",
    "string_zero_not_cross_carrier_evidence_posture",
    "ok_output_not_cross_carrier_evidence_posture",
    "ran_7_tests_not_cross_carrier_evidence_posture",
    "returned_capture_not_cross_carrier_evidence_posture",
    "portable_verification_closure_not_created_posture",
    "cross_carrier_evidence_not_source_transfer_posture",
    "cross_carrier_evidence_not_source_receipt_posture",
    "cross_carrier_evidence_not_reception_authorization_posture",
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
    "repo_local_availability_not_cross_carrier_evidence_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_external_result_v1_failure_preserved_posture",
    "first_success_boundary_test_failure_preserved_posture",
    "first_result_boundary_resolver_failure_preserved_posture",
    "cross_carrier_evidence_boundary_scope",
    "cross_carrier_evidence_boundary_checks",
    "cross_carrier_evidence_boundary_statement",
    "cross_carrier_evidence_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_cross_carrier_evidence_boundary_summary",
)

REPRESENTATIVE_BLOCK_CODES = (
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_QUESTION_UNDECLARED",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_INTENT_UNSUPPORTED",
    "SECOND_CARRIER_EXTERNAL_RESULT_BASIS_MISSING",
    "SECOND_CARRIER_EXTERNAL_RESULT_NOT_RECORDED",
    "SECOND_CARRIER_EXTERNAL_RESULT_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_EXTERNAL_RESULT_VERSION_NOT_0_1_0",
    "SECOND_CARRIER_EXTERNAL_RESULT_DID_NOT_RECORD_BOUNDED_EXTERNAL_RESULT",
    "SECOND_CARRIER_EXTERNAL_RESULT_ALREADY_CREATED_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXTERNAL_RESULT_ALREADY_CREATED_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_EXTERNAL_RESULT_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_EXTERNAL_RESULT_AS_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_ZERO_EXIT_CODE_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_STRING_ZERO_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_STRING_ZERO_AS_DOCTRINE",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_OK_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_RAN_7_TESTS_AS_CROSS_CARRIER_PROOF",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_RETURNED_CAPTURE_AS_CROSS_CARRIER_PROOF",
    "SECOND_CARRIER_EXTERNAL_RESULT_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
    "PREDECESSOR_EXTERNAL_RESULT_V1_FAILURE_MISSING_OR_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_BASIS_MISSING",
    "SECOND_CARRIER_VERIFICATION_BASIS_MISSING",
    "SECOND_CARRIER_VERIFICATION_NOT_RECORDED",
    "SECOND_CARRIER_SUCCESS_BASIS_MISSING",
    "SECOND_CARRIER_SUCCESS_NOT_RECORDED",
    "SECOND_CARRIER_RESULT_BASIS_MISSING",
    "SECOND_CARRIER_RESULT_NOT_RECORDED",
    "RETURNED_CAPTURE_INTAKE_BASIS_MISSING",
    "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
    "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "ZERO_EXIT_CODE_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "STRING_ZERO_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "STRING_ZERO_REPRESENTATION_TURNED_INTO_DOCTRINE",
    "OK_OUTPUT_TREATED_AS_CROSS_CARRIER_EVIDENCE",
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
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_SOURCE",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_AUTHORITY",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_CURRENTNESS",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_FINAL_COMPLETION",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_RUNTIME",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_CROSS_CARRIER_EVIDENCE_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_CROSS_CARRIER_EVIDENCE_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_CROSS_CARRIER_EVIDENCE_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_CROSS_CARRIER_EVIDENCE_AUTHORITY",
    "FIRST_SUCCESS_BOUNDARY_TEST_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    "FIRST_RESULT_BOUNDARY_RESOLVER_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENT_REPORT_ARTIFACT",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_SOURCE",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_AUTHORITY",
    "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENTNESS",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_CROSS_CARRIER_EVIDENCE_BOUNDARY",
    "ARTIFACTS_MUTATED",
    "RETURNED_CAPTURE_MATERIAL_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_CROSS_CARRIER_EVIDENCE_BOUNDARY_SCOPE",
)


def default_request() -> dict[str, Any]:
    return resolver.build_declared_portable_source_body_verification_cross_carrier_evidence_boundary_request()


def resolve_request(request: dict[str, Any]) -> dict[str, Any]:
    return resolver.resolve_portable_source_body_verification_cross_carrier_evidence_boundary(request)


def serialized(result: dict[str, Any]) -> str:
    return json.dumps(result, sort_keys=True)


def checks(result: dict[str, Any]) -> list[dict[str, Any]]:
    return list(result.get("cross_carrier_evidence_boundary_checks", []))


def statement(result: dict[str, Any]) -> dict[str, Any]:
    return dict(result.get("cross_carrier_evidence_boundary_statement", {}))


def non_claims(result: dict[str, Any]) -> dict[str, Any]:
    return dict(result.get("non_claims", {}))


def scope_values(result: dict[str, Any]) -> list[str]:
    return list(result.get("cross_carrier_evidence_boundary_scope", []))


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
        request[key] = True

    return mutate


def remove_non_claim(key: str) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request["declared_non_claims"].pop(key, None)

    return mutate


def mutate_many(**updates: Any) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request.update(updates)

    return mutate


class PortableSourceBodyVerificationCrossCarrierEvidenceBoundaryTest(unittest.TestCase):
    def assert_public_codes(self, result: dict[str, Any]) -> None:
        block = result.get("block")
        if isinstance(block, dict) and block.get("block_code") is not None:
            self.assertIn(block["block_code"], resolver.BLOCK_CODES)
            self.assertNotIn(block["block_code"], REDACTION_PLACEHOLDERS)
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
        for key in TRUE_RECORDED_FIELDS:
            value = statement(result).get(key)
            if result.get("outcome") == BLOCKED:
                self.assertIs(value, False, key)
            else:
                self.assertIs(type(value), bool, key)

    def assert_blocked_result(self, result: dict[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), BLOCKED)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIsNotNone(block.get("block_code"))
        self.assertIn(block.get("block_code"), resolver.BLOCK_CODES)
        self.assert_public_codes(result)
        self.assert_no_forbidden_creation(result)
        self.assert_boolean_fields_are_bool(result)

    def assert_path_blocks_or_raises(self, func: Callable[[], dict[str, Any]]) -> None:
        try:
            result = func()
        except resolver.PortableSourceBodyVerificationCrossCarrierEvidenceBoundaryError:
            return
        self.assert_blocked_result(result)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_portable_source_body_verification_cross_carrier_evidence_boundary",
            "resolve_portable_source_body_verification_cross_carrier_evidence_boundary_from_path",
            "write_portable_source_body_verification_cross_carrier_evidence_boundary_result",
            "build_portable_source_body_verification_cross_carrier_evidence_boundary_summary",
            "build_declared_portable_source_body_verification_cross_carrier_evidence_boundary_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)), name)

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_SCOPE_VALUES",
            "SUPPORTED_CROSS_CARRIER_EVIDENCE_BOUNDARY_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_portable_source_body_verification_cross_carrier_evidence_boundary",
        )
        self.assertEqual(
            resolver.SUPPORTED_CROSS_CARRIER_EVIDENCE_BOUNDARY_SCOPE,
            resolver.SUPPORTED_SCOPE_VALUES,
        )
        self.assertTrue(
            resolver.OUTPUT_ROOT.as_posix().endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_portable_source_body_verification_"
                "cross_carrier_evidence_boundary"
            )
        )

        for official_value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(
                official_value,
                resolver.SUPPORTED_CROSS_CARRIER_EVIDENCE_BOUNDARY_SCOPE,
            )
        for code in REPRESENTATIVE_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES, code)

    def test_successful_recorded_result_from_no_argument_builder(self) -> None:
        request = default_request()
        snapshot = copy.deepcopy(request)
        result = resolve_request(request)
        summary = resolver.build_portable_source_body_verification_cross_carrier_evidence_boundary_summary(
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
        self.assertEqual(
            summary["request_id"],
            request["cross_carrier_evidence_boundary_request_id"],
        )

        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result, section)
        for section in SELECTED_BASIS_FIELDS:
            selected = result[section]
            self.assertIs(selected["selected_basis_reference_shape_preserved"], True)
            self.assertIs(selected["raw_full_prior_artifact_body_returned"], False)
            self.assertIs(selected["hidden_repo_state_used_as_authority"], False)
        self.assertIs(
            result["selected_second_carrier_external_result_terminal_summary_basis"][
                "basis_declared"
            ],
            True,
        )

        selected_external = result["selected_second_carrier_external_result_basis"]
        shortcuts = selected_external["selected_shortcuts"]
        self.assertEqual(
            shortcuts["selected_second_carrier_external_result_result_outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXTERNAL_RESULT_RECORDED",
        )
        self.assertEqual(
            shortcuts["selected_second_carrier_external_result_result_version"],
            "0.1.0",
        )
        self.assertEqual(
            shortcuts["selected_second_carrier_external_result_failed_check_count"],
            0,
        )

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
        custom_request["cross_carrier_evidence_boundary_scope"] = list(
            resolver.SUPPORTED_CROSS_CARRIER_EVIDENCE_BOUNDARY_SCOPE
        )
        custom_result = resolve_request(custom_request)
        self.assertEqual(custom_result["outcome"], RECORDED)
        self.assert_official_scope_strings_preserved(custom_result)
        self.assertEqual(set(scope_values(custom_result)), set(SUPPORTED_SCOPE))

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
            "raw_cross_carrier_evidence_body": HOSTILE_VALUES[10],
            "capture_body": HOSTILE_VALUES[11],
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
                "official_scope": "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
            },
        }
        for basis_key in (
            "selected_second_carrier_external_result_basis",
            "selected_second_carrier_external_result_terminal_summary_basis",
            "selected_second_carrier_external_result_boundary_basis",
            "selected_second_carrier_external_result_boundary_terminal_summary_basis",
            "selected_second_carrier_verification_basis",
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

    def test_representative_blocking_behavior(self) -> None:
        block_cases: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
            ("missing question", mutate_key("cross_carrier_evidence_boundary_question", "")),
            ("explicit block intent", mutate_key("cross_carrier_evidence_boundary_intent", "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_CROSS_CARRIER_EVIDENCE_BOUNDARY")),
            ("unsupported intent", mutate_key("cross_carrier_evidence_boundary_intent", "UNSUPPORTED_INTENT")),
            ("unsupported scope", lambda request: request["cross_carrier_evidence_boundary_scope"].append("UNSUPPORTED_SCOPE")),
            ("missing second carrier external result basis", clear_key("selected_second_carrier_external_result_basis")),
            ("external result not recorded", mutate_key("selected_second_carrier_external_result_result_outcome", "NOT_RECORDED")),
            ("external result failed checks", mutate_key("selected_second_carrier_external_result_failed_check_count", 1)),
            ("external result version wrong", mutate_key("selected_second_carrier_external_result_result_version", "9.9.9")),
            ("external result did not record bounded", mutate_key("selected_second_carrier_external_result_bounded_external_result_recorded", False)),
            ("external result already cross carrier", mutate_key("selected_second_carrier_external_result_already_created_cross_carrier_evidence", True)),
            ("external result already closure", mutate_key("selected_second_carrier_external_result_already_created_portable_verification_closure", True)),
            ("external result treated as cross carrier", mutate_key("selected_second_carrier_external_result_treated_external_result_as_cross_carrier_evidence", True)),
            ("external result treated as closure", mutate_key("selected_second_carrier_external_result_treated_external_result_as_portable_verification_closure", True)),
            ("zero exit treated as cross carrier", mutate_key("zero_exit_code_treated_as_cross_carrier_evidence", True)),
            ("string zero treated as cross carrier", mutate_key("string_zero_treated_as_cross_carrier_evidence", True)),
            ("string zero doctrine", mutate_key("string_zero_representation_turned_into_doctrine", True)),
            ("ok treated as cross carrier", mutate_key("ok_output_treated_as_cross_carrier_evidence", True)),
            ("ran seven treated as proof", mutate_key("ran_7_tests_treated_as_cross_carrier_proof", True)),
            ("returned capture treated as cross carrier", mutate_key("returned_capture_treated_as_cross_carrier_evidence", True)),
            ("official strings redacted", mutate_key("selected_second_carrier_external_result_official_enum_scope_strings_redacted", True)),
            (
                "predecessor v1 missing",
                mutate_many(
                    predecessor_external_result_v1_failure_preserved=False,
                    selected_second_carrier_external_result_predecessor_v1_failure_preserved=False,
                ),
            ),
            ("external result boundary basis missing", clear_key("selected_second_carrier_external_result_boundary_basis")),
            ("external result boundary outcome bad", mutate_key("selected_second_carrier_external_result_boundary_result_outcome", "NOT_RECORDED")),
            ("external result boundary failed checks", mutate_key("selected_second_carrier_external_result_boundary_failed_check_count", 1)),
            ("verification basis missing", clear_key("selected_second_carrier_verification_basis")),
            ("verification not recorded", mutate_key("selected_second_carrier_verification_result_outcome", "NOT_RECORDED")),
            ("verification failed checks", mutate_key("selected_second_carrier_verification_failed_check_count", 1)),
            ("success basis missing", clear_key("selected_second_carrier_success_basis")),
            ("success not recorded", mutate_key("selected_second_carrier_success_result_outcome", "NOT_RECORDED")),
            ("success failed checks", mutate_key("selected_second_carrier_success_failed_check_count", 1)),
            ("result basis missing", clear_key("selected_second_carrier_result_basis")),
            ("result not recorded", mutate_key("selected_second_carrier_result_result_outcome", "NOT_RECORDED")),
            ("result failed checks", mutate_key("selected_second_carrier_result_failed_check_count", 1)),
            ("returned capture intake missing", clear_key("selected_returned_second_carrier_live_capture_intake_basis")),
            ("returned capture intake not preserved", mutate_key("selected_returned_capture_intake_preserved", False)),
            ("returned capture intake not capture-only", mutate_key("selected_returned_capture_intake_capture_only", False)),
            ("MacBook Pro to Air missing", mutate_key("selected_returned_capture_from_macbook_pro_to_macbook_air", False)),
            ("placeholder fields repaired", mutate_key("selected_returned_capture_placeholder_fields_unrepaired", False)),
            ("returned capture material missing", clear_key("selected_returned_capture_material_basis")),
            ("returned zip missing", mutate_key("selected_returned_capture_zip_path", "")),
            ("returned hash missing", mutate_key("selected_returned_capture_hash_path", "")),
            ("returned extracted missing", mutate_key("selected_returned_capture_extracted_directory_path", "")),
            ("returned combined log missing", mutate_key("selected_returned_capture_combined_terminal_log_path", "")),
            ("returned exit code missing", mutate_key("selected_returned_capture_exit_code", None)),
            ("returned command text missing", mutate_key("selected_returned_capture_command_text", "")),
            ("returned started timestamp missing", mutate_key("selected_returned_capture_started_at", "")),
            ("returned completed timestamp missing", mutate_key("selected_returned_capture_completed_at", "")),
            ("declared zero doctrine by nonzero", mutate_key("selected_returned_capture_declared_exit_code", "1")),
            ("output capture basis missing", clear_key("selected_second_carrier_output_capture_basis")),
            ("output capture not recorded", mutate_key("selected_second_carrier_output_capture_result_outcome", "NOT_RECORDED")),
            ("output capture failed checks", mutate_key("selected_second_carrier_output_capture_failed_check_count", 1)),
            ("packet transfer basis missing", clear_key("selected_packet_transfer_basis")),
            ("packet emission basis missing", clear_key("selected_packet_emission_basis")),
            ("command success basis missing", clear_key("selected_command_success_basis")),
            ("command result v2 basis missing", clear_key("selected_command_result_v2_basis")),
            ("output capture v2 basis missing", clear_key("selected_output_capture_v2_basis")),
            ("command output report basis missing", clear_key("selected_command_output_report_artifact_basis")),
            ("evidence manifest basis missing", clear_key("selected_evidence_manifest_basis")),
            ("artifact containment basis missing", clear_key("selected_artifact_containment_basis")),
            ("portable verification basis missing", clear_key("selected_portable_verification_basis")),
            ("boundary treated as cross carrier", mutate_key("cross_carrier_evidence_boundary_treated_as_cross_carrier_evidence", True)),
            ("boundary treated as closure", mutate_key("cross_carrier_evidence_boundary_treated_as_portable_verification_closure", True)),
            ("boundary treated as source transfer", mutate_key("cross_carrier_evidence_boundary_treated_as_source_transfer", True)),
            ("boundary treated as source receipt", mutate_key("cross_carrier_evidence_boundary_treated_as_source_receipt", True)),
            ("boundary treated as reception", mutate_key("cross_carrier_evidence_boundary_treated_as_reception_authorization", True)),
            ("boundary treated as source", mutate_key("cross_carrier_evidence_boundary_treated_as_source", True)),
            ("boundary treated as authority", mutate_key("cross_carrier_evidence_boundary_treated_as_authority", True)),
            ("boundary treated as currentness", mutate_key("cross_carrier_evidence_boundary_treated_as_currentness", True)),
            ("boundary treated as final completion", mutate_key("cross_carrier_evidence_boundary_treated_as_final_completion", True)),
            ("boundary treated as runtime", mutate_key("cross_carrier_evidence_boundary_treated_as_runtime", True)),
            ("boundary treated as continuation", mutate_key("cross_carrier_evidence_boundary_treated_as_continuation", True)),
            ("boundary treated as reusable", mutate_key("cross_carrier_evidence_boundary_treated_as_reusable_permission", True)),
            ("boundary treated as follow-on", mutate_key("cross_carrier_evidence_boundary_treated_as_follow_on_work", True)),
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
            ("artifact existence authority", flip_non_claim("artifact_existence_treated_as_cross_carrier_evidence_authority")),
            ("artifact path currentness", flip_non_claim("artifact_path_treated_as_currentness")),
            ("repo local authority", flip_non_claim("repo_local_availability_treated_as_cross_carrier_evidence_authority")),
            ("hidden repo content", flip_non_claim("hidden_repo_state_used_as_cross_carrier_evidence_content")),
            ("hidden repo authority", flip_non_claim("hidden_repo_state_used_as_cross_carrier_evidence_authority")),
            ("selected basis not reference-shaped", mutate_key("reference_shaped_input_posture", False)),
            ("raw full prior artifact body returned", flip_non_claim("raw_full_prior_artifact_body_returned")),
            ("predecessor external v1 repaired", mutate_key("predecessor_external_result_v1_repaired", True)),
            ("predecessor external v1 hidden", mutate_key("predecessor_external_result_v1_hidden", True)),
            ("predecessor external v1 claimed passed", mutate_key("predecessor_external_result_v1_claimed_passed", True)),
            ("v1 packet emission repaired", mutate_key("v1_packet_emission_repaired", True)),
            ("v1 packet emission hidden", mutate_key("v1_packet_emission_hidden", True)),
            ("v1 packet emission claimed passed", mutate_key("v1_packet_emission_claimed_passed", True)),
            ("first success boundary repaired", mutate_key("first_success_boundary_test_repaired", True)),
            ("first success boundary hidden", mutate_key("first_success_boundary_test_hidden", True)),
            ("first success boundary claimed passed", mutate_key("first_success_boundary_test_claimed_passed", True)),
            ("first result boundary repaired", mutate_key("first_result_boundary_resolver_repaired", True)),
            ("first result boundary hidden", mutate_key("first_result_boundary_resolver_hidden", True)),
            ("first result boundary claimed passed", mutate_key("first_result_boundary_resolver_claimed_passed", True)),
            ("command lineage current report", mutate_key("selected_command_report_lineage_treated_as_current_report_artifact", True)),
            ("command lineage source", mutate_key("selected_command_report_lineage_treated_as_source", True)),
            ("command lineage authority", mutate_key("selected_command_report_lineage_treated_as_authority", True)),
            ("command lineage currentness", mutate_key("selected_command_report_lineage_treated_as_currentness", True)),
            ("consumed request reopened", flip_non_claim("consumed_request_reopened")),
            ("authorization reused", flip_non_claim("authorization_token_reused")),
            ("full prior body emitted", mutate_key("full_prior_artifact_body_emitted_outside_bounded_cross_carrier_evidence_boundary", True)),
            ("artifacts mutated", mutate_key("artifacts_mutated", True)),
            ("returned capture material mutated", mutate_key("returned_capture_material_mutated", True)),
            ("required non-claim missing", remove_non_claim("cross_carrier_evidence_created")),
            ("required non-claim flipped", flip_non_claim("string_zero_representation_turned_into_doctrine")),
        )

        missing_result = resolver.resolve_portable_source_body_verification_cross_carrier_evidence_boundary()
        self.assert_blocked_result(missing_result)
        non_mapping_result = resolver.resolve_portable_source_body_verification_cross_carrier_evidence_boundary(
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

            result = resolver.resolve_portable_source_body_verification_cross_carrier_evidence_boundary_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], RECORDED)
            summary = result[
                "portable_source_body_verification_cross_carrier_evidence_boundary_summary"
            ]
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)

            malformed_path = temp_root / "malformed.json"
            malformed_path.write_text("{not valid json", encoding="utf-8")
            self.assert_path_blocks_or_raises(
                lambda: resolver.resolve_portable_source_body_verification_cross_carrier_evidence_boundary_from_path(
                    malformed_path
                )
            )

            array_path = temp_root / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            self.assert_path_blocks_or_raises(
                lambda: resolver.resolve_portable_source_body_verification_cross_carrier_evidence_boundary_from_path(
                    array_path
                )
            )

            self.assert_path_blocks_or_raises(
                lambda: resolver.resolve_portable_source_body_verification_cross_carrier_evidence_boundary_from_path(
                    temp_root / "missing.json"
                )
            )

            output_root = (
                temp_root
                / "artifacts"
                / "integrity_host_v0_min_coexistence_portable_source_body_verification_cross_carrier_evidence_boundary"
            )
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_portable_source_body_verification_cross_carrier_evidence_boundary_result(
                    result
                )
                second_path = resolver.write_portable_source_body_verification_cross_carrier_evidence_boundary_result(
                    result
                )

            self.assertTrue(first_path.parent.exists())
            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertEqual(first_path.parent, output_root)
            self.assertEqual(second_path.parent, output_root)
            self.assertEqual(json.loads(first_path.read_text(encoding="utf-8"))["outcome"], RECORDED)
            self.assertTrue(second_path.stem.endswith("_001"))
            self.assertIn(
                "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_cross_carrier_evidence_boundary",
                first_path.as_posix(),
            )
            forbidden_components = {
                "actual_second_carrier_live_capture",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_cross_carrier_evidence",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_external_result",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_external_result_boundary",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_verification",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_success",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_result",
                "portable_verification_closure",
                "runtime",
                "deployment",
                "public_release",
            }
            self.assertTrue(forbidden_components.isdisjoint(set(first_path.parts)))
            self.assertTrue(forbidden_components.isdisjoint(set(second_path.parts)))

    def test_non_mutation_of_request_and_selected_inputs(self) -> None:
        request = default_request()
        request["cross_carrier_evidence_boundary_scope"] = list(
            resolver.SUPPORTED_CROSS_CARRIER_EVIDENCE_BOUNDARY_SCOPE
        )
        for key in SELECTED_BASIS_FIELDS:
            request[key]["non_mutation_marker"] = {"nested": [key, "preserve"]}
        for key in POSTURE_SECTIONS:
            request[key] = {"declared": True, "non_mutation_marker": [key, "preserve"]}
        request["declared_non_claims"]["non_mutation_marker"] = False
        snapshot = copy.deepcopy(request)

        result = resolve_request(request)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(request, snapshot)

    def test_predecessor_failure_preservation(self) -> None:
        request = default_request()
        result = resolve_request(request)
        summary = resolver.build_portable_source_body_verification_cross_carrier_evidence_boundary_summary(
            result
        )
        recorded_statement = statement(result)
        claims = non_claims(result)

        self.assertIs(recorded_statement["predecessor_external_result_v1_failure_preserved"], True)
        self.assertIs(recorded_statement["first_success_boundary_test_failure_preserved"], True)
        self.assertIs(recorded_statement["first_result_boundary_resolver_failure_preserved"], True)
        self.assertIs(claims["predecessor_external_result_v1_repaired"], False)
        self.assertIs(claims["predecessor_external_result_v1_hidden"], False)
        self.assertIs(claims["predecessor_external_result_v1_claimed_passed"], False)
        self.assertIs(claims["v1_packet_emission_repaired"], False)
        self.assertIs(claims["v1_packet_emission_hidden"], False)
        self.assertIs(claims["v1_packet_emission_claimed_passed"], False)
        self.assertIs(claims["first_success_boundary_test_repaired"], False)
        self.assertIs(claims["first_success_boundary_test_hidden"], False)
        self.assertIs(claims["first_success_boundary_test_claimed_passed"], False)
        self.assertIs(claims["first_result_boundary_resolver_repaired"], False)
        self.assertIs(claims["first_result_boundary_resolver_hidden"], False)
        self.assertIs(claims["first_result_boundary_resolver_claimed_passed"], False)

        predecessor_basis = result["selected_predecessor_failure_basis"]["basis"]
        self.assertIs(predecessor_basis["predecessor_external_result_v1_failure_preserved"], True)
        self.assertIs(predecessor_basis["first_success_boundary_test_failure_preserved"], True)
        self.assertIs(predecessor_basis["first_result_boundary_resolver_failure_preserved"], True)
        self.assertIs(predecessor_basis["v1_packet_emission_failure_preserved"], True)

        self.assertIs(summary["predecessor_external_result_v1_failure_preserved"], True)
        self.assertIs(summary["first_success_boundary_test_preserved_as_failed_predecessor"], True)
        self.assertIs(summary["v1_packet_emission_predecessor_failure_preserved"], True)
        self.assertIs(summary["first_result_boundary_resolver_preserved_as_failed_predecessor"], True)
        self.assertIs(summary["cross_carrier_evidence_not_created"], True)
        self.assertIs(summary["portable_verification_closure_not_created"], True)
        self.assertIs(summary["external_result_not_cross_carrier_evidence"], True)


if __name__ == "__main__":
    unittest.main()
