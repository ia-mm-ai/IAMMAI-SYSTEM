"""Executable checks for cross-carrier evidence v2 posture only.

This suite is downstream of the cross-carrier-evidence-boundary line. It
verifies that the v2 resolver records one bounded cross-carrier evidence
posture only and blocks the predecessor-missed overreach conditions where the
boundary treats string "0" as doctrine or promotes returned capture into
cross-carrier evidence/proof.

The predecessor cross-carrier evidence resolver remains preserved
conformance-failure evidence. This suite does not repair, hide, rename, delete,
or claim passed that predecessor. It also preserves predecessor external-result
v1, first success-boundary, first result-boundary, and v1 packet-emission
failure surfaces as preserved predecessor evidence. Official enum, scope, and
block-code strings are checked for exact preservation while hostile raw body
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

import resolve_portable_source_body_verification_cross_carrier_evidence_v2 as resolver


RECORDED = resolver.OUTCOME_RECORDED
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = set(resolver.OUTCOME_FAMILY)
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_CROSS_CARRIER_EVIDENCE_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
TRUE_RECORDED_FIELDS = tuple(resolver.ALLOWED_TRUE_RECORDED_FIELDS)
SELECTED_BASIS_KEYS = tuple(resolver.SELECTED_BASIS_KEYS)
POSTURE_KEYS = tuple(resolver.POSTURE_KEYS)

RAW_SENTINELS = (
    "RAW_CROSS_CARRIER_EVIDENCE_BODY_MUST_NOT_RETURN",
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
    "hostile-capture-body-value",
    "hostile-cross-carrier-evidence-body-value",
    "hostile-portable-verification-closure-body-value",
    "hostile-source-body-value",
    "hostile-authority-body-value",
    "hostile-current-working-tree-value",
    "hostile-local-cache-value",
    "hostile-repo-local-only-dependency-value",
)
REDACTION_PLACEHOLDERS = {
    "[bounded-cross-carrier-evidence-redacted]",
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
    "STRING_ZERO_NOT_CROSS_CARRIER_EVIDENCE_AS_STANDALONE_INFERENCE",
    "CROSS_CARRIER_EVIDENCE_NOT_PORTABLE_VERIFICATION_CLOSURE",
)

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_cross_carrier_evidence_metadata",
    "declared_cross_carrier_evidence_question",
    "selected_cross_carrier_evidence_boundary_basis",
    "selected_cross_carrier_evidence_boundary_terminal_summary_basis",
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
    "cross_carrier_evidence_spec_only_posture",
    "one_bounded_cross_carrier_evidence_posture",
    "cross_carrier_evidence_boundary_basis_preserved_posture",
    "second_carrier_external_result_basis_preserved_posture",
    "external_result_artifact_basis_preserved_posture",
    "returned_second_carrier_capture_basis_preserved_posture",
    "capture_intake_basis_preserved_posture",
    "second_carrier_output_capture_basis_preserved_posture",
    "cross_carrier_evidence_recorded_bounded_posture",
    "cross_carrier_evidence_artifact_recorded_or_bounded_posture",
    "cross_carrier_evidence_not_portable_verification_closure_posture",
    "cross_carrier_evidence_not_source_transfer_posture",
    "cross_carrier_evidence_not_source_receipt_posture",
    "cross_carrier_evidence_not_reception_authorization_posture",
    "zero_exit_code_not_cross_carrier_evidence_as_standalone_inference_posture",
    "string_zero_not_cross_carrier_evidence_as_standalone_inference_posture",
    "ok_output_not_cross_carrier_evidence_as_standalone_inference_posture",
    "ran_7_tests_not_cross_carrier_evidence_as_standalone_inference_posture",
    "returned_capture_not_cross_carrier_evidence_as_standalone_inference_posture",
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
    "repo_local_availability_not_cross_carrier_evidence_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_external_result_v1_failure_preserved_posture",
    "first_success_boundary_test_failure_preserved_posture",
    "first_result_boundary_resolver_failure_preserved_posture",
    "cross_carrier_evidence_scope",
    "cross_carrier_evidence_checks",
    "cross_carrier_evidence_statement",
    "cross_carrier_evidence_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_cross_carrier_evidence_summary",
)

REPRESENTATIVE_BLOCK_CODES = (
    "CROSS_CARRIER_EVIDENCE_QUESTION_UNDECLARED",
    "CROSS_CARRIER_EVIDENCE_INTENT_UNSUPPORTED",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_BASIS_MISSING",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_NOT_RECORDED",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_FAILED_CHECKS_PRESENT",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_VERSION_NOT_0_1_0",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_DID_NOT_DECLARE_FUTURE_CROSS_CARRIER_EVIDENCE_REVIEW_STEP",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_ALREADY_CREATED_CROSS_CARRIER_EVIDENCE",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_ALREADY_CREATED_PORTABLE_VERIFICATION_CLOSURE",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_BOUNDARY_AS_CROSS_CARRIER_EVIDENCE",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_BOUNDARY_AS_PORTABLE_VERIFICATION_CLOSURE",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_ZERO_EXIT_CODE_AS_CROSS_CARRIER_EVIDENCE",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_STRING_ZERO_AS_CROSS_CARRIER_EVIDENCE",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_STRING_ZERO_AS_DOCTRINE",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_RETURNED_CAPTURE_AS_CROSS_CARRIER_EVIDENCE",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_OK_AS_CROSS_CARRIER_EVIDENCE",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_RAN_7_TESTS_AS_CROSS_CARRIER_EVIDENCE",
    "CROSS_CARRIER_EVIDENCE_BOUNDARY_REDACTED_OFFICIAL_ENUM_SCOPE_STRINGS",
    "PREDECESSOR_EXTERNAL_RESULT_V1_FAILURE_MISSING_OR_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
    "SECOND_CARRIER_EXTERNAL_RESULT_BASIS_MISSING",
    "SECOND_CARRIER_EXTERNAL_RESULT_NOT_RECORDED",
    "SECOND_CARRIER_EXTERNAL_RESULT_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_EXTERNAL_RESULT_ALREADY_CREATED_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXTERNAL_RESULT_ALREADY_CREATED_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_EXTERNAL_RESULT_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_EXTERNAL_RESULT_AS_PORTABLE_VERIFICATION_CLOSURE",
    "SECOND_CARRIER_EXTERNAL_RESULT_TREATED_STRING_ZERO_AS_DOCTRINE",
    "SECOND_CARRIER_EXTERNAL_RESULT_BOUNDARY_BASIS_MISSING",
    "SECOND_CARRIER_VERIFICATION_BASIS_MISSING",
    "SECOND_CARRIER_VERIFICATION_NOT_RECORDED",
    "SECOND_CARRIER_VERIFICATION_FAILED_CHECKS_PRESENT",
    "RETURNED_CAPTURE_INTAKE_BASIS_MISSING",
    "RETURNED_CAPTURE_INTAKE_NOT_PRESERVED",
    "RETURNED_CAPTURE_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "ZERO_EXIT_CODE_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "STRING_ZERO_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "STRING_ZERO_REPRESENTATION_TURNED_INTO_DOCTRINE",
    "OK_OUTPUT_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "RAN_7_TESTS_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "PLACEHOLDER_CARRIER_FIELDS_REPAIRED",
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
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_CROSS_CARRIER_EVIDENCE",
    "ARTIFACTS_MUTATED",
    "RETURNED_CAPTURE_MATERIAL_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_CROSS_CARRIER_EVIDENCE_SCOPE",
)


def build_request(**overrides: Any) -> dict[str, Any]:
    return resolver.build_declared_portable_source_body_verification_cross_carrier_evidence_request(
        **overrides
    )


def resolved(request: Any) -> dict[str, Any]:
    return resolver.resolve_portable_source_body_verification_cross_carrier_evidence(request)


def statement(result: dict[str, Any]) -> dict[str, Any]:
    return result.get("cross_carrier_evidence_statement", {})


def non_claims(result: dict[str, Any]) -> dict[str, Any]:
    return result.get("non_claims", {})


def checks(result: dict[str, Any]) -> list[dict[str, Any]]:
    return list(result.get("cross_carrier_evidence_checks", []))


def summary(result: dict[str, Any]) -> dict[str, Any]:
    return result.get("portable_source_body_verification_cross_carrier_evidence_summary", {})


def scope_values(result: dict[str, Any]) -> list[str]:
    scope = result.get("cross_carrier_evidence_scope", {})
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


def remove_non_claim(name: str) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request["declared_non_claims"].pop(name, None)

    return mutate


def set_nested(section: str, name: str, value: Any) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        target = request.setdefault(section, {})
        if not isinstance(target, dict):
            target = {}
            request[section] = target
        target[name] = value

    return mutate


def set_non_claim(name: str, value: Any = True) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request[name] = value
        request["declared_non_claims"][name] = value

    return mutate


class CrossCarrierEvidenceV2Test(unittest.TestCase):
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
            result.get("cross_carrier_evidence_non_meaning", {}),
        ):
            for key, value in section.items():
                self.assertIs(type(value), bool, key)
        scope = result.get("cross_carrier_evidence_scope", {})
        self.assertIs(type(scope.get("official_enum_scope_strings_not_redacted")), bool)
        for posture_key in POSTURE_KEYS:
            posture = result.get(posture_key, {})
            self.assertIs(type(posture.get("declared")), bool, posture_key)
            for generated_key in (
                "creates_portable_verification_closure",
                "creates_source_transfer",
                "creates_source_receipt",
                "creates_reception_authorization",
                "creates_source_authority_currentness_runtime_final_completion_or_follow_on",
            ):
                self.assertIs(type(posture.get(generated_key)), bool, posture_key)

    def assert_no_raw_or_hidden_sentinels(self, result: dict[str, Any]) -> None:
        body = serialized(result)
        for sentinel in RAW_SENTINELS:
            self.assertNotIn(sentinel, body)
        for hostile in HOSTILE_VALUES:
            self.assertNotIn(hostile, body)

    def assert_official_scope_strings_preserved(self, result: dict[str, Any]) -> None:
        scope = result.get("cross_carrier_evidence_scope", {})
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
        forbidden_false = (
            "portable_verification_closure_created",
            "source_transfer_occurred",
            "source_receipt_occurred",
            "reception_authorization_created",
            "cross_carrier_evidence_treated_as_portable_verification_closure",
            "cross_carrier_evidence_treated_as_source_transfer",
            "cross_carrier_evidence_treated_as_source_receipt",
            "cross_carrier_evidence_treated_as_reception_authorization",
            "cross_carrier_evidence_treated_as_source",
            "cross_carrier_evidence_treated_as_authority",
            "cross_carrier_evidence_treated_as_currentness",
            "cross_carrier_evidence_treated_as_final_completion",
            "cross_carrier_evidence_treated_as_runtime",
            "cross_carrier_evidence_treated_as_continuation",
            "cross_carrier_evidence_treated_as_reusable_permission",
            "cross_carrier_evidence_treated_as_follow_on_work",
            "zero_exit_code_treated_as_cross_carrier_evidence_standalone",
            "string_zero_treated_as_cross_carrier_evidence_standalone",
            "string_zero_representation_turned_into_doctrine",
            "ok_output_treated_as_cross_carrier_evidence_standalone",
            "ran_7_tests_treated_as_cross_carrier_evidence_standalone",
            "returned_capture_treated_as_cross_carrier_evidence_standalone",
            "receiving_carrier_treated_as_authority",
            "artifact_existence_treated_as_cross_carrier_evidence_authority",
            "artifact_path_treated_as_currentness",
            "repo_local_availability_treated_as_cross_carrier_evidence_authority",
            "hidden_repo_state_used_as_cross_carrier_evidence_content",
            "hidden_repo_state_used_as_cross_carrier_evidence_authority",
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
            "returned_capture_material_mutated",
            "consumed_request_reopened",
            "authorization_token_reused",
            "predecessor_external_result_v1_repaired",
            "predecessor_external_result_v1_hidden",
            "predecessor_external_result_v1_claimed_passed",
            "v1_packet_emission_repaired",
            "v1_packet_emission_hidden",
            "v1_packet_emission_claimed_passed",
            "first_success_boundary_test_repaired",
            "first_success_boundary_test_hidden",
            "first_success_boundary_test_claimed_passed",
            "first_result_boundary_resolver_repaired",
            "first_result_boundary_resolver_hidden",
            "first_result_boundary_resolver_claimed_passed",
        )
        for key in forbidden_false:
            self.assertIs(claims.get(key), False, key)

    def assert_blocked_result(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertIsInstance(result.get("block"), dict)
        self.assertIsNotNone(result["block"].get("block_code"))
        self.assert_public_block_codes(result)
        self.assert_no_forbidden_creation(result)
        self.assert_generated_booleans_are_bool(result)
        self.assert_official_scope_strings_preserved(result)

    def assert_path_blocks_or_raises(self, path: Path) -> None:
        try:
            result = resolver.resolve_portable_source_body_verification_cross_carrier_evidence_from_path(
                path
            )
        except resolver.PortableSourceBodyVerificationCrossCarrierEvidenceError:
            return
        self.assert_blocked_result(result)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_portable_source_body_verification_cross_carrier_evidence",
            "resolve_portable_source_body_verification_cross_carrier_evidence_from_path",
            "write_portable_source_body_verification_cross_carrier_evidence_result",
            "build_portable_source_body_verification_cross_carrier_evidence_summary",
            "build_declared_portable_source_body_verification_cross_carrier_evidence_request",
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
            "SUPPORTED_CROSS_CARRIER_EVIDENCE_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_portable_source_body_verification_cross_carrier_evidence_v2",
        )
        self.assertEqual(
            resolver.SUPPORTED_CROSS_CARRIER_EVIDENCE_SCOPE,
            resolver.SUPPORTED_SCOPE_VALUES,
        )
        self.assertTrue(
            str(resolver.OUTPUT_ROOT)
            .replace("\\", "/")
            .endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_portable_source_body_verification_"
                "cross_carrier_evidence"
            )
        )
        for official in OFFICIAL_SCOPE_VALUES:
            self.assertIn(official, resolver.SUPPORTED_CROSS_CARRIER_EVIDENCE_SCOPE)
        for code in REPRESENTATIVE_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_successful_recorded_result_from_no_argument_builder(self) -> None:
        request = build_request()
        request_snapshot = copy.deepcopy(request)
        result = resolved(request)
        compact = resolver.build_portable_source_body_verification_cross_carrier_evidence_summary(
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
            "resolve_portable_source_body_verification_cross_carrier_evidence_v2",
        )
        self.assertEqual(compact["request_id"], request["cross_carrier_evidence_request_id"])
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
        self.assert_no_raw_or_hidden_sentinels(result)

    def test_official_enum_strings_are_preserved_without_redaction_placeholders(self) -> None:
        result = resolved(build_request())
        emitted_scope = scope_values(result)
        for official in OFFICIAL_SCOPE_VALUES:
            self.assertIn(official, emitted_scope)
        for value in emitted_scope:
            self.assertNotIn(value, REDACTION_PLACEHOLDERS)
        self.assert_official_scope_strings_preserved(result)

        request = build_request(cross_carrier_evidence_scope=list(SUPPORTED_SCOPE))
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
            "capture_body": HOSTILE_VALUES[11],
            "cross_carrier_evidence_body": HOSTILE_VALUES[12],
            "portable_verification_closure_body": HOSTILE_VALUES[13],
            "source_body": HOSTILE_VALUES[14],
            "authority_body": HOSTILE_VALUES[15],
            "hidden_repo_state": "hidden-state:" + RAW_SENTINELS[2],
            "current_working_tree": HOSTILE_VALUES[16],
            "local_cache": HOSTILE_VALUES[17],
            "repo_local_only_dependency": HOSTILE_VALUES[18],
            "nested": {
                "items": [
                    RAW_SENTINELS[0],
                    {"deeper": RAW_SENTINELS[1]},
                    {"official_scope": "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED"},
                ]
            },
        }
        for section in (
            "selected_cross_carrier_evidence_boundary_basis",
            "selected_cross_carrier_evidence_boundary_terminal_summary_basis",
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

    def test_predecessor_missed_boundary_overreach_cases_block_with_v2_codes(self) -> None:
        cases = (
            (
                "direct string zero doctrine",
                set_field(
                    "selected_cross_carrier_evidence_boundary_treated_string_zero_as_doctrine",
                    True,
                ),
                "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_STRING_ZERO_AS_DOCTRINE",
            ),
            (
                "nested string zero doctrine in boundary basis",
                set_nested(
                    "selected_cross_carrier_evidence_boundary_basis",
                    "treated_string_zero_as_doctrine",
                    True,
                ),
                "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_STRING_ZERO_AS_DOCTRINE",
            ),
            (
                "nested string zero doctrine in terminal summary basis",
                set_nested(
                    "selected_cross_carrier_evidence_boundary_terminal_summary_basis",
                    "string_zero_representation_turned_into_doctrine",
                    True,
                ),
                "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_STRING_ZERO_AS_DOCTRINE",
            ),
            (
                "direct returned capture evidence",
                set_field(
                    "selected_cross_carrier_evidence_boundary_treated_returned_capture_as_cross_carrier_evidence",
                    True,
                ),
                "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_RETURNED_CAPTURE_AS_CROSS_CARRIER_EVIDENCE",
            ),
            (
                "direct returned capture proof",
                set_field(
                    "selected_cross_carrier_evidence_boundary_treated_returned_capture_as_cross_carrier_proof",
                    True,
                ),
                "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_RETURNED_CAPTURE_AS_CROSS_CARRIER_EVIDENCE",
            ),
            (
                "nested returned capture evidence",
                set_nested(
                    "selected_cross_carrier_evidence_boundary_basis",
                    "returned_capture_treated_as_cross_carrier_evidence",
                    True,
                ),
                "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_RETURNED_CAPTURE_AS_CROSS_CARRIER_EVIDENCE",
            ),
            (
                "nested returned capture proof",
                set_nested(
                    "selected_cross_carrier_evidence_boundary_terminal_summary_basis",
                    "treated_returned_capture_as_cross_carrier_proof",
                    True,
                ),
                "CROSS_CARRIER_EVIDENCE_BOUNDARY_TREATED_RETURNED_CAPTURE_AS_CROSS_CARRIER_EVIDENCE",
            ),
        )
        for label, mutate, expected_code in cases:
            with self.subTest(label=label):
                request = build_request()
                mutate(request)
                result = resolved(request)
                self.assert_blocked_result(result)
                self.assertEqual(result["block"]["block_code"], expected_code)

    def test_representative_blocking_behavior(self) -> None:
        malformed_cases: tuple[Any, ...] = (None, ["not", "a", "mapping"])
        for bad_request in malformed_cases:
            with self.subTest(kind="malformed request", request=repr(bad_request)):
                self.assert_blocked_result(resolved(bad_request))

        cases: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
            ("explicit block intent", set_field("cross_carrier_evidence_intent", "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_CROSS_CARRIER_EVIDENCE")),
            ("undeclared question", set_field("cross_carrier_evidence_question", "")),
            ("unsupported intent", set_field("cross_carrier_evidence_intent", "UNSUPPORTED_INTENT")),
            ("unsupported scope", set_field("cross_carrier_evidence_scope", ["UNSUPPORTED_CROSS_CARRIER_EVIDENCE_SCOPE_VALUE"])),
            ("missing cross-carrier evidence boundary basis", clear_field("selected_cross_carrier_evidence_boundary_basis")),
            ("cross-carrier evidence boundary not recorded", set_field("selected_cross_carrier_evidence_boundary_result_outcome", "NOT_RECORDED")),
            ("cross-carrier evidence boundary failed checks", set_field("selected_cross_carrier_evidence_boundary_failed_check_count", 1)),
            ("cross-carrier evidence boundary version wrong", set_field("selected_cross_carrier_evidence_boundary_result_version", "9.9.9")),
            ("cross-carrier evidence boundary did not declare future review", set_field("selected_cross_carrier_evidence_boundary_declared_future_cross_carrier_evidence_review_step", False)),
            ("cross-carrier evidence boundary created evidence", set_field("selected_cross_carrier_evidence_boundary_already_created_cross_carrier_evidence", True)),
            ("cross-carrier evidence boundary created closure", set_field("selected_cross_carrier_evidence_boundary_already_created_portable_verification_closure", True)),
            ("cross-carrier evidence boundary treated boundary as evidence", set_field("selected_cross_carrier_evidence_boundary_treated_boundary_as_cross_carrier_evidence", True)),
            ("cross-carrier evidence boundary treated boundary as closure", set_field("selected_cross_carrier_evidence_boundary_treated_boundary_as_portable_verification_closure", True)),
            ("cross-carrier evidence boundary treated zero exit code as evidence", set_field("selected_cross_carrier_evidence_boundary_zero_exit_code_not_cross_carrier_evidence", False)),
            ("cross-carrier evidence boundary treated string zero as evidence", set_field("selected_cross_carrier_evidence_boundary_string_zero_not_cross_carrier_evidence", False)),
            ("cross-carrier evidence boundary treated string zero as doctrine", set_field("selected_cross_carrier_evidence_boundary_treated_string_zero_as_doctrine", True)),
            ("cross-carrier evidence boundary treated returned capture as evidence", set_field("selected_cross_carrier_evidence_boundary_treated_returned_capture_as_cross_carrier_evidence", True)),
            ("cross-carrier evidence boundary treated returned capture as proof", set_field("selected_cross_carrier_evidence_boundary_treated_returned_capture_as_cross_carrier_proof", True)),
            ("cross-carrier evidence boundary treated OK as evidence", set_field("selected_cross_carrier_evidence_boundary_ok_not_cross_carrier_evidence", False)),
            ("cross-carrier evidence boundary treated Ran 7 tests as evidence", set_field("selected_cross_carrier_evidence_boundary_ran_7_tests_not_cross_carrier_evidence", False)),
            ("cross-carrier evidence boundary redacted official strings", set_field("selected_cross_carrier_evidence_boundary_official_enum_scope_strings_redacted", True)),
            ("predecessor external-result v1 failure missing", set_field("selected_cross_carrier_evidence_boundary_predecessor_external_result_v1_failure_preserved", False)),
            ("predecessor external-result v1 repaired", set_field("predecessor_external_result_v1_repaired", True)),
            ("second-carrier external result basis missing", clear_field("selected_second_carrier_external_result_basis")),
            ("second-carrier external result not recorded", set_field("selected_second_carrier_external_result_result_outcome", "NOT_RECORDED")),
            ("second-carrier external result failed checks", set_field("selected_second_carrier_external_result_failed_check_count", 1)),
            ("second-carrier external result created evidence", set_field("selected_second_carrier_external_result_already_created_cross_carrier_evidence", True)),
            ("second-carrier external result created closure", set_field("selected_second_carrier_external_result_already_created_portable_verification_closure", True)),
            ("second-carrier external result treated external result as evidence", set_field("selected_second_carrier_external_result_treated_external_result_as_cross_carrier_evidence", True)),
            ("second-carrier external result treated external result as closure", set_field("selected_second_carrier_external_result_treated_external_result_as_portable_verification_closure", True)),
            ("second-carrier external result treated string zero as doctrine", set_field("selected_second_carrier_external_result_treated_string_zero_as_doctrine", True)),
            ("second-carrier external-result boundary basis missing", clear_field("selected_second_carrier_external_result_boundary_basis")),
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
            ("returned capture treated as cross-carrier evidence", set_field("returned_capture_treated_as_cross_carrier_evidence", True)),
            ("zero exit code treated as evidence", set_field("zero_exit_code_treated_as_cross_carrier_evidence", True)),
            ("string zero treated as evidence", set_field("string_zero_treated_as_cross_carrier_evidence", True)),
            ("OK output treated as evidence", set_field("ok_output_treated_as_cross_carrier_evidence", True)),
            ("Ran 7 tests treated as evidence", set_field("ran_7_tests_treated_as_cross_carrier_evidence", True)),
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
            ("cross-carrier evidence treated as closure", set_non_claim("cross_carrier_evidence_treated_as_portable_verification_closure")),
            ("cross-carrier evidence treated as source transfer", set_non_claim("cross_carrier_evidence_treated_as_source_transfer")),
            ("cross-carrier evidence treated as source receipt", set_non_claim("cross_carrier_evidence_treated_as_source_receipt")),
            ("cross-carrier evidence treated as reception authorization", set_non_claim("cross_carrier_evidence_treated_as_reception_authorization")),
            ("cross-carrier evidence treated as source", set_non_claim("cross_carrier_evidence_treated_as_source")),
            ("cross-carrier evidence treated as authority", set_non_claim("cross_carrier_evidence_treated_as_authority")),
            ("cross-carrier evidence treated as currentness", set_non_claim("cross_carrier_evidence_treated_as_currentness")),
            ("cross-carrier evidence treated as final completion", set_non_claim("cross_carrier_evidence_treated_as_final_completion")),
            ("cross-carrier evidence treated as runtime", set_non_claim("cross_carrier_evidence_treated_as_runtime")),
            ("cross-carrier evidence treated as continuation", set_non_claim("cross_carrier_evidence_treated_as_continuation")),
            ("cross-carrier evidence treated as reusable permission", set_non_claim("cross_carrier_evidence_treated_as_reusable_permission")),
            ("cross-carrier evidence treated as follow-on work", set_non_claim("cross_carrier_evidence_treated_as_follow_on_work")),
            ("portable verification closure created", set_non_claim("portable_verification_closure_created")),
            ("source transfer occurred", set_non_claim("source_transfer_occurred")),
            ("source receipt occurred", set_non_claim("source_receipt_occurred")),
            ("reception authorization created", set_non_claim("reception_authorization_created")),
            ("source created", set_non_claim("source_created")),
            ("authority created", set_non_claim("authority_created")),
            ("currentness created", set_non_claim("currentness_created")),
            ("final completion claimed", set_non_claim("final_completion_claimed")),
            ("runtime hosting created", set_non_claim("runtime_hosting_created")),
            ("deployment created", set_non_claim("deployment_created")),
            ("public release created", set_non_claim("public_release_created")),
            ("operation permission created", set_non_claim("operation_permission_created")),
            ("continuation authorized", set_non_claim("continuation_authorized")),
            ("reusable permission created", set_non_claim("reusable_permission_created")),
            ("follow-on work authorized", set_non_claim("follow_on_work_authorized")),
            ("receiving carrier treated as authority", set_non_claim("receiving_carrier_treated_as_authority")),
            ("artifact existence treated as authority", set_non_claim("artifact_existence_treated_as_cross_carrier_evidence_authority")),
            ("artifact path treated as currentness", set_non_claim("artifact_path_treated_as_currentness")),
            ("repo-local availability treated as authority", set_non_claim("repo_local_availability_treated_as_cross_carrier_evidence_authority")),
            ("hidden repo state used as evidence content", set_non_claim("hidden_repo_state_used_as_cross_carrier_evidence_content")),
            ("hidden repo state used as authority", set_non_claim("hidden_repo_state_used_as_cross_carrier_evidence_authority")),
            ("selected basis not reference-shaped", set_field("reference_shaped_input_posture", False)),
            ("raw full prior artifact body returned", set_non_claim("raw_full_prior_artifact_body_returned")),
            ("predecessor failure evidence repaired", set_field("v1_packet_emission_repaired", True)),
            ("first success-boundary hidden", set_field("first_success_boundary_test_hidden", True)),
            ("first result-boundary claimed passed", set_field("first_result_boundary_resolver_claimed_passed", True)),
            ("command report lineage current report artifact", set_field("command_report_lineage_treated_as_current_report_artifact", True)),
            ("command report lineage source", set_field("command_report_lineage_treated_as_source", True)),
            ("command report lineage authority", set_field("command_report_lineage_treated_as_authority", True)),
            ("command report lineage currentness", set_field("command_report_lineage_treated_as_currentness", True)),
            ("consumed request reopened", set_non_claim("consumed_request_reopened")),
            ("authorization token reused", set_non_claim("authorization_token_reused")),
            ("full prior artifact body emitted outside bounded posture", set_field("full_prior_artifact_body_emitted_outside_bounded_cross_carrier_evidence", True)),
            ("string zero representation turned into doctrine", set_field("string_zero_representation_turned_into_doctrine", True)),
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

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request_path = tmp_path / "valid_request.json"
            request_path.write_text(json.dumps(build_request(), indent=2), encoding="utf-8")
            result = resolver.resolve_portable_source_body_verification_cross_carrier_evidence_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], RECORDED)
            self.assertEqual(summary(result)["result_version"], "0.1.0")
            self.assertEqual(
                summary(result)["resolver_module"],
                "resolve_portable_source_body_verification_cross_carrier_evidence_v2",
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
                / "integrity_host_v0_min_coexistence_portable_source_body_verification_cross_carrier_evidence"
            )
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_portable_source_body_verification_cross_carrier_evidence_result(
                    result
                )
                second_path = resolver.write_portable_source_body_verification_cross_carrier_evidence_result(
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
                "integrity_host_v0_min_coexistence_portable_source_body_verification_cross_carrier_evidence_boundary",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_external_result",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_verification",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_success",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_result",
                "portable_verification_closure",
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
        request["cross_carrier_evidence_scope"] = {
            "scope_values": list(SUPPORTED_SCOPE),
            "non_mutation_marker": True,
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

        self.assertIs(compact["predecessor_cross_carrier_evidence_resolver_failure_preserved"], True)
        self.assertIs(
            compact["predecessor_cross_carrier_evidence_resolver_not_repaired_hidden_or_claimed_passed"],
            True,
        )
        self.assertIs(predecessor["predecessor_cross_carrier_evidence_resolver_failure_preserved"], True)
        self.assertIs(predecessor["predecessor_cross_carrier_evidence_resolver_not_repaired"], True)
        self.assertIs(predecessor["predecessor_cross_carrier_evidence_resolver_not_hidden"], True)
        self.assertIs(predecessor["predecessor_cross_carrier_evidence_resolver_not_claimed_passed"], True)
        self.assertIs(statement(result)["predecessor_external_result_v1_failure_preserved"], True)
        self.assertIs(claims["predecessor_external_result_v1_repaired"], False)
        self.assertIs(claims["predecessor_external_result_v1_hidden"], False)
        self.assertIs(claims["predecessor_external_result_v1_claimed_passed"], False)
        self.assertIs(statement(result)["first_success_boundary_test_failure_preserved"], True)
        self.assertIs(claims["first_success_boundary_test_repaired"], False)
        self.assertIs(claims["first_success_boundary_test_hidden"], False)
        self.assertIs(claims["first_success_boundary_test_claimed_passed"], False)
        self.assertIs(compact["v1_packet_emission_predecessor_failure_preserved"], True)
        self.assertIs(claims["v1_packet_emission_repaired"], False)
        self.assertIs(claims["v1_packet_emission_hidden"], False)
        self.assertIs(claims["v1_packet_emission_claimed_passed"], False)
        self.assertIs(statement(result)["first_result_boundary_resolver_failure_preserved"], True)
        self.assertIs(claims["first_result_boundary_resolver_repaired"], False)
        self.assertIs(claims["first_result_boundary_resolver_hidden"], False)
        self.assertIs(claims["first_result_boundary_resolver_claimed_passed"], False)


if __name__ == "__main__":
    unittest.main()
