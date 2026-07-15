"""Executable checks for second-carrier verification posture only.

This suite is downstream of the second-carrier-verification-boundary line. It
verifies that the resolver records one bounded second-carrier verification
posture only: verification is not external result, cross-carrier proof,
portable verification closure, source transfer, source receipt, reception
authorization, source, authority, currentness, runtime, final completion,
continuation, reusable permission, or follow-on work.

The first success-boundary test, first result-boundary resolver, and v1
packet-emission-boundary surfaces remain preserved predecessor failure evidence.
This suite does not repair, hide, delete, rename, or claim passed those
surfaces. Official enum, scope, and block-code strings are checked for exact
preservation, while hostile raw body payload content remains contained.
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

import resolve_portable_source_body_verification_second_carrier_verification as resolver


RECORDED = resolver.OUTCOME_RECORDED
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = set(resolver.OUTCOME_FAMILY)
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_SECOND_CARRIER_VERIFICATION_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
TRUE_RECORDED_FIELDS = tuple(resolver.ALLOWED_TRUE_RECORDED_FIELDS)

RAW_SENTINELS = (
    "RAW_SECOND_CARRIER_VERIFICATION_BODY_MUST_NOT_RETURN",
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
    "hostile-capture-body-value",
    "hostile-second-carrier-verification-body-value",
    "hostile-external-result-body-value",
    "hostile-cross-carrier-evidence-body-value",
    "hostile-portable-verification-closure-body-value",
    "hostile-source-body-value",
    "hostile-authority-body-value",
    "hostile-current-working-tree-value",
    "hostile-local-cache-value",
    "hostile-repo-local-only-dependency-value",
)
REDACTION_PLACEHOLDERS = {
    "[bounded-verification-redacted]",
    "[bounded-redacted-raw-or-hidden-state]",
}
OFFICIAL_SCOPE_VALUES = (
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "RETURNED_RESULT_CONTAINMENT_PRESERVED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "FIRST_SUCCESS_BOUNDARY_TEST_FAILURE_PRESERVED",
    "FIRST_RESULT_BOUNDARY_RESOLVER_FAILURE_PRESERVED",
)

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_second_carrier_verification_metadata",
    "declared_second_carrier_verification_question",
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
    "second_carrier_verification_spec_only_posture",
    "one_bounded_second_carrier_verification_posture",
    "second_carrier_verification_boundary_basis_preserved_posture",
    "second_carrier_success_basis_preserved_posture",
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
    "repo_local_availability_not_verification_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "first_success_boundary_test_failure_preserved_posture",
    "first_result_boundary_resolver_failure_preserved_posture",
    "second_carrier_verification_scope",
    "second_carrier_verification_checks",
    "second_carrier_verification_statement",
    "second_carrier_verification_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_second_carrier_verification_summary",
)

EXPECTED_TRUE_STATEMENT_FIELDS = (
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


def default_request() -> dict[str, Any]:
    return resolver.build_declared_portable_source_body_verification_second_carrier_verification_request()


def resolve_request(request: dict[str, Any]) -> dict[str, Any]:
    return resolver.resolve_portable_source_body_verification_second_carrier_verification(request)


def serialized(result: dict[str, Any]) -> str:
    return json.dumps(result, sort_keys=True)


def mutate_request(mutator: Callable[[dict[str, Any]], None]) -> dict[str, Any]:
    request = default_request()
    mutator(request)
    return request


class SecondCarrierVerificationResolverTests(unittest.TestCase):
    def assert_public_codes(self, result: dict[str, Any]) -> None:
        block = result.get("block")
        if isinstance(block, dict) and block.get("block_code") is not None:
            self.assertIn(block["block_code"], resolver.BLOCK_CODES)
        for check in result.get("second_carrier_verification_checks", []):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_boolean_fields_are_bool(self, result: dict[str, Any]) -> None:
        for section_name in (
            "second_carrier_verification_statement",
            "second_carrier_verification_non_meaning",
            "non_claims",
        ):
            section = result[section_name]
            for key, value in section.items():
                self.assertIs(type(value), bool, f"{section_name}.{key}")
        for check in result["second_carrier_verification_checks"]:
            self.assertIs(type(check["passed"]), bool, check["check_name"])

    def assert_no_raw_sentinels(self, result: dict[str, Any]) -> None:
        body = serialized(result)
        for sentinel in RAW_SENTINELS:
            self.assertNotIn(sentinel, body)
        for hostile_value in HOSTILE_VALUES:
            self.assertNotIn(hostile_value, body)

    def assert_official_scope_preserved(self, result: dict[str, Any]) -> None:
        scope = result["second_carrier_verification_scope"]
        for official in OFFICIAL_SCOPE_VALUES:
            self.assertIn(official, scope)
        for placeholder in REDACTION_PLACEHOLDERS:
            self.assertNotIn(placeholder, scope)
        for scope_value in resolver.SUPPORTED_SECOND_CARRIER_VERIFICATION_SCOPE:
            self.assertIn(scope_value, scope)
        for check in result["second_carrier_verification_checks"]:
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code is not None:
                    self.assertNotIn(code, REDACTION_PLACEHOLDERS)
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_no_later_work_created(self, result: dict[str, Any]) -> None:
        non_claims = result["non_claims"]
        for key in (
            "external_result_created",
            "cross_carrier_evidence_created",
            "portable_verification_closure_created",
            "source_transfer_occurred",
            "source_receipt_occurred",
            "reception_authorization_created",
            "source_created",
            "authority_created",
            "currentness_created",
            "final_completion_claimed",
            "runtime_hosting_created",
            "deployment_created",
            "public_release_created",
            "follow_on_work_authorized",
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
        ):
            self.assertIs(non_claims[key], False, key)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_portable_source_body_verification_second_carrier_verification",
            "resolve_portable_source_body_verification_second_carrier_verification_from_path",
            "write_portable_source_body_verification_second_carrier_verification_result",
            "build_portable_source_body_verification_second_carrier_verification_summary",
            "build_declared_portable_source_body_verification_second_carrier_verification_request",
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
            "SUPPORTED_SECOND_CARRIER_VERIFICATION_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_portable_source_body_verification_second_carrier_verification",
        )
        self.assertEqual(
            resolver.SUPPORTED_SECOND_CARRIER_VERIFICATION_SCOPE,
            resolver.SUPPORTED_SCOPE_VALUES,
        )
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_verification"
            )
        )
        for scope_value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(scope_value, resolver.SUPPORTED_SECOND_CARRIER_VERIFICATION_SCOPE)

        representative_codes = (
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
            "SECOND_CARRIER_SUCCESS_TREATED_SUCCESS_AS_VERIFICATION",
            "SECOND_CARRIER_SUCCESS_TREATED_SUCCESS_AS_EXTERNAL_RESULT",
            "SECOND_CARRIER_SUCCESS_TREATED_ZERO_EXIT_CODE_AS_VERIFICATION",
            "SECOND_CARRIER_SUCCESS_TREATED_OK_AS_VERIFICATION",
            "SECOND_CARRIER_SUCCESS_TREATED_RAN_7_TESTS_AS_CROSS_CARRIER_PROOF",
            "RETURNED_CAPTURE_INTAKE_BASIS_MISSING",
            "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
            "RETURNED_CAPTURE_TREATED_AS_VERIFICATION",
            "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_PROOF",
            "ZERO_EXIT_CODE_TREATED_AS_VERIFICATION",
            "OK_OUTPUT_TREATED_AS_VERIFICATION",
            "RAN_7_TESTS_TREATED_AS_CROSS_CARRIER_PROOF",
            "PLACEHOLDER_CARRIER_FIELDS_REPAIRED",
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
            "PUBLIC_RELEASE_CREATED",
            "FOLLOW_ON_WORK_AUTHORIZED",
            "RECEIVING_CARRIER_TREATED_AS_AUTHORITY",
            "ARTIFACT_EXISTENCE_TREATED_AS_VERIFICATION_AUTHORITY",
            "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
            "REPO_LOCAL_AVAILABILITY_TREATED_AS_VERIFICATION_AUTHORITY",
            "HIDDEN_REPO_STATE_USED_AS_VERIFICATION_CONTENT",
            "HIDDEN_REPO_STATE_USED_AS_VERIFICATION_AUTHORITY",
            "FIRST_SUCCESS_BOUNDARY_TEST_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
            "FIRST_RESULT_BOUNDARY_RESOLVER_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
            "CONSUMED_REQUEST_REOPENED",
            "AUTHORIZATION_TOKEN_REUSED",
            "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_VERIFICATION",
            "ARTIFACTS_MUTATED",
            "RETURNED_CAPTURE_MATERIAL_MUTATED",
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "UNSUPPORTED_SECOND_CARRIER_VERIFICATION_SCOPE",
        )
        for code in representative_codes:
            self.assertIn(code, resolver.BLOCK_CODES, code)

    def test_successful_recorded_result_from_builder(self) -> None:
        request = default_request()
        result = resolve_request(request)
        summary = resolver.build_portable_source_body_verification_second_carrier_verification_summary(
            result
        )

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertIsNone(result["block"])
        self.assertIsNone(summary["block_code"])
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(
            summary["resolver_module"],
            "resolve_portable_source_body_verification_second_carrier_verification",
        )
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(
            summary["request_id"],
            request["second_carrier_verification_request_id"],
        )

        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result, section)

        statement = result["second_carrier_verification_statement"]
        for key in EXPECTED_TRUE_STATEMENT_FIELDS:
            self.assertIs(statement[key], True, key)

        non_claims = result["non_claims"]
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims, key)
            self.assertIs(non_claims[key], False, key)

        self.assert_public_codes(result)
        self.assert_boolean_fields_are_bool(result)
        self.assert_official_scope_preserved(result)
        self.assert_no_raw_sentinels(result)

    def test_official_enum_strings_are_preserved(self) -> None:
        request = default_request()
        result = resolve_request(request)

        self.assertEqual(result["outcome"], RECORDED)
        self.assert_official_scope_preserved(result)
        self.assertEqual(set(result["second_carrier_verification_scope"]), set(SUPPORTED_SCOPE))

        custom = default_request()
        custom["second_carrier_verification_scope"] = list(
            resolver.SUPPORTED_SECOND_CARRIER_VERIFICATION_SCOPE
        )
        custom_result = resolve_request(custom)
        self.assertEqual(custom_result["outcome"], RECORDED)
        self.assertEqual(set(custom_result["second_carrier_verification_scope"]), set(SUPPORTED_SCOPE))
        self.assert_official_scope_preserved(custom_result)

    def test_hostile_raw_hidden_content_is_contained_without_mutating_request(self) -> None:
        request = default_request()
        hostile_sections = (
            "selected_second_carrier_verification_boundary_basis",
            "selected_second_carrier_verification_boundary_terminal_summary_basis",
            "selected_second_carrier_success_basis",
            "selected_second_carrier_success_terminal_summary_basis",
            "selected_second_carrier_result_basis",
            "selected_returned_second_carrier_live_capture_intake_basis",
            "selected_returned_capture_material_basis",
            "selected_second_carrier_output_capture_basis",
            "selected_command_report_lineage_basis",
            "selected_artifact_containment_basis",
        )
        hostile_payload = {
            "raw_body": "hostile-raw-body-value",
            "raw_full_body": "hostile-raw-full-body-value",
            "full_body": "hostile-full-body-value",
            "artifact_body": "hostile-artifact-body-value",
            "raw_result_body": "hostile-raw-result-body-value",
            "raw_output_body": "hostile-raw-output-body-value",
            "raw_capture_body": "hostile-raw-capture-body-value",
            "raw_success_body": "hostile-raw-success-body-value",
            "raw_verification_body": "hostile-raw-verification-body-value",
            "capture_body": "hostile-capture-body-value",
            "second_carrier_verification_body": "hostile-second-carrier-verification-body-value",
            "external_result_body": "hostile-external-result-body-value",
            "cross_carrier_evidence_body": "hostile-cross-carrier-evidence-body-value",
            "portable_verification_closure_body": "hostile-portable-verification-closure-body-value",
            "source_body": "hostile-source-body-value",
            "authority_body": "hostile-authority-body-value",
            "hidden_repo_state": {"value": RAW_SENTINELS[2]},
            "current_working_tree": "hostile-current-working-tree-value",
            "local_cache": "hostile-local-cache-value",
            "repo_local_only_dependency": "hostile-repo-local-only-dependency-value",
            "nested": [
                {"value": RAW_SENTINELS[0]},
                {"value": RAW_SENTINELS[1]},
                {"value": RAW_SENTINELS[2]},
            ],
        }
        for section in hostile_sections:
            request[section]["hostile_content"] = copy.deepcopy(hostile_payload)

        before = copy.deepcopy(request)
        result = resolve_request(request)

        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assertEqual(request, before)
        self.assert_no_raw_sentinels(result)
        self.assert_official_scope_preserved(result)
        self.assert_public_codes(result)
        self.assert_no_later_work_created(result)
        self.assert_boolean_fields_are_bool(result)

    def test_representative_blocking_behavior(self) -> None:
        block_cases: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
            ("explicit block intent", lambda r: r.update(second_carrier_verification_intent=resolver.BLOCK_INTENT)),
            ("unsupported intent", lambda r: r.update(second_carrier_verification_intent="UNSUPPORTED")),
            ("unsupported scope", lambda r: r.update(second_carrier_verification_scope=["UNSUPPORTED_SCOPE"])),
            ("missing verification boundary basis", lambda r: r.pop("selected_second_carrier_verification_boundary_basis")),
            ("boundary not recorded", lambda r: r.update(selected_second_carrier_verification_boundary_result_outcome="NOT_RECORDED")),
            ("boundary failed checks", lambda r: r.update(selected_second_carrier_verification_boundary_failed_check_count=1)),
            ("boundary version wrong", lambda r: r.update(selected_second_carrier_verification_boundary_result_version="9.9.9")),
            ("boundary did not declare future verification", lambda r: r.update(selected_second_carrier_verification_boundary_declared_future_verification_step=False)),
            ("boundary already created verification", lambda r: r.update(selected_second_carrier_verification_boundary_already_created_verification=True)),
            ("boundary already created external result", lambda r: r.update(selected_second_carrier_verification_boundary_already_created_external_result=True)),
            ("boundary already created cross-carrier evidence", lambda r: r.update(selected_second_carrier_verification_boundary_already_created_cross_carrier_evidence=True)),
            ("boundary already created portable closure", lambda r: r.update(selected_second_carrier_verification_boundary_already_created_portable_verification_closure=True)),
            ("boundary treated as verification", lambda r: r.update(selected_second_carrier_verification_boundary_treated_verification_boundary_as_verification=True)),
            ("boundary treated as external result", lambda r: r.update(selected_second_carrier_verification_boundary_treated_verification_boundary_as_external_result=True)),
            ("boundary treated as cross-carrier evidence", lambda r: r.update(selected_second_carrier_verification_boundary_treated_verification_boundary_as_cross_carrier_evidence=True)),
            ("boundary treated as portable closure", lambda r: r.update(selected_second_carrier_verification_boundary_treated_verification_boundary_as_portable_verification_closure=True)),
            ("boundary treated zero exit code as verification", lambda r: r.update(selected_second_carrier_verification_boundary_zero_exit_code_not_verification=False)),
            ("boundary treated OK as verification", lambda r: r.update(selected_second_carrier_verification_boundary_ok_not_verification=False)),
            ("boundary treated Ran 7 tests as proof", lambda r: r.update(selected_second_carrier_verification_boundary_ran_7_tests_not_cross_carrier_proof=False)),
            ("boundary redacted official enums", lambda r: r.update(selected_second_carrier_verification_boundary_official_enum_scope_strings_redacted=True)),
            ("missing success basis", lambda r: r.pop("selected_second_carrier_success_basis")),
            ("success not recorded", lambda r: r.update(selected_second_carrier_success_result_outcome="NOT_RECORDED")),
            ("success failed checks", lambda r: r.update(selected_second_carrier_success_failed_check_count=2)),
            ("success already created verification", lambda r: r["declared_non_claims"].update(second_carrier_verification_treated_as_external_result=True)),
            ("success already created external result", lambda r: r["declared_non_claims"].update(external_result_created=True)),
            ("success treated success as verification", lambda r: r.update(selected_second_carrier_success_treated_success_as_verification=True)),
            ("success treated success as external result", lambda r: r.update(selected_second_carrier_success_treated_success_as_external_result=True)),
            ("success treated zero exit code as verification", lambda r: r.update(selected_second_carrier_success_zero_exit_code_not_verification=False)),
            ("success treated OK as verification", lambda r: r.update(selected_second_carrier_success_ok_not_verification=False)),
            ("success treated Ran 7 tests as proof", lambda r: r.update(selected_second_carrier_success_ran_7_tests_not_cross_carrier_proof=False)),
            ("missing returned capture intake", lambda r: r.pop("selected_returned_second_carrier_live_capture_intake_basis")),
            ("returned capture intake not preserved", lambda r: r.update(selected_returned_capture_intake_preserved=False)),
            ("returned capture treated as verification", lambda r: r.update(selected_returned_capture_intake_capture_only=False)),
            ("returned capture treated as cross-carrier proof", lambda r: r["declared_non_claims"].update(returned_capture_treated_as_cross_carrier_evidence=True)),
            ("zero exit code treated as verification", lambda r: r["declared_non_claims"].update(zero_exit_code_treated_as_verification_standalone=True)),
            ("OK treated as verification", lambda r: r["declared_non_claims"].update(ok_output_treated_as_verification_standalone=True)),
            ("Ran 7 tests treated as proof", lambda r: r["declared_non_claims"].update(ran_7_tests_treated_as_cross_carrier_proof=True)),
            ("placeholder fields repaired", lambda r: r.update(selected_returned_capture_placeholder_fields_unrepaired=False)),
            ("returned capture material missing", lambda r: r.pop("selected_returned_capture_material_basis")),
            ("zip missing", lambda r: r.update(selected_returned_capture_zip_path="")),
            ("hash missing", lambda r: r.update(selected_returned_capture_hash_path="")),
            ("extracted missing", lambda r: r.update(selected_returned_capture_extracted_directory_path="")),
            ("combined log missing", lambda r: r.update(selected_returned_capture_combined_terminal_log_path="")),
            ("exit code missing", lambda r: r.update(selected_returned_capture_exit_code="")),
            ("command text missing", lambda r: r.update(selected_returned_capture_command_text="")),
            ("timestamps missing", lambda r: r.update(selected_returned_capture_started_at="")),
            ("output capture missing", lambda r: r.pop("selected_second_carrier_output_capture_basis")),
            ("output capture not recorded", lambda r: r.update(selected_second_carrier_output_capture_result_outcome="NOT_RECORDED")),
            ("output capture failed checks", lambda r: r.update(selected_second_carrier_output_capture_failed_check_count=1)),
            ("verification external result", lambda r: r["declared_non_claims"].update(second_carrier_verification_treated_as_external_result=True)),
            ("verification cross-carrier evidence", lambda r: r["declared_non_claims"].update(second_carrier_verification_treated_as_cross_carrier_evidence=True)),
            ("verification portable closure", lambda r: r["declared_non_claims"].update(second_carrier_verification_treated_as_portable_verification_closure=True)),
            ("verification source transfer", lambda r: r["declared_non_claims"].update(second_carrier_verification_treated_as_source_transfer=True)),
            ("verification source receipt", lambda r: r["declared_non_claims"].update(second_carrier_verification_treated_as_source_receipt=True)),
            ("verification reception authorization", lambda r: r["declared_non_claims"].update(second_carrier_verification_treated_as_reception_authorization=True)),
            ("verification source", lambda r: r["declared_non_claims"].update(second_carrier_verification_treated_as_source=True)),
            ("verification authority", lambda r: r["declared_non_claims"].update(second_carrier_verification_treated_as_authority=True)),
            ("verification currentness", lambda r: r["declared_non_claims"].update(second_carrier_verification_treated_as_currentness=True)),
            ("verification final completion", lambda r: r["declared_non_claims"].update(second_carrier_verification_treated_as_final_completion=True)),
            ("verification runtime", lambda r: r["declared_non_claims"].update(second_carrier_verification_treated_as_runtime=True)),
            ("verification continuation", lambda r: r["declared_non_claims"].update(second_carrier_verification_treated_as_continuation=True)),
            ("verification reusable", lambda r: r["declared_non_claims"].update(second_carrier_verification_treated_as_reusable_permission=True)),
            ("verification follow-on", lambda r: r["declared_non_claims"].update(second_carrier_verification_treated_as_follow_on_work=True)),
            ("external result created", lambda r: r["declared_non_claims"].update(external_result_created=True)),
            ("cross-carrier evidence created", lambda r: r["declared_non_claims"].update(cross_carrier_evidence_created=True)),
            ("portable closure created", lambda r: r["declared_non_claims"].update(portable_verification_closure_created=True)),
            ("source transfer occurred", lambda r: r["declared_non_claims"].update(source_transfer_occurred=True)),
            ("source receipt occurred", lambda r: r["declared_non_claims"].update(source_receipt_occurred=True)),
            ("reception authorization created", lambda r: r["declared_non_claims"].update(reception_authorization_created=True)),
            ("source created", lambda r: r["declared_non_claims"].update(source_created=True)),
            ("authority created", lambda r: r["declared_non_claims"].update(authority_created=True)),
            ("currentness created", lambda r: r["declared_non_claims"].update(currentness_created=True)),
            ("final completion claimed", lambda r: r["declared_non_claims"].update(final_completion_claimed=True)),
            ("runtime hosting created", lambda r: r["declared_non_claims"].update(runtime_hosting_created=True)),
            ("deployment created", lambda r: r["declared_non_claims"].update(deployment_created=True)),
            ("public release created", lambda r: r["declared_non_claims"].update(public_release_created=True)),
            ("operation permission created", lambda r: r["declared_non_claims"].update(operation_permission_created=True)),
            ("continuation authorized", lambda r: r["declared_non_claims"].update(continuation_authorized=True)),
            ("reusable permission created", lambda r: r["declared_non_claims"].update(reusable_permission_created=True)),
            ("follow-on authorized", lambda r: r["declared_non_claims"].update(follow_on_work_authorized=True)),
            ("receiving carrier authority", lambda r: r["declared_non_claims"].update(receiving_carrier_treated_as_authority=True)),
            ("artifact existence authority", lambda r: r["declared_non_claims"].update(artifact_existence_treated_as_verification_authority=True)),
            ("artifact path currentness", lambda r: r["declared_non_claims"].update(artifact_path_treated_as_currentness=True)),
            ("repo local authority", lambda r: r["declared_non_claims"].update(repo_local_availability_treated_as_verification_authority=True)),
            ("hidden repo content", lambda r: r["declared_non_claims"].update(hidden_repo_state_used_as_verification_content=True)),
            ("hidden repo authority", lambda r: r["declared_non_claims"].update(hidden_repo_state_used_as_verification_authority=True)),
            ("selected basis not reference shaped", lambda r: r.update(selected_basis_reference_shape_posture=False)),
            ("raw prior body returned", lambda r: r["declared_non_claims"].update(raw_full_prior_artifact_body_returned=True)),
            ("predecessor evidence repaired", lambda r: r["declared_non_claims"].update(v1_repaired=True)),
            ("first success boundary hidden", lambda r: r["declared_non_claims"].update(first_success_boundary_test_hidden=True)),
            ("first result boundary hidden", lambda r: r["declared_non_claims"].update(first_result_boundary_resolver_hidden=True)),
            ("command report current artifact", lambda r: r.update(selected_command_report_lineage_basis=None)),
            ("consumed request reopened", lambda r: r["declared_non_claims"].update(consumed_request_reopened=True)),
            ("authorization reused", lambda r: r["declared_non_claims"].update(authorization_token_reused=True)),
            ("full prior emitted", lambda r: r.update(raw_full_prior_artifact_body_not_returned_posture=False)),
            ("artifacts mutated", lambda r: r["declared_non_claims"].update(prior_artifacts_mutated=True)),
            ("returned capture mutated", lambda r: r["declared_non_claims"].update(returned_capture_material_mutated=True)),
            ("required non-claim missing", lambda r: r["declared_non_claims"].pop("external_result_created")),
        )

        special_results = (
            ("missing request", resolver.resolve_portable_source_body_verification_second_carrier_verification(None)),
            ("non-mapping request", resolver.resolve_portable_source_body_verification_second_carrier_verification(["not", "mapping"])),
        )
        for label, result in special_results:
            with self.subTest(label=label):
                self.assertEqual(result["outcome"], BLOCKED)
                self.assert_public_codes(result)
                self.assert_no_later_work_created(result)
                self.assert_boolean_fields_are_bool(result)

        for label, mutator in block_cases:
            with self.subTest(label=label):
                result = resolve_request(mutate_request(mutator))
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertIsNotNone(result["block"])
                self.assert_public_codes(result)
                self.assert_no_later_work_created(result)
                self.assert_boolean_fields_are_bool(result)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request_path = tmp_path / "request.json"
            request = default_request()
            request_path.write_text(json.dumps(request), encoding="utf-8")

            result = resolver.resolve_portable_source_body_verification_second_carrier_verification_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], RECORDED)
            summary = resolver.build_portable_source_body_verification_second_carrier_verification_summary(
                result
            )
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(
                summary["resolver_module"],
                "resolve_portable_source_body_verification_second_carrier_verification",
            )

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            with self.assertRaises(resolver.PortableSourceBodyVerificationSecondCarrierVerificationError):
                resolver.resolve_portable_source_body_verification_second_carrier_verification_from_path(
                    malformed_path
                )

            array_path = tmp_path / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolver.resolve_portable_source_body_verification_second_carrier_verification_from_path(
                array_path
            )
            self.assertEqual(array_result["outcome"], BLOCKED)
            self.assert_public_codes(array_result)

            with self.assertRaises(resolver.PortableSourceBodyVerificationSecondCarrierVerificationError):
                resolver.resolve_portable_source_body_verification_second_carrier_verification_from_path(
                    tmp_path / "missing.json"
                )

            output_root = (
                tmp_path
                / "artifacts"
                / "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_verification"
            )
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                first = resolver.write_portable_source_body_verification_second_carrier_verification_result(
                    result
                )
                second = resolver.write_portable_source_body_verification_second_carrier_verification_result(
                    result
                )

            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertEqual(first.parent, output_root)
            self.assertEqual(second.parent, output_root)
            self.assertEqual(json.loads(first.read_text(encoding="utf-8"))["outcome"], RECORDED)
            self.assertTrue(
                str(first.parent).endswith(
                    "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_verification"
                )
            )
            forbidden_roots = (
                "actual_second_carrier_live_capture",
                "second_carrier_verification_boundary",
                "second_carrier_success",
                "second_carrier_success_boundary",
                "second_carrier_result_boundary_v2",
                "external-result",
                "cross-carrier",
                "portable-verification-closure",
                "runtime",
                "deployment",
                "public-release",
            )
            for forbidden in forbidden_roots:
                self.assertNotIn(forbidden, str(first))

    def test_resolver_does_not_mutate_request_or_selected_sections(self) -> None:
        request = default_request()
        before = copy.deepcopy(request)
        result = resolve_request(request)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(request, before)

    def test_predecessor_failure_preservation(self) -> None:
        result = resolve_request(default_request())
        summary = resolver.build_portable_source_body_verification_second_carrier_verification_summary(
            result
        )
        statement = result["second_carrier_verification_statement"]
        non_claims = result["non_claims"]

        self.assertIs(statement["first_success_boundary_test_failure_preserved"], True)
        self.assertIs(non_claims["first_success_boundary_test_repaired"], False)
        self.assertIs(non_claims["first_success_boundary_test_hidden"], False)
        self.assertIs(non_claims["first_success_boundary_test_claimed_passed"], False)

        self.assertIs(summary["v1_predecessor_failure_preserved"], True)
        self.assertIs(summary["v1_not_repaired"], True)
        self.assertIs(summary["v1_not_hidden"], True)
        self.assertIs(summary["v1_not_claimed_passed"], True)

        self.assertIs(statement["first_result_boundary_resolver_failure_preserved"], True)
        self.assertIs(non_claims["first_result_boundary_resolver_repaired"], False)
        self.assertIs(non_claims["first_result_boundary_resolver_hidden"], False)
        self.assertIs(non_claims["first_result_boundary_resolver_claimed_passed"], False)
        self.assertIs(
            summary["first_result_boundary_resolver_preserved_as_failed_predecessor"],
            True,
        )


if __name__ == "__main__":
    unittest.main()
