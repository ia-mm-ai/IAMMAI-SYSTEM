"""Tests for command-success-boundary v2 raw-body containment.

This suite treats the v1 command-success-boundary resolver as preserved
predecessor conformance-failure evidence. V2 is an additive successor that
keeps the same command-success-boundary law while preventing raw selected-basis
body material from being returned. It records one future command success
boundary only; it does not create command success, success body, authority,
currentness, final completion, public readiness, deployment readiness,
operation permission, continuation, reusable permission, or follow-on work.
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

import resolve_portable_source_body_verification_command_success_boundary_v2 as resolver


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_COMMAND_SUCCESS_BOUNDARY_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
RAW_BODY_SENTINEL = "RAW_COMMAND_SUCCESS_BOUNDARY_BODY_MUST_NOT_RETURN"
HOSTILE_FULL_BODY = "HOSTILE_FULL_BODY_VALUE_MUST_NOT_RETURN"
HOSTILE_RAW_VALUE = "RAW_SELECTED_BASIS_BODY_VALUE_MUST_NOT_RETURN"

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_command_success_boundary_metadata",
    "declared_command_success_boundary_question",
    "selected_command_result_v2_basis",
    "selected_command_result_v2_terminal_summary_basis",
    "selected_command_result_v1_predecessor_failure_basis",
    "selected_command_result_boundary_basis",
    "selected_command_result_boundary_terminal_summary_basis",
    "selected_command_output_report_artifact_basis",
    "selected_command_output_report_artifact_terminal_summary_basis",
    "selected_command_output_report_artifact_boundary_basis",
    "selected_command_output_report_artifact_boundary_terminal_summary_basis",
    "selected_output_capture_v2_basis",
    "selected_output_capture_v2_terminal_summary_basis",
    "selected_output_capture_v1_predecessor_failure_basis",
    "selected_output_capture_boundary_basis",
    "selected_command_output_basis",
    "selected_command_output_boundary_basis",
    "selected_command_output_containment_basis",
    "selected_post_invocation_command_execution_basis",
    "selected_post_invocation_command_execution_terminal_summary_basis",
    "selected_command_invocation_basis",
    "selected_command_execution_review_basis",
    "selected_request_consumption_basis",
    "selected_consumed_request_basis",
    "selected_v2_admitted_request_basis",
    "selected_v1_predecessor_failure_basis",
    "selected_older_command_execution_boundary_lineage_basis",
    "selected_command_report_lineage_basis",
    "selected_command_implementation_boundary_basis",
    "selected_command_boundary_basis",
    "selected_artifact_emission_containment_basis",
    "selected_evidence_manifest_basis",
    "selected_portable_verification_basis",
    "command_success_boundary_only_posture",
    "one_future_command_success_step_posture",
    "command_result_v2_basis_preserved_posture",
    "bounded_command_result_preserved_posture",
    "command_result_v1_predecessor_failure_preserved_posture",
    "command_result_boundary_basis_preserved_posture",
    "command_output_report_artifact_basis_preserved_posture",
    "bounded_command_output_report_artifact_preserved_posture",
    "command_output_report_artifact_boundary_basis_preserved_posture",
    "output_capture_v2_basis_preserved_posture",
    "output_capture_v1_predecessor_failure_preserved_posture",
    "bounded_output_capture_event_preserved_posture",
    "command_output_basis_preserved_posture",
    "execution_trace_audit_only_posture",
    "report_body_absent_or_bounded_posture",
    "result_body_absent_or_bounded_posture",
    "no_report_body_invented_posture",
    "no_result_body_invented_posture",
    "no_success_body_invented_posture",
    "no_command_success_posture",
    "no_success_inference_posture",
    "no_currentness_inference_posture",
    "no_final_completion_inference_posture",
    "no_public_readiness_inference_posture",
    "no_deployment_readiness_inference_posture",
    "no_authority_inference_posture",
    "no_follow_on_work_inference_posture",
    "no_unbounded_pass_fail_inference_posture",
    "no_success_as_currentness_posture",
    "no_success_as_final_completion_posture",
    "no_final_completion_posture",
    "authorization_token_reuse_blocked_posture",
    "consumed_token_closed_posture",
    "no_reopen_consumed_request_posture",
    "returned_result_containment_posture",
    "command_success_boundary_scope",
    "command_success_boundary_checks",
    "command_success_boundary_statement",
    "command_success_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_command_success_boundary_summary",
)

TRUE_RECORDED_FIELDS = (
    "command_success_boundary_recorded",
    "one_future_command_success_step_declared",
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
    "report_body_not_invented",
    "result_body_not_invented",
    "success_body_not_invented",
    "command_success_still_not_created",
    "success_inference_blocked",
    "currentness_inference_blocked",
    "final_completion_inference_blocked",
    "public_readiness_inference_blocked",
    "deployment_readiness_inference_blocked",
    "authority_inference_blocked",
    "follow_on_work_inference_blocked",
    "unbounded_pass_fail_inference_blocked",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
    "returned_result_containment_preserved",
)

REPRESENTATIVE_BLOCK_CODES = (
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    "COMMAND_RESULT_V2_BASIS_MISSING",
    "COMMAND_RESULT_V2_VERSION_NOT_0_2_0",
    "COMMAND_RESULT_V2_PREDECESSOR_FAILURE_EVIDENCE_MISSING",
    "COMMAND_SUCCESS_BOUNDARY_TREATED_AS_SUCCESS",
    "SUCCESS_BODY_INVENTED",
    "COMMAND_SUCCESS_CREATED",
    "SUCCESS_INFERENCE_MADE",
    "CURRENTNESS_INFERENCE_MADE",
    "FINAL_COMPLETION_INFERENCE_MADE",
    "PUBLIC_READINESS_INFERENCE_MADE",
    "DEPLOYMENT_READINESS_INFERENCE_MADE",
    "AUTHORITY_INFERENCE_MADE",
    "FOLLOW_ON_WORK_INFERENCE_MADE",
    "UNBOUNDED_PASS_FAIL_INFERENCE_MADE",
    "UNSUPPORTED_COMMAND_SUCCESS_BOUNDARY_SCOPE",
)

RAW_VALUE_PATTERNS = (
    '"raw_body":',
    '"raw_full_body":',
    '"full_body":',
    '"artifact_body":',
    '"raw_command_success_boundary_body":',
    '"raw_result_body":',
    '"raw_report_body":',
    '"raw_output_body":',
    '"success_body":',
    '"source_body":',
    '"authority_body":',
    '"currentness_claim":',
    '"final_completion_claim":',
)


def _json_text(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=True)


def _request(**overrides: Any) -> dict[str, Any]:
    request = (
        resolver.build_declared_portable_source_body_verification_command_success_boundary_v2_request()
    )
    request["command_success_boundary_scope"] = list(SUPPORTED_SCOPE)
    request["declared_non_claims"] = {key: False for key in REQUIRED_FALSE_NON_CLAIMS}
    request.update(overrides)
    return request


def _set_path(mapping: dict[str, Any], dotted_path: str, value: Any) -> None:
    target = mapping
    parts = dotted_path.split(".")
    for part in parts[:-1]:
        target = target[part]
    target[parts[-1]] = value


def _delete_path(mapping: dict[str, Any], dotted_path: str) -> None:
    target = mapping
    parts = dotted_path.split(".")
    for part in parts[:-1]:
        target = target[part]
    del target[parts[-1]]


def _mutated(mutator: Callable[[dict[str, Any]], None]) -> dict[str, Any]:
    request = _request()
    mutator(request)
    return request


class CommandSuccessBoundaryV2ResolverTests(unittest.TestCase):
    def assert_public_block_codes(self, result: Mapping[str, Any]) -> None:
        block = result.get("block") or {}
        if block.get("block_code") is not None:
            self.assertIn(block["block_code"], resolver.BLOCK_CODES)
        for check in result.get("command_success_boundary_checks", []):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_v2_metadata(self, result: Mapping[str, Any]) -> None:
        metadata = result["portable_source_body_verification_command_success_boundary_metadata"]
        self.assertEqual(metadata["result_version"], "0.2.0")
        self.assertEqual(
            metadata["portable_source_body_verification_command_success_boundary_result_version"],
            "0.2.0",
        )
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_portable_source_body_verification_command_success_boundary_v2",
        )
        self.assertEqual(
            metadata["successor_of"],
            "resolve_portable_source_body_verification_command_success_boundary",
        )
        successor_reason = metadata["successor_reason"]
        self.assertIn("raw", successor_reason.lower())
        self.assertIn("body", successor_reason.lower())
        self.assertIn("containment", successor_reason.lower())
        self.assertNotIn(RAW_BODY_SENTINEL, successor_reason)
        self.assertIs(metadata["v1_predecessor_failure_preserved"], True)
        self.assertIs(metadata["v1_repaired"], False)
        self.assertIs(metadata["v1_hidden"], False)
        self.assertIs(metadata["v1_claimed_passed"], False)
        self.assertIs(metadata["v2_successor_does_not_erase_v1"], True)
        self.assertIs(metadata["returned_result_containment_preserved"], True)
        self.assertIs(metadata["selected_basis_reference_shape_preserved"], True)
        self.assertIs(metadata["raw_full_prior_artifact_body_returned"], False)

    def assert_no_success_or_follow_on(self, result: Mapping[str, Any]) -> None:
        statement = result.get("command_success_boundary_statement", {})
        non_claims = result.get("non_claims", {})
        for key in (
            "command_success_created",
            "success_body_invented",
            "success_inference_made",
            "currentness_inference_made",
            "final_completion_inference_made",
            "public_readiness_inference_made",
            "deployment_readiness_inference_made",
            "authority_inference_made",
            "follow_on_work_inference_made",
            "unbounded_pass_fail_inference_made",
            "authorization_token_reused",
            "consumed_request_reopened",
            "deployment_created",
            "runtime_hosting_created",
            "public_release_created",
            "operation_permission_created",
            "final_completion_claimed",
            "continuation_authorized",
            "reusable_permission_created",
            "follow_on_work_authorized",
            "raw_full_prior_artifact_body_returned",
        ):
            self.assertFalse(non_claims.get(key), key)
            self.assertFalse(statement.get(key), key)

    def assert_no_raw_body_material(self, result: Mapping[str, Any]) -> None:
        text = _json_text(result)
        for value in (RAW_BODY_SENTINEL, HOSTILE_FULL_BODY, HOSTILE_RAW_VALUE):
            self.assertNotIn(value, text)
        for pattern in RAW_VALUE_PATTERNS:
            self.assertNotIn(pattern, text)

    def test_public_api_constants_and_block_codes(self) -> None:
        for name in (
            "resolve_portable_source_body_verification_command_success_boundary_v2",
            "resolve_portable_source_body_verification_command_success_boundary_v2_from_path",
            "write_portable_source_body_verification_command_success_boundary_v2_result",
            "build_portable_source_body_verification_command_success_boundary_v2_summary",
            "build_declared_portable_source_body_verification_command_success_boundary_v2_request",
        ):
            self.assertTrue(callable(getattr(resolver, name, None)), name)
        for name in (
            "resolve_portable_source_body_verification_command_success_boundary",
            "resolve_portable_source_body_verification_command_success_boundary_from_path",
            "write_portable_source_body_verification_command_success_boundary_result",
            "build_portable_source_body_verification_command_success_boundary_summary",
        ):
            self.assertTrue(callable(getattr(resolver, name, None)), name)
        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "RESULT_VERSION",
            "OUTPUT_ROOT",
            "SUPPORTED_COMMAND_SUCCESS_BOUNDARY_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)
        self.assertEqual(resolver.RESULT_VERSION, "0.2.0")
        self.assertTrue(
            resolver.OUTPUT_ROOT.as_posix().endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_portable_source_body_verification_"
                "command_success_boundary_v2"
            )
        )
        self.assertTrue(set(REPRESENTATIVE_BLOCK_CODES).issubset(resolver.BLOCK_CODES))

        alias_result = resolver.resolve_portable_source_body_verification_command_success_boundary(
            declared_command_success_boundary_request=_request()
        )
        self.assertEqual(alias_result["outcome"], RECORDED)
        self.assert_v2_metadata(alias_result)
        alias_summary = resolver.build_portable_source_body_verification_command_success_boundary_summary(
            alias_result
        )
        self.assertEqual(
            alias_summary["resolver_module"],
            "resolve_portable_source_body_verification_command_success_boundary_v2",
        )

    def test_successful_v2_command_success_boundary_recorded_result(self) -> None:
        request = _request()
        request["selected_command_result_v2_basis"]["synthetic_nested_reference"] = {
            "path": "synthetic://command-result-v2-small-reference.json",
            "basis_reference": "synthetic://command-result-v2-small-reference",
        }
        result = resolver.resolve_portable_source_body_verification_command_success_boundary_v2(
            declared_command_success_boundary_request=request
        )

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        metadata = result["portable_source_body_verification_command_success_boundary_metadata"]
        self.assertEqual(metadata["failed_check_count"], 0)
        self.assertIsNone((result.get("block") or {}).get("block_code"))
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        self.assert_public_block_codes(result)
        self.assert_v2_metadata(result)

        selected_v2 = result["selected_command_result_v2_basis"]
        self.assertEqual(
            selected_v2["outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_RECORDED",
        )
        self.assertEqual(selected_v2["result_version"], "0.2.0")
        self.assertEqual(selected_v2["failed_check_count"], 0)
        self.assertTrue(selected_v2["successor_metadata_preserved"])
        self.assertEqual(
            selected_v2["successor_of"],
            "resolve_portable_source_body_verification_command_result",
        )
        self.assertTrue(selected_v2["v1_predecessor_failure_preserved"])
        self.assertFalse(selected_v2["v1_repaired"])
        self.assertFalse(selected_v2["v1_hidden"])
        self.assertFalse(selected_v2["v1_claimed_passed"])
        self.assertTrue(selected_v2["v2_successor_does_not_erase_v1"])
        self.assertTrue(selected_v2["bounded_command_result_recorded"])
        self.assertFalse(selected_v2["command_success_created"])

        statement = result["command_success_boundary_statement"]
        summary = result["portable_source_body_verification_command_success_boundary_summary"]
        for key in TRUE_RECORDED_FIELDS:
            self.assertIs(statement.get(key), True, key)
            self.assertIs(summary.get(key), True, key)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, result["non_claims"])
            self.assertIs(result["non_claims"][key], False, key)
        for key in (
            "command_success_created",
            "success_body_invented",
            "success_inference_made",
            "currentness_inference_made",
            "final_completion_inference_made",
            "public_readiness_inference_made",
            "deployment_readiness_inference_made",
            "authority_inference_made",
            "follow_on_work_inference_made",
            "unbounded_pass_fail_inference_made",
            "command_success_boundary_treated_as_success",
            "command_success_boundary_treated_as_source",
            "command_success_boundary_treated_as_authority",
            "command_success_boundary_treated_as_currentness",
            "command_success_boundary_treated_as_final_completion",
            "command_success_boundary_treated_as_public_readiness",
            "command_success_boundary_treated_as_deployment_readiness",
            "raw_full_prior_artifact_body_returned",
        ):
            self.assertIs(result["non_claims"][key], False, key)
        self.assert_no_success_or_follow_on(result)
        self.assert_no_raw_body_material(result)

    def test_raw_full_body_sentinel_is_contained_without_mutating_input(self) -> None:
        request = _request(command_success_boundary_request_id="raw_body_containment_v2")
        request["selected_command_result_v2_basis"]["raw_body"] = RAW_BODY_SENTINEL
        request["selected_command_result_v2_basis"]["raw_full_body"] = HOSTILE_FULL_BODY
        request["selected_command_result_boundary_basis"]["full_body"] = HOSTILE_RAW_VALUE
        request["selected_command_result_boundary_basis"]["nested"] = [
            {"raw_command_success_boundary_body": RAW_BODY_SENTINEL}
        ]
        request["selected_command_output_report_artifact_basis"]["artifact_body"] = HOSTILE_FULL_BODY
        request["selected_output_capture_v2_basis"]["raw_output_body"] = RAW_BODY_SENTINEL
        request["selected_command_report_lineage_basis"]["raw_result_body"] = HOSTILE_RAW_VALUE
        request["selected_command_report_lineage_basis"]["raw_report_body"] = RAW_BODY_SENTINEL
        request["selected_command_report_lineage_basis"]["success_body"] = HOSTILE_FULL_BODY
        request["selected_command_report_lineage_basis"]["source_body"] = RAW_BODY_SENTINEL
        request["selected_command_report_lineage_basis"]["authority_body"] = HOSTILE_RAW_VALUE
        request["selected_command_report_lineage_basis"]["currentness_claim"] = RAW_BODY_SENTINEL
        request["selected_command_report_lineage_basis"]["final_completion_claim"] = HOSTILE_FULL_BODY
        before = copy.deepcopy(request)

        result = resolver.resolve_portable_source_body_verification_command_success_boundary_v2(
            declared_command_success_boundary_request=request
        )

        self.assertEqual(request, before)
        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assert_v2_metadata(result)
        self.assert_public_block_codes(result)
        self.assert_no_success_or_follow_on(result)
        self.assert_no_raw_body_material(result)
        if result["outcome"] == BLOCKED:
            self.assertIsNotNone((result.get("block") or {}).get("block_code"))
        else:
            self.assertEqual(result["outcome"], RECORDED)

    def test_representative_blocking_behavior_preserves_v2_metadata(self) -> None:
        block_cases: tuple[tuple[str, Any], ...] = (
            ("explicit block intent", lambda request: _set_path(request, "command_success_boundary_intent", resolver.INTENT_BLOCK)),
            ("missing request", None),
            ("non-mapping request", ["not", "mapping"]),
            ("unsupported intent", lambda request: _set_path(request, "command_success_boundary_intent", "UNSUPPORTED_INTENT")),
            ("unsupported scope", lambda request: _set_path(request, "command_success_boundary_scope", ["UNSUPPORTED_SCOPE"])),
            ("missing command result v2 basis", lambda request: _delete_path(request, "selected_command_result_v2_basis")),
            ("command result v2 not recorded", lambda request: _set_path(request, "selected_command_result_v2_basis.outcome", "NOT_RECORDED")),
            ("command result v2 failed checks", lambda request: _set_path(request, "selected_command_result_v2_basis.failed_check_count", 1)),
            ("command result v2 version wrong", lambda request: _set_path(request, "selected_command_result_v2_basis.result_version", "0.1.0")),
            ("command result v2 successor metadata missing", lambda request: _set_path(request, "selected_command_result_v2_basis.successor_metadata_preserved", False)),
            ("command result v2 predecessor missing", lambda request: _set_path(request, "selected_command_result_v2_basis.v1_predecessor_failure_preserved", False)),
            ("command result v2 repaired v1", lambda request: _set_path(request, "selected_command_result_v2_basis.v1_repaired", True)),
            ("command result v2 hid v1", lambda request: _set_path(request, "selected_command_result_v2_basis.v1_hidden", True)),
            ("command result v2 claimed v1 passed", lambda request: _set_path(request, "selected_command_result_v2_basis.v1_claimed_passed", True)),
            ("command result v2 erased v1", lambda request: _set_path(request, "selected_command_result_v2_basis.v2_successor_does_not_erase_v1", False)),
            ("command result v2 not bounded", lambda request: _set_path(request, "selected_command_result_v2_basis.bounded_command_result_recorded", False)),
            ("command result v2 already created success", lambda request: _set_path(request, "selected_command_result_v2_basis.command_success_created", True)),
            ("command result v2 inferred success", lambda request: _set_path(request, "selected_command_result_v2_inferred_success", True)),
            ("command result v2 inferred currentness", lambda request: _set_path(request, "selected_command_result_v2_inferred_currentness", True)),
            ("command result v2 inferred final completion", lambda request: _set_path(request, "selected_command_result_v2_inferred_final_completion", True)),
            ("command result v2 inferred public readiness", lambda request: _set_path(request, "selected_command_result_v2_inferred_public_readiness", True)),
            ("command result v2 inferred deployment readiness", lambda request: _set_path(request, "selected_command_result_v2_inferred_deployment_readiness", True)),
            ("command result v2 inferred authority", lambda request: _set_path(request, "selected_command_result_v2_inferred_authority", True)),
            ("command result v2 inferred follow-on", lambda request: _set_path(request, "selected_command_result_v2_inferred_follow_on_work", True)),
            ("command result v2 inferred unbounded pass/fail", lambda request: _set_path(request, "selected_command_result_v2_inferred_unbounded_pass_fail", True)),
            ("command result treated as success", lambda request: _set_path(request, "command_result_v2_treated_result_as_success", True)),
            ("command result treated as source", lambda request: _set_path(request, "command_result_v2_treated_result_as_source", True)),
            ("command result treated as authority", lambda request: _set_path(request, "command_result_v2_treated_result_as_authority", True)),
            ("command result treated as currentness", lambda request: _set_path(request, "command_result_v2_treated_result_as_currentness", True)),
            ("command result treated as final completion", lambda request: _set_path(request, "command_result_v2_treated_result_as_final_completion", True)),
            ("command result treated as public readiness", lambda request: _set_path(request, "command_result_v2_treated_result_as_public_readiness", True)),
            ("command result treated as deployment readiness", lambda request: _set_path(request, "command_result_v2_treated_result_as_deployment_readiness", True)),
            ("command result boundary missing", lambda request: _delete_path(request, "selected_command_result_boundary_basis")),
            ("command result boundary not recorded", lambda request: _set_path(request, "selected_command_result_boundary_basis.outcome", "NOT_RECORDED")),
            ("command result boundary failed", lambda request: _set_path(request, "selected_command_result_boundary_basis.failed_check_count", 1)),
            ("command output/report artifact missing", lambda request: _delete_path(request, "selected_command_output_report_artifact_basis")),
            ("command output/report artifact not recorded", lambda request: _set_path(request, "selected_command_output_report_artifact_basis.outcome", "NOT_RECORDED")),
            ("command output/report artifact failed", lambda request: _set_path(request, "selected_command_output_report_artifact_basis.failed_check_count", 1)),
            ("command output/report artifact already success", lambda request: _set_path(request, "selected_command_output_report_artifact_basis.command_success_created", True)),
            ("command output/report artifact result authority", lambda request: _set_path(request, "command_output_report_artifact_treated_as_result_authority", True)),
            ("command output/report artifact success", lambda request: _set_path(request, "command_output_report_artifact_treated_as_success", True)),
            ("output capture v2 missing", lambda request: _delete_path(request, "selected_output_capture_v2_basis")),
            ("output capture v2 not recorded", lambda request: _set_path(request, "selected_output_capture_v2_basis.outcome", "NOT_RECORDED")),
            ("output capture v2 failed", lambda request: _set_path(request, "selected_output_capture_v2_basis.failed_check_count", 1)),
            ("output capture v2 wrong version", lambda request: _set_path(request, "selected_output_capture_v2_basis.result_version", "0.1.0")),
            ("output capture v2 JSON-safe missing", lambda request: _set_path(request, "selected_output_capture_v2_basis.json_safe_result", False)),
            ("output capture v2 predecessor missing", lambda request: _set_path(request, "selected_output_capture_v2_basis.v1_predecessor_failure_preserved", False)),
            ("output capture v2 repaired v1", lambda request: _set_path(request, "selected_output_capture_v2_basis.v1_repaired", True)),
            ("output capture v2 hid v1", lambda request: _set_path(request, "selected_output_capture_v2_basis.v1_hidden", True)),
            ("output capture v2 claimed v1 passed", lambda request: _set_path(request, "selected_output_capture_v2_basis.v1_claimed_passed", True)),
            ("output capture v2 erased v1", lambda request: _set_path(request, "selected_output_capture_v2_basis.v2_successor_does_not_erase_v1", False)),
            ("output capture invented stdout", lambda request: _set_path(request, "selected_output_capture_v2_basis.stdout_content_invented", True)),
            ("output capture invented stderr", lambda request: _set_path(request, "selected_output_capture_v2_basis.stderr_content_invented", True)),
            ("output capture invented process output", lambda request: _set_path(request, "selected_output_capture_v2_basis.process_output_content_invented", True)),
            ("output capture invented raw output body", lambda request: _set_path(request, "selected_output_capture_v2_basis.raw_output_body_content_invented", True)),
            ("success boundary treated as success", lambda request: _set_path(request, "command_success_boundary_treated_as_success", True)),
            ("success boundary treated as source", lambda request: _set_path(request, "command_success_boundary_treated_as_source", True)),
            ("success boundary treated as authority", lambda request: _set_path(request, "command_success_boundary_treated_as_authority", True)),
            ("success boundary treated as currentness", lambda request: _set_path(request, "command_success_boundary_treated_as_currentness", True)),
            ("success boundary treated as final completion", lambda request: _set_path(request, "command_success_boundary_treated_as_final_completion", True)),
            ("success boundary treated as public readiness", lambda request: _set_path(request, "command_success_boundary_treated_as_public_readiness", True)),
            ("success boundary treated as deployment readiness", lambda request: _set_path(request, "command_success_boundary_treated_as_deployment_readiness", True)),
            ("success body invented", lambda request: _set_path(request, "success_body_invented", True)),
            ("command success created", lambda request: _set_path(request, "command_success_created", True)),
            ("success inference made", lambda request: _set_path(request, "success_inference_made", True)),
            ("currentness inference made", lambda request: _set_path(request, "currentness_inference_made", True)),
            ("final completion inference made", lambda request: _set_path(request, "final_completion_inference_made", True)),
            ("public readiness inference made", lambda request: _set_path(request, "public_readiness_inference_made", True)),
            ("deployment readiness inference made", lambda request: _set_path(request, "deployment_readiness_inference_made", True)),
            ("authority inference made", lambda request: _set_path(request, "authority_inference_made", True)),
            ("follow-on inference made", lambda request: _set_path(request, "follow_on_work_inference_made", True)),
            ("unbounded pass/fail inference made", lambda request: _set_path(request, "unbounded_pass_fail_inference_made", True)),
            ("execution trace treated as success", lambda request: _set_path(request, "execution_trace_treated_as_success", True)),
            ("execution trace treated as source", lambda request: _set_path(request, "execution_trace_treated_as_source", True)),
            ("execution trace treated as authority", lambda request: _set_path(request, "execution_trace_treated_as_authority", True)),
            ("execution trace treated as currentness", lambda request: _set_path(request, "execution_trace_treated_as_currentness", True)),
            ("execution trace treated as final completion", lambda request: _set_path(request, "execution_trace_treated_as_final_completion", True)),
            ("command success treated as authority", lambda request: _set_path(request, "command_success_treated_as_authority", True)),
            ("command success treated as currentness", lambda request: _set_path(request, "command_success_treated_as_currentness", True)),
            ("command success treated as final completion", lambda request: _set_path(request, "command_success_treated_as_final_completion", True)),
            ("command success treated as public readiness", lambda request: _set_path(request, "command_success_treated_as_public_readiness", True)),
            ("command success treated as deployment readiness", lambda request: _set_path(request, "command_success_treated_as_deployment_readiness", True)),
            ("consumed request reopened", lambda request: _set_path(request, "consumed_request_reopened", True)),
            ("authorization token reused", lambda request: _set_path(request, "authorization_token_reused", True)),
            ("command report lineage current artifact", lambda request: _set_path(request, "selected_command_report_lineage_basis.command_report_lineage_basis_treated_as_current_report_artifact", True)),
            ("command report lineage result authority", lambda request: _set_path(request, "selected_command_report_lineage_basis.command_report_lineage_basis_treated_as_command_result_authority", True)),
            ("command report lineage success", lambda request: _set_path(request, "selected_command_report_lineage_basis.command_report_lineage_basis_treated_as_command_success", True)),
            ("command report lineage source", lambda request: _set_path(request, "selected_command_report_lineage_basis.command_report_lineage_basis_treated_as_source", True)),
            ("command report lineage authority", lambda request: _set_path(request, "selected_command_report_lineage_basis.command_report_lineage_basis_treated_as_authority", True)),
            ("command report lineage currentness", lambda request: _set_path(request, "selected_command_report_lineage_basis.command_report_lineage_basis_treated_as_currentness", True)),
            ("full prior artifact body emitted", lambda request: _set_path(request, "selected_command_report_lineage_basis.full_prior_artifact_body", RAW_BODY_SENTINEL)),
            ("artifacts mutated", lambda request: _set_path(request, "prior_artifacts_mutated", True)),
            ("deployment created", lambda request: _set_path(request, "deployment_created", True)),
            ("runtime hosting created", lambda request: _set_path(request, "runtime_hosting_created", True)),
            ("public release created", lambda request: _set_path(request, "public_release_created", True)),
            ("operation created", lambda request: _set_path(request, "operation_permission_created", True)),
            ("public readiness created", lambda request: _set_path(request, "public_launch_readiness_created", True)),
            ("deployment readiness created", lambda request: _set_path(request, "deployment_readiness_created", True)),
            ("final completion claimed", lambda request: _set_path(request, "final_completion_claimed", True)),
            ("continuation authorized", lambda request: _set_path(request, "continuation_authorized", True)),
            ("reusable permission created", lambda request: _set_path(request, "reusable_permission_created", True)),
            ("follow-on authorized", lambda request: _set_path(request, "follow_on_work_authorized", True)),
            ("mutation performed", lambda request: _set_path(request, "mutation_performed", True)),
            ("replay performed", lambda request: _set_path(request, "replay_performed", True)),
            ("merge performed", lambda request: _set_path(request, "merge_performed", True)),
            ("required non-claim missing", lambda request: _delete_path(request, f"declared_non_claims.{REQUIRED_FALSE_NON_CLAIMS[0]}")),
        )

        for label, mutator in block_cases:
            with self.subTest(label=label):
                if mutator is None or not callable(mutator):
                    request = mutator
                else:
                    request = _mutated(mutator)
                result = resolver.resolve_portable_source_body_verification_command_success_boundary_v2(
                    declared_command_success_boundary_request=request
                )
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertIn(result["outcome"], OUTCOME_FAMILY)
                self.assertIsNotNone((result.get("block") or {}).get("block_code"))
                self.assert_public_block_codes(result)
                self.assert_v2_metadata(result)
                self.assert_no_success_or_follow_on(result)
                self.assert_no_raw_body_material(result)

    def test_path_and_write_behavior_is_bounded_to_v2_root(self) -> None:
        request = _request(command_success_boundary_request_id="success_boundary_v2_path_test")
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            request_path = temp_root / "request.json"
            request_path.write_text(json.dumps(request, indent=2, sort_keys=True), encoding="utf-8")

            result = resolver.resolve_portable_source_body_verification_command_success_boundary_v2_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], RECORDED)
            self.assert_v2_metadata(result)

            malformed_path = temp_root / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            malformed = resolver.resolve_portable_source_body_verification_command_success_boundary_v2_from_path(
                malformed_path
            )
            self.assertEqual(malformed["outcome"], BLOCKED)
            self.assert_v2_metadata(malformed)
            self.assert_public_block_codes(malformed)

            array_path = temp_root / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolver.resolve_portable_source_body_verification_command_success_boundary_v2_from_path(
                array_path
            )
            self.assertEqual(array_result["outcome"], BLOCKED)
            self.assert_v2_metadata(array_result)

            missing_result = resolver.resolve_portable_source_body_verification_command_success_boundary_v2_from_path(
                temp_root / "missing.json"
            )
            self.assertEqual(missing_result["outcome"], BLOCKED)
            self.assert_v2_metadata(missing_result)

            output_root = (
                temp_root
                / "artifacts"
                / "integrity_host_v0_min_coexistence_portable_source_body_verification_command_success_boundary_v2"
            )
            v1_root_name = (
                "integrity_host_v0_min_coexistence_portable_source_body_verification_"
                "command_success_boundary"
            )
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_portable_source_body_verification_command_success_boundary_v2_result(result)
                second_path = resolver.write_portable_source_body_verification_command_success_boundary_v2_result(result)

            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertEqual(first_path.parent, output_root)
            self.assertEqual(second_path.parent, output_root)
            self.assertEqual(first_path.parent.name, f"{v1_root_name}_v2")
            self.assertNotEqual(first_path.parent.name, v1_root_name)
            parsed = json.loads(first_path.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], RECORDED)
            self.assertEqual(
                parsed["portable_source_body_verification_command_success_boundary_metadata"][
                    "result_version"
                ],
                "0.2.0",
            )
            self.assert_no_raw_body_material(parsed)

    def test_summary_helper_preserves_v2_successor_posture(self) -> None:
        request = _request(command_success_boundary_request_id="summary_v2_request")
        result = resolver.resolve_portable_source_body_verification_command_success_boundary_v2(
            declared_command_success_boundary_request=request
        )
        summary = resolver.build_portable_source_body_verification_command_success_boundary_v2_summary(result)

        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertEqual(summary["request_id"], "summary_v2_request")
        self.assertEqual(summary["question"], request["command_success_boundary_question"])
        self.assertEqual(summary["intent"], request["command_success_boundary_intent"])
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.2.0")
        self.assertEqual(
            summary["successor_of"],
            "resolve_portable_source_body_verification_command_success_boundary",
        )
        self.assertIn("raw", summary["successor_reason"].lower())
        self.assertIn("containment", summary["successor_reason"].lower())
        self.assertNotIn(RAW_BODY_SENTINEL, summary["successor_reason"])
        self.assertIs(summary["v1_predecessor_failure_preserved"], True)
        self.assertIs(summary["v1_repaired"], False)
        self.assertIs(summary["v1_hidden"], False)
        self.assertIs(summary["v1_claimed_passed"], False)
        self.assertIs(summary["v2_successor_does_not_erase_v1"], True)
        self.assertIs(summary["returned_result_containment_preserved"], True)
        self.assertIs(summary["selected_basis_reference_shape_preserved"], True)
        self.assertIs(summary["raw_full_prior_artifact_body_returned"], False)
        for key in (
            "command_success_boundary_recorded",
            "one_future_command_success_step_declared",
            "command_result_v2_basis_preserved",
            "bounded_command_result_preserved",
            "command_result_v1_predecessor_failure_preserved",
            "report_body_absent_or_bounded",
            "result_body_absent_or_bounded",
            "report_body_not_invented",
            "result_body_not_invented",
            "success_body_not_invented",
            "command_success_still_not_created",
            "success_inference_blocked",
            "currentness_inference_blocked",
            "final_completion_inference_blocked",
            "public_readiness_inference_blocked",
            "deployment_readiness_inference_blocked",
            "authority_inference_blocked",
            "follow_on_work_inference_blocked",
            "unbounded_pass_fail_inference_blocked",
            "success_boundary_not_success_source_authority_currentness_final_completion_public_readiness_deployment_readiness",
            "command_result_not_success_source_authority_currentness_final_completion_public_readiness_deployment_readiness",
            "output_capture_not_result_success_source_authority_currentness_final_completion",
            "execution_trace_not_success_source_authority_currentness_final_completion",
            "command_report_lineage_not_current_report_artifact_result_authority_success_source_authority_currentness",
            "no_raw_full_prior_artifact_body",
            "no_deployment_runtime_public_release",
            "no_continuation_publication_reusable_follow_on",
        ):
            self.assertIs(summary.get(key), True, key)
        self.assertEqual(
            summary["selected_command_result_v2_outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_RECORDED",
        )
        self.assertEqual(summary["selected_command_result_v2_version"], "0.2.0")
        self.assertEqual(summary["selected_command_result_v2_failed_check_count"], 0)
        self.assertEqual(
            summary["selected_output_capture_v2_outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_RECORDED",
        )
        self.assertEqual(summary["selected_output_capture_v2_version"], "0.2.0")
        self.assertEqual(summary["selected_output_capture_v2_failed_check_count"], 0)
        for key, value in summary["key_non_claims"].items():
            self.assertIs(value, False, key)

    def test_resolver_does_not_mutate_selected_basis_or_postures(self) -> None:
        request = _request()
        request["selected_command_report_lineage_basis"]["synthetic_nested_reference"] = {
            "path": "synthetic://small-reference.json",
            "note": "reference-shaped only",
        }
        tracked_keys = (
            "selected_command_result_v2_basis",
            "selected_command_result_v2_terminal_summary_basis",
            "selected_command_result_v1_predecessor_failure_basis",
            "selected_command_result_boundary_basis",
            "selected_command_output_report_artifact_basis",
            "selected_output_capture_v2_basis",
            "selected_output_capture_v1_predecessor_failure_basis",
            "selected_command_output_basis",
            "selected_post_invocation_command_execution_basis",
            "selected_command_invocation_basis",
            "selected_command_execution_review_basis",
            "selected_request_consumption_basis",
            "selected_consumed_request_basis",
            "selected_v2_admitted_request_basis",
            "selected_command_report_lineage_basis",
            "command_success_boundary_only_posture",
            "one_future_command_success_step_posture",
            "command_success_boundary_scope",
        )
        tracked_before = {key: copy.deepcopy(request[key]) for key in tracked_keys}
        request_before = copy.deepcopy(request)

        result = resolver.resolve_portable_source_body_verification_command_success_boundary_v2(
            declared_command_success_boundary_request=request
        )

        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(request, request_before)
        for key, before_value in tracked_before.items():
            self.assertEqual(request[key], before_value, key)
        self.assert_no_raw_body_material(result)


if __name__ == "__main__":
    unittest.main()
