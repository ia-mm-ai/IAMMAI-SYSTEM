"""Executable checks for second-carrier output capture posture only.

This suite is downstream of recorded second-carrier output-capture-boundary
posture. It verifies that the resolver records one bounded second-carrier
output capture posture only: capture is not result, success, external result,
cross-carrier proof, source transfer, source receipt, reception authorization,
source, authority, currentness, runtime, final completion, continuation,
reusable permission, or follow-on work. Receiving carrier is not authority,
hidden repo state is excluded, repo-local availability is not capture
authority, selected basis stays reference-shaped, the consumed request token
remains closed, and authorization token reuse remains blocked.
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

import resolve_portable_source_body_verification_second_carrier_output_capture as resolver


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_SECOND_CARRIER_OUTPUT_CAPTURE_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
TRUE_RECORDED_FIELDS = tuple(resolver.ALLOWED_TRUE_RECORDED_FIELDS)
SELECTED_BASIS_KEYS = tuple(resolver.SELECTED_BASIS_KEYS)
POSTURE_KEYS = tuple(resolver.POSTURE_KEYS)

RAW_SENTINEL = "RAW_SECOND_CARRIER_OUTPUT_CAPTURE_BODY_MUST_NOT_RETURN"
HOSTILE_RAW_VALUE = "HOSTILE_SECOND_CARRIER_OUTPUT_CAPTURE_FULL_BODY_VALUE_MUST_NOT_RETURN"
REDACTION_STRINGS = {
    "[bounded-redacted-raw-or-hidden-state]",
    "[bounded-reference-redacted-raw-or-hidden-state]",
    "[bounded-reference-omitted-raw-or-hidden-state]",
}

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_second_carrier_output_capture_metadata",
    "declared_second_carrier_output_capture_question",
    "selected_second_carrier_output_capture_boundary_basis",
    "selected_second_carrier_output_capture_boundary_terminal_summary_basis",
    "selected_second_carrier_execution_output_basis",
    "selected_second_carrier_execution_output_terminal_summary_basis",
    "selected_second_carrier_execution_output_boundary_basis",
    "selected_second_carrier_execution_basis",
    "selected_second_carrier_execution_boundary_basis",
    "selected_second_carrier_receipt_basis",
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
    "second_carrier_output_capture_spec_only_posture",
    "one_bounded_second_carrier_output_capture_posture",
    "second_carrier_output_capture_boundary_basis_preserved_posture",
    "second_carrier_execution_output_basis_preserved_posture",
    "output_artifact_basis_preserved_posture",
    "capture_recorded_bounded_posture",
    "capture_artifact_recorded_or_bounded_posture",
    "capture_not_result_posture",
    "capture_not_success_posture",
    "capture_not_external_result_posture",
    "capture_not_cross_carrier_evidence_posture",
    "capture_not_source_transfer_posture",
    "capture_not_source_receipt_posture",
    "capture_not_reception_authorization_posture",
    "second_carrier_result_not_created_posture",
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
    "repo_local_availability_not_capture_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "second_carrier_output_capture_scope",
    "second_carrier_output_capture_checks",
    "second_carrier_output_capture_statement",
    "second_carrier_output_capture_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_second_carrier_output_capture_summary",
)

REPRESENTATIVE_BLOCK_CODES = (
    "SECOND_CARRIER_OUTPUT_CAPTURE_QUESTION_UNDECLARED",
    "SECOND_CARRIER_OUTPUT_CAPTURE_INTENT_UNSUPPORTED",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_BASIS_MISSING",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_NOT_RECORDED",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_VERSION_NOT_0_1_0",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_DID_NOT_DECLARE_FUTURE_CAPTURE_STEP",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_ALREADY_CREATED_CAPTURE",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_ALREADY_CREATED_CAPTURE_ARTIFACT",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_ALREADY_CREATED_SECOND_CARRIER_RESULT",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_ALREADY_CREATED_SECOND_CARRIER_SUCCESS",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_CREATED_EXTERNAL_RESULT",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_CREATED_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_USED_HIDDEN_REPO_STATE_AS_CAPTURE_AUTHORITY",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_REPO_LOCAL_AVAILABILITY_AS_CAPTURE_AUTHORITY",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_TREATED_RECEIVING_CARRIER_AS_AUTHORITY",
    "SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BASIS_MISSING",
    "SECOND_CARRIER_EXECUTION_OUTPUT_NOT_RECORDED",
    "SECOND_CARRIER_EXECUTION_OUTPUT_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_DID_NOT_RECORD_BOUNDED_OUTPUT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_OUTPUT_AS_CAPTURE",
    "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_RESULT",
    "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_SUCCESS",
    "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_SOURCE_TRANSFER",
    "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_SOURCE_RECEIPT",
    "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_RECEPTION_AUTHORIZATION",
    "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_SOURCE",
    "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_AUTHORITY",
    "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_CURRENTNESS",
    "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_FINAL_COMPLETION",
    "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_RUNTIME",
    "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_CONTINUATION",
    "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_REUSABLE_PERMISSION",
    "SECOND_CARRIER_OUTPUT_CAPTURE_TREATED_CAPTURE_AS_FOLLOW_ON_WORK",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_CAPTURE_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_CAPTURE_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_CAPTURE_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_CAPTURE_AUTHORITY",
    "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_CAPTURE",
    "ARTIFACTS_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_SECOND_CARRIER_OUTPUT_CAPTURE_SCOPE",
)

NON_MEANING_FALSE_KEYS = (
    "second_carrier_result_exists",
    "second_carrier_success_exists",
    "external_result_exists",
    "cross_carrier_evidence_exists",
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
    "capture_became_result",
    "capture_became_success",
    "capture_became_external_result",
    "capture_became_cross_carrier_proof",
    "capture_became_source_transfer_source_receipt_or_reception_authorization",
    "capture_became_source_authority_or_currentness",
    "capture_artifact_became_result_success_external_result_or_cross_carrier_evidence",
    "receiving_carrier_became_authority",
    "transferred_packet_became_source_authority_or_currentness",
    "artifact_existence_became_capture_authority",
    "artifact_path_became_currentness",
    "repo_local_availability_became_capture_authority",
    "hidden_repo_state_became_capture_authority",
    "v1_packet_emission_boundary_resolver_repaired_hidden_erased_or_claimed_passed",
)

HOSTILE_KEYS = (
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_result_body",
    "raw_output_body",
    "execution_body",
    "execution_artifact_body",
    "output_body",
    "output_artifact_body",
    "capture_body",
    "capture_artifact_body",
    "captured_second_carrier_output_body",
    "second_carrier_result_body",
    "second_carrier_success_body",
    "external_result_body",
    "cross_carrier_evidence_body",
    "packet_body",
    "source_body",
    "authority_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
    "carrier_possession",
    "copy_presence",
    "receiving_carrier",
    "receipt_artifact_presence",
    "execution_artifact_presence",
    "output_artifact_presence",
    "capture_artifact_presence",
    "capture_path_existence",
    "unlisted_file_dependency",
)

PATH_FORBIDDEN_ROOT_FRAGMENTS = (
    "second_carrier_output_capture_boundary",
    "second_carrier_result",
    "second_carrier_success",
    "external_result",
    "cross_carrier",
    "runtime",
    "deployment",
    "public_release",
)


def _json_text(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=True)


def _valid_request(**overrides: Any) -> dict[str, Any]:
    request = resolver.build_declared_portable_source_body_verification_second_carrier_output_capture_request(
        **overrides
    )
    outcome_by_basis = {
        "selected_second_carrier_execution_output_boundary_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_RECORDED"
        ),
        "selected_second_carrier_execution_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_RECORDED"
        ),
        "selected_second_carrier_execution_boundary_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_BOUNDARY_RECORDED"
        ),
        "selected_second_carrier_receipt_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RECEIPT_RECORDED"
        ),
        "selected_packet_transfer_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_TRANSFER_RECORDED"
        ),
        "selected_packet_emission_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_RECORDED"
        ),
        "selected_packet_emission_boundary_v2_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_BOUNDARY_RECORDED"
        ),
        "selected_packet_artifact_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_ARTIFACT_RECORDED"
        ),
        "selected_command_success_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_RECORDED"
        ),
        "selected_command_result_v2_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_RECORDED"
        ),
        "selected_output_capture_v2_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_RECORDED"
        ),
        "selected_command_output_report_artifact_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_REPORT_ARTIFACT_RECORDED"
        ),
        "selected_command_execution_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_RECORDED"
        ),
    }
    for key, outcome in outcome_by_basis.items():
        request[key].update(
            {
                "outcome": outcome,
                "result_version": "0.1.0",
                "failed_check_count": 0,
                "basis_declared": True,
                "basis_reference_shape_preserved": True,
            }
        )
    request["selected_packet_emission_boundary_v1_predecessor_failure_basis"].update(
        {
            "v1_failure_visible": True,
            "v1_repaired": False,
            "v1_hidden": False,
            "v1_claimed_passed": False,
        }
    )
    request["selected_command_report_lineage_basis"].update(
        {
            "lineage_only": True,
            "command_report_lineage_treated_as_current_report_artifact": False,
            "command_report_lineage_treated_as_source": False,
            "command_report_lineage_treated_as_authority": False,
            "command_report_lineage_treated_as_currentness": False,
        }
    )
    request["declared_non_claims"] = {
        key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS
    }
    request.update(overrides)
    return request


def _resolve(request: dict[str, Any]) -> dict[str, Any]:
    return resolver.resolve_portable_source_body_verification_second_carrier_output_capture(
        declared_second_carrier_output_capture_request=request
    )


def _remove_boundary_basis(request: dict[str, Any]) -> None:
    request["selected_second_carrier_output_capture_boundary_basis"] = {}
    for key in (
        "selected_second_carrier_output_capture_boundary_result_path",
        "selected_second_carrier_output_capture_boundary_result_id",
        "selected_second_carrier_output_capture_boundary_result_outcome",
        "selected_second_carrier_output_capture_boundary_result_version",
    ):
        request.pop(key, None)


def _remove_execution_output_basis(request: dict[str, Any]) -> None:
    request["selected_second_carrier_execution_output_basis"] = {}
    for key in (
        "selected_second_carrier_execution_output_result_path",
        "selected_second_carrier_execution_output_result_id",
        "selected_second_carrier_execution_output_result_outcome",
    ):
        request.pop(key, None)


def _set_request_value(key: str, value: Any) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request[key] = value

    return mutate


def _remove_non_claim(key: str) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request["declared_non_claims"].pop(key, None)

    return mutate


class SecondCarrierOutputCaptureResolverTests(unittest.TestCase):
    def assert_public_block_codes(self, result: dict[str, Any]) -> None:
        block = result.get("block")
        if isinstance(block, dict) and block.get("block_code") is not None:
            self.assertIn(block["block_code"], resolver.BLOCK_CODES)
        checks = result.get("second_carrier_output_capture_checks", [])
        self.assertIsInstance(checks, list)
        for check in checks:
            self.assertIsInstance(check, dict)
            for code_key in ("block_code", "failure_code"):
                code = check.get(code_key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_generated_booleans_are_bool(self, result: dict[str, Any]) -> None:
        for section_name in (
            "second_carrier_output_capture_statement",
            "non_claims",
            "second_carrier_output_capture_non_meaning",
        ):
            section = result.get(section_name)
            self.assertIsInstance(section, dict)
            for key, value in section.items():
                with self.subTest(section=section_name, key=key):
                    self.assertIsInstance(value, bool)
                    self.assertNotIn(value, REDACTION_STRINGS)

    def assert_no_raw_sentinels(self, result: dict[str, Any]) -> None:
        serialized = _json_text(result)
        self.assertNotIn(RAW_SENTINEL, serialized)
        self.assertNotIn(HOSTILE_RAW_VALUE, serialized)

    def assert_no_later_work_created(self, result: dict[str, Any]) -> None:
        non_claims = result.get("non_claims", {})
        self.assertIsInstance(non_claims, dict)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(non_claim=key):
                self.assertIn(key, non_claims)
                self.assertIs(non_claims[key], False)
        statement = result.get("second_carrier_output_capture_statement", {})
        self.assertIsInstance(statement, dict)
        self.assertIs(statement.get("artifacts_mutated"), False)
        self.assertIs(statement.get("authorization_token_reused"), False)
        self.assertIs(statement.get("consumed_request_reopened"), False)
        self.assertIs(statement.get("v1_repaired"), False)
        self.assertIs(statement.get("v1_hidden"), False)
        self.assertIs(statement.get("v1_claimed_passed"), False)

    def assert_blocked(self, result: dict[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), BLOCKED)
        self.assertIsInstance(result.get("block"), dict)
        self.assertIsNotNone(result["block"].get("block_code"))
        self.assertIn(result["block"]["block_code"], resolver.BLOCK_CODES)
        self.assert_public_block_codes(result)
        self.assert_no_later_work_created(result)
        self.assert_generated_booleans_are_bool(result)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_portable_source_body_verification_second_carrier_output_capture",
            "resolve_portable_source_body_verification_second_carrier_output_capture_from_path",
            "write_portable_source_body_verification_second_carrier_output_capture_result",
            "build_portable_source_body_verification_second_carrier_output_capture_summary",
            "build_declared_portable_source_body_verification_second_carrier_output_capture_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "RESULT_VERSION",
            "OUTPUT_ROOT",
            "SUPPORTED_SECOND_CARRIER_OUTPUT_CAPTURE_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name))

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_output_capture"
            )
        )
        for code in REPRESENTATIVE_BLOCK_CODES:
            with self.subTest(block_code=code):
                self.assertIn(code, resolver.BLOCK_CODES)

    def test_successful_second_carrier_output_capture_recorded_result(self) -> None:
        request = _valid_request()
        original = copy.deepcopy(request)
        result = _resolve(request)

        self.assertEqual(request, original)
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertIsNone(result["block"].get("block_code"))
        self.assertEqual(
            result["portable_source_body_verification_second_carrier_output_capture_metadata"][
                "failed_check_count"
            ],
            0,
        )
        for section in TOP_LEVEL_SECTIONS:
            with self.subTest(section=section):
                self.assertIn(section, result)

        metadata = result[
            "portable_source_body_verification_second_carrier_output_capture_metadata"
        ]
        self.assertEqual(
            metadata[
                "portable_source_body_verification_second_carrier_output_capture_result_version"
            ],
            "0.1.0",
        )
        self.assertEqual(metadata["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertEqual(
            metadata["second_carrier_output_capture_request_id"],
            request["second_carrier_output_capture_request_id"],
        )

        statement = result["second_carrier_output_capture_statement"]
        for key in TRUE_RECORDED_FIELDS:
            with self.subTest(true_statement=key):
                self.assertIs(statement[key], True)
                self.assertIsInstance(statement[key], bool)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(false_non_claim=key):
                self.assertIs(result["non_claims"][key], False)
                self.assertIs(statement[key], False)

        non_meaning = result["second_carrier_output_capture_non_meaning"]
        for key in NON_MEANING_FALSE_KEYS:
            with self.subTest(non_meaning=key):
                self.assertIn(key, non_meaning)
                self.assertIs(non_meaning[key], False)

        self.assert_public_block_codes(result)
        self.assert_generated_booleans_are_bool(result)
        self.assert_no_raw_sentinels(result)

    def test_summary_helper_preserves_capture_only_posture(self) -> None:
        result = _resolve(_valid_request())
        summary = resolver.build_portable_source_body_verification_second_carrier_output_capture_summary(
            result
        )
        statement = result["second_carrier_output_capture_statement"]

        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(
            summary["request_id"],
            result["portable_source_body_verification_second_carrier_output_capture_metadata"][
                "second_carrier_output_capture_request_id"
            ],
        )
        self.assertEqual(
            summary["question"],
            result["declared_second_carrier_output_capture_question"]["question"],
        )
        self.assertEqual(
            summary["intent"],
            result["declared_second_carrier_output_capture_question"]["intent"],
        )
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertGreater(summary["passed_check_count"], 0)
        for key in TRUE_RECORDED_FIELDS:
            with self.subTest(summary_true=key):
                self.assertEqual(summary[key], statement[key])
                self.assertIsInstance(summary[key], bool)

        self.assertEqual(
            summary["selected_second_carrier_output_capture_boundary_outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_OUTPUT_CAPTURE_BOUNDARY_RECORDED",
        )
        self.assertEqual(
            summary["selected_second_carrier_output_capture_boundary_result_version"],
            "0.1.0",
        )
        self.assertEqual(
            summary["selected_second_carrier_output_capture_boundary_failed_check_count"],
            0,
        )
        self.assertIs(summary["no_result_success_external_result_or_cross_carrier_evidence"], True)
        self.assertIs(summary["no_source_authority_currentness_final_completion_runtime"], True)
        self.assertIs(summary["no_deployment_public_release_or_follow_on"], True)
        self.assertIs(summary["v1_predecessor_failure_preserved"], True)
        self.assertIs(summary["v1_not_repaired_hidden_or_claimed_passed"], True)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(summary_non_claim=key):
                self.assertIs(summary["key_non_claims"][key], False)

    def test_representative_blocking_behavior(self) -> None:
        simple_cases: list[tuple[str, Callable[[dict[str, Any]], None]]] = [
            ("explicit block intent", _set_request_value("second_carrier_output_capture_intent", resolver.INTENT_BLOCK)),
            ("unsupported intent", _set_request_value("second_carrier_output_capture_intent", "UNSUPPORTED")),
            ("unsupported scope", _set_request_value("second_carrier_output_capture_scope", ["UNSUPPORTED_SCOPE"])),
            ("missing boundary basis", _remove_boundary_basis),
            (
                "boundary not recorded",
                _set_request_value("selected_second_carrier_output_capture_boundary_result_outcome", "NOT_RECORDED"),
            ),
            (
                "boundary failed checks",
                _set_request_value("selected_second_carrier_output_capture_boundary_failed_check_count", 1),
            ),
            (
                "boundary version wrong",
                _set_request_value("selected_second_carrier_output_capture_boundary_result_version", "9.9.9"),
            ),
            (
                "boundary missing future step",
                _set_request_value("selected_second_carrier_output_capture_boundary_declared_future_capture_step", False),
            ),
            (
                "boundary already created capture",
                _set_request_value("selected_second_carrier_output_capture_boundary_already_created_capture", True),
            ),
            (
                "boundary already created capture artifact",
                _set_request_value(
                    "selected_second_carrier_output_capture_boundary_already_created_capture_artifact",
                    True,
                ),
            ),
            (
                "boundary already created result",
                _set_request_value(
                    "selected_second_carrier_output_capture_boundary_already_created_second_carrier_result",
                    True,
                ),
            ),
            (
                "boundary already created success",
                _set_request_value(
                    "selected_second_carrier_output_capture_boundary_already_created_second_carrier_success",
                    True,
                ),
            ),
            (
                "boundary created external result",
                _set_request_value("selected_second_carrier_output_capture_boundary_created_external_result", True),
            ),
            (
                "boundary created cross-carrier evidence",
                _set_request_value(
                    "selected_second_carrier_output_capture_boundary_created_cross_carrier_evidence",
                    True,
                ),
            ),
            (
                "boundary used hidden repo state as capture authority",
                _set_request_value(
                    "selected_second_carrier_output_capture_boundary_used_hidden_repo_state_as_capture_authority",
                    True,
                ),
            ),
            (
                "boundary treated repo-local availability as capture authority",
                _set_request_value(
                    "selected_second_carrier_output_capture_boundary_treated_repo_local_availability_as_capture_authority",
                    True,
                ),
            ),
            (
                "boundary treated receiving carrier as authority",
                _set_request_value(
                    "selected_second_carrier_output_capture_boundary_treated_receiving_carrier_as_authority",
                    True,
                ),
            ),
            (
                "boundary returned raw full prior artifact body",
                _set_request_value(
                    "selected_second_carrier_output_capture_boundary_raw_full_prior_artifact_body_returned",
                    True,
                ),
            ),
            ("execution output basis missing", _remove_execution_output_basis),
            (
                "execution output not recorded",
                _set_request_value("selected_second_carrier_execution_output_result_outcome", "NOT_RECORDED"),
            ),
            (
                "execution output failed checks",
                _set_request_value("selected_second_carrier_execution_output_failed_check_count", 1),
            ),
            (
                "execution output did not record bounded output",
                _set_request_value("selected_second_carrier_execution_output_bounded_output_recorded", False),
            ),
            (
                "execution output treated output as capture",
                _set_request_value("selected_second_carrier_execution_output_treated_output_as_capture", True),
            ),
            ("selected basis not reference-shaped", _set_request_value("selected_basis_not_reference_shaped", True)),
            ("command report lineage current artifact", _set_request_value("command_report_lineage_treated_as_current_report_artifact", True)),
            ("command report lineage source", _set_request_value("command_report_lineage_treated_as_source", True)),
            ("command report lineage authority", _set_request_value("command_report_lineage_treated_as_authority", True)),
            ("command report lineage currentness", _set_request_value("command_report_lineage_treated_as_currentness", True)),
            (
                "full prior body emitted outside bounded capture",
                _set_request_value("full_prior_artifact_body_emitted_outside_bounded_capture", True),
            ),
            ("artifacts mutated", _set_request_value("artifacts_mutated", True)),
            ("required non-claim missing", _remove_non_claim("second_carrier_result_created")),
        ]

        for key in REQUIRED_FALSE_NON_CLAIMS:
            simple_cases.append((f"{key} flipped directly", _set_request_value(key, True)))

        malformed_results = [
            resolver.resolve_portable_source_body_verification_second_carrier_output_capture(None),
            resolver.resolve_portable_source_body_verification_second_carrier_output_capture(
                ["not", "a", "mapping"]  # type: ignore[arg-type]
            ),
        ]
        for result in malformed_results:
            self.assert_blocked(result)

        for name, mutate in simple_cases:
            with self.subTest(block_case=name):
                request = _valid_request()
                mutate(request)
                result = _resolve(request)
                self.assert_blocked(result)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            request_path = temp_root / "request.json"
            request_path.write_text(json.dumps(_valid_request()), encoding="utf-8")

            result = resolver.resolve_portable_source_body_verification_second_carrier_output_capture_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], RECORDED)
            metadata = result[
                "portable_source_body_verification_second_carrier_output_capture_metadata"
            ]
            self.assertEqual(
                metadata[
                    "portable_source_body_verification_second_carrier_output_capture_result_version"
                ],
                "0.1.0",
            )
            self.assertEqual(metadata["resolver_module"], resolver.RESOLVER_MODULE)

            array_path = temp_root / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolver.resolve_portable_source_body_verification_second_carrier_output_capture_from_path(
                array_path
            )
            self.assert_blocked(array_result)

            malformed_path = temp_root / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            with self.assertRaises(resolver.PortableSourceBodyVerificationSecondCarrierOutputCaptureError):
                resolver.resolve_portable_source_body_verification_second_carrier_output_capture_from_path(
                    malformed_path
                )
            with self.assertRaises(resolver.PortableSourceBodyVerificationSecondCarrierOutputCaptureError):
                resolver.resolve_portable_source_body_verification_second_carrier_output_capture_from_path(
                    temp_root / "missing.json"
                )

            patched_root = (
                temp_root
                / "artifacts"
                / "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_output_capture"
            )
            with patch.object(resolver, "OUTPUT_ROOT", patched_root):
                first_path = resolver.write_portable_source_body_verification_second_carrier_output_capture_result(
                    result
                )
                second_path = resolver.write_portable_source_body_verification_second_carrier_output_capture_result(
                    result
                )

            self.assertTrue(first_path.parent.exists())
            self.assertEqual(first_path.parent, patched_root)
            self.assertNotEqual(first_path, second_path)
            self.assertTrue(second_path.stem.endswith("_001"))
            parsed = json.loads(first_path.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], RECORDED)
            relative = first_path.relative_to(temp_root)
            self.assertEqual(
                str(relative.parent),
                "artifacts/"
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_output_capture",
            )
            for forbidden in PATH_FORBIDDEN_ROOT_FRAGMENTS:
                if forbidden == "second_carrier_output_capture":
                    continue
                self.assertNotIn(forbidden, first_path.parent.name)

    def test_resolver_does_not_mutate_request_or_selected_basis(self) -> None:
        request = _valid_request()
        before = copy.deepcopy(request)
        result = _resolve(request)

        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(request, before)
        for key in SELECTED_BASIS_KEYS:
            with self.subTest(selected_basis=key):
                self.assertEqual(request[key], before[key])
        for key in POSTURE_KEYS:
            with self.subTest(posture=key):
                self.assertEqual(request[key], before[key])
        self.assertEqual(
            request["second_carrier_output_capture_scope"],
            before["second_carrier_output_capture_scope"],
        )
        self.assertEqual(request["declared_non_claims"], before["declared_non_claims"])

    def test_raw_full_body_and_hidden_repo_state_containment(self) -> None:
        request = _valid_request()
        hostile_payload = {
            key: HOSTILE_RAW_VALUE for key in HOSTILE_KEYS
        }
        hostile_payload["nested"] = {
            "list": [RAW_SENTINEL, {"raw_full_body": HOSTILE_RAW_VALUE}],
        }
        for key in (
            "selected_second_carrier_output_capture_boundary_basis",
            "selected_second_carrier_execution_output_basis",
            "selected_second_carrier_execution_output_boundary_basis",
            "selected_second_carrier_execution_basis",
            "selected_second_carrier_receipt_basis",
            "selected_packet_transfer_basis",
            "selected_packet_emission_basis",
            "selected_packet_emission_boundary_v2_basis",
            "selected_packet_artifact_basis",
            "selected_command_success_basis",
            "selected_output_capture_v2_basis",
            "selected_command_report_lineage_basis",
            "selected_artifact_containment_basis",
        ):
            request[key]["hostile_reference_payload"] = copy.deepcopy(hostile_payload)

        before = copy.deepcopy(request)
        result = _resolve(request)

        self.assertEqual(request, before)
        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assert_public_block_codes(result)
        self.assert_no_raw_sentinels(result)
        self.assert_no_later_work_created(result)
        self.assert_generated_booleans_are_bool(result)
        non_claims = result["non_claims"]
        self.assertIs(non_claims["hidden_repo_state_used_as_capture_content"], False)
        self.assertIs(non_claims["hidden_repo_state_used_as_capture_authority"], False)
        self.assertIs(non_claims["repo_local_availability_treated_as_capture_authority"], False)
        self.assertIs(non_claims["receiving_carrier_treated_as_authority"], False)
        self.assertIs(non_claims["artifact_existence_treated_as_capture_authority"], False)
        self.assertIs(non_claims["artifact_path_treated_as_currentness"], False)


if __name__ == "__main__":
    unittest.main()
