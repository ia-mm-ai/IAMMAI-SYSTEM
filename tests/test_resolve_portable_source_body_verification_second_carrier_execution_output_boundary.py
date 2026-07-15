"""Executable checks for second-carrier execution output-boundary posture only.

This suite is downstream of recorded second-carrier execution. It verifies that
the resolver records one future execution-output / second-carrier-output step
boundary only: execution output, output artifact, output capture, result,
success, external result, and cross-carrier evidence are not created, and
source/authority/currentness/runtime/final-completion/follow-on remain
unauthorized. Receiving carrier is not authority, hidden repo state is
excluded, repo-local availability is not output authority, selected basis stays
reference-shaped, the consumed request token remains closed, and authorization
token reuse remains blocked.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from collections.abc import Mapping as MappingABC
from pathlib import Path
from typing import Any, Mapping
from unittest.mock import patch


sys.dont_write_bytecode = True

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_portable_source_body_verification_second_carrier_execution_output_boundary as resolver


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
TRUE_RECORDED_FIELDS = tuple(resolver.ALLOWED_TRUE_RECORDED_FIELDS)
SELECTED_BASIS_KEYS = tuple(resolver.SELECTED_BASIS_KEYS)
POSTURE_KEYS = tuple(resolver.POSTURE_KEYS)

RAW_SENTINEL = "RAW_SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_BODY_MUST_NOT_RETURN"
HOSTILE_RAW_VALUE = (
    "HOSTILE_SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_FULL_BODY_VALUE_MUST_NOT_RETURN"
)
REDACTION_STRINGS = {
    "[bounded-redacted-raw-or-hidden-state]",
    "[bounded-reference-redacted-raw-or-hidden-state]",
    "[bounded-reference-omitted-raw-or-hidden-state]",
}

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_second_carrier_execution_output_boundary_metadata",
    "declared_second_carrier_execution_output_boundary_question",
    "selected_second_carrier_execution_basis",
    "selected_second_carrier_execution_terminal_summary_basis",
    "selected_second_carrier_execution_boundary_basis",
    "selected_second_carrier_receipt_basis",
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
    "second_carrier_execution_output_boundary_only_posture",
    "one_future_second_carrier_execution_output_step_posture",
    "second_carrier_execution_basis_preserved_posture",
    "execution_artifact_basis_preserved_posture",
    "execution_not_output_posture",
    "output_not_created_posture",
    "output_artifact_not_created_posture",
    "output_capture_not_created_posture",
    "second_carrier_result_not_created_posture",
    "second_carrier_success_not_created_posture",
    "external_result_not_created_posture",
    "cross_carrier_evidence_not_created_posture",
    "output_not_source_transfer_posture",
    "output_not_source_receipt_posture",
    "output_not_reception_authorization_posture",
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
    "repo_local_availability_not_output_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "second_carrier_execution_output_boundary_scope",
    "second_carrier_execution_output_boundary_checks",
    "second_carrier_execution_output_boundary_statement",
    "second_carrier_execution_output_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_second_carrier_execution_output_boundary_summary",
)

REPRESENTATIVE_BLOCK_CODES = (
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_QUESTION_UNDECLARED",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_INTENT_UNSUPPORTED",
    "SECOND_CARRIER_EXECUTION_BASIS_MISSING",
    "SECOND_CARRIER_EXECUTION_NOT_RECORDED",
    "SECOND_CARRIER_EXECUTION_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_EXECUTION_VERSION_NOT_0_1_0",
    "SECOND_CARRIER_EXECUTION_DID_NOT_RECORD_BOUNDED_EXECUTION",
    "SECOND_CARRIER_EXECUTION_ALREADY_CREATED_EXECUTION_OUTPUT",
    "SECOND_CARRIER_EXECUTION_ALREADY_CREATED_SECOND_CARRIER_OUTPUT_CAPTURE",
    "SECOND_CARRIER_EXECUTION_ALREADY_CREATED_SECOND_CARRIER_RESULT",
    "SECOND_CARRIER_EXECUTION_ALREADY_CREATED_SECOND_CARRIER_SUCCESS",
    "SECOND_CARRIER_EXECUTION_CREATED_EXTERNAL_RESULT",
    "SECOND_CARRIER_EXECUTION_CREATED_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXECUTION_TREATED_EXECUTION_AS_OUTPUT",
    "SECOND_CARRIER_EXECUTION_TREATED_EXECUTION_AS_OUTPUT_CAPTURE",
    "SECOND_CARRIER_EXECUTION_TREATED_EXECUTION_AS_RESULT",
    "SECOND_CARRIER_EXECUTION_TREATED_EXECUTION_AS_SUCCESS",
    "SECOND_CARRIER_EXECUTION_TREATED_EXECUTION_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_EXECUTION_TREATED_EXECUTION_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXECUTION_USED_HIDDEN_REPO_STATE_AS_OUTPUT_AUTHORITY",
    "SECOND_CARRIER_EXECUTION_TREATED_REPO_LOCAL_AVAILABILITY_AS_OUTPUT_AUTHORITY",
    "SECOND_CARRIER_EXECUTION_TREATED_RECEIVING_CARRIER_AS_AUTHORITY",
    "SECOND_CARRIER_EXECUTION_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY_OUTSIDE_BOUNDED_EXECUTION",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_OUTPUT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_OUTPUT_ARTIFACT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_OUTPUT_CAPTURE",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_RESULT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_SUCCESS",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_SOURCE",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_AUTHORITY",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_CURRENTNESS",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_FINAL_COMPLETION",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_RUNTIME",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_CONTINUATION",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
    "EXECUTION_OUTPUT_CREATED",
    "OUTPUT_ARTIFACT_CREATED",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_OUTPUT_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_OUTPUT_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_OUTPUT_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_OUTPUT_AUTHORITY",
    "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_OUTPUT_BOUNDARY",
    "ARTIFACTS_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_SCOPE",
)

NON_MEANING_FALSE_FIELDS = (
    "execution_output_exists",
    "output_artifact_exists",
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
    "output_boundary_became_output",
    "output_boundary_became_capture",
    "output_boundary_became_result",
    "output_boundary_became_success",
    "output_boundary_became_external_result",
    "output_boundary_became_cross_carrier_proof",
    "output_boundary_became_source_transfer",
    "output_boundary_became_source_receipt",
    "output_boundary_became_reception_authorization",
    "output_boundary_became_source",
    "output_boundary_became_authority",
    "output_boundary_became_currentness",
    "execution_became_output",
    "execution_artifact_became_output",
    "receiving_carrier_became_authority",
    "transferred_packet_became_source",
    "transferred_packet_became_authority",
    "transferred_packet_became_currentness",
    "artifact_existence_became_output_authority",
    "artifact_path_became_currentness",
    "repo_local_availability_became_output_authority",
    "hidden_repo_state_became_output_authority",
    "v1_packet_emission_boundary_repaired",
    "v1_packet_emission_boundary_hidden",
    "v1_packet_emission_boundary_erased",
    "v1_packet_emission_boundary_claimed_passed",
)

DOWNSTREAM_FALSE_NON_CLAIMS = (
    "execution_output_created",
    "output_artifact_created",
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


class _DeleteMarker:
    pass


_DELETE = _DeleteMarker()


def _json_text(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=True)


def _valid_request(**overrides: Any) -> dict[str, Any]:
    request = (
        resolver.build_declared_portable_source_body_verification_second_carrier_execution_output_boundary_request(
            second_carrier_execution_output_boundary_request_id=(
                "second_carrier_execution_output_boundary_test_001"
            )
        )
    )
    request["second_carrier_execution_output_boundary_scope"] = list(SUPPORTED_SCOPE)
    request["declared_non_claims"] = {
        key: False for key in REQUIRED_FALSE_NON_CLAIMS
    }

    request["selected_second_carrier_execution_basis"].update(
        {
            "outcome": "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_RECORDED",
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "bounded_second_carrier_execution_recorded": True,
            "execution_output_not_created": True,
            "execution_not_output": True,
            "execution_not_output_capture": True,
            "execution_not_result": True,
            "execution_not_success": True,
            "execution_not_external_result": True,
            "execution_not_cross_carrier_evidence": True,
            "second_carrier_output_capture_not_created": True,
            "second_carrier_result_not_created": True,
            "second_carrier_success_not_created": True,
            "external_result_not_created": True,
            "cross_carrier_evidence_not_created": True,
            "receiving_carrier_not_authority": True,
            "hidden_repo_state_excluded": True,
            "hidden_repo_state_not_used_as_output_authority": True,
            "repo_local_availability_not_output_authority": True,
            "raw_full_prior_artifact_body_not_returned": True,
        }
    )

    basis_outcomes = {
        "selected_second_carrier_execution_terminal_summary_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_RECORDED"
        ),
        "selected_second_carrier_execution_boundary_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_BOUNDARY_RECORDED"
        ),
        "selected_second_carrier_receipt_basis": (
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
            "command_report_lineage_remains_lineage_only": True,
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
                "predecessor_failure_evidence_visible": True,
                "predecessor_failure_evidence_unrepaired": True,
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


def _with_non_claim(non_claim: str, value: bool = True) -> dict[str, Any]:
    non_claims = {key: False for key in REQUIRED_FALSE_NON_CLAIMS}
    non_claims[non_claim] = value
    return {"declared_non_claims": non_claims}


def _resolve(request: Mapping[str, Any] | None) -> dict[str, Any]:
    return (
        resolver.resolve_portable_source_body_verification_second_carrier_execution_output_boundary(
            declared_second_carrier_execution_output_boundary_request=request
        )
    )


class SecondCarrierExecutionOutputBoundaryResolverTests(unittest.TestCase):
    def assertPublicBlockCodes(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if isinstance(block, MappingABC):
            code = block.get("block_code")
            if code:
                self.assertIn(code, resolver.BLOCK_CODES)
        for check in result.get("second_carrier_execution_output_boundary_checks", []):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assertGeneratedBooleansAreBool(self, result: Mapping[str, Any]) -> None:
        for section in (
            "second_carrier_execution_output_boundary_statement",
            "second_carrier_execution_output_boundary_non_meaning",
            "non_claims",
        ):
            for key, value in result.get(section, {}).items():
                with self.subTest(section=section, key=key):
                    self.assertIs(type(value), bool)
                    self.assertNotIn(value, REDACTION_STRINGS)
        for key in POSTURE_KEYS:
            posture = result.get(key, {})
            for posture_key, value in posture.items():
                if isinstance(value, bool):
                    with self.subTest(section=key, key=posture_key):
                        self.assertIs(type(value), bool)
                        self.assertNotIn(value, REDACTION_STRINGS)

    def assertNoRawSentinels(self, result: Mapping[str, Any]) -> None:
        serialized = _json_text(result)
        self.assertNotIn(RAW_SENTINEL, serialized)
        self.assertNotIn(HOSTILE_RAW_VALUE, serialized)
        self.assertNotIn(
            "RAW_SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_BODY_MUST_NOT_RETURN",
            serialized,
        )

    def assertNoDownstreamCreated(self, result: Mapping[str, Any]) -> None:
        statement = result.get("second_carrier_execution_output_boundary_statement", {})
        non_claims = result.get("non_claims", {})
        for key in DOWNSTREAM_FALSE_NON_CLAIMS:
            with self.subTest(non_claim=key):
                self.assertIs(statement.get(key, non_claims.get(key)), False)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_portable_source_body_verification_second_carrier_execution_output_boundary",
            "resolve_portable_source_body_verification_second_carrier_execution_output_boundary_from_path",
            "write_portable_source_body_verification_second_carrier_execution_output_boundary_result",
            "build_portable_source_body_verification_second_carrier_execution_output_boundary_summary",
            "build_declared_portable_source_body_verification_second_carrier_execution_output_boundary_request",
        ):
            self.assertTrue(callable(getattr(resolver, name, None)), name)

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "RESULT_VERSION",
            "OUTPUT_ROOT",
            "SUPPORTED_SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_portable_source_body_verification_"
                "second_carrier_execution_output_boundary"
            )
        )
        for code in REPRESENTATIVE_BLOCK_CODES:
            with self.subTest(block_code=code):
                self.assertIn(code, resolver.BLOCK_CODES)

    def test_successful_second_carrier_execution_output_boundary_recorded_result(self) -> None:
        request = _valid_request()
        result = _resolve(request)

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], RECORDED)
        summary = result[
            "portable_source_body_verification_second_carrier_execution_output_boundary_summary"
        ]
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertIsNone(result["block"])
        self.assertPublicBlockCodes(result)

        for section in TOP_LEVEL_SECTIONS:
            with self.subTest(section=section):
                self.assertIn(section, result)

        metadata = result[
            "portable_source_body_verification_second_carrier_execution_output_boundary_metadata"
        ]
        self.assertEqual(
            metadata[
                "portable_source_body_verification_second_carrier_execution_output_boundary_result_version"
            ],
            "0.1.0",
        )
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_portable_source_body_verification_second_carrier_execution_output_boundary",
        )
        self.assertEqual(
            metadata["second_carrier_execution_output_boundary_request_id"],
            "second_carrier_execution_output_boundary_test_001",
        )

        statement = result["second_carrier_execution_output_boundary_statement"]
        for key in TRUE_RECORDED_FIELDS:
            with self.subTest(statement=key):
                self.assertIs(statement.get(key), True)

        non_claims = result["non_claims"]
        for key in REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(non_claim=key):
                self.assertIs(non_claims.get(key), False)

        non_meaning = result["second_carrier_execution_output_boundary_non_meaning"]
        for key in NON_MEANING_FALSE_FIELDS:
            with self.subTest(non_meaning=key):
                self.assertIs(non_meaning.get(key), False)

        self.assertGeneratedBooleansAreBool(result)
        self.assertNoRawSentinels(result)
        self.assertNoDownstreamCreated(result)

    def test_summary_helper_preserves_output_boundary_posture(self) -> None:
        result = _resolve(_valid_request())
        summary = (
            resolver.build_portable_source_body_verification_second_carrier_execution_output_boundary_summary(
                result
            )
        )

        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(
            summary["second_carrier_execution_output_boundary_request_id"],
            "second_carrier_execution_output_boundary_test_001",
        )
        self.assertEqual(summary["question"], resolver.CORE_QUESTION)
        self.assertEqual(summary["intent"], resolver.INTENT_RECORD)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)
        for key in TRUE_RECORDED_FIELDS:
            with self.subTest(summary_field=key):
                self.assertIs(summary.get(key), True)
        self.assertEqual(
            summary["selected_second_carrier_execution_outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_RECORDED",
        )
        self.assertEqual(summary["selected_second_carrier_execution_version"], "0.1.0")
        self.assertEqual(summary["selected_second_carrier_execution_failed_check_count"], 0)
        self.assertIs(
            summary[
                "no_output_output_capture_result_success_external_result_cross_carrier_evidence"
            ],
            True,
        )
        self.assertIs(
            summary["no_source_authority_currentness_final_completion_runtime"], True
        )
        self.assertIs(summary["no_deployment_public_release_follow_on"], True)
        self.assertIs(summary["v1_predecessor_failure_preserved"], True)
        self.assertIs(summary["v1_not_repaired_hidden_claimed_passed"], True)
        for key, value in summary["key_non_claims"].items():
            with self.subTest(key_non_claim=key):
                self.assertIs(value, False)

    def test_representative_blocking_behavior(self) -> None:
        block_cases: tuple[tuple[str, Any], ...] = (
            ("explicit block intent", {"second_carrier_execution_output_boundary_intent": resolver.INTENT_BLOCK}),
            ("missing request", None),
            ("non-mapping request", ["not", "mapping"]),
            ("unsupported intent", {"second_carrier_execution_output_boundary_intent": "UNSUPPORTED"}),
            ("unsupported scope", {"second_carrier_execution_output_boundary_scope": list(SUPPORTED_SCOPE) + ["UNSUPPORTED"]}),
            ("missing execution basis", {"selected_second_carrier_execution_basis": _DELETE}),
            ("execution not recorded", {"selected_second_carrier_execution_result_outcome": "NO"}),
            ("execution failed checks", {"selected_second_carrier_execution_failed_check_count": 1}),
            ("execution wrong version", {"selected_second_carrier_execution_result_version": "9.9.9"}),
            ("execution did not record bounded execution", {"selected_second_carrier_execution_bounded_execution_recorded": False}),
            ("execution already created output", {"selected_second_carrier_execution_execution_output_created": True}),
            ("execution already created output capture", {"selected_second_carrier_execution_created_second_carrier_output_capture": True}),
            ("execution already created result", {"selected_second_carrier_execution_created_second_carrier_result": True}),
            ("execution already created success", {"selected_second_carrier_execution_created_second_carrier_success": True}),
            ("execution created external result", {"selected_second_carrier_execution_created_external_result": True}),
            ("execution created cross-carrier evidence", {"selected_second_carrier_execution_created_cross_carrier_evidence": True}),
            ("execution treated as output", {"selected_second_carrier_execution_treated_execution_as_output": True}),
            ("execution treated as output capture", {"selected_second_carrier_execution_treated_execution_as_output_capture": True}),
            ("execution treated as result", {"selected_second_carrier_execution_treated_execution_as_result": True}),
            ("execution treated as success", {"selected_second_carrier_execution_treated_execution_as_success": True}),
            ("execution treated as external result", {"selected_second_carrier_execution_treated_execution_as_external_result": True}),
            ("execution treated as cross-carrier evidence", {"selected_second_carrier_execution_treated_execution_as_cross_carrier_evidence": True}),
            ("execution used hidden output authority", {"selected_second_carrier_execution_used_hidden_repo_state_as_output_authority": True}),
            ("execution treated repo local as output authority", {"selected_second_carrier_execution_treated_repo_local_availability_as_output_authority": True}),
            ("execution treated receiving carrier as authority", {"selected_second_carrier_execution_treated_receiving_carrier_as_authority": True}),
            ("execution returned raw prior body", {"selected_second_carrier_execution_raw_full_prior_artifact_body_returned_outside_bounded_execution": True}),
            ("output boundary treated as output", _with_non_claim("second_carrier_execution_output_boundary_treated_as_output")),
            ("output boundary treated as output artifact", _with_non_claim("second_carrier_execution_output_boundary_treated_as_output_artifact")),
            ("output boundary treated as output capture", _with_non_claim("second_carrier_execution_output_boundary_treated_as_output_capture")),
            ("output boundary treated as result", _with_non_claim("second_carrier_execution_output_boundary_treated_as_result")),
            ("output boundary treated as success", _with_non_claim("second_carrier_execution_output_boundary_treated_as_success")),
            ("output boundary treated as external result", _with_non_claim("second_carrier_execution_output_boundary_treated_as_external_result")),
            ("output boundary treated as cross-carrier evidence", _with_non_claim("second_carrier_execution_output_boundary_treated_as_cross_carrier_evidence")),
            ("output boundary treated as source transfer", _with_non_claim("second_carrier_execution_output_boundary_treated_as_source_transfer")),
            ("output boundary treated as source receipt", _with_non_claim("second_carrier_execution_output_boundary_treated_as_source_receipt")),
            ("output boundary treated as reception", _with_non_claim("second_carrier_execution_output_boundary_treated_as_reception_authorization")),
            ("output boundary treated as source", _with_non_claim("second_carrier_execution_output_boundary_treated_as_source")),
            ("output boundary treated as authority", _with_non_claim("second_carrier_execution_output_boundary_treated_as_authority")),
            ("output boundary treated as currentness", _with_non_claim("second_carrier_execution_output_boundary_treated_as_currentness")),
            ("output boundary treated as final completion", _with_non_claim("second_carrier_execution_output_boundary_treated_as_final_completion")),
            ("output boundary treated as runtime", _with_non_claim("second_carrier_execution_output_boundary_treated_as_runtime")),
            ("output boundary treated as continuation", _with_non_claim("second_carrier_execution_output_boundary_treated_as_continuation")),
            ("output boundary treated as reusable", _with_non_claim("second_carrier_execution_output_boundary_treated_as_reusable_permission")),
            ("output boundary treated as follow-on", _with_non_claim("second_carrier_execution_output_boundary_treated_as_follow_on_work")),
            ("execution output created", _with_non_claim("execution_output_created")),
            ("output artifact created", _with_non_claim("output_artifact_created")),
            ("output capture created", _with_non_claim("second_carrier_output_capture_created")),
            ("result created", _with_non_claim("second_carrier_result_created")),
            ("success created", _with_non_claim("second_carrier_success_created")),
            ("external result created", _with_non_claim("external_result_created")),
            ("cross-carrier evidence created", _with_non_claim("cross_carrier_evidence_created")),
            ("source transfer occurred", _with_non_claim("source_transfer_occurred")),
            ("source receipt occurred", _with_non_claim("source_receipt_occurred")),
            ("reception authorization created", _with_non_claim("reception_authorization_created")),
            ("source created", _with_non_claim("source_created")),
            ("authority created", _with_non_claim("authority_created")),
            ("currentness created", _with_non_claim("currentness_created")),
            ("final completion claimed", _with_non_claim("final_completion_claimed")),
            ("runtime hosting created", _with_non_claim("runtime_hosting_created")),
            ("deployment created", _with_non_claim("deployment_created")),
            ("public release created", _with_non_claim("public_release_created")),
            ("operation permission created", _with_non_claim("operation_permission_created")),
            ("continuation authorized", _with_non_claim("continuation_authorized")),
            ("reusable permission created", _with_non_claim("reusable_permission_created")),
            ("follow-on authorized", _with_non_claim("follow_on_work_authorized")),
            ("receiving carrier authority", _with_non_claim("receiving_carrier_treated_as_authority")),
            ("artifact existence authority", _with_non_claim("artifact_existence_treated_as_output_authority")),
            ("artifact path currentness", _with_non_claim("artifact_path_treated_as_currentness")),
            ("repo local authority", _with_non_claim("repo_local_availability_treated_as_output_authority")),
            ("hidden state content", _with_non_claim("hidden_repo_state_used_as_output_content")),
            ("hidden state authority", _with_non_claim("hidden_repo_state_used_as_output_authority")),
            ("not reference shaped", {"reference_shaped_input_posture": False}),
            ("raw prior body returned", _with_non_claim("raw_full_prior_artifact_body_returned")),
            ("v1 repaired", _with_non_claim("v1_repaired")),
            ("v1 hidden", _with_non_claim("v1_hidden")),
            ("v1 claimed passed", _with_non_claim("v1_claimed_passed")),
            ("lineage current artifact", {"command_report_lineage_treated_as_current_report_artifact": True}),
            ("lineage source", {"command_report_lineage_treated_as_source": True}),
            ("lineage authority", {"command_report_lineage_treated_as_authority": True}),
            ("lineage currentness", {"command_report_lineage_treated_as_currentness": True}),
            ("consumed request reopened", _with_non_claim("consumed_request_reopened")),
            ("authorization reused", _with_non_claim("authorization_token_reused")),
            ("full body emitted", {"full_prior_artifact_body_emitted_outside_bounded_output_boundary": True}),
            ("artifacts mutated", _with_non_claim("prior_artifacts_mutated")),
            ("required non-claim missing", {"declared_non_claims": {key: False for key in REQUIRED_FALSE_NON_CLAIMS if key != "execution_output_created"}}),
            ("required non-claim flipped", _with_non_claim("execution_output_created")),
        )

        for name, override in block_cases:
            with self.subTest(block_case=name):
                if override is None:
                    result = _resolve(None)
                elif isinstance(override, list):
                    result = resolver.resolve_portable_source_body_verification_second_carrier_execution_output_boundary(override)  # type: ignore[arg-type]
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

            result = (
                resolver.resolve_portable_source_body_verification_second_carrier_execution_output_boundary_from_path(
                    request_path
                )
            )
            self.assertEqual(result["outcome"], RECORDED)
            metadata = result[
                "portable_source_body_verification_second_carrier_execution_output_boundary_metadata"
            ]
            self.assertEqual(
                metadata[
                    "portable_source_body_verification_second_carrier_execution_output_boundary_result_version"
                ],
                "0.1.0",
            )
            self.assertEqual(
                metadata["resolver_module"],
                "resolve_portable_source_body_verification_second_carrier_execution_output_boundary",
            )

            malformed_path = temp_root / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            with self.assertRaises(
                resolver.PortableSourceBodyVerificationSecondCarrierExecutionOutputBoundaryError
            ):
                resolver.resolve_portable_source_body_verification_second_carrier_execution_output_boundary_from_path(
                    malformed_path
                )

            array_path = temp_root / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = (
                resolver.resolve_portable_source_body_verification_second_carrier_execution_output_boundary_from_path(
                    array_path
                )
            )
            self.assertEqual(array_result["outcome"], BLOCKED)
            self.assertPublicBlockCodes(array_result)

            with self.assertRaises(
                resolver.PortableSourceBodyVerificationSecondCarrierExecutionOutputBoundaryError
            ):
                resolver.resolve_portable_source_body_verification_second_carrier_execution_output_boundary_from_path(
                    temp_root / "missing.json"
                )

            output_root = (
                temp_root
                / "artifacts"
                / "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_execution_output_boundary"
            )
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_portable_source_body_verification_second_carrier_execution_output_boundary_result(
                    result
                )
                second_path = resolver.write_portable_source_body_verification_second_carrier_execution_output_boundary_result(
                    result
                )

            self.assertTrue(first_path.parent.exists())
            self.assertTrue(str(first_path.parent).endswith(str(resolver.OUTPUT_ROOT)))
            self.assertNotEqual(first_path, second_path)
            self.assertEqual(
                json.loads(first_path.read_text(encoding="utf-8"))["outcome"],
                RECORDED,
            )
            self.assertTrue(
                str(first_path.parent).endswith(
                    "artifacts/"
                    "integrity_host_v0_min_coexistence_portable_source_body_verification_"
                    "second_carrier_execution_output_boundary"
                )
            )
            forbidden_root_suffixes = (
                "second_carrier_execution_output",
                "second_carrier_execution",
                "output_capture",
                "second_carrier_result",
                "second_carrier_success",
                "external_result",
                "cross_carrier",
                "runtime",
                "deployment",
                "public_release",
            )
            for forbidden in forbidden_root_suffixes:
                with self.subTest(forbidden_root=forbidden):
                    self.assertFalse(first_path.parent.name.endswith(forbidden))

    def test_non_mutation(self) -> None:
        request = _valid_request()
        before = copy.deepcopy(request)
        selected_basis_before = {key: copy.deepcopy(request[key]) for key in SELECTED_BASIS_KEYS}
        posture_before = {key: copy.deepcopy(request[key]) for key in POSTURE_KEYS}
        scope_before = copy.deepcopy(request["second_carrier_execution_output_boundary_scope"])
        non_claims_before = copy.deepcopy(request["declared_non_claims"])

        result = _resolve(request)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(request, before)
        self.assertEqual({key: request[key] for key in SELECTED_BASIS_KEYS}, selected_basis_before)
        self.assertEqual({key: request[key] for key in POSTURE_KEYS}, posture_before)
        self.assertEqual(request["second_carrier_execution_output_boundary_scope"], scope_before)
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
            "output_body": HOSTILE_RAW_VALUE,
            "output_artifact_body": HOSTILE_RAW_VALUE,
            "second_carrier_output_body": HOSTILE_RAW_VALUE,
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
            "output_path_possibility": HOSTILE_RAW_VALUE,
            "unlisted_file_dependency": HOSTILE_RAW_VALUE,
            "nested": [{"sentinel": RAW_SENTINEL}],
        }
        hostile_sections = (
            "selected_second_carrier_execution_basis",
            "selected_second_carrier_execution_boundary_basis",
            "selected_second_carrier_receipt_basis",
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
        self.assertIs(result["non_claims"]["hidden_repo_state_used_as_output_content"], False)
        self.assertIs(result["non_claims"]["hidden_repo_state_used_as_output_authority"], False)
        self.assertIs(result["non_claims"]["repo_local_availability_treated_as_output_authority"], False)
        self.assertIs(result["non_claims"]["receiving_carrier_treated_as_authority"], False)
        self.assertIs(result["non_claims"]["artifact_existence_treated_as_output_authority"], False)
        self.assertIs(result["non_claims"]["artifact_path_treated_as_currentness"], False)
        self.assertEqual(request, before)
        self.assertGeneratedBooleansAreBool(result)


if __name__ == "__main__":
    unittest.main()
