"""Tests for bounded portable source-body verification command success.

This suite is command-success posture only. It verifies that the resolver can
record one bounded command success downstream of command success boundary v3
without creating source, authority, currentness, final completion, public
readiness, deployment readiness, operation permission, continuation, reusable
permission, derivative reception, vessel relation, another reception request,
or follow-on work.
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

import resolve_portable_source_body_verification_command_success as resolver


RECORDED = resolver.OUTCOME_RECORDED
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {
    resolver.OUTCOME_RECORDED,
    resolver.OUTCOME_NOT_RECORDED,
    resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    resolver.OUTCOME_BLOCKED,
}
RAW_SENTINEL = "RAW_COMMAND_SUCCESS_BODY_MUST_NOT_RETURN"
HOSTILE_RAW_VALUE = "HOSTILE_RAW_FULL_BODY_VALUE_MUST_NOT_RETURN"

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_command_success_metadata",
    "declared_command_success_question",
    "selected_command_success_boundary_v3_basis",
    "selected_command_success_boundary_v3_terminal_summary_basis",
    "selected_command_success_boundary_v1_predecessor_failure_basis",
    "selected_command_success_boundary_v2_predecessor_failure_basis",
    "selected_command_success_boundary_spec_basis",
    "selected_command_result_v2_basis",
    "selected_command_result_v2_terminal_summary_basis",
    "selected_command_result_v1_predecessor_failure_basis",
    "selected_command_output_report_artifact_basis",
    "selected_output_capture_v2_basis",
    "selected_post_invocation_command_execution_basis",
    "selected_command_report_lineage_basis",
    "command_success_scope",
    "command_success_checks",
    "command_success_statement",
    "command_success_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_command_success_summary",
)

TRUE_RECORDED_FIELDS = (
    "command_success_recorded",
    "bounded_command_success_recorded",
    "command_success_boundary_v3_basis_preserved",
    "command_success_boundary_v1_predecessor_failure_preserved",
    "command_success_boundary_v2_predecessor_failure_preserved",
    "command_result_v2_basis_preserved",
    "bounded_command_result_preserved",
    "command_result_v1_predecessor_failure_preserved",
    "command_result_boundary_basis_preserved",
    "command_output_report_artifact_basis_preserved",
    "bounded_command_output_report_artifact_preserved",
    "command_output_report_artifact_boundary_basis_preserved",
    "output_capture_v2_basis_preserved",
    "output_capture_v1_predecessor_failure_preserved",
    "bounded_output_capture_event_preserved",
    "command_output_basis_preserved",
    "recorded_command_execution_event_preserved",
    "execution_trace_audit_only_preserved",
    "report_body_absent_or_bounded",
    "result_body_absent_or_bounded",
    "success_body_absent_or_bounded",
    "report_body_not_invented",
    "result_body_not_invented",
    "success_body_not_invented",
    "source_not_created",
    "authority_not_created",
    "currentness_not_created",
    "final_completion_not_created",
    "public_readiness_not_created",
    "deployment_readiness_not_created",
    "operation_permission_not_created",
    "continuation_not_authorized",
    "reusable_permission_not_created",
    "derivative_reception_not_authorized",
    "vessel_relation_not_authorized",
    "another_reception_request_not_authorized",
    "follow_on_work_not_authorized",
    "source_inference_blocked",
    "authority_inference_blocked",
    "currentness_inference_blocked",
    "final_completion_inference_blocked",
    "public_readiness_inference_blocked",
    "deployment_readiness_inference_blocked",
    "operation_permission_inference_blocked",
    "follow_on_work_inference_blocked",
    "unbounded_pass_fail_inference_blocked",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
    "returned_result_containment_preserved",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "summary_surface_conformance_preserved",
)

REPRESENTATIVE_BLOCK_CODES = (
    "COMMAND_SUCCESS_BOUNDARY_V3_BASIS_MISSING",
    "COMMAND_SUCCESS_BOUNDARY_V3_VERSION_NOT_0_3_0",
    "COMMAND_SUCCESS_BOUNDARY_V3_V1_FAILURE_EVIDENCE_MISSING",
    "COMMAND_SUCCESS_BOUNDARY_V3_V2_FAILURE_EVIDENCE_MISSING",
    "COMMAND_SUCCESS_BOUNDARY_V3_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY",
    "COMMAND_SUCCESS_BOUNDARY_V3_SUMMARY_SURFACE_CONFORMANCE_MISSING",
    "COMMAND_RESULT_V2_BASIS_MISSING",
    "COMMAND_RESULT_V2_VERSION_NOT_0_2_0",
    "COMMAND_SUCCESS_TREATED_AS_SOURCE",
    "COMMAND_SUCCESS_TREATED_AS_AUTHORITY",
    "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS",
    "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION",
    "COMMAND_SUCCESS_TREATED_AS_PUBLIC_READINESS",
    "COMMAND_SUCCESS_TREATED_AS_DEPLOYMENT_READINESS",
    "COMMAND_SUCCESS_TREATED_AS_OPERATION_PERMISSION",
    "COMMAND_SUCCESS_TREATED_AS_FOLLOW_ON_WORK",
    "SUCCESS_BODY_INVENTED",
    "SOURCE_CREATED",
    "AUTHORITY_CREATED",
    "CURRENTNESS_CREATED",
    "FINAL_COMPLETION_CLAIMED",
    "PUBLIC_READINESS_CREATED",
    "DEPLOYMENT_READINESS_CREATED",
    "OPERATION_PERMISSION_CREATED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "SOURCE_INFERENCE_MADE",
    "AUTHORITY_INFERENCE_MADE",
    "CURRENTNESS_INFERENCE_MADE",
    "FINAL_COMPLETION_INFERENCE_MADE",
    "PUBLIC_READINESS_INFERENCE_MADE",
    "DEPLOYMENT_READINESS_INFERENCE_MADE",
    "OPERATION_PERMISSION_INFERENCE_MADE",
    "FOLLOW_ON_WORK_INFERENCE_MADE",
    "UNBOUNDED_PASS_FAIL_INFERENCE_MADE",
    "UNSUPPORTED_COMMAND_SUCCESS_SCOPE",
    "NON_CLAIM_MISSING_OR_FLIPPED",
)


def _json_text(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=True)


def _request(**overrides: Any) -> dict[str, Any]:
    request = resolver.build_declared_portable_source_body_verification_command_success_request()
    request["command_success_request_id"] = "command_success_test_request_001"
    request["command_success_scope"] = list(resolver.SUPPORTED_COMMAND_SUCCESS_SCOPE)
    request["declared_non_claims"] = {
        key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS
    }

    request["selected_command_success_boundary_v3_terminal_summary_basis"].update(
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_BOUNDARY_V3_TERMINAL_SUMMARY_STANDING",
        terminal_summary_readability_basis_only=True,
    )
    request["selected_command_success_boundary_v1_predecessor_failure_basis"].update(
        v1_predecessor_failure_preserved=True,
        v1_repaired=False,
        v1_hidden=False,
        v1_claimed_passed=False,
    )
    request["selected_command_success_boundary_v2_predecessor_failure_basis"].update(
        v2_predecessor_failure_preserved=True,
        v2_repaired=False,
        v2_hidden=False,
        v2_claimed_passed=False,
    )
    request["selected_command_success_boundary_spec_basis"].update(
        basis_reference="spec/PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_BOUNDARY_V0_MIN_SPEC.md"
    )
    request["selected_command_result_v2_terminal_summary_basis"].update(
        terminal_summary_readability_basis_only=True,
        command_result_v2_basis_preserved=True,
    )
    request["selected_command_result_v1_predecessor_failure_basis"].update(
        v1_command_result_predecessor_failure_preserved=True,
        v1_command_result_repaired=False,
        v1_command_result_hidden=False,
        v1_command_result_claimed_passed=False,
    )
    request["selected_command_result_boundary_basis"].update(
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_BOUNDARY_RECORDED"
    )
    request["selected_command_result_boundary_terminal_summary_basis"].update(
        terminal_summary_readability_basis_only=True
    )
    request["selected_command_output_report_artifact_terminal_summary_basis"].update(
        terminal_summary_readability_basis_only=True
    )
    request["selected_command_output_report_artifact_boundary_basis"].update(
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_RECORDED"
    )
    request[
        "selected_command_output_report_artifact_boundary_terminal_summary_basis"
    ].update(terminal_summary_readability_basis_only=True)
    request["selected_output_capture_v2_terminal_summary_basis"].update(
        terminal_summary_readability_basis_only=True
    )
    request["selected_output_capture_v1_predecessor_failure_basis"].update(
        output_capture_v1_predecessor_failure_preserved=True,
        v1_output_capture_repaired=False,
        v1_output_capture_hidden=False,
        v1_output_capture_claimed_passed=False,
    )
    request["selected_output_capture_boundary_basis"].update(
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_BOUNDARY_RECORDED"
    )
    request["selected_command_output_basis"].update(
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_RECORDED"
    )
    request["selected_command_output_boundary_basis"].update(
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_BOUNDARY_RECORDED"
    )
    request["selected_command_output_containment_basis"].update(
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_CONTAINMENT_RECORDED"
    )
    request["selected_post_invocation_command_execution_terminal_summary_basis"].update(
        terminal_summary_readability_basis_only=True
    )
    request["selected_command_invocation_basis"].update(
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_INVOCATION_RECORDED"
    )
    request["selected_command_execution_review_basis"].update(
        outcome="CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_EXECUTION_REVIEW_RECORDED"
    )
    request["selected_request_consumption_basis"].update(
        outcome="ADMITTED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_CONSUMED"
    )
    request["selected_consumed_request_basis"].update(
        consumed_request_token_remains_closed=True,
        consumed_request_reopened=False,
    )
    request["selected_v2_admitted_request_basis"].update(
        outcome="SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_ADMITTED",
        result_version="0.2.0",
        one_bounded_future_invocation_request_admitted=True,
    )
    request["selected_v1_predecessor_failure_basis"].update(
        v1_request_admission_predecessor_failure_preserved=True,
        v1_repaired=False,
        v1_hidden=False,
        v1_claimed_passed=False,
    )
    request["selected_older_command_execution_boundary_lineage_basis"].update(
        older_command_execution_boundary_lineage_only=True,
        older_command_execution_boundary_lineage_treated_as_current_execution=False,
    )

    request.update(overrides)
    return request


def _resolve(request: Mapping[str, Any] | None) -> dict[str, Any]:
    return resolver.resolve_portable_source_body_verification_command_success(request)


def _statement(result: Mapping[str, Any]) -> Mapping[str, Any]:
    return result["command_success_statement"]


def _summary(result: Mapping[str, Any]) -> Mapping[str, Any]:
    return result["portable_source_body_verification_command_success_summary"]


class CommandSuccessResolverTests(unittest.TestCase):
    maxDiff = None

    def assert_public_codes(self, result: Mapping[str, Any]) -> None:
        block = result.get("block", {})
        if isinstance(block, Mapping) and block.get("block_code"):
            self.assertIn(block["block_code"], resolver.BLOCK_CODES)
        for check in result.get("command_success_checks", []):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code:
                    self.assertIn(code, resolver.BLOCK_CODES, check)

    def assert_no_raw_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = _json_text(result)
        self.assertNotIn(RAW_SENTINEL, serialized)
        self.assertNotIn(HOSTILE_RAW_VALUE, serialized)

    def assert_no_collapse(self, result: Mapping[str, Any]) -> None:
        statement = _statement(result)
        non_claims = result["non_claims"]
        if result["outcome"] == RECORDED:
            for key in (
                "source_not_created",
                "authority_not_created",
                "currentness_not_created",
                "final_completion_not_created",
                "public_readiness_not_created",
                "deployment_readiness_not_created",
                "operation_permission_not_created",
                "continuation_not_authorized",
                "reusable_permission_not_created",
                "derivative_reception_not_authorized",
                "vessel_relation_not_authorized",
                "another_reception_request_not_authorized",
                "follow_on_work_not_authorized",
                "authorization_token_reuse_blocked",
                "consumed_request_token_remains_closed",
            ):
                self.assertIs(statement[key], True, key)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(non_claims[key], False, key)
        self.assertFalse(result["command_success_non_meaning"]["source_exists"])
        self.assertFalse(result["command_success_non_meaning"]["authority_exists"])
        self.assertFalse(result["command_success_non_meaning"]["currentness_exists"])
        self.assertFalse(result["command_success_non_meaning"]["final_completion_exists"])
        self.assertFalse(
            result["command_success_non_meaning"][
                "deployment_runtime_public_release_created"
            ]
        )
        self.assertFalse(
            result["command_success_non_meaning"]["follow_on_work_authorized"]
        )

    def assert_blocked(self, request: Mapping[str, Any] | None, expected_code: str | None = None) -> dict[str, Any]:
        result = _resolve(request)
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertIsNotNone(result["block"]["block_code"])
        if expected_code is not None:
            self.assertEqual(result["block"]["block_code"], expected_code)
        self.assert_public_codes(result)
        self.assert_no_raw_sentinels(result)
        self.assert_no_collapse(result)
        return result

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_portable_source_body_verification_command_success",
            "resolve_portable_source_body_verification_command_success_from_path",
            "write_portable_source_body_verification_command_success_result",
            "build_portable_source_body_verification_command_success_summary",
            "build_declared_portable_source_body_verification_command_success_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_portable_source_body_verification_command_success"
            )
        )
        self.assertTrue(resolver.SUPPORTED_COMMAND_SUCCESS_SCOPE)
        self.assertTrue(resolver.REQUIRED_FALSE_NON_CLAIMS)
        for code in REPRESENTATIVE_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_successful_command_success_recorded_result(self) -> None:
        request = _request()
        result = _resolve(request)

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(
            result["portable_source_body_verification_command_success_metadata"][
                "failed_check_count"
            ],
            0,
        )
        self.assertIsNone(result["block"]["block_code"])
        self.assert_public_codes(result)
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)

        metadata = result["portable_source_body_verification_command_success_metadata"]
        self.assertEqual(
            metadata["portable_source_body_verification_command_success_result_version"],
            "0.1.0",
        )
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_portable_source_body_verification_command_success",
        )
        self.assertEqual(metadata["command_success_request_id"], "command_success_test_request_001")

        statement = _statement(result)
        for key in TRUE_RECORDED_FIELDS:
            self.assertIs(statement[key], True, key)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(statement[key], False, key)
            self.assertIs(result["non_claims"][key], False, key)

        non_meaning = result["command_success_non_meaning"]
        self.assertFalse(non_meaning["source_exists"])
        self.assertFalse(non_meaning["authority_exists"])
        self.assertFalse(non_meaning["currentness_exists"])
        self.assertFalse(non_meaning["final_completion_exists"])
        self.assertFalse(non_meaning["deployment_runtime_public_release_created"])
        self.assertFalse(non_meaning["follow_on_work_authorized"])
        self.assertTrue(statement["command_success_boundary_v3_remains_boundary_basis_only"])
        self.assertTrue(statement["command_result_v2_remains_command_result_posture_only"])
        self.assertTrue(statement["output_capture_v2_remains_output_capture_posture_only"])
        self.assertTrue(statement["execution_trace_remains_audit_only"])
        self.assert_no_raw_sentinels(result)

    def test_summary_helper_preserves_bounded_posture(self) -> None:
        result = _resolve(_request())
        summary = resolver.build_portable_source_body_verification_command_success_summary(result)

        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertEqual(summary["request_id"], "command_success_test_request_001")
        self.assertEqual(summary["question"], resolver.CORE_QUESTION)
        self.assertEqual(summary["intent"], resolver.INTENT_RECORD)
        self.assertEqual(summary["failed_check_count"], 0)
        for key in (
            "command_success_recorded",
            "bounded_command_success_recorded",
            "command_success_boundary_v3_basis_preserved",
            "command_success_boundary_v1_predecessor_failure_preserved",
            "command_success_boundary_v2_predecessor_failure_preserved",
            "command_result_v2_basis_preserved",
            "bounded_command_result_preserved",
            "command_output_report_artifact_basis_preserved",
            "bounded_command_output_report_artifact_preserved",
            "report_body_absent_or_bounded",
            "result_body_absent_or_bounded",
            "success_body_absent_or_bounded",
            "report_body_not_invented",
            "result_body_not_invented",
            "success_body_not_invented",
            "source_not_created",
            "authority_not_created",
            "currentness_not_created",
            "final_completion_not_created",
            "public_readiness_not_created",
            "deployment_readiness_not_created",
            "operation_permission_not_created",
            "continuation_not_authorized",
            "reusable_permission_not_created",
            "derivative_reception_not_authorized",
            "vessel_relation_not_authorized",
            "another_reception_request_not_authorized",
            "follow_on_work_not_authorized",
            "source_inference_blocked",
            "authority_inference_blocked",
            "currentness_inference_blocked",
            "final_completion_inference_blocked",
            "public_readiness_inference_blocked",
            "deployment_readiness_inference_blocked",
            "operation_permission_inference_blocked",
            "follow_on_work_inference_blocked",
            "unbounded_pass_fail_inference_blocked",
            "command_success_not_source_authority_currentness_final_completion_readiness_permission_follow_on",
            "command_result_v2_not_success_source_authority_currentness_final_completion_readiness",
            "output_capture_not_result_success_source_authority_currentness_final_completion",
            "execution_trace_not_success_source_authority_currentness_final_completion",
            "command_report_lineage_not_current_report_artifact_result_authority_success_source_authority_currentness",
            "raw_full_prior_artifact_body_not_returned",
            "artifacts_not_mutated",
            "deployment_runtime_public_release_not_created",
            "continuation_publication_reusable_follow_on_not_authorized",
        ):
            self.assertIs(summary[key], True, key)
        self.assertEqual(
            summary["selected_command_success_boundary_v3_outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_BOUNDARY_RECORDED",
        )
        self.assertEqual(summary["selected_command_success_boundary_v3_version"], "0.3.0")
        self.assertEqual(summary["selected_command_success_boundary_v3_failed_check_count"], 0)
        self.assertEqual(
            summary["selected_command_result_v2_outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_RECORDED",
        )
        self.assertEqual(summary["selected_command_result_v2_version"], "0.2.0")
        self.assertEqual(summary["selected_output_capture_v2_version"], "0.2.0")
        self.assertEqual(
            summary["selected_command_output_report_artifact_outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_REPORT_ARTIFACT_RECORDED",
        )
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(summary["key_non_claims"][key], False, key)

    def test_representative_blocking_behavior(self) -> None:
        def mutate(path: tuple[str, ...], value: Any) -> Callable[[dict[str, Any]], None]:
            def apply(request: dict[str, Any]) -> None:
                target = request
                for key in path[:-1]:
                    target = target[key]
                target[path[-1]] = value

            return apply

        def delete(path: tuple[str, ...]) -> Callable[[dict[str, Any]], None]:
            def apply(request: dict[str, Any]) -> None:
                target = request
                for key in path[:-1]:
                    target = target[key]
                del target[path[-1]]

            return apply

        cases: tuple[tuple[str, Callable[[dict[str, Any]], None], str], ...] = (
            ("explicit block intent", mutate(("command_success_intent",), resolver.INTENT_BLOCK), "COMMAND_SUCCESS_EXPLICIT_BLOCK_INTENT"),
            ("unsupported intent", mutate(("command_success_intent",), "BAD_INTENT"), "COMMAND_SUCCESS_INTENT_UNSUPPORTED"),
            ("unsupported scope", mutate(("command_success_scope",), ["COMMAND_SUCCESS_ONLY", "BAD_SCOPE"]), "UNSUPPORTED_COMMAND_SUCCESS_SCOPE"),
            ("missing boundary v3 basis", delete(("selected_command_success_boundary_v3_basis",)), "COMMAND_SUCCESS_BOUNDARY_V3_BASIS_MISSING"),
            ("boundary v3 not recorded", mutate(("selected_command_success_boundary_v3_basis", "outcome"), "NOT_RECORDED"), "COMMAND_SUCCESS_BOUNDARY_V3_NOT_RECORDED"),
            ("boundary v3 failed checks", mutate(("selected_command_success_boundary_v3_basis", "failed_check_count"), 1), "COMMAND_SUCCESS_BOUNDARY_V3_FAILED_CHECKS_PRESENT"),
            ("boundary v3 wrong version", mutate(("selected_command_success_boundary_v3_basis", "result_version"), "0.2.0"), "COMMAND_SUCCESS_BOUNDARY_V3_VERSION_NOT_0_3_0"),
            ("boundary v3 predecessor chain missing", mutate(("selected_command_success_boundary_v3_basis", "predecessor_chain"), []), "COMMAND_SUCCESS_BOUNDARY_V3_PREDECESSOR_CHAIN_MISSING"),
            ("boundary v3 v1 failure missing", mutate(("selected_command_success_boundary_v3_basis", "v1_predecessor_failure_preserved"), False), "COMMAND_SUCCESS_BOUNDARY_V3_V1_FAILURE_EVIDENCE_MISSING"),
            ("boundary v3 v2 failure missing", mutate(("selected_command_success_boundary_v3_basis", "v2_predecessor_failure_preserved"), False), "COMMAND_SUCCESS_BOUNDARY_V3_V2_FAILURE_EVIDENCE_MISSING"),
            ("boundary v3 repaired v1", mutate(("selected_command_success_boundary_v3_basis", "v1_repaired"), True), "COMMAND_SUCCESS_BOUNDARY_V3_REPAIRED_V1"),
            ("boundary v3 hid v1", mutate(("selected_command_success_boundary_v3_basis", "v1_hidden"), True), "COMMAND_SUCCESS_BOUNDARY_V3_HID_V1"),
            ("boundary v3 claimed v1 passed", mutate(("selected_command_success_boundary_v3_basis", "v1_claimed_passed"), True), "COMMAND_SUCCESS_BOUNDARY_V3_CLAIMED_V1_PASSED"),
            ("boundary v3 erased v1", mutate(("selected_command_success_boundary_v3_basis", "v3_command_success_boundary_erased_v1"), True), "COMMAND_SUCCESS_BOUNDARY_V3_ERASED_V1"),
            ("boundary v3 repaired v2", mutate(("selected_command_success_boundary_v3_basis", "v2_repaired"), True), "COMMAND_SUCCESS_BOUNDARY_V3_REPAIRED_V2"),
            ("boundary v3 hid v2", mutate(("selected_command_success_boundary_v3_basis", "v2_hidden"), True), "COMMAND_SUCCESS_BOUNDARY_V3_HID_V2"),
            ("boundary v3 claimed v2 passed", mutate(("selected_command_success_boundary_v3_basis", "v2_claimed_passed"), True), "COMMAND_SUCCESS_BOUNDARY_V3_CLAIMED_V2_PASSED"),
            ("boundary v3 erased v2", mutate(("selected_command_success_boundary_v3_basis", "v3_command_success_boundary_erased_v2"), True), "COMMAND_SUCCESS_BOUNDARY_V3_ERASED_V2"),
            ("boundary v3 future step missing", mutate(("selected_command_success_boundary_v3_basis", "one_future_command_success_step_declared"), False), "COMMAND_SUCCESS_BOUNDARY_V3_DID_NOT_DECLARE_FUTURE_SUCCESS_STEP"),
            ("boundary v3 already created success", mutate(("selected_command_success_boundary_v3_basis", "command_success_created"), True), "COMMAND_SUCCESS_BOUNDARY_V3_ALREADY_CREATED_SUCCESS"),
            ("boundary v3 inferred success", mutate(("selected_command_success_boundary_v3_basis", "success_inference_made"), True), "COMMAND_SUCCESS_BOUNDARY_V3_INFERRED_SUCCESS"),
            ("boundary v3 inferred currentness", mutate(("selected_command_success_boundary_v3_basis", "currentness_inference_made"), True), "COMMAND_SUCCESS_BOUNDARY_V3_INFERRED_CURRENTNESS"),
            ("boundary v3 inferred final completion", mutate(("selected_command_success_boundary_v3_basis", "final_completion_inference_made"), True), "COMMAND_SUCCESS_BOUNDARY_V3_INFERRED_FINAL_COMPLETION"),
            ("boundary v3 inferred public readiness", mutate(("selected_command_success_boundary_v3_basis", "public_readiness_inference_made"), True), "COMMAND_SUCCESS_BOUNDARY_V3_INFERRED_PUBLIC_READINESS"),
            ("boundary v3 inferred deployment readiness", mutate(("selected_command_success_boundary_v3_basis", "deployment_readiness_inference_made"), True), "COMMAND_SUCCESS_BOUNDARY_V3_INFERRED_DEPLOYMENT_READINESS"),
            ("boundary v3 inferred authority", mutate(("selected_command_success_boundary_v3_basis", "authority_inference_made"), True), "COMMAND_SUCCESS_BOUNDARY_V3_INFERRED_AUTHORITY"),
            ("boundary v3 inferred follow on", mutate(("selected_command_success_boundary_v3_basis", "follow_on_work_inference_made"), True), "COMMAND_SUCCESS_BOUNDARY_V3_INFERRED_FOLLOW_ON_WORK"),
            ("boundary v3 inferred unbounded pass fail", mutate(("selected_command_success_boundary_v3_basis", "unbounded_pass_fail_inference_made"), True), "COMMAND_SUCCESS_BOUNDARY_V3_INFERRED_UNBOUNDED_PASS_FAIL"),
            ("boundary v3 not reference shaped", mutate(("selected_command_success_boundary_v3_basis", "selected_basis_reference_shape_preserved"), False), "COMMAND_SUCCESS_BOUNDARY_V3_SELECTED_BASIS_NOT_REFERENCE_SHAPED"),
            ("boundary v3 raw full prior returned", mutate(("selected_command_success_boundary_v3_basis", "raw_full_prior_artifact_body_returned"), True), "COMMAND_SUCCESS_BOUNDARY_V3_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY"),
            ("boundary v3 summary conformance missing", mutate(("selected_command_success_boundary_v3_basis", "summary_surface_conformance_preserved"), False), "COMMAND_SUCCESS_BOUNDARY_V3_SUMMARY_SURFACE_CONFORMANCE_MISSING"),
            ("result v2 missing", delete(("selected_command_result_v2_basis",)), "COMMAND_RESULT_V2_BASIS_MISSING"),
            ("result v2 not recorded", mutate(("selected_command_result_v2_basis", "outcome"), "NOT_RECORDED"), "COMMAND_RESULT_V2_NOT_RECORDED"),
            ("result v2 failed checks", mutate(("selected_command_result_v2_basis", "failed_check_count"), 1), "COMMAND_RESULT_V2_FAILED_CHECKS_PRESENT"),
            ("result v2 wrong version", mutate(("selected_command_result_v2_basis", "result_version"), "0.1.0"), "COMMAND_RESULT_V2_VERSION_NOT_0_2_0"),
            ("result v2 already created success", mutate(("selected_command_result_v2_basis", "command_success_created"), True), "COMMAND_RESULT_V2_ALREADY_CREATED_SUCCESS"),
            ("result v2 treated as success", mutate(("selected_command_result_v2_basis", "command_result_treated_as_success"), True), "COMMAND_RESULT_V2_TREATED_RESULT_AS_SUCCESS"),
            ("result v2 treated as source", mutate(("selected_command_result_v2_basis", "command_result_treated_as_source"), True), "COMMAND_RESULT_V2_TREATED_RESULT_AS_SOURCE"),
            ("result v2 treated as authority", mutate(("selected_command_result_v2_basis", "command_result_treated_as_authority"), True), "COMMAND_RESULT_V2_TREATED_RESULT_AS_AUTHORITY"),
            ("result v2 treated as currentness", mutate(("selected_command_result_v2_basis", "command_result_treated_as_currentness"), True), "COMMAND_RESULT_V2_TREATED_RESULT_AS_CURRENTNESS"),
            ("result v2 treated as final completion", mutate(("selected_command_result_v2_basis", "command_result_treated_as_final_completion"), True), "COMMAND_RESULT_V2_TREATED_RESULT_AS_FINAL_COMPLETION"),
            ("result v2 treated as public readiness", mutate(("selected_command_result_v2_basis", "command_result_treated_as_public_readiness"), True), "COMMAND_RESULT_V2_TREATED_RESULT_AS_PUBLIC_READINESS"),
            ("result v2 treated as deployment readiness", mutate(("selected_command_result_v2_basis", "command_result_treated_as_deployment_readiness"), True), "COMMAND_RESULT_V2_TREATED_RESULT_AS_DEPLOYMENT_READINESS"),
            ("artifact missing", delete(("selected_command_output_report_artifact_basis",)), "COMMAND_OUTPUT_REPORT_ARTIFACT_BASIS_MISSING"),
            ("artifact not recorded", mutate(("selected_command_output_report_artifact_basis", "outcome"), "NOT_RECORDED"), "COMMAND_OUTPUT_REPORT_ARTIFACT_NOT_RECORDED"),
            ("artifact failed checks", mutate(("selected_command_output_report_artifact_basis", "failed_check_count"), 1), "COMMAND_OUTPUT_REPORT_ARTIFACT_FAILED_CHECKS_PRESENT"),
            ("artifact treated as result authority", mutate(("selected_command_output_report_artifact_basis", "command_output_report_artifact_treated_as_result_authority"), True), "COMMAND_OUTPUT_REPORT_ARTIFACT_TREATED_AS_RESULT_AUTHORITY"),
            ("artifact treated as success", mutate(("selected_command_output_report_artifact_basis", "command_output_report_artifact_treated_as_success"), True), "COMMAND_OUTPUT_REPORT_ARTIFACT_TREATED_AS_SUCCESS"),
            ("capture missing", delete(("selected_output_capture_v2_basis",)), "OUTPUT_CAPTURE_V2_BASIS_MISSING"),
            ("capture not recorded", mutate(("selected_output_capture_v2_basis", "outcome"), "NOT_RECORDED"), "OUTPUT_CAPTURE_V2_NOT_RECORDED"),
            ("capture failed checks", mutate(("selected_output_capture_v2_basis", "failed_check_count"), 1), "OUTPUT_CAPTURE_V2_FAILED_CHECKS_PRESENT"),
            ("capture wrong version", mutate(("selected_output_capture_v2_basis", "result_version"), "0.1.0"), "OUTPUT_CAPTURE_V2_VERSION_NOT_0_2_0"),
            ("capture json safe missing", mutate(("selected_output_capture_v2_basis", "json_safe_result"), False), "OUTPUT_CAPTURE_V2_JSON_SAFE_RESULT_NOT_PRESERVED"),
            ("capture predecessor missing", mutate(("selected_output_capture_v2_basis", "v1_predecessor_failure_preserved"), False), "OUTPUT_CAPTURE_V2_PREDECESSOR_FAILURE_EVIDENCE_MISSING"),
            ("capture repaired v1", mutate(("selected_output_capture_v2_basis", "v1_repaired"), True), "OUTPUT_CAPTURE_V2_REPAIRED_V1"),
            ("capture hidden v1", mutate(("selected_output_capture_v2_basis", "v1_hidden"), True), "OUTPUT_CAPTURE_V2_HID_V1"),
            ("capture claimed v1 passed", mutate(("selected_output_capture_v2_basis", "v1_claimed_passed"), True), "OUTPUT_CAPTURE_V2_CLAIMED_V1_PASSED"),
            ("capture erased v1", mutate(("selected_output_capture_v2_basis", "v2_output_capture_erased_v1"), True), "OUTPUT_CAPTURE_V2_ERASED_V1"),
            ("capture invented stdout", mutate(("selected_output_capture_v2_basis", "stdout_content_invented"), True), "OUTPUT_CAPTURE_V2_INVENTED_STDOUT_CONTENT"),
            ("capture invented stderr", mutate(("selected_output_capture_v2_basis", "stderr_content_invented"), True), "OUTPUT_CAPTURE_V2_INVENTED_STDERR_CONTENT"),
            ("capture invented process output", mutate(("selected_output_capture_v2_basis", "process_output_content_invented"), True), "OUTPUT_CAPTURE_V2_INVENTED_PROCESS_OUTPUT_CONTENT"),
            ("capture invented raw output", mutate(("selected_output_capture_v2_basis", "raw_output_body_content_invented"), True), "OUTPUT_CAPTURE_V2_INVENTED_RAW_OUTPUT_BODY_CONTENT"),
            ("execution missing", delete(("selected_post_invocation_command_execution_basis",)), "POST_INVOCATION_COMMAND_EXECUTION_BASIS_MISSING"),
            ("execution not recorded", mutate(("selected_post_invocation_command_execution_basis", "outcome"), None), "POST_INVOCATION_COMMAND_EXECUTION_NOT_RECORDED"),
            ("execution failed checks", mutate(("selected_post_invocation_command_execution_basis", "failed_check_count"), 1), "POST_INVOCATION_COMMAND_EXECUTION_FAILED_CHECKS_PRESENT"),
            ("execution trace not audit only", mutate(("selected_post_invocation_command_execution_basis", "execution_trace_audit_only"), False), "POST_INVOCATION_COMMAND_EXECUTION_TRACE_NOT_AUDIT_ONLY"),
            ("report lineage current artifact", mutate(("selected_command_report_lineage_basis", "command_report_lineage_basis_treated_as_current_report_artifact"), True), "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_CURRENT_REPORT_ARTIFACT"),
            ("report lineage result authority", mutate(("selected_command_report_lineage_basis", "command_report_lineage_basis_treated_as_command_result_authority"), True), "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_COMMAND_RESULT_AUTHORITY"),
            ("report lineage success", mutate(("selected_command_report_lineage_basis", "command_report_lineage_basis_treated_as_command_success"), True), "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_COMMAND_SUCCESS"),
            ("report lineage source", mutate(("selected_command_report_lineage_basis", "command_report_lineage_basis_treated_as_source"), True), "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_SOURCE"),
            ("report lineage authority", mutate(("selected_command_report_lineage_basis", "command_report_lineage_basis_treated_as_authority"), True), "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_AUTHORITY"),
            ("report lineage currentness", mutate(("selected_command_report_lineage_basis", "command_report_lineage_basis_treated_as_currentness"), True), "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_CURRENTNESS"),
            ("required nonclaim flipped", mutate(("declared_non_claims", "source_created"), True), "NON_CLAIM_MISSING_OR_FLIPPED"),
            ("required nonclaim missing", delete(("declared_non_claims", "source_created")), "NON_CLAIM_MISSING_OR_FLIPPED"),
        )

        for label, mutation, code in cases:
            with self.subTest(label=label):
                request = _request()
                mutation(request)
                self.assert_blocked(request, code)

    def test_non_claim_overreach_blocks_are_public(self) -> None:
        overreach_cases = {
            "command_success_treated_as_source": "COMMAND_SUCCESS_TREATED_AS_SOURCE",
            "command_success_treated_as_authority": "COMMAND_SUCCESS_TREATED_AS_AUTHORITY",
            "command_success_treated_as_currentness": "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS",
            "command_success_treated_as_final_completion": "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION",
            "command_success_treated_as_public_readiness": "COMMAND_SUCCESS_TREATED_AS_PUBLIC_READINESS",
            "command_success_treated_as_deployment_readiness": "COMMAND_SUCCESS_TREATED_AS_DEPLOYMENT_READINESS",
            "command_success_treated_as_operation_permission": "COMMAND_SUCCESS_TREATED_AS_OPERATION_PERMISSION",
            "command_success_treated_as_continuation": "COMMAND_SUCCESS_TREATED_AS_CONTINUATION",
            "command_success_treated_as_reusable_permission": "COMMAND_SUCCESS_TREATED_AS_REUSABLE_PERMISSION",
            "command_success_treated_as_derivative_reception": "COMMAND_SUCCESS_TREATED_AS_DERIVATIVE_RECEPTION",
            "command_success_treated_as_vessel_relation": "COMMAND_SUCCESS_TREATED_AS_VESSEL_RELATION",
            "command_success_treated_as_another_reception_request": "COMMAND_SUCCESS_TREATED_AS_ANOTHER_RECEPTION_REQUEST",
            "command_success_treated_as_follow_on_work": "COMMAND_SUCCESS_TREATED_AS_FOLLOW_ON_WORK",
            "success_body_invented": "SUCCESS_BODY_INVENTED",
            "source_created": "SOURCE_CREATED",
            "authority_created": "AUTHORITY_CREATED",
            "currentness_created": "CURRENTNESS_CREATED",
            "final_completion_claimed": "FINAL_COMPLETION_CLAIMED",
            "public_readiness_created": "PUBLIC_READINESS_CREATED",
            "deployment_readiness_created": "DEPLOYMENT_READINESS_CREATED",
            "operation_permission_created": "OPERATION_PERMISSION_CREATED",
            "continuation_authorized": "CONTINUATION_AUTHORIZED",
            "reusable_permission_created": "REUSABLE_PERMISSION_CREATED",
            "derivative_reception_authorized": "DERIVATIVE_RECEPTION_AUTHORIZED",
            "vessel_relation_authorized": "VESSEL_RELATION_AUTHORIZED",
            "another_reception_request_authorized": "ANOTHER_RECEPTION_REQUEST_AUTHORIZED",
            "follow_on_work_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
            "source_inference_made": "SOURCE_INFERENCE_MADE",
            "authority_inference_made": "AUTHORITY_INFERENCE_MADE",
            "currentness_inference_made": "CURRENTNESS_INFERENCE_MADE",
            "final_completion_inference_made": "FINAL_COMPLETION_INFERENCE_MADE",
            "public_readiness_inference_made": "PUBLIC_READINESS_INFERENCE_MADE",
            "deployment_readiness_inference_made": "DEPLOYMENT_READINESS_INFERENCE_MADE",
            "operation_permission_inference_made": "OPERATION_PERMISSION_INFERENCE_MADE",
            "follow_on_work_inference_made": "FOLLOW_ON_WORK_INFERENCE_MADE",
            "unbounded_pass_fail_inference_made": "UNBOUNDED_PASS_FAIL_INFERENCE_MADE",
            "execution_trace_treated_as_success": "EXECUTION_TRACE_TREATED_AS_SUCCESS",
            "execution_trace_treated_as_source": "EXECUTION_TRACE_TREATED_AS_SOURCE",
            "execution_trace_treated_as_authority": "EXECUTION_TRACE_TREATED_AS_AUTHORITY",
            "execution_trace_treated_as_currentness": "EXECUTION_TRACE_TREATED_AS_CURRENTNESS",
            "execution_trace_treated_as_final_completion": "EXECUTION_TRACE_TREATED_AS_FINAL_COMPLETION",
            "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
            "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
            "prior_artifacts_mutated": "ARTIFACTS_MUTATED",
            "deployment_created": "DEPLOYMENT_CREATED",
            "runtime_hosting_created": "RUNTIME_HOSTING_CREATED",
            "public_release_created": "PUBLIC_RELEASE_CREATED",
        }
        for field, code in overreach_cases.items():
            with self.subTest(field=field):
                request = _request()
                request["declared_non_claims"][field] = True
                result = self.assert_blocked(request)
                emitted_codes = {
                    check.get("block_code") or check.get("failure_code")
                    for check in result["command_success_checks"]
                    if check.get("block_code") or check.get("failure_code")
                }
                self.assertIn("NON_CLAIM_MISSING_OR_FLIPPED", emitted_codes)
                self.assertIn(code, emitted_codes)

    def test_missing_and_non_mapping_requests_block(self) -> None:
        self.assert_blocked(None, "DECLARED_COMMAND_SUCCESS_REQUEST_MALFORMED")
        self.assert_blocked(["not", "a", "mapping"], "DECLARED_COMMAND_SUCCESS_REQUEST_MALFORMED")  # type: ignore[arg-type]

    def test_path_and_write_behavior(self) -> None:
        request = _request()
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request_path = tmp_path / "request.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")

            result = resolver.resolve_portable_source_body_verification_command_success_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], RECORDED)
            metadata = result["portable_source_body_verification_command_success_metadata"]
            self.assertEqual(
                metadata["portable_source_body_verification_command_success_result_version"],
                "0.1.0",
            )
            self.assertEqual(
                metadata["resolver_module"],
                "resolve_portable_source_body_verification_command_success",
            )

            malformed = tmp_path / "malformed.json"
            malformed.write_text("{not-json", encoding="utf-8")
            with self.assertRaises(resolver.PortableSourceBodyVerificationCommandSuccessError):
                resolver.resolve_portable_source_body_verification_command_success_from_path(
                    malformed
                )

            array_path = tmp_path / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            with self.assertRaises(resolver.PortableSourceBodyVerificationCommandSuccessError):
                resolver.resolve_portable_source_body_verification_command_success_from_path(
                    array_path
                )

            missing = tmp_path / "missing.json"
            with self.assertRaises(resolver.PortableSourceBodyVerificationCommandSuccessError):
                resolver.resolve_portable_source_body_verification_command_success_from_path(
                    missing
                )

            redirected_root = (
                tmp_path
                / "artifacts"
                / "integrity_host_v0_min_coexistence_portable_source_body_verification_command_success"
            )
            with patch.object(resolver, "OUTPUT_ROOT", redirected_root):
                written = resolver.write_portable_source_body_verification_command_success_result(
                    result
                )
                written_again = resolver.write_portable_source_body_verification_command_success_result(
                    result
                )

            self.assertTrue(written.exists())
            self.assertTrue(written_again.exists())
            self.assertNotEqual(written, written_again)
            self.assertEqual(written.parent, redirected_root)
            parsed = json.loads(written.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], RECORDED)
            self.assertIn(
                "integrity_host_v0_min_coexistence_portable_source_body_verification_command_success",
                str(written),
            )
            self.assertNotIn("command_success_boundary_v3", str(written))
            self.assertNotIn("command_result_v2", str(written))
            self.assertNotIn("manifest", str(written))
            self.assertNotIn("checksum", str(written))
            self.assertNotIn("signature", str(written))
            self.assertNotIn("packet", str(written))
            self.assertNotIn("deployment", str(written))
            self.assertNotIn("runtime", str(written))
            self.assertNotIn("public_release", str(written))

    def test_resolver_does_not_mutate_request_or_selected_basis(self) -> None:
        request = _request()
        original = copy.deepcopy(request)
        result = _resolve(request)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(request, original)
        for key in (
            "selected_command_success_boundary_v3_basis",
            "selected_command_success_boundary_v3_terminal_summary_basis",
            "selected_command_success_boundary_v1_predecessor_failure_basis",
            "selected_command_success_boundary_v2_predecessor_failure_basis",
            "selected_command_success_boundary_spec_basis",
            "selected_command_result_v2_basis",
            "selected_command_result_v1_predecessor_failure_basis",
            "selected_command_output_report_artifact_basis",
            "selected_output_capture_v2_basis",
            "selected_output_capture_v1_predecessor_failure_basis",
            "selected_post_invocation_command_execution_basis",
            "selected_command_report_lineage_basis",
            "command_success_only_posture",
            "one_bounded_command_success_posture",
            "declared_non_claims",
        ):
            self.assertEqual(request[key], original[key], key)

    def test_raw_full_body_containment(self) -> None:
        request = _request()
        for key in (
            "selected_command_success_boundary_v3_basis",
            "selected_command_result_v2_basis",
            "selected_command_output_report_artifact_basis",
            "selected_output_capture_v2_basis",
            "selected_command_report_lineage_basis",
        ):
            request[key].update(
                raw_body=HOSTILE_RAW_VALUE,
                raw_full_body=HOSTILE_RAW_VALUE,
                full_body=HOSTILE_RAW_VALUE,
                artifact_body=HOSTILE_RAW_VALUE,
                raw_result_body=HOSTILE_RAW_VALUE,
                raw_report_body=HOSTILE_RAW_VALUE,
                raw_output_body=HOSTILE_RAW_VALUE,
                success_body=HOSTILE_RAW_VALUE,
                source_body=HOSTILE_RAW_VALUE,
                authority_body=HOSTILE_RAW_VALUE,
                currentness_claim=HOSTILE_RAW_VALUE,
                final_completion_claim=HOSTILE_RAW_VALUE,
                nested_raw={"nested": [RAW_SENTINEL, HOSTILE_RAW_VALUE]},
            )

        original = copy.deepcopy(request)
        result = _resolve(request)
        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assert_public_codes(result)
        self.assert_no_raw_sentinels(result)
        self.assert_no_collapse(result)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
