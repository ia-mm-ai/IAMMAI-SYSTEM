"""Tests for portable source-body verification command result only.

This suite is downstream of the recorded command result boundary. It proves
that one bounded command result may be recorded without creating command
success, inventing success body, inferring success, inferring currentness,
inferring final completion, inferring public readiness, inferring deployment
readiness, inferring unbounded pass/fail posture, source, authority,
continuation, reusable permission, derivative reception, vessel relation,
another reception request, deployment, runtime hosting, public release, or
follow-on work.
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

import resolve_portable_source_body_verification_command_result as resolver
from resolve_portable_source_body_verification_command_result import (
    build_declared_portable_source_body_verification_command_result_request,
    build_portable_source_body_verification_command_result_summary,
    resolve_portable_source_body_verification_command_result,
    resolve_portable_source_body_verification_command_result_from_path,
    write_portable_source_body_verification_command_result_result,
)


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}

QUESTION = resolver.CORE_QUESTION
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_COMMAND_RESULT_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
RAW_FULL_BODY_SENTINEL = "RAW_COMMAND_RESULT_BODY_MUST_NOT_RETURN_" * 8

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

SELECTED_BASIS_KEYS = tuple(resolver.SELECTED_BASIS_KEYS)
BLOCKING_SELECTED_BASIS_KEYS = tuple(
    key
    for key in SELECTED_BASIS_KEYS
    if key != "selected_command_output_report_artifact_boundary_terminal_summary_basis"
)
POSTURE_KEYS = tuple(resolver.POSTURE_KEYS)
RAW_BODY_KEYS = (
    "full_prior_artifact_body",
    "raw_full_prior_artifact_body",
    "prior_artifact_body",
    "embedded_prior_artifact",
    "embedded_prior_artifacts",
    "raw_artifact_body",
    "report_body",
    "result_body",
    "success_body",
    "source_body",
    "authority_body",
    "currentness_claim",
    "final_completion_claim",
    "stdout",
    "stderr",
    "process_output",
    "raw_output_body",
    "command_output_body",
    "output_body",
    "source_body_content",
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
        "basis_reference_shape_preserved": True,
        "basis_remains_basis_only": True,
        "basis_is_not_result": True,
        "basis_is_not_success": True,
        "basis_is_not_source": True,
        "basis_is_not_authority": True,
        "basis_is_not_currentness": True,
        "basis_is_not_final_completion": True,
        "basis_does_not_authorize_continuation_reusable_permission_follow_on_work": True,
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
        terminal_summary_preserves_v1_output_capture_failure=True,
        terminal_summary_preserves_full_upstream_lineage=True,
    )
    basis.update(overrides)
    return basis


def _posture(label: str, **overrides: Any) -> dict[str, Any]:
    posture: dict[str, Any] = {
        "posture_label": label,
        "declared": True,
        "posture_declared": True,
        "posture": label,
        "command_result_only": True,
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
        command_result_not_created=True,
        command_result_still_not_created=True,
        command_result_created=False,
        result_body_absent_or_bounded=True,
        result_body_not_invented=True,
        result_body_invented=False,
        command_success_not_created=True,
        command_success_still_not_created=True,
        command_success_created=False,
        pass_inference_made=False,
        fail_inference_made=False,
        pass_inference_blocked=True,
        fail_inference_blocked=True,
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
        command_output_report_artifact_boundary_basis_preserved=True,
        output_capture_v2_basis_preserved=True,
        output_capture_v1_predecessor_failure_preserved=True,
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
        "command_result_request_id": "command_result_reference_review_001",
        "command_result_question": QUESTION,
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
            v1_produced_clean_in_memory_law_result=True,
            v1_write_failed_on_frozenset_in_expected_posture=True,
            v1_remains_visible_predecessor_implementation_failure_evidence=True,
            v1_remains_visible_predecessor_failure_evidence=True,
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
            consumed_request_basis_recorded=True,
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
    return resolve_portable_source_body_verification_command_result(
        declared_command_result_request=request
    )


class CommandResultTests(unittest.TestCase):
    def assertRecordedResult(self, result: Mapping[str, Any]) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        metadata = result["portable_source_body_verification_command_result_metadata"]
        self.assertEqual(metadata["failed_check_count"], 0)
        self.assertGreater(metadata["passed_check_count"], 0)
        self.assertEqual(
            metadata["portable_source_body_verification_command_result_result_version"],
            "0.1.0",
        )
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_portable_source_body_verification_command_result",
        )
        self.assertIs(metadata["successor_lineage_preserved_in_selected_basis"], True)
        self.assertIs(metadata["short_resolver_filename_used_under_naming_containment"], True)
        self.assertIs(metadata["records_one_bounded_command_result"], True)
        self.assertIs(metadata["creates_command_success"], False)
        self.assertIs(metadata["invents_success_body"], False)
        self.assertIs(metadata["infers_success"], False)
        self.assertIs(metadata["infers_currentness"], False)
        self.assertIs(metadata["infers_final_completion"], False)
        self.assertIs(metadata["infers_public_readiness"], False)
        self.assertIs(metadata["infers_deployment_readiness"], False)
        self.assertIs(metadata["infers_unbounded_pass_fail"], False)
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)

        statement = result["command_result_statement"]
        for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIs(statement[key], True, key)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, result["non_claims"])
            self.assertIs(result["non_claims"][key], False, key)
            self.assertIs(statement[key], False, key)

    def assertBlocked(self, result: Mapping[str, Any]) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertTrue(result["block"]["blocked"])
        self.assertIsNotNone(result["block"]["block_code"])
        self.assertIn(result["block"]["block_code"], resolver.BLOCK_CODES)
        statement = result["command_result_statement"]
        self.assertIs(statement["command_success_created"], False)
        self.assertIs(statement["success_body_invented"], False)
        self.assertIs(statement["success_inference_made"], False)
        self.assertIs(statement["currentness_inference_made"], False)
        self.assertIs(statement["final_completion_inference_made"], False)
        self.assertIs(statement["public_readiness_inference_made"], False)
        self.assertIs(statement["deployment_readiness_inference_made"], False)
        self.assertIs(statement["unbounded_pass_fail_inference_made"], False)
        self.assertIs(result["non_claims"]["follow_on_work_authorized"], False)

    def test_public_api_and_constants_are_present(self) -> None:
        self.assertTrue(callable(resolve_portable_source_body_verification_command_result))
        self.assertTrue(callable(resolve_portable_source_body_verification_command_result_from_path))
        self.assertTrue(callable(write_portable_source_body_verification_command_result_result))
        self.assertTrue(callable(build_portable_source_body_verification_command_result_summary))
        self.assertTrue(callable(build_declared_portable_source_body_verification_command_result_request))
        self.assertEqual(
            {
                resolver.OUTCOME_RECORDED,
                resolver.OUTCOME_NOT_RECORDED,
                resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                resolver.OUTCOME_BLOCKED,
            },
            OUTCOME_FAMILY,
        )
        self.assertEqual(set(SUPPORTED_SCOPE), set(resolver.SUPPORTED_COMMAND_RESULT_SCOPE))
        self.assertIn("command_success_created", REQUIRED_FALSE_NON_CLAIMS)
        self.assertIn("success_body_invented", REQUIRED_FALSE_NON_CLAIMS)
        self.assertIn("success_inference_made", REQUIRED_FALSE_NON_CLAIMS)
        self.assertIn("currentness_inference_made", REQUIRED_FALSE_NON_CLAIMS)
        self.assertIn("final_completion_inference_made", REQUIRED_FALSE_NON_CLAIMS)

    def test_successful_recorded_result_preserves_command_result_only(self) -> None:
        result = _resolve(_valid_request())
        self.assertRecordedResult(result)

        boundary = result["selected_command_result_boundary_basis"]
        self.assertEqual(boundary["outcome"], resolver.COMMAND_RESULT_BOUNDARY_OUTCOME)
        self.assertEqual(boundary["failed_check_count"], 0)
        self.assertIs(boundary["one_future_command_result_step_declared"], True)
        self.assertIs(boundary["command_result_created"], False)
        self.assertIs(boundary["result_body_invented"], False)
        self.assertIs(boundary["command_success_created"], False)
        self.assertIs(boundary["pass_inference_made"], False)
        self.assertIs(boundary["fail_inference_made"], False)
        for key in (
            "command_result_boundary_treated_as_result",
            "command_result_boundary_treated_as_success",
            "command_result_boundary_treated_as_source",
            "command_result_boundary_treated_as_authority",
            "command_result_boundary_treated_as_currentness",
            "command_result_boundary_treated_as_final_completion",
        ):
            self.assertIs(boundary[key], False, key)

        checks = result["command_result_checks"]
        self.assertTrue(checks)
        self.assertTrue(all(check["passed"] is True for check in checks))
        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertIn("block_code", check)
            self.assertIn("failure_code", check)

        non_meaning = result["command_result_non_meaning"]
        self.assertIs(non_meaning["command_success_exists"], False)
        self.assertIs(non_meaning["success_body_exists"], False)
        self.assertIs(non_meaning["success_was_inferred"], False)
        self.assertIs(non_meaning["currentness_was_inferred"], False)
        self.assertIs(non_meaning["final_completion_was_inferred"], False)
        self.assertIs(non_meaning["public_readiness_was_inferred"], False)
        self.assertIs(non_meaning["deployment_readiness_was_inferred"], False)
        self.assertIs(non_meaning["follow_on_work_authorized"], False)

    def test_payload_preserves_absent_result_body_and_non_success_posture(self) -> None:
        result = _resolve(_valid_request())
        self.assertRecordedResult(result)
        payload = result["command_result_payload"]
        self.assertIs(payload["command_result_payload_recorded"], True)
        self.assertEqual(payload["payload_type"], "COMMAND_RESULT_BOUNDED")
        self.assertIs(payload["result_body_present"], False)
        self.assertIs(payload["result_body_absent_or_bounded"], True)
        self.assertIs(payload["result_body_invented"], False)
        self.assertIs(payload["report_body_absent_or_bounded"], True)
        self.assertIs(payload["report_body_invented"], False)
        self.assertIs(payload["success_body_invented"], False)
        self.assertIs(payload["command_success_created"], False)
        for key in (
            "success_inference_made",
            "currentness_inference_made",
            "final_completion_inference_made",
            "public_readiness_inference_made",
            "deployment_readiness_inference_made",
            "unbounded_pass_fail_inference_made",
            "stdout_content_invented",
            "stderr_content_invented",
            "process_output_content_invented",
            "raw_output_body_content_invented",
        ):
            self.assertIs(payload[key], False, key)
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

    def test_selected_basis_lineage_preserves_artifact_output_capture_and_execution(self) -> None:
        result = _resolve(_valid_request())
        self.assertRecordedResult(result)

        artifact = result["selected_command_output_report_artifact_basis"]
        self.assertEqual(artifact["outcome"], resolver.COMMAND_OUTPUT_REPORT_ARTIFACT_OUTCOME)
        self.assertEqual(artifact["failed_check_count"], 0)
        self.assertIs(artifact["bounded_command_output_report_artifact_recorded"], True)
        self.assertIs(artifact["report_body_absent_or_bounded"], True)
        self.assertIs(artifact["report_body_not_invented"], True)
        self.assertIs(artifact["report_body_invented"], False)
        self.assertIs(artifact["command_success_created"], False)
        for key in (
            "command_output_report_artifact_treated_as_result_authority",
            "command_output_report_artifact_treated_as_success",
            "command_output_report_artifact_treated_as_source",
            "command_output_report_artifact_treated_as_authority",
            "command_output_report_artifact_treated_as_currentness",
            "command_output_report_artifact_treated_as_final_completion",
        ):
            self.assertIs(artifact[key], False, key)

        artifact_boundary = result["selected_command_output_report_artifact_boundary_basis"]
        self.assertEqual(
            artifact_boundary["outcome"],
            resolver.COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_OUTCOME,
        )
        self.assertEqual(artifact_boundary["failed_check_count"], 0)
        self.assertIs(
            artifact_boundary["one_future_command_output_report_artifact_step_declared"],
            True,
        )
        self.assertIs(artifact_boundary["command_result_created"], False)
        self.assertIs(artifact_boundary["command_success_created"], False)

        output_capture_v2 = result["selected_output_capture_v2_basis"]
        self.assertEqual(output_capture_v2["outcome"], resolver.OUTPUT_CAPTURE_V2_OUTCOME)
        self.assertEqual(output_capture_v2["result_version"], "0.2.0")
        self.assertEqual(output_capture_v2["failed_check_count"], 0)
        self.assertIs(output_capture_v2["json_safe_result"], True)
        self.assertIs(output_capture_v2["v1_predecessor_failure_preserved"], True)
        self.assertIs(output_capture_v2["v1_repaired"], False)
        self.assertIs(output_capture_v2["v1_hidden"], False)
        self.assertIs(output_capture_v2["v1_claimed_passed"], False)
        self.assertIs(output_capture_v2["v2_successor_does_not_erase_v1"], True)
        for key in (
            "stdout_content_invented",
            "stderr_content_invented",
            "process_output_content_invented",
            "raw_output_body_content_invented",
        ):
            self.assertIs(output_capture_v2[key], False, key)

        self.assertEqual(result["selected_command_output_basis"]["outcome"], resolver.COMMAND_OUTPUT_OUTCOME)
        self.assertEqual(
            result["selected_post_invocation_command_execution_basis"]["outcome"],
            resolver.POST_INVOCATION_COMMAND_EXECUTION_OUTCOME,
        )
        self.assertIs(
            result["selected_post_invocation_command_execution_basis"]["execution_trace_audit_only"],
            True,
        )
        self.assertIs(
            result["selected_consumed_request_basis"]["consumed_request_token_remains_closed"],
            True,
        )
        self.assertIs(
            result["selected_older_command_execution_boundary_lineage_basis"][
                "older_command_execution_boundary_lineage_treated_as_current_execution"
            ],
            False,
        )
        command_report = result["selected_command_report_lineage_basis"]
        self.assertIs(command_report["command_report_lineage_basis_treated_as_current_report_artifact"], False)
        self.assertIs(command_report["command_report_lineage_basis_treated_as_command_result_authority"], False)
        self.assertIs(command_report["command_report_lineage_basis_treated_as_command_success"], False)

    def test_path_resolution_and_json_writing_are_bounded(self) -> None:
        request = _valid_request()
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            request_path = temp_root / "request.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")

            result = resolve_portable_source_body_verification_command_result_from_path(
                request_path
            )
            self.assertRecordedResult(result)

            malformed_path = temp_root / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            self.assertBlocked(
                resolve_portable_source_body_verification_command_result_from_path(
                    malformed_path
                )
            )

            array_path = temp_root / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            self.assertBlocked(
                resolve_portable_source_body_verification_command_result_from_path(
                    array_path
                )
            )

            self.assertBlocked(
                resolve_portable_source_body_verification_command_result_from_path(
                    temp_root / "missing.json"
                )
            )

            patched_output_root = (
                temp_root
                / "artifacts"
                / "integrity_host_v0_min_coexistence_portable_source_body_verification_command_result"
            )
            with patch.object(resolver, "OUTPUT_ROOT", patched_output_root):
                output_path_1 = write_portable_source_body_verification_command_result_result(
                    result
                )
                output_path_2 = write_portable_source_body_verification_command_result_result(
                    result
                )
            self.assertTrue(output_path_1.exists())
            self.assertTrue(output_path_2.exists())
            self.assertNotEqual(output_path_1, output_path_2)
            self.assertEqual(json.loads(output_path_1.read_text(encoding="utf-8"))["outcome"], RECORDED)
            self.assertEqual(output_path_1.parent, patched_output_root)
            self.assertIn(
                "integrity_host_v0_min_coexistence_portable_source_body_verification_command_result",
                output_path_1.parts,
            )
            forbidden_roots = {
                "integrity_host_v0_min_coexistence_portable_source_body_verification_command_result_boundary",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_command_output_report_artifact",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_command_output_report_artifact_boundary",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_output_capture_v2",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_command_output",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_command_report",
            }
            self.assertTrue(forbidden_roots.isdisjoint(output_path_1.parts))

    def test_not_recorded_and_requires_additional_basis_outcomes_are_bounded(self) -> None:
        not_recorded = _resolve(
            _copy_request_with(
                lambda request: request.update(
                    {
                        "command_result_intent": resolver.INTENT_DO_NOT_RECORD,
                        "requested_command_result_outcome": NOT_RECORDED,
                        "not_recorded_basis": {
                            "readable_basis_failed_review": True,
                            "creates_command_success": False,
                            "infers_success": False,
                        },
                    }
                )
            )
        )
        self.assertEqual(not_recorded["outcome"], NOT_RECORDED)
        self.assertIs(not_recorded["not_recorded_basis"]["not_recorded"], True)
        self.assertIs(not_recorded["command_result_statement"]["command_success_created"], False)
        self.assertIs(not_recorded["command_result_statement"]["success_inference_made"], False)
        self.assertIs(not_recorded["command_result_statement"]["currentness_inference_made"], False)

        requires = _resolve(
            _copy_request_with(
                lambda request: request.update(
                    {
                        "requested_command_result_outcome": REQUIRES_ADDITIONAL_BASIS,
                        "additional_basis_context": {
                            "result_body_absent_or_bounded_posture_needs_more_basis": True,
                            "missing_basis_is_not_authorized": True,
                        },
                    }
                )
            )
        )
        self.assertEqual(requires["outcome"], REQUIRES_ADDITIONAL_BASIS)
        self.assertIs(requires["additional_basis_required"]["additional_basis_required"], True)
        self.assertIs(requires["additional_basis_required"]["missing_basis_is_not_scheduled"], True)
        self.assertIs(requires["additional_basis_required"]["missing_basis_is_not_authorized"], True)
        self.assertIs(requires["additional_basis_required"]["missing_basis_is_not_executed"], True)
        self.assertIs(requires["additional_basis_required"]["creates_command_success"], False)
        self.assertIs(requires["additional_basis_required"]["authorizes_follow_on_work"], False)

    def test_blocking_request_boundary_and_scope_cases(self) -> None:
        self.assertBlocked(resolve_portable_source_body_verification_command_result(None))
        self.assertBlocked(
            resolve_portable_source_body_verification_command_result(
                declared_command_result_request=[]
            )
        )
        cases: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
            ("explicit block intent", lambda request: request.update({"command_result_intent": resolver.INTENT_BLOCK})),
            ("unsupported intent", lambda request: request.update({"command_result_intent": "UNSUPPORTED"})),
            ("unsupported scope", lambda request: request.update({"command_result_scope": ["UNSUPPORTED_SCOPE"]})),
            ("missing question", lambda request: request.update({"command_result_question": ""})),
            ("missing boundary basis", lambda request: request.update({"selected_command_result_boundary_basis": {}})),
            ("boundary not recorded", lambda request: request["selected_command_result_boundary_basis"].update({"outcome": "NOT_RECORDED"})),
            ("boundary failed checks", lambda request: request["selected_command_result_boundary_basis"].update({"failed_check_count": 1})),
            ("boundary step not declared", lambda request: request["selected_command_result_boundary_basis"].update({"one_future_command_result_step_declared": False})),
            ("boundary created result body", lambda request: request["selected_command_result_boundary_basis"].update({"result_body_invented": True})),
            ("boundary result body invention not false", lambda request: request["selected_command_result_boundary_basis"].update({"result_body_not_invented": False})),
            ("boundary created success", lambda request: request["selected_command_result_boundary_basis"].update({"command_success_created": True})),
            ("boundary inferred pass", lambda request: request["selected_command_result_boundary_basis"].update({"pass_inference_made": True})),
            ("boundary inferred fail", lambda request: request["selected_command_result_boundary_basis"].update({"fail_inference_made": True})),
        )
        for label, mutator in cases:
            with self.subTest(label=label):
                self.assertBlocked(_resolve(_copy_request_with(mutator)))

    def test_blocking_artifact_report_and_payload_collapse_cases(self) -> None:
        cases: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
            ("missing artifact basis", lambda request: request.update({"selected_command_output_report_artifact_basis": {}})),
            ("artifact not recorded", lambda request: request["selected_command_output_report_artifact_basis"].update({"outcome": "NOT_RECORDED"})),
            ("artifact failed checks", lambda request: request["selected_command_output_report_artifact_basis"].update({"failed_check_count": 1})),
            ("artifact not bounded", lambda request: request["selected_command_output_report_artifact_basis"].update({"bounded_command_output_report_artifact_recorded": False})),
            ("artifact invented report body", lambda request: request["selected_command_output_report_artifact_basis"].update({"report_body_invented": True})),
            ("artifact created success", lambda request: request["selected_command_output_report_artifact_basis"].update({"command_success_created": True})),
            ("artifact treated as result authority", lambda request: request.update({"command_output_report_artifact_treated_as_result_authority": True})),
            ("artifact treated as success", lambda request: request.update({"command_output_report_artifact_treated_as_success": True})),
            ("artifact treated as source", lambda request: request.update({"command_output_report_artifact_treated_as_source": True})),
            ("artifact treated as authority", lambda request: request.update({"command_output_report_artifact_treated_as_authority": True})),
            ("artifact treated as currentness", lambda request: request.update({"command_output_report_artifact_treated_as_currentness": True})),
            ("artifact treated as final completion", lambda request: request.update({"command_output_report_artifact_treated_as_final_completion": True})),
            ("report body treated as result authority", lambda request: request.update({"report_body_treated_as_result_authority": True})),
            ("report body treated as success", lambda request: request.update({"report_body_treated_as_success": True})),
            ("report body treated as source", lambda request: request.update({"report_body_treated_as_source": True})),
            ("report body treated as authority", lambda request: request.update({"report_body_treated_as_authority": True})),
            ("report body treated as currentness", lambda request: request.update({"report_body_treated_as_currentness": True})),
            ("report body treated as final completion", lambda request: request.update({"report_body_treated_as_final_completion": True})),
            ("result treated as success", lambda request: request.update({"command_result_treated_as_success": True})),
            ("result treated as source", lambda request: request.update({"command_result_treated_as_source": True})),
            ("result treated as authority", lambda request: request.update({"command_result_treated_as_authority": True})),
            ("result treated as currentness", lambda request: request.update({"command_result_treated_as_currentness": True})),
            ("result treated as final completion", lambda request: request.update({"command_result_treated_as_final_completion": True})),
            ("result treated as public readiness", lambda request: request.update({"command_result_treated_as_public_readiness": True})),
            ("result treated as deployment readiness", lambda request: request.update({"command_result_treated_as_deployment_readiness": True})),
            ("result body invented", lambda request: request.update({"result_body_invented": True})),
            ("success created", lambda request: request.update({"command_success_created": True})),
            ("success inferred", lambda request: request.update({"success_inference_made": True})),
            ("currentness inferred", lambda request: request.update({"currentness_inference_made": True})),
            ("final completion inferred", lambda request: request.update({"final_completion_inference_made": True})),
            ("public readiness inferred", lambda request: request.update({"public_readiness_inference_made": True})),
            ("deployment readiness inferred", lambda request: request.update({"deployment_readiness_inference_made": True})),
            ("unbounded pass/fail inferred", lambda request: request.update({"unbounded_pass_fail_inference_made": True})),
        )
        for label, mutator in cases:
            with self.subTest(label=label):
                self.assertBlocked(_resolve(_copy_request_with(mutator)))

    def test_blocking_output_capture_v2_cases(self) -> None:
        cases: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
            ("missing output capture v2 basis", lambda request: request.update({"selected_output_capture_v2_basis": {}})),
            ("output capture v2 not recorded", lambda request: request["selected_output_capture_v2_basis"].update({"outcome": "NOT_RECORDED"})),
            ("output capture v2 failed checks", lambda request: request["selected_output_capture_v2_basis"].update({"failed_check_count": 1})),
            ("output capture v2 wrong version", lambda request: request["selected_output_capture_v2_basis"].update({"result_version": "0.1.0"})),
            ("output capture v2 not JSON safe", lambda request: request["selected_output_capture_v2_basis"].update({"json_safe_result": False})),
            ("output capture v2 predecessor failure missing", lambda request: request["selected_output_capture_v2_basis"].update({"v1_predecessor_failure_preserved": False})),
            ("output capture v2 repaired v1", lambda request: request["selected_output_capture_v2_basis"].update({"v1_repaired": True})),
            ("output capture v2 hid v1", lambda request: request["selected_output_capture_v2_basis"].update({"v1_hidden": True})),
            ("output capture v2 claimed v1 passed", lambda request: request["selected_output_capture_v2_basis"].update({"v1_claimed_passed": True})),
            ("output capture v2 erased v1", lambda request: request["selected_output_capture_v2_basis"].update({"v2_successor_does_not_erase_v1": False})),
            ("output capture v2 invented stdout", lambda request: request["selected_output_capture_v2_basis"].update({"stdout_content_invented": True})),
            ("output capture v2 invented stderr", lambda request: request["selected_output_capture_v2_basis"].update({"stderr_content_invented": True})),
            ("output capture v2 invented process output", lambda request: request["selected_output_capture_v2_basis"].update({"process_output_content_invented": True})),
            ("output capture v2 invented raw output body", lambda request: request["selected_output_capture_v2_basis"].update({"raw_output_body_content_invented": True})),
            ("output capture treated as result", lambda request: request.update({"output_capture_treated_as_result": True})),
            ("output capture treated as success", lambda request: request.update({"output_capture_treated_as_success": True})),
            ("output capture treated as source", lambda request: request.update({"output_capture_treated_as_source": True})),
            ("output capture treated as authority", lambda request: request.update({"output_capture_treated_as_authority": True})),
            ("output capture treated as currentness", lambda request: request.update({"output_capture_treated_as_currentness": True})),
            ("output capture treated as final completion", lambda request: request.update({"output_capture_treated_as_final_completion": True})),
        )
        for label, mutator in cases:
            with self.subTest(label=label):
                self.assertBlocked(_resolve(_copy_request_with(mutator)))

    def test_blocking_missing_basis_posture_and_non_claim_sections(self) -> None:
        for key in BLOCKING_SELECTED_BASIS_KEYS:
            with self.subTest(missing_basis=key):
                self.assertBlocked(_resolve(_copy_request_with(lambda request, key=key: request.update({key: {}}))))
        for key in POSTURE_KEYS:
            with self.subTest(missing_posture=key):
                self.assertBlocked(_resolve(_copy_request_with(lambda request, key=key: request.update({key: {}}))))
        self.assertBlocked(
            _resolve(
                _copy_request_with(
                    lambda request: request.update(
                        {"declared_non_claims": {key: False for key in REQUIRED_FALSE_NON_CLAIMS[:-1]}}
                    )
                )
            )
        )
        self.assertBlocked(
            _resolve(
                _copy_request_with(
                    lambda request: request["declared_non_claims"].update({"command_success_created": True})
                )
            )
        )

    def test_blocking_prior_lineage_execution_and_token_cases(self) -> None:
        cases: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
            ("missing output capture boundary", lambda request: request.update({"selected_output_capture_boundary_basis": {}})),
            ("missing command output", lambda request: request.update({"selected_command_output_basis": {}})),
            ("missing post invocation", lambda request: request.update({"selected_post_invocation_command_execution_basis": {}})),
            ("post invocation not recorded", lambda request: request["selected_post_invocation_command_execution_basis"].update({"outcome": "NOT_RECORDED"})),
            ("post invocation failed checks", lambda request: request["selected_post_invocation_command_execution_basis"].update({"failed_check_count": 1})),
            ("post invocation trace not audit only", lambda request: request["selected_post_invocation_command_execution_basis"].update({"execution_trace_audit_only": False})),
            ("execution trace treated as result", lambda request: request.update({"execution_trace_treated_as_result": True})),
            ("execution trace treated as success", lambda request: request.update({"execution_trace_treated_as_success": True})),
            ("execution trace treated as source", lambda request: request.update({"execution_trace_treated_as_source": True})),
            ("execution trace treated as authority", lambda request: request.update({"execution_trace_treated_as_authority": True})),
            ("success treated as currentness", lambda request: request.update({"command_success_created_currentness": True})),
            ("success treated as final completion", lambda request: request.update({"command_success_claimed_final_completion": True})),
            ("consumed request reopened", lambda request: request["selected_consumed_request_basis"].update({"consumed_request_reopened": True})),
            ("authorization token reused", lambda request: request.update({"authorization_token_reused": True})),
            ("v2 admitted request failed checks", lambda request: request["selected_v2_admitted_request_basis"].update({"failed_check_count": 1})),
            ("earlier v2 repaired v1 admission", lambda request: request.update({"v2_treated_as_repairing_v1_request_admission": True})),
            ("earlier v1 request-admission hidden", lambda request: request.update({"v1_request_admission_failure_hidden": True})),
            ("earlier v1 request-admission claimed passed", lambda request: request.update({"v1_request_admission_claimed_passed": True})),
            ("older boundary lineage current execution", lambda request: request["selected_older_command_execution_boundary_lineage_basis"].update({"older_command_execution_boundary_lineage_treated_as_current_execution": True})),
            ("command report lineage current report artifact", lambda request: request["selected_command_report_lineage_basis"].update({"command_report_lineage_basis_treated_as_current_report_artifact": True})),
            ("command report lineage command result authority", lambda request: request["selected_command_report_lineage_basis"].update({"command_report_lineage_basis_treated_as_command_result_authority": True})),
            ("command report lineage command success", lambda request: request["selected_command_report_lineage_basis"].update({"command_report_lineage_basis_treated_as_command_success": True})),
        )
        for label, mutator in cases:
            with self.subTest(label=label):
                self.assertBlocked(_resolve(_copy_request_with(mutator)))

    def test_blocking_overreach_mutation_deployment_and_follow_on_flags(self) -> None:
        overreach_fields = (
            "raw_full_prior_artifact_body_returned",
            "full_prior_artifacts_embedded",
            "prior_artifacts_mutated",
            "deployment_created",
            "runtime_hosting_created",
            "public_release_created",
            "operation_permission_created",
            "public_launch_readiness_created",
            "final_completion_claimed",
            "continuation_authorized",
            "reusable_permission_created",
            "derivative_reception_authorized",
            "vessel_relation_authorized",
            "another_reception_request_authorized",
            "follow_on_work_authorized",
            "mutation_performed",
            "replay_performed",
            "merge_performed",
        )
        for field in overreach_fields:
            with self.subTest(overreach_field=field):
                self.assertBlocked(
                    _resolve(_copy_request_with(lambda request, field=field: request.update({field: True})))
                )

    def test_raw_full_prior_artifact_body_blocks_without_returning_body(self) -> None:
        result = _resolve(
            _copy_request_with(
                lambda request: request.update({"full_prior_artifact_body": RAW_FULL_BODY_SENTINEL})
            )
        )
        self.assertBlocked(result)
        self.assertNotIn(RAW_FULL_BODY_SENTINEL, _json_text(result))
        self.assertEqual(result["block"]["block_code"], "FULL_PRIOR_ARTIFACT_BODY_EMITTED")

    def test_input_selected_basis_payload_posture_and_scope_are_not_mutated(self) -> None:
        request = _valid_request()
        original_request = copy.deepcopy(request)
        selected_basis_originals = {key: copy.deepcopy(request[key]) for key in SELECTED_BASIS_KEYS}
        posture_originals = {key: copy.deepcopy(request[key]) for key in POSTURE_KEYS}
        payload_original = copy.deepcopy(request["command_result_payload"])
        scope_original = copy.deepcopy(request["command_result_scope"])

        result = _resolve(request)
        self.assertRecordedResult(result)
        self.assertEqual(request, original_request)
        for key, original in selected_basis_originals.items():
            self.assertEqual(request[key], original, key)
        for key, original in posture_originals.items():
            self.assertEqual(request[key], original, key)
        self.assertEqual(request["command_result_payload"], payload_original)
        self.assertEqual(request["command_result_scope"], scope_original)

    def test_summary_and_builder_preserve_short_name_lineage_and_non_claims(self) -> None:
        request = _valid_request()
        built = build_declared_portable_source_body_verification_command_result_request(
            command_result_request_id="builder_request",
            selected_command_result_boundary_basis=request["selected_command_result_boundary_basis"],
            selected_command_result_boundary_terminal_summary_basis=request[
                "selected_command_result_boundary_terminal_summary_basis"
            ],
            selected_command_output_report_artifact_basis=request[
                "selected_command_output_report_artifact_basis"
            ],
            selected_command_output_report_artifact_terminal_summary_basis=request[
                "selected_command_output_report_artifact_terminal_summary_basis"
            ],
            selected_command_output_report_artifact_boundary_basis=request[
                "selected_command_output_report_artifact_boundary_basis"
            ],
            selected_command_output_report_artifact_boundary_terminal_summary_basis=request[
                "selected_command_output_report_artifact_boundary_terminal_summary_basis"
            ],
            selected_output_capture_v2_basis=request["selected_output_capture_v2_basis"],
            selected_output_capture_v2_terminal_summary_basis=request[
                "selected_output_capture_v2_terminal_summary_basis"
            ],
            selected_output_capture_v1_predecessor_failure_basis=request[
                "selected_output_capture_v1_predecessor_failure_basis"
            ],
            selected_output_capture_boundary_basis=request["selected_output_capture_boundary_basis"],
            selected_command_output_basis=request["selected_command_output_basis"],
            selected_command_output_boundary_basis=request["selected_command_output_boundary_basis"],
            selected_command_output_containment_basis=request["selected_command_output_containment_basis"],
            selected_post_invocation_command_execution_basis=request[
                "selected_post_invocation_command_execution_basis"
            ],
            selected_post_invocation_command_execution_terminal_summary_basis=request[
                "selected_post_invocation_command_execution_terminal_summary_basis"
            ],
            selected_command_invocation_basis=request["selected_command_invocation_basis"],
            selected_command_execution_review_basis=request["selected_command_execution_review_basis"],
            selected_request_consumption_basis=request["selected_request_consumption_basis"],
            selected_consumed_request_basis=request["selected_consumed_request_basis"],
            selected_v2_admitted_request_basis=request["selected_v2_admitted_request_basis"],
            selected_v1_predecessor_failure_basis=request["selected_v1_predecessor_failure_basis"],
            selected_older_command_execution_boundary_lineage_basis=request[
                "selected_older_command_execution_boundary_lineage_basis"
            ],
            selected_command_report_lineage_basis=request["selected_command_report_lineage_basis"],
            selected_command_implementation_boundary_basis=request[
                "selected_command_implementation_boundary_basis"
            ],
            selected_command_boundary_basis=request["selected_command_boundary_basis"],
            selected_artifact_emission_containment_basis=request[
                "selected_artifact_emission_containment_basis"
            ],
            selected_evidence_manifest_basis=request["selected_evidence_manifest_basis"],
            selected_portable_verification_basis=request["selected_portable_verification_basis"],
        )
        built.update(
            {
                "command_result_payload": request["command_result_payload"],
                "requested_command_result_outcome": RECORDED,
            }
        )
        result = _resolve(built)
        self.assertRecordedResult(result)
        summary = build_portable_source_body_verification_command_result_summary(result)
        self.assertEqual(summary["outcome"], RECORDED)
        self.assertEqual(summary["request_id"], "builder_request")
        self.assertIs(summary["command_result_recorded"], True)
        self.assertIs(summary["bounded_command_result_recorded"], True)
        self.assertIs(summary["command_result_boundary_basis_preserved"], True)
        self.assertIs(summary["command_output_report_artifact_basis_preserved"], True)
        self.assertIs(summary["bounded_command_output_report_artifact_preserved"], True)
        self.assertIs(summary["report_body_absent_or_bounded"], True)
        self.assertIs(summary["result_body_absent_or_bounded"], True)
        self.assertIs(summary["report_body_not_invented"], True)
        self.assertIs(summary["result_body_not_invented"], True)
        self.assertIs(summary["command_success_still_not_created"], True)
        self.assertIs(summary["success_inference_blocked"], True)
        self.assertIs(summary["currentness_inference_blocked"], True)
        self.assertIs(summary["final_completion_inference_blocked"], True)
        self.assertIs(summary["public_readiness_inference_blocked"], True)
        self.assertIs(summary["deployment_readiness_inference_blocked"], True)
        self.assertIs(summary["unbounded_pass_fail_inference_blocked"], True)
        self.assertIs(summary["command_report_lineage_not_current_report_artifact"], True)
        self.assertIs(summary["command_report_lineage_not_command_result_authority"], True)
        self.assertIs(summary["command_report_lineage_not_command_success"], True)
        self.assertIs(summary["key_non_claims"]["follow_on_work_authorized"], False)


if __name__ == "__main__":
    unittest.main()
