"""Executable checks for second-carrier success posture only.

This suite is downstream of the second-carrier-success-boundary line. It
verifies that the resolver records one bounded second-carrier success posture
only: success is not verification, external result, cross-carrier proof,
portable verification closure, source transfer, source receipt, reception
authorization, source, authority, currentness, runtime, final completion,
continuation, reusable permission, or follow-on work.

The predecessor success-boundary test remains preserved failed predecessor test
evidence. This suite does not repair, hide, delete, rename, or claim passed that
test. It also preserves the first result-boundary resolver and v1
packet-emission-boundary surfaces as predecessor failure evidence. Official
enum, scope, and block-code strings are checked for exact preservation, while
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

import resolve_portable_source_body_verification_second_carrier_success as resolver


RECORDED = resolver.OUTCOME_RECORDED
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = set(resolver.OUTCOME_FAMILY)
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_SECOND_CARRIER_SUCCESS_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
TRUE_RECORDED_FIELDS = tuple(resolver.ALLOWED_TRUE_RECORDED_FIELDS)
SELECTED_BASIS_KEYS = tuple(resolver.SELECTED_BASIS_KEYS)
POSTURE_KEYS = tuple(resolver.POSTURE_KEYS)

RAW_SENTINELS = (
    "RAW_SECOND_CARRIER_SUCCESS_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
    "HOSTILE_SECOND_CARRIER_SUCCESS_FULL_BODY_VALUE_MUST_NOT_RETURN",
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
    "hostile-capture-body-value",
    "hostile-second-carrier-success-body-value",
    "hostile-verification-body-value",
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
    "[bounded-success-redacted]",
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
    "portable_source_body_verification_second_carrier_success_metadata",
    "declared_second_carrier_success_question",
    "selected_second_carrier_success_boundary_basis",
    "selected_second_carrier_success_boundary_terminal_summary_basis",
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
    "second_carrier_success_spec_only_posture",
    "one_bounded_second_carrier_success_posture",
    "second_carrier_success_boundary_basis_preserved_posture",
    "second_carrier_result_basis_preserved_posture",
    "returned_second_carrier_capture_basis_preserved_posture",
    "capture_intake_basis_preserved_posture",
    "second_carrier_output_capture_basis_preserved_posture",
    "success_recorded_bounded_posture",
    "success_artifact_recorded_or_bounded_posture",
    "success_not_verification_posture",
    "success_not_external_result_posture",
    "success_not_cross_carrier_evidence_posture",
    "success_not_portable_verification_closure_posture",
    "success_not_source_transfer_posture",
    "success_not_source_receipt_posture",
    "success_not_reception_authorization_posture",
    "zero_exit_code_not_success_as_standalone_inference_posture",
    "ok_output_not_verification_posture",
    "ran_7_tests_not_cross_carrier_proof_posture",
    "returned_capture_not_cross_carrier_proof_posture",
    "verification_not_created_posture",
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
    "repo_local_availability_not_success_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "first_success_boundary_test_failure_preserved_posture",
    "first_result_boundary_resolver_failure_preserved_posture",
    "second_carrier_success_scope",
    "second_carrier_success_checks",
    "second_carrier_success_statement",
    "second_carrier_success_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_second_carrier_success_summary",
)

REPRESENTATIVE_BLOCK_CODES = (
    "SECOND_CARRIER_SUCCESS_QUESTION_UNDECLARED",
    "SECOND_CARRIER_SUCCESS_INTENT_UNSUPPORTED",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_BASIS_MISSING",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_NOT_RECORDED",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_VERSION_NOT_0_1_0",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_DID_NOT_DECLARE_FUTURE_SUCCESS_STEP",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_ALREADY_CREATED_SUCCESS",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_ALREADY_CREATED_VERIFICATION",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_ALREADY_CREATED_EXTERNAL_RESULT",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_ALREADY_CREATED_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_ALREADY_CREATED_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_SUCCESS_BOUNDARY_AS_SUCCESS",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_SUCCESS_BOUNDARY_AS_VERIFICATION",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_SUCCESS_BOUNDARY_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_SUCCESS_BOUNDARY_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_SUCCESS_BOUNDARY_AS_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_ZERO_EXIT_CODE_AS_SUCCESS",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_OK_AS_VERIFICATION",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_TREATED_RAN_7_TESTS_AS_CROSS_CARRIER_PROOF",
    "SECOND_CARRIER_SUCCESS_BOUNDARY_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
    "SECOND_CARRIER_RESULT_BASIS_MISSING",
    "SECOND_CARRIER_RESULT_NOT_RECORDED",
    "SECOND_CARRIER_RESULT_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_RESULT_ALREADY_CREATED_SUCCESS",
    "SECOND_CARRIER_RESULT_ALREADY_CREATED_VERIFICATION",
    "SECOND_CARRIER_RESULT_ALREADY_CREATED_EXTERNAL_RESULT",
    "SECOND_CARRIER_RESULT_ALREADY_CREATED_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_RESULT_TREATED_RESULT_AS_SUCCESS",
    "SECOND_CARRIER_RESULT_TREATED_RESULT_AS_VERIFICATION",
    "SECOND_CARRIER_RESULT_TREATED_ZERO_EXIT_CODE_AS_SUCCESS",
    "SECOND_CARRIER_RESULT_TREATED_OK_AS_VERIFICATION",
    "SECOND_CARRIER_RESULT_TREATED_RAN_7_TESTS_AS_CROSS_CARRIER_PROOF",
    "RETURNED_CAPTURE_INTAKE_BASIS_MISSING",
    "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
    "RETURNED_CAPTURE_TREATED_AS_SUCCESS",
    "RETURNED_CAPTURE_TREATED_AS_VERIFICATION",
    "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_PROOF",
    "PLACEHOLDER_CARRIER_FIELDS_REPAIRED",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BASIS_MISSING",
    "SECOND_CARRIER_OUTPUT_CAPTURE_NOT_RECORDED",
    "SECOND_CARRIER_OUTPUT_CAPTURE_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_SUCCESS_TREATED_AS_VERIFICATION",
    "SECOND_CARRIER_SUCCESS_TREATED_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_SUCCESS_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_SUCCESS_TREATED_AS_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_SUCCESS_TREATED_AS_SOURCE_TRANSFER",
    "SECOND_CARRIER_SUCCESS_TREATED_AS_SOURCE_RECEIPT",
    "SECOND_CARRIER_SUCCESS_TREATED_AS_RECEPTION_AUTHORIZATION",
    "SECOND_CARRIER_SUCCESS_TREATED_AS_SOURCE",
    "SECOND_CARRIER_SUCCESS_TREATED_AS_AUTHORITY",
    "SECOND_CARRIER_SUCCESS_TREATED_AS_CURRENTNESS",
    "SECOND_CARRIER_SUCCESS_TREATED_AS_FINAL_COMPLETION",
    "SECOND_CARRIER_SUCCESS_TREATED_AS_RUNTIME",
    "SECOND_CARRIER_SUCCESS_TREATED_AS_CONTINUATION",
    "SECOND_CARRIER_SUCCESS_TREATED_AS_REUSABLE_PERMISSION",
    "SECOND_CARRIER_SUCCESS_TREATED_AS_FOLLOW_ON_WORK",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_SUCCESS_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_SUCCESS_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_SUCCESS_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_SUCCESS_AUTHORITY",
    "FIRST_SUCCESS_BOUNDARY_TEST_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    "FIRST_RESULT_BOUNDARY_RESOLVER_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_SUCCESS",
    "ARTIFACTS_MUTATED",
    "RETURNED_CAPTURE_MATERIAL_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_SECOND_CARRIER_SUCCESS_SCOPE",
)


def build_request(**overrides: Any) -> dict[str, Any]:
    return resolver.build_declared_portable_source_body_verification_second_carrier_success_request(
        **overrides
    )


def resolve_request(request: Any) -> dict[str, Any]:
    return resolver.resolve_portable_source_body_verification_second_carrier_success(
        request
    )


def checks(result: dict[str, Any]) -> list[dict[str, Any]]:
    return list(result.get("second_carrier_success_checks", ()))


def statement(result: dict[str, Any]) -> dict[str, Any]:
    return dict(result.get("second_carrier_success_statement", {}))


def non_claims(result: dict[str, Any]) -> dict[str, Any]:
    return dict(result.get("non_claims", {}))


def non_meaning(result: dict[str, Any]) -> dict[str, Any]:
    return dict(result.get("second_carrier_success_non_meaning", {}))


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


class PortableSourceBodyVerificationSecondCarrierSuccessTests(unittest.TestCase):
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
                if key == "posture_key":
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
        scope = tuple(result.get("second_carrier_success_scope", ()))
        for official in OFFICIAL_SCOPE_VALUES:
            self.assertIn(official, scope)
        self.assertIn("OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED", scope)
        for value in scope:
            self.assertNotIn(value, REDACTION_PLACEHOLDERS)
        for supported_value in SUPPORTED_SCOPE:
            self.assertNotIn(supported_value, REDACTION_PLACEHOLDERS)
        self.assert_public_block_codes(result)

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
            "success_became_verification",
            "success_became_external_result",
            "success_became_cross_carrier_proof",
            "success_became_portable_verification_closure",
            "returned_capture_became_proof",
            "zero_exit_code_became_automatic_success_without_bounded_resolver_admission",
            "ok_became_verification",
            "ran_7_tests_became_cross_carrier_proof",
            "macbook_pro_became_authority",
            "macbook_air_became_source",
            "artifact_existence_became_success_authority",
            "artifact_path_became_currentness",
            "repo_local_availability_became_success_authority",
            "hidden_repo_state_became_success_authority",
        ):
            self.assertIs(nm.get(key), False, key)

    def assert_blocked_case(self, name: str, request: Any) -> dict[str, Any]:
        result = resolve_request(request)
        self.assertEqual(result["outcome"], BLOCKED, name)
        self.assertIsInstance(result.get("block"), dict, name)
        self.assertIsNotNone(result["block"].get("block_code"), name)
        self.assert_public_block_codes(result)
        self.assert_no_forbidden_creation(result)
        self.assert_generated_booleans_are_bool(result)
        return result

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_portable_source_body_verification_second_carrier_success",
            "resolve_portable_source_body_verification_second_carrier_success_from_path",
            "write_portable_source_body_verification_second_carrier_success_result",
            "build_portable_source_body_verification_second_carrier_success_summary",
            "build_declared_portable_source_body_verification_second_carrier_success_request",
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
            "SUPPORTED_SECOND_CARRIER_SUCCESS_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_portable_source_body_verification_second_carrier_success",
        )
        self.assertEqual(
            resolver.SUPPORTED_SECOND_CARRIER_SUCCESS_SCOPE,
            resolver.SUPPORTED_SCOPE_VALUES,
        )
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_success"
            )
        )
        for scope_value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(scope_value, SUPPORTED_SCOPE)
        for code in REPRESENTATIVE_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES, code)

    def test_successful_recorded_result_from_builder(self) -> None:
        request = build_request()
        result = resolve_request(request)
        summary = resolver.build_portable_source_body_verification_second_carrier_success_summary(
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
            "resolve_portable_source_body_verification_second_carrier_success",
        )
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["request_id"], request["second_carrier_success_request_id"])
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
        self.assert_no_forbidden_creation(result)

    def test_official_enum_strings_are_preserved_without_placeholder_redaction(
        self,
    ) -> None:
        result = resolve_request(build_request())
        scope = tuple(result["second_carrier_success_scope"])
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
            second_carrier_success_scope=list(
                resolver.SUPPORTED_SECOND_CARRIER_SUCCESS_SCOPE
            )
        )
        custom_result = resolve_request(custom_request)
        self.assertEqual(custom_result["outcome"], RECORDED)
        self.assertEqual(
            tuple(custom_result["second_carrier_success_scope"]),
            tuple(resolver.SUPPORTED_SECOND_CARRIER_SUCCESS_SCOPE),
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
            "capture_body": "hostile-capture-body-value",
            "second_carrier_success_body": (
                "hostile-second-carrier-success-body-value"
            ),
            "verification_body": "hostile-verification-body-value",
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
                    "RAW_SECOND_CARRIER_SUCCESS_BODY_MUST_NOT_RETURN",
                    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
                    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
                ]
            },
        }
        for key in (
            "selected_second_carrier_success_boundary_basis",
            "selected_second_carrier_success_boundary_terminal_summary_basis",
            "selected_second_carrier_result_basis",
            "selected_second_carrier_result_terminal_summary_basis",
            "selected_second_carrier_result_boundary_v2_basis",
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
            ("explicit block intent", set_field("second_carrier_success_intent", "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_SUCCESS")),
            ("unsupported intent", set_field("second_carrier_success_intent", "UNSUPPORTED_INTENT")),
            ("unsupported scope", set_field("second_carrier_success_scope", ["UNSUPPORTED_SCOPE"])),
            ("missing second-carrier success boundary basis", remove_field("selected_second_carrier_success_boundary_basis")),
            ("second-carrier success boundary not recorded", set_field("selected_second_carrier_success_boundary_result_outcome", "NOT_RECORDED")),
            ("second-carrier success boundary failed checks", set_field("selected_second_carrier_success_boundary_failed_check_count", 1)),
            ("second-carrier success boundary version not 0.1.0", set_field("selected_second_carrier_success_boundary_result_version", "0.2.0")),
            ("second-carrier success boundary did not declare future success step", set_field("selected_second_carrier_success_boundary_declared_future_success_step", False)),
            ("second-carrier success boundary already created success", set_field("selected_second_carrier_success_boundary_already_created_success", True)),
            ("second-carrier success boundary already created verification", set_field("selected_second_carrier_success_boundary_already_created_verification", True)),
            ("second-carrier success boundary already created external result", set_field("selected_second_carrier_success_boundary_already_created_external_result", True)),
            ("second-carrier success boundary already created cross-carrier evidence", set_field("selected_second_carrier_success_boundary_already_created_cross_carrier_evidence", True)),
            ("second-carrier success boundary already created portable verification closure", set_field("selected_second_carrier_success_boundary_already_created_portable_verification_closure", True)),
            ("second-carrier success boundary treated boundary as success", set_field("selected_second_carrier_success_boundary_treated_success_boundary_as_success", True)),
            ("second-carrier success boundary treated boundary as verification", set_field("selected_second_carrier_success_boundary_treated_success_boundary_as_verification", True)),
            ("second-carrier success boundary treated boundary as external result", set_field("selected_second_carrier_success_boundary_treated_success_boundary_as_external_result", True)),
            ("second-carrier success boundary treated boundary as cross-carrier evidence", set_field("selected_second_carrier_success_boundary_treated_success_boundary_as_cross_carrier_evidence", True)),
            ("second-carrier success boundary treated boundary as portable verification closure", set_field("selected_second_carrier_success_boundary_treated_success_boundary_as_portable_verification_closure", True)),
            ("second-carrier success boundary treated zero exit code as success", set_field("selected_second_carrier_success_boundary_zero_exit_code_not_success", False)),
            ("second-carrier success boundary treated OK as verification", set_field("selected_second_carrier_success_boundary_ok_not_verification", False)),
            ("second-carrier success boundary treated Ran 7 tests as cross-carrier proof", set_field("selected_second_carrier_success_boundary_ran_7_tests_not_cross_carrier_proof", False)),
            ("second-carrier success boundary redacted official enum strings", set_field("selected_second_carrier_success_boundary_official_enum_scope_strings_redacted", True)),
            ("second-carrier result basis missing", remove_field("selected_second_carrier_result_basis")),
            ("second-carrier result not recorded", set_field("selected_second_carrier_result_result_outcome", "NOT_RECORDED")),
            ("second-carrier result failed checks", set_field("selected_second_carrier_result_failed_check_count", 1)),
            ("second-carrier result already created success", set_field("selected_second_carrier_result_already_created_success", True)),
            ("second-carrier result already created verification", set_field("selected_second_carrier_result_already_created_verification", True)),
            ("second-carrier result already created external result", set_field("selected_second_carrier_result_already_created_external_result", True)),
            ("second-carrier result already created cross-carrier evidence", set_field("selected_second_carrier_result_already_created_cross_carrier_evidence", True)),
            ("second-carrier result treated result as success", set_field("selected_second_carrier_result_treated_result_as_success", True)),
            ("second-carrier result treated result as verification", set_field("selected_second_carrier_result_treated_result_as_verification", True)),
            ("second-carrier result treated zero exit code as success", set_field("selected_second_carrier_result_treated_zero_exit_code_as_success", True)),
            ("second-carrier result treated OK as verification", set_field("selected_second_carrier_result_treated_ok_as_verification", True)),
            ("second-carrier result treated Ran 7 tests as cross-carrier proof", set_field("selected_second_carrier_result_treated_ran_7_tests_as_cross_carrier_proof", True)),
            ("returned capture intake basis missing", remove_field("selected_returned_second_carrier_live_capture_intake_basis")),
            ("returned capture intake not preserved", set_field("selected_returned_capture_intake_preserved", False)),
            ("returned capture treated as success", set_field("returned_capture_treated_as_success", True)),
            ("returned capture treated as verification", set_field("returned_capture_treated_as_verification", True)),
            ("returned capture treated as cross-carrier proof", set_field("returned_capture_treated_as_cross_carrier_proof", True)),
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
            ("success treated as verification", flip_non_claim("second_carrier_success_treated_as_verification")),
            ("success treated as external result", flip_non_claim("second_carrier_success_treated_as_external_result")),
            ("success treated as cross-carrier evidence", flip_non_claim("second_carrier_success_treated_as_cross_carrier_evidence")),
            ("success treated as portable verification closure", flip_non_claim("second_carrier_success_treated_as_portable_verification_closure")),
            ("success treated as source transfer", flip_non_claim("second_carrier_success_treated_as_source_transfer")),
            ("success treated as source receipt", flip_non_claim("second_carrier_success_treated_as_source_receipt")),
            ("success treated as reception authorization", flip_non_claim("second_carrier_success_treated_as_reception_authorization")),
            ("success treated as source", flip_non_claim("second_carrier_success_treated_as_source")),
            ("success treated as authority", flip_non_claim("second_carrier_success_treated_as_authority")),
            ("success treated as currentness", flip_non_claim("second_carrier_success_treated_as_currentness")),
            ("success treated as final completion", flip_non_claim("second_carrier_success_treated_as_final_completion")),
            ("success treated as runtime", flip_non_claim("second_carrier_success_treated_as_runtime")),
            ("success treated as continuation", flip_non_claim("second_carrier_success_treated_as_continuation")),
            ("success treated as reusable permission", flip_non_claim("second_carrier_success_treated_as_reusable_permission")),
            ("success treated as follow-on work", flip_non_claim("second_carrier_success_treated_as_follow_on_work")),
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
            ("artifact existence treated as success authority", flip_non_claim("artifact_existence_treated_as_success_authority")),
            ("artifact path treated as currentness", flip_non_claim("artifact_path_treated_as_currentness")),
            ("repo-local availability treated as success authority", flip_non_claim("repo_local_availability_treated_as_success_authority")),
            ("hidden repo state used as success content", flip_non_claim("hidden_repo_state_used_as_success_content")),
            ("hidden repo state used as success authority", flip_non_claim("hidden_repo_state_used_as_success_authority")),
            ("selected basis not reference-shaped", set_field("reference_shaped_input_posture", False)),
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
            ("command report lineage treated as current report artifact", set_field("command_report_lineage_treated_as_current_report_artifact", True)),
            ("command report lineage treated as source", set_field("command_report_lineage_treated_as_source", True)),
            ("command report lineage treated as authority", set_field("command_report_lineage_treated_as_authority", True)),
            ("command report lineage treated as currentness", set_field("command_report_lineage_treated_as_currentness", True)),
            ("consumed request reopened", flip_non_claim("consumed_request_reopened")),
            ("authorization token reused", flip_non_claim("authorization_token_reused")),
            ("full prior artifact body emitted outside bounded success posture", set_field("full_prior_artifact_body_emitted_outside_bounded_success", True)),
            ("artifacts mutated", set_field("artifacts_mutated", True)),
            ("returned capture material mutated", flip_non_claim("returned_capture_material_mutated")),
            ("required non-claim flipped", flip_non_claim("verification_created")),
        )
        for name, mutator in cases:
            with self.subTest(name=name):
                self.assert_blocked_case(name, mutate_request(mutator))

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir_name:
            temp_dir = Path(temp_dir_name)
            request_path = temp_dir / "request.json"
            request_path.write_text(json.dumps(build_request()), encoding="utf-8")
            result = resolver.resolve_portable_source_body_verification_second_carrier_success_from_path(
                request_path
            )
            summary = resolver.build_portable_source_body_verification_second_carrier_success_summary(
                result
            )
            self.assertEqual(result["outcome"], RECORDED)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(
                summary["resolver_module"],
                "resolve_portable_source_body_verification_second_carrier_success",
            )

            bad_json_path = temp_dir / "bad.json"
            bad_json_path.write_text("{not-json", encoding="utf-8")
            with self.assertRaises(
                resolver.PortableSourceBodyVerificationSecondCarrierSuccessError
            ):
                resolver.resolve_portable_source_body_verification_second_carrier_success_from_path(
                    bad_json_path
                )
            array_path = temp_dir / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolver.resolve_portable_source_body_verification_second_carrier_success_from_path(
                array_path
            )
            self.assertEqual(array_result["outcome"], BLOCKED)
            with self.assertRaises(
                resolver.PortableSourceBodyVerificationSecondCarrierSuccessError
            ):
                resolver.resolve_portable_source_body_verification_second_carrier_success_from_path(
                    temp_dir / "missing.json"
                )

            output_root = (
                temp_dir
                / "artifacts"
                / "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_success"
            )
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_portable_source_body_verification_second_carrier_success_result(
                    result
                )
                second_path = resolver.write_portable_source_body_verification_second_carrier_success_result(
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
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_success",
            )
            first_path_text = first_path.as_posix()
            for forbidden in (
                "actual_second_carrier_live_capture",
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
        request["second_carrier_success_scope"] = {"values": list(SUPPORTED_SCOPE)}
        for key in SELECTED_BASIS_KEYS:
            request[key] = {
                "basis_id": key,
                "nested": [{"reference_shape": True, "key": key}],
            }
        for key in POSTURE_KEYS:
            request[key] = True
        before = copy.deepcopy(request)
        result = resolve_request(request)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(request, before)

    def test_predecessor_failure_preservation(self) -> None:
        result = resolve_request(build_request())
        summary = resolver.build_portable_source_body_verification_second_carrier_success_summary(
            result
        )
        st = statement(result)
        nc = non_claims(result)
        predecessor = result["selected_predecessor_failure_basis"]
        v1 = result["selected_packet_emission_boundary_v1_predecessor_failure_basis"]
        self.assertIn("predecessor success-boundary test remains", __doc__ or "")
        self.assertIn("does not repair", __doc__ or "")
        self.assertIs(st["first_success_boundary_test_failure_preserved"], True)
        self.assertIs(st["first_result_boundary_resolver_failure_preserved"], True)
        self.assertIs(predecessor["first_success_boundary_test_failure_preserved"], True)
        self.assertIs(predecessor["first_success_boundary_test_not_repaired"], True)
        self.assertIs(predecessor["first_success_boundary_test_not_hidden"], True)
        self.assertIs(predecessor["first_success_boundary_test_not_claimed_passed"], True)
        self.assertIs(predecessor["first_result_boundary_resolver_failure_preserved"], True)
        self.assertIs(predecessor["first_result_boundary_resolver_not_repaired"], True)
        self.assertIs(predecessor["first_result_boundary_resolver_not_hidden"], True)
        self.assertIs(predecessor["first_result_boundary_resolver_not_claimed_passed"], True)
        self.assertIs(v1["v1_predecessor_failure_preserved"], True)
        self.assertIs(v1["v1_not_repaired"], True)
        self.assertIs(v1["v1_not_hidden"], True)
        self.assertIs(v1["v1_not_claimed_passed"], True)
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
