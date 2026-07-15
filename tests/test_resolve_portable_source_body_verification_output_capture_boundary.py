"""Tests for portable source-body verification output capture boundary.

This suite is bounded to output capture boundary only. It is downstream of
recorded command output and proves that one future output-capture boundary can
be recorded without capturing stdout, stderr, process output, raw output body,
creating output capture, creating an output/report artifact, creating command
result, creating command success, mutating artifacts, deploying, publishing,
continuing, or authorizing follow-on work.
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

import resolve_portable_source_body_verification_output_capture_boundary as resolver
from resolve_portable_source_body_verification_output_capture_boundary import (
    build_declared_portable_source_body_verification_output_capture_boundary_request,
    build_portable_source_body_verification_output_capture_boundary_summary,
    resolve_portable_source_body_verification_output_capture_boundary,
    resolve_portable_source_body_verification_output_capture_boundary_from_path,
    write_portable_source_body_verification_output_capture_boundary_result,
)


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}

QUESTION = resolver.CORE_QUESTION
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_OUTPUT_CAPTURE_BOUNDARY_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
RAW_OUTPUT_SENTINEL = "RAW_STDOUT_OR_OUTPUT_BODY_MUST_NOT_RETURN_" * 6
RAW_PRIOR_SENTINEL = "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN_" * 6

TOP_LEVEL_SECTIONS = tuple(resolver.TOP_LEVEL_SECTIONS)

SELECTED_BASIS_KEYS = (
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
)

POSTURE_KEYS = (
    "output_capture_boundary_only_posture",
    "one_future_output_capture_step_posture",
    "command_output_basis_preserved_posture",
    "bounded_command_output_event_preserved_posture",
    "command_output_boundary_basis_preserved_posture",
    "execution_trace_audit_only_posture",
    "no_stdout_capture_posture",
    "no_stderr_capture_posture",
    "no_process_output_capture_posture",
    "no_raw_output_body_capture_posture",
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

FORBIDDEN_RAW_VALUE_KEYS = {
    "stdout",
    "stderr",
    "process_output",
    "raw_output_body",
    "raw_command_output_body",
    "command_output_body",
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


def _reference_basis(name: str, **overrides: Any) -> dict[str, Any]:
    basis: dict[str, Any] = {
        "basis_id": name,
        "declared": True,
        "basis_declared": True,
        "path": f"synthetic://{name}.json",
        "result_path": f"synthetic://{name}.json",
        "reference_shaped": True,
        "reference_shaped_basis": True,
        "basis_remains_reference_shaped": True,
        "basis_remains_basis_only": True,
        "selected_basis_is_reference_shaped": True,
        "full_upstream_lineage_preserved": True,
        "full_prior_artifact_body_not_emitted": True,
        "full_prior_artifacts_embedded": False,
        "raw_full_prior_artifact_body_returned": False,
        "prior_artifacts_mutated": False,
        "not_stdout_capture": True,
        "not_stderr_capture": True,
        "not_process_output_capture": True,
        "not_raw_output_body_capture": True,
        "not_output_capture": True,
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
        terminal_summary_does_not_capture_stdout=True,
        terminal_summary_does_not_capture_stderr=True,
        terminal_summary_does_not_capture_process_output=True,
        terminal_summary_does_not_capture_raw_output_body=True,
        terminal_summary_does_not_create_output_capture=True,
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
        "stdout_captured": False,
        "stderr_captured": False,
        "process_output_captured": False,
        "raw_output_body_captured": False,
        "stdout_not_captured": True,
        "stderr_not_captured": True,
        "process_output_not_captured": True,
        "raw_output_body_not_captured": True,
        "output_capture_created": False,
        "output_capture_not_created": True,
        "output_report_artifact_created": False,
        "command_output_report_artifact_created": False,
        "command_output_report_artifact_not_created": True,
        "command_result_created": False,
        "command_result_still_not_created": True,
        "command_success_created": False,
        "command_success_still_not_created": True,
        "output_capture_boundary_treated_as_stdout_capture": False,
        "output_capture_boundary_treated_as_stderr_capture": False,
        "output_capture_boundary_treated_as_process_output_capture": False,
        "output_capture_boundary_treated_as_raw_output_body_capture": False,
        "output_capture_boundary_treated_as_output_capture": False,
        "output_capture_boundary_treated_as_output_report_artifact": False,
        "output_capture_boundary_treated_as_result": False,
        "output_capture_boundary_treated_as_success": False,
        "command_output_treated_as_output_capture": False,
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


def _valid_request(**overrides: Any) -> dict[str, Any]:
    request = build_declared_portable_source_body_verification_output_capture_boundary_request(
        output_capture_boundary_request_id="output-capture-boundary-request-001",
        output_capture_boundary_question=QUESTION,
        output_capture_boundary_intent=resolver.INTENT_RECORD,
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
        command_result_not_created=True,
        command_result_still_not_created=True,
        command_success_not_created=True,
        command_success_still_not_created=True,
        command_output_is_not_output_capture=True,
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
        command_output_created=False,
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
    request["output_capture_boundary_scope"] = list(SUPPORTED_SCOPE)
    request["declared_non_claims"] = _false_non_claims()
    request["requested_output_capture_boundary_outcome"] = RECORDED
    request["reference_shaped_input_posture"] = {
        "declared": True,
        "posture_declared": True,
        "reference_shaped_input_posture": True,
        "full_prior_artifact_body_not_emitted": True,
    }
    request.update(overrides)
    return request


def _mutated_request(mutator: Callable[[dict[str, Any]], None]) -> dict[str, Any]:
    request = _valid_request()
    mutator(request)
    return request


def _block_codes(result: dict[str, Any]) -> set[str]:
    codes = {
        check.get("block_code")
        for check in result.get("output_capture_boundary_checks", [])
        if not check.get("passed")
    }
    block = result.get("block", {})
    codes.add(block.get("block_code"))
    return {str(code) for code in codes if code}


def _without_raw_values(value: Any) -> bool:
    if isinstance(value, dict):
        for key, nested in value.items():
            if key in FORBIDDEN_RAW_VALUE_KEYS and nested not in ({}, [], None, False):
                if not (isinstance(nested, dict) and nested.get("omitted") is True):
                    return False
            if not _without_raw_values(nested):
                return False
    if isinstance(value, list):
        return all(_without_raw_values(item) for item in value)
    return True


class OutputCaptureBoundaryResolverTests(unittest.TestCase):
    def assertBlockedWithCode(self, request: Any, expected_code: str) -> dict[str, Any]:
        result = resolve_portable_source_body_verification_output_capture_boundary(
            declared_output_capture_boundary_request=request
        )
        self.assertEqual(BLOCKED, result["outcome"])
        self.assertTrue(result["block"]["blocked"])
        self.assertIn(expected_code, _block_codes(result))
        statement = result["output_capture_boundary_statement"]
        for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertFalse(statement[key], key)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(statement[key], False, key)
            self.assertIs(result["non_claims"][key], False, key)
        return result

    def test_recorded_result_preserves_output_capture_boundary_only_shape(self) -> None:
        request = _valid_request()
        result = resolve_portable_source_body_verification_output_capture_boundary(
            declared_output_capture_boundary_request=request
        )

        self.assertIsInstance(result, dict)
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        self.assertEqual(RECORDED, result["outcome"])
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(0, result["portable_source_body_verification_output_capture_boundary_summary"]["failed_check_count"])

        metadata = result["portable_source_body_verification_output_capture_boundary_metadata"]
        self.assertEqual("0.1.0", metadata["portable_source_body_verification_output_capture_boundary_result_version"])
        self.assertEqual("resolve_portable_source_body_verification_output_capture_boundary", metadata["resolver_module"])
        self.assertEqual(
            "resolve_portable_source_body_verification_output_capture_boundary.py",
            metadata["short_resolver_filename"],
        )
        self.assertTrue(metadata["full_upstream_lineage_preserved_inside_selected_basis"])
        self.assertTrue(
            result["selected_command_output_basis"]["basis"]["full_upstream_lineage_preserved"]
        )

        statement = result["output_capture_boundary_statement"]
        expected_true = (
            "output_capture_boundary_recorded",
            "one_future_output_capture_step_declared",
            "command_output_basis_preserved",
            "bounded_command_output_event_preserved",
            "command_output_boundary_basis_preserved",
            "command_output_containment_basis_preserved",
            "recorded_command_execution_event_preserved",
            "execution_trace_audit_only_preserved",
            "stdout_still_not_captured",
            "stderr_still_not_captured",
            "process_output_still_not_captured",
            "raw_output_body_still_not_captured",
            "output_capture_not_created",
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
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(statement[key], False, key)
            self.assertIs(result["non_claims"][key], False, key)

        command_output = result["selected_command_output_basis"]
        self.assertEqual(resolver.COMMAND_OUTPUT_OUTCOME, command_output["outcome"])
        self.assertEqual(0, command_output["failed_check_count"])
        self.assertTrue(command_output["bounded_command_output_event_recorded"])
        self.assertFalse(command_output["stdout_captured"])
        self.assertFalse(command_output["stderr_captured"])
        self.assertFalse(command_output["process_output_captured"])
        self.assertFalse(command_output["raw_output_body_captured"])
        self.assertFalse(command_output["output_capture_created"])
        self.assertFalse(command_output["command_output_report_artifact_created"])
        self.assertFalse(command_output["command_result_created"])
        self.assertFalse(command_output["command_success_created"])
        self.assertTrue(_without_raw_values(command_output))

        self.assertTrue(result["selected_command_output_terminal_summary_basis"]["declared"])
        self.assertTrue(result["selected_command_output_terminal_summary_basis"]["readability_basis_only"])
        self.assertEqual(
            resolver.POST_INVOCATION_COMMAND_EXECUTION_OUTCOME,
            result["selected_post_invocation_command_execution_basis"]["outcome"],
        )
        self.assertEqual(
            0,
            result["selected_post_invocation_command_execution_basis"]["failed_check_count"],
        )
        self.assertTrue(
            result["selected_post_invocation_command_execution_basis"][
                "bounded_command_execution_event_recorded"
            ]
        )
        self.assertTrue(
            result["selected_post_invocation_command_execution_basis"][
                "execution_trace_audit_only"
            ]
        )
        self.assertEqual(
            resolver.V2_ADMITTED_REQUEST_OUTCOME,
            result["selected_v2_admitted_request_basis"]["outcome"],
        )
        self.assertEqual(
            resolver.V2_ADMITTED_REQUEST_VERSION,
            result["selected_v2_admitted_request_basis"]["version"],
        )
        self.assertTrue(
            result["selected_older_command_execution_boundary_lineage_basis"][
                "lineage_basis_not_treated_as_current_execution"
            ]
        )
        self.assertIn("output capture", result["what_remains_open"]["open_items"])
        self.assertIn("command result", result["what_remains_open"]["open_items"])

    def test_path_and_write_behaviour_are_bounded(self) -> None:
        request = _valid_request()
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request_path = tmp_path / "request.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")

            from_path = resolve_portable_source_body_verification_output_capture_boundary_from_path(
                request_path
            )
            self.assertEqual(RECORDED, from_path["outcome"])

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            malformed = resolve_portable_source_body_verification_output_capture_boundary_from_path(
                malformed_path
            )
            self.assertEqual(BLOCKED, malformed["outcome"])
            self.assertEqual(
                "DECLARED_OUTPUT_CAPTURE_BOUNDARY_REQUEST_UNREADABLE",
                malformed["block"]["block_code"],
            )

            array_path = tmp_path / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolve_portable_source_body_verification_output_capture_boundary_from_path(
                array_path
            )
            self.assertEqual(BLOCKED, array_result["outcome"])
            self.assertEqual(
                "DECLARED_OUTPUT_CAPTURE_BOUNDARY_REQUEST_MALFORMED",
                array_result["block"]["block_code"],
            )

            missing = resolve_portable_source_body_verification_output_capture_boundary_from_path(
                tmp_path / "missing.json"
            )
            self.assertEqual(BLOCKED, missing["outcome"])
            self.assertEqual(
                "DECLARED_OUTPUT_CAPTURE_BOUNDARY_REQUEST_UNREADABLE",
                missing["block"]["block_code"],
            )

            result = resolve_portable_source_body_verification_output_capture_boundary(
                declared_output_capture_boundary_request=request
            )
            output_root = tmp_path / "nested" / "results"
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                first = write_portable_source_body_verification_output_capture_boundary_result(result)
                second = write_portable_source_body_verification_output_capture_boundary_result(result)
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertEqual(RECORDED, json.loads(first.read_text(encoding="utf-8"))["outcome"])
            self.assertEqual(RECORDED, json.loads(second.read_text(encoding="utf-8"))["outcome"])
            self.assertTrue(second.stem.endswith("_001"))

    def test_outcome_family_not_recorded_requires_additional_basis_and_blocked(self) -> None:
        self.assertEqual(OUTCOME_FAMILY, set(resolver.OUTCOME_FAMILY))

        not_recorded_request = _valid_request(
            output_capture_boundary_intent=resolver.INTENT_DO_NOT_RECORD,
            requested_output_capture_boundary_outcome=NOT_RECORDED,
            not_recorded_basis={"review": "readable boundary basis not recorded"},
        )
        not_recorded = resolve_portable_source_body_verification_output_capture_boundary(
            declared_output_capture_boundary_request=not_recorded_request
        )
        self.assertEqual(NOT_RECORDED, not_recorded["outcome"])
        self.assertFalse(not_recorded["block"]["blocked"])
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded"])
        self.assertFalse(
            not_recorded["output_capture_boundary_statement"]["output_capture_boundary_recorded"]
        )

        requires_request = _valid_request(
            requested_output_capture_boundary_outcome=REQUIRES_ADDITIONAL_BASIS,
            additional_basis_context={"missing": "command report basis clarity"},
        )
        requires_request.pop("selected_command_report_basis")
        requires = resolve_portable_source_body_verification_output_capture_boundary(
            declared_output_capture_boundary_request=requires_request
        )
        self.assertEqual(REQUIRES_ADDITIONAL_BASIS, requires["outcome"])
        self.assertFalse(requires["block"]["blocked"])
        self.assertTrue(requires["additional_basis_required"]["required"])
        self.assertTrue(requires["additional_basis_required"]["missing_basis_not_authorized"])

        explicit_block = self.assertBlockedWithCode(
            _valid_request(
                output_capture_boundary_intent=resolver.INTENT_BLOCK,
                block_reason="declared bounded block",
            ),
            "OUTPUT_CAPTURE_BOUNDARY_BLOCKED_BY_REQUEST",
        )
        self.assertEqual("declared bounded block", explicit_block["block"]["block_reason"])

    def test_blocking_cases_for_command_output_basis_execution_and_scope(self) -> None:
        self.assertBlockedWithCode(None, "OUTPUT_CAPTURE_BOUNDARY_QUESTION_UNDECLARED")
        self.assertBlockedWithCode(["not", "mapping"], "DECLARED_OUTPUT_CAPTURE_BOUNDARY_REQUEST_MALFORMED")

        cases: list[tuple[str, str, Callable[[dict[str, Any]], None]]] = [
            (
                "unsupported intent",
                "OUTPUT_CAPTURE_BOUNDARY_INTENT_UNSUPPORTED",
                lambda request: request.__setitem__("output_capture_boundary_intent", "UNSUPPORTED"),
            ),
            (
                "unsupported scope",
                "UNSUPPORTED_OUTPUT_CAPTURE_BOUNDARY_SCOPE",
                lambda request: request.__setitem__("output_capture_boundary_scope", ["OUTPUT_CAPTURE"]),
            ),
            (
                "missing command output terminal summary",
                "COMMAND_OUTPUT_BASIS_MISSING",
                lambda request: request.pop("selected_command_output_terminal_summary_basis"),
            ),
            (
                "missing command output basis",
                "COMMAND_OUTPUT_BASIS_MISSING",
                lambda request: request.pop("selected_command_output_basis"),
            ),
            (
                "command output not recorded",
                "COMMAND_OUTPUT_NOT_RECORDED",
                lambda request: request["selected_command_output_basis"].__setitem__(
                    "outcome", "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_NOT_RECORDED"
                ),
            ),
            (
                "command output failed checks",
                "COMMAND_OUTPUT_FAILED_CHECKS_PRESENT",
                lambda request: request["selected_command_output_basis"].__setitem__(
                    "failed_check_count", 1
                ),
            ),
            (
                "command output event not recorded",
                "COMMAND_OUTPUT_EVENT_NOT_RECORDED",
                lambda request: request["selected_command_output_basis"].update(
                    {
                        "command_output_recorded": False,
                        "command_output_event_recorded": False,
                        "bounded_command_output_event_recorded": False,
                    }
                ),
            ),
            (
                "command output already captured stdout",
                "COMMAND_OUTPUT_ALREADY_CAPTURED_STDOUT",
                lambda request: request["selected_command_output_basis"].__setitem__(
                    "stdout_captured", True
                ),
            ),
            (
                "command output already captured stderr",
                "COMMAND_OUTPUT_ALREADY_CAPTURED_STDERR",
                lambda request: request["selected_command_output_basis"].__setitem__(
                    "stderr_captured", True
                ),
            ),
            (
                "command output already captured process output",
                "COMMAND_OUTPUT_ALREADY_CAPTURED_PROCESS_OUTPUT",
                lambda request: request["selected_command_output_basis"].__setitem__(
                    "process_output_captured", True
                ),
            ),
            (
                "command output already captured raw output body",
                "COMMAND_OUTPUT_ALREADY_CAPTURED_RAW_OUTPUT_BODY",
                lambda request: request["selected_command_output_basis"].__setitem__(
                    "raw_output_body_captured", True
                ),
            ),
            (
                "command output already created output capture",
                "COMMAND_OUTPUT_ALREADY_CREATED_OUTPUT_CAPTURE",
                lambda request: request["selected_command_output_basis"].__setitem__(
                    "output_capture_created", True
                ),
            ),
            (
                "command output already created output report artifact",
                "COMMAND_OUTPUT_ALREADY_CREATED_OUTPUT_REPORT_ARTIFACT",
                lambda request: request["selected_command_output_basis"].__setitem__(
                    "command_output_report_artifact_created", True
                ),
            ),
            (
                "command output already created command result",
                "COMMAND_OUTPUT_ALREADY_CREATED_RESULT",
                lambda request: request["selected_command_output_basis"].__setitem__(
                    "command_result_created", True
                ),
            ),
            (
                "command output already created command success",
                "COMMAND_OUTPUT_ALREADY_CREATED_SUCCESS",
                lambda request: request["selected_command_output_basis"].__setitem__(
                    "command_success_created", True
                ),
            ),
            (
                "missing command output boundary",
                "COMMAND_OUTPUT_BOUNDARY_BASIS_MISSING",
                lambda request: request.pop("selected_command_output_boundary_basis"),
            ),
            (
                "missing command output containment",
                "COMMAND_OUTPUT_CONTAINMENT_BASIS_MISSING",
                lambda request: request.pop("selected_command_output_containment_basis"),
            ),
            (
                "missing post invocation execution",
                "POST_INVOCATION_COMMAND_EXECUTION_BASIS_MISSING",
                lambda request: request.pop("selected_post_invocation_command_execution_basis"),
            ),
            (
                "post invocation execution not recorded",
                "POST_INVOCATION_COMMAND_EXECUTION_NOT_RECORDED",
                lambda request: request["selected_post_invocation_command_execution_basis"].__setitem__(
                    "outcome", "POST_INVOCATION_COMMAND_EXECUTION_NOT_RECORDED"
                ),
            ),
            (
                "post invocation failed checks",
                "POST_INVOCATION_COMMAND_EXECUTION_FAILED_CHECKS_PRESENT",
                lambda request: request["selected_post_invocation_command_execution_basis"].__setitem__(
                    "failed_check_count", 1
                ),
            ),
            (
                "post invocation trace not audit-only",
                "POST_INVOCATION_COMMAND_EXECUTION_TRACE_NOT_AUDIT_ONLY",
                lambda request: request["selected_post_invocation_command_execution_basis"].update(
                    {
                        "execution_trace_audit_only": False,
                        "execution_trace_audit_only_preserved": False,
                    }
                ),
            ),
        ]
        for label, expected, mutator in cases:
            with self.subTest(label=label):
                self.assertBlockedWithCode(_mutated_request(mutator), expected)

    def test_blocking_cases_for_boundary_command_output_and_trace_collapse(self) -> None:
        cases: list[tuple[str, str, str, str]] = [
            (
                "boundary as stdout capture",
                "output_capture_boundary_only_posture",
                "output_capture_boundary_treated_as_stdout_capture",
                "OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_STDOUT_CAPTURE",
            ),
            (
                "boundary as stderr capture",
                "output_capture_boundary_only_posture",
                "output_capture_boundary_treated_as_stderr_capture",
                "OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_STDERR_CAPTURE",
            ),
            (
                "boundary as process output capture",
                "output_capture_boundary_only_posture",
                "output_capture_boundary_treated_as_process_output_capture",
                "OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_PROCESS_OUTPUT_CAPTURE",
            ),
            (
                "boundary as raw output body capture",
                "output_capture_boundary_only_posture",
                "output_capture_boundary_treated_as_raw_output_body_capture",
                "OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_RAW_OUTPUT_BODY_CAPTURE",
            ),
            (
                "boundary as output capture",
                "output_capture_boundary_only_posture",
                "output_capture_boundary_treated_as_output_capture",
                "OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_OUTPUT_CAPTURE",
            ),
            (
                "boundary as output report artifact",
                "output_capture_boundary_only_posture",
                "output_capture_boundary_treated_as_output_report_artifact",
                "OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_OUTPUT_REPORT_ARTIFACT",
            ),
            (
                "boundary as result",
                "output_capture_boundary_only_posture",
                "output_capture_boundary_treated_as_result",
                "OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_RESULT",
            ),
            (
                "boundary as success",
                "output_capture_boundary_only_posture",
                "output_capture_boundary_treated_as_success",
                "OUTPUT_CAPTURE_BOUNDARY_TREATED_AS_SUCCESS",
            ),
            (
                "command output as capture",
                "command_output_basis_preserved_posture",
                "command_output_treated_as_output_capture",
                "COMMAND_OUTPUT_TREATED_AS_OUTPUT_CAPTURE",
            ),
            (
                "command output as output report",
                "command_output_basis_preserved_posture",
                "command_output_treated_as_output_report_artifact",
                "COMMAND_OUTPUT_TREATED_AS_OUTPUT_REPORT_ARTIFACT",
            ),
            (
                "command output as result",
                "command_output_basis_preserved_posture",
                "command_output_treated_as_result",
                "COMMAND_OUTPUT_TREATED_AS_RESULT",
            ),
            (
                "command output as success",
                "command_output_basis_preserved_posture",
                "command_output_treated_as_success",
                "COMMAND_OUTPUT_TREATED_AS_SUCCESS",
            ),
            (
                "command output as source",
                "command_output_basis_preserved_posture",
                "command_output_treated_as_source",
                "COMMAND_OUTPUT_TREATED_AS_SOURCE",
            ),
            (
                "command output as authority",
                "command_output_basis_preserved_posture",
                "command_output_treated_as_authority",
                "COMMAND_OUTPUT_TREATED_AS_AUTHORITY",
            ),
            (
                "command output as currentness",
                "command_output_basis_preserved_posture",
                "command_output_treated_as_currentness",
                "COMMAND_OUTPUT_TREATED_AS_CURRENTNESS",
            ),
            (
                "command output as final completion",
                "command_output_basis_preserved_posture",
                "command_output_treated_as_final_completion",
                "COMMAND_OUTPUT_TREATED_AS_FINAL_COMPLETION",
            ),
            (
                "trace as output capture",
                "execution_trace_audit_only_posture",
                "execution_trace_treated_as_output_capture",
                "EXECUTION_TRACE_TREATED_AS_OUTPUT_CAPTURE",
            ),
            (
                "trace as result",
                "execution_trace_audit_only_posture",
                "execution_trace_treated_as_result",
                "EXECUTION_TRACE_TREATED_AS_RESULT",
            ),
            (
                "trace as success",
                "execution_trace_audit_only_posture",
                "execution_trace_treated_as_success",
                "EXECUTION_TRACE_TREATED_AS_SUCCESS",
            ),
            (
                "trace as source",
                "execution_trace_audit_only_posture",
                "execution_trace_treated_as_source",
                "EXECUTION_TRACE_TREATED_AS_SOURCE",
            ),
            (
                "trace as authority",
                "execution_trace_audit_only_posture",
                "execution_trace_treated_as_authority",
                "EXECUTION_TRACE_TREATED_AS_AUTHORITY",
            ),
            (
                "result as authority",
                "no_result_as_authority_posture",
                "command_result_became_authority",
                "COMMAND_RESULT_TREATED_AS_AUTHORITY",
            ),
            (
                "success as currentness",
                "no_success_as_currentness_posture",
                "command_success_created_currentness",
                "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS",
            ),
            (
                "success as final completion",
                "no_final_completion_posture",
                "command_success_claimed_final_completion",
                "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION",
            ),
        ]
        for label, section, key, expected in cases:
            with self.subTest(label=label):
                self.assertBlockedWithCode(
                    _mutated_request(lambda request, section=section, key=key: request[section].__setitem__(key, True)),
                    expected,
                )

        capture_cases = [
            ("stdout captured", "no_stdout_capture_posture", "stdout_captured", "STDOUT_CAPTURED"),
            ("stderr captured", "no_stderr_capture_posture", "stderr_captured", "STDERR_CAPTURED"),
            (
                "process output captured",
                "no_process_output_capture_posture",
                "process_output_captured",
                "PROCESS_OUTPUT_CAPTURED",
            ),
            (
                "raw output body captured",
                "no_raw_output_body_capture_posture",
                "raw_output_body_captured",
                "RAW_OUTPUT_BODY_CAPTURED",
            ),
            (
                "output capture created",
                "no_output_capture_posture",
                "output_capture_created",
                "OUTPUT_CAPTURE_CREATED",
            ),
            (
                "output report artifact created",
                "no_output_report_artifact_posture",
                "command_output_report_artifact_created",
                "COMMAND_OUTPUT_REPORT_ARTIFACT_CREATED",
            ),
            (
                "command result created",
                "no_command_result_posture",
                "command_result_created",
                "COMMAND_RESULT_CREATED",
            ),
            (
                "command success created",
                "no_command_success_posture",
                "command_success_created",
                "COMMAND_SUCCESS_CREATED",
            ),
        ]
        for label, section, key, expected in capture_cases:
            with self.subTest(label=label):
                self.assertBlockedWithCode(
                    _mutated_request(lambda request, section=section, key=key: request[section].__setitem__(key, True)),
                    expected,
                )

    def test_blocking_cases_for_token_v1_lineage_artifacts_and_follow_on_overreach(self) -> None:
        cases: list[tuple[str, str, Callable[[dict[str, Any]], None]]] = [
            (
                "consumed request reopened",
                "CONSUMED_REQUEST_REOPENED",
                lambda request: request["selected_consumed_request_basis"].__setitem__(
                    "consumed_request_reopened", True
                ),
            ),
            (
                "authorization token reused",
                "AUTHORIZATION_TOKEN_REUSED",
                lambda request: request["selected_command_invocation_basis"].__setitem__(
                    "authorization_token_reused", True
                ),
            ),
            (
                "v1 repaired",
                "V2_TREATED_AS_REPAIRING_V1",
                lambda request: request["selected_v1_predecessor_failure_basis"].__setitem__(
                    "v1_repaired", True
                ),
            ),
            (
                "v1 hidden",
                "V1_FAILURE_HIDDEN",
                lambda request: request["selected_v1_predecessor_failure_basis"].__setitem__(
                    "v1_hidden", True
                ),
            ),
            (
                "v1 claimed passed",
                "V1_CLAIMED_PASSED",
                lambda request: request["selected_v1_predecessor_failure_basis"].__setitem__(
                    "v1_claimed_passed", True
                ),
            ),
            (
                "older lineage as current execution",
                "OLDER_COMMAND_EXECUTION_BOUNDARY_LINEAGE_TREATED_AS_CURRENT_EXECUTION",
                lambda request: request["selected_older_command_execution_boundary_lineage_basis"].__setitem__(
                    "older_command_execution_boundary_lineage_treated_as_current_execution",
                    True,
                ),
            ),
            (
                "artifacts mutated",
                "ARTIFACTS_MUTATED",
                lambda request: request["selected_command_report_basis"].__setitem__(
                    "prior_artifacts_mutated", True
                ),
            ),
            (
                "deployment created",
                "DEPLOYMENT_CREATED",
                lambda request: request["selected_command_report_basis"].__setitem__(
                    "deployment_created", True
                ),
            ),
            (
                "runtime created",
                "RUNTIME_HOSTING_CREATED",
                lambda request: request["selected_command_report_basis"].__setitem__(
                    "runtime_hosting_created", True
                ),
            ),
            (
                "public release created",
                "PUBLIC_RELEASE_CREATED",
                lambda request: request["selected_command_report_basis"].__setitem__(
                    "public_release_created", True
                ),
            ),
            (
                "operation created",
                "OPERATION_CREATED",
                lambda request: request["selected_command_report_basis"].__setitem__(
                    "operation_permission_created", True
                ),
            ),
            (
                "public readiness created",
                "PUBLIC_READINESS_CREATED",
                lambda request: request["selected_command_report_basis"].__setitem__(
                    "public_launch_readiness_created", True
                ),
            ),
            (
                "final completion claimed",
                "FINAL_COMPLETION_CLAIMED",
                lambda request: request["selected_command_report_basis"].__setitem__(
                    "final_completion_claimed", True
                ),
            ),
            (
                "continuation authorized",
                "CONTINUATION_AUTHORIZED",
                lambda request: request["selected_command_report_basis"].__setitem__(
                    "continuation_authorized", True
                ),
            ),
            (
                "reusable permission",
                "REUSABLE_PERMISSION_CREATED",
                lambda request: request["selected_command_report_basis"].__setitem__(
                    "reusable_permission_created", True
                ),
            ),
            (
                "derivative reception",
                "DERIVATIVE_RECEPTION_AUTHORIZED",
                lambda request: request["selected_command_report_basis"].__setitem__(
                    "derivative_reception_authorized", True
                ),
            ),
            (
                "vessel relation",
                "VESSEL_RELATION_AUTHORIZED",
                lambda request: request["selected_command_report_basis"].__setitem__(
                    "vessel_relation_authorized", True
                ),
            ),
            (
                "another reception request",
                "ANOTHER_RECEPTION_REQUEST_AUTHORIZED",
                lambda request: request["selected_command_report_basis"].__setitem__(
                    "another_reception_request_authorized", True
                ),
            ),
            (
                "follow-on work",
                "FOLLOW_ON_WORK_AUTHORIZED",
                lambda request: request["selected_command_report_basis"].__setitem__(
                    "follow_on_work_authorized", True
                ),
            ),
            (
                "merge performed",
                "MUTATION_REPLAY_OR_MERGE_DETECTED",
                lambda request: request["selected_command_report_basis"].__setitem__(
                    "merge_performed", True
                ),
            ),
        ]
        for label, expected, mutator in cases:
            with self.subTest(label=label):
                self.assertBlockedWithCode(_mutated_request(mutator), expected)

    def test_missing_required_basis_and_posture_sections_block(self) -> None:
        basis_cases = [
            ("selected_command_invocation_basis", "COMMAND_OUTPUT_BASIS_MISSING"),
            ("selected_command_execution_review_basis", "COMMAND_OUTPUT_BASIS_MISSING"),
            ("selected_request_consumption_basis", "COMMAND_OUTPUT_BASIS_MISSING"),
            ("selected_consumed_request_basis", "CONSUMED_REQUEST_REOPENED"),
            ("selected_v2_admitted_request_basis", "V2_ADMITTED_REQUEST_BASIS_MISSING"),
            ("selected_v1_predecessor_failure_basis", "V1_PREDECESSOR_FAILURE_BASIS_MISSING"),
            (
                "selected_older_command_execution_boundary_lineage_basis",
                "OLDER_COMMAND_EXECUTION_BOUNDARY_LINEAGE_TREATED_AS_CURRENT_EXECUTION",
            ),
            ("selected_command_report_basis", "COMMAND_REPORT_BASIS_MISSING"),
            (
                "selected_command_implementation_boundary_basis",
                "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING",
            ),
            ("selected_command_boundary_basis", "COMMAND_BOUNDARY_BASIS_MISSING"),
            (
                "selected_artifact_emission_containment_basis",
                "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING",
            ),
            ("selected_evidence_manifest_basis", "EVIDENCE_MANIFEST_BASIS_MISSING"),
            ("selected_portable_verification_basis", "PORTABLE_VERIFICATION_BASIS_MISSING"),
        ]
        for key, expected in basis_cases:
            with self.subTest(key=key):
                self.assertBlockedWithCode(_mutated_request(lambda request, key=key: request.pop(key)), expected)

        posture_cases = [
            ("output_capture_boundary_only_posture", "OUTPUT_CAPTURE_BOUNDARY_ONLY_POSTURE_MISSING"),
            (
                "one_future_output_capture_step_posture",
                "ONE_FUTURE_OUTPUT_CAPTURE_STEP_POSTURE_MISSING",
            ),
            (
                "command_output_basis_preserved_posture",
                "COMMAND_OUTPUT_BASIS_PRESERVED_POSTURE_MISSING",
            ),
            (
                "bounded_command_output_event_preserved_posture",
                "BOUNDED_COMMAND_OUTPUT_EVENT_PRESERVED_POSTURE_MISSING",
            ),
            (
                "command_output_boundary_basis_preserved_posture",
                "COMMAND_OUTPUT_BOUNDARY_BASIS_PRESERVED_POSTURE_MISSING",
            ),
            ("execution_trace_audit_only_posture", "EXECUTION_TRACE_AUDIT_ONLY_POSTURE_MISSING"),
            ("no_stdout_capture_posture", "NO_STDOUT_CAPTURE_POSTURE_MISSING"),
            ("no_stderr_capture_posture", "NO_STDERR_CAPTURE_POSTURE_MISSING"),
            ("no_process_output_capture_posture", "NO_PROCESS_OUTPUT_CAPTURE_POSTURE_MISSING"),
            ("no_raw_output_body_capture_posture", "NO_RAW_OUTPUT_BODY_CAPTURE_POSTURE_MISSING"),
            ("no_output_capture_posture", "NO_OUTPUT_CAPTURE_POSTURE_MISSING"),
            ("no_output_report_artifact_posture", "NO_OUTPUT_REPORT_ARTIFACT_POSTURE_MISSING"),
            ("no_command_result_posture", "NO_COMMAND_RESULT_POSTURE_MISSING"),
            ("no_command_success_posture", "NO_COMMAND_SUCCESS_POSTURE_MISSING"),
            ("no_output_as_source_posture", "NO_OUTPUT_AS_SOURCE_POSTURE_MISSING"),
            ("no_result_as_authority_posture", "NO_RESULT_AS_AUTHORITY_POSTURE_MISSING"),
            ("no_success_as_currentness_posture", "NO_SUCCESS_AS_CURRENTNESS_POSTURE_MISSING"),
            ("no_final_completion_posture", "NO_FINAL_COMPLETION_POSTURE_MISSING"),
            ("authorization_token_reuse_blocked_posture", "AUTHORIZATION_TOKEN_REUSED"),
            ("consumed_token_closed_posture", "CONSUMED_REQUEST_REOPENED"),
            ("no_reopen_consumed_request_posture", "CONSUMED_REQUEST_REOPENED"),
            ("returned_result_containment_posture", "NON_CLAIM_MISSING_OR_FLIPPED"),
            ("reference_shaped_input_posture", "REFERENCE_SHAPED_INPUT_POSTURE_MISSING"),
        ]
        for key, expected in posture_cases:
            with self.subTest(key=key):
                self.assertBlockedWithCode(_mutated_request(lambda request, key=key: request.pop(key)), expected)

    def test_required_non_claim_missing_or_flipped_blocks(self) -> None:
        missing_request = _valid_request()
        missing_request["declared_non_claims"].pop("stdout_captured")
        self.assertBlockedWithCode(missing_request, "NON_CLAIM_MISSING_OR_FLIPPED")

        flipped_request = _valid_request()
        flipped_request["declared_non_claims"]["raw_full_prior_artifact_body_returned"] = True
        self.assertBlockedWithCode(flipped_request, "NON_CLAIM_MISSING_OR_FLIPPED")

    def test_raw_prior_and_raw_output_body_values_are_not_returned(self) -> None:
        prior_body_request = _valid_request()
        prior_body_request["selected_command_report_basis"]["full_prior_artifact_body"] = (
            RAW_PRIOR_SENTINEL
        )
        prior_result = self.assertBlockedWithCode(
            prior_body_request, "FULL_PRIOR_ARTIFACT_BODY_EMITTED"
        )
        prior_text = _json_text(prior_result)
        self.assertNotIn(RAW_PRIOR_SENTINEL, prior_text)
        self.assertIn("raw_full_prior_artifact_body_not_returned", prior_text)

        raw_output_request = _valid_request()
        raw_output_request["selected_command_output_basis"]["stdout"] = RAW_OUTPUT_SENTINEL
        raw_output_result = self.assertBlockedWithCode(raw_output_request, "RAW_OUTPUT_BODY_CAPTURED")
        raw_output_text = _json_text(raw_output_result)
        self.assertNotIn(RAW_OUTPUT_SENTINEL, raw_output_text)
        self.assertIn("raw_output_body_not_returned", raw_output_text)

    def test_summary_helper_preserves_output_capture_boundary_non_claims(self) -> None:
        result = resolve_portable_source_body_verification_output_capture_boundary(
            declared_output_capture_boundary_request=_valid_request()
        )
        summary = build_portable_source_body_verification_output_capture_boundary_summary(result)

        self.assertEqual(RECORDED, summary["outcome"])
        self.assertIsNone(summary["block_code"])
        self.assertTrue(summary["output_capture_boundary_recorded"])
        self.assertTrue(summary["one_future_output_capture_step_declared"])
        self.assertTrue(summary["command_output_basis_preserved"])
        self.assertTrue(summary["bounded_command_output_event_preserved"])
        self.assertTrue(summary["command_output_boundary_basis_preserved"])
        self.assertTrue(summary["command_output_containment_basis_preserved"])
        self.assertTrue(summary["recorded_command_execution_event_preserved"])
        self.assertTrue(summary["execution_trace_audit_only_preserved"])
        self.assertTrue(summary["stdout_still_not_captured"])
        self.assertTrue(summary["stderr_still_not_captured"])
        self.assertTrue(summary["process_output_still_not_captured"])
        self.assertTrue(summary["raw_output_body_still_not_captured"])
        self.assertTrue(summary["output_capture_not_created"])
        self.assertTrue(summary["output_report_artifact_not_created"])
        self.assertTrue(summary["command_result_still_not_created"])
        self.assertTrue(summary["command_success_still_not_created"])
        self.assertEqual(resolver.COMMAND_OUTPUT_OUTCOME, summary["selected_command_output_outcome"])
        self.assertEqual(0, summary["selected_command_output_failed_check_count"])
        self.assertEqual(
            resolver.POST_INVOCATION_COMMAND_EXECUTION_OUTCOME,
            summary["selected_post_invocation_execution_outcome"],
        )
        self.assertEqual(0, summary["selected_post_invocation_execution_failed_check_count"])
        self.assertEqual(resolver.V2_ADMITTED_REQUEST_OUTCOME, summary["selected_v2_outcome"])
        self.assertEqual(resolver.V2_ADMITTED_REQUEST_VERSION, summary["selected_v2_version"])
        self.assertTrue(
            summary[
                "output_capture_boundary_not_stdout_stderr_process_raw_capture_report_result_success"
            ]
        )
        self.assertTrue(
            summary[
                "command_output_not_capture_report_result_success_source_authority_currentness_final_completion"
            ]
        )
        self.assertTrue(summary["execution_trace_not_output_capture_result_success_source_authority"])
        self.assertTrue(summary["result_not_authority"])
        self.assertTrue(summary["success_not_currentness_final_completion"])
        self.assertTrue(
            summary["older_command_execution_boundary_lineage_not_treated_as_current_execution"]
        )
        self.assertTrue(summary["no_raw_full_prior_artifact_body"])
        self.assertTrue(summary["no_artifact_mutation"])
        self.assertTrue(summary["no_deployment_runtime_public_release"])
        self.assertTrue(summary["no_operation_public_readiness_final_completion"])
        self.assertTrue(summary["no_continuation_publication_reusable_follow_on"])
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(summary["key_non_claims"][key], False, key)

    def test_resolver_does_not_mutate_request_selected_basis_posture_or_scope(self) -> None:
        request = _valid_request()
        before = copy.deepcopy(request)
        selected_before = {key: copy.deepcopy(request[key]) for key in SELECTED_BASIS_KEYS}
        posture_before = {key: copy.deepcopy(request[key]) for key in POSTURE_KEYS}
        scope_before = copy.deepcopy(request["output_capture_boundary_scope"])

        result = resolve_portable_source_body_verification_output_capture_boundary(
            declared_output_capture_boundary_request=request
        )

        self.assertEqual(RECORDED, result["outcome"])
        self.assertEqual(before, request)
        for key, value in selected_before.items():
            self.assertEqual(value, request[key], key)
        for key, value in posture_before.items():
            self.assertEqual(value, request[key], key)
        self.assertEqual(scope_before, request["output_capture_boundary_scope"])


if __name__ == "__main__":
    unittest.main()
