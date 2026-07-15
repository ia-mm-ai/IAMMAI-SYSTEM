"""Tests for portable source-body verification command output only.

This suite is downstream of recorded command output boundary. It proves that
one bounded command output event/posture can be recorded without capturing
stdout, stderr, process output, or raw command output body, and without
creating output capture, an output/report artifact, command result, command
success, authority, currentness, final completion, continuation, reusable
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
from typing import Any, Callable
from unittest.mock import patch


sys.dont_write_bytecode = True

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_portable_source_body_verification_command_output as resolver
from resolve_portable_source_body_verification_command_output import (
    build_declared_portable_source_body_verification_command_output_request,
    build_portable_source_body_verification_command_output_summary,
    resolve_portable_source_body_verification_command_output,
    resolve_portable_source_body_verification_command_output_from_path,
    write_portable_source_body_verification_command_output_result,
)


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}
QUESTION = resolver.CORE_QUESTION
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_COMMAND_OUTPUT_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
RAW_OUTPUT_SENTINEL = "RAW_COMMAND_OUTPUT_VALUE_MUST_NOT_RETURN_" * 6
RAW_PRIOR_SENTINEL = "RAW_COMMAND_OUTPUT_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN_" * 6

TOP_LEVEL_SECTIONS = tuple(resolver.TOP_LEVEL_SECTIONS)

POSTURE_KEYS = (
    "command_output_only_posture",
    "one_bounded_command_output_event_posture",
    "command_output_boundary_basis_preserved_posture",
    "command_output_containment_basis_preserved_posture",
    "bounded_output_containment_event_preserved_posture",
    "execution_trace_audit_only_posture",
    "no_output_capture_posture",
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
)

SELECTED_BASIS_KEYS = (
    "selected_command_output_boundary_basis",
    "selected_command_output_boundary_terminal_summary_basis",
    "selected_command_output_containment_basis",
    "selected_command_output_containment_terminal_summary_basis",
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
)

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
    return json.dumps(value, sort_keys=True, ensure_ascii=True)


def _false_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _reference_shape(label: str, **extra: Any) -> dict[str, Any]:
    basis = {
        "basis_label": label,
        "declared": True,
        "basis_reference": f"synthetic://{label}",
        "reference_shaped_basis": True,
        "basis_remains_reference_shaped": True,
        "basis_reference_shape_preserved": True,
        "basis_remains_basis_only": True,
        "basis_is_not_output_capture": True,
        "basis_is_not_command_output_report_artifact": True,
        "basis_is_not_command_result": True,
        "basis_is_not_command_success": True,
        "basis_is_not_source": True,
        "basis_is_not_authority": True,
        "basis_is_not_currentness": True,
        "basis_is_not_final_completion": True,
        "basis_does_not_authorize_continuation_reusable_permission_follow_on_work": True,
        "basis_does_not_create_deployment_runtime_public_release": True,
        "full_upstream_lineage_preserved": True,
        "upstream_lineage": (
            "v2_admission -> request_consumption -> command_execution_review -> "
            "command_invocation -> post_invocation_command_execution -> "
            "command_output_containment -> command_output_boundary -> command_output"
        ),
        "full_prior_artifact_body_not_emitted": True,
        "raw_full_prior_artifact_body_returned": False,
        "prior_artifacts_mutated": False,
    }
    basis.update(extra)
    return basis


def _terminal_summary_basis(label: str, **extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        label,
        terminal_summary_declared=True,
        terminal_summary_path=f"spec/{label}.md",
        terminal_summary_remains_readability_basis_only=True,
        readability_basis_only=True,
        does_not_create_output_capture=True,
        does_not_create_output_report_artifact=True,
        does_not_create_command_output_report_artifact=True,
        does_not_create_command_result=True,
        does_not_create_command_success=True,
        does_not_authorize_follow_on_work=True,
    )
    basis.update(extra)
    return basis


def _command_output_event(**extra: Any) -> dict[str, Any]:
    event = {
        "command_output_event_recorded": True,
        "event_type": "COMMAND_OUTPUT_EVENT_BOUNDED",
        "stdout_captured": False,
        "stderr_captured": False,
        "process_output_captured": False,
        "raw_output_body_captured": False,
        "output_capture_created": False,
        "command_output_report_artifact_created": False,
        "command_result_created": False,
        "command_success_created": False,
        "command_output_is_not_output_capture": True,
        "command_output_is_not_output_report_artifact": True,
        "command_output_is_not_result": True,
        "command_output_is_not_success": True,
        "command_output_is_not_source": True,
        "command_output_is_not_authority": True,
        "command_output_is_not_currentness": True,
        "command_output_is_not_final_completion": True,
    }
    event.update(extra)
    return event


def _posture(label: str, **extra: Any) -> dict[str, Any]:
    posture = {
        "declared": True,
        "posture_declared": True,
        "posture_label": label,
        label: True,
        "command_output_only": True,
        "one_bounded_command_output_event_recorded": True,
        "command_output_boundary_basis_preserved": True,
        "command_output_containment_basis_preserved": True,
        "bounded_output_containment_event_preserved": True,
        "recorded_command_execution_event_preserved": True,
        "execution_trace_audit_only": True,
        "execution_trace_audit_only_preserved": True,
        "stdout_captured": False,
        "stderr_captured": False,
        "process_output_captured": False,
        "raw_output_body_captured": False,
        "output_capture_created": False,
        "command_output_report_artifact_created": False,
        "output_report_artifact_created": False,
        "command_result_created": False,
        "command_success_created": False,
        "output_capture_not_created": True,
        "command_output_report_artifact_not_created": True,
        "output_report_artifact_not_created": True,
        "command_result_not_created": True,
        "command_result_still_not_created": True,
        "command_success_not_created": True,
        "command_success_still_not_created": True,
        "command_output_treated_as_output_capture": False,
        "command_output_treated_as_output_report_artifact": False,
        "command_output_treated_as_result": False,
        "command_output_treated_as_success": False,
        "command_output_treated_as_source": False,
        "command_output_treated_as_authority": False,
        "command_output_treated_as_currentness": False,
        "command_output_treated_as_final_completion": False,
        "boundary_treated_as_output": False,
        "containment_treated_as_output": False,
        "execution_trace_treated_as_output": False,
        "execution_trace_treated_as_result": False,
        "execution_trace_treated_as_success": False,
        "execution_trace_treated_as_source": False,
        "execution_trace_treated_as_authority": False,
        "command_result_became_authority": False,
        "command_success_created_currentness": False,
        "command_success_claimed_final_completion": False,
        "authorization_token_reused": False,
        "authorization_token_reuse_blocked": True,
        "consumed_request_reopened": False,
        "consumed_request_token_remains_closed": True,
        "returned_result_containment_preserved": True,
        "raw_full_prior_artifact_body_returned": False,
    }
    posture.update(extra)
    return posture


def _valid_request(**overrides: Any) -> dict[str, Any]:
    request = build_declared_portable_source_body_verification_command_output_request(
        command_output_request_id="command-output-request-001",
        command_output_question=QUESTION,
        command_output_intent=resolver.INTENT_RECORD,
    )
    request["selected_command_output_boundary_basis"].update(
        _reference_shape(
            "selected_command_output_boundary_basis",
            result_id="command-output-boundary-result-001",
            result_path="artifacts/synthetic/command_output_boundary.json",
            outcome=resolver.COMMAND_OUTPUT_BOUNDARY_OUTCOME,
            failed_check_count=0,
            passed_check_count=62,
            one_future_command_output_step_declared=True,
            command_output_created=False,
            output_capture_created=False,
            command_output_report_artifact_created=False,
            output_report_artifact_created=False,
            command_result_created=False,
            command_success_created=False,
            command_output_not_created=True,
            output_capture_not_created=True,
            command_output_report_artifact_not_created=True,
            output_report_artifact_not_created=True,
            command_result_not_created=True,
            command_success_not_created=True,
        )
    )
    request["selected_command_output_boundary_terminal_summary_basis"] = _terminal_summary_basis(
        "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_BOUNDARY_TERMINAL_SUMMARY_V0"
    )
    request["selected_command_output_containment_basis"].update(
        _reference_shape(
            "selected_command_output_containment_basis",
            result_id="command-output-containment-result-001",
            result_path="artifacts/synthetic/command_output_containment.json",
            outcome=resolver.COMMAND_OUTPUT_CONTAINMENT_OUTCOME,
            failed_check_count=0,
            passed_check_count=64,
            command_output_containment_recorded=True,
            bounded_command_output_containment_event_recorded=True,
            one_bounded_command_output_containment_event_recorded=True,
            command_output_boundary_basis_preserved=True,
            output_capture_created=False,
            command_output_report_artifact_created=False,
            output_report_artifact_created=False,
            command_result_created=False,
            command_success_created=False,
            output_capture_not_created=True,
            command_output_report_artifact_not_created=True,
            output_report_artifact_not_created=True,
            command_result_not_created=True,
            command_success_not_created=True,
        )
    )
    request["selected_command_output_containment_terminal_summary_basis"] = _terminal_summary_basis(
        "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_CONTAINMENT_TERMINAL_SUMMARY_V0"
    )
    request["selected_post_invocation_command_execution_basis"].update(
        _reference_shape(
            "selected_post_invocation_command_execution_basis",
            outcome=resolver.POST_INVOCATION_COMMAND_EXECUTION_OUTCOME,
            failed_check_count=0,
            one_bounded_command_execution_event_recorded=True,
            bounded_command_execution_event_recorded=True,
            recorded_command_execution_event_preserved=True,
            execution_trace_audit_only=True,
            execution_trace_audit_only_preserved=True,
            command_output_treated_as_source=False,
            command_output_treated_as_authority=False,
            command_output_treated_as_currentness=False,
            command_output_treated_as_final_completion=False,
            output_capture_created=False,
            command_result_created=False,
            command_success_created=False,
        )
    )
    request["selected_post_invocation_command_execution_terminal_summary_basis"] = _terminal_summary_basis(
        "PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_TERMINAL_SUMMARY_V0"
    )
    request["selected_command_invocation_basis"].update(
        _reference_shape(
            "selected_command_invocation_basis",
            outcome=resolver.COMMAND_INVOCATION_OUTCOME,
            failed_check_count=0,
            bounded_command_invocation_event_recorded=True,
            authorization_token_spent_exactly_once=True,
            authorization_token_reuse_blocked=True,
        )
    )
    request["selected_command_execution_review_basis"].update(
        _reference_shape(
            "selected_command_execution_review_basis",
            outcome=resolver.COMMAND_EXECUTION_REVIEW_OUTCOME,
            failed_check_count=0,
            review_basis_only=True,
        )
    )
    request["selected_request_consumption_basis"].update(
        _reference_shape(
            "selected_request_consumption_basis",
            outcome=resolver.REQUEST_CONSUMPTION_OUTCOME,
            failed_check_count=0,
            request_consumed_exactly_once=True,
            consumption_token_closed=True,
            consumed_request_basis_recorded=True,
        )
    )
    request["selected_consumed_request_basis"].update(
        _reference_shape(
            "selected_consumed_request_basis",
            consumed_request_basis_declared=True,
            consumed_request_token_remains_closed=True,
            consumed_request_is_not_reopened=True,
            consumed_request_reopened=False,
            consumed_request_basis_is_basis_only=True,
        )
    )
    request["selected_v2_admitted_request_basis"].update(
        _reference_shape(
            "selected_v2_admitted_request_basis",
            outcome=resolver.V2_ADMITTED_REQUEST_OUTCOME,
            result_version=resolver.V2_ADMITTED_REQUEST_VERSION,
            failed_check_count=0,
            successor_metadata_preserved=True,
            returned_result_containment_preserved=True,
            v2_does_not_claim_v1_passed=True,
            v2_successor_does_not_repair_v1=True,
            v2_treated_as_repairing_v1=False,
            v2_repairs_v1=False,
        )
    )
    request["selected_v1_predecessor_failure_basis"].update(
        _reference_shape(
            "selected_v1_predecessor_failure_basis",
            v1_predecessor_failure_basis_declared=True,
            v1_remains_visible_predecessor_failure_evidence=True,
            v1_is_not_repaired=True,
            v1_is_not_hidden=True,
            v1_is_not_claimed_passed=True,
            v1_repaired=False,
            v1_hidden=False,
            v1_claimed_passed=False,
            v2_successor_does_not_erase_v1=True,
            predecessor_failure_evidence_is_lineage_evidence_only=True,
        )
    )
    request["selected_older_command_execution_boundary_lineage_basis"].update(
        _reference_shape(
            "selected_older_command_execution_boundary_lineage_basis",
            basis_remains_prior_scaffolding_only=True,
            lineage_basis_not_treated_as_current_execution=True,
            older_command_execution_boundary_lineage_treated_as_current_execution=False,
            output_capture_created=False,
            command_result_created=False,
            command_success_created=False,
        )
    )
    for key in (
        "selected_command_report_basis",
        "selected_command_implementation_boundary_basis",
        "selected_command_boundary_basis",
        "selected_artifact_emission_containment_basis",
        "selected_evidence_manifest_basis",
        "selected_portable_verification_basis",
    ):
        request[key].update(_reference_shape(key))
    request["command_output_event"] = _command_output_event()
    request["command_output_scope"] = list(SUPPORTED_SCOPE)
    request["requested_command_output_outcome"] = RECORDED
    request["declared_non_claims"] = _false_non_claims()
    request["reference_shaped_input_posture"] = {
        "declared": True,
        "reference_shaped_input_posture": True,
        "full_prior_artifact_body_not_emitted": True,
    }
    for key in POSTURE_KEYS:
        request[key] = _posture(key)
    request.update(overrides)
    return request


def _resolve(request: dict[str, Any]) -> dict[str, Any]:
    return resolve_portable_source_body_verification_command_output(
        declared_command_output_request=request
    )


def _nested_set(mapping: dict[str, Any], path: tuple[str, ...], value: Any) -> None:
    current: dict[str, Any] = mapping
    for key in path[:-1]:
        current = current[key]
    current[path[-1]] = value


def _nested_pop(mapping: dict[str, Any], path: tuple[str, ...]) -> None:
    current: dict[str, Any] = mapping
    for key in path[:-1]:
        current = current[key]
    current.pop(path[-1])


def _contains_forbidden_raw_value(value: Any) -> bool:
    if isinstance(value, dict):
        for key, nested in value.items():
            if key in FORBIDDEN_RAW_VALUE_KEYS and nested not in (False, None, "", {}):
                return True
            if _contains_forbidden_raw_value(nested):
                return True
    elif isinstance(value, list):
        return any(_contains_forbidden_raw_value(item) for item in value)
    return False


class CommandOutputResolverTests(unittest.TestCase):
    def assertBlocked(self, request: dict[str, Any], expected_code: str | set[str]) -> dict[str, Any]:
        result = _resolve(request)
        self.assertEqual(BLOCKED, result["outcome"])
        codes = {expected_code} if isinstance(expected_code, str) else expected_code
        self.assertIn(result["block"]["block_code"], codes)
        statement = result["command_output_statement"]
        for false_key in (
            "stdout_captured",
            "stderr_captured",
            "process_output_captured",
            "raw_output_body_captured",
            "output_capture_created",
            "command_output_report_artifact_created",
            "command_result_created",
            "command_success_created",
            "command_output_treated_as_output_capture",
            "command_output_treated_as_output_report_artifact",
            "command_output_treated_as_result",
            "command_output_treated_as_success",
            "command_output_treated_as_source",
            "command_output_treated_as_authority",
            "command_output_treated_as_currentness",
            "command_output_treated_as_final_completion",
            "boundary_treated_as_output",
            "containment_treated_as_output",
            "execution_trace_treated_as_output",
            "command_result_became_authority",
            "command_success_created_currentness",
            "command_success_claimed_final_completion",
            "follow_on_work_authorized",
        ):
            self.assertFalse(statement[false_key], false_key)
        return result

    def test_recorded_result_preserves_command_output_only_shape(self) -> None:
        request = _valid_request()
        result = _resolve(request)

        self.assertIsInstance(result, dict)
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        self.assertEqual(RECORDED, result["outcome"])
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(0, result["portable_source_body_verification_command_output_summary"]["failed_check_count"])

        metadata = result["portable_source_body_verification_command_output_metadata"]
        self.assertEqual("0.1.0", metadata["portable_source_body_verification_command_output_result_version"])
        self.assertEqual("resolve_portable_source_body_verification_command_output", metadata["resolver_module"])
        self.assertEqual("resolve_portable_source_body_verification_command_output.py", metadata["short_resolver_filename"])
        self.assertTrue(metadata["full_upstream_lineage_preserved_inside_selected_basis"])

        statement = result["command_output_statement"]
        for key in (
            "command_output_recorded",
            "bounded_command_output_event_recorded",
            "command_output_boundary_basis_preserved",
            "command_output_containment_basis_preserved",
            "bounded_output_containment_event_preserved",
            "recorded_command_execution_event_preserved",
            "execution_trace_audit_only_preserved",
            "output_capture_not_created",
            "command_output_report_artifact_not_created",
            "command_result_still_not_created",
            "command_success_still_not_created",
            "authorization_token_reuse_blocked",
            "consumed_request_token_remains_closed",
            "v1_predecessor_failure_preserved",
            "returned_result_containment_preserved",
        ):
            self.assertTrue(statement[key], key)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, result["non_claims"])
            self.assertFalse(result["non_claims"][key], key)
            self.assertFalse(statement.get(key, False), key)

        event = result["command_output_event"]
        self.assertTrue(event["command_output_event_recorded"])
        self.assertEqual("COMMAND_OUTPUT_EVENT_BOUNDED", event["event_type"])
        for key in (
            "stdout_captured",
            "stderr_captured",
            "process_output_captured",
            "raw_output_body_captured",
            "output_capture_created",
            "command_output_report_artifact_created",
            "command_result_created",
            "command_success_created",
        ):
            self.assertFalse(event[key], key)
        for key in (
            "command_output_is_not_output_capture",
            "command_output_is_not_output_report_artifact",
            "command_output_is_not_result",
            "command_output_is_not_success",
            "command_output_is_not_source",
            "command_output_is_not_authority",
            "command_output_is_not_currentness",
            "command_output_is_not_final_completion",
        ):
            self.assertTrue(event[key], key)
        self.assertFalse(_contains_forbidden_raw_value(result))

        boundary = result["selected_command_output_boundary_basis"]
        self.assertEqual(resolver.COMMAND_OUTPUT_BOUNDARY_OUTCOME, boundary["outcome"])
        self.assertEqual(0, boundary["failed_check_count"])
        self.assertTrue(boundary["one_future_command_output_step_declared"])
        self.assertTrue(boundary["output_capture_not_created"])
        self.assertTrue(boundary["command_output_report_artifact_not_created"])
        self.assertTrue(boundary["command_result_not_created"])
        self.assertTrue(boundary["command_success_not_created"])

        containment = result["selected_command_output_containment_basis"]
        self.assertEqual(resolver.COMMAND_OUTPUT_CONTAINMENT_OUTCOME, containment["outcome"])
        self.assertEqual(0, containment["failed_check_count"])
        self.assertTrue(containment["bounded_output_containment_event_recorded"])
        self.assertTrue(containment["command_output_boundary_basis_preserved"])

        post_invocation = result["selected_post_invocation_command_execution_basis"]
        self.assertEqual(resolver.POST_INVOCATION_COMMAND_EXECUTION_OUTCOME, post_invocation["outcome"])
        self.assertEqual(0, post_invocation["failed_check_count"])
        self.assertTrue(post_invocation["bounded_command_execution_event_recorded"])
        self.assertTrue(post_invocation["execution_trace_audit_only"])

        v2 = result["selected_v2_admitted_request_basis"]
        self.assertEqual(resolver.V2_ADMITTED_REQUEST_OUTCOME, v2["outcome"])
        self.assertEqual(resolver.V2_ADMITTED_REQUEST_VERSION, v2["version"])
        self.assertEqual(0, v2["failed_check_count"])
        self.assertTrue(
            result["selected_older_command_execution_boundary_lineage_basis"][
                "lineage_basis_not_treated_as_current_execution"
            ]
        )
        self.assertIn("command result", result["what_remains_open"]["open_items"])
        self.assertTrue(result["what_remains_open"]["open_means_not_authorized"])

    def test_path_and_write_behaviour_are_bounded(self) -> None:
        request = _valid_request()
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request_path = tmp_path / "request.json"
            request_path.write_text(json.dumps(request, sort_keys=True), encoding="utf-8")

            from_path = resolve_portable_source_body_verification_command_output_from_path(request_path)
            self.assertEqual(RECORDED, from_path["outcome"])

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            malformed = resolve_portable_source_body_verification_command_output_from_path(malformed_path)
            self.assertEqual(BLOCKED, malformed["outcome"])
            self.assertEqual("DECLARED_COMMAND_OUTPUT_REQUEST_UNREADABLE", malformed["block"]["block_code"])

            array_path = tmp_path / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolve_portable_source_body_verification_command_output_from_path(array_path)
            self.assertEqual(BLOCKED, array_result["outcome"])
            self.assertEqual("DECLARED_COMMAND_OUTPUT_REQUEST_MALFORMED", array_result["block"]["block_code"])

            missing = resolve_portable_source_body_verification_command_output_from_path(tmp_path / "missing.json")
            self.assertEqual(BLOCKED, missing["outcome"])
            self.assertEqual("DECLARED_COMMAND_OUTPUT_REQUEST_UNREADABLE", missing["block"]["block_code"])

            with patch.object(resolver, "OUTPUT_ROOT", tmp_path / "results"):
                first = write_portable_source_body_verification_command_output_result(from_path)
                second = write_portable_source_body_verification_command_output_result(from_path)
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertTrue(first.parent.exists())
            self.assertEqual(RECORDED, json.loads(first.read_text(encoding="utf-8"))["outcome"])

    def test_outcome_family_not_recorded_requires_additional_basis_and_blocked(self) -> None:
        self.assertEqual(
            OUTCOME_FAMILY,
            {
                resolver.OUTCOME_RECORDED,
                resolver.OUTCOME_NOT_RECORDED,
                resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                resolver.OUTCOME_BLOCKED,
            },
        )

        not_recorded_request = _valid_request(
            command_output_intent=resolver.INTENT_DO_NOT_RECORD,
            requested_command_output_outcome=NOT_RECORDED,
            not_recorded_basis={"review_readable": True, "recording_declined": True},
        )
        not_recorded = _resolve(not_recorded_request)
        self.assertEqual(NOT_RECORDED, not_recorded["outcome"])
        self.assertFalse(not_recorded["block"]["blocked"])
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded"])
        self.assertFalse(not_recorded["command_output_statement"]["command_output_recorded"])

        needs_basis_request = _valid_request(
            requested_command_output_outcome=REQUIRES_ADDITIONAL_BASIS,
            additional_basis_context={"missing": "command report basis unclear"},
        )
        _nested_pop(needs_basis_request, ("selected_command_report_basis",))
        needs_basis = _resolve(needs_basis_request)
        self.assertEqual(REQUIRES_ADDITIONAL_BASIS, needs_basis["outcome"])
        self.assertTrue(needs_basis["additional_basis_required"]["required"])
        self.assertTrue(needs_basis["additional_basis_required"]["missing_basis_not_authorized"])

        blocked = _resolve(_valid_request(command_output_intent=resolver.INTENT_BLOCK))
        self.assertEqual(BLOCKED, blocked["outcome"])
        self.assertEqual("COMMAND_OUTPUT_BLOCKED_BY_REQUEST", blocked["block"]["block_code"])

    def test_blocking_cases_for_boundary_containment_execution_and_scope(self) -> None:
        cases: list[tuple[str, Callable[[dict[str, Any]], None], str | set[str]]] = [
            ("missing request", lambda request: None, "COMMAND_OUTPUT_QUESTION_UNDECLARED"),
            ("unsupported intent", lambda request: request.__setitem__("command_output_intent", "UNSUPPORTED"), "COMMAND_OUTPUT_INTENT_UNSUPPORTED"),
            ("unsupported scope", lambda request: request.__setitem__("command_output_scope", ["UNSUPPORTED_SCOPE"]), "UNSUPPORTED_COMMAND_OUTPUT_SCOPE"),
            ("missing boundary basis", lambda request: _nested_pop(request, ("selected_command_output_boundary_basis",)), "COMMAND_OUTPUT_BOUNDARY_BASIS_MISSING"),
            ("boundary not recorded", lambda request: _nested_set(request, ("selected_command_output_boundary_basis", "outcome"), "NO"), "COMMAND_OUTPUT_BOUNDARY_NOT_RECORDED"),
            ("boundary failed checks", lambda request: _nested_set(request, ("selected_command_output_boundary_basis", "failed_check_count"), 1), "COMMAND_OUTPUT_BOUNDARY_FAILED_CHECKS_PRESENT"),
            ("boundary step not declared", lambda request: _nested_set(request, ("selected_command_output_boundary_basis", "one_future_command_output_step_declared"), False), "COMMAND_OUTPUT_BOUNDARY_STEP_NOT_DECLARED"),
            ("boundary created output", lambda request: _nested_set(request, ("selected_command_output_boundary_basis", "command_output_created"), True), "COMMAND_OUTPUT_BOUNDARY_ALREADY_CREATED_OUTPUT"),
            ("boundary created capture", lambda request: _nested_set(request, ("selected_command_output_boundary_basis", "output_capture_created"), True), "COMMAND_OUTPUT_BOUNDARY_ALREADY_CREATED_OUTPUT_CAPTURE"),
            ("boundary created report", lambda request: _nested_set(request, ("selected_command_output_boundary_basis", "command_output_report_artifact_created"), True), "COMMAND_OUTPUT_BOUNDARY_ALREADY_CREATED_OUTPUT_REPORT_ARTIFACT"),
            ("boundary created result", lambda request: _nested_set(request, ("selected_command_output_boundary_basis", "command_result_created"), True), "COMMAND_OUTPUT_BOUNDARY_ALREADY_CREATED_RESULT"),
            ("boundary created success", lambda request: _nested_set(request, ("selected_command_output_boundary_basis", "command_success_created"), True), "COMMAND_OUTPUT_BOUNDARY_ALREADY_CREATED_SUCCESS"),
            ("missing containment", lambda request: _nested_pop(request, ("selected_command_output_containment_basis",)), "COMMAND_OUTPUT_CONTAINMENT_BASIS_MISSING"),
            ("containment not recorded", lambda request: _nested_set(request, ("selected_command_output_containment_basis", "outcome"), "NO"), "COMMAND_OUTPUT_CONTAINMENT_NOT_RECORDED"),
            ("containment failed checks", lambda request: _nested_set(request, ("selected_command_output_containment_basis", "failed_check_count"), 1), "COMMAND_OUTPUT_CONTAINMENT_FAILED_CHECKS_PRESENT"),
            ("containment event missing", lambda request: (_nested_set(request, ("selected_command_output_containment_basis", "bounded_command_output_containment_event_recorded"), False), _nested_set(request, ("selected_command_output_containment_basis", "one_bounded_command_output_containment_event_recorded"), False), _nested_set(request, ("selected_command_output_containment_basis", "command_output_containment_recorded"), False)), "COMMAND_OUTPUT_CONTAINMENT_EVENT_NOT_RECORDED"),
            ("containment boundary basis not preserved", lambda request: _nested_set(request, ("selected_command_output_containment_basis", "command_output_boundary_basis_preserved"), False), "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_BASIS_NOT_PRESERVED"),
            ("missing execution", lambda request: _nested_pop(request, ("selected_post_invocation_command_execution_basis",)), "POST_INVOCATION_COMMAND_EXECUTION_BASIS_MISSING"),
            ("execution not recorded", lambda request: _nested_set(request, ("selected_post_invocation_command_execution_basis", "outcome"), "NO"), "POST_INVOCATION_COMMAND_EXECUTION_NOT_RECORDED"),
            ("execution failed checks", lambda request: _nested_set(request, ("selected_post_invocation_command_execution_basis", "failed_check_count"), 1), "POST_INVOCATION_COMMAND_EXECUTION_FAILED_CHECKS_PRESENT"),
            ("execution trace not audit only", lambda request: (_nested_set(request, ("selected_post_invocation_command_execution_basis", "execution_trace_audit_only"), False), _nested_set(request, ("selected_post_invocation_command_execution_basis", "execution_trace_audit_only_preserved"), False), request.__setitem__("selected_post_invocation_command_execution_trace_audit_only", False)), "POST_INVOCATION_COMMAND_EXECUTION_TRACE_NOT_AUDIT_ONLY"),
        ]

        none_result = resolve_portable_source_body_verification_command_output(None)
        self.assertEqual(BLOCKED, none_result["outcome"])
        self.assertEqual("COMMAND_OUTPUT_QUESTION_UNDECLARED", none_result["block"]["block_code"])
        non_mapping = resolve_portable_source_body_verification_command_output(["not", "mapping"])  # type: ignore[arg-type]
        self.assertEqual(BLOCKED, non_mapping["outcome"])
        self.assertEqual("DECLARED_COMMAND_OUTPUT_REQUEST_MALFORMED", non_mapping["block"]["block_code"])

        for name, mutate, code in cases[1:]:
            with self.subTest(name=name):
                request = _valid_request()
                mutate(request)
                self.assertBlocked(request, code)

    def test_blocking_cases_for_capture_result_success_and_authority_collapse(self) -> None:
        cases: list[tuple[str, tuple[str, ...], Any, str]] = [
            ("stdout captured", ("command_output_event", "stdout_captured"), True, "STDOUT_CAPTURED"),
            ("stderr captured", ("command_output_event", "stderr_captured"), True, "STDERR_CAPTURED"),
            ("process output captured", ("command_output_event", "process_output_captured"), True, "PROCESS_OUTPUT_CAPTURED"),
            ("raw output body captured", ("command_output_event", "raw_output_body_captured"), True, "RAW_OUTPUT_BODY_CAPTURED"),
            ("output capture created", ("command_output_event", "output_capture_created"), True, "OUTPUT_CAPTURE_CREATED"),
            ("output report created", ("command_output_event", "command_output_report_artifact_created"), True, "COMMAND_OUTPUT_REPORT_ARTIFACT_CREATED"),
            ("command result created", ("command_output_event", "command_result_created"), True, "COMMAND_RESULT_CREATED"),
            ("command success created", ("command_output_event", "command_success_created"), True, "COMMAND_SUCCESS_CREATED"),
            ("output as capture", ("command_output_only_posture", "command_output_treated_as_output_capture"), True, "COMMAND_OUTPUT_TREATED_AS_OUTPUT_CAPTURE"),
            ("output as report", ("command_output_only_posture", "command_output_treated_as_output_report_artifact"), True, "COMMAND_OUTPUT_TREATED_AS_OUTPUT_REPORT_ARTIFACT"),
            ("output as result", ("command_output_only_posture", "command_output_treated_as_result"), True, "COMMAND_OUTPUT_TREATED_AS_RESULT"),
            ("output as success", ("command_output_only_posture", "command_output_treated_as_success"), True, "COMMAND_OUTPUT_TREATED_AS_SUCCESS"),
            ("output as source", ("command_output_only_posture", "command_output_treated_as_source"), True, "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
            ("output as authority", ("command_output_only_posture", "command_output_treated_as_authority"), True, "COMMAND_OUTPUT_TREATED_AS_AUTHORITY"),
            ("output as currentness", ("command_output_only_posture", "command_output_treated_as_currentness"), True, "COMMAND_OUTPUT_TREATED_AS_CURRENTNESS"),
            ("output as final completion", ("command_output_only_posture", "command_output_treated_as_final_completion"), True, "COMMAND_OUTPUT_TREATED_AS_FINAL_COMPLETION"),
            ("boundary as output", ("command_output_only_posture", "boundary_treated_as_output"), True, "BOUNDARY_TREATED_AS_OUTPUT"),
            ("containment as output", ("command_output_only_posture", "containment_treated_as_output"), True, "CONTAINMENT_TREATED_AS_OUTPUT"),
            ("trace as output", ("execution_trace_audit_only_posture", "execution_trace_treated_as_output"), True, "EXECUTION_TRACE_TREATED_AS_OUTPUT"),
            ("trace as result", ("execution_trace_audit_only_posture", "execution_trace_treated_as_result"), True, "EXECUTION_TRACE_TREATED_AS_RESULT"),
            ("trace as success", ("execution_trace_audit_only_posture", "execution_trace_treated_as_success"), True, "EXECUTION_TRACE_TREATED_AS_SUCCESS"),
            ("trace as source", ("execution_trace_audit_only_posture", "execution_trace_treated_as_source"), True, "EXECUTION_TRACE_TREATED_AS_SOURCE"),
            ("trace as authority", ("execution_trace_audit_only_posture", "execution_trace_treated_as_authority"), True, "EXECUTION_TRACE_TREATED_AS_AUTHORITY"),
            ("result as authority", ("no_result_as_authority_posture", "command_result_became_authority"), True, "COMMAND_RESULT_TREATED_AS_AUTHORITY"),
            ("success as currentness", ("no_success_as_currentness_posture", "command_success_created_currentness"), True, "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
            ("success as final completion", ("no_final_completion_posture", "command_success_claimed_final_completion"), True, "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
        ]
        for name, path, value, code in cases:
            with self.subTest(name=name):
                request = _valid_request()
                _nested_set(request, path, value)
                self.assertBlocked(request, code)

    def test_blocking_cases_for_token_v1_lineage_artifacts_and_follow_on_overreach(self) -> None:
        cases: list[tuple[str, tuple[str, ...], Any, str]] = [
            ("consumed request reopened", ("selected_consumed_request_basis", "consumed_request_reopened"), True, "CONSUMED_REQUEST_REOPENED"),
            ("authorization reused", ("authorization_token_reuse_blocked_posture", "authorization_token_reused"), True, "AUTHORIZATION_TOKEN_REUSED"),
            ("v1 repaired", ("selected_v1_predecessor_failure_basis", "v1_repaired"), True, "V2_TREATED_AS_REPAIRING_V1"),
            ("v1 hidden", ("selected_v1_predecessor_failure_basis", "v1_hidden"), True, "V1_FAILURE_HIDDEN"),
            ("v1 claimed passed", ("selected_v1_predecessor_failure_basis", "v1_claimed_passed"), True, "V1_CLAIMED_PASSED"),
            ("older lineage current execution", ("selected_older_command_execution_boundary_lineage_basis", "older_command_execution_boundary_lineage_treated_as_current_execution"), True, "OLDER_COMMAND_EXECUTION_BOUNDARY_LINEAGE_TREATED_AS_CURRENT_EXECUTION"),
            ("artifacts mutated", ("selected_command_report_basis", "prior_artifacts_mutated"), True, "ARTIFACTS_MUTATED"),
            ("deployment created", ("selected_command_report_basis", "deployment_created"), True, "DEPLOYMENT_CREATED"),
            ("runtime created", ("selected_command_report_basis", "runtime_hosting_created"), True, "RUNTIME_HOSTING_CREATED"),
            ("public release created", ("selected_command_report_basis", "public_release_created"), True, "PUBLIC_RELEASE_CREATED"),
            ("operation created", ("selected_command_report_basis", "operation_permission_created"), True, "OPERATION_CREATED"),
            ("public readiness created", ("selected_command_report_basis", "public_launch_readiness_created"), True, "PUBLIC_READINESS_CREATED"),
            ("final completion claimed", ("selected_command_report_basis", "final_completion_claimed"), True, "FINAL_COMPLETION_CLAIMED"),
            ("continuation authorized", ("selected_command_report_basis", "continuation_authorized"), True, "CONTINUATION_AUTHORIZED"),
            ("reusable permission created", ("selected_command_report_basis", "reusable_permission_created"), True, "REUSABLE_PERMISSION_CREATED"),
            ("derivative reception authorized", ("selected_command_report_basis", "derivative_reception_authorized"), True, "DERIVATIVE_RECEPTION_AUTHORIZED"),
            ("vessel relation authorized", ("selected_command_report_basis", "vessel_relation_authorized"), True, "VESSEL_RELATION_AUTHORIZED"),
            ("another reception request authorized", ("selected_command_report_basis", "another_reception_request_authorized"), True, "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"),
            ("follow on work authorized", ("selected_command_report_basis", "follow_on_work_authorized"), True, "FOLLOW_ON_WORK_AUTHORIZED"),
            ("mutation replay merge", ("selected_command_report_basis", "merge_performed"), True, "MUTATION_REPLAY_OR_MERGE_DETECTED"),
        ]
        for name, path, value, code in cases:
            with self.subTest(name=name):
                request = _valid_request()
                _nested_set(request, path, value)
                self.assertBlocked(request, code)

    def test_missing_required_basis_and_posture_sections_block(self) -> None:
        basis_codes = {
            "selected_command_invocation_basis": "COMMAND_OUTPUT_BOUNDARY_BASIS_MISSING",
            "selected_command_execution_review_basis": "COMMAND_OUTPUT_BOUNDARY_BASIS_MISSING",
            "selected_request_consumption_basis": "COMMAND_OUTPUT_BOUNDARY_BASIS_MISSING",
            "selected_consumed_request_basis": "CONSUMED_REQUEST_REOPENED",
            "selected_v2_admitted_request_basis": "V2_ADMITTED_REQUEST_BASIS_MISSING",
            "selected_v1_predecessor_failure_basis": "V1_PREDECESSOR_FAILURE_BASIS_MISSING",
            "selected_older_command_execution_boundary_lineage_basis": "OLDER_COMMAND_EXECUTION_BOUNDARY_LINEAGE_TREATED_AS_CURRENT_EXECUTION",
            "selected_command_report_basis": "COMMAND_REPORT_BASIS_MISSING",
            "selected_command_implementation_boundary_basis": "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING",
            "selected_command_boundary_basis": "COMMAND_BOUNDARY_BASIS_MISSING",
            "selected_artifact_emission_containment_basis": "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING",
            "selected_evidence_manifest_basis": "EVIDENCE_MANIFEST_BASIS_MISSING",
            "selected_portable_verification_basis": "PORTABLE_VERIFICATION_BASIS_MISSING",
        }
        for key, code in basis_codes.items():
            with self.subTest(missing_basis=key):
                request = _valid_request()
                request.pop(key)
                self.assertBlocked(request, code)

        posture_codes = {
            "command_output_only_posture": "COMMAND_OUTPUT_ONLY_POSTURE_MISSING",
            "one_bounded_command_output_event_posture": "ONE_BOUNDED_COMMAND_OUTPUT_EVENT_POSTURE_MISSING",
            "command_output_boundary_basis_preserved_posture": "COMMAND_OUTPUT_BOUNDARY_BASIS_PRESERVED_POSTURE_MISSING",
            "command_output_containment_basis_preserved_posture": "COMMAND_OUTPUT_CONTAINMENT_BASIS_PRESERVED_POSTURE_MISSING",
            "bounded_output_containment_event_preserved_posture": "BOUNDED_OUTPUT_CONTAINMENT_EVENT_PRESERVED_POSTURE_MISSING",
            "execution_trace_audit_only_posture": "EXECUTION_TRACE_AUDIT_ONLY_POSTURE_MISSING",
            "no_output_capture_posture": "NO_OUTPUT_CAPTURE_POSTURE_MISSING",
            "no_output_report_artifact_posture": "NO_OUTPUT_REPORT_ARTIFACT_POSTURE_MISSING",
            "no_command_result_posture": "NO_COMMAND_RESULT_POSTURE_MISSING",
            "no_command_success_posture": "NO_COMMAND_SUCCESS_POSTURE_MISSING",
            "no_output_as_source_posture": "NO_OUTPUT_AS_SOURCE_POSTURE_MISSING",
            "no_result_as_authority_posture": "NO_RESULT_AS_AUTHORITY_POSTURE_MISSING",
            "no_success_as_currentness_posture": "NO_SUCCESS_AS_CURRENTNESS_POSTURE_MISSING",
            "no_final_completion_posture": "NO_FINAL_COMPLETION_POSTURE_MISSING",
        }
        for key, code in posture_codes.items():
            with self.subTest(missing_posture=key):
                request = _valid_request()
                request.pop(key)
                self.assertBlocked(request, code)

    def test_required_non_claim_missing_or_flipped_blocks(self) -> None:
        missing = _valid_request()
        missing["declared_non_claims"].pop("stdout_captured")
        self.assertBlocked(missing, "NON_CLAIM_MISSING_OR_FLIPPED")

        flipped = _valid_request()
        flipped["declared_non_claims"]["full_prior_artifacts_embedded"] = True
        self.assertBlocked(flipped, "NON_CLAIM_MISSING_OR_FLIPPED")

    def test_raw_prior_and_raw_output_body_values_are_not_returned(self) -> None:
        raw_prior = _valid_request()
        raw_prior["selected_command_report_basis"]["full_prior_artifact_body"] = RAW_PRIOR_SENTINEL
        prior_result = self.assertBlocked(raw_prior, "FULL_PRIOR_ARTIFACT_BODY_EMITTED")
        self.assertNotIn(RAW_PRIOR_SENTINEL, _json_text(prior_result))
        self.assertIn("raw_full_prior_artifact_body_not_returned", _json_text(prior_result))

        raw_output = _valid_request()
        raw_output["command_output_event"]["stdout"] = RAW_OUTPUT_SENTINEL
        output_result = self.assertBlocked(raw_output, "RAW_OUTPUT_BODY_CAPTURED")
        self.assertNotIn(RAW_OUTPUT_SENTINEL, _json_text(output_result))
        self.assertIn("raw output field present", _json_text(output_result))

    def test_summary_helper_preserves_command_output_non_claims(self) -> None:
        result = _resolve(_valid_request())
        summary = build_portable_source_body_verification_command_output_summary(result)
        self.assertEqual(RECORDED, summary["outcome"])
        self.assertTrue(summary["command_output_recorded"])
        self.assertTrue(summary["bounded_command_output_event_recorded"])
        self.assertTrue(summary["stdout_not_captured"])
        self.assertTrue(summary["stderr_not_captured"])
        self.assertTrue(summary["process_output_not_captured"])
        self.assertTrue(summary["raw_output_body_not_captured"])
        self.assertTrue(
            summary[
                "command_output_not_capture_report_result_success_source_authority_currentness_final_completion"
            ]
        )
        self.assertTrue(summary["boundary_not_output"])
        self.assertTrue(summary["containment_not_output"])
        self.assertTrue(summary["execution_trace_not_output_result_success_source_authority"])
        self.assertTrue(summary["no_deployment_runtime_public_release"])
        self.assertTrue(summary["no_continuation_publication_reusable_follow_on"])
        for key, value in summary["key_non_claims"].items():
            self.assertFalse(value, key)

    def test_resolver_does_not_mutate_request_selected_basis_event_posture_or_scope(self) -> None:
        request = _valid_request()
        before = copy.deepcopy(request)
        selected_before = {key: copy.deepcopy(request[key]) for key in SELECTED_BASIS_KEYS}
        event_before = copy.deepcopy(request["command_output_event"])
        posture_before = {key: copy.deepcopy(request[key]) for key in POSTURE_KEYS}
        scope_before = copy.deepcopy(request["command_output_scope"])

        result = _resolve(request)

        self.assertEqual(RECORDED, result["outcome"])
        self.assertEqual(before, request)
        for key, value in selected_before.items():
            self.assertEqual(value, request[key], key)
        self.assertEqual(event_before, request["command_output_event"])
        for key, value in posture_before.items():
            self.assertEqual(value, request[key], key)
        self.assertEqual(scope_before, request["command_output_scope"])


if __name__ == "__main__":
    unittest.main()
