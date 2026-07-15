"""Tests for portable source-body verification post-invocation command execution.

This suite is bounded to post-invocation command execution only. The resolver
may record one declared bounded command execution event downstream of recorded
command invocation and post-invocation execution boundary, but these tests do
not run a real command, create command output, create command result, create
command success, create execution permission, create execution approval,
create standing or repeat execution lanes, reopen consumed request state,
reuse authorization, deploy, publish, continue, or authorize follow-on work.
"""

from __future__ import annotations

import copy
import json
import os
import subprocess
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

import resolve_portable_source_body_verification_post_invocation_command_execution as resolver
from resolve_portable_source_body_verification_post_invocation_command_execution import (
    build_declared_portable_source_body_verification_post_invocation_command_execution_request,
    build_portable_source_body_verification_post_invocation_command_execution_summary,
    resolve_portable_source_body_verification_post_invocation_command_execution,
    resolve_portable_source_body_verification_post_invocation_command_execution_from_path,
    write_portable_source_body_verification_post_invocation_command_execution_result,
)


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}

QUESTION = resolver.CORE_POST_INVOCATION_COMMAND_EXECUTION_QUESTION
BOUNDARY_OUTCOME = resolver.POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_OUTCOME
COMMAND_INVOCATION_OUTCOME = resolver.COMMAND_INVOCATION_OUTCOME
COMMAND_EXECUTION_REVIEW_OUTCOME = resolver.COMMAND_EXECUTION_REVIEW_OUTCOME
REQUEST_CONSUMPTION_OUTCOME = resolver.REQUEST_CONSUMPTION_OUTCOME
V2_ADMITTED_REQUEST_OUTCOME = resolver.V2_ADMITTED_REQUEST_OUTCOME
V2_ADMITTED_REQUEST_VERSION = resolver.V2_ADMITTED_REQUEST_VERSION
V1_PREDECESSOR_RESOLVER_MODULE = resolver.V1_PREDECESSOR_RESOLVER_MODULE
V2_ADMITTED_REQUEST_RESOLVER_MODULE = resolver.V2_ADMITTED_REQUEST_RESOLVER_MODULE
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_POST_INVOCATION_COMMAND_EXECUTION_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
RAW_FULL_BODY_SENTINEL = "RAW_POST_INVOCATION_COMMAND_EXECUTION_FULL_BODY_MUST_NOT_RETURN_" * 6

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_post_invocation_command_execution_metadata",
    "declared_post_invocation_command_execution_question",
    "selected_post_invocation_command_execution_boundary_basis",
    "selected_post_invocation_command_execution_boundary_terminal_summary_basis",
    "selected_command_invocation_basis",
    "selected_command_invocation_terminal_summary_basis",
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
    "post_invocation_command_execution_only_posture",
    "one_bounded_command_execution_event_posture",
    "execution_trace_audit_only_posture",
    "no_command_output_posture",
    "no_command_result_posture",
    "no_command_success_posture",
    "no_execution_permission_posture",
    "no_execution_approval_posture",
    "no_standing_execution_lane_posture",
    "no_repeat_execution_permission_posture",
    "authorization_token_reuse_blocked_posture",
    "consumed_token_closed_posture",
    "no_reopen_consumed_request_posture",
    "returned_result_containment_posture",
    "post_invocation_command_execution_scope",
    "post_invocation_command_execution_checks",
    "post_invocation_command_execution_statement",
    "post_invocation_command_execution_non_meaning",
    "execution_trace",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_post_invocation_command_execution_summary",
)

OPEN_ITEMS = (
    "post_invocation_command_execution_test",
    "post_invocation_command_execution_live_artifact",
    "command_output_boundary_or_output_containment_if_separately_specified",
    "command_output",
    "command_result",
    "command_success",
    "command_output_report_artifact_from_live_execution",
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
        "basis_remains_basis_only": True,
        "basis_is_not_command_output_result_success": True,
        "basis_is_not_execution_permission_or_approval": True,
        "basis_is_not_authority_currentness_final_completion": True,
        "basis_does_not_authorize_continuation_reusable_permission_follow_on_work": True,
        "basis_does_not_create_deployment_runtime_public_release": True,
        "full_upstream_lineage_preserved": True,
        "upstream_lineage": (
            "v2_admission -> request_consumption -> command_execution_review -> "
            "command_invocation -> post_invocation_command_execution_boundary -> "
            "post_invocation_command_execution"
        ),
        "full_prior_artifact_body_not_emitted": True,
        "raw_full_prior_artifact_body_returned": False,
        "prior_artifacts_mutated": False,
    }
    basis.update(extra)
    return basis


def _boundary_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "post_invocation_command_execution_boundary",
        result_id="post_invocation_command_execution_boundary_reference_review_001",
        result_path="artifacts/synthetic_post_invocation_command_execution_boundary_result.json",
        outcome=BOUNDARY_OUTCOME,
        failed_check_count=0,
        passed_check_count=99,
        one_future_command_execution_step_declared=True,
        one_future_command_execution_step_posture_declared=True,
        boundary_did_not_execute_command=True,
        boundary_did_not_create_command_output=True,
        boundary_did_not_create_command_result=True,
        boundary_did_not_create_command_success=True,
        boundary_did_not_create_output_result_success=True,
        boundary_did_not_create_execution_permission=True,
        boundary_did_not_create_execution_approval=True,
        boundary_did_not_create_execution_permission_or_approval=True,
        boundary_basis_remains_boundary_basis_only=True,
    )
    basis.update(extra)
    return basis


def _boundary_terminal_summary_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "post_invocation_command_execution_boundary_terminal_summary",
        terminal_summary_declared=True,
        terminal_summary_path=(
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_"
            "BOUNDARY_TERMINAL_SUMMARY_V0.md"
        ),
        terminal_summary_remains_readability_basis_only=True,
        terminal_summary_does_not_execute_command=True,
        terminal_summary_does_not_create_command_output=True,
        terminal_summary_does_not_create_command_result=True,
        terminal_summary_does_not_create_command_success=True,
        terminal_summary_does_not_create_output_result_success=True,
        terminal_summary_does_not_authorize_follow_on_work=True,
    )
    basis.update(extra)
    return basis


def _command_invocation_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "command_invocation",
        result_id="command_invocation_reference_review_001",
        result_path="artifacts/synthetic_command_invocation_result.json",
        outcome=COMMAND_INVOCATION_OUTCOME,
        failed_check_count=0,
        bounded_command_invocation_event_recorded=True,
        command_invocation_event_recorded=True,
        authorization_token_spent_exactly_once=True,
        authorization_token_spent_exactly_once_preserved=True,
        one_shot_authorization_token_spent_exactly_once=True,
        authorization_token_reuse_blocked=True,
        authorization_token_not_reused=True,
        authorization_token_reuse_blocked_preserved=True,
        command_execution_still_not_performed=True,
        command_output_still_not_created=True,
        command_result_still_not_created=True,
        command_success_still_not_created=True,
        execution_permission_not_created=True,
        execution_approval_not_created=True,
        consumed_request_token_remains_closed=True,
        command_invocation_basis_remains_invocation_basis_only=True,
    )
    basis.update(extra)
    return basis


def _command_invocation_terminal_summary_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "command_invocation_terminal_summary",
        terminal_summary_declared=True,
        terminal_summary_path="spec/PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_INVOCATION_TERMINAL_SUMMARY_V0.md",
        terminal_summary_remains_readability_basis_only=True,
        terminal_summary_does_not_create_command_execution=True,
        terminal_summary_does_not_create_command_output=True,
        terminal_summary_does_not_create_command_result=True,
        terminal_summary_does_not_create_command_success=True,
        terminal_summary_does_not_create_output_result_success=True,
        terminal_summary_does_not_authorize_follow_on_work=True,
    )
    basis.update(extra)
    return basis


