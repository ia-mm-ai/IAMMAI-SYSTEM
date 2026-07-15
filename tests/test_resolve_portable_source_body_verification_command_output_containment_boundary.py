"""Tests for portable source-body verification command output containment boundary.

This suite is bounded to command output containment boundary only. The resolver
may preserve one recorded command execution event and audit-only execution trace
for one future command output containment step, but these tests do not create
command output, capture output, create output/report artifacts, create command
result, create command success, deploy, publish, continue, or authorize follow-on
work.
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

import resolve_portable_source_body_verification_command_output_containment_boundary as resolver
from resolve_portable_source_body_verification_command_output_containment_boundary import (
    build_declared_portable_source_body_verification_command_output_containment_boundary_request,
    build_portable_source_body_verification_command_output_containment_boundary_summary,
    resolve_portable_source_body_verification_command_output_containment_boundary,
    resolve_portable_source_body_verification_command_output_containment_boundary_from_path,
    write_portable_source_body_verification_command_output_containment_boundary_result,
)


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}

QUESTION = resolver.CORE_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_QUESTION
POST_INVOCATION_COMMAND_EXECUTION_OUTCOME = resolver.POST_INVOCATION_COMMAND_EXECUTION_OUTCOME
POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_OUTCOME = resolver.POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_OUTCOME
COMMAND_INVOCATION_OUTCOME = resolver.COMMAND_INVOCATION_OUTCOME
COMMAND_EXECUTION_REVIEW_OUTCOME = resolver.COMMAND_EXECUTION_REVIEW_OUTCOME
REQUEST_CONSUMPTION_OUTCOME = resolver.REQUEST_CONSUMPTION_OUTCOME
V2_ADMITTED_REQUEST_OUTCOME = resolver.V2_ADMITTED_REQUEST_OUTCOME
V2_ADMITTED_REQUEST_VERSION = resolver.V2_ADMITTED_REQUEST_VERSION
V1_PREDECESSOR_RESOLVER_MODULE = resolver.V1_PREDECESSOR_RESOLVER_MODULE
V2_ADMITTED_REQUEST_RESOLVER_MODULE = resolver.V2_ADMITTED_REQUEST_RESOLVER_MODULE
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
RAW_FULL_BODY_SENTINEL = "RAW_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_FULL_BODY_MUST_NOT_RETURN_" * 6

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_command_output_containment_boundary_metadata",
    "declared_command_output_containment_boundary_question",
    "selected_post_invocation_command_execution_basis",
    "selected_post_invocation_command_execution_terminal_summary_basis",
    "selected_post_invocation_command_execution_boundary_basis",
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
    "output_containment_boundary_only_posture",
    "one_future_command_output_containment_step_posture",
    "execution_event_preserved_posture",
    "execution_trace_audit_only_posture",
    "no_command_output_posture",
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
    "command_output_containment_boundary_scope",
    "command_output_containment_boundary_checks",
    "command_output_containment_boundary_statement",
    "command_output_containment_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_command_output_containment_boundary_summary",
)

OPEN_ITEMS = (
    "command_output_containment_boundary_test",
    "command_output_containment_boundary_live_artifact",
    "command_output_step_if_separately_specified",
    "command_output",
    "output_capture",
    "command_output_report_artifact",
    "command_result",
    "command_success",
    "manifest_implementation",
    "checksum_implementation",
    "signature_implementation",
    "source_body_packet_implementation",
    "reproducible_environment_declaration",
    "runtime_hosting",
    "deployment",
    "public_release",
    "source_transfer",
    "source_migration",
    "source_receipt",
    "reception_authorization",
    "derivative_reception",
    "vessel_relation",
    "adoption",
    "authority_creation",
    "currentness_creation",
    "operation_permission",
    "public_readiness",
    "final_completion",
    "continuation",
    "publication_flow",
    "reusable_permission",
    "successor_reception_request",
    "follow_on_work",
)


def _json_text(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=True)


def _false_non_claims() -> dict[str, bool]:
    return {name: False for name in REQUIRED_FALSE_NON_CLAIMS}


def _reference_shape(label: str, **extra: Any) -> dict[str, Any]:
    basis = {
        "basis_label": label,
        "declared": True,
        "basis_reference": f"synthetic://{label}",
        "reference_shaped_basis": True,
        "basis_remains_reference_shaped": True,
        "basis_reference_shape_preserved": True,
        "basis_remains_basis_only": True,
        "basis_is_not_command_output_result_success": True,
        "basis_is_not_authority_currentness_final_completion": True,
        "basis_does_not_authorize_continuation_reusable_permission_follow_on_work": True,
        "basis_does_not_create_deployment_runtime_public_release": True,
        "full_upstream_lineage_preserved": True,
        "upstream_lineage": (
            "v2_admission -> request_consumption -> command_execution_review -> "
            "command_invocation -> post_invocation_command_execution_boundary -> "
            "post_invocation_command_execution -> command_output_containment_boundary"
        ),
        "full_prior_artifact_body_not_emitted": True,
        "raw_full_prior_artifact_body_returned": False,
        "prior_artifacts_mutated": False,
    }
    basis.update(extra)
    return basis


def _post_invocation_execution_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "post_invocation_command_execution",
        result_id="post_invocation_command_execution_reference_review_001",
        result_path="artifacts/synthetic_post_invocation_command_execution_result.json",
        outcome=POST_INVOCATION_COMMAND_EXECUTION_OUTCOME,
        failed_check_count=0,
        passed_check_count=62,
        post_invocation_command_execution_recorded=True,
        bounded_command_execution_event_recorded=True,
        execution_event_recorded=True,
        execution_trace_recorded_as_audit_only=True,
        execution_trace_audit_only=True,
        trace_is_audit_only=True,
        command_output_still_not_created=True,
        command_output_not_created=True,
        command_output_created=False,
        command_result_still_not_created=True,
        command_result_not_created=True,
        command_result_created=False,
        command_success_still_not_created=True,
        command_success_not_created=True,
        command_success_created=False,
        execution_permission_not_created=True,
        execution_approval_not_created=True,
        execution_trace_is_not_output=True,
        execution_trace_is_not_result=True,
        execution_trace_is_not_success=True,
        execution_trace_is_not_source=True,
        execution_trace_is_not_authority=True,
        execution_trace={
            "trace_id": "synthetic-audit-trace",
            "trace_type": "EXECUTION_TRACE_AUDIT_ONLY",
            "execution_event_recorded": True,
            "execution_trace_recorded_as_audit_only": True,
            "command_output_created": False,
            "command_result_created": False,
            "command_success_created": False,
            "trace_is_not_output": True,
            "trace_is_not_result": True,
            "trace_is_not_success": True,
            "trace_is_not_source": True,
            "trace_is_not_authority": True,
        },
        authorization_token_reuse_blocked=True,
        consumed_request_token_remains_closed=True,
        returned_result_containment_preserved=True,
    )
    basis.update(extra)
    return basis


def _post_invocation_terminal_summary_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "post_invocation_command_execution_terminal_summary",
        terminal_summary_declared=True,
        terminal_summary_path="spec/PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_TERMINAL_SUMMARY_V0.md",
        terminal_summary_remains_readability_basis_only=True,
        terminal_summary_does_not_create_command_output=True,
        terminal_summary_does_not_create_command_result=True,
        terminal_summary_does_not_create_command_success=True,
        terminal_summary_does_not_authorize_follow_on_work=True,
    )
    basis.update(extra)
    return basis


def _post_invocation_execution_boundary_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "post_invocation_command_execution_boundary",
        outcome=POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_OUTCOME,
        failed_check_count=0,
        one_future_command_execution_step_declared=True,
        boundary_basis_remains_boundary_basis_only=True,
        boundary_did_not_execute_command=True,
        boundary_did_not_create_command_output=True,
        boundary_did_not_create_command_result=True,
        boundary_did_not_create_command_success=True,
        boundary_did_not_create_authority_currentness_final_completion=True,
        boundary_did_not_authorize_follow_on_work=True,
    )
    basis.update(extra)
    return basis


def _command_invocation_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "command_invocation",
        outcome=COMMAND_INVOCATION_OUTCOME,
        failed_check_count=0,
        bounded_command_invocation_event_recorded=True,
        command_invocation_event_recorded=True,
        authorization_token_spent_exactly_once=True,
        one_shot_authorization_token_spent_exactly_once=True,
        authorization_token_reuse_blocked=True,
        authorization_token_not_reused=True,
        command_invocation_basis_remains_invocation_basis_only=True,
    )
    basis.update(extra)
    return basis


def _command_execution_review_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "command_execution_review",
        outcome=COMMAND_EXECUTION_REVIEW_OUTCOME,
        failed_check_count=0,
        review_basis_only=True,
        review_basis_remains_review_basis_only=True,
        command_output_still_not_created=True,
        command_result_still_not_created=True,
        command_success_still_not_created=True,
    )
    basis.update(extra)
    return basis


def _request_consumption_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "request_consumption",
        outcome=REQUEST_CONSUMPTION_OUTCOME,
        failed_check_count=0,
        request_consumed_exactly_once=True,
        consumption_token_closed=True,
        consumed_request_basis_recorded=True,
        request_consumption_basis_only=True,
    )
    basis.update(extra)
    return basis


def _consumed_request_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "consumed_request",
        consumed_request_basis_declared=True,
        consumed_request_token_remains_closed=True,
        consumed_token_closed=True,
        consumed_request_is_not_reopened=True,
        consumed_request_not_reopened=True,
        consumed_request_basis_is_basis_only=True,
    )
    basis.update(extra)
    return basis


def _v2_admitted_request_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "v2_admitted_request",
        outcome=V2_ADMITTED_REQUEST_OUTCOME,
        result_version=V2_ADMITTED_REQUEST_VERSION,
        failed_check_count=0,
        successor_of=V1_PREDECESSOR_RESOLVER_MODULE,
        successor_reason="preserve returned-result containment and visible predecessor failure lineage",
        resolver_module=V2_ADMITTED_REQUEST_RESOLVER_MODULE,
        successor_metadata_preserved=True,
        returned_result_containment_preserved=True,
        v2_does_not_claim_v1_passed=True,
        v2_successor_does_not_erase_v1=True,
    )
    basis.update(extra)
    return basis


def _v1_predecessor_failure_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "v1_predecessor_failure",
        v1_predecessor_failure_basis_declared=True,
        v1_predecessor_failure_remains_visible=True,
        v1_remains_visible_predecessor_failure_evidence=True,
        visible_predecessor_failure_evidence=True,
        v1_is_not_repaired=True,
        v1_is_not_hidden=True,
        v1_is_not_claimed_passed=True,
        v2_successor_does_not_erase_v1=True,
        predecessor_failure_evidence_is_lineage_evidence_only=True,
    )
    basis.update(extra)
    return basis


def _older_command_execution_boundary_lineage_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "older_command_execution_boundary_lineage",
        lineage_basis_declared=True,
        basis_remains_prior_scaffolding_only=True,
        lineage_basis_not_treated_as_current_execution=True,
        older_command_execution_boundary_lineage_treated_as_current_execution=False,
        command_output_created=False,
        command_result_created=False,
        command_success_created=False,
    )
    basis.update(extra)
    return basis


def _generic_prior_basis(label: str, **extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        label,
        basis_is_not_command_output=True,
        basis_is_not_command_result=True,
        basis_is_not_command_success=True,
        basis_is_not_authority=True,
        basis_is_not_currentness=True,
        basis_is_not_final_completion=True,
        basis_is_not_continuation=True,
        basis_is_not_follow_on_work=True,
    )
    basis.update(extra)
    return basis


def _posture(label: str, **extra: Any) -> dict[str, Any]:
    posture = {
        "posture_label": label,
        "declared": True,
        "posture_declared": True,
        "command_output_created": False,
        "output_capture_created": False,
        "command_output_report_artifact_created": False,
        "command_result_created": False,
        "command_success_created": False,
        "command_output_not_created": True,
        "output_capture_not_created": True,
        "command_output_report_artifact_not_created": True,
        "command_result_not_created": True,
        "command_success_not_created": True,
        "command_output_not_source": True,
        "command_result_not_authority": True,
        "command_success_not_currentness": True,
        "command_success_not_final_completion": True,
        "authorization_token_reuse_blocked": True,
        "authorization_token_reused": False,
        "consumed_request_token_remains_closed": True,
        "consumed_request_not_reopened": True,
        "consumed_request_reopened": False,
        "returned_result_containment_preserved": True,
        "no_raw_full_prior_artifact_body_returned": True,
        "raw_full_prior_artifact_body_returned": False,
    }
    posture.update(extra)
    return posture


def _postures() -> dict[str, dict[str, Any]]:
    return {
        "output_containment_boundary_only_posture": _posture(
            "output_containment_boundary_only",
            output_containment_boundary_only=True,
            command_output_containment_boundary_only=True,
        ),
        "one_future_command_output_containment_step_posture": _posture(
            "one_future_command_output_containment_step",
            one_future_command_output_containment_step_declared=True,
            one_future_command_output_containment_step_only=True,
        ),
        "execution_event_preserved_posture": _posture(
            "execution_event_preserved",
            recorded_command_execution_event_preserved=True,
            execution_event_preserved=True,
        ),
        "execution_trace_audit_only_posture": _posture(
            "execution_trace_audit_only",
            execution_trace_audit_only_preserved=True,
            execution_trace_audit_only=True,
            trace_is_audit_only=True,
        ),
        "no_command_output_posture": _posture("no_command_output", command_output_still_not_created=True),
        "no_output_capture_posture": _posture("no_output_capture", command_output_capture_not_created=True),
        "no_output_report_artifact_posture": _posture(
            "no_output_report_artifact",
            output_report_artifact_not_created=True,
        ),
        "no_command_result_posture": _posture("no_command_result", command_result_still_not_created=True),
        "no_command_success_posture": _posture("no_command_success", command_success_still_not_created=True),
        "no_output_as_source_posture": _posture("no_output_as_source", output_not_source=True),
        "no_result_as_authority_posture": _posture("no_result_as_authority", result_not_authority=True),
        "no_success_as_currentness_posture": _posture("no_success_as_currentness", success_not_currentness=True),
        "no_final_completion_posture": _posture(
            "no_final_completion",
            no_final_completion=True,
            final_completion_not_claimed=True,
            final_completion_claimed=False,
        ),
        "authorization_token_reuse_blocked_posture": _posture(
            "authorization_token_reuse_blocked",
            authorization_token_not_reused=True,
        ),
        "consumed_token_closed_posture": _posture("consumed_token_closed", consumed_token_closed=True),
        "no_reopen_consumed_request_posture": _posture(
            "no_reopen_consumed_request",
            no_reopen_consumed_request=True,
        ),
        "returned_result_containment_posture": _posture("returned_result_containment"),
    }


def _valid_request(**overrides: Any) -> dict[str, Any]:
    request = {
        "command_output_containment_boundary_request_id": "command_output_containment_boundary_reference_review_001",
        "command_output_containment_boundary_question": QUESTION,
        "command_output_containment_boundary_intent": resolver.INTENT_RECORD,
        "selected_post_invocation_command_execution_basis": _post_invocation_execution_basis(),
        "selected_post_invocation_command_execution_terminal_summary_basis": _post_invocation_terminal_summary_basis(),
        "selected_post_invocation_command_execution_boundary_basis": _post_invocation_execution_boundary_basis(),
        "selected_command_invocation_basis": _command_invocation_basis(),
        "selected_command_execution_review_basis": _command_execution_review_basis(),
        "selected_request_consumption_basis": _request_consumption_basis(),
        "selected_consumed_request_basis": _consumed_request_basis(),
        "selected_v2_admitted_request_basis": _v2_admitted_request_basis(),
        "selected_v1_predecessor_failure_basis": _v1_predecessor_failure_basis(),
        "selected_older_command_execution_boundary_lineage_basis": _older_command_execution_boundary_lineage_basis(),
        "selected_command_report_basis": _generic_prior_basis("command_report"),
        "selected_command_implementation_boundary_basis": _generic_prior_basis("command_implementation_boundary"),
        "selected_command_boundary_basis": _generic_prior_basis("command_boundary"),
        "selected_artifact_emission_containment_basis": _generic_prior_basis("artifact_emission_containment"),
        "selected_evidence_manifest_basis": _generic_prior_basis("evidence_manifest"),
        "selected_portable_verification_basis": _generic_prior_basis("portable_verification"),
        "command_output_containment_boundary_scope": list(SUPPORTED_SCOPE),
        "requested_command_output_containment_boundary_outcome": RECORDED,
        "declared_non_claims": _false_non_claims(),
        "selected_post_invocation_command_execution_result_outcome": POST_INVOCATION_COMMAND_EXECUTION_OUTCOME,
        "selected_post_invocation_command_execution_failed_check_count": 0,
        "selected_post_invocation_command_execution_event_recorded": True,
        "selected_post_invocation_command_execution_trace_audit_only": True,
        "selected_post_invocation_command_execution_output_created": False,
        "selected_post_invocation_command_execution_result_created": False,
        "selected_post_invocation_command_execution_success_created": False,
        "selected_v2_admitted_request_outcome": V2_ADMITTED_REQUEST_OUTCOME,
        "selected_v2_admitted_request_version": V2_ADMITTED_REQUEST_VERSION,
        "selected_v2_failed_check_count": 0,
    }
    request.update(_postures())
    for key, value in overrides.items():
        request[key] = value
    return request


def _resolve(request: dict[str, Any]) -> dict[str, Any]:
    return resolve_portable_source_body_verification_command_output_containment_boundary(
        declared_command_output_containment_boundary_request=request
    )


class CommandOutputContainmentBoundaryTests(unittest.TestCase):
    def assertRecorded(self, result: dict[str, Any]) -> None:
        self.assertIsInstance(result, dict)
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assertIsNone(result["block"]["code"])
        self.assertIsNone(result["block"]["reason"])

        summary = result["portable_source_body_verification_command_output_containment_boundary_summary"]
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertTrue(all(check["passed"] for check in result["command_output_containment_boundary_checks"]))

        statement = result["command_output_containment_boundary_statement"]
        for key in (
            "command_output_containment_boundary_recorded",
            "recorded_command_execution_event_preserved",
            "execution_trace_audit_only_preserved",
            "one_future_command_output_containment_step_declared",
            "command_output_still_not_created",
            "output_capture_not_created",
            "command_output_report_artifact_not_created",
            "command_result_still_not_created",
            "command_success_still_not_created",
            "authorization_token_reuse_blocked",
            "consumed_request_token_remains_closed",
            "v1_predecessor_failure_preserved",
            "returned_result_containment_preserved",
        ):
            self.assertIs(statement[key], True, key)

        non_claims = result["non_claims"]
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)
            self.assertIs(statement[key], False, key)

    def assertBlocked(self, request: dict[str, Any], expected_code: str | tuple[str, ...]) -> dict[str, Any]:
        result = _resolve(request)
        self.assertEqual(result["outcome"], BLOCKED)
        if isinstance(expected_code, tuple):
            self.assertIn(result["block"]["code"], expected_code)
        else:
            self.assertEqual(result["block"]["code"], expected_code)
        self.assertFalse(result["command_output_containment_boundary_statement"]["command_output_created"])
        self.assertFalse(result["command_output_containment_boundary_statement"]["output_capture_created"])
        self.assertFalse(result["command_output_containment_boundary_statement"]["command_output_report_artifact_created"])
        self.assertFalse(result["command_output_containment_boundary_statement"]["command_result_created"])
        self.assertFalse(result["command_output_containment_boundary_statement"]["command_success_created"])
        return result

    def test_recorded_result_shape_and_non_claims(self) -> None:
        result = _resolve(_valid_request())
        self.assertRecorded(result)

        metadata = result["portable_source_body_verification_command_output_containment_boundary_metadata"]
        self.assertTrue(metadata["portable_source_body_verification_command_output_containment_boundary_result_id"])
        self.assertTrue(metadata["portable_source_body_verification_command_output_containment_boundary_result_type"])
        self.assertEqual(
            metadata["portable_source_body_verification_command_output_containment_boundary_result_version"],
            "0.1.0",
        )
        self.assertTrue(metadata["generated_at"])
        self.assertEqual(metadata["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertTrue(metadata["naming_containment"]["short_resolver_filename_used_intentionally"])
        self.assertTrue(metadata["naming_containment"]["full_upstream_lineage_preserved_in_selected_basis"])

    def test_selected_basis_lineage_is_preserved_without_output_promotion(self) -> None:
        result = _resolve(_valid_request())
        self.assertRecorded(result)

        execution = result["selected_post_invocation_command_execution_basis"]
        self.assertEqual(execution["outcome"], POST_INVOCATION_COMMAND_EXECUTION_OUTCOME)
        self.assertEqual(execution["failed_check_count"], 0)
        self.assertTrue(execution["bounded_command_execution_event_recorded"])
        self.assertTrue(execution["execution_trace_recorded_as_audit_only"])
        self.assertTrue(execution["command_output_still_not_created"])
        self.assertTrue(execution["command_result_still_not_created"])
        self.assertTrue(execution["command_success_still_not_created"])
        self.assertTrue(execution["execution_trace_is_not_output"])
        self.assertTrue(execution["execution_trace_is_not_result"])
        self.assertTrue(execution["execution_trace_is_not_success"])
        self.assertTrue(execution["execution_trace_is_not_source"])
        self.assertTrue(execution["execution_trace_is_not_authority"])
        self.assertTrue(execution["basis_remains_reference_shaped"])

        terminal = result["selected_post_invocation_command_execution_terminal_summary_basis"]
        self.assertTrue(terminal["terminal_summary_declared"])
        self.assertTrue(terminal["terminal_summary_remains_readability_basis_only"])
        self.assertTrue(terminal["terminal_summary_does_not_create_command_output"])
        self.assertTrue(terminal["terminal_summary_does_not_create_command_result"])
        self.assertTrue(terminal["terminal_summary_does_not_create_command_success"])
        self.assertTrue(terminal["terminal_summary_does_not_authorize_follow_on_work"])

        boundary = result["selected_post_invocation_command_execution_boundary_basis"]
        self.assertEqual(boundary["outcome"], POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_OUTCOME)
        self.assertTrue(boundary["boundary_basis_remains_boundary_basis_only"])
        self.assertTrue(boundary["boundary_did_not_create_command_output"])
        self.assertTrue(boundary["boundary_did_not_create_command_result"])
        self.assertTrue(boundary["boundary_did_not_create_command_success"])
        self.assertTrue(boundary["boundary_did_not_create_authority_currentness_final_completion"])

        invocation = result["selected_command_invocation_basis"]
        self.assertEqual(invocation["outcome"], COMMAND_INVOCATION_OUTCOME)
        self.assertEqual(invocation["failed_check_count"], 0)
        self.assertTrue(invocation["bounded_command_invocation_event_recorded"])
        self.assertTrue(invocation["authorization_token_spent_exactly_once"])
        self.assertTrue(invocation["authorization_token_reuse_blocked"])

        consumption = result["selected_request_consumption_basis"]
        consumed = result["selected_consumed_request_basis"]
        self.assertTrue(consumption["request_consumed_exactly_once"])
        self.assertTrue(consumption["consumption_token_closed"])
        self.assertTrue(consumed["consumed_request_token_remains_closed"])
        self.assertTrue(consumed["consumed_request_not_reopened"])

        v2 = result["selected_v2_admitted_request_basis"]
        v1 = result["selected_v1_predecessor_failure_basis"]
        self.assertEqual(v2["outcome"], V2_ADMITTED_REQUEST_OUTCOME)
        self.assertEqual(v2["result_version"], V2_ADMITTED_REQUEST_VERSION)
        self.assertTrue(v2["returned_result_containment_preserved"])
        self.assertTrue(v1["v1_predecessor_failure_remains_visible"])
        self.assertTrue(v1["v1_is_not_repaired"])
        self.assertTrue(v1["v1_is_not_hidden"])
        self.assertTrue(v1["v1_is_not_claimed_passed"])

        lineage = result["selected_older_command_execution_boundary_lineage_basis"]
        self.assertTrue(lineage["basis_remains_prior_scaffolding_only"])
        self.assertTrue(lineage["lineage_basis_not_treated_as_current_execution"])
        self.assertFalse(lineage["older_command_execution_boundary_lineage_treated_as_current_execution"])

    def test_check_records_are_explicit_and_cover_boundary_posture(self) -> None:
        result = _resolve(_valid_request())
        self.assertRecorded(result)
        checks = result["command_output_containment_boundary_checks"]
        required_fields = {"check_name", "passed", "expected_posture", "actual_posture", "block_code", "failure_code"}
        for check in checks:
            self.assertTrue(required_fields.issubset(check), check)

        names = {check["check_name"] for check in checks}
        expected_names = {
            "command output containment boundary question declared",
            "command output containment boundary intent supported",
            "post-invocation command execution terminal summary basis declared",
            "post-invocation command execution live artifact basis declared",
            "post-invocation command execution outcome recorded",
            "post-invocation command execution failed check count zero",
            "post-invocation command execution event recorded",
            "post-invocation command execution trace audit-only",
            "post-invocation command execution command output not created",
            "post-invocation command execution command result not created",
            "post-invocation command execution command success not created",
            "command invocation basis declared",
            "command execution review basis declared",
            "request consumption basis declared",
            "consumed request basis declared",
            "output-containment-boundary-only posture declared",
            "one-future-command-output-containment-step posture declared",
            "execution-event-preserved posture declared",
            "execution-trace-audit-only posture declared",
            "no-command-output posture declared",
            "no-output-capture posture declared",
            "no-output-report-artifact posture declared",
            "no-command-result posture declared",
            "no-command-success posture declared",
            "no-output-as-source posture declared",
            "no-result-as-authority posture declared",
            "no-success-as-currentness posture declared",
            "no-final-completion posture declared",
            "execution trace not output result success source authority",
            "raw full prior artifact body not emitted",
            "non-claims remain false",
        }
        self.assertTrue(expected_names.issubset(names))

    def test_non_meaning_and_what_remains_open_are_preserved(self) -> None:
        result = _resolve(_valid_request())
        non_meaning = result["command_output_containment_boundary_non_meaning"]
        for suffix in (
            "command_output_exists",
            "output_was_captured",
            "command_output_report_artifact_exists",
            "command_result_exists",
            "command_success_exists",
            "execution_trace_is_output",
            "execution_trace_is_result",
            "execution_trace_is_success",
            "execution_trace_is_source",
            "execution_trace_is_authority",
            "output_is_source",
            "result_is_authority",
            "success_is_currentness",
            "success_is_final_completion",
            "consumed_request_token_reopened",
            "authorization_token_reusable",
            "v1_repaired_hidden_or_passed",
            "deployment_runtime_public_release",
            "public_readiness",
            "final_completion",
            "continuation",
            "reusable_permission",
            "derivative_reception",
            "vessel_relation",
            "another_reception_request",
            "follow_on_work",
        ):
            self.assertIs(non_meaning[f"command_output_containment_boundary_does_not_mean_{suffix}"], True)

        remains_open = result["what_remains_open"]
        for item in OPEN_ITEMS:
            self.assertIn(item, remains_open["open_items"])
        self.assertTrue(remains_open["open_means_not_scheduled"])
        self.assertTrue(remains_open["open_means_not_authorized"])
        self.assertTrue(remains_open["open_means_not_executed"])

    def test_requires_additional_basis_and_not_recorded_are_bounded(self) -> None:
        requires_request = _valid_request(
            requested_command_output_containment_boundary_outcome=REQUIRES_ADDITIONAL_BASIS,
            additional_basis_context={"missing": "separate output containment evidence"},
        )
        requires_result = _resolve(requires_request)
        self.assertEqual(requires_result["outcome"], REQUIRES_ADDITIONAL_BASIS)
        self.assertTrue(requires_result["additional_basis_required"]["requires_additional_basis"])
        self.assertEqual(
            requires_result["additional_basis_required"]["additional_basis_context"]["missing"],
            "separate output containment evidence",
        )
        self.assertTrue(requires_result["additional_basis_required"]["missing_basis_not_scheduled"])
        self.assertTrue(requires_result["additional_basis_required"]["missing_basis_not_authorized"])
        self.assertTrue(requires_result["additional_basis_required"]["missing_basis_not_executed"])
        self.assertFalse(requires_result["non_claims"]["command_output_created"])
        self.assertFalse(requires_result["non_claims"]["follow_on_work_authorized"])

        not_recorded_request = _valid_request(
            requested_command_output_containment_boundary_outcome=NOT_RECORDED,
            not_recorded_basis={"reason": "readable review did not record containment boundary"},
        )
        not_recorded_result = _resolve(not_recorded_request)
        self.assertEqual(not_recorded_result["outcome"], NOT_RECORDED)
        self.assertTrue(not_recorded_result["not_recorded_basis"]["not_recorded"])
        self.assertEqual(
            not_recorded_result["not_recorded_basis"]["not_recorded_basis"]["reason"],
            "readable review did not record containment boundary",
        )
        self.assertTrue(not_recorded_result["not_recorded_basis"]["not_recorded_does_not_authorize_next_work"])
        self.assertFalse(not_recorded_result["non_claims"]["command_result_created"])
        self.assertFalse(not_recorded_result["non_claims"]["command_success_created"])

    def test_summary_helper_preserves_key_fields(self) -> None:
        result = _resolve(_valid_request())
        summary = build_portable_source_body_verification_command_output_containment_boundary_summary(result)
        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(summary["request_id"], "command_output_containment_boundary_reference_review_001")
        self.assertEqual(summary["question"], QUESTION)
        self.assertEqual(summary["intent"], resolver.INTENT_RECORD)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertTrue(summary["command_output_containment_boundary_recorded"])
        self.assertTrue(summary["recorded_command_execution_event_preserved"])
        self.assertTrue(summary["execution_trace_audit_only_preserved"])
        self.assertTrue(summary["one_future_output_containment_step_declared"])
        self.assertTrue(summary["command_output_still_not_created"])
        self.assertTrue(summary["output_capture_not_created"])
        self.assertTrue(summary["output_report_artifact_not_created"])
        self.assertTrue(summary["command_result_still_not_created"])
        self.assertTrue(summary["command_success_still_not_created"])
        self.assertEqual(summary["selected_post_invocation_execution_outcome"], POST_INVOCATION_COMMAND_EXECUTION_OUTCOME)
        self.assertEqual(summary["selected_post_invocation_execution_failed_check_count"], 0)
        self.assertEqual(summary["selected_v2_admitted_request_outcome"], V2_ADMITTED_REQUEST_OUTCOME)
        self.assertEqual(summary["selected_v2_admitted_request_version"], V2_ADMITTED_REQUEST_VERSION)
        self.assertEqual(summary["selected_v2_admitted_request_failed_check_count"], 0)
        self.assertTrue(summary["execution_trace_not_output_result_success_source_authority"])
        self.assertTrue(summary["output_not_source"])
        self.assertTrue(summary["result_not_authority"])
        self.assertTrue(summary["success_not_currentness"])
        self.assertTrue(summary["success_not_final_completion"])
        self.assertTrue(summary["older_command_execution_boundary_lineage_not_treated_as_current_execution"])
        self.assertTrue(summary["no_raw_full_prior_artifact_body"])
        self.assertTrue(summary["no_artifact_mutation"])
        self.assertTrue(summary["no_deployment_runtime_public_release"])
        self.assertTrue(summary["no_operation_public_readiness_final_completion"])
        self.assertTrue(summary["no_continuation_publication_reusable_follow_on"])
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(summary["key_non_claims"][key], False)

    def test_request_builder_preserves_basis_and_does_not_infer_output(self) -> None:
        postures = _postures()
        built = build_declared_portable_source_body_verification_command_output_containment_boundary_request(
            "builder_request_001",
            QUESTION,
            _post_invocation_execution_basis(),
            _post_invocation_terminal_summary_basis(),
            _post_invocation_execution_boundary_basis(),
            _command_invocation_basis(),
            _command_execution_review_basis(),
            _request_consumption_basis(),
            _consumed_request_basis(),
            _v2_admitted_request_basis(),
            _v1_predecessor_failure_basis(),
            _older_command_execution_boundary_lineage_basis(),
            _generic_prior_basis("command_report"),
            _generic_prior_basis("command_implementation_boundary"),
            _generic_prior_basis("command_boundary"),
            _generic_prior_basis("artifact_emission_containment"),
            _generic_prior_basis("evidence_manifest"),
            _generic_prior_basis("portable_verification"),
            postures["output_containment_boundary_only_posture"],
            postures["one_future_command_output_containment_step_posture"],
            postures["execution_event_preserved_posture"],
            postures["execution_trace_audit_only_posture"],
            postures["no_command_output_posture"],
            postures["no_output_capture_posture"],
            postures["no_output_report_artifact_posture"],
            postures["no_command_result_posture"],
            postures["no_command_success_posture"],
            postures["no_output_as_source_posture"],
            postures["no_result_as_authority_posture"],
            postures["no_success_as_currentness_posture"],
            postures["no_final_completion_posture"],
            postures["authorization_token_reuse_blocked_posture"],
            postures["consumed_token_closed_posture"],
            postures["no_reopen_consumed_request_posture"],
            postures["returned_result_containment_posture"],
            list(SUPPORTED_SCOPE),
            selected_post_invocation_command_execution_result_outcome=POST_INVOCATION_COMMAND_EXECUTION_OUTCOME,
            selected_post_invocation_command_execution_failed_check_count=0,
            selected_post_invocation_command_execution_event_recorded=True,
            selected_post_invocation_command_execution_trace_audit_only=True,
            selected_post_invocation_command_execution_output_created=False,
            selected_post_invocation_command_execution_result_created=False,
            selected_post_invocation_command_execution_success_created=False,
            selected_v2_admitted_request_outcome=V2_ADMITTED_REQUEST_OUTCOME,
            selected_v2_admitted_request_version=V2_ADMITTED_REQUEST_VERSION,
            selected_v2_failed_check_count=0,
            additional_basis_context={"context": "preserved"},
            not_recorded_basis={"reason": "preserved"},
        )
        self.assertEqual(built["command_output_containment_boundary_request_id"], "builder_request_001")
        self.assertEqual(built["command_output_containment_boundary_question"], QUESTION)
        self.assertEqual(built["selected_post_invocation_command_execution_basis"]["outcome"], POST_INVOCATION_COMMAND_EXECUTION_OUTCOME)
        self.assertEqual(built["selected_v2_admitted_request_basis"]["outcome"], V2_ADMITTED_REQUEST_OUTCOME)
        self.assertEqual(built["additional_basis_context"]["context"], "preserved")
        self.assertEqual(built["not_recorded_basis"]["reason"], "preserved")
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(built["declared_non_claims"][key], False)
        self.assertFalse(built["declared_non_claims"]["command_output_created"])
        self.assertFalse(built["declared_non_claims"]["output_capture_created"])
        self.assertFalse(built["declared_non_claims"]["command_output_report_artifact_created"])
        self.assertFalse(built["declared_non_claims"]["command_result_created"])
        self.assertFalse(built["declared_non_claims"]["command_success_created"])

        result = _resolve(built)
        self.assertRecorded(result)

    def test_path_based_request_and_write_behavior_are_additive(self) -> None:
        request = _valid_request()
        mapping_result = _resolve(request)
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            request_path = temp_root / "request.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")
            path_result = resolve_portable_source_body_verification_command_output_containment_boundary_from_path(
                request_path
            )
            self.assertEqual(path_result["outcome"], RECORDED)
            self.assertEqual(set(mapping_result.keys()), set(path_result.keys()))
            metadata = path_result["portable_source_body_verification_command_output_containment_boundary_metadata"]
            self.assertEqual(metadata["declared_command_output_containment_boundary_request_path"], str(request_path))

            malformed_path = temp_root / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            malformed = resolve_portable_source_body_verification_command_output_containment_boundary_from_path(
                malformed_path
            )
            self.assertEqual(malformed["outcome"], BLOCKED)
            self.assertEqual(malformed["block"]["code"], "DECLARED_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_REQUEST_MALFORMED")

            array_path = temp_root / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolve_portable_source_body_verification_command_output_containment_boundary_from_path(
                array_path
            )
            self.assertEqual(array_result["outcome"], BLOCKED)
            self.assertEqual(array_result["block"]["code"], "DECLARED_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_REQUEST_MALFORMED")

            missing = resolve_portable_source_body_verification_command_output_containment_boundary_from_path(
                temp_root / "missing.json"
            )
            self.assertEqual(missing["outcome"], BLOCKED)
            self.assertEqual(missing["block"]["code"], "DECLARED_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_REQUEST_UNREADABLE")

            explicit_output = temp_root / "nested" / "result.json"
            written = write_portable_source_body_verification_command_output_containment_boundary_result(
                mapping_result,
                explicit_output,
            )
            self.assertEqual(written, explicit_output)
            self.assertTrue(written.exists())
            self.assertEqual(json.loads(written.read_text(encoding="utf-8"))["outcome"], RECORDED)

            patched_root = temp_root / "bounded_command_output_containment_boundary_root"
            with patch.object(
                resolver,
                "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_ROOT",
                patched_root,
            ):
                first = write_portable_source_body_verification_command_output_containment_boundary_result(mapping_result)
                second = write_portable_source_body_verification_command_output_containment_boundary_result(mapping_result)
            self.assertEqual(first.parent, patched_root)
            self.assertEqual(second.parent, patched_root)
            self.assertNotEqual(first, second)
            self.assertTrue(second.stem.endswith("_001"))
            self.assertNotIn("post_invocation_command_execution_boundary", str(first))
            self.assertNotIn("command_invocation", str(first))
            self.assertNotIn("deployment", str(first))

    def test_reference_shaped_containment_blocks_raw_full_artifact_body(self) -> None:
        request = _valid_request()
        request["selected_post_invocation_command_execution_basis"]["full_artifact_body"] = RAW_FULL_BODY_SENTINEL
        result = self.assertBlocked(request, "FULL_PRIOR_ARTIFACT_BODY_EMITTED")
        self.assertNotIn(RAW_FULL_BODY_SENTINEL, _json_text(result))
        self.assertIn("omitted", _json_text(result))
        self.assertFalse(result["non_claims"]["command_output_created"])
        self.assertFalse(result["non_claims"]["output_capture_created"])
        self.assertFalse(result["non_claims"]["command_result_created"])
        self.assertFalse(result["non_claims"]["command_success_created"])

    def test_execution_trace_overread_blocks_without_mutation(self) -> None:
        request = _valid_request(execution_trace_treated_as_output=True)
        before = copy.deepcopy(request)
        result = self.assertBlocked(request, "EXECUTION_TRACE_TREATED_AS_OUTPUT")
        self.assertEqual(request, before)
        self.assertFalse(result["non_claims"]["prior_artifacts_mutated"])

    def test_resolver_does_not_mutate_inputs_or_selected_basis(self) -> None:
        request = _valid_request()
        before = copy.deepcopy(request)
        first = _resolve(request)
        second = _resolve(request)
        self.assertEqual(request, before)
        self.assertEqual(first["outcome"], RECORDED)
        self.assertEqual(second["outcome"], RECORDED)
        for key in (
            "selected_post_invocation_command_execution_basis",
            "selected_post_invocation_command_execution_terminal_summary_basis",
            "selected_post_invocation_command_execution_boundary_basis",
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
            "output_containment_boundary_only_posture",
            "one_future_command_output_containment_step_posture",
            "execution_event_preserved_posture",
            "execution_trace_audit_only_posture",
            "command_output_containment_boundary_scope",
        ):
            self.assertEqual(request[key], before[key], key)

    def test_malformed_missing_and_explicit_block_requests_block(self) -> None:
        explicit = _valid_request(command_output_containment_boundary_intent=resolver.INTENT_BLOCK)
        self.assertBlocked(explicit, "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_BLOCKED_BY_REQUEST")

        missing = resolve_portable_source_body_verification_command_output_containment_boundary()
        self.assertEqual(missing["outcome"], BLOCKED)
        self.assertEqual(missing["block"]["code"], "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_QUESTION_UNDECLARED")

        malformed = resolve_portable_source_body_verification_command_output_containment_boundary(
            declared_command_output_containment_boundary_request=["not", "a", "mapping"]  # type: ignore[arg-type]
        )
        self.assertEqual(malformed["outcome"], BLOCKED)
        self.assertEqual(malformed["block"]["code"], "DECLARED_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_REQUEST_MALFORMED")

    def test_required_basis_and_posture_blocking_cases(self) -> None:
        cases: tuple[tuple[str, Callable[[dict[str, Any]], None], str], ...] = (
            (
                "missing execution basis",
                lambda request: request.pop("selected_post_invocation_command_execution_basis"),
                "POST_INVOCATION_COMMAND_EXECUTION_BASIS_MISSING",
            ),
            (
                "execution not recorded",
                lambda request: request.__setitem__(
                    "selected_post_invocation_command_execution_result_outcome",
                    "PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_NOT_RECORDED",
                ),
                "POST_INVOCATION_COMMAND_EXECUTION_NOT_RECORDED",
            ),
            (
                "execution failed checks",
                lambda request: request.__setitem__("selected_post_invocation_command_execution_failed_check_count", 1),
                "POST_INVOCATION_COMMAND_EXECUTION_FAILED_CHECKS_PRESENT",
            ),
            (
                "execution event not recorded",
                lambda request: request.__setitem__("selected_post_invocation_command_execution_event_recorded", False),
                "POST_INVOCATION_COMMAND_EXECUTION_EVENT_NOT_RECORDED",
            ),
            (
                "trace not audit only",
                lambda request: request.__setitem__("selected_post_invocation_command_execution_trace_audit_only", False),
                "POST_INVOCATION_COMMAND_EXECUTION_TRACE_NOT_AUDIT_ONLY",
            ),
            (
                "command output already created",
                lambda request: request.__setitem__("selected_post_invocation_command_execution_output_created", True),
                "COMMAND_OUTPUT_ALREADY_CREATED",
            ),
            (
                "command result already created",
                lambda request: request.__setitem__("selected_post_invocation_command_execution_result_created", True),
                "COMMAND_RESULT_ALREADY_CREATED",
            ),
            (
                "command success already created",
                lambda request: request.__setitem__("selected_post_invocation_command_execution_success_created", True),
                "COMMAND_SUCCESS_ALREADY_CREATED",
            ),
            (
                "missing v2 basis",
                lambda request: request.pop("selected_v2_admitted_request_basis"),
                "V2_ADMITTED_REQUEST_BASIS_MISSING",
            ),
            (
                "v2 failed checks",
                lambda request: request.__setitem__("selected_v2_failed_check_count", 1),
                "V2_ADMITTED_REQUEST_FAILED_CHECKS_PRESENT",
            ),
            (
                "missing v1 basis",
                lambda request: request.pop("selected_v1_predecessor_failure_basis"),
                "V1_PREDECESSOR_FAILURE_BASIS_MISSING",
            ),
            (
                "v2 repairs v1",
                lambda request: request["selected_v2_admitted_request_basis"].__setitem__(
                    "v2_treated_as_repairing_v1",
                    True,
                ),
                "V2_TREATED_AS_REPAIRING_V1",
            ),
            (
                "v1 hidden",
                lambda request: request["selected_v1_predecessor_failure_basis"].__setitem__("v1_hidden", True),
                "V1_FAILURE_HIDDEN",
            ),
            (
                "v1 claimed passed",
                lambda request: request["selected_v1_predecessor_failure_basis"].__setitem__("v1_claimed_passed", True),
                "V1_CLAIMED_PASSED",
            ),
            (
                "lineage current execution",
                lambda request: request["selected_older_command_execution_boundary_lineage_basis"].__setitem__(
                    "older_command_execution_boundary_lineage_treated_as_current_execution",
                    True,
                ),
                "OLDER_COMMAND_EXECUTION_BOUNDARY_LINEAGE_TREATED_AS_CURRENT_EXECUTION",
            ),
            (
                "missing command report",
                lambda request: request.pop("selected_command_report_basis"),
                "COMMAND_REPORT_BASIS_MISSING",
            ),
            (
                "missing implementation boundary",
                lambda request: request.pop("selected_command_implementation_boundary_basis"),
                "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING",
            ),
            (
                "missing command boundary",
                lambda request: request.pop("selected_command_boundary_basis"),
                "COMMAND_BOUNDARY_BASIS_MISSING",
            ),
            (
                "missing containment",
                lambda request: request.pop("selected_artifact_emission_containment_basis"),
                "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING",
            ),
            (
                "missing evidence manifest",
                lambda request: request.pop("selected_evidence_manifest_basis"),
                "EVIDENCE_MANIFEST_BASIS_MISSING",
            ),
            (
                "missing portable verification",
                lambda request: request.pop("selected_portable_verification_basis"),
                "PORTABLE_VERIFICATION_BASIS_MISSING",
            ),
            (
                "missing posture",
                lambda request: request.pop("no_command_output_posture"),
                "NO_COMMAND_OUTPUT_POSTURE_MISSING",
            ),
            (
                "unsupported scope",
                lambda request: request["command_output_containment_boundary_scope"].append("UNSUPPORTED_SCOPE"),
                "UNSUPPORTED_COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_SCOPE",
            ),
        )
        for name, mutator, expected in cases:
            with self.subTest(name=name):
                request = _valid_request()
                mutator(request)
                self.assertBlocked(request, expected)

    def test_collapse_flags_block_without_creating_output_result_success(self) -> None:
        cases: tuple[tuple[str, str | tuple[str, ...]], ...] = (
            ("command_output_created", "COMMAND_OUTPUT_ALREADY_CREATED"),
            ("output_capture_created", "OUTPUT_CAPTURE_ALREADY_CREATED"),
            ("command_output_report_artifact_created", "COMMAND_OUTPUT_REPORT_ARTIFACT_ALREADY_CREATED"),
            ("command_result_created", "COMMAND_RESULT_ALREADY_CREATED"),
            ("command_success_created", "COMMAND_SUCCESS_ALREADY_CREATED"),
            ("execution_trace_treated_as_result", ("EXECUTION_TRACE_TREATED_AS_OUTPUT", "EXECUTION_TRACE_TREATED_AS_RESULT")),
            ("execution_trace_treated_as_success", ("EXECUTION_TRACE_TREATED_AS_OUTPUT", "EXECUTION_TRACE_TREATED_AS_SUCCESS")),
            ("execution_trace_treated_as_source", ("EXECUTION_TRACE_TREATED_AS_OUTPUT", "EXECUTION_TRACE_TREATED_AS_SOURCE")),
            ("execution_trace_treated_as_authority", ("EXECUTION_TRACE_TREATED_AS_OUTPUT", "EXECUTION_TRACE_TREATED_AS_AUTHORITY")),
            ("command_output_became_source", "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
            ("command_result_became_authority", "COMMAND_RESULT_TREATED_AS_AUTHORITY"),
            ("command_success_created_currentness", "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
            ("command_success_claimed_final_completion", "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
            ("authorization_token_reused", "AUTHORIZATION_TOKEN_REUSED"),
            ("consumed_request_reopened", "CONSUMED_REQUEST_REOPENED"),
            ("artifacts_mutated", "ARTIFACTS_MUTATED"),
            ("deployment_created", "DEPLOYMENT_CREATED"),
            ("runtime_hosting_created", "RUNTIME_HOSTING_CREATED"),
            ("public_release_created", "PUBLIC_RELEASE_CREATED"),
            ("operation_permission_created", "OPERATION_CREATED"),
            ("public_launch_readiness_created", "PUBLIC_READINESS_CREATED"),
            ("final_completion_claimed", "FINAL_COMPLETION_CLAIMED"),
            ("continuation_authorized", "CONTINUATION_AUTHORIZED"),
            ("reusable_permission_created", "REUSABLE_PERMISSION_CREATED"),
            ("derivative_reception_authorized", "DERIVATIVE_RECEPTION_AUTHORIZED"),
            ("vessel_relation_authorized", "VESSEL_RELATION_AUTHORIZED"),
            ("another_reception_request_authorized", "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"),
            ("follow_on_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
        )
        for flag, expected in cases:
            with self.subTest(flag=flag):
                request = _valid_request(**{flag: True})
                self.assertBlocked(request, expected)

    def test_mutation_replay_merge_and_non_claim_failures_block(self) -> None:
        for flag in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(flag=flag):
                self.assertBlocked(_valid_request(**{flag: True}), "MUTATION_REPLAY_OR_MERGE_DETECTED")

        missing_non_claim = _valid_request()
        missing_non_claim["declared_non_claims"].pop("command_output_created")
        self.assertBlocked(missing_non_claim, "NON_CLAIM_MISSING_OR_FLIPPED")

        flipped_non_claim = _valid_request()
        flipped_non_claim["declared_non_claims"]["command_output_created"] = True
        self.assertBlocked(
            flipped_non_claim,
            ("COMMAND_OUTPUT_ALREADY_CREATED", "NON_CLAIM_MISSING_OR_FLIPPED"),
        )

    def test_resolver_module_exposes_no_execution_libraries_or_cli_surface(self) -> None:
        self.assertNotIn("subprocess", resolver.__dict__)
        self.assertNotIn("os", resolver.__dict__)
        self.assertNotIn("socket", resolver.__dict__)
        self.assertNotIn("urllib", resolver.__dict__)
        result = _resolve(_valid_request())
        self.assertRecorded(result)
        self.assertNotIn("stdout", _json_text(result))
        self.assertNotIn("stderr", _json_text(result))
        self.assertNotIn("process_output", _json_text(result))


if __name__ == "__main__":
    unittest.main()
