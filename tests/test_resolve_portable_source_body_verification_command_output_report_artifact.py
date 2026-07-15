"""Tests for command output/report artifact only.

This suite is downstream of the recorded command output/report artifact
boundary. It proves that one bounded command output/report artifact posture may
be recorded without inventing report body, creating command result, creating
command success, source, authority, currentness, final completion, deployment,
continuation, reusable permission, derivative reception, vessel relation,
another reception request, or follow-on work.
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

import resolve_portable_source_body_verification_command_output_report_artifact as resolver
from resolve_portable_source_body_verification_command_output_report_artifact import (
    build_declared_portable_source_body_verification_command_output_report_artifact_request,
    build_portable_source_body_verification_command_output_report_artifact_summary,
    resolve_portable_source_body_verification_command_output_report_artifact,
    resolve_portable_source_body_verification_command_output_report_artifact_from_path,
    write_portable_source_body_verification_command_output_report_artifact_result,
)


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}

QUESTION = resolver.CORE_QUESTION
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_COMMAND_OUTPUT_REPORT_ARTIFACT_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
RAW_FULL_BODY_SENTINEL = "RAW_COMMAND_OUTPUT_REPORT_ARTIFACT_BODY_MUST_NOT_RETURN_" * 6

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_command_output_report_artifact_metadata",
    "declared_command_output_report_artifact_question",
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
    "command_output_report_artifact_only_posture",
    "one_bounded_command_output_report_artifact_posture",
    "command_output_report_artifact_boundary_basis_preserved_posture",
    "output_capture_v2_basis_preserved_posture",
    "output_capture_v1_predecessor_failure_preserved_posture",
    "bounded_output_capture_event_preserved_posture",
    "command_output_basis_preserved_posture",
    "execution_trace_audit_only_posture",
    "report_body_absent_or_bounded_posture",
    "no_report_body_invented_posture",
    "no_command_result_posture",
    "no_command_success_posture",
    "no_artifact_as_source_posture",
    "no_result_as_authority_posture",
    "no_success_as_currentness_posture",
    "no_final_completion_posture",
    "authorization_token_reuse_blocked_posture",
    "consumed_token_closed_posture",
    "no_reopen_consumed_request_posture",
    "returned_result_containment_posture",
    "command_output_report_artifact_scope",
    "command_output_report_artifact_checks",
    "command_output_report_artifact_statement",
    "command_output_report_artifact_non_meaning",
    "command_output_report_artifact_payload",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_command_output_report_artifact_summary",
)

SELECTED_BASIS_KEYS = tuple(resolver.SELECTED_BASIS_KEYS)
POSTURE_KEYS = tuple(resolver.POSTURE_KEYS)
RAW_BODY_KEYS = (
    "report_body",
    "stdout",
    "stderr",
    "process_output",
    "raw_output_body",
    "command_output_body",
    "result_body",
    "success_body",
    "source_body",
    "authority_body",
    "currentness_claim",
    "final_completion_claim",
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
        "report_body_invented": False,
        "command_output_report_artifact_created": False,
        "report_artifact_created": False,
        "report_body_created": False,
        "command_result_created": False,
        "command_success_created": False,
        "command_output_report_artifact_treated_as_result": False,
        "command_output_report_artifact_treated_as_success": False,
        "command_output_report_artifact_treated_as_source": False,
        "command_output_report_artifact_treated_as_authority": False,
        "command_output_report_artifact_treated_as_currentness": False,
        "command_output_report_artifact_treated_as_final_completion": False,
        "report_artifact_treated_as_result": False,
        "report_artifact_treated_as_success": False,
        "report_artifact_treated_as_source": False,
        "report_artifact_treated_as_authority": False,
        "report_artifact_treated_as_currentness": False,
        "report_artifact_treated_as_final_completion": False,
        "report_body_treated_as_result": False,
        "report_body_treated_as_success": False,
        "report_body_treated_as_source": False,
        "report_body_treated_as_authority": False,
        "report_body_treated_as_currentness": False,
        "report_body_treated_as_final_completion": False,
        "output_capture_treated_as_result": False,
        "output_capture_treated_as_success": False,
        "output_capture_treated_as_source": False,
        "output_capture_treated_as_authority": False,
        "output_capture_treated_as_currentness": False,
        "output_capture_treated_as_final_completion": False,
        "execution_trace_treated_as_report_artifact": False,
        "execution_trace_treated_as_result": False,
        "execution_trace_treated_as_success": False,
        "execution_trace_treated_as_source": False,
        "execution_trace_treated_as_authority": False,
        "command_result_became_authority": False,
        "command_success_created_currentness": False,
        "command_success_claimed_final_completion": False,
        "authorization_token_reused": False,
        "consumed_request_reopened": False,
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


def _terminal_summary_basis(label: str, **overrides: Any) -> dict[str, Any]:
    basis = _reference_basis(
        label,
        terminal_summary_declared=True,
        terminal_summary_path=f"spec/{label}.md",
        terminal_summary_remains_readability_basis_only=True,
        readability_basis_only=True,
        terminal_summary_preserves_v1_output_capture_failure=True,
        terminal_summary_does_not_repair_v1=True,
        terminal_summary_does_not_hide_v1=True,
        terminal_summary_does_not_claim_v1_passed=True,
        terminal_summary_does_not_create_report_artifact=True,
        terminal_summary_does_not_create_report_body=True,
        terminal_summary_does_not_invent_report_body=True,
        terminal_summary_does_not_create_command_result=True,
        terminal_summary_does_not_create_command_success=True,
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
        "command_output_report_artifact_only": True,
        "one_bounded_command_output_report_artifact_recorded": True,
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
        "report_body_invented": False,
        "report_body_not_invented": True,
        "command_result_created": False,
        "command_result_not_created": True,
        "command_result_still_not_created": True,
        "command_success_created": False,
        "command_success_not_created": True,
        "command_success_still_not_created": True,
        "command_output_report_artifact_treated_as_result": False,
        "command_output_report_artifact_treated_as_success": False,
        "command_output_report_artifact_treated_as_source": False,
        "command_output_report_artifact_treated_as_authority": False,
        "command_output_report_artifact_treated_as_currentness": False,
        "command_output_report_artifact_treated_as_final_completion": False,
        "report_body_treated_as_result": False,
        "report_body_treated_as_success": False,
        "report_body_treated_as_source": False,
        "report_body_treated_as_authority": False,
        "report_body_treated_as_currentness": False,
        "report_body_treated_as_final_completion": False,
        "output_capture_treated_as_result": False,
        "output_capture_treated_as_success": False,
        "output_capture_treated_as_source": False,
        "output_capture_treated_as_authority": False,
        "output_capture_treated_as_currentness": False,
        "output_capture_treated_as_final_completion": False,
        "execution_trace_treated_as_report_artifact": False,
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
        "full_prior_artifacts_embedded": False,
        "prior_artifacts_mutated": False,
    }
    posture.update(overrides)
    return posture


def _boundary_basis(**overrides: Any) -> dict[str, Any]:
    basis = _reference_basis(
        "command_output_report_artifact_boundary",
        outcome=resolver.COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_OUTCOME,
        failed_check_count=0,
        passed_check_count=125,
        one_future_command_output_report_artifact_step_declared=True,
        output_capture_v2_basis_preserved=True,
        output_capture_v1_predecessor_failure_preserved=True,
        report_artifact_not_created=True,
        report_artifact_created=False,
        report_body_not_created=True,
        report_body_created=False,
        report_body_not_invented=True,
        report_body_invented=False,
        command_result_not_created=True,
        command_result_created=False,
        command_success_not_created=True,
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
        successor_metadata_preserved=True,
        successor_of="resolve_portable_source_body_verification_output_capture",
        successor_reason=(
            "v1 produced clean in-memory output-capture resolution but failed "
            "JSON writing because expected_posture contained frozenset"
        ),
        v1_predecessor_failure_preserved=True,
        v1_repaired=False,
        v1_hidden=False,
        v1_claimed_passed=False,
        v2_successor_does_not_erase_v1=True,
        output_capture_event_recorded=True,
        bounded_output_capture_event_recorded=True,
        stdout_content_invented=False,
        stderr_content_invented=False,
        process_output_content_invented=False,
        raw_output_body_content_invented=False,
        command_output_report_artifact_created=False,
        report_artifact_created=False,
        command_result_created=False,
        command_success_created=False,
        output_capture_v2_remains_output_capture_posture_only=True,
    )
    basis.update(overrides)
    return basis


def _payload(**overrides: Any) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "command_output_report_artifact_payload_recorded": True,
        "payload_type": "COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDED",
        "report_body_present": False,
        "report_body_absent_or_bounded": True,
        "report_body_invented": False,
        "stdout_content_invented": False,
        "stderr_content_invented": False,
        "process_output_content_invented": False,
        "raw_output_body_content_invented": False,
        "command_output_body_invented": False,
        "result_body_invented": False,
        "success_body_invented": False,
        "source_body_invented": False,
        "authority_body_invented": False,
        "currentness_claim_created": False,
        "final_completion_claim_created": False,
        "command_result_created": False,
        "command_success_created": False,
        "command_output_report_artifact_is_not_result": True,
        "command_output_report_artifact_is_not_success": True,
        "command_output_report_artifact_is_not_source": True,
        "command_output_report_artifact_is_not_authority": True,
        "command_output_report_artifact_is_not_currentness": True,
        "command_output_report_artifact_is_not_final_completion": True,
    }
    payload.update(overrides)
    return payload


def _valid_request(**overrides: Any) -> dict[str, Any]:
    request: dict[str, Any] = {
        "command_output_report_artifact_request_id": (
            "command_output_report_artifact_reference_review_001"
        ),
        "command_output_report_artifact_question": QUESTION,
        "command_output_report_artifact_intent": resolver.INTENT_RECORD,
        "selected_command_output_report_artifact_boundary_basis": _boundary_basis(),
        "selected_command_output_report_artifact_boundary_terminal_summary_basis": (
            _terminal_summary_basis("command_output_report_artifact_boundary_terminal_summary")
        ),
        "selected_output_capture_v2_basis": _output_capture_v2_basis(),
        "selected_output_capture_v2_terminal_summary_basis": _terminal_summary_basis(
            "output_capture_v2_terminal_summary"
        ),
        "selected_output_capture_v1_predecessor_failure_basis": _reference_basis(
            "output_capture_v1_predecessor_failure",
            selected_output_capture_v1_predecessor_path=(
                "src/resolve_portable_source_body_verification_output_capture.py"
            ),
            v1_output_capture_predecessor_failure_preserved=True,
            v1_produced_clean_in_memory_law_result=True,
            v1_write_failed_on_frozenset_in_expected_posture=True,
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
            command_report_lineage_basis_treated_as_current_report_artifact=False,
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
        "command_output_report_artifact_payload": _payload(),
        "command_output_report_artifact_scope": list(SUPPORTED_SCOPE),
        "requested_command_output_report_artifact_outcome": RECORDED,
        "declared_non_claims": _false_non_claims(),
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
    return resolve_portable_source_body_verification_command_output_report_artifact(
        declared_command_output_report_artifact_request=request
    )


class CommandOutputReportArtifactTests(unittest.TestCase):
    def assertRecordedArtifact(self, result: Mapping[str, Any]) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        metadata = result[
            "portable_source_body_verification_command_output_report_artifact_metadata"
        ]
        self.assertEqual(metadata["failed_check_count"], 0)
        self.assertGreater(metadata["passed_check_count"], 0)
        self.assertEqual(metadata["portable_source_body_verification_command_output_report_artifact_result_version"], "0.1.0")
        self.assertEqual(metadata["resolver_module"], "resolve_portable_source_body_verification_command_output_report_artifact")
        self.assertIs(metadata["successor_lineage_preserved_in_selected_basis"], True)
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)

        statement = result["command_output_report_artifact_statement"]
        for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIs(statement[key], True, key)
        for key in (
            "report_body_invented",
            "command_result_created",
            "command_success_created",
            "command_output_report_artifact_treated_as_result",
            "command_output_report_artifact_treated_as_success",
            "command_output_report_artifact_treated_as_source",
            "command_output_report_artifact_treated_as_authority",
            "command_output_report_artifact_treated_as_currentness",
            "command_output_report_artifact_treated_as_final_completion",
        ):
            self.assertIs(statement[key], False, key)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, result["non_claims"])
            self.assertIs(result["non_claims"][key], False, key)

    def assertBlocked(self, result: Mapping[str, Any]) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertTrue(result["block"]["blocked"])
        self.assertIsNotNone(result["block"]["block_code"])
        self.assertIn(result["block"]["block_code"], resolver.BLOCK_CODES)
        statement = result["command_output_report_artifact_statement"]
        self.assertIs(statement["command_result_created"], False)
        self.assertIs(statement["command_success_created"], False)
        self.assertIs(statement["report_body_invented"], False)
        self.assertIs(result["non_claims"]["follow_on_work_authorized"], False)

    def test_public_api_and_constants_are_present(self) -> None:
        self.assertTrue(callable(resolve_portable_source_body_verification_command_output_report_artifact))
        self.assertTrue(callable(resolve_portable_source_body_verification_command_output_report_artifact_from_path))
        self.assertTrue(callable(write_portable_source_body_verification_command_output_report_artifact_result))
        self.assertTrue(callable(build_portable_source_body_verification_command_output_report_artifact_summary))
        self.assertTrue(callable(build_declared_portable_source_body_verification_command_output_report_artifact_request))
        self.assertEqual(
            {
                resolver.OUTCOME_RECORDED,
                resolver.OUTCOME_NOT_RECORDED,
                resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                resolver.OUTCOME_BLOCKED,
            },
            OUTCOME_FAMILY,
        )
        self.assertEqual(set(SUPPORTED_SCOPE), set(resolver.SUPPORTED_COMMAND_OUTPUT_REPORT_ARTIFACT_SCOPE))
        self.assertIn("report_body_invented", REQUIRED_FALSE_NON_CLAIMS)
        self.assertIn("command_result_created", REQUIRED_FALSE_NON_CLAIMS)
        self.assertIn("command_success_created", REQUIRED_FALSE_NON_CLAIMS)

    def test_successful_recorded_result_preserves_bounded_artifact_only(self) -> None:
        result = _resolve(_valid_request())
        self.assertRecordedArtifact(result)

        boundary = result["selected_command_output_report_artifact_boundary_basis"]
        self.assertEqual(boundary["outcome"], resolver.COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_OUTCOME)
        self.assertEqual(boundary["failed_check_count"], 0)
        self.assertIs(boundary["one_future_command_output_report_artifact_step_declared"], True)
        self.assertIs(boundary["output_capture_v2_basis_preserved"], True)
        self.assertIs(boundary["output_capture_v1_predecessor_failure_preserved"], True)
        self.assertIs(boundary["report_artifact_created"], False)
        self.assertIs(boundary["report_body_created"], False)
        self.assertIs(boundary["report_body_invented"], False)
        self.assertIs(boundary["command_result_created"], False)
        self.assertIs(boundary["command_success_created"], False)

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
        self.assertIs(output_capture_v2["output_capture_event_recorded"], True)
        for key in (
            "stdout_content_invented",
            "stderr_content_invented",
            "process_output_content_invented",
            "raw_output_body_content_invented",
            "command_output_report_artifact_created",
            "command_result_created",
            "command_success_created",
        ):
            self.assertIs(output_capture_v2[key], False, key)

        checks = result["command_output_report_artifact_checks"]
        self.assertTrue(checks)
        self.assertTrue(all(check["passed"] is True for check in checks))
        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertIn("block_code", check)
            self.assertIn("failure_code", check)

    def test_payload_preserves_absent_report_body_and_non_result_posture(self) -> None:
        result = _resolve(_valid_request())
        self.assertRecordedArtifact(result)
        payload = result["command_output_report_artifact_payload"]
        self.assertIs(payload["command_output_report_artifact_payload_recorded"], True)
        self.assertEqual(payload["payload_type"], "COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDED")
        self.assertIs(payload["report_body_present"], False)
        self.assertIs(payload["report_body_absent_or_bounded"], True)
        for key in (
            "report_body_invented",
            "stdout_content_invented",
            "stderr_content_invented",
            "process_output_content_invented",
            "raw_output_body_content_invented",
            "command_output_body_invented",
            "result_body_invented",
            "success_body_invented",
            "source_body_invented",
            "authority_body_invented",
            "currentness_claim_created",
            "final_completion_claim_created",
            "command_result_created",
            "command_success_created",
        ):
            self.assertIs(payload[key], False, key)
        for key in (
            "command_output_report_artifact_is_not_result",
            "command_output_report_artifact_is_not_success",
            "command_output_report_artifact_is_not_source",
            "command_output_report_artifact_is_not_authority",
            "command_output_report_artifact_is_not_currentness",
            "command_output_report_artifact_is_not_final_completion",
        ):
            self.assertIs(payload[key], True, key)
        for raw_key in RAW_BODY_KEYS:
            self.assertNotIn(raw_key, payload, raw_key)

        non_meaning = result["command_output_report_artifact_non_meaning"]
        self.assertIs(non_meaning["command_result_exists"], False)
        self.assertIs(non_meaning["command_success_exists"], False)
        self.assertIs(non_meaning["artifact_is_source"], False)
        self.assertIs(non_meaning["artifact_is_authority"], False)
        self.assertIs(non_meaning["artifact_is_currentness"], False)
        self.assertIs(non_meaning["artifact_is_final_completion"], False)

    def test_path_resolution_and_json_writing_are_bounded(self) -> None:
        request = _valid_request()
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            request_path = temp_root / "request.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")

            result = resolve_portable_source_body_verification_command_output_report_artifact_from_path(
                request_path
            )
            self.assertRecordedArtifact(result)

            malformed_path = temp_root / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            self.assertBlocked(
                resolve_portable_source_body_verification_command_output_report_artifact_from_path(
                    malformed_path
                )
            )

            array_path = temp_root / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            self.assertBlocked(
                resolve_portable_source_body_verification_command_output_report_artifact_from_path(
                    array_path
                )
            )

            self.assertBlocked(
                resolve_portable_source_body_verification_command_output_report_artifact_from_path(
                    temp_root / "missing.json"
                )
            )

            patched_output_root = (
                temp_root
                / "artifacts"
                / "integrity_host_v0_min_coexistence_portable_source_body_verification_command_output_report_artifact"
            )
            with patch.object(resolver, "OUTPUT_ROOT", patched_output_root):
                output_path_1 = write_portable_source_body_verification_command_output_report_artifact_result(
                    result
                )
                output_path_2 = write_portable_source_body_verification_command_output_report_artifact_result(
                    result
                )
            self.assertTrue(output_path_1.exists())
            self.assertTrue(output_path_2.exists())
            self.assertNotEqual(output_path_1, output_path_2)
            self.assertEqual(json.loads(output_path_1.read_text(encoding="utf-8"))["outcome"], RECORDED)
            self.assertEqual(output_path_1.parent, patched_output_root)
            self.assertIn(
                "integrity_host_v0_min_coexistence_portable_source_body_verification_command_output_report_artifact",
                output_path_1.parts,
            )
            forbidden_roots = {
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
                        "command_output_report_artifact_intent": resolver.INTENT_DO_NOT_RECORD,
                        "requested_command_output_report_artifact_outcome": NOT_RECORDED,
                        "not_recorded_basis": {
                            "readable_basis_failed_review": True,
                            "creates_command_result": False,
                            "creates_command_success": False,
                        },
                    }
                )
            )
        )
        self.assertEqual(not_recorded["outcome"], NOT_RECORDED)
        self.assertIs(not_recorded["not_recorded_basis"]["not_recorded"], True)
        self.assertIs(not_recorded["command_output_report_artifact_statement"]["command_result_created"], False)
        self.assertIs(not_recorded["command_output_report_artifact_statement"]["command_success_created"], False)

        requires = _resolve(
            _copy_request_with(
                lambda request: request.update(
                    {
                        "requested_command_output_report_artifact_outcome": REQUIRES_ADDITIONAL_BASIS,
                        "additional_basis_context": {
                            "report_body_absent_or_bounded_posture_needs_more_basis": True,
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

    def test_blocking_request_shape_boundary_and_scope_cases(self) -> None:
        self.assertBlocked(
            resolve_portable_source_body_verification_command_output_report_artifact(None)
        )
        self.assertBlocked(
            resolve_portable_source_body_verification_command_output_report_artifact(
                declared_command_output_report_artifact_request=[]
            )
        )
        cases: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
            ("explicit block intent", lambda request: request.update({"command_output_report_artifact_intent": resolver.INTENT_BLOCK})),
            ("unsupported intent", lambda request: request.update({"command_output_report_artifact_intent": "UNSUPPORTED"})),
            ("unsupported scope", lambda request: request.update({"command_output_report_artifact_scope": ["UNSUPPORTED_SCOPE"]})),
            ("missing question", lambda request: request.update({"command_output_report_artifact_question": ""})),
            ("missing boundary basis", lambda request: request.update({"selected_command_output_report_artifact_boundary_basis": {}})),
            ("boundary not recorded", lambda request: request["selected_command_output_report_artifact_boundary_basis"].update({"outcome": "NOT_RECORDED"})),
            ("boundary failed checks", lambda request: request["selected_command_output_report_artifact_boundary_basis"].update({"failed_check_count": 1})),
            ("boundary step not declared", lambda request: request["selected_command_output_report_artifact_boundary_basis"].update({"one_future_command_output_report_artifact_step_declared": False})),
            ("boundary output capture v2 not preserved", lambda request: request["selected_command_output_report_artifact_boundary_basis"].update({"output_capture_v2_basis_preserved": False})),
            ("boundary v1 failure not preserved", lambda request: request["selected_command_output_report_artifact_boundary_basis"].update({"output_capture_v1_predecessor_failure_preserved": False})),
            ("boundary already created report artifact", lambda request: request["selected_command_output_report_artifact_boundary_basis"].update({"report_artifact_created": True})),
            ("boundary already created report body", lambda request: request["selected_command_output_report_artifact_boundary_basis"].update({"report_body_created": True})),
            ("boundary already invented report body", lambda request: request["selected_command_output_report_artifact_boundary_basis"].update({"report_body_invented": True})),
            ("boundary already created result", lambda request: request["selected_command_output_report_artifact_boundary_basis"].update({"command_result_created": True})),
            ("boundary already created success", lambda request: request["selected_command_output_report_artifact_boundary_basis"].update({"command_success_created": True})),
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
            ("output capture v2 created report artifact", lambda request: request["selected_output_capture_v2_basis"].update({"command_output_report_artifact_created": True})),
            ("output capture v2 created result", lambda request: request["selected_output_capture_v2_basis"].update({"command_result_created": True})),
            ("output capture v2 created success", lambda request: request["selected_output_capture_v2_basis"].update({"command_success_created": True})),
        )
        for label, mutator in cases:
            with self.subTest(label=label):
                self.assertBlocked(_resolve(_copy_request_with(mutator)))

    def test_blocking_missing_basis_and_posture_sections(self) -> None:
        for key in SELECTED_BASIS_KEYS:
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
                    lambda request: request["declared_non_claims"].update({"command_result_created": True})
                )
            )
        )

    def test_blocking_prior_lineage_and_execution_basis_cases(self) -> None:
        cases: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
            ("post invocation not recorded", lambda request: request["selected_post_invocation_command_execution_basis"].update({"outcome": "NOT_RECORDED"})),
            ("post invocation failed checks", lambda request: request["selected_post_invocation_command_execution_basis"].update({"failed_check_count": 1})),
            ("post invocation trace not audit only", lambda request: request["selected_post_invocation_command_execution_basis"].update({"execution_trace_audit_only": False})),
            ("consumed request reopened", lambda request: request["selected_consumed_request_basis"].update({"consumed_request_reopened": True})),
            ("v2 admitted request failed checks", lambda request: request["selected_v2_admitted_request_basis"].update({"failed_check_count": 1})),
            ("earlier v1 repaired", lambda request: request["selected_v1_predecessor_failure_basis"].update({"v1_repaired": True})),
            ("earlier v1 hidden", lambda request: request["selected_v1_predecessor_failure_basis"].update({"v1_hidden": True})),
            ("earlier v1 claimed passed", lambda request: request["selected_v1_predecessor_failure_basis"].update({"v1_claimed_passed": True})),
            ("older boundary lineage current execution", lambda request: request["selected_older_command_execution_boundary_lineage_basis"].update({"older_command_execution_boundary_lineage_treated_as_current_execution": True})),
            ("command report lineage current report artifact", lambda request: request["selected_command_report_lineage_basis"].update({"command_report_lineage_basis_treated_as_current_report_artifact": True})),
        )
        for label, mutator in cases:
            with self.subTest(label=label):
                self.assertBlocked(_resolve(_copy_request_with(mutator)))

    def test_blocking_overreach_and_collapse_flags(self) -> None:
        overreach_fields = (
            "command_output_report_artifact_treated_as_result",
            "command_output_report_artifact_treated_as_success",
            "command_output_report_artifact_treated_as_source",
            "command_output_report_artifact_treated_as_authority",
            "command_output_report_artifact_treated_as_currentness",
            "command_output_report_artifact_treated_as_final_completion",
            "report_body_invented",
            "report_body_treated_as_result",
            "report_body_treated_as_success",
            "report_body_treated_as_source",
            "report_body_treated_as_authority",
            "report_body_treated_as_currentness",
            "report_body_treated_as_final_completion",
            "output_capture_treated_as_result",
            "output_capture_treated_as_success",
            "output_capture_treated_as_source",
            "output_capture_treated_as_authority",
            "output_capture_treated_as_currentness",
            "output_capture_treated_as_final_completion",
            "command_result_created",
            "command_success_created",
            "execution_trace_treated_as_report_artifact",
            "execution_trace_treated_as_result",
            "execution_trace_treated_as_success",
            "execution_trace_treated_as_source",
            "execution_trace_treated_as_authority",
            "command_result_became_authority",
            "command_success_created_currentness",
            "command_success_claimed_final_completion",
            "consumed_request_reopened",
            "authorization_token_reused",
            "v2_treated_as_repairing_v1_request_admission",
            "v1_request_admission_failure_hidden",
            "v1_request_admission_claimed_passed",
            "raw_full_prior_artifact_body_returned",
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
        payload_original = copy.deepcopy(request["command_output_report_artifact_payload"])
        scope_original = copy.deepcopy(request["command_output_report_artifact_scope"])

        result = _resolve(request)
        self.assertRecordedArtifact(result)
        self.assertEqual(request, original_request)
        for key, original in selected_basis_originals.items():
            self.assertEqual(request[key], original, key)
        for key, original in posture_originals.items():
            self.assertEqual(request[key], original, key)
        self.assertEqual(request["command_output_report_artifact_payload"], payload_original)
        self.assertEqual(request["command_output_report_artifact_scope"], scope_original)

    def test_summary_and_builder_preserve_short_name_lineage_and_non_claims(self) -> None:
        request = _valid_request()
        built = build_declared_portable_source_body_verification_command_output_report_artifact_request(
            command_output_report_artifact_request_id="builder_request",
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
                "command_output_report_artifact_payload": request[
                    "command_output_report_artifact_payload"
                ],
                "requested_command_output_report_artifact_outcome": RECORDED,
            }
        )
        result = _resolve(built)
        self.assertRecordedArtifact(result)
        summary = build_portable_source_body_verification_command_output_report_artifact_summary(
            result
        )
        self.assertEqual(summary["outcome"], RECORDED)
        self.assertEqual(summary["request_id"], "builder_request")
        self.assertIs(summary["command_output_report_artifact_recorded"], True)
        self.assertIs(summary["bounded_command_output_report_artifact_recorded"], True)
        self.assertIs(summary["report_body_not_invented"], True)
        self.assertIs(summary["command_result_still_not_created"], True)
        self.assertIs(summary["command_success_still_not_created"], True)
        self.assertIs(summary["command_report_lineage_not_current_report_artifact"], True)
        self.assertIs(summary["key_non_claims"]["follow_on_work_authorized"], False)
        metadata = result[
            "portable_source_body_verification_command_output_report_artifact_metadata"
        ]
        self.assertIs(metadata["short_resolver_filename_used_under_naming_containment"], True)
        self.assertIs(metadata["successor_lineage_preserved_in_selected_basis"], True)


if __name__ == "__main__":
    unittest.main()