def _command_execution_review_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "command_execution_review",
        result_id="command_execution_review_reference_review_001",
        result_path="artifacts/synthetic_command_execution_review_result.json",
        outcome=COMMAND_EXECUTION_REVIEW_OUTCOME,
        failed_check_count=0,
        command_execution_review_basis_remains_review_basis_only=True,
        review_basis_remains_review_basis_only=True,
        command_execution_review_did_not_create_command_output=True,
        command_execution_review_did_not_create_command_result=True,
        command_execution_review_did_not_create_command_success=True,
        command_execution_review_did_not_create_output_result_success=True,
    )
    basis.update(extra)
    return basis


def _request_consumption_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "request_consumption",
        result_id="request_consumption_reference_review_001",
        result_path="artifacts/synthetic_request_consumption_result.json",
        outcome=REQUEST_CONSUMPTION_OUTCOME,
        failed_check_count=0,
        request_consumed_exactly_once=True,
        request_consumed=True,
        consumption_token_closed=True,
        consumed_token_closed=True,
        consumed_request_basis_recorded=True,
        request_consumption_basis_only=True,
        request_consumption_basis_does_not_authorize_output_result_success=True,
    )
    basis.update(extra)
    return basis


def _consumed_request_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "consumed_request",
        consumed_request_basis_declared=True,
        consumed_request_basis_recorded=True,
        consumed_request_token_remains_closed=True,
        consumed_request_token_closed=True,
        consumption_token_closed=True,
        consumed_token_closed=True,
        token_closed=True,
        consumed_request_not_reopened=True,
        consumed_request_is_not_reopened=True,
        no_reopen_consumed_request=True,
        request_not_reopened=True,
        consumed_request_basis_only=True,
    )
    basis.update(extra)
    return basis


def _v2_admitted_request_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "v2_admitted_request",
        result_id="v2_admission_reference_review_001",
        result_path="artifacts/synthetic_v2_admission_result.json",
        outcome=V2_ADMITTED_REQUEST_OUTCOME,
        result_version=V2_ADMITTED_REQUEST_VERSION,
        failed_check_count=0,
        successor_of=V1_PREDECESSOR_RESOLVER_MODULE,
        successor_reason="returned-result containment successor",
        resolver_module=V2_ADMITTED_REQUEST_RESOLVER_MODULE,
        successor_metadata_preserved=True,
        v2_successor_metadata_preserved=True,
        returned_result_containment_preserved=True,
        returned_result_containment_posture_preserved=True,
        v2_does_not_claim_v1_passed=True,
        v2_successor_does_not_erase_v1=True,
        v2_successor_does_not_repair_v1=True,
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
        v1_repaired=False,
        v1_hidden=False,
        v1_claimed_passed=False,
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
        older_command_execution_boundary_surfaces_remain_lineage_only=True,
        lineage_basis_is_not_current_execution=True,
        older_command_execution_boundary_lineage_treated_as_current_execution=False,
        command_execution_boundary_lineage_basis_treated_as_current_execution=False,
        lineage_basis_treated_as_current_execution=False,
        current_execution=False,
        command_execution_performed=False,
        command_output_created=False,
        command_result_created=False,
        command_success_created=False,
    )
    basis.update(extra)
    return basis


def _command_basis(label: str, **extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        label,
        basis_remains_reference_shaped=True,
        basis_is_not_command_output_result_success=True,
        basis_is_not_execution_permission_or_approval=True,
        basis_is_not_authority_currentness_final_completion_continuation_follow_on_work=True,
    )
    basis.update(extra)
    return basis


def _posture(label: str, **extra: Any) -> dict[str, Any]:
    posture = {
        "posture_label": label,
        "declared": True,
        "posture_declared": True,
        "basis_remains_basis_only": True,
        "reference_shaped_basis": True,
        "post_invocation_command_execution_only": label == "post_invocation_command_execution_only",
        "post_invocation_command_execution_only_posture_declared": (
            label == "post_invocation_command_execution_only"
        ),
        "one_bounded_command_execution_event_recorded": label == "one_bounded_command_execution_event",
        "one_bounded_command_execution_event_posture_declared": label == "one_bounded_command_execution_event",
        "execution_trace_recorded_as_audit_only": label == "execution_trace_audit_only",
        "execution_trace_audit_only": label == "execution_trace_audit_only",
        "trace_is_audit_only": label == "execution_trace_audit_only",
        "command_output_not_created": True,
        "command_result_not_created": True,
        "command_success_not_created": True,
        "command_output_still_not_created": True,
        "command_result_still_not_created": True,
        "command_success_still_not_created": True,
        "execution_permission_not_created": True,
        "execution_approval_not_created": True,
        "standing_execution_lane_not_created": True,
        "repeat_execution_permission_not_created": True,
        "no_standing_execution_lane": True,
        "no_repeat_execution_permission": True,
        "authorization_token_reuse_blocked": True,
        "authorization_token_not_reused": True,
        "consumed_request_token_remains_closed": True,
        "consumed_token_closed": True,
        "consumed_request_not_reopened": True,
        "no_reopen_consumed_request": True,
        "returned_result_containment_preserved": True,
        "no_raw_full_prior_artifact_body_returned": True,
        "command_output_created": False,
        "command_result_created": False,
        "command_success_created": False,
        "execution_permission_created": False,
        "execution_approval_created": False,
        "standing_execution_lane_created": False,
        "repeat_execution_permission_created": False,
        "authorization_token_reused": False,
        "consumed_request_reopened": False,
    }
    posture.update(extra)
    return posture


def _execution_trace(**extra: Any) -> dict[str, Any]:
    trace = {
        "trace_id": "post_invocation_command_execution_trace_001",
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
    }
    trace.update(extra)
    return trace


