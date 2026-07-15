"""Executable checks for second-carrier-execution-boundary posture only.

This suite is downstream of recorded second-carrier receipt. It verifies that
the resolver records one future second-carrier execution step boundary only:
second-carrier execution has not been created, execution artifact/output have
not been created, second-carrier output capture/result/success have not been
created, external result and cross-carrier evidence have not been created, and
source/authority/currentness/runtime/final-completion/follow-on remain
unauthorized. Receiving carrier is not authority, hidden repo state is
excluded, repo-local availability is not execution authority, selected basis
stays reference-shaped, the consumed request token remains closed, and
authorization token reuse remains blocked.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Callable, Mapping
from unittest.mock import patch


sys.dont_write_bytecode = True

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_portable_source_body_verification_second_carrier_execution_boundary as resolver


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_SECOND_CARRIER_EXECUTION_BOUNDARY_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
TRUE_RECORDED_FIELDS = tuple(resolver.ALLOWED_TRUE_RECORDED_FIELDS)
SELECTED_BASIS_KEYS = tuple(resolver.SELECTED_BASIS_KEYS)
POSTURE_KEYS = tuple(resolver.POSTURE_KEYS)

RAW_SENTINEL = "RAW_SECOND_CARRIER_EXECUTION_BOUNDARY_BODY_MUST_NOT_RETURN"
HOSTILE_RAW_VALUE = (
    "HOSTILE_SECOND_CARRIER_EXECUTION_BOUNDARY_FULL_BODY_VALUE_MUST_NOT_RETURN"
)
REDACTION_STRINGS = {
    "[bounded-redacted-raw-or-hidden-state]",
    "[bounded-reference-omitted-raw-or-hidden-state]",
}

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_second_carrier_execution_boundary_metadata",
    "declared_second_carrier_execution_boundary_question",
    "selected_second_carrier_receipt_basis",
    "selected_second_carrier_receipt_terminal_summary_basis",
    "selected_second_carrier_receipt_boundary_basis",
    "selected_packet_transfer_basis",
    "selected_packet_transfer_boundary_basis",
    "selected_packet_emission_basis",
    "selected_packet_emission_boundary_v2_basis",
    "selected_packet_emission_boundary_v1_predecessor_failure_basis",
    "selected_packet_artifact_basis",
    "selected_packet_boundary_basis",
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
    "second_carrier_execution_boundary_only_posture",
    "one_future_second_carrier_execution_step_posture",
    "second_carrier_receipt_basis_preserved_posture",
    "receipt_artifact_basis_preserved_posture",
    "receipt_not_execution_posture",
    "execution_not_created_posture",
    "execution_artifact_not_created_posture",
    "execution_output_not_created_posture",
    "second_carrier_output_capture_not_created_posture",
    "second_carrier_result_not_created_posture",
    "second_carrier_success_not_created_posture",
    "external_result_not_created_posture",
    "cross_carrier_evidence_not_created_posture",
    "execution_not_source_transfer_posture",
    "execution_not_source_receipt_posture",
    "execution_not_reception_authorization_posture",
    "source_not_created_posture",
    "authority_not_created_posture",
    "currentness_not_created_posture",
    "final_completion_not_created_posture",
    "runtime_not_created_posture",
    "continuation_not_authorized_posture",
    "reusable_permission_not_created_posture",
    "follow_on_work_not_authorized_posture",
    "receiving_carrier_not_authority_posture",
    "hidden_repo_state_excluded_posture",
    "repo_local_availability_not_execution_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "second_carrier_execution_boundary_scope",
    "second_carrier_execution_boundary_checks",
    "second_carrier_execution_boundary_statement",
    "second_carrier_execution_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_second_carrier_execution_boundary_summary",
)

REPRESENTATIVE_BLOCK_CODES = (
    "SECOND_CARRIER_EXECUTION_BOUNDARY_QUESTION_UNDECLARED",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_INTENT_UNSUPPORTED",
    "SECOND_CARRIER_RECEIPT_BASIS_MISSING",
    "SECOND_CARRIER_RECEIPT_NOT_RECORDED",
    "SECOND_CARRIER_RECEIPT_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_RECEIPT_VERSION_NOT_0_1_0",
    "SECOND_CARRIER_RECEIPT_DID_NOT_RECORD_BOUNDED_RECEIPT",
    "SECOND_CARRIER_RECEIPT_TREATED_RECEIPT_AS_EXECUTION",
    "SECOND_CARRIER_RECEIPT_TREATED_RECEIPT_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_RECEIPT_TREATED_RECEIPT_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_RECEIPT_AUTHORIZED_SECOND_CARRIER_EXECUTION",
    "SECOND_CARRIER_RECEIPT_CREATED_EXTERNAL_RESULT",
    "SECOND_CARRIER_RECEIPT_CREATED_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_RECEIPT_USED_HIDDEN_REPO_STATE_AS_EXECUTION_AUTHORITY",
    "SECOND_CARRIER_RECEIPT_TREATED_REPO_LOCAL_AVAILABILITY_AS_EXECUTION_AUTHORITY",
    "SECOND_CARRIER_RECEIPT_TREATED_RECEIVING_CARRIER_AS_AUTHORITY",
    "SECOND_CARRIER_RECEIPT_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY_OUTSIDE_BOUNDED_RECEIPT",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_EXECUTION",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_EXECUTION_ARTIFACT",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_EXECUTION_OUTPUT",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_SECOND_CARRIER_OUTPUT_CAPTURE",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_SECOND_CARRIER_RESULT",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_SECOND_CARRIER_SUCCESS",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_SOURCE",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_AUTHORITY",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_CURRENTNESS",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_FINAL_COMPLETION",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_RUNTIME",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_CONTINUATION",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
    "SECOND_CARRIER_EXECUTION_CREATED",
    "EXECUTION_ARTIFACT_CREATED",
    "EXECUTION_OUTPUT_CREATED",
    "SECOND_CARRIER_OUTPUT_CAPTURE_CREATED",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_EXECUTION_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_EXECUTION_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_EXECUTION_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_EXECUTION_AUTHORITY",
    "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_EXECUTION_BOUNDARY",
    "ARTIFACTS_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_SECOND_CARRIER_EXECUTION_BOUNDARY_SCOPE",
)

NON_MEANING_FALSE_FIELDS = (
    "second_carrier_executed_anything",
    "execution_artifact_exists",
    "execution_output_exists",
    "second_carrier_output_capture_exists",
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
    "execution_boundary_became_execution",
    "execution_boundary_became_output",
    "execution_boundary_became_result",
    "execution_boundary_became_success",
    "execution_boundary_became_external_result",
    "execution_boundary_became_cross_carrier_proof",
    "execution_boundary_became_source_transfer",
    "execution_boundary_became_source_receipt",
    "execution_boundary_became_reception_authorization",
    "execution_boundary_became_source",
    "execution_boundary_became_authority",
    "execution_boundary_became_currentness",
    "receipt_became_execution",
    "receipt_artifact_became_output",
    "receipt_artifact_became_result",
    "receipt_artifact_became_external_result",
    "receiving_carrier_became_authority",
    "transferred_packet_became_source",
    "transferred_packet_became_authority",
    "transferred_packet_became_currentness",
    "artifact_existence_became_execution_authority",
    "artifact_path_became_currentness",
    "repo_local_availability_became_execution_authority",
    "hidden_repo_state_became_execution_authority",
    "v1_packet_emission_boundary_repaired",
    "v1_packet_emission_boundary_hidden",
    "v1_packet_emission_boundary_erased",
    "v1_packet_emission_boundary_claimed_passed",
)


def _json_text(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=True)


def _false_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _valid_request(**overrides: Any) -> dict[str, Any]:
    request = (
        resolver.build_declared_portable_source_body_verification_second_carrier_execution_boundary_request(
            "second_carrier_execution_boundary_test_request_001"
        )
    )
    basis_outcomes = {
        "selected_second_carrier_receipt_boundary_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RECEIPT_BOUNDARY_RECORDED"
        ),
        "selected_packet_transfer_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_TRANSFER_RECORDED"
        ),
        "selected_packet_transfer_boundary_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_TRANSFER_BOUNDARY_RECORDED"
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
        "selected_packet_boundary_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_BOUNDARY_RECORDED"
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
    for basis_key, outcome in basis_outcomes.items():
        request[basis_key]["outcome"] = outcome
        request[basis_key]["failed_check_count"] = 0
    request["selected_packet_transfer_basis"]["bounded_packet_transfer_recorded"] = True
    request["selected_packet_transfer_basis"]["transfer_not_receipt"] = True
    request["second_carrier_execution_boundary_scope"] = list(SUPPORTED_SCOPE)
    request["declared_non_claims"] = _false_non_claims()
    request.update(copy.deepcopy(overrides))
    return request


def _with_top_level(key: str, value: Any) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request[key] = value

    return mutate


def _with_basis_flag(
    basis_key: str,
    key: str,
    value: Any,
) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request[basis_key][key] = value

    return mutate


def _delete_key(key: str) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        del request[key]

    return mutate


class SecondCarrierExecutionBoundaryResolverTest(unittest.TestCase):
    def assert_public_block_codes(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if isinstance(block, Mapping):
            block_code = block.get("block_code")
            if block_code is not None:
                self.assertIn(block_code, resolver.BLOCK_CODES)

        for check in result.get("second_carrier_execution_boundary_checks", []):
            if not isinstance(check, Mapping):
                continue
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_generated_boolean_fields(self, result: Mapping[str, Any]) -> None:
        for section_name in (
            "second_carrier_execution_boundary_statement",
            "second_carrier_execution_boundary_non_meaning",
            "non_claims",
        ):
            section = result.get(section_name)
            self.assertIsInstance(section, dict)
            for key, value in section.items():
                with self.subTest(section=section_name, key=key):
                    self.assertIsInstance(value, bool)
                    self.assertNotIn(value, REDACTION_STRINGS)

        summary = result.get(
            "portable_source_body_verification_second_carrier_execution_boundary_summary"
        )
        self.assertIsInstance(summary, dict)
        for key, value in summary.items():
            if isinstance(value, bool):
                with self.subTest(summary_bool=key):
                    self.assertIsInstance(value, bool)
                    self.assertNotIn(value, REDACTION_STRINGS)
        key_non_claims = summary.get("key_non_claims", {})
        self.assertIsInstance(key_non_claims, dict)
        for key, value in key_non_claims.items():
            with self.subTest(summary_non_claim=key):
                self.assertIsInstance(value, bool)
                self.assertNotIn(value, REDACTION_STRINGS)

    def assert_no_raw_or_hidden_sentinels(
        self,
        result: Mapping[str, Any],
        *extra_sentinels: str,
    ) -> None:
        serialized = _json_text(result)
        for sentinel in (RAW_SENTINEL, HOSTILE_RAW_VALUE, *extra_sentinels):
            self.assertNotIn(sentinel, serialized)

    def assert_no_execution_or_later_work_created(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims", {})
        self.assertIsInstance(non_claims, dict)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(no_claim=key):
                self.assertIn(key, non_claims)
                self.assertIs(non_claims[key], False)

    def assert_recorded_execution_boundary_result(
        self,
        result: Mapping[str, Any],
        request: Mapping[str, Any],
    ) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result.get("outcome"), RECORDED)
        self.assertIsNone(result.get("block"))
        for section in TOP_LEVEL_SECTIONS:
            with self.subTest(section=section):
                self.assertIn(section, result)

        metadata = result[
            "portable_source_body_verification_second_carrier_execution_boundary_metadata"
        ]
        self.assertEqual(
            metadata[
                "portable_source_body_verification_second_carrier_execution_boundary_result_version"
            ],
            "0.1.0",
        )
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_portable_source_body_verification_second_carrier_execution_boundary",
        )
        self.assertEqual(
            metadata[
                "portable_source_body_verification_second_carrier_execution_boundary_request_id"
            ],
            request["second_carrier_execution_boundary_request_id"],
        )

        summary = result[
            "portable_source_body_verification_second_carrier_execution_boundary_summary"
        ]
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertGreater(summary["passed_check_count"], 0)

        statement = result["second_carrier_execution_boundary_statement"]
        for key in TRUE_RECORDED_FIELDS:
            with self.subTest(statement_true=key):
                self.assertIs(statement.get(key), True)

        non_claims = result["non_claims"]
        for key in REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(non_claim_false=key):
                self.assertIn(key, non_claims)
                self.assertIs(non_claims[key], False)

        non_meaning = result["second_carrier_execution_boundary_non_meaning"]
        for key in NON_MEANING_FALSE_FIELDS:
            with self.subTest(non_meaning_false=key):
                self.assertIn(key, non_meaning)
                self.assertIs(non_meaning[key], False)

        receipt_basis = result["selected_second_carrier_receipt_basis"]
        self.assertEqual(
            receipt_basis["selected_second_carrier_receipt_result_outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RECEIPT_RECORDED",
        )
        self.assertEqual(
            receipt_basis["selected_second_carrier_receipt_result_version"],
            "0.1.0",
        )
        self.assertEqual(
            receipt_basis["selected_second_carrier_receipt_failed_check_count"],
            0,
        )
        self.assertIs(
            receipt_basis["selected_second_carrier_receipt_bounded_receipt_recorded"],
            True,
        )
        self.assertIs(
            receipt_basis["selected_second_carrier_receipt_receipt_not_execution"],
            True,
        )
        self.assertIs(
            receipt_basis[
                "selected_second_carrier_receipt_receiving_carrier_not_authority"
            ],
            True,
        )

        scope = result["second_carrier_execution_boundary_scope"]
        self.assertEqual(set(scope["declared_scope"]), set(SUPPORTED_SCOPE))
        self.assertEqual(scope["unsupported_scope"], [])

        remains_open = result["what_remains_open"]
        self.assertIn(
            "second-carrier execution spec/resolver/test/live artifact",
            remains_open["open_items"],
        )
        self.assertIs(remains_open["open_means_not_scheduled"], True)
        self.assertIs(remains_open["open_means_not_authorized"], True)
        self.assertIs(remains_open["open_means_not_executed"], True)

        self.assert_public_block_codes(result)
        self.assert_generated_boolean_fields(result)
        self.assert_no_raw_or_hidden_sentinels(result)

    def test_public_api_and_constants(self) -> None:
        for public_name in (
            "resolve_portable_source_body_verification_second_carrier_execution_boundary",
            "resolve_portable_source_body_verification_second_carrier_execution_boundary_from_path",
            "write_portable_source_body_verification_second_carrier_execution_boundary_result",
            "build_portable_source_body_verification_second_carrier_execution_boundary_summary",
            "build_declared_portable_source_body_verification_second_carrier_execution_boundary_request",
        ):
            with self.subTest(public_api=public_name):
                self.assertTrue(callable(getattr(resolver, public_name, None)))

        for constant_name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "RESULT_VERSION",
            "OUTPUT_ROOT",
            "SUPPORTED_SECOND_CARRIER_EXECUTION_BOUNDARY_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "BLOCK_CODES",
        ):
            with self.subTest(constant=constant_name):
                self.assertTrue(hasattr(resolver, constant_name))

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_portable_source_body_verification_"
                "second_carrier_execution_boundary"
            )
        )
        self.assertEqual(set(SUPPORTED_SCOPE), set(resolver.SUPPORTED_SECOND_CARRIER_EXECUTION_BOUNDARY_SCOPE))
        self.assertEqual(set(REQUIRED_FALSE_NON_CLAIMS), set(resolver.REQUIRED_FALSE_NON_CLAIMS))

        for block_code in REPRESENTATIVE_BLOCK_CODES:
            with self.subTest(block_code=block_code):
                self.assertIn(block_code, resolver.BLOCK_CODES)

    def test_records_successful_second_carrier_execution_boundary_only(self) -> None:
        request = _valid_request()
        original_request = copy.deepcopy(request)

        result = resolver.resolve_portable_source_body_verification_second_carrier_execution_boundary(
            declared_second_carrier_execution_boundary_request=request
        )

        self.assertEqual(request, original_request)
        self.assert_recorded_execution_boundary_result(result, request)

        statement = result["second_carrier_execution_boundary_statement"]
        for key in (
            "second_carrier_execution_boundary_recorded",
            "one_future_second_carrier_execution_step_declared",
            "second_carrier_receipt_basis_preserved",
            "receipt_artifact_basis_preserved",
            "receipt_not_execution",
            "execution_not_created",
            "execution_artifact_not_created",
            "execution_output_not_created",
            "second_carrier_output_capture_not_created",
            "second_carrier_result_not_created",
            "second_carrier_success_not_created",
            "external_result_not_created",
            "cross_carrier_evidence_not_created",
            "execution_not_source_transfer",
            "execution_not_source_receipt",
            "execution_not_reception_authorization",
            "source_not_created",
            "authority_not_created",
            "currentness_not_created",
            "final_completion_not_created",
            "runtime_not_created",
            "continuation_not_authorized",
            "reusable_permission_not_created",
            "follow_on_work_not_authorized",
            "receiving_carrier_not_authority",
            "hidden_repo_state_excluded",
            "hidden_repo_state_not_used_as_execution_authority",
            "repo_local_availability_not_execution_authority",
            "selected_basis_reference_shape_preserved",
            "raw_full_prior_artifact_body_not_returned",
            "authorization_token_reuse_blocked",
            "consumed_request_token_remains_closed",
        ):
            with self.subTest(statement=key):
                self.assertIs(statement[key], True)

        self.assert_no_execution_or_later_work_created(result)

    def test_summary_helper_preserves_execution_boundary_posture(self) -> None:
        request = _valid_request()
        result = resolver.resolve_portable_source_body_verification_second_carrier_execution_boundary(
            declared_second_carrier_execution_boundary_request=request
        )

        summary = (
            resolver.build_portable_source_body_verification_second_carrier_execution_boundary_summary(
                result
            )
        )
        statement = result["second_carrier_execution_boundary_statement"]

        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(
            summary["request_id"], request["second_carrier_execution_boundary_request_id"]
        )
        self.assertEqual(summary["question"], request["second_carrier_execution_boundary_question"])
        self.assertEqual(summary["intent"], request["second_carrier_execution_boundary_intent"])
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertGreater(summary["passed_check_count"], 0)

        for key in (
            "second_carrier_execution_boundary_recorded",
            "one_future_second_carrier_execution_step_declared",
            "second_carrier_receipt_basis_preserved",
            "receipt_artifact_basis_preserved",
            "receipt_not_execution",
            "execution_not_created",
            "execution_artifact_not_created",
            "execution_output_not_created",
            "second_carrier_output_capture_not_created",
            "second_carrier_result_not_created",
            "second_carrier_success_not_created",
            "external_result_not_created",
            "cross_carrier_evidence_not_created",
            "execution_not_source_transfer",
            "execution_not_source_receipt",
            "execution_not_reception_authorization",
            "source_not_created",
            "authority_not_created",
            "currentness_not_created",
            "final_completion_not_created",
            "runtime_not_created",
            "follow_on_work_not_authorized",
            "receiving_carrier_not_authority",
            "hidden_repo_state_excluded",
            "hidden_repo_state_not_used_as_execution_authority",
            "repo_local_availability_not_execution_authority",
            "selected_basis_reference_shape_preserved",
            "raw_full_prior_artifact_body_not_returned",
        ):
            with self.subTest(summary_key=key):
                self.assertIs(summary[key], statement[key])

        self.assertEqual(
            summary["selected_second_carrier_receipt_outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RECEIPT_RECORDED",
        )
        self.assertEqual(summary["selected_second_carrier_receipt_version"], "0.1.0")
        self.assertEqual(summary["selected_second_carrier_receipt_failed_check_count"], 0)
        self.assertIs(
            summary["no_execution_output_result_success_external_result_cross_carrier_evidence"],
            True,
        )
        self.assertIs(
            summary["no_source_authority_currentness_final_completion_runtime"],
            True,
        )
        self.assertIs(summary["no_deployment_public_release_follow_on"], True)
        self.assertIs(summary["v1_predecessor_failure_preserved"], True)
        self.assertIs(summary["v1_not_repaired_hidden_or_claimed_passed"], True)

        key_non_claims = summary["key_non_claims"]
        for key, value in key_non_claims.items():
            with self.subTest(key_non_claim=key):
                self.assertIs(value, False)

    def test_representative_blocking_behavior(self) -> None:
        malformed_cases: tuple[tuple[str, Any], ...] = (
            ("missing request", None),
            ("non-mapping request", ["not", "a", "mapping"]),
        )
        for label, supplied_request in malformed_cases:
            with self.subTest(block_case=label):
                result = (
                    resolver.resolve_portable_source_body_verification_second_carrier_execution_boundary(
                        declared_second_carrier_execution_boundary_request=supplied_request
                    )
                )
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertIn(result["block"]["block_code"], resolver.BLOCK_CODES)
                self.assert_public_block_codes(result)
                self.assert_no_execution_or_later_work_created(result)

        def missing_non_claim(request: dict[str, Any]) -> None:
            del request["declared_non_claims"]["second_carrier_execution_created"]

        cases: list[tuple[str, Callable[[dict[str, Any]], None], str]] = [
            (
                "explicit block intent",
                _with_top_level("second_carrier_execution_boundary_intent", resolver.INTENT_BLOCK),
                "SECOND_CARRIER_EXECUTION_BOUNDARY_BLOCK_REQUESTED",
            ),
            (
                "unsupported intent",
                _with_top_level("second_carrier_execution_boundary_intent", "UNSUPPORTED"),
                "SECOND_CARRIER_EXECUTION_BOUNDARY_INTENT_UNSUPPORTED",
            ),
            (
                "unsupported scope",
                _with_top_level(
                    "second_carrier_execution_boundary_scope",
                    list(SUPPORTED_SCOPE) + ["UNSUPPORTED_SCOPE"],
                ),
                "UNSUPPORTED_SECOND_CARRIER_EXECUTION_BOUNDARY_SCOPE",
            ),
            (
                "question undeclared",
                _with_top_level("second_carrier_execution_boundary_question", ""),
                "SECOND_CARRIER_EXECUTION_BOUNDARY_QUESTION_UNDECLARED",
            ),
            (
                "missing second-carrier receipt basis",
                _delete_key("selected_second_carrier_receipt_basis"),
                "SECOND_CARRIER_RECEIPT_BASIS_MISSING",
            ),
            (
                "receipt not recorded",
                _with_top_level("selected_second_carrier_receipt_result_outcome", "NOT_RECORDED"),
                "SECOND_CARRIER_RECEIPT_NOT_RECORDED",
            ),
            (
                "receipt failed checks",
                _with_top_level("selected_second_carrier_receipt_failed_check_count", 1),
                "SECOND_CARRIER_RECEIPT_FAILED_CHECKS_PRESENT",
            ),
            (
                "receipt version mismatch",
                _with_top_level("selected_second_carrier_receipt_result_version", "9.9.9"),
                "SECOND_CARRIER_RECEIPT_VERSION_NOT_0_1_0",
            ),
            (
                "receipt did not record bounded receipt",
                _with_top_level("selected_second_carrier_receipt_bounded_receipt_recorded", False),
                "SECOND_CARRIER_RECEIPT_DID_NOT_RECORD_BOUNDED_RECEIPT",
            ),
            (
                "receipt treated as execution",
                _with_top_level("selected_second_carrier_receipt_receipt_not_execution", False),
                "SECOND_CARRIER_RECEIPT_TREATED_RECEIPT_AS_EXECUTION",
            ),
            (
                "receipt treated as external result",
                _with_top_level(
                    "selected_second_carrier_receipt_receipt_not_external_result",
                    False,
                ),
                "SECOND_CARRIER_RECEIPT_TREATED_RECEIPT_AS_EXTERNAL_RESULT",
            ),
            (
                "receipt treated as cross-carrier evidence",
                _with_top_level(
                    "selected_second_carrier_receipt_receipt_not_cross_carrier_evidence",
                    False,
                ),
                "SECOND_CARRIER_RECEIPT_TREATED_RECEIPT_AS_CROSS_CARRIER_EVIDENCE",
            ),
            (
                "receipt authorized second-carrier execution",
                _with_top_level(
                    "selected_second_carrier_receipt_authorized_second_carrier_execution",
                    True,
                ),
                "SECOND_CARRIER_RECEIPT_AUTHORIZED_SECOND_CARRIER_EXECUTION",
            ),
            (
                "receipt created external result",
                _with_top_level("selected_second_carrier_receipt_created_external_result", True),
                "SECOND_CARRIER_RECEIPT_CREATED_EXTERNAL_RESULT",
            ),
            (
                "receipt created cross-carrier evidence",
                _with_top_level(
                    "selected_second_carrier_receipt_created_cross_carrier_evidence",
                    True,
                ),
                "SECOND_CARRIER_RECEIPT_CREATED_CROSS_CARRIER_EVIDENCE",
            ),
            (
                "receipt used hidden repo state as execution authority",
                _with_top_level(
                    "selected_second_carrier_receipt_used_hidden_repo_state_as_execution_authority",
                    True,
                ),
                "SECOND_CARRIER_RECEIPT_USED_HIDDEN_REPO_STATE_AS_EXECUTION_AUTHORITY",
            ),
            (
                "receipt treated repo-local availability as execution authority",
                _with_top_level(
                    "selected_second_carrier_receipt_treated_repo_local_availability_as_execution_authority",
                    True,
                ),
                "SECOND_CARRIER_RECEIPT_TREATED_REPO_LOCAL_AVAILABILITY_AS_EXECUTION_AUTHORITY",
            ),
            (
                "receipt treated receiving carrier as authority",
                _with_top_level(
                    "selected_second_carrier_receipt_receiving_carrier_not_authority",
                    False,
                ),
                "SECOND_CARRIER_RECEIPT_TREATED_RECEIVING_CARRIER_AS_AUTHORITY",
            ),
            (
                "receipt returned raw prior body outside receipt posture",
                _with_top_level(
                    "selected_second_carrier_receipt_raw_full_prior_artifact_body_returned_outside_bounded_receipt",
                    True,
                ),
                "SECOND_CARRIER_RECEIPT_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY_OUTSIDE_BOUNDED_RECEIPT",
            ),
            (
                "selected basis not reference-shaped",
                _with_top_level("reference_shaped_input_posture", False),
                "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
            ),
            (
                "full prior body emitted outside bounded execution boundary",
                _with_top_level(
                    "full_prior_artifact_body_emitted_outside_bounded_execution_boundary",
                    True,
                ),
                "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_EXECUTION_BOUNDARY",
            ),
            (
                "command report lineage treated as current report artifact",
                _with_basis_flag(
                    "selected_command_report_lineage_basis",
                    "command_report_lineage_treated_as_current_report_artifact",
                    True,
                ),
                "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENT_REPORT_ARTIFACT",
            ),
            (
                "command report lineage treated as source",
                _with_basis_flag(
                    "selected_command_report_lineage_basis",
                    "command_report_lineage_treated_as_source",
                    True,
                ),
                "COMMAND_REPORT_LINEAGE_TREATED_AS_SOURCE",
            ),
            (
                "command report lineage treated as authority",
                _with_basis_flag(
                    "selected_command_report_lineage_basis",
                    "command_report_lineage_treated_as_authority",
                    True,
                ),
                "COMMAND_REPORT_LINEAGE_TREATED_AS_AUTHORITY",
            ),
            (
                "command report lineage treated as currentness",
                _with_basis_flag(
                    "selected_command_report_lineage_basis",
                    "command_report_lineage_treated_as_currentness",
                    True,
                ),
                "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENTNESS",
            ),
            (
                "required non-claim missing",
                missing_non_claim,
                "NON_CLAIM_MISSING_OR_FLIPPED",
            ),
        ]

        forbidden_flag_cases = {
            "second_carrier_execution_boundary_treated_as_execution": (
                "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_EXECUTION"
            ),
            "second_carrier_execution_boundary_treated_as_execution_artifact": (
                "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_EXECUTION_ARTIFACT"
            ),
            "second_carrier_execution_boundary_treated_as_execution_output": (
                "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_EXECUTION_OUTPUT"
            ),
            "second_carrier_execution_boundary_treated_as_second_carrier_output_capture": (
                "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_SECOND_CARRIER_OUTPUT_CAPTURE"
            ),
            "second_carrier_execution_boundary_treated_as_second_carrier_result": (
                "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_SECOND_CARRIER_RESULT"
            ),
            "second_carrier_execution_boundary_treated_as_second_carrier_success": (
                "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_SECOND_CARRIER_SUCCESS"
            ),
            "second_carrier_execution_boundary_treated_as_external_result": (
                "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_EXTERNAL_RESULT"
            ),
            "second_carrier_execution_boundary_treated_as_cross_carrier_evidence": (
                "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_CROSS_CARRIER_EVIDENCE"
            ),
            "second_carrier_execution_boundary_treated_as_source_transfer": (
                "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_SOURCE_TRANSFER"
            ),
            "second_carrier_execution_boundary_treated_as_source_receipt": (
                "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_SOURCE_RECEIPT"
            ),
            "second_carrier_execution_boundary_treated_as_reception_authorization": (
                "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION"
            ),
            "second_carrier_execution_boundary_treated_as_source": (
                "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_SOURCE"
            ),
            "second_carrier_execution_boundary_treated_as_authority": (
                "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_AUTHORITY"
            ),
            "second_carrier_execution_boundary_treated_as_currentness": (
                "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_CURRENTNESS"
            ),
            "second_carrier_execution_boundary_treated_as_final_completion": (
                "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_FINAL_COMPLETION"
            ),
            "second_carrier_execution_boundary_treated_as_runtime": (
                "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_RUNTIME"
            ),
            "second_carrier_execution_boundary_treated_as_continuation": (
                "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_CONTINUATION"
            ),
            "second_carrier_execution_boundary_treated_as_reusable_permission": (
                "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION"
            ),
            "second_carrier_execution_boundary_treated_as_follow_on_work": (
                "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK"
            ),
            "second_carrier_execution_created": "SECOND_CARRIER_EXECUTION_CREATED",
            "execution_artifact_created": "EXECUTION_ARTIFACT_CREATED",
            "execution_output_created": "EXECUTION_OUTPUT_CREATED",
            "second_carrier_output_capture_created": "SECOND_CARRIER_OUTPUT_CAPTURE_CREATED",
            "second_carrier_result_created": "SECOND_CARRIER_RESULT_CREATED",
            "second_carrier_success_created": "SECOND_CARRIER_SUCCESS_CREATED",
            "external_result_created": "EXTERNAL_RESULT_CREATED",
            "cross_carrier_evidence_created": "CROSS_CARRIER_EVIDENCE_CREATED",
            "source_transfer_occurred": "SOURCE_TRANSFER_OCCURRED",
            "source_receipt_occurred": "SOURCE_RECEIPT_OCCURRED",
            "reception_authorization_created": "RECEPTION_AUTHORIZATION_CREATED",
            "source_created": "SOURCE_CREATED",
            "authority_created": "AUTHORITY_CREATED",
            "currentness_created": "CURRENTNESS_CREATED",
            "final_completion_claimed": "FINAL_COMPLETION_CLAIMED",
            "runtime_hosting_created": "RUNTIME_HOSTING_CREATED",
            "deployment_created": "DEPLOYMENT_CREATED",
            "public_release_created": "PUBLIC_RELEASE_CREATED",
            "operation_permission_created": "OPERATION_PERMISSION_CREATED",
            "continuation_authorized": "CONTINUATION_AUTHORIZED",
            "reusable_permission_created": "REUSABLE_PERMISSION_CREATED",
            "derivative_reception_authorized": "DERIVATIVE_RECEPTION_AUTHORIZED",
            "vessel_relation_authorized": "VESSEL_RELATION_AUTHORIZED",
            "another_reception_request_authorized": "ANOTHER_RECEPTION_REQUEST_AUTHORIZED",
            "follow_on_work_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
            "receiving_carrier_treated_as_authority": "RECEIVING_CARRIER_TREATED_AS_AUTHORITY",
            "artifact_existence_treated_as_execution_authority": (
                "ARTIFACT_EXISTENCE_TREATED_AS_EXECUTION_AUTHORITY"
            ),
            "artifact_path_treated_as_currentness": "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
            "repo_local_availability_treated_as_execution_authority": (
                "REPO_LOCAL_AVAILABILITY_TREATED_AS_EXECUTION_AUTHORITY"
            ),
            "hidden_repo_state_used_as_execution_content": (
                "HIDDEN_REPO_STATE_USED_AS_EXECUTION_CONTENT"
            ),
            "hidden_repo_state_used_as_execution_authority": (
                "HIDDEN_REPO_STATE_USED_AS_EXECUTION_AUTHORITY"
            ),
            "raw_full_prior_artifact_body_returned": "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
            "prior_artifacts_mutated": "ARTIFACTS_MUTATED",
            "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
            "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
            "v1_repaired": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
            "v1_hidden": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
            "v1_claimed_passed": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        }
        for key, expected_code in forbidden_flag_cases.items():
            cases.append((f"{key} true", _with_top_level(key, True), expected_code))

        for label, mutate, expected_code in cases:
            with self.subTest(block_case=label):
                request = _valid_request()
                mutate(request)
                result = (
                    resolver.resolve_portable_source_body_verification_second_carrier_execution_boundary(
                        declared_second_carrier_execution_boundary_request=request
                    )
                )
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertIsInstance(result["block"], dict)
                self.assertIn(result["block"]["block_code"], resolver.BLOCK_CODES)
                emitted_codes = {
                    check.get("block_code")
                    for check in result["second_carrier_execution_boundary_checks"]
                    if check.get("block_code")
                }
                self.assertIn(expected_code, emitted_codes)
                self.assert_public_block_codes(result)
                self.assert_no_execution_or_later_work_created(result)
                self.assertIs(result["non_claims"]["consumed_request_reopened"], False)
                self.assertIs(result["non_claims"]["authorization_token_reused"], False)
                self.assertIs(result["non_claims"]["v1_repaired"], False)
                self.assertIs(result["non_claims"]["v1_hidden"], False)
                self.assertIs(result["non_claims"]["v1_claimed_passed"], False)

    def test_path_and_write_behavior(self) -> None:
        request = _valid_request()

        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            request_path = tmp / "declared_request.json"
            request_path.write_text(
                json.dumps(request, indent=2, sort_keys=True),
                encoding="utf-8",
            )

            result = (
                resolver.resolve_portable_source_body_verification_second_carrier_execution_boundary_from_path(
                    request_path
                )
            )
            self.assertEqual(result["outcome"], RECORDED)
            metadata = result[
                "portable_source_body_verification_second_carrier_execution_boundary_metadata"
            ]
            self.assertEqual(
                metadata[
                    "portable_source_body_verification_second_carrier_execution_boundary_result_version"
                ],
                "0.1.0",
            )
            self.assertEqual(
                metadata["resolver_module"],
                "resolve_portable_source_body_verification_second_carrier_execution_boundary",
            )

            bad_json_path = tmp / "bad.json"
            bad_json_path.write_text("{bad json", encoding="utf-8")
            with self.assertRaises(
                resolver.PortableSourceBodyVerificationSecondCarrierExecutionBoundaryError
            ):
                resolver.resolve_portable_source_body_verification_second_carrier_execution_boundary_from_path(
                    bad_json_path
                )

            array_path = tmp / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = (
                resolver.resolve_portable_source_body_verification_second_carrier_execution_boundary_from_path(
                    array_path
                )
            )
            self.assertEqual(array_result["outcome"], BLOCKED)
            self.assert_public_block_codes(array_result)

            with self.assertRaises(
                resolver.PortableSourceBodyVerificationSecondCarrierExecutionBoundaryError
            ):
                resolver.resolve_portable_source_body_verification_second_carrier_execution_boundary_from_path(
                    tmp / "missing.json"
                )

            output_root = (
                tmp
                / "artifacts"
                / "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_execution_boundary"
            )
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = (
                    resolver.write_portable_source_body_verification_second_carrier_execution_boundary_result(
                        result
                    )
                )
                second_path = (
                    resolver.write_portable_source_body_verification_second_carrier_execution_boundary_result(
                        result
                    )
                )

            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertEqual(first_path.parent, output_root)
            self.assertEqual(second_path.parent, output_root)
            self.assertEqual(
                first_path.parent.name,
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_execution_boundary",
            )
            parsed = json.loads(first_path.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], RECORDED)

            written_path_text = first_path.as_posix()
            for forbidden_root in (
                "/integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_receipt/",
                "/integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_execution/",
                "/integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_output_capture/",
                "/integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_result/",
                "/integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_success/",
                "/integrity_host_v0_min_coexistence_portable_source_body_verification_external_result/",
                "/integrity_host_v0_min_coexistence_portable_source_body_verification_cross_carrier/",
                "/runtime/",
                "/deployment/",
                "/public_release/",
            ):
                with self.subTest(forbidden_root=forbidden_root):
                    self.assertNotIn(forbidden_root, written_path_text)

    def test_input_request_and_selected_basis_are_not_mutated(self) -> None:
        request = _valid_request()
        original = copy.deepcopy(request)
        selected_basis_originals = {
            key: copy.deepcopy(request[key]) for key in SELECTED_BASIS_KEYS
        }
        posture_originals = {key: copy.deepcopy(request[key]) for key in POSTURE_KEYS}
        scope_original = copy.deepcopy(request["second_carrier_execution_boundary_scope"])
        non_claims_original = copy.deepcopy(request["declared_non_claims"])

        result = resolver.resolve_portable_source_body_verification_second_carrier_execution_boundary(
            declared_second_carrier_execution_boundary_request=request
        )

        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(request, original)
        for key, expected in selected_basis_originals.items():
            with self.subTest(selected_basis=key):
                self.assertEqual(request[key], expected)
        for key, expected in posture_originals.items():
            with self.subTest(posture=key):
                self.assertEqual(request[key], expected)
        self.assertEqual(request["second_carrier_execution_boundary_scope"], scope_original)
        self.assertEqual(request["declared_non_claims"], non_claims_original)

    def test_raw_full_body_and_hidden_repo_state_containment(self) -> None:
        request = _valid_request()
        injected_sections = (
            "selected_second_carrier_receipt_basis",
            "selected_second_carrier_receipt_boundary_basis",
            "selected_packet_transfer_basis",
            "selected_packet_transfer_boundary_basis",
            "selected_packet_emission_basis",
            "selected_packet_emission_boundary_v2_basis",
            "selected_packet_artifact_basis",
            "selected_packet_boundary_basis",
            "selected_command_success_basis",
            "selected_output_capture_v2_basis",
            "selected_command_report_lineage_basis",
            "selected_artifact_containment_basis",
        )
        hostile_keys = (
            "raw_body",
            "raw_full_body",
            "full_body",
            "artifact_body",
            "raw_result_body",
            "raw_output_body",
            "execution_body",
            "execution_artifact_body",
            "execution_output_body",
            "second_carrier_output_capture_body",
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
            "unlisted_file_dependency",
        )
        for section_name in injected_sections:
            section = request[section_name]
            for hostile_key in hostile_keys:
                section[hostile_key] = HOSTILE_RAW_VALUE
            section["nested_hostile"] = {
                "raw_full_body": RAW_SENTINEL,
                "list": [
                    {"execution_body": RAW_SENTINEL},
                    "RAW_SECOND_CARRIER_EXECUTION_BOUNDARY_BODY_MUST_NOT_RETURN",
                ],
            }

        original = copy.deepcopy(request)
        result = resolver.resolve_portable_source_body_verification_second_carrier_execution_boundary(
            declared_second_carrier_execution_boundary_request=request
        )

        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assert_public_block_codes(result)
        self.assert_no_raw_or_hidden_sentinels(result)
        self.assert_no_execution_or_later_work_created(result)
        self.assertIs(result["non_claims"]["hidden_repo_state_used_as_execution_content"], False)
        self.assertIs(result["non_claims"]["hidden_repo_state_used_as_execution_authority"], False)
        self.assertIs(
            result["non_claims"]["repo_local_availability_treated_as_execution_authority"],
            False,
        )
        self.assertIs(result["non_claims"]["receiving_carrier_treated_as_authority"], False)
        self.assertIs(
            result["non_claims"]["artifact_existence_treated_as_execution_authority"],
            False,
        )
        self.assertIs(result["non_claims"]["artifact_path_treated_as_currentness"], False)
        self.assertEqual(request, original)
        self.assert_generated_boolean_fields(result)


if __name__ == "__main__":
    unittest.main()
