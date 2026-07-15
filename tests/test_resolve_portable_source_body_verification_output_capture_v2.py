"""Tests for portable source-body verification output capture v2.

This suite is bounded to the additive v2 containment-wrapper successor. V2
preserves the v1 output-capture law and keeps the v1 JSON serialization failure
visible while recursively converting returned and written structures into
JSON-safe values. It does not invent stdout, stderr, process output, raw output
body, create an output/report artifact, command result, command success,
authority, currentness, final completion, deployment, publication, or follow-on
work.
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

import resolve_portable_source_body_verification_output_capture as v1_resolver
import resolve_portable_source_body_verification_output_capture_v2 as resolver
from resolve_portable_source_body_verification_output_capture_v2 import (
    build_portable_source_body_verification_output_capture_v2_summary,
    resolve_portable_source_body_verification_output_capture_v2,
    resolve_portable_source_body_verification_output_capture_v2_from_path,
    write_portable_source_body_verification_output_capture_v2_result,
)


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}

QUESTION = resolver.CORE_OUTPUT_CAPTURE_QUESTION
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_OUTPUT_CAPTURE_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
RAW_PRIOR_SENTINEL = "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN_" * 6

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_output_capture_metadata",
    "declared_output_capture_question",
    "selected_output_capture_boundary_basis",
    "selected_output_capture_boundary_terminal_summary_basis",
    "selected_command_output_basis",
    "selected_command_output_terminal_summary_basis",
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
    "selected_command_report_basis",
    "selected_command_implementation_boundary_basis",
    "selected_command_boundary_basis",
    "selected_artifact_emission_containment_basis",
    "selected_evidence_manifest_basis",
    "selected_portable_verification_basis",
    "output_capture_only_posture",
    "one_bounded_output_capture_event_posture",
    "output_capture_boundary_basis_preserved_posture",
    "command_output_basis_preserved_posture",
    "bounded_command_output_event_preserved_posture",
    "execution_trace_audit_only_posture",
    "no_stdout_content_invented_posture",
    "no_stderr_content_invented_posture",
    "no_process_output_content_invented_posture",
    "no_raw_output_body_content_invented_posture",
    "no_output_report_artifact_posture",
    "no_command_result_posture",
    "no_command_success_posture",
    "no_output_as_source_posture",
    "no_result_as_authority_posture",
    "no_success_as_currentness_posture",
    "no_final_completion_posture",
    "authorization_token_reuse_blocked_posture",
    "consumed_token_closed_posture",
    "no_reopen_consumed_request_posture",
    "returned_result_containment_posture",
    "reference_shaped_input_posture",
    "output_capture_scope",
    "output_capture_checks",
    "output_capture_statement",
    "output_capture_non_meaning",
    "output_capture_event",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_output_capture_summary",
    "portable_source_body_verification_output_capture_v2_successor_posture",
)

SELECTED_BASIS_KEYS = tuple(resolver.SELECTED_BASIS_KEYS)
POSTURE_KEYS = tuple(resolver.POSTURE_KEYS)

FORBIDDEN_RAW_VALUE_KEYS = {
    "stdout",
    "stderr",
    "process_output",
    "raw_output_body",
    "output_body",
    "result_body",
    "success_body",
    "source_body",
    "authority_body",
    "currentness_claim",
    "final_completion_claim",
}


def _false_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _reference_basis(name: str, **overrides: Any) -> dict[str, Any]:
    basis: dict[str, Any] = {
        "basis_id": name,
        "declared": True,
        "basis_declared": True,
        "path": f"synthetic://{name}.json",
        "result_path": f"synthetic://{name}.json",
        "basis_reference": f"synthetic://{name}",
        "reference_shaped_basis": True,
        "basis_remains_reference_shaped": True,
        "basis_reference_shape_preserved": True,
        "basis_remains_basis_only": True,
        "selected_basis_is_reference_shaped": True,
        "full_upstream_lineage_preserved": True,
        "full_prior_artifact_body_not_emitted": True,
        "full_prior_artifacts_embedded": False,
        "raw_full_prior_artifact_body_returned": False,
        "prior_artifacts_mutated": False,
        "not_output_report_artifact": True,
        "not_command_output_report_artifact": True,
        "not_command_result": True,
        "not_command_success": True,
        "not_source": True,
        "not_authority": True,
        "not_currentness": True,
        "not_final_completion": True,
        "not_continuation": True,
        "not_follow_on_work": True,
        "stdout_captured": False,
        "stderr_captured": False,
        "process_output_captured": False,
        "raw_output_body_captured": False,
        "output_capture_created": False,
        "output_report_artifact_created": False,
        "command_output_report_artifact_created": False,
        "command_result_created": False,
        "command_success_created": False,
        "authorization_token_reused": False,
        "consumed_request_reopened": False,
        "v1_repaired": False,
        "v1_hidden": False,
        "v1_claimed_passed": False,
        "deployment_created": False,
        "runtime_hosting_created": False,
        "public_release_created": False,
        "operation_permission_created": False,
        "public_launch_readiness_created": False,
        "final_completion_claimed": False,
        "continuation_authorized": False,
        "publication_flow_opened": False,
        "reusable_permission_created": False,
        "derivative_reception_authorized": False,
        "vessel_relation_authorized": False,
        "another_reception_request_authorized": False,
        "follow_on_work_authorized": False,
        "mutation_performed": False,
        "replay_performed": False,
        "merge_performed": False,
    }
    basis.update(overrides)
    return basis


def _terminal_summary_basis(name: str, **overrides: Any) -> dict[str, Any]:
    basis = _reference_basis(
        name,
        terminal_summary_declared=True,
        terminal_summary_path=f"spec/{name}.md",
        terminal_summary_remains_readability_basis_only=True,
        readability_basis_only=True,
        terminal_summary_does_not_invent_stdout=True,
        terminal_summary_does_not_invent_stderr=True,
        terminal_summary_does_not_invent_process_output=True,
        terminal_summary_does_not_invent_raw_output_body=True,
        terminal_summary_does_not_create_output_report_artifact=True,
        terminal_summary_does_not_create_command_result=True,
        terminal_summary_does_not_create_command_success=True,
        terminal_summary_does_not_authorize_follow_on_work=True,
    )
    basis.update(overrides)
    return basis


def _posture(name: str, **overrides: Any) -> dict[str, Any]:
    posture: dict[str, Any] = {
        "posture_id": name,
        "declared": True,
        "posture_declared": True,
        "stdout_content_present": False,
        "stderr_content_present": False,
        "process_output_content_present": False,
        "raw_output_body_content_present": False,
        "stdout_content_absent_without_invention": True,
        "stderr_content_absent_without_invention": True,
        "process_output_content_absent_without_invention": True,
        "raw_output_body_content_absent_without_invention": True,
        "stdout_content_invented": False,
        "stderr_content_invented": False,
        "process_output_content_invented": False,
        "raw_output_body_content_invented": False,
        "command_output_report_artifact_created": False,
        "output_report_artifact_created": False,
        "command_output_report_artifact_not_created": True,
        "command_result_created": False,
        "command_result_not_created": True,
        "command_result_still_not_created": True,
        "command_success_created": False,
        "command_success_not_created": True,
        "command_success_still_not_created": True,
        "output_capture_treated_as_output_report_artifact": False,
        "output_capture_treated_as_result": False,
        "output_capture_treated_as_success": False,
        "output_capture_treated_as_source": False,
        "output_capture_treated_as_authority": False,
        "output_capture_treated_as_currentness": False,
        "output_capture_treated_as_final_completion": False,
        "command_output_treated_as_output_report_artifact": False,
        "command_output_treated_as_result": False,
        "command_output_treated_as_success": False,
        "command_output_treated_as_source": False,
        "command_output_treated_as_authority": False,
        "command_output_treated_as_currentness": False,
        "command_output_treated_as_final_completion": False,
        "execution_trace_audit_only": True,
        "execution_trace_audit_only_preserved": True,
        "execution_trace_treated_as_output_capture": False,
        "execution_trace_treated_as_result": False,
        "execution_trace_treated_as_success": False,
        "execution_trace_treated_as_source": False,
        "execution_trace_treated_as_authority": False,
        "command_result_became_authority": False,
        "command_success_created_currentness": False,
        "command_success_claimed_final_completion": False,
        "authorization_token_reuse_blocked": True,
        "authorization_token_reused": False,
        "consumed_request_token_remains_closed": True,
        "consumed_request_reopened": False,
        "returned_result_containment_preserved": True,
        "raw_full_prior_artifact_body_returned": False,
    }
    posture.update(overrides)
    return posture


def _output_capture_event(**overrides: Any) -> dict[str, Any]:
    event: dict[str, Any] = {
        "output_capture_event_recorded": True,
        "event_type": "OUTPUT_CAPTURE_EVENT_BOUNDED",
        "stdout_content_present": False,
        "stderr_content_present": False,
        "process_output_content_present": False,
        "raw_output_body_content_present": False,
        "stdout_content_absent_without_invention": True,
        "stderr_content_absent_without_invention": True,
        "process_output_content_absent_without_invention": True,
        "raw_output_body_content_absent_without_invention": True,
        "stdout_content_invented": False,
        "stderr_content_invented": False,
        "process_output_content_invented": False,
        "raw_output_body_content_invented": False,
        "command_output_report_artifact_created": False,
        "command_result_created": False,
        "command_success_created": False,
        "output_capture_is_not_output_report_artifact": True,
        "output_capture_is_not_result": True,
        "output_capture_is_not_success": True,
        "output_capture_is_not_source": True,
        "output_capture_is_not_authority": True,
        "output_capture_is_not_currentness": True,
        "output_capture_is_not_final_completion": True,
    }
    event.update(overrides)
    return event


def _valid_request(**overrides: Any) -> dict[str, Any]:
    request = resolver.build_declared_portable_source_body_verification_output_capture_v2_request(
        output_capture_request_id="output-capture-v2-request-001",
        output_capture_question=QUESTION,
        output_capture_intent=resolver.INTENT_RECORD,
    )
    request["selected_output_capture_boundary_basis"] = _reference_basis(
        "selected_output_capture_boundary_basis",
        portable_source_body_verification_output_capture_boundary_result_id=(
            "output-capture-boundary-result-001"
        ),
        outcome=resolver.OUTPUT_CAPTURE_BOUNDARY_OUTCOME,
        failed_check_count=0,
        passed_check_count=120,
        output_capture_boundary_recorded=True,
        one_future_output_capture_step_declared=True,
        stdout_not_captured=True,
        stderr_not_captured=True,
        process_output_not_captured=True,
        raw_output_body_not_captured=True,
        output_capture_not_created=True,
        command_output_report_artifact_not_created=True,
        output_report_artifact_not_created=True,
        command_result_not_created=True,
        command_result_still_not_created=True,
        command_success_not_created=True,
        command_success_still_not_created=True,
    )
    request["selected_output_capture_boundary_terminal_summary_basis"] = _terminal_summary_basis(
        "PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_BOUNDARY_TERMINAL_SUMMARY_V0"
    )
    request["selected_command_output_basis"] = _reference_basis(
        "selected_command_output_basis",
        portable_source_body_verification_command_output_result_id="command-output-result-001",
        outcome=resolver.COMMAND_OUTPUT_OUTCOME,
        failed_check_count=0,
        passed_check_count=109,
        command_output_recorded=True,
        bounded_command_output_event_recorded=True,
        command_output_event_recorded=True,
        stdout_not_captured=True,
        stderr_not_captured=True,
        process_output_not_captured=True,
        raw_output_body_not_captured=True,
        output_capture_not_created=True,
        command_output_report_artifact_not_created=True,
        output_report_artifact_not_created=True,
        command_result_not_created=True,
        command_result_still_not_created=True,
        command_success_not_created=True,
        command_success_still_not_created=True,
        command_output_is_not_output_report_artifact=True,
        command_output_is_not_result=True,
        command_output_is_not_success=True,
        command_output_is_not_source=True,
        command_output_is_not_authority=True,
        command_output_is_not_currentness=True,
        command_output_is_not_final_completion=True,
    )
    request["selected_command_output_terminal_summary_basis"] = _terminal_summary_basis(
        "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_TERMINAL_SUMMARY_V0"
    )
    request["selected_command_output_boundary_basis"] = _reference_basis(
        "selected_command_output_boundary_basis",
        outcome=resolver.COMMAND_OUTPUT_BOUNDARY_OUTCOME,
        failed_check_count=0,
        one_future_command_output_step_declared=True,
        command_output_containment_basis_preserved=True,
    )
    request["selected_command_output_containment_basis"] = _reference_basis(
        "selected_command_output_containment_basis",
        outcome=resolver.COMMAND_OUTPUT_CONTAINMENT_OUTCOME,
        failed_check_count=0,
        one_bounded_output_containment_event_recorded=True,
        bounded_command_output_containment_event_recorded=True,
        command_output_boundary_basis_preserved=True,
    )
    request["selected_post_invocation_command_execution_basis"] = _reference_basis(
        "selected_post_invocation_command_execution_basis",
        outcome=resolver.POST_INVOCATION_COMMAND_EXECUTION_OUTCOME,
        failed_check_count=0,
        one_bounded_command_execution_event_recorded=True,
        bounded_command_execution_event_recorded=True,
        recorded_command_execution_event_preserved=True,
        execution_trace_audit_only=True,
        execution_trace_audit_only_preserved=True,
    )
    request["selected_post_invocation_command_execution_terminal_summary_basis"] = (
        _terminal_summary_basis(
            "PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_TERMINAL_SUMMARY_V0",
            execution_trace_audit_only_preserved=True,
        )
    )
    request["selected_command_invocation_basis"] = _reference_basis(
        "selected_command_invocation_basis",
        outcome=resolver.COMMAND_INVOCATION_OUTCOME,
        failed_check_count=0,
        bounded_command_invocation_event_recorded=True,
        authorization_token_spent_exactly_once=True,
        authorization_token_reuse_blocked=True,
    )
    request["selected_command_execution_review_basis"] = _reference_basis(
        "selected_command_execution_review_basis",
        outcome=resolver.COMMAND_EXECUTION_REVIEW_OUTCOME,
        failed_check_count=0,
        review_basis_only=True,
    )
    request["selected_request_consumption_basis"] = _reference_basis(
        "selected_request_consumption_basis",
        outcome=resolver.REQUEST_CONSUMPTION_OUTCOME,
        failed_check_count=0,
        request_consumed_exactly_once=True,
        consumption_token_closed=True,
        consumed_request_basis_recorded=True,
    )
    request["selected_consumed_request_basis"] = _reference_basis(
        "selected_consumed_request_basis",
        consumed_request_basis_declared=True,
        consumed_request_token_remains_closed=True,
        consumed_request_is_not_reopened=True,
        consumed_request_basis_is_basis_only=True,
    )
    request["selected_v2_admitted_request_basis"] = _reference_basis(
        "selected_v2_admitted_request_basis",
        outcome=resolver.V2_ADMITTED_REQUEST_OUTCOME,
        result_version=resolver.V2_ADMITTED_REQUEST_VERSION,
        version=resolver.V2_ADMITTED_REQUEST_VERSION,
        failed_check_count=0,
        successor_metadata_preserved=True,
        returned_result_containment_preserved=True,
        v2_does_not_claim_v1_passed=True,
        v2_treated_as_repairing_v1=False,
        v2_repairs_v1=False,
    )
    request["selected_v1_predecessor_failure_basis"] = _reference_basis(
        "selected_v1_predecessor_failure_basis",
        v1_predecessor_failure_basis_declared=True,
        v1_remains_visible_predecessor_failure_evidence=True,
        v1_is_not_repaired=True,
        v1_is_not_hidden=True,
        v1_is_not_claimed_passed=True,
        v2_successor_does_not_erase_v1=True,
        predecessor_failure_evidence_is_lineage_evidence_only=True,
    )
    request["selected_older_command_execution_boundary_lineage_basis"] = _reference_basis(
        "selected_older_command_execution_boundary_lineage_basis",
        basis_remains_prior_scaffolding_only=True,
        lineage_basis_not_treated_as_current_execution=True,
        older_command_execution_boundary_lineage_treated_as_current_execution=False,
    )
    for key in (
        "selected_command_report_basis",
        "selected_command_implementation_boundary_basis",
        "selected_command_boundary_basis",
        "selected_artifact_emission_containment_basis",
        "selected_evidence_manifest_basis",
        "selected_portable_verification_basis",
    ):
        request[key] = _reference_basis(key)
    for key in POSTURE_KEYS:
        request[key] = _posture(key)
    request["reference_shaped_input_posture"].update(
        {
            "reference_shaped_input_posture": True,
            "full_prior_artifact_body_not_emitted": True,
        }
    )
    request["output_capture_event"] = _output_capture_event()
    request["output_capture_scope"] = list(SUPPORTED_SCOPE)
    request["declared_non_claims"] = _false_non_claims()
    request["requested_output_capture_outcome"] = RECORDED
    request.update(overrides)
    return request


def _mutated_request(mutator: Callable[[dict[str, Any]], None]) -> dict[str, Any]:
    request = _valid_request()
    mutator(request)
    return request


def _block_codes(result: Mapping[str, Any]) -> set[str]:
    codes = {
        check.get("block_code")
        for check in result.get("output_capture_checks", [])
        if isinstance(check, Mapping) and not check.get("passed")
    }
    block = result.get("block", {})
    if isinstance(block, Mapping):
        codes.add(block.get("block_code"))
    return {str(code) for code in codes if code}


def _find_check(result: Mapping[str, Any], check_name: str) -> Mapping[str, Any]:
    for check in result.get("output_capture_checks", []):
        if isinstance(check, Mapping) and check.get("check_name") == check_name:
            return check
    raise AssertionError(f"missing check: {check_name}")


def _contains_forbidden_raw_value(value: Any) -> bool:
    if isinstance(value, Mapping):
        for key, nested in value.items():
            if key in FORBIDDEN_RAW_VALUE_KEYS and nested not in (False, None, "", {}, []):
                return True
            if _contains_forbidden_raw_value(nested):
                return True
    elif isinstance(value, list):
        return any(_contains_forbidden_raw_value(item) for item in value)
    return False


class OutputCaptureV2ResolverTests(unittest.TestCase):
    def assertNoUnsafeJsonObjects(self, value: Any) -> None:
        if isinstance(value, Mapping):
            for nested in value.values():
                self.assertNoUnsafeJsonObjects(nested)
            return
        if isinstance(value, list):
            for nested in value:
                self.assertNoUnsafeJsonObjects(nested)
            return
        self.assertNotIsInstance(value, (set, frozenset, tuple, Path))

    def assertV2Metadata(self, result: Mapping[str, Any]) -> None:
        metadata = result["portable_source_body_verification_output_capture_metadata"]
        summary = result["portable_source_body_verification_output_capture_summary"]
        posture = result["portable_source_body_verification_output_capture_v2_successor_posture"]
        for carrier in (metadata, summary, posture):
            self.assertEqual(resolver.SUCCESSOR_OF, carrier["successor_of"])
            self.assertIn("v1", carrier["successor_reason"])
            self.assertIn("frozenset", carrier["successor_reason"])
            self.assertIn("expected_posture", carrier["successor_reason"])
            self.assertTrue(carrier["v1_predecessor_failure_preserved"])
            self.assertFalse(carrier["v1_repaired"])
            self.assertFalse(carrier["v1_hidden"])
            self.assertFalse(carrier["v1_claimed_passed"])
            self.assertTrue(carrier["returned_result_containment_preserved"])
        self.assertEqual(resolver.RESOLVER_MODULE, metadata["resolver_module"])
        self.assertEqual(
            "0.2.0",
            metadata["portable_source_body_verification_output_capture_result_version"],
        )
        self.assertEqual("0.2.0", metadata["result_version"])
        self.assertTrue(metadata["v2_successor_does_not_erase_v1"])
        self.assertEqual("0.2.0", summary["result_version"])
        self.assertTrue(summary["v2_successor_does_not_erase_v1"])
        self.assertTrue(posture["v2_successor_does_not_erase_v1"])
        self.assertTrue(posture["same_output_capture_law_preserved"])
        self.assertTrue(posture["json_safe_returned_result_preserved"])

    def assertRecordedLaw(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(RECORDED, result["outcome"])
        self.assertFalse(result["block"]["blocked"])
        self.assertIsNone(result["block"]["block_code"])
        summary = result["portable_source_body_verification_output_capture_summary"]
        self.assertEqual(0, summary["failed_check_count"])
        self.assertGreaterEqual(summary["passed_check_count"], 120)
        statement = result["output_capture_statement"]
        for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIs(statement[key], True, key)
        for key in resolver.ALLOWED_FALSE_RECORDED_FIELDS:
            self.assertIs(statement[key], False, key)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(statement[key], False, key)
            self.assertIs(result["non_claims"][key], False, key)

        event = result["output_capture_event"]
        self.assertTrue(event["output_capture_event_recorded"])
        self.assertEqual("OUTPUT_CAPTURE_EVENT_BOUNDED", event["event_type"])
        self.assertFalse(event["stdout_content_present"])
        self.assertFalse(event["stderr_content_present"])
        self.assertFalse(event["process_output_content_present"])
        self.assertFalse(event["raw_output_body_content_present"])
        self.assertTrue(event["stdout_content_absent_without_invention"])
        self.assertTrue(event["stderr_content_absent_without_invention"])
        self.assertTrue(event["process_output_content_absent_without_invention"])
        self.assertTrue(event["raw_output_body_content_absent_without_invention"])
        self.assertFalse(event["stdout_content_invented"])
        self.assertFalse(event["stderr_content_invented"])
        self.assertFalse(event["process_output_content_invented"])
        self.assertFalse(event["raw_output_body_content_invented"])
        self.assertFalse(event["command_output_report_artifact_created"])
        self.assertFalse(event["command_result_created"])
        self.assertFalse(event["command_success_created"])
        self.assertTrue(event["output_capture_is_not_output_report_artifact"])
        self.assertTrue(event["output_capture_is_not_result"])
        self.assertTrue(event["output_capture_is_not_success"])
        self.assertTrue(event["output_capture_is_not_source"])
        self.assertTrue(event["output_capture_is_not_authority"])
        self.assertTrue(event["output_capture_is_not_currentness"])
        self.assertTrue(event["output_capture_is_not_final_completion"])
        self.assertFalse(_contains_forbidden_raw_value(event))

        non_meaning = result["output_capture_non_meaning"]
        self.assertFalse(non_meaning["output_report_artifact_exists"])
        self.assertFalse(non_meaning["command_result_exists"])
        self.assertFalse(non_meaning["command_success_exists"])
        self.assertFalse(non_meaning["output_capture_is_authority"])
        self.assertFalse(non_meaning["output_capture_is_currentness"])
        self.assertFalse(non_meaning["output_capture_is_final_completion"])
        self.assertTrue(summary["output_capture_recorded"])
        self.assertTrue(summary["bounded_output_capture_event_recorded"])
        self.assertFalse(summary["stdout_content_present"])
        self.assertFalse(summary["stderr_content_present"])
        self.assertFalse(summary["process_output_content_present"])
        self.assertFalse(summary["raw_output_body_content_present"])
        self.assertTrue(summary["stdout_content_absent_without_invention"])
        self.assertTrue(summary["stderr_content_absent_without_invention"])
        self.assertTrue(summary["process_output_content_absent_without_invention"])
        self.assertTrue(summary["raw_output_body_content_absent_without_invention"])
        self.assertTrue(summary["command_output_report_artifact_not_created"])
        self.assertTrue(summary["command_result_still_not_created"])
        self.assertTrue(summary["command_success_still_not_created"])
        self.assertTrue(summary["no_deployment_runtime_public_release"])
        self.assertTrue(summary["no_operation_public_readiness_final_completion"])
        self.assertTrue(summary["no_continuation_publication_reusable_follow_on"])

    def assertBlockedWithCode(self, request: Any, expected_code: str) -> dict[str, Any]:
        result = resolve_portable_source_body_verification_output_capture_v2(
            declared_output_capture_request=request
        )
        self.assertEqual(BLOCKED, result["outcome"])
        self.assertTrue(result["block"]["blocked"])
        self.assertIn(expected_code, _block_codes(result))
        self.assertV2Metadata(result)
        self.assertNoUnsafeJsonObjects(result)
        json.dumps(result, sort_keys=True, ensure_ascii=False)
        statement = result["output_capture_statement"]
        self.assertFalse(statement["output_capture_recorded"])
        self.assertFalse(statement["bounded_output_capture_event_recorded"])
        self.assertFalse(statement["command_output_report_artifact_created"])
        self.assertFalse(statement["command_result_created"])
        self.assertFalse(statement["command_success_created"])
        self.assertFalse(statement["output_capture_treated_as_authority"])
        self.assertFalse(statement["output_capture_treated_as_currentness"])
        self.assertFalse(statement["output_capture_treated_as_final_completion"])
        self.assertFalse(statement["follow_on_work_authorized"])
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(statement[key], False, key)
            self.assertIs(result["non_claims"][key], False, key)
        return result

    def test_public_api_and_successor_metadata(self) -> None:
        for name in (
            "resolve_portable_source_body_verification_output_capture_v2",
            "resolve_portable_source_body_verification_output_capture_v2_from_path",
            "write_portable_source_body_verification_output_capture_v2_result",
            "build_portable_source_body_verification_output_capture_v2_summary",
            "build_declared_portable_source_body_verification_output_capture_v2_request",
        ):
            self.assertTrue(hasattr(resolver, name), name)
        self.assertEqual(OUTCOME_FAMILY, set(resolver.OUTCOME_FAMILY))
        self.assertEqual(v1_resolver.OUTCOME_RECORDED, resolver.OUTCOME_RECORDED)
        self.assertNotIn("full reimplementation", (resolver.__doc__ or "").lower())

        result = resolve_portable_source_body_verification_output_capture_v2(_valid_request())
        self.assertV2Metadata(result)
        self.assertRecordedLaw(result)

    def test_successful_v2_recorded_result_preserves_v1_output_capture_law(self) -> None:
        request = _valid_request()
        original_request = copy.deepcopy(request)
        selected_originals = {key: copy.deepcopy(request[key]) for key in SELECTED_BASIS_KEYS}
        posture_originals = {key: copy.deepcopy(request[key]) for key in POSTURE_KEYS}
        event_original = copy.deepcopy(request["output_capture_event"])
        scope_original = copy.deepcopy(request["output_capture_scope"])

        result = resolve_portable_source_body_verification_output_capture_v2(
            declared_output_capture_request=request
        )

        self.assertIsInstance(result, dict)
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        self.assertRecordedLaw(result)
        self.assertV2Metadata(result)
        self.assertNoUnsafeJsonObjects(result)
        json.dumps(result, sort_keys=True, ensure_ascii=False)

        metadata = result["portable_source_body_verification_output_capture_metadata"]
        self.assertEqual(resolver.RESOLVER_MODULE, metadata["resolver_module"])
        self.assertEqual(
            "resolve_portable_source_body_verification_output_capture_v2.py",
            metadata["short_resolver_filename"],
        )
        self.assertTrue(
            result["selected_output_capture_boundary_basis"]["basis"][
                "full_upstream_lineage_preserved"
            ]
        )
        self.assertEqual(
            resolver.OUTPUT_CAPTURE_BOUNDARY_OUTCOME,
            result["selected_output_capture_boundary_basis"]["outcome"],
        )
        self.assertEqual(
            resolver.COMMAND_OUTPUT_OUTCOME,
            result["selected_command_output_basis"]["outcome"],
        )
        self.assertEqual(
            resolver.POST_INVOCATION_COMMAND_EXECUTION_OUTCOME,
            result["selected_post_invocation_command_execution_basis"]["outcome"],
        )
        self.assertTrue(
            result["selected_older_command_execution_boundary_lineage_basis"][
                "lineage_basis_not_treated_as_current_execution"
            ]
        )
        self.assertEqual(original_request, request)
        for key, original in selected_originals.items():
            self.assertEqual(original, request[key], key)
        for key, original in posture_originals.items():
            self.assertEqual(original, request[key], key)
        self.assertEqual(event_original, request["output_capture_event"])
        self.assertEqual(scope_original, request["output_capture_scope"])

    def test_json_safe_containment_preserves_checks_and_recursive_values(self) -> None:
        v1_result = v1_resolver.resolve_portable_source_body_verification_output_capture(
            declared_output_capture_request=_valid_request()
        )
        v1_intent_check = _find_check(v1_result, "output capture intent supported")
        self.assertIsInstance(v1_intent_check["expected_posture"], frozenset)
        with self.assertRaises(TypeError) as raised:
            json.dumps(v1_result, sort_keys=True, ensure_ascii=False)
        self.assertIn("frozenset", str(raised.exception))

        request = _valid_request()
        probe = {
            "set_probe": {"b", "a"},
            "frozenset_probe": frozenset({"d", "c"}),
            "tuple_probe": ("z", "y"),
            "path_probe": Path("synthetic/probe/path.json"),
            "nested": {"mixed": (Path("synthetic/nested"), frozenset({3, "2"}))},
        }
        request["selected_command_report_basis"]["json_safe_probe"] = probe
        original_request = copy.deepcopy(request)

        result = resolve_portable_source_body_verification_output_capture_v2(
            declared_output_capture_request=request
        )

        self.assertRecordedLaw(result)
        self.assertNoUnsafeJsonObjects(result)
        json.dumps(result, sort_keys=True, ensure_ascii=False)
        self.assertEqual(original_request, request)

        checks = result["output_capture_checks"]
        self.assertGreater(len(checks), 0)
        self.assertTrue(any(check["passed"] for check in checks))
        intent_check = _find_check(result, "output capture intent supported")
        self.assertIsInstance(intent_check["expected_posture"], list)
        self.assertEqual(set(resolver.SUPPORTED_INTENTS), set(intent_check["expected_posture"]))

        returned_probe = result["selected_command_report_basis"]["basis"]["json_safe_probe"]
        self.assertEqual(["a", "b"], returned_probe["set_probe"])
        self.assertEqual(["c", "d"], returned_probe["frozenset_probe"])
        self.assertEqual(["z", "y"], returned_probe["tuple_probe"])
        self.assertEqual("synthetic/probe/path.json", returned_probe["path_probe"])
        self.assertEqual("synthetic/nested", returned_probe["nested"]["mixed"][0])
        self.assertEqual(["2", 3], returned_probe["nested"]["mixed"][1])

    def test_v2_write_behavior_uses_v2_root_and_preserves_json_safe_result(self) -> None:
        self.assertIn(
            "integrity_host_v0_min_coexistence_portable_source_body_verification_output_capture_v2",
            str(resolver.PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_V2_ROOT),
        )
        self.assertNotEqual(
            str(v1_resolver.PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_ROOT),
            str(resolver.PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_V2_ROOT),
        )

        result = resolve_portable_source_body_verification_output_capture_v2(_valid_request())
        with tempfile.TemporaryDirectory() as tempdir_name:
            tempdir = Path(tempdir_name)
            with patch.object(resolver, "OUTPUT_ROOT", tempdir / "v2_root"):
                first_path = write_portable_source_body_verification_output_capture_v2_result(result)
                second_path = write_portable_source_body_verification_output_capture_v2_result(result)
            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertEqual(
                "output-capture-v2-request-001__portable_source_body_verification_output_capture_v2_result_001.json",
                second_path.name,
            )
            self.assertIn("v2_root", str(first_path.parent))
            self.assertNotIn(
                "integrity_host_v0_min_coexistence_portable_source_body_verification_output_capture/",
                str(first_path),
            )

            for path in (first_path, second_path):
                loaded = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(RECORDED, loaded["outcome"])
                self.assertV2Metadata(loaded)
                self.assertRecordedLaw(loaded)
                self.assertNoUnsafeJsonObjects(loaded)

            explicit_path = tempdir / "nested" / "explicit_result.json"
            written = write_portable_source_body_verification_output_capture_v2_result(
                result, explicit_path
            )
            self.assertTrue(written.exists())
            self.assertEqual("explicit_result.json", written.name)
            loaded = json.loads(written.read_text(encoding="utf-8"))
            self.assertEqual("0.2.0", loaded["portable_source_body_verification_output_capture_metadata"]["result_version"])

    def test_path_based_request_behavior_is_v2_contained(self) -> None:
        request = _valid_request()
        with tempfile.TemporaryDirectory() as tempdir_name:
            tempdir = Path(tempdir_name)
            request_path = tempdir / "request.json"
            request_path.write_text(json.dumps(request, sort_keys=True), encoding="utf-8")

            result = resolve_portable_source_body_verification_output_capture_v2_from_path(
                request_path
            )
            self.assertRecordedLaw(result)
            self.assertV2Metadata(result)
            self.assertNoUnsafeJsonObjects(result)
            json.dumps(result, sort_keys=True, ensure_ascii=False)

            malformed_path = tempdir / "malformed.json"
            malformed_path.write_text("{not valid json", encoding="utf-8")
            malformed = resolve_portable_source_body_verification_output_capture_v2_from_path(
                malformed_path
            )
            self.assertEqual(BLOCKED, malformed["outcome"])
            self.assertIn("DECLARED_OUTPUT_CAPTURE_REQUEST_MALFORMED", _block_codes(malformed))
            self.assertV2Metadata(malformed)
            self.assertNoUnsafeJsonObjects(malformed)

            array_path = tempdir / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolve_portable_source_body_verification_output_capture_v2_from_path(
                array_path
            )
            self.assertEqual(BLOCKED, array_result["outcome"])
            self.assertIn(
                "DECLARED_OUTPUT_CAPTURE_REQUEST_MALFORMED", _block_codes(array_result)
            )
            self.assertV2Metadata(array_result)

            missing_result = resolve_portable_source_body_verification_output_capture_v2_from_path(
                tempdir / "missing.json"
            )
            self.assertEqual(BLOCKED, missing_result["outcome"])
            self.assertIn(
                "DECLARED_OUTPUT_CAPTURE_REQUEST_UNREADABLE", _block_codes(missing_result)
            )
            self.assertV2Metadata(missing_result)

    def test_v1_failure_visibility_is_preserved_in_metadata_summary_and_posture(self) -> None:
        result = resolve_portable_source_body_verification_output_capture_v2(_valid_request())
        self.assertV2Metadata(result)
        metadata = result["portable_source_body_verification_output_capture_metadata"]
        summary = result["portable_source_body_verification_output_capture_summary"]
        posture = result["portable_source_body_verification_output_capture_v2_successor_posture"]
        for carrier in (metadata, summary, posture):
            self.assertIn("v1 produced clean in-memory", carrier["successor_reason"])
            self.assertIn("JSON", carrier["successor_reason"])
            self.assertIn("writing", carrier["successor_reason"])
            self.assertIn("frozenset", carrier["successor_reason"])
            self.assertIn("expected_posture", carrier["successor_reason"])
            self.assertTrue(carrier["v1_predecessor_failure_preserved"])
            self.assertFalse(carrier["v1_repaired"])
            self.assertFalse(carrier["v1_hidden"])
            self.assertFalse(carrier["v1_claimed_passed"])
        self.assertTrue(posture["same_output_capture_law_preserved"])
        self.assertFalse(posture["stdout_content_invented"])
        self.assertFalse(posture["command_output_report_artifact_created"])
        self.assertFalse(posture["command_result_created"])
        self.assertFalse(posture["command_success_created"])
        self.assertFalse(posture["authority_created"])
        self.assertFalse(posture["currentness_created"])
        self.assertFalse(posture["final_completion_claimed"])
        self.assertFalse(posture["follow_on_work_authorized"])

    def test_summary_helper_preserves_v2_successor_and_output_capture_law(self) -> None:
        result = resolve_portable_source_body_verification_output_capture_v2(_valid_request())
        summary = build_portable_source_body_verification_output_capture_v2_summary(result)

        self.assertEqual(RECORDED, summary["outcome"])
        self.assertIsNone(summary["block_code"])
        self.assertEqual("output-capture-v2-request-001", summary["output_capture_request_id"])
        self.assertEqual(QUESTION, summary["question"])
        self.assertEqual(resolver.INTENT_RECORD, summary["intent"])
        self.assertEqual(0, summary["failed_check_count"])
        self.assertGreaterEqual(summary["passed_check_count"], 120)
        self.assertTrue(summary["output_capture_recorded"])
        self.assertTrue(summary["bounded_output_capture_event_recorded"])
        self.assertFalse(summary["stdout_content_present"])
        self.assertFalse(summary["stderr_content_present"])
        self.assertFalse(summary["process_output_content_present"])
        self.assertFalse(summary["raw_output_body_content_present"])
        self.assertTrue(summary["stdout_content_absent_without_invention"])
        self.assertTrue(summary["stderr_content_absent_without_invention"])
        self.assertTrue(summary["process_output_content_absent_without_invention"])
        self.assertTrue(summary["raw_output_body_content_absent_without_invention"])
        self.assertTrue(summary["command_output_report_artifact_not_created"])
        self.assertTrue(summary["command_result_still_not_created"])
        self.assertTrue(summary["command_success_still_not_created"])
        self.assertEqual(
            resolver.OUTPUT_CAPTURE_BOUNDARY_OUTCOME,
            summary["selected_output_capture_boundary_outcome"],
        )
        self.assertEqual(resolver.COMMAND_OUTPUT_OUTCOME, summary["selected_command_output_outcome"])
        self.assertEqual(
            resolver.POST_INVOCATION_COMMAND_EXECUTION_OUTCOME,
            summary["selected_post_invocation_execution_outcome"],
        )
        self.assertEqual(resolver.V2_ADMITTED_REQUEST_OUTCOME, summary["selected_v2_outcome"])
        self.assertEqual(resolver.V2_ADMITTED_REQUEST_VERSION, summary["selected_v2_version"])
        self.assertEqual("0.2.0", summary["result_version"])
        self.assertEqual(resolver.SUCCESSOR_OF, summary["successor_of"])
        self.assertIn("frozenset", summary["successor_reason"])
        self.assertTrue(summary["v1_predecessor_failure_preserved"])
        self.assertFalse(summary["v1_repaired"])
        self.assertFalse(summary["v1_hidden"])
        self.assertFalse(summary["v1_claimed_passed"])
        self.assertTrue(summary["returned_result_containment_preserved"])
        self.assertTrue(summary["no_deployment_runtime_public_release"])
        self.assertTrue(summary["no_operation_public_readiness_final_completion"])
        self.assertTrue(summary["no_continuation_publication_reusable_follow_on"])
        self.assertFalse(summary["stdout_content_invented"])
        self.assertFalse(summary["command_output_report_artifact_created"])
        self.assertFalse(summary["command_result_created"])
        self.assertFalse(summary["command_success_created"])
        self.assertFalse(summary["authority_created"])
        self.assertFalse(summary["currentness_created"])
        self.assertFalse(summary["final_completion_claimed"])
        self.assertFalse(summary["follow_on_work_authorized"])

    def test_v2_preserves_not_recorded_requires_additional_basis_and_blocked_outcomes(self) -> None:
        not_recorded_request = _valid_request(
            output_capture_intent=resolver.INTENT_DO_NOT_RECORD,
            requested_output_capture_outcome=NOT_RECORDED,
            not_recorded_basis={"reason": "readable output-capture basis failed review"},
        )
        not_recorded = resolve_portable_source_body_verification_output_capture_v2(
            not_recorded_request
        )
        self.assertEqual(NOT_RECORDED, not_recorded["outcome"])
        self.assertFalse(not_recorded["block"]["blocked"])
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded"])
        self.assertV2Metadata(not_recorded)
        self.assertNoUnsafeJsonObjects(not_recorded)

        requires_request = _valid_request(
            requested_output_capture_outcome=REQUIRES_ADDITIONAL_BASIS,
            additional_basis_context={
                "missing_basis": "selected command report basis needs clearer reference"
            },
        )
        del requires_request["selected_command_report_basis"]
        requires = resolve_portable_source_body_verification_output_capture_v2(requires_request)
        self.assertEqual(REQUIRES_ADDITIONAL_BASIS, requires["outcome"])
        self.assertFalse(requires["block"]["blocked"])
        self.assertTrue(requires["additional_basis_required"]["required"])
        self.assertTrue(requires["additional_basis_required"]["missing_basis_not_authorized"])
        self.assertTrue(requires["additional_basis_required"]["missing_basis_not_executed"])
        self.assertV2Metadata(requires)
        self.assertNoUnsafeJsonObjects(requires)

        blocked = self.assertBlockedWithCode(
            _valid_request(
                output_capture_intent=resolver.INTENT_BLOCK,
                block_reason="explicit v2 blocked request",
            ),
            "OUTPUT_CAPTURE_BLOCKED_BY_REQUEST",
        )
        self.assertEqual("OUTPUT_CAPTURE_BLOCKED_BY_REQUEST", blocked["block"]["block_code"])

    def test_v2_blocks_representative_collapse_attempts_without_creating_stronger_posture(
        self,
    ) -> None:
        cases: list[tuple[str, Callable[[dict[str, Any]], None], str]] = [
            (
                "stdout content invented",
                lambda request: request["declared_non_claims"].update(
                    stdout_content_invented=True
                ),
                "STDOUT_CONTENT_INVENTED",
            ),
            (
                "stderr content invented",
                lambda request: request["declared_non_claims"].update(
                    stderr_content_invented=True
                ),
                "STDERR_CONTENT_INVENTED",
            ),
            (
                "process output content invented",
                lambda request: request["declared_non_claims"].update(
                    process_output_content_invented=True
                ),
                "PROCESS_OUTPUT_CONTENT_INVENTED",
            ),
            (
                "raw output body content invented",
                lambda request: request["declared_non_claims"].update(
                    raw_output_body_content_invented=True
                ),
                "RAW_OUTPUT_BODY_CONTENT_INVENTED",
            ),
            (
                "output report artifact created",
                lambda request: request["declared_non_claims"].update(
                    command_output_report_artifact_created=True
                ),
                "COMMAND_OUTPUT_REPORT_ARTIFACT_CREATED",
            ),
            (
                "command result created",
                lambda request: request["declared_non_claims"].update(command_result_created=True),
                "COMMAND_RESULT_CREATED",
            ),
            (
                "command success created",
                lambda request: request["declared_non_claims"].update(command_success_created=True),
                "COMMAND_SUCCESS_CREATED",
            ),
            (
                "output capture treated as output report",
                lambda request: request["declared_non_claims"].update(
                    output_capture_treated_as_output_report_artifact=True
                ),
                "OUTPUT_CAPTURE_TREATED_AS_OUTPUT_REPORT_ARTIFACT",
            ),
            (
                "output capture treated as result",
                lambda request: request["declared_non_claims"].update(
                    output_capture_treated_as_result=True
                ),
                "OUTPUT_CAPTURE_TREATED_AS_RESULT",
            ),
            (
                "output capture treated as success",
                lambda request: request["declared_non_claims"].update(
                    output_capture_treated_as_success=True
                ),
                "OUTPUT_CAPTURE_TREATED_AS_SUCCESS",
            ),
            (
                "output capture treated as source",
                lambda request: request["declared_non_claims"].update(
                    output_capture_treated_as_source=True
                ),
                "OUTPUT_CAPTURE_TREATED_AS_SOURCE",
            ),
            (
                "output capture treated as authority",
                lambda request: request["declared_non_claims"].update(
                    output_capture_treated_as_authority=True
                ),
                "OUTPUT_CAPTURE_TREATED_AS_AUTHORITY",
            ),
            (
                "output capture treated as currentness",
                lambda request: request["declared_non_claims"].update(
                    output_capture_treated_as_currentness=True
                ),
                "OUTPUT_CAPTURE_TREATED_AS_CURRENTNESS",
            ),
            (
                "output capture treated as final completion",
                lambda request: request["declared_non_claims"].update(
                    output_capture_treated_as_final_completion=True
                ),
                "OUTPUT_CAPTURE_TREATED_AS_FINAL_COMPLETION",
            ),
            (
                "command output treated as output report",
                lambda request: request["declared_non_claims"].update(
                    command_output_treated_as_output_report_artifact=True
                ),
                "COMMAND_OUTPUT_TREATED_AS_OUTPUT_REPORT_ARTIFACT",
            ),
            (
                "command output treated as result",
                lambda request: request["declared_non_claims"].update(
                    command_output_treated_as_result=True
                ),
                "COMMAND_OUTPUT_TREATED_AS_RESULT",
            ),
            (
                "command output treated as success",
                lambda request: request["declared_non_claims"].update(
                    command_output_treated_as_success=True
                ),
                "COMMAND_OUTPUT_TREATED_AS_SUCCESS",
            ),
            (
                "command output treated as source",
                lambda request: request["declared_non_claims"].update(
                    command_output_treated_as_source=True
                ),
                "COMMAND_OUTPUT_TREATED_AS_SOURCE",
            ),
            (
                "command output treated as authority",
                lambda request: request["declared_non_claims"].update(
                    command_output_treated_as_authority=True
                ),
                "COMMAND_OUTPUT_TREATED_AS_AUTHORITY",
            ),
            (
                "command output treated as currentness",
                lambda request: request["declared_non_claims"].update(
                    command_output_treated_as_currentness=True
                ),
                "COMMAND_OUTPUT_TREATED_AS_CURRENTNESS",
            ),
            (
                "command output treated as final completion",
                lambda request: request["declared_non_claims"].update(
                    command_output_treated_as_final_completion=True
                ),
                "COMMAND_OUTPUT_TREATED_AS_FINAL_COMPLETION",
            ),
            (
                "execution trace treated as output capture",
                lambda request: request["declared_non_claims"].update(
                    execution_trace_treated_as_output_capture=True
                ),
                "EXECUTION_TRACE_TREATED_AS_OUTPUT_CAPTURE",
            ),
            (
                "execution trace treated as result",
                lambda request: request["declared_non_claims"].update(
                    execution_trace_treated_as_result=True
                ),
                "EXECUTION_TRACE_TREATED_AS_RESULT",
            ),
            (
                "execution trace treated as success",
                lambda request: request["declared_non_claims"].update(
                    execution_trace_treated_as_success=True
                ),
                "EXECUTION_TRACE_TREATED_AS_SUCCESS",
            ),
            (
                "execution trace treated as source",
                lambda request: request["declared_non_claims"].update(
                    execution_trace_treated_as_source=True
                ),
                "EXECUTION_TRACE_TREATED_AS_SOURCE",
            ),
            (
                "execution trace treated as authority",
                lambda request: request["declared_non_claims"].update(
                    execution_trace_treated_as_authority=True
                ),
                "EXECUTION_TRACE_TREATED_AS_AUTHORITY",
            ),
            (
                "result treated as authority",
                lambda request: request["declared_non_claims"].update(
                    command_result_became_authority=True
                ),
                "COMMAND_RESULT_TREATED_AS_AUTHORITY",
            ),
            (
                "success treated as currentness",
                lambda request: request["declared_non_claims"].update(
                    command_success_created_currentness=True
                ),
                "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS",
            ),
            (
                "success treated as final completion",
                lambda request: request["declared_non_claims"].update(
                    command_success_claimed_final_completion=True
                ),
                "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION",
            ),
            (
                "consumed request reopened",
                lambda request: request["selected_consumed_request_basis"].update(
                    consumed_request_reopened=True
                ),
                "CONSUMED_REQUEST_REOPENED",
            ),
            (
                "authorization token reused",
                lambda request: request["selected_command_invocation_basis"].update(
                    authorization_token_reused=True
                ),
                "AUTHORIZATION_TOKEN_REUSED",
            ),
            (
                "v1 repaired",
                lambda request: request["selected_v1_predecessor_failure_basis"].update(
                    v1_repaired=True
                ),
                "V2_TREATED_AS_REPAIRING_V1",
            ),
            (
                "v1 hidden",
                lambda request: request["selected_v1_predecessor_failure_basis"].update(
                    v1_hidden=True
                ),
                "V1_FAILURE_HIDDEN",
            ),
            (
                "v1 claimed passed",
                lambda request: request["selected_v1_predecessor_failure_basis"].update(
                    v1_claimed_passed=True
                ),
                "V1_CLAIMED_PASSED",
            ),
            (
                "older lineage treated as current execution",
                lambda request: request[
                    "selected_older_command_execution_boundary_lineage_basis"
                ].update(older_command_execution_boundary_lineage_treated_as_current_execution=True),
                "OLDER_COMMAND_EXECUTION_BOUNDARY_LINEAGE_TREATED_AS_CURRENT_EXECUTION",
            ),
            (
                "full prior artifact body emitted",
                lambda request: request["selected_command_report_basis"].update(
                    full_prior_artifact_body=RAW_PRIOR_SENTINEL
                ),
                "FULL_PRIOR_ARTIFACT_BODY_EMITTED",
            ),
            (
                "artifacts mutated",
                lambda request: request["selected_command_report_basis"].update(
                    prior_artifacts_mutated=True
                ),
                "ARTIFACTS_MUTATED",
            ),
            (
                "deployment created",
                lambda request: request["declared_non_claims"].update(deployment_created=True),
                "DEPLOYMENT_CREATED",
            ),
            (
                "runtime hosting created",
                lambda request: request["declared_non_claims"].update(
                    runtime_hosting_created=True
                ),
                "RUNTIME_HOSTING_CREATED",
            ),
            (
                "public release created",
                lambda request: request["declared_non_claims"].update(
                    public_release_created=True
                ),
                "PUBLIC_RELEASE_CREATED",
            ),
            (
                "operation created",
                lambda request: request["declared_non_claims"].update(
                    operation_permission_created=True
                ),
                "OPERATION_CREATED",
            ),
            (
                "public readiness created",
                lambda request: request["declared_non_claims"].update(
                    public_launch_readiness_created=True
                ),
                "PUBLIC_READINESS_CREATED",
            ),
            (
                "final completion claimed",
                lambda request: request["declared_non_claims"].update(
                    final_completion_claimed=True
                ),
                "FINAL_COMPLETION_CLAIMED",
            ),
            (
                "continuation authorized",
                lambda request: request["declared_non_claims"].update(
                    continuation_authorized=True
                ),
                "CONTINUATION_AUTHORIZED",
            ),
            (
                "publication flow opened",
                lambda request: request["declared_non_claims"].update(
                    publication_flow_opened=True
                ),
                "CONTINUATION_AUTHORIZED",
            ),
            (
                "reusable permission created",
                lambda request: request["declared_non_claims"].update(
                    reusable_permission_created=True
                ),
                "REUSABLE_PERMISSION_CREATED",
            ),
            (
                "derivative reception authorized",
                lambda request: request["declared_non_claims"].update(
                    derivative_reception_authorized=True
                ),
                "DERIVATIVE_RECEPTION_AUTHORIZED",
            ),
            (
                "vessel relation authorized",
                lambda request: request["declared_non_claims"].update(
                    vessel_relation_authorized=True
                ),
                "VESSEL_RELATION_AUTHORIZED",
            ),
            (
                "another reception request authorized",
                lambda request: request["declared_non_claims"].update(
                    another_reception_request_authorized=True
                ),
                "ANOTHER_RECEPTION_REQUEST_AUTHORIZED",
            ),
            (
                "follow-on work authorized",
                lambda request: request["declared_non_claims"].update(
                    follow_on_work_authorized=True
                ),
                "FOLLOW_ON_WORK_AUTHORIZED",
            ),
            (
                "mutation performed",
                lambda request: request["declared_non_claims"].update(mutation_performed=True),
                "MUTATION_REPLAY_OR_MERGE_DETECTED",
            ),
            (
                "replay performed",
                lambda request: request["declared_non_claims"].update(replay_performed=True),
                "MUTATION_REPLAY_OR_MERGE_DETECTED",
            ),
            (
                "merge performed",
                lambda request: request["declared_non_claims"].update(merge_performed=True),
                "MUTATION_REPLAY_OR_MERGE_DETECTED",
            ),
            (
                "required non-claim missing",
                lambda request: request["declared_non_claims"].pop("stdout_content_invented"),
                "NON_CLAIM_MISSING_OR_FLIPPED",
            ),
            (
                "required non-claim flipped",
                lambda request: request["declared_non_claims"].update(command_became_authority=True),
                "NON_CLAIM_MISSING_OR_FLIPPED",
            ),
        ]
        for label, mutator, expected_code in cases:
            with self.subTest(label=label):
                result = self.assertBlockedWithCode(_mutated_request(mutator), expected_code)
                result_text = json.dumps(result, sort_keys=True, ensure_ascii=False)
                self.assertNotIn(RAW_PRIOR_SENTINEL, result_text)
                self.assertFalse(result["output_capture_statement"]["command_result_created"])
                self.assertFalse(result["output_capture_statement"]["command_success_created"])
                self.assertFalse(result["output_capture_statement"]["follow_on_work_authorized"])


if __name__ == "__main__":
    unittest.main()