def _valid_request(**overrides: Any) -> dict[str, Any]:
    request = {
        "post_invocation_command_execution_request_id": "post_invocation_command_execution_reference_review_001",
        "post_invocation_command_execution_question": QUESTION,
        "post_invocation_command_execution_intent": resolver.INTENT_RECORD,
        "selected_post_invocation_command_execution_boundary_basis": _boundary_basis(),
        "selected_post_invocation_command_execution_boundary_terminal_summary_basis": (
            _boundary_terminal_summary_basis()
        ),
        "selected_command_invocation_basis": _command_invocation_basis(),
        "selected_command_invocation_terminal_summary_basis": _command_invocation_terminal_summary_basis(),
        "selected_command_execution_review_basis": _command_execution_review_basis(),
        "selected_request_consumption_basis": _request_consumption_basis(),
        "selected_consumed_request_basis": _consumed_request_basis(),
        "selected_v2_admitted_request_basis": _v2_admitted_request_basis(),
        "selected_v1_predecessor_failure_basis": _v1_predecessor_failure_basis(),
        "selected_older_command_execution_boundary_lineage_basis": (
            _older_command_execution_boundary_lineage_basis()
        ),
        "selected_command_report_basis": _command_basis("command_report"),
        "selected_command_implementation_boundary_basis": _command_basis("command_implementation_boundary"),
        "selected_command_boundary_basis": _command_basis("command_boundary"),
        "selected_artifact_emission_containment_basis": _command_basis("artifact_emission_containment"),
        "selected_evidence_manifest_basis": _command_basis("evidence_manifest"),
        "selected_portable_verification_basis": _command_basis("portable_verification"),
        "post_invocation_command_execution_only_posture": _posture("post_invocation_command_execution_only"),
        "one_bounded_command_execution_event_posture": _posture("one_bounded_command_execution_event"),
        "execution_trace_audit_only_posture": _posture("execution_trace_audit_only"),
        "no_command_output_posture": _posture("no_command_output"),
        "no_command_result_posture": _posture("no_command_result"),
        "no_command_success_posture": _posture("no_command_success"),
        "no_execution_permission_posture": _posture("no_execution_permission"),
        "no_execution_approval_posture": _posture("no_execution_approval"),
        "no_standing_execution_lane_posture": _posture("no_standing_execution_lane"),
        "no_repeat_execution_permission_posture": _posture("no_repeat_execution_permission"),
        "authorization_token_reuse_blocked_posture": _posture("authorization_token_reuse_blocked"),
        "consumed_token_closed_posture": _posture("consumed_token_closed"),
        "no_reopen_consumed_request_posture": _posture("no_reopen_consumed_request"),
        "returned_result_containment_posture": _posture("returned_result_containment"),
        "post_invocation_command_execution_scope": list(SUPPORTED_SCOPE),
        "execution_trace": _execution_trace(),
        "selected_post_invocation_command_execution_boundary_result_path": "artifact://post_invocation_boundary",
        "selected_post_invocation_command_execution_boundary_result_id": (
            "post_invocation_command_execution_boundary_reference_review_001"
        ),
        "selected_post_invocation_command_execution_boundary_result_outcome": BOUNDARY_OUTCOME,
        "selected_post_invocation_command_execution_boundary_failed_check_count": 0,
        "selected_post_invocation_command_execution_boundary_step_declared": True,
        "selected_command_invocation_result_path": "artifact://command_invocation",
        "selected_command_invocation_result_id": "command_invocation_reference_review_001",
        "selected_command_invocation_result_outcome": COMMAND_INVOCATION_OUTCOME,
        "selected_command_invocation_failed_check_count": 0,
        "selected_command_invocation_event_recorded": True,
        "selected_command_invocation_authorization_token_spent_exactly_once": True,
        "selected_command_invocation_authorization_token_reuse_blocked": True,
        "selected_command_execution_review_result_path": "artifact://command_execution_review",
        "selected_command_execution_review_result_id": "command_execution_review_reference_review_001",
        "selected_command_execution_review_result_outcome": COMMAND_EXECUTION_REVIEW_OUTCOME,
        "selected_command_execution_review_failed_check_count": 0,
        "selected_request_consumption_result_path": "artifact://request_consumption",
        "selected_request_consumption_result_id": "request_consumption_reference_review_001",
        "selected_request_consumption_result_outcome": REQUEST_CONSUMPTION_OUTCOME,
        "selected_request_consumption_failed_check_count": 0,
        "selected_v2_admitted_request_artifact_path": "artifact://v2_admitted_request",
        "selected_v2_admitted_request_artifact_id": "v2_admission_reference_review_001",
        "selected_v2_admitted_request_outcome": V2_ADMITTED_REQUEST_OUTCOME,
        "selected_v2_admitted_request_version": V2_ADMITTED_REQUEST_VERSION,
        "selected_v2_failed_check_count": 0,
        "selected_v2_successor_metadata": {
            "successor_of": V1_PREDECESSOR_RESOLVER_MODULE,
            "successor_reason": "returned-result containment successor",
            "resolver_module": V2_ADMITTED_REQUEST_RESOLVER_MODULE,
        },
        "selected_v1_predecessor_artifact_path": "artifact://v1_predecessor_failure",
        "selected_v1_predecessor_artifact_id": "v1_predecessor_failure_reference_001",
        "selected_v1_predecessor_outcome": "PREDECESSOR_FAILURE_REMAINS_VISIBLE",
        "selected_older_command_execution_boundary_lineage_result_path": "artifact://older_execution_boundary",
        "selected_command_report_path": "artifact://command_report",
        "selected_command_implementation_boundary_result_path": "artifact://command_implementation_boundary",
        "selected_command_boundary_result_path": "artifact://command_boundary",
        "selected_artifact_emission_containment_result_path": "artifact://artifact_emission_containment",
        "selected_evidence_manifest_result_path": "artifact://evidence_manifest",
        "selected_portable_verification_result_path": "artifact://portable_verification",
        "requested_post_invocation_command_execution_outcome": RECORDED,
        "declared_non_claims": _false_non_claims(),
    }
    request.update(copy.deepcopy(overrides))
    return request


def _resolve(request: dict[str, Any]) -> dict[str, Any]:
    return resolve_portable_source_body_verification_post_invocation_command_execution(
        declared_post_invocation_command_execution_request=request
    )


def _failed_count(result: dict[str, Any]) -> int:
    return sum(1 for check in result["post_invocation_command_execution_checks"] if not check["passed"])


