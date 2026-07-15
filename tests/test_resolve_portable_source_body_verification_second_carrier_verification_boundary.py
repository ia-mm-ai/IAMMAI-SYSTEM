"""Executable checks for second-carrier verification-boundary posture only.

This suite is downstream of recorded second-carrier success. It verifies that
the resolver records one future second-carrier verification step boundary only:
verification is not created, success is not verification, external result and
cross-carrier evidence are not created, portable verification closure is not
created, source transfer/source receipt/reception authorization are not created,
and source, authority, currentness, runtime, final completion, continuation,
reusable permission, and follow-on work remain uncreated.

The first success-boundary test remains preserved predecessor failure evidence.
This suite does not repair, hide, delete, rename, or claim passed that test. It
also preserves the first result-boundary resolver and v1 packet-emission-
boundary surfaces as predecessor failure evidence. Official enum, scope, and
block-code strings are checked for exact preservation, while hostile raw body
payload content remains contained.
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

import resolve_portable_source_body_verification_second_carrier_verification_boundary as resolver


RECORDED = resolver.OUTCOME_RECORDED
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = set(resolver.OUTCOME_FAMILY)
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_SECOND_CARRIER_VERIFICATION_BOUNDARY_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
TRUE_RECORDED_FIELDS = tuple(resolver.ALLOWED_TRUE_RECORDED_FIELDS)
SELECTED_BASIS_KEYS = tuple(resolver.SELECTED_BASIS_KEYS)
POSTURE_KEYS = tuple(resolver.POSTURE_KEYS)

RAW_SENTINELS = (
    "RAW_SECOND_CARRIER_VERIFICATION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
    "HOSTILE_SECOND_CARRIER_VERIFICATION_BOUNDARY_FULL_BODY_VALUE_MUST_NOT_RETURN",
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
    "[bounded-verification-boundary-redacted]",
    "[bounded-redacted-raw-or-hidden-state]",
}
OFFICIAL_SCOPE_VALUES = (
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "RETURNED_RESULT_CONTAINMENT_PRESERVED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "FIRST_SUCCESS_BOUNDARY_TEST_FAILURE_PRESERVED",
    "FIRST_RESULT_BOUNDARY_RESOLVER_FAILURE_PRESERVED",
    "VERIFICATION_NOT_CREATED",
    "VERIFICATION_BOUNDARY_NOT_VERIFICATION",
)

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_second_carrier_verification_boundary_metadata",
    "declared_second_carrier_verification_boundary_question",
    "selected_second_carrier_success_basis",
    "selected_second_carrier_success_terminal_summary_basis",
    "selected_second_carrier_success_boundary_basis",
    "selected_second_carrier_success_boundary_terminal_summary_basis",
    "selected_second_carrier_result_basis",
    "selected_second_carrier_result_terminal_summary_basis",
    "selected_second_carrier_result_boundary_v2_basis",
    "selected_returned_second_carrier_live_capture_intake_basis",
    "selected_returned_capture_material_basis",
    "selected_second_carrier_output_capture_basis",
    "selected_second_carrier_output_capture_terminal_summary_basis",
    "selected_second_carrier_output_capture_boundary_basis",
    "selected_second_carrier_execution_output_basis",
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
    "second_carrier_verification_boundary_only_posture",
    "one_future_second_carrier_verification_step_posture",
    "second_carrier_success_basis_preserved_posture",
    "second_carrier_success_boundary_basis_preserved_posture",
    "second_carrier_result_basis_preserved_posture",
    "returned_second_carrier_capture_basis_preserved_posture",
    "capture_intake_basis_preserved_posture",
    "second_carrier_output_capture_basis_preserved_posture",
    "success_artifact_basis_preserved_posture",
    "verification_not_created_posture",
    "verification_boundary_not_verification_posture",
    "success_not_verification_posture",
    "success_not_external_result_posture",
    "zero_exit_code_not_verification_posture",
    "ok_output_not_verification_posture",
    "ran_7_tests_not_cross_carrier_proof_posture",
    "returned_capture_not_cross_carrier_proof_posture",
    "external_result_not_created_posture",
    "cross_carrier_evidence_not_created_posture",
    "portable_verification_closure_not_created_posture",
    "verification_not_source_transfer_posture",
    "verification_not_source_receipt_posture",
    "verification_not_reception_authorization_posture",
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
    "second_carrier_verification_boundary_scope",
    "second_carrier_verification_boundary_checks",
    "second_carrier_verification_boundary_statement",
    "second_carrier_verification_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_second_carrier_verification_boundary_summary",
)

REPRESENTATIVE_BLOCK_CODES = (
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_QUESTION_UNDECLARED",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_INTENT_UNSUPPORTED",
    "SECOND_CARRIER_SUCCESS_BASIS_MISSING",
    "SECOND_CARRIER_SUCCESS_NOT_RECORDED",
    "SECOND_CARRIER_SUCCESS_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_SUCCESS_VERSION_NOT_0_1_0",
    "SECOND_CARRIER_SUCCESS_DID_NOT_RECORD_BOUNDED_SUCCESS",
    "SECOND_CARRIER_SUCCESS_ALREADY_CREATED_VERIFICATION",
    "SECOND_CARRIER_SUCCESS_ALREADY_CREATED_EXTERNAL_RESULT",
    "SECOND_CARRIER_SUCCESS_ALREADY_CREATED_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_SUCCESS_ALREADY_CREATED_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_SUCCESS_TREATED_SUCCESS_AS_VERIFICATION",
    "SECOND_CARRIER_SUCCESS_TREATED_SUCCESS_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_SUCCESS_TREATED_SUCCESS_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_SUCCESS_TREATED_SUCCESS_AS_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_SUCCESS_TREATED_ZERO_EXIT_CODE_AS_VERIFICATION",
    "SECOND_CARRIER_SUCCESS_TREATED_OK_AS_VERIFICATION",
    "SECOND_CARRIER_SUCCESS_TREATED_RAN_7_TESTS_AS_CROSS_CARRIER_PROOF",
    "SECOND_CARRIER_SUCCESS_TREATED_RETURNED_CAPTURE_AS_CROSS_CARRIER_PROOF",
    "SECOND_CARRIER_SUCCESS_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_BASIS_MISSING",
    "SECOND_CARRIER_RESULT_BASIS_MISSING",
    "SECOND_CARRIER_RESULT_NOT_RECORDED",
    "SECOND_CARRIER_RESULT_FAILED_CHECKS_PRESENT",
    "RETURNED_CAPTURE_INTAKE_BASIS_MISSING",
    "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
    "RETURNED_CAPTURE_TREATED_AS_VERIFICATION",
    "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_PROOF",
    "ZERO_EXIT_CODE_TREATED_AS_VERIFICATION",
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
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_VERIFICATION",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_SOURCE",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_AUTHORITY",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_CURRENTNESS",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_FINAL_COMPLETION",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_RUNTIME",
    "SECOND_CARRIER_VERIFICATION_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
    "VERIFICATION_CREATED",
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
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_VERIFICATION_BOUNDARY",
    "ARTIFACTS_MUTATED",
    "RETURNED_CAPTURE_MATERIAL_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_SECOND_CARRIER_VERIFICATION_BOUNDARY_SCOPE",
)


def build_request(**overrides: Any) -> dict[str, Any]:
    return resolver.build_declared_portable_source_body_verification_second_carrier_verification_boundary_request(
        **overrides
    )


def resolve_request(request: Any) -> dict[str, Any]:
    return resolver.resolve_portable_source_body_verification_second_carrier_verification_boundary(
        request
    )


def checks(result: dict[str, Any]) -> list[dict[str, Any]]:
    return list(result.get("second_carrier_verification_boundary_checks", ()))


def statement(result: dict[str, Any]) -> dict[str, Any]:
    return dict(result.get("second_carrier_verification_boundary_statement", {}))


def non_claims(result: dict[str, Any]) -> dict[str, Any]:
    return dict(result.get("non_claims", {}))


def non_meaning(result: dict[str, Any]) -> dict[str, Any]:
    return dict(result.get("second_carrier_verification_boundary_non_meaning", {}))


def mutate_request(mutator: Callable[[dict[str, Any]], None]) -> dict[str, Any]:
    request = build_request()
    mutator(request)
    return request


def set_field(key: str, value: Any) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request[key] = value

    return mutate


def remove_field(key: str) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request.pop(key, None)

    return mutate


def flip_non_claim(key: str) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request.setdefault("declared_non_claims", {})[key] = True

    return mutate


def declared_block(code: str) -> dict[str, Any]:
    return build_request(
        second_carrier_verification_boundary_intent=(
            "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_VERIFICATION_BOUNDARY"
        ),
        block_code=code,
        block_reason=f"declared bounded block for {code}",
    )


class PortableSourceBodyVerificationSecondCarrierVerificationBoundaryTests(
    unittest.TestCase
):
    def assert_public_block_codes(self, result: dict[str, Any]) -> None:
        block = result.get("block")
        if isinstance(block, dict) and block.get("block_code") is not None:
            self.assertIn(block["block_code"], resolver.BLOCK_CODES)
            self.assertNotIn(block["block_code"], REDACTION_PLACEHOLDERS)
        for check in checks(result):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES, check)
                    self.assertNotIn(code, REDACTION_PLACEHOLDERS, check)

    def assert_generated_booleans_are_bool(self, result: dict[str, Any]) -> None:
        for key, value in statement(result).items():
            self.assertIsInstance(value, bool, key)
            self.assertNotIsInstance(value, str, key)
        for key, value in non_claims(result).items():
            self.assertIsInstance(value, bool, key)
            self.assertNotIsInstance(value, str, key)
        for key, value in non_meaning(result).items():
            self.assertIsInstance(value, bool, key)
            self.assertNotIsInstance(value, str, key)
        for check in checks(result):
            self.assertIsInstance(check.get("passed"), bool, check)
        for section_key in POSTURE_KEYS:
            section = result.get(section_key)
            self.assertIsInstance(section, dict, section_key)
            for key, value in section.items():
                if key in {"posture_key", "declared_posture"}:
                    continue
                if isinstance(value, bool):
                    self.assertIsInstance(value, bool, f"{section_key}.{key}")
                else:
                    self.assertNotIn(str(value), REDACTION_PLACEHOLDERS)

    def assert_no_raw_sentinels(self, result: dict[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in RAW_SENTINELS:
            self.assertNotIn(sentinel, serialized)
        for hostile_value in HOSTILE_VALUES:
            self.assertNotIn(hostile_value, serialized)

    def assert_official_enum_strings_preserved(self, result: dict[str, Any]) -> None:
        scope = tuple(result.get("second_carrier_verification_boundary_scope", ()))
        for official in OFFICIAL_SCOPE_VALUES:
            self.assertIn(official, scope)
        for value in scope:
            self.assertNotIn(value, REDACTION_PLACEHOLDERS)
        for supported_value in SUPPORTED_SCOPE:
            self.assertIn(supported_value, scope)
            self.assertNotIn(supported_value, REDACTION_PLACEHOLDERS)
        self.assert_public_block_codes(result)

    def assert_selected_basis_reference_shaped(self, result: dict[str, Any]) -> None:
        for key in SELECTED_BASIS_KEYS:
            section = result.get(key)
            self.assertIsInstance(section, dict, key)
            self.assertIs(section.get("basis_reference_shape_preserved"), True, key)
            self.assertIs(section.get("basis_only"), True, key)

    def assert_no_forbidden_creation(self, result: dict[str, Any]) -> None:
        nc = non_claims(result)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(nc.get(key), False, key)
        nm = non_meaning(result)
        for key in (
            "verification_has_occurred",
            "external_result_exists",
            "cross_carrier_evidence_exists",
            "portable_verification_closure_exists",
            "source_transfer_occurred",
            "source_receipt_occurred",
            "reception_authorization_exists",
            "source_exists",
            "authority_exists",
            "currentness_exists",
            "final_completion_exists",
            "runtime_exists",
            "deployment_exists",
            "public_release_exists",
            "continuation_authorized",
            "reusable_permission_exists",
            "follow_on_work_authorized",
            "verification_boundary_became_verification",
            "verification_boundary_became_external_result",
            "verification_boundary_became_cross_carrier_proof",
            "verification_boundary_became_portable_verification_closure",
            "verification_boundary_became_source_transfer_source_receipt_or_reception",
            "verification_boundary_became_source_authority_or_currentness",
            "success_became_verification",
            "success_became_external_result",
            "zero_exit_code_became_verification",
            "ok_became_verification_by_itself",
            "ran_7_tests_became_cross_carrier_proof",
            "returned_capture_became_proof",
            "macbook_pro_became_authority",
            "macbook_air_became_source",
            "artifact_existence_became_verification_authority",
            "artifact_path_became_currentness",
            "repo_local_availability_became_verification_authority",
            "hidden_repo_state_became_verification_authority",
            "first_success_boundary_test_repaired_hidden_erased_or_claimed_passed",
            "first_result_boundary_resolver_repaired_hidden_erased_or_claimed_passed",
            "v1_packet_emission_boundary_repaired_hidden_erased_or_claimed_passed",
        ):
            self.assertIs(nm.get(key), False, key)

    def assert_blocked_case(
        self, name: str, request: Any, expected_code: str | None = None
    ) -> dict[str, Any]:
        result = resolve_request(request)
        self.assertEqual(result["outcome"], BLOCKED, name)
        self.assertIsInstance(result.get("block"), dict, name)
        self.assertIsNotNone(result["block"].get("block_code"), name)
        if expected_code is not None:
            self.assertEqual(result["block"].get("block_code"), expected_code, name)
        self.assert_public_block_codes(result)
        self.assert_no_forbidden_creation(result)
        self.assert_generated_booleans_are_bool(result)
        return result

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_portable_source_body_verification_second_carrier_verification_boundary",
            "resolve_portable_source_body_verification_second_carrier_verification_boundary_from_path",
            "write_portable_source_body_verification_second_carrier_verification_boundary_result",
            "build_portable_source_body_verification_second_carrier_verification_boundary_summary",
            "build_declared_portable_source_body_verification_second_carrier_verification_boundary_request",
        ):
            self.assertTrue(callable(getattr(resolver, name, None)), name)
        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_SCOPE_VALUES",
            "SUPPORTED_SECOND_CARRIER_VERIFICATION_BOUNDARY_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_portable_source_body_verification_second_carrier_verification_boundary",
        )
        self.assertEqual(
            resolver.SUPPORTED_SECOND_CARRIER_VERIFICATION_BOUNDARY_SCOPE,
            resolver.SUPPORTED_SCOPE_VALUES,
        )
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_verification_boundary"
            )
        )
        for scope_value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(scope_value, SUPPORTED_SCOPE)
        for code in REPRESENTATIVE_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES, code)

    def test_successful_recorded_result_from_builder(self) -> None:
        request = build_request()
        result = resolve_request(request)
        summary = resolver.build_portable_source_body_verification_second_carrier_verification_boundary_summary(
            result
        )

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertIsNone(result.get("block"))
        self.assertIsNone(summary.get("block_code"))
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(
            summary["resolver_module"],
            "resolve_portable_source_body_verification_second_carrier_verification_boundary",
        )
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(
            summary["request_id"],
            request["second_carrier_verification_boundary_request_id"],
        )
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result, section)

        st = statement(result)
        for key in TRUE_RECORDED_FIELDS:
            self.assertIs(st.get(key), True, key)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(non_claims(result).get(key), False, key)

        self.assert_public_block_codes(result)
        self.assert_generated_booleans_are_bool(result)
        self.assert_no_raw_sentinels(result)
        self.assert_official_enum_strings_preserved(result)
        self.assert_selected_basis_reference_shaped(result)
        self.assert_no_forbidden_creation(result)

    def test_official_enum_strings_are_preserved_without_placeholder_redaction(
        self,
    ) -> None:
        result = resolve_request(build_request())
        scope = tuple(result["second_carrier_verification_boundary_scope"])
        self.assert_official_enum_strings_preserved(result)
        for official in OFFICIAL_SCOPE_VALUES:
            self.assertIn(official, scope)
        for value in scope:
            self.assertNotIn(value, REDACTION_PLACEHOLDERS)
        for check in checks(result):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code is not None:
                    self.assertNotIn(code, REDACTION_PLACEHOLDERS)
                    self.assertIn(code, resolver.BLOCK_CODES)

        custom_request = build_request(
            second_carrier_verification_boundary_scope=list(
                resolver.SUPPORTED_SECOND_CARRIER_VERIFICATION_BOUNDARY_SCOPE
            )
        )
        custom_result = resolve_request(custom_request)
        self.assertEqual(custom_result["outcome"], RECORDED)
        self.assertEqual(
            tuple(custom_result["second_carrier_verification_boundary_scope"]),
            tuple(resolver.SUPPORTED_SECOND_CARRIER_VERIFICATION_BOUNDARY_SCOPE),
        )
        self.assert_official_enum_strings_preserved(custom_result)

    def test_raw_hidden_hostile_content_containment(self) -> None:
        request = build_request()
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
            "second_carrier_verification_body": (
                "hostile-second-carrier-verification-body-value"
            ),
            "external_result_body": "hostile-external-result-body-value",
            "cross_carrier_evidence_body": (
                "hostile-cross-carrier-evidence-body-value"
            ),
            "portable_verification_closure_body": (
                "hostile-portable-verification-closure-body-value"
            ),
            "source_body": "hostile-source-body-value",
            "authority_body": "hostile-authority-body-value",
            "hidden_repo_state": "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
            "current_working_tree": "hostile-current-working-tree-value",
            "local_cache": "hostile-local-cache-value",
            "repo_local_only_dependency": (
                "hostile-repo-local-only-dependency-value"
            ),
            "nested": {
                "sentinels": [
                    "RAW_SECOND_CARRIER_VERIFICATION_BOUNDARY_BODY_MUST_NOT_RETURN",
                    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
                    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
                ]
            },
        }
        for key in (
            "selected_second_carrier_success_basis",
            "selected_second_carrier_success_terminal_summary_basis",
            "selected_second_carrier_success_boundary_basis",
            "selected_second_carrier_success_boundary_terminal_summary_basis",
            "selected_second_carrier_result_basis",
            "selected_returned_second_carrier_live_capture_intake_basis",
            "selected_returned_capture_material_basis",
            "selected_second_carrier_output_capture_basis",
            "selected_command_report_lineage_basis",
            "selected_artifact_containment_basis",
        ):
            request[key] = {
                **request[key],
                "hostile_payload": copy.deepcopy(hostile_payload),
            }
        before = copy.deepcopy(request)
        result = resolve_request(request)

        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assertEqual(request, before)
        self.assert_no_raw_sentinels(result)
        self.assert_official_enum_strings_preserved(result)
        self.assert_public_block_codes(result)
        self.assert_no_forbidden_creation(result)
        self.assert_generated_booleans_are_bool(result)

    def test_representative_blocking_behavior(self) -> None:
        self.assert_blocked_case("missing request", None)
        self.assert_blocked_case("non-mapping request", ["not", "a", "mapping"])

        cases: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
            ("explicit block intent", set_field("second_carrier_verification_boundary_intent", "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_VERIFICATION_BOUNDARY")),
            ("unsupported intent", set_field("second_carrier_verification_boundary_intent", "UNSUPPORTED_INTENT")),
            ("unsupported scope", set_field("second_carrier_verification_boundary_scope", ["UNSUPPORTED_SCOPE"])),
            ("missing second-carrier success basis", remove_field("selected_second_carrier_success_basis")),
            ("second-carrier success not recorded", set_field("selected_second_carrier_success_result_outcome", "NOT_RECORDED")),
            ("second-carrier success failed checks", set_field("selected_second_carrier_success_failed_check_count", 1)),
            ("second-carrier success version not 0.1.0", set_field("selected_second_carrier_success_result_version", "0.2.0")),
            ("second-carrier success did not record bounded success", set_field("selected_second_carrier_success_bounded_success_recorded", False)),
            ("second-carrier success already created verification", set_field("selected_second_carrier_success_already_created_verification", True)),
            ("second-carrier success already created external result", set_field("selected_second_carrier_success_already_created_external_result", True)),
            ("second-carrier success already created cross-carrier evidence", set_field("selected_second_carrier_success_already_created_cross_carrier_evidence", True)),
            ("second-carrier success already created portable verification closure", set_field("selected_second_carrier_success_already_created_portable_verification_closure", True)),
            ("second-carrier success treated success as verification", set_field("selected_second_carrier_success_treated_success_as_verification", True)),
            ("second-carrier success treated success as external result", set_field("selected_second_carrier_success_treated_success_as_external_result", True)),
            ("second-carrier success treated success as cross-carrier evidence", set_field("selected_second_carrier_success_treated_success_as_cross_carrier_evidence", True)),
            ("second-carrier success treated success as portable verification closure", set_field("selected_second_carrier_success_treated_success_as_portable_verification_closure", True)),
            ("second-carrier success treated zero exit code as verification", set_field("selected_second_carrier_success_zero_exit_code_not_verification", False)),
            ("second-carrier success treated OK as verification", set_field("selected_second_carrier_success_ok_not_verification", False)),
            ("second-carrier success treated Ran 7 tests as cross-carrier proof", set_field("selected_second_carrier_success_ran_7_tests_not_cross_carrier_proof", False)),
            ("second-carrier success treated returned capture as cross-carrier proof", set_field("selected_second_carrier_success_returned_capture_not_cross_carrier_proof", False)),
            ("second-carrier success redacted official enum strings", set_field("selected_second_carrier_success_official_enum_scope_strings_redacted", True)),
            ("second-carrier success boundary basis missing", remove_field("selected_second_carrier_success_boundary_basis")),
            ("second-carrier success boundary not recorded", set_field("selected_second_carrier_success_boundary_result_outcome", "NOT_RECORDED")),
            ("second-carrier success boundary failed checks", set_field("selected_second_carrier_success_boundary_failed_check_count", 1)),
            ("second-carrier result basis missing", remove_field("selected_second_carrier_result_basis")),
            ("second-carrier result not recorded", set_field("selected_second_carrier_result_result_outcome", "NOT_RECORDED")),
            ("second-carrier result failed checks", set_field("selected_second_carrier_result_failed_check_count", 1)),
            ("second-carrier result version not 0.1.0", set_field("selected_second_carrier_result_result_version", "0.2.0")),
            ("second-carrier result did not record bounded result", set_field("selected_second_carrier_result_bounded_result_recorded", False)),
            ("second-carrier result boundary v2 basis missing", remove_field("selected_second_carrier_result_boundary_v2_basis")),
            ("second-carrier result boundary v2 not recorded", set_field("selected_second_carrier_result_boundary_v2_result_outcome", "NOT_RECORDED")),
            ("second-carrier result boundary v2 failed checks", set_field("selected_second_carrier_result_boundary_v2_failed_check_count", 1)),
            ("returned capture intake basis missing", remove_field("selected_returned_second_carrier_live_capture_intake_basis")),
            ("returned capture intake not preserved", set_field("selected_returned_capture_intake_preserved", False)),
            ("returned capture intake not capture-only", set_field("selected_returned_capture_intake_capture_only", False)),
            ("returned MacBook Pro to MacBook Air context not preserved", set_field("selected_returned_capture_from_macbook_pro_to_macbook_air", False)),
            ("placeholder carrier fields repaired", set_field("selected_returned_capture_placeholder_fields_unrepaired", False)),
            ("returned capture material missing", remove_field("selected_returned_capture_material_basis")),
            ("returned zip path missing", remove_field("selected_returned_capture_zip_path")),
            ("returned hash path missing", remove_field("selected_returned_capture_hash_path")),
            ("returned extracted directory missing", remove_field("selected_returned_capture_extracted_directory_path")),
            ("returned combined terminal log missing", remove_field("selected_returned_capture_combined_terminal_log_path")),
            ("returned exit code missing", remove_field("selected_returned_capture_exit_code")),
            ("returned command text missing", remove_field("selected_returned_capture_command_text")),
            ("returned timestamps missing", remove_field("selected_returned_capture_started_at")),
            ("second-carrier output capture basis missing", remove_field("selected_second_carrier_output_capture_basis")),
            ("second-carrier output capture not recorded", set_field("selected_second_carrier_output_capture_result_outcome", "NOT_RECORDED")),
            ("second-carrier output capture failed checks", set_field("selected_second_carrier_output_capture_failed_check_count", 1)),
            ("selected basis not reference-shaped", remove_field("selected_packet_transfer_basis")),
            ("verification boundary treated as verification", flip_non_claim("second_carrier_verification_boundary_treated_as_verification")),
            ("verification boundary treated as external result", flip_non_claim("second_carrier_verification_boundary_treated_as_external_result")),
            ("verification boundary treated as cross-carrier evidence", flip_non_claim("second_carrier_verification_boundary_treated_as_cross_carrier_evidence")),
            ("verification boundary treated as portable verification closure", flip_non_claim("second_carrier_verification_boundary_treated_as_portable_verification_closure")),
            ("verification boundary treated as source transfer", flip_non_claim("second_carrier_verification_boundary_treated_as_source_transfer")),
            ("verification boundary treated as source receipt", flip_non_claim("second_carrier_verification_boundary_treated_as_source_receipt")),
            ("verification boundary treated as reception authorization", flip_non_claim("second_carrier_verification_boundary_treated_as_reception_authorization")),
            ("verification boundary treated as source", flip_non_claim("second_carrier_verification_boundary_treated_as_source")),
            ("verification boundary treated as authority", flip_non_claim("second_carrier_verification_boundary_treated_as_authority")),
            ("verification boundary treated as currentness", flip_non_claim("second_carrier_verification_boundary_treated_as_currentness")),
            ("verification boundary treated as final completion", flip_non_claim("second_carrier_verification_boundary_treated_as_final_completion")),
            ("verification boundary treated as runtime", flip_non_claim("second_carrier_verification_boundary_treated_as_runtime")),
            ("verification boundary treated as continuation", flip_non_claim("second_carrier_verification_boundary_treated_as_continuation")),
            ("verification boundary treated as reusable permission", flip_non_claim("second_carrier_verification_boundary_treated_as_reusable_permission")),
            ("verification boundary treated as follow-on work", flip_non_claim("second_carrier_verification_boundary_treated_as_follow_on_work")),
            ("success treated as verification", flip_non_claim("second_carrier_success_treated_as_verification")),
            ("success treated as external result", flip_non_claim("second_carrier_success_treated_as_external_result")),
            ("zero exit code treated as verification", flip_non_claim("zero_exit_code_treated_as_verification")),
            ("OK output treated as verification", flip_non_claim("ok_output_treated_as_verification")),
            ("Ran 7 tests treated as cross-carrier proof", flip_non_claim("ran_7_tests_treated_as_cross_carrier_proof")),
            ("returned capture treated as cross-carrier evidence", flip_non_claim("returned_capture_treated_as_cross_carrier_evidence")),
            ("verification created", flip_non_claim("verification_created")),
            ("external result created", flip_non_claim("external_result_created")),
            ("cross-carrier evidence created", flip_non_claim("cross_carrier_evidence_created")),
            ("portable verification closure created", flip_non_claim("portable_verification_closure_created")),
            ("source transfer occurred", flip_non_claim("source_transfer_occurred")),
            ("source receipt occurred", flip_non_claim("source_receipt_occurred")),
            ("reception authorization created", flip_non_claim("reception_authorization_created")),
            ("source created", flip_non_claim("source_created")),
            ("authority created", flip_non_claim("authority_created")),
            ("currentness created", flip_non_claim("currentness_created")),
            ("final completion claimed", flip_non_claim("final_completion_claimed")),
            ("runtime hosting created", flip_non_claim("runtime_hosting_created")),
            ("deployment created", flip_non_claim("deployment_created")),
            ("public release created", flip_non_claim("public_release_created")),
            ("operation permission created", flip_non_claim("operation_permission_created")),
            ("continuation authorized", flip_non_claim("continuation_authorized")),
            ("reusable permission created", flip_non_claim("reusable_permission_created")),
            ("derivative reception authorized", flip_non_claim("derivative_reception_authorized")),
            ("vessel relation authorized", flip_non_claim("vessel_relation_authorized")),
            ("another reception request authorized", flip_non_claim("another_reception_request_authorized")),
            ("follow-on authorized", flip_non_claim("follow_on_work_authorized")),
            ("receiving carrier treated as authority", flip_non_claim("receiving_carrier_treated_as_authority")),
            ("artifact existence treated as verification authority", flip_non_claim("artifact_existence_treated_as_verification_authority")),
            ("artifact path treated as currentness", flip_non_claim("artifact_path_treated_as_currentness")),
            ("repo-local availability treated as verification authority", flip_non_claim("repo_local_availability_treated_as_verification_authority")),
            ("hidden repo state used as verification content", flip_non_claim("hidden_repo_state_used_as_verification_content")),
            ("hidden repo state used as verification authority", flip_non_claim("hidden_repo_state_used_as_verification_authority")),
            ("raw full prior artifact body returned", flip_non_claim("raw_full_prior_artifact_body_returned")),
            ("predecessor failure evidence repaired", flip_non_claim("v1_repaired")),
            ("predecessor failure evidence hidden", flip_non_claim("v1_hidden")),
            ("predecessor failure evidence claimed passed", flip_non_claim("v1_claimed_passed")),
            ("first success-boundary test repaired", flip_non_claim("first_success_boundary_test_repaired")),
            ("first success-boundary test hidden", flip_non_claim("first_success_boundary_test_hidden")),
            ("first success-boundary test claimed passed", flip_non_claim("first_success_boundary_test_claimed_passed")),
            ("first result-boundary resolver repaired", flip_non_claim("first_result_boundary_resolver_repaired")),
            ("first result-boundary resolver hidden", flip_non_claim("first_result_boundary_resolver_hidden")),
            ("first result-boundary resolver claimed passed", flip_non_claim("first_result_boundary_resolver_claimed_passed")),
            ("consumed request reopened", flip_non_claim("consumed_request_reopened")),
            ("authorization token reused", flip_non_claim("authorization_token_reused")),
            ("artifacts mutated", flip_non_claim("prior_artifacts_mutated")),
            ("returned capture material mutated", flip_non_claim("returned_capture_material_mutated")),
            ("required non-claim flipped", flip_non_claim("verification_created")),
        )
        for name, mutator in cases:
            with self.subTest(name=name):
                self.assert_blocked_case(name, mutate_request(mutator))

        declared_only_codes = (
            "RETURNED_CAPTURE_TREATED_AS_VERIFICATION",
            "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_PROOF",
            "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENT_REPORT_ARTIFACT",
            "COMMAND_REPORT_LINEAGE_TREATED_AS_SOURCE",
            "COMMAND_REPORT_LINEAGE_TREATED_AS_AUTHORITY",
            "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENTNESS",
            "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_VERIFICATION_BOUNDARY",
        )
        for code in declared_only_codes:
            with self.subTest(name=f"declared block {code}"):
                self.assert_blocked_case(code, declared_block(code), code)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir_name:
            temp_dir = Path(temp_dir_name)
            request_path = temp_dir / "request.json"
            request_path.write_text(json.dumps(build_request()), encoding="utf-8")
            result = resolver.resolve_portable_source_body_verification_second_carrier_verification_boundary_from_path(
                request_path
            )
            summary = resolver.build_portable_source_body_verification_second_carrier_verification_boundary_summary(
                result
            )
            self.assertEqual(result["outcome"], RECORDED)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(
                summary["resolver_module"],
                "resolve_portable_source_body_verification_second_carrier_verification_boundary",
            )

            bad_json_path = temp_dir / "bad.json"
            bad_json_path.write_text("{not-json", encoding="utf-8")
            with self.assertRaises(
                resolver.PortableSourceBodyVerificationSecondCarrierVerificationBoundaryError
            ):
                resolver.resolve_portable_source_body_verification_second_carrier_verification_boundary_from_path(
                    bad_json_path
                )
            array_path = temp_dir / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            with self.assertRaises(
                resolver.PortableSourceBodyVerificationSecondCarrierVerificationBoundaryError
            ):
                resolver.resolve_portable_source_body_verification_second_carrier_verification_boundary_from_path(
                    array_path
                )
            with self.assertRaises(
                resolver.PortableSourceBodyVerificationSecondCarrierVerificationBoundaryError
            ):
                resolver.resolve_portable_source_body_verification_second_carrier_verification_boundary_from_path(
                    temp_dir / "missing.json"
                )

            output_root = (
                temp_dir
                / "artifacts"
                / "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_verification_boundary"
            )
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_portable_source_body_verification_second_carrier_verification_boundary_result(
                    result
                )
                second_path = resolver.write_portable_source_body_verification_second_carrier_verification_boundary_result(
                    result
                )
            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertTrue(first_path.parent.exists())
            parsed = json.loads(first_path.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], RECORDED)
            self.assertEqual(
                output_root.name,
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_verification_boundary",
            )
            first_path_text = first_path.as_posix()
            for forbidden in (
                "actual_second_carrier_live_capture",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_verification/",
                "second_carrier_success/",
                "second_carrier_success_boundary",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_result/",
                "second_carrier_result_boundary_v2",
                "external_result",
                "cross_carrier",
                "portable_verification_closure",
                "runtime",
                "deployment",
                "public_release",
            ):
                self.assertNotIn(forbidden, first_path_text)

    def test_non_mutation_of_request_and_selected_inputs(self) -> None:
        request = build_request()
        request["second_carrier_verification_boundary_scope"] = list(SUPPORTED_SCOPE)
        for key in SELECTED_BASIS_KEYS:
            request[key] = {
                "basis_id": key,
                "nested": [{"reference_shape": True, "key": key}],
            }
        for key in POSTURE_KEYS:
            request[key] = True
        request["declared_non_claims"] = {
            key: False for key in REQUIRED_FALSE_NON_CLAIMS
        }
        before = copy.deepcopy(request)
        result = resolve_request(request)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(request, before)
        self.assert_selected_basis_reference_shaped(result)

    def test_predecessor_failure_preservation(self) -> None:
        result = resolve_request(build_request())
        summary = resolver.build_portable_source_body_verification_second_carrier_verification_boundary_summary(
            result
        )
        st = statement(result)
        nc = non_claims(result)
        predecessor = result["selected_predecessor_failure_basis"]
        v1 = result["selected_packet_emission_boundary_v1_predecessor_failure_basis"]
        self.assertIn("first success-boundary test remains", __doc__ or "")
        self.assertIn("does not repair", __doc__ or "")
        self.assertIs(st["first_success_boundary_test_failure_preserved"], True)
        self.assertIs(st["first_result_boundary_resolver_failure_preserved"], True)
        self.assertIs(predecessor["basis_declared"], True)
        self.assertIs(predecessor["basis_reference_shape_preserved"], True)
        self.assertIs(v1["basis_declared"], True)
        self.assertIs(v1["basis_reference_shape_preserved"], True)
        self.assertIs(nc["first_success_boundary_test_repaired"], False)
        self.assertIs(nc["first_success_boundary_test_hidden"], False)
        self.assertIs(nc["first_success_boundary_test_claimed_passed"], False)
        self.assertIs(nc["v1_repaired"], False)
        self.assertIs(nc["v1_hidden"], False)
        self.assertIs(nc["v1_claimed_passed"], False)
        self.assertIs(nc["first_result_boundary_resolver_repaired"], False)
        self.assertIs(nc["first_result_boundary_resolver_hidden"], False)
        self.assertIs(nc["first_result_boundary_resolver_claimed_passed"], False)
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


if __name__ == "__main__":
    unittest.main()
