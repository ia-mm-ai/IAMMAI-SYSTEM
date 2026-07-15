"""Tests for command output/report artifact boundary only.

This suite is downstream of recorded output capture v2. It proves that one
future command output/report artifact boundary may be recorded without creating
a report artifact, report body, command result, command success, source,
authority, currentness, final completion, deployment, continuation, reusable
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

import resolve_portable_source_body_verification_command_output_report_artifact_boundary as resolver
from resolve_portable_source_body_verification_command_output_report_artifact_boundary import (
    build_declared_portable_source_body_verification_command_output_report_artifact_boundary_request,
    build_portable_source_body_verification_command_output_report_artifact_boundary_summary,
    resolve_portable_source_body_verification_command_output_report_artifact_boundary,
    resolve_portable_source_body_verification_command_output_report_artifact_boundary_from_path,
    write_portable_source_body_verification_command_output_report_artifact_boundary_result,
)


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}

QUESTION = resolver.CORE_QUESTION
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
RAW_FULL_BODY_SENTINEL = "RAW_COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_BODY_MUST_NOT_RETURN_" * 6

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_command_output_report_artifact_boundary_metadata",
    "declared_command_output_report_artifact_boundary_question",
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
    "command_output_report_artifact_boundary_only_posture",
    "one_future_command_output_report_artifact_step_posture",
    "output_capture_v2_basis_preserved_posture",
    "output_capture_v1_predecessor_failure_preserved_posture",
    "bounded_output_capture_event_preserved_posture",
    "command_output_basis_preserved_posture",
    "execution_trace_audit_only_posture",
    "no_report_artifact_created_posture",
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
    "command_output_report_artifact_boundary_scope",
    "command_output_report_artifact_boundary_checks",
    "command_output_report_artifact_boundary_statement",
    "command_output_report_artifact_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_command_output_report_artifact_boundary_summary",
)

SELECTED_BASIS_KEYS = tuple(resolver.SELECTED_BASIS_KEYS)
POSTURE_KEYS = tuple(resolver.POSTURE_KEYS)


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
        "basis_is_not_report_artifact": True,
        "basis_is_not_report_body": True,
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
        "command_output_report_artifact_created": False,
        "report_artifact_created": False,
        "report_body_created": False,
        "report_body_invented": False,
        "command_result_created": False,
        "command_success_created": False,
        "report_artifact_boundary_treated_as_report_artifact": False,
        "report_artifact_boundary_treated_as_result": False,
        "report_artifact_boundary_treated_as_success": False,
        "report_artifact_boundary_treated_as_source": False,
        "report_artifact_boundary_treated_as_authority": False,
        "report_artifact_boundary_treated_as_currentness": False,
        "report_artifact_boundary_treated_as_final_completion": False,
        "output_capture_treated_as_report_artifact": False,
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
        "command_output_report_artifact_boundary_only": True,
        "one_future_command_output_report_artifact_step_declared": True,
        "output_capture_v2_basis_preserved": True,
        "output_capture_v1_predecessor_failure_preserved": True,
        "bounded_output_capture_event_preserved": True,
        "command_output_basis_preserved": True,
        "recorded_command_execution_event_preserved": True,
        "execution_trace_audit_only": True,
        "execution_trace_audit_only_preserved": True,
        "command_output_report_artifact_created": False,
        "command_output_report_artifact_not_created": True,
        "report_artifact_created": False,
        "report_body_created": False,
        "report_body_not_created": True,
        "report_body_invented": False,
        "report_body_not_invented": True,
        "command_result_created": False,
        "command_result_not_created": True,
        "command_result_still_not_created": True,
        "command_success_created": False,
        "command_success_not_created": True,
        "command_success_still_not_created": True,
        "report_artifact_boundary_treated_as_report_artifact": False,
        "report_artifact_boundary_treated_as_result": False,
        "report_artifact_boundary_treated_as_success": False,
        "report_artifact_boundary_treated_as_source": False,
        "report_artifact_boundary_treated_as_authority": False,
        "report_artifact_boundary_treated_as_currentness": False,
        "report_artifact_boundary_treated_as_final_completion": False,
        "output_capture_treated_as_report_artifact": False,
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


def _valid_request(**overrides: Any) -> dict[str, Any]:
    request: dict[str, Any] = {
        "command_output_report_artifact_boundary_request_id": (
            "command_output_report_artifact_boundary_reference_review_001"
        ),
        "command_output_report_artifact_boundary_question": QUESTION,
        "command_output_report_artifact_boundary_intent": resolver.INTENT_RECORD,
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
        "command_output_report_artifact_boundary_scope": list(SUPPORTED_SCOPE),
        "requested_command_output_report_artifact_boundary_outcome": RECORDED,
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
    return resolve_portable_source_body_verification_command_output_report_artifact_boundary(
        declared_command_output_report_artifact_boundary_request=request
    )


class CommandOutputReportArtifactBoundaryTests(unittest.TestCase):
    def assertRecordedBoundary(self, result: Mapping[str, Any]) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        metadata = result[
            "portable_source_body_verification_command_output_report_artifact_boundary_metadata"
        ]
        self.assertEqual(metadata["failed_check_count"], 0)
        self.assertGreater(metadata["passed_check_count"], 0)
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        statement = result["command_output_report_artifact_boundary_statement"]
        for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIs(statement[key], True, key)
        for key in (
            "command_output_report_artifact_created",
            "report_artifact_created",
            "report_body_created",
            "report_body_invented",
            "command_result_created",
            "command_success_created",
            "report_artifact_boundary_treated_as_report_artifact",
            "report_artifact_boundary_treated_as_result",
            "report_artifact_boundary_treated_as_success",
            "report_artifact_boundary_treated_as_source",
            "report_artifact_boundary_treated_as_authority",
            "report_artifact_boundary_treated_as_currentness",
            "report_artifact_boundary_treated_as_final_completion",
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
        statement = result["command_output_report_artifact_boundary_statement"]
        self.assertIs(statement["command_output_report_artifact_created"], False)
        self.assertIs(statement["report_body_created"], False)
        self.assertIs(statement["report_body_invented"], False)
        self.assertIs(statement["command_result_created"], False)
        self.assertIs(statement["command_success_created"], False)
        self.assertIs(result["non_claims"]["follow_on_work_authorized"], False)

    def test_public_api_is_present(self) -> None:
        self.assertTrue(callable(resolve_portable_source_body_verification_command_output_report_artifact_boundary))
        self.assertTrue(callable(resolve_portable_source_body_verification_command_output_report_artifact_boundary_from_path))
        self.assertTrue(callable(write_portable_source_body_verification_command_output_report_artifact_boundary_result))
        self.assertTrue(callable(build_portable_source_body_verification_command_output_report_artifact_boundary_summary))
        self.assertTrue(callable(build_declared_portable_source_body_verification_command_output_report_artifact_boundary_request))
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_portable_source_body_verification_command_output_report_artifact_boundary",
        )

    def test_successful_recorded_result_preserves_boundary_only_posture(self) -> None:
        request = _valid_request()
        original_request = copy.deepcopy(request)
        result = _resolve(request)

        self.assertRecordedBoundary(result)
        self.assertEqual(request, original_request)

        metadata = result[
            "portable_source_body_verification_command_output_report_artifact_boundary_metadata"
        ]
        self.assertEqual(
            metadata[
                "portable_source_body_verification_command_output_report_artifact_boundary_result_version"
            ],
            "0.1.0",
        )
        self.assertEqual(metadata["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertIs(metadata["short_resolver_filename_used_under_naming_containment"], True)
        self.assertIs(metadata["successor_lineage_preserved_in_selected_basis"], True)

        selected_v2 = result["selected_output_capture_v2_basis"]
        self.assertEqual(selected_v2["outcome"], resolver.OUTPUT_CAPTURE_V2_OUTCOME)
        self.assertEqual(selected_v2["result_version"], "0.2.0")
        self.assertEqual(selected_v2["failed_check_count"], 0)
        self.assertIs(selected_v2["json_safe_result"], True)
        self.assertEqual(
            selected_v2["successor_of"],
            "resolve_portable_source_body_verification_output_capture",
        )
        self.assertIs(selected_v2["v1_predecessor_failure_preserved"], True)
        self.assertIs(selected_v2["v1_repaired"], False)
        self.assertIs(selected_v2["v1_hidden"], False)
        self.assertIs(selected_v2["v1_claimed_passed"], False)
        self.assertIs(selected_v2["v2_successor_does_not_erase_v1"], True)
        self.assertIs(selected_v2["output_capture_event_recorded"], True)
        self.assertIs(selected_v2["stdout_content_invented"], False)
        self.assertIs(selected_v2["stderr_content_invented"], False)
        self.assertIs(selected_v2["process_output_content_invented"], False)
        self.assertIs(selected_v2["raw_output_body_content_invented"], False)
        self.assertIs(selected_v2["command_output_report_artifact_created"], False)
        self.assertIs(selected_v2["command_result_created"], False)
        self.assertIs(selected_v2["command_success_created"], False)

        selected_command_report = result["selected_command_report_lineage_basis"]
        self.assertIs(selected_command_report["basis_remains_lineage_only"], True)
        self.assertIs(selected_command_report["current_report_artifact"], False)
        self.assertIs(
            selected_command_report[
                "command_report_lineage_basis_treated_as_current_report_artifact"
            ],
            False,
        )
        self.assertIs(
            result["selected_older_command_execution_boundary_lineage_basis"][
                "older_command_execution_boundary_lineage_treated_as_current_execution"
            ],
            False,
        )

        scope = result["command_output_report_artifact_boundary_scope"]
        self.assertEqual(set(scope["declared_scope"]), set(SUPPORTED_SCOPE))
        self.assertEqual(scope["unsupported_scope"], [])
        self.assertTrue(all(check["passed"] for check in result["command_output_report_artifact_boundary_checks"]))
        self.assertNotIn(RAW_FULL_BODY_SENTINEL, _json_text(result))

    def test_summary_helper_preserves_boundary_facts(self) -> None:
        result = _resolve(_valid_request())
        summary = build_portable_source_body_verification_command_output_report_artifact_boundary_summary(
            result
        )

        self.assertEqual(summary["outcome"], RECORDED)
        self.assertEqual(summary["request_id"], result["declared_command_output_report_artifact_boundary_question"]["command_output_report_artifact_boundary_request_id"])
        self.assertEqual(summary["question"], QUESTION)
        self.assertEqual(summary["intent"], resolver.INTENT_RECORD)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertIs(summary["command_output_report_artifact_boundary_recorded"], True)
        self.assertIs(summary["one_future_command_output_report_artifact_step_declared"], True)
        self.assertIs(summary["output_capture_v2_basis_preserved"], True)
        self.assertIs(summary["output_capture_v1_predecessor_failure_preserved"], True)
        self.assertIs(summary["bounded_output_capture_event_preserved"], True)
        self.assertIs(summary["command_output_basis_preserved"], True)
        self.assertIs(summary["execution_trace_audit_only_preserved"], True)
        self.assertIs(summary["command_output_report_artifact_not_created"], True)
        self.assertIs(summary["report_body_not_created"], True)
        self.assertIs(summary["report_body_not_invented"], True)
        self.assertIs(summary["command_result_still_not_created"], True)
        self.assertIs(summary["command_success_still_not_created"], True)
        self.assertEqual(
            summary["selected_output_capture_v2_outcome"],
            resolver.OUTPUT_CAPTURE_V2_OUTCOME,
        )
        self.assertEqual(summary["selected_output_capture_v2_result_version"], "0.2.0")
        self.assertEqual(summary["selected_output_capture_v2_failed_check_count"], 0)
        self.assertIs(summary["report_artifact_boundary_not_report_artifact"], True)
        self.assertIs(summary["output_capture_not_report_artifact"], True)
        self.assertIs(summary["execution_trace_not_report_artifact"], True)
        self.assertIs(summary["result_not_authority"], True)
        self.assertIs(summary["success_not_currentness"], True)
        self.assertIs(summary["success_not_final_completion"], True)
        self.assertIs(summary["command_report_lineage_not_current_report_artifact"], True)
        self.assertFalse(summary["deployment_created"])
        self.assertFalse(summary["follow_on_work_authorized"])

    def test_path_and_write_behavior_is_bounded_to_temp_and_v2_boundary_root(self) -> None:
        request = _valid_request()
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            request_path = temp_root / "request.json"
            request_path.write_text(json.dumps(request, sort_keys=True), encoding="utf-8")
            result = resolve_portable_source_body_verification_command_output_report_artifact_boundary_from_path(
                request_path
            )
            self.assertRecordedBoundary(result)

            malformed_path = temp_root / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            self.assertBlocked(
                resolve_portable_source_body_verification_command_output_report_artifact_boundary_from_path(
                    malformed_path
                )
            )
            array_path = temp_root / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            self.assertBlocked(
                resolve_portable_source_body_verification_command_output_report_artifact_boundary_from_path(
                    array_path
                )
            )
            self.assertBlocked(
                resolve_portable_source_body_verification_command_output_report_artifact_boundary_from_path(
                    temp_root / "missing.json"
                )
            )

            explicit_path = temp_root / "nested" / "result.json"
            first_written = write_portable_source_body_verification_command_output_report_artifact_boundary_result(
                result,
                explicit_path,
            )
            second_written = write_portable_source_body_verification_command_output_report_artifact_boundary_result(
                result,
                explicit_path,
            )
            self.assertTrue(first_written.exists())
            self.assertTrue(second_written.exists())
            self.assertNotEqual(first_written, second_written)
            parsed = json.loads(first_written.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], RECORDED)
            self.assertEqual(
                parsed[
                    "portable_source_body_verification_command_output_report_artifact_boundary_metadata"
                ]["resolver_module"],
                resolver.RESOLVER_MODULE,
            )

            patched_root = temp_root / "artifacts" / (
                "integrity_host_v0_min_coexistence_portable_source_body_verification_"
                "command_output_report_artifact_boundary"
            )
            with patch.object(resolver, "OUTPUT_ROOT", patched_root):
                default_written = write_portable_source_body_verification_command_output_report_artifact_boundary_result(
                    result
                )
            self.assertTrue(default_written.exists())
            self.assertIn(
                "integrity_host_v0_min_coexistence_portable_source_body_verification_command_output_report_artifact_boundary",
                str(default_written),
            )
            self.assertNotIn(
                "integrity_host_v0_min_coexistence_portable_source_body_verification_output_capture_v2/",
                str(default_written),
            )
            self.assertNotIn(
                "integrity_host_v0_min_coexistence_portable_source_body_verification_command_output/",
                str(default_written),
            )

        self.assertIn(
            "integrity_host_v0_min_coexistence_portable_source_body_verification_command_output_report_artifact_boundary",
            str(resolver.OUTPUT_ROOT),
        )
        self.assertNotEqual(
            str(resolver.OUTPUT_ROOT),
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_output_capture_v2",
        )

    def test_not_recorded_requires_additional_basis_and_blocked_are_distinct_outcomes(self) -> None:
        not_recorded_request = _valid_request(
            requested_command_output_report_artifact_boundary_outcome=NOT_RECORDED,
            not_recorded_basis={"review_failed_without_collapse": True},
        )
        not_recorded = _resolve(not_recorded_request)
        self.assertEqual(not_recorded["outcome"], NOT_RECORDED)
        self.assertFalse(not_recorded["block"]["blocked"])
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded"])
        self.assertFalse(not_recorded["not_recorded_basis"]["creates_report_artifact"])

        requires_request = _valid_request(
            requested_command_output_report_artifact_boundary_outcome=REQUIRES_ADDITIONAL_BASIS,
            additional_basis_context={"missing_non_collapse_basis": True},
        )
        requires = _resolve(requires_request)
        self.assertEqual(requires["outcome"], REQUIRES_ADDITIONAL_BASIS)
        self.assertFalse(requires["block"]["blocked"])
        self.assertTrue(requires["additional_basis_required"]["additional_basis_required"])
        self.assertTrue(requires["additional_basis_required"]["missing_basis_is_not_authorized"])

        blocked = _resolve(
            _copy_request_with(
                lambda request: request.update(
                    command_output_report_artifact_boundary_intent="UNSUPPORTED"
                )
            )
        )
        self.assertBlocked(blocked)

        self.assertEqual({not_recorded["outcome"], requires["outcome"], blocked["outcome"], RECORDED}, OUTCOME_FAMILY)

    def test_blocking_cases_preserve_no_report_result_success_posture(self) -> None:
        cases: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
            ("explicit block intent", lambda r: r.update(command_output_report_artifact_boundary_intent=resolver.INTENT_BLOCK)),
            ("unsupported intent", lambda r: r.update(command_output_report_artifact_boundary_intent="UNSUPPORTED_INTENT")),
            ("unsupported scope", lambda r: r["command_output_report_artifact_boundary_scope"].append("UNSUPPORTED_SCOPE")),
            ("missing output capture v2 basis", lambda r: r.pop("selected_output_capture_v2_basis")),
            ("output capture v2 not recorded", lambda r: r["selected_output_capture_v2_basis"].update(outcome="NOT_RECORDED")),
            ("output capture v2 failed checks", lambda r: r["selected_output_capture_v2_basis"].update(failed_check_count=1)),
            ("output capture v2 wrong version", lambda r: r["selected_output_capture_v2_basis"].update(result_version="0.1.0")),
            ("output capture v2 not JSON safe", lambda r: r["selected_output_capture_v2_basis"].update(json_safe_result=False)),
            ("output capture v2 predecessor failure missing", lambda r: r["selected_output_capture_v2_basis"].update(v1_predecessor_failure_preserved=False)),
            ("output capture v2 repaired v1", lambda r: r["selected_output_capture_v2_basis"].update(v1_repaired=True)),
            ("output capture v2 hid v1", lambda r: r["selected_output_capture_v2_basis"].update(v1_hidden=True)),
            ("output capture v2 claimed v1 passed", lambda r: r["selected_output_capture_v2_basis"].update(v1_claimed_passed=True)),
            ("output capture v2 erased v1", lambda r: r["selected_output_capture_v2_basis"].update(v2_successor_does_not_erase_v1=False)),
            ("output capture v2 created report artifact", lambda r: r["selected_output_capture_v2_basis"].update(command_output_report_artifact_created=True)),
            ("output capture v2 created result", lambda r: r["selected_output_capture_v2_basis"].update(command_result_created=True)),
            ("output capture v2 created success", lambda r: r["selected_output_capture_v2_basis"].update(command_success_created=True)),
            ("output capture v2 invented stdout", lambda r: r["selected_output_capture_v2_basis"].update(stdout_content_invented=True)),
            ("output capture v2 invented stderr", lambda r: r["selected_output_capture_v2_basis"].update(stderr_content_invented=True)),
            ("output capture v2 invented process output", lambda r: r["selected_output_capture_v2_basis"].update(process_output_content_invented=True)),
            ("output capture v2 invented raw output body", lambda r: r["selected_output_capture_v2_basis"].update(raw_output_body_content_invented=True)),
            ("missing output capture boundary basis", lambda r: r.pop("selected_output_capture_boundary_basis")),
            ("missing command output basis", lambda r: r.pop("selected_command_output_basis")),
            ("missing post-invocation basis", lambda r: r.pop("selected_post_invocation_command_execution_basis")),
            ("post-invocation not recorded", lambda r: r["selected_post_invocation_command_execution_basis"].update(outcome="NOT_RECORDED")),
            ("post-invocation failed checks", lambda r: r["selected_post_invocation_command_execution_basis"].update(failed_check_count=1)),
            ("post-invocation trace not audit-only", lambda r: r["selected_post_invocation_command_execution_basis"].update(execution_trace_audit_only=False)),
            ("boundary treated as report artifact", lambda r: r.update(report_artifact_boundary_treated_as_report_artifact=True)),
            ("boundary treated as result", lambda r: r.update(report_artifact_boundary_treated_as_result=True)),
            ("boundary treated as success", lambda r: r.update(report_artifact_boundary_treated_as_success=True)),
            ("boundary treated as source", lambda r: r.update(report_artifact_boundary_treated_as_source=True)),
            ("boundary treated as authority", lambda r: r.update(report_artifact_boundary_treated_as_authority=True)),
            ("boundary treated as currentness", lambda r: r.update(report_artifact_boundary_treated_as_currentness=True)),
            ("boundary treated as final completion", lambda r: r.update(report_artifact_boundary_treated_as_final_completion=True)),
            ("output capture treated as report artifact", lambda r: r.update(output_capture_treated_as_report_artifact=True)),
            ("output capture treated as result", lambda r: r.update(output_capture_treated_as_result=True)),
            ("output capture treated as success", lambda r: r.update(output_capture_treated_as_success=True)),
            ("output capture treated as source", lambda r: r.update(output_capture_treated_as_source=True)),
            ("output capture treated as authority", lambda r: r.update(output_capture_treated_as_authority=True)),
            ("output capture treated as currentness", lambda r: r.update(output_capture_treated_as_currentness=True)),
            ("output capture treated as final completion", lambda r: r.update(output_capture_treated_as_final_completion=True)),
            ("report artifact created", lambda r: r.update(report_artifact_created=True)),
            ("report body created", lambda r: r.update(report_body_created=True)),
            ("report body invented", lambda r: r.update(report_body_invented=True)),
            ("command result created", lambda r: r.update(command_result_created=True)),
            ("command success created", lambda r: r.update(command_success_created=True)),
            ("execution trace treated as report artifact", lambda r: r.update(execution_trace_treated_as_report_artifact=True)),
            ("execution trace treated as result", lambda r: r.update(execution_trace_treated_as_result=True)),
            ("execution trace treated as success", lambda r: r.update(execution_trace_treated_as_success=True)),
            ("execution trace treated as source", lambda r: r.update(execution_trace_treated_as_source=True)),
            ("execution trace treated as authority", lambda r: r.update(execution_trace_treated_as_authority=True)),
            ("result treated as authority", lambda r: r.update(command_result_became_authority=True)),
            ("success treated as currentness", lambda r: r.update(command_success_created_currentness=True)),
            ("success treated as final completion", lambda r: r.update(command_success_claimed_final_completion=True)),
            ("consumed request reopened", lambda r: r.update(consumed_request_reopened=True)),
            ("authorization token reused", lambda r: r.update(authorization_token_reused=True)),
            ("older lineage current execution", lambda r: r["selected_older_command_execution_boundary_lineage_basis"].update(older_command_execution_boundary_lineage_treated_as_current_execution=True)),
            ("command report lineage current artifact", lambda r: r["selected_command_report_lineage_basis"].update(current_report_artifact=True)),
            ("missing command boundary basis", lambda r: r.pop("selected_command_boundary_basis")),
            ("missing posture section", lambda r: r.pop("no_command_success_posture")),
            ("full prior body returned", lambda r: r.update(raw_full_prior_artifact_body_returned=True)),
            ("artifacts mutated", lambda r: r.update(prior_artifacts_mutated=True)),
            ("deployment created", lambda r: r.update(deployment_created=True)),
            ("runtime hosting created", lambda r: r.update(runtime_hosting_created=True)),
            ("public release created", lambda r: r.update(public_release_created=True)),
            ("operation created", lambda r: r.update(operation_permission_created=True)),
            ("public readiness created", lambda r: r.update(public_launch_readiness_created=True)),
            ("final completion claimed", lambda r: r.update(final_completion_claimed=True)),
            ("continuation authorized", lambda r: r.update(continuation_authorized=True)),
            ("reusable permission created", lambda r: r.update(reusable_permission_created=True)),
            ("follow-on work authorized", lambda r: r.update(follow_on_work_authorized=True)),
            ("derivative reception authorized", lambda r: r.update(derivative_reception_authorized=True)),
            ("vessel relation authorized", lambda r: r.update(vessel_relation_authorized=True)),
            ("another reception request authorized", lambda r: r.update(another_reception_request_authorized=True)),
            ("mutation detected", lambda r: r.update(mutation_performed=True)),
            ("replay detected", lambda r: r.update(replay_performed=True)),
            ("merge detected", lambda r: r.update(merge_performed=True)),
            ("required non-claim missing", lambda r: r["declared_non_claims"].pop(REQUIRED_FALSE_NON_CLAIMS[0])),
            ("required non-claim flipped", lambda r: r["declared_non_claims"].update({REQUIRED_FALSE_NON_CLAIMS[1]: True})),
        )
        for name, mutator in cases:
            with self.subTest(name=name):
                result = _resolve(_copy_request_with(mutator))
                self.assertBlocked(result)

        self.assertBlocked(
            resolve_portable_source_body_verification_command_output_report_artifact_boundary()
        )
        self.assertBlocked(
            resolve_portable_source_body_verification_command_output_report_artifact_boundary(
                declared_command_output_report_artifact_boundary_request=["not", "mapping"]
            )
        )

    def test_non_mutation_for_selected_basis_postures_scope_and_request(self) -> None:
        request = _valid_request()
        selected_snapshots = {
            key: copy.deepcopy(request[key])
            for key in SELECTED_BASIS_KEYS
        }
        posture_snapshots = {
            key: copy.deepcopy(request[key])
            for key in POSTURE_KEYS
        }
        scope_snapshot = copy.deepcopy(request["command_output_report_artifact_boundary_scope"])
        request_snapshot = copy.deepcopy(request)

        result = _resolve(request)

        self.assertRecordedBoundary(result)
        self.assertEqual(request, request_snapshot)
        for key, snapshot in selected_snapshots.items():
            self.assertEqual(request[key], snapshot, key)
        for key, snapshot in posture_snapshots.items():
            self.assertEqual(request[key], snapshot, key)
        self.assertEqual(request["command_output_report_artifact_boundary_scope"], scope_snapshot)

    def test_raw_full_prior_artifact_body_is_not_returned_from_selected_basis(self) -> None:
        request = _valid_request()
        request["selected_command_report_lineage_basis"]["raw_full_prior_artifact_body"] = (
            RAW_FULL_BODY_SENTINEL
        )
        request["selected_output_capture_v2_basis"]["full_prior_artifact_body"] = (
            RAW_FULL_BODY_SENTINEL
        )

        result = _resolve(request)

        self.assertRecordedBoundary(result)
        text = _json_text(result)
        self.assertNotIn(RAW_FULL_BODY_SENTINEL, text)
        self.assertTrue(
            result["selected_command_report_lineage_basis"]["raw_full_prior_artifact_body"][
                "raw_full_prior_artifact_body_omitted"
            ]
        )
        self.assertTrue(
            result["selected_output_capture_v2_basis"]["full_prior_artifact_body"][
                "raw_full_prior_artifact_body_omitted"
            ]
        )

    def test_builder_builds_valid_declared_request_without_report_result_success(self) -> None:
        request = build_declared_portable_source_body_verification_command_output_report_artifact_boundary_request(
            command_output_report_artifact_boundary_request_id="builder_request",
            selected_output_capture_v2_basis=_output_capture_v2_basis(),
            selected_output_capture_v2_terminal_summary_basis=_terminal_summary_basis("builder_v2_summary"),
            selected_output_capture_v1_predecessor_failure_basis=_valid_request()["selected_output_capture_v1_predecessor_failure_basis"],
            selected_output_capture_boundary_basis=_valid_request()["selected_output_capture_boundary_basis"],
            selected_command_output_basis=_valid_request()["selected_command_output_basis"],
            selected_command_output_boundary_basis=_valid_request()["selected_command_output_boundary_basis"],
            selected_command_output_containment_basis=_valid_request()["selected_command_output_containment_basis"],
            selected_post_invocation_command_execution_basis=_valid_request()["selected_post_invocation_command_execution_basis"],
            selected_post_invocation_command_execution_terminal_summary_basis=_valid_request()["selected_post_invocation_command_execution_terminal_summary_basis"],
            selected_command_invocation_basis=_valid_request()["selected_command_invocation_basis"],
            selected_command_execution_review_basis=_valid_request()["selected_command_execution_review_basis"],
            selected_request_consumption_basis=_valid_request()["selected_request_consumption_basis"],
            selected_consumed_request_basis=_valid_request()["selected_consumed_request_basis"],
            selected_v2_admitted_request_basis=_valid_request()["selected_v2_admitted_request_basis"],
            selected_v1_predecessor_failure_basis=_valid_request()["selected_v1_predecessor_failure_basis"],
            selected_older_command_execution_boundary_lineage_basis=_valid_request()["selected_older_command_execution_boundary_lineage_basis"],
            selected_command_report_lineage_basis=_valid_request()["selected_command_report_lineage_basis"],
            selected_command_implementation_boundary_basis=_valid_request()["selected_command_implementation_boundary_basis"],
            selected_command_boundary_basis=_valid_request()["selected_command_boundary_basis"],
            selected_artifact_emission_containment_basis=_valid_request()["selected_artifact_emission_containment_basis"],
            selected_evidence_manifest_basis=_valid_request()["selected_evidence_manifest_basis"],
            selected_portable_verification_basis=_valid_request()["selected_portable_verification_basis"],
            command_output_report_artifact_boundary_scope=SUPPORTED_SCOPE,
        )
        result = _resolve(request)
        self.assertRecordedBoundary(result)
        self.assertFalse(result["non_claims"]["command_output_report_artifact_created"])
        self.assertFalse(result["non_claims"]["report_body_invented"])
        self.assertFalse(result["non_claims"]["command_result_created"])
        self.assertFalse(result["non_claims"]["command_success_created"])


if __name__ == "__main__":
    unittest.main()