class PortableSourceBodyVerificationPostInvocationCommandExecutionTests(unittest.TestCase):
    def assertBlocked(self, result: dict[str, Any], block_code: str) -> None:
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(result["block"]["code"], block_code)

    def assertNoOutputResultSuccessOrFollowOn(self, result: dict[str, Any]) -> None:
        statement = result["post_invocation_command_execution_statement"]
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(statement[key], False, key)
            self.assertIs(result["non_claims"][key], False, key)
        for key in (
            "command_output_created",
            "command_result_created",
            "command_success_created",
            "execution_permission_created",
            "execution_approval_created",
            "standing_execution_lane_created",
            "repeat_execution_permission_created",
            "authorization_token_reused",
            "consumed_request_reopened",
            "execution_treated_as_output",
            "execution_treated_as_result",
            "execution_treated_as_success",
            "execution_trace_treated_as_output",
            "execution_trace_treated_as_result",
            "execution_trace_treated_as_success",
            "execution_trace_treated_as_source",
            "execution_trace_treated_as_authority",
            "v1_repaired",
            "v1_hidden",
            "v1_claimed_passed",
        ):
            self.assertIs(statement[key], False, key)

    def test_recorded_result_shape_statement_metadata_and_non_claims(self) -> None:
        result = _resolve(_valid_request())
        self.assertIsInstance(result, dict)
        self.assertEqual(set(TOP_LEVEL_SECTIONS), set(result))
        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertIsNone(result["block"]["code"])
        self.assertIsNone(result["block"]["reason"])
        self.assertEqual(_failed_count(result), 0)

        metadata = result["portable_source_body_verification_post_invocation_command_execution_metadata"]
        for key in (
            "portable_source_body_verification_post_invocation_command_execution_result_id",
            "portable_source_body_verification_post_invocation_command_execution_result_type",
            "portable_source_body_verification_post_invocation_command_execution_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key], key)
        self.assertEqual(
            metadata["portable_source_body_verification_post_invocation_command_execution_result_version"],
            "0.1.0",
        )
        self.assertEqual(metadata["resolver_module"], "resolve_portable_source_body_verification_post_invocation_command_execution")
        self.assertTrue(metadata["naming_containment"]["short_resolver_filename_used_intentionally"])
        self.assertTrue(metadata["naming_containment"]["full_upstream_lineage_preserved_in_selected_basis"])
        self.assertTrue(metadata["lineage_posture"]["downstream_of_recorded_command_invocation"])
        self.assertTrue(metadata["lineage_posture"]["downstream_of_post_invocation_command_execution_boundary"])

        declared = result["declared_post_invocation_command_execution_question"]
        self.assertEqual(declared["question"], QUESTION)
        self.assertEqual(declared["intent"], resolver.INTENT_RECORD)
        self.assertTrue(declared["post_invocation_command_execution_is_not_command_output"])
        self.assertTrue(declared["post_invocation_command_execution_is_not_command_result"])
        self.assertTrue(declared["post_invocation_command_execution_is_not_command_success"])

        statement = result["post_invocation_command_execution_statement"]
        for key in (
            "post_invocation_command_execution_recorded",
            "bounded_command_execution_event_recorded",
            "execution_trace_recorded_as_audit_only",
            "command_output_still_not_created",
            "command_result_still_not_created",
            "command_success_still_not_created",
            "execution_permission_not_created",
            "execution_approval_not_created",
            "authorization_token_reuse_blocked",
            "consumed_request_token_remains_closed",
            "v1_predecessor_failure_preserved",
            "returned_result_containment_preserved",
        ):
            self.assertIs(statement[key], True, key)
        self.assertNoOutputResultSuccessOrFollowOn(result)

    def test_execution_trace_is_audit_only_and_contains_no_output_result_success_body(self) -> None:
        result = _resolve(_valid_request())
        trace = result["execution_trace"]
        self.assertEqual(trace["trace_type"], "EXECUTION_TRACE_AUDIT_ONLY")
        self.assertTrue(trace["execution_event_recorded"])
        self.assertTrue(trace["execution_trace_recorded_as_audit_only"])
        self.assertIs(trace["command_output_created"], False)
        self.assertIs(trace["command_result_created"], False)
        self.assertIs(trace["command_success_created"], False)
        for key in (
            "trace_is_not_output",
            "trace_is_not_result",
            "trace_is_not_success",
            "trace_is_not_source",
            "trace_is_not_authority",
            "stdout_not_recorded",
            "stderr_not_recorded",
            "process_output_not_recorded",
            "real_command_not_run_by_resolver",
            "subprocess_not_run_by_resolver",
            "network_not_called_by_resolver",
        ):
            self.assertIs(trace[key], True, key)
        for forbidden_key in (
            "stdout",
            "stderr",
            "process_output",
            "command_output",
            "output_body",
            "result_body",
            "success_body",
            "source_body",
            "authority_body",
            "currentness_claim",
            "final_completion_claim",
        ):
            self.assertNotIn(forbidden_key, trace)

    def test_selected_basis_lineage_is_preserved_reference_shaped(self) -> None:
        result = _resolve(_valid_request())
        boundary = result["selected_post_invocation_command_execution_boundary_basis"]
        self.assertEqual(boundary["outcome"], BOUNDARY_OUTCOME)
        self.assertEqual(boundary["failed_check_count"], 0)
        self.assertTrue(boundary["one_future_command_execution_step_declared"])
        self.assertTrue(boundary["boundary_did_not_execute_command"])
        self.assertTrue(boundary["boundary_did_not_create_output_result_success"])
        self.assertTrue(boundary["boundary_did_not_create_execution_permission_or_approval"])
        self.assertTrue(boundary["reference_shaped_basis"])

        invocation = result["selected_command_invocation_basis"]
        self.assertEqual(invocation["outcome"], COMMAND_INVOCATION_OUTCOME)
        self.assertEqual(invocation["failed_check_count"], 0)
        self.assertTrue(invocation["bounded_command_invocation_event_recorded"])
        self.assertTrue(invocation["authorization_token_spent_exactly_once"])
        self.assertTrue(invocation["authorization_token_reuse_blocked"])
        self.assertTrue(invocation["command_execution_still_not_performed"])
        self.assertTrue(invocation["command_output_still_not_created"])
        self.assertTrue(invocation["command_result_still_not_created"])
        self.assertTrue(invocation["command_success_still_not_created"])
        self.assertTrue(invocation["consumed_request_token_remains_closed"])
        self.assertTrue(invocation["reference_shaped_basis"])

        review = result["selected_command_execution_review_basis"]
        self.assertEqual(review["outcome"], COMMAND_EXECUTION_REVIEW_OUTCOME)
        self.assertEqual(review["failed_check_count"], 0)
        self.assertTrue(review["command_execution_review_basis_remains_review_basis_only"])
        self.assertTrue(review["command_execution_review_did_not_create_output_result_success"])

        consumption = result["selected_request_consumption_basis"]
        self.assertEqual(consumption["outcome"], REQUEST_CONSUMPTION_OUTCOME)
        self.assertEqual(consumption["failed_check_count"], 0)
        self.assertTrue(consumption["request_consumed_exactly_once"])
        self.assertTrue(consumption["consumption_token_closed"])
        self.assertTrue(consumption["consumed_request_basis_recorded"])

        consumed = result["selected_consumed_request_basis"]
        self.assertTrue(consumed["consumed_request_token_remains_closed"])
        self.assertTrue(consumed["consumed_request_not_reopened"])
        self.assertTrue(consumed["consumed_request_basis_only"])

        v2 = result["selected_v2_admitted_request_basis"]
        self.assertEqual(v2["outcome"], V2_ADMITTED_REQUEST_OUTCOME)
        self.assertEqual(v2["result_version"], V2_ADMITTED_REQUEST_VERSION)
        self.assertEqual(v2["failed_check_count"], 0)
        self.assertTrue(v2["successor_metadata_preserved"])
        self.assertTrue(v2["returned_result_containment_preserved"])
        self.assertTrue(v2["reference_shaped_basis"])

        v1 = result["selected_v1_predecessor_failure_basis"]
        self.assertTrue(v1["v1_predecessor_failure_remains_visible"])
        self.assertTrue(v1["v1_is_not_repaired"])
        self.assertTrue(v1["v1_is_not_hidden"])
        self.assertTrue(v1["v1_is_not_claimed_passed"])
        self.assertTrue(v1["predecessor_failure_evidence_is_lineage_evidence_only"])

        lineage = result["selected_older_command_execution_boundary_lineage_basis"]
        self.assertTrue(lineage["lineage_basis_declared"])
        self.assertTrue(lineage["basis_remains_prior_scaffolding_only"])
        self.assertTrue(lineage["older_command_execution_boundary_surfaces_remain_lineage_only"])
        self.assertTrue(lineage["lineage_basis_is_not_current_execution"])
        self.assertIs(lineage["older_command_execution_boundary_lineage_treated_as_current_execution"], False)

        for section in (
            "selected_command_report_basis",
            "selected_command_implementation_boundary_basis",
            "selected_command_boundary_basis",
            "selected_artifact_emission_containment_basis",
            "selected_evidence_manifest_basis",
            "selected_portable_verification_basis",
        ):
            self.assertTrue(result[section]["declared"], section)
            self.assertTrue(result[section]["reference_shaped_basis"], section)
            self.assertTrue(result[section]["basis_is_not_command_output_result_success"], section)

    def test_checks_include_required_fields_and_named_review_conditions(self) -> None:
        result = _resolve(_valid_request())
        checks = result["post_invocation_command_execution_checks"]
        self.assertGreaterEqual(len(checks), 50)
        for check in checks:
            for key in ("check_name", "passed", "expected_posture", "actual_posture", "block_code", "failure_code"):
                self.assertIn(key, check)
            self.assertIs(check["passed"], True, check["check_name"])
            self.assertIsNone(check["block_code"])
            self.assertIsNone(check["failure_code"])
        names = {check["check_name"] for check in checks}
        expected_names = {
            "post-invocation command execution question declared",
            "post-invocation command execution intent supported",
            "post-invocation command execution boundary terminal summary basis declared",
            "post-invocation command execution boundary live artifact basis declared",
            "post-invocation command execution boundary outcome recorded",
            "post-invocation command execution boundary failed check count zero",
            "post-invocation command execution boundary one future execution step declared",
            "command invocation terminal summary basis declared",
            "command invocation basis declared",
            "command invocation outcome recorded",
            "command invocation failed check count zero",
            "command invocation event recorded",
            "command invocation authorization token spent exactly once",
            "command invocation authorization token reuse blocked",
            "command execution review basis declared",
            "request consumption basis declared",
            "consumed request basis declared",
            "consumed request token remains closed",
            "consumed request not reopened",
            "v2 admitted request basis declared",
            "v2 admitted request outcome admitted",
            "v2 admitted request version 0.2.0",
            "v2 successor metadata preserved",
            "v2 returned-result containment preserved",
            "v1 predecessor failure remains visible",
            "older command execution boundary lineage basis not current execution",
            "command report basis declared",
            "command implementation boundary basis declared",
            "command boundary basis declared",
            "artifact emission containment basis declared",
            "evidence-manifest basis declared",
            "portable verification basis declared",
            "post-invocation-command-execution-only posture declared",
            "one-bounded-command-execution-event posture declared",
            "execution-trace-audit-only posture declared",
            "no-command-output posture declared",
            "no-command-result posture declared",
            "no-command-success posture declared",
            "no-standing-execution-lane posture declared",
            "no-repeat-execution-permission posture declared",
            "post-invocation command execution scope supported",
            "reference-shaped input posture preserved",
            "execution trace is audit only",
            "collapse flags absent",
            "raw full prior artifact body not emitted",
            "non-claims remain false",
        }
        self.assertTrue(expected_names.issubset(names))

    def test_non_meaning_and_what_remains_open(self) -> None:
        result = _resolve(_valid_request())
        non_meaning = result["post_invocation_command_execution_non_meaning"]
        for suffix in (
            "command_output_exists",
            "command_result_exists",
            "command_success_exists",
            "execution_permission_exists",
            "execution_approval_exists",
            "execution_trace_is_output",
            "execution_trace_is_result",
            "execution_trace_is_success",
            "execution_trace_is_source",
            "execution_trace_is_authority",
            "standing_execution_lane_exists",
            "repeat_execution_permission_exists",
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
            self.assertIs(non_meaning[f"post_invocation_command_execution_does_not_mean_{suffix}"], True, suffix)

        remains_open = result["what_remains_open"]
        for item in OPEN_ITEMS:
            self.assertIn(item, remains_open["open_items"])
        self.assertTrue(remains_open["open_means_not_scheduled"])
        self.assertTrue(remains_open["open_means_not_authorized"])
        self.assertTrue(remains_open["open_means_not_executed"])

    def test_requires_additional_basis_and_not_recorded_outcomes_are_bounded(self) -> None:
        additional_context = {"needed": "execution trace containment needs additional bounded basis"}
        additional = _resolve(
            _valid_request(
                requested_post_invocation_command_execution_outcome=REQUIRES_ADDITIONAL_BASIS,
                additional_basis_context=additional_context,
            )
        )
        self.assertEqual(additional["outcome"], REQUIRES_ADDITIONAL_BASIS)
        self.assertEqual(additional["additional_basis_required"]["additional_basis_context"], additional_context)
        self.assertTrue(additional["additional_basis_required"]["missing_basis_not_scheduled"])
        self.assertTrue(additional["additional_basis_required"]["missing_basis_not_authorized"])
        self.assertTrue(additional["additional_basis_required"]["missing_basis_not_executed"])
        self.assertTrue(additional["additional_basis_required"]["additional_basis_does_not_run_real_command"])
        self.assertTrue(additional["additional_basis_required"]["additional_basis_does_not_create_output_result_success"])
        self.assertNoOutputResultSuccessOrFollowOn(additional)

        not_recorded_basis = {"reason": "readable execution basis failed bounded review"}
        not_recorded = _resolve(
            _valid_request(
                requested_post_invocation_command_execution_outcome=NOT_RECORDED,
                not_recorded_basis=not_recorded_basis,
            )
        )
        self.assertEqual(not_recorded["outcome"], NOT_RECORDED)
        self.assertEqual(not_recorded["not_recorded_basis"]["not_recorded_basis"], not_recorded_basis)
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded_does_not_repair"])
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded_does_not_authorize_next_work"])
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded_does_not_run_real_command"])
        self.assertNoOutputResultSuccessOrFollowOn(not_recorded)

    def test_summary_helper_preserves_expected_fields(self) -> None:
        result = _resolve(_valid_request())
        summary = build_portable_source_body_verification_post_invocation_command_execution_summary(result)
        self.assertEqual(summary, result["portable_source_body_verification_post_invocation_command_execution_summary"])
        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(summary["request_id"], "post_invocation_command_execution_reference_review_001")
        self.assertEqual(summary["question"], QUESTION)
        self.assertEqual(summary["intent"], resolver.INTENT_RECORD)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)
        for key in (
            "post_invocation_execution_recorded",
            "bounded_command_execution_event_recorded",
            "execution_trace_audit_only",
            "command_output_result_success_still_not_created",
            "execution_permission_not_created",
            "execution_approval_not_created",
            "authorization_token_reuse_blocked",
            "consumed_request_token_remains_closed",
            "v1_predecessor_failure_preserved",
            "returned_result_containment_preserved",
            "execution_trace_not_output_result_success_source_authority",
            "no_standing_repeat_execution_lane",
            "older_command_execution_boundary_lineage_not_treated_as_current_execution",
            "no_raw_full_prior_artifact_body",
            "no_artifact_mutation",
            "no_deployment_runtime_public_release",
            "no_operation_public_readiness_final_completion",
            "no_continuation_publication_reusable_follow_on",
        ):
            self.assertIs(summary[key], True, key)
        self.assertEqual(summary["selected_boundary_outcome"], BOUNDARY_OUTCOME)
        self.assertEqual(summary["selected_boundary_failed_check_count"], 0)
        self.assertEqual(summary["selected_command_invocation_outcome"], COMMAND_INVOCATION_OUTCOME)
        self.assertEqual(summary["selected_command_invocation_failed_check_count"], 0)
        self.assertEqual(summary["selected_command_execution_review_outcome"], COMMAND_EXECUTION_REVIEW_OUTCOME)
        self.assertEqual(summary["selected_request_consumption_outcome"], REQUEST_CONSUMPTION_OUTCOME)
        self.assertEqual(summary["selected_v2_admitted_request_outcome"], V2_ADMITTED_REQUEST_OUTCOME)
        self.assertEqual(summary["selected_v2_admitted_request_version"], V2_ADMITTED_REQUEST_VERSION)
        self.assertEqual(summary["selected_v2_admitted_request_failed_check_count"], 0)
        self.assertEqual(summary["key_non_claims"], _false_non_claims())

    def test_request_builder_helper_builds_valid_resolvable_request(self) -> None:
        additional_context = {"basis": "additional post-invocation command execution context"}
        not_recorded_basis = {"reason": "not recorded basis"}
        request = build_declared_portable_source_body_verification_post_invocation_command_execution_request(
            "builder_post_invocation_command_execution_001",
            QUESTION,
            _boundary_basis(),
            _boundary_terminal_summary_basis(),
            _command_invocation_basis(),
            _command_invocation_terminal_summary_basis(),
            _command_execution_review_basis(),
            _request_consumption_basis(),
            _consumed_request_basis(),
            _v2_admitted_request_basis(),
            _v1_predecessor_failure_basis(),
            _older_command_execution_boundary_lineage_basis(),
            _command_basis("command_report"),
            _command_basis("command_implementation_boundary"),
            _command_basis("command_boundary"),
            _command_basis("artifact_emission_containment"),
            _command_basis("evidence_manifest"),
            _command_basis("portable_verification"),
            _posture("post_invocation_command_execution_only"),
            _posture("one_bounded_command_execution_event"),
            _posture("execution_trace_audit_only"),
            _posture("no_command_output"),
            _posture("no_command_result"),
            _posture("no_command_success"),
            _posture("no_execution_permission"),
            _posture("no_execution_approval"),
            _posture("no_standing_execution_lane"),
            _posture("no_repeat_execution_permission"),
            _posture("authorization_token_reuse_blocked"),
            _posture("consumed_token_closed"),
            _posture("no_reopen_consumed_request"),
            _posture("returned_result_containment"),
            list(SUPPORTED_SCOPE),
            selected_post_invocation_command_execution_boundary_result_path="artifact://post_invocation_boundary",
            selected_post_invocation_command_execution_boundary_result_id="post_invocation_boundary_001",
            selected_post_invocation_command_execution_boundary_result_outcome=BOUNDARY_OUTCOME,
            selected_post_invocation_command_execution_boundary_failed_check_count=0,
            selected_post_invocation_command_execution_boundary_step_declared=True,
            selected_command_invocation_result_outcome=COMMAND_INVOCATION_OUTCOME,
            selected_command_invocation_failed_check_count=0,
            selected_command_invocation_event_recorded=True,
            selected_command_invocation_authorization_token_spent_exactly_once=True,
            selected_command_invocation_authorization_token_reuse_blocked=True,
            selected_command_execution_review_result_outcome=COMMAND_EXECUTION_REVIEW_OUTCOME,
            selected_command_execution_review_failed_check_count=0,
            selected_request_consumption_result_outcome=REQUEST_CONSUMPTION_OUTCOME,
            selected_request_consumption_failed_check_count=0,
            selected_v2_admitted_request_outcome=V2_ADMITTED_REQUEST_OUTCOME,
            selected_v2_admitted_request_version=V2_ADMITTED_REQUEST_VERSION,
            selected_v2_failed_check_count=0,
            selected_v2_successor_metadata={
                "successor_of": V1_PREDECESSOR_RESOLVER_MODULE,
                "successor_reason": "returned-result containment successor",
                "resolver_module": V2_ADMITTED_REQUEST_RESOLVER_MODULE,
            },
            execution_trace=_execution_trace(),
            requested_post_invocation_command_execution_outcome=RECORDED,
            additional_basis_context=additional_context,
            not_recorded_basis=not_recorded_basis,
        )
        self.assertEqual(request["post_invocation_command_execution_request_id"], "builder_post_invocation_command_execution_001")
        self.assertEqual(request["post_invocation_command_execution_question"], QUESTION)
        for key in TOP_LEVEL_SECTIONS:
            if key.startswith("selected_") or key.endswith("_posture"):
                self.assertIn(key, request)
        self.assertEqual(request["post_invocation_command_execution_scope"], list(SUPPORTED_SCOPE))
        self.assertEqual(request["execution_trace"], _execution_trace())
        self.assertEqual(request["additional_basis_context"], additional_context)
        self.assertEqual(request["not_recorded_basis"], not_recorded_basis)
        self.assertEqual(request["declared_non_claims"], _false_non_claims())
        result = _resolve(request)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertNoOutputResultSuccessOrFollowOn(result)

    def test_path_based_request_and_write_behavior(self) -> None:
        request = _valid_request()
        mapping_result = _resolve(request)
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            request_path = temp / "request.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")
            path_result = resolve_portable_source_body_verification_post_invocation_command_execution_from_path(
                request_path
            )
            self.assertEqual(path_result["outcome"], RECORDED)
            self.assertEqual(set(path_result), set(mapping_result))
            self.assertEqual(
                path_result["portable_source_body_verification_post_invocation_command_execution_metadata"][
                    "declared_post_invocation_command_execution_request_path"
                ],
                str(request_path),
            )

            malformed_path = temp / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            self.assertBlocked(
                resolve_portable_source_body_verification_post_invocation_command_execution_from_path(malformed_path),
                "DECLARED_POST_INVOCATION_COMMAND_EXECUTION_REQUEST_MALFORMED",
            )
            array_path = temp / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            self.assertBlocked(
                resolve_portable_source_body_verification_post_invocation_command_execution_from_path(array_path),
                "DECLARED_POST_INVOCATION_COMMAND_EXECUTION_REQUEST_MALFORMED",
            )
            self.assertBlocked(
                resolve_portable_source_body_verification_post_invocation_command_execution_from_path(
                    temp / "missing.json"
                ),
                "DECLARED_POST_INVOCATION_COMMAND_EXECUTION_REQUEST_UNREADABLE",
            )

            explicit_output = temp / "nested" / "result.json"
            written = write_portable_source_body_verification_post_invocation_command_execution_result(
                mapping_result,
                explicit_output,
            )
            self.assertEqual(written, explicit_output)
            parsed = json.loads(written.read_text(encoding="utf-8"))
            for section in TOP_LEVEL_SECTIONS:
                self.assertIn(section, parsed)

            default_root = temp / "post_invocation_command_execution_root"
            with patch.object(
                resolver,
                "PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_ROOT",
                default_root,
            ):
                first = write_portable_source_body_verification_post_invocation_command_execution_result(mapping_result)
                second = write_portable_source_body_verification_post_invocation_command_execution_result(mapping_result)
            self.assertTrue(first.is_file())
            self.assertTrue(second.is_file())
            self.assertNotEqual(first, second)
            self.assertEqual(first.parent, default_root)
            self.assertEqual(second.parent, default_root)
            self.assertTrue(second.stem.endswith("_001"))
            for forbidden_root_fragment in (
                "post_invocation_command_execution_boundary",
                "command_invocation",
                "command_execution_review",
                "request_consumption",
                "command_execution_boundary",
                "command_implementation",
                "command_boundary",
                "artifact_emission_containment",
                "evidence_manifest",
                "deployment",
                "runtime",
                "public_release",
            ):
                self.assertNotIn(forbidden_root_fragment, str(first.parent))

    def test_reference_shaped_containment_blocks_full_body_without_returning_raw_value(self) -> None:
        request = _valid_request(
            selected_post_invocation_command_execution_boundary_basis=_boundary_basis(
                full_artifact_body=RAW_FULL_BODY_SENTINEL
            )
        )
        result = _resolve(request)
        self.assertBlocked(result, "FULL_PRIOR_ARTIFACT_BODY_EMITTED")
        self.assertNotIn(RAW_FULL_BODY_SENTINEL, _json_text(result))
        self.assertNoOutputResultSuccessOrFollowOn(result)

    def test_execution_trace_forbidden_body_blocks_without_returning_raw_value(self) -> None:
        request = _valid_request(
            execution_trace=_execution_trace(command_output_body=RAW_FULL_BODY_SENTINEL)
        )
        result = _resolve(request)
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertIn(
            result["block"]["code"],
            {
                "EXECUTION_TRACE_TREATED_AS_OUTPUT",
                "EXECUTION_TRACE_TREATED_AS_RESULT",
                "EXECUTION_TRACE_TREATED_AS_SUCCESS",
                "EXECUTION_TRACE_TREATED_AS_SOURCE",
                "EXECUTION_TRACE_TREATED_AS_AUTHORITY",
            },
        )
        self.assertNotIn(RAW_FULL_BODY_SENTINEL, _json_text(result))
        self.assertNoOutputResultSuccessOrFollowOn(result)

    def test_no_real_execution_modules_are_used(self) -> None:
        self.assertNotIn("subprocess", resolver.__dict__)
        self.assertNotIn("os", resolver.__dict__)
        with (
            patch.object(subprocess, "run", side_effect=AssertionError("subprocess.run must not be called")) as run,
            patch.object(subprocess, "Popen", side_effect=AssertionError("subprocess.Popen must not be called")) as popen,
            patch.object(os, "system", side_effect=AssertionError("os.system must not be called")) as system,
            patch.object(os, "popen", side_effect=AssertionError("os.popen must not be called")) as popen_os,
        ):
            result = _resolve(_valid_request())
        self.assertEqual(result["outcome"], RECORDED)
        self.assertFalse(run.called)
        self.assertFalse(popen.called)
        self.assertFalse(system.called)
        self.assertFalse(popen_os.called)
        trace = result["execution_trace"]
        self.assertTrue(trace["real_command_not_run_by_resolver"])
        self.assertTrue(trace["subprocess_not_run_by_resolver"])
        self.assertTrue(trace["network_not_called_by_resolver"])

    def test_non_mutation_of_request_basis_postures_trace_and_scope(self) -> None:
        request = _valid_request()
        original = copy.deepcopy(request)
        selected_originals = {
            key: copy.deepcopy(request[key])
            for key in (
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
                "post_invocation_command_execution_only_posture",
                "execution_trace",
                "post_invocation_command_execution_scope",
            )
        }
        first = _resolve(request)
        second = _resolve(request)
        self.assertEqual(first["outcome"], RECORDED)
        self.assertEqual(second["outcome"], RECORDED)
        self.assertEqual(request, original)
        for key, value in selected_originals.items():
            self.assertEqual(request[key], value, key)

        with tempfile.TemporaryDirectory() as temp_dir:
            artifact_path = Path(temp_dir) / "post_invocation_execution" / "result.json"
            written = write_portable_source_body_verification_post_invocation_command_execution_result(
                first,
                artifact_path,
            )
            self.assertTrue(written.is_file())
            self.assertEqual(written.parent, artifact_path.parent)

    def test_missing_and_malformed_requests_block(self) -> None:
        self.assertBlocked(
            resolve_portable_source_body_verification_post_invocation_command_execution(None),
            "POST_INVOCATION_COMMAND_EXECUTION_QUESTION_UNDECLARED",
        )
        self.assertBlocked(
            resolve_portable_source_body_verification_post_invocation_command_execution("not a mapping"),  # type: ignore[arg-type]
            "DECLARED_POST_INVOCATION_COMMAND_EXECUTION_REQUEST_MALFORMED",
        )
        self.assertBlocked(
            _resolve(_valid_request(post_invocation_command_execution_intent=resolver.INTENT_BLOCK)),
            "POST_INVOCATION_COMMAND_EXECUTION_BLOCKED_BY_REQUEST",
        )
        self.assertBlocked(
            _resolve(_valid_request(post_invocation_command_execution_intent="UNSUPPORTED_INTENT")),
            "POST_INVOCATION_COMMAND_EXECUTION_INTENT_UNSUPPORTED",
        )

    def test_required_basis_and_posture_blocking_cases(self) -> None:
        def set_nested(key: str, values: dict[str, Any]) -> Callable[[dict[str, Any]], None]:
            def mutate(request: dict[str, Any]) -> None:
                request[key].update(values)

            return mutate

        def set_nested_and_root(
            key: str,
            values: dict[str, Any],
            root_values: dict[str, Any],
        ) -> Callable[[dict[str, Any]], None]:
            def mutate(request: dict[str, Any]) -> None:
                request[key].update(values)
                request.update(root_values)

            return mutate

        cases: list[tuple[str, Callable[[dict[str, Any]], None], str]] = [
            ("missing boundary terminal summary", lambda r: r.pop("selected_post_invocation_command_execution_boundary_terminal_summary_basis"), "POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_BASIS_MISSING"),
            ("missing boundary basis", lambda r: r.pop("selected_post_invocation_command_execution_boundary_basis"), "POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_BASIS_MISSING"),
            ("boundary outcome not recorded", set_nested_and_root("selected_post_invocation_command_execution_boundary_basis", {"outcome": "NOT_RECORDED"}, {"selected_post_invocation_command_execution_boundary_result_outcome": "NOT_RECORDED"}), "POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_NOT_RECORDED"),
            ("boundary failed checks", set_nested_and_root("selected_post_invocation_command_execution_boundary_basis", {"failed_check_count": 1}, {"selected_post_invocation_command_execution_boundary_failed_check_count": 1}), "POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_FAILED_CHECKS_PRESENT"),
            ("boundary step missing", lambda r: (r["selected_post_invocation_command_execution_boundary_basis"].update({"one_future_command_execution_step_declared": False, "one_future_command_execution_step_posture_declared": False}), r.__setitem__("selected_post_invocation_command_execution_boundary_step_declared", False)), "POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_STEP_NOT_DECLARED"),
            ("missing invocation", lambda r: r.pop("selected_command_invocation_basis"), "COMMAND_INVOCATION_BASIS_MISSING"),
            ("invocation not recorded", set_nested_and_root("selected_command_invocation_basis", {"outcome": "NOT_RECORDED"}, {"selected_command_invocation_result_outcome": "NOT_RECORDED"}), "COMMAND_INVOCATION_NOT_RECORDED"),
            ("invocation failed checks", set_nested_and_root("selected_command_invocation_basis", {"failed_check_count": 1}, {"selected_command_invocation_failed_check_count": 1}), "COMMAND_INVOCATION_FAILED_CHECKS_PRESENT"),
            ("invocation event missing", lambda r: r.__setitem__("selected_command_invocation_event_recorded", False), "COMMAND_INVOCATION_EVENT_NOT_RECORDED"),
            ("token not spent", lambda r: r.__setitem__("selected_command_invocation_authorization_token_spent_exactly_once", False), "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_NOT_SPENT_EXACTLY_ONCE"),
            ("token reuse not blocked", lambda r: r.__setitem__("selected_command_invocation_authorization_token_reuse_blocked", False), "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_REUSE_NOT_BLOCKED"),
            ("missing review", lambda r: r.pop("selected_command_execution_review_basis"), "COMMAND_EXECUTION_REVIEW_BASIS_MISSING"),
            ("review not recorded", set_nested_and_root("selected_command_execution_review_basis", {"outcome": "NOT_RECORDED"}, {"selected_command_execution_review_result_outcome": "NOT_RECORDED"}), "COMMAND_EXECUTION_REVIEW_NOT_RECORDED"),
            ("review failed checks", set_nested_and_root("selected_command_execution_review_basis", {"failed_check_count": 1}, {"selected_command_execution_review_failed_check_count": 1}), "COMMAND_EXECUTION_REVIEW_FAILED_CHECKS_PRESENT"),
            ("missing consumption", lambda r: r.pop("selected_request_consumption_basis"), "REQUEST_CONSUMPTION_BASIS_MISSING"),
            ("consumption not consumed", set_nested_and_root("selected_request_consumption_basis", {"outcome": "NOT_CONSUMED"}, {"selected_request_consumption_result_outcome": "NOT_CONSUMED"}), "REQUEST_CONSUMPTION_NOT_CONSUMED"),
            ("consumption failed checks", set_nested_and_root("selected_request_consumption_basis", {"failed_check_count": 1}, {"selected_request_consumption_failed_check_count": 1}), "REQUEST_CONSUMPTION_FAILED_CHECKS_PRESENT"),
            ("missing consumed basis", lambda r: r.pop("selected_consumed_request_basis"), "CONSUMED_REQUEST_BASIS_MISSING"),
            ("consumed token not closed", set_nested("selected_consumed_request_basis", {"consumed_request_token_remains_closed": False, "consumption_token_closed": False, "consumed_token_closed": False, "token_closed": False}), "CONSUMED_TOKEN_NOT_CLOSED"),
            ("consumed request reopened", set_nested("selected_consumed_request_basis", {"consumed_request_reopened": True}), "CONSUMED_REQUEST_REOPENED"),
            ("missing v2", lambda r: r.pop("selected_v2_admitted_request_basis"), "V2_ADMITTED_REQUEST_BASIS_MISSING"),
            ("v2 not admitted", set_nested_and_root("selected_v2_admitted_request_basis", {"outcome": "NOT_ADMITTED"}, {"selected_v2_admitted_request_outcome": "NOT_ADMITTED"}), "V2_ADMITTED_REQUEST_NOT_ADMITTED"),
            ("v2 wrong version", set_nested_and_root("selected_v2_admitted_request_basis", {"result_version": "0.1.0"}, {"selected_v2_admitted_request_version": "0.1.0"}), "V2_ADMITTED_REQUEST_VERSION_NOT_0_2_0"),
            ("v2 failed checks", set_nested_and_root("selected_v2_admitted_request_basis", {"failed_check_count": 1}, {"selected_v2_failed_check_count": 1}), "V2_ADMITTED_REQUEST_FAILED_CHECKS_PRESENT"),
            ("v2 metadata missing", lambda r: (r.pop("selected_v2_successor_metadata"), r["selected_v2_admitted_request_basis"].update({"successor_of": "", "successor_reason": "", "resolver_module": "", "successor_metadata_preserved": False, "v2_successor_metadata_preserved": False})), "V2_SUCCESSOR_METADATA_MISSING"),
            ("v2 containment missing", set_nested("selected_v2_admitted_request_basis", {"returned_result_containment_preserved": False, "returned_result_containment_posture_preserved": False, "returned_result_containment_declared": False, "no_raw_full_prior_artifact_body_returned": False}), "V2_RETURNED_RESULT_CONTAINMENT_MISSING"),
            ("missing v1", lambda r: r.pop("selected_v1_predecessor_failure_basis"), "V1_PREDECESSOR_FAILURE_BASIS_MISSING"),
            ("v2 repairing v1", set_nested("selected_v2_admitted_request_basis", {"v2_treated_as_repairing_v1": True}), "V2_TREATED_AS_REPAIRING_V1"),
            ("v1 hidden", set_nested("selected_v1_predecessor_failure_basis", {"v1_hidden": True}), "V1_FAILURE_HIDDEN"),
            ("v1 claimed passed", set_nested("selected_v1_predecessor_failure_basis", {"v1_claimed_passed": True}), "V1_CLAIMED_PASSED"),
            ("lineage current execution", set_nested("selected_older_command_execution_boundary_lineage_basis", {"older_command_execution_boundary_lineage_treated_as_current_execution": True}), "OLDER_COMMAND_EXECUTION_BOUNDARY_LINEAGE_TREATED_AS_CURRENT_EXECUTION"),
            ("missing command report", lambda r: r.pop("selected_command_report_basis"), "COMMAND_REPORT_BASIS_MISSING"),
            ("missing implementation boundary", lambda r: r.pop("selected_command_implementation_boundary_basis"), "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING"),
            ("missing command boundary", lambda r: r.pop("selected_command_boundary_basis"), "COMMAND_BOUNDARY_BASIS_MISSING"),
            ("missing containment", lambda r: r.pop("selected_artifact_emission_containment_basis"), "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING"),
            ("missing evidence", lambda r: r.pop("selected_evidence_manifest_basis"), "EVIDENCE_MANIFEST_BASIS_MISSING"),
            ("missing portable verification", lambda r: r.pop("selected_portable_verification_basis"), "PORTABLE_VERIFICATION_BASIS_MISSING"),
            ("missing posture", lambda r: r.pop("post_invocation_command_execution_only_posture"), "POST_INVOCATION_COMMAND_EXECUTION_ONLY_POSTURE_MISSING"),
            ("unsupported scope", lambda r: r.__setitem__("post_invocation_command_execution_scope", ["UNSUPPORTED_POST_INVOCATION_COMMAND_EXECUTION_SCOPE"]), "UNSUPPORTED_POST_INVOCATION_COMMAND_EXECUTION_SCOPE"),
        ]
        for name, mutate, block_code in cases:
            with self.subTest(name=name):
                request = _valid_request()
                mutate(request)
                self.assertBlocked(_resolve(request), block_code)

    def test_collapse_flags_block_with_representative_codes(self) -> None:
        cases = (
            ("command_output_created", "COMMAND_OUTPUT_CREATED"),
            ("command_result_created", "COMMAND_RESULT_CREATED"),
            ("command_success_created", "COMMAND_SUCCESS_CREATED"),
            ("execution_permission_created", "EXECUTION_PERMISSION_CREATED"),
            ("execution_approval_created", "EXECUTION_APPROVAL_CREATED"),
            ("standing_execution_lane_created", "STANDING_EXECUTION_LANE_CREATED"),
            ("repeat_execution_permission_created", "REPEAT_EXECUTION_PERMISSION_CREATED"),
            ("authorization_token_reused", "AUTHORIZATION_TOKEN_REUSED"),
            ("consumed_request_reopened", "CONSUMED_REQUEST_REOPENED"),
            ("execution_treated_as_output", "EXECUTION_TREATED_AS_OUTPUT"),
            ("execution_treated_as_result", "EXECUTION_TREATED_AS_RESULT"),
            ("execution_treated_as_success", "EXECUTION_TREATED_AS_SUCCESS"),
            ("execution_trace_treated_as_output", "EXECUTION_TRACE_TREATED_AS_OUTPUT"),
            ("execution_trace_treated_as_result", "EXECUTION_TRACE_TREATED_AS_RESULT"),
            ("execution_trace_treated_as_success", "EXECUTION_TRACE_TREATED_AS_SUCCESS"),
            ("execution_trace_treated_as_source", "EXECUTION_TRACE_TREATED_AS_SOURCE"),
            ("execution_trace_treated_as_authority", "EXECUTION_TRACE_TREATED_AS_AUTHORITY"),
            ("command_output_became_source", "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
            ("command_result_became_authority", "COMMAND_RESULT_TREATED_AS_AUTHORITY"),
            ("command_success_created_currentness", "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
            ("command_success_claimed_final_completion", "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
            ("prior_artifacts_mutated", "ARTIFACTS_MUTATED"),
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
            ("real_command_run", "REAL_COMMAND_EXECUTION_ATTEMPTED"),
            ("subprocess_run", "REAL_COMMAND_EXECUTION_ATTEMPTED"),
            ("network_call_performed", "REAL_COMMAND_EXECUTION_ATTEMPTED"),
        )
        for flag, block_code in cases:
            with self.subTest(flag=flag):
                request = _valid_request(**{flag: True})
                self.assertBlocked(_resolve(request), block_code)

    def test_mutation_replay_merge_and_non_claim_failures_block(self) -> None:
        request = _valid_request(mutation_performed=True, replay_performed=True, merge_performed=True)
        self.assertBlocked(_resolve(request), "MUTATION_REPLAY_OR_MERGE_DETECTED")

        missing_non_claim = _valid_request()
        missing_non_claim["declared_non_claims"].pop("command_output_created")
        self.assertBlocked(_resolve(missing_non_claim), "NON_CLAIM_MISSING_OR_FLIPPED")

        flipped_non_claim = _valid_request()
        flipped_non_claim["declared_non_claims"]["command_output_created"] = True
        self.assertBlocked(_resolve(flipped_non_claim), "COMMAND_OUTPUT_CREATED")


if __name__ == "__main__":
    unittest.main()
