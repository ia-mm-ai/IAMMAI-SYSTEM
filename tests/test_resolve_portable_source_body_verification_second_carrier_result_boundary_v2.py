"""Executable checks for second-carrier result-boundary-v2 posture only.

This suite is downstream of returned real second-carrier live capture intake and
the preserved first result-boundary resolver failure. It verifies that v2 records
one future second-carrier result step only while preserving that no result,
success, external result, cross-carrier evidence, source transfer, source
receipt, reception authorization, source, authority, currentness, runtime, final
completion, continuation, reusable permission, or follow-on work is created.
It also verifies that official scope and block-code strings are not redacted
while hostile raw body payload content remains contained.
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

import resolve_portable_source_body_verification_second_carrier_result_boundary_v2 as resolver


RECORDED = resolver.OUTCOME_RECORDED
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = set(resolver.OUTCOME_FAMILY)
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_SECOND_CARRIER_RESULT_BOUNDARY_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
TRUE_RECORDED_FIELDS = tuple(resolver.ALLOWED_TRUE_RECORDED_FIELDS)
SELECTED_BASIS_KEYS = tuple(resolver.SELECTED_BASIS_KEYS)
POSTURE_KEYS = tuple(resolver.POSTURE_KEYS)

RAW_SENTINELS = (
    "RAW_SECOND_CARRIER_RESULT_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
    "HOSTILE_SECOND_CARRIER_RESULT_BOUNDARY_FULL_BODY_VALUE_MUST_NOT_RETURN",
)
REDACTION_STRINGS = {
    "[bounded-result-boundary-redacted]",
    "[bounded-result-boundary-redacted-raw-body]",
}

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_second_carrier_result_boundary_metadata",
    "declared_second_carrier_result_boundary_question",
    "selected_returned_second_carrier_live_capture_intake_basis",
    "selected_actual_second_carrier_live_capture_packet_basis",
    "selected_actual_second_carrier_live_runbook_basis",
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
    "second_carrier_result_boundary_only_posture",
    "one_future_second_carrier_result_step_posture",
    "returned_second_carrier_capture_basis_preserved_posture",
    "capture_intake_basis_preserved_posture",
    "second_carrier_output_capture_basis_preserved_posture",
    "capture_artifact_basis_preserved_posture",
    "zero_exit_code_not_success_posture",
    "ok_output_not_verification_posture",
    "returned_capture_not_cross_carrier_proof_posture",
    "result_not_created_posture",
    "second_carrier_success_not_created_posture",
    "external_result_not_created_posture",
    "cross_carrier_evidence_not_created_posture",
    "result_not_source_transfer_posture",
    "result_not_source_receipt_posture",
    "result_not_reception_authorization_posture",
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
    "second_carrier_result_boundary_scope",
    "second_carrier_result_boundary_checks",
    "second_carrier_result_boundary_statement",
    "second_carrier_result_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_second_carrier_result_boundary_v2_summary",
)

REPRESENTATIVE_BLOCK_CODES = (
    "SECOND_CARRIER_RESULT_BOUNDARY_QUESTION_UNDECLARED",
    "SECOND_CARRIER_RESULT_BOUNDARY_INTENT_UNSUPPORTED",
    "RETURNED_CAPTURE_INTAKE_BASIS_MISSING",
    "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
    "RETURNED_CAPTURE_TREATED_AS_RESULT",
    "RETURNED_CAPTURE_TREATED_AS_SUCCESS",
    "RETURNED_CAPTURE_TREATED_AS_VERIFICATION",
    "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_PROOF",
    "ZERO_EXIT_CODE_TREATED_AS_SUCCESS",
    "OK_OUTPUT_TREATED_AS_VERIFICATION",
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
    "SECOND_CARRIER_RESULT_BOUNDARY_TREATED_AS_RESULT",
    "SECOND_CARRIER_RESULT_BOUNDARY_TREATED_AS_SUCCESS",
    "SECOND_CARRIER_RESULT_BOUNDARY_TREATED_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_RESULT_BOUNDARY_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_RESULT_CREATED",
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
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_RESULT_BOUNDARY",
    "ARTIFACTS_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_SECOND_CARRIER_RESULT_BOUNDARY_SCOPE",
)

NO_CREATION_FALSE_KEYS = (
    "second_carrier_result_created",
    "second_carrier_success_created",
    "external_result_created",
    "cross_carrier_evidence_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "returned_capture_treated_as_result",
    "returned_capture_treated_as_success",
    "returned_capture_treated_as_verification",
    "returned_capture_treated_as_cross_carrier_evidence",
    "returned_capture_treated_as_source",
    "returned_capture_treated_as_authority",
    "returned_capture_treated_as_currentness",
    "returned_capture_treated_as_runtime",
    "returned_capture_treated_as_final_completion",
    "zero_exit_code_treated_as_success",
    "ok_output_treated_as_verification",
    "ran_7_tests_treated_as_cross_carrier_proof",
    "receiving_carrier_treated_as_authority",
    "artifact_existence_treated_as_result_authority",
    "artifact_path_treated_as_currentness",
    "repo_local_availability_treated_as_result_authority",
    "hidden_repo_state_used_as_result_content",
    "hidden_repo_state_used_as_result_authority",
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
    "v1_repaired",
    "v1_hidden",
    "v1_claimed_passed",
    "first_result_boundary_resolver_repaired",
    "first_result_boundary_resolver_hidden",
    "first_result_boundary_resolver_claimed_passed",
)


def build_request(**overrides: Any) -> dict[str, Any]:
    return resolver.build_declared_portable_source_body_verification_second_carrier_result_boundary_v2_request(
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


class SecondCarrierResultBoundaryV2Test(unittest.TestCase):
    """Bounded second-carrier-result-boundary-v2 executable checks."""

    def assert_public_block_codes(self, result: dict[str, Any]) -> None:
        block = result.get("block")
        if block:
            self.assertIn(block.get("block_code"), resolver.BLOCK_CODES)
        for check in result.get("second_carrier_result_boundary_checks", []):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_generated_bools_are_bools(self, result: dict[str, Any]) -> None:
        statement = result.get("second_carrier_result_boundary_statement", {})
        for key in TRUE_RECORDED_FIELDS:
            self.assertIsInstance(statement.get(key), bool, key)
        non_claims = result.get("non_claims", {})
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIsInstance(non_claims.get(key), bool, key)
        for check in result.get("second_carrier_result_boundary_checks", []):
            self.assertIsInstance(check.get("passed"), bool, check.get("check_name"))

    def assert_no_raw_or_hidden_sentinels(self, result: dict[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in RAW_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def assert_official_enum_strings_not_redacted(self, result: dict[str, Any]) -> None:
        scope_section = result.get("second_carrier_result_boundary_scope", {})
        scope_values = scope_section.get("scope_values", [])
        supported_values = scope_section.get("supported_scope_values", [])
        self.assertIn("RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED", scope_values)
        self.assertIn("RETURNED_RESULT_CONTAINMENT_PRESERVED", scope_values)
        self.assertIn("RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED", supported_values)
        self.assertIn("RETURNED_RESULT_CONTAINMENT_PRESERVED", supported_values)
        self.assertNotIn("[bounded-result-boundary-redacted]", scope_values)
        for value in scope_values:
            self.assertIn(value, resolver.SUPPORTED_SECOND_CARRIER_RESULT_BOUNDARY_SCOPE)
            self.assertNotIn(value, REDACTION_STRINGS)

    def assert_no_result_success_or_authority_created(
        self, result: dict[str, Any], ignored_non_claims: set[str] | None = None
    ) -> None:
        ignored = ignored_non_claims or set()
        non_claims = result.get("non_claims", {})
        for key in NO_CREATION_FALSE_KEYS:
            if key not in ignored:
                self.assertIs(non_claims.get(key), False, key)
        non_meaning = result.get("second_carrier_result_boundary_non_meaning", {})
        for value in non_meaning.values():
            self.assertIs(value, False)

    def assert_recorded_result_is_clean(self, result: dict[str, Any]) -> None:
        summary = resolver.build_portable_source_body_verification_second_carrier_result_boundary_v2_summary(
            result
        )
        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertIsNone(result.get("block"))
        self.assertEqual(summary["result_version"], "0.2.0")
        self.assertEqual(
            summary["resolver_module"],
            "resolve_portable_source_body_verification_second_carrier_result_boundary_v2",
        )
        self.assertGreater(summary["passed_check_count"], 0)
        self.assert_public_block_codes(result)
        self.assert_generated_bools_are_bools(result)
        self.assert_no_raw_or_hidden_sentinels(result)
        self.assert_official_enum_strings_not_redacted(result)
        self.assert_no_result_success_or_authority_created(result)

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
        self.assert_no_result_success_or_authority_created(result, ignored_non_claims)

    def test_public_api_and_constants(self) -> None:
        public_names = (
            "resolve_portable_source_body_verification_second_carrier_result_boundary_v2",
            "resolve_portable_source_body_verification_second_carrier_result_boundary_v2_from_path",
            "write_portable_source_body_verification_second_carrier_result_boundary_v2_result",
            "build_portable_source_body_verification_second_carrier_result_boundary_v2_summary",
            "build_declared_portable_source_body_verification_second_carrier_result_boundary_v2_request",
            "resolve_portable_source_body_verification_second_carrier_result_boundary",
            "resolve_portable_source_body_verification_second_carrier_result_boundary_from_path",
            "write_portable_source_body_verification_second_carrier_result_boundary_result",
            "build_portable_source_body_verification_second_carrier_result_boundary_summary",
            "build_declared_portable_source_body_verification_second_carrier_result_boundary_request",
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_SCOPE_VALUES",
            "SUPPORTED_SECOND_CARRIER_RESULT_BOUNDARY_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        )
        for name in public_names:
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.2.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_portable_source_body_verification_second_carrier_result_boundary_v2",
        )
        self.assertEqual(
            resolver.SUPPORTED_SECOND_CARRIER_RESULT_BOUNDARY_SCOPE,
            resolver.SUPPORTED_SCOPE_VALUES,
        )
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_portable_source_body_verification_"
                "second_carrier_result_boundary_v2"
            )
        )
        self.assertIn(
            "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
            resolver.SUPPORTED_SECOND_CARRIER_RESULT_BOUNDARY_SCOPE,
        )
        self.assertIn(
            "RETURNED_RESULT_CONTAINMENT_PRESERVED",
            resolver.SUPPORTED_SECOND_CARRIER_RESULT_BOUNDARY_SCOPE,
        )
        for code in REPRESENTATIVE_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES, code)

    def test_successful_v2_recorded_result_from_no_argument_builder(self) -> None:
        request = build_request()
        result = resolver.resolve_portable_source_body_verification_second_carrier_result_boundary_v2(
            request
        )
        summary = resolver.build_portable_source_body_verification_second_carrier_result_boundary_v2_summary(
            result
        )

        self.assertIsInstance(result, dict)
        self.assert_recorded_result_is_clean(result)
        self.assertEqual(
            summary["request_id"], request["second_carrier_result_boundary_request_id"]
        )
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result, section)
        self.assertIn(
            "portable_source_body_verification_second_carrier_result_boundary_summary",
            result,
        )

        statement = result["second_carrier_result_boundary_statement"]
        for key in TRUE_RECORDED_FIELDS:
            self.assertIs(statement.get(key), True, key)
        non_claims = result["non_claims"]
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(non_claims.get(key), False, key)

        intake = result["selected_returned_second_carrier_live_capture_intake_basis"]
        capture = result["selected_returned_capture_material_basis"]
        self.assertIs(
            intake["selected_returned_capture_from_macbook_pro_to_macbook_air"], True
        )
        self.assertEqual(capture["raw_placeholder_carrier_label"], "SECOND_DEVICE_LABEL_TO_FILL")
        self.assertEqual(capture["raw_placeholder_carrier_type"], "Mac/Linux/etc_TO_FILL")
        self.assertIs(capture["placeholder_fields_unrepaired"], True)
        self.assertEqual(capture["selected_returned_capture_exit_code"], "0")
        self.assertEqual(capture["selected_returned_capture_ok_line"], "OK")
        self.assertIn("Ran 7 tests", capture["selected_returned_capture_ran_7_tests_line"])

    def test_official_enum_strings_are_not_redacted(self) -> None:
        result = resolver.resolve_portable_source_body_verification_second_carrier_result_boundary_v2(
            build_request()
        )
        self.assert_recorded_result_is_clean(result)

        checks = result["second_carrier_result_boundary_checks"]
        for check in checks:
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code:
                    self.assertIn(code, resolver.BLOCK_CODES)
                    self.assertNotEqual(code, "[bounded-result-boundary-redacted]")

        request = build_request(
            second_carrier_result_boundary_scope=list(
                resolver.SUPPORTED_SECOND_CARRIER_RESULT_BOUNDARY_SCOPE
            )
        )
        all_scope_result = resolver.resolve_portable_source_body_verification_second_carrier_result_boundary_v2(
            request
        )
        self.assert_recorded_result_is_clean(all_scope_result)

    def test_raw_and_hidden_hostile_content_is_contained_without_redacting_official_enums(
        self,
    ) -> None:
        request = build_request()
        hostile_payload = {
            "raw_body": "RAW_SECOND_CARRIER_RESULT_BOUNDARY_BODY_MUST_NOT_RETURN",
            "raw_full_body": "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
            "full_body": "HOSTILE_SECOND_CARRIER_RESULT_BOUNDARY_FULL_BODY_VALUE_MUST_NOT_RETURN",
            "artifact_body": "artifact-body-hostile",
            "raw_result_body": "raw-result-hostile",
            "raw_output_body": "raw-output-hostile",
            "raw_capture_body": "raw-capture-hostile",
            "capture_body": "capture-body-hostile",
            "second_carrier_result_body": "second-carrier-result-hostile",
            "external_result_body": "external-result-hostile",
            "cross_carrier_evidence_body": "cross-carrier-evidence-hostile",
            "source_body": "source-hostile",
            "authority_body": "authority-hostile",
            "hidden_repo_state": "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
            "current_working_tree": "current-tree-hostile",
            "local_cache": "local-cache-hostile",
            "repo_local_only_dependency": "repo-local-only-hostile",
            "nested": {
                "official_scope": "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
                "sentinels": [
                    "RAW_SECOND_CARRIER_RESULT_BOUNDARY_BODY_MUST_NOT_RETURN",
                    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
                    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
                ],
            },
        }
        injected_sections = (
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
        result = resolver.resolve_portable_source_body_verification_second_carrier_result_boundary_v2(
            request
        )

        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assert_no_raw_or_hidden_sentinels(result)
        serialized = json.dumps(result, sort_keys=True)
        for hostile in (
            "artifact-body-hostile",
            "raw-result-hostile",
            "raw-output-hostile",
            "raw-capture-hostile",
            "capture-body-hostile",
            "second-carrier-result-hostile",
            "external-result-hostile",
            "cross-carrier-evidence-hostile",
            "source-hostile",
            "authority-hostile",
            "current-tree-hostile",
            "local-cache-hostile",
            "repo-local-only-hostile",
        ):
            self.assertNotIn(hostile, serialized)
        self.assert_official_enum_strings_not_redacted(result)
        self.assert_public_block_codes(result)
        self.assert_generated_bools_are_bools(result)
        self.assert_no_result_success_or_authority_created(result)
        self.assertEqual(request, original)

    def test_representative_blocking_behavior(self) -> None:
        def with_non_claim(key: str) -> Callable[[dict[str, Any]], None]:
            return lambda request: mutate_non_claim(request, key, True)

        cases: list[tuple[str, Callable[[dict[str, Any]], None], str | None, set[str]]] = [
            (
                "explicit block intent",
                lambda request: request.update(
                    {
                        "second_carrier_result_boundary_intent": resolver.INTENT_BLOCK,
                        "block_reason": "operator requested bounded block",
                    }
                ),
                "SECOND_CARRIER_RESULT_BOUNDARY_BLOCK_REQUESTED",
                set(),
            ),
            (
                "unsupported intent",
                lambda request: request.update(
                    {"second_carrier_result_boundary_intent": "UNSUPPORTED_INTENT"}
                ),
                "SECOND_CARRIER_RESULT_BOUNDARY_INTENT_UNSUPPORTED",
                set(),
            ),
            (
                "unsupported scope",
                lambda request: request.update(
                    {"second_carrier_result_boundary_scope": ["UNSUPPORTED_SCOPE"]}
                ),
                "UNSUPPORTED_SECOND_CARRIER_RESULT_BOUNDARY_SCOPE",
                set(),
            ),
            (
                "missing returned capture intake basis",
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
                with_non_claim("returned_capture_treated_as_result"),
                "RETURNED_CAPTURE_TREATED_AS_RESULT",
                {"returned_capture_treated_as_result"},
            ),
            (
                "returned capture treated as success",
                with_non_claim("returned_capture_treated_as_success"),
                None,
                {"returned_capture_treated_as_success"},
            ),
            (
                "returned capture treated as verification",
                with_non_claim("returned_capture_treated_as_verification"),
                None,
                {"returned_capture_treated_as_verification"},
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
                "result boundary treated as result",
                with_non_claim("second_carrier_result_boundary_treated_as_result"),
                None,
                {"second_carrier_result_boundary_treated_as_result"},
            ),
            (
                "result boundary treated as success",
                with_non_claim("second_carrier_result_boundary_treated_as_success"),
                None,
                {"second_carrier_result_boundary_treated_as_success"},
            ),
            (
                "result boundary treated as external result",
                with_non_claim("second_carrier_result_boundary_treated_as_external_result"),
                None,
                {"second_carrier_result_boundary_treated_as_external_result"},
            ),
            (
                "result boundary treated as cross-carrier evidence",
                with_non_claim(
                    "second_carrier_result_boundary_treated_as_cross_carrier_evidence"
                ),
                None,
                {"second_carrier_result_boundary_treated_as_cross_carrier_evidence"},
            ),
            (
                "second-carrier result created",
                with_non_claim("second_carrier_result_created"),
                "SECOND_CARRIER_RESULT_CREATED",
                {"second_carrier_result_created"},
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
                None,
                {"source_transfer_occurred"},
            ),
            (
                "source receipt occurred",
                with_non_claim("source_receipt_occurred"),
                None,
                {"source_receipt_occurred"},
            ),
            (
                "reception authorization created",
                with_non_claim("reception_authorization_created"),
                None,
                {"reception_authorization_created"},
            ),
            ("source created", with_non_claim("source_created"), None, {"source_created"}),
            ("authority created", with_non_claim("authority_created"), None, {"authority_created"}),
            (
                "currentness created",
                with_non_claim("currentness_created"),
                None,
                {"currentness_created"},
            ),
            (
                "final completion claimed",
                with_non_claim("final_completion_claimed"),
                None,
                {"final_completion_claimed"},
            ),
            (
                "runtime hosting created",
                with_non_claim("runtime_hosting_created"),
                None,
                {"runtime_hosting_created"},
            ),
            (
                "deployment created",
                with_non_claim("deployment_created"),
                None,
                {"deployment_created"},
            ),
            (
                "public release created",
                with_non_claim("public_release_created"),
                None,
                {"public_release_created"},
            ),
            (
                "operation permission created",
                with_non_claim("operation_permission_created"),
                None,
                {"operation_permission_created"},
            ),
            (
                "continuation authorized",
                with_non_claim("continuation_authorized"),
                None,
                {"continuation_authorized"},
            ),
            (
                "reusable permission created",
                with_non_claim("reusable_permission_created"),
                None,
                {"reusable_permission_created"},
            ),
            (
                "follow-on work authorized",
                with_non_claim("follow_on_work_authorized"),
                None,
                {"follow_on_work_authorized"},
            ),
            (
                "receiving carrier treated as authority",
                with_non_claim("receiving_carrier_treated_as_authority"),
                None,
                {"receiving_carrier_treated_as_authority"},
            ),
            (
                "artifact existence treated as result authority",
                with_non_claim("artifact_existence_treated_as_result_authority"),
                None,
                {"artifact_existence_treated_as_result_authority"},
            ),
            (
                "artifact path treated as currentness",
                with_non_claim("artifact_path_treated_as_currentness"),
                None,
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
                None,
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
                "FIRST_RESULT_BOUNDARY_RESOLVER_HIDDEN_OR_REPAIRED",
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
                "full prior artifact body emitted outside boundary posture",
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
                    "second_carrier_result_created"
                ),
                "NON_CLAIM_MISSING_OR_FLIPPED",
                set(),
            ),
        ]

        missing_result = resolver.resolve_portable_source_body_verification_second_carrier_result_boundary_v2(
            None
        )
        self.assert_blocked_result_is_bounded(
            missing_result,
            "DECLARED_SECOND_CARRIER_RESULT_BOUNDARY_REQUEST_MALFORMED",
        )
        non_mapping_result = resolver.resolve_portable_source_body_verification_second_carrier_result_boundary_v2(
            ["not", "a", "mapping"]
        )
        self.assert_blocked_result_is_bounded(
            non_mapping_result,
            "DECLARED_SECOND_CARRIER_RESULT_BOUNDARY_REQUEST_MALFORMED",
        )

        for name, mutator, expected_code, ignored in cases:
            with self.subTest(name=name):
                request = build_request()
                mutator(request)
                result = resolver.resolve_portable_source_body_verification_second_carrier_result_boundary_v2(
                    request
                )
                self.assert_blocked_result_is_bounded(result, expected_code, ignored)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            request_path = root / "valid_request.json"
            request = build_request()
            request_path.write_text(json.dumps(request), encoding="utf-8")

            result = resolver.resolve_portable_source_body_verification_second_carrier_result_boundary_v2_from_path(
                request_path
            )
            self.assert_recorded_result_is_clean(result)
            alias_result = resolver.resolve_portable_source_body_verification_second_carrier_result_boundary_from_path(
                request_path
            )
            self.assert_recorded_result_is_clean(alias_result)

            malformed_path = root / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            with self.assertRaises(
                resolver.PortableSourceBodyVerificationSecondCarrierResultBoundaryV2Error
            ):
                resolver.resolve_portable_source_body_verification_second_carrier_result_boundary_v2_from_path(
                    malformed_path
                )

            array_path = root / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolver.resolve_portable_source_body_verification_second_carrier_result_boundary_v2_from_path(
                array_path
            )
            self.assert_blocked_result_is_bounded(
                array_result,
                "DECLARED_SECOND_CARRIER_RESULT_BOUNDARY_REQUEST_MALFORMED",
            )

            with self.assertRaises(
                resolver.PortableSourceBodyVerificationSecondCarrierResultBoundaryV2Error
            ):
                resolver.resolve_portable_source_body_verification_second_carrier_result_boundary_v2_from_path(
                    root / "missing.json"
                )

            output_root = root / "artifacts" / (
                "integrity_host_v0_min_coexistence_portable_source_body_verification_"
                "second_carrier_result_boundary_v2"
            )
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_portable_source_body_verification_second_carrier_result_boundary_v2_result(
                    result
                )
                second_path = resolver.write_portable_source_body_verification_second_carrier_result_boundary_v2_result(
                    result
                )
                alias_path = resolver.write_portable_source_body_verification_second_carrier_result_boundary_result(
                    result
                )

            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertTrue(alias_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertNotEqual(second_path, alias_path)
            self.assertEqual(first_path.parent, output_root)
            self.assertIn("second_carrier_result_boundary_v2_result", first_path.name)
            parsed = json.loads(first_path.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], RECORDED)
            for path in (first_path, second_path, alias_path):
                text = str(path)
                self.assertNotIn("actual_second_carrier_live_capture", text)
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
        request["second_carrier_result_boundary_scope"] = list(SUPPORTED_SCOPE)
        original = copy.deepcopy(request)

        result = resolver.resolve_portable_source_body_verification_second_carrier_result_boundary_v2(
            request
        )

        self.assert_recorded_result_is_clean(result)
        self.assertEqual(request, original)
        for key in SELECTED_BASIS_KEYS:
            self.assertEqual(request[key], original[key], key)
        for key in POSTURE_KEYS:
            self.assertEqual(request[key], original[key], key)
        self.assertEqual(
            request["second_carrier_result_boundary_scope"],
            original["second_carrier_result_boundary_scope"],
        )
        self.assertEqual(request["declared_non_claims"], original["declared_non_claims"])

    def test_compatibility_aliases_behave_as_v2(self) -> None:
        request = resolver.build_declared_portable_source_body_verification_second_carrier_result_boundary_request()
        result = resolver.resolve_portable_source_body_verification_second_carrier_result_boundary(
            request
        )
        summary = resolver.build_portable_source_body_verification_second_carrier_result_boundary_summary(
            result
        )
        self.assert_recorded_result_is_clean(result)
        self.assertEqual(summary["result_version"], "0.2.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)

        with tempfile.TemporaryDirectory() as tmp:
            output_root = Path(tmp) / "artifacts" / (
                "integrity_host_v0_min_coexistence_portable_source_body_verification_"
                "second_carrier_result_boundary_v2"
            )
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                written = resolver.write_portable_source_body_verification_second_carrier_result_boundary_result(
                    result
                )
            self.assertEqual(written.parent, output_root)
            self.assertTrue(written.exists())

    def test_predecessor_failure_preservation(self) -> None:
        result = resolver.resolve_portable_source_body_verification_second_carrier_result_boundary_v2(
            build_request()
        )
        summary = result["portable_source_body_verification_second_carrier_result_boundary_v2_summary"]
        self.assert_recorded_result_is_clean(result)

        predecessor_basis = result["selected_predecessor_failure_basis"]
        self.assertIs(
            predecessor_basis[
                "first_result_boundary_resolver_preserved_as_failed_predecessor"
            ],
            True,
        )
        self.assertIn(
            "resolve_portable_source_body_verification_second_carrier_result_boundary.py",
            json.dumps(predecessor_basis, sort_keys=True),
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
