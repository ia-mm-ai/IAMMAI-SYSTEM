"""Executable checks for second-carrier execution posture only.

This suite is downstream of recorded second-carrier execution boundary. It
verifies that the resolver records one bounded second-carrier execution posture
only: execution output is not created, second-carrier output capture/result/
success are not created, external result and cross-carrier evidence are not
created, and source/authority/currentness/runtime/final-completion/follow-on
remain unauthorized. Receiving carrier is not authority, hidden repo state is
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
from collections.abc import Mapping as MappingABC
from pathlib import Path
from typing import Any, Callable, Mapping
from unittest.mock import patch


sys.dont_write_bytecode = True

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_portable_source_body_verification_second_carrier_execution as resolver


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_SECOND_CARRIER_EXECUTION_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
TRUE_RECORDED_FIELDS = tuple(resolver.ALLOWED_TRUE_RECORDED_FIELDS)
SELECTED_BASIS_KEYS = tuple(resolver.SELECTED_BASIS_KEYS)
POSTURE_KEYS = tuple(resolver.POSTURE_KEYS)

RAW_SENTINEL = "RAW_SECOND_CARRIER_EXECUTION_BODY_MUST_NOT_RETURN"
HOSTILE_RAW_VALUE = "HOSTILE_SECOND_CARRIER_EXECUTION_FULL_BODY_VALUE_MUST_NOT_RETURN"
REDACTION_STRINGS = {
    "[bounded-redacted-raw-or-hidden-state]",
    "[bounded-reference-omitted-raw-or-hidden-state]",
}

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_second_carrier_execution_metadata",
    "declared_second_carrier_execution_question",
    "selected_second_carrier_execution_boundary_basis",
    "selected_second_carrier_execution_boundary_terminal_summary_basis",
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
    "second_carrier_execution_spec_only_posture",
    "one_bounded_second_carrier_execution_posture",
    "second_carrier_execution_boundary_basis_preserved_posture",
    "second_carrier_receipt_basis_preserved_posture",
    "receipt_artifact_basis_preserved_posture",
    "execution_recorded_bounded_posture",
    "execution_artifact_recorded_or_bounded_posture",
    "execution_output_not_created_posture",
    "execution_not_output_capture_posture",
    "execution_not_result_posture",
    "execution_not_success_posture",
    "execution_not_external_result_posture",
    "execution_not_cross_carrier_evidence_posture",
    "execution_not_source_transfer_posture",
    "execution_not_source_receipt_posture",
    "execution_not_reception_authorization_posture",
    "second_carrier_output_capture_not_created_posture",
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
    "repo_local_availability_not_execution_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "second_carrier_execution_scope",
    "second_carrier_execution_checks",
    "second_carrier_execution_statement",
    "second_carrier_execution_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_second_carrier_execution_summary",
)

REPRESENTATIVE_BLOCK_CODES = (
    "SECOND_CARRIER_EXECUTION_QUESTION_UNDECLARED",
    "SECOND_CARRIER_EXECUTION_INTENT_UNSUPPORTED",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_BASIS_MISSING",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_NOT_RECORDED",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_VERSION_NOT_0_1_0",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_DID_NOT_DECLARE_FUTURE_EXECUTION_STEP",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_ALREADY_CREATED_EXECUTION",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_ALREADY_CREATED_EXECUTION_ARTIFACT",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_ALREADY_CREATED_EXECUTION_OUTPUT",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_ALREADY_CREATED_SECOND_CARRIER_OUTPUT_CAPTURE",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_ALREADY_CREATED_SECOND_CARRIER_RESULT",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_ALREADY_CREATED_SECOND_CARRIER_SUCCESS",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_CREATED_EXTERNAL_RESULT",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_CREATED_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_USED_HIDDEN_REPO_STATE_AS_EXECUTION_AUTHORITY",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_REPO_LOCAL_AVAILABILITY_AS_EXECUTION_AUTHORITY",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_TREATED_RECEIVING_CARRIER_AS_AUTHORITY",
    "SECOND_CARRIER_EXECUTION_BOUNDARY_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY",
    "SECOND_CARRIER_RECEIPT_BASIS_MISSING",
    "SECOND_CARRIER_RECEIPT_NOT_RECORDED",
    "SECOND_CARRIER_RECEIPT_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_RECEIPT_DID_NOT_RECORD_BOUNDED_RECEIPT",
    "SECOND_CARRIER_RECEIPT_TREATED_RECEIPT_AS_EXECUTION",
    "SECOND_CARRIER_EXECUTION_TREATED_AS_OUTPUT",
    "SECOND_CARRIER_EXECUTION_TREATED_AS_OUTPUT_CAPTURE",
    "SECOND_CARRIER_EXECUTION_TREATED_AS_RESULT",
    "SECOND_CARRIER_EXECUTION_TREATED_AS_SUCCESS",
    "SECOND_CARRIER_EXECUTION_TREATED_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_EXECUTION_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXECUTION_TREATED_AS_SOURCE_TRANSFER",
    "SECOND_CARRIER_EXECUTION_TREATED_AS_SOURCE_RECEIPT",
    "SECOND_CARRIER_EXECUTION_TREATED_AS_RECEPTION_AUTHORIZATION",
    "SECOND_CARRIER_EXECUTION_TREATED_AS_SOURCE",
    "SECOND_CARRIER_EXECUTION_TREATED_AS_AUTHORITY",
    "SECOND_CARRIER_EXECUTION_TREATED_AS_CURRENTNESS",
    "SECOND_CARRIER_EXECUTION_TREATED_AS_FINAL_COMPLETION",
    "SECOND_CARRIER_EXECUTION_TREATED_AS_RUNTIME",
    "SECOND_CARRIER_EXECUTION_TREATED_AS_CONTINUATION",
    "SECOND_CARRIER_EXECUTION_TREATED_AS_REUSABLE_PERMISSION",
    "SECOND_CARRIER_EXECUTION_TREATED_AS_FOLLOW_ON_WORK",
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
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_EXECUTION",
    "ARTIFACTS_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_SECOND_CARRIER_EXECUTION_SCOPE",
)

NON_MEANING_FALSE_FIELDS = (
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
    "execution_became_output",
    "execution_became_result",
    "execution_became_success",
    "execution_became_external_result",
    "execution_became_cross_carrier_proof",
    "execution_became_source_transfer",
    "execution_became_source_receipt",
    "execution_became_reception_authorization",
    "execution_became_source",
    "execution_became_authority",
    "execution_became_currentness",
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

DOWNSTREAM_FALSE_NON_CLAIMS = (
    "execution_output_created",
    "second_carrier_output_capture_created",
    "second_carrier_result_created",
    "second_carrier_success_created",
    "external_result_created",
    "cross_carrier_evidence_created",
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
    "operation_permission_created",
    "continuation_authorized",
    "reusable_permission_created",
    "derivative_reception_authorized",
    "vessel_relation_authorized",
    "another_reception_request_authorized",
    "follow_on_work_authorized",
    "consumed_request_reopened",
    "authorization_token_reused",
    "v1_repaired",
    "v1_hidden",
    "v1_claimed_passed",
)


def _json_text(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=True)


def _valid_request(**overrides: Any) -> dict[str, Any]:
    request = (
        resolver.build_declared_portable_source_body_verification_second_carrier_execution_request(
            second_carrier_execution_request_id="second_carrier_execution_test_001"
        )
    )
    request["second_carrier_execution_scope"] = list(SUPPORTED_SCOPE)
    request["declared_non_claims"] = {
        key: False for key in REQUIRED_FALSE_NON_CLAIMS
    }

    basis_outcomes = {
        "selected_second_carrier_execution_boundary_terminal_summary_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_BOUNDARY_RECORDED"
        ),
        "selected_second_carrier_receipt_terminal_summary_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RECEIPT_RECORDED"
        ),
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
    for key, outcome in basis_outcomes.items():
        request[key].update(
            {
                "outcome": outcome,
                "result_version": "0.1.0",
                "failed_check_count": 0,
                "basis_remains_basis_only": True,
                "reference_shape_preserved": True,
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
    for key in (
        "selected_packet_emission_boundary_v1_predecessor_failure_basis",
        "selected_predecessor_failure_basis",
    ):
        request[key].update(
            {
                "predecessor_failure_visible": True,
                "v1_repaired": False,
                "v1_hidden": False,
                "v1_claimed_passed": False,
            }
        )
    request["selected_evidence_manifest_basis"].update({"basis_declared": True})
    request["selected_artifact_containment_basis"].update({"basis_declared": True})
    request["selected_portable_verification_basis"].update({"basis_declared": True})

    for key, value in overrides.items():
        if value is _DELETE:
            request.pop(key, None)
        else:
            request[key] = value
    return request


class _DeleteMarker:
    pass


_DELETE = _DeleteMarker()


def _mutated_request(mutator: Callable[[dict[str, Any]], None]) -> dict[str, Any]:
    request = _valid_request()
    mutator(request)
    return request


def _resolve(request: Mapping[str, Any] | None) -> dict[str, Any]:
    return resolver.resolve_portable_source_body_verification_second_carrier_execution(
        declared_second_carrier_execution_request=request
    )


class SecondCarrierExecutionResolverTests(unittest.TestCase):
    def assertPublicBlockCodes(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if isinstance(block, MappingABC):
            code = block.get("block_code")
            if code:
                self.assertIn(code, resolver.BLOCK_CODES)
        for check in result.get("second_carrier_execution_checks", []):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assertGeneratedBooleansAreBool(self, result: Mapping[str, Any]) -> None:
        for section in (
            "second_carrier_execution_statement",
            "second_carrier_execution_non_meaning",
            "non_claims",
        ):
            for key, value in result.get(section, {}).items():
                with self.subTest(section=section, key=key):
                    self.assertIs(type(value), bool)
                    self.assertNotIn(value, REDACTION_STRINGS)
        for key in POSTURE_KEYS:
            posture = result.get(key, {})
            for boolean_key in ("declared", "preserved"):
                with self.subTest(section=key, key=boolean_key):
                    self.assertIs(type(posture.get(boolean_key)), bool)

    def assertNoRawSentinels(self, result: Mapping[str, Any]) -> None:
        serialized = _json_text(result)
        self.assertNotIn(RAW_SENTINEL, serialized)
        self.assertNotIn(HOSTILE_RAW_VALUE, serialized)
        self.assertNotIn("RAW_SECOND_CARRIER_EXECUTION_BODY_MUST_NOT_RETURN", serialized)

    def assertNoDownstreamCreated(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims", {})
        for key in DOWNSTREAM_FALSE_NON_CLAIMS:
            with self.subTest(non_claim=key):
                self.assertIs(non_claims.get(key), False)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_portable_source_body_verification_second_carrier_execution",
            "resolve_portable_source_body_verification_second_carrier_execution_from_path",
            "write_portable_source_body_verification_second_carrier_execution_result",
            "build_portable_source_body_verification_second_carrier_execution_summary",
            "build_declared_portable_source_body_verification_second_carrier_execution_request",
        ):
            self.assertTrue(callable(getattr(resolver, name, None)), name)

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "RESULT_VERSION",
            "OUTPUT_ROOT",
            "SUPPORTED_SECOND_CARRIER_EXECUTION_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_portable_source_body_verification_"
                "second_carrier_execution"
            )
        )
        for code in REPRESENTATIVE_BLOCK_CODES:
            with self.subTest(block_code=code):
                self.assertIn(code, resolver.BLOCK_CODES)

    def test_successful_second_carrier_execution_recorded_result(self) -> None:
        request = _valid_request()
        result = _resolve(request)

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(result["portable_source_body_verification_second_carrier_execution_summary"]["failed_check_count"], 0)
        self.assertIsNone(result["block"])
        self.assertPublicBlockCodes(result)

        for section in TOP_LEVEL_SECTIONS:
            with self.subTest(section=section):
                self.assertIn(section, result)

        metadata = result["portable_source_body_verification_second_carrier_execution_metadata"]
        self.assertEqual(
            metadata["portable_source_body_verification_second_carrier_execution_result_version"],
            "0.1.0",
        )
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_portable_source_body_verification_second_carrier_execution",
        )
        self.assertEqual(
            metadata["portable_source_body_verification_second_carrier_execution_request_id"],
            "second_carrier_execution_test_001",
        )

        statement = result["second_carrier_execution_statement"]
        for key in TRUE_RECORDED_FIELDS:
            with self.subTest(statement=key):
                self.assertIs(statement.get(key), True)

        non_claims = result["non_claims"]
        for key in REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(non_claim=key):
                self.assertIs(non_claims.get(key), False)

        non_meaning = result["second_carrier_execution_non_meaning"]
        for key in NON_MEANING_FALSE_FIELDS:
            with self.subTest(non_meaning=key):
                self.assertIs(non_meaning.get(key), False)

        self.assertGeneratedBooleansAreBool(result)
        self.assertNoRawSentinels(result)
        self.assertNoDownstreamCreated(result)

    def test_summary_helper_preserves_execution_posture(self) -> None:
        result = _resolve(_valid_request())
        summary = resolver.build_portable_source_body_verification_second_carrier_execution_summary(
            result
        )

        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(summary["second_carrier_execution_request_id"], "second_carrier_execution_test_001")
        self.assertEqual(summary["question"], resolver.CORE_QUESTION)
        self.assertEqual(summary["intent"], resolver.INTENT_RECORD)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)
        for key in TRUE_RECORDED_FIELDS:
            with self.subTest(summary_field=key):
                self.assertIs(summary.get(key), True)
        self.assertEqual(
            summary["selected_second_carrier_execution_boundary_outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_BOUNDARY_RECORDED",
        )
        self.assertEqual(summary["selected_second_carrier_execution_boundary_result_version"], "0.1.0")
        self.assertEqual(summary["selected_second_carrier_execution_boundary_failed_check_count"], 0)
        self.assertIs(summary["no_output_result_success_external_result_or_cross_carrier_evidence"], True)
        self.assertIs(summary["no_source_authority_currentness_final_completion_or_runtime"], True)
        self.assertIs(summary["no_deployment_public_release_or_follow_on"], True)
        self.assertIs(summary["v1_predecessor_failure_preserved"], True)
        self.assertIs(summary["v1_not_repaired_hidden_or_claimed_passed"], True)
        for key, value in summary["key_non_claims"].items():
            with self.subTest(key_non_claim=key):
                self.assertIs(value, False)

    def test_representative_blocking_behavior(self) -> None:
        block_cases: tuple[tuple[str, Any], ...] = (
            ("explicit block intent", {"second_carrier_execution_intent": resolver.INTENT_BLOCK}),
            ("missing request", None),
            ("non-mapping request", ["not", "mapping"]),
            ("unsupported intent", {"second_carrier_execution_intent": "UNSUPPORTED"}),
            ("unsupported scope", {"second_carrier_execution_scope": list(SUPPORTED_SCOPE) + ["UNSUPPORTED"]}),
            ("missing execution boundary basis", {"selected_second_carrier_execution_boundary_basis": _DELETE}),
            ("boundary not recorded", {"selected_second_carrier_execution_boundary_result_outcome": "NO"}),
            ("boundary failed checks", {"selected_second_carrier_execution_boundary_failed_check_count": 1}),
            ("boundary wrong version", {"selected_second_carrier_execution_boundary_result_version": "9.9.9"}),
            ("boundary no future step", {"selected_second_carrier_execution_boundary_declared_future_execution_step": False}),
            ("boundary already created execution", {"selected_second_carrier_execution_boundary_already_created_execution": True}),
            ("boundary already created execution artifact", {"selected_second_carrier_execution_boundary_already_created_execution_artifact": True}),
            ("boundary already created execution output", {"selected_second_carrier_execution_boundary_already_created_execution_output": True}),
            ("boundary already created output capture", {"selected_second_carrier_execution_boundary_already_created_second_carrier_output_capture": True}),
            ("boundary already created result", {"selected_second_carrier_execution_boundary_already_created_second_carrier_result": True}),
            ("boundary already created success", {"selected_second_carrier_execution_boundary_already_created_second_carrier_success": True}),
            ("boundary created external result", {"selected_second_carrier_execution_boundary_created_external_result": True}),
            ("boundary created cross-carrier evidence", {"selected_second_carrier_execution_boundary_created_cross_carrier_evidence": True}),
            ("boundary used hidden authority", {"selected_second_carrier_execution_boundary_used_hidden_repo_state_as_execution_authority": True}),
            ("boundary treated repo local as authority", {"selected_second_carrier_execution_boundary_treated_repo_local_availability_as_execution_authority": True}),
            ("boundary treated receiving carrier as authority", {"selected_second_carrier_execution_boundary_treated_receiving_carrier_as_authority": True}),
            ("boundary returned raw body", {"selected_second_carrier_execution_boundary_raw_full_prior_artifact_body_returned": True}),
            ("receipt basis missing", {"selected_second_carrier_receipt_basis": _DELETE}),
            ("receipt not recorded", {"selected_second_carrier_receipt_result_outcome": "NO"}),
            ("receipt failed checks", {"selected_second_carrier_receipt_failed_check_count": 1}),
            ("receipt not bounded", {"selected_second_carrier_receipt_bounded_receipt_recorded": False}),
            ("receipt treated as execution", {"selected_second_carrier_receipt_receipt_not_execution": False}),
            ("execution treated as output", {"second_carrier_execution_treated_as_output": True}),
            ("execution treated as output capture", {"second_carrier_execution_treated_as_output_capture": True}),
            ("execution treated as result", {"second_carrier_execution_treated_as_result": True}),
            ("execution treated as success", {"second_carrier_execution_treated_as_success": True}),
            ("execution treated as external result", {"second_carrier_execution_treated_as_external_result": True}),
            ("execution treated as cross-carrier evidence", {"second_carrier_execution_treated_as_cross_carrier_evidence": True}),
            ("execution treated as source transfer", {"second_carrier_execution_treated_as_source_transfer": True}),
            ("execution treated as source receipt", {"second_carrier_execution_treated_as_source_receipt": True}),
            ("execution treated as reception authorization", {"second_carrier_execution_treated_as_reception_authorization": True}),
            ("execution treated as source", {"second_carrier_execution_treated_as_source": True}),
            ("execution treated as authority", {"second_carrier_execution_treated_as_authority": True}),
            ("execution treated as currentness", {"second_carrier_execution_treated_as_currentness": True}),
            ("execution treated as final completion", {"second_carrier_execution_treated_as_final_completion": True}),
            ("execution treated as runtime", {"second_carrier_execution_treated_as_runtime": True}),
            ("execution treated as continuation", {"second_carrier_execution_treated_as_continuation": True}),
            ("execution treated as reusable permission", {"second_carrier_execution_treated_as_reusable_permission": True}),
            ("execution treated as follow-on", {"second_carrier_execution_treated_as_follow_on_work": True}),
            ("execution output created", {"execution_output_created": True}),
            ("output capture created", {"second_carrier_output_capture_created": True}),
            ("result created", {"second_carrier_result_created": True}),
            ("success created", {"second_carrier_success_created": True}),
            ("external result created", {"external_result_created": True}),
            ("cross-carrier evidence created", {"cross_carrier_evidence_created": True}),
            ("source transfer occurred", {"source_transfer_occurred": True}),
            ("source receipt occurred", {"source_receipt_occurred": True}),
            ("reception authorization created", {"reception_authorization_created": True}),
            ("source created", {"source_created": True}),
            ("authority created", {"authority_created": True}),
            ("currentness created", {"currentness_created": True}),
            ("final completion claimed", {"final_completion_claimed": True}),
            ("runtime hosting created", {"runtime_hosting_created": True}),
            ("deployment created", {"deployment_created": True}),
            ("public release created", {"public_release_created": True}),
            ("operation permission created", {"operation_permission_created": True}),
            ("continuation authorized", {"continuation_authorized": True}),
            ("reusable permission created", {"reusable_permission_created": True}),
            ("follow-on authorized", {"follow_on_work_authorized": True}),
            ("receiving carrier authority", {"receiving_carrier_treated_as_authority": True}),
            ("artifact existence authority", {"artifact_existence_treated_as_execution_authority": True}),
            ("artifact path currentness", {"artifact_path_treated_as_currentness": True}),
            ("repo local authority", {"repo_local_availability_treated_as_execution_authority": True}),
            ("hidden state content", {"hidden_repo_state_used_as_execution_content": True}),
            ("hidden state authority", {"hidden_repo_state_used_as_execution_authority": True}),
            ("not reference shaped", {"reference_shaped_input_posture": False}),
            ("raw prior body returned", {"raw_full_prior_artifact_body_returned": True}),
            ("v1 repaired", {"v1_repaired": True}),
            ("v1 hidden", {"v1_hidden": True}),
            ("v1 claimed passed", {"v1_claimed_passed": True}),
            ("lineage current artifact", {"command_report_lineage_treated_as_current_report_artifact": True}),
            ("lineage source", {"command_report_lineage_treated_as_source": True}),
            ("lineage authority", {"command_report_lineage_treated_as_authority": True}),
            ("lineage currentness", {"command_report_lineage_treated_as_currentness": True}),
            ("consumed request reopened", {"consumed_request_reopened": True}),
            ("authorization reused", {"authorization_token_reused": True}),
            ("full body emitted", {"full_prior_artifact_body_emitted_outside_bounded_execution": True}),
            ("artifacts mutated", {"prior_artifacts_mutated": True}),
            ("required non-claim missing", {"declared_non_claims": {key: False for key in REQUIRED_FALSE_NON_CLAIMS if key != "execution_output_created"}}),
            ("required non-claim flipped", {"declared_non_claims": {**{key: False for key in REQUIRED_FALSE_NON_CLAIMS}, "execution_output_created": True}}),
        )

        for name, override in block_cases:
            with self.subTest(block_case=name):
                if override is None:
                    result = _resolve(None)
                elif isinstance(override, list):
                    result = resolver.resolve_portable_source_body_verification_second_carrier_execution(override)  # type: ignore[arg-type]
                else:
                    result = _resolve(_valid_request(**override))
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertIsInstance(result.get("block"), MappingABC)
                self.assertTrue(result["block"].get("block_code"))
                self.assertIn(result["block"]["block_code"], resolver.BLOCK_CODES)
                self.assertPublicBlockCodes(result)
                self.assertNoDownstreamCreated(result)
                self.assertGeneratedBooleansAreBool(result)

    def test_path_and_write_behavior(self) -> None:
        request = _valid_request()
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            request_path = temp_root / "request.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")

            result = resolver.resolve_portable_source_body_verification_second_carrier_execution_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], RECORDED)
            metadata = result["portable_source_body_verification_second_carrier_execution_metadata"]
            self.assertEqual(
                metadata["portable_source_body_verification_second_carrier_execution_result_version"],
                "0.1.0",
            )
            self.assertEqual(
                metadata["resolver_module"],
                "resolve_portable_source_body_verification_second_carrier_execution",
            )

            malformed_path = temp_root / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            with self.assertRaises(resolver.PortableSourceBodyVerificationSecondCarrierExecutionError):
                resolver.resolve_portable_source_body_verification_second_carrier_execution_from_path(
                    malformed_path
                )

            array_path = temp_root / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolver.resolve_portable_source_body_verification_second_carrier_execution_from_path(
                array_path
            )
            self.assertEqual(array_result["outcome"], BLOCKED)
            self.assertPublicBlockCodes(array_result)

            with self.assertRaises(resolver.PortableSourceBodyVerificationSecondCarrierExecutionError):
                resolver.resolve_portable_source_body_verification_second_carrier_execution_from_path(
                    temp_root / "missing.json"
                )

            output_root = (
                temp_root
                / "artifacts"
                / "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_execution"
            )
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_portable_source_body_verification_second_carrier_execution_result(
                    result
                )
                second_path = resolver.write_portable_source_body_verification_second_carrier_execution_result(
                    result
                )

            self.assertTrue(first_path.parent.exists())
            self.assertTrue(str(first_path.parent).endswith(str(resolver.OUTPUT_ROOT)))
            self.assertNotEqual(first_path, second_path)
            self.assertEqual(json.loads(first_path.read_text(encoding="utf-8"))["outcome"], RECORDED)
            forbidden_roots = (
                "second_carrier_execution_boundary",
                "execution_output",
                "output_capture",
                "second_carrier_result",
                "second_carrier_success",
                "external_result",
                "cross_carrier",
                "runtime",
                "deployment",
                "public_release",
            )
            for forbidden in forbidden_roots:
                with self.subTest(forbidden_root=forbidden):
                    self.assertNotIn(forbidden, str(first_path.parent))

    def test_non_mutation(self) -> None:
        request = _valid_request()
        before = copy.deepcopy(request)
        selected_basis_before = {key: copy.deepcopy(request[key]) for key in SELECTED_BASIS_KEYS}
        posture_before = {key: copy.deepcopy(request[key]) for key in POSTURE_KEYS}
        scope_before = copy.deepcopy(request["second_carrier_execution_scope"])
        non_claims_before = copy.deepcopy(request["declared_non_claims"])

        result = _resolve(request)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(request, before)
        self.assertEqual({key: request[key] for key in SELECTED_BASIS_KEYS}, selected_basis_before)
        self.assertEqual({key: request[key] for key in POSTURE_KEYS}, posture_before)
        self.assertEqual(request["second_carrier_execution_scope"], scope_before)
        self.assertEqual(request["declared_non_claims"], non_claims_before)

    def test_raw_full_body_and_hidden_repo_state_containment(self) -> None:
        request = _valid_request()
        hostile_payload = {
            "raw_body": HOSTILE_RAW_VALUE,
            "raw_full_body": HOSTILE_RAW_VALUE,
            "full_body": HOSTILE_RAW_VALUE,
            "artifact_body": HOSTILE_RAW_VALUE,
            "raw_result_body": HOSTILE_RAW_VALUE,
            "raw_output_body": HOSTILE_RAW_VALUE,
            "execution_body": HOSTILE_RAW_VALUE,
            "execution_artifact_body": HOSTILE_RAW_VALUE,
            "execution_output_body": HOSTILE_RAW_VALUE,
            "second_carrier_output_capture_body": HOSTILE_RAW_VALUE,
            "second_carrier_result_body": HOSTILE_RAW_VALUE,
            "second_carrier_success_body": HOSTILE_RAW_VALUE,
            "external_result_body": HOSTILE_RAW_VALUE,
            "cross_carrier_evidence_body": HOSTILE_RAW_VALUE,
            "packet_body": HOSTILE_RAW_VALUE,
            "source_body": HOSTILE_RAW_VALUE,
            "authority_body": HOSTILE_RAW_VALUE,
            "hidden_repo_state": HOSTILE_RAW_VALUE,
            "current_working_tree": HOSTILE_RAW_VALUE,
            "local_cache": HOSTILE_RAW_VALUE,
            "repo_local_only_dependency": HOSTILE_RAW_VALUE,
            "carrier_possession": HOSTILE_RAW_VALUE,
            "copy_presence": HOSTILE_RAW_VALUE,
            "receiving_carrier": HOSTILE_RAW_VALUE,
            "receipt_artifact_presence": HOSTILE_RAW_VALUE,
            "execution_artifact_presence": HOSTILE_RAW_VALUE,
            "unlisted_file_dependency": HOSTILE_RAW_VALUE,
            "nested": [{"sentinel": RAW_SENTINEL}],
        }
        hostile_sections = (
            "selected_second_carrier_execution_boundary_basis",
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
        for key in hostile_sections:
            request[key].update(copy.deepcopy(hostile_payload))

        before = copy.deepcopy(request)
        result = _resolve(request)
        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assertPublicBlockCodes(result)
        self.assertNoRawSentinels(result)
        self.assertNoDownstreamCreated(result)
        self.assertIs(result["non_claims"]["hidden_repo_state_used_as_execution_content"], False)
        self.assertIs(result["non_claims"]["hidden_repo_state_used_as_execution_authority"], False)
        self.assertIs(result["non_claims"]["repo_local_availability_treated_as_execution_authority"], False)
        self.assertIs(result["non_claims"]["receiving_carrier_treated_as_authority"], False)
        self.assertIs(result["non_claims"]["artifact_existence_treated_as_execution_authority"], False)
        self.assertIs(result["non_claims"]["artifact_path_treated_as_currentness"], False)
        self.assertEqual(request, before)
        self.assertGeneratedBooleansAreBool(result)


if __name__ == "__main__":
    unittest.main()
