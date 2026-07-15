"""Executable checks for portable-verification-closure-boundary posture only.

This suite is downstream of the cross-carrier evidence line. It verifies that
the resolver records one future line-level portable verification closure review
step only. Portable verification closure, final completion, source transfer,
source receipt, reception authorization, source, authority, currentness,
runtime, deployment, public release, continuation, reusable permission, and
follow-on work are not created.

The predecessor cross-carrier evidence resolver/v2/test, predecessor external
result v1, first success-boundary test, first result-boundary resolver, and v1
packet-emission-boundary surfaces remain preserved failure evidence. This suite
does not repair, hide, delete, rename, or claim passed those surfaces. Official
enum, scope, and block-code strings are checked for exact preservation while
hostile raw body payload content remains contained.
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

import resolve_portable_source_body_verification_portable_verification_closure_boundary as resolver


RECORDED = resolver.OUTCOME_RECORDED
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = set(resolver.OUTCOME_FAMILY)
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
TRUE_RECORDED_FIELDS = tuple(resolver.ALLOWED_TRUE_RECORDED_FIELDS)
SELECTED_BASIS_KEYS = tuple(resolver.SELECTED_BASIS_KEYS)
POSTURE_KEYS = tuple(resolver.POSTURE_KEYS)

RAW_SENTINELS = (
    "RAW_PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_BODY_MUST_NOT_RETURN",
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
    "hostile-raw-cross-carrier-evidence-body-value",
    "hostile-raw-portable-verification-closure-body-value",
    "hostile-capture-body-value",
    "hostile-cross-carrier-evidence-body-value",
    "hostile-portable-verification-closure-body-value",
    "hostile-final-completion-body-value",
    "hostile-source-body-value",
    "hostile-authority-body-value",
    "hostile-current-working-tree-value",
    "hostile-local-cache-value",
    "hostile-repo-local-only-dependency-value",
)
REDACTION_PLACEHOLDERS = {
    "[bounded-portable-verification-closure-boundary-redacted]",
    "[bounded-redacted-raw-or-hidden-state]",
}
OFFICIAL_SCOPE_VALUES = (
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "RETURNED_RESULT_CONTAINMENT_PRESERVED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "PREDECESSOR_CROSS_CARRIER_EVIDENCE_FAILURE_PRESERVED",
    "PREDECESSOR_EXTERNAL_RESULT_V1_FAILURE_PRESERVED",
    "FIRST_SUCCESS_BOUNDARY_TEST_FAILURE_PRESERVED",
    "FIRST_RESULT_BOUNDARY_RESOLVER_FAILURE_PRESERVED",
    "STRING_ZERO_NOT_PORTABLE_VERIFICATION_CLOSURE",
    "PORTABLE_VERIFICATION_CLOSURE_NOT_CREATED",
    "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_NOT_PORTABLE_VERIFICATION_CLOSURE",
    "FINAL_COMPLETION_NOT_CREATED",
)

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_portable_verification_closure_boundary_metadata",
    "declared_portable_verification_closure_boundary_question",
    "selected_cross_carrier_evidence_basis",
    "selected_cross_carrier_evidence_terminal_summary_basis",
    "selected_cross_carrier_evidence_boundary_basis",
    "selected_second_carrier_external_result_basis",
    "selected_second_carrier_external_result_terminal_summary_basis",
    "selected_second_carrier_external_result_boundary_basis",
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
    "portable_verification_closure_boundary_only_posture",
    "one_future_portable_verification_closure_review_step_posture",
    "cross_carrier_evidence_basis_preserved_posture",
    "cross_carrier_evidence_artifact_basis_preserved_posture",
    "cross_carrier_evidence_boundary_basis_preserved_posture",
    "second_carrier_external_result_basis_preserved_posture",
    "returned_second_carrier_capture_basis_preserved_posture",
    "capture_intake_basis_preserved_posture",
    "second_carrier_output_capture_basis_preserved_posture",
    "portable_verification_closure_not_created_posture",
    "portable_verification_closure_boundary_not_portable_verification_closure_posture",
    "cross_carrier_evidence_not_portable_verification_closure_posture",
    "zero_exit_code_not_portable_verification_closure_posture",
    "string_zero_not_portable_verification_closure_posture",
    "ok_output_not_portable_verification_closure_posture",
    "ran_7_tests_not_portable_verification_closure_posture",
    "returned_capture_not_portable_verification_closure_posture",
    "final_completion_not_created_posture",
    "portable_verification_closure_not_source_transfer_posture",
    "portable_verification_closure_not_source_receipt_posture",
    "portable_verification_closure_not_reception_authorization_posture",
    "receiving_carrier_not_authority_posture",
    "source_not_created_posture",
    "authority_not_created_posture",
    "currentness_not_created_posture",
    "runtime_not_created_posture",
    "continuation_not_authorized_posture",
    "reusable_permission_not_created_posture",
    "follow_on_work_not_authorized_posture",
    "hidden_repo_state_excluded_posture",
    "repo_local_availability_not_portable_verification_closure_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_cross_carrier_evidence_failure_preserved_posture",
    "predecessor_external_result_v1_failure_preserved_posture",
    "first_success_boundary_test_failure_preserved_posture",
    "first_result_boundary_resolver_failure_preserved_posture",
    "portable_verification_closure_boundary_scope",
    "portable_verification_closure_boundary_checks",
    "portable_verification_closure_boundary_statement",
    "portable_verification_closure_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_portable_verification_closure_boundary_summary",
)

REPRESENTATIVE_BLOCK_CODES = (
    "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_QUESTION_UNDECLARED",
    "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_INTENT_UNSUPPORTED",
    "CROSS_CARRIER_EVIDENCE_BASIS_MISSING",
    "CROSS_CARRIER_EVIDENCE_NOT_RECORDED",
    "CROSS_CARRIER_EVIDENCE_FAILED_CHECKS_PRESENT",
    "CROSS_CARRIER_EVIDENCE_VERSION_NOT_0_1_0",
    "CROSS_CARRIER_EVIDENCE_DID_NOT_RECORD_BOUNDED_EVIDENCE",
    "CROSS_CARRIER_EVIDENCE_ALREADY_CREATED_PORTABLE_VERIFICATION_CLOSURE",
    "CROSS_CARRIER_EVIDENCE_ALREADY_CREATED_FINAL_COMPLETION",
    "CROSS_CARRIER_EVIDENCE_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
    "CROSS_CARRIER_EVIDENCE_TREATED_AS_SOURCE_TRANSFER",
    "CROSS_CARRIER_EVIDENCE_TREATED_AS_SOURCE_RECEIPT",
    "CROSS_CARRIER_EVIDENCE_TREATED_AS_RECEPTION_AUTHORIZATION",
    "CROSS_CARRIER_EVIDENCE_TREATED_AS_SOURCE",
    "CROSS_CARRIER_EVIDENCE_TREATED_AS_AUTHORITY",
    "CROSS_CARRIER_EVIDENCE_TREATED_AS_CURRENTNESS",
    "CROSS_CARRIER_EVIDENCE_TREATED_AS_FINAL_COMPLETION",
    "CROSS_CARRIER_EVIDENCE_TREATED_AS_RUNTIME",
    "CROSS_CARRIER_EVIDENCE_TREATED_AS_FOLLOW_ON_WORK",
    "CROSS_CARRIER_EVIDENCE_TREATED_ZERO_EXIT_CODE_AS_PORTABLE_VERIFICATION_CLOSURE",
    "CROSS_CARRIER_EVIDENCE_TREATED_STRING_ZERO_AS_PORTABLE_VERIFICATION_CLOSURE",
    "CROSS_CARRIER_EVIDENCE_TREATED_STRING_ZERO_AS_DOCTRINE",
    "CROSS_CARRIER_EVIDENCE_TREATED_OK_AS_PORTABLE_VERIFICATION_CLOSURE",
    "CROSS_CARRIER_EVIDENCE_TREATED_RAN_7_TESTS_AS_PORTABLE_VERIFICATION_CLOSURE",
    "CROSS_CARRIER_EVIDENCE_TREATED_RETURNED_CAPTURE_AS_PORTABLE_VERIFICATION_CLOSURE",
    "CROSS_CARRIER_EVIDENCE_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
    "PREDECESSOR_CROSS_CARRIER_EVIDENCE_FAILURE_MISSING_OR_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
    "PREDECESSOR_EXTERNAL_RESULT_V1_FAILURE_MISSING_OR_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_BASIS_MISSING",
    "SECOND_CARRIER_EXTERNAL_RESULT_BASIS_MISSING",
    "SECOND_CARRIER_EXTERNAL_RESULT_NOT_RECORDED",
    "SECOND_CARRIER_EXTERNAL_RESULT_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_EXTERNAL_RESULT_ALREADY_CREATED_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_EXTERNAL_RESULT_AS_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_STRING_ZERO_AS_DOCTRINE",
    "SECOND_CARRIER_VERIFICATION_BASIS_MISSING",
    "SECOND_CARRIER_VERIFICATION_NOT_RECORDED",
    "SECOND_CARRIER_SUCCESS_BASIS_MISSING",
    "SECOND_CARRIER_SUCCESS_NOT_RECORDED",
    "SECOND_CARRIER_RESULT_BASIS_MISSING",
    "SECOND_CARRIER_RESULT_NOT_RECORDED",
    "RETURNED_CAPTURE_INTAKE_BASIS_MISSING",
    "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
    "RETURNED_CAPTURE_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
    "ZERO_EXIT_CODE_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
    "STRING_ZERO_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
    "STRING_ZERO_REPRESENTATION_TURNED_INTO_DOCTRINE",
    "OK_OUTPUT_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
    "RAN_7_TESTS_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
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
    "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
    "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_FINAL_COMPLETION",
    "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_SOURCE",
    "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_AUTHORITY",
    "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_CURRENTNESS",
    "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_RUNTIME",
    "PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
    "PORTABLE_VERIFICATION_CLOSURE_CREATED",
    "FINAL_COMPLETION_CLAIMED",
    "SOURCE_TRANSFER_OCCURRED",
    "SOURCE_RECEIPT_OCCURRED",
    "RECEPTION_AUTHORIZATION_CREATED",
    "SOURCE_CREATED",
    "AUTHORITY_CREATED",
    "CURRENTNESS_CREATED",
    "RUNTIME_HOSTING_CREATED",
    "PUBLIC_RELEASE_CREATED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "RECEIVING_CARRIER_TREATED_AS_AUTHORITY",
    "ARTIFACT_EXISTENCE_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_PORTABLE_VERIFICATION_CLOSURE_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_PORTABLE_VERIFICATION_CLOSURE_AUTHORITY",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_PORTABLE_VERIFICATION_CLOSURE_BOUNDARY",
    "ARTIFACTS_MUTATED",
    "RETURNED_CAPTURE_MATERIAL_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_SCOPE",
)


def build_request(**overrides: Any) -> dict[str, Any]:
    return resolver.build_declared_portable_source_body_verification_portable_verification_closure_boundary_request(
        **overrides
    )


def resolved(request: Any) -> dict[str, Any]:
    return resolver.resolve_portable_source_body_verification_portable_verification_closure_boundary(
        request
    )


def statement(result: dict[str, Any]) -> dict[str, Any]:
    return result.get("portable_verification_closure_boundary_statement", {})


def non_claims(result: dict[str, Any]) -> dict[str, Any]:
    return result.get("non_claims", {})


def checks(result: dict[str, Any]) -> list[dict[str, Any]]:
    return list(result.get("portable_verification_closure_boundary_checks", []))


def summary(result: dict[str, Any]) -> dict[str, Any]:
    return result.get(
        "portable_source_body_verification_portable_verification_closure_boundary_summary",
        {},
    )


def scope_values(result: dict[str, Any]) -> list[str]:
    scope = result.get("portable_verification_closure_boundary_scope", {})
    if isinstance(scope, dict):
        return list(scope.get("scope_values", []))
    return list(scope)


def serialized(result: dict[str, Any]) -> str:
    return json.dumps(result, sort_keys=True)


def set_field(name: str, value: Any) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request[name] = value

    return mutate


def set_fields(values: dict[str, Any]) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request.update(values)

    return mutate


def clear_field(name: str) -> Callable[[dict[str, Any]], None]:
    return set_field(name, None)


def remove_non_claim(name: str) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request["declared_non_claims"].pop(name, None)

    return mutate


def set_non_claim(name: str, value: Any = True) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request[name] = value
        if name in request["declared_non_claims"]:
            request["declared_non_claims"][name] = value

    return mutate


class PortableVerificationClosureBoundaryTest(unittest.TestCase):
    def assert_public_block_codes(self, result: dict[str, Any]) -> None:
        block = result.get("block")
        if isinstance(block, dict) and block.get("block_code"):
            self.assertIn(block["block_code"], resolver.BLOCK_CODES)
        for record in checks(result):
            for code_key in ("block_code", "failure_code"):
                code = record.get(code_key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_generated_booleans_are_bool(self, result: dict[str, Any]) -> None:
        for section in (
            statement(result),
            non_claims(result),
            result.get("portable_verification_closure_boundary_non_meaning", {}),
        ):
            for key, value in section.items():
                self.assertIs(type(value), bool, key)
        scope = result.get("portable_verification_closure_boundary_scope", {})
        self.assertIs(type(scope.get("official_enum_scope_strings_not_redacted")), bool)
        for posture_key in POSTURE_KEYS:
            posture = result.get(posture_key, {})
            self.assertIs(type(posture.get("declared")), bool, posture_key)
            for generated_key in (
                "creates_portable_verification_closure",
                "creates_final_completion",
                "creates_source_transfer",
                "creates_source_receipt",
                "creates_reception_authorization",
                "creates_source_authority_currentness_runtime_or_follow_on",
            ):
                self.assertIs(type(posture.get(generated_key)), bool, posture_key)

    def assert_no_raw_or_hidden_sentinels(self, result: dict[str, Any]) -> None:
        body = serialized(result)
        for sentinel in RAW_SENTINELS:
            self.assertNotIn(sentinel, body)
        for hostile in HOSTILE_VALUES:
            self.assertNotIn(hostile, body)

    def assert_official_scope_strings_preserved(self, result: dict[str, Any]) -> None:
        scope = result.get("portable_verification_closure_boundary_scope", {})
        emitted_scope = scope_values(result)
        supported_scope = list(scope.get("supported_scope_values", []))
        all_scope_strings = set(emitted_scope) | set(supported_scope)
        for official in OFFICIAL_SCOPE_VALUES:
            self.assertIn(official, all_scope_strings)
        for value in emitted_scope + supported_scope:
            self.assertNotIn(value, REDACTION_PLACEHOLDERS)
        for official in SUPPORTED_SCOPE:
            self.assertIn(official, supported_scope)
        emitted_codes = {
            record.get("block_code")
            for record in checks(result)
            if record.get("block_code") is not None
        }
        emitted_codes |= {
            record.get("failure_code")
            for record in checks(result)
            if record.get("failure_code") is not None
        }
        for code in emitted_codes:
            self.assertIn(code, resolver.BLOCK_CODES)
            self.assertNotIn(code, REDACTION_PLACEHOLDERS)

    def assert_no_forbidden_creation(self, result: dict[str, Any]) -> None:
        claims = non_claims(result)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(claims.get(key), False, key)

    def assert_predecessors_not_repaired_hidden_or_claimed_passed(
        self, result: dict[str, Any]
    ) -> None:
        claims = non_claims(result)
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
            self.assertIs(claims.get(key), False, key)

    def assert_blocked_result(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertIsInstance(result.get("block"), dict)
        self.assertIsNotNone(result["block"].get("block_code"))
        self.assert_public_block_codes(result)
        self.assert_no_forbidden_creation(result)
        self.assert_predecessors_not_repaired_hidden_or_claimed_passed(result)
        self.assert_generated_booleans_are_bool(result)
        self.assert_official_scope_strings_preserved(result)

    def assert_path_blocks_or_raises(self, path: Path) -> None:
        try:
            result = resolver.resolve_portable_source_body_verification_portable_verification_closure_boundary_from_path(
                path
            )
        except resolver.PortableSourceBodyVerificationPortableVerificationClosureBoundaryError:
            return
        self.assert_blocked_result(result)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_portable_source_body_verification_portable_verification_closure_boundary",
            "resolve_portable_source_body_verification_portable_verification_closure_boundary_from_path",
            "write_portable_source_body_verification_portable_verification_closure_boundary_result",
            "build_portable_source_body_verification_portable_verification_closure_boundary_summary",
            "build_declared_portable_source_body_verification_portable_verification_closure_boundary_request",
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
            "SUPPORTED_PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_portable_source_body_verification_portable_verification_closure_boundary",
        )
        self.assertEqual(
            resolver.SUPPORTED_PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_SCOPE,
            resolver.SUPPORTED_SCOPE_VALUES,
        )
        self.assertTrue(
            str(resolver.OUTPUT_ROOT)
            .replace("\\", "/")
            .endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_portable_source_body_verification_"
                "portable_verification_closure_boundary"
            )
        )
        for official in OFFICIAL_SCOPE_VALUES:
            self.assertIn(official, resolver.SUPPORTED_PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_SCOPE)
        for code in REPRESENTATIVE_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_successful_recorded_result_from_no_argument_builder(self) -> None:
        request = build_request()
        request_snapshot = copy.deepcopy(request)
        result = resolved(request)
        compact = resolver.build_portable_source_body_verification_portable_verification_closure_boundary_summary(
            result
        )

        self.assertEqual(request, request_snapshot)
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertIsNone(result["block"])
        self.assertEqual(compact["failed_check_count"], 0)
        self.assertGreater(compact["passed_check_count"], 0)
        self.assertEqual(compact["result_version"], "0.1.0")
        self.assertEqual(
            compact["resolver_module"],
            "resolve_portable_source_body_verification_portable_verification_closure_boundary",
        )
        self.assertEqual(
            compact["request_id"],
            request["portable_verification_closure_boundary_request_id"],
        )
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)

        for key in TRUE_RECORDED_FIELDS:
            self.assertIs(statement(result).get(key), True, key)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(non_claims(result).get(key), False, key)

        self.assert_public_block_codes(result)
        self.assert_generated_booleans_are_bool(result)
        self.assert_official_scope_strings_preserved(result)
        self.assert_no_forbidden_creation(result)
        self.assert_predecessors_not_repaired_hidden_or_claimed_passed(result)
        self.assert_no_raw_or_hidden_sentinels(result)

    def test_official_enum_strings_are_preserved_without_redaction_placeholders(self) -> None:
        result = resolved(build_request())
        emitted_scope = scope_values(result)
        for official in OFFICIAL_SCOPE_VALUES:
            self.assertIn(official, emitted_scope)
        for value in emitted_scope:
            self.assertNotIn(value, REDACTION_PLACEHOLDERS)
        self.assert_official_scope_strings_preserved(result)

        request = build_request(
            portable_verification_closure_boundary_scope=list(SUPPORTED_SCOPE)
        )
        custom_result = resolved(request)
        self.assertEqual(custom_result["outcome"], RECORDED)
        self.assertEqual(scope_values(custom_result), list(SUPPORTED_SCOPE))
        self.assert_official_scope_strings_preserved(custom_result)
        self.assert_public_block_codes(custom_result)

    def test_raw_and_hidden_hostile_content_is_contained(self) -> None:
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
            "raw_cross_carrier_evidence_body": HOSTILE_VALUES[10],
            "raw_portable_verification_closure_body": HOSTILE_VALUES[11],
            "raw_portable_verification_closure_boundary_body": RAW_SENTINELS[0],
            "capture_body": HOSTILE_VALUES[12],
            "cross_carrier_evidence_body": HOSTILE_VALUES[13],
            "portable_verification_closure_body": HOSTILE_VALUES[14],
            "final_completion_body": HOSTILE_VALUES[15],
            "source_body": HOSTILE_VALUES[16],
            "authority_body": HOSTILE_VALUES[17],
            "hidden_repo_state": "hidden-state:" + RAW_SENTINELS[2],
            "current_working_tree": HOSTILE_VALUES[18],
            "local_cache": HOSTILE_VALUES[19],
            "repo_local_only_dependency": HOSTILE_VALUES[20],
            "nested": {
                "items": [
                    RAW_SENTINELS[0],
                    {"deeper": RAW_SENTINELS[1]},
                    {"official_scope": "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED"},
                ]
            },
        }
        for section in (
            "selected_cross_carrier_evidence_basis",
            "selected_cross_carrier_evidence_terminal_summary_basis",
            "selected_cross_carrier_evidence_boundary_basis",
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
            request[section]["hostile_probe"] = copy.deepcopy(hostile_payload)

        before = copy.deepcopy(request)
        result = resolved(request)
        self.assertEqual(request, before)
        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assert_no_raw_or_hidden_sentinels(result)
        self.assert_official_scope_strings_preserved(result)
        self.assert_public_block_codes(result)
        self.assert_no_forbidden_creation(result)
        self.assert_generated_booleans_are_bool(result)
        claims = non_claims(result)
        self.assertIs(claims["hidden_repo_state_used_as_portable_verification_closure_content"], False)
        self.assertIs(claims["hidden_repo_state_used_as_portable_verification_closure_authority"], False)
        self.assertIs(claims["repo_local_availability_treated_as_portable_verification_closure_authority"], False)
        self.assertIs(claims["receiving_carrier_treated_as_authority"], False)
        self.assertIs(claims["artifact_existence_treated_as_portable_verification_closure_authority"], False)
        self.assertIs(claims["artifact_path_treated_as_currentness"], False)
        self.assertIs(claims["string_zero_treated_as_portable_verification_closure"], False)
        self.assertIs(claims["string_zero_representation_turned_into_doctrine"], False)

    def test_representative_blocking_behavior(self) -> None:
        malformed_cases: tuple[Any, ...] = (None, ["not", "a", "mapping"])
        for bad_request in malformed_cases:
            with self.subTest(kind="malformed request", request=repr(bad_request)):
                self.assert_blocked_result(resolved(bad_request))

        cases: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
            ("explicit block intent", set_field("portable_verification_closure_boundary_intent", "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_PORTABLE_VERIFICATION_CLOSURE_BOUNDARY")),
            ("undeclared question", set_field("portable_verification_closure_boundary_question", "")),
            ("unsupported intent", set_field("portable_verification_closure_boundary_intent", "UNSUPPORTED_INTENT")),
            ("unsupported scope", set_field("portable_verification_closure_boundary_scope", ["UNSUPPORTED_PORTABLE_VERIFICATION_CLOSURE_BOUNDARY_SCOPE_VALUE"])),
            ("missing cross-carrier evidence basis", clear_field("selected_cross_carrier_evidence_basis")),
            ("missing cross-carrier evidence terminal summary basis", clear_field("selected_cross_carrier_evidence_terminal_summary_basis")),
            ("cross-carrier evidence not recorded", set_field("selected_cross_carrier_evidence_result_outcome", "NOT_RECORDED")),
            ("cross-carrier evidence failed checks", set_field("selected_cross_carrier_evidence_failed_check_count", 1)),
            ("cross-carrier evidence version wrong", set_field("selected_cross_carrier_evidence_result_version", "9.9.9")),
            ("cross-carrier evidence did not record bounded evidence", set_field("selected_cross_carrier_evidence_bounded_evidence_recorded", False)),
            ("cross-carrier evidence already created closure", set_field("selected_cross_carrier_evidence_already_created_portable_verification_closure", True)),
            ("cross-carrier evidence already created final completion", set_field("selected_cross_carrier_evidence_already_created_final_completion", True)),
            ("cross-carrier evidence treated as closure", set_field("selected_cross_carrier_evidence_treated_as_portable_verification_closure", True)),
            ("cross-carrier evidence treated as source transfer", set_field("selected_cross_carrier_evidence_treated_as_source_transfer", True)),
            ("cross-carrier evidence treated as source receipt", set_field("selected_cross_carrier_evidence_treated_as_source_receipt", True)),
            ("cross-carrier evidence treated as reception authorization", set_field("selected_cross_carrier_evidence_treated_as_reception_authorization", True)),
            ("cross-carrier evidence treated as source", set_field("selected_cross_carrier_evidence_treated_as_source", True)),
            ("cross-carrier evidence treated as authority", set_field("selected_cross_carrier_evidence_treated_as_authority", True)),
            ("cross-carrier evidence treated as currentness", set_field("selected_cross_carrier_evidence_treated_as_currentness", True)),
            ("cross-carrier evidence treated as final completion", set_field("selected_cross_carrier_evidence_treated_as_final_completion", True)),
            ("cross-carrier evidence treated as runtime", set_field("selected_cross_carrier_evidence_treated_as_runtime", True)),
            ("cross-carrier evidence treated as follow-on work", set_field("selected_cross_carrier_evidence_treated_as_follow_on_work", True)),
            ("cross-carrier evidence treated zero exit as closure", set_field("selected_cross_carrier_evidence_zero_exit_code_not_portable_verification_closure", False)),
            ("cross-carrier evidence treated string zero as closure", set_field("selected_cross_carrier_evidence_string_zero_not_portable_verification_closure", False)),
            ("cross-carrier evidence treated string zero as doctrine", set_field("selected_cross_carrier_evidence_treated_string_zero_as_doctrine", True)),
            ("cross-carrier evidence treated OK as closure", set_field("selected_cross_carrier_evidence_ok_not_portable_verification_closure", False)),
            ("cross-carrier evidence treated Ran 7 as closure", set_field("selected_cross_carrier_evidence_ran_7_tests_not_portable_verification_closure", False)),
            ("cross-carrier evidence treated returned capture as closure", set_field("selected_cross_carrier_evidence_returned_capture_not_portable_verification_closure", False)),
            ("cross-carrier evidence redacted official strings", set_field("selected_cross_carrier_evidence_official_enum_scope_strings_redacted", True)),
            ("predecessor cross-carrier evidence failure missing", set_fields({"predecessor_cross_carrier_evidence_failure_preserved": False, "selected_cross_carrier_evidence_predecessor_failure_preserved": False})),
            ("predecessor cross-carrier evidence repaired", set_field("predecessor_cross_carrier_evidence_repaired", True)),
            ("predecessor cross-carrier evidence hidden", set_field("predecessor_cross_carrier_evidence_hidden", True)),
            ("predecessor cross-carrier evidence claimed passed", set_field("predecessor_cross_carrier_evidence_claimed_passed", True)),
            ("predecessor external-result v1 failure missing", set_field("predecessor_external_result_v1_failure_preserved", False)),
            ("predecessor external-result v1 repaired", set_field("predecessor_external_result_v1_repaired", True)),
            ("predecessor external-result v1 hidden", set_field("predecessor_external_result_v1_hidden", True)),
            ("predecessor external-result v1 claimed passed", set_field("predecessor_external_result_v1_claimed_passed", True)),
            ("cross-carrier evidence boundary basis missing", clear_field("selected_cross_carrier_evidence_boundary_basis")),
            ("second-carrier external result basis missing", clear_field("selected_second_carrier_external_result_basis")),
            ("second-carrier external result not recorded", set_field("selected_second_carrier_external_result_result_outcome", "NOT_RECORDED")),
            ("second-carrier external result failed checks", set_field("selected_second_carrier_external_result_failed_check_count", 1)),
            ("second-carrier external result created closure", set_field("selected_second_carrier_external_result_already_created_portable_verification_closure", True)),
            ("second-carrier external result treated external result as closure", set_field("selected_second_carrier_external_result_treated_external_result_as_portable_verification_closure", True)),
            ("second-carrier external result treated string zero as doctrine", set_field("selected_second_carrier_external_result_treated_string_zero_as_doctrine", True)),
            ("second-carrier verification basis missing", clear_field("selected_second_carrier_verification_basis")),
            ("second-carrier verification not recorded", set_field("selected_second_carrier_verification_result_outcome", "NOT_RECORDED")),
            ("second-carrier verification failed checks", set_field("selected_second_carrier_verification_failed_check_count", 1)),
            ("second-carrier success basis missing", clear_field("selected_second_carrier_success_basis")),
            ("second-carrier success not recorded", set_field("selected_second_carrier_success_result_outcome", "NOT_RECORDED")),
            ("second-carrier success failed checks", set_field("selected_second_carrier_success_failed_check_count", 1)),
            ("second-carrier result basis missing", clear_field("selected_second_carrier_result_basis")),
            ("second-carrier result not recorded", set_field("selected_second_carrier_result_result_outcome", "NOT_RECORDED")),
            ("second-carrier result failed checks", set_field("selected_second_carrier_result_failed_check_count", 1)),
            ("returned capture intake basis missing", clear_field("selected_returned_second_carrier_live_capture_intake_basis")),
            ("returned capture intake not preserved", set_field("selected_returned_capture_intake_preserved", False)),
            ("returned capture treated as closure", set_field("returned_capture_treated_as_portable_verification_closure", True)),
            ("zero exit code treated as closure", set_field("zero_exit_code_treated_as_portable_verification_closure", True)),
            ("string zero treated as closure", set_field("string_zero_treated_as_portable_verification_closure", True)),
            ("OK output treated as closure", set_field("ok_output_treated_as_portable_verification_closure", True)),
            ("Ran 7 tests treated as closure", set_field("ran_7_tests_treated_as_portable_verification_closure", True)),
            ("placeholder carrier fields repaired", set_field("selected_returned_capture_placeholder_fields_unrepaired", False)),
            ("returned capture material missing", clear_field("selected_returned_capture_material_basis")),
            ("returned zip path missing", set_field("selected_returned_capture_zip_path", "")),
            ("returned hash path missing", set_field("selected_returned_capture_hash_path", "")),
            ("returned extracted directory missing", set_field("selected_returned_capture_extracted_directory_path", "")),
            ("returned combined terminal log missing", set_field("selected_returned_capture_combined_terminal_log_path", "")),
            ("returned exit code missing", clear_field("selected_returned_capture_exit_code")),
            ("returned command text missing", set_field("selected_returned_capture_command_text", "")),
            ("returned timestamps missing", set_field("selected_returned_capture_started_at", "")),
            ("second-carrier output capture basis missing", clear_field("selected_second_carrier_output_capture_basis")),
            ("second-carrier output capture not recorded", set_field("selected_second_carrier_output_capture_result_outcome", "NOT_RECORDED")),
            ("second-carrier output capture failed checks", set_field("selected_second_carrier_output_capture_failed_check_count", 1)),
            ("boundary treated as closure", set_field("portable_verification_closure_boundary_treated_as_portable_verification_closure", True)),
            ("boundary treated as final completion", set_field("portable_verification_closure_boundary_treated_as_final_completion", True)),
            ("boundary treated as source transfer", set_field("portable_verification_closure_boundary_treated_as_source_transfer", True)),
            ("boundary treated as source receipt", set_field("portable_verification_closure_boundary_treated_as_source_receipt", True)),
            ("boundary treated as reception authorization", set_field("portable_verification_closure_boundary_treated_as_reception_authorization", True)),
            ("boundary treated as source", set_field("portable_verification_closure_boundary_treated_as_source", True)),
            ("boundary treated as authority", set_field("portable_verification_closure_boundary_treated_as_authority", True)),
            ("boundary treated as currentness", set_field("portable_verification_closure_boundary_treated_as_currentness", True)),
            ("boundary treated as runtime", set_field("portable_verification_closure_boundary_treated_as_runtime", True)),
            ("boundary treated as continuation", set_field("portable_verification_closure_boundary_treated_as_continuation", True)),
            ("boundary treated as reusable permission", set_field("portable_verification_closure_boundary_treated_as_reusable_permission", True)),
            ("boundary treated as follow-on work", set_field("portable_verification_closure_boundary_treated_as_follow_on_work", True)),
            ("portable verification closure created", set_non_claim("portable_verification_closure_created")),
            ("final completion claimed", set_non_claim("final_completion_claimed")),
            ("source transfer occurred", set_non_claim("source_transfer_occurred")),
            ("source receipt occurred", set_non_claim("source_receipt_occurred")),
            ("reception authorization created", set_non_claim("reception_authorization_created")),
            ("source created", set_non_claim("source_created")),
            ("authority created", set_non_claim("authority_created")),
            ("currentness created", set_non_claim("currentness_created")),
            ("runtime hosting created", set_non_claim("runtime_hosting_created")),
            ("deployment created", set_non_claim("deployment_created")),
            ("public release created", set_non_claim("public_release_created")),
            ("operation permission created", set_non_claim("operation_permission_created")),
            ("continuation authorized", set_non_claim("continuation_authorized")),
            ("reusable permission created", set_non_claim("reusable_permission_created")),
            ("derivative reception authorized", set_non_claim("derivative_reception_authorized")),
            ("vessel relation authorized", set_non_claim("vessel_relation_authorized")),
            ("another reception request authorized", set_non_claim("another_reception_request_authorized")),
            ("follow-on work authorized", set_non_claim("follow_on_work_authorized")),
            ("receiving carrier treated as authority", set_non_claim("receiving_carrier_treated_as_authority")),
            ("artifact existence treated as closure authority", set_non_claim("artifact_existence_treated_as_portable_verification_closure_authority")),
            ("artifact path treated as currentness", set_non_claim("artifact_path_treated_as_currentness")),
            ("repo-local availability treated as authority", set_non_claim("repo_local_availability_treated_as_portable_verification_closure_authority")),
            ("hidden repo state used as content", set_non_claim("hidden_repo_state_used_as_portable_verification_closure_content")),
            ("hidden repo state used as authority", set_non_claim("hidden_repo_state_used_as_portable_verification_closure_authority")),
            ("selected basis not reference-shaped", set_field("reference_shaped_input_posture", False)),
            ("raw full prior artifact body returned", set_non_claim("raw_full_prior_artifact_body_returned")),
            ("v1 packet-emission repaired", set_field("v1_packet_emission_repaired", True)),
            ("first success-boundary hidden", set_field("first_success_boundary_test_hidden", True)),
            ("first result-boundary claimed passed", set_field("first_result_boundary_resolver_claimed_passed", True)),
            ("command report lineage current report artifact", set_field("command_report_lineage_treated_as_current_report_artifact", True)),
            ("command report lineage source", set_field("command_report_lineage_treated_as_source", True)),
            ("command report lineage authority", set_field("command_report_lineage_treated_as_authority", True)),
            ("command report lineage currentness", set_field("command_report_lineage_treated_as_currentness", True)),
            ("consumed request reopened", set_non_claim("consumed_request_reopened")),
            ("authorization token reused", set_non_claim("authorization_token_reused")),
            ("full prior artifact body emitted outside bounded posture", set_field("full_prior_artifact_body_emitted_outside_bounded_portable_verification_closure_boundary", True)),
            ("string zero representation turned into doctrine", set_field("selected_returned_capture_declared_exit_code", "doctrine")),
            ("artifacts mutated", set_non_claim("prior_artifacts_mutated")),
            ("returned capture material mutated", set_non_claim("returned_capture_material_mutated")),
            ("required non-claim missing", remove_non_claim("source_created")),
        )
        for label, mutate in cases:
            with self.subTest(label=label):
                request = build_request()
                mutate(request)
                mutated_snapshot = copy.deepcopy(request)
                result = resolved(request)
                self.assertEqual(request, mutated_snapshot)
                self.assert_blocked_result(result)
                claims = non_claims(result)
                self.assertIs(claims["zero_exit_code_treated_as_portable_verification_closure"], False)
                self.assertIs(claims["string_zero_treated_as_portable_verification_closure"], False)
                self.assertIs(claims["string_zero_representation_turned_into_doctrine"], False)
                self.assertIs(claims["ok_output_treated_as_portable_verification_closure"], False)
                self.assertIs(claims["ran_7_tests_treated_as_portable_verification_closure"], False)
                self.assertIs(claims["returned_capture_treated_as_portable_verification_closure"], False)
                self.assertIs(claims["consumed_request_reopened"], False)
                self.assertIs(claims["authorization_token_reused"], False)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request_path = tmp_path / "valid_request.json"
            request_path.write_text(json.dumps(build_request(), indent=2), encoding="utf-8")
            result = resolver.resolve_portable_source_body_verification_portable_verification_closure_boundary_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], RECORDED)
            self.assertEqual(summary(result)["result_version"], "0.1.0")
            self.assertEqual(
                summary(result)["resolver_module"],
                "resolve_portable_source_body_verification_portable_verification_closure_boundary",
            )

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            self.assert_path_blocks_or_raises(malformed_path)

            array_path = tmp_path / "array.json"
            array_path.write_text(json.dumps([build_request()]), encoding="utf-8")
            self.assert_path_blocks_or_raises(array_path)

            missing_path = tmp_path / "missing.json"
            self.assert_path_blocks_or_raises(missing_path)

            output_root = (
                tmp_path
                / "artifacts"
                / "integrity_host_v0_min_coexistence_portable_source_body_verification_portable_verification_closure_boundary"
            )
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_portable_source_body_verification_portable_verification_closure_boundary_result(
                    result
                )
                second_path = resolver.write_portable_source_body_verification_portable_verification_closure_boundary_result(
                    result
                )
            self.assertEqual(first_path.parent, output_root)
            self.assertEqual(second_path.parent, output_root)
            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertTrue(second_path.stem.endswith("_001"))
            self.assertEqual(json.loads(first_path.read_text(encoding="utf-8"))["outcome"], RECORDED)
            self.assertEqual(json.loads(second_path.read_text(encoding="utf-8"))["outcome"], RECORDED)
            forbidden_roots = (
                "actual_second_carrier_live_capture",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_cross_carrier_evidence",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_cross_carrier_evidence_boundary",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_external_result",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_verification",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_success",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_result",
                "runtime",
                "deployment",
                "public_release",
            )
            for forbidden in forbidden_roots:
                self.assertNotIn(forbidden, first_path.parts)
                self.assertNotIn(forbidden, second_path.parts)

    def test_non_mutation_of_input_sections(self) -> None:
        request = build_request()
        for field in SELECTED_BASIS_KEYS:
            request[field]["non_mutation_marker"] = {"kept": True}
        for field in POSTURE_KEYS:
            request[field]["non_mutation_marker"] = ["kept"]
        request["portable_verification_closure_boundary_scope"] = {
            "scope_values": list(SUPPORTED_SCOPE),
            "non_mutation_marker": False,
        }
        request["declared_non_claims"]["non_mutation_marker"] = False
        snapshot = copy.deepcopy(request)
        result = resolved(request)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(request, snapshot)

    def test_predecessor_failure_preservation(self) -> None:
        result = resolved(build_request())
        compact = summary(result)
        predecessor = result["selected_predecessor_failure_basis"]
        claims = non_claims(result)

        self.assertIs(compact["predecessor_cross_carrier_evidence_failure_preserved"], True)
        self.assertIs(statement(result)["predecessor_cross_carrier_evidence_failure_preserved"], True)
        self.assertIs(predecessor["predecessor_cross_carrier_evidence_failure_preserved"], True)
        self.assertIs(predecessor["predecessor_cross_carrier_evidence_not_repaired"], True)
        self.assertIs(predecessor["predecessor_cross_carrier_evidence_not_hidden"], True)
        self.assertIs(predecessor["predecessor_cross_carrier_evidence_not_claimed_passed"], True)
        self.assertIs(claims["predecessor_cross_carrier_evidence_repaired"], False)
        self.assertIs(claims["predecessor_cross_carrier_evidence_hidden"], False)
        self.assertIs(claims["predecessor_cross_carrier_evidence_claimed_passed"], False)
        self.assertIs(compact["predecessor_external_result_v1_failure_preserved"], True)
        self.assertIs(statement(result)["predecessor_external_result_v1_failure_preserved"], True)
        self.assertIs(predecessor["predecessor_external_result_v1_failure_preserved"], True)
        self.assertIs(predecessor["predecessor_external_result_v1_not_repaired"], True)
        self.assertIs(predecessor["predecessor_external_result_v1_not_hidden"], True)
        self.assertIs(predecessor["predecessor_external_result_v1_not_claimed_passed"], True)
        self.assertIs(claims["predecessor_external_result_v1_repaired"], False)
        self.assertIs(claims["predecessor_external_result_v1_hidden"], False)
        self.assertIs(claims["predecessor_external_result_v1_claimed_passed"], False)
        self.assertIs(statement(result)["first_success_boundary_test_failure_preserved"], True)
        self.assertIs(predecessor["first_success_boundary_test_failure_preserved"], True)
        self.assertIs(claims["first_success_boundary_test_repaired"], False)
        self.assertIs(claims["first_success_boundary_test_hidden"], False)
        self.assertIs(claims["first_success_boundary_test_claimed_passed"], False)
        self.assertIs(compact["v1_packet_emission_predecessor_failure_preserved"], True)
        self.assertIs(predecessor["v1_packet_emission_boundary_failure_preserved"], True)
        self.assertIs(claims["v1_packet_emission_repaired"], False)
        self.assertIs(claims["v1_packet_emission_hidden"], False)
        self.assertIs(claims["v1_packet_emission_claimed_passed"], False)
        self.assertIs(statement(result)["first_result_boundary_resolver_failure_preserved"], True)
        self.assertIs(
            compact["first_result_boundary_resolver_preserved_as_failed_predecessor"],
            True,
        )
        self.assertIs(predecessor["first_result_boundary_resolver_failure_preserved"], True)
        self.assertIs(claims["first_result_boundary_resolver_repaired"], False)
        self.assertIs(claims["first_result_boundary_resolver_hidden"], False)
        self.assertIs(claims["first_result_boundary_resolver_claimed_passed"], False)


if __name__ == "__main__":
    unittest.main()
