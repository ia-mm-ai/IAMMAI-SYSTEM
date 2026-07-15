"""Tests for portable source-body verification packet boundary only.

This suite is downstream of local command success. It verifies that the packet
boundary resolver records one future packet-step boundary only: no packet
exists, no packet is emitted or transferred, no second carrier has received or
executed anything, no external result or cross-carrier evidence exists, command
success remains local command-success posture only, hidden repo state is not
packet authority, and source/authority/currentness/final completion/runtime/
follow-on work remain unauthorized.
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

import resolve_portable_source_body_verification_packet_boundary as resolver


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_PACKET_BOUNDARY_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
EXTRA_FALSE_NON_CLAIMS = tuple(getattr(resolver, "EXTRA_FALSE_NON_CLAIMS", ()))

RAW_SENTINEL = "RAW_PACKET_BOUNDARY_BODY_MUST_NOT_RETURN"
HOSTILE_RAW_VALUE = "HOSTILE_PACKET_BOUNDARY_FULL_BODY_VALUE_MUST_NOT_RETURN"

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_packet_boundary_metadata",
    "declared_packet_boundary_question",
    "selected_command_success_basis",
    "selected_command_success_terminal_summary_basis",
    "selected_command_success_spec_basis",
    "selected_command_success_boundary_v3_basis",
    "selected_command_result_v2_basis",
    "selected_output_capture_v2_basis",
    "selected_command_output_report_artifact_basis",
    "selected_command_execution_basis",
    "selected_command_report_lineage_basis",
    "selected_predecessor_failure_basis",
    "packet_boundary_only_posture",
    "one_future_packet_step_posture",
    "local_command_success_basis_preserved_posture",
    "command_success_not_packet_emission_posture",
    "packet_not_created_posture",
    "packet_not_emitted_posture",
    "packet_transfer_not_authorized_posture",
    "second_carrier_execution_not_authorized_posture",
    "second_carrier_receipt_not_created_posture",
    "cross_carrier_evidence_not_created_posture",
    "source_not_created_posture",
    "authority_not_created_posture",
    "currentness_not_created_posture",
    "final_completion_not_created_posture",
    "runtime_not_created_posture",
    "continuation_not_authorized_posture",
    "reusable_permission_not_created_posture",
    "follow_on_work_not_authorized_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "hidden_repo_state_not_used_as_packet_authority_posture",
    "packet_boundary_scope",
    "packet_boundary_checks",
    "packet_boundary_statement",
    "packet_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_packet_boundary_summary",
)

TRUE_RECORDED_FIELDS = (
    "packet_boundary_recorded",
    "one_future_packet_step_declared",
    "local_command_success_basis_preserved",
    "command_success_not_packet_emission",
    "packet_not_created",
    "packet_not_emitted",
    "packet_transfer_not_authorized",
    "second_carrier_execution_not_authorized",
    "second_carrier_receipt_not_created",
    "cross_carrier_evidence_not_created",
    "source_not_created",
    "authority_not_created",
    "currentness_not_created",
    "final_completion_not_created",
    "runtime_not_created",
    "continuation_not_authorized",
    "reusable_permission_not_created",
    "follow_on_work_not_authorized",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "hidden_repo_state_not_used_as_packet_authority",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
)

REPRESENTATIVE_BLOCK_CODES = (
    "PACKET_BOUNDARY_QUESTION_UNDECLARED",
    "PACKET_BOUNDARY_INTENT_UNSUPPORTED",
    "COMMAND_SUCCESS_BASIS_MISSING",
    "COMMAND_SUCCESS_NOT_RECORDED",
    "COMMAND_SUCCESS_FAILED_CHECKS_PRESENT",
    "COMMAND_SUCCESS_VERSION_NOT_0_1_0",
    "COMMAND_SUCCESS_TREATED_AS_PACKET_EMISSION",
    "COMMAND_SUCCESS_AUTHORIZED_PACKET_CREATION",
    "COMMAND_SUCCESS_AUTHORIZED_PACKET_EMISSION",
    "COMMAND_SUCCESS_AUTHORIZED_PACKET_TRANSFER",
    "COMMAND_SUCCESS_AUTHORIZED_SECOND_CARRIER_EXECUTION",
    "COMMAND_SUCCESS_AUTHORIZED_CROSS_CARRIER_EVIDENCE_REVIEW",
    "PACKET_ALREADY_CREATED",
    "PACKET_ALREADY_EMITTED",
    "PACKET_ALREADY_TRANSFERRED",
    "SECOND_CARRIER_EXECUTION_ALREADY_CREATED",
    "SECOND_CARRIER_RECEIPT_ALREADY_CREATED",
    "EXTERNAL_RESULT_ALREADY_CREATED",
    "CROSS_CARRIER_EVIDENCE_ALREADY_CREATED",
    "SOURCE_BODY_PACKET_ALREADY_CREATED",
    "MANIFEST_ALREADY_CREATED",
    "CHECKSUM_ALREADY_CREATED",
    "SIGNATURE_ALREADY_CREATED",
    "REPRODUCIBLE_ENVIRONMENT_ALREADY_DECLARED",
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
    "PACKET_TREATED_AS_SOURCE",
    "PACKET_TREATED_AS_AUTHORITY",
    "PACKET_TREATED_AS_CURRENTNESS",
    "PACKET_TREATED_AS_FINAL_COMPLETION",
    "PACKET_TREATED_AS_RUNTIME",
    "PACKET_TREATED_AS_CROSS_CARRIER_PROOF",
    "ARTIFACT_EXISTENCE_TREATED_AS_PACKET_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "HIDDEN_REPO_STATE_USED_AS_PACKET_AUTHORITY",
    "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED",
    "ARTIFACTS_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_PACKET_BOUNDARY_SCOPE",
)


def _json_text(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=True)


def _false_non_claims() -> dict[str, bool]:
    non_claims = {key: False for key in REQUIRED_FALSE_NON_CLAIMS}
    non_claims.update({key: False for key in EXTRA_FALSE_NON_CLAIMS})
    return non_claims


def _request(**overrides: Any) -> dict[str, Any]:
    request = resolver.build_declared_portable_source_body_verification_packet_boundary_request(
        packet_boundary_request_id="packet_boundary_test_request_001"
    )
    request["packet_boundary_scope"] = list(SUPPORTED_SCOPE)
    request["declared_non_claims"] = _false_non_claims()
    request["selected_command_success_basis"].update(
        {
            "outcome": "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_RECORDED",
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "command_success_recorded": True,
            "bounded_command_success_recorded": True,
            "command_success_boundary_v3_basis_preserved": True,
            "command_result_v2_basis_preserved": True,
            "bounded_command_result_preserved": True,
            "output_capture_v2_basis_preserved": True,
            "command_output_report_artifact_basis_preserved": True,
            "execution_trace_audit_only_preserved": True,
            "command_success_treated_as_packet_emission": False,
            "command_success_treated_as_source": False,
            "command_success_treated_as_authority": False,
            "command_success_treated_as_currentness": False,
            "command_success_treated_as_final_completion": False,
            "command_success_treated_as_cross_carrier_proof": False,
            "command_success_authorized_packet_creation": False,
            "command_success_authorized_packet_emission": False,
            "command_success_authorized_packet_transfer": False,
            "command_success_authorized_second_carrier_execution": False,
            "command_success_authorized_cross_carrier_evidence_review": False,
            "source_not_created": True,
            "authority_not_created": True,
            "currentness_not_created": True,
            "final_completion_not_created": True,
            "runtime_not_created": True,
            "continuation_not_authorized": True,
            "reusable_permission_not_created": True,
            "follow_on_work_not_authorized": True,
        }
    )
    request["selected_command_success_terminal_summary_basis"].update(
        {
            "terminal_summary_readability_basis_only": True,
            "local_command_success_not_packet_emission": True,
            "local_command_success_not_cross_carrier_proof": True,
        }
    )
    request["selected_command_success_boundary_v3_basis"].update(
        {
            "outcome": "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_BOUNDARY_RECORDED",
            "result_version": "0.3.0",
            "failed_check_count": 0,
            "boundary_basis_only": True,
        }
    )
    request["selected_command_result_v2_basis"].update(
        {
            "outcome": "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_RECORDED",
            "result_version": "0.2.0",
            "failed_check_count": 0,
            "command_result_v2_remains_command_result_posture_only": True,
        }
    )
    request["selected_output_capture_v2_basis"].update(
        {
            "outcome": "PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_RECORDED",
            "result_version": "0.2.0",
            "failed_check_count": 0,
            "output_capture_v2_remains_output_capture_posture_only": True,
        }
    )
    request["selected_command_output_report_artifact_basis"].update(
        {
            "outcome": (
                "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_REPORT_ARTIFACT_RECORDED"
            ),
            "failed_check_count": 0,
            "command_output_report_artifact_remains_artifact_posture_only": True,
        }
    )
    request["selected_command_execution_basis"].update(
        {
            "outcome": (
                "PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_RECORDED"
            ),
            "failed_check_count": 0,
            "execution_trace_audit_only": True,
            "execution_trace_audit_only_preserved": True,
        }
    )
    request["selected_command_report_lineage_basis"].update(
        {
            "lineage_only": True,
            "command_report_lineage_treated_as_current_report_artifact": False,
            "command_report_lineage_treated_as_command_result_authority": False,
            "command_report_lineage_treated_as_command_success": False,
            "command_report_lineage_treated_as_source": False,
            "command_report_lineage_treated_as_authority": False,
            "command_report_lineage_treated_as_currentness": False,
        }
    )
    request["selected_predecessor_failure_basis"].update(
        {
            "predecessor_failures_visible": True,
            "predecessor_failures_repaired": False,
            "predecessor_failures_hidden": False,
            "predecessor_failures_claimed_passed": False,
        }
    )
    request.update(overrides)
    return request


def _mutated(mutator: Callable[[dict[str, Any]], None]) -> dict[str, Any]:
    request = _request()
    mutator(request)
    return request


def _codes(result: Mapping[str, Any]) -> set[str]:
    codes: set[str] = set()
    block = result.get("block") or {}
    if isinstance(block, Mapping) and block.get("block_code"):
        codes.add(str(block["block_code"]))
    for check in result.get("packet_boundary_checks", []):
        if isinstance(check, Mapping):
            for key in ("block_code", "failure_code"):
                if check.get(key):
                    codes.add(str(check[key]))
    return codes


class PacketBoundaryResolverTests(unittest.TestCase):
    def assert_public_block_codes(self, result: Mapping[str, Any]) -> None:
        block = result.get("block") or {}
        if isinstance(block, Mapping) and block.get("block_code") is not None:
            self.assertIn(block["block_code"], resolver.BLOCK_CODES)
        for check in result.get("packet_boundary_checks", []):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_no_raw_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = _json_text(result)
        self.assertNotIn(RAW_SENTINEL, serialized)
        self.assertNotIn(HOSTILE_RAW_VALUE, serialized)

    def assert_no_created_or_authorized_collapse(self, result: Mapping[str, Any]) -> None:
        non_claims = result["non_claims"]
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(non_claims[key], False, key)
        non_meaning = result["packet_boundary_non_meaning"]
        for key in (
            "packet_exists",
            "packet_was_emitted",
            "packet_was_copied_to_another_device",
            "packet_was_received_by_another_carrier",
            "another_device_executed_verification",
            "external_result_exists",
            "cross_carrier_evidence_exists",
            "source_body_packet_exists",
            "manifest_exists",
            "checksum_exists",
            "signature_exists",
            "reproducible_environment_declared",
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
            "command_success_became_packet_permission",
            "packet_boundary_became_packet_emission",
            "local_command_success_became_cross_carrier_proof",
            "artifact_path_became_packet_authority",
            "artifact_existence_became_source_standing",
            "local_repo_state_became_portable_packet_content",
            "hidden_repo_state_became_authority",
        ):
            self.assertIs(non_meaning[key], False, key)
        self.assertIs(non_claims["consumed_request_reopened"], False)
        self.assertIs(non_claims["authorization_token_reused"], False)

    def assert_blocked(
        self,
        request: Any,
        expected_top_code: str | None = None,
        expected_emitted_code: str | None = None,
    ) -> dict[str, Any]:
        result = resolver.resolve_portable_source_body_verification_packet_boundary(
            declared_packet_boundary_request=request
        )
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertIsNotNone(result["block"]["block_code"])
        self.assert_public_block_codes(result)
        self.assert_no_created_or_authorized_collapse(result)
        if expected_top_code is not None:
            self.assertEqual(result["block"]["block_code"], expected_top_code)
        if expected_emitted_code is not None:
            self.assertIn(expected_emitted_code, _codes(result))
        return result

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_portable_source_body_verification_packet_boundary",
            "resolve_portable_source_body_verification_packet_boundary_from_path",
            "write_portable_source_body_verification_packet_boundary_result",
            "build_portable_source_body_verification_packet_boundary_summary",
            "build_declared_portable_source_body_verification_packet_boundary_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "RESULT_VERSION",
            "OUTPUT_ROOT",
            "SUPPORTED_PACKET_BOUNDARY_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_portable_source_body_verification_packet_boundary"
            )
        )
        for code in REPRESENTATIVE_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES, code)

    def test_successful_packet_boundary_recorded_result(self) -> None:
        request = _request()
        result = resolver.resolve_portable_source_body_verification_packet_boundary(
            declared_packet_boundary_request=request
        )

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(
            result["portable_source_body_verification_packet_boundary_metadata"][
                "failed_check_count"
            ],
            0,
        )
        self.assertFalse(result["block"]["blocked"])
        self.assertIsNone(result["block"]["block_code"])
        self.assert_public_block_codes(result)
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)

        metadata = result["portable_source_body_verification_packet_boundary_metadata"]
        self.assertEqual(
            metadata["portable_source_body_verification_packet_boundary_result_version"],
            "0.1.0",
        )
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_portable_source_body_verification_packet_boundary",
        )
        self.assertEqual(metadata["packet_boundary_request_id"], "packet_boundary_test_request_001")

        statement = result["packet_boundary_statement"]
        for field in TRUE_RECORDED_FIELDS:
            self.assertIs(statement[field], True, field)
        for field in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(result["non_claims"][field], False, field)
        self.assertIs(statement["packet_boundary_is_not_packet"], True)
        self.assertIs(statement["packet_boundary_is_not_packet_emission"], True)
        self.assertIs(statement["local_command_success_remains_local_command_success_posture_only"], True)
        self.assertIs(statement["execution_trace_remains_audit_only"], True)
        self.assert_no_created_or_authorized_collapse(result)

    def test_summary_helper_preserves_bounded_packet_boundary_posture(self) -> None:
        result = resolver.resolve_portable_source_body_verification_packet_boundary(
            declared_packet_boundary_request=_request()
        )
        summary = resolver.build_portable_source_body_verification_packet_boundary_summary(
            result
        )

        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertEqual(summary["request_id"], "packet_boundary_test_request_001")
        self.assertEqual(summary["question"], resolver.CORE_QUESTION)
        self.assertEqual(summary["intent"], resolver.INTENT_RECORD)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)
        for field in (
            "packet_boundary_recorded",
            "one_future_packet_step_declared",
            "local_command_success_basis_preserved",
            "command_success_not_packet_emission",
            "packet_not_created",
            "packet_not_emitted",
            "packet_transfer_not_authorized",
            "second_carrier_execution_not_authorized",
            "second_carrier_receipt_not_created",
            "cross_carrier_evidence_not_created",
            "source_not_created",
            "authority_not_created",
            "currentness_not_created",
            "final_completion_not_created",
            "runtime_not_created",
            "follow_on_work_not_authorized",
            "selected_basis_reference_shape_preserved",
            "hidden_repo_state_not_used_as_packet_authority",
            "raw_full_prior_artifact_body_not_returned",
            "authorization_token_reuse_blocked",
            "consumed_request_token_remains_closed",
            "no_packet_transfer_receipt_cross_carrier_evidence",
            "no_source_authority_currentness_final_completion_runtime",
            "no_deployment_public_release_follow_on",
            "command_success_not_packet_permission",
            "hidden_repo_state_not_packet_authority",
        ):
            self.assertIs(summary[field], True, field)
        self.assertEqual(
            summary["selected_command_success_outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_RECORDED",
        )
        self.assertEqual(summary["selected_command_success_version"], "0.1.0")
        self.assertEqual(summary["selected_command_success_failed_check_count"], 0)
        for field in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(summary["key_non_claims"][field], False, field)

    def test_missing_and_non_mapping_requests_block(self) -> None:
        self.assert_blocked(None, "DECLARED_PACKET_BOUNDARY_REQUEST_MALFORMED")
        self.assert_blocked(["not", "a", "mapping"], "DECLARED_PACKET_BOUNDARY_REQUEST_MALFORMED")

    def test_representative_blocking_behavior(self) -> None:
        exact_cases: tuple[tuple[str, Callable[[dict[str, Any]], None], str], ...] = (
            (
                "explicit block intent",
                lambda r: r.update(packet_boundary_intent=resolver.INTENT_BLOCK),
                "PACKET_BOUNDARY_EXPLICIT_BLOCK_INTENT",
            ),
            (
                "unsupported intent",
                lambda r: r.update(packet_boundary_intent="UNSUPPORTED_PACKET_BOUNDARY_INTENT"),
                "PACKET_BOUNDARY_INTENT_UNSUPPORTED",
            ),
            (
                "unsupported scope",
                lambda r: r.update(packet_boundary_scope=["PACKET_BOUNDARY_ONLY", "UNSUPPORTED"]),
                "UNSUPPORTED_PACKET_BOUNDARY_SCOPE",
            ),
            (
                "missing command success basis",
                lambda r: r.pop("selected_command_success_basis"),
                "COMMAND_SUCCESS_BASIS_MISSING",
            ),
            (
                "missing command success terminal summary basis",
                lambda r: r.pop("selected_command_success_terminal_summary_basis"),
                "COMMAND_SUCCESS_TERMINAL_SUMMARY_BASIS_MISSING",
            ),
            (
                "missing command success boundary v3 basis",
                lambda r: r.pop("selected_command_success_boundary_v3_basis"),
                "COMMAND_SUCCESS_BOUNDARY_V3_BASIS_MISSING",
            ),
            (
                "command success boundary v3 not recorded",
                lambda r: (
                    r["selected_command_success_boundary_v3_basis"].update(
                        outcome="NOT_RECORDED"
                    ),
                    r["selected_command_success_basis"].update(
                        command_success_boundary_v3_basis_preserved=False
                    ),
                ),
                "COMMAND_SUCCESS_BOUNDARY_V3_NOT_RECORDED",
            ),
            (
                "missing command result v2 basis",
                lambda r: r.pop("selected_command_result_v2_basis"),
                "COMMAND_RESULT_V2_BASIS_MISSING",
            ),
            (
                "command result v2 not recorded",
                lambda r: (
                    r["selected_command_result_v2_basis"].update(outcome="NOT_RECORDED"),
                    r["selected_command_success_basis"].update(
                        command_result_v2_basis_preserved=False
                    ),
                ),
                "COMMAND_RESULT_V2_NOT_RECORDED",
            ),
            (
                "missing output capture v2 basis",
                lambda r: r.pop("selected_output_capture_v2_basis"),
                "OUTPUT_CAPTURE_V2_BASIS_MISSING",
            ),
            (
                "output capture v2 not recorded",
                lambda r: (
                    r["selected_output_capture_v2_basis"].update(outcome="NOT_RECORDED"),
                    r["selected_command_success_basis"].update(
                        output_capture_v2_basis_preserved=False
                    ),
                ),
                "OUTPUT_CAPTURE_V2_NOT_RECORDED",
            ),
            (
                "missing command output/report artifact basis",
                lambda r: r.pop("selected_command_output_report_artifact_basis"),
                "COMMAND_OUTPUT_REPORT_ARTIFACT_BASIS_MISSING",
            ),
            (
                "command output/report artifact not recorded",
                lambda r: (
                    r["selected_command_output_report_artifact_basis"].update(
                        outcome="NOT_RECORDED"
                    ),
                    r["selected_command_success_basis"].update(
                        command_output_report_artifact_basis_preserved=False
                    ),
                ),
                "COMMAND_OUTPUT_REPORT_ARTIFACT_NOT_RECORDED",
            ),
            (
                "execution trace not audit-only",
                lambda r: (
                    r["selected_command_execution_basis"].update(
                        execution_trace_audit_only=False,
                        execution_trace_audit_only_preserved=False,
                    ),
                    r["selected_command_success_basis"].update(
                        execution_trace_audit_only_preserved=False
                    ),
                ),
                "EXECUTION_TRACE_NOT_AUDIT_ONLY",
            ),
            (
                "command report lineage not lineage-only",
                lambda r: r["selected_command_report_lineage_basis"].update(
                    lineage_only=False
                ),
                "COMMAND_REPORT_LINEAGE_NOT_LINEAGE_ONLY",
            ),
            (
                "command success not recorded",
                lambda r: r["selected_command_success_basis"].update(outcome="NOT_RECORDED"),
                "COMMAND_SUCCESS_NOT_RECORDED",
            ),
            (
                "command success failed checks",
                lambda r: r["selected_command_success_basis"].update(failed_check_count=1),
                "COMMAND_SUCCESS_FAILED_CHECKS_PRESENT",
            ),
            (
                "command success wrong version",
                lambda r: r["selected_command_success_basis"].update(result_version="0.0.9"),
                "COMMAND_SUCCESS_VERSION_NOT_0_1_0",
            ),
            (
                "command success treated as packet emission",
                lambda r: r["selected_command_success_basis"].update(
                    command_success_treated_as_packet_emission=True
                ),
                "COMMAND_SUCCESS_TREATED_AS_PACKET_EMISSION",
            ),
            (
                "command success treated as source",
                lambda r: r["selected_command_success_basis"].update(
                    command_success_treated_as_source=True
                ),
                "COMMAND_SUCCESS_TREATED_AS_SOURCE",
            ),
            (
                "command success treated as authority",
                lambda r: r["selected_command_success_basis"].update(
                    command_success_treated_as_authority=True
                ),
                "COMMAND_SUCCESS_TREATED_AS_AUTHORITY",
            ),
            (
                "command success treated as currentness",
                lambda r: r["selected_command_success_basis"].update(
                    command_success_treated_as_currentness=True
                ),
                "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS",
            ),
            (
                "command success treated as final completion",
                lambda r: r["selected_command_success_basis"].update(
                    command_success_treated_as_final_completion=True
                ),
                "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION",
            ),
            (
                "command success authorized packet creation",
                lambda r: r["selected_command_success_basis"].update(
                    command_success_authorized_packet_creation=True
                ),
                "COMMAND_SUCCESS_AUTHORIZED_PACKET_CREATION",
            ),
            (
                "command success authorized packet emission",
                lambda r: r["selected_command_success_basis"].update(
                    command_success_authorized_packet_emission=True
                ),
                "COMMAND_SUCCESS_AUTHORIZED_PACKET_EMISSION",
            ),
            (
                "command success authorized packet transfer",
                lambda r: r["selected_command_success_basis"].update(
                    command_success_authorized_packet_transfer=True
                ),
                "COMMAND_SUCCESS_AUTHORIZED_PACKET_TRANSFER",
            ),
            (
                "command success authorized second carrier",
                lambda r: r["selected_command_success_basis"].update(
                    command_success_authorized_second_carrier_execution=True
                ),
                "COMMAND_SUCCESS_AUTHORIZED_SECOND_CARRIER_EXECUTION",
            ),
            (
                "command success authorized cross-carrier evidence",
                lambda r: r["selected_command_success_basis"].update(
                    command_success_authorized_cross_carrier_evidence_review=True
                ),
                "COMMAND_SUCCESS_AUTHORIZED_CROSS_CARRIER_EVIDENCE_REVIEW",
            ),
            (
                "packet already created",
                lambda r: r["packet_not_created_posture"].update(packet_created=True),
                "PACKET_ALREADY_CREATED",
            ),
            (
                "packet already emitted",
                lambda r: r["packet_not_emitted_posture"].update(packet_emitted=True),
                "PACKET_ALREADY_EMITTED",
            ),
            (
                "packet already transferred",
                lambda r: r["packet_transfer_not_authorized_posture"].update(packet_transferred=True),
                "PACKET_ALREADY_TRANSFERRED",
            ),
            (
                "second carrier execution already created",
                lambda r: r["second_carrier_execution_not_authorized_posture"].update(
                    second_carrier_execution_created=True
                ),
                "SECOND_CARRIER_EXECUTION_ALREADY_CREATED",
            ),
            (
                "second carrier receipt already created",
                lambda r: r["second_carrier_receipt_not_created_posture"].update(
                    second_carrier_receipt_created=True
                ),
                "SECOND_CARRIER_RECEIPT_ALREADY_CREATED",
            ),
            (
                "cross-carrier evidence already created",
                lambda r: r["cross_carrier_evidence_not_created_posture"].update(
                    cross_carrier_evidence_created=True
                ),
                "CROSS_CARRIER_EVIDENCE_ALREADY_CREATED",
            ),
            (
                "source created",
                lambda r: r["source_not_created_posture"].update(source_created=True),
                "SOURCE_CREATED",
            ),
            (
                "authority created",
                lambda r: r["authority_not_created_posture"].update(authority_created=True),
                "AUTHORITY_CREATED",
            ),
            (
                "currentness created",
                lambda r: r["currentness_not_created_posture"].update(currentness_created=True),
                "CURRENTNESS_CREATED",
            ),
            (
                "final completion claimed",
                lambda r: r["final_completion_not_created_posture"].update(
                    final_completion_claimed=True
                ),
                "FINAL_COMPLETION_CLAIMED",
            ),
            (
                "runtime hosting created",
                lambda r: r["runtime_not_created_posture"].update(runtime_hosting_created=True),
                "RUNTIME_HOSTING_CREATED",
            ),
            (
                "continuation authorized",
                lambda r: r["continuation_not_authorized_posture"].update(
                    continuation_authorized=True
                ),
                "CONTINUATION_AUTHORIZED",
            ),
            (
                "reusable permission created",
                lambda r: r["reusable_permission_not_created_posture"].update(
                    reusable_permission_created=True
                ),
                "REUSABLE_PERMISSION_CREATED",
            ),
            (
                "follow-on work authorized",
                lambda r: r["follow_on_work_not_authorized_posture"].update(
                    follow_on_work_authorized=True
                ),
                "FOLLOW_ON_WORK_AUTHORIZED",
            ),
            (
                "selected basis not reference shaped",
                lambda r: r["selected_command_success_basis"].update(reference_shaped=False),
                "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
            ),
            (
                "raw full prior body returned",
                lambda r: r["selected_command_success_basis"].update(
                    raw_full_prior_artifact_body_returned=True
                ),
                "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
            ),
            (
                "hidden repo state used",
                lambda r: r["hidden_repo_state_not_used_as_packet_authority_posture"].update(
                    hidden_repo_state_used_as_packet_authority=True
                ),
                "HIDDEN_REPO_STATE_USED_AS_PACKET_AUTHORITY",
            ),
            (
                "command report lineage current report artifact",
                lambda r: r["selected_command_report_lineage_basis"].update(
                    command_report_lineage_treated_as_current_report_artifact=True
                ),
                "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENT_REPORT_ARTIFACT",
            ),
            (
                "command report lineage command result authority",
                lambda r: r["selected_command_report_lineage_basis"].update(
                    command_report_lineage_treated_as_command_result_authority=True
                ),
                "COMMAND_REPORT_LINEAGE_TREATED_AS_COMMAND_RESULT_AUTHORITY",
            ),
            (
                "command report lineage command success",
                lambda r: r["selected_command_report_lineage_basis"].update(
                    command_report_lineage_treated_as_command_success=True
                ),
                "COMMAND_REPORT_LINEAGE_TREATED_AS_COMMAND_SUCCESS",
            ),
            (
                "command report lineage source",
                lambda r: r["selected_command_report_lineage_basis"].update(
                    command_report_lineage_treated_as_source=True
                ),
                "COMMAND_REPORT_LINEAGE_TREATED_AS_SOURCE",
            ),
            (
                "command report lineage authority",
                lambda r: r["selected_command_report_lineage_basis"].update(
                    command_report_lineage_treated_as_authority=True
                ),
                "COMMAND_REPORT_LINEAGE_TREATED_AS_AUTHORITY",
            ),
            (
                "command report lineage currentness",
                lambda r: r["selected_command_report_lineage_basis"].update(
                    command_report_lineage_treated_as_currentness=True
                ),
                "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENTNESS",
            ),
            (
                "predecessor failure hidden",
                lambda r: r["selected_predecessor_failure_basis"].update(
                    predecessor_failures_hidden=True
                ),
                "PREDECESSOR_FAILURE_EVIDENCE_NOT_VISIBLE",
            ),
        )
        for label, mutator, code in exact_cases:
            with self.subTest(label=label):
                self.assert_blocked(_mutated(mutator), code)

        non_claim_code_cases = (
            ("external_result_created", "EXTERNAL_RESULT_ALREADY_CREATED"),
            ("source_body_packet_created", "SOURCE_BODY_PACKET_ALREADY_CREATED"),
            ("manifest_created", "MANIFEST_ALREADY_CREATED"),
            ("checksum_created", "CHECKSUM_ALREADY_CREATED"),
            ("signature_created", "SIGNATURE_ALREADY_CREATED"),
            ("reproducible_environment_declared", "REPRODUCIBLE_ENVIRONMENT_ALREADY_DECLARED"),
            ("deployment_created", "DEPLOYMENT_CREATED"),
            ("public_release_created", "PUBLIC_RELEASE_CREATED"),
            ("operation_permission_created", "OPERATION_PERMISSION_CREATED"),
            ("derivative_reception_authorized", "DERIVATIVE_RECEPTION_AUTHORIZED"),
            ("vessel_relation_authorized", "VESSEL_RELATION_AUTHORIZED"),
            ("another_reception_request_authorized", "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"),
            ("packet_treated_as_source", "PACKET_TREATED_AS_SOURCE"),
            ("packet_treated_as_authority", "PACKET_TREATED_AS_AUTHORITY"),
            ("packet_treated_as_currentness", "PACKET_TREATED_AS_CURRENTNESS"),
            ("packet_treated_as_final_completion", "PACKET_TREATED_AS_FINAL_COMPLETION"),
            ("packet_treated_as_runtime", "PACKET_TREATED_AS_RUNTIME"),
            ("packet_treated_as_cross_carrier_proof", "PACKET_TREATED_AS_CROSS_CARRIER_PROOF"),
            ("artifact_existence_treated_as_packet_authority", "ARTIFACT_EXISTENCE_TREATED_AS_PACKET_AUTHORITY"),
            ("artifact_path_treated_as_currentness", "ARTIFACT_PATH_TREATED_AS_CURRENTNESS"),
            ("consumed_request_reopened", "CONSUMED_REQUEST_REOPENED"),
            ("authorization_token_reused", "AUTHORIZATION_TOKEN_REUSED"),
            ("prior_artifacts_mutated", "ARTIFACTS_MUTATED"),
        )
        for field, code in non_claim_code_cases:
            with self.subTest(non_claim=field):
                self.assert_blocked(
                    _mutated(lambda r, f=field: r["declared_non_claims"].update({f: True})),
                    expected_emitted_code=code,
                )

        extra_non_claim_cases = (
            ("full_prior_artifact_body_emitted", "FULL_PRIOR_ARTIFACT_BODY_EMITTED"),
            ("mutation_performed", "MUTATION_PERFORMED"),
            ("replay_performed", "REPLAY_PERFORMED"),
            ("merge_performed", "MERGE_PERFORMED"),
        )
        for field, code in extra_non_claim_cases:
            with self.subTest(extra_non_claim=field):
                self.assert_blocked(
                    _mutated(lambda r, f=field: r["declared_non_claims"].update({f: True})),
                    expected_emitted_code=code,
                )

        self.assert_blocked(
            _mutated(lambda r: r["declared_non_claims"].pop("packet_created")),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )

    def test_path_and_write_behavior_use_temp_output_root(self) -> None:
        request = _request()
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            request_path = temp / "request.json"
            request_path.write_text(json.dumps(request, sort_keys=True), encoding="utf-8")

            result = resolver.resolve_portable_source_body_verification_packet_boundary_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], RECORDED)
            metadata = result["portable_source_body_verification_packet_boundary_metadata"]
            self.assertEqual(
                metadata["portable_source_body_verification_packet_boundary_result_version"],
                "0.1.0",
            )
            self.assertEqual(
                metadata["resolver_module"],
                "resolve_portable_source_body_verification_packet_boundary",
            )

            malformed_path = temp / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            with self.assertRaises(resolver.PortableSourceBodyVerificationPacketBoundaryError):
                resolver.resolve_portable_source_body_verification_packet_boundary_from_path(
                    malformed_path
                )

            array_path = temp / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            with self.assertRaises(resolver.PortableSourceBodyVerificationPacketBoundaryError):
                resolver.resolve_portable_source_body_verification_packet_boundary_from_path(
                    array_path
                )

            missing_path = temp / "missing.json"
            with self.assertRaises(resolver.PortableSourceBodyVerificationPacketBoundaryError):
                resolver.resolve_portable_source_body_verification_packet_boundary_from_path(
                    missing_path
                )

            output_root = (
                temp
                / "artifacts"
                / "integrity_host_v0_min_coexistence_portable_source_body_verification_packet_boundary"
            )
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                first = resolver.write_portable_source_body_verification_packet_boundary_result(
                    result
                )
                second = resolver.write_portable_source_body_verification_packet_boundary_result(
                    result
                )

            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertEqual(first.parent, output_root)
            self.assertEqual(second.parent, output_root)
            parsed = json.loads(first.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], RECORDED)
            self.assertIn(
                "integrity_host_v0_min_coexistence_portable_source_body_verification_packet_boundary",
                str(first),
            )
            for forbidden_root_fragment in (
                "command_success/",
                "command_success_boundary",
                "command_result",
                "output_capture",
                "packet_artifact",
                "packet_emission",
                "manifest",
                "checksum",
                "signature",
                "cross_carrier",
                "runtime",
                "deployment",
                "public_release",
            ):
                self.assertNotIn(forbidden_root_fragment, str(first))

    def test_resolver_does_not_mutate_request_or_selected_basis_inputs(self) -> None:
        request = _request()
        before = copy.deepcopy(request)
        result = resolver.resolve_portable_source_body_verification_packet_boundary(
            declared_packet_boundary_request=request
        )
        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(request, before)

        for key in (
            "selected_command_success_basis",
            "selected_command_success_terminal_summary_basis",
            "selected_command_success_spec_basis",
            "selected_command_success_boundary_v3_basis",
            "selected_command_result_v2_basis",
            "selected_output_capture_v2_basis",
            "selected_command_output_report_artifact_basis",
            "selected_command_execution_basis",
            "selected_command_report_lineage_basis",
            "selected_predecessor_failure_basis",
            "packet_boundary_scope",
            "declared_non_claims",
        ):
            self.assertEqual(request[key], before[key], key)
        for key in resolver.POSTURE_KEYS:
            self.assertEqual(request[key], before[key], key)

    def test_raw_full_body_and_hidden_repo_state_containment(self) -> None:
        request = _request()
        hostile_payload = {
            "raw_body": HOSTILE_RAW_VALUE,
            "raw_full_body": HOSTILE_RAW_VALUE,
            "full_body": HOSTILE_RAW_VALUE,
            "artifact_body": HOSTILE_RAW_VALUE,
            "raw_result_body": HOSTILE_RAW_VALUE,
            "raw_output_body": HOSTILE_RAW_VALUE,
            "packet_body": HOSTILE_RAW_VALUE,
            "source_body": HOSTILE_RAW_VALUE,
            "authority_body": HOSTILE_RAW_VALUE,
            "hidden_repo_state": HOSTILE_RAW_VALUE,
            "current_working_tree": HOSTILE_RAW_VALUE,
            "local_cache": HOSTILE_RAW_VALUE,
            "unlisted_file_dependency": HOSTILE_RAW_VALUE,
            "nested": [{"sentinel": RAW_SENTINEL}],
        }
        for key in (
            "selected_command_success_basis",
            "selected_command_success_boundary_v3_basis",
            "selected_command_result_v2_basis",
            "selected_output_capture_v2_basis",
            "selected_command_report_lineage_basis",
        ):
            request[key]["hostile_containment_probe"] = copy.deepcopy(hostile_payload)

        before = copy.deepcopy(request)
        result = resolver.resolve_portable_source_body_verification_packet_boundary(
            declared_packet_boundary_request=request
        )
        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assert_public_block_codes(result)
        self.assert_no_raw_sentinels(result)
        self.assert_no_created_or_authorized_collapse(result)
        self.assertIs(
            result["packet_boundary_statement"][
                "hidden_repo_state_not_used_as_packet_authority"
            ],
            result["outcome"] == RECORDED,
        )
        self.assertIs(result["non_claims"]["hidden_repo_state_used_as_packet_authority"], False)
        self.assertEqual(request, before)

    def test_input_not_mutated_when_raw_probe_is_present(self) -> None:
        request = _request()
        request["selected_command_success_basis"]["raw_body"] = HOSTILE_RAW_VALUE
        request["selected_command_success_basis"]["nested"] = [RAW_SENTINEL]
        before = copy.deepcopy(request)
        result = resolver.resolve_portable_source_body_verification_packet_boundary(
            declared_packet_boundary_request=request
        )
        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assertEqual(request, before)
        self.assert_no_raw_sentinels(result)


if __name__ == "__main__":
    unittest.main()
