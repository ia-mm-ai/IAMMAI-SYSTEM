"""Tests for the post-invocation command execution boundary resolver.

This suite is bounded to the post-invocation command execution boundary only.
It is downstream of recorded command invocation, preserves older command
execution boundary surfaces as lineage only, and does not create command
execution, command output, command result, command success, execution
permission, execution approval, standing/repeat execution lanes, deployment,
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
from typing import Any
from unittest.mock import patch


sys.dont_write_bytecode = True

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_portable_source_body_verification_post_invocation_command_execution_boundary as resolver
from resolve_portable_source_body_verification_post_invocation_command_execution_boundary import (
    build_declared_portable_source_body_verification_post_invocation_command_execution_boundary_request,
    build_portable_source_body_verification_post_invocation_command_execution_boundary_summary,
    resolve_portable_source_body_verification_post_invocation_command_execution_boundary,
    resolve_portable_source_body_verification_post_invocation_command_execution_boundary_from_path,
    write_portable_source_body_verification_post_invocation_command_execution_boundary_result,
)


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}

QUESTION = resolver.CORE_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_QUESTION
COMMAND_INVOCATION_OUTCOME = resolver.COMMAND_INVOCATION_OUTCOME
COMMAND_INVOCATION_BOUNDARY_OUTCOME = resolver.COMMAND_INVOCATION_BOUNDARY_OUTCOME
COMMAND_INVOCATION_AUTHORIZATION_OUTCOME = resolver.COMMAND_INVOCATION_AUTHORIZATION_OUTCOME
COMMAND_EXECUTION_REVIEW_OUTCOME = resolver.COMMAND_EXECUTION_REVIEW_OUTCOME
REQUEST_CONSUMPTION_OUTCOME = resolver.REQUEST_CONSUMPTION_OUTCOME
V2_ADMITTED_REQUEST_OUTCOME = resolver.V2_ADMITTED_REQUEST_OUTCOME
V2_ADMITTED_REQUEST_VERSION = resolver.V2_ADMITTED_REQUEST_VERSION
V1_PREDECESSOR_RESOLVER_MODULE = resolver.V1_PREDECESSOR_RESOLVER_MODULE
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
RAW_FULL_BODY_SENTINEL = "RAW_POST_INVOCATION_FULL_BODY_MUST_NOT_RETURN_" * 8

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_post_invocation_command_execution_boundary_metadata",
    "declared_post_invocation_command_execution_boundary_question",
    "selected_command_invocation_basis",
    "selected_command_invocation_terminal_summary_basis",
    "selected_command_invocation_boundary_basis",
    "selected_command_invocation_authorization_basis",
    "selected_command_execution_review_basis",
    "selected_request_consumption_basis",
    "selected_consumed_request_basis",
    "selected_v2_admitted_request_basis",
    "selected_v1_predecessor_failure_basis",
    "selected_command_execution_boundary_lineage_basis",
    "selected_command_report_basis",
    "selected_command_implementation_boundary_basis",
    "selected_command_boundary_basis",
    "selected_artifact_emission_containment_basis",
    "selected_evidence_manifest_basis",
    "selected_portable_verification_basis",
    "post_invocation_execution_boundary_only_posture",
    "one_future_command_execution_step_posture",
    "invocation_basis_preserved_posture",
    "authorization_token_spent_exactly_once_posture",
    "authorization_token_reuse_blocked_posture",
    "no_command_execution_posture",
    "no_output_result_success_posture",
    "no_execution_permission_posture",
    "no_execution_approval_posture",
    "no_standing_execution_lane_posture",
    "no_repeat_execution_permission_posture",
    "no_standing_invocation_lane_posture",
    "no_repeat_invocation_permission_posture",
    "consumed_token_closed_posture",
    "no_reopen_consumed_request_posture",
    "returned_result_containment_posture",
    "post_invocation_command_execution_boundary_scope",
    "post_invocation_command_execution_boundary_checks",
    "post_invocation_command_execution_boundary_statement",
    "post_invocation_command_execution_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_post_invocation_command_execution_boundary_summary",
)

OPEN_ITEMS = (
    "post_invocation_command_execution_boundary_test",
    "post_invocation_command_execution_boundary_live_artifact",
    "command_execution_step_if_separately_specified",
    "command_execution",
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
        "basis_remains_basis_only": True,
        "basis_is_not_command_execution": True,
        "basis_is_not_command_output_result_success": True,
        "basis_is_not_execution_permission_or_approval": True,
        "basis_is_not_authority_currentness_final_completion": True,
        "basis_does_not_authorize_continuation_reusable_permission_follow_on_work": True,
        "basis_does_not_create_standing_or_repeat_execution_lane": True,
        "basis_does_not_create_standing_or_repeat_invocation_lane": True,
        "full_upstream_lineage_preserved": True,
        "upstream_lineage": (
            "command_invocation_terminal_summary -> command_invocation -> "
            "command_invocation_boundary -> command_invocation_authorization -> "
            "command_execution_review -> request_consumption -> v2_admission -> "
            "v1_predecessor_failure"
        ),
        "full_prior_artifact_body_not_emitted": True,
        "prior_artifacts_mutated": False,
    }
    basis.update(extra)
    return basis


def _command_invocation_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "command_invocation",
        result_id="command_invocation_reference_review_001",
        result_path="artifacts/synthetic_command_invocation_result.json",
        outcome=COMMAND_INVOCATION_OUTCOME,
        failed_check_count=0,
        command_invocation_recorded=True,
        bounded_command_invocation_event_recorded=True,
        command_invocation_event_recorded=True,
        authorization_token_spent_exactly_once=True,
        one_shot_authorization_token_spent_exactly_once=True,
        authorization_token_reuse_blocked=True,
        authorization_token_not_reused=True,
        command_execution_still_not_performed=True,
        command_output_still_not_created=True,
        command_result_still_not_created=True,
        command_success_still_not_created=True,
        execution_permission_not_created=True,
        execution_approval_not_created=True,
        consumed_request_token_remains_closed=True,
        invocation_basis_remains_invocation_basis_only=True,
        command_invocation_is_not_command_execution=True,
        command_invocation_is_not_command_output_result_success=True,
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
        terminal_summary_does_not_create_output_result_success=True,
        terminal_summary_does_not_authorize_follow_on_work=True,
    )
    basis.update(extra)
    return basis


def _command_invocation_boundary_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "command_invocation_boundary",
        result_id="command_invocation_boundary_reference_review_001",
        result_path="artifacts/synthetic_command_invocation_boundary_result.json",
        outcome=COMMAND_INVOCATION_BOUNDARY_OUTCOME,
        failed_check_count=0,
        authorization_token_preserved=True,
        authorization_token_not_spent=True,
        boundary_basis_remains_boundary_basis_only=True,
        boundary_did_not_execute_command=True,
        boundary_did_not_create_output_result_success=True,
        boundary_did_not_create_execution_permission_or_approval=True,
        boundary_did_not_create_standing_execution_lane_or_repeat_execution_permission=True,
        boundary_did_not_create_standing_invocation_lane_or_repeat_invocation_permission=True,
        boundary_did_not_create_final_completion_continuation_reusable_permission_follow_on_work=True,
    )
    basis.update(extra)
    return basis


def _command_invocation_authorization_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "command_invocation_authorization",
        result_id="command_invocation_authorization_reference_review_001",
        result_path="artifacts/synthetic_command_invocation_authorization_result.json",
        outcome=COMMAND_INVOCATION_AUTHORIZATION_OUTCOME,
        failed_check_count=0,
        authorization_token_created=True,
        command_invocation_authorization_token_created=True,
        authorization_token_is_one_shot=True,
        authorization_token_one_shot=True,
        authorization_basis_preserved=True,
        authorization_basis_remains_authorization_basis_only=True,
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
        command_execution_review_did_not_create_execution_output_result_success=True,
        command_execution_review_did_not_create_execution_permission_or_approval=True,
        command_execution_review_did_not_create_standing_lane_repeat_permission_final_completion_continuation_reusable_permission_follow_on_work=True,
    )
    basis.update(extra)
    return basis


def _request_consumption_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "request_consumption",
        result_id="request_consumption_reference_record_001",
        result_path="artifacts/synthetic_request_consumption_result.json",
        outcome=REQUEST_CONSUMPTION_OUTCOME,
        failed_check_count=0,
        request_consumed_exactly_once=True,
        request_consumed=True,
        consumption_token_closed=True,
        consumed_token_closed=True,
        consumed_request_basis_recorded=True,
        request_consumption_basis_does_not_authorize_execution_output_result_success=True,
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
        consumed_token_closed=True,
        token_closed=True,
        consumed_request_not_reopened=True,
        consumed_request_is_not_reopened=True,
        request_not_reopened=True,
        consumed_request_basis_only=True,
    )
    basis.update(extra)
    return basis


def _v2_admitted_request_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "v2_admitted_request",
        result_id="v2_admission_reference_record_001",
        result_path="artifacts/synthetic_v2_admission_result.json",
        outcome=V2_ADMITTED_REQUEST_OUTCOME,
        result_version=V2_ADMITTED_REQUEST_VERSION,
        failed_check_count=0,
        passed_check_count=42,
        successor_of=V1_PREDECESSOR_RESOLVER_MODULE,
        successor_reason="returned-result containment successor",
        resolver_module="resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2",
        successor_metadata_preserved=True,
        selected_v2_successor_metadata={"successor_of": V1_PREDECESSOR_RESOLVER_MODULE},
        returned_result_containment_preserved=True,
        selected_basis_is_reference_shaped=True,
        v2_does_not_claim_v1_passed=True,
        v2_successor_does_not_erase_v1=True,
    )
    basis.update(extra)
    return basis


def _v1_predecessor_failure_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "v1_predecessor_failure",
        v1_predecessor_failure_basis_declared=True,
        v1_remains_visible_predecessor_failure_evidence=True,
        visible_predecessor_failure_evidence=True,
        v1_predecessor_failure_remains_visible=True,
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


def _command_execution_boundary_lineage_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "command_execution_boundary_lineage",
        lineage_basis_declared=True,
        basis_remains_prior_scaffolding_only=True,
        older_command_execution_boundary_surfaces_remain_lineage_only=True,
        lineage_basis_is_not_current_execution=True,
        command_execution_boundary_lineage_treated_as_current_execution=False,
        selected_command_execution_boundary_lineage_basis_treated_as_current_execution=False,
        current_execution=False,
        command_execution_performed=False,
    )
    basis.update(extra)
    return basis


def _command_basis(label: str, **extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        label,
        basis_remains_reference_shaped=True,
        basis_is_not_command_execution=True,
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
        "reference_shaped_basis": True,
        "post_invocation_execution_boundary_only_posture_declared": label == "post_invocation_execution_boundary_only",
        "one_future_command_execution_step_posture_declared": label == "one_future_command_execution_step",
        "invocation_basis_preserved_posture_declared": label == "invocation_basis_preserved",
        "authorization_token_spent_exactly_once_posture_declared": label == "authorization_token_spent_exactly_once",
        "authorization_token_reuse_blocked_posture_declared": label == "authorization_token_reuse_blocked",
        "authorization_token_spent_exactly_once_preserved": label == "authorization_token_spent_exactly_once",
        "authorization_token_spent_exactly_once": label == "authorization_token_spent_exactly_once",
        "authorization_token_reuse_blocked": label == "authorization_token_reuse_blocked",
        "authorization_token_not_reused": label == "authorization_token_reuse_blocked",
        "command_execution_not_performed": True,
        "command_output_not_created": True,
        "command_result_not_created": True,
        "command_success_not_created": True,
        "output_result_success_not_created": True,
        "execution_permission_not_created": True,
        "execution_approval_not_created": True,
        "standing_execution_lane_created": False,
        "repeat_execution_permission_created": False,
        "standing_invocation_lane_created": False,
        "repeat_invocation_permission_created": False,
        "no_standing_execution_lane": True,
        "no_repeat_execution_permission": True,
        "no_standing_invocation_lane": True,
        "no_repeat_invocation_permission": True,
        "consumed_request_token_remains_closed": True,
        "consumed_request_not_reopened": True,
        "returned_result_containment_preserved": True,
        "no_raw_full_prior_artifact_body_returned": True,
    }
    posture.update(extra)
    return posture


def _valid_request(**overrides: Any) -> dict[str, Any]:
    request = {
        "post_invocation_command_execution_boundary_request_id": "post_invocation_command_execution_boundary_reference_review_001",
        "post_invocation_command_execution_boundary_question": QUESTION,
        "post_invocation_command_execution_boundary_intent": resolver.INTENT_RECORD,
        "selected_command_invocation_basis": _command_invocation_basis(),
        "selected_command_invocation_terminal_summary_basis": _command_invocation_terminal_summary_basis(),
        "selected_command_invocation_boundary_basis": _command_invocation_boundary_basis(),
        "selected_command_invocation_authorization_basis": _command_invocation_authorization_basis(),
        "selected_command_execution_review_basis": _command_execution_review_basis(),
        "selected_request_consumption_basis": _request_consumption_basis(),
        "selected_consumed_request_basis": _consumed_request_basis(),
        "selected_v2_admitted_request_basis": _v2_admitted_request_basis(),
        "selected_v1_predecessor_failure_basis": _v1_predecessor_failure_basis(),
        "selected_command_execution_boundary_lineage_basis": _command_execution_boundary_lineage_basis(),
        "selected_command_report_basis": _command_basis("command_report"),
        "selected_command_implementation_boundary_basis": _command_basis("command_implementation_boundary"),
        "selected_command_boundary_basis": _command_basis("command_boundary"),
        "selected_artifact_emission_containment_basis": _command_basis("artifact_emission_containment"),
        "selected_evidence_manifest_basis": _command_basis("evidence_manifest"),
        "selected_portable_verification_basis": _command_basis("portable_verification"),
        "post_invocation_execution_boundary_only_posture": _posture("post_invocation_execution_boundary_only"),
        "one_future_command_execution_step_posture": _posture("one_future_command_execution_step"),
        "invocation_basis_preserved_posture": _posture("invocation_basis_preserved"),
        "authorization_token_spent_exactly_once_posture": _posture("authorization_token_spent_exactly_once"),
        "authorization_token_reuse_blocked_posture": _posture("authorization_token_reuse_blocked"),
        "no_command_execution_posture": _posture("no_command_execution"),
        "no_output_result_success_posture": _posture("no_output_result_success"),
        "no_execution_permission_posture": _posture("no_execution_permission"),
        "no_execution_approval_posture": _posture("no_execution_approval"),
        "no_standing_execution_lane_posture": _posture("no_standing_execution_lane"),
        "no_repeat_execution_permission_posture": _posture("no_repeat_execution_permission"),
        "no_standing_invocation_lane_posture": _posture("no_standing_invocation_lane"),
        "no_repeat_invocation_permission_posture": _posture("no_repeat_invocation_permission"),
        "consumed_token_closed_posture": _posture("consumed_token_closed"),
        "no_reopen_consumed_request_posture": _posture("no_reopen_consumed_request"),
        "returned_result_containment_posture": _posture("returned_result_containment"),
        "post_invocation_command_execution_boundary_scope": list(SUPPORTED_SCOPE),
        "requested_post_invocation_command_execution_boundary_outcome": RECORDED,
        "declared_non_claims": _false_non_claims(),
    }
    request.update(overrides)
    return request


def _resolve(request: dict[str, Any]) -> dict[str, Any]:
    return resolve_portable_source_body_verification_post_invocation_command_execution_boundary(
        declared_post_invocation_command_execution_boundary_request=request
    )


def _failed_count(result: dict[str, Any]) -> int:
    return sum(
        1 for check in result["post_invocation_command_execution_boundary_checks"] if not check["passed"]
    )


class PortableSourceBodyVerificationPostInvocationCommandExecutionBoundaryTests(unittest.TestCase):
    def assertBlocked(self, result: dict[str, Any], block_code: str) -> None:
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(result["block"]["code"], block_code)

    def assertNoExecutionOrFollowOnFlags(self, result: dict[str, Any]) -> None:
        statement = result["post_invocation_command_execution_boundary_statement"]
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(statement[key], False, key)
            self.assertIs(result["non_claims"][key], False, key)

    def test_recorded_result_shape_and_statement(self) -> None:
        result = _resolve(_valid_request())
        self.assertIsInstance(result, dict)
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertIsNone(result["block"]["code"])
        self.assertIsNone(result["block"]["reason"])
        self.assertEqual(_failed_count(result), 0)

        statement = result["post_invocation_command_execution_boundary_statement"]
        for key in (
            "post_invocation_command_execution_boundary_recorded",
            "recorded_command_invocation_basis_preserved",
            "one_future_command_execution_step_declared",
            "authorization_token_spent_exactly_once_preserved",
            "authorization_token_reuse_blocked",
            "command_execution_still_not_performed",
            "command_output_still_not_created",
            "command_result_still_not_created",
            "command_success_still_not_created",
            "execution_permission_not_created",
            "execution_approval_not_created",
            "consumed_request_token_remains_closed",
            "v1_predecessor_failure_preserved",
            "returned_result_containment_preserved",
        ):
            self.assertIs(statement[key], True, key)
        for key in (
            "command_executed",
            "command_execution_performed",
            "command_output_created",
            "command_result_created",
            "command_success_created",
            "execution_permission_created",
            "execution_approval_created",
            "standing_execution_lane_created",
            "repeat_execution_permission_created",
            "standing_invocation_lane_created",
            "repeat_invocation_permission_created",
            "authorization_token_reused",
            "consumed_request_reopened",
            "execution_boundary_treated_as_execution",
            "execution_boundary_treated_as_command_output",
            "execution_boundary_treated_as_command_result",
            "execution_boundary_treated_as_command_success",
            "invocation_basis_treated_as_execution",
            "invocation_basis_treated_as_command_success",
            "v1_repaired",
            "v1_hidden",
            "v1_claimed_passed",
        ):
            self.assertIs(statement[key], False, key)
        self.assertNoExecutionOrFollowOnFlags(result)

    def test_metadata_and_lineage_are_preserved_with_short_resolver_name(self) -> None:
        result = _resolve(_valid_request())
        metadata = result[
            "portable_source_body_verification_post_invocation_command_execution_boundary_metadata"
        ]
        for key in (
            "portable_source_body_verification_post_invocation_command_execution_boundary_result_id",
            "portable_source_body_verification_post_invocation_command_execution_boundary_result_type",
            "portable_source_body_verification_post_invocation_command_execution_boundary_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key])
        self.assertEqual(
            metadata[
                "portable_source_body_verification_post_invocation_command_execution_boundary_result_version"
            ],
            "0.1.0",
        )
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_portable_source_body_verification_post_invocation_command_execution_boundary",
        )
        self.assertTrue(metadata["naming_containment"]["short_resolver_filename_used_intentionally"])
        self.assertTrue(metadata["naming_containment"]["full_upstream_lineage_preserved_in_selected_basis"])
        self.assertTrue(metadata["lineage_posture"]["downstream_of_recorded_command_invocation"])
        self.assertTrue(metadata["lineage_posture"]["older_command_execution_boundary_surfaces_remain_lineage_only"])
        self.assertTrue(result["selected_command_invocation_basis"]["full_upstream_lineage_preserved"])
        self.assertTrue(
            result["selected_command_execution_boundary_lineage_basis"][
                "older_command_execution_boundary_surfaces_remain_lineage_only"
            ]
        )

    def test_selected_basis_lineage_behavior(self) -> None:
        result = _resolve(_valid_request())
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
        self.assertTrue(invocation["execution_permission_not_created"])
        self.assertTrue(invocation["execution_approval_not_created"])
        self.assertTrue(invocation["consumed_request_token_remains_closed"])
        self.assertTrue(invocation["reference_shaped_basis"])

        terminal_summary = result["selected_command_invocation_terminal_summary_basis"]
        self.assertTrue(terminal_summary["terminal_summary_declared"])
        self.assertTrue(terminal_summary["terminal_summary_remains_readability_basis_only"])
        self.assertTrue(terminal_summary["terminal_summary_does_not_create_command_execution"])
        self.assertTrue(terminal_summary["terminal_summary_does_not_create_output_result_success"])
        self.assertTrue(terminal_summary["terminal_summary_does_not_authorize_follow_on_work"])

        boundary = result["selected_command_invocation_boundary_basis"]
        self.assertEqual(boundary["outcome"], COMMAND_INVOCATION_BOUNDARY_OUTCOME)
        self.assertEqual(boundary["failed_check_count"], 0)
        self.assertTrue(boundary["boundary_basis_remains_boundary_basis_only"])
        self.assertTrue(boundary["boundary_did_not_execute_command"])
        self.assertTrue(boundary["boundary_did_not_create_output_result_success"])

        authorization = result["selected_command_invocation_authorization_basis"]
        self.assertEqual(authorization["outcome"], COMMAND_INVOCATION_AUTHORIZATION_OUTCOME)
        self.assertEqual(authorization["failed_check_count"], 0)
        self.assertTrue(authorization["authorization_token_is_one_shot"])
        self.assertTrue(authorization["authorization_basis_remains_authorization_basis_only"])

        review = result["selected_command_execution_review_basis"]
        self.assertEqual(review["outcome"], COMMAND_EXECUTION_REVIEW_OUTCOME)
        self.assertEqual(review["failed_check_count"], 0)
        self.assertTrue(review["command_execution_review_basis_remains_review_basis_only"])

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

        lineage = result["selected_command_execution_boundary_lineage_basis"]
        self.assertTrue(lineage["lineage_basis_declared"])
        self.assertTrue(lineage["basis_remains_prior_scaffolding_only"])
        self.assertTrue(lineage["older_command_execution_boundary_surfaces_remain_lineage_only"])
        self.assertTrue(lineage["lineage_basis_is_not_current_execution"])
        self.assertIs(lineage["command_execution_boundary_lineage_treated_as_current_execution"], False)

    def test_checks_are_explicit_and_pass_for_recorded(self) -> None:
        result = _resolve(_valid_request())
        checks = result["post_invocation_command_execution_boundary_checks"]
        self.assertGreater(len(checks), 45)
        for check in checks:
            for key in ("check_name", "passed", "expected_posture", "actual_posture", "block_code", "failure_code"):
                self.assertIn(key, check)
            self.assertIs(check["passed"], True, check["check_name"])
            self.assertIsNone(check["block_code"])
            self.assertIsNone(check["failure_code"])
        names = {check["check_name"] for check in checks}
        expected_names = {
            "post-invocation command execution boundary question declared",
            "post-invocation command execution boundary intent supported",
            "command invocation terminal summary basis declared",
            "command invocation live artifact basis declared",
            "command invocation live artifact recorded",
            "command invocation failed check count zero",
            "command invocation event recorded",
            "authorization token spent exactly once",
            "authorization token reuse blocked",
            "command invocation boundary basis declared",
            "command invocation authorization basis declared",
            "command execution review basis declared",
            "request consumption basis declared",
            "consumed request basis declared",
            "v2 admitted request basis declared",
            "v1 predecessor failure basis declared",
            "command execution boundary lineage basis not treated as current execution",
            "command report basis declared",
            "command implementation boundary basis declared",
            "command boundary basis declared",
            "artifact emission containment basis declared",
            "evidence-manifest basis declared",
            "portable verification basis declared",
            "post-invocation-execution-boundary-only posture declared",
            "one-future-command-execution-step posture declared",
            "invocation-basis-preserved posture declared",
            "authorization-token-spent-exactly-once posture declared",
            "authorization-token-reuse-blocked posture declared",
            "no-standing-execution-lane posture declared",
            "no-repeat-execution-permission posture declared",
            "post-invocation command execution boundary scope supported",
            "raw full prior artifact body not emitted",
            "collapse flags absent",
            "non-claims remain false",
        }
        self.assertTrue(expected_names.issubset(names))
        self.assertEqual(_failed_count(result), 0)

    def test_non_meaning_preserves_execution_boundary_limits(self) -> None:
        non_meaning = _resolve(_valid_request())["post_invocation_command_execution_boundary_non_meaning"]
        for suffix in (
            "command_executed",
            "command_output_exists",
            "command_result_exists",
            "command_success_exists",
            "execution_permission_exists",
            "execution_approval_exists",
            "authorization_token_reusable",
            "command_success_creates_currentness",
            "command_success_claims_final_completion",
            "command_output_becomes_source",
            "command_result_becomes_authority",
            "standing_execution_lane_exists",
            "repeat_execution_permission_exists",
            "standing_invocation_lane_exists",
            "repeat_invocation_permission_exists",
            "consumed_request_token_reopened",
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
            self.assertIs(
                non_meaning[
                    f"post_invocation_command_execution_boundary_does_not_mean_{suffix}"
                ],
                True,
            )

    def test_additional_basis_and_not_recorded_outcomes_are_bounded(self) -> None:
        additional_context = {"missing_basis": ["post-invocation execution boundary lineage unclear"]}
        additional = _resolve(
            _valid_request(
                requested_post_invocation_command_execution_boundary_outcome=REQUIRES_ADDITIONAL_BASIS,
                additional_basis_context=additional_context,
            )
        )
        self.assertEqual(additional["outcome"], REQUIRES_ADDITIONAL_BASIS)
        self.assertEqual(
            additional["additional_basis_required"]["additional_basis_context"],
            additional_context,
        )
        self.assertTrue(additional["additional_basis_required"]["missing_basis_not_scheduled"])
        self.assertTrue(additional["additional_basis_required"]["missing_basis_not_authorized"])
        self.assertTrue(additional["additional_basis_required"]["missing_basis_not_executed"])
        self.assertTrue(additional["additional_basis_required"]["additional_basis_does_not_execute_command"])
        self.assertNoExecutionOrFollowOnFlags(additional)

        not_recorded_basis = {"reason": "readable boundary basis failed bounded review"}
        not_recorded = _resolve(
            _valid_request(
                requested_post_invocation_command_execution_boundary_outcome=NOT_RECORDED,
                not_recorded_basis=not_recorded_basis,
            )
        )
        self.assertEqual(not_recorded["outcome"], NOT_RECORDED)
        self.assertEqual(not_recorded["not_recorded_basis"]["not_recorded_basis"], not_recorded_basis)
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded_does_not_repair"])
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded_does_not_authorize_next_work"])
        self.assertNoExecutionOrFollowOnFlags(not_recorded)

    def test_what_remains_open(self) -> None:
        remains_open = _resolve(_valid_request())["what_remains_open"]
        for item in OPEN_ITEMS:
            self.assertIn(item, remains_open["open_items"])
        self.assertTrue(remains_open["open_means_not_scheduled"])
        self.assertTrue(remains_open["open_means_not_authorized"])
        self.assertTrue(remains_open["open_means_not_executed"])

    def test_summary_helper(self) -> None:
        result = _resolve(_valid_request())
        summary = build_portable_source_body_verification_post_invocation_command_execution_boundary_summary(
            result
        )
        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(summary["request_id"], "post_invocation_command_execution_boundary_reference_review_001")
        self.assertEqual(summary["question"], QUESTION)
        self.assertEqual(summary["intent"], resolver.INTENT_RECORD)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)
        for key in (
            "post_invocation_boundary_recorded",
            "recorded_command_invocation_basis_preserved",
            "one_future_command_execution_step_declared",
            "authorization_token_spent_exactly_once_preserved",
            "authorization_token_reuse_blocked",
            "command_execution_still_not_performed",
            "command_output_result_success_still_not_created",
            "execution_permission_not_created",
            "execution_approval_not_created",
            "consumed_request_token_remains_closed",
            "v1_predecessor_failure_preserved",
            "returned_result_containment_preserved",
            "no_standing_repeat_execution_lane",
            "no_standing_repeat_invocation_lane",
            "older_command_execution_boundary_lineage_not_treated_as_current_execution",
            "no_raw_full_prior_artifact_body",
            "no_artifact_mutation",
            "no_deployment_runtime_public_release",
            "no_operation_public_readiness_final_completion",
            "no_continuation_publication_reusable_follow_on",
        ):
            self.assertIs(summary[key], True, key)
        self.assertIs(summary["not_recorded"], False)
        self.assertIs(summary["requires_additional_basis"], False)
        self.assertEqual(summary["selected_command_invocation_outcome"], COMMAND_INVOCATION_OUTCOME)
        self.assertEqual(summary["selected_command_execution_review_outcome"], COMMAND_EXECUTION_REVIEW_OUTCOME)
        self.assertEqual(summary["selected_request_consumption_outcome"], REQUEST_CONSUMPTION_OUTCOME)
        self.assertEqual(summary["selected_v2_admitted_request_outcome"], V2_ADMITTED_REQUEST_OUTCOME)
        self.assertEqual(summary["selected_v2_admitted_request_version"], V2_ADMITTED_REQUEST_VERSION)
        self.assertEqual(summary["key_non_claims"], _false_non_claims())

    def test_request_builder_helper(self) -> None:
        additional_context = {"basis": "post-invocation context"}
        not_recorded_basis = {"reason": "not recorded basis"}
        request = build_declared_portable_source_body_verification_post_invocation_command_execution_boundary_request(
            "builder_post_invocation_boundary_001",
            QUESTION,
            _command_invocation_basis(),
            _command_invocation_terminal_summary_basis(),
            _command_invocation_boundary_basis(),
            _command_invocation_authorization_basis(),
            _command_execution_review_basis(),
            _request_consumption_basis(),
            _consumed_request_basis(),
            _v2_admitted_request_basis(),
            _v1_predecessor_failure_basis(),
            _command_execution_boundary_lineage_basis(),
            _command_basis("command_report"),
            _command_basis("command_implementation_boundary"),
            _command_basis("command_boundary"),
            _command_basis("artifact_emission_containment"),
            _command_basis("evidence_manifest"),
            _command_basis("portable_verification"),
            _posture("post_invocation_execution_boundary_only"),
            _posture("one_future_command_execution_step"),
            _posture("invocation_basis_preserved"),
            _posture("authorization_token_spent_exactly_once"),
            _posture("authorization_token_reuse_blocked"),
            _posture("no_command_execution"),
            _posture("no_output_result_success"),
            _posture("no_execution_permission"),
            _posture("no_execution_approval"),
            _posture("no_standing_execution_lane"),
            _posture("no_repeat_execution_permission"),
            _posture("no_standing_invocation_lane"),
            _posture("no_repeat_invocation_permission"),
            _posture("consumed_token_closed"),
            _posture("no_reopen_consumed_request"),
            _posture("returned_result_containment"),
            list(SUPPORTED_SCOPE),
            selected_command_invocation_result_path="artifact://command_invocation",
            selected_command_invocation_result_id="command_invocation_reference_review_001",
            selected_command_invocation_result_outcome=COMMAND_INVOCATION_OUTCOME,
            selected_command_invocation_failed_check_count=0,
            selected_command_invocation_event_recorded=True,
            selected_command_invocation_authorization_token_spent_exactly_once=True,
            selected_command_invocation_authorization_token_reuse_blocked=True,
            selected_command_execution_review_result_path="artifact://command_execution_review",
            selected_command_execution_review_result_id="command_execution_review_reference_review_001",
            selected_command_execution_review_result_outcome=COMMAND_EXECUTION_REVIEW_OUTCOME,
            selected_command_execution_review_failed_check_count=0,
            selected_request_consumption_result_path="artifact://request_consumption",
            selected_request_consumption_result_id="request_consumption_reference_review_001",
            selected_request_consumption_result_outcome=REQUEST_CONSUMPTION_OUTCOME,
            selected_request_consumption_failed_check_count=0,
            selected_v2_admitted_request_artifact_path="artifact://v2",
            selected_v2_admitted_request_artifact_id="v2_reference_review_001",
            selected_v2_admitted_request_outcome=V2_ADMITTED_REQUEST_OUTCOME,
            selected_v2_admitted_request_version=V2_ADMITTED_REQUEST_VERSION,
            selected_v2_failed_check_count=0,
            requested_post_invocation_command_execution_boundary_outcome=RECORDED,
            additional_basis_context=additional_context,
            not_recorded_basis=not_recorded_basis,
        )
        self.assertEqual(request["post_invocation_command_execution_boundary_request_id"], "builder_post_invocation_boundary_001")
        self.assertEqual(request["post_invocation_command_execution_boundary_question"], QUESTION)
        for key in (
            "selected_command_invocation_basis",
            "selected_command_invocation_terminal_summary_basis",
            "selected_command_invocation_boundary_basis",
            "selected_command_invocation_authorization_basis",
            "selected_command_execution_review_basis",
            "selected_request_consumption_basis",
            "selected_consumed_request_basis",
            "selected_v2_admitted_request_basis",
            "selected_v1_predecessor_failure_basis",
            "selected_command_execution_boundary_lineage_basis",
            "selected_command_report_basis",
            "selected_command_implementation_boundary_basis",
            "selected_command_boundary_basis",
            "selected_artifact_emission_containment_basis",
            "selected_evidence_manifest_basis",
            "selected_portable_verification_basis",
            "post_invocation_execution_boundary_only_posture",
            "one_future_command_execution_step_posture",
            "invocation_basis_preserved_posture",
            "authorization_token_spent_exactly_once_posture",
            "authorization_token_reuse_blocked_posture",
            "no_command_execution_posture",
            "no_output_result_success_posture",
            "no_execution_permission_posture",
            "no_execution_approval_posture",
            "no_standing_execution_lane_posture",
            "no_repeat_execution_permission_posture",
            "no_standing_invocation_lane_posture",
            "no_repeat_invocation_permission_posture",
            "consumed_token_closed_posture",
            "no_reopen_consumed_request_posture",
            "returned_result_containment_posture",
        ):
            self.assertIn(key, request)
        self.assertEqual(request["post_invocation_command_execution_boundary_scope"], list(SUPPORTED_SCOPE))
        self.assertEqual(request["selected_command_invocation_result_path"], "artifact://command_invocation")
        self.assertEqual(request["selected_command_invocation_result_id"], "command_invocation_reference_review_001")
        self.assertEqual(request["selected_command_invocation_result_outcome"], COMMAND_INVOCATION_OUTCOME)
        self.assertEqual(request["selected_command_invocation_failed_check_count"], 0)
        self.assertIs(request["selected_command_invocation_event_recorded"], True)
        self.assertIs(request["selected_command_invocation_authorization_token_spent_exactly_once"], True)
        self.assertIs(request["selected_command_invocation_authorization_token_reuse_blocked"], True)
        self.assertEqual(request["selected_command_execution_review_result_outcome"], COMMAND_EXECUTION_REVIEW_OUTCOME)
        self.assertEqual(request["selected_request_consumption_result_outcome"], REQUEST_CONSUMPTION_OUTCOME)
        self.assertEqual(request["selected_v2_admitted_request_outcome"], V2_ADMITTED_REQUEST_OUTCOME)
        self.assertEqual(request["selected_v2_admitted_request_version"], V2_ADMITTED_REQUEST_VERSION)
        self.assertEqual(request["additional_basis_context"], additional_context)
        self.assertEqual(request["not_recorded_basis"], not_recorded_basis)
        self.assertEqual(request["declared_non_claims"], _false_non_claims())
        result = _resolve(request)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertNoExecutionOrFollowOnFlags(result)

    def test_path_based_request_and_write_behavior(self) -> None:
        request = _valid_request()
        mapping_result = _resolve(request)
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            request_path = temp / "request.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")
            path_result = resolve_portable_source_body_verification_post_invocation_command_execution_boundary_from_path(
                request_path
            )
            self.assertEqual(path_result["outcome"], RECORDED)
            self.assertEqual(set(path_result), set(mapping_result))
            self.assertEqual(
                path_result[
                    "portable_source_body_verification_post_invocation_command_execution_boundary_metadata"
                ]["declared_post_invocation_command_execution_boundary_request_path"],
                str(request_path),
            )

            malformed_path = temp / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            self.assertBlocked(
                resolve_portable_source_body_verification_post_invocation_command_execution_boundary_from_path(
                    malformed_path
                ),
                "DECLARED_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_REQUEST_MALFORMED",
            )
            array_path = temp / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            self.assertBlocked(
                resolve_portable_source_body_verification_post_invocation_command_execution_boundary_from_path(
                    array_path
                ),
                "DECLARED_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_REQUEST_MALFORMED",
            )
            self.assertBlocked(
                resolve_portable_source_body_verification_post_invocation_command_execution_boundary_from_path(
                    temp / "missing.json"
                ),
                "DECLARED_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_REQUEST_UNREADABLE",
            )

            explicit_output = temp / "nested" / "result.json"
            written = write_portable_source_body_verification_post_invocation_command_execution_boundary_result(
                mapping_result, explicit_output
            )
            self.assertEqual(written, explicit_output)
            parsed = json.loads(written.read_text(encoding="utf-8"))
            for section in TOP_LEVEL_SECTIONS:
                self.assertIn(section, parsed)

            default_root = temp / "post_invocation_root"
            with patch.object(
                resolver,
                "PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_ROOT",
                default_root,
            ):
                first = write_portable_source_body_verification_post_invocation_command_execution_boundary_result(
                    mapping_result
                )
                second = write_portable_source_body_verification_post_invocation_command_execution_boundary_result(
                    mapping_result
                )
            self.assertEqual(first.parent, default_root)
            self.assertEqual(second.parent, default_root)
            self.assertNotEqual(first, second)
            self.assertTrue(second.stem.endswith("_001"))
            self.assertNotIn("command_invocation_boundary", str(first.parent))
            self.assertNotIn("command_invocation_authorization", str(first.parent))
            self.assertNotIn("command_execution_review", str(first.parent))

    def test_reference_shaped_containment_blocks_full_body_without_returning_value(self) -> None:
        request = _valid_request(
            selected_command_invocation_basis=_command_invocation_basis(
                full_artifact_body=RAW_FULL_BODY_SENTINEL
            )
        )
        result = _resolve(request)
        self.assertBlocked(result, "FULL_PRIOR_ARTIFACT_BODY_EMITTED")
        text = _json_text(result)
        self.assertNotIn(RAW_FULL_BODY_SENTINEL, text)
        self.assertIn(resolver.FULL_BODY_OMISSION_MARKER, text)
        self.assertNoExecutionOrFollowOnFlags(result)

        request = _valid_request(
            selected_request_consumption_basis=_request_consumption_basis(
                full_artifact_body=RAW_FULL_BODY_SENTINEL
            )
        )
        result = _resolve(request)
        self.assertBlocked(result, "FULL_PRIOR_ARTIFACT_BODY_EMITTED")
        text = _json_text(result)
        self.assertNotIn(RAW_FULL_BODY_SENTINEL, text)
        self.assertIn(resolver.FULL_BODY_OMISSION_MARKER, text)
        self.assertNoExecutionOrFollowOnFlags(result)

    def test_resolver_does_not_mutate_inputs(self) -> None:
        request = _valid_request()
        before = copy.deepcopy(request)
        first = _resolve(request)
        second = _resolve(request)
        self.assertEqual(request, before)
        self.assertEqual(first["outcome"], RECORDED)
        self.assertEqual(second["outcome"], RECORDED)
        for key in (
            "selected_command_invocation_basis",
            "selected_command_invocation_terminal_summary_basis",
            "selected_command_invocation_boundary_basis",
            "selected_command_invocation_authorization_basis",
            "selected_command_execution_review_basis",
            "selected_request_consumption_basis",
            "selected_consumed_request_basis",
            "selected_v2_admitted_request_basis",
            "selected_v1_predecessor_failure_basis",
            "selected_command_execution_boundary_lineage_basis",
            "selected_command_report_basis",
            "selected_command_implementation_boundary_basis",
            "selected_command_boundary_basis",
            "selected_artifact_emission_containment_basis",
            "selected_evidence_manifest_basis",
            "selected_portable_verification_basis",
            "post_invocation_execution_boundary_only_posture",
            "one_future_command_execution_step_posture",
            "invocation_basis_preserved_posture",
            "authorization_token_spent_exactly_once_posture",
            "authorization_token_reuse_blocked_posture",
            "no_command_execution_posture",
            "no_output_result_success_posture",
            "no_execution_permission_posture",
            "no_execution_approval_posture",
            "no_standing_execution_lane_posture",
            "no_repeat_execution_permission_posture",
            "no_standing_invocation_lane_posture",
            "no_repeat_invocation_permission_posture",
            "consumed_token_closed_posture",
            "no_reopen_consumed_request_posture",
            "returned_result_containment_posture",
            "post_invocation_command_execution_boundary_scope",
        ):
            self.assertEqual(request[key], before[key], key)
        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "additive_result.json"
            written = write_portable_source_body_verification_post_invocation_command_execution_boundary_result(
                first, output_path
            )
            self.assertEqual(written, output_path)
            self.assertTrue(written.exists())

    def test_missing_and_malformed_inputs_block(self) -> None:
        explicit_block = _resolve(
            _valid_request(
                post_invocation_command_execution_boundary_intent=resolver.INTENT_BLOCK,
                block_reason="caller requested block",
            )
        )
        self.assertBlocked(explicit_block, "POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_BLOCKED_BY_REQUEST")
        self.assertBlocked(
            resolve_portable_source_body_verification_post_invocation_command_execution_boundary(),
            "POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_QUESTION_UNDECLARED",
        )
        self.assertBlocked(
            resolve_portable_source_body_verification_post_invocation_command_execution_boundary(
                declared_post_invocation_command_execution_boundary_request=["not", "mapping"]
            ),
            "DECLARED_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_REQUEST_MALFORMED",
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            malformed = temp / "malformed.json"
            malformed.write_text("{bad", encoding="utf-8")
            self.assertBlocked(
                resolve_portable_source_body_verification_post_invocation_command_execution_boundary_from_path(
                    malformed
                ),
                "DECLARED_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_REQUEST_MALFORMED",
            )
            self.assertBlocked(
                resolve_portable_source_body_verification_post_invocation_command_execution_boundary_from_path(
                    temp / "missing.json"
                ),
                "DECLARED_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_REQUEST_UNREADABLE",
            )

    def test_basis_specific_blocking(self) -> None:
        cases = (
            ("selected_command_invocation_basis", None, "COMMAND_INVOCATION_BASIS_MISSING"),
            (
                "selected_command_invocation_basis",
                _command_invocation_basis(outcome="WRONG"),
                "COMMAND_INVOCATION_NOT_RECORDED",
            ),
            (
                "selected_command_invocation_basis",
                _command_invocation_basis(failed_check_count=1),
                "COMMAND_INVOCATION_FAILED_CHECKS_PRESENT",
            ),
            (
                "selected_command_invocation_basis",
                _command_invocation_basis(
                    command_invocation_recorded=False,
                    bounded_command_invocation_event_recorded=False,
                    command_invocation_event_recorded=False,
                ),
                "COMMAND_INVOCATION_EVENT_NOT_RECORDED",
            ),
            (
                "selected_command_invocation_basis",
                _command_invocation_basis(authorization_token_spent_exactly_once=False, one_shot_authorization_token_spent_exactly_once=False),
                "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_NOT_SPENT_EXACTLY_ONCE",
            ),
            (
                "selected_command_invocation_basis",
                _command_invocation_basis(authorization_token_reuse_blocked=False, authorization_token_not_reused=False),
                "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_REUSE_NOT_BLOCKED",
            ),
            ("selected_command_invocation_boundary_basis", None, "COMMAND_INVOCATION_BOUNDARY_BASIS_MISSING"),
            (
                "selected_command_invocation_boundary_basis",
                _command_invocation_boundary_basis(outcome="WRONG"),
                "COMMAND_INVOCATION_BOUNDARY_NOT_RECORDED",
            ),
            (
                "selected_command_invocation_boundary_basis",
                _command_invocation_boundary_basis(failed_check_count=1),
                "COMMAND_INVOCATION_BOUNDARY_FAILED_CHECKS_PRESENT",
            ),
            ("selected_command_invocation_authorization_basis", None, "COMMAND_INVOCATION_AUTHORIZATION_BASIS_MISSING"),
            (
                "selected_command_invocation_authorization_basis",
                _command_invocation_authorization_basis(outcome="WRONG"),
                "COMMAND_INVOCATION_AUTHORIZATION_NOT_RECORDED",
            ),
            (
                "selected_command_invocation_authorization_basis",
                _command_invocation_authorization_basis(failed_check_count=1),
                "COMMAND_INVOCATION_AUTHORIZATION_FAILED_CHECKS_PRESENT",
            ),
            ("selected_command_execution_review_basis", None, "COMMAND_EXECUTION_REVIEW_BASIS_MISSING"),
            (
                "selected_command_execution_review_basis",
                _command_execution_review_basis(outcome="WRONG"),
                "COMMAND_EXECUTION_REVIEW_NOT_RECORDED",
            ),
            (
                "selected_command_execution_review_basis",
                _command_execution_review_basis(failed_check_count=1),
                "COMMAND_EXECUTION_REVIEW_FAILED_CHECKS_PRESENT",
            ),
            ("selected_request_consumption_basis", None, "REQUEST_CONSUMPTION_BASIS_MISSING"),
            (
                "selected_request_consumption_basis",
                _request_consumption_basis(outcome="WRONG"),
                "REQUEST_CONSUMPTION_NOT_CONSUMED",
            ),
            (
                "selected_request_consumption_basis",
                _request_consumption_basis(failed_check_count=1),
                "REQUEST_CONSUMPTION_FAILED_CHECKS_PRESENT",
            ),
            ("selected_consumed_request_basis", None, "CONSUMED_REQUEST_BASIS_MISSING"),
            (
                "selected_consumed_request_basis",
                _consumed_request_basis(consumed_request_token_remains_closed=False, consumed_request_token_closed=False, consumed_token_closed=False, token_closed=False),
                "CONSUMED_TOKEN_NOT_CLOSED",
            ),
            (
                "selected_consumed_request_basis",
                _consumed_request_basis(consumed_request_reopened=True),
                "CONSUMED_REQUEST_REOPENED",
            ),
            ("selected_v2_admitted_request_basis", None, "V2_ADMITTED_REQUEST_BASIS_MISSING"),
            (
                "selected_v2_admitted_request_basis",
                _v2_admitted_request_basis(outcome="WRONG"),
                "V2_ADMITTED_REQUEST_NOT_ADMITTED",
            ),
            (
                "selected_v2_admitted_request_basis",
                _v2_admitted_request_basis(result_version="0.1.0"),
                "V2_ADMITTED_REQUEST_VERSION_NOT_0_2_0",
            ),
            (
                "selected_v2_admitted_request_basis",
                _v2_admitted_request_basis(failed_check_count=1),
                "V2_ADMITTED_REQUEST_FAILED_CHECKS_PRESENT",
            ),
            (
                "selected_v2_admitted_request_basis",
                _v2_admitted_request_basis(successor_of=None, successor_reason=None, resolver_module=None, successor_metadata_preserved=False),
                "V2_SUCCESSOR_METADATA_MISSING",
            ),
            (
                "selected_v2_admitted_request_basis",
                _v2_admitted_request_basis(returned_result_containment_preserved=False),
                "V2_RETURNED_RESULT_CONTAINMENT_MISSING",
            ),
            ("selected_v1_predecessor_failure_basis", None, "V1_PREDECESSOR_FAILURE_BASIS_MISSING"),
            (
                "selected_v1_predecessor_failure_basis",
                _v1_predecessor_failure_basis(v2_treated_as_repairing_v1=True),
                "V2_TREATED_AS_REPAIRING_V1",
            ),
            (
                "selected_v1_predecessor_failure_basis",
                _v1_predecessor_failure_basis(v1_hidden=True),
                "V1_FAILURE_HIDDEN",
            ),
            (
                "selected_v1_predecessor_failure_basis",
                _v1_predecessor_failure_basis(v1_claimed_passed=True),
                "V1_CLAIMED_PASSED",
            ),
            (
                "selected_command_execution_boundary_lineage_basis",
                _command_execution_boundary_lineage_basis(lineage_basis_treated_as_current_execution=True),
                "COMMAND_EXECUTION_BOUNDARY_LINEAGE_BASIS_TREATED_AS_CURRENT_EXECUTION",
            ),
            ("selected_command_report_basis", None, "COMMAND_REPORT_BASIS_MISSING"),
            ("selected_command_implementation_boundary_basis", None, "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING"),
            ("selected_command_boundary_basis", None, "COMMAND_BOUNDARY_BASIS_MISSING"),
            ("selected_artifact_emission_containment_basis", None, "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING"),
            ("selected_evidence_manifest_basis", None, "EVIDENCE_MANIFEST_BASIS_MISSING"),
            ("selected_portable_verification_basis", None, "PORTABLE_VERIFICATION_BASIS_MISSING"),
            ("post_invocation_execution_boundary_only_posture", None, "POST_INVOCATION_EXECUTION_BOUNDARY_ONLY_POSTURE_MISSING"),
            ("one_future_command_execution_step_posture", None, "ONE_FUTURE_COMMAND_EXECUTION_STEP_POSTURE_MISSING"),
            ("invocation_basis_preserved_posture", None, "INVOCATION_BASIS_PRESERVED_POSTURE_MISSING"),
            ("authorization_token_spent_exactly_once_posture", None, "AUTHORIZATION_TOKEN_SPENT_EXACTLY_ONCE_POSTURE_MISSING"),
            ("authorization_token_reuse_blocked_posture", None, "AUTHORIZATION_TOKEN_REUSE_BLOCKED_POSTURE_MISSING"),
            ("no_standing_execution_lane_posture", None, "NO_STANDING_EXECUTION_LANE_POSTURE_MISSING"),
            ("no_repeat_execution_permission_posture", None, "NO_REPEAT_EXECUTION_PERMISSION_POSTURE_MISSING"),
            (
                "post_invocation_command_execution_boundary_scope",
                ["POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_ONLY", "UNSUPPORTED_SCOPE"],
                "UNSUPPORTED_POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_SCOPE",
            ),
        )
        for key, value, block_code in cases:
            with self.subTest(key=key, block_code=block_code):
                request = _valid_request()
                if value is None:
                    request.pop(key)
                else:
                    request[key] = value
                self.assertBlocked(_resolve(request), block_code)

    def test_collapse_flags_block_execution_and_follow_on_overreach(self) -> None:
        cases = (
            ("command_execution_performed", "COMMAND_EXECUTION_PERFORMED"),
            ("command_output_created", "COMMAND_OUTPUT_CREATED"),
            ("command_result_created", "COMMAND_RESULT_CREATED"),
            ("command_success_created", "COMMAND_SUCCESS_CREATED"),
            ("execution_permission_created", "EXECUTION_PERMISSION_CREATED"),
            ("execution_approval_created", "EXECUTION_APPROVAL_CREATED"),
            ("standing_execution_lane_created", "STANDING_EXECUTION_LANE_CREATED"),
            ("repeat_execution_permission_created", "REPEAT_EXECUTION_PERMISSION_CREATED"),
            ("standing_invocation_lane_created", "STANDING_INVOCATION_LANE_CREATED"),
            ("repeat_invocation_permission_created", "REPEAT_INVOCATION_PERMISSION_CREATED"),
            ("authorization_token_reused", "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_REUSE_NOT_BLOCKED"),
            ("consumed_request_reopened", "CONSUMED_REQUEST_REOPENED"),
            ("execution_boundary_treated_as_execution", "EXECUTION_BOUNDARY_TREATED_AS_EXECUTION"),
            ("execution_boundary_treated_as_command_output", "EXECUTION_BOUNDARY_TREATED_AS_COMMAND_OUTPUT"),
            ("execution_boundary_treated_as_command_result", "EXECUTION_BOUNDARY_TREATED_AS_COMMAND_RESULT"),
            ("execution_boundary_treated_as_command_success", "EXECUTION_BOUNDARY_TREATED_AS_COMMAND_SUCCESS"),
            ("invocation_basis_treated_as_execution", "INVOCATION_BASIS_TREATED_AS_EXECUTION"),
            ("invocation_basis_treated_as_command_success", "INVOCATION_BASIS_TREATED_AS_COMMAND_SUCCESS"),
            ("command_output_became_source", "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
            ("command_result_became_authority", "COMMAND_RESULT_TREATED_AS_AUTHORITY"),
            ("command_success_created_currentness", "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
            ("command_success_claimed_final_completion", "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
            ("prior_artifacts_mutated", "ARTIFACTS_MUTATED"),
            ("deployment_created", "DEPLOYMENT_CREATED"),
            ("runtime_hosting_created", "RUNTIME_HOSTING_CREATED"),
            ("public_release_created", "PUBLIC_RELEASE_CREATED"),
            ("operation_permission_created", "OPERATION_PERMISSION_CREATED"),
            ("public_launch_readiness_created", "PUBLIC_READINESS_CREATED"),
            ("final_completion_claimed", "FINAL_COMPLETION_CLAIMED"),
            ("continuation_authorized", "CONTINUATION_AUTHORIZED"),
            ("reusable_permission_created", "REUSABLE_PERMISSION_CREATED"),
            ("derivative_reception_authorized", "DERIVATIVE_RECEPTION_AUTHORIZED"),
            ("vessel_relation_authorized", "VESSEL_RELATION_AUTHORIZED"),
            ("another_reception_request_authorized", "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"),
            ("follow_on_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
        )
        for field, block_code in cases:
            with self.subTest(field=field):
                request = _valid_request()
                request["declared_non_claims"][field] = True
                self.assertBlocked(_resolve(request), block_code)

        lineage_request = _valid_request(
            selected_command_execution_boundary_lineage_basis=_command_execution_boundary_lineage_basis(
                command_execution_boundary_lineage_treated_as_current_execution=True
            )
        )
        self.assertBlocked(
            _resolve(lineage_request),
            "COMMAND_EXECUTION_BOUNDARY_LINEAGE_BASIS_TREATED_AS_CURRENT_EXECUTION",
        )

    def test_mutation_replay_merge_and_non_claim_failures_block(self) -> None:
        request = _valid_request()
        request["mutation_performed"] = True
        request["replay_performed"] = True
        request["merge_performed"] = True
        self.assertBlocked(_resolve(request), "MUTATION_REPLAY_OR_MERGE_DETECTED")

        missing_non_claim = _valid_request()
        missing_non_claim["declared_non_claims"].pop("command_executed")
        self.assertBlocked(missing_non_claim_result := _resolve(missing_non_claim), "NON_CLAIM_MISSING_OR_FLIPPED")
        self.assertEqual(missing_non_claim_result["outcome"], BLOCKED)

        flipped_non_claim = _valid_request()
        flipped_non_claim["declared_non_claims"]["command_executed"] = True
        self.assertBlocked(flipped_non_claim_result := _resolve(flipped_non_claim), "COMMAND_EXECUTION_PERFORMED")
        self.assertEqual(flipped_non_claim_result["outcome"], BLOCKED)


if __name__ == "__main__":
    unittest.main()
