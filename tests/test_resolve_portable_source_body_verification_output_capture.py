"""Tests for portable source-body verification output capture.

This suite is bounded to output capture only. It is downstream of recorded
output capture boundary and proves that one bounded output-capture event can be
recorded without inventing stdout, stderr, process output, raw output body,
creating a command output/report artifact, creating command result, creating
command success, mutating artifacts, deploying, publishing, continuing, or
authorizing follow-on work.
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

import resolve_portable_source_body_verification_output_capture as resolver
from resolve_portable_source_body_verification_output_capture import (
    build_declared_portable_source_body_verification_output_capture_request,
    build_portable_source_body_verification_output_capture_summary,
    resolve_portable_source_body_verification_output_capture,
    resolve_portable_source_body_verification_output_capture_from_path,
    write_portable_source_body_verification_output_capture_result,
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
RAW_OUTPUT_SENTINEL = "RAW_OUTPUT_CONTENT_MUST_NOT_RETURN_" * 6

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


def _json_text(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=True, default=_json_default)


def _json_default(value: Any) -> Any:
    if isinstance(value, (set, frozenset)):
        return sorted(value)
    if isinstance(value, Path):
        return str(value)
    raise TypeError(f"Object of type {type(value).__name__} is not JSON serializable")


def _json_safe(value: Any) -> Any:
    return json.loads(_json_text(value))


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
    request = build_declared_portable_source_body_verification_output_capture_request(
        output_capture_request_id="output-capture-request-001",
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


def _block_codes(result: dict[str, Any]) -> set[str]:
    codes = {
        check.get("block_code")
        for check in result.get("output_capture_checks", [])
        if not check.get("passed")
    }
    block = result.get("block", {})
    codes.add(block.get("block_code"))
    return {str(code) for code in codes if code}


def _without_raw_values(value: Any) -> bool:
    if isinstance(value, dict):
        for key, nested in value.items():
            if key in FORBIDDEN_RAW_VALUE_KEYS and nested not in ({}, [], None, False):
                return False
            if not _without_raw_values(nested):
                return False
    if isinstance(value, list):
        return all(_without_raw_values(item) for item in value)
    return True


class OutputCaptureResolverTests(unittest.TestCase):
    def assertBlockedWithCode(self, request: Any, expected_code: str) -> dict[str, Any]:
        result = resolve_portable_source_body_verification_output_capture(
            declared_output_capture_request=request
        )
        self.assertEqual(BLOCKED, result["outcome"])
        self.assertTrue(result["block"]["blocked"])
        self.assertIn(expected_code, _block_codes(result))
        statement = result["output_capture_statement"]
        for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertFalse(statement[key], key)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(statement[key], False, key)
            self.assertIs(result["non_claims"][key], False, key)
        return result

    def test_recorded_result_preserves_output_capture_only_shape(self) -> None:
        request = _valid_request()
        original_request = copy.deepcopy(request)
        selected_originals = {key: copy.deepcopy(request[key]) for key in SELECTED_BASIS_KEYS}
        posture_originals = {key: copy.deepcopy(request[key]) for key in POSTURE_KEYS}
        event_original = copy.deepcopy(request["output_capture_event"])
        scope_original = copy.deepcopy(request["output_capture_scope"])

        result = resolve_portable_source_body_verification_output_capture(
            declared_output_capture_request=request
        )

        self.assertIsInstance(result, dict)
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        self.assertEqual(RECORDED, result["outcome"])
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(
            0,
            result["portable_source_body_verification_output_capture_summary"][
                "failed_check_count"
            ],
        )

        metadata = result["portable_source_body_verification_output_capture_metadata"]
        self.assertEqual(
            "0.1.0", metadata["portable_source_body_verification_output_capture_result_version"]
        )
        self.assertEqual(
            "resolve_portable_source_body_verification_output_capture",
            metadata["resolver_module"],
        )
        self.assertEqual(
            "resolve_portable_source_body_verification_output_capture.py",
            metadata["short_resolver_filename"],
        )
        self.assertTrue(metadata["full_upstream_lineage_preserved_inside_selected_basis"])
        self.assertTrue(
            result["selected_output_capture_boundary_basis"]["basis"][
                "full_upstream_lineage_preserved"
            ]
        )
        self.assertTrue(
            result["selected_command_output_basis"]["basis"]["full_upstream_lineage_preserved"]
        )

        boundary = result["selected_output_capture_boundary_basis"]
        self.assertEqual(resolver.OUTPUT_CAPTURE_BOUNDARY_OUTCOME, boundary["outcome"])
        self.assertEqual(0, boundary["failed_check_count"])
        self.assertTrue(boundary["one_future_output_capture_step_declared"])
        self.assertTrue(boundary["stdout_not_captured"])
        self.assertTrue(boundary["stderr_not_captured"])
        self.assertTrue(boundary["process_output_not_captured"])
        self.assertTrue(boundary["raw_output_body_not_captured"])
        self.assertTrue(boundary["output_capture_not_created"])
        self.assertTrue(boundary["command_output_report_artifact_not_created"])
        self.assertTrue(boundary["command_result_not_created"])
        self.assertTrue(boundary["command_success_not_created"])

        command_output = result["selected_command_output_basis"]
        self.assertEqual(resolver.COMMAND_OUTPUT_OUTCOME, command_output["outcome"])
        self.assertEqual(0, command_output["failed_check_count"])
        self.assertTrue(command_output["bounded_command_output_event_recorded"])
        self.assertTrue(command_output["stdout_not_captured"])
        self.assertTrue(command_output["stderr_not_captured"])
        self.assertTrue(command_output["process_output_not_captured"])
        self.assertTrue(command_output["raw_output_body_not_captured"])
        self.assertTrue(command_output["output_capture_not_created"])
        self.assertTrue(command_output["command_output_report_artifact_not_created"])
        self.assertTrue(command_output["command_result_not_created"])
        self.assertTrue(command_output["command_success_not_created"])

        statement = result["output_capture_statement"]
        expected_true = (
            "output_capture_recorded",
            "bounded_output_capture_event_recorded",
            "output_capture_boundary_basis_preserved",
            "command_output_basis_preserved",
            "bounded_command_output_event_preserved",
            "command_output_boundary_basis_preserved",
            "command_output_containment_basis_preserved",
            "recorded_command_execution_event_preserved",
            "execution_trace_audit_only_preserved",
            "stdout_content_absent_without_invention",
            "stderr_content_absent_without_invention",
            "process_output_content_absent_without_invention",
            "raw_output_body_content_absent_without_invention",
            "command_output_report_artifact_not_created",
            "command_result_still_not_created",
            "command_success_still_not_created",
            "authorization_token_reuse_blocked",
            "consumed_request_token_remains_closed",
            "v1_predecessor_failure_preserved",
            "returned_result_containment_preserved",
        )
        for key in expected_true:
            self.assertIs(statement[key], True, key)
        for key in (
            "stdout_content_present",
            "stderr_content_present",
            "process_output_content_present",
            "raw_output_body_content_present",
        ):
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
        for key in FORBIDDEN_RAW_VALUE_KEYS:
            self.assertNotIn(key, event)

        non_meaning = result["output_capture_non_meaning"]
        self.assertFalse(non_meaning["output_report_artifact_exists"])
        self.assertFalse(non_meaning["command_result_exists"])
        self.assertFalse(non_meaning["command_success_exists"])
        self.assertFalse(non_meaning["output_capture_is_authority"])
        self.assertFalse(non_meaning["output_capture_is_currentness"])
        self.assertFalse(non_meaning["output_capture_is_final_completion"])

        summary = result["portable_source_body_verification_output_capture_summary"]
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
        self.assertTrue(
            summary[
                "output_capture_not_report_result_success_source_authority_currentness_final_completion"
            ]
        )
        self.assertTrue(
            summary[
                "command_output_not_report_result_success_source_authority_currentness_final_completion"
            ]
        )
        self.assertTrue(summary["execution_trace_not_output_capture_result_success_source_authority"])
        self.assertTrue(
            summary["older_command_execution_boundary_lineage_not_treated_as_current_execution"]
        )
        self.assertTrue(summary["no_deployment_runtime_public_release"])
        self.assertTrue(summary["no_operation_public_readiness_final_completion"])
        self.assertTrue(summary["no_continuation_publication_reusable_follow_on"])

        self.assertTrue(_without_raw_values(result))
        self.assertEqual(original_request, request)
        for key, original in selected_originals.items():
            self.assertEqual(original, request[key], key)
        for key, original in posture_originals.items():
            self.assertEqual(original, request[key], key)
        self.assertEqual(event_original, request["output_capture_event"])
        self.assertEqual(scope_original, request["output_capture_scope"])

    def test_path_resolution_and_write_behavior_are_bounded(self) -> None:
        request = _valid_request()
        with tempfile.TemporaryDirectory() as tempdir_name:
            tempdir = Path(tempdir_name)
            request_path = tempdir / "request.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")

            result = resolve_portable_source_body_verification_output_capture_from_path(request_path)
            self.assertEqual(RECORDED, result["outcome"])

            malformed_path = tempdir / "malformed.json"
            malformed_path.write_text("{not valid json", encoding="utf-8")
            malformed = resolve_portable_source_body_verification_output_capture_from_path(
                malformed_path
            )
            self.assertEqual(BLOCKED, malformed["outcome"])
            self.assertIn("DECLARED_OUTPUT_CAPTURE_REQUEST_MALFORMED", _block_codes(malformed))

            array_path = tempdir / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolve_portable_source_body_verification_output_capture_from_path(
                array_path
            )
            self.assertEqual(BLOCKED, array_result["outcome"])
            self.assertIn(
                "DECLARED_OUTPUT_CAPTURE_REQUEST_MALFORMED", _block_codes(array_result)
            )

            missing_result = resolve_portable_source_body_verification_output_capture_from_path(
                tempdir / "missing.json"
            )
            self.assertEqual(BLOCKED, missing_result["outcome"])
            self.assertIn(
                "DECLARED_OUTPUT_CAPTURE_REQUEST_UNREADABLE", _block_codes(missing_result)
            )

            output_path = tempdir / "nested" / "output_capture_result.json"
            writable_result = _json_safe(result)
            first_path = write_portable_source_body_verification_output_capture_result(
                writable_result, output_path
            )
            second_path = write_portable_source_body_verification_output_capture_result(
                writable_result, output_path
            )
            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertEqual("output_capture_result_001.json", second_path.name)
            self.assertEqual(RECORDED, json.loads(first_path.read_text(encoding="utf-8"))["outcome"])
            self.assertEqual(RECORDED, json.loads(second_path.read_text(encoding="utf-8"))["outcome"])

            with patch.object(resolver, "OUTPUT_ROOT", tempdir / "default_root"):
                default_path = write_portable_source_body_verification_output_capture_result(
                    writable_result
                )
            self.assertTrue(default_path.exists())
            self.assertIn(
                "portable_source_body_verification_output_capture_result.json",
                default_path.name,
            )

    def test_outcome_family_not_recorded_requires_additional_basis_and_blocked(self) -> None:
        self.assertEqual(OUTCOME_FAMILY, set(resolver.OUTCOME_FAMILY))

        not_recorded_request = _valid_request(
            output_capture_intent=resolver.INTENT_DO_NOT_RECORD,
            requested_output_capture_outcome=NOT_RECORDED,
            not_recorded_basis={"reason": "readable output-capture basis failed review"},
        )
        not_recorded = resolve_portable_source_body_verification_output_capture(
            declared_output_capture_request=not_recorded_request
        )
        self.assertEqual(NOT_RECORDED, not_recorded["outcome"])
        self.assertFalse(not_recorded["block"]["blocked"])
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded"])
        self.assertFalse(not_recorded["output_capture_statement"]["output_capture_recorded"])

        requires_request = _valid_request(
            requested_output_capture_outcome=REQUIRES_ADDITIONAL_BASIS,
            additional_basis_context={
                "missing_basis": "selected command report basis needs clearer reference"
            },
        )
        del requires_request["selected_command_report_basis"]
        requires = resolve_portable_source_body_verification_output_capture(
            declared_output_capture_request=requires_request
        )
        self.assertEqual(REQUIRES_ADDITIONAL_BASIS, requires["outcome"])
        self.assertFalse(requires["block"]["blocked"])
        self.assertTrue(requires["additional_basis_required"]["required"])
        self.assertTrue(requires["additional_basis_required"]["missing_basis_not_authorized"])
        self.assertTrue(requires["additional_basis_required"]["missing_basis_not_executed"])

        blocked = self.assertBlockedWithCode(
            _valid_request(
                output_capture_intent=resolver.INTENT_BLOCK,
                block_reason="explicitly blocked by request",
            ),
            "OUTPUT_CAPTURE_BLOCKED_BY_REQUEST",
        )
        self.assertEqual("OUTPUT_CAPTURE_BLOCKED_BY_REQUEST", blocked["block"]["block_code"])

    def test_blocking_cases_for_boundary_command_output_execution_and_scope(self) -> None:
        cases: list[tuple[str, Any, str]] = [
            ("missing request", None, "OUTPUT_CAPTURE_QUESTION_UNDECLARED"),
            ("non-mapping request", [], "DECLARED_OUTPUT_CAPTURE_REQUEST_MALFORMED"),
            (
                "unsupported intent",
                _mutated_request(lambda request: request.update(output_capture_intent="RUN_IT")),
                "OUTPUT_CAPTURE_INTENT_UNSUPPORTED",
            ),
            (
                "unsupported scope",
                _mutated_request(lambda request: request.update(output_capture_scope=["WRONG"])),
                "UNSUPPORTED_OUTPUT_CAPTURE_SCOPE",
            ),
            (
                "missing boundary basis",
                _mutated_request(lambda request: request.pop("selected_output_capture_boundary_basis")),
                "OUTPUT_CAPTURE_BOUNDARY_BASIS_MISSING",
            ),
            (
                "boundary not recorded",
                _mutated_request(
                    lambda request: request["selected_output_capture_boundary_basis"].update(
                        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_BOUNDARY_NOT_RECORDED"
                    )
                ),
                "OUTPUT_CAPTURE_BOUNDARY_NOT_RECORDED",
            ),
            (
                "boundary failed checks",
                _mutated_request(
                    lambda request: request["selected_output_capture_boundary_basis"].update(
                        failed_check_count=1
                    )
                ),
                "OUTPUT_CAPTURE_BOUNDARY_FAILED_CHECKS_PRESENT",
            ),
            (
                "boundary step not declared",
                _mutated_request(
                    lambda request: request["selected_output_capture_boundary_basis"].update(
                        one_future_output_capture_step_declared=False,
                        output_capture_boundary_recorded=False,
                    )
                ),
                "OUTPUT_CAPTURE_BOUNDARY_STEP_NOT_DECLARED",
            ),
            (
                "boundary stdout captured",
                _mutated_request(
                    lambda request: request["selected_output_capture_boundary_basis"].update(
                        stdout_captured=True
                    )
                ),
                "OUTPUT_CAPTURE_BOUNDARY_ALREADY_CAPTURED_STDOUT",
            ),
            (
                "boundary stderr captured",
                _mutated_request(
                    lambda request: request["selected_output_capture_boundary_basis"].update(
                        stderr_captured=True
                    )
                ),
                "OUTPUT_CAPTURE_BOUNDARY_ALREADY_CAPTURED_STDERR",
            ),
            (
                "boundary process output captured",
                _mutated_request(
                    lambda request: request["selected_output_capture_boundary_basis"].update(
                        process_output_captured=True
                    )
                ),
                "OUTPUT_CAPTURE_BOUNDARY_ALREADY_CAPTURED_PROCESS_OUTPUT",
            ),
            (
                "boundary raw output body captured",
                _mutated_request(
                    lambda request: request["selected_output_capture_boundary_basis"].update(
                        raw_output_body_captured=True
                    )
                ),
                "OUTPUT_CAPTURE_BOUNDARY_ALREADY_CAPTURED_RAW_OUTPUT_BODY",
            ),
            (
                "boundary created output capture",
                _mutated_request(
                    lambda request: request["selected_output_capture_boundary_basis"].update(
                        output_capture_created=True
                    )
                ),
                "OUTPUT_CAPTURE_BOUNDARY_ALREADY_CREATED_OUTPUT_CAPTURE",
            ),
            (
                "boundary created output report",
                _mutated_request(
                    lambda request: request["selected_output_capture_boundary_basis"].update(
                        command_output_report_artifact_created=True
                    )
                ),
                "OUTPUT_CAPTURE_BOUNDARY_ALREADY_CREATED_OUTPUT_REPORT_ARTIFACT",
            ),
            (
                "boundary created result",
                _mutated_request(
                    lambda request: request["selected_output_capture_boundary_basis"].update(
                        command_result_created=True
                    )
                ),
                "OUTPUT_CAPTURE_BOUNDARY_ALREADY_CREATED_RESULT",
            ),
            (
                "boundary created success",
                _mutated_request(
                    lambda request: request["selected_output_capture_boundary_basis"].update(
                        command_success_created=True
                    )
                ),
                "OUTPUT_CAPTURE_BOUNDARY_ALREADY_CREATED_SUCCESS",
            ),
            (
                "missing command output basis",
                _mutated_request(lambda request: request.pop("selected_command_output_basis")),
                "COMMAND_OUTPUT_BASIS_MISSING",
            ),
            (
                "command output not recorded",
                _mutated_request(
                    lambda request: request["selected_command_output_basis"].update(
                        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_NOT_RECORDED"
                    )
                ),
                "COMMAND_OUTPUT_NOT_RECORDED",
            ),
            (
                "command output failed checks",
                _mutated_request(
                    lambda request: request["selected_command_output_basis"].update(
                        failed_check_count=1
                    )
                ),
                "COMMAND_OUTPUT_FAILED_CHECKS_PRESENT",
            ),
            (
                "command output event not recorded",
                _mutated_request(
                    lambda request: request["selected_command_output_basis"].update(
                        bounded_command_output_event_recorded=False,
                        command_output_event_recorded=False,
                        command_output_recorded=False,
                    )
                ),
                "COMMAND_OUTPUT_EVENT_NOT_RECORDED",
            ),
            (
                "command output stdout captured",
                _mutated_request(
                    lambda request: request["selected_command_output_basis"].update(
                        stdout_captured=True
                    )
                ),
                "COMMAND_OUTPUT_ALREADY_CAPTURED_STDOUT",
            ),
            (
                "command output stderr captured",
                _mutated_request(
                    lambda request: request["selected_command_output_basis"].update(
                        stderr_captured=True
                    )
                ),
                "COMMAND_OUTPUT_ALREADY_CAPTURED_STDERR",
            ),
            (
                "command output process output captured",
                _mutated_request(
                    lambda request: request["selected_command_output_basis"].update(
                        process_output_captured=True
                    )
                ),
                "COMMAND_OUTPUT_ALREADY_CAPTURED_PROCESS_OUTPUT",
            ),
            (
                "command output raw output body captured",
                _mutated_request(
                    lambda request: request["selected_command_output_basis"].update(
                        raw_output_body_captured=True
                    )
                ),
                "COMMAND_OUTPUT_ALREADY_CAPTURED_RAW_OUTPUT_BODY",
            ),
            (
                "command output created output capture",
                _mutated_request(
                    lambda request: request["selected_command_output_basis"].update(
                        output_capture_created=True
                    )
                ),
                "COMMAND_OUTPUT_ALREADY_CREATED_OUTPUT_CAPTURE",
            ),
            (
                "command output created output report",
                _mutated_request(
                    lambda request: request["selected_command_output_basis"].update(
                        command_output_report_artifact_created=True
                    )
                ),
                "COMMAND_OUTPUT_ALREADY_CREATED_OUTPUT_REPORT_ARTIFACT",
            ),
            (
                "command output created result",
                _mutated_request(
                    lambda request: request["selected_command_output_basis"].update(
                        command_result_created=True
                    )
                ),
                "COMMAND_OUTPUT_ALREADY_CREATED_RESULT",
            ),
            (
                "command output created success",
                _mutated_request(
                    lambda request: request["selected_command_output_basis"].update(
                        command_success_created=True
                    )
                ),
                "COMMAND_OUTPUT_ALREADY_CREATED_SUCCESS",
            ),
            (
                "missing post-invocation execution",
                _mutated_request(
                    lambda request: request.pop("selected_post_invocation_command_execution_basis")
                ),
                "POST_INVOCATION_COMMAND_EXECUTION_BASIS_MISSING",
            ),
            (
                "post-invocation not recorded",
                _mutated_request(
                    lambda request: request[
                        "selected_post_invocation_command_execution_basis"
                    ].update(outcome="POST_INVOCATION_COMMAND_EXECUTION_NOT_RECORDED")
                ),
                "POST_INVOCATION_COMMAND_EXECUTION_NOT_RECORDED",
            ),
            (
                "post-invocation failed checks",
                _mutated_request(
                    lambda request: request[
                        "selected_post_invocation_command_execution_basis"
                    ].update(failed_check_count=1)
                ),
                "POST_INVOCATION_COMMAND_EXECUTION_FAILED_CHECKS_PRESENT",
            ),
            (
                "post-invocation trace not audit-only",
                _mutated_request(
                    lambda request: request[
                        "selected_post_invocation_command_execution_basis"
                    ].update(
                        execution_trace_audit_only=False,
                        execution_trace_audit_only_preserved=False,
                        execution_trace_recorded_as_audit_only=False,
                    )
                ),
                "POST_INVOCATION_COMMAND_EXECUTION_TRACE_NOT_AUDIT_ONLY",
            ),
        ]
        for label, request, expected_code in cases:
            with self.subTest(label=label):
                self.assertBlockedWithCode(request, expected_code)

    def test_blocking_cases_for_output_capture_command_output_and_trace_collapse(self) -> None:
        flag_cases = {
            "stdout_content_invented": "STDOUT_CONTENT_INVENTED",
            "stderr_content_invented": "STDERR_CONTENT_INVENTED",
            "process_output_content_invented": "PROCESS_OUTPUT_CONTENT_INVENTED",
            "raw_output_body_content_invented": "RAW_OUTPUT_BODY_CONTENT_INVENTED",
            "output_capture_treated_as_output_report_artifact": (
                "OUTPUT_CAPTURE_TREATED_AS_OUTPUT_REPORT_ARTIFACT"
            ),
            "output_capture_treated_as_result": "OUTPUT_CAPTURE_TREATED_AS_RESULT",
            "output_capture_treated_as_success": "OUTPUT_CAPTURE_TREATED_AS_SUCCESS",
            "output_capture_treated_as_source": "OUTPUT_CAPTURE_TREATED_AS_SOURCE",
            "output_capture_treated_as_authority": "OUTPUT_CAPTURE_TREATED_AS_AUTHORITY",
            "output_capture_treated_as_currentness": "OUTPUT_CAPTURE_TREATED_AS_CURRENTNESS",
            "output_capture_treated_as_final_completion": (
                "OUTPUT_CAPTURE_TREATED_AS_FINAL_COMPLETION"
            ),
            "command_output_treated_as_output_report_artifact": (
                "COMMAND_OUTPUT_TREATED_AS_OUTPUT_REPORT_ARTIFACT"
            ),
            "command_output_treated_as_result": "COMMAND_OUTPUT_TREATED_AS_RESULT",
            "command_output_treated_as_success": "COMMAND_OUTPUT_TREATED_AS_SUCCESS",
            "command_output_treated_as_source": "COMMAND_OUTPUT_TREATED_AS_SOURCE",
            "command_output_treated_as_authority": "COMMAND_OUTPUT_TREATED_AS_AUTHORITY",
            "command_output_treated_as_currentness": "COMMAND_OUTPUT_TREATED_AS_CURRENTNESS",
            "command_output_treated_as_final_completion": (
                "COMMAND_OUTPUT_TREATED_AS_FINAL_COMPLETION"
            ),
            "command_output_report_artifact_created": "COMMAND_OUTPUT_REPORT_ARTIFACT_CREATED",
            "command_result_created": "COMMAND_RESULT_CREATED",
            "command_success_created": "COMMAND_SUCCESS_CREATED",
            "execution_trace_treated_as_output_capture": (
                "EXECUTION_TRACE_TREATED_AS_OUTPUT_CAPTURE"
            ),
            "execution_trace_treated_as_result": "EXECUTION_TRACE_TREATED_AS_RESULT",
            "execution_trace_treated_as_success": "EXECUTION_TRACE_TREATED_AS_SUCCESS",
            "execution_trace_treated_as_source": "EXECUTION_TRACE_TREATED_AS_SOURCE",
            "execution_trace_treated_as_authority": "EXECUTION_TRACE_TREATED_AS_AUTHORITY",
            "command_result_became_authority": "COMMAND_RESULT_TREATED_AS_AUTHORITY",
            "command_success_created_currentness": "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS",
            "command_success_claimed_final_completion": (
                "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"
            ),
        }
        for flag, expected_code in flag_cases.items():
            with self.subTest(flag=flag):
                request = _mutated_request(
                    lambda mutable, flag=flag: mutable["declared_non_claims"].update(
                        {flag: True}
                    )
                )
                self.assertBlockedWithCode(request, expected_code)

    def test_blocking_cases_for_token_v1_lineage_artifacts_and_follow_on_overreach(self) -> None:
        cases: list[tuple[str, Callable[[dict[str, Any]], None], str]] = [
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
                "older lineage treated current",
                lambda request: request[
                    "selected_older_command_execution_boundary_lineage_basis"
                ].update(older_command_execution_boundary_lineage_treated_as_current_execution=True),
                "OLDER_COMMAND_EXECUTION_BOUNDARY_LINEAGE_TREATED_AS_CURRENT_EXECUTION",
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
                "runtime created",
                lambda request: request["declared_non_claims"].update(runtime_hosting_created=True),
                "RUNTIME_HOSTING_CREATED",
            ),
            (
                "public release created",
                lambda request: request["declared_non_claims"].update(public_release_created=True),
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
                "merge performed",
                lambda request: request["declared_non_claims"].update(merge_performed=True),
                "MUTATION_REPLAY_OR_MERGE_DETECTED",
            ),
        ]
        for label, mutator, expected_code in cases:
            with self.subTest(label=label):
                self.assertBlockedWithCode(_mutated_request(mutator), expected_code)

    def test_missing_required_basis_and_posture_sections_block(self) -> None:
        missing_basis_cases = {
            "selected_output_capture_boundary_terminal_summary_basis": (
                "OUTPUT_CAPTURE_BOUNDARY_BASIS_MISSING"
            ),
            "selected_command_output_terminal_summary_basis": "COMMAND_OUTPUT_BASIS_MISSING",
            "selected_command_output_boundary_basis": "COMMAND_OUTPUT_BOUNDARY_BASIS_MISSING",
            "selected_command_output_containment_basis": "COMMAND_OUTPUT_CONTAINMENT_BASIS_MISSING",
            "selected_command_invocation_basis": "COMMAND_OUTPUT_BASIS_MISSING",
            "selected_command_execution_review_basis": "COMMAND_OUTPUT_BASIS_MISSING",
            "selected_request_consumption_basis": "COMMAND_OUTPUT_BASIS_MISSING",
            "selected_consumed_request_basis": "CONSUMED_REQUEST_REOPENED",
            "selected_v2_admitted_request_basis": "V2_ADMITTED_REQUEST_BASIS_MISSING",
            "selected_v1_predecessor_failure_basis": "V1_PREDECESSOR_FAILURE_BASIS_MISSING",
            "selected_older_command_execution_boundary_lineage_basis": (
                "OLDER_COMMAND_EXECUTION_BOUNDARY_LINEAGE_TREATED_AS_CURRENT_EXECUTION"
            ),
            "selected_command_report_basis": "COMMAND_REPORT_BASIS_MISSING",
            "selected_command_implementation_boundary_basis": (
                "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING"
            ),
            "selected_command_boundary_basis": "COMMAND_BOUNDARY_BASIS_MISSING",
            "selected_artifact_emission_containment_basis": (
                "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING"
            ),
            "selected_evidence_manifest_basis": "EVIDENCE_MANIFEST_BASIS_MISSING",
            "selected_portable_verification_basis": "PORTABLE_VERIFICATION_BASIS_MISSING",
        }
        for key, expected_code in missing_basis_cases.items():
            with self.subTest(missing_basis=key):
                self.assertBlockedWithCode(
                    _mutated_request(lambda request, key=key: request.pop(key)),
                    expected_code,
                )

        posture_codes = {
            "output_capture_only_posture": "OUTPUT_CAPTURE_ONLY_POSTURE_MISSING",
            "one_bounded_output_capture_event_posture": (
                "ONE_BOUNDED_OUTPUT_CAPTURE_EVENT_POSTURE_MISSING"
            ),
            "output_capture_boundary_basis_preserved_posture": (
                "OUTPUT_CAPTURE_BOUNDARY_BASIS_PRESERVED_POSTURE_MISSING"
            ),
            "command_output_basis_preserved_posture": (
                "COMMAND_OUTPUT_BASIS_PRESERVED_POSTURE_MISSING"
            ),
            "bounded_command_output_event_preserved_posture": (
                "BOUNDED_COMMAND_OUTPUT_EVENT_PRESERVED_POSTURE_MISSING"
            ),
            "execution_trace_audit_only_posture": "EXECUTION_TRACE_AUDIT_ONLY_POSTURE_MISSING",
            "no_stdout_content_invented_posture": "NO_STDOUT_CONTENT_INVENTED_POSTURE_MISSING",
            "no_stderr_content_invented_posture": "NO_STDERR_CONTENT_INVENTED_POSTURE_MISSING",
            "no_process_output_content_invented_posture": (
                "NO_PROCESS_OUTPUT_CONTENT_INVENTED_POSTURE_MISSING"
            ),
            "no_raw_output_body_content_invented_posture": (
                "NO_RAW_OUTPUT_BODY_CONTENT_INVENTED_POSTURE_MISSING"
            ),
            "no_output_report_artifact_posture": "NO_OUTPUT_REPORT_ARTIFACT_POSTURE_MISSING",
            "no_command_result_posture": "NO_COMMAND_RESULT_POSTURE_MISSING",
            "no_command_success_posture": "NO_COMMAND_SUCCESS_POSTURE_MISSING",
            "no_output_as_source_posture": "NO_OUTPUT_AS_SOURCE_POSTURE_MISSING",
            "no_result_as_authority_posture": "NO_RESULT_AS_AUTHORITY_POSTURE_MISSING",
            "no_success_as_currentness_posture": "NO_SUCCESS_AS_CURRENTNESS_POSTURE_MISSING",
            "no_final_completion_posture": "NO_FINAL_COMPLETION_POSTURE_MISSING",
            "authorization_token_reuse_blocked_posture": "AUTHORIZATION_TOKEN_REUSED",
            "consumed_token_closed_posture": "CONSUMED_REQUEST_REOPENED",
            "no_reopen_consumed_request_posture": "CONSUMED_REQUEST_REOPENED",
            "returned_result_containment_posture": "NON_CLAIM_MISSING_OR_FLIPPED",
            "reference_shaped_input_posture": "REFERENCE_SHAPED_INPUT_POSTURE_MISSING",
        }
        for key in POSTURE_KEYS:
            with self.subTest(missing_posture=key):
                self.assertBlockedWithCode(
                    _mutated_request(lambda request, key=key: request.pop(key)),
                    posture_codes[key],
                )

    def test_required_non_claim_missing_or_flipped_blocks(self) -> None:
        missing = _mutated_request(
            lambda request: request["declared_non_claims"].pop("stdout_content_invented")
        )
        self.assertBlockedWithCode(missing, "NON_CLAIM_MISSING_OR_FLIPPED")

        flipped = _mutated_request(
            lambda request: request["declared_non_claims"].update(command_became_authority=True)
        )
        self.assertBlockedWithCode(flipped, "NON_CLAIM_MISSING_OR_FLIPPED")

    def test_raw_prior_and_raw_output_values_are_blocked_and_not_returned(self) -> None:
        full_body_request = _mutated_request(
            lambda request: request["selected_command_report_basis"].update(
                full_prior_artifact_body=RAW_PRIOR_SENTINEL
            )
        )
        full_body_result = self.assertBlockedWithCode(
            full_body_request, "FULL_PRIOR_ARTIFACT_BODY_EMITTED"
        )
        full_body_text = _json_text(full_body_result)
        self.assertNotIn(RAW_PRIOR_SENTINEL, full_body_text)
        self.assertIn("full_prior_artifact_body_omitted", full_body_text)
        self.assertIn("full prior artifact body not emitted", full_body_text)

        raw_output_request = _mutated_request(
            lambda request: request["selected_command_output_basis"].update(
                stdout_content=RAW_OUTPUT_SENTINEL
            )
        )
        raw_output_result = self.assertBlockedWithCode(
            raw_output_request, "STDOUT_CONTENT_INVENTED"
        )
        raw_output_text = _json_text(raw_output_result)
        self.assertNotIn(RAW_OUTPUT_SENTINEL, raw_output_text)
        self.assertIn("stdout_content_omitted", raw_output_text)
        self.assertIn("raw output content not emitted", raw_output_text)

    def test_summary_helper_preserves_bounded_non_authoritative_shape(self) -> None:
        result = resolve_portable_source_body_verification_output_capture(
            declared_output_capture_request=_valid_request()
        )
        summary = build_portable_source_body_verification_output_capture_summary(result)

        self.assertEqual(RECORDED, summary["outcome"])
        self.assertIsNone(summary["block_code"])
        self.assertEqual(0, summary["failed_check_count"])
        self.assertTrue(summary["output_capture_recorded"])
        self.assertTrue(summary["bounded_output_capture_event_recorded"])
        self.assertTrue(summary["output_capture_boundary_basis_preserved"])
        self.assertTrue(summary["command_output_basis_preserved"])
        self.assertTrue(summary["bounded_command_output_event_preserved"])
        self.assertTrue(summary["recorded_command_execution_event_preserved"])
        self.assertTrue(summary["execution_trace_audit_only_preserved"])
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
        self.assertTrue(
            summary[
                "output_capture_not_report_result_success_source_authority_currentness_final_completion"
            ]
        )
        self.assertTrue(summary["result_not_authority"])
        self.assertTrue(summary["success_not_currentness_final_completion"])
        self.assertTrue(summary["no_raw_full_prior_artifact_body"])
        self.assertTrue(summary["no_artifact_mutation"])
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(summary["key_non_claims"][key], False, key)


if __name__ == "__main__":
    unittest.main()
