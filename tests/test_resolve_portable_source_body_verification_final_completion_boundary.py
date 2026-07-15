"""Executable checks for final-completion-boundary posture only.

This suite is downstream of portable verification closure. It verifies that the
resolver records one future final-completion review step only. Final completion,
source transfer, source receipt, reception authorization, source, authority,
currentness, runtime, deployment, public release, operation permission,
continuation, reusable permission, and follow-on work are not created.

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

import resolve_portable_source_body_verification_final_completion_boundary as resolver


RECORDED = resolver.OUTCOME_RECORDED
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = set(resolver.OUTCOME_FAMILY)
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_FINAL_COMPLETION_BOUNDARY_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
TRUE_RECORDED_FIELDS = tuple(resolver.ALLOWED_TRUE_RECORDED_FIELDS)
SELECTED_BASIS_KEYS = tuple(resolver.SELECTED_BASIS_KEYS)
POSTURE_KEYS = tuple(resolver.POSTURE_KEYS)

RAW_SENTINELS = (
    "RAW_FINAL_COMPLETION_BOUNDARY_BODY_MUST_NOT_RETURN",
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
    "hostile-raw-final-completion-body-value",
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
    "[bounded-final-completion-boundary-redacted]",
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
    "STRING_ZERO_NOT_FINAL_COMPLETION",
    "FINAL_COMPLETION_NOT_CREATED",
    "FINAL_COMPLETION_BOUNDARY_NOT_FINAL_COMPLETION",
    "PORTABLE_VERIFICATION_CLOSURE_NOT_FINAL_COMPLETION",
)

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_final_completion_boundary_metadata",
    "declared_final_completion_boundary_question",
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
    "final_completion_boundary_scope",
    "final_completion_boundary_checks",
    "final_completion_boundary_statement",
    "final_completion_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_final_completion_boundary_summary",
)

REPRESENTATIVE_BLOCK_CODES = (
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
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_FINAL_COMPLETION_BOUNDARY",
    "ARTIFACTS_MUTATED",
    "RETURNED_CAPTURE_MATERIAL_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_FINAL_COMPLETION_BOUNDARY_SCOPE",
)


def build_request(**overrides: Any) -> dict[str, Any]:
    return resolver.build_declared_portable_source_body_verification_final_completion_boundary_request(
        **overrides
    )


def resolved(request: Any) -> dict[str, Any]:
    return resolver.resolve_portable_source_body_verification_final_completion_boundary(request)


def statement(result: dict[str, Any]) -> dict[str, Any]:
    return result.get("final_completion_boundary_statement", {})


def non_claims(result: dict[str, Any]) -> dict[str, Any]:
    return result.get("non_claims", {})


def checks(result: dict[str, Any]) -> list[dict[str, Any]]:
    return list(result.get("final_completion_boundary_checks", []))


def summary(result: dict[str, Any]) -> dict[str, Any]:
    return result.get(
        "portable_source_body_verification_final_completion_boundary_summary",
        {},
    )


def scope_values(result: dict[str, Any]) -> list[str]:
    scope = result.get("final_completion_boundary_scope", {})
    if isinstance(scope, dict):
        return list(scope.get("scope_values", []))
    return list(scope)


def serialized(result: dict[str, Any]) -> str:
    return json.dumps(result, sort_keys=True)


def set_field(name: str, value: Any) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request[name] = value

    return mutate


def clear_field(name: str) -> Callable[[dict[str, Any]], None]:
    return set_field(name, None)


def set_nested_basis(
    basis_name: str,
    field_name: str,
    value: Any,
    shortcut_name: str | None = None,
) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        if isinstance(request.get(basis_name), dict):
            request[basis_name][field_name] = value
        if shortcut_name is not None:
            request[shortcut_name] = value

    return mutate


def set_non_claim_probe(name: str, value: Any = True) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request[name] = value

    return mutate


def remove_non_claim(name: str) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request["declared_non_claims"].pop(name, None)

    return mutate


def combine(*mutators: Callable[[dict[str, Any]], None]) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        for mutator in mutators:
            mutator(request)

    return mutate


class FinalCompletionBoundaryTest(unittest.TestCase):
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
            result.get("final_completion_boundary_non_meaning", {}),
        ):
            for key, value in section.items():
                self.assertIs(type(value), bool, key)
        for posture_key in POSTURE_KEYS:
            posture = result.get(posture_key, {})
            for generated_key in ("declared", "bounded", "basis_declared"):
                if generated_key in posture:
                    self.assertIs(type(posture[generated_key]), bool, posture_key)

    def assert_no_raw_or_hidden_sentinels(self, result: dict[str, Any]) -> None:
        body = serialized(result)
        for sentinel in RAW_SENTINELS:
            self.assertNotIn(sentinel, body)
        for hostile in HOSTILE_VALUES:
            self.assertNotIn(hostile, body)

    def assert_official_scope_strings_preserved(self, result: dict[str, Any]) -> None:
        emitted_scope = scope_values(result)
        for official in OFFICIAL_SCOPE_VALUES:
            self.assertIn(official, emitted_scope)
        for value in emitted_scope:
            self.assertNotIn(value, REDACTION_PLACEHOLDERS)
        for official in SUPPORTED_SCOPE:
            self.assertIn(official, emitted_scope)
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

    def assert_non_claims_false(self, result: dict[str, Any]) -> None:
        claims = non_claims(result)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(claims.get(key), False, key)

    def assert_no_forbidden_creation(self, result: dict[str, Any]) -> None:
        claims = non_claims(result)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIsNot(claims.get(key), True, key)
        posture = statement(result)
        for key in (
            "final_completion_not_created",
            "final_completion_boundary_not_final_completion",
            "portable_verification_closure_not_final_completion",
            "zero_exit_code_not_final_completion",
            "string_zero_not_final_completion",
            "ok_output_not_final_completion",
            "ran_7_tests_not_final_completion",
            "returned_capture_not_final_completion",
            "source_not_created",
            "authority_not_created",
            "currentness_not_created",
            "runtime_not_created",
            "deployment_not_created",
            "public_release_not_created",
            "operation_permission_not_created",
            "follow_on_work_not_authorized",
            "hidden_repo_state_excluded",
            "hidden_repo_state_not_used_as_final_completion_authority",
            "repo_local_availability_not_final_completion_authority",
            "authorization_token_reuse_blocked",
            "consumed_request_token_remains_closed",
        ):
            self.assertIs(posture.get(key), True, key)

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
            self.assertIsNot(claims.get(key), True, key)

    def assert_blocked_result(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertIsInstance(result.get("block"), dict)
        self.assertIsNotNone(result["block"].get("block_code"))
        self.assert_public_block_codes(result)
        self.assert_no_forbidden_creation(result)
        self.assert_predecessors_not_repaired_hidden_or_claimed_passed(result)
        self.assert_generated_booleans_are_bool(result)

    def assert_path_blocks_or_raises(self, path: Path) -> None:
        try:
            result = resolver.resolve_portable_source_body_verification_final_completion_boundary_from_path(
                path
            )
        except resolver.PortableSourceBodyVerificationFinalCompletionBoundaryError:
            return
        self.assert_blocked_result(result)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_portable_source_body_verification_final_completion_boundary",
            "resolve_portable_source_body_verification_final_completion_boundary_from_path",
            "write_portable_source_body_verification_final_completion_boundary_result",
            "build_portable_source_body_verification_final_completion_boundary_summary",
            "build_declared_portable_source_body_verification_final_completion_boundary_request",
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
            "SUPPORTED_FINAL_COMPLETION_BOUNDARY_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_portable_source_body_verification_final_completion_boundary",
        )
        self.assertEqual(
            resolver.SUPPORTED_FINAL_COMPLETION_BOUNDARY_SCOPE,
            resolver.SUPPORTED_SCOPE_VALUES,
        )
        self.assertTrue(
            str(resolver.OUTPUT_ROOT)
            .replace("\\", "/")
            .endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_portable_source_body_verification_"
                "final_completion_boundary"
            )
        )
        for official in OFFICIAL_SCOPE_VALUES:
            self.assertIn(official, resolver.SUPPORTED_FINAL_COMPLETION_BOUNDARY_SCOPE)
        for code in REPRESENTATIVE_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_successful_recorded_result_from_no_argument_builder(self) -> None:
        request = build_request()
        request_snapshot = copy.deepcopy(request)
        result = resolved(request)
        compact = resolver.build_portable_source_body_verification_final_completion_boundary_summary(
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
            "resolve_portable_source_body_verification_final_completion_boundary",
        )
        self.assertEqual(
            compact["request_id"],
            request["final_completion_boundary_request_id"],
        )
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)

        for key in TRUE_RECORDED_FIELDS:
            self.assertIs(statement(result).get(key), True, key)
        self.assert_non_claims_false(result)
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

        request = build_request(final_completion_boundary_scope=list(SUPPORTED_SCOPE))
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
            "raw_final_completion_body": HOSTILE_VALUES[12],
            "capture_body": HOSTILE_VALUES[13],
            "cross_carrier_evidence_body": HOSTILE_VALUES[14],
            "portable_verification_closure_body": HOSTILE_VALUES[15],
            "final_completion_body": HOSTILE_VALUES[16],
            "source_body": HOSTILE_VALUES[17],
            "authority_body": HOSTILE_VALUES[18],
            "hidden_repo_state": "hidden-state:" + RAW_SENTINELS[2],
            "current_working_tree": HOSTILE_VALUES[19],
            "local_cache": HOSTILE_VALUES[20],
            "repo_local_only_dependency": HOSTILE_VALUES[21],
            "nested": {
                "items": [
                    RAW_SENTINELS[0],
                    {"deeper": RAW_SENTINELS[1]},
                    {"official_scope": "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED"},
                ]
            },
        }
        for section in (
            "selected_portable_verification_closure_basis",
            "selected_portable_verification_closure_terminal_summary_basis",
            "selected_portable_verification_closure_boundary_basis",
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
            request[section].update(copy.deepcopy(hostile_payload))

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
        for key in (
            "hidden_repo_state_used_as_final_completion_content",
            "hidden_repo_state_used_as_final_completion_authority",
            "repo_local_availability_treated_as_final_completion_authority",
            "receiving_carrier_treated_as_authority",
            "artifact_existence_treated_as_final_completion_authority",
            "artifact_path_treated_as_currentness",
            "string_zero_treated_as_final_completion",
            "string_zero_representation_turned_into_doctrine",
        ):
            self.assertIs(claims.get(key), False, key)

    def test_representative_blocking_behavior(self) -> None:
        block_cases: tuple[tuple[str, Any], ...] = (
            ("explicit block intent", set_field("final_completion_boundary_intent", "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_BOUNDARY")),
            ("missing request", None),
            ("non-mapping request", ["not", "a", "mapping"]),
            ("unsupported intent", set_field("final_completion_boundary_intent", "UNSUPPORTED")),
            ("unsupported scope", set_field("final_completion_boundary_scope", ["UNSUPPORTED_SCOPE"])),
            ("missing portable verification closure basis", clear_field("selected_portable_verification_closure_basis")),
            ("portable verification closure not recorded", set_nested_basis("selected_portable_verification_closure_basis", "outcome", "NO", "selected_portable_verification_closure_result_outcome")),
            ("portable verification closure failed checks", set_nested_basis("selected_portable_verification_closure_basis", "failed_check_count", 1, "selected_portable_verification_closure_failed_check_count")),
            ("portable verification closure version not 0.1.0", set_nested_basis("selected_portable_verification_closure_basis", "result_version", "9.9.9", "selected_portable_verification_closure_result_version")),
            ("portable verification closure did not record bounded closure", set_nested_basis("selected_portable_verification_closure_basis", "bounded_portable_verification_closure_recorded", False, "selected_portable_verification_closure_bounded_closure_recorded")),
            ("portable verification closure already created final completion", set_field("selected_portable_verification_closure_already_created_final_completion", True)),
            ("portable verification closure treated as final completion", set_field("selected_portable_verification_closure_treated_as_final_completion", True)),
            ("portable verification closure treated as source transfer", set_field("selected_portable_verification_closure_treated_as_source_transfer", True)),
            ("portable verification closure treated as source receipt", set_field("selected_portable_verification_closure_treated_as_source_receipt", True)),
            ("portable verification closure treated as reception authorization", set_field("selected_portable_verification_closure_treated_as_reception_authorization", True)),
            ("portable verification closure treated as source", set_field("selected_portable_verification_closure_treated_as_source", True)),
            ("portable verification closure treated as authority", set_field("selected_portable_verification_closure_treated_as_authority", True)),
            ("portable verification closure treated as currentness", set_field("selected_portable_verification_closure_treated_as_currentness", True)),
            ("portable verification closure treated as runtime", set_field("selected_portable_verification_closure_treated_as_runtime", True)),
            ("portable verification closure treated as deployment", set_field("selected_portable_verification_closure_treated_as_deployment", True)),
            ("portable verification closure treated as public release", set_field("selected_portable_verification_closure_treated_as_public_release", True)),
            ("portable verification closure treated as operation permission", set_field("selected_portable_verification_closure_treated_as_operation_permission", True)),
            ("portable verification closure treated as follow-on work", set_field("selected_portable_verification_closure_treated_as_follow_on_work", True)),
            ("portable verification closure treated zero exit code as final completion", set_field("selected_portable_verification_closure_treated_zero_exit_code_as_final_completion", True)),
            ("portable verification closure treated string zero as final completion", set_field("selected_portable_verification_closure_treated_string_zero_as_final_completion", True)),
            ("portable verification closure treated string zero as doctrine", set_field("selected_portable_verification_closure_treated_string_zero_as_doctrine", True)),
            ("portable verification closure treated OK as final completion", set_field("selected_portable_verification_closure_treated_ok_as_final_completion", True)),
            ("portable verification closure treated Ran 7 tests as final completion", set_field("selected_portable_verification_closure_treated_ran_7_tests_as_final_completion", True)),
            ("portable verification closure treated returned capture as final completion", set_field("selected_portable_verification_closure_treated_returned_capture_as_final_completion", True)),
            ("portable verification closure redacted official enum strings", set_field("selected_portable_verification_closure_official_enum_scope_strings_redacted", True)),
            ("predecessor cross-carrier evidence failure missing", combine(set_field("predecessor_cross_carrier_evidence_failure_preserved", False), set_field("selected_portable_verification_closure_predecessor_cross_carrier_evidence_failure_preserved", False))),
            ("predecessor external-result v1 failure missing", set_field("predecessor_external_result_v1_failure_preserved", False)),
            ("portable-verification-closure-boundary basis missing", clear_field("selected_portable_verification_closure_boundary_basis")),
            ("cross-carrier evidence basis missing", clear_field("selected_cross_carrier_evidence_basis")),
            ("cross-carrier evidence not recorded", set_nested_basis("selected_cross_carrier_evidence_basis", "outcome", "NO", "selected_cross_carrier_evidence_result_outcome")),
            ("cross-carrier evidence failed checks", set_field("selected_cross_carrier_evidence_failed_check_count", 1)),
            ("second-carrier external result basis missing", clear_field("selected_second_carrier_external_result_basis")),
            ("second-carrier external result not recorded", set_nested_basis("selected_second_carrier_external_result_basis", "outcome", "NO", "selected_second_carrier_external_result_result_outcome")),
            ("second-carrier external result failed checks", set_field("selected_second_carrier_external_result_failed_check_count", 1)),
            ("second-carrier verification basis missing", clear_field("selected_second_carrier_verification_basis")),
            ("second-carrier verification not recorded", set_nested_basis("selected_second_carrier_verification_basis", "outcome", "NO", "selected_second_carrier_verification_result_outcome")),
            ("second-carrier success basis missing", clear_field("selected_second_carrier_success_basis")),
            ("second-carrier success not recorded", set_nested_basis("selected_second_carrier_success_basis", "outcome", "NO", "selected_second_carrier_success_result_outcome")),
            ("second-carrier result basis missing", clear_field("selected_second_carrier_result_basis")),
            ("second-carrier result not recorded", set_nested_basis("selected_second_carrier_result_basis", "outcome", "NO", "selected_second_carrier_result_result_outcome")),
            ("returned capture intake basis missing", clear_field("selected_returned_second_carrier_live_capture_intake_basis")),
            ("returned capture intake not preserved", set_field("selected_returned_capture_intake_preserved", False)),
            ("returned capture treated as final completion", set_field("selected_returned_capture_intake_capture_only", False)),
            ("zero exit code treated as final completion", set_non_claim_probe("zero_exit_code_treated_as_final_completion")),
            ("string zero treated as final completion", set_non_claim_probe("string_zero_treated_as_final_completion")),
            ("OK output treated as final completion", set_non_claim_probe("ok_output_treated_as_final_completion")),
            ("Ran 7 tests treated as final completion", set_non_claim_probe("ran_7_tests_treated_as_final_completion")),
            ("placeholder carrier fields repaired", set_field("selected_returned_capture_placeholder_fields_unrepaired", False)),
            ("returned capture material missing", clear_field("selected_returned_capture_material_basis")),
            ("returned zip path missing", clear_field("selected_returned_capture_zip_path")),
            ("returned hash path missing", clear_field("selected_returned_capture_hash_path")),
            ("returned extracted directory missing", clear_field("selected_returned_capture_extracted_directory_path")),
            ("returned combined terminal log missing", clear_field("selected_returned_capture_combined_terminal_log_path")),
            ("returned exit code missing", clear_field("selected_returned_capture_exit_code")),
            ("returned command text missing", clear_field("selected_returned_capture_command_text")),
            ("returned timestamps missing", clear_field("selected_returned_capture_started_at")),
            ("second-carrier output capture basis missing", clear_field("selected_second_carrier_output_capture_basis")),
            ("second-carrier output capture not recorded", set_nested_basis("selected_second_carrier_output_capture_basis", "outcome", "NO", "selected_second_carrier_output_capture_result_outcome")),
            ("second-carrier output capture failed checks", set_field("selected_second_carrier_output_capture_failed_check_count", 1)),
            ("final-completion boundary treated as final completion", set_non_claim_probe("final_completion_boundary_treated_as_final_completion")),
            ("final-completion boundary treated as source transfer", set_non_claim_probe("final_completion_boundary_treated_as_source_transfer")),
            ("final-completion boundary treated as source receipt", set_non_claim_probe("final_completion_boundary_treated_as_source_receipt")),
            ("final-completion boundary treated as reception authorization", set_non_claim_probe("final_completion_boundary_treated_as_reception_authorization")),
            ("final-completion boundary treated as source", set_non_claim_probe("final_completion_boundary_treated_as_source")),
            ("final-completion boundary treated as authority", set_non_claim_probe("final_completion_boundary_treated_as_authority")),
            ("final-completion boundary treated as currentness", set_non_claim_probe("final_completion_boundary_treated_as_currentness")),
            ("final-completion boundary treated as runtime", set_non_claim_probe("final_completion_boundary_treated_as_runtime")),
            ("final-completion boundary treated as deployment", set_non_claim_probe("final_completion_boundary_treated_as_deployment")),
            ("final-completion boundary treated as public release", set_non_claim_probe("final_completion_boundary_treated_as_public_release")),
            ("final-completion boundary treated as operation permission", set_non_claim_probe("final_completion_boundary_treated_as_operation_permission")),
            ("final-completion boundary treated as continuation", set_non_claim_probe("final_completion_boundary_treated_as_continuation")),
            ("final-completion boundary treated as reusable permission", set_non_claim_probe("final_completion_boundary_treated_as_reusable_permission")),
            ("final-completion boundary treated as follow-on work", set_non_claim_probe("final_completion_boundary_treated_as_follow_on_work")),
            ("final completion created", set_non_claim_probe("final_completion_created")),
            ("source transfer occurred", set_non_claim_probe("source_transfer_occurred")),
            ("source receipt occurred", set_non_claim_probe("source_receipt_occurred")),
            ("reception authorization created", set_non_claim_probe("reception_authorization_created")),
            ("source created", set_non_claim_probe("source_created")),
            ("authority created", set_non_claim_probe("authority_created")),
            ("currentness created", set_non_claim_probe("currentness_created")),
            ("runtime hosting created", set_non_claim_probe("runtime_hosting_created")),
            ("deployment created", set_non_claim_probe("deployment_created")),
            ("public release created", set_non_claim_probe("public_release_created")),
            ("operation permission created", set_non_claim_probe("operation_permission_created")),
            ("continuation authorized", set_non_claim_probe("continuation_authorized")),
            ("reusable permission created", set_non_claim_probe("reusable_permission_created")),
            ("follow-on work authorized", set_non_claim_probe("follow_on_work_authorized")),
            ("receiving carrier treated as authority", set_non_claim_probe("receiving_carrier_treated_as_authority")),
            ("artifact existence treated as final-completion authority", set_non_claim_probe("artifact_existence_treated_as_final_completion_authority")),
            ("artifact path treated as currentness", set_non_claim_probe("artifact_path_treated_as_currentness")),
            ("repo-local availability treated as final-completion authority", set_non_claim_probe("repo_local_availability_treated_as_final_completion_authority")),
            ("hidden repo state used as final-completion content", set_non_claim_probe("hidden_repo_state_used_as_final_completion_content")),
            ("hidden repo state used as final-completion authority", set_non_claim_probe("hidden_repo_state_used_as_final_completion_authority")),
            ("selected basis not reference-shaped", set_field("reference_shaped_input_posture", False)),
            ("raw full prior artifact body returned", set_non_claim_probe("raw_full_prior_artifact_body_returned")),
            ("predecessor failure evidence hidden", set_field("hidden", True)),
            ("predecessor failure evidence repaired", set_field("repaired", True)),
            ("predecessor failure evidence claimed passed", set_field("claimed_passed", True)),
            ("first success-boundary test hidden", set_non_claim_probe("first_success_boundary_test_hidden")),
            ("first success-boundary test repaired", set_non_claim_probe("first_success_boundary_test_repaired")),
            ("first success-boundary test claimed passed", set_non_claim_probe("first_success_boundary_test_claimed_passed")),
            ("first result-boundary resolver hidden", set_non_claim_probe("first_result_boundary_resolver_hidden")),
            ("first result-boundary resolver repaired", set_non_claim_probe("first_result_boundary_resolver_repaired")),
            ("first result-boundary resolver claimed passed", set_non_claim_probe("first_result_boundary_resolver_claimed_passed")),
            ("command report lineage treated as current report artifact", set_field("command_report_lineage_treated_as_current_report_artifact", True)),
            ("command report lineage treated as source", set_field("command_report_lineage_treated_as_source", True)),
            ("command report lineage treated as authority", set_field("command_report_lineage_treated_as_authority", True)),
            ("command report lineage treated as currentness", set_field("command_report_lineage_treated_as_currentness", True)),
            ("consumed request reopened", set_non_claim_probe("consumed_request_reopened")),
            ("authorization token reused", set_non_claim_probe("authorization_token_reused")),
            ("full prior artifact body emitted outside boundary", set_field("full_prior_artifact_body_emitted_outside_bounded_final_completion_boundary", True)),
            ("string zero representation turned into doctrine", set_non_claim_probe("string_zero_representation_turned_into_doctrine")),
            ("artifacts mutated", set_field("artifacts_mutated", True)),
            ("returned capture material mutated", set_non_claim_probe("returned_capture_material_mutated")),
            ("required non-claim missing", remove_non_claim("final_completion_created")),
        )

        for label, mutator in block_cases:
            with self.subTest(label=label):
                if mutator is None or not callable(mutator):
                    result = resolved(mutator)
                else:
                    request = build_request()
                    mutator(request)
                    result = resolved(request)
                self.assert_blocked_result(result)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request_path = tmp_path / "request.json"
            request = build_request()
            request_path.write_text(json.dumps(request), encoding="utf-8")

            result = resolver.resolve_portable_source_body_verification_final_completion_boundary_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], RECORDED)
            self.assertEqual(summary(result)["result_version"], "0.1.0")
            self.assertEqual(
                summary(result)["resolver_module"],
                "resolve_portable_source_body_verification_final_completion_boundary",
            )

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            self.assert_path_blocks_or_raises(malformed_path)

            array_path = tmp_path / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            self.assert_path_blocks_or_raises(array_path)
            self.assert_path_blocks_or_raises(tmp_path / "missing.json")

            output_root = (
                tmp_path
                / "artifacts"
                / "integrity_host_v0_min_coexistence_portable_source_body_verification_final_completion_boundary"
            )
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                first = resolver.write_portable_source_body_verification_final_completion_boundary_result(
                    result
                )
                second = resolver.write_portable_source_body_verification_final_completion_boundary_result(
                    result
                )

            self.assertTrue(first.parent.exists())
            self.assertTrue(second.parent.exists())
            self.assertNotEqual(first, second)
            json.loads(first.read_text(encoding="utf-8"))
            json.loads(second.read_text(encoding="utf-8"))
            normalized = str(first).replace("\\", "/")
            self.assertIn(
                "artifacts/"
                "integrity_host_v0_min_coexistence_portable_source_body_verification_"
                "final_completion_boundary/",
                normalized,
            )
            for forbidden_root in (
                "actual_second_carrier_live_capture",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_final_completion/",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_portable_verification_closure/",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_portable_verification_closure_boundary/",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_cross_carrier_evidence/",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_external_result/",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_verification/",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_success/",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_result/",
                "runtime",
                "deployment",
                "public_release",
            ):
                self.assertNotIn(forbidden_root, normalized)

    def test_non_mutation_of_request_basis_postures_scope_and_non_claims(self) -> None:
        request = build_request()
        snapshot = copy.deepcopy(request)
        result = resolved(request)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(request, snapshot)
        for key in SELECTED_BASIS_KEYS:
            self.assertEqual(request[key], snapshot[key], key)
        for key in POSTURE_KEYS:
            self.assertEqual(request[key], snapshot[key], key)
        self.assertEqual(
            request["final_completion_boundary_scope"],
            snapshot["final_completion_boundary_scope"],
        )
        self.assertEqual(request["declared_non_claims"], snapshot["declared_non_claims"])

    def test_predecessor_failure_preservation_in_result_and_summary(self) -> None:
        result = resolved(build_request())
        compact = summary(result)
        posture = statement(result)
        claims = non_claims(result)

        self.assertIs(posture["predecessor_cross_carrier_evidence_failure_preserved"], True)
        self.assertIs(claims["predecessor_cross_carrier_evidence_repaired"], False)
        self.assertIs(claims["predecessor_cross_carrier_evidence_hidden"], False)
        self.assertIs(claims["predecessor_cross_carrier_evidence_claimed_passed"], False)

        self.assertIs(posture["predecessor_external_result_v1_failure_preserved"], True)
        self.assertIs(claims["predecessor_external_result_v1_repaired"], False)
        self.assertIs(claims["predecessor_external_result_v1_hidden"], False)
        self.assertIs(claims["predecessor_external_result_v1_claimed_passed"], False)

        self.assertIs(posture["first_success_boundary_test_failure_preserved"], True)
        self.assertIs(claims["first_success_boundary_test_repaired"], False)
        self.assertIs(claims["first_success_boundary_test_hidden"], False)
        self.assertIs(claims["first_success_boundary_test_claimed_passed"], False)

        self.assertIs(claims["v1_packet_emission_repaired"], False)
        self.assertIs(claims["v1_packet_emission_hidden"], False)
        self.assertIs(claims["v1_packet_emission_claimed_passed"], False)

        self.assertIs(posture["first_result_boundary_resolver_failure_preserved"], True)
        self.assertIs(claims["first_result_boundary_resolver_repaired"], False)
        self.assertIs(claims["first_result_boundary_resolver_hidden"], False)
        self.assertIs(claims["first_result_boundary_resolver_claimed_passed"], False)

        self.assertIs(compact["predecessor_cross_carrier_evidence_failure_preserved"], True)
        self.assertIs(compact["predecessor_external_result_v1_failure_preserved"], True)
        self.assertIs(compact["first_success_boundary_test_preserved_as_failed_predecessor"], True)
        self.assertIs(compact["v1_packet_emission_predecessor_failure_preserved"], True)
        self.assertIs(compact["first_result_boundary_resolver_preserved_as_failed_predecessor"], True)


if __name__ == "__main__":
    unittest.main()
