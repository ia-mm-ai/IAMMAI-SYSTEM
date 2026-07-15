"""Tests for portable source-body verification command result v2.

This suite treats v1 command-result resolution as visible predecessor
conformance-failure evidence and verifies that v2 fixes public block-code
conformance for output-capture treatment blocks without changing the bounded
command-result law. V2 records one command result only; it does not create
command success, infer success/currentness/final completion/public readiness/
deployment readiness, infer unbounded pass/fail, or authorize follow-on work.
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

import resolve_portable_source_body_verification_command_result_v2 as resolver


RECORDED = resolver.OUTCOME_RECORDED
BLOCKED = resolver.OUTCOME_BLOCKED
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_COMMAND_RESULT_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
POSTURE_KEYS = tuple(resolver.POSTURE_KEYS)
SELECTED_BASIS_KEYS = tuple(resolver.SELECTED_BASIS_KEYS)
RAW_FULL_BODY_SENTINEL = "RAW_COMMAND_RESULT_V2_BODY_MUST_NOT_RETURN_" * 8

MISSING_V1_BLOCK_CODES = (
    "OUTPUT_CAPTURE_TREATED_AS_RESULT",
    "OUTPUT_CAPTURE_TREATED_AS_SUCCESS",
    "OUTPUT_CAPTURE_TREATED_AS_SOURCE",
    "OUTPUT_CAPTURE_TREATED_AS_AUTHORITY",
    "OUTPUT_CAPTURE_TREATED_AS_CURRENTNESS",
    "OUTPUT_CAPTURE_TREATED_AS_FINAL_COMPLETION",
)

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_command_result_metadata",
    "declared_command_result_question",
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
    "command_result_only_posture",
    "bounded_command_result_posture",
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
    "no_command_success_posture",
    "no_success_inference_posture",
    "no_currentness_inference_posture",
    "no_final_completion_inference_posture",
    "no_public_readiness_inference_posture",
    "no_deployment_readiness_inference_posture",
    "no_unbounded_pass_fail_inference_posture",
    "no_result_as_authority_posture",
    "no_success_as_currentness_posture",
    "no_final_completion_posture",
    "authorization_token_reuse_blocked_posture",
    "consumed_token_closed_posture",
    "no_reopen_consumed_request_posture",
    "returned_result_containment_posture",
    "command_result_scope",
    "command_result_checks",
    "command_result_statement",
    "command_result_non_meaning",
    "command_result_payload",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_command_result_summary",
)


def _json_text(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=True)


def _false_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _reference_basis(label: str, **overrides: Any) -> dict[str, Any]:
    basis: dict[str, Any] = {
        "basis_label": label,
        "declared": True,
        "basis_declared": True,
        "basis_reference": f"synthetic://{label}",
        "path": f"synthetic://{label}.json",
        "result_path": f"synthetic://{label}.json",
        "reference_shaped_basis": True,
        "basis_remains_reference_shaped": True,
        "basis_remains_basis_only": True,
        "basis_is_not_result": True,
        "basis_is_not_success": True,
        "basis_is_not_source": True,
        "basis_is_not_authority": True,
        "basis_is_not_currentness": True,
        "basis_is_not_final_completion": True,
        "full_upstream_lineage_preserved": True,
        "full_prior_artifact_body_not_emitted": True,
        "full_prior_artifacts_embedded": False,
        "raw_full_prior_artifact_body_returned": False,
        "prior_artifacts_mutated": False,
        "report_body_absent_or_bounded": True,
        "report_body_not_invented": True,
        "report_body_invented": False,
        "result_body_absent_or_bounded": True,
        "result_body_not_invented": True,
        "result_body_invented": False,
        "command_result_created": False,
        "command_success_created": False,
        "success_body_invented": False,
        "success_inference_made": False,
        "currentness_inference_made": False,
        "final_completion_inference_made": False,
        "public_readiness_inference_made": False,
        "deployment_readiness_inference_made": False,
        "unbounded_pass_fail_inference_made": False,
        "pass_inference_made": False,
        "fail_inference_made": False,
        "authorization_token_reuse_blocked": True,
        "authorization_token_reused": False,
        "consumed_request_token_remains_closed": True,
        "consumed_request_reopened": False,
        "returned_result_containment_preserved": True,
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
    basis.update(_false_non_claims())
    basis.update(overrides)
    return basis


def _terminal_summary_basis(label: str, **overrides: Any) -> dict[str, Any]:
    basis = _reference_basis(
        label,
        terminal_summary_declared=True,
        terminal_summary_path=f"spec/{label}.md",
        terminal_summary_remains_readability_basis_only=True,
        readability_basis_only=True,
        terminal_summary_does_not_create_command_result=True,
        terminal_summary_does_not_create_command_success=True,
        terminal_summary_does_not_infer_success=True,
        terminal_summary_does_not_infer_currentness=True,
        terminal_summary_does_not_infer_final_completion=True,
        terminal_summary_does_not_infer_public_readiness=True,
        terminal_summary_does_not_infer_deployment_readiness=True,
        terminal_summary_does_not_authorize_follow_on_work=True,
    )
    basis.update(overrides)
    return basis


def _posture(label: str, **overrides: Any) -> dict[str, Any]:
    posture: dict[str, Any] = {
        "posture_label": label,
        "declared": True,
        "posture_declared": True,
        "posture": label,
        "command_result_recorded": True,
        "bounded_command_result_recorded": True,
        "command_result_boundary_basis_preserved": True,
        "command_output_report_artifact_basis_preserved": True,
        "bounded_command_output_report_artifact_preserved": True,
        "command_output_report_artifact_boundary_basis_preserved": True,
        "output_capture_v2_basis_preserved": True,
        "output_capture_v1_predecessor_failure_preserved": True,
        "bounded_output_capture_event_preserved": True,
        "command_output_basis_preserved": True,
        "recorded_command_execution_event_preserved": True,
        "execution_trace_audit_only": True,
        "execution_trace_audit_only_preserved": True,
        "report_body_present": False,
        "report_body_absent_or_bounded": True,
        "report_body_not_invented": True,
        "result_body_present": False,
        "result_body_absent_or_bounded": True,
        "result_body_not_invented": True,
        "command_success_not_created": True,
        "command_success_still_not_created": True,
        "success_inference_blocked": True,
        "currentness_inference_blocked": True,
        "final_completion_inference_blocked": True,
        "public_readiness_inference_blocked": True,
        "deployment_readiness_inference_blocked": True,
        "unbounded_pass_fail_inference_blocked": True,
        "authorization_token_reuse_blocked": True,
        "consumed_request_token_remains_closed": True,
        "returned_result_containment_preserved": True,
        "v1_predecessor_failure_preserved": True,
        "v1_repaired": False,
        "v1_hidden": False,
        "v1_claimed_passed": False,
        "v2_successor_does_not_erase_v1": True,
    }
    posture.update(_false_non_claims())
    posture.update(overrides)
    return posture


def _command_result_boundary_basis(**overrides: Any) -> dict[str, Any]:
    basis = _reference_basis(
        "command_result_boundary",
        outcome=resolver.COMMAND_RESULT_BOUNDARY_OUTCOME,
        result_version="0.1.0",
        failed_check_count=0,
        passed_check_count=148,
        one_future_command_result_step_declared=True,
        one_future_command_result_step_only=True,
        command_result_created=False,
        result_body_not_invented=True,
        result_body_invented=False,
        command_success_created=False,
        pass_inference_made=False,
        fail_inference_made=False,
        command_result_boundary_treated_as_result=False,
        command_result_boundary_treated_as_success=False,
        command_result_boundary_treated_as_source=False,
        command_result_boundary_treated_as_authority=False,
        command_result_boundary_treated_as_currentness=False,
        command_result_boundary_treated_as_final_completion=False,
        command_result_boundary_remains_boundary_only=True,
    )
    basis.update(overrides)
    return basis


def _command_output_report_artifact_basis(**overrides: Any) -> dict[str, Any]:
    basis = _reference_basis(
        "command_output_report_artifact",
        outcome=resolver.COMMAND_OUTPUT_REPORT_ARTIFACT_OUTCOME,
        result_version="0.1.0",
        failed_check_count=0,
        passed_check_count=133,
        command_output_report_artifact_recorded=True,
        bounded_command_output_report_artifact_recorded=True,
        report_body_present=False,
        report_body_absent_or_bounded=True,
        report_body_not_invented=True,
        report_body_invented=False,
        command_result_created=False,
        command_success_created=False,
        artifact_remains_artifact_posture_only=True,
        command_output_report_artifact_treated_as_result_authority=False,
        command_output_report_artifact_treated_as_result=False,
        command_output_report_artifact_treated_as_success=False,
        command_output_report_artifact_treated_as_source=False,
        command_output_report_artifact_treated_as_authority=False,
        command_output_report_artifact_treated_as_currentness=False,
        command_output_report_artifact_treated_as_final_completion=False,
    )
    basis.update(overrides)
    return basis


def _command_output_report_artifact_boundary_basis(**overrides: Any) -> dict[str, Any]:
    basis = _reference_basis(
        "command_output_report_artifact_boundary",
        outcome=resolver.COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_OUTCOME,
        failed_check_count=0,
        passed_check_count=125,
        one_future_command_output_report_artifact_step_declared=True,
        one_future_report_artifact_step_declared=True,
        command_result_created=False,
        command_success_created=False,
        boundary_remains_boundary_only=True,
    )
    basis.update(overrides)
    return basis


def _output_capture_v2_basis(**overrides: Any) -> dict[str, Any]:
    basis = _reference_basis(
        "output_capture_v2",
        outcome=resolver.OUTPUT_CAPTURE_V2_OUTCOME,
        result_version=resolver.OUTPUT_CAPTURE_V2_VERSION,
        failed_check_count=0,
        passed_check_count=125,
        json_safe_result=True,
        v1_predecessor_failure_preserved=True,
        v1_repaired=False,
        v1_hidden=False,
        v1_claimed_passed=False,
        v2_successor_does_not_erase_v1=True,
        bounded_output_capture_event_recorded=True,
        one_bounded_output_capture_event_recorded=True,
        stdout_content_invented=False,
        stderr_content_invented=False,
        process_output_content_invented=False,
        raw_output_body_content_invented=False,
        output_capture_v2_remains_output_capture_posture_only=True,
    )
    basis.update(overrides)
    return basis


def _command_result_payload(**overrides: Any) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "command_result_payload_recorded": True,
        "payload_type": "COMMAND_RESULT_BOUNDED",
        "result_body_present": False,
        "result_body_absent_or_bounded": True,
        "result_body_invented": False,
        "report_body_absent_or_bounded": True,
        "report_body_invented": False,
        "stdout_content_invented": False,
        "stderr_content_invented": False,
        "process_output_content_invented": False,
        "raw_output_body_content_invented": False,
        "success_body_invented": False,
        "command_success_created": False,
        "success_inference_made": False,
        "currentness_inference_made": False,
        "final_completion_inference_made": False,
        "public_readiness_inference_made": False,
        "deployment_readiness_inference_made": False,
        "unbounded_pass_fail_inference_made": False,
        "command_result_is_not_success": True,
        "command_result_is_not_source": True,
        "command_result_is_not_authority": True,
        "command_result_is_not_currentness": True,
        "command_result_is_not_final_completion": True,
        "command_result_is_not_public_readiness": True,
        "command_result_is_not_deployment_readiness": True,
    }
    payload.update(overrides)
    return payload


def _valid_request(**overrides: Any) -> dict[str, Any]:
    request: dict[str, Any] = {
        "command_result_request_id": "command_result_v2_reference_review_001",
        "command_result_question": resolver.CORE_QUESTION,
        "command_result_intent": resolver.INTENT_RECORD,
        "selected_command_result_boundary_basis": _command_result_boundary_basis(),
        "selected_command_result_boundary_terminal_summary_basis": _terminal_summary_basis(
            "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_BOUNDARY_TERMINAL_SUMMARY_V0"
        ),
        "selected_command_output_report_artifact_basis": _command_output_report_artifact_basis(),
        "selected_command_output_report_artifact_terminal_summary_basis": _terminal_summary_basis(
            "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_REPORT_ARTIFACT_TERMINAL_SUMMARY_V0"
        ),
        "selected_command_output_report_artifact_boundary_basis": (
            _command_output_report_artifact_boundary_basis()
        ),
        "selected_command_output_report_artifact_boundary_terminal_summary_basis": (
            _terminal_summary_basis(
                "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_TERMINAL_SUMMARY_V0"
            )
        ),
        "selected_output_capture_v2_basis": _output_capture_v2_basis(),
        "selected_output_capture_v2_terminal_summary_basis": _terminal_summary_basis(
            "PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_V2_TERMINAL_SUMMARY_V0"
        ),
        "selected_output_capture_v1_predecessor_failure_basis": _reference_basis(
            "output_capture_v1_predecessor_failure",
            selected_output_capture_v1_predecessor_path=(
                "src/resolve_portable_source_body_verification_output_capture.py"
            ),
            v1_predecessor_failure_basis_declared=True,
            v1_output_capture_predecessor_failure_preserved=True,
            v1_write_failed_on_frozenset_in_expected_posture=True,
            v1_output_capture_repaired=False,
            v1_output_capture_hidden=False,
            v1_output_capture_claimed_passed=False,
            v2_output_capture_erased_v1=False,
            predecessor_failure_basis_only=True,
        ),
        "selected_output_capture_boundary_basis": _reference_basis(
            "output_capture_boundary",
            outcome=resolver.OUTPUT_CAPTURE_BOUNDARY_OUTCOME,
            failed_check_count=0,
            one_future_output_capture_step_declared=True,
        ),
        "selected_command_output_basis": _reference_basis(
            "command_output",
            outcome=resolver.COMMAND_OUTPUT_OUTCOME,
            failed_check_count=0,
            one_bounded_command_output_event_recorded=True,
        ),
        "selected_command_output_boundary_basis": _reference_basis(
            "command_output_boundary",
            outcome=resolver.COMMAND_OUTPUT_BOUNDARY_OUTCOME,
            failed_check_count=0,
        ),
        "selected_command_output_containment_basis": _reference_basis(
            "command_output_containment",
            outcome=resolver.COMMAND_OUTPUT_CONTAINMENT_OUTCOME,
            failed_check_count=0,
        ),
        "selected_post_invocation_command_execution_basis": _reference_basis(
            "post_invocation_command_execution",
            outcome=resolver.POST_INVOCATION_COMMAND_EXECUTION_OUTCOME,
            failed_check_count=0,
            bounded_execution_event_recorded=True,
            one_bounded_command_execution_event_recorded=True,
            execution_trace_audit_only=True,
        ),
        "selected_post_invocation_command_execution_terminal_summary_basis": (
            _terminal_summary_basis("post_invocation_command_execution_terminal_summary")
        ),
        "selected_command_invocation_basis": _reference_basis(
            "command_invocation",
            outcome=resolver.COMMAND_INVOCATION_OUTCOME,
            failed_check_count=0,
            authorization_token_spent_exactly_once=True,
            authorization_token_reuse_blocked=True,
        ),
        "selected_command_execution_review_basis": _reference_basis(
            "command_execution_review",
            outcome=resolver.COMMAND_EXECUTION_REVIEW_OUTCOME,
            failed_check_count=0,
            review_basis_only=True,
        ),
        "selected_request_consumption_basis": _reference_basis(
            "request_consumption",
            outcome=resolver.REQUEST_CONSUMPTION_OUTCOME,
            failed_check_count=0,
            request_consumed_exactly_once=True,
            consumption_token_closed=True,
        ),
        "selected_consumed_request_basis": _reference_basis(
            "consumed_request",
            consumed_request_token_remains_closed=True,
            consumed_request_is_reopened=False,
            consumed_request_reopened=False,
            consumed_request_basis_only=True,
        ),
        "selected_v2_admitted_request_basis": _reference_basis(
            "v2_admitted_request",
            outcome=resolver.V2_ADMITTED_REQUEST_OUTCOME,
            result_version=resolver.V2_ADMITTED_REQUEST_VERSION,
            failed_check_count=0,
            successor_metadata_preserved=True,
            returned_result_containment_preserved=True,
            v2_does_not_claim_v1_passed=True,
        ),
        "selected_v1_predecessor_failure_basis": _reference_basis(
            "earlier_v1_predecessor_failure",
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
        ),
        "selected_older_command_execution_boundary_lineage_basis": _reference_basis(
            "older_command_execution_boundary_lineage",
            basis_remains_prior_scaffolding_only=True,
            lineage_basis_not_treated_as_current_execution=True,
            older_command_execution_boundary_lineage_treated_as_current_execution=False,
        ),
        "selected_command_report_lineage_basis": _reference_basis(
            "command_report_lineage",
            basis_remains_lineage_only=True,
            command_report_lineage_basis_not_current_report_artifact=True,
            command_report_lineage_basis_not_command_result_authority=True,
            command_report_lineage_basis_not_command_success=True,
            command_report_lineage_basis_treated_as_current_report_artifact=False,
            command_report_lineage_basis_treated_as_command_result_authority=False,
            command_report_lineage_basis_treated_as_command_result=False,
            command_report_lineage_basis_treated_as_command_success=False,
            current_report_artifact=False,
        ),
        "selected_command_implementation_boundary_basis": _reference_basis(
            "command_implementation_boundary"
        ),
        "selected_command_boundary_basis": _reference_basis("command_boundary"),
        "selected_artifact_emission_containment_basis": _reference_basis(
            "artifact_emission_containment"
        ),
        "selected_evidence_manifest_basis": _reference_basis("evidence_manifest"),
        "selected_portable_verification_basis": _reference_basis("portable_verification"),
        "command_result_scope": sorted(SUPPORTED_SCOPE),
        "command_result_payload": _command_result_payload(),
        "requested_command_result_outcome": RECORDED,
        "declared_non_claims": _false_non_claims(),
        "reference_shaped_input_posture": True,
    }
    for key in POSTURE_KEYS:
        request[key] = _posture(key)
    request.update(overrides)
    return request


def _copy_request_with(mutator: Callable[[dict[str, Any]], None]) -> dict[str, Any]:
    request = _valid_request()
    mutator(request)
    return request


def _resolve(request: Mapping[str, Any]) -> dict[str, Any]:
    return resolver.resolve_portable_source_body_verification_command_result_v2(
        declared_command_result_request=request
    )


class CommandResultV2Tests(unittest.TestCase):
    def assertPublicBlockConformance(self, result: Mapping[str, Any]) -> None:
        block = result.get("block", {})
        block_code = block.get("block_code") if isinstance(block, Mapping) else None
        if block_code is not None:
            self.assertIn(block_code, resolver.BLOCK_CODES)
        for check in result.get("command_result_checks", []):
            for code_key in ("block_code", "failure_code"):
                code = check.get(code_key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES, (check.get("check_name"), code))

    def assertV2Metadata(self, result: Mapping[str, Any]) -> None:
        metadata = result["portable_source_body_verification_command_result_metadata"]
        self.assertEqual(
            metadata["portable_source_body_verification_command_result_result_version"],
            "0.2.0",
        )
        self.assertEqual(metadata["result_version"], "0.2.0")
        self.assertEqual(metadata["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertEqual(metadata["resolver_module"], "resolve_portable_source_body_verification_command_result_v2")
        self.assertEqual(metadata["successor_of"], "resolve_portable_source_body_verification_command_result")
        self.assertIn("conformance-failure", metadata["successor_reason"])
        self.assertIn("undeclared public block codes", metadata["successor_reason"])
        self.assertIn("OUTPUT_CAPTURE_TREATED_AS_RESULT", metadata["successor_reason"])
        self.assertIs(metadata["v1_predecessor_failure_preserved"], True)
        self.assertIs(metadata["v1_repaired"], False)
        self.assertIs(metadata["v1_hidden"], False)
        self.assertIs(metadata["v1_claimed_passed"], False)
        self.assertIs(metadata["v2_successor_does_not_erase_v1"], True)
        self.assertIs(metadata["returned_result_containment_preserved"], True)

    def assertNoSuccessOrFollowOn(self, result: Mapping[str, Any]) -> None:
        statement = result["command_result_statement"]
        non_claims = result["non_claims"]
        for key in (
            "command_success_created",
            "success_body_invented",
            "success_inference_made",
            "currentness_inference_made",
            "final_completion_inference_made",
            "public_readiness_inference_made",
            "deployment_readiness_inference_made",
            "unbounded_pass_fail_inference_made",
            "follow_on_work_authorized",
        ):
            self.assertIs(statement.get(key, non_claims.get(key)), False, key)
            self.assertIs(non_claims.get(key, False), False, key)

    def assertRecorded(self, result: Mapping[str, Any]) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertIs(result["block"]["blocked"], False)
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(
            result["portable_source_body_verification_command_result_metadata"]["failed_check_count"],
            0,
        )
        self.assertV2Metadata(result)
        self.assertPublicBlockConformance(result)
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        statement = result["command_result_statement"]
        for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIs(statement[key], True, key)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, result["non_claims"])
            self.assertIs(result["non_claims"][key], False, key)
            self.assertIs(statement[key], False, key)
        self.assertNoSuccessOrFollowOn(result)

    def assertBlocked(self, result: Mapping[str, Any], expected_code: str | None = None) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertIs(result["block"]["blocked"], True)
        self.assertIsNotNone(result["block"]["block_code"])
        if expected_code is not None:
            self.assertEqual(result["block"]["block_code"], expected_code)
        self.assertIn(result["block"]["block_code"], resolver.BLOCK_CODES)
        self.assertV2Metadata(result)
        self.assertPublicBlockConformance(result)
        self.assertNoSuccessOrFollowOn(result)

    def test_public_api_block_codes_and_aliases_are_v2(self) -> None:
        for api_name in (
            "resolve_portable_source_body_verification_command_result_v2",
            "resolve_portable_source_body_verification_command_result_v2_from_path",
            "write_portable_source_body_verification_command_result_v2_result",
            "build_portable_source_body_verification_command_result_v2_summary",
            "build_declared_portable_source_body_verification_command_result_v2_request",
        ):
            self.assertTrue(callable(getattr(resolver, api_name)), api_name)
        for block_code in MISSING_V1_BLOCK_CODES:
            self.assertIn(block_code, resolver.BLOCK_CODES)

        if hasattr(resolver, "resolve_portable_source_body_verification_command_result"):
            alias_result = resolver.resolve_portable_source_body_verification_command_result(
                declared_command_result_request=_valid_request()
            )
            self.assertRecorded(alias_result)
            self.assertEqual(
                alias_result["portable_source_body_verification_command_result_metadata"][
                    "resolver_module"
                ],
                "resolve_portable_source_body_verification_command_result_v2",
            )
        for alias_name in (
            "resolve_portable_source_body_verification_command_result_from_path",
            "write_portable_source_body_verification_command_result_result",
            "build_portable_source_body_verification_command_result_summary",
        ):
            if hasattr(resolver, alias_name):
                self.assertTrue(callable(getattr(resolver, alias_name)), alias_name)

    def test_successful_recorded_result_preserves_v2_successor_posture(self) -> None:
        result = _resolve(_valid_request())
        self.assertRecorded(result)

        boundary = result["selected_command_result_boundary_basis"]
        self.assertEqual(boundary["outcome"], resolver.COMMAND_RESULT_BOUNDARY_OUTCOME)
        self.assertEqual(boundary["failed_check_count"], 0)
        self.assertIs(boundary["one_future_command_result_step_declared"], True)
        self.assertIs(boundary["command_result_created"], False)
        self.assertIs(boundary["result_body_invented"], False)
        self.assertIs(boundary["command_success_created"], False)
        self.assertIs(boundary["pass_inference_made"], False)
        self.assertIs(boundary["fail_inference_made"], False)

        artifact = result["selected_command_output_report_artifact_basis"]
        self.assertEqual(artifact["outcome"], resolver.COMMAND_OUTPUT_REPORT_ARTIFACT_OUTCOME)
        self.assertEqual(artifact["failed_check_count"], 0)
        self.assertIs(artifact["bounded_command_output_report_artifact_recorded"], True)
        self.assertIs(artifact["report_body_absent_or_bounded"], True)
        self.assertIs(artifact["report_body_not_invented"], True)
        self.assertIs(artifact["command_success_created"], False)

        output_capture = result["selected_output_capture_v2_basis"]
        self.assertEqual(output_capture["outcome"], resolver.OUTPUT_CAPTURE_V2_OUTCOME)
        self.assertEqual(output_capture["result_version"], "0.2.0")
        self.assertEqual(output_capture["failed_check_count"], 0)
        self.assertIs(output_capture["json_safe_result"], True)
        self.assertIs(output_capture["v1_predecessor_failure_preserved"], True)
        self.assertIs(output_capture["v1_repaired"], False)
        self.assertIs(output_capture["v1_hidden"], False)
        self.assertIs(output_capture["v1_claimed_passed"], False)
        self.assertIs(output_capture["v2_successor_does_not_erase_v1"], True)
        for key in (
            "stdout_content_invented",
            "stderr_content_invented",
            "process_output_content_invented",
            "raw_output_body_content_invented",
        ):
            self.assertIs(output_capture[key], False, key)

        payload = result["command_result_payload"]
        self.assertEqual(payload["payload_type"], "COMMAND_RESULT_BOUNDED")
        self.assertIs(payload["result_body_present"], False)
        self.assertIs(payload["result_body_absent_or_bounded"], True)
        self.assertIs(payload["result_body_invented"], False)
        self.assertIs(payload["report_body_absent_or_bounded"], True)
        self.assertIs(payload["report_body_invented"], False)
        self.assertIs(payload["success_body_invented"], False)
        self.assertIs(payload["command_success_created"], False)
        for key in (
            "command_result_is_not_success",
            "command_result_is_not_source",
            "command_result_is_not_authority",
            "command_result_is_not_currentness",
            "command_result_is_not_final_completion",
            "command_result_is_not_public_readiness",
            "command_result_is_not_deployment_readiness",
        ):
            self.assertIs(payload[key], True, key)
        for raw_key in (
            "result_body",
            "success_body",
            "report_body",
            "source_body",
            "authority_body",
            "currentness_claim",
            "final_completion_claim",
            "public_readiness_claim",
            "deployment_readiness_claim",
        ):
            self.assertNotIn(raw_key, payload, raw_key)

    def test_six_v1_output_capture_treatment_cases_are_public_blocks(self) -> None:
        cases = (
            ("output_capture_treated_as_result", "OUTPUT_CAPTURE_TREATED_AS_RESULT"),
            ("output_capture_treated_as_success", "OUTPUT_CAPTURE_TREATED_AS_SUCCESS"),
            ("output_capture_treated_as_source", "OUTPUT_CAPTURE_TREATED_AS_SOURCE"),
            ("output_capture_treated_as_authority", "OUTPUT_CAPTURE_TREATED_AS_AUTHORITY"),
            ("output_capture_treated_as_currentness", "OUTPUT_CAPTURE_TREATED_AS_CURRENTNESS"),
            (
                "output_capture_treated_as_final_completion",
                "OUTPUT_CAPTURE_TREATED_AS_FINAL_COMPLETION",
            ),
        )
        for field, expected_code in cases:
            with self.subTest(field=field):
                request = _copy_request_with(
                    lambda request, field=field: request["selected_output_capture_v2_basis"].update(
                        {field: True}
                    )
                )
                result = _resolve(request)
                self.assertBlocked(result, expected_code)

    def test_representative_blocking_behavior_uses_declared_public_codes(self) -> None:
        self.assertBlocked(
            resolver.resolve_portable_source_body_verification_command_result_v2(None),
            "DECLARED_COMMAND_RESULT_REQUEST_MALFORMED",
        )
        self.assertBlocked(
            resolver.resolve_portable_source_body_verification_command_result_v2(
                declared_command_result_request=[]
            ),
            "DECLARED_COMMAND_RESULT_REQUEST_MALFORMED",
        )

        cases: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
            ("explicit block intent", lambda request: request.update({"command_result_intent": resolver.INTENT_BLOCK})),
            ("unsupported intent", lambda request: request.update({"command_result_intent": "UNSUPPORTED"})),
            ("unsupported scope", lambda request: request.update({"command_result_scope": ["UNSUPPORTED_SCOPE"]})),
            ("missing boundary basis", lambda request: request.update({"selected_command_result_boundary_basis": {}})),
            ("boundary not recorded", lambda request: request["selected_command_result_boundary_basis"].update({"outcome": "NOT_RECORDED"})),
            ("boundary failed checks", lambda request: request["selected_command_result_boundary_basis"].update({"failed_check_count": 1})),
            ("boundary step not declared", lambda request: request["selected_command_result_boundary_basis"].update({"one_future_command_result_step_declared": False})),
            ("boundary created result body", lambda request: request["selected_command_result_boundary_basis"].update({"result_body_invented": True})),
            ("boundary created success", lambda request: request["selected_command_result_boundary_basis"].update({"command_success_created": True})),
            ("boundary inferred pass", lambda request: request["selected_command_result_boundary_basis"].update({"pass_inference_made": True})),
            ("boundary inferred fail", lambda request: request["selected_command_result_boundary_basis"].update({"fail_inference_made": True})),
            ("missing artifact basis", lambda request: request.update({"selected_command_output_report_artifact_basis": {}})),
            ("artifact not recorded", lambda request: request["selected_command_output_report_artifact_basis"].update({"outcome": "NOT_RECORDED"})),
            ("artifact invented report body", lambda request: request["selected_command_output_report_artifact_basis"].update({"report_body_invented": True})),
            ("artifact created success", lambda request: request["selected_command_output_report_artifact_basis"].update({"command_success_created": True})),
            ("artifact treated result authority", lambda request: request.update({"command_output_report_artifact_treated_as_result_authority": True})),
            ("artifact treated success", lambda request: request.update({"command_output_report_artifact_treated_as_success": True})),
            ("missing output capture v2", lambda request: request.update({"selected_output_capture_v2_basis": {}})),
            ("output capture not recorded", lambda request: request["selected_output_capture_v2_basis"].update({"outcome": "NOT_RECORDED"})),
            ("output capture wrong version", lambda request: request["selected_output_capture_v2_basis"].update({"result_version": "0.1.0"})),
            ("output capture not JSON safe", lambda request: request["selected_output_capture_v2_basis"].update({"json_safe_result": False})),
            ("output capture predecessor missing", lambda request: request["selected_output_capture_v2_basis"].update({"v1_predecessor_failure_preserved": False})),
            ("output capture repaired v1", lambda request: request["selected_output_capture_v2_basis"].update({"v1_repaired": True})),
            ("output capture hid v1", lambda request: request["selected_output_capture_v2_basis"].update({"v1_hidden": True})),
            ("output capture claimed v1 passed", lambda request: request["selected_output_capture_v2_basis"].update({"v1_claimed_passed": True})),
            ("output capture erased v1", lambda request: request["selected_output_capture_v2_basis"].update({"v2_successor_does_not_erase_v1": False})),
            ("output capture invented stdout", lambda request: request["selected_output_capture_v2_basis"].update({"stdout_content_invented": True})),
            ("output capture invented stderr", lambda request: request["selected_output_capture_v2_basis"].update({"stderr_content_invented": True})),
            ("output capture invented process output", lambda request: request["selected_output_capture_v2_basis"].update({"process_output_content_invented": True})),
            ("output capture invented raw output", lambda request: request["selected_output_capture_v2_basis"].update({"raw_output_body_content_invented": True})),
            ("result treated as success", lambda request: request.update({"command_result_treated_as_success": True})),
            ("result treated as source", lambda request: request.update({"command_result_treated_as_source": True})),
            ("result treated as authority", lambda request: request.update({"command_result_treated_as_authority": True})),
            ("result treated as currentness", lambda request: request.update({"command_result_treated_as_currentness": True})),
            ("result treated as final completion", lambda request: request.update({"command_result_treated_as_final_completion": True})),
            ("result treated as public readiness", lambda request: request.update({"command_result_treated_as_public_readiness": True})),
            ("result treated as deployment readiness", lambda request: request.update({"command_result_treated_as_deployment_readiness": True})),
            ("result body invented", lambda request: request.update({"result_body_invented": True})),
            ("command success created", lambda request: request.update({"command_success_created": True})),
            ("success inference made", lambda request: request.update({"success_inference_made": True})),
            ("currentness inference made", lambda request: request.update({"currentness_inference_made": True})),
            ("final completion inference made", lambda request: request.update({"final_completion_inference_made": True})),
            ("public readiness inference made", lambda request: request.update({"public_readiness_inference_made": True})),
            ("deployment readiness inference made", lambda request: request.update({"deployment_readiness_inference_made": True})),
            ("unbounded pass/fail inference made", lambda request: request.update({"unbounded_pass_fail_inference_made": True})),
            ("execution trace result", lambda request: request.update({"execution_trace_treated_as_result": True})),
            ("execution trace success", lambda request: request.update({"execution_trace_treated_as_success": True})),
            ("execution trace source", lambda request: request.update({"execution_trace_treated_as_source": True})),
            ("execution trace authority", lambda request: request.update({"execution_trace_treated_as_authority": True})),
            ("consumed request reopened", lambda request: request["selected_consumed_request_basis"].update({"consumed_request_reopened": True})),
            ("authorization token reused", lambda request: request.update({"authorization_token_reused": True})),
            ("command report current artifact", lambda request: request["selected_command_report_lineage_basis"].update({"command_report_lineage_basis_treated_as_current_report_artifact": True})),
            ("command report result authority", lambda request: request["selected_command_report_lineage_basis"].update({"command_report_lineage_basis_treated_as_command_result_authority": True})),
            ("command report command success", lambda request: request["selected_command_report_lineage_basis"].update({"command_report_lineage_basis_treated_as_command_success": True})),
            ("full prior artifact body", lambda request: request.update({"full_prior_artifact_body": RAW_FULL_BODY_SENTINEL})),
            ("artifacts mutated", lambda request: request.update({"prior_artifacts_mutated": True})),
            ("deployment created", lambda request: request.update({"deployment_created": True})),
            ("runtime hosting created", lambda request: request.update({"runtime_hosting_created": True})),
            ("public release created", lambda request: request.update({"public_release_created": True})),
            ("continuation authorized", lambda request: request.update({"continuation_authorized": True})),
            ("reusable permission", lambda request: request.update({"reusable_permission_created": True})),
            ("follow-on authorized", lambda request: request.update({"follow_on_work_authorized": True})),
            ("mutation performed", lambda request: request.update({"mutation_performed": True})),
            ("replay performed", lambda request: request.update({"replay_performed": True})),
            ("merge performed", lambda request: request.update({"merge_performed": True})),
            ("non-claim missing", lambda request: request.update({"declared_non_claims": {key: False for key in REQUIRED_FALSE_NON_CLAIMS[:-1]}})),
            ("non-claim flipped", lambda request: request["declared_non_claims"].update({"command_success_created": True})),
        )
        for label, mutator in cases:
            with self.subTest(label=label):
                result = _resolve(_copy_request_with(mutator))
                self.assertBlocked(result)
                if label == "full prior artifact body":
                    self.assertNotIn(RAW_FULL_BODY_SENTINEL, _json_text(result))

    def test_path_and_write_behavior_are_v2_scoped(self) -> None:
        request = _valid_request()
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            request_path = temp_root / "request.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")

            result = resolver.resolve_portable_source_body_verification_command_result_v2_from_path(
                request_path
            )
            self.assertRecorded(result)

            malformed_path = temp_root / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            self.assertBlocked(
                resolver.resolve_portable_source_body_verification_command_result_v2_from_path(
                    malformed_path
                )
            )

            array_path = temp_root / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            self.assertBlocked(
                resolver.resolve_portable_source_body_verification_command_result_v2_from_path(
                    array_path
                )
            )
            self.assertBlocked(
                resolver.resolve_portable_source_body_verification_command_result_v2_from_path(
                    temp_root / "missing.json"
                )
            )

            patched_output_root = (
                temp_root
                / "artifacts"
                / "integrity_host_v0_min_coexistence_portable_source_body_verification_command_result_v2"
            )
            with patch.object(resolver, "OUTPUT_ROOT", patched_output_root):
                output_path_1 = resolver.write_portable_source_body_verification_command_result_v2_result(
                    result
                )
                output_path_2 = resolver.write_portable_source_body_verification_command_result_v2_result(
                    result
                )
            self.assertTrue(output_path_1.exists())
            self.assertTrue(output_path_2.exists())
            self.assertNotEqual(output_path_1, output_path_2)
            written = json.loads(output_path_1.read_text(encoding="utf-8"))
            self.assertEqual(written["outcome"], RECORDED)
            self.assertEqual(
                written["portable_source_body_verification_command_result_metadata"]["result_version"],
                "0.2.0",
            )
            self.assertEqual(output_path_1.parent, patched_output_root)
            self.assertIn(
                "integrity_host_v0_min_coexistence_portable_source_body_verification_command_result_v2",
                output_path_1.parts,
            )
            self.assertNotIn(
                "integrity_host_v0_min_coexistence_portable_source_body_verification_command_result",
                output_path_1.parts,
            )

    def test_summary_helper_preserves_successor_lineage_and_non_claims(self) -> None:
        result = _resolve(_valid_request())
        self.assertRecorded(result)
        summary = resolver.build_portable_source_body_verification_command_result_v2_summary(result)
        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertEqual(summary["request_id"], "command_result_v2_reference_review_001")
        self.assertEqual(summary["question"], resolver.CORE_QUESTION)
        self.assertEqual(summary["intent"], resolver.INTENT_RECORD)
        self.assertEqual(summary["result_version"], "0.2.0")
        self.assertEqual(summary["successor_of"], "resolve_portable_source_body_verification_command_result")
        self.assertIn("OUTPUT_CAPTURE_TREATED_AS_RESULT", summary["successor_reason"])
        self.assertIs(summary["v1_predecessor_failure_preserved"], True)
        self.assertIs(summary["v1_repaired"], False)
        self.assertIs(summary["v1_hidden"], False)
        self.assertIs(summary["v1_claimed_passed"], False)
        self.assertIs(summary["v2_successor_does_not_erase_v1"], True)
        for key in (
            "command_result_recorded",
            "bounded_command_result_recorded",
            "command_result_boundary_basis_preserved",
            "command_output_report_artifact_basis_preserved",
            "report_body_absent_or_bounded",
            "result_body_absent_or_bounded",
            "report_body_not_invented",
            "result_body_not_invented",
            "command_success_still_not_created",
            "success_inference_blocked",
            "currentness_inference_blocked",
            "final_completion_inference_blocked",
            "public_readiness_inference_blocked",
            "deployment_readiness_inference_blocked",
            "unbounded_pass_fail_inference_blocked",
        ):
            self.assertIs(summary[key], True, key)
        self.assertIs(
            summary["output_capture_not_result_success_source_authority_currentness_final_completion"],
            True,
        )
        self.assertIs(summary["no_deployment_runtime_public_release"], True)
        self.assertIs(summary["no_continuation_publication_reusable_follow_on"], True)
        self.assertIs(summary["key_non_claims"]["follow_on_work_authorized"], False)

        blocked = _resolve(
            _copy_request_with(lambda request: request.update({"output_capture_treated_as_result": True}))
        )
        self.assertBlocked(blocked, "OUTPUT_CAPTURE_TREATED_AS_RESULT")
        blocked_summary = resolver.build_portable_source_body_verification_command_result_v2_summary(
            blocked
        )
        self.assertEqual(blocked_summary["outcome"], BLOCKED)
        self.assertEqual(blocked_summary["block_code"], "OUTPUT_CAPTURE_TREATED_AS_RESULT")
        self.assertEqual(blocked_summary["result_version"], "0.2.0")
        self.assertIs(blocked_summary["v1_predecessor_failure_preserved"], True)

    def test_builder_helper_and_non_mutation(self) -> None:
        request = _valid_request()
        built = resolver.build_declared_portable_source_body_verification_command_result_v2_request(
            command_result_request_id="builder_v2_request",
            **{key: request[key] for key in SELECTED_BASIS_KEYS},
        )
        built.update(
            {
                "command_result_payload": request["command_result_payload"],
                "requested_command_result_outcome": RECORDED,
            }
        )
        result = _resolve(built)
        self.assertRecorded(result)

        request = _valid_request()
        original_request = copy.deepcopy(request)
        selected_basis_originals = {key: copy.deepcopy(request[key]) for key in SELECTED_BASIS_KEYS}
        posture_originals = {key: copy.deepcopy(request[key]) for key in POSTURE_KEYS}
        payload_original = copy.deepcopy(request["command_result_payload"])
        scope_original = copy.deepcopy(request["command_result_scope"])

        result = _resolve(request)
        self.assertRecorded(result)
        self.assertEqual(request, original_request)
        for key, original in selected_basis_originals.items():
            self.assertEqual(request[key], original, key)
        for key, original in posture_originals.items():
            self.assertEqual(request[key], original, key)
        self.assertEqual(request["command_result_payload"], payload_original)
        self.assertEqual(request["command_result_scope"], scope_original)


if __name__ == "__main__":
    unittest.main()
